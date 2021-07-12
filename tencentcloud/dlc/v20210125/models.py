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
        :param AddInfo: 要操作的工作组和用户信息
        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.UserIdSetOfWorkGroupId`
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param PolicySet: 鉴权策略集合
        :type PolicySet: list of Policy
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachWorkGroupPolicyRequest(AbstractModel):
    """AttachWorkGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param PolicySet: 要绑定的策略集合
        :type PolicySet: list of Policy
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindWorkGroupsToUserRequest(AbstractModel):
    """BindWorkGroupsToUser请求参数结构体

    """

    def __init__(self):
        """
        :param AddInfo: 绑定的用户和工作组信息
        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.WorkGroupIdSetOfUserId`
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CSV(AbstractModel):
    """CSV类型数据格式

    """

    def __init__(self):
        """
        :param CodeCompress: 压缩格式，["Snappy", "Gzip", "None"选一]。
        :type CodeCompress: str
        :param CSVSerde: CSV序列化及反序列化数据结构。
        :type CSVSerde: :class:`tencentcloud.dlc.v20210125.models.CSVSerde`
        :param HeadLines: 标题行，默认为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadLines: int
        :param Format: 格式，默认值为CSV
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        """
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
        :param Escape: CSV序列化转义符，默认为"\\"，最长8个字符，如 Escape: "/\"
        :type Escape: str
        :param Quote: CSV序列化字段域符，默认为"'"，最长8个字符, 如 Quote: "\""
        :type Quote: str
        :param Separator: CSV序列化分隔符，默认为"\t"，最长8个字符, 如 Separator: "\t"
        :type Separator: str
        """
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
        :param TaskId: 任务Id，全局唯一
        :type TaskId: str
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Column(AbstractModel):
    """数据表列信息。

    """

    def __init__(self):
        """
        :param Name: 列名称，不区分大小写，最大支持25个字符。
        :type Name: str
        :param Type: 列类型，支持如下类型定义:
