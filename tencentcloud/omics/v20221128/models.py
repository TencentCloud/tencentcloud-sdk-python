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


class CVMOption(AbstractModel):
    """云服务器配置。

    """

    def __init__(self):
        r"""
        :param _Zone: 云服务器可用区。
        :type Zone: str
        :param _InstanceType: 云服务器实例规格。
        :type InstanceType: str
        """
        self._Zone = None
        self._InstanceType = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterOption(AbstractModel):
    """计算集群配置。

    """

    def __init__(self):
        r"""
        :param _Zone: 计算集群可用区。
        :type Zone: str
        :param _Type: 计算集群类型，取值范围：
- KUBERNETES
        :type Type: str
        """
        self._Zone = None
        self._Type = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 环境名称。
        :type Name: str
        :param _Config: 环境配置信息。
        :type Config: :class:`tencentcloud.omics.v20221128.models.EnvironmentConfig`
        :param _Description: 环境描述。
        :type Description: str
        """
        self._Name = None
        self._Config = None
        self._Description = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Config") is not None:
            self._Config = EnvironmentConfig()
            self._Config._deserialize(params.get("Config"))
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _WorkflowUuid: 工作流UUID。
        :type WorkflowUuid: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._WorkflowUuid = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def WorkflowUuid(self):
        return self._WorkflowUuid

    @WorkflowUuid.setter
    def WorkflowUuid(self, WorkflowUuid):
        self._WorkflowUuid = WorkflowUuid

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._WorkflowUuid = params.get("WorkflowUuid")
        self._RequestId = params.get("RequestId")


class DatabaseOption(AbstractModel):
    """数据库配置。

    """

    def __init__(self):
        r"""
        :param _Zone: 数据库可用区。
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentRequest(AbstractModel):
    """DeleteEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        """
        self._EnvironmentId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentResponse(AbstractModel):
    """DeleteEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkflowUuid: 工作流UUID。
        :type WorkflowUuid: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkflowUuid = None
        self._RequestId = None

    @property
    def WorkflowUuid(self):
        return self._WorkflowUuid

    @WorkflowUuid.setter
    def WorkflowUuid(self, WorkflowUuid):
        self._WorkflowUuid = WorkflowUuid

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkflowUuid = params.get("WorkflowUuid")
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 过滤器，支持过滤字段：
- EnvironmentId：环境ID
- Name：名称
- Status：环境状态
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param _Environments: 环境详情列表。
        :type Environments: list of Environment
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Environments = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Environments(self):
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Environments") is not None:
            self._Environments = []
            for item in params.get("Environments"):
                obj = Environment()
                obj._deserialize(item)
                self._Environments.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunGroupsRequest(AbstractModel):
    """DescribeRunGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- Name：任务批次名称
- RunGroupId：任务批次ID
- Status：任务批次状态
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunGroupsResponse(AbstractModel):
    """DescribeRunGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param _RunGroups: 任务批次列表。
        :type RunGroups: list of RunGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RunGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RunGroups(self):
        return self._RunGroups

    @RunGroups.setter
    def RunGroups(self, RunGroups):
        self._RunGroups = RunGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RunGroups") is not None:
            self._RunGroups = []
            for item in params.get("RunGroups"):
                obj = RunGroup()
                obj._deserialize(item)
                self._RunGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunsRequest(AbstractModel):
    """DescribeRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- RunGroupId：任务批次ID
- Status：任务状态
- RunUuid：任务UUID
- UserDefinedId：用户定义ID
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunsResponse(AbstractModel):
    """DescribeRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param _Runs: 任务列表。
        :type Runs: list of Run
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Runs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Runs(self):
        return self._Runs

    @Runs.setter
    def Runs(self, Runs):
        self._Runs = Runs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Runs") is not None:
            self._Runs = []
            for item in params.get("Runs"):
                obj = Run()
                obj._deserialize(item)
                self._Runs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- Name：表格名称
- TableId：表格ID
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数。
        :type TotalCount: int
        :param _Tables: 表格列表。
        :type Tables: list of Table
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tables = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = Table()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesRowsRequest(AbstractModel):
    """DescribeTablesRows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _TableId: 表格ID。
        :type TableId: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤器，支持过滤字段：
