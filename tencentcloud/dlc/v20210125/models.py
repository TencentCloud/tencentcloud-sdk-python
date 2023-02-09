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


class AddDMSPartitionsRequest(AbstractModel):
    """AddDMSPartitions请求参数结构体

    """

    def __init__(self):
        r"""
        :param Partitions: 分区
        :type Partitions: list of DMSPartition
        """
        self.Partitions = None


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDMSPartitionsResponse(AbstractModel):
    """AddDMSPartitions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 成功数量
        :type Total: int
        :param Partitions: 分区值
        :type Partitions: list of DMSPartition
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Partitions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.RequestId = params.get("RequestId")


class AddUsersToWorkGroupRequest(AbstractModel):
    """AddUsersToWorkGroup请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AlterDMSDatabaseRequest(AbstractModel):
    """AlterDMSDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param CurrentName: 当前名称
        :type CurrentName: str
        :param SchemaName: schema名称
        :type SchemaName: str
        :param Location: 路径
        :type Location: str
        :param Asset: 基础对象
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        """
        self.CurrentName = None
        self.SchemaName = None
        self.Location = None
        self.Asset = None


    def _deserialize(self, params):
        self.CurrentName = params.get("CurrentName")
        self.SchemaName = params.get("SchemaName")
        self.Location = params.get("Location")
        if params.get("Asset") is not None:
            self.Asset = Asset()
            self.Asset._deserialize(params.get("Asset"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlterDMSDatabaseResponse(AbstractModel):
    """AlterDMSDatabase返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AlterDMSPartitionRequest(AbstractModel):
    """AlterDMSPartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param CurrentDbName: 当前名称，变更前db名称
        :type CurrentDbName: str
        :param CurrentTableName: 当前名称，变更前table名称
        :type CurrentTableName: str
        :param CurrentValues: 当前名称，变更前Part名称
        :type CurrentValues: str
        :param Partition: 分区
        :type Partition: :class:`tencentcloud.dlc.v20210125.models.DMSPartition`
        """
        self.CurrentDbName = None
        self.CurrentTableName = None
        self.CurrentValues = None
        self.Partition = None


    def _deserialize(self, params):
        self.CurrentDbName = params.get("CurrentDbName")
        self.CurrentTableName = params.get("CurrentTableName")
        self.CurrentValues = params.get("CurrentValues")
        if params.get("Partition") is not None:
            self.Partition = DMSPartition()
            self.Partition._deserialize(params.get("Partition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlterDMSPartitionResponse(AbstractModel):
    """AlterDMSPartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AlterDMSTableRequest(AbstractModel):
    """AlterDMSTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param CurrentName: 当前名称
        :type CurrentName: str
        :param CurrentDbName: 当前数据库名称
        :type CurrentDbName: str
        :param Asset: 基础对象
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param Type: 表类型
        :type Type: str
        :param DbName: 数据库名称
        :type DbName: str
        :param StorageSize: 存储大小
        :type StorageSize: int
        :param RecordCount: 记录数量
        :type RecordCount: int
        :param LifeTime: 生命周期
        :type LifeTime: int
        :param DataUpdateTime: 数据更新时间
        :type DataUpdateTime: str
        :param StructUpdateTime: 结构更新时间
        :type StructUpdateTime: str
        :param LastAccessTime: 最后访问时间
        :type LastAccessTime: str
        :param Sds: 存储对象
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        :param Columns: 列
        :type Columns: list of DMSColumn
        :param PartitionKeys: 分区键值
        :type PartitionKeys: list of DMSColumn
        :param ViewOriginalText: 视图文本
        :type ViewOriginalText: str
        :param ViewExpandedText: 视图文本
        :type ViewExpandedText: str
        :param Partitions: 分区
        :type Partitions: list of DMSPartition
        :param Name: 当前表名
        :type Name: str
        """
        self.CurrentName = None
        self.CurrentDbName = None
        self.Asset = None
        self.Type = None
        self.DbName = None
        self.StorageSize = None
        self.RecordCount = None
        self.LifeTime = None
        self.DataUpdateTime = None
        self.StructUpdateTime = None
        self.LastAccessTime = None
        self.Sds = None
        self.Columns = None
        self.PartitionKeys = None
        self.ViewOriginalText = None
        self.ViewExpandedText = None
        self.Partitions = None
        self.Name = None


    def _deserialize(self, params):
        self.CurrentName = params.get("CurrentName")
        self.CurrentDbName = params.get("CurrentDbName")
        if params.get("Asset") is not None:
            self.Asset = Asset()
            self.Asset._deserialize(params.get("Asset"))
        self.Type = params.get("Type")
        self.DbName = params.get("DbName")
        self.StorageSize = params.get("StorageSize")
        self.RecordCount = params.get("RecordCount")
        self.LifeTime = params.get("LifeTime")
        self.DataUpdateTime = params.get("DataUpdateTime")
        self.StructUpdateTime = params.get("StructUpdateTime")
        self.LastAccessTime = params.get("LastAccessTime")
        if params.get("Sds") is not None:
            self.Sds = DMSSds()
            self.Sds._deserialize(params.get("Sds"))
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.Columns.append(obj)
        if params.get("PartitionKeys") is not None:
            self.PartitionKeys = []
            for item in params.get("PartitionKeys"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.PartitionKeys.append(obj)
        self.ViewOriginalText = params.get("ViewOriginalText")
        self.ViewExpandedText = params.get("ViewExpandedText")
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlterDMSTableResponse(AbstractModel):
    """AlterDMSTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Asset(AbstractModel):
    """元数据基本对象

    """

    def __init__(self):
        r"""
        :param Id: 主键
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Guid: 对象GUID值
注意：此字段可能返回 null，表示取不到有效值。
        :type Guid: str
        :param Catalog: 数据目录
注意：此字段可能返回 null，表示取不到有效值。
        :type Catalog: str
        :param Description: 描述信息
        :type Description: str
        :param Owner: 对象owner
        :type Owner: str
        :param OwnerAccount: 对象owner账户
        :type OwnerAccount: str
        :param PermValues: 权限
        :type PermValues: list of KVPair
        :param Params: 附加属性
        :type Params: list of KVPair
        :param BizParams: 附加业务属性
        :type BizParams: list of KVPair
        :param DataVersion: 数据版本
        :type DataVersion: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifiedTime: 修改时间
        :type ModifiedTime: str
        :param DatasourceId: 数据源主键
        :type DatasourceId: int
        """
        self.Id = None
        self.Name = None
        self.Guid = None
        self.Catalog = None
        self.Description = None
        self.Owner = None
        self.OwnerAccount = None
        self.PermValues = None
        self.Params = None
        self.BizParams = None
        self.DataVersion = None
        self.CreateTime = None
        self.ModifiedTime = None
        self.DatasourceId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Guid = params.get("Guid")
        self.Catalog = params.get("Catalog")
        self.Description = params.get("Description")
        self.Owner = params.get("Owner")
        self.OwnerAccount = params.get("OwnerAccount")
        if params.get("PermValues") is not None:
            self.PermValues = []
            for item in params.get("PermValues"):
                obj = KVPair()
                obj._deserialize(item)
                self.PermValues.append(obj)
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self.Params.append(obj)
        if params.get("BizParams") is not None:
            self.BizParams = []
            for item in params.get("BizParams"):
                obj = KVPair()
                obj._deserialize(item)
                self.BizParams.append(obj)
        self.DataVersion = params.get("DataVersion")
        self.CreateTime = params.get("CreateTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.DatasourceId = params.get("DatasourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户Id，和子用户uin相同，需要先使用CreateUser接口创建用户。可以使用DescribeUsers接口查看。
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        


class CancelNotebookSessionStatementBatchRequest(AbstractModel):
    """CancelNotebookSessionStatementBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param BatchId: 批任务唯一标识
        :type BatchId: str
        """
        self.SessionId = None
        self.BatchId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelNotebookSessionStatementBatchResponse(AbstractModel):
    """CancelNotebookSessionStatementBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelNotebookSessionStatementRequest(AbstractModel):
    """CancelNotebookSessionStatement请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param StatementId: Session Statement唯一标识
        :type StatementId: str
        """
        self.SessionId = None
        self.StatementId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.StatementId = params.get("StatementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelNotebookSessionStatementResponse(AbstractModel):
    """CancelNotebookSessionStatement返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckLockMetaDataRequest(AbstractModel):
    """CheckLockMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param LockId: 锁ID
        :type LockId: int
        :param DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        :param TxnId: 事务ID
        :type TxnId: int
        :param ElapsedMs: 过期时间ms
        :type ElapsedMs: int
        """
        self.LockId = None
        self.DatasourceConnectionName = None
        self.TxnId = None
        self.ElapsedMs = None


    def _deserialize(self, params):
        self.LockId = params.get("LockId")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.TxnId = params.get("TxnId")
        self.ElapsedMs = params.get("ElapsedMs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckLockMetaDataResponse(AbstractModel):
    """CheckLockMetaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param LockId: 锁ID
        :type LockId: int
        :param LockState: 锁状态：ACQUIRED、WAITING、ABORT、NOT_ACQUIRED
        :type LockState: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LockId = None
        self.LockState = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LockId = params.get("LockId")
        self.LockState = params.get("LockState")
        self.RequestId = params.get("RequestId")


class Column(AbstractModel):
    """数据表列信息。

    """

    def __init__(self):
        r"""
        :param Name: 列名称，不区分大小写，最大支持25个字符。
        :type Name: str
        :param Type: 列类型，支持如下类型定义:
string|tinyint|smallint|int|bigint|boolean|float|double|decimal|timestamp|date|binary|array<data_type>|map<primitive_type, data_type>|struct<col_name : data_type [COMMENT col_comment], ...>|uniontype<data_type, data_type, ...>。
        :type Type: str
        :param Comment: 对该类的注释。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param Precision: 表示整个 numeric 的长度
注意：此字段可能返回 null，表示取不到有效值。
        :type Precision: int
        :param Scale: 表示小数部分的长度
注意：此字段可能返回 null，表示取不到有效值。
        :type Scale: int
        :param Nullable: 是否为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Nullable: str
        :param Position: 字段位置，小的在前
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: int
        :param CreateTime: 字段创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ModifiedTime: 字段修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param IsPartition: 是否为分区字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPartition: bool
        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.Precision = None
        self.Scale = None
        self.Nullable = None
        self.Position = None
        self.CreateTime = None
        self.ModifiedTime = None
        self.IsPartition = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        self.Precision = params.get("Precision")
        self.Scale = params.get("Scale")
        self.Nullable = params.get("Nullable")
        self.Position = params.get("Position")
        self.CreateTime = params.get("CreateTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.IsPartition = params.get("IsPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDMSDatabaseRequest(AbstractModel):
    """CreateDMSDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param Asset: 基础元数据对象
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param SchemaName: Schema目录
        :type SchemaName: str
        :param Location: Db存储路径
        :type Location: str
        :param Name: 数据库名称
        :type Name: str
        """
        self.Asset = None
        self.SchemaName = None
        self.Location = None
        self.Name = None


    def _deserialize(self, params):
        if params.get("Asset") is not None:
            self.Asset = Asset()
            self.Asset._deserialize(params.get("Asset"))
        self.SchemaName = params.get("SchemaName")
        self.Location = params.get("Location")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDMSDatabaseResponse(AbstractModel):
    """CreateDMSDatabase返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDMSTableRequest(AbstractModel):
    """CreateDMSTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param Asset: 基础对象
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param Type: 表类型
        :type Type: str
        :param DbName: 数据库名称
        :type DbName: str
        :param StorageSize: 存储大小
        :type StorageSize: int
        :param RecordCount: 记录数量
        :type RecordCount: int
        :param LifeTime: 生命周期
        :type LifeTime: int
        :param DataUpdateTime: 数据更新时间
        :type DataUpdateTime: str
        :param StructUpdateTime: 结构更新时间
        :type StructUpdateTime: str
        :param LastAccessTime: 最后访问时间
        :type LastAccessTime: str
        :param Sds: 存储对象
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        :param Columns: 列
        :type Columns: list of DMSColumn
        :param PartitionKeys: 分区键值
        :type PartitionKeys: list of DMSColumn
        :param ViewOriginalText: 视图文本
        :type ViewOriginalText: str
        :param ViewExpandedText: 视图文本
        :type ViewExpandedText: str
        :param Partitions: 分区
        :type Partitions: list of DMSPartition
        :param Name: 表名称
        :type Name: str
        """
        self.Asset = None
        self.Type = None
        self.DbName = None
        self.StorageSize = None
        self.RecordCount = None
        self.LifeTime = None
        self.DataUpdateTime = None
        self.StructUpdateTime = None
        self.LastAccessTime = None
        self.Sds = None
        self.Columns = None
        self.PartitionKeys = None
        self.ViewOriginalText = None
        self.ViewExpandedText = None
        self.Partitions = None
        self.Name = None


    def _deserialize(self, params):
        if params.get("Asset") is not None:
            self.Asset = Asset()
            self.Asset._deserialize(params.get("Asset"))
        self.Type = params.get("Type")
        self.DbName = params.get("DbName")
        self.StorageSize = params.get("StorageSize")
        self.RecordCount = params.get("RecordCount")
        self.LifeTime = params.get("LifeTime")
        self.DataUpdateTime = params.get("DataUpdateTime")
        self.StructUpdateTime = params.get("StructUpdateTime")
        self.LastAccessTime = params.get("LastAccessTime")
        if params.get("Sds") is not None:
            self.Sds = DMSSds()
            self.Sds._deserialize(params.get("Sds"))
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.Columns.append(obj)
        if params.get("PartitionKeys") is not None:
            self.PartitionKeys = []
            for item in params.get("PartitionKeys"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.PartitionKeys.append(obj)
        self.ViewOriginalText = params.get("ViewOriginalText")
        self.ViewExpandedText = params.get("ViewExpandedText")
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDMSTableResponse(AbstractModel):
    """CreateDMSTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDatabaseRequest(AbstractModel):
    """CreateDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatabaseInfo: 数据库基础信息
        :type DatabaseInfo: :class:`tencentcloud.dlc.v20210125.models.DatabaseInfo`
        :param DatasourceConnectionName: 数据源名称，默认为DataLakeCatalog
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
        r"""
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


class CreateExportTaskRequest(AbstractModel):
    """CreateExportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param InputType: 数据来源，lakefsStorage、taskResult
        :type InputType: str
        :param InputConf: 导出任务输入配置
        :type InputConf: list of KVPair
        :param OutputConf: 导出任务输出配置
        :type OutputConf: list of KVPair
        :param OutputType: 目标数据源的类型，目前支持导出到cos
        :type OutputType: str
        """
        self.InputType = None
        self.InputConf = None
        self.OutputConf = None
        self.OutputType = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("InputConf") is not None:
            self.InputConf = []
            for item in params.get("InputConf"):
                obj = KVPair()
                obj._deserialize(item)
                self.InputConf.append(obj)
        if params.get("OutputConf") is not None:
            self.OutputConf = []
            for item in params.get("OutputConf"):
                obj = KVPair()
                obj._deserialize(item)
                self.OutputConf.append(obj)
        self.OutputType = params.get("OutputType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExportTaskResponse(AbstractModel):
    """CreateExportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateImportTaskRequest(AbstractModel):
    """CreateImportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param InputType: 数据来源，cos
        :type InputType: str
        :param InputConf: 输入配置
        :type InputConf: list of KVPair
        :param OutputConf: 输出配置
        :type OutputConf: list of KVPair
        :param OutputType: 目标数据源的类型，目前支持导入到托管存储，即lakefsStorage
        :type OutputType: str
        """
        self.InputType = None
        self.InputConf = None
        self.OutputConf = None
        self.OutputType = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("InputConf") is not None:
            self.InputConf = []
            for item in params.get("InputConf"):
                obj = KVPair()
                obj._deserialize(item)
                self.InputConf.append(obj)
        if params.get("OutputConf") is not None:
            self.OutputConf = []
            for item in params.get("OutputConf"):
                obj = KVPair()
                obj._deserialize(item)
                self.OutputConf.append(obj)
        self.OutputType = params.get("OutputType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImportTaskResponse(AbstractModel):
    """CreateImportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateInternalTableRequest(AbstractModel):
    """CreateInternalTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param TableBaseInfo: 表基本信息
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param Columns: 表字段信息
        :type Columns: list of TColumn
        :param Partitions: 表分区信息
        :type Partitions: list of TPartition
        :param Properties: 表属性信息
        :type Properties: list of Property
        """
        self.TableBaseInfo = None
        self.Columns = None
        self.Partitions = None
        self.Properties = None


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self.TableBaseInfo = TableBaseInfo()
            self.TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = TColumn()
                obj._deserialize(item)
                self.Columns.append(obj)
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = TPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
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
        


class CreateInternalTableResponse(AbstractModel):
    """CreateInternalTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param Execution: 创建托管存储内表sql语句描述
        :type Execution: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Execution = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Execution = params.get("Execution")
        self.RequestId = params.get("RequestId")


class CreateNotebookSessionRequest(AbstractModel):
    """CreateNotebookSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: Session名称
        :type Name: str
        :param Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        :param DataEngineName: DLC Spark作业引擎名称
        :type DataEngineName: str
        :param ProgramDependentFiles: session文件地址，当前支持：cosn://和lakefs://两种路径
        :type ProgramDependentFiles: list of str
        :param ProgramDependentJars: 依赖的jar程序地址，当前支持：cosn://和lakefs://两种路径
        :type ProgramDependentJars: list of str
        :param ProgramDependentPython: 依赖的python程序地址，当前支持：cosn://和lakefs://两种路径
        :type ProgramDependentPython: list of str
        :param ProgramArchives: 依赖的pyspark虚拟环境地址，当前支持：cosn://和lakefs://两种路径
        :type ProgramArchives: list of str
        :param DriverSize: 指定的Driver规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type DriverSize: str
        :param ExecutorSize: 指定的Executor规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type ExecutorSize: str
        :param ExecutorNumbers: 指定的Executor数量，默认为1
        :type ExecutorNumbers: int
        :param Arguments: Session相关配置，当前支持：dlc.eni、dlc.role.arn、dlc.sql.set.config以及用户指定的配置，注：roleArn必填；
        :type Arguments: list of KVPair
        :param ProxyUser: 代理用户，默认为root
        :type ProxyUser: str
        :param TimeoutInSecond: 指定的Session超时时间，单位秒，默认3600秒
        :type TimeoutInSecond: int
        :param ExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于ExecutorNumbers
        :type ExecutorMaxNumbers: int
        """
        self.Name = None
        self.Kind = None
        self.DataEngineName = None
        self.ProgramDependentFiles = None
        self.ProgramDependentJars = None
        self.ProgramDependentPython = None
        self.ProgramArchives = None
        self.DriverSize = None
        self.ExecutorSize = None
        self.ExecutorNumbers = None
        self.Arguments = None
        self.ProxyUser = None
        self.TimeoutInSecond = None
        self.ExecutorMaxNumbers = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Kind = params.get("Kind")
        self.DataEngineName = params.get("DataEngineName")
        self.ProgramDependentFiles = params.get("ProgramDependentFiles")
        self.ProgramDependentJars = params.get("ProgramDependentJars")
        self.ProgramDependentPython = params.get("ProgramDependentPython")
        self.ProgramArchives = params.get("ProgramArchives")
        self.DriverSize = params.get("DriverSize")
        self.ExecutorSize = params.get("ExecutorSize")
        self.ExecutorNumbers = params.get("ExecutorNumbers")
        if params.get("Arguments") is not None:
            self.Arguments = []
            for item in params.get("Arguments"):
                obj = KVPair()
                obj._deserialize(item)
                self.Arguments.append(obj)
        self.ProxyUser = params.get("ProxyUser")
        self.TimeoutInSecond = params.get("TimeoutInSecond")
        self.ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookSessionResponse(AbstractModel):
    """CreateNotebookSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param SparkAppId: Spark任务返回的AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppId: str
        :param State: Session状态，包含：not_started（未启动）、starting（已启动）、idle（等待输入）、busy(正在运行statement)、shutting_down（停止）、error（异常）、dead（已退出）、killed（被杀死）、success（正常停止）
        :type State: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionId = None
        self.SparkAppId = None
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.SparkAppId = params.get("SparkAppId")
        self.State = params.get("State")
        self.RequestId = params.get("RequestId")


class CreateNotebookSessionStatementRequest(AbstractModel):
    """CreateNotebookSessionStatement请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param Code: 执行的代码
        :type Code: str
        :param Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        """
        self.SessionId = None
        self.Code = None
        self.Kind = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Code = params.get("Code")
        self.Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookSessionStatementResponse(AbstractModel):
    """CreateNotebookSessionStatement返回参数结构体

    """

    def __init__(self):
        r"""
        :param NotebookSessionStatement: Session Statement详情
        :type NotebookSessionStatement: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionStatementInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookSessionStatement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotebookSessionStatement") is not None:
            self.NotebookSessionStatement = NotebookSessionStatementInfo()
            self.NotebookSessionStatement._deserialize(params.get("NotebookSessionStatement"))
        self.RequestId = params.get("RequestId")


class CreateNotebookSessionStatementSupportBatchSQLRequest(AbstractModel):
    """CreateNotebookSessionStatementSupportBatchSQL请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param Code: 执行的代码
        :type Code: str
        :param Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        :param SaveResult: 是否保存运行结果
        :type SaveResult: bool
        """
        self.SessionId = None
        self.Code = None
        self.Kind = None
        self.SaveResult = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Code = params.get("Code")
        self.Kind = params.get("Kind")
        self.SaveResult = params.get("SaveResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookSessionStatementSupportBatchSQLResponse(AbstractModel):
    """CreateNotebookSessionStatementSupportBatchSQL返回参数结构体

    """

    def __init__(self):
        r"""
        :param NotebookSessionStatementBatches: Session Statement详情
        :type NotebookSessionStatementBatches: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionStatementBatchInformation`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookSessionStatementBatches = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotebookSessionStatementBatches") is not None:
            self.NotebookSessionStatementBatches = NotebookSessionStatementBatchInformation()
            self.NotebookSessionStatementBatches._deserialize(params.get("NotebookSessionStatementBatches"))
        self.RequestId = params.get("RequestId")


class CreateResultDownloadRequest(AbstractModel):
    """CreateResultDownload请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 查询结果任务Id
        :type TaskId: str
        :param Format: 下载格式
        :type Format: str
        :param Force: 是否重新生成下载文件，仅当之前任务为 Timout | Error 时有效
        :type Force: bool
        """
        self.TaskId = None
        self.Format = None
        self.Force = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Format = params.get("Format")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResultDownloadResponse(AbstractModel):
    """CreateResultDownload返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadId: 下载任务Id
        :type DownloadId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadId = params.get("DownloadId")
        self.RequestId = params.get("RequestId")


class CreateScriptRequest(AbstractModel):
    """CreateScript请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSparkAppRequest(AbstractModel):
    """CreateSparkApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: spark应用名
        :type AppName: str
        :param AppType: 1代表spark jar应用，2代表spark streaming应用
        :type AppType: int
        :param DataEngine: 执行spark作业的数据引擎
        :type DataEngine: str
        :param AppFile: spark应用的执行入口
        :type AppFile: str
        :param RoleArn: 执行spark作业的角色ID
        :type RoleArn: int
        :param AppDriverSize: spark作业driver资源规格大小, 可取small,medium,large,xlarge
        :type AppDriverSize: str
        :param AppExecutorSize: spark作业executor资源规格大小, 可取small,medium,large,xlarge
        :type AppExecutorSize: str
        :param AppExecutorNums: spark作业executor个数
        :type AppExecutorNums: int
        :param Eni: 该字段已下线，请使用字段Datasource
        :type Eni: str
        :param IsLocal: 是否本地上传，可去cos,lakefs
        :type IsLocal: str
        :param MainClass: spark jar作业时的主类
        :type MainClass: str
        :param AppConf: spark配置，以换行符分隔
        :type AppConf: str
        :param IsLocalJars: 是否本地上传，包含cos,lakefs
        :type IsLocalJars: str
        :param AppJars: spark jar作业依赖jars，以逗号分隔
        :type AppJars: str
        :param IsLocalFiles: 是否本地上传，包含cos,lakefs
        :type IsLocalFiles: str
        :param AppFiles: spark作业依赖资源，以逗号分隔
        :type AppFiles: str
        :param CmdArgs: spark作业命令行参数
        :type CmdArgs: str
        :param MaxRetries: 只对spark流任务生效
        :type MaxRetries: int
        :param DataSource: 数据源名
        :type DataSource: str
        :param IsLocalPythonFiles: pyspark：依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
        :type IsLocalPythonFiles: str
        :param AppPythonFiles: pyspark：python依赖, 除py文件外，还支持zip/egg等归档格式，多文件以逗号分隔
        :type AppPythonFiles: str
        :param IsLocalArchives: archives：依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
        :type IsLocalArchives: str
        :param AppArchives: archives：依赖资源
        :type AppArchives: str
        :param SparkImage: Spark Image 版本
        :type SparkImage: str
        :param SparkImageVersion: Spark Image 版本名称
        :type SparkImageVersion: str
        :param AppExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于AppExecutorNums
        :type AppExecutorMaxNumbers: int
        """
        self.AppName = None
        self.AppType = None
        self.DataEngine = None
        self.AppFile = None
        self.RoleArn = None
        self.AppDriverSize = None
        self.AppExecutorSize = None
        self.AppExecutorNums = None
        self.Eni = None
        self.IsLocal = None
        self.MainClass = None
        self.AppConf = None
        self.IsLocalJars = None
        self.AppJars = None
        self.IsLocalFiles = None
        self.AppFiles = None
        self.CmdArgs = None
        self.MaxRetries = None
        self.DataSource = None
        self.IsLocalPythonFiles = None
        self.AppPythonFiles = None
        self.IsLocalArchives = None
        self.AppArchives = None
        self.SparkImage = None
        self.SparkImageVersion = None
        self.AppExecutorMaxNumbers = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.AppType = params.get("AppType")
        self.DataEngine = params.get("DataEngine")
        self.AppFile = params.get("AppFile")
        self.RoleArn = params.get("RoleArn")
        self.AppDriverSize = params.get("AppDriverSize")
        self.AppExecutorSize = params.get("AppExecutorSize")
        self.AppExecutorNums = params.get("AppExecutorNums")
        self.Eni = params.get("Eni")
        self.IsLocal = params.get("IsLocal")
        self.MainClass = params.get("MainClass")
        self.AppConf = params.get("AppConf")
        self.IsLocalJars = params.get("IsLocalJars")
        self.AppJars = params.get("AppJars")
        self.IsLocalFiles = params.get("IsLocalFiles")
        self.AppFiles = params.get("AppFiles")
        self.CmdArgs = params.get("CmdArgs")
        self.MaxRetries = params.get("MaxRetries")
        self.DataSource = params.get("DataSource")
        self.IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self.AppPythonFiles = params.get("AppPythonFiles")
        self.IsLocalArchives = params.get("IsLocalArchives")
        self.AppArchives = params.get("AppArchives")
        self.SparkImage = params.get("SparkImage")
        self.SparkImageVersion = params.get("SparkImageVersion")
        self.AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkAppResponse(AbstractModel):
    """CreateSparkApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param SparkAppId: App唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SparkAppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SparkAppId = params.get("SparkAppId")
        self.RequestId = params.get("RequestId")


class CreateSparkAppTaskRequest(AbstractModel):
    """CreateSparkAppTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobName: spark作业名
        :type JobName: str
        :param CmdArgs: spark作业的命令行参数，以空格分隔；一般用于周期性调用使用
        :type CmdArgs: str
        """
        self.JobName = None
        self.CmdArgs = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        self.CmdArgs = params.get("CmdArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkAppTaskResponse(AbstractModel):
    """CreateSparkAppTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批Id
        :type BatchId: str
        :param TaskId: 任务Id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateStoreLocationRequest(AbstractModel):
    """CreateStoreLocation请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param Task: 计算任务，该参数中包含任务类型及其相关配置信息
        :type Task: :class:`tencentcloud.dlc.v20210125.models.Task`
        :param DatabaseName: 数据库名称。如果SQL语句中有数据库名称，优先使用SQL语句中的数据库，否则使用该参数指定的数据库（注：当提交建库sql时，该字段传空字符串）。
        :type DatabaseName: str
        :param DatasourceConnectionName: 默认数据源名称。
        :type DatasourceConnectionName: str
        :param DataEngineName: 数据引擎名称，不填提交到默认集群
        :type DataEngineName: str
        """
        self.Task = None
        self.DatabaseName = None
        self.DatasourceConnectionName = None
        self.DataEngineName = None


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self.Task = Task()
            self.Task._deserialize(params.get("Task"))
        self.DatabaseName = params.get("DatabaseName")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.DataEngineName = params.get("DataEngineName")
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
        r"""
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


class CreateTasksInOrderRequest(AbstractModel):
    """CreateTasksInOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatabaseName: 数据库名称。如果SQL语句中有数据库名称，优先使用SQL语句中的数据库，否则使用该参数指定的数据库。
        :type DatabaseName: str
        :param Tasks: SQL任务信息
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TasksInfo`
        :param DatasourceConnectionName: 数据源名称，默认为COSDataCatalog
        :type DatasourceConnectionName: str
        """
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
        r"""
        :param BatchId: 本批次提交的任务的批次Id
        :type BatchId: str
        :param TaskIdSet: 任务Id集合，按照执行顺序排列
        :type TaskIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param DatabaseName: 数据库名称。如果SQL语句中有数据库名称，优先使用SQL语句中的数据库，否则使用该参数指定的数据库（注：当提交建库sql时，该字段传空字符串）。
        :type DatabaseName: str
        :param Tasks: SQL任务信息
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TasksInfo`
        :param DatasourceConnectionName: 数据源名称，默认为DataLakeCatalog
        :type DatasourceConnectionName: str
        :param DataEngineName: 计算引擎名称，不填任务提交到默认集群
        :type DataEngineName: str
        """
        self.DatabaseName = None
        self.Tasks = None
        self.DatasourceConnectionName = None
        self.DataEngineName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        if params.get("Tasks") is not None:
            self.Tasks = TasksInfo()
            self.Tasks._deserialize(params.get("Tasks"))
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.DataEngineName = params.get("DataEngineName")
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
        r"""
        :param BatchId: 本批次提交的任务的批次Id
        :type BatchId: str
        :param TaskIdSet: 任务Id集合，按照执行顺序排列
        :type TaskIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param UserId: 需要授权的子用户uin，可以通过腾讯云控制台右上角 → “账号信息” → “账号ID进行查看”。
        :type UserId: str
        :param UserDescription: 用户描述信息，方便区分不同用户
        :type UserDescription: str
        :param PolicySet: 绑定到用户的权限集合
        :type PolicySet: list of Policy
        :param UserType: 用户类型。ADMIN：管理员 COMMON：一般用户。当用户类型为管理员的时候，不能设置权限集合和绑定的工作组集合，管理员默认拥有所有权限。该参数不填默认为COMMON
        :type UserType: str
        :param WorkGroupIds: 绑定到用户的工作组ID集合。
        :type WorkGroupIds: list of int
        :param UserAlias: 用户别名，字符长度小50
        :type UserAlias: str
        """
        self.UserId = None
        self.UserDescription = None
        self.PolicySet = None
        self.UserType = None
        self.WorkGroupIds = None
        self.UserAlias = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserDescription = params.get("UserDescription")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        self.UserType = params.get("UserType")
        self.WorkGroupIds = params.get("WorkGroupIds")
        self.UserAlias = params.get("UserAlias")
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
        r"""
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
        r"""
        :param WorkGroupName: 工作组名称
        :type WorkGroupName: str
        :param WorkGroupDescription: 工作组描述
        :type WorkGroupDescription: str
        :param PolicySet: 工作组绑定的鉴权策略集合
        :type PolicySet: list of Policy
        :param UserIds: 需要绑定到工作组的用户Id集合
        :type UserIds: list of str
        """
        self.WorkGroupName = None
        self.WorkGroupDescription = None
        self.PolicySet = None
        self.UserIds = None


    def _deserialize(self, params):
        self.WorkGroupName = params.get("WorkGroupName")
        self.WorkGroupDescription = params.get("WorkGroupDescription")
        if params.get("PolicySet") is not None:
            self.PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicySet.append(obj)
        self.UserIds = params.get("UserIds")
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
        r"""
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


class CrontabResumeSuspendStrategy(AbstractModel):
    """定时启停策略信息

    """

    def __init__(self):
        r"""
        :param ResumeTime: 定时拉起时间：如：周一8点
注意：此字段可能返回 null，表示取不到有效值。
        :type ResumeTime: str
        :param SuspendTime: 定时挂起时间：如：周一20点
注意：此字段可能返回 null，表示取不到有效值。
        :type SuspendTime: str
        :param SuspendStrategy: 挂起配置：0（默认）：等待任务结束后挂起、1：强制挂起
注意：此字段可能返回 null，表示取不到有效值。
        :type SuspendStrategy: int
        """
        self.ResumeTime = None
        self.SuspendTime = None
        self.SuspendStrategy = None


    def _deserialize(self, params):
        self.ResumeTime = params.get("ResumeTime")
        self.SuspendTime = params.get("SuspendTime")
        self.SuspendStrategy = params.get("SuspendStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSColumn(AbstractModel):
    """迁移列对象

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Position: 排序
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: int
        :param Params: 附加参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of KVPair
        :param BizParams: 业务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type BizParams: list of KVPair
        :param IsPartition: 是否分区
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPartition: bool
        """
        self.Name = None
        self.Description = None
        self.Type = None
        self.Position = None
        self.Params = None
        self.BizParams = None
        self.IsPartition = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.Position = params.get("Position")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self.Params.append(obj)
        if params.get("BizParams") is not None:
            self.BizParams = []
            for item in params.get("BizParams"):
                obj = KVPair()
                obj._deserialize(item)
                self.BizParams.append(obj)
        self.IsPartition = params.get("IsPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSColumnOrder(AbstractModel):
    """列排序对象

    """

    def __init__(self):
        r"""
        :param Col: 列名
注意：此字段可能返回 null，表示取不到有效值。
        :type Col: str
        :param Order: 排序
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: int
        """
        self.Col = None
        self.Order = None


    def _deserialize(self, params):
        self.Col = params.get("Col")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSPartition(AbstractModel):
    """迁移元数据分区对象

    """

    def __init__(self):
        r"""
        :param DatabaseName: 数据库名称
        :type DatabaseName: str
        :param SchemaName: 数据目录名称
        :type SchemaName: str
        :param TableName: 表名称
        :type TableName: str
        :param DataVersion: 数据版本
        :type DataVersion: int
        :param Name: 分区名称
        :type Name: str
        :param Values: 值列表
        :type Values: list of str
        :param StorageSize: 存储大小
        :type StorageSize: int
        :param RecordCount: 记录数量
        :type RecordCount: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifiedTime: 修改时间
        :type ModifiedTime: str
        :param LastAccessTime: 最后访问时间
        :type LastAccessTime: str
        :param Params: 附件属性
        :type Params: list of KVPair
        :param Sds: 存储对象
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        """
        self.DatabaseName = None
        self.SchemaName = None
        self.TableName = None
        self.DataVersion = None
        self.Name = None
        self.Values = None
        self.StorageSize = None
        self.RecordCount = None
        self.CreateTime = None
        self.ModifiedTime = None
        self.LastAccessTime = None
        self.Params = None
        self.Sds = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.SchemaName = params.get("SchemaName")
        self.TableName = params.get("TableName")
        self.DataVersion = params.get("DataVersion")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.StorageSize = params.get("StorageSize")
        self.RecordCount = params.get("RecordCount")
        self.CreateTime = params.get("CreateTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.LastAccessTime = params.get("LastAccessTime")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self.Params.append(obj)
        if params.get("Sds") is not None:
            self.Sds = DMSSds()
            self.Sds._deserialize(params.get("Sds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSSds(AbstractModel):
    """元数据存储描述属性

    """

    def __init__(self):
        r"""
        :param Location: 存储地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param InputFormat: 输入格式
注意：此字段可能返回 null，表示取不到有效值。
        :type InputFormat: str
        :param OutputFormat: 输出格式
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputFormat: str
        :param NumBuckets: bucket数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NumBuckets: int
        :param Compressed: 是是否压缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Compressed: bool
        :param StoredAsSubDirectories: 是否有子目录
注意：此字段可能返回 null，表示取不到有效值。
        :type StoredAsSubDirectories: bool
        :param SerdeLib: 序列化lib
注意：此字段可能返回 null，表示取不到有效值。
        :type SerdeLib: str
        :param SerdeName: 序列化名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SerdeName: str
        :param BucketCols: 桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketCols: list of str
        :param SerdeParams: 序列化参数
注意：此字段可能返回 null，表示取不到有效值。
        :type SerdeParams: list of KVPair
        :param Params: 附加参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of KVPair
        :param SortCols: 列排序(Expired)
注意：此字段可能返回 null，表示取不到有效值。
        :type SortCols: :class:`tencentcloud.dlc.v20210125.models.DMSColumnOrder`
        :param Cols: 列
注意：此字段可能返回 null，表示取不到有效值。
        :type Cols: list of DMSColumn
        :param SortColumns: 列排序字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SortColumns: list of DMSColumnOrder
        """
        self.Location = None
        self.InputFormat = None
        self.OutputFormat = None
        self.NumBuckets = None
        self.Compressed = None
        self.StoredAsSubDirectories = None
        self.SerdeLib = None
        self.SerdeName = None
        self.BucketCols = None
        self.SerdeParams = None
        self.Params = None
        self.SortCols = None
        self.Cols = None
        self.SortColumns = None


    def _deserialize(self, params):
        self.Location = params.get("Location")
        self.InputFormat = params.get("InputFormat")
        self.OutputFormat = params.get("OutputFormat")
        self.NumBuckets = params.get("NumBuckets")
        self.Compressed = params.get("Compressed")
        self.StoredAsSubDirectories = params.get("StoredAsSubDirectories")
        self.SerdeLib = params.get("SerdeLib")
        self.SerdeName = params.get("SerdeName")
        self.BucketCols = params.get("BucketCols")
        if params.get("SerdeParams") is not None:
            self.SerdeParams = []
            for item in params.get("SerdeParams"):
                obj = KVPair()
                obj._deserialize(item)
                self.SerdeParams.append(obj)
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self.Params.append(obj)
        if params.get("SortCols") is not None:
            self.SortCols = DMSColumnOrder()
            self.SortCols._deserialize(params.get("SortCols"))
        if params.get("Cols") is not None:
            self.Cols = []
            for item in params.get("Cols"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.Cols.append(obj)
        if params.get("SortColumns") is not None:
            self.SortColumns = []
            for item in params.get("SortColumns"):
                obj = DMSColumnOrder()
                obj._deserialize(item)
                self.SortColumns.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSTable(AbstractModel):
    """DMSTable基本信息

    """

    def __init__(self):
        r"""
        :param ViewOriginalText: 视图文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewOriginalText: str
        :param ViewExpandedText: 视图文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewExpandedText: str
        :param Retention: hive维护版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Retention: int
        :param Sds: 存储对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        :param PartitionKeys: 分区列
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionKeys: list of DMSColumn
        :param Partitions: 分区
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of DMSPartition
        :param Type: 表类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param DbName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param SchemaName: Schema名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param StorageSize: 存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSize: int
        :param RecordCount: 记录数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCount: int
        :param LifeTime: 生命周期
注意：此字段可能返回 null，表示取不到有效值。
        :type LifeTime: int
        :param LastAccessTime: 最后访问时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastAccessTime: str
        :param DataUpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUpdateTime: str
        :param StructUpdateTime: 结构更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StructUpdateTime: str
        :param Columns: 列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of DMSColumn
        :param Name: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.ViewOriginalText = None
        self.ViewExpandedText = None
        self.Retention = None
        self.Sds = None
        self.PartitionKeys = None
        self.Partitions = None
        self.Type = None
        self.DbName = None
        self.SchemaName = None
        self.StorageSize = None
        self.RecordCount = None
        self.LifeTime = None
        self.LastAccessTime = None
        self.DataUpdateTime = None
        self.StructUpdateTime = None
        self.Columns = None
        self.Name = None


    def _deserialize(self, params):
        self.ViewOriginalText = params.get("ViewOriginalText")
        self.ViewExpandedText = params.get("ViewExpandedText")
        self.Retention = params.get("Retention")
        if params.get("Sds") is not None:
            self.Sds = DMSSds()
            self.Sds._deserialize(params.get("Sds"))
        if params.get("PartitionKeys") is not None:
            self.PartitionKeys = []
            for item in params.get("PartitionKeys"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.PartitionKeys.append(obj)
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.Type = params.get("Type")
        self.DbName = params.get("DbName")
        self.SchemaName = params.get("SchemaName")
        self.StorageSize = params.get("StorageSize")
        self.RecordCount = params.get("RecordCount")
        self.LifeTime = params.get("LifeTime")
        self.LastAccessTime = params.get("LastAccessTime")
        self.DataUpdateTime = params.get("DataUpdateTime")
        self.StructUpdateTime = params.get("StructUpdateTime")
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.Columns.append(obj)
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSTableInfo(AbstractModel):
    """DMSTable信息

    """

    def __init__(self):
        r"""
        :param Table: DMS表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: :class:`tencentcloud.dlc.v20210125.models.DMSTable`
        :param Asset: 基础对象信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        """
        self.Table = None
        self.Asset = None


    def _deserialize(self, params):
        if params.get("Table") is not None:
            self.Table = DMSTable()
            self.Table._deserialize(params.get("Table"))
        if params.get("Asset") is not None:
            self.Asset = Asset()
            self.Asset._deserialize(params.get("Asset"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineInfo(AbstractModel):
    """DataEngine详细信息

    """

    def __init__(self):
        r"""
        :param DataEngineName: DataEngine名称
        :type DataEngineName: str
        :param EngineType: 引擎类型 spark/presto
        :type EngineType: str
        :param ClusterType: 集群资源类型 spark_private/presto_private/presto_cu/spark_cu
        :type ClusterType: str
        :param QuotaId: 引用ID
        :type QuotaId: str
        :param State: 数据引擎状态  -2已删除 -1失败 0初始化中 1挂起 2运行中 3准备删除 4删除中
        :type State: int
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param UpdateTime: 更新时间
        :type UpdateTime: int
        :param Size: 集群规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Mode: 计费模式 0共享模式 1按量计费 2包年包月
        :type Mode: int
        :param MinClusters: 最小集群数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinClusters: int
        :param MaxClusters: 最大集群数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxClusters: int
        :param AutoResume: 是否自动恢复
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoResume: bool
        :param SpendAfter: 自动恢复时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SpendAfter: int
        :param CidrBlock: 集群网段
注意：此字段可能返回 null，表示取不到有效值。
        :type CidrBlock: str
        :param DefaultDataEngine: 是否为默认引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDataEngine: bool
        :param Message: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param DataEngineId: 引擎id
        :type DataEngineId: str
        :param SubAccountUin: 操作者
        :type SubAccountUin: str
        :param ExpireTime: 到期时间
        :type ExpireTime: str
        :param IsolatedTime: 隔离时间
        :type IsolatedTime: str
        :param ReversalTime: 冲正时间
        :type ReversalTime: str
        :param UserAlias: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param TagList: 标签对集合
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of TagInfo
        :param Permissions: 引擎拥有的权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Permissions: list of str
        :param AutoSuspend: 是否自定挂起集群：false（默认）：不自动挂起、true：自动挂起
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSuspend: bool
        :param CrontabResumeSuspend: 定时启停集群策略：0（默认）：关闭定时策略、1：开启定时策略（注：定时启停策略与自动挂起策略互斥）
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabResumeSuspend: int
        :param CrontabResumeSuspendStrategy: 定时启停策略，复杂类型：包含启停时间、挂起集群策略
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabResumeSuspendStrategy: :class:`tencentcloud.dlc.v20210125.models.CrontabResumeSuspendStrategy`
        :param EngineExecType: 引擎执行任务类型，有效值：SQL/BATCH
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineExecType: str
        :param RenewFlag: 自动续费标志，0，初始状态，默认不自动续费，若用户有预付费不停服特权，自动续费。1：自动续费。2：明确不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param AutoSuspendTime: 集群自动挂起时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSuspendTime: int
        :param NetworkConnectionSet: 网络连接配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConnectionSet: list of NetworkConnection
        :param UiURL: ui的跳转地址
注意：此字段可能返回 null，表示取不到有效值。
        :type UiURL: str
        """
        self.DataEngineName = None
        self.EngineType = None
        self.ClusterType = None
        self.QuotaId = None
        self.State = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Size = None
        self.Mode = None
        self.MinClusters = None
        self.MaxClusters = None
        self.AutoResume = None
        self.SpendAfter = None
        self.CidrBlock = None
        self.DefaultDataEngine = None
        self.Message = None
        self.DataEngineId = None
        self.SubAccountUin = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.ReversalTime = None
        self.UserAlias = None
        self.TagList = None
        self.Permissions = None
        self.AutoSuspend = None
        self.CrontabResumeSuspend = None
        self.CrontabResumeSuspendStrategy = None
        self.EngineExecType = None
        self.RenewFlag = None
        self.AutoSuspendTime = None
        self.NetworkConnectionSet = None
        self.UiURL = None


    def _deserialize(self, params):
        self.DataEngineName = params.get("DataEngineName")
        self.EngineType = params.get("EngineType")
        self.ClusterType = params.get("ClusterType")
        self.QuotaId = params.get("QuotaId")
        self.State = params.get("State")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Size = params.get("Size")
        self.Mode = params.get("Mode")
        self.MinClusters = params.get("MinClusters")
        self.MaxClusters = params.get("MaxClusters")
        self.AutoResume = params.get("AutoResume")
        self.SpendAfter = params.get("SpendAfter")
        self.CidrBlock = params.get("CidrBlock")
        self.DefaultDataEngine = params.get("DefaultDataEngine")
        self.Message = params.get("Message")
        self.DataEngineId = params.get("DataEngineId")
        self.SubAccountUin = params.get("SubAccountUin")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.ReversalTime = params.get("ReversalTime")
        self.UserAlias = params.get("UserAlias")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.Permissions = params.get("Permissions")
        self.AutoSuspend = params.get("AutoSuspend")
        self.CrontabResumeSuspend = params.get("CrontabResumeSuspend")
        if params.get("CrontabResumeSuspendStrategy") is not None:
            self.CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy()
            self.CrontabResumeSuspendStrategy._deserialize(params.get("CrontabResumeSuspendStrategy"))
        self.EngineExecType = params.get("EngineExecType")
        self.RenewFlag = params.get("RenewFlag")
        self.AutoSuspendTime = params.get("AutoSuspendTime")
        if params.get("NetworkConnectionSet") is not None:
            self.NetworkConnectionSet = []
            for item in params.get("NetworkConnectionSet"):
                obj = NetworkConnection()
                obj._deserialize(item)
                self.NetworkConnectionSet.append(obj)
        self.UiURL = params.get("UiURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataFormat(AbstractModel):
    """数据表数据格式。

    """

    def __init__(self):
        r"""
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
        


class DataGovernPolicy(AbstractModel):
    """数据治理规则

    """


class DatabaseInfo(AbstractModel):
    """数据库对象

    """

    def __init__(self):
        r"""
        :param DatabaseName: 数据库名称，长度0~128，支持数字、字母下划线，不允许数字大头，统一转换为小写。
        :type DatabaseName: str
        :param Comment: 数据库描述信息，长度 0~500。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param Properties: 数据库属性列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param Location: 数据库cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        """
        self.DatabaseName = None
        self.Comment = None
        self.Properties = None
        self.Location = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.Comment = params.get("Comment")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self.Properties.append(obj)
        self.Location = params.get("Location")
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
        r"""
        :param DatabaseName: 数据库名称。
        :type DatabaseName: str
        :param Comment: 数据库描述信息，长度 0~256。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param Properties: 允许针对数据库的属性元数据信息进行指定。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param CreateTime: 数据库创建时间戳，单位：s。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ModifiedTime: 数据库更新时间戳，单位：s。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param Location: cos存储路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param UserAlias: 建库用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param UserSubUin: 建库用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSubUin: str
        :param GovernPolicy: 数据治理配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type GovernPolicy: :class:`tencentcloud.dlc.v20210125.models.DataGovernPolicy`
        :param DatabaseId: 数据库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        """
        self.DatabaseName = None
        self.Comment = None
        self.Properties = None
        self.CreateTime = None
        self.ModifiedTime = None
        self.Location = None
        self.UserAlias = None
        self.UserSubUin = None
        self.GovernPolicy = None
        self.DatabaseId = None


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
        self.Location = params.get("Location")
        self.UserAlias = params.get("UserAlias")
        self.UserSubUin = params.get("UserSubUin")
        if params.get("GovernPolicy") is not None:
            self.GovernPolicy = DataGovernPolicy()
            self.GovernPolicy._deserialize(params.get("GovernPolicy"))
        self.DatabaseId = params.get("DatabaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookSessionRequest(AbstractModel):
    """DeleteNotebookSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        """
        self.SessionId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookSessionResponse(AbstractModel):
    """DeleteNotebookSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScriptRequest(AbstractModel):
    """DeleteScript请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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


class DeleteSparkAppRequest(AbstractModel):
    """DeleteSparkApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: spark应用名
        :type AppName: str
        """
        self.AppName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSparkAppResponse(AbstractModel):
    """DeleteSparkApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDMSDatabaseRequest(AbstractModel):
    """DescribeDMSDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 数据库名称
        :type Name: str
        :param SchemaName: schema名称
        :type SchemaName: str
        :param Pattern: 匹配规则
        :type Pattern: str
        """
        self.Name = None
        self.SchemaName = None
        self.Pattern = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SchemaName = params.get("SchemaName")
        self.Pattern = params.get("Pattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDMSDatabaseResponse(AbstractModel):
    """DescribeDMSDatabase返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param SchemaName: schema名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param Location: 存储地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param Asset: 数据对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.SchemaName = None
        self.Location = None
        self.Asset = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SchemaName = params.get("SchemaName")
        self.Location = params.get("Location")
        if params.get("Asset") is not None:
            self.Asset = Asset()
            self.Asset._deserialize(params.get("Asset"))
        self.RequestId = params.get("RequestId")


class DescribeDMSPartitionsRequest(AbstractModel):
    """DescribeDMSPartitions请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatabaseName: 数据库名
        :type DatabaseName: str
        :param TableName: 表名称
        :type TableName: str
        :param SchemaName: schema名称
        :type SchemaName: str
        :param Name: 名称
        :type Name: str
        :param Values: 单个分区名称，精准匹配
        :type Values: list of str
        :param PartitionNames: 多个分区名称，精准匹配
        :type PartitionNames: list of str
        :param PartValues: 多个分区字段的匹配，模糊匹配
        :type PartValues: list of str
        :param Filter: 过滤SQL
        :type Filter: str
        :param MaxParts: 最大分区数量
        :type MaxParts: int
        :param Offset: 翻页跳过数量
        :type Offset: int
        :param Limit: 页面数量
        :type Limit: int
        :param Expression: 表达式
        :type Expression: str
        """
        self.DatabaseName = None
        self.TableName = None
        self.SchemaName = None
        self.Name = None
        self.Values = None
        self.PartitionNames = None
        self.PartValues = None
        self.Filter = None
        self.MaxParts = None
        self.Offset = None
        self.Limit = None
        self.Expression = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.TableName = params.get("TableName")
        self.SchemaName = params.get("SchemaName")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.PartitionNames = params.get("PartitionNames")
        self.PartValues = params.get("PartValues")
        self.Filter = params.get("Filter")
        self.MaxParts = params.get("MaxParts")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDMSPartitionsResponse(AbstractModel):
    """DescribeDMSPartitions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Partitions: 分区信息
        :type Partitions: list of DMSPartition
        :param Total: 总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Partitions = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDMSTableRequest(AbstractModel):
    """DescribeDMSTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param DbName: 数据库名称
        :type DbName: str
        :param SchemaName: 数据库schema名称
        :type SchemaName: str
        :param Name: 表名称
        :type Name: str
        :param Catalog: 数据目录
        :type Catalog: str
        :param Keyword: 查询关键词
        :type Keyword: str
        :param Pattern: 查询模式
        :type Pattern: str
        :param Type: 表类型
        :type Type: str
        """
        self.DbName = None
        self.SchemaName = None
        self.Name = None
        self.Catalog = None
        self.Keyword = None
        self.Pattern = None
        self.Type = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.SchemaName = params.get("SchemaName")
        self.Name = params.get("Name")
        self.Catalog = params.get("Catalog")
        self.Keyword = params.get("Keyword")
        self.Pattern = params.get("Pattern")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDMSTableResponse(AbstractModel):
    """DescribeDMSTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param Asset: 基础对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param ViewOriginalText: 视图文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewOriginalText: str
        :param ViewExpandedText: 视图文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewExpandedText: str
        :param Retention: hive维护版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Retention: int
        :param Sds: 存储对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        :param PartitionKeys: 分区列
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionKeys: list of DMSColumn
        :param Partitions: 分区
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of DMSPartition
        :param Type: 表类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param DbName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param SchemaName: Schame名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param StorageSize: 存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSize: int
        :param RecordCount: 记录数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCount: int
        :param LifeTime: 生命周期
注意：此字段可能返回 null，表示取不到有效值。
        :type LifeTime: int
        :param LastAccessTime: 最后访问时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastAccessTime: str
        :param DataUpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUpdateTime: str
        :param StructUpdateTime: 结构更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StructUpdateTime: str
        :param Columns: 列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of DMSColumn
        :param Name: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Asset = None
        self.ViewOriginalText = None
        self.ViewExpandedText = None
        self.Retention = None
        self.Sds = None
        self.PartitionKeys = None
        self.Partitions = None
        self.Type = None
        self.DbName = None
        self.SchemaName = None
        self.StorageSize = None
        self.RecordCount = None
        self.LifeTime = None
        self.LastAccessTime = None
        self.DataUpdateTime = None
        self.StructUpdateTime = None
        self.Columns = None
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Asset") is not None:
            self.Asset = Asset()
            self.Asset._deserialize(params.get("Asset"))
        self.ViewOriginalText = params.get("ViewOriginalText")
        self.ViewExpandedText = params.get("ViewExpandedText")
        self.Retention = params.get("Retention")
        if params.get("Sds") is not None:
            self.Sds = DMSSds()
            self.Sds._deserialize(params.get("Sds"))
        if params.get("PartitionKeys") is not None:
            self.PartitionKeys = []
            for item in params.get("PartitionKeys"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.PartitionKeys.append(obj)
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.Type = params.get("Type")
        self.DbName = params.get("DbName")
        self.SchemaName = params.get("SchemaName")
        self.StorageSize = params.get("StorageSize")
        self.RecordCount = params.get("RecordCount")
        self.LifeTime = params.get("LifeTime")
        self.LastAccessTime = params.get("LastAccessTime")
        self.DataUpdateTime = params.get("DataUpdateTime")
        self.StructUpdateTime = params.get("StructUpdateTime")
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = DMSColumn()
                obj._deserialize(item)
                self.Columns.append(obj)
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class DescribeDMSTablesRequest(AbstractModel):
    """DescribeDMSTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param DbName: 数据库名称
        :type DbName: str
        :param SchemaName: 数据库schema名称
        :type SchemaName: str
        :param Name: 表名称
        :type Name: str
        :param Catalog: 数据目录
        :type Catalog: str
        :param Keyword: 查询关键词
        :type Keyword: str
        :param Pattern: 查询模式
        :type Pattern: str
        :param Type: 表类型
        :type Type: str
        :param StartTime: 筛选参数：更新开始时间
        :type StartTime: str
        :param EndTime: 筛选参数：更新结束时间
        :type EndTime: str
        :param Limit: 分页参数
        :type Limit: int
        :param Offset: 分页参数
        :type Offset: int
        :param Sort: 排序字段：create_time：创建时间
        :type Sort: str
        :param Asc: 排序字段：true：升序（默认），false：降序
        :type Asc: bool
        """
        self.DbName = None
        self.SchemaName = None
        self.Name = None
        self.Catalog = None
        self.Keyword = None
        self.Pattern = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Sort = None
        self.Asc = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.SchemaName = params.get("SchemaName")
        self.Name = params.get("Name")
        self.Catalog = params.get("Catalog")
        self.Keyword = params.get("Keyword")
        self.Pattern = params.get("Pattern")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Sort = params.get("Sort")
        self.Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDMSTablesResponse(AbstractModel):
    """DescribeDMSTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param TableList: DMS元数据列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TableList: list of DMSTableInfo
        :param TotalCount: 统计值
注意：此字段可能返回 null，表示取不到有效值。
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
                obj = DMSTableInfo()
                obj._deserialize(item)
                self.TableList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDataEnginesRequest(AbstractModel):
    """DescribeDataEngines请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 滤类型，传参Name应为以下其中一个,
data-engine-name - String 
engine-type - String
state - String 
mode - String 
create-time - String 
message - String
        :type Filters: list of Filter
        :param SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc。
        :type Sorting: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param DatasourceConnectionName: 已废弃，请使用DatasourceConnectionNameSet
        :type DatasourceConnectionName: str
        :param ExcludePublicEngine: 是否不返回共享引擎，true不返回共享引擎，false可以返回共享引擎
        :type ExcludePublicEngine: bool
        :param AccessTypes: 参数应该为引擎权限类型，有效类型："USE", "MODIFY", "OPERATE", "MONITOR", "DELETE"
        :type AccessTypes: list of str
        :param EngineExecType: 引擎执行任务类型，有效值：SQL/BATCH
        :type EngineExecType: str
        :param EngineType: 引擎类型，有效值：spark/presto
        :type EngineType: str
        :param DatasourceConnectionNameSet: 网络配置列表，若传入该参数，则返回网络配置关联的计算引擎
        :type DatasourceConnectionNameSet: list of str
        """
        self.Offset = None
        self.Filters = None
        self.SortBy = None
        self.Sorting = None
        self.Limit = None
        self.DatasourceConnectionName = None
        self.ExcludePublicEngine = None
        self.AccessTypes = None
        self.EngineExecType = None
        self.EngineType = None
        self.DatasourceConnectionNameSet = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortBy = params.get("SortBy")
        self.Sorting = params.get("Sorting")
        self.Limit = params.get("Limit")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.ExcludePublicEngine = params.get("ExcludePublicEngine")
        self.AccessTypes = params.get("AccessTypes")
        self.EngineExecType = params.get("EngineExecType")
        self.EngineType = params.get("EngineType")
        self.DatasourceConnectionNameSet = params.get("DatasourceConnectionNameSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEnginesResponse(AbstractModel):
    """DescribeDataEngines返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataEngines: 数据引擎列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngines: list of DataEngineInfo
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataEngines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataEngines") is not None:
            self.DataEngines = []
            for item in params.get("DataEngines"):
                obj = DataEngineInfo()
                obj._deserialize(item)
                self.DataEngines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 数据偏移量，从0开始，默认为0。
        :type Offset: int
        :param KeyWord: 模糊匹配，库名关键字。
        :type KeyWord: str
        :param DatasourceConnectionName: 数据源唯名称，该名称可以通过DescribeDatasourceConnection接口查询到。默认为DataLakeCatalog
        :type DatasourceConnectionName: str
        :param Sort: 排序字段，当前版本仅支持按库名排序
        :type Sort: str
        :param Asc: 排序类型：false：降序（默认）、true：升序
        :type Asc: bool
        """
        self.Limit = None
        self.Offset = None
        self.KeyWord = None
        self.DatasourceConnectionName = None
        self.Sort = None
        self.Asc = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.KeyWord = params.get("KeyWord")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.Sort = params.get("Sort")
        self.Asc = params.get("Asc")
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
        r"""
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


class DescribeNotebookSessionLogRequest(AbstractModel):
    """DescribeNotebookSessionLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param Limit: 分页参数，默认200
        :type Limit: int
        :param Offset: 分页参数，默认0
        :type Offset: int
        """
        self.SessionId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionLogResponse(AbstractModel):
    """DescribeNotebookSessionLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Logs: 日志信息，默认获取最新的200条
        :type Logs: list of str
        :param Limit: 分页参数，默认200
        :type Limit: int
        :param Offset: 分页参数，默认0
        :type Offset: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Logs = None
        self.Limit = None
        self.Offset = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Logs = params.get("Logs")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RequestId = params.get("RequestId")


class DescribeNotebookSessionRequest(AbstractModel):
    """DescribeNotebookSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        """
        self.SessionId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionResponse(AbstractModel):
    """DescribeNotebookSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param Session: Session详情信息
        :type Session: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Session = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Session") is not None:
            self.Session = NotebookSessionInfo()
            self.Session._deserialize(params.get("Session"))
        self.RequestId = params.get("RequestId")


class DescribeNotebookSessionStatementRequest(AbstractModel):
    """DescribeNotebookSessionStatement请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param StatementId: Session Statement唯一标识
        :type StatementId: str
        """
        self.SessionId = None
        self.StatementId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.StatementId = params.get("StatementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionStatementResponse(AbstractModel):
    """DescribeNotebookSessionStatement返回参数结构体

    """

    def __init__(self):
        r"""
        :param NotebookSessionStatement: Session Statement详情
        :type NotebookSessionStatement: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionStatementInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookSessionStatement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotebookSessionStatement") is not None:
            self.NotebookSessionStatement = NotebookSessionStatementInfo()
            self.NotebookSessionStatement._deserialize(params.get("NotebookSessionStatement"))
        self.RequestId = params.get("RequestId")


class DescribeNotebookSessionStatementSqlResultRequest(AbstractModel):
    """DescribeNotebookSessionStatementSqlResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务唯一ID
        :type TaskId: str
        :param MaxResults: 返回结果的最大行数，范围0~1000，默认为1000.
        :type MaxResults: int
        :param NextToken: 上一次请求响应返回的分页信息。第一次可以不带，从头开始返回数据，每次返回MaxResults字段设置的数据量。
        :type NextToken: str
        """
        self.TaskId = None
        self.MaxResults = None
        self.NextToken = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.MaxResults = params.get("MaxResults")
        self.NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionStatementSqlResultResponse(AbstractModel):
    """DescribeNotebookSessionStatementSqlResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: str
        :param ResultSet: 结果数据
        :type ResultSet: str
        :param ResultSchema: schema
        :type ResultSchema: list of Column
        :param NextToken: 分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param OutputPath: 存储结果地址
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputPath: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.ResultSet = None
        self.ResultSchema = None
        self.NextToken = None
        self.OutputPath = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ResultSet = params.get("ResultSet")
        if params.get("ResultSchema") is not None:
            self.ResultSchema = []
            for item in params.get("ResultSchema"):
                obj = Column()
                obj._deserialize(item)
                self.ResultSchema.append(obj)
        self.NextToken = params.get("NextToken")
        self.OutputPath = params.get("OutputPath")
        self.RequestId = params.get("RequestId")


class DescribeNotebookSessionStatementsRequest(AbstractModel):
    """DescribeNotebookSessionStatements请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param BatchId: 批任务id
        :type BatchId: str
        """
        self.SessionId = None
        self.BatchId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionStatementsResponse(AbstractModel):
    """DescribeNotebookSessionStatements返回参数结构体

    """

    def __init__(self):
        r"""
        :param NotebookSessionStatements: Session Statement详情
        :type NotebookSessionStatements: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionStatementBatchInformation`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotebookSessionStatements = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotebookSessionStatements") is not None:
            self.NotebookSessionStatements = NotebookSessionStatementBatchInformation()
            self.NotebookSessionStatements._deserialize(params.get("NotebookSessionStatements"))
        self.RequestId = params.get("RequestId")


class DescribeNotebookSessionsRequest(AbstractModel):
    """DescribeNotebookSessions请求参数结构体

    """

    def __init__(self):
        r"""
        :param DataEngineName: DLC Spark作业引擎名称
        :type DataEngineName: str
        :param State: Session状态，包含：not_started（未启动）、starting（已启动）、idle（等待输入）、busy(正在运行statement)、shutting_down（停止）、error（异常）、dead（已退出）、killed（被杀死）、success（正常停止）
        :type State: list of str
        :param SortFields: 排序字段（默认按创建时间）
        :type SortFields: list of str
        :param Asc: 排序字段：true：升序、false：降序（默认）
        :type Asc: bool
        :param Limit: 分页字段
        :type Limit: int
        :param Offset: 分页字段
        :type Offset: int
        """
        self.DataEngineName = None
        self.State = None
        self.SortFields = None
        self.Asc = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DataEngineName = params.get("DataEngineName")
        self.State = params.get("State")
        self.SortFields = params.get("SortFields")
        self.Asc = params.get("Asc")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionsResponse(AbstractModel):
    """DescribeNotebookSessions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalElements: session总数量
        :type TotalElements: int
        :param TotalPages: 总页数
        :type TotalPages: int
        :param Page: 当前页码
        :type Page: int
        :param Size: 当前页数量
        :type Size: int
        :param Sessions: session列表信息
        :type Sessions: list of NotebookSessions
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalElements = None
        self.TotalPages = None
        self.Page = None
        self.Size = None
        self.Sessions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalElements = params.get("TotalElements")
        self.TotalPages = params.get("TotalPages")
        self.Page = params.get("Page")
        self.Size = params.get("Size")
        if params.get("Sessions") is not None:
            self.Sessions = []
            for item in params.get("Sessions"):
                obj = NotebookSessions()
                obj._deserialize(item)
                self.Sessions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResultDownloadRequest(AbstractModel):
    """DescribeResultDownload请求参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadId: 查询任务Id
        :type DownloadId: str
        """
        self.DownloadId = None


    def _deserialize(self, params):
        self.DownloadId = params.get("DownloadId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResultDownloadResponse(AbstractModel):
    """DescribeResultDownload返回参数结构体

    """

    def __init__(self):
        r"""
        :param Path: 下载文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Status: 任务状态 init | queue | format | compress | success|  timeout | error
        :type Status: str
        :param Reason: 任务异常原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param SecretId: 临时AK
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretId: str
        :param SecretKey: 临时SK
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param Token: 临时Token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Path = None
        self.Status = None
        self.Reason = None
        self.SecretId = None
        self.SecretKey = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class DescribeScriptsRequest(AbstractModel):
    """DescribeScripts请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param SortBy: 按字段排序，支持如下字段类型，update-time
        :type SortBy: str
        :param Sorting: 排序方式，desc表示正序，asc表示反序，默认asc
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
        r"""
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


class DescribeSparkAppJobRequest(AbstractModel):
    """DescribeSparkAppJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: spark作业Id，与JobName同时存在时，JobName无效
        :type JobId: str
        :param JobName: spark作业名
        :type JobName: str
        """
        self.JobId = None
        self.JobName = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkAppJobResponse(AbstractModel):
    """DescribeSparkAppJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param Job: spark作业详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.dlc.v20210125.models.SparkJobInfo`
        :param IsExists: 查询的spark作业是否存在
        :type IsExists: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Job = None
        self.IsExists = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = SparkJobInfo()
            self.Job._deserialize(params.get("Job"))
        self.IsExists = params.get("IsExists")
        self.RequestId = params.get("RequestId")


class DescribeSparkAppJobsRequest(AbstractModel):
    """DescribeSparkAppJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param SortBy: 返回结果按照该字段排序
        :type SortBy: str
        :param Sorting: 正序或者倒序，例如：desc
        :type Sorting: str
        :param Filters: 按照该参数过滤,支持spark-job-name
        :type Filters: list of Filter
        :param StartTime: 更新时间起始点
        :type StartTime: str
        :param EndTime: 更新时间截止点
        :type EndTime: str
        :param Offset: 查询列表偏移量
        :type Offset: int
        :param Limit: 查询列表限制数量
        :type Limit: int
        """
        self.SortBy = None
        self.Sorting = None
        self.Filters = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SortBy = params.get("SortBy")
        self.Sorting = params.get("Sorting")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkAppJobsResponse(AbstractModel):
    """DescribeSparkAppJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param SparkAppJobs: spark作业列表详情
        :type SparkAppJobs: list of SparkJobInfo
        :param TotalCount: spark作业总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SparkAppJobs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SparkAppJobs") is not None:
            self.SparkAppJobs = []
            for item in params.get("SparkAppJobs"):
                obj = SparkJobInfo()
                obj._deserialize(item)
                self.SparkAppJobs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSparkAppTasksRequest(AbstractModel):
    """DescribeSparkAppTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: spark作业Id
        :type JobId: str
        :param Offset: 分页查询偏移量
        :type Offset: int
        :param Limit: 分页查询Limit
        :type Limit: int
        :param TaskId: 执行实例id
        :type TaskId: str
        :param StartTime: 更新时间起始点
        :type StartTime: str
        :param EndTime: 更新时间截止点
        :type EndTime: str
        :param Filters: 按照该参数过滤,支持task-state
        :type Filters: list of Filter
        """
        self.JobId = None
        self.Offset = None
        self.Limit = None
        self.TaskId = None
        self.StartTime = None
        self.EndTime = None
        self.Filters = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TaskId = params.get("TaskId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
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
        


class DescribeSparkAppTasksResponse(AbstractModel):
    """DescribeSparkAppTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tasks: 任务结果（该字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TaskResponseInfo`
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param SparkAppTasks: 任务结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppTasks: list of TaskResponseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tasks = None
        self.TotalCount = None
        self.SparkAppTasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = TaskResponseInfo()
            self.Tasks._deserialize(params.get("Tasks"))
        self.TotalCount = params.get("TotalCount")
        if params.get("SparkAppTasks") is not None:
            self.SparkAppTasks = []
            for item in params.get("SparkAppTasks"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self.SparkAppTasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStoreLocationRequest(AbstractModel):
    """DescribeStoreLocation请求参数结构体

    """


class DescribeStoreLocationResponse(AbstractModel):
    """DescribeStoreLocation返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param DatasourceConnectionName: 指定查询的数据源名称，默认为DataLakeCatalog
        :type DatasourceConnectionName: str
        :param StartTime: 起始时间：用于对更新时间的筛选
        :type StartTime: str
        :param EndTime: 终止时间：用于对更新时间的筛选
        :type EndTime: str
        :param Sort: 排序字段，支持：CreateTime、UpdateTime、StorageSize、RecordCount、Name（不传则默认按name升序）
        :type Sort: str
        :param Asc: 排序字段，false：降序（默认）；true：升序
        :type Asc: bool
        :param TableType: table type，表类型查询,可用值:EXTERNAL_TABLE,INDEX_TABLE,MANAGED_TABLE,MATERIALIZED_VIEW,TABLE,VIEW,VIRTUAL_VIEW
        :type TableType: str
        :param TableFormat: 筛选字段-表格式：不传（默认）为查全部；LAKEFS：托管表；ICEBERG：非托管iceberg表；HIVE：非托管hive表；OTHER：非托管其它；
        :type TableFormat: str
        """
        self.DatabaseName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.DatasourceConnectionName = None
        self.StartTime = None
        self.EndTime = None
        self.Sort = None
        self.Asc = None
        self.TableType = None
        self.TableFormat = None


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
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Sort = params.get("Sort")
        self.Asc = params.get("Asc")
        self.TableType = params.get("TableType")
        self.TableFormat = params.get("TableFormat")
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


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务唯一ID
        :type TaskId: str
        :param NextToken: 上一次请求响应返回的分页信息。第一次可以不带，从头开始返回数据，每次返回MaxResults字段设置的数据量。
        :type NextToken: str
        :param MaxResults: 返回结果的最大行数，范围0~1000，默认为1000.
        :type MaxResults: int
        """
        self.TaskId = None
        self.NextToken = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.NextToken = params.get("NextToken")
        self.MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskInfo: 查询的任务信息，返回为空表示输入任务ID对应的任务不存在。只有当任务状态为成功（2）的时候，才会返回任务的结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfo: :class:`tencentcloud.dlc.v20210125.models.TaskResultInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = TaskResultInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件，如下支持的过滤类型，传参Name应为以下其中一个,其中task-id支持最大50个过滤个数，其他过滤参数支持的总数不超过5个。
task-id - String - （任务ID准确过滤）task-id取值形如：e386471f-139a-4e59-877f-50ece8135b99。
task-state - String - （任务状态过滤）取值范围 0(初始化)， 1(运行中)， 2(成功)， -1(失败)。
task-sql-keyword - String - （SQL语句关键字模糊过滤）取值形如：DROP TABLE。
task-operator- string （子uin过滤）
task-kind - string （任务类型过滤）
        :type Filters: list of Filter
        :param SortBy: 排序字段，支持如下字段类型，create-time（创建时间，默认）、update-time（更新时间）
        :type SortBy: str
        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc。
        :type Sorting: str
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。默认为45天前的当前时刻
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS时间跨度在(0,30天]，支持最近45天数据查询。默认为当前时刻
        :type EndTime: str
        :param DataEngineName: 支持计算资源名字筛选
        :type DataEngineName: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.SortBy = None
        self.Sorting = None
        self.StartTime = None
        self.EndTime = None
        self.DataEngineName = None


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
        self.DataEngineName = params.get("DataEngineName")
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
        r"""
        :param TaskList: 任务对象列表。
        :type TaskList: list of TaskResponseInfo
        :param TotalCount: 实例总数。
        :type TotalCount: int
        :param TasksOverview: 任务概览信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TasksOverview: :class:`tencentcloud.dlc.v20210125.models.TasksOverview`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskList = None
        self.TotalCount = None
        self.TasksOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskList") is not None:
            self.TaskList = []
            for item in params.get("TaskList"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self.TaskList.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("TasksOverview") is not None:
            self.TasksOverview = TasksOverview()
            self.TasksOverview._deserialize(params.get("TasksOverview"))
        self.RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    """DescribeUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 指定查询的子用户uin，用户需要通过CreateUser接口创建。
        :type UserId: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认20，最大值100
        :type Limit: int
        :param SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc
        :type Sorting: str
        :param Filters: 过滤条件，支持如下字段类型，user-type：根据用户类型过滤。user-keyword：根据用户名称过滤
        :type Filters: list of Filter
        """
        self.UserId = None
        self.Offset = None
        self.Limit = None
        self.SortBy = None
        self.Sorting = None
        self.Filters = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribeUsersResponse(AbstractModel):
    """DescribeUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询到的用户总数
        :type TotalCount: int
        :param UserSet: 查询到的授权用户信息集合
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
        r"""
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
        :param Sort: 排序字段
        :type Sort: str
        :param Asc: 排序规则，true:升序；false:降序
        :type Asc: bool
        :param StartTime: 按视图更新时间筛选，开始时间，如2021-11-11 00:00:00
        :type StartTime: str
        :param EndTime: 按视图更新时间筛选，结束时间，如2021-11-12 00:00:00
        :type EndTime: str
        """
        self.DatabaseName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.DatasourceConnectionName = None
        self.Sort = None
        self.Asc = None
        self.StartTime = None
        self.EndTime = None


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
        self.Sort = params.get("Sort")
        self.Asc = params.get("Asc")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
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
        r"""
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
        r"""
        :param WorkGroupId: 查询的工作组Id，不填或填0表示不过滤。
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DropDMSDatabaseRequest(AbstractModel):
    """DropDMSDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 数据库名称
        :type Name: str
        :param DeleteData: 是否删除数据
        :type DeleteData: bool
        :param Cascade: 是否级联删除
        :type Cascade: bool
        """
        self.Name = None
        self.DeleteData = None
        self.Cascade = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DeleteData = params.get("DeleteData")
        self.Cascade = params.get("Cascade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropDMSDatabaseResponse(AbstractModel):
    """DropDMSDatabase返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DropDMSPartitionsRequest(AbstractModel):
    """DropDMSPartitions请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatabaseName: 数据库名称
        :type DatabaseName: str
        :param SchemaName: 数据库Schema名称
        :type SchemaName: str
        :param TableName: 数据表名称
        :type TableName: str
        :param Name: 分区名称
        :type Name: str
        :param Values: 单个分区名称
        :type Values: list of str
        :param DeleteData: 是否删除分区数据
        :type DeleteData: bool
        """
        self.DatabaseName = None
        self.SchemaName = None
        self.TableName = None
        self.Name = None
        self.Values = None
        self.DeleteData = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.SchemaName = params.get("SchemaName")
        self.TableName = params.get("TableName")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.DeleteData = params.get("DeleteData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropDMSPartitionsResponse(AbstractModel):
    """DropDMSPartitions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 状态
        :type Status: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DropDMSTableRequest(AbstractModel):
    """DropDMSTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param DbName: 数据库名称
        :type DbName: str
        :param Name: 表名称
        :type Name: str
        :param DeleteData: 是否删除数据
        :type DeleteData: bool
        :param EnvProps: 环境属性
        :type EnvProps: :class:`tencentcloud.dlc.v20210125.models.KVPair`
        """
        self.DbName = None
        self.Name = None
        self.DeleteData = None
        self.EnvProps = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.Name = params.get("Name")
        self.DeleteData = params.get("DeleteData")
        if params.get("EnvProps") is not None:
            self.EnvProps = KVPair()
            self.EnvProps._deserialize(params.get("EnvProps"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropDMSTableResponse(AbstractModel):
    """DropDMSTable返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        


class GenerateCreateMangedTableSqlRequest(AbstractModel):
    """GenerateCreateMangedTableSql请求参数结构体

    """


class GenerateCreateMangedTableSqlResponse(AbstractModel):
    """GenerateCreateMangedTableSql返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class JobLogResult(AbstractModel):
    """日志详情

    """

    def __init__(self):
        r"""
        :param Time: 日志时间戳，毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param TopicId: 日志topic id
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param TopicName: 日志topic name
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param LogJson: 日志内容，json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type LogJson: str
        """
        self.Time = None
        self.TopicId = None
        self.TopicName = None
        self.LogJson = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.LogJson = params.get("LogJson")
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
        r"""
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
        


class ListTaskJobLogDetailRequest(AbstractModel):
    """ListTaskJobLogDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 列表返回的Id
        :type TaskId: str
        :param StartTime: 开始运行时间，unix时间戳（毫秒）
        :type StartTime: int
        :param EndTime: 结束运行时间，unix时间戳（毫秒）
        :type EndTime: int
        :param Limit: 分页大小，最大1000，配合Context一起使用
        :type Limit: int
        :param Context: 下一次分页参数，第一次传空
        :type Context: str
        :param Asc: 最近1000条日志是否升序排列，true:升序排序，false:倒序，默认false，倒序排列
        :type Asc: bool
        :param Filters: 预览日志的通用过滤条件
        :type Filters: list of Filter
        """
        self.TaskId = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Context = None
        self.Asc = None
        self.Filters = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Asc = params.get("Asc")
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
        


class ListTaskJobLogDetailResponse(AbstractModel):
    """ListTaskJobLogDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 下一次分页参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param ListOver: 是否获取完结
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOver: bool
        :param Results: 日志详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of JobLogResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.ListOver = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.ListOver = params.get("ListOver")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = JobLogResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class LockComponentInfo(AbstractModel):
    """元数据加锁内容

    """

    def __init__(self):
        r"""
        :param DbName: 数据库名称
        :type DbName: str
        :param TableName: 表名称
        :type TableName: str
        :param Partition: 分区
        :type Partition: str
        :param LockType: 锁类型：SHARED_READ、SHARED_WRITE、EXCLUSIVE
        :type LockType: str
        :param LockLevel: 锁级别：DB、TABLE、PARTITION
        :type LockLevel: str
        :param DataOperationType: 锁操作：SELECT,INSERT,UPDATE,DELETE,UNSET,NO_TXN
        :type DataOperationType: str
        :param IsAcid: 是否保持Acid
        :type IsAcid: bool
        :param IsDynamicPartitionWrite: 是否动态分区写
        :type IsDynamicPartitionWrite: bool
        """
        self.DbName = None
        self.TableName = None
        self.Partition = None
        self.LockType = None
        self.LockLevel = None
        self.DataOperationType = None
        self.IsAcid = None
        self.IsDynamicPartitionWrite = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.TableName = params.get("TableName")
        self.Partition = params.get("Partition")
        self.LockType = params.get("LockType")
        self.LockLevel = params.get("LockLevel")
        self.DataOperationType = params.get("DataOperationType")
        self.IsAcid = params.get("IsAcid")
        self.IsDynamicPartitionWrite = params.get("IsDynamicPartitionWrite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockMetaDataRequest(AbstractModel):
    """LockMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param LockComponentList: 加锁内容
        :type LockComponentList: list of LockComponentInfo
        :param DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        :param TxnId: 事务id
        :type TxnId: int
        :param AgentInfo: 客户端信息
        :type AgentInfo: str
        :param Hostname: 主机名
        :type Hostname: str
        """
        self.LockComponentList = None
        self.DatasourceConnectionName = None
        self.TxnId = None
        self.AgentInfo = None
        self.Hostname = None


    def _deserialize(self, params):
        if params.get("LockComponentList") is not None:
            self.LockComponentList = []
            for item in params.get("LockComponentList"):
                obj = LockComponentInfo()
                obj._deserialize(item)
                self.LockComponentList.append(obj)
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.TxnId = params.get("TxnId")
        self.AgentInfo = params.get("AgentInfo")
        self.Hostname = params.get("Hostname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockMetaDataResponse(AbstractModel):
    """LockMetaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param LockId: 锁id
        :type LockId: int
        :param LockState: 锁状态：ACQUIRED、WAITING、ABORT、NOT_ACQUIRED
        :type LockState: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LockId = None
        self.LockState = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LockId = params.get("LockId")
        self.LockState = params.get("LockState")
        self.RequestId = params.get("RequestId")


class ModifyGovernEventRuleRequest(AbstractModel):
    """ModifyGovernEventRule请求参数结构体

    """


class ModifyGovernEventRuleResponse(AbstractModel):
    """ModifyGovernEventRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySparkAppRequest(AbstractModel):
    """ModifySparkApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: spark应用名
        :type AppName: str
        :param AppType: 1代表spark jar应用，2代表spark streaming应用
        :type AppType: int
        :param DataEngine: 执行spark作业的数据引擎
        :type DataEngine: str
        :param AppFile: spark应用的执行入口
        :type AppFile: str
        :param RoleArn: 执行spark作业的角色ID
        :type RoleArn: int
        :param AppDriverSize: spark作业driver资源规格大小, 可取small,medium,large,xlarge
        :type AppDriverSize: str
        :param AppExecutorSize: spark作业executor资源规格大小, 可取small,medium,large,xlarge
        :type AppExecutorSize: str
        :param AppExecutorNums: spark作业executor个数
        :type AppExecutorNums: int
        :param SparkAppId: spark应用Id
        :type SparkAppId: str
        :param Eni: 该字段已下线，请使用字段Datasource
        :type Eni: str
        :param IsLocal: 是否本地上传，可取cos,lakefs
        :type IsLocal: str
        :param MainClass: spark jar作业时的主类
        :type MainClass: str
        :param AppConf: spark配置，以换行符分隔
        :type AppConf: str
        :param IsLocalJars: jar资源依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
        :type IsLocalJars: str
        :param AppJars: spark jar作业依赖jars，以逗号分隔
        :type AppJars: str
        :param IsLocalFiles: file资源依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
        :type IsLocalFiles: str
        :param AppFiles: spark作业依赖资源，以逗号分隔
        :type AppFiles: str
        :param IsLocalPythonFiles: pyspark：依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
        :type IsLocalPythonFiles: str
        :param AppPythonFiles: pyspark：python依赖, 除py文件外，还支持zip/egg等归档格式，多文件以逗号分隔
        :type AppPythonFiles: str
        :param CmdArgs: spark作业命令行参数
        :type CmdArgs: str
        :param MaxRetries: 只对spark流任务生效
        :type MaxRetries: int
        :param DataSource: 数据源名
        :type DataSource: str
        :param IsLocalArchives: archives：依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
        :type IsLocalArchives: str
        :param AppArchives: archives：依赖资源
        :type AppArchives: str
        :param SparkImage: Spark Image 版本
        :type SparkImage: str
        :param SparkImageVersion: Spark Image 版本名称
        :type SparkImageVersion: str
        :param AppExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于AppExecutorNums
        :type AppExecutorMaxNumbers: int
        """
        self.AppName = None
        self.AppType = None
        self.DataEngine = None
        self.AppFile = None
        self.RoleArn = None
        self.AppDriverSize = None
        self.AppExecutorSize = None
        self.AppExecutorNums = None
        self.SparkAppId = None
        self.Eni = None
        self.IsLocal = None
        self.MainClass = None
        self.AppConf = None
        self.IsLocalJars = None
        self.AppJars = None
        self.IsLocalFiles = None
        self.AppFiles = None
        self.IsLocalPythonFiles = None
        self.AppPythonFiles = None
        self.CmdArgs = None
        self.MaxRetries = None
        self.DataSource = None
        self.IsLocalArchives = None
        self.AppArchives = None
        self.SparkImage = None
        self.SparkImageVersion = None
        self.AppExecutorMaxNumbers = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.AppType = params.get("AppType")
        self.DataEngine = params.get("DataEngine")
        self.AppFile = params.get("AppFile")
        self.RoleArn = params.get("RoleArn")
        self.AppDriverSize = params.get("AppDriverSize")
        self.AppExecutorSize = params.get("AppExecutorSize")
        self.AppExecutorNums = params.get("AppExecutorNums")
        self.SparkAppId = params.get("SparkAppId")
        self.Eni = params.get("Eni")
        self.IsLocal = params.get("IsLocal")
        self.MainClass = params.get("MainClass")
        self.AppConf = params.get("AppConf")
        self.IsLocalJars = params.get("IsLocalJars")
        self.AppJars = params.get("AppJars")
        self.IsLocalFiles = params.get("IsLocalFiles")
        self.AppFiles = params.get("AppFiles")
        self.IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self.AppPythonFiles = params.get("AppPythonFiles")
        self.CmdArgs = params.get("CmdArgs")
        self.MaxRetries = params.get("MaxRetries")
        self.DataSource = params.get("DataSource")
        self.IsLocalArchives = params.get("IsLocalArchives")
        self.AppArchives = params.get("AppArchives")
        self.SparkImage = params.get("SparkImage")
        self.SparkImageVersion = params.get("SparkImageVersion")
        self.AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySparkAppResponse(AbstractModel):
    """ModifySparkApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NetworkConnection(AbstractModel):
    """网络配置

    """

    def __init__(self):
        r"""
        :param Id: 网络配置id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param AssociateId: 网络配置唯一标志符
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateId: str
        :param HouseId: 计算引擎id
注意：此字段可能返回 null，表示取不到有效值。
        :type HouseId: str
        :param DatasourceConnectionId: 数据源id(已废弃)
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionId: str
        :param State: 网络配置状态（0-初始化，1-正常）
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param Appid: 创建用户Appid
注意：此字段可能返回 null，表示取不到有效值。
        :type Appid: int
        :param HouseName: 计算引擎名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HouseName: str
        :param DatasourceConnectionName: 网络配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionName: str
        :param NetworkConnectionType: 网络配置类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConnectionType: int
        :param Uin: 创建用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param SubAccountUin: 创建用户SubAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param NetworkConnectionDesc: 网络配置描述
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConnectionDesc: str
        :param DatasourceConnectionVpcId: 数据源vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionVpcId: str
        :param DatasourceConnectionSubnetId: 数据源SubnetId
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionSubnetId: str
        :param DatasourceConnectionCidrBlock: 数据源SubnetId
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionCidrBlock: str
        :param DatasourceConnectionSubnetCidrBlock: 数据源SubnetCidrBlock
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionSubnetCidrBlock: str
        """
        self.Id = None
        self.AssociateId = None
        self.HouseId = None
        self.DatasourceConnectionId = None
        self.State = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Appid = None
        self.HouseName = None
        self.DatasourceConnectionName = None
        self.NetworkConnectionType = None
        self.Uin = None
        self.SubAccountUin = None
        self.NetworkConnectionDesc = None
        self.DatasourceConnectionVpcId = None
        self.DatasourceConnectionSubnetId = None
        self.DatasourceConnectionCidrBlock = None
        self.DatasourceConnectionSubnetCidrBlock = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.AssociateId = params.get("AssociateId")
        self.HouseId = params.get("HouseId")
        self.DatasourceConnectionId = params.get("DatasourceConnectionId")
        self.State = params.get("State")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Appid = params.get("Appid")
        self.HouseName = params.get("HouseName")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.NetworkConnectionType = params.get("NetworkConnectionType")
        self.Uin = params.get("Uin")
        self.SubAccountUin = params.get("SubAccountUin")
        self.NetworkConnectionDesc = params.get("NetworkConnectionDesc")
        self.DatasourceConnectionVpcId = params.get("DatasourceConnectionVpcId")
        self.DatasourceConnectionSubnetId = params.get("DatasourceConnectionSubnetId")
        self.DatasourceConnectionCidrBlock = params.get("DatasourceConnectionCidrBlock")
        self.DatasourceConnectionSubnetCidrBlock = params.get("DatasourceConnectionSubnetCidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSessionInfo(AbstractModel):
    """Notebook Session详细信息。

    """

    def __init__(self):
        r"""
        :param Name: Session名称
        :type Name: str
        :param Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        :param DataEngineName: DLC Spark作业引擎名称
        :type DataEngineName: str
        :param Arguments: Session相关配置，当前支持：eni、roleArn以及用户指定的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Arguments: list of KVPair
        :param ProgramDependentFiles: 运行程序地址，当前支持：cosn://和lakefs://两种路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramDependentFiles: list of str
        :param ProgramDependentJars: 依赖的jar程序地址，当前支持：cosn://和lakefs://两种路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramDependentJars: list of str
        :param ProgramDependentPython: 依赖的python程序地址，当前支持：cosn://和lakefs://两种路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramDependentPython: list of str
        :param ProgramArchives: 依赖的pyspark虚拟环境地址，当前支持：cosn://和lakefs://两种路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramArchives: list of str
        :param DriverSize: 指定的Driver规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
注意：此字段可能返回 null，表示取不到有效值。
        :type DriverSize: str
        :param ExecutorSize: 指定的Executor规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorSize: str
        :param ExecutorNumbers: 指定的Executor数量，默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorNumbers: int
        :param ProxyUser: 代理用户，默认为root
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyUser: str
        :param TimeoutInSecond: 指定的Session超时时间，单位秒，默认3600秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutInSecond: int
        :param SparkAppId: Spark任务返回的AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppId: str
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param State: Session状态，包含：not_started（未启动）、starting（已启动）、idle（等待输入）、busy(正在运行statement)、shutting_down（停止）、error（异常）、dead（已退出）、killed（被杀死）、success（正常停止）
        :type State: str
        :param CreateTime: Session创建时间
        :type CreateTime: str
        :param AppInfo: 其它信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppInfo: list of KVPair
        :param SparkUiUrl: Spark ui地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkUiUrl: str
        :param ExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于ExecutorNumbers
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorMaxNumbers: int
        """
        self.Name = None
        self.Kind = None
        self.DataEngineName = None
        self.Arguments = None
        self.ProgramDependentFiles = None
        self.ProgramDependentJars = None
        self.ProgramDependentPython = None
        self.ProgramArchives = None
        self.DriverSize = None
        self.ExecutorSize = None
        self.ExecutorNumbers = None
        self.ProxyUser = None
        self.TimeoutInSecond = None
        self.SparkAppId = None
        self.SessionId = None
        self.State = None
        self.CreateTime = None
        self.AppInfo = None
        self.SparkUiUrl = None
        self.ExecutorMaxNumbers = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Kind = params.get("Kind")
        self.DataEngineName = params.get("DataEngineName")
        if params.get("Arguments") is not None:
            self.Arguments = []
            for item in params.get("Arguments"):
                obj = KVPair()
                obj._deserialize(item)
                self.Arguments.append(obj)
        self.ProgramDependentFiles = params.get("ProgramDependentFiles")
        self.ProgramDependentJars = params.get("ProgramDependentJars")
        self.ProgramDependentPython = params.get("ProgramDependentPython")
        self.ProgramArchives = params.get("ProgramArchives")
        self.DriverSize = params.get("DriverSize")
        self.ExecutorSize = params.get("ExecutorSize")
        self.ExecutorNumbers = params.get("ExecutorNumbers")
        self.ProxyUser = params.get("ProxyUser")
        self.TimeoutInSecond = params.get("TimeoutInSecond")
        self.SparkAppId = params.get("SparkAppId")
        self.SessionId = params.get("SessionId")
        self.State = params.get("State")
        self.CreateTime = params.get("CreateTime")
        if params.get("AppInfo") is not None:
            self.AppInfo = []
            for item in params.get("AppInfo"):
                obj = KVPair()
                obj._deserialize(item)
                self.AppInfo.append(obj)
        self.SparkUiUrl = params.get("SparkUiUrl")
        self.ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSessionStatementBatchInformation(AbstractModel):
    """按批提交Statement运行SQL任务。

    """

    def __init__(self):
        r"""
        :param NotebookSessionStatementBatch: 任务详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookSessionStatementBatch: list of NotebookSessionStatementInfo
        :param IsAvailable: 当前批任务是否运行完成
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAvailable: bool
        :param SessionId: Session唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param BatchId: Batch唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        """
        self.NotebookSessionStatementBatch = None
        self.IsAvailable = None
        self.SessionId = None
        self.BatchId = None


    def _deserialize(self, params):
        if params.get("NotebookSessionStatementBatch") is not None:
            self.NotebookSessionStatementBatch = []
            for item in params.get("NotebookSessionStatementBatch"):
                obj = NotebookSessionStatementInfo()
                obj._deserialize(item)
                self.NotebookSessionStatementBatch.append(obj)
        self.IsAvailable = params.get("IsAvailable")
        self.SessionId = params.get("SessionId")
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSessionStatementInfo(AbstractModel):
    """NotebookSessionStatement详情。

    """

    def __init__(self):
        r"""
        :param Completed: 完成时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Completed: int
        :param Started: 开始时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Started: int
        :param Progress: 完成进度，百分制
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param StatementId: Session Statement唯一标识
        :type StatementId: str
        :param State: Session Statement状态，包含：waiting（排队中）、running（运行中）、available（正常）、error（异常）、cancelling（取消中）、cancelled（已取消）
        :type State: str
        :param OutPut: Statement输出信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OutPut: :class:`tencentcloud.dlc.v20210125.models.StatementOutput`
        :param BatchId: 批任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param Code: 运行语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self.Completed = None
        self.Started = None
        self.Progress = None
        self.StatementId = None
        self.State = None
        self.OutPut = None
        self.BatchId = None
        self.Code = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Completed = params.get("Completed")
        self.Started = params.get("Started")
        self.Progress = params.get("Progress")
        self.StatementId = params.get("StatementId")
        self.State = params.get("State")
        if params.get("OutPut") is not None:
            self.OutPut = StatementOutput()
            self.OutPut._deserialize(params.get("OutPut"))
        self.BatchId = params.get("BatchId")
        self.Code = params.get("Code")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSessions(AbstractModel):
    """notebook session列表信息。

    """

    def __init__(self):
        r"""
        :param Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        :param SessionId: Session唯一标识
        :type SessionId: str
        :param ProxyUser: 代理用户，默认为root
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyUser: str
        :param State: Session状态，包含：not_started（未启动）、starting（已启动）、idle（等待输入）、busy(正在运行statement)、shutting_down（停止）、error（异常）、dead（已退出）、killed（被杀死）、success（正常停止）
        :type State: str
        :param SparkAppId: Spark任务返回的AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppId: str
        :param Name: Session名称
        :type Name: str
        :param CreateTime: Session创建时间
        :type CreateTime: str
        :param DataEngineName: 引擎名称
        :type DataEngineName: str
        :param LastRunningTime: 最新的运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastRunningTime: str
        :param Creator: 创建者
        :type Creator: str
        :param SparkUiUrl: spark ui地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkUiUrl: str
        """
        self.Kind = None
        self.SessionId = None
        self.ProxyUser = None
        self.State = None
        self.SparkAppId = None
        self.Name = None
        self.CreateTime = None
        self.DataEngineName = None
        self.LastRunningTime = None
        self.Creator = None
        self.SparkUiUrl = None


    def _deserialize(self, params):
        self.Kind = params.get("Kind")
        self.SessionId = params.get("SessionId")
        self.ProxyUser = params.get("ProxyUser")
        self.State = params.get("State")
        self.SparkAppId = params.get("SparkAppId")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.DataEngineName = params.get("DataEngineName")
        self.LastRunningTime = params.get("LastRunningTime")
        self.Creator = params.get("Creator")
        self.SparkUiUrl = params.get("SparkUiUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Other(AbstractModel):
    """数据格式其它类型。

    """

    def __init__(self):
        r"""
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
        r"""
        :param Name: 分区列名。
        :type Name: str
        :param Type: 分区类型。
        :type Type: str
        :param Comment: 对分区的描述。
        :type Comment: str
        :param Transform: 隐式分区转换策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Transform: str
        :param TransformArgs: 转换策略参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TransformArgs: list of str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.Transform = None
        self.TransformArgs = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        self.Transform = params.get("Transform")
        self.TransformArgs = params.get("TransformArgs")
        self.CreateTime = params.get("CreateTime")
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
        r"""
        :param Database: 需要授权的数据库名，填*代表当前Catalog下所有数据库。当授权类型为管理员级别时，只允许填“*”，当授权类型为数据连接级别时只允许填空，其他类型下可以任意指定数据库。
        :type Database: str
        :param Catalog: 需要授权的数据源名称，管理员级别下只支持填*（代表该级别全部资源）；数据源级别和数据库级别鉴权的情况下，只支持填COSDataCatalog或者*；在数据表级别鉴权下可以填写用户自定义数据源。不填情况下默认为DataLakeCatalog。注意：如果是对用户自定义数据源进行鉴权，DLC能够管理的权限是用户接入数据源的时候提供的账户的子集。
        :type Catalog: str
        :param Table: 需要授权的表名，填*代表当前Database下所有表。当授权类型为管理员级别时，只允许填“*”，当授权类型为数据连接级别、数据库级别时只允许填空，其他类型下可以任意指定数据表。
        :type Table: str
        :param Operation: 授权的权限操作，对于不同级别的鉴权提供不同操作。管理员权限：ALL，不填默认为ALL；数据连接级鉴权：CREATE；数据库级别鉴权：ALL、CREATE、ALTER、DROP；数据表权限：ALL、SELECT、INSERT、ALTER、DELETE、DROP、UPDATE。注意：在数据表权限下，指定的数据源不为COSDataCatalog的时候，只支持SELECT操作。
        :type Operation: str
        :param PolicyType: 授权类型，现在支持八种授权类型：ADMIN:管理员级别鉴权 DATASOURCE：数据连接级别鉴权 DATABASE：数据库级别鉴权 TABLE：表级别鉴权 VIEW：视图级别鉴权 FUNCTION：函数级别鉴权 COLUMN：列级别鉴权 ENGINE：数据引擎鉴权。不填默认为管理员级别鉴权。
        :type PolicyType: str
        :param Function: 需要授权的函数名，填*代表当前Catalog下所有函数。当授权类型为管理员级别时，只允许填“*”，当授权类型为数据连接级别时只允许填空，其他类型下可以任意指定函数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Function: str
        :param View: 需要授权的视图，填*代表当前Database下所有视图。当授权类型为管理员级别时，只允许填“*”，当授权类型为数据连接级别、数据库级别时只允许填空，其他类型下可以任意指定视图。
注意：此字段可能返回 null，表示取不到有效值。
        :type View: str
        :param Column: 需要授权的列，填*代表当前所有列。当授权类型为管理员级别时，只允许填“*”
注意：此字段可能返回 null，表示取不到有效值。
        :type Column: str
        :param DataEngine: 需要授权的数据引擎，填*代表当前所有引擎。当授权类型为管理员级别时，只允许填“*”
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngine: str
        :param ReAuth: 用户是否可以进行二次授权。当为true的时候，被授权的用户可以将本次获取的权限再次授权给其他子用户。默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type ReAuth: bool
        :param Source: 权限来源，入参不填。USER：权限来自用户本身；WORKGROUP：权限来自绑定的工作组
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param Mode: 授权模式，入参不填。COMMON：普通模式；SENIOR：高级模式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param Operator: 操作者，入参不填。
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param CreateTime: 权限创建的时间，入参不填
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param SourceId: 权限所属工作组的ID，只有当该权限的来源为工作组时才会有值。即仅当Source字段的值为WORKGROUP时该字段才有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceId: int
        :param SourceName: 权限所属工作组的名称，只有当该权限的来源为工作组时才会有值。即仅当Source字段的值为WORKGROUP时该字段才有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceName: str
        """
        self.Database = None
        self.Catalog = None
        self.Table = None
        self.Operation = None
        self.PolicyType = None
        self.Function = None
        self.View = None
        self.Column = None
        self.DataEngine = None
        self.ReAuth = None
        self.Source = None
        self.Mode = None
        self.Operator = None
        self.CreateTime = None
        self.SourceId = None
        self.SourceName = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Catalog = params.get("Catalog")
        self.Table = params.get("Table")
        self.Operation = params.get("Operation")
        self.PolicyType = params.get("PolicyType")
        self.Function = params.get("Function")
        self.View = params.get("View")
        self.Column = params.get("Column")
        self.DataEngine = params.get("DataEngine")
        self.ReAuth = params.get("ReAuth")
        self.Source = params.get("Source")
        self.Mode = params.get("Mode")
        self.Operator = params.get("Operator")
        self.CreateTime = params.get("CreateTime")
        self.SourceId = params.get("SourceId")
        self.SourceName = params.get("SourceName")
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
        r"""
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
        


class ReportHeartbeatMetaDataRequest(AbstractModel):
    """ReportHeartbeatMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        :param LockId: 锁ID
        :type LockId: int
        :param TxnId: 事务ID
        :type TxnId: int
        """
        self.DatasourceConnectionName = None
        self.LockId = None
        self.TxnId = None


    def _deserialize(self, params):
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.LockId = params.get("LockId")
        self.TxnId = params.get("TxnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportHeartbeatMetaDataResponse(AbstractModel):
    """ReportHeartbeatMetaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SQLTask(AbstractModel):
    """SQL查询任务

    """

    def __init__(self):
        r"""
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
        r"""
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
        


class SparkJobInfo(AbstractModel):
    """spark作业详情。

    """

    def __init__(self):
        r"""
        :param JobId: spark作业ID
        :type JobId: str
        :param JobName: spark作业名
        :type JobName: str
        :param JobType: spark作业类型，可去1或者2，1表示batch作业， 2表示streaming作业
        :type JobType: int
        :param DataEngine: 引擎名
        :type DataEngine: str
        :param Eni: 该字段已下线，请使用字段Datasource
        :type Eni: str
        :param IsLocal: 程序包是否本地上传，cos或者lakefs
        :type IsLocal: str
        :param JobFile: 程序包路径
        :type JobFile: str
        :param RoleArn: 角色ID
        :type RoleArn: int
        :param MainClass: spark作业运行主类
        :type MainClass: str
        :param CmdArgs: 命令行参数，spark作业命令行参数，空格分隔
        :type CmdArgs: str
        :param JobConf: spark原生配置，换行符分隔
        :type JobConf: str
        :param IsLocalJars: 依赖jars是否本地上传，cos或者lakefs
        :type IsLocalJars: str
        :param JobJars: spark作业依赖jars，逗号分隔
        :type JobJars: str
        :param IsLocalFiles: 依赖文件是否本地上传，cos或者lakefs
        :type IsLocalFiles: str
        :param JobFiles: spark作业依赖文件，逗号分隔
        :type JobFiles: str
        :param JobDriverSize: spark作业driver资源大小
        :type JobDriverSize: str
        :param JobExecutorSize: spark作业executor资源大小
        :type JobExecutorSize: str
        :param JobExecutorNums: spark作业executor个数
        :type JobExecutorNums: int
        :param JobMaxAttempts: spark流任务最大重试次数
        :type JobMaxAttempts: int
        :param JobCreator: spark作业创建者
        :type JobCreator: str
        :param JobCreateTime: spark作业创建时间
        :type JobCreateTime: int
        :param JobUpdateTime: spark作业更新时间
        :type JobUpdateTime: int
        :param CurrentTaskId: spark作业最近任务ID
        :type CurrentTaskId: str
        :param JobStatus: spark作业最近运行状态
        :type JobStatus: int
        :param StreamingStat: spark流作业统计
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamingStat: :class:`tencentcloud.dlc.v20210125.models.StreamingStatistics`
        :param DataSource: 数据源名
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param IsLocalPythonFiles: pyspark：依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLocalPythonFiles: str
        :param AppPythonFiles: 注：该返回值已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type AppPythonFiles: str
        :param IsLocalArchives: archives：依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLocalArchives: str
        :param JobArchives: archives：依赖资源
注意：此字段可能返回 null，表示取不到有效值。
        :type JobArchives: str
        :param SparkImage: Spark Image 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkImage: str
        :param JobPythonFiles: pyspark：python依赖, 除py文件外，还支持zip/egg等归档格式，多文件以逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type JobPythonFiles: str
        :param TaskNum: 当前job正在运行或准备运行的任务个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNum: int
        :param DataEngineStatus: 引擎状态：-100（默认：未知状态），-2~11：引擎正常状态；
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineStatus: int
        :param JobExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于JobExecutorNums
注意：此字段可能返回 null，表示取不到有效值。
        :type JobExecutorMaxNumbers: int
        """
        self.JobId = None
        self.JobName = None
        self.JobType = None
        self.DataEngine = None
        self.Eni = None
        self.IsLocal = None
        self.JobFile = None
        self.RoleArn = None
        self.MainClass = None
        self.CmdArgs = None
        self.JobConf = None
        self.IsLocalJars = None
        self.JobJars = None
        self.IsLocalFiles = None
        self.JobFiles = None
        self.JobDriverSize = None
        self.JobExecutorSize = None
        self.JobExecutorNums = None
        self.JobMaxAttempts = None
        self.JobCreator = None
        self.JobCreateTime = None
        self.JobUpdateTime = None
        self.CurrentTaskId = None
        self.JobStatus = None
        self.StreamingStat = None
        self.DataSource = None
        self.IsLocalPythonFiles = None
        self.AppPythonFiles = None
        self.IsLocalArchives = None
        self.JobArchives = None
        self.SparkImage = None
        self.JobPythonFiles = None
        self.TaskNum = None
        self.DataEngineStatus = None
        self.JobExecutorMaxNumbers = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.JobType = params.get("JobType")
        self.DataEngine = params.get("DataEngine")
        self.Eni = params.get("Eni")
        self.IsLocal = params.get("IsLocal")
        self.JobFile = params.get("JobFile")
        self.RoleArn = params.get("RoleArn")
        self.MainClass = params.get("MainClass")
        self.CmdArgs = params.get("CmdArgs")
        self.JobConf = params.get("JobConf")
        self.IsLocalJars = params.get("IsLocalJars")
        self.JobJars = params.get("JobJars")
        self.IsLocalFiles = params.get("IsLocalFiles")
        self.JobFiles = params.get("JobFiles")
        self.JobDriverSize = params.get("JobDriverSize")
        self.JobExecutorSize = params.get("JobExecutorSize")
        self.JobExecutorNums = params.get("JobExecutorNums")
        self.JobMaxAttempts = params.get("JobMaxAttempts")
        self.JobCreator = params.get("JobCreator")
        self.JobCreateTime = params.get("JobCreateTime")
        self.JobUpdateTime = params.get("JobUpdateTime")
        self.CurrentTaskId = params.get("CurrentTaskId")
        self.JobStatus = params.get("JobStatus")
        if params.get("StreamingStat") is not None:
            self.StreamingStat = StreamingStatistics()
            self.StreamingStat._deserialize(params.get("StreamingStat"))
        self.DataSource = params.get("DataSource")
        self.IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self.AppPythonFiles = params.get("AppPythonFiles")
        self.IsLocalArchives = params.get("IsLocalArchives")
        self.JobArchives = params.get("JobArchives")
        self.SparkImage = params.get("SparkImage")
        self.JobPythonFiles = params.get("JobPythonFiles")
        self.TaskNum = params.get("TaskNum")
        self.DataEngineStatus = params.get("DataEngineStatus")
        self.JobExecutorMaxNumbers = params.get("JobExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatementOutput(AbstractModel):
    """notebook session statement输出信息。

    """

    def __init__(self):
        r"""
        :param ExecutionCount: 执行总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionCount: int
        :param Data: Statement数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of KVPair
        :param Status: Statement状态:ok,error
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ErrorName: 错误名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorName: str
        :param ErrorValue: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorValue: str
        :param ErrorMessage: 错误堆栈信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: list of str
        :param SQLResult: SQL类型任务结果返回
注意：此字段可能返回 null，表示取不到有效值。
        :type SQLResult: str
        """
        self.ExecutionCount = None
        self.Data = None
        self.Status = None
        self.ErrorName = None
        self.ErrorValue = None
        self.ErrorMessage = None
        self.SQLResult = None


    def _deserialize(self, params):
        self.ExecutionCount = params.get("ExecutionCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KVPair()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.ErrorName = params.get("ErrorName")
        self.ErrorValue = params.get("ErrorValue")
        self.ErrorMessage = params.get("ErrorMessage")
        self.SQLResult = params.get("SQLResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamingStatistics(AbstractModel):
    """spark流任务统计信息

    """

    def __init__(self):
        r"""
        :param StartTime: 任务开始时间
        :type StartTime: str
        :param Receivers: 数据接收器数
        :type Receivers: int
        :param NumActiveReceivers: 运行中的接收器数
        :type NumActiveReceivers: int
        :param NumInactiveReceivers: 不活跃的接收器数
        :type NumInactiveReceivers: int
        :param NumActiveBatches: 运行中的批数
        :type NumActiveBatches: int
        :param NumRetainedCompletedBatches: 待处理的批数
        :type NumRetainedCompletedBatches: int
        :param NumTotalCompletedBatches: 已完成的批数
        :type NumTotalCompletedBatches: int
        :param AverageInputRate: 平均输入速率
        :type AverageInputRate: float
        :param AverageSchedulingDelay: 平均等待时长
        :type AverageSchedulingDelay: float
        :param AverageProcessingTime: 平均处理时长
        :type AverageProcessingTime: float
        :param AverageTotalDelay: 平均延时
        :type AverageTotalDelay: float
        """
        self.StartTime = None
        self.Receivers = None
        self.NumActiveReceivers = None
        self.NumInactiveReceivers = None
        self.NumActiveBatches = None
        self.NumRetainedCompletedBatches = None
        self.NumTotalCompletedBatches = None
        self.AverageInputRate = None
        self.AverageSchedulingDelay = None
        self.AverageProcessingTime = None
        self.AverageTotalDelay = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Receivers = params.get("Receivers")
        self.NumActiveReceivers = params.get("NumActiveReceivers")
        self.NumInactiveReceivers = params.get("NumInactiveReceivers")
        self.NumActiveBatches = params.get("NumActiveBatches")
        self.NumRetainedCompletedBatches = params.get("NumRetainedCompletedBatches")
        self.NumTotalCompletedBatches = params.get("NumTotalCompletedBatches")
        self.AverageInputRate = params.get("AverageInputRate")
        self.AverageSchedulingDelay = params.get("AverageSchedulingDelay")
        self.AverageProcessingTime = params.get("AverageProcessingTime")
        self.AverageTotalDelay = params.get("AverageTotalDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendResumeDataEngineRequest(AbstractModel):
    """SuspendResumeDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param DataEngineName: 虚拟集群名称
        :type DataEngineName: str
        :param Operate: 操作类型 suspend/resume
        :type Operate: str
        """
        self.DataEngineName = None
        self.Operate = None


    def _deserialize(self, params):
        self.DataEngineName = params.get("DataEngineName")
        self.Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendResumeDataEngineResponse(AbstractModel):
    """SuspendResumeDataEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataEngineName: 虚拟集群详细信息
        :type DataEngineName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataEngineName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataEngineName = params.get("DataEngineName")
        self.RequestId = params.get("RequestId")


class TColumn(AbstractModel):
    """表字段描述信息

    """

    def __init__(self):
        r"""
        :param Name: 字段名称
        :type Name: str
        :param Type: 字段类型
        :type Type: str
        :param Comment: 字段描述
        :type Comment: str
        :param Default: 字段默认值
        :type Default: str
        :param NotNull: 字段是否是非空
        :type NotNull: bool
        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.Default = None
        self.NotNull = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        self.Default = params.get("Default")
        self.NotNull = params.get("NotNull")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TPartition(AbstractModel):
    """表分区字段信息

    """

    def __init__(self):
        r"""
        :param Name: 字段名称
        :type Name: str
        :param Type: 字段类型
        :type Type: str
        :param Comment: 字段描述
        :type Comment: str
        :param PartitionType: 分区类型
        :type PartitionType: str
        :param PartitionFormat: 分区格式
        :type PartitionFormat: str
        :param PartitionDot: 分区分隔数
        :type PartitionDot: int
        :param Transform: 分区转换策略
        :type Transform: str
        :param TransformArgs: 策略参数
        :type TransformArgs: list of str
        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.PartitionType = None
        self.PartitionFormat = None
        self.PartitionDot = None
        self.Transform = None
        self.TransformArgs = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
        self.PartitionType = params.get("PartitionType")
        self.PartitionFormat = params.get("PartitionFormat")
        self.PartitionDot = params.get("PartitionDot")
        self.Transform = params.get("Transform")
        self.TransformArgs = params.get("TransformArgs")
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
        r"""
        :param DatabaseName: 该数据表所属数据库名字
        :type DatabaseName: str
        :param TableName: 数据表名字
        :type TableName: str
        :param DatasourceConnectionName: 该数据表所属数据源名字
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionName: str
        :param TableComment: 该数据表备注
注意：此字段可能返回 null，表示取不到有效值。
        :type TableComment: str
        :param Type: 具体类型，表or视图
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param TableFormat: 数据格式类型，hive，iceberg等
注意：此字段可能返回 null，表示取不到有效值。
        :type TableFormat: str
        :param UserAlias: 建表用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param UserSubUin: 建表用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSubUin: str
        :param GovernPolicy: 数据治理配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type GovernPolicy: :class:`tencentcloud.dlc.v20210125.models.DataGovernPolicy`
        """
        self.DatabaseName = None
        self.TableName = None
        self.DatasourceConnectionName = None
        self.TableComment = None
        self.Type = None
        self.TableFormat = None
        self.UserAlias = None
        self.UserSubUin = None
        self.GovernPolicy = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.TableName = params.get("TableName")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.TableComment = params.get("TableComment")
        self.Type = params.get("Type")
        self.TableFormat = params.get("TableFormat")
        self.UserAlias = params.get("UserAlias")
        self.UserSubUin = params.get("UserSubUin")
        if params.get("GovernPolicy") is not None:
            self.GovernPolicy = DataGovernPolicy()
            self.GovernPolicy._deserialize(params.get("GovernPolicy"))
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
        r"""
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
        r"""
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
        :param StorageSize: 数据表存储大小（单位：Byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSize: int
        :param RecordCount: 数据表行数
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCount: int
        """
        self.TableBaseInfo = None
        self.Columns = None
        self.Partitions = None
        self.Location = None
        self.Properties = None
        self.ModifiedTime = None
        self.CreateTime = None
        self.InputFormat = None
        self.StorageSize = None
        self.RecordCount = None


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
        self.StorageSize = params.get("StorageSize")
        self.RecordCount = params.get("RecordCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签对信息

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
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
        r"""
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
        r"""
        :param DatabaseName: 任务所属Database的名称。
        :type DatabaseName: str
        :param DataAmount: 任务数据量。
        :type DataAmount: int
        :param Id: 任务Id。
        :type Id: str
        :param UsedTime: 计算耗时，单位： ms
        :type UsedTime: int
        :param OutputPath: 任务输出路径。
        :type OutputPath: str
        :param CreateTime: 任务创建时间。
        :type CreateTime: str
        :param State: 任务状态：0 初始化， 1 执行中， 2 执行成功，-1 执行失败，-3 已取消。
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
        :param ProgressDetail: 任务进度明细
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgressDetail: str
        :param UpdateTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param DataEngineId: 计算资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineId: str
        :param OperateUin: 执行sql的子uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUin: str
        :param DataEngineName: 计算资源名字
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineName: str
        :param InputType: 导入类型是本地导入还是cos
注意：此字段可能返回 null，表示取不到有效值。
        :type InputType: str
        :param InputConf: 导入配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InputConf: str
        :param DataNumber: 数据条数
注意：此字段可能返回 null，表示取不到有效值。
        :type DataNumber: int
        :param CanDownload: 查询数据能不能下载
注意：此字段可能返回 null，表示取不到有效值。
        :type CanDownload: bool
        :param UserAlias: 用户别名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param SparkJobName: spark应用作业名
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkJobName: str
        :param SparkJobId: spark应用作业Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkJobId: str
        :param SparkJobFile: spark应用入口jar文件
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkJobFile: str
        :param UiUrl: spark ui url
注意：此字段可能返回 null，表示取不到有效值。
        :type UiUrl: str
        :param TotalTime: 任务耗时，单位： ms
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTime: int
        :param CmdArgs: spark app job执行task的程序入口参数
注意：此字段可能返回 null，表示取不到有效值。
        :type CmdArgs: str
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
        self.ProgressDetail = None
        self.UpdateTime = None
        self.DataEngineId = None
        self.OperateUin = None
        self.DataEngineName = None
        self.InputType = None
        self.InputConf = None
        self.DataNumber = None
        self.CanDownload = None
        self.UserAlias = None
        self.SparkJobName = None
        self.SparkJobId = None
        self.SparkJobFile = None
        self.UiUrl = None
        self.TotalTime = None
        self.CmdArgs = None


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
        self.ProgressDetail = params.get("ProgressDetail")
        self.UpdateTime = params.get("UpdateTime")
        self.DataEngineId = params.get("DataEngineId")
        self.OperateUin = params.get("OperateUin")
        self.DataEngineName = params.get("DataEngineName")
        self.InputType = params.get("InputType")
        self.InputConf = params.get("InputConf")
        self.DataNumber = params.get("DataNumber")
        self.CanDownload = params.get("CanDownload")
        self.UserAlias = params.get("UserAlias")
        self.SparkJobName = params.get("SparkJobName")
        self.SparkJobId = params.get("SparkJobId")
        self.SparkJobFile = params.get("SparkJobFile")
        self.UiUrl = params.get("UiUrl")
        self.TotalTime = params.get("TotalTime")
        self.CmdArgs = params.get("CmdArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResultInfo(AbstractModel):
    """任务结果信息。

    """

    def __init__(self):
        r"""
        :param TaskId: 任务唯一ID
        :type TaskId: str
        :param DatasourceConnectionName: 数据源名称，当前任务执行时候选中的默认数据源
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionName: str
        :param DatabaseName: 数据库名称，当前任务执行时候选中的默认数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param SQL: 当前执行的SQL，一个任务包含一个SQL
        :type SQL: str
        :param SQLType: 执行任务的类型，现在分为DDL、DML、DQL
        :type SQLType: str
        :param State: 任务当前的状态，0：初始化 1：任务运行中 2：任务执行成功 -1：任务执行失败 -3：用户手动终止。只有任务执行成功的情况下，才会返回任务执行的结果
        :type State: int
        :param DataAmount: 扫描的数据量，单位byte
        :type DataAmount: int
        :param UsedTime: 计算耗时，单位： ms
        :type UsedTime: int
        :param OutputPath: 任务结果输出的COS桶地址
        :type OutputPath: str
        :param CreateTime: 任务创建时间，时间戳
        :type CreateTime: str
        :param OutputMessage: 任务执行信息，成功时返回success，失败时返回失败原因
        :type OutputMessage: str
        :param RowAffectInfo: 被影响的行数
        :type RowAffectInfo: str
        :param ResultSchema: 结果的schema信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultSchema: list of Column
        :param ResultSet: 结果信息，反转义后，外层数组的每个元素为一行数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultSet: str
        :param NextToken: 分页信息，如果没有更多结果数据，nextToken为空
        :type NextToken: str
        :param Percentage: 任务执行进度num/100(%)
        :type Percentage: int
        :param ProgressDetail: 任务进度明细
        :type ProgressDetail: str
        :param DisplayFormat: 控制台展示格式。table：表格展示 text：文本展示
        :type DisplayFormat: str
        :param TotalTime: 任务耗时，单位： ms
        :type TotalTime: int
        """
        self.TaskId = None
        self.DatasourceConnectionName = None
        self.DatabaseName = None
        self.SQL = None
        self.SQLType = None
        self.State = None
        self.DataAmount = None
        self.UsedTime = None
        self.OutputPath = None
        self.CreateTime = None
        self.OutputMessage = None
        self.RowAffectInfo = None
        self.ResultSchema = None
        self.ResultSet = None
        self.NextToken = None
        self.Percentage = None
        self.ProgressDetail = None
        self.DisplayFormat = None
        self.TotalTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        self.DatabaseName = params.get("DatabaseName")
        self.SQL = params.get("SQL")
        self.SQLType = params.get("SQLType")
        self.State = params.get("State")
        self.DataAmount = params.get("DataAmount")
        self.UsedTime = params.get("UsedTime")
        self.OutputPath = params.get("OutputPath")
        self.CreateTime = params.get("CreateTime")
        self.OutputMessage = params.get("OutputMessage")
        self.RowAffectInfo = params.get("RowAffectInfo")
        if params.get("ResultSchema") is not None:
            self.ResultSchema = []
            for item in params.get("ResultSchema"):
                obj = Column()
                obj._deserialize(item)
                self.ResultSchema.append(obj)
        self.ResultSet = params.get("ResultSet")
        self.NextToken = params.get("NextToken")
        self.Percentage = params.get("Percentage")
        self.ProgressDetail = params.get("ProgressDetail")
        self.DisplayFormat = params.get("DisplayFormat")
        self.TotalTime = params.get("TotalTime")
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
        r"""
        :param TaskType: 任务类型，SQLTask：SQL查询任务。SparkSQLTask：Spark SQL查询任务
        :type TaskType: str
        :param FailureTolerance: 容错策略。Proceed：前面任务出错/取消后继续执行后面的任务。Terminate：前面的任务出错/取消之后终止后面任务的执行，后面的任务全部标记为已取消。
        :type FailureTolerance: str
        :param SQL: base64加密后的SQL语句，用";"号分隔每个SQL语句，一次最多提交50个任务。严格按照前后顺序执行
        :type SQL: str
        :param Config: 任务的配置信息，当前仅支持SparkSQLTask任务。
        :type Config: list of KVPair
        :param Params: 任务的用户自定义参数信息
        :type Params: list of KVPair
        """
        self.TaskType = None
        self.FailureTolerance = None
        self.SQL = None
        self.Config = None
        self.Params = None


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
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self.Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TasksOverview(AbstractModel):
    """任务概览

    """

    def __init__(self):
        r"""
        :param TaskQueuedCount: 正在排队的任务个数
        :type TaskQueuedCount: int
        :param TaskInitCount: 初始化的任务个数
        :type TaskInitCount: int
        :param TaskRunningCount: 正在执行的任务个数
        :type TaskRunningCount: int
        :param TotalTaskCount: 当前时间范围的总任务个数
        :type TotalTaskCount: int
        """
        self.TaskQueuedCount = None
        self.TaskInitCount = None
        self.TaskRunningCount = None
        self.TotalTaskCount = None


    def _deserialize(self, params):
        self.TaskQueuedCount = params.get("TaskQueuedCount")
        self.TaskInitCount = params.get("TaskInitCount")
        self.TaskRunningCount = params.get("TaskRunningCount")
        self.TotalTaskCount = params.get("TotalTaskCount")
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnlockMetaDataRequest(AbstractModel):
    """UnlockMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param LockId: 锁ID
        :type LockId: int
        :param DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        """
        self.LockId = None
        self.DatasourceConnectionName = None


    def _deserialize(self, params):
        self.LockId = params.get("LockId")
        self.DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockMetaDataResponse(AbstractModel):
    """UnlockMetaData返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param UserId: 用户Id，和子用户uin相同
        :type UserId: str
        :param UserDescription: 用户描述信息，方便区分不同用户
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDescription: str
        :param PolicySet: 单独给用户绑定的权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicySet: list of Policy
        :param Creator: 当前用户的创建者
        :type Creator: str
        :param CreateTime: 创建时间，格式如2021-07-28 16:19:32
        :type CreateTime: str
        :param WorkGroupSet: 关联的工作组集合
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupSet: list of WorkGroupMessage
        :param IsOwner: 是否是主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOwner: bool
        :param UserType: 用户类型。ADMIN：管理员 COMMON：普通用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param UserAlias: 用户别名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        """
        self.UserId = None
        self.UserDescription = None
        self.PolicySet = None
        self.Creator = None
        self.CreateTime = None
        self.WorkGroupSet = None
        self.IsOwner = None
        self.UserType = None
        self.UserAlias = None


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
        self.UserType = params.get("UserType")
        self.UserAlias = params.get("UserAlias")
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
        r"""
        :param UserId: 用户Id，和CAM侧子用户Uin匹配
        :type UserId: str
        :param UserDescription: 用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDescription: str
        :param Creator: 当前用户的创建者
        :type Creator: str
        :param CreateTime: 当前用户的创建时间，形如2021-07-28 16:19:32
        :type CreateTime: str
        :param UserAlias: 用户别名
        :type UserAlias: str
        """
        self.UserId = None
        self.UserDescription = None
        self.Creator = None
        self.CreateTime = None
        self.UserAlias = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserDescription = params.get("UserDescription")
        self.Creator = params.get("Creator")
        self.CreateTime = params.get("CreateTime")
        self.UserAlias = params.get("UserAlias")
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
        r"""
        :param DatabaseName: 该视图所属数据库名字
        :type DatabaseName: str
        :param ViewName: 视图名称
        :type ViewName: str
        :param UserAlias: 视图创建人昵称
        :type UserAlias: str
        :param UserSubUin: 视图创建人ID
        :type UserSubUin: str
        """
        self.DatabaseName = None
        self.ViewName = None
        self.UserAlias = None
        self.UserSubUin = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.ViewName = params.get("ViewName")
        self.UserAlias = params.get("UserAlias")
        self.UserSubUin = params.get("UserSubUin")
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
        r"""
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
        r"""
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
        r"""
        :param WorkGroupId: 查询到的工作组唯一Id
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
        :param Creator: 工作组的创建人
        :type Creator: str
        :param CreateTime: 工作组的创建时间，形如2021-07-28 16:19:32
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
        r"""
        :param WorkGroupId: 工作组唯一Id
        :type WorkGroupId: int
        :param WorkGroupName: 工作组名称
        :type WorkGroupName: str
        :param WorkGroupDescription: 工作组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupDescription: str
        :param Creator: 创建者
        :type Creator: str
        :param CreateTime: 工作组创建的时间，形如2021-07-28 16:19:32
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
        