string|tinyint|smallint|int|bigint|boolean|float|double|decimal|timestamp|date|binary|array<data_type>|map<primitive_type, data_type>|struct<col_name : data_type [COMMENT col_comment], ...>|uniontype<data_type, data_type, ...>。
        :type Type: str
        :param Comment: 对该类的注释。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        """
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
        :param DatabaseInfo: 数据库基础信息
        :type DatabaseInfo: :class:`tencentcloud.dlc.v20210125.models.DatabaseInfo`
        :param DatasourceConnectionName: 数据源名称，默认为CosDataCatalog
        :type DatasourceConnectionName: str
        """
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
        :param Execution: 生成的建库执行语句对象。
        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ScriptName: 脚本名称，最大不能超过255个字符。
        :type ScriptName: str
        :param SQLStatement: base64编码后的sql语句
        :type SQLStatement: str
        :param ScriptDesc: 脚本描述， 不能超过50个字符
        :type ScriptDesc: str
        :param DatabaseName: 数据库名称
        :type DatabaseName: str
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateStoreLocationRequest(AbstractModel):
    """CreateStoreLocation请求参数结构体

    """

    def __init__(self):
        """
        :param StoreLocation: 计算结果存储cos路径，如：cosn://bucketname/
        :type StoreLocation: str
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTableRequest(AbstractModel):
    """CreateTable请求参数结构体

    """

    def __init__(self):
        """
        :param TableInfo: 数据表配置信息
        :type TableInfo: :class:`tencentcloud.dlc.v20210125.models.TableInfo`
        """
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
        :param Execution: 生成的建表执行语句对象。
        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Task: 计算任务，该参数中包含任务类型及其相关配置信息
        :type Task: :class:`tencentcloud.dlc.v20210125.models.Task`
        :param DatabaseName: 数据库名称。任务在执行前均会USE该数据库， 除了首次建库时，其他情况建议均添加上。
        :type DatabaseName: str
        :param DatasourceConnectionName: 默认数据源名称。
        :type DatasourceConnectionName: str
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户Id，当前主账号的子账号Uin，和CAM侧匹配
        :type UserId: str
        :param UserDescription: 用户描述
        :type UserDescription: str
        :param PolicySet: 绑定到用户的权限集合
        :type PolicySet: list of Policy
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWorkGroupRequest(AbstractModel):
    """CreateWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupName: 工作组名称
        :type WorkGroupName: str
        :param WorkGroupDescription: 工作组描述
        :type WorkGroupDescription: str
        :param PolicySet: 工作组绑定的鉴权策略集合
        :type PolicySet: list of Policy
        """
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
        :param WorkGroupId: 工作组Id，全局唯一
        :type WorkGroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TextFile: :class:`tencentcloud.dlc.v20210125.models.TextFile`
        :param CSV: 文本格式，CSV。
注意：此字段可能返回 null，表示取不到有效值。
        :type CSV: :class:`tencentcloud.dlc.v20210125.models.CSV`
        :param Json: 文本格式，Json。
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: :class:`tencentcloud.dlc.v20210125.models.Other`
        :param Parquet: Parquet格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Parquet: :class:`tencentcloud.dlc.v20210125.models.Other`
        :param ORC: ORC格式
注意：此字段可能返回 null，表示取不到有效值。
        :type ORC: :class:`tencentcloud.dlc.v20210125.models.Other`
        :param AVRO: AVRO格式
注意：此字段可能返回 null，表示取不到有效值。
        :type AVRO: :class:`tencentcloud.dlc.v20210125.models.Other`
        """
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
        :param DatabaseName: 数据库名称。
        :type DatabaseName: str
        :param Comment: 数据库描述信息，长度 0~256。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param Properties: 数据库属性列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        """
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
        :param DatabaseName: 数据库名称。
        :type DatabaseName: str
        :param Comment: 数据库描述信息，长度 0~256。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param Properties: 数据库属性列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param CreateTime: 数据库创建时间戳，单位：s。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ModifiedTime: 数据库更新时间戳，单位：s。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        """
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
        :param ScriptIds: 脚本id，其可以通过DescribeScripts接口提取
        :type ScriptIds: list of str
        """
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
        :param ScriptsAffected: 删除的脚本数量
        :type ScriptsAffected: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param UserIds: 需要删除的用户的Id
        :type UserIds: list of str
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsersFromWorkGroupRequest(AbstractModel):
    """DeleteUsersFromWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AddInfo: 要删除的用户信息
        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.UserIdSetOfWorkGroupId`
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWorkGroupRequest(AbstractModel):
    """DeleteWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupIds: 要删除的工作组Id集合
        :type WorkGroupIds: list of int
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 数据偏移量，从0开始，默认为0。
        :type Offset: int
        :param KeyWord: 模糊匹配，库名关键字。
        :type KeyWord: str
        :param DatasourceConnectionName: 数据源唯名称，该名称可以通过DescribeDatasourceConnection接口查询到。默认为CosDataCatalog
        :type DatasourceConnectionName: str
        """
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
        :param DatabaseList: 数据库对象列表。
        :type DatabaseList: list of DatabaseResponseInfo
        :param TotalCount: 实例总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param SortBy: 按字段排序，支持如下字段类型，update-time
        :type SortBy: str
        :param Sorting: 排序方式，desc表示正序，asc表示反序
        :type Sorting: str
        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
script-id - String - （过滤条件）script-id取值形如：157de0d1-26b4-4df2-a2d0-b64afc406c25。
script-name-keyword - String - （过滤条件）数据表名称,形如：script-test。
        :type Filters: list of Filter
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Scripts: list of Script
        :param TotalCount: 实例总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type StoreLocation: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param TableName: 查询对象表名称
        :type TableName: str
        :param DatabaseName: 查询表所在的数据库名称。
        :type DatabaseName: str
        :param DatasourceConnectionName: 查询表所在的数据源名称
        :type DatasourceConnectionName: str
        """
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
        :param Table: 数据表对象
        :type Table: :class:`tencentcloud.dlc.v20210125.models.TableResponseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param DatabaseName: 列出该数据库下所属数据表。
        :type DatabaseName: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 数据偏移量，从0开始，默认为0。
        :type Offset: int
        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
