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


class DeregisterMigrationTaskRequest(AbstractModel):
    """DeregisterMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
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
        


class DeregisterMigrationTaskResponse(AbstractModel):
    """DeregisterMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeMigrationTaskRequest(AbstractModel):
    """DescribeMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，例如msp-jitoh33n
        :type TaskId: str
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
        


class DescribeMigrationTaskResponse(AbstractModel):
    """DescribeMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 迁移详情列表
        :type TaskStatus: list of TaskStatus
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatus = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskStatus") is not None:
            self._TaskStatus = []
            for item in params.get("TaskStatus"):
                obj = TaskStatus()
                obj._deserialize(item)
                self._TaskStatus.append(obj)
        self._RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """迁移目的信息

    """

    def __init__(self):
        r"""
        :param _Region: 迁移目的地域
        :type Region: str
        :param _Ip: 迁移目的Ip
        :type Ip: str
        :param _Port: 迁移目的端口
        :type Port: str
        :param _InstanceId: 迁移目的实例Id
        :type InstanceId: str
        """
        self._Region = None
        self._Ip = None
        self._Port = None
        self._InstanceId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationProjectRequest(AbstractModel):
    """ListMigrationProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 记录起始数，默认值为0
        :type Offset: int
        :param _Limit: 返回条数，默认值为500
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationProjectResponse(AbstractModel):
    """ListMigrationProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Projects: 项目列表
        :type Projects: list of Project
        :param _TotalCount: 项目总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Projects = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Projects(self):
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

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
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListMigrationTaskRequest(AbstractModel):
    """ListMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 记录起始数，默认值为0
        :type Offset: int
        :param _Limit: 记录条数，默认值为10
        :type Limit: int
        :param _ProjectId: 项目ID，默认值为空
        :type ProjectId: int
        """
        self._Offset = None
        self._Limit = None
        self._ProjectId = None

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationTaskResponse(AbstractModel):
    """ListMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总条数
        :type TotalCount: int
        :param _Tasks: 迁移任务列表
        :type Tasks: list of Task
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyMigrationTaskBelongToProjectRequest(AbstractModel):
    """ModifyMigrationTaskBelongToProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，例如msp-jitoh33n
        :type TaskId: str
        :param _ProjectId: 项目ID，例如10005
        :type ProjectId: int
        """
        self._TaskId = None
        self._ProjectId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationTaskBelongToProjectResponse(AbstractModel):
    """ModifyMigrationTaskBelongToProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyMigrationTaskStatusRequest(AbstractModel):
    """ModifyMigrationTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，取值为unstart，migrating，finish，fail之一，分别代表该迁移任务状态为迁移未开始，迁移中，迁移完成，迁移失败
        :type Status: str
        :param _TaskId: 任务ID，例如msp-jitoh33n
        :type TaskId: str
        """
        self._Status = None
        self._TaskId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationTaskStatusResponse(AbstractModel):
    """ModifyMigrationTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class Project(AbstractModel):
    """列表类型

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectName: 项目名称
        :type ProjectName: str
        """
        self._ProjectId = None
        self._ProjectName = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterMigrationTaskRequest(AbstractModel):
    """RegisterMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskType: 任务类型，取值database（数据库迁移）、file（文件迁移）、host（主机迁移）
        :type TaskType: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ServiceSupplier: 服务提供商名称
        :type ServiceSupplier: str
        :param _CreateTime: 迁移任务创建时间
        :type CreateTime: str
        :param _UpdateTime: 迁移任务更新时间
        :type UpdateTime: str
        :param _MigrateClass: 迁移类别，如数据库迁移中mysql:mysql代表从mysql迁移到mysql，文件迁移中oss:cos代表从阿里云oss迁移到腾讯云cos
        :type MigrateClass: str
        :param _SrcInfo: 迁移任务源信息
        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`
        :param _DstInfo: 迁移任务目的信息
        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`
        :param _SrcAccessType: 源实例接入类型，数据库迁移时填写值为：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)
        :type SrcAccessType: str
        :param _SrcDatabaseType: 源实例数据库类型，数据库迁移时填写，取值为mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb 之一
        :type SrcDatabaseType: str
        :param _DstAccessType: 目标实例接入类型，数据库迁移时填写值为：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)
        :type DstAccessType: str
        :param _DstDatabaseType: 目标实例数据库类型,数据库迁移时填写，取值为mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb 之一
        :type DstDatabaseType: str
        """
        self._TaskType = None
        self._TaskName = None
        self._ServiceSupplier = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MigrateClass = None
        self._SrcInfo = None
        self._DstInfo = None
        self._SrcAccessType = None
        self._SrcDatabaseType = None
        self._DstAccessType = None
        self._DstDatabaseType = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ServiceSupplier(self):
        return self._ServiceSupplier

    @ServiceSupplier.setter
    def ServiceSupplier(self, ServiceSupplier):
        self._ServiceSupplier = ServiceSupplier

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MigrateClass(self):
        return self._MigrateClass

    @MigrateClass.setter
    def MigrateClass(self, MigrateClass):
        self._MigrateClass = MigrateClass

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def SrcAccessType(self):
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcDatabaseType(self):
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def DstAccessType(self):
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstDatabaseType(self):
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._TaskName = params.get("TaskName")
        self._ServiceSupplier = params.get("ServiceSupplier")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MigrateClass = params.get("MigrateClass")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._SrcAccessType = params.get("SrcAccessType")
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        self._DstDatabaseType = params.get("DstDatabaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterMigrationTaskResponse(AbstractModel):
    """RegisterMigrationTask返回参数结构体

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


