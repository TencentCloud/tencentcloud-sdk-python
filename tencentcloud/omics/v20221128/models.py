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
        :param Zone: 云服务器可用区。
        :type Zone: str
        :param InstanceType: 云服务器实例规格。
        :type InstanceType: str
        """
        self.Zone = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterOption(AbstractModel):
    """计算集群配置。

    """

    def __init__(self):
        r"""
        :param Zone: 计算集群可用区。
        :type Zone: str
        :param Type: 计算集群类型，取值范围：
- KUBERNETES
        :type Type: str
        """
        self.Zone = None
        self.Type = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 环境名称。
        :type Name: str
        :param Config: 环境配置信息。
        :type Config: :class:`tencentcloud.omics.v20221128.models.EnvironmentConfig`
        :param Description: 环境描述。
        :type Description: str
        """
        self.Name = None
        self.Config = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Config") is not None:
            self.Config = EnvironmentConfig()
            self.Config._deserialize(params.get("Config"))
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param WorkflowUuid: 工作流UUID。
        :type WorkflowUuid: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.WorkflowUuid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.WorkflowUuid = params.get("WorkflowUuid")
        self.RequestId = params.get("RequestId")


class DatabaseOption(AbstractModel):
    """数据库配置。

    """

    def __init__(self):
        r"""
        :param Zone: 数据库可用区。
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentRequest(AbstractModel):
    """DeleteEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境ID。
        :type EnvironmentId: str
        """
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentResponse(AbstractModel):
    """DeleteEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkflowUuid: 工作流UUID。
        :type WorkflowUuid: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkflowUuid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkflowUuid = params.get("WorkflowUuid")
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Filters: 过滤器，支持过滤字段：
- EnvironmentId：环境ID
- Name：名称
- Status：环境状态
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param Environments: 环境详情列表。
        :type Environments: list of Environment
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Environments = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Environments") is not None:
            self.Environments = []
            for item in params.get("Environments"):
                obj = Environment()
                obj._deserialize(item)
                self.Environments.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRunGroupsRequest(AbstractModel):
    """DescribeRunGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID。
        :type ProjectId: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤器，支持过滤字段：
- Name：任务批次名称
- RunGroupId：任务批次ID
- Status：任务批次状态
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunGroupsResponse(AbstractModel):
    """DescribeRunGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param RunGroups: 任务批次列表。
        :type RunGroups: list of RunGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RunGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RunGroups") is not None:
            self.RunGroups = []
            for item in params.get("RunGroups"):
                obj = RunGroup()
                obj._deserialize(item)
                self.RunGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRunsRequest(AbstractModel):
    """DescribeRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID。
        :type ProjectId: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤器，支持过滤字段：
- RunGroupId：任务批次ID
- Status：任务状态
- RunUuid：任务UUID
- UserDefinedId：用户定义ID
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunsResponse(AbstractModel):
    """DescribeRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的数量。
        :type TotalCount: int
        :param Runs: 任务列表。
        :type Runs: list of Run
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Runs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Runs") is not None:
            self.Runs = []
            for item in params.get("Runs"):
                obj = Run()
                obj._deserialize(item)
                self.Runs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID。
        :type ProjectId: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤器，支持过滤字段：