table-name - String - （过滤条件）数据表名称,形如：table-001。
table-id - String - （过滤条件）table id形如：12342。
        :type Filters: list of Filter
        :param DatasourceConnectionName: 指定查询的数据源名称，默认为CosDataCatalog
        :type DatasourceConnectionName: str
        """
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
        :param TableList: 数据表对象列表。
        :type TableList: list of TableResponseInfo
        :param TotalCount: 实例总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为以下其中一个,每个过滤参数支持的过滤值不超过5个。
task-id - String - （任务ID过滤）task-id取值形如：e386471f-139a-4e59-877f-50ece8135b99。
task-state - String - （任务状态过滤）取值范围 0(初始化)， 1(运行中)， 2(成功)， -1(失败)。
task-sql-keyword - String - （SQL语句关键字）取值形如：DROP TABLE。
        :type Filters: list of Filter
        :param SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc。
        :type Sorting: str
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。默认为45天前的当前时刻
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS时间跨度在(0,30天]，支持最近45天数据查询。默认为当前时刻
        :type EndTime: str
        """
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
        :param TaskList: 任务对象列表。
        :type TaskList: list of TaskResponseInfo
        :param TotalCount: 实例总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param UserId: 查询的用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认20，最大值100
        :type Limit: int
        :param SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc
        :type Sorting: str
        """
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
        :param TotalCount: 用户总数
        :type TotalCount: int
        :param UserSet: 用户集合
        :type UserSet: list of UserInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param DatabaseName: 列出该数据库下所属数据表。
        :type DatabaseName: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 数据偏移量，从0开始，默认为0。
        :type Offset: int
        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
view-name - String - （过滤条件）数据表名称,形如：view-001。
view-id - String - （过滤条件）view id形如：12342。
        :type Filters: list of Filter
        :param DatasourceConnectionName: 数据库所属的数据源名称
        :type DatasourceConnectionName: str
        """
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
        :param ViewList: 视图对象列表。
        :type ViewList: list of ViewResponseInfo
        :param TotalCount: 实例总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param WorkGroupId: 查询的工作组Id
        :type WorkGroupId: int
        :param Filters: 过滤条件，当前仅支持按照工作组名称进行模糊搜索。Key为workgroup-name
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认20，最大值100
        :type Limit: int
        :param SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc
        :type Sorting: str
        """
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
        :param TotalCount: 工作组总数
        :type TotalCount: int
        :param WorkGroupSet: 工作组信息集合
        :type WorkGroupSet: list of WorkGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param PolicySet: 解绑的权限集合
        :type PolicySet: list of Policy
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachWorkGroupPolicyRequest(AbstractModel):
    """DetachWorkGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param PolicySet: 解绑的权限集合
        :type PolicySet: list of Policy
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Execution(AbstractModel):
    """SQL语句对象

    """

    def __init__(self):
        """
        :param SQL: 自动生成SQL语句。
        :type SQL: str
        """
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
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑或（OR）关系。
        :type Name: str
        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
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
        


class KVPair(AbstractModel):
    """配置格式

    """

    def __init__(self):
        """
        :param Key: 配置的key值
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 配置的value值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param UserDescription: 用户描述
        :type UserDescription: str
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWorkGroupRequest(AbstractModel):
    """ModifyWorkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param WorkGroupDescription: 工作组描述
        :type WorkGroupDescription: str
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Other(AbstractModel):
    """数据格式其它类型。

    """

    def __init__(self):
        """
        :param Format: 枚举类型，默认值为Json，可选值为[Json, Parquet, ORC, AVRD]之一。
        :type Format: str
        """
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
        :param Name: 分区列名。
        :type Name: str
        :param Type: 分区类型。
        :type Type: str
        :param Comment: 对分区的描述。
        :type Comment: str
        """
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
        :param Catalog: 需要授权的数据源名称，*代表拥有全部数据源权限
        :type Catalog: str
        :param Database: 需要授权的数据库名称，*代表拥有全部数据库名称
        :type Database: str
        :param Table: 需要授权的表名称，*代表拥有全部表权限
        :type Table: str
        :param Operation: 授权的操作，当前只支持“ALL”
        :type Operation: str
        """
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
        :param Key: 属性key名称。
        :type Key: str
        :param Value: 属性key对应的value。
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
        


