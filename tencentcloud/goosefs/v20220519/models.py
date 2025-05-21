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


class AddCrossVpcSubnetSupportForClientNodeRequest(AbstractModel):
    """AddCrossVpcSubnetSupportForClientNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _SubnetInfo: 子网信息
        :type SubnetInfo: :class:`tencentcloud.goosefs.v20220519.models.SubnetInfo`
        """
        self._FileSystemId = None
        self._SubnetInfo = None

    @property
    def FileSystemId(self):
        """文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SubnetInfo(self):
        """子网信息
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.SubnetInfo`
        """
        return self._SubnetInfo

    @SubnetInfo.setter
    def SubnetInfo(self, SubnetInfo):
        self._SubnetInfo = SubnetInfo


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("SubnetInfo") is not None:
            self._SubnetInfo = SubnetInfo()
            self._SubnetInfo._deserialize(params.get("SubnetInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCrossVpcSubnetSupportForClientNodeResponse(AbstractModel):
    """AddCrossVpcSubnetSupportForClientNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AttachFileSystemBucketRequest(AbstractModel):
    """AttachFileSystemBucket请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 无
        :type FileSystemId: str
        :param _Bucket: 关联新Bucket
        :type Bucket: :class:`tencentcloud.goosefs.v20220519.models.MappedBucket`
        """
        self._FileSystemId = None
        self._Bucket = None

    @property
    def FileSystemId(self):
        """无
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Bucket(self):
        """关联新Bucket
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.MappedBucket`
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("Bucket") is not None:
            self._Bucket = MappedBucket()
            self._Bucket._deserialize(params.get("Bucket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachFileSystemBucketResponse(AbstractModel):
    """AttachFileSystemBucket返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchAddClientNodesRequest(AbstractModel):
    """BatchAddClientNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _ClientNodes: 添加客户端节点列表
        :type ClientNodes: list of LinuxNodeAttribute
        :param _SingleClusterFlag: 是否单集群默认是false	
        :type SingleClusterFlag: bool
        """
        self._FileSystemId = None
        self._ClientNodes = None
        self._SingleClusterFlag = None

    @property
    def FileSystemId(self):
        """文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def ClientNodes(self):
        """添加客户端节点列表
        :rtype: list of LinuxNodeAttribute
        """
        return self._ClientNodes

    @ClientNodes.setter
    def ClientNodes(self, ClientNodes):
        self._ClientNodes = ClientNodes

    @property
    def SingleClusterFlag(self):
        """是否单集群默认是false	
        :rtype: bool
        """
        return self._SingleClusterFlag

    @SingleClusterFlag.setter
    def SingleClusterFlag(self, SingleClusterFlag):
        self._SingleClusterFlag = SingleClusterFlag


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("ClientNodes") is not None:
            self._ClientNodes = []
            for item in params.get("ClientNodes"):
                obj = LinuxNodeAttribute()
                obj._deserialize(item)
                self._ClientNodes.append(obj)
        self._SingleClusterFlag = params.get("SingleClusterFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAddClientNodesResponse(AbstractModel):
    """BatchAddClientNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchDeleteClientNodesRequest(AbstractModel):
    """BatchDeleteClientNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _ClientNodes: 删除的客户端节点列表
        :type ClientNodes: list of LinuxNodeAttribute
        :param _SingleClusterFlag: 是否单集群，默认是false
        :type SingleClusterFlag: bool
        """
        self._FileSystemId = None
        self._ClientNodes = None
        self._SingleClusterFlag = None

    @property
    def FileSystemId(self):
        """文件系统id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def ClientNodes(self):
        """删除的客户端节点列表
        :rtype: list of LinuxNodeAttribute
        """
        return self._ClientNodes

    @ClientNodes.setter
    def ClientNodes(self, ClientNodes):
        self._ClientNodes = ClientNodes

    @property
    def SingleClusterFlag(self):
        """是否单集群，默认是false
        :rtype: bool
        """
        return self._SingleClusterFlag

    @SingleClusterFlag.setter
    def SingleClusterFlag(self, SingleClusterFlag):
        self._SingleClusterFlag = SingleClusterFlag


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("ClientNodes") is not None:
            self._ClientNodes = []
            for item in params.get("ClientNodes"):
                obj = LinuxNodeAttribute()
                obj._deserialize(item)
                self._ClientNodes.append(obj)
        self._SingleClusterFlag = params.get("SingleClusterFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteClientNodesResponse(AbstractModel):
    """BatchDeleteClientNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChargeAttribute(AbstractModel):
    """付费信息详情

    """

    def __init__(self):
        r"""
        :param _CurDeadline: 到期时间
        :type CurDeadline: str
        :param _PayMode: 付费方式
        :type PayMode: str
        :param _AutoRenewFlag: 自动付费标识：0:默认未设置 1:自动续费 2 不自动续费
        :type AutoRenewFlag: int
        :param _ResourceId: 资源ID
        :type ResourceId: str
        """
        self._CurDeadline = None
        self._PayMode = None
        self._AutoRenewFlag = None
        self._ResourceId = None

    @property
    def CurDeadline(self):
        """到期时间
        :rtype: str
        """
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline

    @property
    def PayMode(self):
        """付费方式
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def AutoRenewFlag(self):
        """自动付费标识：0:默认未设置 1:自动续费 2 不自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._CurDeadline = params.get("CurDeadline")
        self._PayMode = params.get("PayMode")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientClusterManagerNodeInfo(AbstractModel):
    """客户侧集群管理节点信息

    """

    def __init__(self):
        r"""
        :param _NodeIp: 客户端节点IP
        :type NodeIp: str
        :param _NodeInstanceId: 节点Instance Id
        :type NodeInstanceId: str
        :param _InitialPassword: 初始密码
        :type InitialPassword: str
        """
        self._NodeIp = None
        self._NodeInstanceId = None
        self._InitialPassword = None

    @property
    def NodeIp(self):
        """客户端节点IP
        :rtype: str
        """
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

    @property
    def NodeInstanceId(self):
        """节点Instance Id
        :rtype: str
        """
        return self._NodeInstanceId

    @NodeInstanceId.setter
    def NodeInstanceId(self, NodeInstanceId):
        self._NodeInstanceId = NodeInstanceId

    @property
    def InitialPassword(self):
        """初始密码
        :rtype: str
        """
        return self._InitialPassword

    @InitialPassword.setter
    def InitialPassword(self, InitialPassword):
        self._InitialPassword = InitialPassword


    def _deserialize(self, params):
        self._NodeIp = params.get("NodeIp")
        self._NodeInstanceId = params.get("NodeInstanceId")
        self._InitialPassword = params.get("InitialPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientNodeAttribute(AbstractModel):
    """客户端节点属性

    """

    def __init__(self):
        r"""
        :param _ClientNodeIp: 客户端节点IP
        :type ClientNodeIp: str
        :param _Status: 客户端节点服务状态, Active(运行中), Adding(添加中), Destroying(销毁中), Down(已停止)
        :type Status: str
        :param _ClientType: 客户端节点类型，extend(扩展节点)，manager(管理节点)
        :type ClientType: str
        :param _VpcId: 节点所属vpcid	
        :type VpcId: str
        :param _SubnetId: 节点所属子网id
        :type SubnetId: str
        :param _InstanceId: cvmId
        :type InstanceId: str
        :param _MountPoint: 自定义挂载点
        :type MountPoint: str
        """
        self._ClientNodeIp = None
        self._Status = None
        self._ClientType = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceId = None
        self._MountPoint = None

    @property
    def ClientNodeIp(self):
        """客户端节点IP
        :rtype: str
        """
        return self._ClientNodeIp

    @ClientNodeIp.setter
    def ClientNodeIp(self, ClientNodeIp):
        self._ClientNodeIp = ClientNodeIp

    @property
    def Status(self):
        """客户端节点服务状态, Active(运行中), Adding(添加中), Destroying(销毁中), Down(已停止)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClientType(self):
        """客户端节点类型，extend(扩展节点)，manager(管理节点)
        :rtype: str
        """
        return self._ClientType

    @ClientType.setter
    def ClientType(self, ClientType):
        self._ClientType = ClientType

    @property
    def VpcId(self):
        """节点所属vpcid	
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """节点所属子网id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceId(self):
        """cvmId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MountPoint(self):
        """自定义挂载点
        :rtype: str
        """
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint


    def _deserialize(self, params):
        self._ClientNodeIp = params.get("ClientNodeIp")
        self._Status = params.get("Status")
        self._ClientType = params.get("ClientType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceId = params.get("InstanceId")
        self._MountPoint = params.get("MountPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """节点 IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

    @property
    def LocalDirectory(self):
        """挂载点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LocalDirectory

    @LocalDirectory.setter
    def LocalDirectory(self, LocalDirectory):
        self._LocalDirectory = LocalDirectory

    @property
    def GooseFSDirectory(self):
        """可以访问的 GooseFS 目录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GooseFSDirectory

    @GooseFSDirectory.setter
    def GooseFSDirectory(self, GooseFSDirectory):
        self._GooseFSDirectory = GooseFSDirectory

    @property
    def Token(self):
        """token
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        """角色名
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DirectoryList(self):
        """目录列表
        :rtype: list of str
        """
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
        """数据流通任务类型, FS_TO_COS(文件系统到COS Bucket),或者COS_TO_FS(COS Bucket到文件系统)
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Bucket(self):
        """COS存储桶名
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def FileSystemId(self):
        """文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TaskPath(self):
        """对于FS_TO_COS, TaskPath是Bucket映射目录的相对路径, 对于COS_TO_FS是COS上的路径。如果置为空, 则表示全部数据
        :rtype: str
        """
        return self._TaskPath

    @TaskPath.setter
    def TaskPath(self, TaskPath):
        self._TaskPath = TaskPath

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def RepositoryType(self):
        """数据流通方式 MSP_AFM 手动加载  RAW_AFM 按需加载
        :rtype: str
        """
        return self._RepositoryType

    @RepositoryType.setter
    def RepositoryType(self, RepositoryType):
        self._RepositoryType = RepositoryType

    @property
    def TextLocation(self):
        """文件列表下载地址，以http开头
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateFileSystemRequest(AbstractModel):
    """CreateFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 文件系统类型, 可填goosefs和goosefsx
        :type Type: str
        :param _Name: 文件系统名
        :type Name: str
        :param _Description: 文件系统备注描述
        :type Description: str
        :param _VpcId: vpc网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Zone: 子网所在的可用区
        :type Zone: str
        :param _Tag: 文件系统关联的tag
        :type Tag: list of Tag
        :param _GooseFSxBuildElements: GooseFSx构建时要传递的参数
        :type GooseFSxBuildElements: :class:`tencentcloud.goosefs.v20220519.models.GooseFSxBuildElement`
        :param _SecurityGroupId: 客户端集群所属的安全组
        :type SecurityGroupId: str
        :param _ClusterPort: 集群ssh通信端口，默认是22
        :type ClusterPort: int
        """
        self._Type = None
        self._Name = None
        self._Description = None
        self._VpcId = None
        self._SubnetId = None
        self._Zone = None
        self._Tag = None
        self._GooseFSxBuildElements = None
        self._SecurityGroupId = None
        self._ClusterPort = None

    @property
    def Type(self):
        """文件系统类型, 可填goosefs和goosefsx
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """文件系统名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """文件系统备注描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VpcId(self):
        """vpc网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Zone(self):
        """子网所在的可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Tag(self):
        """文件系统关联的tag
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def GooseFSxBuildElements(self):
        """GooseFSx构建时要传递的参数
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.GooseFSxBuildElement`
        """
        return self._GooseFSxBuildElements

    @GooseFSxBuildElements.setter
    def GooseFSxBuildElements(self, GooseFSxBuildElements):
        self._GooseFSxBuildElements = GooseFSxBuildElements

    @property
    def SecurityGroupId(self):
        """客户端集群所属的安全组
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def ClusterPort(self):
        """集群ssh通信端口，默认是22
        :rtype: int
        """
        return self._ClusterPort

    @ClusterPort.setter
    def ClusterPort(self, ClusterPort):
        self._ClusterPort = ClusterPort


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Zone = params.get("Zone")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("GooseFSxBuildElements") is not None:
            self._GooseFSxBuildElements = GooseFSxBuildElement()
            self._GooseFSxBuildElements._deserialize(params.get("GooseFSxBuildElements"))
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._ClusterPort = params.get("ClusterPort")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateFilesetRequest(AbstractModel):
    """CreateFileset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _FsetName: Fileset名称
        :type FsetName: str
        :param _FsetDir: Fileset目录
        :type FsetDir: str
        :param _QuotaSizeLimit: Fileset容量配额（需带单位G）
        :type QuotaSizeLimit: str
        :param _QuotaFilesLimit: Fileset文件数配额
        :type QuotaFilesLimit: str
        :param _AuditState: Fileset文件删除操作审计
        :type AuditState: str
        """
        self._FileSystemId = None
        self._FsetName = None
        self._FsetDir = None
        self._QuotaSizeLimit = None
        self._QuotaFilesLimit = None
        self._AuditState = None

    @property
    def FileSystemId(self):
        """文件系统id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsetName(self):
        """Fileset名称
        :rtype: str
        """
        return self._FsetName

    @FsetName.setter
    def FsetName(self, FsetName):
        self._FsetName = FsetName

    @property
    def FsetDir(self):
        """Fileset目录
        :rtype: str
        """
        return self._FsetDir

    @FsetDir.setter
    def FsetDir(self, FsetDir):
        self._FsetDir = FsetDir

    @property
    def QuotaSizeLimit(self):
        """Fileset容量配额（需带单位G）
        :rtype: str
        """
        return self._QuotaSizeLimit

    @QuotaSizeLimit.setter
    def QuotaSizeLimit(self, QuotaSizeLimit):
        self._QuotaSizeLimit = QuotaSizeLimit

    @property
    def QuotaFilesLimit(self):
        """Fileset文件数配额
        :rtype: str
        """
        return self._QuotaFilesLimit

    @QuotaFilesLimit.setter
    def QuotaFilesLimit(self, QuotaFilesLimit):
        self._QuotaFilesLimit = QuotaFilesLimit

    @property
    def AuditState(self):
        """Fileset文件删除操作审计
        :rtype: str
        """
        return self._AuditState

    @AuditState.setter
    def AuditState(self, AuditState):
        self._AuditState = AuditState


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FsetName = params.get("FsetName")
        self._FsetDir = params.get("FsetDir")
        self._QuotaSizeLimit = params.get("QuotaSizeLimit")
        self._QuotaFilesLimit = params.get("QuotaFilesLimit")
        self._AuditState = params.get("AuditState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFilesetResponse(AbstractModel):
    """CreateFileset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FsetId: Fileset id
        :type FsetId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FsetId = None
        self._RequestId = None

    @property
    def FsetId(self):
        """Fileset id
        :rtype: str
        """
        return self._FsetId

    @FsetId.setter
    def FsetId(self, FsetId):
        self._FsetId = FsetId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FsetId = params.get("FsetId")
        self._RequestId = params.get("RequestId")


class DeleteCrossVpcSubnetSupportForClientNodeRequest(AbstractModel):
    """DeleteCrossVpcSubnetSupportForClientNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _SubnetInfo: 子网信息
        :type SubnetInfo: :class:`tencentcloud.goosefs.v20220519.models.SubnetInfo`
        """
        self._FileSystemId = None
        self._SubnetInfo = None

    @property
    def FileSystemId(self):
        """文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def SubnetInfo(self):
        """子网信息
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.SubnetInfo`
        """
        return self._SubnetInfo

    @SubnetInfo.setter
    def SubnetInfo(self, SubnetInfo):
        self._SubnetInfo = SubnetInfo


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("SubnetInfo") is not None:
            self._SubnetInfo = SubnetInfo()
            self._SubnetInfo._deserialize(params.get("SubnetInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCrossVpcSubnetSupportForClientNodeResponse(AbstractModel):
    """DeleteCrossVpcSubnetSupportForClientNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """文件系统ID
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
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteFilesetRequest(AbstractModel):
    """DeleteFileset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _FsetId: Fileset id
        :type FsetId: str
        """
        self._FileSystemId = None
        self._FsetId = None

    @property
    def FileSystemId(self):
        """文件系统id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsetId(self):
        """Fileset id
        :rtype: str
        """
        return self._FsetId

    @FsetId.setter
    def FsetId(self, FsetId):
        self._FsetId = FsetId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FsetId = params.get("FsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFilesetResponse(AbstractModel):
    """DeleteFileset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeClientNodesRequest(AbstractModel):
    """DescribeClientNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统Id
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        """文件系统Id
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
        


class DescribeClientNodesResponse(AbstractModel):
    """DescribeClientNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientNodes: 客户端节点数组
        :type ClientNodes: list of ClientNodeAttribute
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientNodes = None
        self._RequestId = None

    @property
    def ClientNodes(self):
        """客户端节点数组
        :rtype: list of ClientNodeAttribute
        """
        return self._ClientNodes

    @ClientNodes.setter
    def ClientNodes(self, ClientNodes):
        self._ClientNodes = ClientNodes

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClientNodes") is not None:
            self._ClientNodes = []
            for item in params.get("ClientNodes"):
                obj = ClientNodeAttribute()
                obj._deserialize(item)
                self._ClientNodes.append(obj)
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
        """集群ID
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientTokens = None
        self._RequestId = None

    @property
    def ClientTokens(self):
        """客户端凭证
        :rtype: list of ClientToken
        """
        return self._ClientTokens

    @ClientTokens.setter
    def ClientTokens(self, ClientTokens):
        self._ClientTokens = ClientTokens

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        """角色名
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleTokens = None
        self._RequestId = None

    @property
    def RoleTokens(self):
        """角色凭证
        :rtype: list of RoleToken
        """
        return self._RoleTokens

    @RoleTokens.setter
    def RoleTokens(self, RoleTokens):
        self._RoleTokens = RoleTokens

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        """角色名
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterRoles = None
        self._RequestId = None

    @property
    def ClusterRoles(self):
        """集群角色
        :rtype: list of ClusterRole
        """
        return self._ClusterRoles

    @ClusterRoles.setter
    def ClusterRoles(self, ClusterRoles):
        self._ClusterRoles = ClusterRoles

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        """task id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FileSystemId(self):
        """file system id
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._FinishedFileNumber = None
        self._FinishedCapacity = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """任务状态 0(初始化中), 1(运行中), 2(已完成), 3(任务失败)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FinishedFileNumber(self):
        """已完成的文件数量
        :rtype: int
        """
        return self._FinishedFileNumber

    @FinishedFileNumber.setter
    def FinishedFileNumber(self, FinishedFileNumber):
        self._FinishedFileNumber = FinishedFileNumber

    @property
    def FinishedCapacity(self):
        """已完成的数据量
        :rtype: int
        """
        return self._FinishedCapacity

    @FinishedCapacity.setter
    def FinishedCapacity(self, FinishedCapacity):
        self._FinishedCapacity = FinishedCapacity

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeFileSystemBucketsRequest(AbstractModel):
    """DescribeFileSystemBuckets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        """文件系统ID
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
        


class DescribeFileSystemBucketsResponse(AbstractModel):
    """DescribeFileSystemBuckets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BucketList: bucket列表
        :type BucketList: list of MappedBucket
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BucketList = None
        self._RequestId = None

    @property
    def BucketList(self):
        """bucket列表
        :rtype: list of MappedBucket
        """
        return self._BucketList

    @BucketList.setter
    def BucketList(self, BucketList):
        self._BucketList = BucketList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BucketList") is not None:
            self._BucketList = []
            for item in params.get("BucketList"):
                obj = MappedBucket()
                obj._deserialize(item)
                self._BucketList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileSystemsRequest(AbstractModel):
    """DescribeFileSystems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 每页的数量
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页的数量
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
    """DescribeFileSystems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FSAttributeList: 文件系统列表
        :type FSAttributeList: list of FSAttribute
        :param _TotalCount: 总共的文件系统数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FSAttributeList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FSAttributeList(self):
        """文件系统列表
        :rtype: list of FSAttribute
        """
        return self._FSAttributeList

    @FSAttributeList.setter
    def FSAttributeList(self, FSAttributeList):
        self._FSAttributeList = FSAttributeList

    @property
    def TotalCount(self):
        """总共的文件系统数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FSAttributeList") is not None:
            self._FSAttributeList = []
            for item in params.get("FSAttributeList"):
                obj = FSAttribute()
                obj._deserialize(item)
                self._FSAttributeList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFilesetGeneralConfigRequest(AbstractModel):
    """DescribeFilesetGeneralConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        """文件系统id
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
        


class DescribeFilesetGeneralConfigResponse(AbstractModel):
    """DescribeFilesetGeneralConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnforceQuotaOnRoot: 配额对root用户生效
        :type EnforceQuotaOnRoot: str
        :param _Status: 配置状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnforceQuotaOnRoot = None
        self._Status = None
        self._RequestId = None

    @property
    def EnforceQuotaOnRoot(self):
        """配额对root用户生效
        :rtype: str
        """
        return self._EnforceQuotaOnRoot

    @EnforceQuotaOnRoot.setter
    def EnforceQuotaOnRoot(self, EnforceQuotaOnRoot):
        self._EnforceQuotaOnRoot = EnforceQuotaOnRoot

    @property
    def Status(self):
        """配置状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnforceQuotaOnRoot = params.get("EnforceQuotaOnRoot")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeFilesetsRequest(AbstractModel):
    """DescribeFilesets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _FilesetIds: FsetId列表
        :type FilesetIds: list of str
        :param _FilesetDirs: FsetDir列表
        :type FilesetDirs: list of str
        """
        self._FileSystemId = None
        self._FilesetIds = None
        self._FilesetDirs = None

    @property
    def FileSystemId(self):
        """文件系统id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FilesetIds(self):
        """FsetId列表
        :rtype: list of str
        """
        return self._FilesetIds

    @FilesetIds.setter
    def FilesetIds(self, FilesetIds):
        self._FilesetIds = FilesetIds

    @property
    def FilesetDirs(self):
        """FsetDir列表
        :rtype: list of str
        """
        return self._FilesetDirs

    @FilesetDirs.setter
    def FilesetDirs(self, FilesetDirs):
        self._FilesetDirs = FilesetDirs


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FilesetIds = params.get("FilesetIds")
        self._FilesetDirs = params.get("FilesetDirs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFilesetsResponse(AbstractModel):
    """DescribeFilesets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FilesetList: Fileset列表
        :type FilesetList: list of FilesetInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FilesetList = None
        self._RequestId = None

    @property
    def FilesetList(self):
        """Fileset列表
        :rtype: list of FilesetInfo
        """
        return self._FilesetList

    @FilesetList.setter
    def FilesetList(self, FilesetList):
        self._FilesetList = FilesetList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FilesetList") is not None:
            self._FilesetList = []
            for item in params.get("FilesetList"):
                obj = FilesetInfo()
                obj._deserialize(item)
                self._FilesetList.append(obj)
        self._RequestId = params.get("RequestId")


class DetachFileSystemBucketRequest(AbstractModel):
    """DetachFileSystemBucket请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _BucketName: 要解绑的Bucket名
        :type BucketName: str
        """
        self._FileSystemId = None
        self._BucketName = None

    @property
    def FileSystemId(self):
        """文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def BucketName(self):
        """要解绑的Bucket名
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._BucketName = params.get("BucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachFileSystemBucketResponse(AbstractModel):
    """DetachFileSystemBucket返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ExpandCapacityRequest(AbstractModel):
    """ExpandCapacity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _ExpandedCapacity: 新增扩容的系统容量
        :type ExpandedCapacity: int
        :param _ModifyType: 容量修改类型：add/sub
        :type ModifyType: str
        """
        self._FileSystemId = None
        self._ExpandedCapacity = None
        self._ModifyType = None

    @property
    def FileSystemId(self):
        """文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def ExpandedCapacity(self):
        """新增扩容的系统容量
        :rtype: int
        """
        return self._ExpandedCapacity

    @ExpandedCapacity.setter
    def ExpandedCapacity(self, ExpandedCapacity):
        self._ExpandedCapacity = ExpandedCapacity

    @property
    def ModifyType(self):
        """容量修改类型：add/sub
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._ExpandedCapacity = params.get("ExpandedCapacity")
        self._ModifyType = params.get("ModifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandCapacityResponse(AbstractModel):
    """ExpandCapacity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FSAttribute(AbstractModel):
    """文件系统属性

    """

    def __init__(self):
        r"""
        :param _Type: 文件系统类型, 可填goosefs和goosefsx
        :type Type: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _GooseFSxAttribute: GooseFSx文件系统属性
        :type GooseFSxAttribute: :class:`tencentcloud.goosefs.v20220519.models.GooseFSxAttribute`
        :param _Status: 文件系统状态 ACTIVE(运行中), CREATING(创建中), DESTROYING(销毁中), FAIL(创建失败),EXPANDING(扩容中),PROBING(容灾中)
        :type Status: str
        :param _Name: 文件系统名
        :type Name: str
        :param _Description: 文件系统备注描述
        :type Description: str
        :param _VpcId: vpc ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Zone: 子网所在的可用区
        :type Zone: str
        :param _Tag: Tag数组
        :type Tag: list of Tag
        :param _ModifyTime: 更新属性时间
        :type ModifyTime: str
        :param _ChargeAttribute: 文件系统付费信息
        :type ChargeAttribute: :class:`tencentcloud.goosefs.v20220519.models.ChargeAttribute`
        """
        self._Type = None
        self._FileSystemId = None
        self._CreateTime = None
        self._GooseFSxAttribute = None
        self._Status = None
        self._Name = None
        self._Description = None
        self._VpcId = None
        self._SubnetId = None
        self._Zone = None
        self._Tag = None
        self._ModifyTime = None
        self._ChargeAttribute = None

    @property
    def Type(self):
        """文件系统类型, 可填goosefs和goosefsx
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FileSystemId(self):
        """文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GooseFSxAttribute(self):
        """GooseFSx文件系统属性
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.GooseFSxAttribute`
        """
        return self._GooseFSxAttribute

    @GooseFSxAttribute.setter
    def GooseFSxAttribute(self, GooseFSxAttribute):
        self._GooseFSxAttribute = GooseFSxAttribute

    @property
    def Status(self):
        """文件系统状态 ACTIVE(运行中), CREATING(创建中), DESTROYING(销毁中), FAIL(创建失败),EXPANDING(扩容中),PROBING(容灾中)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Name(self):
        """文件系统名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """文件系统备注描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VpcId(self):
        """vpc ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Zone(self):
        """子网所在的可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Tag(self):
        """Tag数组
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ModifyTime(self):
        """更新属性时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ChargeAttribute(self):
        """文件系统付费信息
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.ChargeAttribute`
        """
        return self._ChargeAttribute

    @ChargeAttribute.setter
    def ChargeAttribute(self, ChargeAttribute):
        self._ChargeAttribute = ChargeAttribute


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._FileSystemId = params.get("FileSystemId")
        self._CreateTime = params.get("CreateTime")
        if params.get("GooseFSxAttribute") is not None:
            self._GooseFSxAttribute = GooseFSxAttribute()
            self._GooseFSxAttribute._deserialize(params.get("GooseFSxAttribute"))
        self._Status = params.get("Status")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Zone = params.get("Zone")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ModifyTime = params.get("ModifyTime")
        if params.get("ChargeAttribute") is not None:
            self._ChargeAttribute = ChargeAttribute()
            self._ChargeAttribute._deserialize(params.get("ChargeAttribute"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilesetInfo(AbstractModel):
    """Fileset信息

    """

    def __init__(self):
        r"""
        :param _FsetId: Fileset id
        :type FsetId: str
        :param _FsetName: Fileset名称
        :type FsetName: str
        :param _FsetDir: Fileset目录
        :type FsetDir: str
        :param _QuotaSizeLimit: Fileset容量配额限定值
        :type QuotaSizeLimit: str
        :param _QuotaSizeUsed: 已使用容量配额
        :type QuotaSizeUsed: str
        :param _QuotaSizeUsedPercent: 容量配额使用占比
        :type QuotaSizeUsedPercent: str
        :param _QuotaFilesLimit: Fileset文件数配额限定值
        :type QuotaFilesLimit: str
        :param _QuotaFilesUsed: 已使用文件数配额
        :type QuotaFilesUsed: str
        :param _QuotaFilesUsedPercent: 文件数配额使用占比
        :type QuotaFilesUsedPercent: str
        :param _AuditState: Fileset审计
        :type AuditState: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _Status: Fileset状态：creating 配置中 active 已生效 modify 修改中
        :type Status: str
        """
        self._FsetId = None
        self._FsetName = None
        self._FsetDir = None
        self._QuotaSizeLimit = None
        self._QuotaSizeUsed = None
        self._QuotaSizeUsedPercent = None
        self._QuotaFilesLimit = None
        self._QuotaFilesUsed = None
        self._QuotaFilesUsedPercent = None
        self._AuditState = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Status = None

    @property
    def FsetId(self):
        """Fileset id
        :rtype: str
        """
        return self._FsetId

    @FsetId.setter
    def FsetId(self, FsetId):
        self._FsetId = FsetId

    @property
    def FsetName(self):
        """Fileset名称
        :rtype: str
        """
        return self._FsetName

    @FsetName.setter
    def FsetName(self, FsetName):
        self._FsetName = FsetName

    @property
    def FsetDir(self):
        """Fileset目录
        :rtype: str
        """
        return self._FsetDir

    @FsetDir.setter
    def FsetDir(self, FsetDir):
        self._FsetDir = FsetDir

    @property
    def QuotaSizeLimit(self):
        """Fileset容量配额限定值
        :rtype: str
        """
        return self._QuotaSizeLimit

    @QuotaSizeLimit.setter
    def QuotaSizeLimit(self, QuotaSizeLimit):
        self._QuotaSizeLimit = QuotaSizeLimit

    @property
    def QuotaSizeUsed(self):
        """已使用容量配额
        :rtype: str
        """
        return self._QuotaSizeUsed

    @QuotaSizeUsed.setter
    def QuotaSizeUsed(self, QuotaSizeUsed):
        self._QuotaSizeUsed = QuotaSizeUsed

    @property
    def QuotaSizeUsedPercent(self):
        """容量配额使用占比
        :rtype: str
        """
        return self._QuotaSizeUsedPercent

    @QuotaSizeUsedPercent.setter
    def QuotaSizeUsedPercent(self, QuotaSizeUsedPercent):
        self._QuotaSizeUsedPercent = QuotaSizeUsedPercent

    @property
    def QuotaFilesLimit(self):
        """Fileset文件数配额限定值
        :rtype: str
        """
        return self._QuotaFilesLimit

    @QuotaFilesLimit.setter
    def QuotaFilesLimit(self, QuotaFilesLimit):
        self._QuotaFilesLimit = QuotaFilesLimit

    @property
    def QuotaFilesUsed(self):
        """已使用文件数配额
        :rtype: str
        """
        return self._QuotaFilesUsed

    @QuotaFilesUsed.setter
    def QuotaFilesUsed(self, QuotaFilesUsed):
        self._QuotaFilesUsed = QuotaFilesUsed

    @property
    def QuotaFilesUsedPercent(self):
        """文件数配额使用占比
        :rtype: str
        """
        return self._QuotaFilesUsedPercent

    @QuotaFilesUsedPercent.setter
    def QuotaFilesUsedPercent(self, QuotaFilesUsedPercent):
        self._QuotaFilesUsedPercent = QuotaFilesUsedPercent

    @property
    def AuditState(self):
        """Fileset审计
        :rtype: str
        """
        return self._AuditState

    @AuditState.setter
    def AuditState(self, AuditState):
        self._AuditState = AuditState

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Status(self):
        """Fileset状态：creating 配置中 active 已生效 modify 修改中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._FsetId = params.get("FsetId")
        self._FsetName = params.get("FsetName")
        self._FsetDir = params.get("FsetDir")
        self._QuotaSizeLimit = params.get("QuotaSizeLimit")
        self._QuotaSizeUsed = params.get("QuotaSizeUsed")
        self._QuotaSizeUsedPercent = params.get("QuotaSizeUsedPercent")
        self._QuotaFilesLimit = params.get("QuotaFilesLimit")
        self._QuotaFilesUsed = params.get("QuotaFilesUsed")
        self._QuotaFilesUsedPercent = params.get("QuotaFilesUsedPercent")
        self._AuditState = params.get("AuditState")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFSxAttribute(AbstractModel):
    """GooseFSx文件系统的属性

    """

    def __init__(self):
        r"""
        :param _Model: GooseFSx的型号
        :type Model: str
        :param _Capacity: 容量单位是GB, 例如4608(4.5TB)
        :type Capacity: int
        :param _MappedBucketList: 要关联映射的bucket列表
        :type MappedBucketList: list of MappedBucket
        :param _ClientManagerNodeList: 客户侧管理节点信息
        :type ClientManagerNodeList: list of ClientClusterManagerNodeInfo
        """
        self._Model = None
        self._Capacity = None
        self._MappedBucketList = None
        self._ClientManagerNodeList = None

    @property
    def Model(self):
        """GooseFSx的型号
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Capacity(self):
        """容量单位是GB, 例如4608(4.5TB)
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def MappedBucketList(self):
        """要关联映射的bucket列表
        :rtype: list of MappedBucket
        """
        return self._MappedBucketList

    @MappedBucketList.setter
    def MappedBucketList(self, MappedBucketList):
        self._MappedBucketList = MappedBucketList

    @property
    def ClientManagerNodeList(self):
        """客户侧管理节点信息
        :rtype: list of ClientClusterManagerNodeInfo
        """
        return self._ClientManagerNodeList

    @ClientManagerNodeList.setter
    def ClientManagerNodeList(self, ClientManagerNodeList):
        self._ClientManagerNodeList = ClientManagerNodeList


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Capacity = params.get("Capacity")
        if params.get("MappedBucketList") is not None:
            self._MappedBucketList = []
            for item in params.get("MappedBucketList"):
                obj = MappedBucket()
                obj._deserialize(item)
                self._MappedBucketList.append(obj)
        if params.get("ClientManagerNodeList") is not None:
            self._ClientManagerNodeList = []
            for item in params.get("ClientManagerNodeList"):
                obj = ClientClusterManagerNodeInfo()
                obj._deserialize(item)
                self._ClientManagerNodeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFSxBuildElement(AbstractModel):
    """GooseFSx创建时候的属性

    """

    def __init__(self):
        r"""
        :param _Model: GooseFSx的型号
        :type Model: str
        :param _Capacity: 容量单位是GB, 例如4608(4.5TB)
        :type Capacity: int
        :param _MappedBucketList: 要关联映射的bucket列表
        :type MappedBucketList: list of MappedBucket
        """
        self._Model = None
        self._Capacity = None
        self._MappedBucketList = None

    @property
    def Model(self):
        """GooseFSx的型号
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Capacity(self):
        """容量单位是GB, 例如4608(4.5TB)
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def MappedBucketList(self):
        """要关联映射的bucket列表
        :rtype: list of MappedBucket
        """
        return self._MappedBucketList

    @MappedBucketList.setter
    def MappedBucketList(self, MappedBucketList):
        self._MappedBucketList = MappedBucketList


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Capacity = params.get("Capacity")
        if params.get("MappedBucketList") is not None:
            self._MappedBucketList = []
            for item in params.get("MappedBucketList"):
                obj = MappedBucket()
                obj._deserialize(item)
                self._MappedBucketList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinuxNodeAttribute(AbstractModel):
    """添加删除客户端节点列表

    """

    def __init__(self):
        r"""
        :param _InstanceId: cvmId
        :type InstanceId: str
        :param _VpcId: 节点所属vpcid
        :type VpcId: str
        :param _SubnetId: 节点所属子网id
        :type SubnetId: str
        :param _LinuxClientNodeIp: linux客户端节点地址
        :type LinuxClientNodeIp: str
        :param _MountPoint: 自定义挂载点
        :type MountPoint: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._LinuxClientNodeIp = None
        self._MountPoint = None

    @property
    def InstanceId(self):
        """cvmId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        """节点所属vpcid
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """节点所属子网id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def LinuxClientNodeIp(self):
        """linux客户端节点地址
        :rtype: str
        """
        return self._LinuxClientNodeIp

    @LinuxClientNodeIp.setter
    def LinuxClientNodeIp(self, LinuxClientNodeIp):
        self._LinuxClientNodeIp = LinuxClientNodeIp

    @property
    def MountPoint(self):
        """自定义挂载点
        :rtype: str
        """
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._LinuxClientNodeIp = params.get("LinuxClientNodeIp")
        self._MountPoint = params.get("MountPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MappedBucket(AbstractModel):
    """关联的对象Bucket, 并将其映射到文件系统某个路径上

    """

    def __init__(self):
        r"""
        :param _BucketName: 对象存储Bucket名
        :type BucketName: str
        :param _FileSystemPath: 映射到的文件系统路径, 默认为/
        :type FileSystemPath: str
        :param _DataRepositoryTaskAutoStrategy: 数据流动的自动策略, 包含加载与沉降。策略可以是多种的组合
按需加载(OnDemandImport)
自动加载元数据(AutoImportMeta)
自动加载数据(AutoImportData)
周期加载(PeriodImport)

周期沉降(PeriodExport)
立即沉降(ImmediateExport)
        :type DataRepositoryTaskAutoStrategy: list of str
        :param _RuleId: 绑定bucket的数据流动策略ID
        :type RuleId: str
        :param _RuleDescription: 规则备注与描述
        :type RuleDescription: str
        :param _Status: 桶关联状态 0：关联中 1：关联完成
        :type Status: int
        :param _AccelerateFlag: 是否使用全球加速域名
        :type AccelerateFlag: bool
        :param _BucketRegion: 桶所在的园区
        :type BucketRegion: str
        :param _Endpoint: 自定义Endpoint
        :type Endpoint: str
        """
        self._BucketName = None
        self._FileSystemPath = None
        self._DataRepositoryTaskAutoStrategy = None
        self._RuleId = None
        self._RuleDescription = None
        self._Status = None
        self._AccelerateFlag = None
        self._BucketRegion = None
        self._Endpoint = None

    @property
    def BucketName(self):
        """对象存储Bucket名
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def FileSystemPath(self):
        """映射到的文件系统路径, 默认为/
        :rtype: str
        """
        return self._FileSystemPath

    @FileSystemPath.setter
    def FileSystemPath(self, FileSystemPath):
        self._FileSystemPath = FileSystemPath

    @property
    def DataRepositoryTaskAutoStrategy(self):
        """数据流动的自动策略, 包含加载与沉降。策略可以是多种的组合
按需加载(OnDemandImport)
自动加载元数据(AutoImportMeta)
自动加载数据(AutoImportData)
周期加载(PeriodImport)

周期沉降(PeriodExport)
立即沉降(ImmediateExport)
        :rtype: list of str
        """
        return self._DataRepositoryTaskAutoStrategy

    @DataRepositoryTaskAutoStrategy.setter
    def DataRepositoryTaskAutoStrategy(self, DataRepositoryTaskAutoStrategy):
        self._DataRepositoryTaskAutoStrategy = DataRepositoryTaskAutoStrategy

    @property
    def RuleId(self):
        """绑定bucket的数据流动策略ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleDescription(self):
        """规则备注与描述
        :rtype: str
        """
        return self._RuleDescription

    @RuleDescription.setter
    def RuleDescription(self, RuleDescription):
        self._RuleDescription = RuleDescription

    @property
    def Status(self):
        """桶关联状态 0：关联中 1：关联完成
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccelerateFlag(self):
        """是否使用全球加速域名
        :rtype: bool
        """
        return self._AccelerateFlag

    @AccelerateFlag.setter
    def AccelerateFlag(self, AccelerateFlag):
        self._AccelerateFlag = AccelerateFlag

    @property
    def BucketRegion(self):
        """桶所在的园区
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def Endpoint(self):
        """自定义Endpoint
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._FileSystemPath = params.get("FileSystemPath")
        self._DataRepositoryTaskAutoStrategy = params.get("DataRepositoryTaskAutoStrategy")
        self._RuleId = params.get("RuleId")
        self._RuleDescription = params.get("RuleDescription")
        self._Status = params.get("Status")
        self._AccelerateFlag = params.get("AccelerateFlag")
        self._BucketRegion = params.get("BucketRegion")
        self._Endpoint = params.get("Endpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataRepositoryBandwidthRequest(AbstractModel):
    """ModifyDataRepositoryBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _Bandwidth: 带宽, 单位MB/S
        :type Bandwidth: int
        """
        self._FileSystemId = None
        self._Bandwidth = None

    @property
    def FileSystemId(self):
        """文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Bandwidth(self):
        """带宽, 单位MB/S
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataRepositoryBandwidthResponse(AbstractModel):
    """ModifyDataRepositoryBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class QueryCrossVpcSubnetSupportForClientNodeRequest(AbstractModel):
    """QueryCrossVpcSubnetSupportForClientNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        """文件系统ID
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
        


class QueryCrossVpcSubnetSupportForClientNodeResponse(AbstractModel):
    """QueryCrossVpcSubnetSupportForClientNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetInfoCollection: 支持的子网信息集合
        :type SubnetInfoCollection: list of SubnetInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubnetInfoCollection = None
        self._RequestId = None

    @property
    def SubnetInfoCollection(self):
        """支持的子网信息集合
        :rtype: list of SubnetInfo
        """
        return self._SubnetInfoCollection

    @SubnetInfoCollection.setter
    def SubnetInfoCollection(self, SubnetInfoCollection):
        self._SubnetInfoCollection = SubnetInfoCollection

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SubnetInfoCollection") is not None:
            self._SubnetInfoCollection = []
            for item in params.get("SubnetInfoCollection"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self._SubnetInfoCollection.append(obj)
        self._RequestId = params.get("RequestId")


class QueryDataRepositoryBandwidthRequest(AbstractModel):
    """QueryDataRepositoryBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        """文件系统ID
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
        


class QueryDataRepositoryBandwidthResponse(AbstractModel):
    """QueryDataRepositoryBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Bandwidth: 数据流动带宽, 单位MB/s
        :type Bandwidth: int
        :param _BandwidthStatus: 带宽状态。1:待扩容;2:运行中;3:扩容中
        :type BandwidthStatus: int
        :param _MinBandwidth: 能设置的最小带宽, 单位MB/s
        :type MinBandwidth: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Bandwidth = None
        self._BandwidthStatus = None
        self._MinBandwidth = None
        self._RequestId = None

    @property
    def Bandwidth(self):
        """数据流动带宽, 单位MB/s
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def BandwidthStatus(self):
        """带宽状态。1:待扩容;2:运行中;3:扩容中
        :rtype: int
        """
        return self._BandwidthStatus

    @BandwidthStatus.setter
    def BandwidthStatus(self, BandwidthStatus):
        self._BandwidthStatus = BandwidthStatus

    @property
    def MinBandwidth(self):
        """能设置的最小带宽, 单位MB/s
        :rtype: int
        """
        return self._MinBandwidth

    @MinBandwidth.setter
    def MinBandwidth(self, MinBandwidth):
        self._MinBandwidth = MinBandwidth

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Bandwidth = params.get("Bandwidth")
        self._BandwidthStatus = params.get("BandwidthStatus")
        self._MinBandwidth = params.get("MinBandwidth")
        self._RequestId = params.get("RequestId")


class RoleToken(AbstractModel):
    """角色凭证

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名
        :type RoleName: str
        :param _Token: 用于goosefs client/sdk等
        :type Token: str
        """
        self._RoleName = None
        self._Token = None

    @property
    def RoleName(self):
        """角色名
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Token(self):
        """用于goosefs client/sdk等
        :rtype: str
        """
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
        


class SubnetInfo(AbstractModel):
    """vpc子网信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        """vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """文件系统关联的标签

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
        """标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值
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
        


class UpdateFilesetGeneralConfigRequest(AbstractModel):
    """UpdateFilesetGeneralConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _EnforceQuotaOnRoot: 配额对root用户生效
        :type EnforceQuotaOnRoot: str
        """
        self._FileSystemId = None
        self._EnforceQuotaOnRoot = None

    @property
    def FileSystemId(self):
        """文件系统id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def EnforceQuotaOnRoot(self):
        """配额对root用户生效
        :rtype: str
        """
        return self._EnforceQuotaOnRoot

    @EnforceQuotaOnRoot.setter
    def EnforceQuotaOnRoot(self, EnforceQuotaOnRoot):
        self._EnforceQuotaOnRoot = EnforceQuotaOnRoot


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._EnforceQuotaOnRoot = params.get("EnforceQuotaOnRoot")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFilesetGeneralConfigResponse(AbstractModel):
    """UpdateFilesetGeneralConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateFilesetRequest(AbstractModel):
    """UpdateFileset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统id
        :type FileSystemId: str
        :param _FsetId: Fileset id
        :type FsetId: str
        :param _QuotaSizeLimit: 容量配额限定值
        :type QuotaSizeLimit: str
        :param _QuotaFilesLimit: 文件数配额限定值
        :type QuotaFilesLimit: str
        :param _AuditState: Fileset文件删除操作审计
        :type AuditState: str
        """
        self._FileSystemId = None
        self._FsetId = None
        self._QuotaSizeLimit = None
        self._QuotaFilesLimit = None
        self._AuditState = None

    @property
    def FileSystemId(self):
        """文件系统id
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FsetId(self):
        """Fileset id
        :rtype: str
        """
        return self._FsetId

    @FsetId.setter
    def FsetId(self, FsetId):
        self._FsetId = FsetId

    @property
    def QuotaSizeLimit(self):
        """容量配额限定值
        :rtype: str
        """
        return self._QuotaSizeLimit

    @QuotaSizeLimit.setter
    def QuotaSizeLimit(self, QuotaSizeLimit):
        self._QuotaSizeLimit = QuotaSizeLimit

    @property
    def QuotaFilesLimit(self):
        """文件数配额限定值
        :rtype: str
        """
        return self._QuotaFilesLimit

    @QuotaFilesLimit.setter
    def QuotaFilesLimit(self, QuotaFilesLimit):
        self._QuotaFilesLimit = QuotaFilesLimit

    @property
    def AuditState(self):
        """Fileset文件删除操作审计
        :rtype: str
        """
        return self._AuditState

    @AuditState.setter
    def AuditState(self, AuditState):
        self._AuditState = AuditState


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FsetId = params.get("FsetId")
        self._QuotaSizeLimit = params.get("QuotaSizeLimit")
        self._QuotaFilesLimit = params.get("QuotaFilesLimit")
        self._AuditState = params.get("AuditState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFilesetResponse(AbstractModel):
    """UpdateFileset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")