- Tr：表格数据，支持模糊查询
- TableRowUuid：表格行UUID
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._TableId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TableId(self):
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TableId = params.get("TableId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesRowsResponse(AbstractModel):
    """DescribeTablesRows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数。
        :type TotalCount: int
        :param _Rows: 表格行列表。
        :type Rows: list of TableRow
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TableRow()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """组学平台环境详情。

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _Name: 环境名称。
        :type Name: str
        :param _Description: 环境描述信息。
        :type Description: str
        :param _Region: 环境地域。
        :type Region: str
        :param _Type: 环境类型，取值范围：
- KUBERNETES：Kubernetes容器集群
- HPC：HPC高性能计算集群
        :type Type: str
        :param _Status: 环境状态，取值范围：
- INITIALIZING：创建中
- INITIALIZATION_ERROR：创建失败
- RUNNING：运行中
- ERROR：异常
- DELETING：正在删除
- DELETE_ERROR：删除失败
        :type Status: str
        :param _Available: 环境是否可用。环境需要可用才能投递计算任务。
        :type Available: bool
        :param _Message: 环境信息。
        :type Message: str
        :param _ResourceIds: 云资源ID。
        :type ResourceIds: :class:`tencentcloud.omics.v20221128.models.ResourceIds`
        :param _LastWorkflowUuid: 上个工作流UUID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastWorkflowUuid: str
        :param _CreationTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._Description = None
        self._Region = None
        self._Type = None
        self._Status = None
        self._Available = None
        self._Message = None
        self._ResourceIds = None
        self._LastWorkflowUuid = None
        self._CreationTime = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def LastWorkflowUuid(self):
        return self._LastWorkflowUuid

    @LastWorkflowUuid.setter
    def LastWorkflowUuid(self, LastWorkflowUuid):
        self._LastWorkflowUuid = LastWorkflowUuid

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Region = params.get("Region")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Available = params.get("Available")
        self._Message = params.get("Message")
        if params.get("ResourceIds") is not None:
            self._ResourceIds = ResourceIds()
            self._ResourceIds._deserialize(params.get("ResourceIds"))
        self._LastWorkflowUuid = params.get("LastWorkflowUuid")
        self._CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentConfig(AbstractModel):
    """环境配置。

    """

    def __init__(self):
        r"""
        :param _VPCOption: 私有网络配置。
        :type VPCOption: :class:`tencentcloud.omics.v20221128.models.VPCOption`
        :param _ClusterOption: 计算集群配置。
        :type ClusterOption: :class:`tencentcloud.omics.v20221128.models.ClusterOption`
        :param _DatabaseOption: 数据库配置。
        :type DatabaseOption: :class:`tencentcloud.omics.v20221128.models.DatabaseOption`
        :param _StorageOption: 存储配置。
        :type StorageOption: :class:`tencentcloud.omics.v20221128.models.StorageOption`
        :param _CVMOption: 云服务器配置。
        :type CVMOption: :class:`tencentcloud.omics.v20221128.models.CVMOption`
        """
        self._VPCOption = None
        self._ClusterOption = None
        self._DatabaseOption = None
        self._StorageOption = None
        self._CVMOption = None

    @property
    def VPCOption(self):
        return self._VPCOption

    @VPCOption.setter
    def VPCOption(self, VPCOption):
        self._VPCOption = VPCOption

    @property
    def ClusterOption(self):
        return self._ClusterOption

    @ClusterOption.setter
    def ClusterOption(self, ClusterOption):
        self._ClusterOption = ClusterOption

    @property
    def DatabaseOption(self):
        return self._DatabaseOption

    @DatabaseOption.setter
    def DatabaseOption(self, DatabaseOption):
        self._DatabaseOption = DatabaseOption

    @property
    def StorageOption(self):
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

    @property
    def CVMOption(self):
        return self._CVMOption

    @CVMOption.setter
    def CVMOption(self, CVMOption):
        self._CVMOption = CVMOption


    def _deserialize(self, params):
        if params.get("VPCOption") is not None:
            self._VPCOption = VPCOption()
            self._VPCOption._deserialize(params.get("VPCOption"))
        if params.get("ClusterOption") is not None:
            self._ClusterOption = ClusterOption()
            self._ClusterOption._deserialize(params.get("ClusterOption"))
        if params.get("DatabaseOption") is not None:
            self._DatabaseOption = DatabaseOption()
            self._DatabaseOption._deserialize(params.get("DatabaseOption"))
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOption()
            self._StorageOption._deserialize(params.get("StorageOption"))
        if params.get("CVMOption") is not None:
            self._CVMOption = CVMOption()
            self._CVMOption._deserialize(params.get("CVMOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecutionTime(AbstractModel):
    """执行时间。

    """

    def __init__(self):
        r"""
        :param _SubmitTime: 提交时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitTime: str
        :param _StartTime: 开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._SubmitTime = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SubmitTime(self):
        return self._SubmitTime

    @SubmitTime.setter
    def SubmitTime(self, SubmitTime):
        self._SubmitTime = SubmitTime

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


    def _deserialize(self, params):
        self._SubmitTime = params.get("SubmitTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。

    - 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。

    - 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段。
        :type Name: str
        :param _Values: 过滤字段值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
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
        


class GetRunCallsRequest(AbstractModel):
    """GetRunCalls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RunUuid: 任务Uuid。
        :type RunUuid: str
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _Path: 作业路径
        :type Path: str
        """
        self._RunUuid = None
        self._ProjectId = None
        self._Path = None

    @property
    def RunUuid(self):
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunCallsResponse(AbstractModel):
    """GetRunCalls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Calls: 作业详情。
        :type Calls: list of RunMetadata
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Calls = None
        self._RequestId = None

    @property
    def Calls(self):
        return self._Calls

    @Calls.setter
    def Calls(self, Calls):
        self._Calls = Calls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Calls") is not None:
            self._Calls = []
            for item in params.get("Calls"):
                obj = RunMetadata()
                obj._deserialize(item)
                self._Calls.append(obj)
        self._RequestId = params.get("RequestId")


class GetRunStatusRequest(AbstractModel):
    """GetRunStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RunUuid: 任务Uuid。
        :type RunUuid: str
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        """
        self._RunUuid = None
        self._ProjectId = None

    @property
    def RunUuid(self):
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunStatusResponse(AbstractModel):
    """GetRunStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metadata: 作业详情。
        :type Metadata: :class:`tencentcloud.omics.v20221128.models.RunMetadata`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metadata = None
        self._RequestId = None

    @property
    def Metadata(self):
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Metadata") is not None:
            self._Metadata = RunMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        self._RequestId = params.get("RequestId")


class ImportTableFileRequest(AbstractModel):
    """ImportTableFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 表格关联的项目ID。
        :type ProjectId: str
        :param _Name: 表格名称，支持20个字符内的英文字符、数字和下划线。
        :type Name: str
        :param _CosUri: 表格文件Cos对象路径。
        :type CosUri: str
        :param _DataType: 表格文件中每列的数据类型，支持的类型包括：Int、Float、String、File、Boolean、Array[Int]、Array[Float]、Array[String]、Array[File]、Array[Boolean]
        :type DataType: list of str
        :param _Description: 表格描述。
        :type Description: str
        """
        self._ProjectId = None
        self._Name = None
        self._CosUri = None
        self._DataType = None
        self._Description = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CosUri(self):
        return self._CosUri

    @CosUri.setter
    def CosUri(self, CosUri):
        self._CosUri = CosUri

    @property
    def DataType(self):
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._CosUri = params.get("CosUri")
        self._DataType = params.get("DataType")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportTableFileResponse(AbstractModel):
    """ImportTableFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableId: 表格ID。
        :type TableId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableId = None
        self._RequestId = None

    @property
    def TableId(self):
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TableId = params.get("TableId")
        self._RequestId = params.get("RequestId")


class ResourceIds(AbstractModel):
    """云资源ID。

    """

    def __init__(self):
        r"""
        :param _VPCId: 私有网络ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VPCId: str
        :param _SubnetId: 子网ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _SecurityGroupId: 安全组ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupId: str
        :param _TDSQLCId: TDSQL-C Mysql版数据库ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TDSQLCId: str
        :param _CFSId: 文件存储ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CFSId: str
        :param _CFSStorageType: 文件存储类型：取值范围：
- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
注意：此字段可能返回 null，表示取不到有效值。
        :type CFSStorageType: str
        :param _CVMId: 云服务器ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CVMId: str
        :param _EKSId: 弹性容器集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSId: str
        """
        self._VPCId = None
        self._SubnetId = None
        self._SecurityGroupId = None
        self._TDSQLCId = None
        self._CFSId = None
        self._CFSStorageType = None
        self._CVMId = None
        self._EKSId = None

    @property
    def VPCId(self):
        return self._VPCId

    @VPCId.setter
    def VPCId(self, VPCId):
        self._VPCId = VPCId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def TDSQLCId(self):
        return self._TDSQLCId

    @TDSQLCId.setter
    def TDSQLCId(self, TDSQLCId):
        self._TDSQLCId = TDSQLCId

    @property
    def CFSId(self):
        return self._CFSId

    @CFSId.setter
    def CFSId(self, CFSId):
        self._CFSId = CFSId

    @property
    def CFSStorageType(self):
        return self._CFSStorageType

    @CFSStorageType.setter
    def CFSStorageType(self, CFSStorageType):
        self._CFSStorageType = CFSStorageType

    @property
    def CVMId(self):
        return self._CVMId

    @CVMId.setter
    def CVMId(self, CVMId):
        self._CVMId = CVMId

    @property
    def EKSId(self):
        return self._EKSId

    @EKSId.setter
    def EKSId(self, EKSId):
        self._EKSId = EKSId


    def _deserialize(self, params):
        self._VPCId = params.get("VPCId")
        self._SubnetId = params.get("SubnetId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._TDSQLCId = params.get("TDSQLCId")
        self._CFSId = params.get("CFSId")
        self._CFSStorageType = params.get("CFSStorageType")
        self._CVMId = params.get("CVMId")
        self._EKSId = params.get("EKSId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRunsRequest(AbstractModel):
    """RetryRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 关联项目ID。
        :type ProjectId: str
        :param _RunUuids: 任务UUID。
        :type RunUuids: list of str
        """
        self._ProjectId = None
        self._RunUuids = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RunUuids(self):
        return self._RunUuids

    @RunUuids.setter
    def RunUuids(self, RunUuids):
        self._RunUuids = RunUuids


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RunUuids = params.get("RunUuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRunsResponse(AbstractModel):
    """RetryRuns返回参数结构体

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


class Run(AbstractModel):
    """任务。

    """

    def __init__(self):
        r"""
        :param _RunUuid: 任务UUID。
        :type RunUuid: str
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _UserDefinedId: 用户定义ID，单例运行为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefinedId: str
        :param _TableId: 表格ID，单例运行为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param _TableRowUuid: 表格行UUID，单例运行为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableRowUuid: str
        :param _Status: 任务状态。
        :type Status: str
        :param _Input: 任务输入。
        :type Input: str
        :param _Option: 运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _ExecutionTime: 执行时间。
        :type ExecutionTime: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        :param _ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self._RunUuid = None
        self._ProjectId = None
        self._ApplicationId = None
        self._RunGroupId = None
        self._EnvironmentId = None
        self._UserDefinedId = None
        self._TableId = None
        self._TableRowUuid = None
        self._Status = None
        self._Input = None
        self._Option = None
        self._ExecutionTime = None
        self._ErrorMessage = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def RunUuid(self):
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RunGroupId(self):
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def UserDefinedId(self):
        return self._UserDefinedId

    @UserDefinedId.setter
    def UserDefinedId(self, UserDefinedId):
        self._UserDefinedId = UserDefinedId

    @property
    def TableId(self):
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def TableRowUuid(self):
        return self._TableRowUuid

    @TableRowUuid.setter
    def TableRowUuid(self, TableRowUuid):
        self._TableRowUuid = TableRowUuid

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option

    @property
    def ExecutionTime(self):
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

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


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        self._ApplicationId = params.get("ApplicationId")
        self._RunGroupId = params.get("RunGroupId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._UserDefinedId = params.get("UserDefinedId")
        self._TableId = params.get("TableId")
        self._TableRowUuid = params.get("TableRowUuid")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        if params.get("ExecutionTime") is not None:
            self._ExecutionTime = ExecutionTime()
            self._ExecutionTime._deserialize(params.get("ExecutionTime"))
        self._ErrorMessage = params.get("ErrorMessage")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunApplicationRequest(AbstractModel):
    """RunApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _Name: 任务批次名称。
        :type Name: str
        :param _EnvironmentId: 投递环境ID。
        :type EnvironmentId: str
        :param _InputBase64: 任务输入JSON。需要进行base64编码。
        :type InputBase64: str
        :param _CacheClearDelay: 任务缓存清理时间。不填表示不清理。
        :type CacheClearDelay: int
        :param _Option: 运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _Description: 任务批次描述。
        :type Description: str
        :param _TableId: 批量投递表格ID，不填表示单例投递。
        :type TableId: str
        :param _TableRowUuids: 批量投递表格行UUID。不填表示表格全部行。
        :type TableRowUuids: list of str
        :param _ApplicationVersionId: 应用版本ID。不填表示使用当前最新版本。
        :type ApplicationVersionId: str
        """
        self._ApplicationId = None
        self._ProjectId = None
        self._Name = None
        self._EnvironmentId = None
        self._InputBase64 = None
        self._CacheClearDelay = None
        self._Option = None
        self._Description = None
        self._TableId = None
        self._TableRowUuids = None
        self._ApplicationVersionId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def InputBase64(self):
        return self._InputBase64

    @InputBase64.setter
    def InputBase64(self, InputBase64):
        self._InputBase64 = InputBase64

    @property
    def CacheClearDelay(self):
        return self._CacheClearDelay

    @CacheClearDelay.setter
    def CacheClearDelay(self, CacheClearDelay):
        self._CacheClearDelay = CacheClearDelay

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TableId(self):
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def TableRowUuids(self):
        return self._TableRowUuids

    @TableRowUuids.setter
    def TableRowUuids(self, TableRowUuids):
        self._TableRowUuids = TableRowUuids

    @property
    def ApplicationVersionId(self):
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._EnvironmentId = params.get("EnvironmentId")
        self._InputBase64 = params.get("InputBase64")
        self._CacheClearDelay = params.get("CacheClearDelay")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        self._Description = params.get("Description")
        self._TableId = params.get("TableId")
        self._TableRowUuids = params.get("TableRowUuids")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunApplicationResponse(AbstractModel):
    """RunApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RunGroupId = None
        self._RequestId = None

    @property
    def RunGroupId(self):
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._RequestId = params.get("RequestId")


class RunGroup(AbstractModel):
    """任务。

    """

    def __init__(self):
        r"""
        :param _RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param _ProjectId: 项目ID。
        :type ProjectId: str
        :param _ProjectName: 项目名称。
        :type ProjectName: str
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _ApplicationName: 应用名称。
        :type ApplicationName: str
        :param _ApplicationType: 应用类型。
        :type ApplicationType: str
        :param _EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param _EnvironmentName: 环境名称。
        :type EnvironmentName: str
        :param _TableId: 表格ID，单例运行为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param _Name: 任务名称。
        :type Name: str
        :param _Description: 任务描述。
        :type Description: str
        :param _Status: 任务状态。
        :type Status: str
        :param _Input: 任务输入。
        :type Input: str
        :param _Option: 运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _TotalRun: 任务总数量。
        :type TotalRun: int
        :param _RunStatusCounts: 各状态任务的数量。
        :type RunStatusCounts: list of RunStatusCount
        :param _ExecutionTime: 执行时间。
        :type ExecutionTime: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        :param _ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self._RunGroupId = None
        self._ProjectId = None
        self._ProjectName = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._ApplicationType = None
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._TableId = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._Input = None
        self._Option = None
        self._TotalRun = None
        self._RunStatusCounts = None
        self._ExecutionTime = None
        self._ErrorMessage = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def RunGroupId(self):
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

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
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def TableId(self):
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option

    @property
    def TotalRun(self):
        return self._TotalRun

    @TotalRun.setter
    def TotalRun(self, TotalRun):
        self._TotalRun = TotalRun

    @property
    def RunStatusCounts(self):
        return self._RunStatusCounts

    @RunStatusCounts.setter
    def RunStatusCounts(self, RunStatusCounts):
        self._RunStatusCounts = RunStatusCounts

    @property
    def ExecutionTime(self):
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

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


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationType = params.get("ApplicationType")
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._TableId = params.get("TableId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        self._TotalRun = params.get("TotalRun")
        if params.get("RunStatusCounts") is not None:
            self._RunStatusCounts = []
            for item in params.get("RunStatusCounts"):
                obj = RunStatusCount()
                obj._deserialize(item)
                self._RunStatusCounts.append(obj)
        if params.get("ExecutionTime") is not None:
            self._ExecutionTime = ExecutionTime()
            self._ExecutionTime._deserialize(params.get("ExecutionTime"))
        self._ErrorMessage = params.get("ErrorMessage")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMetadata(AbstractModel):
    """任务作业详情。

    """

    def __init__(self):
        r"""
        :param _RunType: 任务类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type RunType: str
        :param _RunId: 任务ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RunId: str
        :param _ParentId: 父层ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param _JobId: 作业ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _CallName: 作业名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CallName: str
        :param _ScatterIndex: Scatter索引。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScatterIndex: str
        :param _Input: 输入。
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: str
        :param _Output: 输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ErrorMessage: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _SubmitTime: 提交时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitTime: str
        :param _EndTime: 结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Command: 命令行。
注意：此字段可能返回 null，表示取不到有效值。
        :type Command: str
        :param _Runtime: 运行时。
注意：此字段可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param _Preprocess: 预处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type Preprocess: bool
        :param _PostProcess: 后处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostProcess: bool
        :param _CallCached: Cache命中
注意：此字段可能返回 null，表示取不到有效值。
        :type CallCached: bool
        :param _Stdout: 标准输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Stdout: str
        :param _Stderr: 错误输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Stderr: str
        """
        self._RunType = None
        self._RunId = None
        self._ParentId = None
        self._JobId = None
        self._CallName = None
        self._ScatterIndex = None
        self._Input = None
        self._Output = None
        self._Status = None
        self._ErrorMessage = None
        self._StartTime = None
        self._SubmitTime = None
        self._EndTime = None
        self._Command = None
        self._Runtime = None
        self._Preprocess = None
        self._PostProcess = None
        self._CallCached = None
        self._Stdout = None
        self._Stderr = None

    @property
    def RunType(self):
        return self._RunType

    @RunType.setter
    def RunType(self, RunType):
        self._RunType = RunType

    @property
    def RunId(self):
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def ParentId(self):
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CallName(self):
        return self._CallName

    @CallName.setter
    def CallName(self, CallName):
        self._CallName = CallName

    @property
    def ScatterIndex(self):
        return self._ScatterIndex

    @ScatterIndex.setter
    def ScatterIndex(self, ScatterIndex):
        self._ScatterIndex = ScatterIndex

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def SubmitTime(self):
        return self._SubmitTime

    @SubmitTime.setter
    def SubmitTime(self, SubmitTime):
        self._SubmitTime = SubmitTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def Preprocess(self):
        return self._Preprocess

    @Preprocess.setter
    def Preprocess(self, Preprocess):
        self._Preprocess = Preprocess

    @property
    def PostProcess(self):
        return self._PostProcess

    @PostProcess.setter
    def PostProcess(self, PostProcess):
        self._PostProcess = PostProcess

    @property
    def CallCached(self):
        return self._CallCached

    @CallCached.setter
    def CallCached(self, CallCached):
        self._CallCached = CallCached

    @property
    def Stdout(self):
        return self._Stdout

    @Stdout.setter
    def Stdout(self, Stdout):
        self._Stdout = Stdout

    @property
    def Stderr(self):
        return self._Stderr

    @Stderr.setter
    def Stderr(self, Stderr):
        self._Stderr = Stderr


    def _deserialize(self, params):
        self._RunType = params.get("RunType")
        self._RunId = params.get("RunId")
        self._ParentId = params.get("ParentId")
        self._JobId = params.get("JobId")
        self._CallName = params.get("CallName")
        self._ScatterIndex = params.get("ScatterIndex")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._Status = params.get("Status")
        self._ErrorMessage = params.get("ErrorMessage")
        self._StartTime = params.get("StartTime")
        self._SubmitTime = params.get("SubmitTime")
        self._EndTime = params.get("EndTime")
        self._Command = params.get("Command")
        self._Runtime = params.get("Runtime")
        self._Preprocess = params.get("Preprocess")
        self._PostProcess = params.get("PostProcess")
        self._CallCached = params.get("CallCached")
        self._Stdout = params.get("Stdout")
        self._Stderr = params.get("Stderr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunOption(AbstractModel):
    """运行应用选项。

    """

    def __init__(self):
        r"""
        :param _FailureMode: 运行失败模式，取值范围：
- ContinueWhilePossible
- NoNewCalls
        :type FailureMode: str
        :param _UseCallCache: 是否使用Call-Caching功能。
        :type UseCallCache: bool
        :param _UseErrorOnHold: 是否使用错误挂起功能。
        :type UseErrorOnHold: bool
        :param _FinalWorkflowOutputsDir: 输出归档COS路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalWorkflowOutputsDir: str
        :param _UseRelativeOutputPaths: 是否使用相对目录归档输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type UseRelativeOutputPaths: bool
        """
        self._FailureMode = None
        self._UseCallCache = None
        self._UseErrorOnHold = None
        self._FinalWorkflowOutputsDir = None
        self._UseRelativeOutputPaths = None

    @property
    def FailureMode(self):
        return self._FailureMode

    @FailureMode.setter
    def FailureMode(self, FailureMode):
        self._FailureMode = FailureMode

    @property
    def UseCallCache(self):
        return self._UseCallCache

    @UseCallCache.setter
    def UseCallCache(self, UseCallCache):
        self._UseCallCache = UseCallCache

    @property
    def UseErrorOnHold(self):
        return self._UseErrorOnHold

    @UseErrorOnHold.setter
    def UseErrorOnHold(self, UseErrorOnHold):
        self._UseErrorOnHold = UseErrorOnHold

    @property
    def FinalWorkflowOutputsDir(self):
        return self._FinalWorkflowOutputsDir

    @FinalWorkflowOutputsDir.setter
    def FinalWorkflowOutputsDir(self, FinalWorkflowOutputsDir):
        self._FinalWorkflowOutputsDir = FinalWorkflowOutputsDir

    @property
    def UseRelativeOutputPaths(self):
        return self._UseRelativeOutputPaths

    @UseRelativeOutputPaths.setter
    def UseRelativeOutputPaths(self, UseRelativeOutputPaths):
        self._UseRelativeOutputPaths = UseRelativeOutputPaths


    def _deserialize(self, params):
        self._FailureMode = params.get("FailureMode")
        self._UseCallCache = params.get("UseCallCache")
        self._UseErrorOnHold = params.get("UseErrorOnHold")
        self._FinalWorkflowOutputsDir = params.get("FinalWorkflowOutputsDir")
        self._UseRelativeOutputPaths = params.get("UseRelativeOutputPaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunStatusCount(AbstractModel):
    """任务运行状态。

    """

    def __init__(self):
        r"""
        :param _Status: 状态。
        :type Status: str
        :param _Count: 数量。
        :type Count: int
        """
        self._Status = None
        self._Count = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOption(AbstractModel):
    """文件存储配置。

    """

    def __init__(self):
        r"""
        :param _StorageType: 文件存储类型，取值范围：
- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :type StorageType: str
        :param _Zone: 文件存储可用区。
        :type Zone: str
        :param _Capacity: 文件系统容量，turbo系列必填，单位为GiB。 
- turbo标准型起售40TiB，即40960GiB；扩容步长20TiB，即20480 GiB。
- turbo性能型起售20TiB，即20480 GiB；扩容步长10TiB，即10240 GiB。
        :type Capacity: int
        """
        self._StorageType = None
        self._Zone = None
        self._Capacity = None

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._Zone = params.get("Zone")
        self._Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """表格。

    """

    def __init__(self):
        r"""
        :param _TableId: 表格ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param _ProjectId: 关联项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _Name: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 表格描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Columns: 表格列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of TableColumn
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Creator: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        """
        self._TableId = None
        self._ProjectId = None
        self._Name = None
        self._Description = None
        self._Columns = None
        self._CreateTime = None
        self._Creator = None

    @property
    def TableId(self):
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator


    def _deserialize(self, params):
        self._TableId = params.get("TableId")
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = TableColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._Creator = params.get("Creator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumn(AbstractModel):
    """表格列。

    """

    def __init__(self):
        r"""
        :param _Header: 列名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Header: str
        :param _DataType: 列数据类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DataType: str
        """
        self._Header = None
        self._DataType = None

    @property
    def Header(self):
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def DataType(self):
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        self._Header = params.get("Header")
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableRow(AbstractModel):
    """表格行。

    """

    def __init__(self):
        r"""
        :param _TableRowUuid: 表格行UUID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableRowUuid: str
        :param _Content: 表格行内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of str
        """
        self._TableRowUuid = None
        self._Content = None

    @property
    def TableRowUuid(self):
        return self._TableRowUuid

    @TableRowUuid.setter
    def TableRowUuid(self, TableRowUuid):
        self._TableRowUuid = TableRowUuid

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._TableRowUuid = params.get("TableRowUuid")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VPCOption(AbstractModel):
    """私有网络配置。

    """

    def __init__(self):
        r"""
        :param _SubnetZone: 子网可用区。
        :type SubnetZone: str
        :param _VPCCIDRBlock: 私有网络CIDR。
        :type VPCCIDRBlock: str
        :param _SubnetCIDRBlock: 子网CIDR。
        :type SubnetCIDRBlock: str
        """
        self._SubnetZone = None
        self._VPCCIDRBlock = None
        self._SubnetCIDRBlock = None

    @property
    def SubnetZone(self):
        return self._SubnetZone

    @SubnetZone.setter
    def SubnetZone(self, SubnetZone):
        self._SubnetZone = SubnetZone

    @property
    def VPCCIDRBlock(self):
        return self._VPCCIDRBlock

    @VPCCIDRBlock.setter
    def VPCCIDRBlock(self, VPCCIDRBlock):
        self._VPCCIDRBlock = VPCCIDRBlock

    @property
    def SubnetCIDRBlock(self):
        return self._SubnetCIDRBlock

    @SubnetCIDRBlock.setter
    def SubnetCIDRBlock(self, SubnetCIDRBlock):
        self._SubnetCIDRBlock = SubnetCIDRBlock


    def _deserialize(self, params):
        self._SubnetZone = params.get("SubnetZone")
        self._VPCCIDRBlock = params.get("VPCCIDRBlock")
        self._SubnetCIDRBlock = params.get("SubnetCIDRBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        