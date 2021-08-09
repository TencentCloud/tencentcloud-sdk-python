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


class AddUsersToWorkGroupRequest(AbstractModel):
    """AddUsersToWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AddInfo: 要操作的工作组和用户信息\n        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.UserIdSetOfWorkGroupId`\n        """
        self.AddInfo = None


    def _deserialize(self, params):
        if params.get("AddInfo") is not None:
            self.AddInfo = UserIdSetOfWorkGroupId()
            self.AddInfo._deserialize(params.get("AddInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUsersToWorkGroupResponse(AbstractModel):
    """AddUsersToWorkGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户Id，和子用户uin相同，需要先使用CreateUser接口创建用户。可以使用DescribeUsers接口查看。\n        :type UserId: str\n        :param PolicySet: 鉴权策略集合\n        :type PolicySet: list of Policy\n        """
        self.UserId = None
        self.PolicySet = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachWorkGroupPolicyRequest(AbstractModel):
    """AttachWorkGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id\n        :type WorkGroupId: int\n        :param PolicySet: 要绑定的策略集合\n        :type PolicySet: list of Policy\n        """
        self.WorkGroupId = None
        self.PolicySet = None


    def _deserialize(self, params):
        self.WorkGroupId = params.get("WorkGroupId")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachWorkGroupPolicyResponse(AbstractModel):
    """AttachWorkGroupPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindWorkGroupsToUserRequest(AbstractModel):
    """BindWorkGroupsToUser请求参数结构体

    """

    def __init__(self):
        """
        :param AddInfo: 绑定的用户和工作组信息\n        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.WorkGroupIdSetOfUserId`\n        """
        self.AddInfo = None


    def _deserialize(self, params):
        if params.get("AddInfo") is not None:
            self.AddInfo = WorkGroupIdSetOfUserId()
            self.AddInfo._deserialize(params.get("AddInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindWorkGroupsToUserResponse(AbstractModel):
    """BindWorkGroupsToUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CSV(AbstractModel):
    """CSV类型数据格式

    """

    def __init__(self):
        """
        :param CodeCompress: 压缩格式，["Snappy", "Gzip", "None"选一]。\n        :type CodeCompress: str\n        :param CSVSerde: CSV序列化及反序列化数据结构。\n        :type CSVSerde: :class:`tencentcloud.dlc.v20210125.models.CSVSerde`\n        :param HeadLines: 标题行，默认为0。
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeadLines: int\n        :param Format: 格式，默认值为CSV
注意：此字段可能返回 null，表示取不到有效值。\n        :type Format: str\n        """
        self.CodeCompress = None
        self.CSVSerde = None
        self.HeadLines = None
        self.Format = None


    def _deserialize(self, params):
        self.CodeCompress = params.get("CodeCompress")
        if params.get("CSVSerde") is not None:
            self.CSVSerde = CSVSerde()
            self.CSVSerde._deserialize(params.get("CSVSerde"))
        self.HeadLines = params.get("HeadLines")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CSVSerde(AbstractModel):
    """CSV序列化及反序列化数据结构

    """

    def __init__(self):
        """
        :param Escape: CSV序列化转义符，默认为"\\"，最长8个字符，如 Escape: "/\"\n        :type Escape: str\n        :param Quote: CSV序列化字段域符，默认为"'"，最长8个字符, 如 Quote: "\""\n        :type Quote: str\n        :param Separator: CSV序列化分隔符，默认为"\t"，最长8个字符, 如 Separator: "\t"\n        :type Separator: str\n        """
        self.Escape = None
        self.Quote = None
        self.Separator = None


    def _deserialize(self, params):
        self.Escape = params.get("Escape")
        self.Quote = params.get("Quote")
        self.Separator = params.get("Separator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务Id，全局唯一\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Column(AbstractModel):
    """数据表列信息。

    """

    def __init__(self):
        """
        :param Name: 列名称，不区分大小写，最大支持25个字符。\n        :type Name: str\n        :param Type: 列类型，支持如下类型定义:
string|tinyint|smallint|int|bigint|boolean|float|double|decimal|timestamp|date|binary|array<data_type>|map<primitive_type, data_type>|struct<col_name : data_type [COMMENT col_comment], ...>|uniontype<data_type, data_type, ...>。\n        :type Type: str\n        :param Comment: 对该类的注释。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Comment: str\n        """
        self.Name = None
        self.Type = None
        self.Comment = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatabaseRequest(AbstractModel):
    """CreateDatabase请求参数结构体

    """

    def __init__(self):
        """
        :param DatabaseInfo: 数据库基础信息\n        :type DatabaseInfo: :class:`tencentcloud.dlc.v20210125.models.DatabaseInfo`\n        :param DatasourceConnectionName: 数据源名称，默认为CosDataCatalog\n        :type DatasourceConnectionName: str\n        """
        self.DatabaseInfo = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        if params.get("DatabaseInfo") is not None:
            self.DatabaseInfo = DatabaseInfo()
            self.DatabaseInfo._deserialize(params.get("DatabaseInfo"))
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatabaseResponse(AbstractModel):
    """CreateDatabase返回参数结构体

    """

    def __init__(self):
        """
        :param Execution: 生成的建库执行语句对象。\n        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Execution = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Execution") is not None:
            self.Execution = Execution()
            self.Execution._deserialize(params.get("Execution"))
        self.RequestId = params.get("RequestId")


class CreateScriptRequest(AbstractModel):
    """CreateScript请求参数结构体

    """

    def __init__(self):
        """
        :param ScriptName: 脚本名称，最大不能超过255个字符。\n        :type ScriptName: str\n        :param SQLStatement: base64编码后的sql语句\n        :type SQLStatement: str\n        :param ScriptDesc: 脚本描述， 不能超过50个字符\n        :type ScriptDesc: str\n        :param DatabaseName: 数据库名称\n        :type DatabaseName: str\n        """
        self.ScriptName = None
        self.SQLStatement = None
        self.ScriptDesc = None
        self.DatabaseName = None


    def _deserialize(self, params):
        self.ScriptName = params.get("ScriptName")
        self.SQLStatement = params.get("SQLStatement")
        self.ScriptDesc = params.get("ScriptDesc")
        self.DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScriptResponse(AbstractModel):
    """CreateScript返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateStoreLocationRequest(AbstractModel):
    """CreateStoreLocation请求参数结构体

    """

    def __init__(self):
        """
        :param StoreLocation: 计算结果存储cos路径，如：cosn://bucketname/\n        :type StoreLocation: str\n        """
        self.StoreLocation = None


    def _deserialize(self, params):
        self.StoreLocation = params.get("StoreLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStoreLocationResponse(AbstractModel):
    """CreateStoreLocation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTableRequest(AbstractModel):
    """CreateTable请求参数结构体

    """

    def __init__(self):
        """
        :param TableInfo: 数据表配置信息\n        :type TableInfo: :class:`tencentcloud.dlc.v20210125.models.TableInfo`\n        """
        self.TableInfo = None


    def _deserialize(self, params):
        if params.get("TableInfo") is not None:
            self.TableInfo = TableInfo()
            self.TableInfo._deserialize(params.get("TableInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableResponse(AbstractModel):
    """CreateTable返回参数结构体

    """

    def __init__(self):
        """
        :param Execution: 生成的建表执行语句对象。\n        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Execution = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Execution") is not None:
            self.Execution = Execution()
            self.Execution._deserialize(params.get("Execution"))
        self.RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        """
        :param Task: 计算任务，该参数中包含任务类型及其相关配置信息\n        :type Task: :class:`tencentcloud.dlc.v20210125.models.Task`\n        :param DatabaseName: 数据库名称。任务在执行前均会USE该数据库， 除了首次建库时，其他情况建议均添加上。\n        :type DatabaseName: str\n        :param DatasourceConnectionName: 默认数据源名称。\n        :type DatasourceConnectionName: str\n        """
        self.Task = None
        self.DatabaseName = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self.Task = Task()
            self.Task._deserialize(params.get("Task"))
        self.DatabaseName = params.get("DatabaseName")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateTasksInOrderRequest(AbstractModel):
    """CreateTasksInOrder请求参数结构体

    """

    def __init__(self):
        """
        :param DatabaseName: 数据库名称。如果SQL语句中有数据库名称，优先使用SQL语句中的数据库，否则使用该参数指定的数据库。\n        :type DatabaseName: str\n        :param Tasks: SQL任务信息\n        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TasksInfo`\n        :param DatasourceConnectionName: 数据源名称，默认为COSDataCatalog\n        :type DatasourceConnectionName: str\n        """
        self.DatabaseName = None
        self.Tasks = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        if params.get("Tasks") is not None:
            self.Tasks = TasksInfo()
            self.Tasks._deserialize(params.get("Tasks"))
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTasksInOrderResponse(AbstractModel):
    """CreateTasksInOrder返回参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 本批次提交的任务的批次Id\n        :type BatchId: str\n        :param TaskIdSet: 任务Id集合，按照执行顺序排列\n        :type TaskIdSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BatchId = None
        self.TaskIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.TaskIdSet = params.get("TaskIdSet")
        self.RequestId = params.get("RequestId")


class CreateTasksRequest(AbstractModel):
    """CreateTasks请求参数结构体

    """

    def __init__(self):
        """
        :param DatabaseName: 数据库名称。如果SQL语句中有数据库名称，优先使用SQL语句中的数据库，否则使用该参数指定的数据库。\n        :type DatabaseName: str\n        :param Tasks: SQL任务信息\n        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TasksInfo`\n        :param DatasourceConnectionName: 数据源名称，默认为COSDataCatalog\n        :type DatasourceConnectionName: str\n        """
        self.DatabaseName = None
        self.Tasks = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        if params.get("Tasks") is not None:
            self.Tasks = TasksInfo()
            self.Tasks._deserialize(params.get("Tasks"))
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTasksResponse(AbstractModel):
    """CreateTasks返回参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 本批次提交的任务的批次Id\n        :type BatchId: str\n        :param TaskIdSet: 任务Id集合，按照执行顺序排列\n        :type TaskIdSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BatchId = None
        self.TaskIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.TaskIdSet = params.get("TaskIdSet")
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 需要授权的子用户uin，可以通过腾讯云控制台右上角 → “账号信息” → “账号ID进行查看”。\n        :type UserId: str\n        :param UserDescription: 用户描述信息，方便区分不同用户\n        :type UserDescription: str\n        :param PolicySet: 绑定到用户的权限集合\n        :type PolicySet: list of Policy\n        """
        self.UserId = None
        self.UserDescription = None
        self.PolicySet = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserDescription = params.get("UserDescription")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWorkGroupRequest(AbstractModel):
    """CreateWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupName: 工作组名称\n        :type WorkGroupName: str\n        :param WorkGroupDescription: 工作组描述\n        :type WorkGroupDescription: str\n        :param PolicySet: 工作组绑定的鉴权策略集合\n        :type PolicySet: list of Policy\n        """
        self.WorkGroupName = None
        self.WorkGroupDescription = None
        self.PolicySet = None


    def _deserialize(self, params):
        self.WorkGroupName = params.get("WorkGroupName")
        self.WorkGroupDescription = params.get("WorkGroupDescription")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkGroupResponse(AbstractModel):
    """CreateWorkGroup返回参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id，全局唯一\n        :type WorkGroupId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.WorkGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkGroupId = params.get("WorkGroupId")
        self.RequestId = params.get("RequestId")


class DataFormat(AbstractModel):
    """数据表数据格式。

    """

    def __init__(self):
        """
        :param TextFile: 文本格式，TextFile。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TextFile: :class:`tencentcloud.dlc.v20210125.models.TextFile`\n        :param CSV: 文本格式，CSV。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CSV: :class:`tencentcloud.dlc.v20210125.models.CSV`\n        :param Json: 文本格式，Json。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Json: :class:`tencentcloud.dlc.v20210125.models.Other`\n        :param Parquet: Parquet格式
注意：此字段可能返回 null，表示取不到有效值。\n        :type Parquet: :class:`tencentcloud.dlc.v20210125.models.Other`\n        :param ORC: ORC格式
注意：此字段可能返回 null，表示取不到有效值。\n        :type ORC: :class:`tencentcloud.dlc.v20210125.models.Other`\n        :param AVRO: AVRO格式
注意：此字段可能返回 null，表示取不到有效值。\n        :type AVRO: :class:`tencentcloud.dlc.v20210125.models.Other`\n        """
        self.TextFile = None
        self.CSV = None
        self.Json = None
        self.Parquet = None
        self.ORC = None
        self.AVRO = None


    def _deserialize(self, params):
        if params.get("TextFile") is not None:
            self.TextFile = TextFile()
            self.TextFile._deserialize(params.get("TextFile"))
        if params.get("CSV") is not None:
            self.CSV = CSV()
            self.CSV._deserialize(params.get("CSV"))
        if params.get("Json") is not None:
            self.Json = Other()
            self.Json._deserialize(params.get("Json"))
        if params.get("Parquet") is not None:
            self.Parquet = Other()
            self.Parquet._deserialize(params.get("Parquet"))
        if params.get("ORC") is not None:
            self.ORC = Other()
            self.ORC._deserialize(params.get("ORC"))
        if params.get("AVRO") is not None:
            self.AVRO = Other()
            self.AVRO._deserialize(params.get("AVRO"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseInfo(AbstractModel):
    """数据库对象

    """

    def __init__(self):
        """
        :param DatabaseName: 数据库名称。\n        :type DatabaseName: str\n        :param Comment: 数据库描述信息，长度 0~256。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Comment: str\n        :param Properties: 数据库属性列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Properties: list of Property\n        """
        self.DatabaseName = None
        self.Comment = None
        self.Properties = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.Comment = params.get("Comment")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseResponseInfo(AbstractModel):
    """数据库对象

    """

    def __init__(self):
        """
        :param DatabaseName: 数据库名称。\n        :type DatabaseName: str\n        :param Comment: 数据库描述信息，长度 0~256。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Comment: str\n        :param Properties: 数据库属性列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Properties: list of Property\n        :param CreateTime: 数据库创建时间戳，单位：s。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param ModifiedTime: 数据库更新时间戳，单位：s。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        """
        self.DatabaseName = None
        self.Comment = None
        self.Properties = None
        self.CreateTime = None
        self.ModifiedTime = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.Comment = params.get("Comment")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScriptRequest(AbstractModel):
    """DeleteScript请求参数结构体

    """

    def __init__(self):
        """
        :param ScriptIds: 脚本id，其可以通过DescribeScripts接口提取\n        :type ScriptIds: list of str\n        """
        self.ScriptIds = None


    def _deserialize(self, params):
        self.ScriptIds = params.get("ScriptIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScriptResponse(AbstractModel):
    """DeleteScript返回参数结构体

    """

    def __init__(self):
        """
        :param ScriptsAffected: 删除的脚本数量\n        :type ScriptsAffected: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ScriptsAffected = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScriptsAffected = params.get("ScriptsAffected")
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserIds: 需要删除的用户的Id\n        :type UserIds: list of str\n        """
        self.UserIds = None


    def _deserialize(self, params):
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsersFromWorkGroupRequest(AbstractModel):
    """DeleteUsersFromWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AddInfo: 要删除的用户信息\n        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.UserIdSetOfWorkGroupId`\n        """
        self.AddInfo = None


    def _deserialize(self, params):
        if params.get("AddInfo") is not None:
            self.AddInfo = UserIdSetOfWorkGroupId()
            self.AddInfo._deserialize(params.get("AddInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersFromWorkGroupResponse(AbstractModel):
    """DeleteUsersFromWorkGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWorkGroupRequest(AbstractModel):
    """DeleteWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupIds: 要删除的工作组Id集合\n        :type WorkGroupIds: list of int\n        """
        self.WorkGroupIds = None


    def _deserialize(self, params):
        self.WorkGroupIds = params.get("WorkGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkGroupResponse(AbstractModel):
    """DeleteWorkGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。\n        :type Limit: int\n        :param Offset: 数据偏移量，从0开始，默认为0。\n        :type Offset: int\n        :param KeyWord: 模糊匹配，库名关键字。\n        :type KeyWord: str\n        :param DatasourceConnectionName: 数据源唯名称，该名称可以通过DescribeDatasourceConnection接口查询到。默认为CosDataCatalog\n        :type DatasourceConnectionName: str\n        """
        self.Limit = None
        self.Offset = None
        self.KeyWord = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.KeyWord = params.get("KeyWord")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        """
        :param DatabaseList: 数据库对象列表。\n        :type DatabaseList: list of DatabaseResponseInfo\n        :param TotalCount: 实例总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DatabaseList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DatabaseList") is not None:
            self.DatabaseList = []
            for item in params.get("DatabaseList"):
                obj = DatabaseResponseInfo()
                obj._deserialize(item)
                self.DatabaseList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeScriptsRequest(AbstractModel):
    """DescribeScripts请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param SortBy: 按字段排序，支持如下字段类型，update-time\n        :type SortBy: str\n        :param Sorting: 排序方式，desc表示正序，asc表示反序\n        :type Sorting: str\n        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
script-id - String - （过滤条件）script-id取值形如：157de0d1-26b4-4df2-a2d0-b64afc406c25。
script-name-keyword - String - （过滤条件）数据表名称,形如：script-test。\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.SortBy = None
        self.Sorting = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SortBy = params.get("SortBy")
        self.Sorting = params.get("Sorting")
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
        


class DescribeScriptsResponse(AbstractModel):
    """DescribeScripts返回参数结构体

    """

    def __init__(self):
        """
        :param Scripts: Script列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Scripts: list of Script\n        :param TotalCount: 实例总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Scripts = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Scripts") is not None:
            self.Scripts = []
            for item in params.get("Scripts"):
                obj = Script()
                obj._deserialize(item)
                self.Scripts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeStoreLocationRequest(AbstractModel):
    """DescribeStoreLocation请求参数结构体

    """


class DescribeStoreLocationResponse(AbstractModel):
    """DescribeStoreLocation返回参数结构体

    """

    def __init__(self):
        """
        :param StoreLocation: 返回用户设置的结果存储位置路径，如果未设置则返回空字符串：""
注意：此字段可能返回 null，表示取不到有效值。\n        :type StoreLocation: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.StoreLocation = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StoreLocation = params.get("StoreLocation")
        self.RequestId = params.get("RequestId")


class DescribeTableRequest(AbstractModel):
    """DescribeTable请求参数结构体

    """

    def __init__(self):
        """
        :param TableName: 查询对象表名称\n        :type TableName: str\n        :param DatabaseName: 查询表所在的数据库名称。\n        :type DatabaseName: str\n        :param DatasourceConnectionName: 查询表所在的数据源名称\n        :type DatasourceConnectionName: str\n        """
        self.TableName = None
        self.DatabaseName = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.DatabaseName = params.get("DatabaseName")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableResponse(AbstractModel):
    """DescribeTable返回参数结构体

    """

    def __init__(self):
        """
        :param Table: 数据表对象\n        :type Table: :class:`tencentcloud.dlc.v20210125.models.TableResponseInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Table = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Table") is not None:
            self.Table = TableResponseInfo()
            self.Table._deserialize(params.get("Table"))
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        """
        :param DatabaseName: 列出该数据库下所属数据表。\n        :type DatabaseName: str\n        :param Limit: 返回数量，默认为10，最大值为100。\n        :type Limit: int\n        :param Offset: 数据偏移量，从0开始，默认为0。\n        :type Offset: int\n        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
table-name - String - （过滤条件）数据表名称,形如：table-001。
table-id - String - （过滤条件）table id形如：12342。\n        :type Filters: list of Filter\n        :param DatasourceConnectionName: 指定查询的数据源名称，默认为CosDataCatalog\n        :type DatasourceConnectionName: str\n        """
        self.DatabaseName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
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
        """
        :param TableList: 数据表对象列表。\n        :type TableList: list of TableResponseInfo\n        :param TotalCount: 实例总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TableList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TableList") is not None:
            self.TableList = []
            for item in params.get("TableList"):
                obj = TableResponseInfo()
                obj._deserialize(item)
                self.TableList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为以下其中一个,每个过滤参数支持的过滤值不超过5个。
task-id - String - （任务ID过滤）task-id取值形如：e386471f-139a-4e59-877f-50ece8135b99。
task-state - String - （任务状态过滤）取值范围 0(初始化)， 1(运行中)， 2(成功)， -1(失败)。
task-sql-keyword - String - （SQL语句关键字）取值形如：DROP TABLE。\n        :type Filters: list of Filter\n        :param SortBy: 排序字段，支持如下字段类型，create-time\n        :type SortBy: str\n        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc。\n        :type Sorting: str\n        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。默认为45天前的当前时刻\n        :type StartTime: str\n        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS时间跨度在(0,30天]，支持最近45天数据查询。默认为当前时刻\n        :type EndTime: str\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.SortBy = None
        self.Sorting = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortBy = params.get("SortBy")
        self.Sorting = params.get("Sorting")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskList: 任务对象列表。\n        :type TaskList: list of TaskResponseInfo\n        :param TotalCount: 实例总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskList") is not None:
            self.TaskList = []
            for item in params.get("TaskList"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self.TaskList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    """DescribeUsers请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 指定查询的子用户uin，用户需要通过CreateUser接口创建。\n        :type UserId: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认20，最大值100\n        :type Limit: int\n        :param SortBy: 排序字段，支持如下字段类型，create-time\n        :type SortBy: str\n        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc\n        :type Sorting: str\n        """
        self.UserId = None
        self.Offset = None
        self.Limit = None
        self.SortBy = None
        self.Sorting = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Sorting = params.get("Sorting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersResponse(AbstractModel):
    """DescribeUsers返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询到的用户总数\n        :type TotalCount: int\n        :param UserSet: 查询到的授权用户信息集合\n        :type UserSet: list of UserInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.UserSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserSet") is not None:
            self.UserSet = []
            for item in params.get("UserSet"):
                obj = UserInfo()
                obj._deserialize(item)
                self.UserSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeViewsRequest(AbstractModel):
    """DescribeViews请求参数结构体

    """

    def __init__(self):
        """
        :param DatabaseName: 列出该数据库下所属数据表。\n        :type DatabaseName: str\n        :param Limit: 返回数量，默认为10，最大值为100。\n        :type Limit: int\n        :param Offset: 数据偏移量，从0开始，默认为0。\n        :type Offset: int\n        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
view-name - String - （过滤条件）数据表名称,形如：view-001。
view-id - String - （过滤条件）view id形如：12342。\n        :type Filters: list of Filter\n        :param DatasourceConnectionName: 数据库所属的数据源名称\n        :type DatasourceConnectionName: str\n        """
        self.DatabaseName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeViewsResponse(AbstractModel):
    """DescribeViews返回参数结构体

    """

    def __init__(self):
        """
        :param ViewList: 视图对象列表。\n        :type ViewList: list of ViewResponseInfo\n        :param TotalCount: 实例总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ViewList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ViewList") is not None:
            self.ViewList = []
            for item in params.get("ViewList"):
                obj = ViewResponseInfo()
                obj._deserialize(item)
                self.ViewList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWorkGroupsRequest(AbstractModel):
    """DescribeWorkGroups请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupId: 查询的工作组Id，不填或填0表示不过滤。\n        :type WorkGroupId: int\n        :param Filters: 过滤条件，当前仅支持按照工作组名称进行模糊搜索。Key为workgroup-name\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认20，最大值100\n        :type Limit: int\n        :param SortBy: 排序字段，支持如下字段类型，create-time\n        :type SortBy: str\n        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc\n        :type Sorting: str\n        """
        self.WorkGroupId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.SortBy = None
        self.Sorting = None


    def _deserialize(self, params):
        self.WorkGroupId = params.get("WorkGroupId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Sorting = params.get("Sorting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkGroupsResponse(AbstractModel):
    """DescribeWorkGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 工作组总数\n        :type TotalCount: int\n        :param WorkGroupSet: 工作组信息集合\n        :type WorkGroupSet: list of WorkGroupInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.WorkGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WorkGroupSet") is not None:
            self.WorkGroupSet = []
            for item in params.get("WorkGroupSet"):
                obj = WorkGroupInfo()
                obj._deserialize(item)
                self.WorkGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户Id，和CAM侧Uin匹配\n        :type UserId: str\n        :param PolicySet: 解绑的权限集合\n        :type PolicySet: list of Policy\n        """
        self.UserId = None
        self.PolicySet = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachWorkGroupPolicyRequest(AbstractModel):
    """DetachWorkGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id\n        :type WorkGroupId: int\n        :param PolicySet: 解绑的权限集合\n        :type PolicySet: list of Policy\n        """
        self.WorkGroupId = None
        self.PolicySet = None


    def _deserialize(self, params):
        self.WorkGroupId = params.get("WorkGroupId")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachWorkGroupPolicyResponse(AbstractModel):
    """DetachWorkGroupPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Execution(AbstractModel):
    """SQL语句对象

    """

    def __init__(self):
        """
        :param SQL: 自动生成SQL语句。\n        :type SQL: str\n        """
        self.SQL = None


    def _deserialize(self, params):
        self.SQL = params.get("SQL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询列表过滤条件参数

    """

    def __init__(self):
        """
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑或（OR）关系。\n        :type Name: str\n        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。\n        :type Values: list of str\n        """
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
        


class KVPair(AbstractModel):
    """配置格式

    """

    def __init__(self):
        """
        :param Key: 配置的key值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param Value: 配置的value值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
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
        


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户Id，和CAM侧Uin匹配\n        :type UserId: str\n        :param UserDescription: 用户描述\n        :type UserDescription: str\n        """
        self.UserId = None
        self.UserDescription = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserDescription = params.get("UserDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    """ModifyUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWorkGroupRequest(AbstractModel):
    """ModifyWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id\n        :type WorkGroupId: int\n        :param WorkGroupDescription: 工作组描述\n        :type WorkGroupDescription: str\n        """
        self.WorkGroupId = None
        self.WorkGroupDescription = None


    def _deserialize(self, params):
        self.WorkGroupId = params.get("WorkGroupId")
        self.WorkGroupDescription = params.get("WorkGroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkGroupResponse(AbstractModel):
    """ModifyWorkGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Other(AbstractModel):
    """数据格式其它类型。

    """

    def __init__(self):
        """
        :param Format: 枚举类型，默认值为Json，可选值为[Json, Parquet, ORC, AVRD]之一。\n        :type Format: str\n        """
        self.Format = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partition(AbstractModel):
    """数据表分块信息。

    """

    def __init__(self):
        """
        :param Name: 分区列名。\n        :type Name: str\n        :param Type: 分区类型。\n        :type Type: str\n        :param Comment: 对分区的描述。\n        :type Comment: str\n        """
        self.Name = None
        self.Type = None
        self.Comment = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    """权限对象

    """

    def __init__(self):
        """
        :param Catalog: 需要授权的数据源名称，当前仅支持COSDataCatalog或者*\n        :type Catalog: str\n        :param Database: 需要授权的数据库名，填*代表当前Catalog下所有数据库\n        :type Database: str\n        :param Table: 需要授权的表名，填*代表当前Database下所有表\n        :type Table: str\n        :param Operation: 授权粒度，当前只支持ALL，即全部权限\n        :type Operation: str\n        """
        self.Catalog = None
        self.Database = None
        self.Table = None
        self.Operation = None


    def _deserialize(self, params):
        self.Catalog = params.get("Catalog")
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Property(AbstractModel):
    """数据库和数据表属性信息

    """

    def __init__(self):
        """
        :param Key: 属性key名称。\n        :type Key: str\n        :param Value: 属性key对应的value。\n        :type Value: str\n        """
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
        


class SQLTask(AbstractModel):
    """SQL查询任务

    """

    def __init__(self):
        """
        :param SQL: base64加密后的SQL语句\n        :type SQL: str\n        :param Config: 任务的配置信息\n        :type Config: list of KVPair\n        """
        self.SQL = None
        self.Config = None


    def _deserialize(self, params):
        self.SQL = params.get("SQL")
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = KVPair()
                obj._deserialize(item)
                self.Config.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Script(AbstractModel):
    """script实例。

    """

    def __init__(self):
        """
        :param ScriptId: 脚本Id，长度36字节。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScriptId: str\n        :param ScriptName: 脚本名称，长度0-25。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScriptName: str\n        :param ScriptDesc: 脚本描述，长度0-50。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScriptDesc: str\n        :param DatabaseName: 默认关联数据库。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DatabaseName: str\n        :param SQLStatement: SQL描述，长度0-10000。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SQLStatement: str\n        :param UpdateTime: 更新时间戳， 单位：ms。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        """
        self.ScriptId = None
        self.ScriptName = None
        self.ScriptDesc = None
        self.DatabaseName = None
        self.SQLStatement = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ScriptId = params.get("ScriptId")
        self.ScriptName = params.get("ScriptName")
        self.ScriptDesc = params.get("ScriptDesc")
        self.DatabaseName = params.get("DatabaseName")
        self.SQLStatement = params.get("SQLStatement")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableBaseInfo(AbstractModel):
    """数据表配置信息

    """

    def __init__(self):
        """
        :param DatabaseName: 该数据表所属数据库名字\n        :type DatabaseName: str\n        :param TableName: 数据表名字\n        :type TableName: str\n        :param DatasourceConnectionName: 该数据表所属数据源名字
注意：此字段可能返回 null，表示取不到有效值。\n        :type DatasourceConnectionName: str\n        """
        self.DatabaseName = None
        self.TableName = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.TableName = params.get("TableName")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfo(AbstractModel):
    """返回数据表的相关信息。

    """

    def __init__(self):
        """
        :param TableBaseInfo: 数据表配置信息。\n        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`\n        :param DataFormat: 数据表格式。每次入参可选如下其一的KV结构，[TextFile，CSV，Json, Parquet, ORC, AVRD]。\n        :type DataFormat: :class:`tencentcloud.dlc.v20210125.models.DataFormat`\n        :param Columns: 数据表列信息。\n        :type Columns: list of Column\n        :param Partitions: 数据表分块信息。\n        :type Partitions: list of Partition\n        :param Location: 数据存储路径。当前仅支持cos路径，格式如下：cosn://bucket-name/filepath。\n        :type Location: str\n        """
        self.TableBaseInfo = None
        self.DataFormat = None
        self.Columns = None
        self.Partitions = None
        self.Location = None


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self.TableBaseInfo = TableBaseInfo()
            self.TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("DataFormat") is not None:
            self.DataFormat = DataFormat()
            self.DataFormat._deserialize(params.get("DataFormat"))
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self.Columns.append(obj)
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = Partition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableResponseInfo(AbstractModel):
    """查询表信息对象

    """

    def __init__(self):
        """
        :param TableBaseInfo: 数据表基本信息。\n        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`\n        :param Columns: 数据表列信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Columns: list of Column\n        :param Partitions: 数据表分块信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partitions: list of Partition\n        :param Location: 数据存储路径。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Location: str\n        :param Properties: 数据表属性信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Properties: list of Property\n        :param ModifiedTime: 数据表更新时间, 单位: ms。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param CreateTime: 数据表创建时间,单位: ms。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param InputFormat: 数据格式。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InputFormat: str\n        """
        self.TableBaseInfo = None
        self.Columns = None
        self.Partitions = None
        self.Location = None
        self.Properties = None
        self.ModifiedTime = None
        self.CreateTime = None
        self.InputFormat = None


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self.TableBaseInfo = TableBaseInfo()
            self.TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self.Columns.append(obj)
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = Partition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.Location = params.get("Location")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        self.ModifiedTime = params.get("ModifiedTime")
        self.CreateTime = params.get("CreateTime")
        self.InputFormat = params.get("InputFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """任务类型，任务如SQL查询等。

    """

    def __init__(self):
        """
        :param SQLTask: SQL查询任务\n        :type SQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`\n        :param SparkSQLTask: Spark SQL查询任务\n        :type SparkSQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`\n        """
        self.SQLTask = None
        self.SparkSQLTask = None


    def _deserialize(self, params):
        if params.get("SQLTask") is not None:
            self.SQLTask = SQLTask()
            self.SQLTask._deserialize(params.get("SQLTask"))
        if params.get("SparkSQLTask") is not None:
            self.SparkSQLTask = SQLTask()
            self.SparkSQLTask._deserialize(params.get("SparkSQLTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResponseInfo(AbstractModel):
    """任务实例。

    """

    def __init__(self):
        """
        :param DatabaseName: 任务所属Database的名称。\n        :type DatabaseName: str\n        :param DataAmount: 任务数据量。\n        :type DataAmount: int\n        :param Id: 任务Id。\n        :type Id: str\n        :param UsedTime: 计算时长，单位： ms。\n        :type UsedTime: int\n        :param OutputPath: 任务输出路径。\n        :type OutputPath: str\n        :param CreateTime: 任务创建时间。\n        :type CreateTime: str\n        :param State: 任务状态：0 初始化， 1 执行中， 2 执行成功，-1 执行失败，-3 已取消。\n        :type State: int\n        :param SQLType: 任务SQL类型，DDL|DML等\n        :type SQLType: str\n        :param SQL: 任务SQL语句\n        :type SQL: str\n        :param ResultExpired: 结果是否过期。\n        :type ResultExpired: bool\n        :param RowAffectInfo: 数据影响统计信息。\n        :type RowAffectInfo: str\n        :param DataSet: 任务结果数据表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataSet: str\n        :param Error: 失败信息, 例如：errorMessage。该字段已废弃。\n        :type Error: str\n        :param Percentage: 任务执行进度num/100(%)\n        :type Percentage: int\n        :param OutputMessage: 任务执行输出信息。\n        :type OutputMessage: str\n        :param TaskType: 执行SQL的引擎类型\n        :type TaskType: str\n        """
        self.DatabaseName = None
        self.DataAmount = None
        self.Id = None
        self.UsedTime = None
        self.OutputPath = None
        self.CreateTime = None
        self.State = None
        self.SQLType = None
        self.SQL = None
        self.ResultExpired = None
        self.RowAffectInfo = None
        self.DataSet = None
        self.Error = None
        self.Percentage = None
        self.OutputMessage = None
        self.TaskType = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.DataAmount = params.get("DataAmount")
        self.Id = params.get("Id")
        self.UsedTime = params.get("UsedTime")
        self.OutputPath = params.get("OutputPath")
        self.CreateTime = params.get("CreateTime")
        self.State = params.get("State")
        self.SQLType = params.get("SQLType")
        self.SQL = params.get("SQL")
        self.ResultExpired = params.get("ResultExpired")
        self.RowAffectInfo = params.get("RowAffectInfo")
        self.DataSet = params.get("DataSet")
        self.Error = params.get("Error")
        self.Percentage = params.get("Percentage")
        self.OutputMessage = params.get("OutputMessage")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TasksInfo(AbstractModel):
    """批量顺序执行任务集合

    """

    def __init__(self):
        """
        :param TaskType: 任务类型，SQLTask：SQL查询任务。SparkSQLTask：Spark SQL查询任务\n        :type TaskType: str\n        :param FailureTolerance: 容错策略。Proceed：前面任务出错/取消后继续执行后面的任务。Terminate：前面的任务出错/取消之后终止后面任务的执行，后面的任务全部标记为已取消。\n        :type FailureTolerance: str\n        :param SQL: base64加密后的SQL语句，用";"号分隔每个SQL语句，一次最多提交50个任务。严格按照前后顺序执行\n        :type SQL: str\n        :param Config: 任务的配置信息，当前仅支持SparkSQLTask任务。\n        :type Config: list of KVPair\n        """
        self.TaskType = None
        self.FailureTolerance = None
        self.SQL = None
        self.Config = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.FailureTolerance = params.get("FailureTolerance")
        self.SQL = params.get("SQL")
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = KVPair()
                obj._deserialize(item)
                self.Config.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextFile(AbstractModel):
    """文本格式

    """

    def __init__(self):
        """
        :param Format: 文本类型，本参数取值为TextFile。\n        :type Format: str\n        :param Regex: 处理文本用的正则表达式。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Regex: str\n        """
        self.Format = None
        self.Regex = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        self.Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindWorkGroupsFromUserRequest(AbstractModel):
    """UnbindWorkGroupsFromUser请求参数结构体

    """

    def __init__(self):
        """
        :param AddInfo: 解绑的工作组Id和用户Id的关联关系\n        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.WorkGroupIdSetOfUserId`\n        """
        self.AddInfo = None


    def _deserialize(self, params):
        if params.get("AddInfo") is not None:
            self.AddInfo = WorkGroupIdSetOfUserId()
            self.AddInfo._deserialize(params.get("AddInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindWorkGroupsFromUserResponse(AbstractModel):
    """UnbindWorkGroupsFromUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserIdSetOfWorkGroupId(AbstractModel):
    """绑定到同一个工作组的用户Id的集合

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id\n        :type WorkGroupId: int\n        :param UserIds: 用户Id集合，和CAM侧Uin匹配\n        :type UserIds: list of str\n        """
        self.WorkGroupId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.WorkGroupId = params.get("WorkGroupId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """授权用户信息

    """

    def __init__(self):
        """
        :param UserId: 用户Id，和子用户uin相同\n        :type UserId: str\n        :param UserDescription: 用户描述信息，方便区分不同用户
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserDescription: str\n        :param PolicySet: 单独给用户绑定的权限集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type PolicySet: list of Policy\n        :param Creator: 当前用户的创建者\n        :type Creator: str\n        :param CreateTime: 创建时间，格式如2021-07-28 16:19:32\n        :type CreateTime: str\n        :param WorkGroupSet: 关联的工作组集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type WorkGroupSet: list of WorkGroupMessage\n        :param IsOwner: 是否是管理员账号
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsOwner: bool\n        """
        self.UserId = None
        self.UserDescription = None
        self.PolicySet = None
        self.Creator = None
        self.CreateTime = None
        self.WorkGroupSet = None
        self.IsOwner = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserDescription = params.get("UserDescription")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        self.Creator = params.get("Creator")
        self.CreateTime = params.get("CreateTime")
        if params.get("WorkGroupSet") is not None:
            self.WorkGroupSet = []
            for item in params.get("WorkGroupSet"):
                obj = WorkGroupMessage()
                obj._deserialize(item)
                self.WorkGroupSet.append(obj)
        self.IsOwner = params.get("IsOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserMessage(AbstractModel):
    """用户部分信息

    """

    def __init__(self):
        """
        :param UserId: 用户Id，和CAM侧子用户Uin匹配\n        :type UserId: str\n        :param UserDescription: 用户描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserDescription: str\n        :param Creator: 当前用户的创建者\n        :type Creator: str\n        :param CreateTime: 当前用户的创建时间，形如2021-07-28 16:19:32\n        :type CreateTime: str\n        """
        self.UserId = None
        self.UserDescription = None
        self.Creator = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserDescription = params.get("UserDescription")
        self.Creator = params.get("Creator")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewBaseInfo(AbstractModel):
    """视图基本配置信息

    """

    def __init__(self):
        """
        :param DatabaseName: 该视图所属数据库名字\n        :type DatabaseName: str\n        :param ViewName: 视图名称\n        :type ViewName: str\n        """
        self.DatabaseName = None
        self.ViewName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewResponseInfo(AbstractModel):
    """查询视图信息对象

    """

    def __init__(self):
        """
        :param ViewBaseInfo: 视图基本信息。\n        :type ViewBaseInfo: :class:`tencentcloud.dlc.v20210125.models.ViewBaseInfo`\n        :param Columns: 视图列信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Columns: list of Column\n        :param Properties: 视图属性信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Properties: list of Property\n        :param CreateTime: 视图创建时间。\n        :type CreateTime: str\n        :param ModifiedTime: 视图更新时间。\n        :type ModifiedTime: str\n        """
        self.ViewBaseInfo = None
        self.Columns = None
        self.Properties = None
        self.CreateTime = None
        self.ModifiedTime = None


    def _deserialize(self, params):
        if params.get("ViewBaseInfo") is not None:
            self.ViewBaseInfo = ViewBaseInfo()
            self.ViewBaseInfo._deserialize(params.get("ViewBaseInfo"))
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self.Columns.append(obj)
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkGroupIdSetOfUserId(AbstractModel):
    """同一个用户绑定的工作组集合

    """

    def __init__(self):
        """
        :param UserId: 用户Id，和CAM侧Uin匹配\n        :type UserId: str\n        :param WorkGroupIds: 工作组Id集合\n        :type WorkGroupIds: list of int\n        """
        self.UserId = None
        self.WorkGroupIds = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.WorkGroupIds = params.get("WorkGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkGroupInfo(AbstractModel):
    """工作组信息

    """

    def __init__(self):
        """
        :param WorkGroupId: 查询到的工作组唯一Id\n        :type WorkGroupId: int\n        :param WorkGroupName: 工作组名称\n        :type WorkGroupName: str\n        :param WorkGroupDescription: 工作组描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type WorkGroupDescription: str\n        :param UserNum: 工作组关联的用户数量\n        :type UserNum: int\n        :param UserSet: 工作组关联的用户集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserSet: list of UserMessage\n        :param PolicySet: 工作组绑定的权限集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type PolicySet: list of Policy\n        :param Creator: 工作组的创建人\n        :type Creator: str\n        :param CreateTime: 工作组的创建时间，形如2021-07-28 16:19:32\n        :type CreateTime: str\n        """
        self.WorkGroupId = None
        self.WorkGroupName = None
        self.WorkGroupDescription = None
        self.UserNum = None
        self.UserSet = None
        self.PolicySet = None
        self.Creator = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.WorkGroupId = params.get("WorkGroupId")
        self.WorkGroupName = params.get("WorkGroupName")
        self.WorkGroupDescription = params.get("WorkGroupDescription")
        self.UserNum = params.get("UserNum")
        if params.get("UserSet") is not None:
            self.UserSet = []
            for item in params.get("UserSet"):
                obj = UserMessage()
                obj._deserialize(item)
                self.UserSet.append(obj)
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        self.Creator = params.get("Creator")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkGroupMessage(AbstractModel):
    """工作组部分信息

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组唯一Id\n        :type WorkGroupId: int\n        :param WorkGroupName: 工作组名称\n        :type WorkGroupName: str\n        :param WorkGroupDescription: 工作组描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type WorkGroupDescription: str\n        :param Creator: 创建者\n        :type Creator: str\n        :param CreateTime: 工作组创建的时间，形如2021-07-28 16:19:32\n        :type CreateTime: str\n        """
        self.WorkGroupId = None
        self.WorkGroupName = None
        self.WorkGroupDescription = None
        self.Creator = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.WorkGroupId = params.get("WorkGroupId")
        self.WorkGroupName = params.get("WorkGroupName")
        self.WorkGroupDescription = params.get("WorkGroupDescription")
        self.Creator = params.get("Creator")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        