- Name：表格名称
- TableId：表格ID
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 结果总数。
        :type TotalCount: int
        :param Tables: 表格列表。
        :type Tables: list of Table
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tables = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = Table()
                obj._deserialize(item)
                self.Tables.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesRowsRequest(AbstractModel):
    """DescribeTablesRows请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID。
        :type ProjectId: str
        :param TableId: 表格ID。
        :type TableId: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤器，支持过滤字段：
- Tr：表格数据，支持模糊查询
- TableRowUuid：表格行UUID
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.TableId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.TableId = params.get("TableId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesRowsResponse(AbstractModel):
    """DescribeTablesRows返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 结果总数。
        :type TotalCount: int
        :param Rows: 表格行列表。
        :type Rows: list of TableRow
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TableRow()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """组学平台环境详情。

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param Name: 环境名称。
        :type Name: str
        :param Description: 环境描述信息。
        :type Description: str
        :param Region: 环境地域。
        :type Region: str
        :param Type: 环境类型，取值范围：
- KUBERNETES：Kubernetes容器集群
- HPC：HPC高性能计算集群
        :type Type: str
        :param Status: 环境状态，取值范围：
- INITIALIZING：创建中
- INITIALIZATION_ERROR：创建失败
- RUNNING：运行中
- ERROR：异常
- DELETING：正在删除
- DELETE_ERROR：删除失败
        :type Status: str
        :param Available: 环境是否可用。环境需要可用才能投递计算任务。
        :type Available: bool
        :param Message: 环境信息。
        :type Message: str
        :param ResourceIds: 云资源ID。
        :type ResourceIds: :class:`tencentcloud.omics.v20221128.models.ResourceIds`
        :param LastWorkflowUuid: 上个工作流UUID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastWorkflowUuid: str
        :param CreationTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        """
        self.EnvironmentId = None
        self.Name = None
        self.Description = None
        self.Region = None
        self.Type = None
        self.Status = None
        self.Available = None
        self.Message = None
        self.ResourceIds = None
        self.LastWorkflowUuid = None
        self.CreationTime = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Region = params.get("Region")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Available = params.get("Available")
        self.Message = params.get("Message")
        if params.get("ResourceIds") is not None:
            self.ResourceIds = ResourceIds()
            self.ResourceIds._deserialize(params.get("ResourceIds"))
        self.LastWorkflowUuid = params.get("LastWorkflowUuid")
        self.CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentConfig(AbstractModel):
    """环境配置。

    """

    def __init__(self):
        r"""
        :param VPCOption: 私有网络配置。
        :type VPCOption: :class:`tencentcloud.omics.v20221128.models.VPCOption`
        :param ClusterOption: 计算集群配置。
        :type ClusterOption: :class:`tencentcloud.omics.v20221128.models.ClusterOption`
        :param DatabaseOption: 数据库配置。
        :type DatabaseOption: :class:`tencentcloud.omics.v20221128.models.DatabaseOption`
        :param StorageOption: 存储配置。
        :type StorageOption: :class:`tencentcloud.omics.v20221128.models.StorageOption`
        :param CVMOption: 云服务器配置。
        :type CVMOption: :class:`tencentcloud.omics.v20221128.models.CVMOption`
        """
        self.VPCOption = None
        self.ClusterOption = None
        self.DatabaseOption = None
        self.StorageOption = None
        self.CVMOption = None


    def _deserialize(self, params):
        if params.get("VPCOption") is not None:
            self.VPCOption = VPCOption()
            self.VPCOption._deserialize(params.get("VPCOption"))
        if params.get("ClusterOption") is not None:
            self.ClusterOption = ClusterOption()
            self.ClusterOption._deserialize(params.get("ClusterOption"))
        if params.get("DatabaseOption") is not None:
            self.DatabaseOption = DatabaseOption()
            self.DatabaseOption._deserialize(params.get("DatabaseOption"))
        if params.get("StorageOption") is not None:
            self.StorageOption = StorageOption()
            self.StorageOption._deserialize(params.get("StorageOption"))
        if params.get("CVMOption") is not None:
            self.CVMOption = CVMOption()
            self.CVMOption._deserialize(params.get("CVMOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecutionTime(AbstractModel):
    """执行时间。

    """

    def __init__(self):
        r"""
        :param SubmitTime: 提交时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitTime: str
        :param StartTime: 开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.SubmitTime = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SubmitTime = params.get("SubmitTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。

    - 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。

    - 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段。
        :type Name: str
        :param Values: 过滤字段值。
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
        


class GetRunCallsRequest(AbstractModel):
    """GetRunCalls请求参数结构体

    """

    def __init__(self):
        r"""
        :param RunUuid: 任务Uuid。
        :type RunUuid: str
        :param ProjectId: 项目ID。
        :type ProjectId: str
        :param Path: 作业路径
        :type Path: str
        """
        self.RunUuid = None
        self.ProjectId = None
        self.Path = None


    def _deserialize(self, params):
        self.RunUuid = params.get("RunUuid")
        self.ProjectId = params.get("ProjectId")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunCallsResponse(AbstractModel):
    """GetRunCalls返回参数结构体

    """

    def __init__(self):
        r"""
        :param Calls: 作业详情。
        :type Calls: list of RunMetadata
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Calls = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Calls") is not None:
            self.Calls = []
            for item in params.get("Calls"):
                obj = RunMetadata()
                obj._deserialize(item)
                self.Calls.append(obj)
        self.RequestId = params.get("RequestId")


class GetRunStatusRequest(AbstractModel):
    """GetRunStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RunUuid: 任务Uuid。
        :type RunUuid: str
        :param ProjectId: 项目ID。
        :type ProjectId: str
        """
        self.RunUuid = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RunUuid = params.get("RunUuid")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunStatusResponse(AbstractModel):
    """GetRunStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Metadata: 作业详情。
        :type Metadata: :class:`tencentcloud.omics.v20221128.models.RunMetadata`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Metadata = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Metadata") is not None:
            self.Metadata = RunMetadata()
            self.Metadata._deserialize(params.get("Metadata"))
        self.RequestId = params.get("RequestId")


class ImportTableFileRequest(AbstractModel):
    """ImportTableFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 表格关联的项目ID。
        :type ProjectId: str
        :param Name: 表格名称，支持20个字符内的英文字符、数字和下划线。
        :type Name: str
        :param CosUri: 表格文件Cos对象路径。
        :type CosUri: str
        :param DataType: 表格文件中每列的数据类型，支持的类型包括：Int、String、File、Array[File]
        :type DataType: list of str
        :param Description: 表格描述。
        :type Description: str
        """
        self.ProjectId = None
        self.Name = None
        self.CosUri = None
        self.DataType = None
        self.Description = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.CosUri = params.get("CosUri")
        self.DataType = params.get("DataType")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportTableFileResponse(AbstractModel):
    """ImportTableFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param TableId: 表格ID。
        :type TableId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TableId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TableId = params.get("TableId")
        self.RequestId = params.get("RequestId")


class ResourceIds(AbstractModel):
    """云资源ID。

    """

    def __init__(self):
        r"""
        :param VPCId: 私有网络ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VPCId: str
        :param SubnetId: 子网ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param SecurityGroupId: 安全组ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupId: str
        :param TDSQLCId: TDSQL-C Mysql版数据库ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TDSQLCId: str
        :param CFSId: 文件存储ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CFSId: str
        :param CFSStorageType: 文件存储类型：取值范围：
- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
注意：此字段可能返回 null，表示取不到有效值。
        :type CFSStorageType: str
        :param CVMId: 云服务器ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CVMId: str
        :param EKSId: 弹性容器集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSId: str
        """
        self.VPCId = None
        self.SubnetId = None
        self.SecurityGroupId = None
        self.TDSQLCId = None
        self.CFSId = None
        self.CFSStorageType = None
        self.CVMId = None
        self.EKSId = None


    def _deserialize(self, params):
        self.VPCId = params.get("VPCId")
        self.SubnetId = params.get("SubnetId")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.TDSQLCId = params.get("TDSQLCId")
        self.CFSId = params.get("CFSId")
        self.CFSStorageType = params.get("CFSStorageType")
        self.CVMId = params.get("CVMId")
        self.EKSId = params.get("EKSId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRunsRequest(AbstractModel):
    """RetryRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 关联项目ID。
        :type ProjectId: str
        :param RunUuids: 任务UUID。
        :type RunUuids: list of str
        """
        self.ProjectId = None
        self.RunUuids = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RunUuids = params.get("RunUuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRunsResponse(AbstractModel):
    """RetryRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Run(AbstractModel):
    """任务。

    """

    def __init__(self):
        r"""
        :param RunUuid: 任务UUID。
        :type RunUuid: str
        :param ProjectId: 项目ID。
        :type ProjectId: str
        :param ApplicationId: 应用ID。
        :type ApplicationId: str
        :param RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param UserDefinedId: 用户定义ID，单例运行为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefinedId: str
        :param TableId: 表格ID，单例运行为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param TableRowUuid: 表格行UUID，单例运行为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableRowUuid: str
        :param Status: 任务状态。
        :type Status: str
        :param Input: 任务输入。
        :type Input: str
        :param Option: 运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param ExecutionTime: 执行时间。
        :type ExecutionTime: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        :param ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self.RunUuid = None
        self.ProjectId = None
        self.ApplicationId = None
        self.RunGroupId = None
        self.EnvironmentId = None
        self.UserDefinedId = None
        self.TableId = None
        self.TableRowUuid = None
        self.Status = None
        self.Input = None
        self.Option = None
        self.ExecutionTime = None
        self.ErrorMessage = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RunUuid = params.get("RunUuid")
        self.ProjectId = params.get("ProjectId")
        self.ApplicationId = params.get("ApplicationId")
        self.RunGroupId = params.get("RunGroupId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.UserDefinedId = params.get("UserDefinedId")
        self.TableId = params.get("TableId")
        self.TableRowUuid = params.get("TableRowUuid")
        self.Status = params.get("Status")
        self.Input = params.get("Input")
        if params.get("Option") is not None:
            self.Option = RunOption()
            self.Option._deserialize(params.get("Option"))
        if params.get("ExecutionTime") is not None:
            self.ExecutionTime = ExecutionTime()
            self.ExecutionTime._deserialize(params.get("ExecutionTime"))
        self.ErrorMessage = params.get("ErrorMessage")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunApplicationRequest(AbstractModel):
    """RunApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID。
        :type ApplicationId: str
        :param ProjectId: 项目ID。
        :type ProjectId: str
        :param Name: 任务批次名称。
        :type Name: str
        :param EnvironmentId: 投递环境ID。
        :type EnvironmentId: str
        :param InputBase64: 任务输入JSON。需要进行base64编码。
        :type InputBase64: str
        :param CacheClearDelay: 任务缓存清理时间。不填表示不清理。
        :type CacheClearDelay: int
        :param Option: 运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param Description: 任务批次描述。
        :type Description: str
        :param TableId: 批量投递表格ID，不填表示单例投递。
        :type TableId: str
        :param TableRowUuids: 批量投递表格行UUID。不填表示表格全部行。
        :type TableRowUuids: list of str
        """
        self.ApplicationId = None
        self.ProjectId = None
        self.Name = None
        self.EnvironmentId = None
        self.InputBase64 = None
        self.CacheClearDelay = None
        self.Option = None
        self.Description = None
        self.TableId = None
        self.TableRowUuids = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.EnvironmentId = params.get("EnvironmentId")
        self.InputBase64 = params.get("InputBase64")
        self.CacheClearDelay = params.get("CacheClearDelay")
        if params.get("Option") is not None:
            self.Option = RunOption()
            self.Option._deserialize(params.get("Option"))
        self.Description = params.get("Description")
        self.TableId = params.get("TableId")
        self.TableRowUuids = params.get("TableRowUuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunApplicationResponse(AbstractModel):
    """RunApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RunGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RunGroupId = params.get("RunGroupId")
        self.RequestId = params.get("RequestId")


class RunGroup(AbstractModel):
    """任务。

    """

    def __init__(self):
        r"""
        :param RunGroupId: 任务批次ID。
        :type RunGroupId: str
        :param ProjectId: 项目ID。
        :type ProjectId: str
        :param ProjectName: 项目名称。
        :type ProjectName: str
        :param ApplicationId: 应用ID。
        :type ApplicationId: str
        :param ApplicationName: 应用名称。
        :type ApplicationName: str
        :param ApplicationType: 应用类型。
        :type ApplicationType: str
        :param EnvironmentId: 环境ID。
        :type EnvironmentId: str
        :param EnvironmentName: 环境名称。
        :type EnvironmentName: str
        :param TableId: 表格ID，单例运行为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param Name: 任务名称。
        :type Name: str
        :param Description: 任务描述。
        :type Description: str
        :param Status: 任务状态。
        :type Status: str
        :param Input: 任务输入。
        :type Input: str
        :param Option: 运行选项。
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param TotalRun: 任务总数量。
        :type TotalRun: int
        :param RunStatusCounts: 各状态任务的数量。
        :type RunStatusCounts: list of RunStatusCount
        :param ExecutionTime: 执行时间。
        :type ExecutionTime: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        :param ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self.RunGroupId = None
        self.ProjectId = None
        self.ProjectName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.EnvironmentId = None
        self.EnvironmentName = None
        self.TableId = None
        self.Name = None
        self.Description = None
        self.Status = None
        self.Input = None
        self.Option = None
        self.TotalRun = None
        self.RunStatusCounts = None
        self.ExecutionTime = None
        self.ErrorMessage = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RunGroupId = params.get("RunGroupId")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.EnvironmentId = params.get("EnvironmentId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.TableId = params.get("TableId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.Input = params.get("Input")
        if params.get("Option") is not None:
            self.Option = RunOption()
            self.Option._deserialize(params.get("Option"))
        self.TotalRun = params.get("TotalRun")
        if params.get("RunStatusCounts") is not None:
            self.RunStatusCounts = []
            for item in params.get("RunStatusCounts"):
                obj = RunStatusCount()
                obj._deserialize(item)
                self.RunStatusCounts.append(obj)
        if params.get("ExecutionTime") is not None:
            self.ExecutionTime = ExecutionTime()
            self.ExecutionTime._deserialize(params.get("ExecutionTime"))
        self.ErrorMessage = params.get("ErrorMessage")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMetadata(AbstractModel):
    """任务作业详情。

    """

    def __init__(self):
        r"""
        :param RunType: 任务类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type RunType: str
        :param RunId: 任务ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RunId: str
        :param ParentId: 父层ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param JobId: 作业ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param CallName: 作业名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CallName: str
        :param ScatterIndex: Scatter索引。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScatterIndex: str
        :param Input: 输入。
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: str
        :param Output: 输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ErrorMessage: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param SubmitTime: 提交时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitTime: str
        :param EndTime: 结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Command: 命令行。
注意：此字段可能返回 null，表示取不到有效值。
        :type Command: str
        :param Runtime: 运行时。
注意：此字段可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param Preprocess: 预处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type Preprocess: bool
        :param PostProcess: 后处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostProcess: bool
        :param CallCached: Cache命中
注意：此字段可能返回 null，表示取不到有效值。
        :type CallCached: bool
        :param Stdout: 标准输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Stdout: str
        :param Stderr: 错误输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Stderr: str
        """
        self.RunType = None
        self.RunId = None
        self.ParentId = None
        self.JobId = None
        self.CallName = None
        self.ScatterIndex = None
        self.Input = None
        self.Output = None
        self.Status = None
        self.ErrorMessage = None
        self.StartTime = None
        self.SubmitTime = None
        self.EndTime = None
        self.Command = None
        self.Runtime = None
        self.Preprocess = None
        self.PostProcess = None
        self.CallCached = None
        self.Stdout = None
        self.Stderr = None


    def _deserialize(self, params):
        self.RunType = params.get("RunType")
        self.RunId = params.get("RunId")
        self.ParentId = params.get("ParentId")
        self.JobId = params.get("JobId")
        self.CallName = params.get("CallName")
        self.ScatterIndex = params.get("ScatterIndex")
        self.Input = params.get("Input")
        self.Output = params.get("Output")
        self.Status = params.get("Status")
        self.ErrorMessage = params.get("ErrorMessage")
        self.StartTime = params.get("StartTime")
        self.SubmitTime = params.get("SubmitTime")
        self.EndTime = params.get("EndTime")
        self.Command = params.get("Command")
        self.Runtime = params.get("Runtime")
        self.Preprocess = params.get("Preprocess")
        self.PostProcess = params.get("PostProcess")
        self.CallCached = params.get("CallCached")
        self.Stdout = params.get("Stdout")
        self.Stderr = params.get("Stderr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunOption(AbstractModel):
    """运行应用选项。

    """

    def __init__(self):
        r"""
        :param FailureMode: 运行失败模式，取值范围：
- ContinueWhilePossible
- NoNewCalls
        :type FailureMode: str
        :param UseCallCache: 是否使用Call-Caching功能。
        :type UseCallCache: bool
        :param UseErrorOnHold: 是否使用错误挂起功能。
        :type UseErrorOnHold: bool
        :param FinalWorkflowOutputsDir: 输出归档COS路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalWorkflowOutputsDir: str
        :param UseRelativeOutputPaths: 是否使用相对目录归档输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type UseRelativeOutputPaths: bool
        """
        self.FailureMode = None
        self.UseCallCache = None
        self.UseErrorOnHold = None
        self.FinalWorkflowOutputsDir = None
        self.UseRelativeOutputPaths = None


    def _deserialize(self, params):
        self.FailureMode = params.get("FailureMode")
        self.UseCallCache = params.get("UseCallCache")
        self.UseErrorOnHold = params.get("UseErrorOnHold")
        self.FinalWorkflowOutputsDir = params.get("FinalWorkflowOutputsDir")
        self.UseRelativeOutputPaths = params.get("UseRelativeOutputPaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunStatusCount(AbstractModel):
    """任务运行状态。

    """

    def __init__(self):
        r"""
        :param Status: 状态。
        :type Status: str
        :param Count: 数量。
        :type Count: int
        """
        self.Status = None
        self.Count = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOption(AbstractModel):
    """文件存储配置。

    """

    def __init__(self):
        r"""
        :param StorageType: 文件存储类型，取值范围：
- SD：通用标准型
- HP：通用性能型
- TB：turbo标准型
- TP：turbo性能型
        :type StorageType: str
        :param Zone: 文件存储可用区。
        :type Zone: str
        :param Capacity: 文件系统容量，turbo系列必填，单位为GiB。 
- turbo标准型起售40TiB，即40960GiB；扩容步长20TiB，即20480 GiB。
- turbo性能型起售20TiB，即20480 GiB；扩容步长10TiB，即10240 GiB。
        :type Capacity: int
        """
        self.StorageType = None
        self.Zone = None
        self.Capacity = None


    def _deserialize(self, params):
        self.StorageType = params.get("StorageType")
        self.Zone = params.get("Zone")
        self.Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """表格。

    """

    def __init__(self):
        r"""
        :param TableId: 表格ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TableId: str
        :param ProjectId: 关联项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param Name: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 表格描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Columns: 表格列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of TableColumn
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Creator: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        """
        self.TableId = None
        self.ProjectId = None
        self.Name = None
        self.Description = None
        self.Columns = None
        self.CreateTime = None
        self.Creator = None


    def _deserialize(self, params):
        self.TableId = params.get("TableId")
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = TableColumn()
                obj._deserialize(item)
                self.Columns.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.Creator = params.get("Creator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumn(AbstractModel):
    """表格列。

    """

    def __init__(self):
        r"""
        :param Header: 列名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Header: str
        :param DataType: 列数据类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DataType: str
        """
        self.Header = None
        self.DataType = None


    def _deserialize(self, params):
        self.Header = params.get("Header")
        self.DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableRow(AbstractModel):
    """表格行。

    """

    def __init__(self):
        r"""
        :param TableRowUuid: 表格行UUID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableRowUuid: str
        :param Content: 表格行内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of str
        """
        self.TableRowUuid = None
        self.Content = None


    def _deserialize(self, params):
        self.TableRowUuid = params.get("TableRowUuid")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VPCOption(AbstractModel):
    """私有网络配置。

    """

    def __init__(self):
        r"""
        :param SubnetZone: 子网可用区。
        :type SubnetZone: str
        :param VPCCIDRBlock: 私有网络CIDR。
        :type VPCCIDRBlock: str
        :param SubnetCIDRBlock: 子网CIDR。
        :type SubnetCIDRBlock: str
        """
        self.SubnetZone = None
        self.VPCCIDRBlock = None
        self.SubnetCIDRBlock = None


    def _deserialize(self, params):
        self.SubnetZone = params.get("SubnetZone")
        self.VPCCIDRBlock = params.get("VPCCIDRBlock")
        self.SubnetCIDRBlock = params.get("SubnetCIDRBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        