class SrcInfo(AbstractModel):
    """迁移源信息

    """

    def __init__(self):
        r"""
        :param _Region: 迁移源地域
        :type Region: str
        :param _Ip: 迁移源Ip
        :type Ip: str
        :param _Port: 迁移源端口
        :type Port: str
        :param _InstanceId: 迁移源实例Id
        :type InstanceId: str
        """
        self._Region = None
        self._Ip = None
        self._Port = None
        self._InstanceId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """迁移任务类别

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _MigrationType: 迁移类型
        :type MigrationType: str
        :param _Status: 迁移状态
        :type Status: str
        :param _ProjectId: 项目Id
        :type ProjectId: int
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _SrcInfo: 迁移源信息
        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`
        :param _MigrationTimeLine: 迁移时间信息
        :type MigrationTimeLine: :class:`tencentcloud.msp.v20180319.models.TimeObj`
        :param _Updated: 状态更新时间
        :type Updated: str
        :param _DstInfo: 迁移目的信息
        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`
        """
        self._TaskId = None
        self._TaskName = None
        self._MigrationType = None
        self._Status = None
        self._ProjectId = None
        self._ProjectName = None
        self._SrcInfo = None
        self._MigrationTimeLine = None
        self._Updated = None
        self._DstInfo = None

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
    def MigrationType(self):
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def MigrationTimeLine(self):
        return self._MigrationTimeLine

    @MigrationTimeLine.setter
    def MigrationTimeLine(self, MigrationTimeLine):
        self._MigrationTimeLine = MigrationTimeLine

    @property
    def Updated(self):
        return self._Updated

    @Updated.setter
    def Updated(self, Updated):
        self._Updated = Updated

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._MigrationType = params.get("MigrationType")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("MigrationTimeLine") is not None:
            self._MigrationTimeLine = TimeObj()
            self._MigrationTimeLine._deserialize(params.get("MigrationTimeLine"))
        self._Updated = params.get("Updated")
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatus(AbstractModel):
    """迁移详情列表

    """

    def __init__(self):
        r"""
        :param _Status: 迁移状态
        :type Status: str
        :param _Progress: 迁移进度
        :type Progress: str
        :param _UpdateTime: 迁移日期
        :type UpdateTime: str
        """
        self._Status = None
        self._Progress = None
        self._UpdateTime = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeObj(AbstractModel):
    """时间对象

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._CreateTime = None
        self._EndTime = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        