class SQLTask(AbstractModel):
    """SQL查询任务

    """

    def __init__(self):
        """
        :param SQL: base64加密后的SQL语句
        :type SQL: str
        :param Config: 任务的配置信息
        :type Config: list of KVPair
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptId: str
        :param ScriptName: 脚本名称，长度0-25。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptName: str
        :param ScriptDesc: 脚本描述，长度0-50。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptDesc: str
        :param DatabaseName: 默认关联数据库。
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param SQLStatement: SQL描述，长度0-10000。
注意：此字段可能返回 null，表示取不到有效值。
        :type SQLStatement: str
        :param UpdateTime: 更新时间戳， 单位：ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        """
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
        :param DatabaseName: 该数据表所属数据库名字
        :type DatabaseName: str
        :param TableName: 数据表名字
        :type TableName: str
        :param DatasourceConnectionName: 该数据表所属数据源名字
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionName: str
        """
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
        :param TableBaseInfo: 数据表配置信息。
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param DataFormat: 数据表格式。每次入参可选如下其一的KV结构，[TextFile，CSV，Json, Parquet, ORC, AVRD]。
        :type DataFormat: :class:`tencentcloud.dlc.v20210125.models.DataFormat`
        :param Columns: 数据表列信息。
        :type Columns: list of Column
        :param Partitions: 数据表分块信息。
        :type Partitions: list of Partition
        :param Location: 数据存储路径。当前仅支持cos路径，格式如下：cosn://bucket-name/filepath。
        :type Location: str
        """
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
        :param TableBaseInfo: 数据表基本信息。
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param Columns: 数据表列信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param Partitions: 数据表分块信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of Partition
        :param Location: 数据存储路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param Properties: 数据表属性信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param ModifiedTime: 数据表更新时间, 单位: ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param CreateTime: 数据表创建时间,单位: ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param InputFormat: 数据格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputFormat: str
        """
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
        :param SQLTask: SQL查询任务
        :type SQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`
        :param SparkSQLTask: Spark SQL查询任务
        :type SparkSQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`
        """
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
        :param DatabaseName: 任务所属Database的名称。
        :type DatabaseName: str
        :param DataAmount: 任务数据量。
        :type DataAmount: int
        :param Id: 任务Id。
        :type Id: str
        :param UsedTime: 计算时长，单位： ms。
        :type UsedTime: int
        :param OutputPath: 任务输出路径。
        :type OutputPath: str
        :param CreateTime: 任务创建时间。
        :type CreateTime: str
        :param State: 任务状态, 0 初始化， 1 执行中， 2 执行成功，3 数据写入中，-1 执行失败。
        :type State: int
        :param SQLType: 任务SQL类型，DDL|DML等
        :type SQLType: str
        :param SQL: 任务SQL语句
        :type SQL: str
        :param ResultExpired: 结果是否过期。
        :type ResultExpired: bool
        :param RowAffectInfo: 数据影响统计信息。
        :type RowAffectInfo: str
        :param DataSet: 任务结果数据表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSet: str
        :param Error: 失败信息, 例如：errorMessage。该字段已废弃。
        :type Error: str
        :param Percentage: 任务执行进度num/100(%)
        :type Percentage: int
        :param OutputMessage: 任务执行输出信息。
        :type OutputMessage: str
        :param TaskType: 执行SQL的引擎类型
        :type TaskType: str
        """
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
        


class TextFile(AbstractModel):
    """文本格式

    """

    def __init__(self):
        """
        :param Format: 文本类型，本参数取值为TextFile。
        :type Format: str
        :param Regex: 处理文本用的正则表达式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: str
        """
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
        :param AddInfo: 解绑的工作组Id和用户Id的关联关系
        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.WorkGroupIdSetOfUserId`
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserIdSetOfWorkGroupId(AbstractModel):
    """绑定到同一个工作组的用户Id的集合

    """

    def __init__(self):
        """
        :param WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param UserIds: 用户Id集合，和CAM侧Uin匹配
        :type UserIds: list of str
        """
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
        :param UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param UserDescription: 用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDescription: str
        :param PolicySet: 单独给用户绑定的权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicySet: list of Policy
        :param Creator: 创建者
        :type Creator: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param WorkGroupSet: 关联的工作组集合
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupSet: list of WorkGroupMessage
        :param IsOwner: 是否是管理员账号
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOwner: bool
        """
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
        :param UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param UserDescription: 用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDescription: str
        :param Creator: 创建者
        :type Creator: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
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
        :param DatabaseName: 该视图所属数据库名字
        :type DatabaseName: str
        :param ViewName: 视图名称
        :type ViewName: str
        """
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
        :param ViewBaseInfo: 视图基本信息。
        :type ViewBaseInfo: :class:`tencentcloud.dlc.v20210125.models.ViewBaseInfo`
        :param Columns: 视图列信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param Properties: 视图属性信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param CreateTime: 视图创建时间。
        :type CreateTime: str
        :param ModifiedTime: 视图更新时间。
        :type ModifiedTime: str
        """
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
        :param UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param WorkGroupIds: 工作组Id集合
        :type WorkGroupIds: list of int
        """
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
        :param WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param WorkGroupName: 工作组名称
        :type WorkGroupName: str
        :param WorkGroupDescription: 工作组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupDescription: str
        :param UserNum: 工作组关联的用户数量
        :type UserNum: int
        :param UserSet: 工作组关联的用户集合
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSet: list of UserMessage
        :param PolicySet: 工作组绑定的权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicySet: list of Policy
        :param Creator: 创建者
        :type Creator: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
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
        :param WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param WorkGroupName: 工作组名称
        :type WorkGroupName: str
        :param WorkGroupDescription: 工作组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupDescription: str
        :param Creator: 创建者
        :type Creator: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
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
        