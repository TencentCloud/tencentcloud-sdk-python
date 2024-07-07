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


class AccessInfo(AbstractModel):
    """引擎的访问信息

    """

    def __init__(self):
        r"""
        :param _AccessType: 访问引擎的方法
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: str
        :param _AccessConnectionInfos: 访问引擎的url，内部的部分参数需要根据实际情况替换
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessConnectionInfos: list of str
        """
        self._AccessType = None
        self._AccessConnectionInfos = None

    @property
    def AccessType(self):
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def AccessConnectionInfos(self):
        return self._AccessConnectionInfos

    @AccessConnectionInfos.setter
    def AccessConnectionInfos(self, AccessConnectionInfos):
        self._AccessConnectionInfos = AccessConnectionInfos


    def _deserialize(self, params):
        self._AccessType = params.get("AccessType")
        self._AccessConnectionInfos = params.get("AccessConnectionInfos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDMSPartitionsRequest(AbstractModel):
    """AddDMSPartitions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 分区
        :type Partitions: list of DMSPartition
        """
        self._Partitions = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDMSPartitionsResponse(AbstractModel):
    """AddDMSPartitions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 成功数量
        :type Total: int
        :param _Partitions: 分区值
        :type Partitions: list of DMSPartition
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Partitions = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class AddOptimizerEnginesRequest(AbstractModel):
    """AddOptimizerEngines请求参数结构体

    """


class AddOptimizerEnginesResponse(AbstractModel):
    """AddOptimizerEngines返回参数结构体

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


class AddUsersToWorkGroupRequest(AbstractModel):
    """AddUsersToWorkGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AddInfo: 要操作的工作组和用户信息
        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.UserIdSetOfWorkGroupId`
        """
        self._AddInfo = None

    @property
    def AddInfo(self):
        return self._AddInfo

    @AddInfo.setter
    def AddInfo(self, AddInfo):
        self._AddInfo = AddInfo


    def _deserialize(self, params):
        if params.get("AddInfo") is not None:
            self._AddInfo = UserIdSetOfWorkGroupId()
            self._AddInfo._deserialize(params.get("AddInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUsersToWorkGroupResponse(AbstractModel):
    """AddUsersToWorkGroup返回参数结构体

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


class AlterDMSDatabaseRequest(AbstractModel):
    """AlterDMSDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CurrentName: 当前名称
        :type CurrentName: str
        :param _SchemaName: schema名称
        :type SchemaName: str
        :param _Location: 路径
        :type Location: str
        :param _Asset: 基础对象
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        """
        self._CurrentName = None
        self._SchemaName = None
        self._Location = None
        self._Asset = None

    @property
    def CurrentName(self):
        return self._CurrentName

    @CurrentName.setter
    def CurrentName(self, CurrentName):
        self._CurrentName = CurrentName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset


    def _deserialize(self, params):
        self._CurrentName = params.get("CurrentName")
        self._SchemaName = params.get("SchemaName")
        self._Location = params.get("Location")
        if params.get("Asset") is not None:
            self._Asset = Asset()
            self._Asset._deserialize(params.get("Asset"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlterDMSDatabaseResponse(AbstractModel):
    """AlterDMSDatabase返回参数结构体

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


class AlterDMSPartitionRequest(AbstractModel):
    """AlterDMSPartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CurrentDbName: 当前名称，变更前db名称
        :type CurrentDbName: str
        :param _CurrentTableName: 当前名称，变更前table名称
        :type CurrentTableName: str
        :param _CurrentValues: 当前名称，变更前Part名称
        :type CurrentValues: str
        :param _Partition: 分区
        :type Partition: :class:`tencentcloud.dlc.v20210125.models.DMSPartition`
        """
        self._CurrentDbName = None
        self._CurrentTableName = None
        self._CurrentValues = None
        self._Partition = None

    @property
    def CurrentDbName(self):
        return self._CurrentDbName

    @CurrentDbName.setter
    def CurrentDbName(self, CurrentDbName):
        self._CurrentDbName = CurrentDbName

    @property
    def CurrentTableName(self):
        return self._CurrentTableName

    @CurrentTableName.setter
    def CurrentTableName(self, CurrentTableName):
        self._CurrentTableName = CurrentTableName

    @property
    def CurrentValues(self):
        return self._CurrentValues

    @CurrentValues.setter
    def CurrentValues(self, CurrentValues):
        self._CurrentValues = CurrentValues

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._CurrentDbName = params.get("CurrentDbName")
        self._CurrentTableName = params.get("CurrentTableName")
        self._CurrentValues = params.get("CurrentValues")
        if params.get("Partition") is not None:
            self._Partition = DMSPartition()
            self._Partition._deserialize(params.get("Partition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlterDMSPartitionResponse(AbstractModel):
    """AlterDMSPartition返回参数结构体

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


class AlterDMSTableRequest(AbstractModel):
    """AlterDMSTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CurrentName: 当前名称
        :type CurrentName: str
        :param _CurrentDbName: 当前数据库名称
        :type CurrentDbName: str
        :param _Asset: 基础对象
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param _Type: 表类型
        :type Type: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _StorageSize: 存储大小
        :type StorageSize: int
        :param _RecordCount: 记录数量
        :type RecordCount: int
        :param _LifeTime: 生命周期
        :type LifeTime: int
        :param _DataUpdateTime: 数据更新时间
        :type DataUpdateTime: str
        :param _StructUpdateTime: 结构更新时间
        :type StructUpdateTime: str
        :param _LastAccessTime: 最后访问时间
        :type LastAccessTime: str
        :param _Sds: 存储对象
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        :param _Columns: 列
        :type Columns: list of DMSColumn
        :param _PartitionKeys: 分区键值
        :type PartitionKeys: list of DMSColumn
        :param _ViewOriginalText: 视图文本
        :type ViewOriginalText: str
        :param _ViewExpandedText: 视图文本
        :type ViewExpandedText: str
        :param _Partitions: 分区
        :type Partitions: list of DMSPartition
        :param _Name: 当前表名
        :type Name: str
        """
        self._CurrentName = None
        self._CurrentDbName = None
        self._Asset = None
        self._Type = None
        self._DbName = None
        self._StorageSize = None
        self._RecordCount = None
        self._LifeTime = None
        self._DataUpdateTime = None
        self._StructUpdateTime = None
        self._LastAccessTime = None
        self._Sds = None
        self._Columns = None
        self._PartitionKeys = None
        self._ViewOriginalText = None
        self._ViewExpandedText = None
        self._Partitions = None
        self._Name = None

    @property
    def CurrentName(self):
        return self._CurrentName

    @CurrentName.setter
    def CurrentName(self, CurrentName):
        self._CurrentName = CurrentName

    @property
    def CurrentDbName(self):
        return self._CurrentDbName

    @CurrentDbName.setter
    def CurrentDbName(self, CurrentDbName):
        self._CurrentDbName = CurrentDbName

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def StorageSize(self):
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def LifeTime(self):
        return self._LifeTime

    @LifeTime.setter
    def LifeTime(self, LifeTime):
        self._LifeTime = LifeTime

    @property
    def DataUpdateTime(self):
        return self._DataUpdateTime

    @DataUpdateTime.setter
    def DataUpdateTime(self, DataUpdateTime):
        self._DataUpdateTime = DataUpdateTime

    @property
    def StructUpdateTime(self):
        return self._StructUpdateTime

    @StructUpdateTime.setter
    def StructUpdateTime(self, StructUpdateTime):
        self._StructUpdateTime = StructUpdateTime

    @property
    def LastAccessTime(self):
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def Sds(self):
        return self._Sds

    @Sds.setter
    def Sds(self, Sds):
        self._Sds = Sds

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def PartitionKeys(self):
        return self._PartitionKeys

    @PartitionKeys.setter
    def PartitionKeys(self, PartitionKeys):
        self._PartitionKeys = PartitionKeys

    @property
    def ViewOriginalText(self):
        return self._ViewOriginalText

    @ViewOriginalText.setter
    def ViewOriginalText(self, ViewOriginalText):
        self._ViewOriginalText = ViewOriginalText

    @property
    def ViewExpandedText(self):
        return self._ViewExpandedText

    @ViewExpandedText.setter
    def ViewExpandedText(self, ViewExpandedText):
        self._ViewExpandedText = ViewExpandedText

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._CurrentName = params.get("CurrentName")
        self._CurrentDbName = params.get("CurrentDbName")
        if params.get("Asset") is not None:
            self._Asset = Asset()
            self._Asset._deserialize(params.get("Asset"))
        self._Type = params.get("Type")
        self._DbName = params.get("DbName")
        self._StorageSize = params.get("StorageSize")
        self._RecordCount = params.get("RecordCount")
        self._LifeTime = params.get("LifeTime")
        self._DataUpdateTime = params.get("DataUpdateTime")
        self._StructUpdateTime = params.get("StructUpdateTime")
        self._LastAccessTime = params.get("LastAccessTime")
        if params.get("Sds") is not None:
            self._Sds = DMSSds()
            self._Sds._deserialize(params.get("Sds"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("PartitionKeys") is not None:
            self._PartitionKeys = []
            for item in params.get("PartitionKeys"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._PartitionKeys.append(obj)
        self._ViewOriginalText = params.get("ViewOriginalText")
        self._ViewExpandedText = params.get("ViewExpandedText")
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlterDMSTableResponse(AbstractModel):
    """AlterDMSTable返回参数结构体

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


class Asset(AbstractModel):
    """元数据基本对象

    """

    def __init__(self):
        r"""
        :param _Id: 主键
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Guid: 对象GUID值
注意：此字段可能返回 null，表示取不到有效值。
        :type Guid: str
        :param _Catalog: 数据目录
注意：此字段可能返回 null，表示取不到有效值。
        :type Catalog: str
        :param _Description: 描述信息
        :type Description: str
        :param _Owner: 对象owner
        :type Owner: str
        :param _OwnerAccount: 对象owner账户
        :type OwnerAccount: str
        :param _PermValues: 权限
        :type PermValues: list of KVPair
        :param _Params: 附加属性
        :type Params: list of KVPair
        :param _BizParams: 附加业务属性
        :type BizParams: list of KVPair
        :param _DataVersion: 数据版本
        :type DataVersion: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifiedTime: 修改时间
        :type ModifiedTime: str
        :param _DatasourceId: 数据源主键
        :type DatasourceId: int
        """
        self._Id = None
        self._Name = None
        self._Guid = None
        self._Catalog = None
        self._Description = None
        self._Owner = None
        self._OwnerAccount = None
        self._PermValues = None
        self._Params = None
        self._BizParams = None
        self._DataVersion = None
        self._CreateTime = None
        self._ModifiedTime = None
        self._DatasourceId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Guid(self):
        return self._Guid

    @Guid.setter
    def Guid(self, Guid):
        self._Guid = Guid

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def OwnerAccount(self):
        return self._OwnerAccount

    @OwnerAccount.setter
    def OwnerAccount(self, OwnerAccount):
        self._OwnerAccount = OwnerAccount

    @property
    def PermValues(self):
        return self._PermValues

    @PermValues.setter
    def PermValues(self, PermValues):
        self._PermValues = PermValues

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def BizParams(self):
        return self._BizParams

    @BizParams.setter
    def BizParams(self, BizParams):
        self._BizParams = BizParams

    @property
    def DataVersion(self):
        return self._DataVersion

    @DataVersion.setter
    def DataVersion(self, DataVersion):
        self._DataVersion = DataVersion

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def DatasourceId(self):
        return self._DatasourceId

    @DatasourceId.setter
    def DatasourceId(self, DatasourceId):
        self._DatasourceId = DatasourceId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Guid = params.get("Guid")
        self._Catalog = params.get("Catalog")
        self._Description = params.get("Description")
        self._Owner = params.get("Owner")
        self._OwnerAccount = params.get("OwnerAccount")
        if params.get("PermValues") is not None:
            self._PermValues = []
            for item in params.get("PermValues"):
                obj = KVPair()
                obj._deserialize(item)
                self._PermValues.append(obj)
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self._Params.append(obj)
        if params.get("BizParams") is not None:
            self._BizParams = []
            for item in params.get("BizParams"):
                obj = KVPair()
                obj._deserialize(item)
                self._BizParams.append(obj)
        self._DataVersion = params.get("DataVersion")
        self._CreateTime = params.get("CreateTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._DatasourceId = params.get("DatasourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignMangedTablePropertiesRequest(AbstractModel):
    """AssignMangedTableProperties请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableBaseInfo: 表基本信息
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param _Columns: 表字段信息
        :type Columns: list of TColumn
        :param _Partitions: 表分区信息
        :type Partitions: list of TPartition
        :param _Properties: 表属性信息
        :type Properties: list of Property
        :param _UpsertKeys: V2 upsert表 upsert键
        :type UpsertKeys: list of str
        """
        self._TableBaseInfo = None
        self._Columns = None
        self._Partitions = None
        self._Properties = None
        self._UpsertKeys = None

    @property
    def TableBaseInfo(self):
        return self._TableBaseInfo

    @TableBaseInfo.setter
    def TableBaseInfo(self, TableBaseInfo):
        self._TableBaseInfo = TableBaseInfo

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def UpsertKeys(self):
        return self._UpsertKeys

    @UpsertKeys.setter
    def UpsertKeys(self, UpsertKeys):
        self._UpsertKeys = UpsertKeys


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self._TableBaseInfo = TableBaseInfo()
            self._TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = TColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = TPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._UpsertKeys = params.get("UpsertKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignMangedTablePropertiesResponse(AbstractModel):
    """AssignMangedTableProperties返回参数结构体

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


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id，和子用户uin相同，需要先使用CreateUser接口创建用户。可以使用DescribeUsers接口查看。
        :type UserId: str
        :param _PolicySet: 鉴权策略集合
        :type PolicySet: list of Policy
        """
        self._UserId = None
        self._PolicySet = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy返回参数结构体

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


class AttachWorkGroupPolicyRequest(AbstractModel):
    """AttachWorkGroupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param _PolicySet: 要绑定的策略集合
        :type PolicySet: list of Policy
        """
        self._WorkGroupId = None
        self._PolicySet = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachWorkGroupPolicyResponse(AbstractModel):
    """AttachWorkGroupPolicy返回参数结构体

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


class BatchSQLCostInfo(AbstractModel):
    """spark session batch SQL的消耗信息

    """

    def __init__(self):
        r"""
        :param _BatchId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param _DataEngineName: 引擎名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineName: str
        :param _DataEngineId: 引擎id
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineId: str
        :param _Cost: 本次消耗，单位cu
注意：此字段可能返回 null，表示取不到有效值。
        :type Cost: float
        :param _TimeCost: 时间开销，秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeCost: int
        :param _Operator: 操作者
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        """
        self._BatchId = None
        self._DataEngineName = None
        self._DataEngineId = None
        self._Cost = None
        self._TimeCost = None
        self._Operator = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def TimeCost(self):
        return self._TimeCost

    @TimeCost.setter
    def TimeCost(self, TimeCost):
        self._TimeCost = TimeCost

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._DataEngineName = params.get("DataEngineName")
        self._DataEngineId = params.get("DataEngineId")
        self._Cost = params.get("Cost")
        self._TimeCost = params.get("TimeCost")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSqlTask(AbstractModel):
    """SparkSQL批任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: SQL子任务唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _ExecuteSQL: 运行SQL
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecuteSQL: str
        :param _Message: 任务信息，成功则返回：Task Success!，失败则返回异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._TaskId = None
        self._ExecuteSQL = None
        self._Message = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ExecuteSQL(self):
        return self._ExecuteSQL

    @ExecuteSQL.setter
    def ExecuteSQL(self, ExecuteSQL):
        self._ExecuteSQL = ExecuteSQL

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ExecuteSQL = params.get("ExecuteSQL")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindWorkGroupsToUserRequest(AbstractModel):
    """BindWorkGroupsToUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AddInfo: 绑定的用户和工作组信息
        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.WorkGroupIdSetOfUserId`
        """
        self._AddInfo = None

    @property
    def AddInfo(self):
        return self._AddInfo

    @AddInfo.setter
    def AddInfo(self, AddInfo):
        self._AddInfo = AddInfo


    def _deserialize(self, params):
        if params.get("AddInfo") is not None:
            self._AddInfo = WorkGroupIdSetOfUserId()
            self._AddInfo._deserialize(params.get("AddInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindWorkGroupsToUserResponse(AbstractModel):
    """BindWorkGroupsToUser返回参数结构体

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


class CHDFSProductVpcInfo(AbstractModel):
    """chdfs产品vpc信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id

注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _VpcCidrBlock: vpc子网信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcCidrBlock: list of VpcCidrBlock
        :param _RuleId: 规则Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param _AccessGroupId: 权限组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessGroupId: str
        """
        self._VpcId = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._RuleId = None
        self._AccessGroupId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("VpcCidrBlock") is not None:
            self._VpcCidrBlock = []
            for item in params.get("VpcCidrBlock"):
                obj = VpcCidrBlock()
                obj._deserialize(item)
                self._VpcCidrBlock.append(obj)
        self._RuleId = params.get("RuleId")
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CSV(AbstractModel):
    """CSV类型数据格式

    """

    def __init__(self):
        r"""
        :param _CodeCompress: 压缩格式，["Snappy", "Gzip", "None"选一]。
        :type CodeCompress: str
        :param _CSVSerde: CSV序列化及反序列化数据结构。
        :type CSVSerde: :class:`tencentcloud.dlc.v20210125.models.CSVSerde`
        :param _HeadLines: 标题行，默认为0。
        :type HeadLines: int
        :param _Format: 格式，默认值为CSV
        :type Format: str
        """
        self._CodeCompress = None
        self._CSVSerde = None
        self._HeadLines = None
        self._Format = None

    @property
    def CodeCompress(self):
        return self._CodeCompress

    @CodeCompress.setter
    def CodeCompress(self, CodeCompress):
        self._CodeCompress = CodeCompress

    @property
    def CSVSerde(self):
        return self._CSVSerde

    @CSVSerde.setter
    def CSVSerde(self, CSVSerde):
        self._CSVSerde = CSVSerde

    @property
    def HeadLines(self):
        return self._HeadLines

    @HeadLines.setter
    def HeadLines(self, HeadLines):
        self._HeadLines = HeadLines

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._CodeCompress = params.get("CodeCompress")
        if params.get("CSVSerde") is not None:
            self._CSVSerde = CSVSerde()
            self._CSVSerde._deserialize(params.get("CSVSerde"))
        self._HeadLines = params.get("HeadLines")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CSVSerde(AbstractModel):
    """CSV序列化及反序列化数据结构

    """

    def __init__(self):
        r"""
        :param _Escape: CSV序列化转义符，默认为"\\"，最长8个字符，如 Escape: "/\"
        :type Escape: str
        :param _Quote: CSV序列化字段域符，默认为"'"，最长8个字符, 如 Quote: "\""
        :type Quote: str
        :param _Separator: CSV序列化分隔符，默认为"\t"，最长8个字符, 如 Separator: "\t"
        :type Separator: str
        """
        self._Escape = None
        self._Quote = None
        self._Separator = None

    @property
    def Escape(self):
        return self._Escape

    @Escape.setter
    def Escape(self, Escape):
        self._Escape = Escape

    @property
    def Quote(self):
        return self._Quote

    @Quote.setter
    def Quote(self, Quote):
        self._Quote = Quote

    @property
    def Separator(self):
        return self._Separator

    @Separator.setter
    def Separator(self, Separator):
        self._Separator = Separator


    def _deserialize(self, params):
        self._Escape = params.get("Escape")
        self._Quote = params.get("Quote")
        self._Separator = params.get("Separator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelNotebookSessionStatementBatchRequest(AbstractModel):
    """CancelNotebookSessionStatementBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _BatchId: 批任务唯一标识
        :type BatchId: str
        """
        self._SessionId = None
        self._BatchId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelNotebookSessionStatementBatchResponse(AbstractModel):
    """CancelNotebookSessionStatementBatch返回参数结构体

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


class CancelNotebookSessionStatementRequest(AbstractModel):
    """CancelNotebookSessionStatement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _StatementId: Session Statement唯一标识
        :type StatementId: str
        """
        self._SessionId = None
        self._StatementId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def StatementId(self):
        return self._StatementId

    @StatementId.setter
    def StatementId(self, StatementId):
        self._StatementId = StatementId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._StatementId = params.get("StatementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelNotebookSessionStatementResponse(AbstractModel):
    """CancelNotebookSessionStatement返回参数结构体

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


class CancelSparkSessionBatchSQLRequest(AbstractModel):
    """CancelSparkSessionBatchSQL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批任务唯一标识
        :type BatchId: str
        :param _CustomKey: 用户自定义主键，若不为空，则使用该值进行查询
        :type CustomKey: str
        """
        self._BatchId = None
        self._CustomKey = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def CustomKey(self):
        return self._CustomKey

    @CustomKey.setter
    def CustomKey(self, CustomKey):
        self._CustomKey = CustomKey


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._CustomKey = params.get("CustomKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelSparkSessionBatchSQLResponse(AbstractModel):
    """CancelSparkSessionBatchSQL返回参数结构体

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


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id，全局唯一
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
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

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


class CheckDataEngineConfigPairsValidityRequest(AbstractModel):
    """CheckDataEngineConfigPairsValidity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChildImageVersionId: 引擎小版本ID
        :type ChildImageVersionId: str
        :param _DataEngineConfigPairs: 用户自定义参数
        :type DataEngineConfigPairs: list of DataEngineConfigPair
        :param _ImageVersionId: 引擎大版本ID，存在小版本ID时仅需传入小版本ID，不存在时会获取当前大版本下最新的小版本ID。
        :type ImageVersionId: str
        """
        self._ChildImageVersionId = None
        self._DataEngineConfigPairs = None
        self._ImageVersionId = None

    @property
    def ChildImageVersionId(self):
        return self._ChildImageVersionId

    @ChildImageVersionId.setter
    def ChildImageVersionId(self, ChildImageVersionId):
        self._ChildImageVersionId = ChildImageVersionId

    @property
    def DataEngineConfigPairs(self):
        return self._DataEngineConfigPairs

    @DataEngineConfigPairs.setter
    def DataEngineConfigPairs(self, DataEngineConfigPairs):
        self._DataEngineConfigPairs = DataEngineConfigPairs

    @property
    def ImageVersionId(self):
        return self._ImageVersionId

    @ImageVersionId.setter
    def ImageVersionId(self, ImageVersionId):
        self._ImageVersionId = ImageVersionId


    def _deserialize(self, params):
        self._ChildImageVersionId = params.get("ChildImageVersionId")
        if params.get("DataEngineConfigPairs") is not None:
            self._DataEngineConfigPairs = []
            for item in params.get("DataEngineConfigPairs"):
                obj = DataEngineConfigPair()
                obj._deserialize(item)
                self._DataEngineConfigPairs.append(obj)
        self._ImageVersionId = params.get("ImageVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDataEngineConfigPairsValidityResponse(AbstractModel):
    """CheckDataEngineConfigPairsValidity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAvailable: 参数有效性：ture:有效，false:至少存在一个无效参数；
        :type IsAvailable: bool
        :param _UnavailableConfig: 无效参数集合
注意：此字段可能返回 null，表示取不到有效值。
        :type UnavailableConfig: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsAvailable = None
        self._UnavailableConfig = None
        self._RequestId = None

    @property
    def IsAvailable(self):
        return self._IsAvailable

    @IsAvailable.setter
    def IsAvailable(self, IsAvailable):
        self._IsAvailable = IsAvailable

    @property
    def UnavailableConfig(self):
        return self._UnavailableConfig

    @UnavailableConfig.setter
    def UnavailableConfig(self, UnavailableConfig):
        self._UnavailableConfig = UnavailableConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsAvailable = params.get("IsAvailable")
        self._UnavailableConfig = params.get("UnavailableConfig")
        self._RequestId = params.get("RequestId")


class CheckDataEngineImageCanBeRollbackRequest(AbstractModel):
    """CheckDataEngineImageCanBeRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 引擎唯一id
        :type DataEngineId: str
        """
        self._DataEngineId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDataEngineImageCanBeRollbackResponse(AbstractModel):
    """CheckDataEngineImageCanBeRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ToRecordId: 回滚后日志记录id
        :type ToRecordId: str
        :param _FromRecordId: 回滚前日志记录id
        :type FromRecordId: str
        :param _IsRollback: 是否能够回滚
        :type IsRollback: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ToRecordId = None
        self._FromRecordId = None
        self._IsRollback = None
        self._RequestId = None

    @property
    def ToRecordId(self):
        return self._ToRecordId

    @ToRecordId.setter
    def ToRecordId(self, ToRecordId):
        self._ToRecordId = ToRecordId

    @property
    def FromRecordId(self):
        return self._FromRecordId

    @FromRecordId.setter
    def FromRecordId(self, FromRecordId):
        self._FromRecordId = FromRecordId

    @property
    def IsRollback(self):
        return self._IsRollback

    @IsRollback.setter
    def IsRollback(self, IsRollback):
        self._IsRollback = IsRollback

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ToRecordId = params.get("ToRecordId")
        self._FromRecordId = params.get("FromRecordId")
        self._IsRollback = params.get("IsRollback")
        self._RequestId = params.get("RequestId")


class CheckDataEngineImageCanBeUpgradeRequest(AbstractModel):
    """CheckDataEngineImageCanBeUpgrade请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 集群id
        :type DataEngineId: str
        """
        self._DataEngineId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDataEngineImageCanBeUpgradeResponse(AbstractModel):
    """CheckDataEngineImageCanBeUpgrade返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ChildImageVersionId: 当前大版本下，可升级的集群镜像小版本id
        :type ChildImageVersionId: str
        :param _IsUpgrade: 是否能够升级
        :type IsUpgrade: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ChildImageVersionId = None
        self._IsUpgrade = None
        self._RequestId = None

    @property
    def ChildImageVersionId(self):
        return self._ChildImageVersionId

    @ChildImageVersionId.setter
    def ChildImageVersionId(self, ChildImageVersionId):
        self._ChildImageVersionId = ChildImageVersionId

    @property
    def IsUpgrade(self):
        return self._IsUpgrade

    @IsUpgrade.setter
    def IsUpgrade(self, IsUpgrade):
        self._IsUpgrade = IsUpgrade

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ChildImageVersionId = params.get("ChildImageVersionId")
        self._IsUpgrade = params.get("IsUpgrade")
        self._RequestId = params.get("RequestId")


class CheckLockMetaDataRequest(AbstractModel):
    """CheckLockMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LockId: 锁ID
        :type LockId: int
        :param _DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        :param _TxnId: 事务ID
        :type TxnId: int
        :param _ElapsedMs: 过期时间ms
        :type ElapsedMs: int
        """
        self._LockId = None
        self._DatasourceConnectionName = None
        self._TxnId = None
        self._ElapsedMs = None

    @property
    def LockId(self):
        return self._LockId

    @LockId.setter
    def LockId(self, LockId):
        self._LockId = LockId

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def TxnId(self):
        return self._TxnId

    @TxnId.setter
    def TxnId(self, TxnId):
        self._TxnId = TxnId

    @property
    def ElapsedMs(self):
        return self._ElapsedMs

    @ElapsedMs.setter
    def ElapsedMs(self, ElapsedMs):
        self._ElapsedMs = ElapsedMs


    def _deserialize(self, params):
        self._LockId = params.get("LockId")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._TxnId = params.get("TxnId")
        self._ElapsedMs = params.get("ElapsedMs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckLockMetaDataResponse(AbstractModel):
    """CheckLockMetaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LockId: 锁ID
        :type LockId: int
        :param _LockState: 锁状态：ACQUIRED、WAITING、ABORT、NOT_ACQUIRED
        :type LockState: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LockId = None
        self._LockState = None
        self._RequestId = None

    @property
    def LockId(self):
        return self._LockId

    @LockId.setter
    def LockId(self, LockId):
        self._LockId = LockId

    @property
    def LockState(self):
        return self._LockState

    @LockState.setter
    def LockState(self, LockState):
        self._LockState = LockState

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LockId = params.get("LockId")
        self._LockState = params.get("LockState")
        self._RequestId = params.get("RequestId")


class Column(AbstractModel):
    """数据表列信息。

    """

    def __init__(self):
        r"""
        :param _Name: 列名称，不区分大小写，最大支持25个字符。
        :type Name: str
        :param _Type: 列类型，支持如下类型定义:
string|tinyint|smallint|int|bigint|boolean|float|double|decimal|timestamp|date|binary|array<data_type>|map<primitive_type, data_type>|struct<col_name : data_type [COMMENT col_comment], ...>|uniontype<data_type, data_type, ...>。
        :type Type: str
        :param _Comment: 对该类的注释。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _Precision: 表示整个 numeric 的长度
注意：此字段可能返回 null，表示取不到有效值。
        :type Precision: int
        :param _Scale: 表示小数部分的长度
注意：此字段可能返回 null，表示取不到有效值。
        :type Scale: int
        :param _Nullable: 是否为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Nullable: str
        :param _Position: 字段位置，小的在前
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: int
        :param _CreateTime: 字段创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifiedTime: 字段修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _IsPartition: 是否为分区字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPartition: bool
        """
        self._Name = None
        self._Type = None
        self._Comment = None
        self._Precision = None
        self._Scale = None
        self._Nullable = None
        self._Position = None
        self._CreateTime = None
        self._ModifiedTime = None
        self._IsPartition = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Precision(self):
        return self._Precision

    @Precision.setter
    def Precision(self, Precision):
        self._Precision = Precision

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def Nullable(self):
        return self._Nullable

    @Nullable.setter
    def Nullable(self, Nullable):
        self._Nullable = Nullable

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def IsPartition(self):
        return self._IsPartition

    @IsPartition.setter
    def IsPartition(self, IsPartition):
        self._IsPartition = IsPartition


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Comment = params.get("Comment")
        self._Precision = params.get("Precision")
        self._Scale = params.get("Scale")
        self._Nullable = params.get("Nullable")
        self._Position = params.get("Position")
        self._CreateTime = params.get("CreateTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._IsPartition = params.get("IsPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMetrics(AbstractModel):
    """任务公共指标

    """

    def __init__(self):
        r"""
        :param _CreateTaskTime: 创建任务时长，单位：ms
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTaskTime: float
        :param _ProcessTime: 预处理总时长，单位：ms
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessTime: float
        :param _QueueTime: 排队时长，单位：ms
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueTime: float
        :param _ExecutionTime: 执行时长，单位：ms
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionTime: float
        :param _IsResultCacheHit: 是否命中结果缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IsResultCacheHit: bool
        :param _MatchedMVBytes: 匹配物化视图数据量
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchedMVBytes: int
        :param _MatchedMVs: 匹配物化视图列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchedMVs: str
        :param _AffectedBytes: 结果数据量，单位：byte
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedBytes: str
        :param _AffectedRows: 	结果行数
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedRows: int
        :param _ProcessedBytes: 扫描数据量，单位：byte
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedBytes: int
        :param _ProcessedRows: 	扫描行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedRows: int
        """
        self._CreateTaskTime = None
        self._ProcessTime = None
        self._QueueTime = None
        self._ExecutionTime = None
        self._IsResultCacheHit = None
        self._MatchedMVBytes = None
        self._MatchedMVs = None
        self._AffectedBytes = None
        self._AffectedRows = None
        self._ProcessedBytes = None
        self._ProcessedRows = None

    @property
    def CreateTaskTime(self):
        return self._CreateTaskTime

    @CreateTaskTime.setter
    def CreateTaskTime(self, CreateTaskTime):
        self._CreateTaskTime = CreateTaskTime

    @property
    def ProcessTime(self):
        return self._ProcessTime

    @ProcessTime.setter
    def ProcessTime(self, ProcessTime):
        self._ProcessTime = ProcessTime

    @property
    def QueueTime(self):
        return self._QueueTime

    @QueueTime.setter
    def QueueTime(self, QueueTime):
        self._QueueTime = QueueTime

    @property
    def ExecutionTime(self):
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def IsResultCacheHit(self):
        return self._IsResultCacheHit

    @IsResultCacheHit.setter
    def IsResultCacheHit(self, IsResultCacheHit):
        self._IsResultCacheHit = IsResultCacheHit

    @property
    def MatchedMVBytes(self):
        return self._MatchedMVBytes

    @MatchedMVBytes.setter
    def MatchedMVBytes(self, MatchedMVBytes):
        self._MatchedMVBytes = MatchedMVBytes

    @property
    def MatchedMVs(self):
        return self._MatchedMVs

    @MatchedMVs.setter
    def MatchedMVs(self, MatchedMVs):
        self._MatchedMVs = MatchedMVs

    @property
    def AffectedBytes(self):
        return self._AffectedBytes

    @AffectedBytes.setter
    def AffectedBytes(self, AffectedBytes):
        self._AffectedBytes = AffectedBytes

    @property
    def AffectedRows(self):
        return self._AffectedRows

    @AffectedRows.setter
    def AffectedRows(self, AffectedRows):
        self._AffectedRows = AffectedRows

    @property
    def ProcessedBytes(self):
        return self._ProcessedBytes

    @ProcessedBytes.setter
    def ProcessedBytes(self, ProcessedBytes):
        self._ProcessedBytes = ProcessedBytes

    @property
    def ProcessedRows(self):
        return self._ProcessedRows

    @ProcessedRows.setter
    def ProcessedRows(self, ProcessedRows):
        self._ProcessedRows = ProcessedRows


    def _deserialize(self, params):
        self._CreateTaskTime = params.get("CreateTaskTime")
        self._ProcessTime = params.get("ProcessTime")
        self._QueueTime = params.get("QueueTime")
        self._ExecutionTime = params.get("ExecutionTime")
        self._IsResultCacheHit = params.get("IsResultCacheHit")
        self._MatchedMVBytes = params.get("MatchedMVBytes")
        self._MatchedMVs = params.get("MatchedMVs")
        self._AffectedBytes = params.get("AffectedBytes")
        self._AffectedRows = params.get("AffectedRows")
        self._ProcessedBytes = params.get("ProcessedBytes")
        self._ProcessedRows = params.get("ProcessedRows")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosPermission(AbstractModel):
    """cos权限描述

    """

    def __init__(self):
        r"""
        :param _CosPath: cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPath: str
        :param _Permissions: 权限【"read","write"】
注意：此字段可能返回 null，表示取不到有效值。
        :type Permissions: list of str
        """
        self._CosPath = None
        self._Permissions = None

    @property
    def CosPath(self):
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._CosPath = params.get("CosPath")
        self._Permissions = params.get("Permissions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCHDFSBindingProductRequest(AbstractModel):
    """CreateCHDFSBindingProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPoint: 需要绑定的元数据加速桶名
        :type MountPoint: str
        :param _BucketType: 桶的类型，分为cos和lakefs
        :type BucketType: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _EngineName: 引擎名称，ProductName选择DLC产品时，必传此参数。其他产品可不传
        :type EngineName: str
        :param _VpcInfo: vpc信息，产品名称为other时必传此参数
        :type VpcInfo: list of VpcInfo
        """
        self._MountPoint = None
        self._BucketType = None
        self._ProductName = None
        self._EngineName = None
        self._VpcInfo = None

    @property
    def MountPoint(self):
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def BucketType(self):
        return self._BucketType

    @BucketType.setter
    def BucketType(self, BucketType):
        self._BucketType = BucketType

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def EngineName(self):
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def VpcInfo(self):
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo


    def _deserialize(self, params):
        self._MountPoint = params.get("MountPoint")
        self._BucketType = params.get("BucketType")
        self._ProductName = params.get("ProductName")
        self._EngineName = params.get("EngineName")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCHDFSBindingProductResponse(AbstractModel):
    """CreateCHDFSBindingProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointAssociates: 绑定信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MountPointAssociates: list of MountPointAssociates
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MountPointAssociates = None
        self._RequestId = None

    @property
    def MountPointAssociates(self):
        return self._MountPointAssociates

    @MountPointAssociates.setter
    def MountPointAssociates(self, MountPointAssociates):
        self._MountPointAssociates = MountPointAssociates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountPointAssociates") is not None:
            self._MountPointAssociates = []
            for item in params.get("MountPointAssociates"):
                obj = MountPointAssociates()
                obj._deserialize(item)
                self._MountPointAssociates.append(obj)
        self._RequestId = params.get("RequestId")


class CreateDMSDatabaseRequest(AbstractModel):
    """CreateDMSDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Asset: 基础元数据对象
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param _SchemaName: Schema目录
        :type SchemaName: str
        :param _Location: Db存储路径
        :type Location: str
        :param _Name: 数据库名称
        :type Name: str
        """
        self._Asset = None
        self._SchemaName = None
        self._Location = None
        self._Name = None

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        if params.get("Asset") is not None:
            self._Asset = Asset()
            self._Asset._deserialize(params.get("Asset"))
        self._SchemaName = params.get("SchemaName")
        self._Location = params.get("Location")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDMSDatabaseResponse(AbstractModel):
    """CreateDMSDatabase返回参数结构体

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


class CreateDMSTableRequest(AbstractModel):
    """CreateDMSTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Asset: 基础对象
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param _Type: 表类型：EXTERNAL_TABLE, VIRTUAL_VIEW, MATERIALIZED_VIEW
        :type Type: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _StorageSize: 存储大小
        :type StorageSize: int
        :param _RecordCount: 记录数量
        :type RecordCount: int
        :param _LifeTime: 生命周期
        :type LifeTime: int
        :param _DataUpdateTime: 数据更新时间
        :type DataUpdateTime: str
        :param _StructUpdateTime: 结构更新时间
        :type StructUpdateTime: str
        :param _LastAccessTime: 最后访问时间
        :type LastAccessTime: str
        :param _Sds: 存储对象
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        :param _Columns: 列
        :type Columns: list of DMSColumn
        :param _PartitionKeys: 分区键值
        :type PartitionKeys: list of DMSColumn
        :param _ViewOriginalText: 视图文本
        :type ViewOriginalText: str
        :param _ViewExpandedText: 视图文本
        :type ViewExpandedText: str
        :param _Partitions: 分区
        :type Partitions: list of DMSPartition
        :param _Name: 表名称
        :type Name: str
        """
        self._Asset = None
        self._Type = None
        self._DbName = None
        self._StorageSize = None
        self._RecordCount = None
        self._LifeTime = None
        self._DataUpdateTime = None
        self._StructUpdateTime = None
        self._LastAccessTime = None
        self._Sds = None
        self._Columns = None
        self._PartitionKeys = None
        self._ViewOriginalText = None
        self._ViewExpandedText = None
        self._Partitions = None
        self._Name = None

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def StorageSize(self):
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def LifeTime(self):
        return self._LifeTime

    @LifeTime.setter
    def LifeTime(self, LifeTime):
        self._LifeTime = LifeTime

    @property
    def DataUpdateTime(self):
        return self._DataUpdateTime

    @DataUpdateTime.setter
    def DataUpdateTime(self, DataUpdateTime):
        self._DataUpdateTime = DataUpdateTime

    @property
    def StructUpdateTime(self):
        return self._StructUpdateTime

    @StructUpdateTime.setter
    def StructUpdateTime(self, StructUpdateTime):
        self._StructUpdateTime = StructUpdateTime

    @property
    def LastAccessTime(self):
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def Sds(self):
        return self._Sds

    @Sds.setter
    def Sds(self, Sds):
        self._Sds = Sds

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def PartitionKeys(self):
        return self._PartitionKeys

    @PartitionKeys.setter
    def PartitionKeys(self, PartitionKeys):
        self._PartitionKeys = PartitionKeys

    @property
    def ViewOriginalText(self):
        return self._ViewOriginalText

    @ViewOriginalText.setter
    def ViewOriginalText(self, ViewOriginalText):
        self._ViewOriginalText = ViewOriginalText

    @property
    def ViewExpandedText(self):
        return self._ViewExpandedText

    @ViewExpandedText.setter
    def ViewExpandedText(self, ViewExpandedText):
        self._ViewExpandedText = ViewExpandedText

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        if params.get("Asset") is not None:
            self._Asset = Asset()
            self._Asset._deserialize(params.get("Asset"))
        self._Type = params.get("Type")
        self._DbName = params.get("DbName")
        self._StorageSize = params.get("StorageSize")
        self._RecordCount = params.get("RecordCount")
        self._LifeTime = params.get("LifeTime")
        self._DataUpdateTime = params.get("DataUpdateTime")
        self._StructUpdateTime = params.get("StructUpdateTime")
        self._LastAccessTime = params.get("LastAccessTime")
        if params.get("Sds") is not None:
            self._Sds = DMSSds()
            self._Sds._deserialize(params.get("Sds"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("PartitionKeys") is not None:
            self._PartitionKeys = []
            for item in params.get("PartitionKeys"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._PartitionKeys.append(obj)
        self._ViewOriginalText = params.get("ViewOriginalText")
        self._ViewExpandedText = params.get("ViewExpandedText")
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDMSTableResponse(AbstractModel):
    """CreateDMSTable返回参数结构体

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


class CreateDataEngineRequest(AbstractModel):
    """CreateDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineType: 引擎类型spark/presto
        :type EngineType: str
        :param _DataEngineName: 虚拟集群名称
        :type DataEngineName: str
        :param _ClusterType: 集群类型 spark_private/presto_private/presto_cu/spark_cu
        :type ClusterType: str
        :param _Mode: 计费模式 0=共享模式 1=按量计费 2=包年包月
        :type Mode: int
        :param _AutoResume: 是否自动启动集群
        :type AutoResume: bool
        :param _MinClusters: 最小资源
        :type MinClusters: int
        :param _MaxClusters: 最大资源
        :type MaxClusters: int
        :param _DefaultDataEngine: 是否为默认虚拟集群
        :type DefaultDataEngine: bool
        :param _CidrBlock: VPC网段
        :type CidrBlock: str
        :param _Message: 描述信息
        :type Message: str
        :param _Size: 集群规模
        :type Size: int
        :param _PayMode: 计费类型，后付费：0，预付费：1。当前只支持后付费，不填默认为后付费。
        :type PayMode: int
        :param _TimeSpan: 资源使用时长，后付费：固定填3600，预付费：最少填1，代表购买资源一个月，最长不超过120。默认1
        :type TimeSpan: int
        :param _TimeUnit: 资源使用时长的单位，后付费：s，预付费：m。默认为s
        :type TimeUnit: str
        :param _AutoRenew: 资源的自动续费标志。后付费无需续费，固定填0；预付费下：0表示手动续费、1代表自动续费、2代表不续费，在0下如果是大客户，会自动帮大客户续费。默认为0
        :type AutoRenew: int
        :param _Tags: 创建资源的时候需要绑定的标签信息
        :type Tags: list of TagInfo
        :param _AutoSuspend: 是否自定挂起集群：false（默认）：不自动挂起、true：自动挂起
        :type AutoSuspend: bool
        :param _CrontabResumeSuspend: 定时启停集群策略：0（默认）：关闭定时策略、1：开启定时策略（注：定时启停策略与自动挂起策略互斥）
        :type CrontabResumeSuspend: int
        :param _CrontabResumeSuspendStrategy: 定时启停策略，复杂类型：包含启停时间、挂起集群策略
        :type CrontabResumeSuspendStrategy: :class:`tencentcloud.dlc.v20210125.models.CrontabResumeSuspendStrategy`
        :param _EngineExecType: 引擎执行任务类型，有效值：SQL/BATCH，默认为SQL
        :type EngineExecType: str
        :param _MaxConcurrency: 单个集群最大并发任务数，默认5
        :type MaxConcurrency: int
        :param _TolerableQueueTime: 可容忍的排队时间，默认0。当任务排队的时间超过可容忍的时间时可能会触发扩容。如果该参数为0，则表示一旦有任务排队就可能立即触发扩容。
        :type TolerableQueueTime: int
        :param _AutoSuspendTime: 集群自动挂起时间，默认10分钟
        :type AutoSuspendTime: int
        :param _ResourceType: 资源类型。Standard_CU：标准型；Memory_CU：内存型
        :type ResourceType: str
        :param _DataEngineConfigPairs: 集群高级配置
        :type DataEngineConfigPairs: list of DataEngineConfigPair
        :param _ImageVersionName: 集群镜像版本名字。如SuperSQL-P 1.1;SuperSQL-S 3.2等,不传，默认创建最新镜像版本的集群
        :type ImageVersionName: str
        :param _MainClusterName: 主集群名称，创建容灾集群时指定
        :type MainClusterName: str
        :param _ElasticSwitch: spark jar 包年包月集群是否开启弹性
        :type ElasticSwitch: bool
        :param _ElasticLimit: spark jar 包年包月集群弹性上限
        :type ElasticLimit: int
        :param _SessionResourceTemplate: spark作业集群session资源配置模板
        :type SessionResourceTemplate: :class:`tencentcloud.dlc.v20210125.models.SessionResourceTemplate`
        :param _AutoAuthorization: 自动授权
        :type AutoAuthorization: bool
        :param _EngineNetworkId: 引擎网络ID
        :type EngineNetworkId: str
        :param _EngineGeneration: 引擎世代，SuperSQL：代表supersql引擎，Native：代表标准引擎。默认值为SuperSQL
        :type EngineGeneration: str
        """
        self._EngineType = None
        self._DataEngineName = None
        self._ClusterType = None
        self._Mode = None
        self._AutoResume = None
        self._MinClusters = None
        self._MaxClusters = None
        self._DefaultDataEngine = None
        self._CidrBlock = None
        self._Message = None
        self._Size = None
        self._PayMode = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._AutoRenew = None
        self._Tags = None
        self._AutoSuspend = None
        self._CrontabResumeSuspend = None
        self._CrontabResumeSuspendStrategy = None
        self._EngineExecType = None
        self._MaxConcurrency = None
        self._TolerableQueueTime = None
        self._AutoSuspendTime = None
        self._ResourceType = None
        self._DataEngineConfigPairs = None
        self._ImageVersionName = None
        self._MainClusterName = None
        self._ElasticSwitch = None
        self._ElasticLimit = None
        self._SessionResourceTemplate = None
        self._AutoAuthorization = None
        self._EngineNetworkId = None
        self._EngineGeneration = None

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def AutoResume(self):
        return self._AutoResume

    @AutoResume.setter
    def AutoResume(self, AutoResume):
        self._AutoResume = AutoResume

    @property
    def MinClusters(self):
        return self._MinClusters

    @MinClusters.setter
    def MinClusters(self, MinClusters):
        self._MinClusters = MinClusters

    @property
    def MaxClusters(self):
        return self._MaxClusters

    @MaxClusters.setter
    def MaxClusters(self, MaxClusters):
        self._MaxClusters = MaxClusters

    @property
    def DefaultDataEngine(self):
        warnings.warn("parameter `DefaultDataEngine` is deprecated", DeprecationWarning) 

        return self._DefaultDataEngine

    @DefaultDataEngine.setter
    def DefaultDataEngine(self, DefaultDataEngine):
        warnings.warn("parameter `DefaultDataEngine` is deprecated", DeprecationWarning) 

        self._DefaultDataEngine = DefaultDataEngine

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoSuspend(self):
        return self._AutoSuspend

    @AutoSuspend.setter
    def AutoSuspend(self, AutoSuspend):
        self._AutoSuspend = AutoSuspend

    @property
    def CrontabResumeSuspend(self):
        return self._CrontabResumeSuspend

    @CrontabResumeSuspend.setter
    def CrontabResumeSuspend(self, CrontabResumeSuspend):
        self._CrontabResumeSuspend = CrontabResumeSuspend

    @property
    def CrontabResumeSuspendStrategy(self):
        return self._CrontabResumeSuspendStrategy

    @CrontabResumeSuspendStrategy.setter
    def CrontabResumeSuspendStrategy(self, CrontabResumeSuspendStrategy):
        self._CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy

    @property
    def EngineExecType(self):
        return self._EngineExecType

    @EngineExecType.setter
    def EngineExecType(self, EngineExecType):
        self._EngineExecType = EngineExecType

    @property
    def MaxConcurrency(self):
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def TolerableQueueTime(self):
        return self._TolerableQueueTime

    @TolerableQueueTime.setter
    def TolerableQueueTime(self, TolerableQueueTime):
        self._TolerableQueueTime = TolerableQueueTime

    @property
    def AutoSuspendTime(self):
        return self._AutoSuspendTime

    @AutoSuspendTime.setter
    def AutoSuspendTime(self, AutoSuspendTime):
        self._AutoSuspendTime = AutoSuspendTime

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def DataEngineConfigPairs(self):
        return self._DataEngineConfigPairs

    @DataEngineConfigPairs.setter
    def DataEngineConfigPairs(self, DataEngineConfigPairs):
        self._DataEngineConfigPairs = DataEngineConfigPairs

    @property
    def ImageVersionName(self):
        return self._ImageVersionName

    @ImageVersionName.setter
    def ImageVersionName(self, ImageVersionName):
        self._ImageVersionName = ImageVersionName

    @property
    def MainClusterName(self):
        return self._MainClusterName

    @MainClusterName.setter
    def MainClusterName(self, MainClusterName):
        self._MainClusterName = MainClusterName

    @property
    def ElasticSwitch(self):
        return self._ElasticSwitch

    @ElasticSwitch.setter
    def ElasticSwitch(self, ElasticSwitch):
        self._ElasticSwitch = ElasticSwitch

    @property
    def ElasticLimit(self):
        return self._ElasticLimit

    @ElasticLimit.setter
    def ElasticLimit(self, ElasticLimit):
        self._ElasticLimit = ElasticLimit

    @property
    def SessionResourceTemplate(self):
        return self._SessionResourceTemplate

    @SessionResourceTemplate.setter
    def SessionResourceTemplate(self, SessionResourceTemplate):
        self._SessionResourceTemplate = SessionResourceTemplate

    @property
    def AutoAuthorization(self):
        return self._AutoAuthorization

    @AutoAuthorization.setter
    def AutoAuthorization(self, AutoAuthorization):
        self._AutoAuthorization = AutoAuthorization

    @property
    def EngineNetworkId(self):
        return self._EngineNetworkId

    @EngineNetworkId.setter
    def EngineNetworkId(self, EngineNetworkId):
        self._EngineNetworkId = EngineNetworkId

    @property
    def EngineGeneration(self):
        return self._EngineGeneration

    @EngineGeneration.setter
    def EngineGeneration(self, EngineGeneration):
        self._EngineGeneration = EngineGeneration


    def _deserialize(self, params):
        self._EngineType = params.get("EngineType")
        self._DataEngineName = params.get("DataEngineName")
        self._ClusterType = params.get("ClusterType")
        self._Mode = params.get("Mode")
        self._AutoResume = params.get("AutoResume")
        self._MinClusters = params.get("MinClusters")
        self._MaxClusters = params.get("MaxClusters")
        self._DefaultDataEngine = params.get("DefaultDataEngine")
        self._CidrBlock = params.get("CidrBlock")
        self._Message = params.get("Message")
        self._Size = params.get("Size")
        self._PayMode = params.get("PayMode")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._AutoRenew = params.get("AutoRenew")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoSuspend = params.get("AutoSuspend")
        self._CrontabResumeSuspend = params.get("CrontabResumeSuspend")
        if params.get("CrontabResumeSuspendStrategy") is not None:
            self._CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy()
            self._CrontabResumeSuspendStrategy._deserialize(params.get("CrontabResumeSuspendStrategy"))
        self._EngineExecType = params.get("EngineExecType")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._TolerableQueueTime = params.get("TolerableQueueTime")
        self._AutoSuspendTime = params.get("AutoSuspendTime")
        self._ResourceType = params.get("ResourceType")
        if params.get("DataEngineConfigPairs") is not None:
            self._DataEngineConfigPairs = []
            for item in params.get("DataEngineConfigPairs"):
                obj = DataEngineConfigPair()
                obj._deserialize(item)
                self._DataEngineConfigPairs.append(obj)
        self._ImageVersionName = params.get("ImageVersionName")
        self._MainClusterName = params.get("MainClusterName")
        self._ElasticSwitch = params.get("ElasticSwitch")
        self._ElasticLimit = params.get("ElasticLimit")
        if params.get("SessionResourceTemplate") is not None:
            self._SessionResourceTemplate = SessionResourceTemplate()
            self._SessionResourceTemplate._deserialize(params.get("SessionResourceTemplate"))
        self._AutoAuthorization = params.get("AutoAuthorization")
        self._EngineNetworkId = params.get("EngineNetworkId")
        self._EngineGeneration = params.get("EngineGeneration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataEngineResponse(AbstractModel):
    """CreateDataEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 虚拟引擎id
        :type DataEngineId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataEngineId = None
        self._RequestId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        self._RequestId = params.get("RequestId")


class CreateDatabaseRequest(AbstractModel):
    """CreateDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseInfo: 数据库基础信息
        :type DatabaseInfo: :class:`tencentcloud.dlc.v20210125.models.DatabaseInfo`
        :param _DatasourceConnectionName: 数据源名称，默认为DataLakeCatalog
        :type DatasourceConnectionName: str
        """
        self._DatabaseInfo = None
        self._DatasourceConnectionName = None

    @property
    def DatabaseInfo(self):
        return self._DatabaseInfo

    @DatabaseInfo.setter
    def DatabaseInfo(self, DatabaseInfo):
        self._DatabaseInfo = DatabaseInfo

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName


    def _deserialize(self, params):
        if params.get("DatabaseInfo") is not None:
            self._DatabaseInfo = DatabaseInfo()
            self._DatabaseInfo._deserialize(params.get("DatabaseInfo"))
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatabaseResponse(AbstractModel):
    """CreateDatabase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Execution: 生成的建库执行语句对象。
        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Execution = None
        self._RequestId = None

    @property
    def Execution(self):
        return self._Execution

    @Execution.setter
    def Execution(self, Execution):
        self._Execution = Execution

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Execution") is not None:
            self._Execution = Execution()
            self._Execution._deserialize(params.get("Execution"))
        self._RequestId = params.get("RequestId")


class CreateExportTaskRequest(AbstractModel):
    """CreateExportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InputType: 数据来源，lakefsStorage、taskResult
        :type InputType: str
        :param _InputConf: 导出任务输入配置
        :type InputConf: list of KVPair
        :param _OutputConf: 导出任务输出配置
        :type OutputConf: list of KVPair
        :param _OutputType: 目标数据源的类型，目前支持导出到cos
        :type OutputType: str
        """
        self._InputType = None
        self._InputConf = None
        self._OutputConf = None
        self._OutputType = None

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def InputConf(self):
        return self._InputConf

    @InputConf.setter
    def InputConf(self, InputConf):
        self._InputConf = InputConf

    @property
    def OutputConf(self):
        return self._OutputConf

    @OutputConf.setter
    def OutputConf(self, OutputConf):
        self._OutputConf = OutputConf

    @property
    def OutputType(self):
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType


    def _deserialize(self, params):
        self._InputType = params.get("InputType")
        if params.get("InputConf") is not None:
            self._InputConf = []
            for item in params.get("InputConf"):
                obj = KVPair()
                obj._deserialize(item)
                self._InputConf.append(obj)
        if params.get("OutputConf") is not None:
            self._OutputConf = []
            for item in params.get("OutputConf"):
                obj = KVPair()
                obj._deserialize(item)
                self._OutputConf.append(obj)
        self._OutputType = params.get("OutputType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExportTaskResponse(AbstractModel):
    """CreateExportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateImportTaskRequest(AbstractModel):
    """CreateImportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InputType: 数据来源，cos
        :type InputType: str
        :param _InputConf: 输入配置
        :type InputConf: list of KVPair
        :param _OutputConf: 输出配置
        :type OutputConf: list of KVPair
        :param _OutputType: 目标数据源的类型，目前支持导入到托管存储，即lakefsStorage
        :type OutputType: str
        """
        self._InputType = None
        self._InputConf = None
        self._OutputConf = None
        self._OutputType = None

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def InputConf(self):
        return self._InputConf

    @InputConf.setter
    def InputConf(self, InputConf):
        self._InputConf = InputConf

    @property
    def OutputConf(self):
        return self._OutputConf

    @OutputConf.setter
    def OutputConf(self, OutputConf):
        self._OutputConf = OutputConf

    @property
    def OutputType(self):
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType


    def _deserialize(self, params):
        self._InputType = params.get("InputType")
        if params.get("InputConf") is not None:
            self._InputConf = []
            for item in params.get("InputConf"):
                obj = KVPair()
                obj._deserialize(item)
                self._InputConf.append(obj)
        if params.get("OutputConf") is not None:
            self._OutputConf = []
            for item in params.get("OutputConf"):
                obj = KVPair()
                obj._deserialize(item)
                self._OutputConf.append(obj)
        self._OutputType = params.get("OutputType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImportTaskResponse(AbstractModel):
    """CreateImportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateInternalTableRequest(AbstractModel):
    """CreateInternalTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableBaseInfo: 表基本信息
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param _Columns: 表字段信息
        :type Columns: list of TColumn
        :param _Partitions: 表分区信息
        :type Partitions: list of TPartition
        :param _Properties: 表属性信息
        :type Properties: list of Property
        """
        self._TableBaseInfo = None
        self._Columns = None
        self._Partitions = None
        self._Properties = None

    @property
    def TableBaseInfo(self):
        return self._TableBaseInfo

    @TableBaseInfo.setter
    def TableBaseInfo(self, TableBaseInfo):
        self._TableBaseInfo = TableBaseInfo

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self._TableBaseInfo = TableBaseInfo()
            self._TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = TColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = TPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInternalTableResponse(AbstractModel):
    """CreateInternalTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Execution: 创建托管存储内表sql语句描述
        :type Execution: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Execution = None
        self._RequestId = None

    @property
    def Execution(self):
        return self._Execution

    @Execution.setter
    def Execution(self, Execution):
        self._Execution = Execution

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Execution = params.get("Execution")
        self._RequestId = params.get("RequestId")


class CreateNotebookSessionRequest(AbstractModel):
    """CreateNotebookSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: Session名称
        :type Name: str
        :param _Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        :param _DataEngineName: DLC Spark作业引擎名称
        :type DataEngineName: str
        :param _ProgramDependentFiles: session文件地址，当前支持：cosn://和lakefs://两种路径
        :type ProgramDependentFiles: list of str
        :param _ProgramDependentJars: 依赖的jar程序地址，当前支持：cosn://和lakefs://两种路径
        :type ProgramDependentJars: list of str
        :param _ProgramDependentPython: 依赖的python程序地址，当前支持：cosn://和lakefs://两种路径
        :type ProgramDependentPython: list of str
        :param _ProgramArchives: 依赖的pyspark虚拟环境地址，当前支持：cosn://和lakefs://两种路径
        :type ProgramArchives: list of str
        :param _DriverSize: 指定的Driver规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type DriverSize: str
        :param _ExecutorSize: 指定的Executor规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type ExecutorSize: str
        :param _ExecutorNumbers: 指定的Executor数量，默认为1
        :type ExecutorNumbers: int
        :param _Arguments: Session相关配置，当前支持：
1. dlc.eni: 用户配置的eni网关信息，可以通过该字段设置；
2. dlc.role.arn: 用户配置的roleArn鉴权策略配置信息，可以通过该字段设置；
3. dlc.sql.set.config: 用户配置的集群配置信息，可以通过该字段设置；
        :type Arguments: list of KVPair
        :param _ProxyUser: 代理用户，默认为root
        :type ProxyUser: str
        :param _TimeoutInSecond: 指定的Session超时时间，单位秒，默认3600秒
        :type TimeoutInSecond: int
        :param _ExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于ExecutorNumbers
        :type ExecutorMaxNumbers: int
        :param _SparkImage: 指定spark版本名称，当前任务使用该spark镜像运行
        :type SparkImage: str
        :param _IsInherit: 是否继承集群的资源类配置：0：自定义（默认），1：继承集群；
        :type IsInherit: int
        """
        self._Name = None
        self._Kind = None
        self._DataEngineName = None
        self._ProgramDependentFiles = None
        self._ProgramDependentJars = None
        self._ProgramDependentPython = None
        self._ProgramArchives = None
        self._DriverSize = None
        self._ExecutorSize = None
        self._ExecutorNumbers = None
        self._Arguments = None
        self._ProxyUser = None
        self._TimeoutInSecond = None
        self._ExecutorMaxNumbers = None
        self._SparkImage = None
        self._IsInherit = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ProgramDependentFiles(self):
        return self._ProgramDependentFiles

    @ProgramDependentFiles.setter
    def ProgramDependentFiles(self, ProgramDependentFiles):
        self._ProgramDependentFiles = ProgramDependentFiles

    @property
    def ProgramDependentJars(self):
        return self._ProgramDependentJars

    @ProgramDependentJars.setter
    def ProgramDependentJars(self, ProgramDependentJars):
        self._ProgramDependentJars = ProgramDependentJars

    @property
    def ProgramDependentPython(self):
        return self._ProgramDependentPython

    @ProgramDependentPython.setter
    def ProgramDependentPython(self, ProgramDependentPython):
        self._ProgramDependentPython = ProgramDependentPython

    @property
    def ProgramArchives(self):
        return self._ProgramArchives

    @ProgramArchives.setter
    def ProgramArchives(self, ProgramArchives):
        self._ProgramArchives = ProgramArchives

    @property
    def DriverSize(self):
        return self._DriverSize

    @DriverSize.setter
    def DriverSize(self, DriverSize):
        self._DriverSize = DriverSize

    @property
    def ExecutorSize(self):
        return self._ExecutorSize

    @ExecutorSize.setter
    def ExecutorSize(self, ExecutorSize):
        self._ExecutorSize = ExecutorSize

    @property
    def ExecutorNumbers(self):
        return self._ExecutorNumbers

    @ExecutorNumbers.setter
    def ExecutorNumbers(self, ExecutorNumbers):
        self._ExecutorNumbers = ExecutorNumbers

    @property
    def Arguments(self):
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def ProxyUser(self):
        return self._ProxyUser

    @ProxyUser.setter
    def ProxyUser(self, ProxyUser):
        self._ProxyUser = ProxyUser

    @property
    def TimeoutInSecond(self):
        return self._TimeoutInSecond

    @TimeoutInSecond.setter
    def TimeoutInSecond(self, TimeoutInSecond):
        self._TimeoutInSecond = TimeoutInSecond

    @property
    def ExecutorMaxNumbers(self):
        return self._ExecutorMaxNumbers

    @ExecutorMaxNumbers.setter
    def ExecutorMaxNumbers(self, ExecutorMaxNumbers):
        self._ExecutorMaxNumbers = ExecutorMaxNumbers

    @property
    def SparkImage(self):
        return self._SparkImage

    @SparkImage.setter
    def SparkImage(self, SparkImage):
        self._SparkImage = SparkImage

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Kind = params.get("Kind")
        self._DataEngineName = params.get("DataEngineName")
        self._ProgramDependentFiles = params.get("ProgramDependentFiles")
        self._ProgramDependentJars = params.get("ProgramDependentJars")
        self._ProgramDependentPython = params.get("ProgramDependentPython")
        self._ProgramArchives = params.get("ProgramArchives")
        self._DriverSize = params.get("DriverSize")
        self._ExecutorSize = params.get("ExecutorSize")
        self._ExecutorNumbers = params.get("ExecutorNumbers")
        if params.get("Arguments") is not None:
            self._Arguments = []
            for item in params.get("Arguments"):
                obj = KVPair()
                obj._deserialize(item)
                self._Arguments.append(obj)
        self._ProxyUser = params.get("ProxyUser")
        self._TimeoutInSecond = params.get("TimeoutInSecond")
        self._ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        self._SparkImage = params.get("SparkImage")
        self._IsInherit = params.get("IsInherit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookSessionResponse(AbstractModel):
    """CreateNotebookSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _SparkAppId: Spark任务返回的AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppId: str
        :param _State: Session状态，包含：not_started（未启动）、starting（已启动）、idle（等待输入）、busy(正在运行statement)、shutting_down（停止）、error（异常）、dead（已退出）、killed（被杀死）、success（正常停止）
        :type State: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._SparkAppId = None
        self._State = None
        self._RequestId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._SparkAppId = params.get("SparkAppId")
        self._State = params.get("State")
        self._RequestId = params.get("RequestId")


class CreateNotebookSessionStatementRequest(AbstractModel):
    """CreateNotebookSessionStatement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _Code: 执行的代码
        :type Code: str
        :param _Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        """
        self._SessionId = None
        self._Code = None
        self._Kind = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Code = params.get("Code")
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookSessionStatementResponse(AbstractModel):
    """CreateNotebookSessionStatement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookSessionStatement: Session Statement详情
        :type NotebookSessionStatement: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionStatementInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookSessionStatement = None
        self._RequestId = None

    @property
    def NotebookSessionStatement(self):
        return self._NotebookSessionStatement

    @NotebookSessionStatement.setter
    def NotebookSessionStatement(self, NotebookSessionStatement):
        self._NotebookSessionStatement = NotebookSessionStatement

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotebookSessionStatement") is not None:
            self._NotebookSessionStatement = NotebookSessionStatementInfo()
            self._NotebookSessionStatement._deserialize(params.get("NotebookSessionStatement"))
        self._RequestId = params.get("RequestId")


class CreateNotebookSessionStatementSupportBatchSQLRequest(AbstractModel):
    """CreateNotebookSessionStatementSupportBatchSQL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _Code: 执行的代码
        :type Code: str
        :param _Kind: 类型，当前支持：sql
        :type Kind: str
        :param _SaveResult: 是否保存运行结果
        :type SaveResult: bool
        """
        self._SessionId = None
        self._Code = None
        self._Kind = None
        self._SaveResult = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def SaveResult(self):
        return self._SaveResult

    @SaveResult.setter
    def SaveResult(self, SaveResult):
        self._SaveResult = SaveResult


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Code = params.get("Code")
        self._Kind = params.get("Kind")
        self._SaveResult = params.get("SaveResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookSessionStatementSupportBatchSQLResponse(AbstractModel):
    """CreateNotebookSessionStatementSupportBatchSQL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookSessionStatementBatches: Session Statement详情
        :type NotebookSessionStatementBatches: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionStatementBatchInformation`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookSessionStatementBatches = None
        self._RequestId = None

    @property
    def NotebookSessionStatementBatches(self):
        return self._NotebookSessionStatementBatches

    @NotebookSessionStatementBatches.setter
    def NotebookSessionStatementBatches(self, NotebookSessionStatementBatches):
        self._NotebookSessionStatementBatches = NotebookSessionStatementBatches

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotebookSessionStatementBatches") is not None:
            self._NotebookSessionStatementBatches = NotebookSessionStatementBatchInformation()
            self._NotebookSessionStatementBatches._deserialize(params.get("NotebookSessionStatementBatches"))
        self._RequestId = params.get("RequestId")


class CreateResultDownloadRequest(AbstractModel):
    """CreateResultDownload请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 查询结果任务Id
        :type TaskId: str
        :param _Format: 下载格式
        :type Format: str
        :param _Force: 是否重新生成下载文件，仅当之前任务为 Timout | Error 时有效
        :type Force: bool
        """
        self._TaskId = None
        self._Format = None
        self._Force = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Format = params.get("Format")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResultDownloadResponse(AbstractModel):
    """CreateResultDownload返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadId: 下载任务Id
        :type DownloadId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadId = None
        self._RequestId = None

    @property
    def DownloadId(self):
        return self._DownloadId

    @DownloadId.setter
    def DownloadId(self, DownloadId):
        self._DownloadId = DownloadId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadId = params.get("DownloadId")
        self._RequestId = params.get("RequestId")


class CreateScriptRequest(AbstractModel):
    """CreateScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScriptName: 脚本名称，最大不能超过255个字符。
        :type ScriptName: str
        :param _SQLStatement: base64编码后的sql语句
        :type SQLStatement: str
        :param _ScriptDesc: 脚本描述， 不能超过50个字符
        :type ScriptDesc: str
        :param _DatabaseName: 数据库名称
        :type DatabaseName: str
        """
        self._ScriptName = None
        self._SQLStatement = None
        self._ScriptDesc = None
        self._DatabaseName = None

    @property
    def ScriptName(self):
        return self._ScriptName

    @ScriptName.setter
    def ScriptName(self, ScriptName):
        self._ScriptName = ScriptName

    @property
    def SQLStatement(self):
        return self._SQLStatement

    @SQLStatement.setter
    def SQLStatement(self, SQLStatement):
        self._SQLStatement = SQLStatement

    @property
    def ScriptDesc(self):
        return self._ScriptDesc

    @ScriptDesc.setter
    def ScriptDesc(self, ScriptDesc):
        self._ScriptDesc = ScriptDesc

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName


    def _deserialize(self, params):
        self._ScriptName = params.get("ScriptName")
        self._SQLStatement = params.get("SQLStatement")
        self._ScriptDesc = params.get("ScriptDesc")
        self._DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScriptResponse(AbstractModel):
    """CreateScript返回参数结构体

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


class CreateSparkAppRequest(AbstractModel):
    """CreateSparkApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: spark作业名
        :type AppName: str
        :param _AppType: spark作业类型，1代表spark jar作业，2代表spark streaming作业
        :type AppType: int
        :param _DataEngine: 执行spark作业的数据引擎名称
        :type DataEngine: str
        :param _AppFile: spark作业程序包文件路径
        :type AppFile: str
        :param _RoleArn: 数据访问策略，CAM Role arn，控制台通过数据作业—>作业配置获取，SDK通过DescribeUserRoles接口获取对应的值；
        :type RoleArn: int
        :param _AppDriverSize: 指定的Driver规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type AppDriverSize: str
        :param _AppExecutorSize: 指定的Executor规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type AppExecutorSize: str
        :param _AppExecutorNums: spark作业executor个数
        :type AppExecutorNums: int
        :param _Eni: 该字段已下线，请使用字段Datasource
        :type Eni: str
        :param _IsLocal: spark作业程序包是否本地上传，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocal: str
        :param _MainClass: spark作业主类
        :type MainClass: str
        :param _AppConf: spark配置，以换行符分隔
        :type AppConf: str
        :param _IsLocalJars: spark 作业依赖jar包是否本地上传，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocalJars: str
        :param _AppJars: spark 作业依赖jar包（--jars），以逗号分隔
        :type AppJars: str
        :param _IsLocalFiles: spark作业依赖文件资源是否本地上传，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocalFiles: str
        :param _AppFiles: spark作业依赖文件资源（--files）（非jar、zip），以逗号分隔
        :type AppFiles: str
        :param _CmdArgs: spark作业程序入参，空格分割
        :type CmdArgs: str
        :param _MaxRetries: 最大重试次数，只对spark流任务生效
        :type MaxRetries: int
        :param _DataSource: 数据源名称
        :type DataSource: str
        :param _IsLocalPythonFiles: pyspark：依赖上传方式，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocalPythonFiles: str
        :param _AppPythonFiles: pyspark作业依赖python资源（--py-files），支持py/zip/egg等归档格式，多文件以逗号分隔
        :type AppPythonFiles: str
        :param _IsLocalArchives: spark作业依赖archives资源是否本地上传，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocalArchives: str
        :param _AppArchives: spark作业依赖archives资源（--archives），支持tar.gz/tgz/tar等归档格式，以逗号分隔
        :type AppArchives: str
        :param _SparkImage: Spark Image 版本号
        :type SparkImage: str
        :param _SparkImageVersion: Spark Image 版本名称
        :type SparkImageVersion: str
        :param _AppExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于AppExecutorNums
        :type AppExecutorMaxNumbers: int
        :param _SessionId: 关联dlc查询脚本id
        :type SessionId: str
        :param _IsInherit: 任务资源配置是否继承集群模板，0（默认）不继承，1：继承
        :type IsInherit: int
        :param _IsSessionStarted: 是否使用session脚本的sql运行任务：false：否，true：是
        :type IsSessionStarted: bool
        """
        self._AppName = None
        self._AppType = None
        self._DataEngine = None
        self._AppFile = None
        self._RoleArn = None
        self._AppDriverSize = None
        self._AppExecutorSize = None
        self._AppExecutorNums = None
        self._Eni = None
        self._IsLocal = None
        self._MainClass = None
        self._AppConf = None
        self._IsLocalJars = None
        self._AppJars = None
        self._IsLocalFiles = None
        self._AppFiles = None
        self._CmdArgs = None
        self._MaxRetries = None
        self._DataSource = None
        self._IsLocalPythonFiles = None
        self._AppPythonFiles = None
        self._IsLocalArchives = None
        self._AppArchives = None
        self._SparkImage = None
        self._SparkImageVersion = None
        self._AppExecutorMaxNumbers = None
        self._SessionId = None
        self._IsInherit = None
        self._IsSessionStarted = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def AppFile(self):
        return self._AppFile

    @AppFile.setter
    def AppFile(self, AppFile):
        self._AppFile = AppFile

    @property
    def RoleArn(self):
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def AppDriverSize(self):
        return self._AppDriverSize

    @AppDriverSize.setter
    def AppDriverSize(self, AppDriverSize):
        self._AppDriverSize = AppDriverSize

    @property
    def AppExecutorSize(self):
        return self._AppExecutorSize

    @AppExecutorSize.setter
    def AppExecutorSize(self, AppExecutorSize):
        self._AppExecutorSize = AppExecutorSize

    @property
    def AppExecutorNums(self):
        return self._AppExecutorNums

    @AppExecutorNums.setter
    def AppExecutorNums(self, AppExecutorNums):
        self._AppExecutorNums = AppExecutorNums

    @property
    def Eni(self):
        return self._Eni

    @Eni.setter
    def Eni(self, Eni):
        self._Eni = Eni

    @property
    def IsLocal(self):
        return self._IsLocal

    @IsLocal.setter
    def IsLocal(self, IsLocal):
        self._IsLocal = IsLocal

    @property
    def MainClass(self):
        return self._MainClass

    @MainClass.setter
    def MainClass(self, MainClass):
        self._MainClass = MainClass

    @property
    def AppConf(self):
        return self._AppConf

    @AppConf.setter
    def AppConf(self, AppConf):
        self._AppConf = AppConf

    @property
    def IsLocalJars(self):
        return self._IsLocalJars

    @IsLocalJars.setter
    def IsLocalJars(self, IsLocalJars):
        self._IsLocalJars = IsLocalJars

    @property
    def AppJars(self):
        return self._AppJars

    @AppJars.setter
    def AppJars(self, AppJars):
        self._AppJars = AppJars

    @property
    def IsLocalFiles(self):
        return self._IsLocalFiles

    @IsLocalFiles.setter
    def IsLocalFiles(self, IsLocalFiles):
        self._IsLocalFiles = IsLocalFiles

    @property
    def AppFiles(self):
        return self._AppFiles

    @AppFiles.setter
    def AppFiles(self, AppFiles):
        self._AppFiles = AppFiles

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs

    @property
    def MaxRetries(self):
        return self._MaxRetries

    @MaxRetries.setter
    def MaxRetries(self, MaxRetries):
        self._MaxRetries = MaxRetries

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def IsLocalPythonFiles(self):
        return self._IsLocalPythonFiles

    @IsLocalPythonFiles.setter
    def IsLocalPythonFiles(self, IsLocalPythonFiles):
        self._IsLocalPythonFiles = IsLocalPythonFiles

    @property
    def AppPythonFiles(self):
        return self._AppPythonFiles

    @AppPythonFiles.setter
    def AppPythonFiles(self, AppPythonFiles):
        self._AppPythonFiles = AppPythonFiles

    @property
    def IsLocalArchives(self):
        return self._IsLocalArchives

    @IsLocalArchives.setter
    def IsLocalArchives(self, IsLocalArchives):
        self._IsLocalArchives = IsLocalArchives

    @property
    def AppArchives(self):
        return self._AppArchives

    @AppArchives.setter
    def AppArchives(self, AppArchives):
        self._AppArchives = AppArchives

    @property
    def SparkImage(self):
        return self._SparkImage

    @SparkImage.setter
    def SparkImage(self, SparkImage):
        self._SparkImage = SparkImage

    @property
    def SparkImageVersion(self):
        return self._SparkImageVersion

    @SparkImageVersion.setter
    def SparkImageVersion(self, SparkImageVersion):
        self._SparkImageVersion = SparkImageVersion

    @property
    def AppExecutorMaxNumbers(self):
        return self._AppExecutorMaxNumbers

    @AppExecutorMaxNumbers.setter
    def AppExecutorMaxNumbers(self, AppExecutorMaxNumbers):
        self._AppExecutorMaxNumbers = AppExecutorMaxNumbers

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit

    @property
    def IsSessionStarted(self):
        return self._IsSessionStarted

    @IsSessionStarted.setter
    def IsSessionStarted(self, IsSessionStarted):
        self._IsSessionStarted = IsSessionStarted


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._AppType = params.get("AppType")
        self._DataEngine = params.get("DataEngine")
        self._AppFile = params.get("AppFile")
        self._RoleArn = params.get("RoleArn")
        self._AppDriverSize = params.get("AppDriverSize")
        self._AppExecutorSize = params.get("AppExecutorSize")
        self._AppExecutorNums = params.get("AppExecutorNums")
        self._Eni = params.get("Eni")
        self._IsLocal = params.get("IsLocal")
        self._MainClass = params.get("MainClass")
        self._AppConf = params.get("AppConf")
        self._IsLocalJars = params.get("IsLocalJars")
        self._AppJars = params.get("AppJars")
        self._IsLocalFiles = params.get("IsLocalFiles")
        self._AppFiles = params.get("AppFiles")
        self._CmdArgs = params.get("CmdArgs")
        self._MaxRetries = params.get("MaxRetries")
        self._DataSource = params.get("DataSource")
        self._IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self._AppPythonFiles = params.get("AppPythonFiles")
        self._IsLocalArchives = params.get("IsLocalArchives")
        self._AppArchives = params.get("AppArchives")
        self._SparkImage = params.get("SparkImage")
        self._SparkImageVersion = params.get("SparkImageVersion")
        self._AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        self._SessionId = params.get("SessionId")
        self._IsInherit = params.get("IsInherit")
        self._IsSessionStarted = params.get("IsSessionStarted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkAppResponse(AbstractModel):
    """CreateSparkApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SparkAppId: App唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SparkAppId = None
        self._RequestId = None

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SparkAppId = params.get("SparkAppId")
        self._RequestId = params.get("RequestId")


class CreateSparkAppTaskRequest(AbstractModel):
    """CreateSparkAppTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobName: spark作业名
        :type JobName: str
        :param _CmdArgs: spark作业程序入参，以空格分隔；一般用于周期性调用使用
        :type CmdArgs: str
        """
        self._JobName = None
        self._CmdArgs = None

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs


    def _deserialize(self, params):
        self._JobName = params.get("JobName")
        self._CmdArgs = params.get("CmdArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkAppTaskResponse(AbstractModel):
    """CreateSparkAppTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批Id
        :type BatchId: str
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

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
        self._BatchId = params.get("BatchId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateSparkSessionBatchSQLRequest(AbstractModel):
    """CreateSparkSessionBatchSQL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: DLC Spark作业引擎名称
        :type DataEngineName: str
        :param _ExecuteSQL: 运行sql，需要base64编码。
        :type ExecuteSQL: str
        :param _DriverSize: 指定的Driver规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type DriverSize: str
        :param _ExecutorSize: 指定的Executor规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type ExecutorSize: str
        :param _ExecutorNumbers: 指定的Executor数量，默认为1
        :type ExecutorNumbers: int
        :param _ExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于ExecutorNumbers
        :type ExecutorMaxNumbers: int
        :param _TimeoutInSecond: 指定的Session超时时间，单位秒，默认3600秒
        :type TimeoutInSecond: int
        :param _SessionId: Session唯一标识，当指定sessionid，则使用该session运行任务。
        :type SessionId: str
        :param _SessionName: 指定要创建的session名称
        :type SessionName: str
        :param _Arguments: Session相关配置，当前支持：1.dlc.eni：用户配置的eni网关信息，可以用过该字段设置；
2.dlc.role.arn：用户配置的roleArn鉴权策略配置信息，可以用过该字段设置；
3.dlc.sql.set.config：用户配置的集群配置信息，可以用过该字段设置；
        :type Arguments: list of KVPair
        :param _IsInherit: 是否继承集群的资源类配置：0：不继承（默认），1：继承集群；
        :type IsInherit: int
        :param _CustomKey: 用户自定义主键，需唯一
        :type CustomKey: str
        """
        self._DataEngineName = None
        self._ExecuteSQL = None
        self._DriverSize = None
        self._ExecutorSize = None
        self._ExecutorNumbers = None
        self._ExecutorMaxNumbers = None
        self._TimeoutInSecond = None
        self._SessionId = None
        self._SessionName = None
        self._Arguments = None
        self._IsInherit = None
        self._CustomKey = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ExecuteSQL(self):
        return self._ExecuteSQL

    @ExecuteSQL.setter
    def ExecuteSQL(self, ExecuteSQL):
        self._ExecuteSQL = ExecuteSQL

    @property
    def DriverSize(self):
        return self._DriverSize

    @DriverSize.setter
    def DriverSize(self, DriverSize):
        self._DriverSize = DriverSize

    @property
    def ExecutorSize(self):
        return self._ExecutorSize

    @ExecutorSize.setter
    def ExecutorSize(self, ExecutorSize):
        self._ExecutorSize = ExecutorSize

    @property
    def ExecutorNumbers(self):
        return self._ExecutorNumbers

    @ExecutorNumbers.setter
    def ExecutorNumbers(self, ExecutorNumbers):
        self._ExecutorNumbers = ExecutorNumbers

    @property
    def ExecutorMaxNumbers(self):
        return self._ExecutorMaxNumbers

    @ExecutorMaxNumbers.setter
    def ExecutorMaxNumbers(self, ExecutorMaxNumbers):
        self._ExecutorMaxNumbers = ExecutorMaxNumbers

    @property
    def TimeoutInSecond(self):
        return self._TimeoutInSecond

    @TimeoutInSecond.setter
    def TimeoutInSecond(self, TimeoutInSecond):
        self._TimeoutInSecond = TimeoutInSecond

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SessionName(self):
        return self._SessionName

    @SessionName.setter
    def SessionName(self, SessionName):
        self._SessionName = SessionName

    @property
    def Arguments(self):
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit

    @property
    def CustomKey(self):
        return self._CustomKey

    @CustomKey.setter
    def CustomKey(self, CustomKey):
        self._CustomKey = CustomKey


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._ExecuteSQL = params.get("ExecuteSQL")
        self._DriverSize = params.get("DriverSize")
        self._ExecutorSize = params.get("ExecutorSize")
        self._ExecutorNumbers = params.get("ExecutorNumbers")
        self._ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        self._TimeoutInSecond = params.get("TimeoutInSecond")
        self._SessionId = params.get("SessionId")
        self._SessionName = params.get("SessionName")
        if params.get("Arguments") is not None:
            self._Arguments = []
            for item in params.get("Arguments"):
                obj = KVPair()
                obj._deserialize(item)
                self._Arguments.append(obj)
        self._IsInherit = params.get("IsInherit")
        self._CustomKey = params.get("CustomKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkSessionBatchSQLResponse(AbstractModel):
    """CreateSparkSessionBatchSQL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批任务唯一标识
        :type BatchId: str
        :param _Statements: Statement任务列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Statements: list of StatementInformation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._Statements = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def Statements(self):
        return self._Statements

    @Statements.setter
    def Statements(self, Statements):
        self._Statements = Statements

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        if params.get("Statements") is not None:
            self._Statements = []
            for item in params.get("Statements"):
                obj = StatementInformation()
                obj._deserialize(item)
                self._Statements.append(obj)
        self._RequestId = params.get("RequestId")


class CreateStoreLocationRequest(AbstractModel):
    """CreateStoreLocation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StoreLocation: 计算结果存储cos路径，如：cosn://bucketname/
        :type StoreLocation: str
        """
        self._StoreLocation = None

    @property
    def StoreLocation(self):
        return self._StoreLocation

    @StoreLocation.setter
    def StoreLocation(self, StoreLocation):
        self._StoreLocation = StoreLocation


    def _deserialize(self, params):
        self._StoreLocation = params.get("StoreLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStoreLocationResponse(AbstractModel):
    """CreateStoreLocation返回参数结构体

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


class CreateTableRequest(AbstractModel):
    """CreateTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableInfo: 数据表配置信息
        :type TableInfo: :class:`tencentcloud.dlc.v20210125.models.TableInfo`
        """
        self._TableInfo = None

    @property
    def TableInfo(self):
        return self._TableInfo

    @TableInfo.setter
    def TableInfo(self, TableInfo):
        self._TableInfo = TableInfo


    def _deserialize(self, params):
        if params.get("TableInfo") is not None:
            self._TableInfo = TableInfo()
            self._TableInfo._deserialize(params.get("TableInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableResponse(AbstractModel):
    """CreateTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Execution: 生成的建表执行语句对象。
        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Execution = None
        self._RequestId = None

    @property
    def Execution(self):
        return self._Execution

    @Execution.setter
    def Execution(self, Execution):
        self._Execution = Execution

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Execution") is not None:
            self._Execution = Execution()
            self._Execution._deserialize(params.get("Execution"))
        self._RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Task: 计算任务，该参数中包含任务类型及其相关配置信息
        :type Task: :class:`tencentcloud.dlc.v20210125.models.Task`
        :param _DatabaseName: 数据库名称。如果SQL语句中有数据库名称，优先使用SQL语句中的数据库，否则使用该参数指定的数据库（注：当提交建库sql时，该字段传空字符串）。
        :type DatabaseName: str
        :param _DatasourceConnectionName: 默认数据源名称。
        :type DatasourceConnectionName: str
        :param _DataEngineName: 数据引擎名称，不填提交到默认集群
        :type DataEngineName: str
        :param _ResourceGroupName: 标准spark执行任务resourceGroupName
        :type ResourceGroupName: str
        """
        self._Task = None
        self._DatabaseName = None
        self._DatasourceConnectionName = None
        self._DataEngineName = None
        self._ResourceGroupName = None

    @property
    def Task(self):
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self._Task = Task()
            self._Task._deserialize(params.get("Task"))
        self._DatabaseName = params.get("DatabaseName")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._DataEngineName = params.get("DataEngineName")
        self._ResourceGroupName = params.get("ResourceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateTasksInOrderRequest(AbstractModel):
    """CreateTasksInOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名称。如果SQL语句中有数据库名称，优先使用SQL语句中的数据库，否则使用该参数指定的数据库。
        :type DatabaseName: str
        :param _Tasks: SQL任务信息
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TasksInfo`
        :param _DatasourceConnectionName: 数据源名称，默认为COSDataCatalog
        :type DatasourceConnectionName: str
        """
        self._DatabaseName = None
        self._Tasks = None
        self._DatasourceConnectionName = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        if params.get("Tasks") is not None:
            self._Tasks = TasksInfo()
            self._Tasks._deserialize(params.get("Tasks"))
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTasksInOrderResponse(AbstractModel):
    """CreateTasksInOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 本批次提交的任务的批次Id
        :type BatchId: str
        :param _TaskIdSet: 任务Id集合，按照执行顺序排列
        :type TaskIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._TaskIdSet = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def TaskIdSet(self):
        return self._TaskIdSet

    @TaskIdSet.setter
    def TaskIdSet(self, TaskIdSet):
        self._TaskIdSet = TaskIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._TaskIdSet = params.get("TaskIdSet")
        self._RequestId = params.get("RequestId")


class CreateTasksRequest(AbstractModel):
    """CreateTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名称。如果SQL语句中有数据库名称，优先使用SQL语句中的数据库，否则使用该参数指定的数据库（注：当提交建库sql时，该字段传空字符串）。
        :type DatabaseName: str
        :param _Tasks: SQL任务信息
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TasksInfo`
        :param _DatasourceConnectionName: 数据源名称，默认为DataLakeCatalog
        :type DatasourceConnectionName: str
        :param _DataEngineName: 计算引擎名称，不填任务提交到默认集群
        :type DataEngineName: str
        :param _ResourceGroupName: spark集群资源组名称
        :type ResourceGroupName: str
        """
        self._DatabaseName = None
        self._Tasks = None
        self._DatasourceConnectionName = None
        self._DataEngineName = None
        self._ResourceGroupName = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        if params.get("Tasks") is not None:
            self._Tasks = TasksInfo()
            self._Tasks._deserialize(params.get("Tasks"))
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._DataEngineName = params.get("DataEngineName")
        self._ResourceGroupName = params.get("ResourceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTasksResponse(AbstractModel):
    """CreateTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 本批次提交的任务的批次Id
        :type BatchId: str
        :param _TaskIdSet: 任务Id集合，按照执行顺序排列
        :type TaskIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._TaskIdSet = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def TaskIdSet(self):
        return self._TaskIdSet

    @TaskIdSet.setter
    def TaskIdSet(self, TaskIdSet):
        self._TaskIdSet = TaskIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._TaskIdSet = params.get("TaskIdSet")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 需要授权的子用户uin，可以通过腾讯云控制台右上角 → “账号信息” → “账号ID进行查看”。
        :type UserId: str
        :param _UserDescription: 用户描述信息，方便区分不同用户
        :type UserDescription: str
        :param _PolicySet: 绑定到用户的权限集合
        :type PolicySet: list of Policy
        :param _UserType: 用户类型。ADMIN：管理员 COMMON：一般用户。当用户类型为管理员的时候，不能设置权限集合和绑定的工作组集合，管理员默认拥有所有权限。该参数不填默认为COMMON
        :type UserType: str
        :param _WorkGroupIds: 绑定到用户的工作组ID集合。
        :type WorkGroupIds: list of int
        :param _UserAlias: 用户别名，字符长度小50
        :type UserAlias: str
        """
        self._UserId = None
        self._UserDescription = None
        self._PolicySet = None
        self._UserType = None
        self._WorkGroupIds = None
        self._UserAlias = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserDescription(self):
        return self._UserDescription

    @UserDescription.setter
    def UserDescription(self, UserDescription):
        self._UserDescription = UserDescription

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def WorkGroupIds(self):
        return self._WorkGroupIds

    @WorkGroupIds.setter
    def WorkGroupIds(self, WorkGroupIds):
        self._WorkGroupIds = WorkGroupIds

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserDescription = params.get("UserDescription")
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        self._UserType = params.get("UserType")
        self._WorkGroupIds = params.get("WorkGroupIds")
        self._UserAlias = params.get("UserAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

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


class CreateWorkGroupRequest(AbstractModel):
    """CreateWorkGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupName: 工作组名称
        :type WorkGroupName: str
        :param _WorkGroupDescription: 工作组描述
        :type WorkGroupDescription: str
        :param _PolicySet: 工作组绑定的鉴权策略集合
        :type PolicySet: list of Policy
        :param _UserIds: 需要绑定到工作组的用户Id集合
        :type UserIds: list of str
        """
        self._WorkGroupName = None
        self._WorkGroupDescription = None
        self._PolicySet = None
        self._UserIds = None

    @property
    def WorkGroupName(self):
        return self._WorkGroupName

    @WorkGroupName.setter
    def WorkGroupName(self, WorkGroupName):
        self._WorkGroupName = WorkGroupName

    @property
    def WorkGroupDescription(self):
        return self._WorkGroupDescription

    @WorkGroupDescription.setter
    def WorkGroupDescription(self, WorkGroupDescription):
        self._WorkGroupDescription = WorkGroupDescription

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._WorkGroupName = params.get("WorkGroupName")
        self._WorkGroupDescription = params.get("WorkGroupDescription")
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkGroupResponse(AbstractModel):
    """CreateWorkGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 工作组Id，全局唯一
        :type WorkGroupId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkGroupId = None
        self._RequestId = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        self._RequestId = params.get("RequestId")


class CrontabResumeSuspendStrategy(AbstractModel):
    """定时启停策略信息

    """

    def __init__(self):
        r"""
        :param _ResumeTime: 定时拉起时间：如：周一&周三8点
注意：此字段可能返回 null，表示取不到有效值。
        :type ResumeTime: str
        :param _SuspendTime: 定时挂起时间：如：周一&周三20点
注意：此字段可能返回 null，表示取不到有效值。
        :type SuspendTime: str
        :param _SuspendStrategy: 挂起配置：0（默认）：等待任务结束后挂起、1：强制挂起
注意：此字段可能返回 null，表示取不到有效值。
        :type SuspendStrategy: int
        """
        self._ResumeTime = None
        self._SuspendTime = None
        self._SuspendStrategy = None

    @property
    def ResumeTime(self):
        return self._ResumeTime

    @ResumeTime.setter
    def ResumeTime(self, ResumeTime):
        self._ResumeTime = ResumeTime

    @property
    def SuspendTime(self):
        return self._SuspendTime

    @SuspendTime.setter
    def SuspendTime(self, SuspendTime):
        self._SuspendTime = SuspendTime

    @property
    def SuspendStrategy(self):
        return self._SuspendStrategy

    @SuspendStrategy.setter
    def SuspendStrategy(self, SuspendStrategy):
        self._SuspendStrategy = SuspendStrategy


    def _deserialize(self, params):
        self._ResumeTime = params.get("ResumeTime")
        self._SuspendTime = params.get("SuspendTime")
        self._SuspendStrategy = params.get("SuspendStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DLCCatalogAccess(AbstractModel):
    """DLC 数据目录访问权限

    """

    def __init__(self):
        r"""
        :param _VpcId: VPCID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _Product: 产品类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: str
        :param _Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._VpcId = None
        self._Product = None
        self._Description = None
        self._CreateTime = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

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


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Product = params.get("Product")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSColumn(AbstractModel):
    """迁移列对象

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Position: 排序
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: int
        :param _Params: 附加参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of KVPair
        :param _BizParams: 业务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type BizParams: list of KVPair
        :param _IsPartition: 是否分区
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPartition: bool
        """
        self._Name = None
        self._Description = None
        self._Type = None
        self._Position = None
        self._Params = None
        self._BizParams = None
        self._IsPartition = None

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
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def BizParams(self):
        return self._BizParams

    @BizParams.setter
    def BizParams(self, BizParams):
        self._BizParams = BizParams

    @property
    def IsPartition(self):
        return self._IsPartition

    @IsPartition.setter
    def IsPartition(self, IsPartition):
        self._IsPartition = IsPartition


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        self._Position = params.get("Position")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self._Params.append(obj)
        if params.get("BizParams") is not None:
            self._BizParams = []
            for item in params.get("BizParams"):
                obj = KVPair()
                obj._deserialize(item)
                self._BizParams.append(obj)
        self._IsPartition = params.get("IsPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSColumnOrder(AbstractModel):
    """列排序对象

    """

    def __init__(self):
        r"""
        :param _Col: 列名
注意：此字段可能返回 null，表示取不到有效值。
        :type Col: str
        :param _Order: 排序
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: int
        """
        self._Col = None
        self._Order = None

    @property
    def Col(self):
        return self._Col

    @Col.setter
    def Col(self, Col):
        self._Col = Col

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Col = params.get("Col")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSPartition(AbstractModel):
    """迁移元数据分区对象

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名称
        :type DatabaseName: str
        :param _SchemaName: 数据目录名称
        :type SchemaName: str
        :param _TableName: 表名称
        :type TableName: str
        :param _DataVersion: 数据版本
        :type DataVersion: int
        :param _Name: 分区名称
        :type Name: str
        :param _Values: 值列表
        :type Values: list of str
        :param _StorageSize: 存储大小
        :type StorageSize: int
        :param _RecordCount: 记录数量
        :type RecordCount: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifiedTime: 修改时间
        :type ModifiedTime: str
        :param _LastAccessTime: 最后访问时间
        :type LastAccessTime: str
        :param _Params: 附件属性
        :type Params: list of KVPair
        :param _Sds: 存储对象
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        """
        self._DatabaseName = None
        self._SchemaName = None
        self._TableName = None
        self._DataVersion = None
        self._Name = None
        self._Values = None
        self._StorageSize = None
        self._RecordCount = None
        self._CreateTime = None
        self._ModifiedTime = None
        self._LastAccessTime = None
        self._Params = None
        self._Sds = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def DataVersion(self):
        return self._DataVersion

    @DataVersion.setter
    def DataVersion(self, DataVersion):
        self._DataVersion = DataVersion

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

    @property
    def StorageSize(self):
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def LastAccessTime(self):
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def Sds(self):
        return self._Sds

    @Sds.setter
    def Sds(self, Sds):
        self._Sds = Sds


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._SchemaName = params.get("SchemaName")
        self._TableName = params.get("TableName")
        self._DataVersion = params.get("DataVersion")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._StorageSize = params.get("StorageSize")
        self._RecordCount = params.get("RecordCount")
        self._CreateTime = params.get("CreateTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._LastAccessTime = params.get("LastAccessTime")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self._Params.append(obj)
        if params.get("Sds") is not None:
            self._Sds = DMSSds()
            self._Sds._deserialize(params.get("Sds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSSds(AbstractModel):
    """元数据存储描述属性

    """

    def __init__(self):
        r"""
        :param _Location: 存储地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param _InputFormat: 输入格式
注意：此字段可能返回 null，表示取不到有效值。
        :type InputFormat: str
        :param _OutputFormat: 输出格式
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputFormat: str
        :param _NumBuckets: bucket数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NumBuckets: int
        :param _Compressed: 是是否压缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Compressed: bool
        :param _StoredAsSubDirectories: 是否有子目录
注意：此字段可能返回 null，表示取不到有效值。
        :type StoredAsSubDirectories: bool
        :param _SerdeLib: 序列化lib
注意：此字段可能返回 null，表示取不到有效值。
        :type SerdeLib: str
        :param _SerdeName: 序列化名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SerdeName: str
        :param _BucketCols: 桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketCols: list of str
        :param _SerdeParams: 序列化参数
注意：此字段可能返回 null，表示取不到有效值。
        :type SerdeParams: list of KVPair
        :param _Params: 附加参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of KVPair
        :param _SortCols: 列排序(Expired)
注意：此字段可能返回 null，表示取不到有效值。
        :type SortCols: :class:`tencentcloud.dlc.v20210125.models.DMSColumnOrder`
        :param _Cols: 列
注意：此字段可能返回 null，表示取不到有效值。
        :type Cols: list of DMSColumn
        :param _SortColumns: 列排序字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SortColumns: list of DMSColumnOrder
        """
        self._Location = None
        self._InputFormat = None
        self._OutputFormat = None
        self._NumBuckets = None
        self._Compressed = None
        self._StoredAsSubDirectories = None
        self._SerdeLib = None
        self._SerdeName = None
        self._BucketCols = None
        self._SerdeParams = None
        self._Params = None
        self._SortCols = None
        self._Cols = None
        self._SortColumns = None

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def InputFormat(self):
        return self._InputFormat

    @InputFormat.setter
    def InputFormat(self, InputFormat):
        self._InputFormat = InputFormat

    @property
    def OutputFormat(self):
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def NumBuckets(self):
        return self._NumBuckets

    @NumBuckets.setter
    def NumBuckets(self, NumBuckets):
        self._NumBuckets = NumBuckets

    @property
    def Compressed(self):
        return self._Compressed

    @Compressed.setter
    def Compressed(self, Compressed):
        self._Compressed = Compressed

    @property
    def StoredAsSubDirectories(self):
        return self._StoredAsSubDirectories

    @StoredAsSubDirectories.setter
    def StoredAsSubDirectories(self, StoredAsSubDirectories):
        self._StoredAsSubDirectories = StoredAsSubDirectories

    @property
    def SerdeLib(self):
        return self._SerdeLib

    @SerdeLib.setter
    def SerdeLib(self, SerdeLib):
        self._SerdeLib = SerdeLib

    @property
    def SerdeName(self):
        return self._SerdeName

    @SerdeName.setter
    def SerdeName(self, SerdeName):
        self._SerdeName = SerdeName

    @property
    def BucketCols(self):
        return self._BucketCols

    @BucketCols.setter
    def BucketCols(self, BucketCols):
        self._BucketCols = BucketCols

    @property
    def SerdeParams(self):
        return self._SerdeParams

    @SerdeParams.setter
    def SerdeParams(self, SerdeParams):
        self._SerdeParams = SerdeParams

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def SortCols(self):
        return self._SortCols

    @SortCols.setter
    def SortCols(self, SortCols):
        self._SortCols = SortCols

    @property
    def Cols(self):
        return self._Cols

    @Cols.setter
    def Cols(self, Cols):
        self._Cols = Cols

    @property
    def SortColumns(self):
        return self._SortColumns

    @SortColumns.setter
    def SortColumns(self, SortColumns):
        self._SortColumns = SortColumns


    def _deserialize(self, params):
        self._Location = params.get("Location")
        self._InputFormat = params.get("InputFormat")
        self._OutputFormat = params.get("OutputFormat")
        self._NumBuckets = params.get("NumBuckets")
        self._Compressed = params.get("Compressed")
        self._StoredAsSubDirectories = params.get("StoredAsSubDirectories")
        self._SerdeLib = params.get("SerdeLib")
        self._SerdeName = params.get("SerdeName")
        self._BucketCols = params.get("BucketCols")
        if params.get("SerdeParams") is not None:
            self._SerdeParams = []
            for item in params.get("SerdeParams"):
                obj = KVPair()
                obj._deserialize(item)
                self._SerdeParams.append(obj)
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self._Params.append(obj)
        if params.get("SortCols") is not None:
            self._SortCols = DMSColumnOrder()
            self._SortCols._deserialize(params.get("SortCols"))
        if params.get("Cols") is not None:
            self._Cols = []
            for item in params.get("Cols"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._Cols.append(obj)
        if params.get("SortColumns") is not None:
            self._SortColumns = []
            for item in params.get("SortColumns"):
                obj = DMSColumnOrder()
                obj._deserialize(item)
                self._SortColumns.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSTable(AbstractModel):
    """DMSTable基本信息

    """

    def __init__(self):
        r"""
        :param _ViewOriginalText: 视图文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewOriginalText: str
        :param _ViewExpandedText: 视图文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewExpandedText: str
        :param _Retention: hive维护版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Retention: int
        :param _Sds: 存储对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        :param _PartitionKeys: 分区列
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionKeys: list of DMSColumn
        :param _Partitions: 分区
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of DMSPartition
        :param _Type: 表类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _DbName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param _SchemaName: Schema名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param _StorageSize: 存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSize: int
        :param _RecordCount: 记录数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCount: int
        :param _LifeTime: 生命周期
注意：此字段可能返回 null，表示取不到有效值。
        :type LifeTime: int
        :param _LastAccessTime: 最后访问时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastAccessTime: str
        :param _DataUpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUpdateTime: str
        :param _StructUpdateTime: 结构更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StructUpdateTime: str
        :param _Columns: 列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of DMSColumn
        :param _Name: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._ViewOriginalText = None
        self._ViewExpandedText = None
        self._Retention = None
        self._Sds = None
        self._PartitionKeys = None
        self._Partitions = None
        self._Type = None
        self._DbName = None
        self._SchemaName = None
        self._StorageSize = None
        self._RecordCount = None
        self._LifeTime = None
        self._LastAccessTime = None
        self._DataUpdateTime = None
        self._StructUpdateTime = None
        self._Columns = None
        self._Name = None

    @property
    def ViewOriginalText(self):
        return self._ViewOriginalText

    @ViewOriginalText.setter
    def ViewOriginalText(self, ViewOriginalText):
        self._ViewOriginalText = ViewOriginalText

    @property
    def ViewExpandedText(self):
        return self._ViewExpandedText

    @ViewExpandedText.setter
    def ViewExpandedText(self, ViewExpandedText):
        self._ViewExpandedText = ViewExpandedText

    @property
    def Retention(self):
        return self._Retention

    @Retention.setter
    def Retention(self, Retention):
        self._Retention = Retention

    @property
    def Sds(self):
        return self._Sds

    @Sds.setter
    def Sds(self, Sds):
        self._Sds = Sds

    @property
    def PartitionKeys(self):
        return self._PartitionKeys

    @PartitionKeys.setter
    def PartitionKeys(self, PartitionKeys):
        self._PartitionKeys = PartitionKeys

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def StorageSize(self):
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def LifeTime(self):
        return self._LifeTime

    @LifeTime.setter
    def LifeTime(self, LifeTime):
        self._LifeTime = LifeTime

    @property
    def LastAccessTime(self):
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def DataUpdateTime(self):
        return self._DataUpdateTime

    @DataUpdateTime.setter
    def DataUpdateTime(self, DataUpdateTime):
        self._DataUpdateTime = DataUpdateTime

    @property
    def StructUpdateTime(self):
        return self._StructUpdateTime

    @StructUpdateTime.setter
    def StructUpdateTime(self, StructUpdateTime):
        self._StructUpdateTime = StructUpdateTime

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ViewOriginalText = params.get("ViewOriginalText")
        self._ViewExpandedText = params.get("ViewExpandedText")
        self._Retention = params.get("Retention")
        if params.get("Sds") is not None:
            self._Sds = DMSSds()
            self._Sds._deserialize(params.get("Sds"))
        if params.get("PartitionKeys") is not None:
            self._PartitionKeys = []
            for item in params.get("PartitionKeys"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._PartitionKeys.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._Type = params.get("Type")
        self._DbName = params.get("DbName")
        self._SchemaName = params.get("SchemaName")
        self._StorageSize = params.get("StorageSize")
        self._RecordCount = params.get("RecordCount")
        self._LifeTime = params.get("LifeTime")
        self._LastAccessTime = params.get("LastAccessTime")
        self._DataUpdateTime = params.get("DataUpdateTime")
        self._StructUpdateTime = params.get("StructUpdateTime")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DMSTableInfo(AbstractModel):
    """DMSTable信息

    """

    def __init__(self):
        r"""
        :param _Table: DMS表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: :class:`tencentcloud.dlc.v20210125.models.DMSTable`
        :param _Asset: 基础对象信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        """
        self._Table = None
        self._Asset = None

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset


    def _deserialize(self, params):
        if params.get("Table") is not None:
            self._Table = DMSTable()
            self._Table._deserialize(params.get("Table"))
        if params.get("Asset") is not None:
            self._Asset = Asset()
            self._Asset._deserialize(params.get("Asset"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineBasicInfo(AbstractModel):
    """DataEngine基本信息

    """

    def __init__(self):
        r"""
        :param _DataEngineName: DataEngine名称
        :type DataEngineName: str
        :param _State: 数据引擎状态  -2已删除 -1失败 0初始化中 1挂起 2运行中 3准备删除 4删除中
        :type State: int
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        :param _Message: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _DataEngineId: 引擎id
        :type DataEngineId: str
        :param _DataEngineType: 引擎类型，有效值：PrestoSQL/SparkSQL/SparkBatch
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineType: str
        :param _AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _UserUin: 账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserUin: str
        """
        self._DataEngineName = None
        self._State = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Message = None
        self._DataEngineId = None
        self._DataEngineType = None
        self._AppId = None
        self._UserUin = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

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
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def DataEngineType(self):
        return self._DataEngineType

    @DataEngineType.setter
    def DataEngineType(self, DataEngineType):
        self._DataEngineType = DataEngineType

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UserUin(self):
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Message = params.get("Message")
        self._DataEngineId = params.get("DataEngineId")
        self._DataEngineType = params.get("DataEngineType")
        self._AppId = params.get("AppId")
        self._UserUin = params.get("UserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineConfigInstanceInfo(AbstractModel):
    """引擎配置信息

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 引擎ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineId: str
        :param _DataEngineConfigPairs: 用户自定义配置项集合
        :type DataEngineConfigPairs: list of DataEngineConfigPair
        :param _SessionResourceTemplate: 作业集群资源参数配置模板
        :type SessionResourceTemplate: :class:`tencentcloud.dlc.v20210125.models.SessionResourceTemplate`
        """
        self._DataEngineId = None
        self._DataEngineConfigPairs = None
        self._SessionResourceTemplate = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def DataEngineConfigPairs(self):
        return self._DataEngineConfigPairs

    @DataEngineConfigPairs.setter
    def DataEngineConfigPairs(self, DataEngineConfigPairs):
        self._DataEngineConfigPairs = DataEngineConfigPairs

    @property
    def SessionResourceTemplate(self):
        return self._SessionResourceTemplate

    @SessionResourceTemplate.setter
    def SessionResourceTemplate(self, SessionResourceTemplate):
        self._SessionResourceTemplate = SessionResourceTemplate


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        if params.get("DataEngineConfigPairs") is not None:
            self._DataEngineConfigPairs = []
            for item in params.get("DataEngineConfigPairs"):
                obj = DataEngineConfigPair()
                obj._deserialize(item)
                self._DataEngineConfigPairs.append(obj)
        if params.get("SessionResourceTemplate") is not None:
            self._SessionResourceTemplate = SessionResourceTemplate()
            self._SessionResourceTemplate._deserialize(params.get("SessionResourceTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineConfigPair(AbstractModel):
    """引擎配置

    """

    def __init__(self):
        r"""
        :param _ConfigItem: 配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigItem: str
        :param _ConfigValue: 配置值
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigValue: str
        """
        self._ConfigItem = None
        self._ConfigValue = None

    @property
    def ConfigItem(self):
        return self._ConfigItem

    @ConfigItem.setter
    def ConfigItem(self, ConfigItem):
        self._ConfigItem = ConfigItem

    @property
    def ConfigValue(self):
        return self._ConfigValue

    @ConfigValue.setter
    def ConfigValue(self, ConfigValue):
        self._ConfigValue = ConfigValue


    def _deserialize(self, params):
        self._ConfigItem = params.get("ConfigItem")
        self._ConfigValue = params.get("ConfigValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineImageVersion(AbstractModel):
    """集群大版本镜像信息。

    """

    def __init__(self):
        r"""
        :param _ImageVersionId: 镜像大版本ID
        :type ImageVersionId: str
        :param _ImageVersion: 镜像大版本名称
        :type ImageVersion: str
        :param _Description: 镜像大版本描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _IsPublic: 是否为公共版本：1：公共；2：私有
        :type IsPublic: int
        :param _EngineType: 集群类型：SparkSQL/PrestoSQL/SparkBatch
        :type EngineType: str
        :param _IsSharedEngine: 版本状态：1：初始化；2：上线；3：下线
        :type IsSharedEngine: int
        :param _State: 版本状态：1：初始化；2：上线；3：下线
        :type State: int
        :param _InsertTime: 插入时间
        :type InsertTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._ImageVersionId = None
        self._ImageVersion = None
        self._Description = None
        self._IsPublic = None
        self._EngineType = None
        self._IsSharedEngine = None
        self._State = None
        self._InsertTime = None
        self._UpdateTime = None

    @property
    def ImageVersionId(self):
        return self._ImageVersionId

    @ImageVersionId.setter
    def ImageVersionId(self, ImageVersionId):
        self._ImageVersionId = ImageVersionId

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def IsSharedEngine(self):
        return self._IsSharedEngine

    @IsSharedEngine.setter
    def IsSharedEngine(self, IsSharedEngine):
        self._IsSharedEngine = IsSharedEngine

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ImageVersionId = params.get("ImageVersionId")
        self._ImageVersion = params.get("ImageVersion")
        self._Description = params.get("Description")
        self._IsPublic = params.get("IsPublic")
        self._EngineType = params.get("EngineType")
        self._IsSharedEngine = params.get("IsSharedEngine")
        self._State = params.get("State")
        self._InsertTime = params.get("InsertTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineInfo(AbstractModel):
    """DataEngine详细信息

    """

    def __init__(self):
        r"""
        :param _DataEngineName: DataEngine名称
        :type DataEngineName: str
        :param _EngineType: 引擎类型 spark/presto
        :type EngineType: str
        :param _ClusterType: 集群资源类型 spark_private/presto_private/presto_cu/spark_cu
        :type ClusterType: str
        :param _QuotaId: 引用ID
        :type QuotaId: str
        :param _State: 数据引擎状态  -2已删除 -1失败 0初始化中 1挂起 2运行中 3准备删除 4删除中
        :type State: int
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        :param _Size: 集群规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _Mode: 计费模式 0共享模式 1按量计费 2包年包月
        :type Mode: int
        :param _MinClusters: 最小集群数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinClusters: int
        :param _MaxClusters: 最大集群数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxClusters: int
        :param _AutoResume: 是否自动恢复
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoResume: bool
        :param _SpendAfter: 自动恢复时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SpendAfter: int
        :param _CidrBlock: 集群网段
注意：此字段可能返回 null，表示取不到有效值。
        :type CidrBlock: str
        :param _DefaultDataEngine: 是否为默认引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDataEngine: bool
        :param _Message: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _DataEngineId: 引擎id
        :type DataEngineId: str
        :param _SubAccountUin: 操作者
        :type SubAccountUin: str
        :param _ExpireTime: 到期时间
        :type ExpireTime: str
        :param _IsolatedTime: 隔离时间
        :type IsolatedTime: str
        :param _ReversalTime: 冲正时间
        :type ReversalTime: str
        :param _UserAlias: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param _TagList: 标签对集合
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of TagInfo
        :param _Permissions: 引擎拥有的权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Permissions: list of str
        :param _AutoSuspend: 是否自定挂起集群：false（默认）：不自动挂起、true：自动挂起
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSuspend: bool
        :param _CrontabResumeSuspend: 定时启停集群策略：0（默认）：关闭定时策略、1：开启定时策略（注：定时启停策略与自动挂起策略互斥）
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabResumeSuspend: int
        :param _CrontabResumeSuspendStrategy: 定时启停策略，复杂类型：包含启停时间、挂起集群策略
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabResumeSuspendStrategy: :class:`tencentcloud.dlc.v20210125.models.CrontabResumeSuspendStrategy`
        :param _EngineExecType: 引擎执行任务类型，有效值：SQL/BATCH
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineExecType: str
        :param _RenewFlag: 自动续费标志，0，初始状态，默认不自动续费，若用户有预付费不停服特权，自动续费。1：自动续费。2：明确不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _AutoSuspendTime: 集群自动挂起时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSuspendTime: int
        :param _NetworkConnectionSet: 网络连接配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConnectionSet: list of NetworkConnection
        :param _UiURL: ui的跳转地址
注意：此字段可能返回 null，表示取不到有效值。
        :type UiURL: str
        :param _ResourceType: 引擎的资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _ImageVersionId: 集群镜像版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageVersionId: str
        :param _ChildImageVersionId: 集群镜像小版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildImageVersionId: str
        :param _ImageVersionName: 集群镜像版本名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageVersionName: str
        :param _StartStandbyCluster: 是否开启备集群
注意：此字段可能返回 null，表示取不到有效值。
        :type StartStandbyCluster: bool
        :param _ElasticSwitch: spark jar 包年包月集群是否开启弹性
注意：此字段可能返回 null，表示取不到有效值。
        :type ElasticSwitch: bool
        :param _ElasticLimit: spark jar 包年包月集群弹性上限
注意：此字段可能返回 null，表示取不到有效值。
        :type ElasticLimit: int
        :param _DefaultHouse: 是否为默认引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultHouse: bool
        :param _MaxConcurrency: 单个集群任务最大并发数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConcurrency: int
        :param _TolerableQueueTime: 任务排队上限时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TolerableQueueTime: int
        :param _UserAppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAppId: int
        :param _UserUin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type UserUin: str
        :param _SessionResourceTemplate: SessionResourceTemplate
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionResourceTemplate: :class:`tencentcloud.dlc.v20210125.models.SessionResourceTemplate`
        :param _AutoAuthorization: 自动授权开关
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoAuthorization: bool
        :param _EngineGeneration: 引擎版本，支持Native/SuperSQL
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineGeneration: str
        :param _EngineTypeDetail: 引擎详细类型，支持：SparkSQL/SparkBatch/PrestoSQL/Kyuubi
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineTypeDetail: str
        :param _EngineNetworkId: 引擎网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineNetworkId: str
        :param _EngineResourceGroupCount: 标准引擎关联的资源组个数
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineResourceGroupCount: int
        :param _EngineResourceUsedCU: 引擎当前使用量（Cu）
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineResourceUsedCU: int
        :param _AccessInfos: 引擎的访问信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessInfos: list of AccessInfo
        :param _EngineNetworkName: 引擎所在网络名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineNetworkName: str
        """
        self._DataEngineName = None
        self._EngineType = None
        self._ClusterType = None
        self._QuotaId = None
        self._State = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Size = None
        self._Mode = None
        self._MinClusters = None
        self._MaxClusters = None
        self._AutoResume = None
        self._SpendAfter = None
        self._CidrBlock = None
        self._DefaultDataEngine = None
        self._Message = None
        self._DataEngineId = None
        self._SubAccountUin = None
        self._ExpireTime = None
        self._IsolatedTime = None
        self._ReversalTime = None
        self._UserAlias = None
        self._TagList = None
        self._Permissions = None
        self._AutoSuspend = None
        self._CrontabResumeSuspend = None
        self._CrontabResumeSuspendStrategy = None
        self._EngineExecType = None
        self._RenewFlag = None
        self._AutoSuspendTime = None
        self._NetworkConnectionSet = None
        self._UiURL = None
        self._ResourceType = None
        self._ImageVersionId = None
        self._ChildImageVersionId = None
        self._ImageVersionName = None
        self._StartStandbyCluster = None
        self._ElasticSwitch = None
        self._ElasticLimit = None
        self._DefaultHouse = None
        self._MaxConcurrency = None
        self._TolerableQueueTime = None
        self._UserAppId = None
        self._UserUin = None
        self._SessionResourceTemplate = None
        self._AutoAuthorization = None
        self._EngineGeneration = None
        self._EngineTypeDetail = None
        self._EngineNetworkId = None
        self._EngineResourceGroupCount = None
        self._EngineResourceUsedCU = None
        self._AccessInfos = None
        self._EngineNetworkName = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def QuotaId(self):
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

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
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def MinClusters(self):
        return self._MinClusters

    @MinClusters.setter
    def MinClusters(self, MinClusters):
        self._MinClusters = MinClusters

    @property
    def MaxClusters(self):
        return self._MaxClusters

    @MaxClusters.setter
    def MaxClusters(self, MaxClusters):
        self._MaxClusters = MaxClusters

    @property
    def AutoResume(self):
        return self._AutoResume

    @AutoResume.setter
    def AutoResume(self, AutoResume):
        self._AutoResume = AutoResume

    @property
    def SpendAfter(self):
        return self._SpendAfter

    @SpendAfter.setter
    def SpendAfter(self, SpendAfter):
        self._SpendAfter = SpendAfter

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def DefaultDataEngine(self):
        return self._DefaultDataEngine

    @DefaultDataEngine.setter
    def DefaultDataEngine(self, DefaultDataEngine):
        self._DefaultDataEngine = DefaultDataEngine

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsolatedTime(self):
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def ReversalTime(self):
        return self._ReversalTime

    @ReversalTime.setter
    def ReversalTime(self, ReversalTime):
        self._ReversalTime = ReversalTime

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def AutoSuspend(self):
        return self._AutoSuspend

    @AutoSuspend.setter
    def AutoSuspend(self, AutoSuspend):
        self._AutoSuspend = AutoSuspend

    @property
    def CrontabResumeSuspend(self):
        return self._CrontabResumeSuspend

    @CrontabResumeSuspend.setter
    def CrontabResumeSuspend(self, CrontabResumeSuspend):
        self._CrontabResumeSuspend = CrontabResumeSuspend

    @property
    def CrontabResumeSuspendStrategy(self):
        return self._CrontabResumeSuspendStrategy

    @CrontabResumeSuspendStrategy.setter
    def CrontabResumeSuspendStrategy(self, CrontabResumeSuspendStrategy):
        self._CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy

    @property
    def EngineExecType(self):
        return self._EngineExecType

    @EngineExecType.setter
    def EngineExecType(self, EngineExecType):
        self._EngineExecType = EngineExecType

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def AutoSuspendTime(self):
        return self._AutoSuspendTime

    @AutoSuspendTime.setter
    def AutoSuspendTime(self, AutoSuspendTime):
        self._AutoSuspendTime = AutoSuspendTime

    @property
    def NetworkConnectionSet(self):
        return self._NetworkConnectionSet

    @NetworkConnectionSet.setter
    def NetworkConnectionSet(self, NetworkConnectionSet):
        self._NetworkConnectionSet = NetworkConnectionSet

    @property
    def UiURL(self):
        return self._UiURL

    @UiURL.setter
    def UiURL(self, UiURL):
        self._UiURL = UiURL

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ImageVersionId(self):
        return self._ImageVersionId

    @ImageVersionId.setter
    def ImageVersionId(self, ImageVersionId):
        self._ImageVersionId = ImageVersionId

    @property
    def ChildImageVersionId(self):
        return self._ChildImageVersionId

    @ChildImageVersionId.setter
    def ChildImageVersionId(self, ChildImageVersionId):
        self._ChildImageVersionId = ChildImageVersionId

    @property
    def ImageVersionName(self):
        return self._ImageVersionName

    @ImageVersionName.setter
    def ImageVersionName(self, ImageVersionName):
        self._ImageVersionName = ImageVersionName

    @property
    def StartStandbyCluster(self):
        return self._StartStandbyCluster

    @StartStandbyCluster.setter
    def StartStandbyCluster(self, StartStandbyCluster):
        self._StartStandbyCluster = StartStandbyCluster

    @property
    def ElasticSwitch(self):
        return self._ElasticSwitch

    @ElasticSwitch.setter
    def ElasticSwitch(self, ElasticSwitch):
        self._ElasticSwitch = ElasticSwitch

    @property
    def ElasticLimit(self):
        return self._ElasticLimit

    @ElasticLimit.setter
    def ElasticLimit(self, ElasticLimit):
        self._ElasticLimit = ElasticLimit

    @property
    def DefaultHouse(self):
        return self._DefaultHouse

    @DefaultHouse.setter
    def DefaultHouse(self, DefaultHouse):
        self._DefaultHouse = DefaultHouse

    @property
    def MaxConcurrency(self):
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def TolerableQueueTime(self):
        return self._TolerableQueueTime

    @TolerableQueueTime.setter
    def TolerableQueueTime(self, TolerableQueueTime):
        self._TolerableQueueTime = TolerableQueueTime

    @property
    def UserAppId(self):
        return self._UserAppId

    @UserAppId.setter
    def UserAppId(self, UserAppId):
        self._UserAppId = UserAppId

    @property
    def UserUin(self):
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def SessionResourceTemplate(self):
        return self._SessionResourceTemplate

    @SessionResourceTemplate.setter
    def SessionResourceTemplate(self, SessionResourceTemplate):
        self._SessionResourceTemplate = SessionResourceTemplate

    @property
    def AutoAuthorization(self):
        return self._AutoAuthorization

    @AutoAuthorization.setter
    def AutoAuthorization(self, AutoAuthorization):
        self._AutoAuthorization = AutoAuthorization

    @property
    def EngineGeneration(self):
        return self._EngineGeneration

    @EngineGeneration.setter
    def EngineGeneration(self, EngineGeneration):
        self._EngineGeneration = EngineGeneration

    @property
    def EngineTypeDetail(self):
        return self._EngineTypeDetail

    @EngineTypeDetail.setter
    def EngineTypeDetail(self, EngineTypeDetail):
        self._EngineTypeDetail = EngineTypeDetail

    @property
    def EngineNetworkId(self):
        return self._EngineNetworkId

    @EngineNetworkId.setter
    def EngineNetworkId(self, EngineNetworkId):
        self._EngineNetworkId = EngineNetworkId

    @property
    def EngineResourceGroupCount(self):
        return self._EngineResourceGroupCount

    @EngineResourceGroupCount.setter
    def EngineResourceGroupCount(self, EngineResourceGroupCount):
        self._EngineResourceGroupCount = EngineResourceGroupCount

    @property
    def EngineResourceUsedCU(self):
        return self._EngineResourceUsedCU

    @EngineResourceUsedCU.setter
    def EngineResourceUsedCU(self, EngineResourceUsedCU):
        self._EngineResourceUsedCU = EngineResourceUsedCU

    @property
    def AccessInfos(self):
        return self._AccessInfos

    @AccessInfos.setter
    def AccessInfos(self, AccessInfos):
        self._AccessInfos = AccessInfos

    @property
    def EngineNetworkName(self):
        return self._EngineNetworkName

    @EngineNetworkName.setter
    def EngineNetworkName(self, EngineNetworkName):
        self._EngineNetworkName = EngineNetworkName


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._EngineType = params.get("EngineType")
        self._ClusterType = params.get("ClusterType")
        self._QuotaId = params.get("QuotaId")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Size = params.get("Size")
        self._Mode = params.get("Mode")
        self._MinClusters = params.get("MinClusters")
        self._MaxClusters = params.get("MaxClusters")
        self._AutoResume = params.get("AutoResume")
        self._SpendAfter = params.get("SpendAfter")
        self._CidrBlock = params.get("CidrBlock")
        self._DefaultDataEngine = params.get("DefaultDataEngine")
        self._Message = params.get("Message")
        self._DataEngineId = params.get("DataEngineId")
        self._SubAccountUin = params.get("SubAccountUin")
        self._ExpireTime = params.get("ExpireTime")
        self._IsolatedTime = params.get("IsolatedTime")
        self._ReversalTime = params.get("ReversalTime")
        self._UserAlias = params.get("UserAlias")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._Permissions = params.get("Permissions")
        self._AutoSuspend = params.get("AutoSuspend")
        self._CrontabResumeSuspend = params.get("CrontabResumeSuspend")
        if params.get("CrontabResumeSuspendStrategy") is not None:
            self._CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy()
            self._CrontabResumeSuspendStrategy._deserialize(params.get("CrontabResumeSuspendStrategy"))
        self._EngineExecType = params.get("EngineExecType")
        self._RenewFlag = params.get("RenewFlag")
        self._AutoSuspendTime = params.get("AutoSuspendTime")
        if params.get("NetworkConnectionSet") is not None:
            self._NetworkConnectionSet = []
            for item in params.get("NetworkConnectionSet"):
                obj = NetworkConnection()
                obj._deserialize(item)
                self._NetworkConnectionSet.append(obj)
        self._UiURL = params.get("UiURL")
        self._ResourceType = params.get("ResourceType")
        self._ImageVersionId = params.get("ImageVersionId")
        self._ChildImageVersionId = params.get("ChildImageVersionId")
        self._ImageVersionName = params.get("ImageVersionName")
        self._StartStandbyCluster = params.get("StartStandbyCluster")
        self._ElasticSwitch = params.get("ElasticSwitch")
        self._ElasticLimit = params.get("ElasticLimit")
        self._DefaultHouse = params.get("DefaultHouse")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._TolerableQueueTime = params.get("TolerableQueueTime")
        self._UserAppId = params.get("UserAppId")
        self._UserUin = params.get("UserUin")
        if params.get("SessionResourceTemplate") is not None:
            self._SessionResourceTemplate = SessionResourceTemplate()
            self._SessionResourceTemplate._deserialize(params.get("SessionResourceTemplate"))
        self._AutoAuthorization = params.get("AutoAuthorization")
        self._EngineGeneration = params.get("EngineGeneration")
        self._EngineTypeDetail = params.get("EngineTypeDetail")
        self._EngineNetworkId = params.get("EngineNetworkId")
        self._EngineResourceGroupCount = params.get("EngineResourceGroupCount")
        self._EngineResourceUsedCU = params.get("EngineResourceUsedCU")
        if params.get("AccessInfos") is not None:
            self._AccessInfos = []
            for item in params.get("AccessInfos"):
                obj = AccessInfo()
                obj._deserialize(item)
                self._AccessInfos.append(obj)
        self._EngineNetworkName = params.get("EngineNetworkName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineScaleInfo(AbstractModel):
    """引擎规格详情

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 引擎ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineId: str
        :param _DataEngineName: 引擎名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineName: str
        :param _ScaleDetail: 引擎规格详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleDetail: list of DataEngineScaleInfoDetail
        """
        self._DataEngineId = None
        self._DataEngineName = None
        self._ScaleDetail = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ScaleDetail(self):
        return self._ScaleDetail

    @ScaleDetail.setter
    def ScaleDetail(self, ScaleDetail):
        self._ScaleDetail = ScaleDetail


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        self._DataEngineName = params.get("DataEngineName")
        if params.get("ScaleDetail") is not None:
            self._ScaleDetail = []
            for item in params.get("ScaleDetail"):
                obj = DataEngineScaleInfoDetail()
                obj._deserialize(item)
                self._ScaleDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineScaleInfoDetail(AbstractModel):
    """引擎规格详情

    """

    def __init__(self):
        r"""
        :param _StartTime: 统计开始时间，格式为：yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 统计结束时间，格式为：yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CU: 当前统计时间段，引擎规格
注意：此字段可能返回 null，表示取不到有效值。
        :type CU: int
        """
        self._StartTime = None
        self._EndTime = None
        self._CU = None

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

    @property
    def CU(self):
        return self._CU

    @CU.setter
    def CU(self, CU):
        self._CU = CU


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CU = params.get("CU")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataFormat(AbstractModel):
    """数据表数据格式。

    """

    def __init__(self):
        r"""
        :param _TextFile: 文本格式，TextFile。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextFile: :class:`tencentcloud.dlc.v20210125.models.TextFile`
        :param _CSV: 文本格式，CSV。
注意：此字段可能返回 null，表示取不到有效值。
        :type CSV: :class:`tencentcloud.dlc.v20210125.models.CSV`
        :param _Json: 文本格式，Json。
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: :class:`tencentcloud.dlc.v20210125.models.Other`
        :param _Parquet: Parquet格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Parquet: :class:`tencentcloud.dlc.v20210125.models.Other`
        :param _ORC: ORC格式
注意：此字段可能返回 null，表示取不到有效值。
        :type ORC: :class:`tencentcloud.dlc.v20210125.models.Other`
        :param _AVRO: AVRO格式
注意：此字段可能返回 null，表示取不到有效值。
        :type AVRO: :class:`tencentcloud.dlc.v20210125.models.Other`
        """
        self._TextFile = None
        self._CSV = None
        self._Json = None
        self._Parquet = None
        self._ORC = None
        self._AVRO = None

    @property
    def TextFile(self):
        return self._TextFile

    @TextFile.setter
    def TextFile(self, TextFile):
        self._TextFile = TextFile

    @property
    def CSV(self):
        return self._CSV

    @CSV.setter
    def CSV(self, CSV):
        self._CSV = CSV

    @property
    def Json(self):
        return self._Json

    @Json.setter
    def Json(self, Json):
        self._Json = Json

    @property
    def Parquet(self):
        return self._Parquet

    @Parquet.setter
    def Parquet(self, Parquet):
        self._Parquet = Parquet

    @property
    def ORC(self):
        return self._ORC

    @ORC.setter
    def ORC(self, ORC):
        self._ORC = ORC

    @property
    def AVRO(self):
        return self._AVRO

    @AVRO.setter
    def AVRO(self, AVRO):
        self._AVRO = AVRO


    def _deserialize(self, params):
        if params.get("TextFile") is not None:
            self._TextFile = TextFile()
            self._TextFile._deserialize(params.get("TextFile"))
        if params.get("CSV") is not None:
            self._CSV = CSV()
            self._CSV._deserialize(params.get("CSV"))
        if params.get("Json") is not None:
            self._Json = Other()
            self._Json._deserialize(params.get("Json"))
        if params.get("Parquet") is not None:
            self._Parquet = Other()
            self._Parquet._deserialize(params.get("Parquet"))
        if params.get("ORC") is not None:
            self._ORC = Other()
            self._ORC._deserialize(params.get("ORC"))
        if params.get("AVRO") is not None:
            self._AVRO = Other()
            self._AVRO._deserialize(params.get("AVRO"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataGovernPolicy(AbstractModel):
    """数据治理规则

    """

    def __init__(self):
        r"""
        :param _RuleType: 治理规则类型，Customize: 自定义；Intelligence: 智能治理
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _GovernEngine: 治理引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type GovernEngine: str
        """
        self._RuleType = None
        self._GovernEngine = None

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def GovernEngine(self):
        return self._GovernEngine

    @GovernEngine.setter
    def GovernEngine(self, GovernEngine):
        self._GovernEngine = GovernEngine


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._GovernEngine = params.get("GovernEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceInfo(AbstractModel):
    """数据源详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据源实例的唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 数据源的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _JdbcUrl: 数据源的JDBC访问链接
注意：此字段可能返回 null，表示取不到有效值。
        :type JdbcUrl: str
        :param _User: 用于访问数据源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _Password: 数据源访问密码，需要base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Location: 数据源的VPC和子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: :class:`tencentcloud.dlc.v20210125.models.DatasourceConnectionLocation`
        :param _DbName: 默认数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._JdbcUrl = None
        self._User = None
        self._Password = None
        self._Location = None
        self._DbName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def JdbcUrl(self):
        return self._JdbcUrl

    @JdbcUrl.setter
    def JdbcUrl(self, JdbcUrl):
        self._JdbcUrl = JdbcUrl

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._JdbcUrl = params.get("JdbcUrl")
        self._User = params.get("User")
        self._Password = params.get("Password")
        if params.get("Location") is not None:
            self._Location = DatasourceConnectionLocation()
            self._Location._deserialize(params.get("Location"))
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseInfo(AbstractModel):
    """数据库对象

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名称，长度0~128，支持数字、字母下划线，不允许数字大头，统一转换为小写。
        :type DatabaseName: str
        :param _Comment: 数据库描述信息，长度 0~500。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _Properties: 数据库属性列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param _Location: 数据库cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        """
        self._DatabaseName = None
        self._Comment = None
        self._Properties = None
        self._Location = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._Comment = params.get("Comment")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseResponseInfo(AbstractModel):
    """数据库对象

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名称。
        :type DatabaseName: str
        :param _Comment: 数据库描述信息，长度 0~256。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _Properties: 允许针对数据库的属性元数据信息进行指定。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param _CreateTime: 数据库创建时间戳，单位：s。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifiedTime: 数据库更新时间戳，单位：s。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _Location: cos存储路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param _UserAlias: 建库用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param _UserSubUin: 建库用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSubUin: str
        :param _GovernPolicy: 数据治理配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type GovernPolicy: :class:`tencentcloud.dlc.v20210125.models.DataGovernPolicy`
        :param _DatabaseId: 数据库ID（无效字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseId: str
        """
        self._DatabaseName = None
        self._Comment = None
        self._Properties = None
        self._CreateTime = None
        self._ModifiedTime = None
        self._Location = None
        self._UserAlias = None
        self._UserSubUin = None
        self._GovernPolicy = None
        self._DatabaseId = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def UserSubUin(self):
        return self._UserSubUin

    @UserSubUin.setter
    def UserSubUin(self, UserSubUin):
        self._UserSubUin = UserSubUin

    @property
    def GovernPolicy(self):
        return self._GovernPolicy

    @GovernPolicy.setter
    def GovernPolicy(self, GovernPolicy):
        self._GovernPolicy = GovernPolicy

    @property
    def DatabaseId(self):
        return self._DatabaseId

    @DatabaseId.setter
    def DatabaseId(self, DatabaseId):
        self._DatabaseId = DatabaseId


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._Comment = params.get("Comment")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._Location = params.get("Location")
        self._UserAlias = params.get("UserAlias")
        self._UserSubUin = params.get("UserSubUin")
        if params.get("GovernPolicy") is not None:
            self._GovernPolicy = DataGovernPolicy()
            self._GovernPolicy._deserialize(params.get("GovernPolicy"))
        self._DatabaseId = params.get("DatabaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasourceConnectionConfig(AbstractModel):
    """数据源属性

    """

    def __init__(self):
        r"""
        :param _Mysql: Mysql数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Mysql: :class:`tencentcloud.dlc.v20210125.models.MysqlInfo`
        :param _Hive: Hive数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Hive: :class:`tencentcloud.dlc.v20210125.models.HiveInfo`
        :param _Kafka: Kafka数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Kafka: :class:`tencentcloud.dlc.v20210125.models.KafkaInfo`
        :param _OtherDatasourceConnection: 其他数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherDatasourceConnection: :class:`tencentcloud.dlc.v20210125.models.OtherDatasourceConnection`
        :param _PostgreSql: PostgreSQL数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type PostgreSql: :class:`tencentcloud.dlc.v20210125.models.DataSourceInfo`
        :param _SqlServer: SQLServer数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlServer: :class:`tencentcloud.dlc.v20210125.models.DataSourceInfo`
        :param _ClickHouse: ClickHouse数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type ClickHouse: :class:`tencentcloud.dlc.v20210125.models.DataSourceInfo`
        :param _Elasticsearch: Elasticsearch数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Elasticsearch: :class:`tencentcloud.dlc.v20210125.models.ElasticsearchInfo`
        :param _TDSQLPostgreSql: TDSQL-PostgreSQL数据源连接的属性
注意：此字段可能返回 null，表示取不到有效值。
        :type TDSQLPostgreSql: :class:`tencentcloud.dlc.v20210125.models.DataSourceInfo`
        """
        self._Mysql = None
        self._Hive = None
        self._Kafka = None
        self._OtherDatasourceConnection = None
        self._PostgreSql = None
        self._SqlServer = None
        self._ClickHouse = None
        self._Elasticsearch = None
        self._TDSQLPostgreSql = None

    @property
    def Mysql(self):
        return self._Mysql

    @Mysql.setter
    def Mysql(self, Mysql):
        self._Mysql = Mysql

    @property
    def Hive(self):
        return self._Hive

    @Hive.setter
    def Hive(self, Hive):
        self._Hive = Hive

    @property
    def Kafka(self):
        return self._Kafka

    @Kafka.setter
    def Kafka(self, Kafka):
        self._Kafka = Kafka

    @property
    def OtherDatasourceConnection(self):
        return self._OtherDatasourceConnection

    @OtherDatasourceConnection.setter
    def OtherDatasourceConnection(self, OtherDatasourceConnection):
        self._OtherDatasourceConnection = OtherDatasourceConnection

    @property
    def PostgreSql(self):
        return self._PostgreSql

    @PostgreSql.setter
    def PostgreSql(self, PostgreSql):
        self._PostgreSql = PostgreSql

    @property
    def SqlServer(self):
        return self._SqlServer

    @SqlServer.setter
    def SqlServer(self, SqlServer):
        self._SqlServer = SqlServer

    @property
    def ClickHouse(self):
        return self._ClickHouse

    @ClickHouse.setter
    def ClickHouse(self, ClickHouse):
        self._ClickHouse = ClickHouse

    @property
    def Elasticsearch(self):
        return self._Elasticsearch

    @Elasticsearch.setter
    def Elasticsearch(self, Elasticsearch):
        self._Elasticsearch = Elasticsearch

    @property
    def TDSQLPostgreSql(self):
        return self._TDSQLPostgreSql

    @TDSQLPostgreSql.setter
    def TDSQLPostgreSql(self, TDSQLPostgreSql):
        self._TDSQLPostgreSql = TDSQLPostgreSql


    def _deserialize(self, params):
        if params.get("Mysql") is not None:
            self._Mysql = MysqlInfo()
            self._Mysql._deserialize(params.get("Mysql"))
        if params.get("Hive") is not None:
            self._Hive = HiveInfo()
            self._Hive._deserialize(params.get("Hive"))
        if params.get("Kafka") is not None:
            self._Kafka = KafkaInfo()
            self._Kafka._deserialize(params.get("Kafka"))
        if params.get("OtherDatasourceConnection") is not None:
            self._OtherDatasourceConnection = OtherDatasourceConnection()
            self._OtherDatasourceConnection._deserialize(params.get("OtherDatasourceConnection"))
        if params.get("PostgreSql") is not None:
            self._PostgreSql = DataSourceInfo()
            self._PostgreSql._deserialize(params.get("PostgreSql"))
        if params.get("SqlServer") is not None:
            self._SqlServer = DataSourceInfo()
            self._SqlServer._deserialize(params.get("SqlServer"))
        if params.get("ClickHouse") is not None:
            self._ClickHouse = DataSourceInfo()
            self._ClickHouse._deserialize(params.get("ClickHouse"))
        if params.get("Elasticsearch") is not None:
            self._Elasticsearch = ElasticsearchInfo()
            self._Elasticsearch._deserialize(params.get("Elasticsearch"))
        if params.get("TDSQLPostgreSql") is not None:
            self._TDSQLPostgreSql = DataSourceInfo()
            self._TDSQLPostgreSql._deserialize(params.get("TDSQLPostgreSql"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasourceConnectionInfo(AbstractModel):
    """数据源信息

    """

    def __init__(self):
        r"""
        :param _Id: 数据源数字Id
        :type Id: int
        :param _DatasourceConnectionId: 数据源字符串Id
        :type DatasourceConnectionId: str
        :param _DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        :param _DatasourceConnectionDesc: 数据源描述
        :type DatasourceConnectionDesc: str
        :param _DatasourceConnectionType: 数据源类型，支持DataLakeCatalog、IcebergCatalog、Result、Mysql、HiveCos、HiveHdfs
        :type DatasourceConnectionType: str
        :param _DatasourceConnectionConfig: 数据源属性
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionConfig: :class:`tencentcloud.dlc.v20210125.models.DatasourceConnectionConfig`
        :param _State: 数据源状态：0（初始化）、1（成功）、-1（已删除）、-2（失败）、-3（删除中）
        :type State: int
        :param _Region: 地域
        :type Region: str
        :param _AppId: 用户AppId
        :type AppId: str
        :param _CreateTime: 数据源创建时间
        :type CreateTime: str
        :param _UpdateTime: 数据源最近一次更新时间
        :type UpdateTime: str
        :param _Message: 数据源同步失败原因
        :type Message: str
        :param _DataEngines: 数据源绑定的计算引擎信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngines: list of DataEngineInfo
        :param _UserAlias: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param _NetworkConnectionSet: 网络配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConnectionSet: list of NetworkConnection
        :param _ConnectivityState: 连通性状态：0（未测试，默认）、1（正常）、2（失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectivityState: int
        :param _ConnectivityTips: 连通性测试提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectivityTips: str
        """
        self._Id = None
        self._DatasourceConnectionId = None
        self._DatasourceConnectionName = None
        self._DatasourceConnectionDesc = None
        self._DatasourceConnectionType = None
        self._DatasourceConnectionConfig = None
        self._State = None
        self._Region = None
        self._AppId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Message = None
        self._DataEngines = None
        self._UserAlias = None
        self._NetworkConnectionSet = None
        self._ConnectivityState = None
        self._ConnectivityTips = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DatasourceConnectionId(self):
        return self._DatasourceConnectionId

    @DatasourceConnectionId.setter
    def DatasourceConnectionId(self, DatasourceConnectionId):
        self._DatasourceConnectionId = DatasourceConnectionId

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def DatasourceConnectionDesc(self):
        return self._DatasourceConnectionDesc

    @DatasourceConnectionDesc.setter
    def DatasourceConnectionDesc(self, DatasourceConnectionDesc):
        self._DatasourceConnectionDesc = DatasourceConnectionDesc

    @property
    def DatasourceConnectionType(self):
        return self._DatasourceConnectionType

    @DatasourceConnectionType.setter
    def DatasourceConnectionType(self, DatasourceConnectionType):
        self._DatasourceConnectionType = DatasourceConnectionType

    @property
    def DatasourceConnectionConfig(self):
        return self._DatasourceConnectionConfig

    @DatasourceConnectionConfig.setter
    def DatasourceConnectionConfig(self, DatasourceConnectionConfig):
        self._DatasourceConnectionConfig = DatasourceConnectionConfig

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def DataEngines(self):
        return self._DataEngines

    @DataEngines.setter
    def DataEngines(self, DataEngines):
        self._DataEngines = DataEngines

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def NetworkConnectionSet(self):
        return self._NetworkConnectionSet

    @NetworkConnectionSet.setter
    def NetworkConnectionSet(self, NetworkConnectionSet):
        self._NetworkConnectionSet = NetworkConnectionSet

    @property
    def ConnectivityState(self):
        return self._ConnectivityState

    @ConnectivityState.setter
    def ConnectivityState(self, ConnectivityState):
        self._ConnectivityState = ConnectivityState

    @property
    def ConnectivityTips(self):
        return self._ConnectivityTips

    @ConnectivityTips.setter
    def ConnectivityTips(self, ConnectivityTips):
        self._ConnectivityTips = ConnectivityTips


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DatasourceConnectionId = params.get("DatasourceConnectionId")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._DatasourceConnectionDesc = params.get("DatasourceConnectionDesc")
        self._DatasourceConnectionType = params.get("DatasourceConnectionType")
        if params.get("DatasourceConnectionConfig") is not None:
            self._DatasourceConnectionConfig = DatasourceConnectionConfig()
            self._DatasourceConnectionConfig._deserialize(params.get("DatasourceConnectionConfig"))
        self._State = params.get("State")
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Message = params.get("Message")
        if params.get("DataEngines") is not None:
            self._DataEngines = []
            for item in params.get("DataEngines"):
                obj = DataEngineInfo()
                obj._deserialize(item)
                self._DataEngines.append(obj)
        self._UserAlias = params.get("UserAlias")
        if params.get("NetworkConnectionSet") is not None:
            self._NetworkConnectionSet = []
            for item in params.get("NetworkConnectionSet"):
                obj = NetworkConnection()
                obj._deserialize(item)
                self._NetworkConnectionSet.append(obj)
        self._ConnectivityState = params.get("ConnectivityState")
        self._ConnectivityTips = params.get("ConnectivityTips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasourceConnectionLocation(AbstractModel):
    """数据源连接的网络信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 数据连接所在Vpc实例Id，如“vpc-azd4dt1c”。
        :type VpcId: str
        :param _VpcCidrBlock: Vpc的IPv4 CIDR
        :type VpcCidrBlock: str
        :param _SubnetId: 数据连接所在子网的实例Id，如“subnet-bthucmmy”
        :type SubnetId: str
        :param _SubnetCidrBlock: Subnet的IPv4 CIDR
        :type SubnetCidrBlock: str
        """
        self._VpcId = None
        self._VpcCidrBlock = None
        self._SubnetId = None
        self._SubnetCidrBlock = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetCidrBlock(self):
        return self._SubnetCidrBlock

    @SubnetCidrBlock.setter
    def SubnetCidrBlock(self, SubnetCidrBlock):
        self._SubnetCidrBlock = SubnetCidrBlock


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetId = params.get("SubnetId")
        self._SubnetCidrBlock = params.get("SubnetCidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCHDFSBindingProductRequest(AbstractModel):
    """DeleteCHDFSBindingProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPoint: 需要解绑的元数据加速桶名
        :type MountPoint: str
        :param _BucketType: 桶的类型，分为cos和lakefs
        :type BucketType: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _EngineName: 引擎名称，ProductName选择DLC产品时，必传此参数。其他产品可不传
        :type EngineName: str
        :param _VpcInfo: vpc信息，ProductName选择other时，必传此参数
        :type VpcInfo: list of VpcInfo
        """
        self._MountPoint = None
        self._BucketType = None
        self._ProductName = None
        self._EngineName = None
        self._VpcInfo = None

    @property
    def MountPoint(self):
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def BucketType(self):
        return self._BucketType

    @BucketType.setter
    def BucketType(self, BucketType):
        self._BucketType = BucketType

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def EngineName(self):
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def VpcInfo(self):
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo


    def _deserialize(self, params):
        self._MountPoint = params.get("MountPoint")
        self._BucketType = params.get("BucketType")
        self._ProductName = params.get("ProductName")
        self._EngineName = params.get("EngineName")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCHDFSBindingProductResponse(AbstractModel):
    """DeleteCHDFSBindingProduct返回参数结构体

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


class DeleteDataEngineRequest(AbstractModel):
    """DeleteDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineNames: 删除虚拟集群的名称数组
        :type DataEngineNames: list of str
        """
        self._DataEngineNames = None

    @property
    def DataEngineNames(self):
        return self._DataEngineNames

    @DataEngineNames.setter
    def DataEngineNames(self, DataEngineNames):
        self._DataEngineNames = DataEngineNames


    def _deserialize(self, params):
        self._DataEngineNames = params.get("DataEngineNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDataEngineResponse(AbstractModel):
    """DeleteDataEngine返回参数结构体

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


class DeleteNotebookSessionRequest(AbstractModel):
    """DeleteNotebookSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookSessionResponse(AbstractModel):
    """DeleteNotebookSession返回参数结构体

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


class DeleteScriptRequest(AbstractModel):
    """DeleteScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScriptIds: 脚本id，其可以通过DescribeScripts接口提取
        :type ScriptIds: list of str
        """
        self._ScriptIds = None

    @property
    def ScriptIds(self):
        return self._ScriptIds

    @ScriptIds.setter
    def ScriptIds(self, ScriptIds):
        self._ScriptIds = ScriptIds


    def _deserialize(self, params):
        self._ScriptIds = params.get("ScriptIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScriptResponse(AbstractModel):
    """DeleteScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScriptsAffected: 删除的脚本数量
        :type ScriptsAffected: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScriptsAffected = None
        self._RequestId = None

    @property
    def ScriptsAffected(self):
        return self._ScriptsAffected

    @ScriptsAffected.setter
    def ScriptsAffected(self, ScriptsAffected):
        self._ScriptsAffected = ScriptsAffected

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScriptsAffected = params.get("ScriptsAffected")
        self._RequestId = params.get("RequestId")


class DeleteSparkAppRequest(AbstractModel):
    """DeleteSparkApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: spark作业名
        :type AppName: str
        """
        self._AppName = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSparkAppResponse(AbstractModel):
    """DeleteSparkApp返回参数结构体

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


class DeleteThirdPartyAccessUserRequest(AbstractModel):
    """DeleteThirdPartyAccessUser请求参数结构体

    """


class DeleteThirdPartyAccessUserResponse(AbstractModel):
    """DeleteThirdPartyAccessUser返回参数结构体

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


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIds: 需要删除的用户的Id
        :type UserIds: list of str
        """
        self._UserIds = None

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

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


class DeleteUsersFromWorkGroupRequest(AbstractModel):
    """DeleteUsersFromWorkGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AddInfo: 要删除的用户信息
        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.UserIdSetOfWorkGroupId`
        """
        self._AddInfo = None

    @property
    def AddInfo(self):
        return self._AddInfo

    @AddInfo.setter
    def AddInfo(self, AddInfo):
        self._AddInfo = AddInfo


    def _deserialize(self, params):
        if params.get("AddInfo") is not None:
            self._AddInfo = UserIdSetOfWorkGroupId()
            self._AddInfo._deserialize(params.get("AddInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersFromWorkGroupResponse(AbstractModel):
    """DeleteUsersFromWorkGroup返回参数结构体

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


class DeleteWorkGroupRequest(AbstractModel):
    """DeleteWorkGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupIds: 要删除的工作组Id集合
        :type WorkGroupIds: list of int
        """
        self._WorkGroupIds = None

    @property
    def WorkGroupIds(self):
        return self._WorkGroupIds

    @WorkGroupIds.setter
    def WorkGroupIds(self, WorkGroupIds):
        self._WorkGroupIds = WorkGroupIds


    def _deserialize(self, params):
        self._WorkGroupIds = params.get("WorkGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkGroupResponse(AbstractModel):
    """DeleteWorkGroup返回参数结构体

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


class DescribeAdvancedStoreLocationRequest(AbstractModel):
    """DescribeAdvancedStoreLocation请求参数结构体

    """


class DescribeAdvancedStoreLocationResponse(AbstractModel):
    """DescribeAdvancedStoreLocation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 是否启用高级设置：0-否，1-是
        :type Enable: int
        :param _StoreLocation: 查询结果保存cos路径
        :type StoreLocation: str
        :param _HasLakeFs: 是否有托管存储权限
        :type HasLakeFs: bool
        :param _LakeFsStatus: 托管存储状态，HasLakeFs等于true时，该值才有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type LakeFsStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Enable = None
        self._StoreLocation = None
        self._HasLakeFs = None
        self._LakeFsStatus = None
        self._RequestId = None

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def StoreLocation(self):
        return self._StoreLocation

    @StoreLocation.setter
    def StoreLocation(self, StoreLocation):
        self._StoreLocation = StoreLocation

    @property
    def HasLakeFs(self):
        return self._HasLakeFs

    @HasLakeFs.setter
    def HasLakeFs(self, HasLakeFs):
        self._HasLakeFs = HasLakeFs

    @property
    def LakeFsStatus(self):
        return self._LakeFsStatus

    @LakeFsStatus.setter
    def LakeFsStatus(self, LakeFsStatus):
        self._LakeFsStatus = LakeFsStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._StoreLocation = params.get("StoreLocation")
        self._HasLakeFs = params.get("HasLakeFs")
        self._LakeFsStatus = params.get("LakeFsStatus")
        self._RequestId = params.get("RequestId")


class DescribeDLCCatalogAccessRequest(AbstractModel):
    """DescribeDLCCatalogAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 显示条数
        :type Limit: int
        :param _Offset: 记录数量
        :type Offset: int
        :param _Filter: 过滤条件
        :type Filter: :class:`tencentcloud.dlc.v20210125.models.Filter`
        """
        self._Limit = None
        self._Offset = None
        self._Filter = None

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
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDLCCatalogAccessResponse(AbstractModel):
    """DescribeDLCCatalogAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Rows: DLCCatalog授权列表
        :type Rows: list of DLCCatalogAccess
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
                obj = DLCCatalogAccess()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDMSDatabaseRequest(AbstractModel):
    """DescribeDMSDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 数据库名称
        :type Name: str
        :param _SchemaName: schema名称
        :type SchemaName: str
        :param _Pattern: 匹配规则
        :type Pattern: str
        """
        self._Name = None
        self._SchemaName = None
        self._Pattern = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def Pattern(self):
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SchemaName = params.get("SchemaName")
        self._Pattern = params.get("Pattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDMSDatabaseResponse(AbstractModel):
    """DescribeDMSDatabase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _SchemaName: schema名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param _Location: 存储地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param _Asset: 数据对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._SchemaName = None
        self._Location = None
        self._Asset = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SchemaName = params.get("SchemaName")
        self._Location = params.get("Location")
        if params.get("Asset") is not None:
            self._Asset = Asset()
            self._Asset._deserialize(params.get("Asset"))
        self._RequestId = params.get("RequestId")


class DescribeDMSPartitionsRequest(AbstractModel):
    """DescribeDMSPartitions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名
        :type DatabaseName: str
        :param _TableName: 表名称
        :type TableName: str
        :param _SchemaName: schema名称
        :type SchemaName: str
        :param _Name: 名称
        :type Name: str
        :param _Values: 单个分区名称，精准匹配
        :type Values: list of str
        :param _PartitionNames: 多个分区名称，精准匹配
        :type PartitionNames: list of str
        :param _PartValues: 多个分区字段的匹配，模糊匹配
        :type PartValues: list of str
        :param _Filter: 过滤SQL
        :type Filter: str
        :param _MaxParts: 最大分区数量
        :type MaxParts: int
        :param _Offset: 翻页跳过数量
        :type Offset: int
        :param _Limit: 页面数量
        :type Limit: int
        :param _Expression: 表达式
        :type Expression: str
        """
        self._DatabaseName = None
        self._TableName = None
        self._SchemaName = None
        self._Name = None
        self._Values = None
        self._PartitionNames = None
        self._PartValues = None
        self._Filter = None
        self._MaxParts = None
        self._Offset = None
        self._Limit = None
        self._Expression = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

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

    @property
    def PartitionNames(self):
        return self._PartitionNames

    @PartitionNames.setter
    def PartitionNames(self, PartitionNames):
        self._PartitionNames = PartitionNames

    @property
    def PartValues(self):
        return self._PartValues

    @PartValues.setter
    def PartValues(self, PartValues):
        self._PartValues = PartValues

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def MaxParts(self):
        return self._MaxParts

    @MaxParts.setter
    def MaxParts(self, MaxParts):
        self._MaxParts = MaxParts

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
    def Expression(self):
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._SchemaName = params.get("SchemaName")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._PartitionNames = params.get("PartitionNames")
        self._PartValues = params.get("PartValues")
        self._Filter = params.get("Filter")
        self._MaxParts = params.get("MaxParts")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDMSPartitionsResponse(AbstractModel):
    """DescribeDMSPartitions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 分区信息
        :type Partitions: list of DMSPartition
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Partitions = None
        self._Total = None
        self._RequestId = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDMSTableRequest(AbstractModel):
    """DescribeDMSTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        :param _SchemaName: 数据库schema名称
        :type SchemaName: str
        :param _Name: 表名称
        :type Name: str
        :param _Catalog: 数据目录
        :type Catalog: str
        :param _Keyword: 查询关键词
        :type Keyword: str
        :param _Pattern: 查询模式
        :type Pattern: str
        :param _Type: 表类型
        :type Type: str
        """
        self._DbName = None
        self._SchemaName = None
        self._Name = None
        self._Catalog = None
        self._Keyword = None
        self._Pattern = None
        self._Type = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Pattern(self):
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._SchemaName = params.get("SchemaName")
        self._Name = params.get("Name")
        self._Catalog = params.get("Catalog")
        self._Keyword = params.get("Keyword")
        self._Pattern = params.get("Pattern")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDMSTableResponse(AbstractModel):
    """DescribeDMSTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Asset: 基础对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Asset: :class:`tencentcloud.dlc.v20210125.models.Asset`
        :param _ViewOriginalText: 视图文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewOriginalText: str
        :param _ViewExpandedText: 视图文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewExpandedText: str
        :param _Retention: hive维护版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Retention: int
        :param _Sds: 存储对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Sds: :class:`tencentcloud.dlc.v20210125.models.DMSSds`
        :param _PartitionKeys: 分区列
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionKeys: list of DMSColumn
        :param _Partitions: 分区
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of DMSPartition
        :param _Type: 表类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _DbName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param _SchemaName: Schame名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param _StorageSize: 存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSize: int
        :param _RecordCount: 记录数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCount: int
        :param _LifeTime: 生命周期
注意：此字段可能返回 null，表示取不到有效值。
        :type LifeTime: int
        :param _LastAccessTime: 最后访问时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastAccessTime: str
        :param _DataUpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUpdateTime: str
        :param _StructUpdateTime: 结构更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StructUpdateTime: str
        :param _Columns: 列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of DMSColumn
        :param _Name: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Asset = None
        self._ViewOriginalText = None
        self._ViewExpandedText = None
        self._Retention = None
        self._Sds = None
        self._PartitionKeys = None
        self._Partitions = None
        self._Type = None
        self._DbName = None
        self._SchemaName = None
        self._StorageSize = None
        self._RecordCount = None
        self._LifeTime = None
        self._LastAccessTime = None
        self._DataUpdateTime = None
        self._StructUpdateTime = None
        self._Columns = None
        self._Name = None
        self._RequestId = None

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def ViewOriginalText(self):
        return self._ViewOriginalText

    @ViewOriginalText.setter
    def ViewOriginalText(self, ViewOriginalText):
        self._ViewOriginalText = ViewOriginalText

    @property
    def ViewExpandedText(self):
        return self._ViewExpandedText

    @ViewExpandedText.setter
    def ViewExpandedText(self, ViewExpandedText):
        self._ViewExpandedText = ViewExpandedText

    @property
    def Retention(self):
        return self._Retention

    @Retention.setter
    def Retention(self, Retention):
        self._Retention = Retention

    @property
    def Sds(self):
        return self._Sds

    @Sds.setter
    def Sds(self, Sds):
        self._Sds = Sds

    @property
    def PartitionKeys(self):
        return self._PartitionKeys

    @PartitionKeys.setter
    def PartitionKeys(self, PartitionKeys):
        self._PartitionKeys = PartitionKeys

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def StorageSize(self):
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def LifeTime(self):
        return self._LifeTime

    @LifeTime.setter
    def LifeTime(self, LifeTime):
        self._LifeTime = LifeTime

    @property
    def LastAccessTime(self):
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def DataUpdateTime(self):
        return self._DataUpdateTime

    @DataUpdateTime.setter
    def DataUpdateTime(self, DataUpdateTime):
        self._DataUpdateTime = DataUpdateTime

    @property
    def StructUpdateTime(self):
        return self._StructUpdateTime

    @StructUpdateTime.setter
    def StructUpdateTime(self, StructUpdateTime):
        self._StructUpdateTime = StructUpdateTime

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Asset") is not None:
            self._Asset = Asset()
            self._Asset._deserialize(params.get("Asset"))
        self._ViewOriginalText = params.get("ViewOriginalText")
        self._ViewExpandedText = params.get("ViewExpandedText")
        self._Retention = params.get("Retention")
        if params.get("Sds") is not None:
            self._Sds = DMSSds()
            self._Sds._deserialize(params.get("Sds"))
        if params.get("PartitionKeys") is not None:
            self._PartitionKeys = []
            for item in params.get("PartitionKeys"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._PartitionKeys.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = DMSPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._Type = params.get("Type")
        self._DbName = params.get("DbName")
        self._SchemaName = params.get("SchemaName")
        self._StorageSize = params.get("StorageSize")
        self._RecordCount = params.get("RecordCount")
        self._LifeTime = params.get("LifeTime")
        self._LastAccessTime = params.get("LastAccessTime")
        self._DataUpdateTime = params.get("DataUpdateTime")
        self._StructUpdateTime = params.get("StructUpdateTime")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = DMSColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._Name = params.get("Name")
        self._RequestId = params.get("RequestId")


class DescribeDMSTablesRequest(AbstractModel):
    """DescribeDMSTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        :param _SchemaName: 数据库schema名称
        :type SchemaName: str
        :param _Name: 表名称
        :type Name: str
        :param _Catalog: 数据目录
        :type Catalog: str
        :param _Keyword: 查询关键词
        :type Keyword: str
        :param _Pattern: 查询模式
        :type Pattern: str
        :param _Type: 表类型
        :type Type: str
        :param _StartTime: 筛选参数：更新开始时间
        :type StartTime: str
        :param _EndTime: 筛选参数：更新结束时间
        :type EndTime: str
        :param _Limit: 分页参数
        :type Limit: int
        :param _Offset: 分页参数
        :type Offset: int
        :param _Sort: 排序字段：create_time：创建时间
        :type Sort: str
        :param _Asc: 排序字段：true：升序（默认），false：降序
        :type Asc: bool
        """
        self._DbName = None
        self._SchemaName = None
        self._Name = None
        self._Catalog = None
        self._Keyword = None
        self._Pattern = None
        self._Type = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Sort = None
        self._Asc = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Pattern(self):
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._SchemaName = params.get("SchemaName")
        self._Name = params.get("Name")
        self._Catalog = params.get("Catalog")
        self._Keyword = params.get("Keyword")
        self._Pattern = params.get("Pattern")
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Sort = params.get("Sort")
        self._Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDMSTablesResponse(AbstractModel):
    """DescribeDMSTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableList: DMS元数据列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TableList: list of DMSTableInfo
        :param _TotalCount: 统计值
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TableList(self):
        return self._TableList

    @TableList.setter
    def TableList(self, TableList):
        self._TableList = TableList

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
        if params.get("TableList") is not None:
            self._TableList = []
            for item in params.get("TableList"):
                obj = DMSTableInfo()
                obj._deserialize(item)
                self._TableList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDataEngineEventsRequest(AbstractModel):
    """DescribeDataEngineEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: 虚拟集群名称
        :type DataEngineName: str
        :param _Limit: 返回数量，默认为10，最大为100
        :type Limit: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        """
        self._DataEngineName = None
        self._Limit = None
        self._Offset = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

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


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEngineEventsResponse(AbstractModel):
    """DescribeDataEngineEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 事件详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of HouseEventsInfo
        :param _Page: 分页号
注意：此字段可能返回 null，表示取不到有效值。
        :type Page: int
        :param _Size: 分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _TotalPages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPages: int
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._Page = None
        self._Size = None
        self._TotalPages = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def TotalPages(self):
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

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
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = HouseEventsInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._Page = params.get("Page")
        self._Size = params.get("Size")
        self._TotalPages = params.get("TotalPages")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDataEngineImageVersionsRequest(AbstractModel):
    """DescribeDataEngineImageVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineType: 引擎类型：SQL、SparkBatch、StandardSpark、StandardPresto
        :type EngineType: str
        """
        self._EngineType = None

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEngineImageVersionsResponse(AbstractModel):
    """DescribeDataEngineImageVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageParentVersions: 集群大版本镜像信息列表
        :type ImageParentVersions: list of DataEngineImageVersion
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageParentVersions = None
        self._Total = None
        self._RequestId = None

    @property
    def ImageParentVersions(self):
        return self._ImageParentVersions

    @ImageParentVersions.setter
    def ImageParentVersions(self, ImageParentVersions):
        self._ImageParentVersions = ImageParentVersions

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageParentVersions") is not None:
            self._ImageParentVersions = []
            for item in params.get("ImageParentVersions"):
                obj = DataEngineImageVersion()
                obj._deserialize(item)
                self._ImageParentVersions.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDataEnginePythonSparkImagesRequest(AbstractModel):
    """DescribeDataEnginePythonSparkImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChildImageVersionId: 集群镜像小版本ID
        :type ChildImageVersionId: str
        """
        self._ChildImageVersionId = None

    @property
    def ChildImageVersionId(self):
        return self._ChildImageVersionId

    @ChildImageVersionId.setter
    def ChildImageVersionId(self, ChildImageVersionId):
        self._ChildImageVersionId = ChildImageVersionId


    def _deserialize(self, params):
        self._ChildImageVersionId = params.get("ChildImageVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEnginePythonSparkImagesResponse(AbstractModel):
    """DescribeDataEnginePythonSparkImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PythonSparkImages: PYSPARK镜像信息列表
        :type PythonSparkImages: list of PythonSparkImage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PythonSparkImages = None
        self._RequestId = None

    @property
    def PythonSparkImages(self):
        return self._PythonSparkImages

    @PythonSparkImages.setter
    def PythonSparkImages(self, PythonSparkImages):
        self._PythonSparkImages = PythonSparkImages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PythonSparkImages") is not None:
            self._PythonSparkImages = []
            for item in params.get("PythonSparkImages"):
                obj = PythonSparkImage()
                obj._deserialize(item)
                self._PythonSparkImages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDataEngineRequest(AbstractModel):
    """DescribeDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: House名称
        :type DataEngineName: str
        """
        self._DataEngineName = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEngineResponse(AbstractModel):
    """DescribeDataEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngine: 数据引擎详细信息
        :type DataEngine: :class:`tencentcloud.dlc.v20210125.models.DataEngineInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataEngine = None
        self._RequestId = None

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataEngine") is not None:
            self._DataEngine = DataEngineInfo()
            self._DataEngine._deserialize(params.get("DataEngine"))
        self._RequestId = params.get("RequestId")


class DescribeDataEnginesRequest(AbstractModel):
    """DescribeDataEngines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤类型，支持如下的过滤类型，传参Name应为以下其中一个, data-engine-name - String（数据引擎名称）：engine-type - String（引擎类型：spark：spark 引擎，presto：presto引擎），state - String (数据引擎状态 -2已删除 -1失败 0初始化中 1挂起 2运行中 3准备删除 4删除中) ， mode - String（计费模式 0共享模式 1按量计费 2包年包月） ， create-time - String（创建时间，10位时间戳） message - String （描述信息），cluster-type - String (集群资源类型 spark_private/presto_private/presto_cu/spark_cu/kyuubi_cu)，engine-id - String（数据引擎ID），key-word - String（数据引擎名称或集群资源类型或描述信息模糊搜索），engine-exec-type - String（引擎执行任务类型，SQL/BATCH），engine-network-id - String（引擎网络Id）
        :type Filters: list of Filter
        :param _SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param _Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc。
        :type Sorting: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _DatasourceConnectionName: 已废弃，请使用DatasourceConnectionNameSet
        :type DatasourceConnectionName: str
        :param _ExcludePublicEngine: 是否不返回共享引擎，true不返回共享引擎，false可以返回共享引擎
        :type ExcludePublicEngine: bool
        :param _AccessTypes: 参数应该为引擎权限类型，有效类型："USE", "MODIFY", "OPERATE", "MONITOR", "DELETE"
        :type AccessTypes: list of str
        :param _EngineExecType: 引擎执行任务类型，有效值：SQL/BATCH，默认为SQL
        :type EngineExecType: str
        :param _EngineType: 引擎类型，有效值：spark/presto/kyuubi，为空时默认获取非kyuubi引擎（网关引擎）
        :type EngineType: str
        :param _DatasourceConnectionNameSet: 网络配置列表，若传入该参数，则返回网络配置关联的计算引擎
        :type DatasourceConnectionNameSet: list of str
        :param _EngineGeneration: 引擎版本，有效值：Native/SuperSQL，为空时默认获取SuperSQL引擎
        :type EngineGeneration: str
        :param _EngineTypeDetail: 引擎类型，支持：SparkSQL、SparkBatch、PrestoSQL、Kyuubi
        :type EngineTypeDetail: str
        """
        self._Offset = None
        self._Filters = None
        self._SortBy = None
        self._Sorting = None
        self._Limit = None
        self._DatasourceConnectionName = None
        self._ExcludePublicEngine = None
        self._AccessTypes = None
        self._EngineExecType = None
        self._EngineType = None
        self._DatasourceConnectionNameSet = None
        self._EngineGeneration = None
        self._EngineTypeDetail = None

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

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def ExcludePublicEngine(self):
        return self._ExcludePublicEngine

    @ExcludePublicEngine.setter
    def ExcludePublicEngine(self, ExcludePublicEngine):
        self._ExcludePublicEngine = ExcludePublicEngine

    @property
    def AccessTypes(self):
        return self._AccessTypes

    @AccessTypes.setter
    def AccessTypes(self, AccessTypes):
        self._AccessTypes = AccessTypes

    @property
    def EngineExecType(self):
        return self._EngineExecType

    @EngineExecType.setter
    def EngineExecType(self, EngineExecType):
        self._EngineExecType = EngineExecType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def DatasourceConnectionNameSet(self):
        return self._DatasourceConnectionNameSet

    @DatasourceConnectionNameSet.setter
    def DatasourceConnectionNameSet(self, DatasourceConnectionNameSet):
        self._DatasourceConnectionNameSet = DatasourceConnectionNameSet

    @property
    def EngineGeneration(self):
        return self._EngineGeneration

    @EngineGeneration.setter
    def EngineGeneration(self, EngineGeneration):
        self._EngineGeneration = EngineGeneration

    @property
    def EngineTypeDetail(self):
        return self._EngineTypeDetail

    @EngineTypeDetail.setter
    def EngineTypeDetail(self, EngineTypeDetail):
        self._EngineTypeDetail = EngineTypeDetail


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        self._Limit = params.get("Limit")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._ExcludePublicEngine = params.get("ExcludePublicEngine")
        self._AccessTypes = params.get("AccessTypes")
        self._EngineExecType = params.get("EngineExecType")
        self._EngineType = params.get("EngineType")
        self._DatasourceConnectionNameSet = params.get("DatasourceConnectionNameSet")
        self._EngineGeneration = params.get("EngineGeneration")
        self._EngineTypeDetail = params.get("EngineTypeDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEnginesResponse(AbstractModel):
    """DescribeDataEngines返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngines: 数据引擎列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngines: list of DataEngineInfo
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataEngines = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DataEngines(self):
        return self._DataEngines

    @DataEngines.setter
    def DataEngines(self, DataEngines):
        self._DataEngines = DataEngines

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
        if params.get("DataEngines") is not None:
            self._DataEngines = []
            for item in params.get("DataEngines"):
                obj = DataEngineInfo()
                obj._deserialize(item)
                self._DataEngines.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDataEnginesScaleDetailRequest(AbstractModel):
    """DescribeDataEnginesScaleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineNames: 引擎名称列表
        :type DataEngineNames: list of str
        :param _StartTime: 开始时间，时间格式：yyyy-MM-dd HH:mm:ss，最长查询一个月内的记录
        :type StartTime: str
        :param _EndTime: 结束时间，时间格式：yyyy-MM-dd HH:mm:ss，最长查询一个月内的记录
        :type EndTime: str
        """
        self._DataEngineNames = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DataEngineNames(self):
        return self._DataEngineNames

    @DataEngineNames.setter
    def DataEngineNames(self, DataEngineNames):
        self._DataEngineNames = DataEngineNames

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
        self._DataEngineNames = params.get("DataEngineNames")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEnginesScaleDetailResponse(AbstractModel):
    """DescribeDataEnginesScaleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Scales: 引擎规格统计详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Scales: list of DataEngineScaleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Scales = None
        self._RequestId = None

    @property
    def Scales(self):
        return self._Scales

    @Scales.setter
    def Scales(self, Scales):
        self._Scales = Scales

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Scales") is not None:
            self._Scales = []
            for item in params.get("Scales"):
                obj = DataEngineScaleInfo()
                obj._deserialize(item)
                self._Scales.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始，默认为0。
        :type Offset: int
        :param _KeyWord: 模糊匹配，库名关键字。
        :type KeyWord: str
        :param _DatasourceConnectionName: 数据源唯名称，该名称可以通过DescribeDatasourceConnection接口查询到。默认为DataLakeCatalog
        :type DatasourceConnectionName: str
        :param _Sort: 排序字段，CreateTime：创建时间，Name：数据库名称
        :type Sort: str
        :param _Asc: 排序类型：false：降序（默认）、true：升序
        :type Asc: bool
        """
        self._Limit = None
        self._Offset = None
        self._KeyWord = None
        self._DatasourceConnectionName = None
        self._Sort = None
        self._Asc = None

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
    def KeyWord(self):
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._KeyWord = params.get("KeyWord")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._Sort = params.get("Sort")
        self._Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseList: 数据库对象列表。
        :type DatabaseList: list of DatabaseResponseInfo
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DatabaseList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DatabaseList(self):
        return self._DatabaseList

    @DatabaseList.setter
    def DatabaseList(self, DatabaseList):
        self._DatabaseList = DatabaseList

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
        if params.get("DatabaseList") is not None:
            self._DatabaseList = []
            for item in params.get("DatabaseList"):
                obj = DatabaseResponseInfo()
                obj._deserialize(item)
                self._DatabaseList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDatasourceConnectionRequest(AbstractModel):
    """DescribeDatasourceConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasourceConnectionIds: 连接ID列表，指定要查询的连接ID
        :type DatasourceConnectionIds: list of str
        :param _Filters: 过滤条件，当前支持的过滤键为：DatasourceConnectionName（数据源连接名）。
DatasourceConnectionType   （数据源连接连接类型）
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大值100
        :type Limit: int
        :param _SortBy: 排序字段，支持如下字段类型，create-time（默认，创建时间）、update-time（更新时间）
        :type SortBy: str
        :param _Sorting: 排序方式，desc表示正序，asc表示反序， 默认为desc
        :type Sorting: str
        :param _StartTime: 筛选字段：起始时间
        :type StartTime: str
        :param _EndTime: 筛选字段：截止时间
        :type EndTime: str
        :param _DatasourceConnectionNames: 连接名称列表，指定要查询的连接名称
        :type DatasourceConnectionNames: list of str
        :param _DatasourceConnectionTypes: 连接类型，支持Mysql/HiveCos/Kafka/DataLakeCatalog
        :type DatasourceConnectionTypes: list of str
        :param _HiveVersion: 返回指定hive版本的数据源，该参数指定后，会过滤掉该参数指定版本以外的hive数据源，非hive数据源正常返回
        :type HiveVersion: list of str
        """
        self._DatasourceConnectionIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._SortBy = None
        self._Sorting = None
        self._StartTime = None
        self._EndTime = None
        self._DatasourceConnectionNames = None
        self._DatasourceConnectionTypes = None
        self._HiveVersion = None

    @property
    def DatasourceConnectionIds(self):
        return self._DatasourceConnectionIds

    @DatasourceConnectionIds.setter
    def DatasourceConnectionIds(self, DatasourceConnectionIds):
        self._DatasourceConnectionIds = DatasourceConnectionIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

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

    @property
    def DatasourceConnectionNames(self):
        return self._DatasourceConnectionNames

    @DatasourceConnectionNames.setter
    def DatasourceConnectionNames(self, DatasourceConnectionNames):
        self._DatasourceConnectionNames = DatasourceConnectionNames

    @property
    def DatasourceConnectionTypes(self):
        return self._DatasourceConnectionTypes

    @DatasourceConnectionTypes.setter
    def DatasourceConnectionTypes(self, DatasourceConnectionTypes):
        self._DatasourceConnectionTypes = DatasourceConnectionTypes

    @property
    def HiveVersion(self):
        return self._HiveVersion

    @HiveVersion.setter
    def HiveVersion(self, HiveVersion):
        self._HiveVersion = HiveVersion


    def _deserialize(self, params):
        self._DatasourceConnectionIds = params.get("DatasourceConnectionIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DatasourceConnectionNames = params.get("DatasourceConnectionNames")
        self._DatasourceConnectionTypes = params.get("DatasourceConnectionTypes")
        self._HiveVersion = params.get("HiveVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasourceConnectionResponse(AbstractModel):
    """DescribeDatasourceConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据连接总数
        :type TotalCount: int
        :param _ConnectionSet: 数据连接对象集合
        :type ConnectionSet: list of DatasourceConnectionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConnectionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConnectionSet(self):
        return self._ConnectionSet

    @ConnectionSet.setter
    def ConnectionSet(self, ConnectionSet):
        self._ConnectionSet = ConnectionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConnectionSet") is not None:
            self._ConnectionSet = []
            for item in params.get("ConnectionSet"):
                obj = DatasourceConnectionInfo()
                obj._deserialize(item)
                self._ConnectionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEngineUsageInfoRequest(AbstractModel):
    """DescribeEngineUsageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 数据引擎ID
        :type DataEngineId: str
        """
        self._DataEngineId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEngineUsageInfoResponse(AbstractModel):
    """DescribeEngineUsageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 集群总规格
        :type Total: int
        :param _Used: 已占用集群规格
        :type Used: int
        :param _Available: 剩余集群规格
        :type Available: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Used = None
        self._Available = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._Available = params.get("Available")
        self._RequestId = params.get("RequestId")


class DescribeForbiddenTableProRequest(AbstractModel):
    """DescribeForbiddenTablePro请求参数结构体

    """


class DescribeForbiddenTableProResponse(AbstractModel):
    """DescribeForbiddenTablePro返回参数结构体

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


class DescribeLakeFsDirSummaryRequest(AbstractModel):
    """DescribeLakeFsDirSummary请求参数结构体

    """


class DescribeLakeFsDirSummaryResponse(AbstractModel):
    """DescribeLakeFsDirSummary返回参数结构体

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


class DescribeLakeFsInfoRequest(AbstractModel):
    """DescribeLakeFsInfo请求参数结构体

    """


class DescribeLakeFsInfoResponse(AbstractModel):
    """DescribeLakeFsInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LakeFsInfos: 托管存储信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LakeFsInfos: list of LakeFsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LakeFsInfos = None
        self._RequestId = None

    @property
    def LakeFsInfos(self):
        return self._LakeFsInfos

    @LakeFsInfos.setter
    def LakeFsInfos(self, LakeFsInfos):
        self._LakeFsInfos = LakeFsInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LakeFsInfos") is not None:
            self._LakeFsInfos = []
            for item in params.get("LakeFsInfos"):
                obj = LakeFsInfo()
                obj._deserialize(item)
                self._LakeFsInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLakeFsTaskResultRequest(AbstractModel):
    """DescribeLakeFsTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FsPath: 需要访问的任务结果路径
        :type FsPath: str
        """
        self._FsPath = None

    @property
    def FsPath(self):
        return self._FsPath

    @FsPath.setter
    def FsPath(self, FsPath):
        self._FsPath = FsPath


    def _deserialize(self, params):
        self._FsPath = params.get("FsPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLakeFsTaskResultResponse(AbstractModel):
    """DescribeLakeFsTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 路径的访问实例
        :type AccessToken: :class:`tencentcloud.dlc.v20210125.models.LakeFileSystemToken`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessToken = None
        self._RequestId = None

    @property
    def AccessToken(self):
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessToken") is not None:
            self._AccessToken = LakeFileSystemToken()
            self._AccessToken._deserialize(params.get("AccessToken"))
        self._RequestId = params.get("RequestId")


class DescribeNotebookSessionLogRequest(AbstractModel):
    """DescribeNotebookSessionLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _Limit: 分页参数，默认200
        :type Limit: int
        :param _Offset: 分页参数，默认0
        :type Offset: int
        """
        self._SessionId = None
        self._Limit = None
        self._Offset = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionLogResponse(AbstractModel):
    """DescribeNotebookSessionLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Logs: 日志信息，默认获取最新的200条
        :type Logs: list of str
        :param _Limit: 分页参数，默认200
        :type Limit: int
        :param _Offset: 分页参数，默认0
        :type Offset: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Logs = None
        self._Limit = None
        self._Offset = None
        self._RequestId = None

    @property
    def Logs(self):
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Logs = params.get("Logs")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RequestId = params.get("RequestId")


class DescribeNotebookSessionRequest(AbstractModel):
    """DescribeNotebookSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionResponse(AbstractModel):
    """DescribeNotebookSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Session: Session详情信息
        :type Session: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Session") is not None:
            self._Session = NotebookSessionInfo()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class DescribeNotebookSessionStatementRequest(AbstractModel):
    """DescribeNotebookSessionStatement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _StatementId: Session Statement唯一标识
        :type StatementId: str
        :param _TaskId: 任务唯一标识
        :type TaskId: str
        """
        self._SessionId = None
        self._StatementId = None
        self._TaskId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def StatementId(self):
        return self._StatementId

    @StatementId.setter
    def StatementId(self, StatementId):
        self._StatementId = StatementId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._StatementId = params.get("StatementId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionStatementResponse(AbstractModel):
    """DescribeNotebookSessionStatement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookSessionStatement: Session Statement详情
        :type NotebookSessionStatement: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionStatementInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookSessionStatement = None
        self._RequestId = None

    @property
    def NotebookSessionStatement(self):
        return self._NotebookSessionStatement

    @NotebookSessionStatement.setter
    def NotebookSessionStatement(self, NotebookSessionStatement):
        self._NotebookSessionStatement = NotebookSessionStatement

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotebookSessionStatement") is not None:
            self._NotebookSessionStatement = NotebookSessionStatementInfo()
            self._NotebookSessionStatement._deserialize(params.get("NotebookSessionStatement"))
        self._RequestId = params.get("RequestId")


class DescribeNotebookSessionStatementSqlResultRequest(AbstractModel):
    """DescribeNotebookSessionStatementSqlResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一ID
        :type TaskId: str
        :param _MaxResults: 返回结果的最大行数，范围0~1000，默认为1000.
        :type MaxResults: int
        :param _NextToken: 上一次请求响应返回的分页信息。第一次可以不带，从头开始返回数据，每次返回MaxResults字段设置的数据量。
        :type NextToken: str
        """
        self._TaskId = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionStatementSqlResultResponse(AbstractModel):
    """DescribeNotebookSessionStatementSqlResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _ResultSet: 结果数据
        :type ResultSet: str
        :param _ResultSchema: schema
        :type ResultSchema: list of Column
        :param _NextToken: 分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _OutputPath: 存储结果地址
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputPath: str
        :param _UseTime: 引擎计算耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type UseTime: int
        :param _AffectRows: 结果条数
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectRows: int
        :param _DataAmount: 数据扫描量
注意：此字段可能返回 null，表示取不到有效值。
        :type DataAmount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ResultSet = None
        self._ResultSchema = None
        self._NextToken = None
        self._OutputPath = None
        self._UseTime = None
        self._AffectRows = None
        self._DataAmount = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ResultSet(self):
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def ResultSchema(self):
        return self._ResultSchema

    @ResultSchema.setter
    def ResultSchema(self, ResultSchema):
        self._ResultSchema = ResultSchema

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def OutputPath(self):
        return self._OutputPath

    @OutputPath.setter
    def OutputPath(self, OutputPath):
        self._OutputPath = OutputPath

    @property
    def UseTime(self):
        return self._UseTime

    @UseTime.setter
    def UseTime(self, UseTime):
        self._UseTime = UseTime

    @property
    def AffectRows(self):
        return self._AffectRows

    @AffectRows.setter
    def AffectRows(self, AffectRows):
        self._AffectRows = AffectRows

    @property
    def DataAmount(self):
        return self._DataAmount

    @DataAmount.setter
    def DataAmount(self, DataAmount):
        self._DataAmount = DataAmount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ResultSet = params.get("ResultSet")
        if params.get("ResultSchema") is not None:
            self._ResultSchema = []
            for item in params.get("ResultSchema"):
                obj = Column()
                obj._deserialize(item)
                self._ResultSchema.append(obj)
        self._NextToken = params.get("NextToken")
        self._OutputPath = params.get("OutputPath")
        self._UseTime = params.get("UseTime")
        self._AffectRows = params.get("AffectRows")
        self._DataAmount = params.get("DataAmount")
        self._RequestId = params.get("RequestId")


class DescribeNotebookSessionStatementsRequest(AbstractModel):
    """DescribeNotebookSessionStatements请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _BatchId: 批任务id
        :type BatchId: str
        """
        self._SessionId = None
        self._BatchId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionStatementsResponse(AbstractModel):
    """DescribeNotebookSessionStatements返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookSessionStatements: Session Statement详情
        :type NotebookSessionStatements: :class:`tencentcloud.dlc.v20210125.models.NotebookSessionStatementBatchInformation`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookSessionStatements = None
        self._RequestId = None

    @property
    def NotebookSessionStatements(self):
        return self._NotebookSessionStatements

    @NotebookSessionStatements.setter
    def NotebookSessionStatements(self, NotebookSessionStatements):
        self._NotebookSessionStatements = NotebookSessionStatements

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotebookSessionStatements") is not None:
            self._NotebookSessionStatements = NotebookSessionStatementBatchInformation()
            self._NotebookSessionStatements._deserialize(params.get("NotebookSessionStatements"))
        self._RequestId = params.get("RequestId")


class DescribeNotebookSessionsRequest(AbstractModel):
    """DescribeNotebookSessions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: DLC Spark作业引擎名称
        :type DataEngineName: str
        :param _State: Session状态，包含：not_started（未启动）、starting（已启动）、idle（等待输入）、busy(正在运行statement)、shutting_down（停止）、error（异常）、dead（已退出）、killed（被杀死）、success（正常停止）
        :type State: list of str
        :param _SortFields: 排序字段（默认按创建时间）
        :type SortFields: list of str
        :param _Asc: 排序字段：true：升序、false：降序（默认）
        :type Asc: bool
        :param _Limit: 分页参数，默认10
        :type Limit: int
        :param _Offset: 分页参数，默认0
        :type Offset: int
        """
        self._DataEngineName = None
        self._State = None
        self._SortFields = None
        self._Asc = None
        self._Limit = None
        self._Offset = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def SortFields(self):
        return self._SortFields

    @SortFields.setter
    def SortFields(self, SortFields):
        self._SortFields = SortFields

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

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


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._State = params.get("State")
        self._SortFields = params.get("SortFields")
        self._Asc = params.get("Asc")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookSessionsResponse(AbstractModel):
    """DescribeNotebookSessions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalElements: session总数量
        :type TotalElements: int
        :param _TotalPages: 总页数
        :type TotalPages: int
        :param _Page: 当前页码
        :type Page: int
        :param _Size: 当前页数量
        :type Size: int
        :param _Sessions: session列表信息
        :type Sessions: list of NotebookSessions
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalElements = None
        self._TotalPages = None
        self._Page = None
        self._Size = None
        self._Sessions = None
        self._RequestId = None

    @property
    def TotalElements(self):
        return self._TotalElements

    @TotalElements.setter
    def TotalElements(self, TotalElements):
        self._TotalElements = TotalElements

    @property
    def TotalPages(self):
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Sessions(self):
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalElements = params.get("TotalElements")
        self._TotalPages = params.get("TotalPages")
        self._Page = params.get("Page")
        self._Size = params.get("Size")
        if params.get("Sessions") is not None:
            self._Sessions = []
            for item in params.get("Sessions"):
                obj = NotebookSessions()
                obj._deserialize(item)
                self._Sessions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOtherCHDFSBindingListRequest(AbstractModel):
    """DescribeOtherCHDFSBindingList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BucketId: 桶名
        :type BucketId: str
        """
        self._BucketId = None

    @property
    def BucketId(self):
        return self._BucketId

    @BucketId.setter
    def BucketId(self, BucketId):
        self._BucketId = BucketId


    def _deserialize(self, params):
        self._BucketId = params.get("BucketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOtherCHDFSBindingListResponse(AbstractModel):
    """DescribeOtherCHDFSBindingList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OtherCHDFSBindingList: 非DLC 产品绑定列表
        :type OtherCHDFSBindingList: list of OtherCHDFSBinding
        :param _Total: 总记录数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OtherCHDFSBindingList = None
        self._Total = None
        self._RequestId = None

    @property
    def OtherCHDFSBindingList(self):
        return self._OtherCHDFSBindingList

    @OtherCHDFSBindingList.setter
    def OtherCHDFSBindingList(self, OtherCHDFSBindingList):
        self._OtherCHDFSBindingList = OtherCHDFSBindingList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OtherCHDFSBindingList") is not None:
            self._OtherCHDFSBindingList = []
            for item in params.get("OtherCHDFSBindingList"):
                obj = OtherCHDFSBinding()
                obj._deserialize(item)
                self._OtherCHDFSBindingList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeResultDownloadRequest(AbstractModel):
    """DescribeResultDownload请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadId: 查询任务Id
        :type DownloadId: str
        """
        self._DownloadId = None

    @property
    def DownloadId(self):
        return self._DownloadId

    @DownloadId.setter
    def DownloadId(self, DownloadId):
        self._DownloadId = DownloadId


    def _deserialize(self, params):
        self._DownloadId = params.get("DownloadId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResultDownloadResponse(AbstractModel):
    """DescribeResultDownload返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Path: 下载文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Status: 任务状态 init | queue | format | compress | success|  timeout | error
        :type Status: str
        :param _Reason: 任务异常原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _SecretId: 临时AK
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretId: str
        :param _SecretKey: 临时SK
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _Token: 临时Token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Path = None
        self._Status = None
        self._Reason = None
        self._SecretId = None
        self._SecretKey = None
        self._Token = None
        self._RequestId = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def SecretId(self):
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class DescribeScriptsRequest(AbstractModel):
    """DescribeScripts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _SortBy: 按字段排序，支持如下字段类型，update-time
        :type SortBy: str
        :param _Sorting: 排序方式，desc表示正序，asc表示反序，默认asc
        :type Sorting: str
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
script-id - String - （过滤条件）script-id取值形如：157de0d1-26b4-4df2-a2d0-b64afc406c25。
script-name-keyword - String - （过滤条件）数据表名称,形如：script-test。
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._SortBy = None
        self._Sorting = None
        self._Filters = None

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
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
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
        


class DescribeScriptsResponse(AbstractModel):
    """DescribeScripts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Scripts: Script列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Scripts: list of Script
        :param _TotalCount: 实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Scripts = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Scripts(self):
        return self._Scripts

    @Scripts.setter
    def Scripts(self, Scripts):
        self._Scripts = Scripts

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
        if params.get("Scripts") is not None:
            self._Scripts = []
            for item in params.get("Scripts"):
                obj = Script()
                obj._deserialize(item)
                self._Scripts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSparkAppJobRequest(AbstractModel):
    """DescribeSparkAppJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: spark作业Id，与JobName同时存在时，JobName无效，JobId与JobName至少存在一个
        :type JobId: str
        :param _JobName: spark作业名
        :type JobName: str
        """
        self._JobId = None
        self._JobName = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkAppJobResponse(AbstractModel):
    """DescribeSparkAppJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Job: spark作业详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.dlc.v20210125.models.SparkJobInfo`
        :param _IsExists: 查询的spark作业是否存在
        :type IsExists: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Job = None
        self._IsExists = None
        self._RequestId = None

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def IsExists(self):
        return self._IsExists

    @IsExists.setter
    def IsExists(self, IsExists):
        self._IsExists = IsExists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = SparkJobInfo()
            self._Job._deserialize(params.get("Job"))
        self._IsExists = params.get("IsExists")
        self._RequestId = params.get("RequestId")


class DescribeSparkAppJobsRequest(AbstractModel):
    """DescribeSparkAppJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SortBy: 返回结果按照该字段排序
        :type SortBy: str
        :param _Sorting: 正序或者倒序，例如：desc
        :type Sorting: str
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一:spark-job-name（作业名称），spark-job-id（作业id），spark-app-type（作业类型，1：批任务，2：流任务，4：SQL作业），user-name（创建人），key-word（作业名称或ID关键词模糊搜索）
        :type Filters: list of Filter
        :param _StartTime: 更新时间起始点，支持格式：yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param _EndTime: 更新时间截止点，支持格式：yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        :param _Offset: 查询列表偏移量, 默认值0
        :type Offset: int
        :param _Limit: 查询列表限制数量, 默认值100
        :type Limit: int
        """
        self._SortBy = None
        self._Sorting = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkAppJobsResponse(AbstractModel):
    """DescribeSparkAppJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SparkAppJobs: spark作业列表详情
        :type SparkAppJobs: list of SparkJobInfo
        :param _TotalCount: spark作业总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SparkAppJobs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SparkAppJobs(self):
        return self._SparkAppJobs

    @SparkAppJobs.setter
    def SparkAppJobs(self, SparkAppJobs):
        self._SparkAppJobs = SparkAppJobs

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
        if params.get("SparkAppJobs") is not None:
            self._SparkAppJobs = []
            for item in params.get("SparkAppJobs"):
                obj = SparkJobInfo()
                obj._deserialize(item)
                self._SparkAppJobs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSparkAppTasksRequest(AbstractModel):
    """DescribeSparkAppTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: spark作业Id
        :type JobId: str
        :param _Offset: 分页查询偏移量
        :type Offset: int
        :param _Limit: 分页查询Limit
        :type Limit: int
        :param _TaskId: 执行实例id
        :type TaskId: str
        :param _StartTime: 更新时间起始点，支持格式：yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param _EndTime: 更新时间截止点，支持格式：yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        :param _Filters: 按照该参数过滤,支持task-state
        :type Filters: list of Filter
        """
        self._JobId = None
        self._Offset = None
        self._Limit = None
        self._TaskId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TaskId = params.get("TaskId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
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
        


class DescribeSparkAppTasksResponse(AbstractModel):
    """DescribeSparkAppTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务结果（该字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TaskResponseInfo`
        :param _TotalCount: 任务总数
        :type TotalCount: int
        :param _SparkAppTasks: 任务结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppTasks: list of TaskResponseInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._TotalCount = None
        self._SparkAppTasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SparkAppTasks(self):
        return self._SparkAppTasks

    @SparkAppTasks.setter
    def SparkAppTasks(self, SparkAppTasks):
        self._SparkAppTasks = SparkAppTasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = TaskResponseInfo()
            self._Tasks._deserialize(params.get("Tasks"))
        self._TotalCount = params.get("TotalCount")
        if params.get("SparkAppTasks") is not None:
            self._SparkAppTasks = []
            for item in params.get("SparkAppTasks"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self._SparkAppTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSparkSessionBatchSQLCostRequest(AbstractModel):
    """DescribeSparkSessionBatchSQLCost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchIds: SparkSQL唯一标识
        :type BatchIds: list of str
        """
        self._BatchIds = None

    @property
    def BatchIds(self):
        return self._BatchIds

    @BatchIds.setter
    def BatchIds(self, BatchIds):
        self._BatchIds = BatchIds


    def _deserialize(self, params):
        self._BatchIds = params.get("BatchIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkSessionBatchSQLCostResponse(AbstractModel):
    """DescribeSparkSessionBatchSQLCost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CostInfo: 任务消耗
注意：此字段可能返回 null，表示取不到有效值。
        :type CostInfo: list of BatchSQLCostInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CostInfo = None
        self._RequestId = None

    @property
    def CostInfo(self):
        return self._CostInfo

    @CostInfo.setter
    def CostInfo(self, CostInfo):
        self._CostInfo = CostInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CostInfo") is not None:
            self._CostInfo = []
            for item in params.get("CostInfo"):
                obj = BatchSQLCostInfo()
                obj._deserialize(item)
                self._CostInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSparkSessionBatchSQLRequest(AbstractModel):
    """DescribeSparkSessionBatchSQL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: SparkSQL唯一标识
        :type BatchId: str
        :param _CustomKey: 用户自定义主键, 若不为空，则按照该值查询
        :type CustomKey: str
        """
        self._BatchId = None
        self._CustomKey = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def CustomKey(self):
        return self._CustomKey

    @CustomKey.setter
    def CustomKey(self, CustomKey):
        self._CustomKey = CustomKey


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._CustomKey = params.get("CustomKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkSessionBatchSQLResponse(AbstractModel):
    """DescribeSparkSessionBatchSQL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _State: 状态：0：运行中、1：成功、2：失败、3：取消、4：超时；
        :type State: int
        :param _Tasks: SQL子任务列表，仅展示运行完成的子任务，若某个任务运行失败，后续其它子任务不返回
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of BatchSqlTask
        :param _Event: 非sql运行的异常事件信息，包含资源创建失败、调度异常，JOB超时等，正常运行下该Event值为空
        :type Event: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._State = None
        self._Tasks = None
        self._Event = None
        self._RequestId = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Event(self):
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._State = params.get("State")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = BatchSqlTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Event = params.get("Event")
        self._RequestId = params.get("RequestId")


class DescribeSparkSessionBatchSqlLogRequest(AbstractModel):
    """DescribeSparkSessionBatchSqlLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: SparkSQL唯一标识
        :type BatchId: str
        :param _CustomKey: 用户自定义主键，若不为空，则按照该值进行查询
        :type CustomKey: str
        """
        self._BatchId = None
        self._CustomKey = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def CustomKey(self):
        return self._CustomKey

    @CustomKey.setter
    def CustomKey(self, CustomKey):
        self._CustomKey = CustomKey


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._CustomKey = params.get("CustomKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkSessionBatchSqlLogResponse(AbstractModel):
    """DescribeSparkSessionBatchSqlLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _State: 状态：0：运行中、1：成功、2：失败、3：取消、4：超时；
        :type State: int
        :param _LogSet: 日志信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSet: list of SparkSessionBatchLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._State = None
        self._LogSet = None
        self._RequestId = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def LogSet(self):
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._State = params.get("State")
        if params.get("LogSet") is not None:
            self._LogSet = []
            for item in params.get("LogSet"):
                obj = SparkSessionBatchLog()
                obj._deserialize(item)
                self._LogSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStoreLocationRequest(AbstractModel):
    """DescribeStoreLocation请求参数结构体

    """


class DescribeStoreLocationResponse(AbstractModel):
    """DescribeStoreLocation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StoreLocation: 返回用户设置的结果存储位置路径，如果未设置则返回空字符串：""
注意：此字段可能返回 null，表示取不到有效值。
        :type StoreLocation: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StoreLocation = None
        self._RequestId = None

    @property
    def StoreLocation(self):
        return self._StoreLocation

    @StoreLocation.setter
    def StoreLocation(self, StoreLocation):
        self._StoreLocation = StoreLocation

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StoreLocation = params.get("StoreLocation")
        self._RequestId = params.get("RequestId")


class DescribeSubUserAccessPolicyRequest(AbstractModel):
    """DescribeSubUserAccessPolicy请求参数结构体

    """


class DescribeSubUserAccessPolicyResponse(AbstractModel):
    """DescribeSubUserAccessPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyDocument: 子用户访问策略
        :type PolicyDocument: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyDocument = None
        self._RequestId = None

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyDocument = params.get("PolicyDocument")
        self._RequestId = params.get("RequestId")


class DescribeTableRequest(AbstractModel):
    """DescribeTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableName: 查询对象表名称
        :type TableName: str
        :param _DatabaseName: 查询表所在的数据库名称。
        :type DatabaseName: str
        :param _DatasourceConnectionName: 查询表所在的数据源名称
        :type DatasourceConnectionName: str
        """
        self._TableName = None
        self._DatabaseName = None
        self._DatasourceConnectionName = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._DatabaseName = params.get("DatabaseName")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableResponse(AbstractModel):
    """DescribeTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Table: 数据表对象
        :type Table: :class:`tencentcloud.dlc.v20210125.models.TableResponseInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Table = None
        self._RequestId = None

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Table") is not None:
            self._Table = TableResponseInfo()
            self._Table._deserialize(params.get("Table"))
        self._RequestId = params.get("RequestId")


class DescribeTablesNameRequest(AbstractModel):
    """DescribeTablesName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 列出该数据库下所属数据表。
        :type DatabaseName: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
table-name - String - （过滤条件）数据表名称,形如：table-001。
table-id - String - （过滤条件）table id形如：12342。
        :type Filters: list of Filter
        :param _DatasourceConnectionName: 指定查询的数据源名称，默认为DataLakeCatalog
        :type DatasourceConnectionName: str
        :param _StartTime: 起始时间：用于对更新时间的筛选，格式为yyyy-mm-dd HH:MM:SS
        :type StartTime: str
        :param _EndTime: 终止时间：用于对更新时间的筛选，格式为yyyy-mm-dd HH:MM:SS
        :type EndTime: str
        :param _Sort: 排序字段，支持：CreateTime（创建时间）、UpdateTime（更新时间）、StorageSize（存储空间）、RecordCount（行数）、Name（表名称）（不传则默认按name升序）
        :type Sort: str
        :param _Asc: 排序字段，false：降序（默认）；true：升序
        :type Asc: bool
        :param _TableType: table type，表类型查询,可用值:EXTERNAL_TABLE,INDEX_TABLE,MANAGED_TABLE,MATERIALIZED_VIEW,TABLE,VIEW,VIRTUAL_VIEW
        :type TableType: str
        :param _TableFormat: 筛选字段-表格式：不传（默认）为查全部；LAKEFS：托管表；ICEBERG：非托管iceberg表；HIVE：非托管hive表；OTHER：非托管其它；
        :type TableFormat: str
        """
        self._DatabaseName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._DatasourceConnectionName = None
        self._StartTime = None
        self._EndTime = None
        self._Sort = None
        self._Asc = None
        self._TableType = None
        self._TableFormat = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

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

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

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

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def TableFormat(self):
        return self._TableFormat

    @TableFormat.setter
    def TableFormat(self, TableFormat):
        self._TableFormat = TableFormat


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Sort = params.get("Sort")
        self._Asc = params.get("Asc")
        self._TableType = params.get("TableType")
        self._TableFormat = params.get("TableFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesNameResponse(AbstractModel):
    """DescribeTablesName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableNameList: 数据表名称对象列表。
        :type TableNameList: list of str
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableNameList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TableNameList(self):
        return self._TableNameList

    @TableNameList.setter
    def TableNameList(self, TableNameList):
        self._TableNameList = TableNameList

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
        self._TableNameList = params.get("TableNameList")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 列出该数据库下所属数据表。
        :type DatabaseName: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
table-name - String - （过滤条件）数据表名称,形如：table-001。
table-id - String - （过滤条件）table id形如：12342。
        :type Filters: list of Filter
        :param _DatasourceConnectionName: 指定查询的数据源名称，默认为DataLakeCatalog
        :type DatasourceConnectionName: str
        :param _StartTime: 起始时间：用于对更新时间的筛选，格式为yyyy-mm-dd HH:MM:SS
        :type StartTime: str
        :param _EndTime: 终止时间：用于对更新时间的筛选，格式为yyyy-mm-dd HH:MM:SS
        :type EndTime: str
        :param _Sort: 排序字段，支持：CreateTime（创建时间）、UpdateTime（更新时间）、StorageSize（存储空间）、RecordCount（行数）、Name（表名称）（不传则默认按name升序）
        :type Sort: str
        :param _Asc: 排序字段，false：降序（默认）；true：升序
        :type Asc: bool
        :param _TableType: table type，表类型查询,可用值:EXTERNAL_TABLE,INDEX_TABLE,MANAGED_TABLE,MATERIALIZED_VIEW,TABLE,VIEW,VIRTUAL_VIEW
        :type TableType: str
        :param _TableFormat: 筛选字段-表格式：不传（默认）为查全部；LAKEFS：托管表；ICEBERG：非托管iceberg表；HIVE：非托管hive表；OTHER：非托管其它；
        :type TableFormat: str
        """
        self._DatabaseName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._DatasourceConnectionName = None
        self._StartTime = None
        self._EndTime = None
        self._Sort = None
        self._Asc = None
        self._TableType = None
        self._TableFormat = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

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

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

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

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def TableFormat(self):
        return self._TableFormat

    @TableFormat.setter
    def TableFormat(self, TableFormat):
        self._TableFormat = TableFormat


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Sort = params.get("Sort")
        self._Asc = params.get("Asc")
        self._TableType = params.get("TableType")
        self._TableFormat = params.get("TableFormat")
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
        :param _TableList: 数据表对象列表。
        :type TableList: list of TableResponseInfo
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TableList(self):
        return self._TableList

    @TableList.setter
    def TableList(self, TableList):
        self._TableList = TableList

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
        if params.get("TableList") is not None:
            self._TableList = []
            for item in params.get("TableList"):
                obj = TableResponseInfo()
                obj._deserialize(item)
                self._TableList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTaskLogRequest(AbstractModel):
    """DescribeTaskLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 列表返回的Id
        :type TaskId: str
        :param _StartTime: 开始运行时间，unix时间戳（毫秒）
        :type StartTime: int
        :param _EndTime: 结束运行时间，unix时间戳（毫秒）
        :type EndTime: int
        :param _Limit: 分页大小，最大1000，配合Context一起使用
        :type Limit: int
        :param _Context: 下一次分页参数，第一次传空。透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时。
        :type Context: str
        :param _Asc: 是否升序排列，true:升序排序，false:倒序，默认false，倒序排列
        :type Asc: bool
        :param _Filters: 预览日志的通用过滤条件
        :type Filters: list of Filter
        :param _BatchId: SparkSQL任务唯一ID
        :type BatchId: str
        """
        self._TaskId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Context = None
        self._Asc = None
        self._Filters = None
        self._BatchId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Asc = params.get("Asc")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogResponse(AbstractModel):
    """DescribeTaskLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 下一次分页参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _ListOver: 是否获取完结
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOver: bool
        :param _Results: 日志详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of JobLogResult
        :param _LogUrl: 日志url
注意：此字段可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Results = None
        self._LogUrl = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def LogUrl(self):
        return self._LogUrl

    @LogUrl.setter
    def LogUrl(self, LogUrl):
        self._LogUrl = LogUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = JobLogResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._LogUrl = params.get("LogUrl")
        self._RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一ID
        :type TaskId: str
        :param _NextToken: 上一次请求响应返回的分页信息。第一次可以不带，从头开始返回数据，每次返回MaxResults字段设置的数据量。
        :type NextToken: str
        :param _MaxResults: 返回结果的最大行数，范围0~1000，默认为1000.
        :type MaxResults: int
        :param _IsTransformDataType: 是否转化数据类型
        :type IsTransformDataType: bool
        """
        self._TaskId = None
        self._NextToken = None
        self._MaxResults = None
        self._IsTransformDataType = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def IsTransformDataType(self):
        return self._IsTransformDataType

    @IsTransformDataType.setter
    def IsTransformDataType(self, IsTransformDataType):
        self._IsTransformDataType = IsTransformDataType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        self._IsTransformDataType = params.get("IsTransformDataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfo: 查询的任务信息，返回为空表示输入任务ID对应的任务不存在。只有当任务状态为成功（2）的时候，才会返回任务的结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfo: :class:`tencentcloud.dlc.v20210125.models.TaskResultInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfo = None
        self._RequestId = None

    @property
    def TaskInfo(self):
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self._TaskInfo = TaskResultInfo()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class DescribeTasksCostInfoRequest(AbstractModel):
    """DescribeTasksCostInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为以下其中一个,其中task-id支持最大50个过滤个数，其他过滤参数支持的总数不超过5个。
task-id - String - （任务ID准确过滤）task-id取值形如：e386471f-139a-4e59-877f-50ece8135b99。
task-state - String - （任务状态过滤）取值范围 0(初始化)， 1(运行中)， 2(成功)， -1(失败)。
task-sql-keyword - String - （SQL语句关键字模糊过滤）取值形如：DROP TABLE。
task-operator- string （子uin过滤）
        :type Filters: list of Filter
        :param _StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。默认为45天前的当前时刻
        :type StartTime: str
        :param _EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS时间跨度在(0,30天]，支持最近45天数据查询。默认为当前时刻
        :type EndTime: str
        :param _DataEngineName: 数据引擎名称，用于筛选
        :type DataEngineName: str
        :param _SearchAfter: 下一页的标识
        :type SearchAfter: str
        :param _PageSize: 每页的大小
        :type PageSize: int
        """
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._DataEngineName = None
        self._SearchAfter = None
        self._PageSize = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def SearchAfter(self):
        return self._SearchAfter

    @SearchAfter.setter
    def SearchAfter(self, SearchAfter):
        self._SearchAfter = SearchAfter

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DataEngineName = params.get("DataEngineName")
        self._SearchAfter = params.get("SearchAfter")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksCostInfoResponse(AbstractModel):
    """DescribeTasksCostInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchAfter: 下一页的标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchAfter: str
        :param _Data: 返回的数据，字符串类型的二维数组，首行为列中文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SearchAfter = None
        self._Data = None
        self._RequestId = None

    @property
    def SearchAfter(self):
        return self._SearchAfter

    @SearchAfter.setter
    def SearchAfter(self, SearchAfter):
        self._SearchAfter = SearchAfter

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SearchAfter = params.get("SearchAfter")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeTasksOverviewRequest(AbstractModel):
    """DescribeTasksOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Filters: 筛选条件
        :type Filters: list of Filter
        :param _DataEngineName: 引擎名
        :type DataEngineName: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._DataEngineName = None

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

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DataEngineName = params.get("DataEngineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksOverviewResponse(AbstractModel):
    """DescribeTasksOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TasksOverview: 各类任务个数大于0
        :type TasksOverview: :class:`tencentcloud.dlc.v20210125.models.TasksOverview`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TasksOverview = None
        self._RequestId = None

    @property
    def TasksOverview(self):
        return self._TasksOverview

    @TasksOverview.setter
    def TasksOverview(self, TasksOverview):
        self._TasksOverview = TasksOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TasksOverview") is not None:
            self._TasksOverview = TasksOverview()
            self._TasksOverview._deserialize(params.get("TasksOverview"))
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为以下其中一个,其中task-id支持最大50个过滤个数，其他过滤参数支持的总数不超过5个。
task-id - String - （任务ID准确过滤）task-id取值形如：e386471f-139a-4e59-877f-50ece8135b99。
task-state - String - （任务状态过滤）取值范围 0(初始化)， 1(运行中)， 2(成功)， -1(失败)。
task-sql-keyword - String - （SQL语句关键字模糊过滤）取值形如：DROP TABLE。
task-operator- string （子uin过滤）
task-kind - string （任务类型过滤）
        :type Filters: list of Filter
        :param _SortBy: 排序字段，支持如下字段类型，create-time（创建时间，默认）、update-time（更新时间）
        :type SortBy: str
        :param _Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc。
        :type Sorting: str
        :param _StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。默认为45天前的当前时刻
        :type StartTime: str
        :param _EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS时间跨度在(0,30天]，支持最近45天数据查询。默认为当前时刻
        :type EndTime: str
        :param _DataEngineName: 数据引擎名称，用于筛选
        :type DataEngineName: str
        :param _ResourceGroupName: spark引擎资源组名称
        :type ResourceGroupName: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._SortBy = None
        self._Sorting = None
        self._StartTime = None
        self._EndTime = None
        self._DataEngineName = None
        self._ResourceGroupName = None

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

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

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

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DataEngineName = params.get("DataEngineName")
        self._ResourceGroupName = params.get("ResourceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskList: 任务对象列表。
        :type TaskList: list of TaskResponseInfo
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _TasksOverview: 任务概览信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TasksOverview: :class:`tencentcloud.dlc.v20210125.models.TasksOverview`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskList = None
        self._TotalCount = None
        self._TasksOverview = None
        self._RequestId = None

    @property
    def TaskList(self):
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TasksOverview(self):
        return self._TasksOverview

    @TasksOverview.setter
    def TasksOverview(self, TasksOverview):
        self._TasksOverview = TasksOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("TasksOverview") is not None:
            self._TasksOverview = TasksOverview()
            self._TasksOverview._deserialize(params.get("TasksOverview"))
        self._RequestId = params.get("RequestId")


class DescribeThirdPartyAccessUserRequest(AbstractModel):
    """DescribeThirdPartyAccessUser请求参数结构体

    """


class DescribeThirdPartyAccessUserResponse(AbstractModel):
    """DescribeThirdPartyAccessUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户信息
        :type UserInfo: :class:`tencentcloud.dlc.v20210125.models.OpendThirdAccessUserInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserInfo = None
        self._RequestId = None

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = OpendThirdAccessUserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._RequestId = params.get("RequestId")


class DescribeUpdatableDataEnginesRequest(AbstractModel):
    """DescribeUpdatableDataEngines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineConfigCommand: 引擎配置操作命令，UpdateSparkSQLLakefsPath 更新托管表路径，UpdateSparkSQLResultPath 更新结果桶路径
        :type DataEngineConfigCommand: str
        """
        self._DataEngineConfigCommand = None

    @property
    def DataEngineConfigCommand(self):
        return self._DataEngineConfigCommand

    @DataEngineConfigCommand.setter
    def DataEngineConfigCommand(self, DataEngineConfigCommand):
        self._DataEngineConfigCommand = DataEngineConfigCommand


    def _deserialize(self, params):
        self._DataEngineConfigCommand = params.get("DataEngineConfigCommand")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpdatableDataEnginesResponse(AbstractModel):
    """DescribeUpdatableDataEngines返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineBasicInfos: 集群基础信息
        :type DataEngineBasicInfos: list of DataEngineBasicInfo
        :param _TotalCount: 集群个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataEngineBasicInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DataEngineBasicInfos(self):
        return self._DataEngineBasicInfos

    @DataEngineBasicInfos.setter
    def DataEngineBasicInfos(self, DataEngineBasicInfos):
        self._DataEngineBasicInfos = DataEngineBasicInfos

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
        if params.get("DataEngineBasicInfos") is not None:
            self._DataEngineBasicInfos = []
            for item in params.get("DataEngineBasicInfos"):
                obj = DataEngineBasicInfo()
                obj._deserialize(item)
                self._DataEngineBasicInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserDataEngineConfigRequest(AbstractModel):
    """DescribeUserDataEngineConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sorting: 排序方式，desc表示倒序，asc表示正序
        :type Sorting: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为以下其中一个,每种过滤参数支持的过滤值不超过5个。
app-id - String - （appid过滤）
engine-id - String - （引擎ID过滤）
        :type Filters: list of Filter
        """
        self._Sorting = None
        self._Limit = None
        self._Offset = None
        self._SortBy = None
        self._Filters = None

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

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
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Sorting = params.get("Sorting")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SortBy = params.get("SortBy")
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
        


class DescribeUserDataEngineConfigResponse(AbstractModel):
    """DescribeUserDataEngineConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineConfigInstanceInfos: 用户引擎自定义配置项列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineConfigInstanceInfos: list of DataEngineConfigInstanceInfo
        :param _TotalCount: 配置项总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataEngineConfigInstanceInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DataEngineConfigInstanceInfos(self):
        return self._DataEngineConfigInstanceInfos

    @DataEngineConfigInstanceInfos.setter
    def DataEngineConfigInstanceInfos(self, DataEngineConfigInstanceInfos):
        self._DataEngineConfigInstanceInfos = DataEngineConfigInstanceInfos

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
        if params.get("DataEngineConfigInstanceInfos") is not None:
            self._DataEngineConfigInstanceInfos = []
            for item in params.get("DataEngineConfigInstanceInfos"):
                obj = DataEngineConfigInstanceInfo()
                obj._deserialize(item)
                self._DataEngineConfigInstanceInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id
        :type UserId: str
        :param _Type: 查询的信息类型，Group：工作组 DataAuth：数据权限 EngineAuth:引擎权限
        :type Type: str
        :param _Filters: 查询的过滤条件。

当Type为Group时，支持Key为workgroup-name的模糊搜索；

当Type为DataAuth时，支持key：

policy-type：权限类型。

policy-source：数据来源。

data-name：库表的模糊搜索。

当Type为EngineAuth时，支持key：

policy-type：权限类型。

policy-source：数据来源。

engine-name：库表的模糊搜索。
        :type Filters: list of Filter
        :param _SortBy: 排序字段。

当Type为Group时，支持create-time、group-name

当Type为DataAuth时，支持create-time

当Type为EngineAuth时，支持create-time
        :type SortBy: str
        :param _Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc
        :type Sorting: str
        :param _Limit: 返回数量，默认20，最大值100
        :type Limit: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        """
        self._UserId = None
        self._Type = None
        self._Filters = None
        self._SortBy = None
        self._Sorting = None
        self._Limit = None
        self._Offset = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

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


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Type = params.get("Type")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: :class:`tencentcloud.dlc.v20210125.models.UserDetailInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserInfo = None
        self._RequestId = None

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = UserDetailInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._RequestId = params.get("RequestId")


class DescribeUserRolesRequest(AbstractModel):
    """DescribeUserRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 列举的数量限制
        :type Limit: int
        :param _Offset: 列举的偏移位置
        :type Offset: int
        :param _Fuzzy: 按照arn模糊列举
        :type Fuzzy: str
        :param _SortBy: 返回结果按照该字段排序
        :type SortBy: str
        :param _Sorting: 正序或者倒序，例如：desc
        :type Sorting: str
        """
        self._Limit = None
        self._Offset = None
        self._Fuzzy = None
        self._SortBy = None
        self._Sorting = None

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
    def Fuzzy(self):
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Fuzzy = params.get("Fuzzy")
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserRolesResponse(AbstractModel):
    """DescribeUserRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 符合列举条件的总数量
        :type Total: int
        :param _UserRoles: 用户角色信息
        :type UserRoles: list of UserRole
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._UserRoles = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserRoles(self):
        return self._UserRoles

    @UserRoles.setter
    def UserRoles(self, UserRoles):
        self._UserRoles = UserRoles

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("UserRoles") is not None:
            self._UserRoles = []
            for item in params.get("UserRoles"):
                obj = UserRole()
                obj._deserialize(item)
                self._UserRoles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserTypeRequest(AbstractModel):
    """DescribeUserType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID（UIN），如果不填默认为调用方的子UIN
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserTypeResponse(AbstractModel):
    """DescribeUserType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserType: 用户类型。ADMIN：管理员 COMMON：普通用户
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserType = None
        self._RequestId = None

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserType = params.get("UserType")
        self._RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    """DescribeUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 指定查询的子用户uin，用户需要通过CreateUser接口创建。
        :type UserId: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大值100
        :type Limit: int
        :param _SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param _Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc
        :type Sorting: str
        :param _Filters: 过滤条件，支持如下字段类型，user-type：根据用户类型过滤。user-keyword：根据用户名称过滤
        :type Filters: list of Filter
        """
        self._UserId = None
        self._Offset = None
        self._Limit = None
        self._SortBy = None
        self._Sorting = None
        self._Filters = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

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
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
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
        


class DescribeUsersResponse(AbstractModel):
    """DescribeUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的用户总数
        :type TotalCount: int
        :param _UserSet: 查询到的授权用户信息集合
        :type UserSet: list of UserInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UserSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserSet(self):
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UserSet") is not None:
            self._UserSet = []
            for item in params.get("UserSet"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeViewsRequest(AbstractModel):
    """DescribeViews请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 列出该数据库下所属数据表。
        :type DatabaseName: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 数据偏移量，从0开始，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为其一
view-name - String - （过滤条件）数据表名称,形如：view-001。
view-id - String - （过滤条件）view id形如：12342。
        :type Filters: list of Filter
        :param _DatasourceConnectionName: 数据库所属的数据源名称
        :type DatasourceConnectionName: str
        :param _Sort: 排序字段
        :type Sort: str
        :param _Asc: 排序规则，true:升序；false:降序
        :type Asc: bool
        :param _StartTime: 按视图更新时间筛选，开始时间，如2021-11-11 00:00:00
        :type StartTime: str
        :param _EndTime: 按视图更新时间筛选，结束时间，如2021-11-12 00:00:00
        :type EndTime: str
        """
        self._DatabaseName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._DatasourceConnectionName = None
        self._Sort = None
        self._Asc = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

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

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

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
        self._DatabaseName = params.get("DatabaseName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._Sort = params.get("Sort")
        self._Asc = params.get("Asc")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeViewsResponse(AbstractModel):
    """DescribeViews返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ViewList: 视图对象列表。
        :type ViewList: list of ViewResponseInfo
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ViewList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ViewList(self):
        return self._ViewList

    @ViewList.setter
    def ViewList(self, ViewList):
        self._ViewList = ViewList

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
        if params.get("ViewList") is not None:
            self._ViewList = []
            for item in params.get("ViewList"):
                obj = ViewResponseInfo()
                obj._deserialize(item)
                self._ViewList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWorkGroupInfoRequest(AbstractModel):
    """DescribeWorkGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param _Type: 查询信息类型：User：用户信息 DataAuth：数据权限 EngineAuth：引擎权限
        :type Type: str
        :param _Filters: 查询的过滤条件。

当Type为User时，支持Key为user-name的模糊搜索；

当Type为DataAuth时，支持key：

policy-type：权限类型。

policy-source：数据来源。

data-name：库表的模糊搜索。

当Type为EngineAuth时，支持key：

policy-type：权限类型。

policy-source：数据来源。

engine-name：库表的模糊搜索。
        :type Filters: list of Filter
        :param _SortBy: 排序字段。

当Type为User时，支持create-time、user-name

当Type为DataAuth时，支持create-time

当Type为EngineAuth时，支持create-time
        :type SortBy: str
        :param _Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc
        :type Sorting: str
        :param _Limit: 返回数量，默认20，最大值100
        :type Limit: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        """
        self._WorkGroupId = None
        self._Type = None
        self._Filters = None
        self._SortBy = None
        self._Sorting = None
        self._Limit = None
        self._Offset = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

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


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        self._Type = params.get("Type")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkGroupInfoResponse(AbstractModel):
    """DescribeWorkGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupInfo: 工作组详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupInfo: :class:`tencentcloud.dlc.v20210125.models.WorkGroupDetailInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkGroupInfo = None
        self._RequestId = None

    @property
    def WorkGroupInfo(self):
        return self._WorkGroupInfo

    @WorkGroupInfo.setter
    def WorkGroupInfo(self, WorkGroupInfo):
        self._WorkGroupInfo = WorkGroupInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WorkGroupInfo") is not None:
            self._WorkGroupInfo = WorkGroupDetailInfo()
            self._WorkGroupInfo._deserialize(params.get("WorkGroupInfo"))
        self._RequestId = params.get("RequestId")


class DescribeWorkGroupsRequest(AbstractModel):
    """DescribeWorkGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 查询的工作组Id，不填或填0表示不过滤。
        :type WorkGroupId: int
        :param _Filters: 过滤条件，当前仅支持按照工作组名称进行模糊搜索。Key为workgroup-name
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大值100
        :type Limit: int
        :param _SortBy: 排序字段，支持如下字段类型，create-time
        :type SortBy: str
        :param _Sorting: 排序方式，desc表示正序，asc表示反序， 默认为asc
        :type Sorting: str
        """
        self._WorkGroupId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._SortBy = None
        self._Sorting = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkGroupsResponse(AbstractModel):
    """DescribeWorkGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 工作组总数
        :type TotalCount: int
        :param _WorkGroupSet: 工作组信息集合
        :type WorkGroupSet: list of WorkGroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._WorkGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def WorkGroupSet(self):
        return self._WorkGroupSet

    @WorkGroupSet.setter
    def WorkGroupSet(self, WorkGroupSet):
        self._WorkGroupSet = WorkGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("WorkGroupSet") is not None:
            self._WorkGroupSet = []
            for item in params.get("WorkGroupSet"):
                obj = WorkGroupInfo()
                obj._deserialize(item)
                self._WorkGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param _PolicySet: 解绑的权限集合
        :type PolicySet: list of Policy
        """
        self._UserId = None
        self._PolicySet = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy返回参数结构体

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


class DetachWorkGroupPolicyRequest(AbstractModel):
    """DetachWorkGroupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param _PolicySet: 解绑的权限集合
        :type PolicySet: list of Policy
        """
        self._WorkGroupId = None
        self._PolicySet = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachWorkGroupPolicyResponse(AbstractModel):
    """DetachWorkGroupPolicy返回参数结构体

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


class DropDMSDatabaseRequest(AbstractModel):
    """DropDMSDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 数据库名称
        :type Name: str
        :param _DeleteData: 是否删除数据
        :type DeleteData: bool
        :param _Cascade: 是否级联删除
        :type Cascade: bool
        """
        self._Name = None
        self._DeleteData = None
        self._Cascade = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeleteData(self):
        return self._DeleteData

    @DeleteData.setter
    def DeleteData(self, DeleteData):
        self._DeleteData = DeleteData

    @property
    def Cascade(self):
        return self._Cascade

    @Cascade.setter
    def Cascade(self, Cascade):
        self._Cascade = Cascade


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DeleteData = params.get("DeleteData")
        self._Cascade = params.get("Cascade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropDMSDatabaseResponse(AbstractModel):
    """DropDMSDatabase返回参数结构体

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


class DropDMSPartitionsRequest(AbstractModel):
    """DropDMSPartitions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名称
        :type DatabaseName: str
        :param _SchemaName: 数据库Schema名称
        :type SchemaName: str
        :param _TableName: 数据表名称
        :type TableName: str
        :param _Name: 分区名称
        :type Name: str
        :param _Values: 单个分区名称
        :type Values: list of str
        :param _DeleteData: 是否删除分区数据
        :type DeleteData: bool
        """
        self._DatabaseName = None
        self._SchemaName = None
        self._TableName = None
        self._Name = None
        self._Values = None
        self._DeleteData = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

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

    @property
    def DeleteData(self):
        return self._DeleteData

    @DeleteData.setter
    def DeleteData(self, DeleteData):
        self._DeleteData = DeleteData


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._SchemaName = params.get("SchemaName")
        self._TableName = params.get("TableName")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._DeleteData = params.get("DeleteData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropDMSPartitionsResponse(AbstractModel):
    """DropDMSPartitions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态
        :type Status: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DropDMSTableRequest(AbstractModel):
    """DropDMSTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        :param _Name: 表名称
        :type Name: str
        :param _DeleteData: 是否删除数据
        :type DeleteData: bool
        :param _EnvProps: 环境属性
        :type EnvProps: :class:`tencentcloud.dlc.v20210125.models.KVPair`
        """
        self._DbName = None
        self._Name = None
        self._DeleteData = None
        self._EnvProps = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeleteData(self):
        return self._DeleteData

    @DeleteData.setter
    def DeleteData(self, DeleteData):
        self._DeleteData = DeleteData

    @property
    def EnvProps(self):
        return self._EnvProps

    @EnvProps.setter
    def EnvProps(self, EnvProps):
        self._EnvProps = EnvProps


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._Name = params.get("Name")
        self._DeleteData = params.get("DeleteData")
        if params.get("EnvProps") is not None:
            self._EnvProps = KVPair()
            self._EnvProps._deserialize(params.get("EnvProps"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropDMSTableResponse(AbstractModel):
    """DropDMSTable返回参数结构体

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


class ElasticsearchInfo(AbstractModel):
    """Elasticsearch数据源的详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 数据源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _User: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _Password: 密码，需要base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Location: 数据源的VPC和子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: :class:`tencentcloud.dlc.v20210125.models.DatasourceConnectionLocation`
        :param _DbName: 默认数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param _ServiceInfo: 访问Elasticsearch的ip、端口信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceInfo: list of IpPortPair
        """
        self._InstanceId = None
        self._InstanceName = None
        self._User = None
        self._Password = None
        self._Location = None
        self._DbName = None
        self._ServiceInfo = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def ServiceInfo(self):
        return self._ServiceInfo

    @ServiceInfo.setter
    def ServiceInfo(self, ServiceInfo):
        self._ServiceInfo = ServiceInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._User = params.get("User")
        self._Password = params.get("Password")
        if params.get("Location") is not None:
            self._Location = DatasourceConnectionLocation()
            self._Location._deserialize(params.get("Location"))
        self._DbName = params.get("DbName")
        if params.get("ServiceInfo") is not None:
            self._ServiceInfo = []
            for item in params.get("ServiceInfo"):
                obj = IpPortPair()
                obj._deserialize(item)
                self._ServiceInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Execution(AbstractModel):
    """SQL语句对象

    """

    def __init__(self):
        r"""
        :param _SQL: 自动生成SQL语句。
        :type SQL: str
        """
        self._SQL = None

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL


    def _deserialize(self, params):
        self._SQL = params.get("SQL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FavorInfo(AbstractModel):
    """FavorInfo

    """

    def __init__(self):
        r"""
        :param _Priority: 优先事项
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _Catalog: Catalog名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Catalog: str
        :param _DataBase: DataBase名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DataBase: str
        :param _Table: Table名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        """
        self._Priority = None
        self._Catalog = None
        self._DataBase = None
        self._Table = None

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def DataBase(self):
        return self._DataBase

    @DataBase.setter
    def DataBase(self, DataBase):
        self._DataBase = DataBase

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Priority = params.get("Priority")
        self._Catalog = params.get("Catalog")
        self._DataBase = params.get("DataBase")
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询列表过滤条件参数

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑或（OR）关系。
        :type Name: str
        :param _Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
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
        


class GenerateCreateMangedTableSqlRequest(AbstractModel):
    """GenerateCreateMangedTableSql请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableBaseInfo: 表基本信息
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param _Columns: 表字段信息
        :type Columns: list of TColumn
        :param _Partitions: 表分区信息
        :type Partitions: list of TPartition
        :param _Properties: 表属性信息
        :type Properties: list of Property
        :param _UpsertKeys: V2 upsert表 upsert键
        :type UpsertKeys: list of str
        """
        self._TableBaseInfo = None
        self._Columns = None
        self._Partitions = None
        self._Properties = None
        self._UpsertKeys = None

    @property
    def TableBaseInfo(self):
        return self._TableBaseInfo

    @TableBaseInfo.setter
    def TableBaseInfo(self, TableBaseInfo):
        self._TableBaseInfo = TableBaseInfo

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def UpsertKeys(self):
        return self._UpsertKeys

    @UpsertKeys.setter
    def UpsertKeys(self, UpsertKeys):
        self._UpsertKeys = UpsertKeys


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self._TableBaseInfo = TableBaseInfo()
            self._TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = TColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = TPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._UpsertKeys = params.get("UpsertKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateCreateMangedTableSqlResponse(AbstractModel):
    """GenerateCreateMangedTableSql返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Execution: 创建托管存储内表sql语句描述
        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Execution = None
        self._RequestId = None

    @property
    def Execution(self):
        return self._Execution

    @Execution.setter
    def Execution(self, Execution):
        self._Execution = Execution

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Execution") is not None:
            self._Execution = Execution()
            self._Execution._deserialize(params.get("Execution"))
        self._RequestId = params.get("RequestId")


class GetOptimizerPolicyRequest(AbstractModel):
    """GetOptimizerPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SmartPolicy: 策略描述
        :type SmartPolicy: :class:`tencentcloud.dlc.v20210125.models.SmartPolicy`
        """
        self._SmartPolicy = None

    @property
    def SmartPolicy(self):
        return self._SmartPolicy

    @SmartPolicy.setter
    def SmartPolicy(self, SmartPolicy):
        self._SmartPolicy = SmartPolicy


    def _deserialize(self, params):
        if params.get("SmartPolicy") is not None:
            self._SmartPolicy = SmartPolicy()
            self._SmartPolicy._deserialize(params.get("SmartPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOptimizerPolicyResponse(AbstractModel):
    """GetOptimizerPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SmartOptimizerPolicy: 智能优化策略
        :type SmartOptimizerPolicy: :class:`tencentcloud.dlc.v20210125.models.SmartOptimizerPolicy`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SmartOptimizerPolicy = None
        self._RequestId = None

    @property
    def SmartOptimizerPolicy(self):
        return self._SmartOptimizerPolicy

    @SmartOptimizerPolicy.setter
    def SmartOptimizerPolicy(self, SmartOptimizerPolicy):
        self._SmartOptimizerPolicy = SmartOptimizerPolicy

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SmartOptimizerPolicy") is not None:
            self._SmartOptimizerPolicy = SmartOptimizerPolicy()
            self._SmartOptimizerPolicy._deserialize(params.get("SmartOptimizerPolicy"))
        self._RequestId = params.get("RequestId")


class GrantDLCCatalogAccessRequest(AbstractModel):
    """GrantDLCCatalogAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 授权VpcId
        :type VpcId: str
        :param _Product: 产品(EMR|DLC|Doris|Inlong|Wedata)
        :type Product: str
        :param _Description: 描述
        :type Description: str
        :param _VpcUin: VPC所属账号UIN
        :type VpcUin: str
        :param _VpcAppId: VPC所属账号AppId
        :type VpcAppId: int
        """
        self._VpcId = None
        self._Product = None
        self._Description = None
        self._VpcUin = None
        self._VpcAppId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VpcUin(self):
        return self._VpcUin

    @VpcUin.setter
    def VpcUin(self, VpcUin):
        self._VpcUin = VpcUin

    @property
    def VpcAppId(self):
        return self._VpcAppId

    @VpcAppId.setter
    def VpcAppId(self, VpcAppId):
        self._VpcAppId = VpcAppId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Product = params.get("Product")
        self._Description = params.get("Description")
        self._VpcUin = params.get("VpcUin")
        self._VpcAppId = params.get("VpcAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantDLCCatalogAccessResponse(AbstractModel):
    """GrantDLCCatalogAccess返回参数结构体

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


class HiveInfo(AbstractModel):
    """hive类型数据源的信息

    """

    def __init__(self):
        r"""
        :param _MetaStoreUrl: hive metastore的地址
        :type MetaStoreUrl: str
        :param _Type: hive数据源类型，代表数据储存的位置，COS或者HDFS
        :type Type: str
        :param _Location: 数据源所在的私有网络信息
        :type Location: :class:`tencentcloud.dlc.v20210125.models.DatasourceConnectionLocation`
        :param _User: 如果类型为HDFS，需要传一个用户名
        :type User: str
        :param _HighAvailability: 如果类型为HDFS，需要选择是否高可用
        :type HighAvailability: bool
        :param _BucketUrl: 如果类型为COS，需要填写COS桶连接
        :type BucketUrl: str
        :param _HdfsProperties: json字符串。如果类型为HDFS，需要填写该字段
        :type HdfsProperties: str
        :param _Mysql: Hive的元数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Mysql: :class:`tencentcloud.dlc.v20210125.models.MysqlInfo`
        :param _InstanceId: emr集群Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: emr集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _HiveVersion: EMR集群中hive组件的版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type HiveVersion: str
        :param _KerberosInfo: Kerberos详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KerberosInfo: :class:`tencentcloud.dlc.v20210125.models.KerberosInfo`
        :param _KerberosEnable: 是否开启Kerberos
注意：此字段可能返回 null，表示取不到有效值。
        :type KerberosEnable: bool
        """
        self._MetaStoreUrl = None
        self._Type = None
        self._Location = None
        self._User = None
        self._HighAvailability = None
        self._BucketUrl = None
        self._HdfsProperties = None
        self._Mysql = None
        self._InstanceId = None
        self._InstanceName = None
        self._HiveVersion = None
        self._KerberosInfo = None
        self._KerberosEnable = None

    @property
    def MetaStoreUrl(self):
        return self._MetaStoreUrl

    @MetaStoreUrl.setter
    def MetaStoreUrl(self, MetaStoreUrl):
        self._MetaStoreUrl = MetaStoreUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def HighAvailability(self):
        return self._HighAvailability

    @HighAvailability.setter
    def HighAvailability(self, HighAvailability):
        self._HighAvailability = HighAvailability

    @property
    def BucketUrl(self):
        return self._BucketUrl

    @BucketUrl.setter
    def BucketUrl(self, BucketUrl):
        self._BucketUrl = BucketUrl

    @property
    def HdfsProperties(self):
        return self._HdfsProperties

    @HdfsProperties.setter
    def HdfsProperties(self, HdfsProperties):
        self._HdfsProperties = HdfsProperties

    @property
    def Mysql(self):
        return self._Mysql

    @Mysql.setter
    def Mysql(self, Mysql):
        self._Mysql = Mysql

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def HiveVersion(self):
        return self._HiveVersion

    @HiveVersion.setter
    def HiveVersion(self, HiveVersion):
        self._HiveVersion = HiveVersion

    @property
    def KerberosInfo(self):
        return self._KerberosInfo

    @KerberosInfo.setter
    def KerberosInfo(self, KerberosInfo):
        self._KerberosInfo = KerberosInfo

    @property
    def KerberosEnable(self):
        return self._KerberosEnable

    @KerberosEnable.setter
    def KerberosEnable(self, KerberosEnable):
        self._KerberosEnable = KerberosEnable


    def _deserialize(self, params):
        self._MetaStoreUrl = params.get("MetaStoreUrl")
        self._Type = params.get("Type")
        if params.get("Location") is not None:
            self._Location = DatasourceConnectionLocation()
            self._Location._deserialize(params.get("Location"))
        self._User = params.get("User")
        self._HighAvailability = params.get("HighAvailability")
        self._BucketUrl = params.get("BucketUrl")
        self._HdfsProperties = params.get("HdfsProperties")
        if params.get("Mysql") is not None:
            self._Mysql = MysqlInfo()
            self._Mysql._deserialize(params.get("Mysql"))
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._HiveVersion = params.get("HiveVersion")
        if params.get("KerberosInfo") is not None:
            self._KerberosInfo = KerberosInfo()
            self._KerberosInfo._deserialize(params.get("KerberosInfo"))
        self._KerberosEnable = params.get("KerberosEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HouseEventsInfo(AbstractModel):
    """集群事件日志

    """

    def __init__(self):
        r"""
        :param _Time: 事件时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: list of str
        :param _EventsAction: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EventsAction: list of str
        :param _ClusterInfo: 集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterInfo: list of str
        """
        self._Time = None
        self._EventsAction = None
        self._ClusterInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def EventsAction(self):
        return self._EventsAction

    @EventsAction.setter
    def EventsAction(self, EventsAction):
        self._EventsAction = EventsAction

    @property
    def ClusterInfo(self):
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._EventsAction = params.get("EventsAction")
        self._ClusterInfo = params.get("ClusterInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpPortPair(AbstractModel):
    """ip端口对信息

    """

    def __init__(self):
        r"""
        :param _Ip: ip信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 端口信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        """
        self._Ip = None
        self._Port = None

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


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobLogResult(AbstractModel):
    """日志详情

    """

    def __init__(self):
        r"""
        :param _Time: 日志时间戳，毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param _TopicId: 日志topic id
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _TopicName: 日志topic name
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _LogJson: 日志内容，json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type LogJson: str
        :param _PkgLogId: 日志ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgLogId: str
        """
        self._Time = None
        self._TopicId = None
        self._TopicName = None
        self._LogJson = None
        self._PkgLogId = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def LogJson(self):
        return self._LogJson

    @LogJson.setter
    def LogJson(self, LogJson):
        self._LogJson = LogJson

    @property
    def PkgLogId(self):
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._LogJson = params.get("LogJson")
        self._PkgLogId = params.get("PkgLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    """配置格式

    """

    def __init__(self):
        r"""
        :param _Key: 配置的key值
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 配置的value值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class KafkaInfo(AbstractModel):
    """Kafka连接信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: kakfa实例Id
        :type InstanceId: str
        :param _Location: kakfa数据源的网络信息
        :type Location: :class:`tencentcloud.dlc.v20210125.models.DatasourceConnectionLocation`
        """
        self._InstanceId = None
        self._Location = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Location") is not None:
            self._Location = DatasourceConnectionLocation()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KerberosInfo(AbstractModel):
    """Kerberos详细信息

    """

    def __init__(self):
        r"""
        :param _Krb5Conf: Krb5Conf文件值
        :type Krb5Conf: str
        :param _KeyTab: KeyTab文件值
        :type KeyTab: str
        :param _ServicePrincipal: 服务主体
        :type ServicePrincipal: str
        """
        self._Krb5Conf = None
        self._KeyTab = None
        self._ServicePrincipal = None

    @property
    def Krb5Conf(self):
        return self._Krb5Conf

    @Krb5Conf.setter
    def Krb5Conf(self, Krb5Conf):
        self._Krb5Conf = Krb5Conf

    @property
    def KeyTab(self):
        return self._KeyTab

    @KeyTab.setter
    def KeyTab(self, KeyTab):
        self._KeyTab = KeyTab

    @property
    def ServicePrincipal(self):
        return self._ServicePrincipal

    @ServicePrincipal.setter
    def ServicePrincipal(self, ServicePrincipal):
        self._ServicePrincipal = ServicePrincipal


    def _deserialize(self, params):
        self._Krb5Conf = params.get("Krb5Conf")
        self._KeyTab = params.get("KeyTab")
        self._ServicePrincipal = params.get("ServicePrincipal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LakeFileSystemToken(AbstractModel):
    """LakeFileSystem使用的临时token

    """

    def __init__(self):
        r"""
        :param _SecretId: Token使用的临时密钥的ID
        :type SecretId: str
        :param _SecretKey: Token使用的临时密钥
        :type SecretKey: str
        :param _Token: Token信息
        :type Token: str
        :param _ExpiredTime: 过期时间
        :type ExpiredTime: int
        :param _IssueTime: 颁布时间
        :type IssueTime: int
        """
        self._SecretId = None
        self._SecretKey = None
        self._Token = None
        self._ExpiredTime = None
        self._IssueTime = None

    @property
    def SecretId(self):
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def IssueTime(self):
        return self._IssueTime

    @IssueTime.setter
    def IssueTime(self, IssueTime):
        self._IssueTime = IssueTime


    def _deserialize(self, params):
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._Token = params.get("Token")
        self._ExpiredTime = params.get("ExpiredTime")
        self._IssueTime = params.get("IssueTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LakeFsInfo(AbstractModel):
    """描述DLC托管存储基本信息

    """

    def __init__(self):
        r"""
        :param _Name: 托管存储名称
        :type Name: str
        :param _Type: 托管存储类型
        :type Type: str
        :param _SpaceUsedSize: 容量
        :type SpaceUsedSize: float
        :param _CreateTimeStamp: 创建时候的时间戳
        :type CreateTimeStamp: int
        """
        self._Name = None
        self._Type = None
        self._SpaceUsedSize = None
        self._CreateTimeStamp = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SpaceUsedSize(self):
        return self._SpaceUsedSize

    @SpaceUsedSize.setter
    def SpaceUsedSize(self, SpaceUsedSize):
        self._SpaceUsedSize = SpaceUsedSize

    @property
    def CreateTimeStamp(self):
        return self._CreateTimeStamp

    @CreateTimeStamp.setter
    def CreateTimeStamp(self, CreateTimeStamp):
        self._CreateTimeStamp = CreateTimeStamp


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._SpaceUsedSize = params.get("SpaceUsedSize")
        self._CreateTimeStamp = params.get("CreateTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskJobLogDetailRequest(AbstractModel):
    """ListTaskJobLogDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 列表返回的Id
        :type TaskId: str
        :param _StartTime: 开始运行时间，unix时间戳（毫秒）
        :type StartTime: int
        :param _EndTime: 结束运行时间，unix时间戳（毫秒）
        :type EndTime: int
        :param _Limit: 分页大小，最大1000，配合Context一起使用
        :type Limit: int
        :param _Context: 下一次分页参数，第一次传空
        :type Context: str
        :param _Asc: 最近1000条日志是否升序排列，true:升序排序，false:倒序，默认false，倒序排列
        :type Asc: bool
        :param _Filters: 预览日志的通用过滤条件
        :type Filters: list of Filter
        :param _BatchId: SparkSQL任务唯一ID
        :type BatchId: str
        """
        self._TaskId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Context = None
        self._Asc = None
        self._Filters = None
        self._BatchId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Asc = params.get("Asc")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskJobLogDetailResponse(AbstractModel):
    """ListTaskJobLogDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 下一次分页参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _ListOver: 是否获取完结
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOver: bool
        :param _Results: 日志详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of JobLogResult
        :param _LogUrl: 日志url
注意：此字段可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Results = None
        self._LogUrl = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def LogUrl(self):
        return self._LogUrl

    @LogUrl.setter
    def LogUrl(self, LogUrl):
        self._LogUrl = LogUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = JobLogResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._LogUrl = params.get("LogUrl")
        self._RequestId = params.get("RequestId")


class ListTaskJobLogNameRequest(AbstractModel):
    """ListTaskJobLogName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 查询的taskId
        :type TaskId: str
        :param _BatchId: SparkSQL批任务唯一ID
        :type BatchId: str
        """
        self._TaskId = None
        self._BatchId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskJobLogNameResponse(AbstractModel):
    """ListTaskJobLogName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Names: 日志名称列表
        :type Names: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Names = None
        self._RequestId = None

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Names = params.get("Names")
        self._RequestId = params.get("RequestId")


class LockComponentInfo(AbstractModel):
    """元数据加锁内容

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        :param _TableName: 表名称
        :type TableName: str
        :param _Partition: 分区
        :type Partition: str
        :param _LockType: 锁类型：SHARED_READ、SHARED_WRITE、EXCLUSIVE
        :type LockType: str
        :param _LockLevel: 锁级别：DB、TABLE、PARTITION
        :type LockLevel: str
        :param _DataOperationType: 锁操作：SELECT,INSERT,UPDATE,DELETE,UNSET,NO_TXN
        :type DataOperationType: str
        :param _IsAcid: 是否保持Acid
        :type IsAcid: bool
        :param _IsDynamicPartitionWrite: 是否动态分区写
        :type IsDynamicPartitionWrite: bool
        """
        self._DbName = None
        self._TableName = None
        self._Partition = None
        self._LockType = None
        self._LockLevel = None
        self._DataOperationType = None
        self._IsAcid = None
        self._IsDynamicPartitionWrite = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def LockType(self):
        return self._LockType

    @LockType.setter
    def LockType(self, LockType):
        self._LockType = LockType

    @property
    def LockLevel(self):
        return self._LockLevel

    @LockLevel.setter
    def LockLevel(self, LockLevel):
        self._LockLevel = LockLevel

    @property
    def DataOperationType(self):
        return self._DataOperationType

    @DataOperationType.setter
    def DataOperationType(self, DataOperationType):
        self._DataOperationType = DataOperationType

    @property
    def IsAcid(self):
        return self._IsAcid

    @IsAcid.setter
    def IsAcid(self, IsAcid):
        self._IsAcid = IsAcid

    @property
    def IsDynamicPartitionWrite(self):
        return self._IsDynamicPartitionWrite

    @IsDynamicPartitionWrite.setter
    def IsDynamicPartitionWrite(self, IsDynamicPartitionWrite):
        self._IsDynamicPartitionWrite = IsDynamicPartitionWrite


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._TableName = params.get("TableName")
        self._Partition = params.get("Partition")
        self._LockType = params.get("LockType")
        self._LockLevel = params.get("LockLevel")
        self._DataOperationType = params.get("DataOperationType")
        self._IsAcid = params.get("IsAcid")
        self._IsDynamicPartitionWrite = params.get("IsDynamicPartitionWrite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockMetaDataRequest(AbstractModel):
    """LockMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LockComponentList: 加锁内容
        :type LockComponentList: list of LockComponentInfo
        :param _DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        :param _TxnId: 事务id
        :type TxnId: int
        :param _AgentInfo: 客户端信息
        :type AgentInfo: str
        :param _Hostname: 主机名
        :type Hostname: str
        """
        self._LockComponentList = None
        self._DatasourceConnectionName = None
        self._TxnId = None
        self._AgentInfo = None
        self._Hostname = None

    @property
    def LockComponentList(self):
        return self._LockComponentList

    @LockComponentList.setter
    def LockComponentList(self, LockComponentList):
        self._LockComponentList = LockComponentList

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def TxnId(self):
        return self._TxnId

    @TxnId.setter
    def TxnId(self, TxnId):
        self._TxnId = TxnId

    @property
    def AgentInfo(self):
        return self._AgentInfo

    @AgentInfo.setter
    def AgentInfo(self, AgentInfo):
        self._AgentInfo = AgentInfo

    @property
    def Hostname(self):
        return self._Hostname

    @Hostname.setter
    def Hostname(self, Hostname):
        self._Hostname = Hostname


    def _deserialize(self, params):
        if params.get("LockComponentList") is not None:
            self._LockComponentList = []
            for item in params.get("LockComponentList"):
                obj = LockComponentInfo()
                obj._deserialize(item)
                self._LockComponentList.append(obj)
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._TxnId = params.get("TxnId")
        self._AgentInfo = params.get("AgentInfo")
        self._Hostname = params.get("Hostname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockMetaDataResponse(AbstractModel):
    """LockMetaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LockId: 锁id
        :type LockId: int
        :param _LockState: 锁状态：ACQUIRED、WAITING、ABORT、NOT_ACQUIRED
        :type LockState: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LockId = None
        self._LockState = None
        self._RequestId = None

    @property
    def LockId(self):
        return self._LockId

    @LockId.setter
    def LockId(self, LockId):
        self._LockId = LockId

    @property
    def LockState(self):
        return self._LockState

    @LockState.setter
    def LockState(self, LockState):
        self._LockState = LockState

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LockId = params.get("LockId")
        self._LockState = params.get("LockState")
        self._RequestId = params.get("RequestId")


class ModifyAdvancedStoreLocationRequest(AbstractModel):
    """ModifyAdvancedStoreLocation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StoreLocation: 查询结果保存cos路径
        :type StoreLocation: str
        :param _Enable: 是否启用高级设置：0-否，1-是
        :type Enable: int
        """
        self._StoreLocation = None
        self._Enable = None

    @property
    def StoreLocation(self):
        return self._StoreLocation

    @StoreLocation.setter
    def StoreLocation(self, StoreLocation):
        self._StoreLocation = StoreLocation

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._StoreLocation = params.get("StoreLocation")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAdvancedStoreLocationResponse(AbstractModel):
    """ModifyAdvancedStoreLocation返回参数结构体

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


class ModifyDataEngineDescriptionRequest(AbstractModel):
    """ModifyDataEngineDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: 要修改的引擎的名称
        :type DataEngineName: str
        :param _Message: 引擎的描述信息，最大长度为250
        :type Message: str
        """
        self._DataEngineName = None
        self._Message = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataEngineDescriptionResponse(AbstractModel):
    """ModifyDataEngineDescription返回参数结构体

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


class ModifyGovernEventRuleRequest(AbstractModel):
    """ModifyGovernEventRule请求参数结构体

    """


class ModifyGovernEventRuleResponse(AbstractModel):
    """ModifyGovernEventRule返回参数结构体

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


class ModifySparkAppBatchRequest(AbstractModel):
    """ModifySparkAppBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SparkAppId: 需要批量修改的Spark作业任务ID列表
        :type SparkAppId: list of str
        :param _DataEngine: 引擎ID
        :type DataEngine: str
        :param _AppDriverSize: driver规格：small,medium,large,xlarge；内存型(引擎类型)：m.small,m.medium,m.large,m.xlarge
        :type AppDriverSize: str
        :param _AppExecutorSize: executor规格：small,medium,large,xlarge；内存型(引擎类型)：m.small,m.medium,m.large,m.xlarge
        :type AppExecutorSize: str
        :param _AppExecutorNums: 指定executor数量，最小值为1，最大值小于集群规格
        :type AppExecutorNums: int
        :param _AppExecutorMaxNumbers: 指定executor max数量（动态配置场景下），最小值为1，最大值小于集群规格（当ExecutorMaxNumbers小于ExecutorNums时，改值设定为ExecutorNums）
        :type AppExecutorMaxNumbers: int
        :param _IsInherit: 任务资源配置是否继承集群模板，0（默认）不继承，1：继承
        :type IsInherit: int
        """
        self._SparkAppId = None
        self._DataEngine = None
        self._AppDriverSize = None
        self._AppExecutorSize = None
        self._AppExecutorNums = None
        self._AppExecutorMaxNumbers = None
        self._IsInherit = None

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def AppDriverSize(self):
        return self._AppDriverSize

    @AppDriverSize.setter
    def AppDriverSize(self, AppDriverSize):
        self._AppDriverSize = AppDriverSize

    @property
    def AppExecutorSize(self):
        return self._AppExecutorSize

    @AppExecutorSize.setter
    def AppExecutorSize(self, AppExecutorSize):
        self._AppExecutorSize = AppExecutorSize

    @property
    def AppExecutorNums(self):
        return self._AppExecutorNums

    @AppExecutorNums.setter
    def AppExecutorNums(self, AppExecutorNums):
        self._AppExecutorNums = AppExecutorNums

    @property
    def AppExecutorMaxNumbers(self):
        return self._AppExecutorMaxNumbers

    @AppExecutorMaxNumbers.setter
    def AppExecutorMaxNumbers(self, AppExecutorMaxNumbers):
        self._AppExecutorMaxNumbers = AppExecutorMaxNumbers

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit


    def _deserialize(self, params):
        self._SparkAppId = params.get("SparkAppId")
        self._DataEngine = params.get("DataEngine")
        self._AppDriverSize = params.get("AppDriverSize")
        self._AppExecutorSize = params.get("AppExecutorSize")
        self._AppExecutorNums = params.get("AppExecutorNums")
        self._AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        self._IsInherit = params.get("IsInherit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySparkAppBatchResponse(AbstractModel):
    """ModifySparkAppBatch返回参数结构体

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


class ModifySparkAppRequest(AbstractModel):
    """ModifySparkApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: spark作业名
        :type AppName: str
        :param _AppType: spark作业类型，1代表spark jar作业，2代表spark streaming作业
        :type AppType: int
        :param _DataEngine: 执行spark作业的数据引擎名称
        :type DataEngine: str
        :param _AppFile: spark作业程序包文件路径
        :type AppFile: str
        :param _RoleArn: 数据访问策略，CAM Role arn
        :type RoleArn: int
        :param _AppDriverSize: 指定的Driver规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type AppDriverSize: str
        :param _AppExecutorSize: 指定的Executor规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
        :type AppExecutorSize: str
        :param _AppExecutorNums: spark作业executor个数
        :type AppExecutorNums: int
        :param _SparkAppId: spark作业Id
        :type SparkAppId: str
        :param _Eni: 该字段已下线，请使用字段Datasource
        :type Eni: str
        :param _IsLocal: spark作业程序包是否本地上传，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocal: str
        :param _MainClass: spark作业主类
        :type MainClass: str
        :param _AppConf: spark配置，以换行符分隔
        :type AppConf: str
        :param _IsLocalJars: spark 作业依赖jar包是否本地上传，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocalJars: str
        :param _AppJars: spark 作业依赖jar包（--jars），以逗号分隔
        :type AppJars: str
        :param _IsLocalFiles: spark作业依赖文件资源是否本地上传，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocalFiles: str
        :param _AppFiles: spark作业依赖文件资源（--files）（非jar、zip），以逗号分隔
        :type AppFiles: str
        :param _IsLocalPythonFiles: pyspark：依赖上传方式，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocalPythonFiles: str
        :param _AppPythonFiles: pyspark作业依赖python资源（--py-files），支持py/zip/egg等归档格式，多文件以逗号分隔
        :type AppPythonFiles: str
        :param _CmdArgs: spark作业程序入参
        :type CmdArgs: str
        :param _MaxRetries: 最大重试次数，只对spark流任务生效
        :type MaxRetries: int
        :param _DataSource: 数据源名
        :type DataSource: str
        :param _IsLocalArchives: spark作业依赖archives资源是否本地上传，cos：存放与cos，lakefs：本地上传（控制台使用，该方式不支持直接接口调用）
        :type IsLocalArchives: str
        :param _AppArchives: spark作业依赖archives资源（--archives），支持tar.gz/tgz/tar等归档格式，以逗号分隔
        :type AppArchives: str
        :param _SparkImage: Spark Image 版本号
        :type SparkImage: str
        :param _SparkImageVersion: Spark Image 版本名称
        :type SparkImageVersion: str
        :param _AppExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于AppExecutorNums
        :type AppExecutorMaxNumbers: int
        :param _SessionId: 关联dlc查询脚本
        :type SessionId: str
        :param _IsInherit: 任务资源配置是否继承集群配置模板：0（默认）不继承、1：继承
        :type IsInherit: int
        :param _IsSessionStarted: 是否使用session脚本的sql运行任务：false：否，true：是
        :type IsSessionStarted: bool
        """
        self._AppName = None
        self._AppType = None
        self._DataEngine = None
        self._AppFile = None
        self._RoleArn = None
        self._AppDriverSize = None
        self._AppExecutorSize = None
        self._AppExecutorNums = None
        self._SparkAppId = None
        self._Eni = None
        self._IsLocal = None
        self._MainClass = None
        self._AppConf = None
        self._IsLocalJars = None
        self._AppJars = None
        self._IsLocalFiles = None
        self._AppFiles = None
        self._IsLocalPythonFiles = None
        self._AppPythonFiles = None
        self._CmdArgs = None
        self._MaxRetries = None
        self._DataSource = None
        self._IsLocalArchives = None
        self._AppArchives = None
        self._SparkImage = None
        self._SparkImageVersion = None
        self._AppExecutorMaxNumbers = None
        self._SessionId = None
        self._IsInherit = None
        self._IsSessionStarted = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def AppFile(self):
        return self._AppFile

    @AppFile.setter
    def AppFile(self, AppFile):
        self._AppFile = AppFile

    @property
    def RoleArn(self):
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def AppDriverSize(self):
        return self._AppDriverSize

    @AppDriverSize.setter
    def AppDriverSize(self, AppDriverSize):
        self._AppDriverSize = AppDriverSize

    @property
    def AppExecutorSize(self):
        return self._AppExecutorSize

    @AppExecutorSize.setter
    def AppExecutorSize(self, AppExecutorSize):
        self._AppExecutorSize = AppExecutorSize

    @property
    def AppExecutorNums(self):
        return self._AppExecutorNums

    @AppExecutorNums.setter
    def AppExecutorNums(self, AppExecutorNums):
        self._AppExecutorNums = AppExecutorNums

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def Eni(self):
        return self._Eni

    @Eni.setter
    def Eni(self, Eni):
        self._Eni = Eni

    @property
    def IsLocal(self):
        return self._IsLocal

    @IsLocal.setter
    def IsLocal(self, IsLocal):
        self._IsLocal = IsLocal

    @property
    def MainClass(self):
        return self._MainClass

    @MainClass.setter
    def MainClass(self, MainClass):
        self._MainClass = MainClass

    @property
    def AppConf(self):
        return self._AppConf

    @AppConf.setter
    def AppConf(self, AppConf):
        self._AppConf = AppConf

    @property
    def IsLocalJars(self):
        return self._IsLocalJars

    @IsLocalJars.setter
    def IsLocalJars(self, IsLocalJars):
        self._IsLocalJars = IsLocalJars

    @property
    def AppJars(self):
        return self._AppJars

    @AppJars.setter
    def AppJars(self, AppJars):
        self._AppJars = AppJars

    @property
    def IsLocalFiles(self):
        return self._IsLocalFiles

    @IsLocalFiles.setter
    def IsLocalFiles(self, IsLocalFiles):
        self._IsLocalFiles = IsLocalFiles

    @property
    def AppFiles(self):
        return self._AppFiles

    @AppFiles.setter
    def AppFiles(self, AppFiles):
        self._AppFiles = AppFiles

    @property
    def IsLocalPythonFiles(self):
        return self._IsLocalPythonFiles

    @IsLocalPythonFiles.setter
    def IsLocalPythonFiles(self, IsLocalPythonFiles):
        self._IsLocalPythonFiles = IsLocalPythonFiles

    @property
    def AppPythonFiles(self):
        return self._AppPythonFiles

    @AppPythonFiles.setter
    def AppPythonFiles(self, AppPythonFiles):
        self._AppPythonFiles = AppPythonFiles

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs

    @property
    def MaxRetries(self):
        return self._MaxRetries

    @MaxRetries.setter
    def MaxRetries(self, MaxRetries):
        self._MaxRetries = MaxRetries

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def IsLocalArchives(self):
        return self._IsLocalArchives

    @IsLocalArchives.setter
    def IsLocalArchives(self, IsLocalArchives):
        self._IsLocalArchives = IsLocalArchives

    @property
    def AppArchives(self):
        return self._AppArchives

    @AppArchives.setter
    def AppArchives(self, AppArchives):
        self._AppArchives = AppArchives

    @property
    def SparkImage(self):
        return self._SparkImage

    @SparkImage.setter
    def SparkImage(self, SparkImage):
        self._SparkImage = SparkImage

    @property
    def SparkImageVersion(self):
        return self._SparkImageVersion

    @SparkImageVersion.setter
    def SparkImageVersion(self, SparkImageVersion):
        self._SparkImageVersion = SparkImageVersion

    @property
    def AppExecutorMaxNumbers(self):
        return self._AppExecutorMaxNumbers

    @AppExecutorMaxNumbers.setter
    def AppExecutorMaxNumbers(self, AppExecutorMaxNumbers):
        self._AppExecutorMaxNumbers = AppExecutorMaxNumbers

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit

    @property
    def IsSessionStarted(self):
        return self._IsSessionStarted

    @IsSessionStarted.setter
    def IsSessionStarted(self, IsSessionStarted):
        self._IsSessionStarted = IsSessionStarted


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._AppType = params.get("AppType")
        self._DataEngine = params.get("DataEngine")
        self._AppFile = params.get("AppFile")
        self._RoleArn = params.get("RoleArn")
        self._AppDriverSize = params.get("AppDriverSize")
        self._AppExecutorSize = params.get("AppExecutorSize")
        self._AppExecutorNums = params.get("AppExecutorNums")
        self._SparkAppId = params.get("SparkAppId")
        self._Eni = params.get("Eni")
        self._IsLocal = params.get("IsLocal")
        self._MainClass = params.get("MainClass")
        self._AppConf = params.get("AppConf")
        self._IsLocalJars = params.get("IsLocalJars")
        self._AppJars = params.get("AppJars")
        self._IsLocalFiles = params.get("IsLocalFiles")
        self._AppFiles = params.get("AppFiles")
        self._IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self._AppPythonFiles = params.get("AppPythonFiles")
        self._CmdArgs = params.get("CmdArgs")
        self._MaxRetries = params.get("MaxRetries")
        self._DataSource = params.get("DataSource")
        self._IsLocalArchives = params.get("IsLocalArchives")
        self._AppArchives = params.get("AppArchives")
        self._SparkImage = params.get("SparkImage")
        self._SparkImageVersion = params.get("SparkImageVersion")
        self._AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        self._SessionId = params.get("SessionId")
        self._IsInherit = params.get("IsInherit")
        self._IsSessionStarted = params.get("IsSessionStarted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySparkAppResponse(AbstractModel):
    """ModifySparkApp返回参数结构体

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


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param _UserDescription: 用户描述
        :type UserDescription: str
        """
        self._UserId = None
        self._UserDescription = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserDescription(self):
        return self._UserDescription

    @UserDescription.setter
    def UserDescription(self, UserDescription):
        self._UserDescription = UserDescription


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserDescription = params.get("UserDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    """ModifyUser返回参数结构体

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


class ModifyUserTypeRequest(AbstractModel):
    """ModifyUserType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserType: 用户要修改到的类型，ADMIN：管理员，COMMON：一般用户。
        :type UserType: str
        """
        self._UserId = None
        self._UserType = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserTypeResponse(AbstractModel):
    """ModifyUserType返回参数结构体

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


class ModifyWorkGroupRequest(AbstractModel):
    """ModifyWorkGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param _WorkGroupDescription: 工作组描述，最大字符数限制50
        :type WorkGroupDescription: str
        """
        self._WorkGroupId = None
        self._WorkGroupDescription = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def WorkGroupDescription(self):
        return self._WorkGroupDescription

    @WorkGroupDescription.setter
    def WorkGroupDescription(self, WorkGroupDescription):
        self._WorkGroupDescription = WorkGroupDescription


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        self._WorkGroupDescription = params.get("WorkGroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkGroupResponse(AbstractModel):
    """ModifyWorkGroup返回参数结构体

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


class MountPointAssociates(AbstractModel):
    """绑定融合桶信息

    """

    def __init__(self):
        r"""
        :param _BucketId: 桶Id
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketId: str
        :param _VpcId: vpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcCidrBlock: 子网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcCidrBlock: str
        :param _AccessGroupId: 权限组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessGroupId: str
        :param _AccessRuleId: 权限规则Id
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessRuleId: int
        """
        self._BucketId = None
        self._VpcId = None
        self._VpcCidrBlock = None
        self._AccessGroupId = None
        self._AccessRuleId = None

    @property
    def BucketId(self):
        return self._BucketId

    @BucketId.setter
    def BucketId(self, BucketId):
        self._BucketId = BucketId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def AccessRuleId(self):
        return self._AccessRuleId

    @AccessRuleId.setter
    def AccessRuleId(self, AccessRuleId):
        self._AccessRuleId = AccessRuleId


    def _deserialize(self, params):
        self._BucketId = params.get("BucketId")
        self._VpcId = params.get("VpcId")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._AccessGroupId = params.get("AccessGroupId")
        self._AccessRuleId = params.get("AccessRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MysqlInfo(AbstractModel):
    """Mysql类型数据源信息

    """

    def __init__(self):
        r"""
        :param _JdbcUrl: 连接mysql的jdbc url
        :type JdbcUrl: str
        :param _User: 用户名
        :type User: str
        :param _Password: mysql密码
        :type Password: str
        :param _Location: mysql数据源的网络信息
        :type Location: :class:`tencentcloud.dlc.v20210125.models.DatasourceConnectionLocation`
        :param _DbName: 数据库名称
        :type DbName: str
        :param _InstanceId: 数据库实例ID，和数据库侧保持一致
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 数据库实例名称，和数据库侧保持一致
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        """
        self._JdbcUrl = None
        self._User = None
        self._Password = None
        self._Location = None
        self._DbName = None
        self._InstanceId = None
        self._InstanceName = None

    @property
    def JdbcUrl(self):
        return self._JdbcUrl

    @JdbcUrl.setter
    def JdbcUrl(self, JdbcUrl):
        self._JdbcUrl = JdbcUrl

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._JdbcUrl = params.get("JdbcUrl")
        self._User = params.get("User")
        self._Password = params.get("Password")
        if params.get("Location") is not None:
            self._Location = DatasourceConnectionLocation()
            self._Location._deserialize(params.get("Location"))
        self._DbName = params.get("DbName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkConnection(AbstractModel):
    """网络配置

    """

    def __init__(self):
        r"""
        :param _Id: 网络配置id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _AssociateId: 网络配置唯一标志符
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateId: str
        :param _HouseId: 计算引擎id
注意：此字段可能返回 null，表示取不到有效值。
        :type HouseId: str
        :param _DatasourceConnectionId: 数据源id(已废弃)
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionId: str
        :param _State: 网络配置状态（0-初始化，1-正常）
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _Appid: 创建用户Appid
注意：此字段可能返回 null，表示取不到有效值。
        :type Appid: int
        :param _HouseName: 计算引擎名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HouseName: str
        :param _DatasourceConnectionName: 网络配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionName: str
        :param _NetworkConnectionType: 网络配置类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConnectionType: int
        :param _Uin: 创建用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubAccountUin: 创建用户SubAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _NetworkConnectionDesc: 网络配置描述
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConnectionDesc: str
        :param _DatasourceConnectionVpcId: 数据源vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionVpcId: str
        :param _DatasourceConnectionSubnetId: 数据源SubnetId
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionSubnetId: str
        :param _DatasourceConnectionCidrBlock: 数据源SubnetId
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionCidrBlock: str
        :param _DatasourceConnectionSubnetCidrBlock: 数据源SubnetCidrBlock
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionSubnetCidrBlock: str
        """
        self._Id = None
        self._AssociateId = None
        self._HouseId = None
        self._DatasourceConnectionId = None
        self._State = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Appid = None
        self._HouseName = None
        self._DatasourceConnectionName = None
        self._NetworkConnectionType = None
        self._Uin = None
        self._SubAccountUin = None
        self._NetworkConnectionDesc = None
        self._DatasourceConnectionVpcId = None
        self._DatasourceConnectionSubnetId = None
        self._DatasourceConnectionCidrBlock = None
        self._DatasourceConnectionSubnetCidrBlock = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AssociateId(self):
        return self._AssociateId

    @AssociateId.setter
    def AssociateId(self, AssociateId):
        self._AssociateId = AssociateId

    @property
    def HouseId(self):
        return self._HouseId

    @HouseId.setter
    def HouseId(self, HouseId):
        self._HouseId = HouseId

    @property
    def DatasourceConnectionId(self):
        return self._DatasourceConnectionId

    @DatasourceConnectionId.setter
    def DatasourceConnectionId(self, DatasourceConnectionId):
        self._DatasourceConnectionId = DatasourceConnectionId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

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
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def HouseName(self):
        return self._HouseName

    @HouseName.setter
    def HouseName(self, HouseName):
        self._HouseName = HouseName

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def NetworkConnectionType(self):
        return self._NetworkConnectionType

    @NetworkConnectionType.setter
    def NetworkConnectionType(self, NetworkConnectionType):
        self._NetworkConnectionType = NetworkConnectionType

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def NetworkConnectionDesc(self):
        return self._NetworkConnectionDesc

    @NetworkConnectionDesc.setter
    def NetworkConnectionDesc(self, NetworkConnectionDesc):
        self._NetworkConnectionDesc = NetworkConnectionDesc

    @property
    def DatasourceConnectionVpcId(self):
        return self._DatasourceConnectionVpcId

    @DatasourceConnectionVpcId.setter
    def DatasourceConnectionVpcId(self, DatasourceConnectionVpcId):
        self._DatasourceConnectionVpcId = DatasourceConnectionVpcId

    @property
    def DatasourceConnectionSubnetId(self):
        return self._DatasourceConnectionSubnetId

    @DatasourceConnectionSubnetId.setter
    def DatasourceConnectionSubnetId(self, DatasourceConnectionSubnetId):
        self._DatasourceConnectionSubnetId = DatasourceConnectionSubnetId

    @property
    def DatasourceConnectionCidrBlock(self):
        return self._DatasourceConnectionCidrBlock

    @DatasourceConnectionCidrBlock.setter
    def DatasourceConnectionCidrBlock(self, DatasourceConnectionCidrBlock):
        self._DatasourceConnectionCidrBlock = DatasourceConnectionCidrBlock

    @property
    def DatasourceConnectionSubnetCidrBlock(self):
        return self._DatasourceConnectionSubnetCidrBlock

    @DatasourceConnectionSubnetCidrBlock.setter
    def DatasourceConnectionSubnetCidrBlock(self, DatasourceConnectionSubnetCidrBlock):
        self._DatasourceConnectionSubnetCidrBlock = DatasourceConnectionSubnetCidrBlock


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AssociateId = params.get("AssociateId")
        self._HouseId = params.get("HouseId")
        self._DatasourceConnectionId = params.get("DatasourceConnectionId")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Appid = params.get("Appid")
        self._HouseName = params.get("HouseName")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._NetworkConnectionType = params.get("NetworkConnectionType")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._NetworkConnectionDesc = params.get("NetworkConnectionDesc")
        self._DatasourceConnectionVpcId = params.get("DatasourceConnectionVpcId")
        self._DatasourceConnectionSubnetId = params.get("DatasourceConnectionSubnetId")
        self._DatasourceConnectionCidrBlock = params.get("DatasourceConnectionCidrBlock")
        self._DatasourceConnectionSubnetCidrBlock = params.get("DatasourceConnectionSubnetCidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSessionInfo(AbstractModel):
    """Notebook Session详细信息。

    """

    def __init__(self):
        r"""
        :param _Name: Session名称
        :type Name: str
        :param _Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        :param _DataEngineName: DLC Spark作业引擎名称
        :type DataEngineName: str
        :param _Arguments: Session相关配置，当前支持：eni、roleArn以及用户指定的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Arguments: list of KVPair
        :param _ProgramDependentFiles: 运行程序地址，当前支持：cosn://和lakefs://两种路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramDependentFiles: list of str
        :param _ProgramDependentJars: 依赖的jar程序地址，当前支持：cosn://和lakefs://两种路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramDependentJars: list of str
        :param _ProgramDependentPython: 依赖的python程序地址，当前支持：cosn://和lakefs://两种路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramDependentPython: list of str
        :param _ProgramArchives: 依赖的pyspark虚拟环境地址，当前支持：cosn://和lakefs://两种路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramArchives: list of str
        :param _DriverSize: 指定的Driver规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
注意：此字段可能返回 null，表示取不到有效值。
        :type DriverSize: str
        :param _ExecutorSize: 指定的Executor规格，当前支持：small（默认，1cu）、medium（2cu）、large（4cu）、xlarge（8cu）
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorSize: str
        :param _ExecutorNumbers: 指定的Executor数量，默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorNumbers: int
        :param _ProxyUser: 代理用户，默认为root
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyUser: str
        :param _TimeoutInSecond: 指定的Session超时时间，单位秒，默认3600秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutInSecond: int
        :param _SparkAppId: Spark任务返回的AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppId: str
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _State: Session状态，包含：not_started（未启动）、starting（已启动）、idle（等待输入）、busy(正在运行statement)、shutting_down（停止）、error（异常）、dead（已退出）、killed（被杀死）、success（正常停止）
        :type State: str
        :param _CreateTime: Session创建时间
        :type CreateTime: str
        :param _AppInfo: 其它信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppInfo: list of KVPair
        :param _SparkUiUrl: Spark ui地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkUiUrl: str
        :param _ExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于ExecutorNumbers
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorMaxNumbers: int
        """
        self._Name = None
        self._Kind = None
        self._DataEngineName = None
        self._Arguments = None
        self._ProgramDependentFiles = None
        self._ProgramDependentJars = None
        self._ProgramDependentPython = None
        self._ProgramArchives = None
        self._DriverSize = None
        self._ExecutorSize = None
        self._ExecutorNumbers = None
        self._ProxyUser = None
        self._TimeoutInSecond = None
        self._SparkAppId = None
        self._SessionId = None
        self._State = None
        self._CreateTime = None
        self._AppInfo = None
        self._SparkUiUrl = None
        self._ExecutorMaxNumbers = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def Arguments(self):
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def ProgramDependentFiles(self):
        return self._ProgramDependentFiles

    @ProgramDependentFiles.setter
    def ProgramDependentFiles(self, ProgramDependentFiles):
        self._ProgramDependentFiles = ProgramDependentFiles

    @property
    def ProgramDependentJars(self):
        return self._ProgramDependentJars

    @ProgramDependentJars.setter
    def ProgramDependentJars(self, ProgramDependentJars):
        self._ProgramDependentJars = ProgramDependentJars

    @property
    def ProgramDependentPython(self):
        return self._ProgramDependentPython

    @ProgramDependentPython.setter
    def ProgramDependentPython(self, ProgramDependentPython):
        self._ProgramDependentPython = ProgramDependentPython

    @property
    def ProgramArchives(self):
        return self._ProgramArchives

    @ProgramArchives.setter
    def ProgramArchives(self, ProgramArchives):
        self._ProgramArchives = ProgramArchives

    @property
    def DriverSize(self):
        return self._DriverSize

    @DriverSize.setter
    def DriverSize(self, DriverSize):
        self._DriverSize = DriverSize

    @property
    def ExecutorSize(self):
        return self._ExecutorSize

    @ExecutorSize.setter
    def ExecutorSize(self, ExecutorSize):
        self._ExecutorSize = ExecutorSize

    @property
    def ExecutorNumbers(self):
        return self._ExecutorNumbers

    @ExecutorNumbers.setter
    def ExecutorNumbers(self, ExecutorNumbers):
        self._ExecutorNumbers = ExecutorNumbers

    @property
    def ProxyUser(self):
        return self._ProxyUser

    @ProxyUser.setter
    def ProxyUser(self, ProxyUser):
        self._ProxyUser = ProxyUser

    @property
    def TimeoutInSecond(self):
        return self._TimeoutInSecond

    @TimeoutInSecond.setter
    def TimeoutInSecond(self, TimeoutInSecond):
        self._TimeoutInSecond = TimeoutInSecond

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AppInfo(self):
        return self._AppInfo

    @AppInfo.setter
    def AppInfo(self, AppInfo):
        self._AppInfo = AppInfo

    @property
    def SparkUiUrl(self):
        return self._SparkUiUrl

    @SparkUiUrl.setter
    def SparkUiUrl(self, SparkUiUrl):
        self._SparkUiUrl = SparkUiUrl

    @property
    def ExecutorMaxNumbers(self):
        return self._ExecutorMaxNumbers

    @ExecutorMaxNumbers.setter
    def ExecutorMaxNumbers(self, ExecutorMaxNumbers):
        self._ExecutorMaxNumbers = ExecutorMaxNumbers


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Kind = params.get("Kind")
        self._DataEngineName = params.get("DataEngineName")
        if params.get("Arguments") is not None:
            self._Arguments = []
            for item in params.get("Arguments"):
                obj = KVPair()
                obj._deserialize(item)
                self._Arguments.append(obj)
        self._ProgramDependentFiles = params.get("ProgramDependentFiles")
        self._ProgramDependentJars = params.get("ProgramDependentJars")
        self._ProgramDependentPython = params.get("ProgramDependentPython")
        self._ProgramArchives = params.get("ProgramArchives")
        self._DriverSize = params.get("DriverSize")
        self._ExecutorSize = params.get("ExecutorSize")
        self._ExecutorNumbers = params.get("ExecutorNumbers")
        self._ProxyUser = params.get("ProxyUser")
        self._TimeoutInSecond = params.get("TimeoutInSecond")
        self._SparkAppId = params.get("SparkAppId")
        self._SessionId = params.get("SessionId")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        if params.get("AppInfo") is not None:
            self._AppInfo = []
            for item in params.get("AppInfo"):
                obj = KVPair()
                obj._deserialize(item)
                self._AppInfo.append(obj)
        self._SparkUiUrl = params.get("SparkUiUrl")
        self._ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSessionStatementBatchInformation(AbstractModel):
    """按批提交Statement运行SQL任务。

    """

    def __init__(self):
        r"""
        :param _NotebookSessionStatementBatch: 任务详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookSessionStatementBatch: list of NotebookSessionStatementInfo
        :param _IsAvailable: 当前批任务是否运行完成
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAvailable: bool
        :param _SessionId: Session唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _BatchId: Batch唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        """
        self._NotebookSessionStatementBatch = None
        self._IsAvailable = None
        self._SessionId = None
        self._BatchId = None

    @property
    def NotebookSessionStatementBatch(self):
        return self._NotebookSessionStatementBatch

    @NotebookSessionStatementBatch.setter
    def NotebookSessionStatementBatch(self, NotebookSessionStatementBatch):
        self._NotebookSessionStatementBatch = NotebookSessionStatementBatch

    @property
    def IsAvailable(self):
        return self._IsAvailable

    @IsAvailable.setter
    def IsAvailable(self, IsAvailable):
        self._IsAvailable = IsAvailable

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        if params.get("NotebookSessionStatementBatch") is not None:
            self._NotebookSessionStatementBatch = []
            for item in params.get("NotebookSessionStatementBatch"):
                obj = NotebookSessionStatementInfo()
                obj._deserialize(item)
                self._NotebookSessionStatementBatch.append(obj)
        self._IsAvailable = params.get("IsAvailable")
        self._SessionId = params.get("SessionId")
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSessionStatementInfo(AbstractModel):
    """NotebookSessionStatement详情。

    """

    def __init__(self):
        r"""
        :param _Completed: 完成时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Completed: int
        :param _Started: 开始时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Started: int
        :param _Progress: 完成进度，百分制
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param _StatementId: Session Statement唯一标识
        :type StatementId: str
        :param _State: Session Statement状态，包含：waiting（排队中）、running（运行中）、available（正常）、error（异常）、cancelling（取消中）、cancelled（已取消）
        :type State: str
        :param _OutPut: Statement输出信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OutPut: :class:`tencentcloud.dlc.v20210125.models.StatementOutput`
        :param _BatchId: 批任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param _Code: 运行语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._Completed = None
        self._Started = None
        self._Progress = None
        self._StatementId = None
        self._State = None
        self._OutPut = None
        self._BatchId = None
        self._Code = None
        self._TaskId = None

    @property
    def Completed(self):
        return self._Completed

    @Completed.setter
    def Completed(self, Completed):
        self._Completed = Completed

    @property
    def Started(self):
        return self._Started

    @Started.setter
    def Started(self, Started):
        self._Started = Started

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StatementId(self):
        return self._StatementId

    @StatementId.setter
    def StatementId(self, StatementId):
        self._StatementId = StatementId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def OutPut(self):
        return self._OutPut

    @OutPut.setter
    def OutPut(self, OutPut):
        self._OutPut = OutPut

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Completed = params.get("Completed")
        self._Started = params.get("Started")
        self._Progress = params.get("Progress")
        self._StatementId = params.get("StatementId")
        self._State = params.get("State")
        if params.get("OutPut") is not None:
            self._OutPut = StatementOutput()
            self._OutPut._deserialize(params.get("OutPut"))
        self._BatchId = params.get("BatchId")
        self._Code = params.get("Code")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSessions(AbstractModel):
    """notebook session列表信息。

    """

    def __init__(self):
        r"""
        :param _Kind: 类型，当前支持：spark、pyspark、sparkr、sql
        :type Kind: str
        :param _SessionId: Session唯一标识
        :type SessionId: str
        :param _ProxyUser: 代理用户，默认为root
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyUser: str
        :param _State: Session状态，包含：not_started（未启动）、starting（已启动）、idle（等待输入）、busy(正在运行statement)、shutting_down（停止）、error（异常）、dead（已退出）、killed（被杀死）、success（正常停止）
        :type State: str
        :param _SparkAppId: Spark任务返回的AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkAppId: str
        :param _Name: Session名称
        :type Name: str
        :param _CreateTime: Session创建时间
        :type CreateTime: str
        :param _DataEngineName: 引擎名称
        :type DataEngineName: str
        :param _LastRunningTime: 最新的运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastRunningTime: str
        :param _Creator: 创建者
        :type Creator: str
        :param _SparkUiUrl: spark ui地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkUiUrl: str
        """
        self._Kind = None
        self._SessionId = None
        self._ProxyUser = None
        self._State = None
        self._SparkAppId = None
        self._Name = None
        self._CreateTime = None
        self._DataEngineName = None
        self._LastRunningTime = None
        self._Creator = None
        self._SparkUiUrl = None

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ProxyUser(self):
        return self._ProxyUser

    @ProxyUser.setter
    def ProxyUser(self, ProxyUser):
        self._ProxyUser = ProxyUser

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def LastRunningTime(self):
        return self._LastRunningTime

    @LastRunningTime.setter
    def LastRunningTime(self, LastRunningTime):
        self._LastRunningTime = LastRunningTime

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def SparkUiUrl(self):
        return self._SparkUiUrl

    @SparkUiUrl.setter
    def SparkUiUrl(self, SparkUiUrl):
        self._SparkUiUrl = SparkUiUrl


    def _deserialize(self, params):
        self._Kind = params.get("Kind")
        self._SessionId = params.get("SessionId")
        self._ProxyUser = params.get("ProxyUser")
        self._State = params.get("State")
        self._SparkAppId = params.get("SparkAppId")
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._DataEngineName = params.get("DataEngineName")
        self._LastRunningTime = params.get("LastRunningTime")
        self._Creator = params.get("Creator")
        self._SparkUiUrl = params.get("SparkUiUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpendThirdAccessUserInfo(AbstractModel):
    """开通了第三方访问的用户信息

    """

    def __init__(self):
        r"""
        :param _Id: id信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Uin: 用户主UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _CreateTime: 开通时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._Id = None
        self._Uin = None
        self._AppId = None
        self._CreateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Other(AbstractModel):
    """数据格式其它类型。

    """

    def __init__(self):
        r"""
        :param _Format: 枚举类型，默认值为Json，可选值为[Json, Parquet, ORC, AVRD]之一。
        :type Format: str
        """
        self._Format = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherCHDFSBinding(AbstractModel):
    """非DLC产品CHDFS绑定

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _SuperUser: 用户名称（该字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type SuperUser: list of str
        :param _VpcInfo: vpc配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcInfo: list of CHDFSProductVpcInfo
        :param _IsBind: 是否与该桶绑定（该字段已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBind: bool
        """
        self._ProductName = None
        self._SuperUser = None
        self._VpcInfo = None
        self._IsBind = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SuperUser(self):
        return self._SuperUser

    @SuperUser.setter
    def SuperUser(self, SuperUser):
        self._SuperUser = SuperUser

    @property
    def VpcInfo(self):
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def IsBind(self):
        return self._IsBind

    @IsBind.setter
    def IsBind(self, IsBind):
        self._IsBind = IsBind


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._SuperUser = params.get("SuperUser")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = CHDFSProductVpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        self._IsBind = params.get("IsBind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherDatasourceConnection(AbstractModel):
    """其他数据源

    """

    def __init__(self):
        r"""
        :param _Location: 网络参数
        :type Location: :class:`tencentcloud.dlc.v20210125.models.DatasourceConnectionLocation`
        """
        self._Location = None

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        if params.get("Location") is not None:
            self._Location = DatasourceConnectionLocation()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partition(AbstractModel):
    """数据表分块信息。

    """

    def __init__(self):
        r"""
        :param _Name: 分区列名。
        :type Name: str
        :param _Type: 分区类型。
        :type Type: str
        :param _Comment: 对分区的描述。
        :type Comment: str
        :param _Transform: 隐式分区转换策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Transform: str
        :param _TransformArgs: 转换策略参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TransformArgs: list of str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        """
        self._Name = None
        self._Type = None
        self._Comment = None
        self._Transform = None
        self._TransformArgs = None
        self._CreateTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Transform(self):
        return self._Transform

    @Transform.setter
    def Transform(self, Transform):
        self._Transform = Transform

    @property
    def TransformArgs(self):
        return self._TransformArgs

    @TransformArgs.setter
    def TransformArgs(self, TransformArgs):
        self._TransformArgs = TransformArgs

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Comment = params.get("Comment")
        self._Transform = params.get("Transform")
        self._TransformArgs = params.get("TransformArgs")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    """权限对象

    """

    def __init__(self):
        r"""
        :param _Database: 需要授权的数据库名，填*代表当前Catalog下所有数据库。当授权类型为管理员级别时，只允许填“*”，当授权类型为数据连接级别时只允许填空，其他类型下可以任意指定数据库。
        :type Database: str
        :param _Catalog: 需要授权的数据源名称，管理员级别下只支持填*（代表该级别全部资源）；数据源级别和数据库级别鉴权的情况下，只支持填COSDataCatalog或者*；在数据表级别鉴权下可以填写用户自定义数据源。不填情况下默认为DataLakeCatalog。注意：如果是对用户自定义数据源进行鉴权，DLC能够管理的权限是用户接入数据源的时候提供的账户的子集。
        :type Catalog: str
        :param _Table: 需要授权的表名，填*代表当前Database下所有表。当授权类型为管理员级别时，只允许填“*”，当授权类型为数据连接级别、数据库级别时只允许填空，其他类型下可以任意指定数据表。
        :type Table: str
        :param _Operation: 授权的权限操作，对于不同级别的鉴权提供不同操作。管理员权限：ALL，不填默认为ALL；数据连接级鉴权：CREATE；数据库级别鉴权：ALL、CREATE、ALTER、DROP；数据表权限：ALL、SELECT、INSERT、ALTER、DELETE、DROP、UPDATE。注意：在数据表权限下，指定的数据源不为COSDataCatalog的时候，只支持SELECT操作。
        :type Operation: str
        :param _PolicyType: 授权类型，现在支持八种授权类型：ADMIN:管理员级别鉴权 DATASOURCE：数据连接级别鉴权 DATABASE：数据库级别鉴权 TABLE：表级别鉴权 VIEW：视图级别鉴权 FUNCTION：函数级别鉴权 COLUMN：列级别鉴权 ENGINE：数据引擎鉴权。不填默认为管理员级别鉴权。
        :type PolicyType: str
        :param _Function: 需要授权的函数名，填*代表当前Catalog下所有函数。当授权类型为管理员级别时，只允许填“*”，当授权类型为数据连接级别时只允许填空，其他类型下可以任意指定函数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Function: str
        :param _View: 需要授权的视图，填*代表当前Database下所有视图。当授权类型为管理员级别时，只允许填“*”，当授权类型为数据连接级别、数据库级别时只允许填空，其他类型下可以任意指定视图。
注意：此字段可能返回 null，表示取不到有效值。
        :type View: str
        :param _Column: 需要授权的列，填*代表当前所有列。当授权类型为管理员级别时，只允许填“*”
注意：此字段可能返回 null，表示取不到有效值。
        :type Column: str
        :param _DataEngine: 需要授权的数据引擎，填*代表当前所有引擎。当授权类型为管理员级别时，只允许填“*”
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngine: str
        :param _ReAuth: 用户是否可以进行二次授权。当为true的时候，被授权的用户可以将本次获取的权限再次授权给其他子用户。默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type ReAuth: bool
        :param _Source: 权限来源，入参不填。USER：权限来自用户本身；WORKGROUP：权限来自绑定的工作组
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _Mode: 授权模式，入参不填。COMMON：普通模式；SENIOR：高级模式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param _Operator: 操作者，入参不填。
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _CreateTime: 权限创建的时间，入参不填
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _SourceId: 权限所属工作组的ID，只有当该权限的来源为工作组时才会有值。即仅当Source字段的值为WORKGROUP时该字段才有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceId: int
        :param _SourceName: 权限所属工作组的名称，只有当该权限的来源为工作组时才会有值。即仅当Source字段的值为WORKGROUP时该字段才有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceName: str
        :param _Id: 策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        """
        self._Database = None
        self._Catalog = None
        self._Table = None
        self._Operation = None
        self._PolicyType = None
        self._Function = None
        self._View = None
        self._Column = None
        self._DataEngine = None
        self._ReAuth = None
        self._Source = None
        self._Mode = None
        self._Operator = None
        self._CreateTime = None
        self._SourceId = None
        self._SourceName = None
        self._Id = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def View(self):
        return self._View

    @View.setter
    def View(self, View):
        self._View = View

    @property
    def Column(self):
        return self._Column

    @Column.setter
    def Column(self, Column):
        self._Column = Column

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def ReAuth(self):
        return self._ReAuth

    @ReAuth.setter
    def ReAuth(self, ReAuth):
        self._ReAuth = ReAuth

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SourceId(self):
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Catalog = params.get("Catalog")
        self._Table = params.get("Table")
        self._Operation = params.get("Operation")
        self._PolicyType = params.get("PolicyType")
        self._Function = params.get("Function")
        self._View = params.get("View")
        self._Column = params.get("Column")
        self._DataEngine = params.get("DataEngine")
        self._ReAuth = params.get("ReAuth")
        self._Source = params.get("Source")
        self._Mode = params.get("Mode")
        self._Operator = params.get("Operator")
        self._CreateTime = params.get("CreateTime")
        self._SourceId = params.get("SourceId")
        self._SourceName = params.get("SourceName")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policys(AbstractModel):
    """策略集合

    """

    def __init__(self):
        r"""
        :param _PolicySet: 策略集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicySet: list of Policy
        :param _TotalCount: 策略总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._PolicySet = None
        self._TotalCount = None

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrestoMonitorMetrics(AbstractModel):
    """Presto监控指标

    """

    def __init__(self):
        r"""
        :param _LocalCacheHitRate: 	Alluxio本地缓存命中率
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalCacheHitRate: float
        :param _FragmentCacheHitRate: Fragment缓存命中率
注意：此字段可能返回 null，表示取不到有效值。
        :type FragmentCacheHitRate: float
        """
        self._LocalCacheHitRate = None
        self._FragmentCacheHitRate = None

    @property
    def LocalCacheHitRate(self):
        return self._LocalCacheHitRate

    @LocalCacheHitRate.setter
    def LocalCacheHitRate(self, LocalCacheHitRate):
        self._LocalCacheHitRate = LocalCacheHitRate

    @property
    def FragmentCacheHitRate(self):
        return self._FragmentCacheHitRate

    @FragmentCacheHitRate.setter
    def FragmentCacheHitRate(self, FragmentCacheHitRate):
        self._FragmentCacheHitRate = FragmentCacheHitRate


    def _deserialize(self, params):
        self._LocalCacheHitRate = params.get("LocalCacheHitRate")
        self._FragmentCacheHitRate = params.get("FragmentCacheHitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Property(AbstractModel):
    """数据库和数据表属性信息

    """

    def __init__(self):
        r"""
        :param _Key: 属性key名称。
        :type Key: str
        :param _Value: 属性key对应的value。
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
        


class PythonSparkImage(AbstractModel):
    """python-spark镜像信息。

    """

    def __init__(self):
        r"""
        :param _SparkImageId: spark镜像唯一id
        :type SparkImageId: str
        :param _ChildImageVersionId: 集群小版本镜像id
        :type ChildImageVersionId: str
        :param _SparkImageVersion: spark镜像名称
        :type SparkImageVersion: str
        :param _Description: spark镜像描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._SparkImageId = None
        self._ChildImageVersionId = None
        self._SparkImageVersion = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def SparkImageId(self):
        return self._SparkImageId

    @SparkImageId.setter
    def SparkImageId(self, SparkImageId):
        self._SparkImageId = SparkImageId

    @property
    def ChildImageVersionId(self):
        return self._ChildImageVersionId

    @ChildImageVersionId.setter
    def ChildImageVersionId(self, ChildImageVersionId):
        self._ChildImageVersionId = ChildImageVersionId

    @property
    def SparkImageVersion(self):
        return self._SparkImageVersion

    @SparkImageVersion.setter
    def SparkImageVersion(self, SparkImageVersion):
        self._SparkImageVersion = SparkImageVersion

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
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._SparkImageId = params.get("SparkImageId")
        self._ChildImageVersionId = params.get("ChildImageVersionId")
        self._SparkImageVersion = params.get("SparkImageVersion")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResultRequest(AbstractModel):
    """QueryResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _NextToken: lastReadFile为上一次读取的文件，lastReadOffset为上一次读取到的位置
        :type NextToken: str
        """
        self._TaskId = None
        self._NextToken = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResultResponse(AbstractModel):
    """QueryResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _ResultSet: 结果数据
        :type ResultSet: str
        :param _ResultSchema: schema
        :type ResultSchema: list of Column
        :param _NextToken: 分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ResultSet = None
        self._ResultSchema = None
        self._NextToken = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ResultSet(self):
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def ResultSchema(self):
        return self._ResultSchema

    @ResultSchema.setter
    def ResultSchema(self, ResultSchema):
        self._ResultSchema = ResultSchema

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ResultSet = params.get("ResultSet")
        if params.get("ResultSchema") is not None:
            self._ResultSchema = []
            for item in params.get("ResultSchema"):
                obj = Column()
                obj._deserialize(item)
                self._ResultSchema.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class QueryTaskCostDetailRequest(AbstractModel):
    """QueryTaskCostDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，如下支持的过滤类型，传参Name应为以下其中一个,其中task-id支持最大50个过滤个数，其他过滤参数支持的总数不超过5个。
task-id - String - （任务ID准确过滤）task-id取值形如：e386471f-139a-4e59-877f-50ece8135b99。
task-state - String - （任务状态过滤）取值范围 0(初始化)， 1(运行中)， 2(成功)， -1(失败)。
task-sql-keyword - String - （SQL语句关键字模糊过滤）取值形如：DROP TABLE。
task-operator- string （子uin过滤）
        :type Filters: list of Filter
        :param _StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。默认为45天前的当前时刻
        :type StartTime: str
        :param _EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS时间跨度在(0,30天]，支持最近45天数据查询。默认为当前时刻
        :type EndTime: str
        :param _DataEngineName: 数据引擎名称，用于筛选
        :type DataEngineName: str
        :param _SearchAfter: 下一页的标识
        :type SearchAfter: str
        :param _PageSize: 每页的大小
        :type PageSize: int
        """
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._DataEngineName = None
        self._SearchAfter = None
        self._PageSize = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def SearchAfter(self):
        return self._SearchAfter

    @SearchAfter.setter
    def SearchAfter(self, SearchAfter):
        self._SearchAfter = SearchAfter

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DataEngineName = params.get("DataEngineName")
        self._SearchAfter = params.get("SearchAfter")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTaskCostDetailResponse(AbstractModel):
    """QueryTaskCostDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchAfter: 下一页的标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchAfter: str
        :param _Data: 返回的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SearchAfter = None
        self._Data = None
        self._RequestId = None

    @property
    def SearchAfter(self):
        return self._SearchAfter

    @SearchAfter.setter
    def SearchAfter(self, SearchAfter):
        self._SearchAfter = SearchAfter

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SearchAfter = params.get("SearchAfter")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class RegisterThirdPartyAccessUserRequest(AbstractModel):
    """RegisterThirdPartyAccessUser请求参数结构体

    """


class RegisterThirdPartyAccessUserResponse(AbstractModel):
    """RegisterThirdPartyAccessUser返回参数结构体

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


class RenewDataEngineRequest(AbstractModel):
    """RenewDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: CU队列名称
        :type DataEngineName: str
        :param _TimeSpan: 续费时长，单位月，最少续费1一个月
        :type TimeSpan: int
        :param _PayMode: 付费类型，默认为1，预付费
        :type PayMode: int
        :param _TimeUnit: 单位，默认m，仅能填m
        :type TimeUnit: str
        :param _RenewFlag: 自动续费标志，0，初始状态，默认不自动续费，若用户有预付费不停服特权，自动续费。1：自动续费。2：明确不自动续费。不传该参数默认为0
        :type RenewFlag: int
        """
        self._DataEngineName = None
        self._TimeSpan = None
        self._PayMode = None
        self._TimeUnit = None
        self._RenewFlag = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._TimeSpan = params.get("TimeSpan")
        self._PayMode = params.get("PayMode")
        self._TimeUnit = params.get("TimeUnit")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDataEngineResponse(AbstractModel):
    """RenewDataEngine返回参数结构体

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


class ReportHeartbeatMetaDataRequest(AbstractModel):
    """ReportHeartbeatMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        :param _LockId: 锁ID
        :type LockId: int
        :param _TxnId: 事务ID
        :type TxnId: int
        """
        self._DatasourceConnectionName = None
        self._LockId = None
        self._TxnId = None

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def LockId(self):
        return self._LockId

    @LockId.setter
    def LockId(self, LockId):
        self._LockId = LockId

    @property
    def TxnId(self):
        return self._TxnId

    @TxnId.setter
    def TxnId(self, TxnId):
        self._TxnId = TxnId


    def _deserialize(self, params):
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._LockId = params.get("LockId")
        self._TxnId = params.get("TxnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportHeartbeatMetaDataResponse(AbstractModel):
    """ReportHeartbeatMetaData返回参数结构体

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


class ResourceInfo(AbstractModel):
    """ResourceInfo

    """

    def __init__(self):
        r"""
        :param _AttributionType: 归属类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AttributionType: str
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _Name: 引擎名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Instance: 如资源类型为spark-sql 取值为Name, 如为spark-batch 取值为session app_name
注意：此字段可能返回 null，表示取不到有效值。
        :type Instance: str
        :param _Favor: 亲和性
注意：此字段可能返回 null，表示取不到有效值。
        :type Favor: list of FavorInfo
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._AttributionType = None
        self._ResourceType = None
        self._Name = None
        self._Instance = None
        self._Favor = None
        self._Status = None

    @property
    def AttributionType(self):
        return self._AttributionType

    @AttributionType.setter
    def AttributionType(self, AttributionType):
        self._AttributionType = AttributionType

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Instance(self):
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def Favor(self):
        return self._Favor

    @Favor.setter
    def Favor(self, Favor):
        self._Favor = Favor

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AttributionType = params.get("AttributionType")
        self._ResourceType = params.get("ResourceType")
        self._Name = params.get("Name")
        self._Instance = params.get("Instance")
        if params.get("Favor") is not None:
            self._Favor = []
            for item in params.get("Favor"):
                obj = FavorInfo()
                obj._deserialize(item)
                self._Favor.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDataEngineRequest(AbstractModel):
    """RestartDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 引擎ID
        :type DataEngineId: str
        :param _ForcedOperation: 是否强制重启，忽略任务
        :type ForcedOperation: bool
        """
        self._DataEngineId = None
        self._ForcedOperation = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def ForcedOperation(self):
        return self._ForcedOperation

    @ForcedOperation.setter
    def ForcedOperation(self, ForcedOperation):
        self._ForcedOperation = ForcedOperation


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        self._ForcedOperation = params.get("ForcedOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDataEngineResponse(AbstractModel):
    """RestartDataEngine返回参数结构体

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


class RevokeDLCCatalogAccessRequest(AbstractModel):
    """RevokeDLCCatalogAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VpcID
        :type VpcId: str
        """
        self._VpcId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeDLCCatalogAccessResponse(AbstractModel):
    """RevokeDLCCatalogAccess返回参数结构体

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


class RollbackDataEngineImageRequest(AbstractModel):
    """RollbackDataEngineImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 引擎ID
        :type DataEngineId: str
        :param _FromRecordId: 检查是否能回滚的接口返回的FromRecordId参数
        :type FromRecordId: str
        :param _ToRecordId: 检查是否能回滚的接口返回的ToRecordId参数
        :type ToRecordId: str
        """
        self._DataEngineId = None
        self._FromRecordId = None
        self._ToRecordId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def FromRecordId(self):
        return self._FromRecordId

    @FromRecordId.setter
    def FromRecordId(self, FromRecordId):
        self._FromRecordId = FromRecordId

    @property
    def ToRecordId(self):
        return self._ToRecordId

    @ToRecordId.setter
    def ToRecordId(self, ToRecordId):
        self._ToRecordId = ToRecordId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        self._FromRecordId = params.get("FromRecordId")
        self._ToRecordId = params.get("ToRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackDataEngineImageResponse(AbstractModel):
    """RollbackDataEngineImage返回参数结构体

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


class SQLTask(AbstractModel):
    """SQL查询任务

    """

    def __init__(self):
        r"""
        :param _SQL: base64加密后的SQL语句
        :type SQL: str
        :param _Config: 任务的配置信息
        :type Config: list of KVPair
        """
        self._SQL = None
        self._Config = None

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._SQL = params.get("SQL")
        if params.get("Config") is not None:
            self._Config = []
            for item in params.get("Config"):
                obj = KVPair()
                obj._deserialize(item)
                self._Config.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Script(AbstractModel):
    """script实例。

    """

    def __init__(self):
        r"""
        :param _ScriptId: 脚本Id，长度36字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptId: str
        :param _ScriptName: 脚本名称，长度0-25。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptName: str
        :param _ScriptDesc: 脚本描述，长度0-50。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptDesc: str
        :param _DatabaseName: 默认关联数据库。
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param _SQLStatement: SQL描述，长度0-10000。
注意：此字段可能返回 null，表示取不到有效值。
        :type SQLStatement: str
        :param _UpdateTime: 更新时间戳， 单位：ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        """
        self._ScriptId = None
        self._ScriptName = None
        self._ScriptDesc = None
        self._DatabaseName = None
        self._SQLStatement = None
        self._UpdateTime = None

    @property
    def ScriptId(self):
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ScriptName(self):
        return self._ScriptName

    @ScriptName.setter
    def ScriptName(self, ScriptName):
        self._ScriptName = ScriptName

    @property
    def ScriptDesc(self):
        return self._ScriptDesc

    @ScriptDesc.setter
    def ScriptDesc(self, ScriptDesc):
        self._ScriptDesc = ScriptDesc

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SQLStatement(self):
        return self._SQLStatement

    @SQLStatement.setter
    def SQLStatement(self, SQLStatement):
        self._SQLStatement = SQLStatement

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ScriptName = params.get("ScriptName")
        self._ScriptDesc = params.get("ScriptDesc")
        self._DatabaseName = params.get("DatabaseName")
        self._SQLStatement = params.get("SQLStatement")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionResourceTemplate(AbstractModel):
    """Spark批作业集群Session资源配置模板；

    """

    def __init__(self):
        r"""
        :param _DriverSize: driver规格：small,medium,large,xlarge；内存型(引擎类型)：m.small,m.medium,m.large,m.xlarge
注意：此字段可能返回 null，表示取不到有效值。
        :type DriverSize: str
        :param _ExecutorSize: executor规格：small,medium,large,xlarge；内存型(引擎类型)：m.small,m.medium,m.large,m.xlarge
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorSize: str
        :param _ExecutorNums: 指定executor数量，最小值为1，最大值小于集群规格
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorNums: int
        :param _ExecutorMaxNumbers: 指定executor max数量（动态配置场景下），最小值为1，最大值小于集群规格（当ExecutorMaxNumbers小于ExecutorNums时，改值设定为ExecutorNums）
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorMaxNumbers: int
        """
        self._DriverSize = None
        self._ExecutorSize = None
        self._ExecutorNums = None
        self._ExecutorMaxNumbers = None

    @property
    def DriverSize(self):
        return self._DriverSize

    @DriverSize.setter
    def DriverSize(self, DriverSize):
        self._DriverSize = DriverSize

    @property
    def ExecutorSize(self):
        return self._ExecutorSize

    @ExecutorSize.setter
    def ExecutorSize(self, ExecutorSize):
        self._ExecutorSize = ExecutorSize

    @property
    def ExecutorNums(self):
        return self._ExecutorNums

    @ExecutorNums.setter
    def ExecutorNums(self, ExecutorNums):
        self._ExecutorNums = ExecutorNums

    @property
    def ExecutorMaxNumbers(self):
        return self._ExecutorMaxNumbers

    @ExecutorMaxNumbers.setter
    def ExecutorMaxNumbers(self, ExecutorMaxNumbers):
        self._ExecutorMaxNumbers = ExecutorMaxNumbers


    def _deserialize(self, params):
        self._DriverSize = params.get("DriverSize")
        self._ExecutorSize = params.get("ExecutorSize")
        self._ExecutorNums = params.get("ExecutorNums")
        self._ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartOptimizerIndexPolicy(AbstractModel):
    """SmartOptimizerIndexPolicy

    """

    def __init__(self):
        r"""
        :param _IndexEnable: 开启索引
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexEnable: str
        """
        self._IndexEnable = None

    @property
    def IndexEnable(self):
        return self._IndexEnable

    @IndexEnable.setter
    def IndexEnable(self, IndexEnable):
        self._IndexEnable = IndexEnable


    def _deserialize(self, params):
        self._IndexEnable = params.get("IndexEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartOptimizerLifecyclePolicy(AbstractModel):
    """SmartOptimizerLifecyclePolicy

    """

    def __init__(self):
        r"""
        :param _LifecycleEnable: 生命周期启用
注意：此字段可能返回 null，表示取不到有效值。
        :type LifecycleEnable: str
        :param _Expiration: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Expiration: int
        :param _DropTable: 是否删表
注意：此字段可能返回 null，表示取不到有效值。
        :type DropTable: bool
        """
        self._LifecycleEnable = None
        self._Expiration = None
        self._DropTable = None

    @property
    def LifecycleEnable(self):
        return self._LifecycleEnable

    @LifecycleEnable.setter
    def LifecycleEnable(self, LifecycleEnable):
        self._LifecycleEnable = LifecycleEnable

    @property
    def Expiration(self):
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def DropTable(self):
        return self._DropTable

    @DropTable.setter
    def DropTable(self, DropTable):
        self._DropTable = DropTable


    def _deserialize(self, params):
        self._LifecycleEnable = params.get("LifecycleEnable")
        self._Expiration = params.get("Expiration")
        self._DropTable = params.get("DropTable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartOptimizerPolicy(AbstractModel):
    """SmartOptimizerPolicy

    """

    def __init__(self):
        r"""
        :param _Inherit: 是否继承
注意：此字段可能返回 null，表示取不到有效值。
        :type Inherit: str
        :param _Resources: ResourceInfo
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of ResourceInfo
        :param _Written: SmartOptimizerWrittenPolicy
注意：此字段可能返回 null，表示取不到有效值。
        :type Written: :class:`tencentcloud.dlc.v20210125.models.SmartOptimizerWrittenPolicy`
        :param _Lifecycle: SmartOptimizerLifecyclePolicy
注意：此字段可能返回 null，表示取不到有效值。
        :type Lifecycle: :class:`tencentcloud.dlc.v20210125.models.SmartOptimizerLifecyclePolicy`
        :param _Index: SmartOptimizerIndexPolicy
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: :class:`tencentcloud.dlc.v20210125.models.SmartOptimizerIndexPolicy`
        """
        self._Inherit = None
        self._Resources = None
        self._Written = None
        self._Lifecycle = None
        self._Index = None

    @property
    def Inherit(self):
        return self._Inherit

    @Inherit.setter
    def Inherit(self, Inherit):
        self._Inherit = Inherit

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Written(self):
        return self._Written

    @Written.setter
    def Written(self, Written):
        self._Written = Written

    @property
    def Lifecycle(self):
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Inherit = params.get("Inherit")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("Written") is not None:
            self._Written = SmartOptimizerWrittenPolicy()
            self._Written._deserialize(params.get("Written"))
        if params.get("Lifecycle") is not None:
            self._Lifecycle = SmartOptimizerLifecyclePolicy()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        if params.get("Index") is not None:
            self._Index = SmartOptimizerIndexPolicy()
            self._Index._deserialize(params.get("Index"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartOptimizerWrittenPolicy(AbstractModel):
    """SmartOptimizerWrittenPolicy

    """


class SmartPolicy(AbstractModel):
    """SmartPolicyRequest

    """

    def __init__(self):
        r"""
        :param _BaseInfo: 基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseInfo: :class:`tencentcloud.dlc.v20210125.models.SmartPolicyBaseInfo`
        :param _Policy: 策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: :class:`tencentcloud.dlc.v20210125.models.SmartOptimizerPolicy`
        """
        self._BaseInfo = None
        self._Policy = None

    @property
    def BaseInfo(self):
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        if params.get("BaseInfo") is not None:
            self._BaseInfo = SmartPolicyBaseInfo()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("Policy") is not None:
            self._Policy = SmartOptimizerPolicy()
            self._Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartPolicyBaseInfo(AbstractModel):
    """SmartPolicyBaseInfo

    """

    def __init__(self):
        r"""
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _PolicyType: Catalog/Database/Table
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param _Catalog: Catalog名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Catalog: str
        :param _Database: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Table: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _AppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        """
        self._Uin = None
        self._PolicyType = None
        self._Catalog = None
        self._Database = None
        self._Table = None
        self._AppId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._PolicyType = params.get("PolicyType")
        self._Catalog = params.get("Catalog")
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkJobInfo(AbstractModel):
    """spark作业详情。

    """

    def __init__(self):
        r"""
        :param _JobId: spark作业ID
        :type JobId: str
        :param _JobName: spark作业名
        :type JobName: str
        :param _JobType: spark作业类型，可去1或者2，1表示batch作业， 2表示streaming作业
        :type JobType: int
        :param _DataEngine: 引擎名
        :type DataEngine: str
        :param _Eni: 该字段已下线，请使用字段Datasource
        :type Eni: str
        :param _IsLocal: 程序包是否本地上传，cos或者lakefs
        :type IsLocal: str
        :param _JobFile: 程序包路径
        :type JobFile: str
        :param _RoleArn: 角色ID
        :type RoleArn: int
        :param _MainClass: spark作业运行主类
        :type MainClass: str
        :param _CmdArgs: 命令行参数，spark作业命令行参数，空格分隔
        :type CmdArgs: str
        :param _JobConf: spark原生配置，换行符分隔
        :type JobConf: str
        :param _IsLocalJars: 依赖jars是否本地上传，cos或者lakefs
        :type IsLocalJars: str
        :param _JobJars: spark作业依赖jars，逗号分隔
        :type JobJars: str
        :param _IsLocalFiles: 依赖文件是否本地上传，cos或者lakefs
        :type IsLocalFiles: str
        :param _JobFiles: spark作业依赖文件，逗号分隔
        :type JobFiles: str
        :param _JobDriverSize: spark作业driver资源大小
        :type JobDriverSize: str
        :param _JobExecutorSize: spark作业executor资源大小
        :type JobExecutorSize: str
        :param _JobExecutorNums: spark作业executor个数
        :type JobExecutorNums: int
        :param _JobMaxAttempts: spark流任务最大重试次数
        :type JobMaxAttempts: int
        :param _JobCreator: spark作业创建者
        :type JobCreator: str
        :param _JobCreateTime: spark作业创建时间
        :type JobCreateTime: int
        :param _JobUpdateTime: spark作业更新时间
        :type JobUpdateTime: int
        :param _CurrentTaskId: spark作业最近任务ID
        :type CurrentTaskId: str
        :param _JobStatus: spark作业最近运行状态，初始化：0，运行中：1，成功：2，数据写入中： 3， 排队中： 4， 失败： -1， 已删除： -3，已过期： -5
        :type JobStatus: int
        :param _StreamingStat: spark流作业统计
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamingStat: :class:`tencentcloud.dlc.v20210125.models.StreamingStatistics`
        :param _DataSource: 数据源名
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param _IsLocalPythonFiles: pyspark：依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLocalPythonFiles: str
        :param _AppPythonFiles: 注：该返回值已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type AppPythonFiles: str
        :param _IsLocalArchives: archives：依赖上传方式，1、cos；2、lakefs（控制台使用，该方式不支持直接接口调用）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLocalArchives: str
        :param _JobArchives: archives：依赖资源
注意：此字段可能返回 null，表示取不到有效值。
        :type JobArchives: str
        :param _SparkImage: Spark Image 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkImage: str
        :param _JobPythonFiles: pyspark：python依赖, 除py文件外，还支持zip/egg等归档格式，多文件以逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type JobPythonFiles: str
        :param _TaskNum: 当前job正在运行或准备运行的任务个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNum: int
        :param _DataEngineStatus: 引擎状态：-100（默认：未知状态），-2~11：引擎正常状态；
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineStatus: int
        :param _JobExecutorMaxNumbers: 指定的Executor数量（最大值），默认为1，当开启动态分配有效，若未开启，则该值等于JobExecutorNums
注意：此字段可能返回 null，表示取不到有效值。
        :type JobExecutorMaxNumbers: int
        :param _SparkImageVersion: 镜像版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkImageVersion: str
        :param _SessionId: 查询脚本关联id
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _DataEngineClusterType: spark_emr_livy
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineClusterType: str
        :param _DataEngineImageVersion: Spark 3.2-EMR
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineImageVersion: str
        :param _IsInherit: 任务资源配置是否继承集群模板，0（默认）不继承，1：继承
注意：此字段可能返回 null，表示取不到有效值。
        :type IsInherit: int
        :param _IsSessionStarted: 是否使用session脚本的sql运行任务：false：否，true：是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSessionStarted: bool
        :param _EngineTypeDetail: 引擎详细类型：SparkSQL、PrestoSQL、SparkBatch、StandardSpark、StandardPresto
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineTypeDetail: str
        """
        self._JobId = None
        self._JobName = None
        self._JobType = None
        self._DataEngine = None
        self._Eni = None
        self._IsLocal = None
        self._JobFile = None
        self._RoleArn = None
        self._MainClass = None
        self._CmdArgs = None
        self._JobConf = None
        self._IsLocalJars = None
        self._JobJars = None
        self._IsLocalFiles = None
        self._JobFiles = None
        self._JobDriverSize = None
        self._JobExecutorSize = None
        self._JobExecutorNums = None
        self._JobMaxAttempts = None
        self._JobCreator = None
        self._JobCreateTime = None
        self._JobUpdateTime = None
        self._CurrentTaskId = None
        self._JobStatus = None
        self._StreamingStat = None
        self._DataSource = None
        self._IsLocalPythonFiles = None
        self._AppPythonFiles = None
        self._IsLocalArchives = None
        self._JobArchives = None
        self._SparkImage = None
        self._JobPythonFiles = None
        self._TaskNum = None
        self._DataEngineStatus = None
        self._JobExecutorMaxNumbers = None
        self._SparkImageVersion = None
        self._SessionId = None
        self._DataEngineClusterType = None
        self._DataEngineImageVersion = None
        self._IsInherit = None
        self._IsSessionStarted = None
        self._EngineTypeDetail = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobType(self):
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def Eni(self):
        return self._Eni

    @Eni.setter
    def Eni(self, Eni):
        self._Eni = Eni

    @property
    def IsLocal(self):
        return self._IsLocal

    @IsLocal.setter
    def IsLocal(self, IsLocal):
        self._IsLocal = IsLocal

    @property
    def JobFile(self):
        return self._JobFile

    @JobFile.setter
    def JobFile(self, JobFile):
        self._JobFile = JobFile

    @property
    def RoleArn(self):
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def MainClass(self):
        return self._MainClass

    @MainClass.setter
    def MainClass(self, MainClass):
        self._MainClass = MainClass

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs

    @property
    def JobConf(self):
        return self._JobConf

    @JobConf.setter
    def JobConf(self, JobConf):
        self._JobConf = JobConf

    @property
    def IsLocalJars(self):
        return self._IsLocalJars

    @IsLocalJars.setter
    def IsLocalJars(self, IsLocalJars):
        self._IsLocalJars = IsLocalJars

    @property
    def JobJars(self):
        return self._JobJars

    @JobJars.setter
    def JobJars(self, JobJars):
        self._JobJars = JobJars

    @property
    def IsLocalFiles(self):
        return self._IsLocalFiles

    @IsLocalFiles.setter
    def IsLocalFiles(self, IsLocalFiles):
        self._IsLocalFiles = IsLocalFiles

    @property
    def JobFiles(self):
        return self._JobFiles

    @JobFiles.setter
    def JobFiles(self, JobFiles):
        self._JobFiles = JobFiles

    @property
    def JobDriverSize(self):
        return self._JobDriverSize

    @JobDriverSize.setter
    def JobDriverSize(self, JobDriverSize):
        self._JobDriverSize = JobDriverSize

    @property
    def JobExecutorSize(self):
        return self._JobExecutorSize

    @JobExecutorSize.setter
    def JobExecutorSize(self, JobExecutorSize):
        self._JobExecutorSize = JobExecutorSize

    @property
    def JobExecutorNums(self):
        return self._JobExecutorNums

    @JobExecutorNums.setter
    def JobExecutorNums(self, JobExecutorNums):
        self._JobExecutorNums = JobExecutorNums

    @property
    def JobMaxAttempts(self):
        return self._JobMaxAttempts

    @JobMaxAttempts.setter
    def JobMaxAttempts(self, JobMaxAttempts):
        self._JobMaxAttempts = JobMaxAttempts

    @property
    def JobCreator(self):
        return self._JobCreator

    @JobCreator.setter
    def JobCreator(self, JobCreator):
        self._JobCreator = JobCreator

    @property
    def JobCreateTime(self):
        return self._JobCreateTime

    @JobCreateTime.setter
    def JobCreateTime(self, JobCreateTime):
        self._JobCreateTime = JobCreateTime

    @property
    def JobUpdateTime(self):
        return self._JobUpdateTime

    @JobUpdateTime.setter
    def JobUpdateTime(self, JobUpdateTime):
        self._JobUpdateTime = JobUpdateTime

    @property
    def CurrentTaskId(self):
        return self._CurrentTaskId

    @CurrentTaskId.setter
    def CurrentTaskId(self, CurrentTaskId):
        self._CurrentTaskId = CurrentTaskId

    @property
    def JobStatus(self):
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def StreamingStat(self):
        return self._StreamingStat

    @StreamingStat.setter
    def StreamingStat(self, StreamingStat):
        self._StreamingStat = StreamingStat

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def IsLocalPythonFiles(self):
        return self._IsLocalPythonFiles

    @IsLocalPythonFiles.setter
    def IsLocalPythonFiles(self, IsLocalPythonFiles):
        self._IsLocalPythonFiles = IsLocalPythonFiles

    @property
    def AppPythonFiles(self):
        return self._AppPythonFiles

    @AppPythonFiles.setter
    def AppPythonFiles(self, AppPythonFiles):
        self._AppPythonFiles = AppPythonFiles

    @property
    def IsLocalArchives(self):
        return self._IsLocalArchives

    @IsLocalArchives.setter
    def IsLocalArchives(self, IsLocalArchives):
        self._IsLocalArchives = IsLocalArchives

    @property
    def JobArchives(self):
        return self._JobArchives

    @JobArchives.setter
    def JobArchives(self, JobArchives):
        self._JobArchives = JobArchives

    @property
    def SparkImage(self):
        return self._SparkImage

    @SparkImage.setter
    def SparkImage(self, SparkImage):
        self._SparkImage = SparkImage

    @property
    def JobPythonFiles(self):
        return self._JobPythonFiles

    @JobPythonFiles.setter
    def JobPythonFiles(self, JobPythonFiles):
        self._JobPythonFiles = JobPythonFiles

    @property
    def TaskNum(self):
        return self._TaskNum

    @TaskNum.setter
    def TaskNum(self, TaskNum):
        self._TaskNum = TaskNum

    @property
    def DataEngineStatus(self):
        return self._DataEngineStatus

    @DataEngineStatus.setter
    def DataEngineStatus(self, DataEngineStatus):
        self._DataEngineStatus = DataEngineStatus

    @property
    def JobExecutorMaxNumbers(self):
        return self._JobExecutorMaxNumbers

    @JobExecutorMaxNumbers.setter
    def JobExecutorMaxNumbers(self, JobExecutorMaxNumbers):
        self._JobExecutorMaxNumbers = JobExecutorMaxNumbers

    @property
    def SparkImageVersion(self):
        return self._SparkImageVersion

    @SparkImageVersion.setter
    def SparkImageVersion(self, SparkImageVersion):
        self._SparkImageVersion = SparkImageVersion

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def DataEngineClusterType(self):
        return self._DataEngineClusterType

    @DataEngineClusterType.setter
    def DataEngineClusterType(self, DataEngineClusterType):
        self._DataEngineClusterType = DataEngineClusterType

    @property
    def DataEngineImageVersion(self):
        return self._DataEngineImageVersion

    @DataEngineImageVersion.setter
    def DataEngineImageVersion(self, DataEngineImageVersion):
        self._DataEngineImageVersion = DataEngineImageVersion

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit

    @property
    def IsSessionStarted(self):
        return self._IsSessionStarted

    @IsSessionStarted.setter
    def IsSessionStarted(self, IsSessionStarted):
        self._IsSessionStarted = IsSessionStarted

    @property
    def EngineTypeDetail(self):
        return self._EngineTypeDetail

    @EngineTypeDetail.setter
    def EngineTypeDetail(self, EngineTypeDetail):
        self._EngineTypeDetail = EngineTypeDetail


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._JobType = params.get("JobType")
        self._DataEngine = params.get("DataEngine")
        self._Eni = params.get("Eni")
        self._IsLocal = params.get("IsLocal")
        self._JobFile = params.get("JobFile")
        self._RoleArn = params.get("RoleArn")
        self._MainClass = params.get("MainClass")
        self._CmdArgs = params.get("CmdArgs")
        self._JobConf = params.get("JobConf")
        self._IsLocalJars = params.get("IsLocalJars")
        self._JobJars = params.get("JobJars")
        self._IsLocalFiles = params.get("IsLocalFiles")
        self._JobFiles = params.get("JobFiles")
        self._JobDriverSize = params.get("JobDriverSize")
        self._JobExecutorSize = params.get("JobExecutorSize")
        self._JobExecutorNums = params.get("JobExecutorNums")
        self._JobMaxAttempts = params.get("JobMaxAttempts")
        self._JobCreator = params.get("JobCreator")
        self._JobCreateTime = params.get("JobCreateTime")
        self._JobUpdateTime = params.get("JobUpdateTime")
        self._CurrentTaskId = params.get("CurrentTaskId")
        self._JobStatus = params.get("JobStatus")
        if params.get("StreamingStat") is not None:
            self._StreamingStat = StreamingStatistics()
            self._StreamingStat._deserialize(params.get("StreamingStat"))
        self._DataSource = params.get("DataSource")
        self._IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self._AppPythonFiles = params.get("AppPythonFiles")
        self._IsLocalArchives = params.get("IsLocalArchives")
        self._JobArchives = params.get("JobArchives")
        self._SparkImage = params.get("SparkImage")
        self._JobPythonFiles = params.get("JobPythonFiles")
        self._TaskNum = params.get("TaskNum")
        self._DataEngineStatus = params.get("DataEngineStatus")
        self._JobExecutorMaxNumbers = params.get("JobExecutorMaxNumbers")
        self._SparkImageVersion = params.get("SparkImageVersion")
        self._SessionId = params.get("SessionId")
        self._DataEngineClusterType = params.get("DataEngineClusterType")
        self._DataEngineImageVersion = params.get("DataEngineImageVersion")
        self._IsInherit = params.get("IsInherit")
        self._IsSessionStarted = params.get("IsSessionStarted")
        self._EngineTypeDetail = params.get("EngineTypeDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkMonitorMetrics(AbstractModel):
    """Spark监控数据

    """

    def __init__(self):
        r"""
        :param _ShuffleWriteBytesCos: shuffle写溢出到COS数据量，单位：byte
注意：此字段可能返回 null，表示取不到有效值。
        :type ShuffleWriteBytesCos: int
        :param _ShuffleWriteBytesTotal: shuffle写数据量，单位：byte
注意：此字段可能返回 null，表示取不到有效值。
        :type ShuffleWriteBytesTotal: int
        """
        self._ShuffleWriteBytesCos = None
        self._ShuffleWriteBytesTotal = None

    @property
    def ShuffleWriteBytesCos(self):
        return self._ShuffleWriteBytesCos

    @ShuffleWriteBytesCos.setter
    def ShuffleWriteBytesCos(self, ShuffleWriteBytesCos):
        self._ShuffleWriteBytesCos = ShuffleWriteBytesCos

    @property
    def ShuffleWriteBytesTotal(self):
        return self._ShuffleWriteBytesTotal

    @ShuffleWriteBytesTotal.setter
    def ShuffleWriteBytesTotal(self, ShuffleWriteBytesTotal):
        self._ShuffleWriteBytesTotal = ShuffleWriteBytesTotal


    def _deserialize(self, params):
        self._ShuffleWriteBytesCos = params.get("ShuffleWriteBytesCos")
        self._ShuffleWriteBytesTotal = params.get("ShuffleWriteBytesTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkSessionBatchLog(AbstractModel):
    """SparkSQL批任务运行日志

    """

    def __init__(self):
        r"""
        :param _Step: 日志步骤：BEG/CS/DS/DSS/DSF/FINF/RTO/CANCEL/CT/DT/DTS/DTF/FINT/EXCE
注意：此字段可能返回 null，表示取不到有效值。
        :type Step: str
        :param _Time: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param _Message: 日志提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Operate: 日志操作
注意：此字段可能返回 null，表示取不到有效值。
        :type Operate: list of SparkSessionBatchLogOperate
        """
        self._Step = None
        self._Time = None
        self._Message = None
        self._Operate = None

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate


    def _deserialize(self, params):
        self._Step = params.get("Step")
        self._Time = params.get("Time")
        self._Message = params.get("Message")
        if params.get("Operate") is not None:
            self._Operate = []
            for item in params.get("Operate"):
                obj = SparkSessionBatchLogOperate()
                obj._deserialize(item)
                self._Operate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkSessionBatchLogOperate(AbstractModel):
    """SparkSQL批任务日志操作信息。

    """

    def __init__(self):
        r"""
        :param _Text: 操作提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Operate: 操作类型：COPY、LOG、UI、RESULT、List、TAB
注意：此字段可能返回 null，表示取不到有效值。
        :type Operate: str
        :param _Supplement: 补充信息：如：taskid、sessionid、sparkui等
注意：此字段可能返回 null，表示取不到有效值。
        :type Supplement: list of KVPair
        """
        self._Text = None
        self._Operate = None
        self._Supplement = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def Supplement(self):
        return self._Supplement

    @Supplement.setter
    def Supplement(self, Supplement):
        self._Supplement = Supplement


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Operate = params.get("Operate")
        if params.get("Supplement") is not None:
            self._Supplement = []
            for item in params.get("Supplement"):
                obj = KVPair()
                obj._deserialize(item)
                self._Supplement.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatementInformation(AbstractModel):
    """statement信息

    """

    def __init__(self):
        r"""
        :param _TaskId: SQL任务唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _SQL: SQL内容
注意：此字段可能返回 null，表示取不到有效值。
        :type SQL: str
        """
        self._TaskId = None
        self._SQL = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SQL = params.get("SQL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatementOutput(AbstractModel):
    """notebook session statement输出信息。

    """

    def __init__(self):
        r"""
        :param _ExecutionCount: 执行总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionCount: int
        :param _Data: Statement数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of KVPair
        :param _Status: Statement状态:ok,error
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ErrorName: 错误名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorName: str
        :param _ErrorValue: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorValue: str
        :param _ErrorMessage: 错误堆栈信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: list of str
        :param _SQLResult: SQL类型任务结果返回
注意：此字段可能返回 null，表示取不到有效值。
        :type SQLResult: str
        """
        self._ExecutionCount = None
        self._Data = None
        self._Status = None
        self._ErrorName = None
        self._ErrorValue = None
        self._ErrorMessage = None
        self._SQLResult = None

    @property
    def ExecutionCount(self):
        return self._ExecutionCount

    @ExecutionCount.setter
    def ExecutionCount(self, ExecutionCount):
        self._ExecutionCount = ExecutionCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorName(self):
        return self._ErrorName

    @ErrorName.setter
    def ErrorName(self, ErrorName):
        self._ErrorName = ErrorName

    @property
    def ErrorValue(self):
        return self._ErrorValue

    @ErrorValue.setter
    def ErrorValue(self, ErrorValue):
        self._ErrorValue = ErrorValue

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def SQLResult(self):
        return self._SQLResult

    @SQLResult.setter
    def SQLResult(self, SQLResult):
        self._SQLResult = SQLResult


    def _deserialize(self, params):
        self._ExecutionCount = params.get("ExecutionCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KVPair()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Status = params.get("Status")
        self._ErrorName = params.get("ErrorName")
        self._ErrorValue = params.get("ErrorValue")
        self._ErrorMessage = params.get("ErrorMessage")
        self._SQLResult = params.get("SQLResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamingStatistics(AbstractModel):
    """spark流任务统计信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 任务开始时间
        :type StartTime: str
        :param _Receivers: 数据接收器数
        :type Receivers: int
        :param _NumActiveReceivers: 运行中的接收器数
        :type NumActiveReceivers: int
        :param _NumInactiveReceivers: 不活跃的接收器数
        :type NumInactiveReceivers: int
        :param _NumActiveBatches: 运行中的批数
        :type NumActiveBatches: int
        :param _NumRetainedCompletedBatches: 待处理的批数
        :type NumRetainedCompletedBatches: int
        :param _NumTotalCompletedBatches: 已完成的批数
        :type NumTotalCompletedBatches: int
        :param _AverageInputRate: 平均输入速率
        :type AverageInputRate: float
        :param _AverageSchedulingDelay: 平均等待时长
        :type AverageSchedulingDelay: float
        :param _AverageProcessingTime: 平均处理时长
        :type AverageProcessingTime: float
        :param _AverageTotalDelay: 平均延时
        :type AverageTotalDelay: float
        """
        self._StartTime = None
        self._Receivers = None
        self._NumActiveReceivers = None
        self._NumInactiveReceivers = None
        self._NumActiveBatches = None
        self._NumRetainedCompletedBatches = None
        self._NumTotalCompletedBatches = None
        self._AverageInputRate = None
        self._AverageSchedulingDelay = None
        self._AverageProcessingTime = None
        self._AverageTotalDelay = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def NumActiveReceivers(self):
        return self._NumActiveReceivers

    @NumActiveReceivers.setter
    def NumActiveReceivers(self, NumActiveReceivers):
        self._NumActiveReceivers = NumActiveReceivers

    @property
    def NumInactiveReceivers(self):
        return self._NumInactiveReceivers

    @NumInactiveReceivers.setter
    def NumInactiveReceivers(self, NumInactiveReceivers):
        self._NumInactiveReceivers = NumInactiveReceivers

    @property
    def NumActiveBatches(self):
        return self._NumActiveBatches

    @NumActiveBatches.setter
    def NumActiveBatches(self, NumActiveBatches):
        self._NumActiveBatches = NumActiveBatches

    @property
    def NumRetainedCompletedBatches(self):
        return self._NumRetainedCompletedBatches

    @NumRetainedCompletedBatches.setter
    def NumRetainedCompletedBatches(self, NumRetainedCompletedBatches):
        self._NumRetainedCompletedBatches = NumRetainedCompletedBatches

    @property
    def NumTotalCompletedBatches(self):
        return self._NumTotalCompletedBatches

    @NumTotalCompletedBatches.setter
    def NumTotalCompletedBatches(self, NumTotalCompletedBatches):
        self._NumTotalCompletedBatches = NumTotalCompletedBatches

    @property
    def AverageInputRate(self):
        return self._AverageInputRate

    @AverageInputRate.setter
    def AverageInputRate(self, AverageInputRate):
        self._AverageInputRate = AverageInputRate

    @property
    def AverageSchedulingDelay(self):
        return self._AverageSchedulingDelay

    @AverageSchedulingDelay.setter
    def AverageSchedulingDelay(self, AverageSchedulingDelay):
        self._AverageSchedulingDelay = AverageSchedulingDelay

    @property
    def AverageProcessingTime(self):
        return self._AverageProcessingTime

    @AverageProcessingTime.setter
    def AverageProcessingTime(self, AverageProcessingTime):
        self._AverageProcessingTime = AverageProcessingTime

    @property
    def AverageTotalDelay(self):
        return self._AverageTotalDelay

    @AverageTotalDelay.setter
    def AverageTotalDelay(self, AverageTotalDelay):
        self._AverageTotalDelay = AverageTotalDelay


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Receivers = params.get("Receivers")
        self._NumActiveReceivers = params.get("NumActiveReceivers")
        self._NumInactiveReceivers = params.get("NumInactiveReceivers")
        self._NumActiveBatches = params.get("NumActiveBatches")
        self._NumRetainedCompletedBatches = params.get("NumRetainedCompletedBatches")
        self._NumTotalCompletedBatches = params.get("NumTotalCompletedBatches")
        self._AverageInputRate = params.get("AverageInputRate")
        self._AverageSchedulingDelay = params.get("AverageSchedulingDelay")
        self._AverageProcessingTime = params.get("AverageProcessingTime")
        self._AverageTotalDelay = params.get("AverageTotalDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendResumeDataEngineRequest(AbstractModel):
    """SuspendResumeDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: 虚拟集群名称
        :type DataEngineName: str
        :param _Operate: 操作类型 suspend/resume
        :type Operate: str
        """
        self._DataEngineName = None
        self._Operate = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendResumeDataEngineResponse(AbstractModel):
    """SuspendResumeDataEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: 虚拟集群详细信息
        :type DataEngineName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataEngineName = None
        self._RequestId = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._RequestId = params.get("RequestId")


class SwitchDataEngineImageRequest(AbstractModel):
    """SwitchDataEngineImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 引擎ID
        :type DataEngineId: str
        :param _NewImageVersionId: 新镜像版本ID
        :type NewImageVersionId: str
        """
        self._DataEngineId = None
        self._NewImageVersionId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def NewImageVersionId(self):
        return self._NewImageVersionId

    @NewImageVersionId.setter
    def NewImageVersionId(self, NewImageVersionId):
        self._NewImageVersionId = NewImageVersionId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        self._NewImageVersionId = params.get("NewImageVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDataEngineImageResponse(AbstractModel):
    """SwitchDataEngineImage返回参数结构体

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


class SwitchDataEngineRequest(AbstractModel):
    """SwitchDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineName: 主集群名称
        :type DataEngineName: str
        :param _StartStandbyCluster: 是否开启备集群
        :type StartStandbyCluster: bool
        """
        self._DataEngineName = None
        self._StartStandbyCluster = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def StartStandbyCluster(self):
        return self._StartStandbyCluster

    @StartStandbyCluster.setter
    def StartStandbyCluster(self, StartStandbyCluster):
        self._StartStandbyCluster = StartStandbyCluster


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._StartStandbyCluster = params.get("StartStandbyCluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDataEngineResponse(AbstractModel):
    """SwitchDataEngine返回参数结构体

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


class TColumn(AbstractModel):
    """表字段描述信息

    """

    def __init__(self):
        r"""
        :param _Name: 字段名称
        :type Name: str
        :param _Type: 字段类型
        :type Type: str
        :param _Comment: 字段描述
        :type Comment: str
        :param _Default: 字段默认值
        :type Default: str
        :param _NotNull: 字段是否是非空
        :type NotNull: bool
        :param _Precision: 表示整个 numeric 的长度,取值1-38
        :type Precision: int
        :param _Scale: 表示小数部分的长度
Scale小于Precision
        :type Scale: int
        """
        self._Name = None
        self._Type = None
        self._Comment = None
        self._Default = None
        self._NotNull = None
        self._Precision = None
        self._Scale = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def NotNull(self):
        return self._NotNull

    @NotNull.setter
    def NotNull(self, NotNull):
        self._NotNull = NotNull

    @property
    def Precision(self):
        return self._Precision

    @Precision.setter
    def Precision(self, Precision):
        self._Precision = Precision

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Comment = params.get("Comment")
        self._Default = params.get("Default")
        self._NotNull = params.get("NotNull")
        self._Precision = params.get("Precision")
        self._Scale = params.get("Scale")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TPartition(AbstractModel):
    """表分区字段信息

    """

    def __init__(self):
        r"""
        :param _Name: 字段名称
        :type Name: str
        :param _Type: 字段类型
        :type Type: str
        :param _Comment: 字段描述
        :type Comment: str
        :param _PartitionType: 分区类型
        :type PartitionType: str
        :param _PartitionFormat: 分区格式
        :type PartitionFormat: str
        :param _PartitionDot: 分区分隔数
        :type PartitionDot: int
        :param _Transform: 分区转换策略
        :type Transform: str
        :param _TransformArgs: 策略参数
        :type TransformArgs: list of str
        """
        self._Name = None
        self._Type = None
        self._Comment = None
        self._PartitionType = None
        self._PartitionFormat = None
        self._PartitionDot = None
        self._Transform = None
        self._TransformArgs = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def PartitionType(self):
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def PartitionFormat(self):
        return self._PartitionFormat

    @PartitionFormat.setter
    def PartitionFormat(self, PartitionFormat):
        self._PartitionFormat = PartitionFormat

    @property
    def PartitionDot(self):
        return self._PartitionDot

    @PartitionDot.setter
    def PartitionDot(self, PartitionDot):
        self._PartitionDot = PartitionDot

    @property
    def Transform(self):
        return self._Transform

    @Transform.setter
    def Transform(self, Transform):
        self._Transform = Transform

    @property
    def TransformArgs(self):
        return self._TransformArgs

    @TransformArgs.setter
    def TransformArgs(self, TransformArgs):
        self._TransformArgs = TransformArgs


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Comment = params.get("Comment")
        self._PartitionType = params.get("PartitionType")
        self._PartitionFormat = params.get("PartitionFormat")
        self._PartitionDot = params.get("PartitionDot")
        self._Transform = params.get("Transform")
        self._TransformArgs = params.get("TransformArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableBaseInfo(AbstractModel):
    """数据表配置信息

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 该数据表所属数据库名字
        :type DatabaseName: str
        :param _TableName: 数据表名字
        :type TableName: str
        :param _DatasourceConnectionName: 该数据表所属数据源名字
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionName: str
        :param _TableComment: 该数据表备注
注意：此字段可能返回 null，表示取不到有效值。
        :type TableComment: str
        :param _Type: 具体类型，表or视图
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _TableFormat: 数据格式类型，hive，iceberg等
注意：此字段可能返回 null，表示取不到有效值。
        :type TableFormat: str
        :param _UserAlias: 建表用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param _UserSubUin: 建表用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSubUin: str
        :param _GovernPolicy: 数据治理配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type GovernPolicy: :class:`tencentcloud.dlc.v20210125.models.DataGovernPolicy`
        :param _DbGovernPolicyIsDisable: 库数据治理是否关闭，关闭：true，开启：false
注意：此字段可能返回 null，表示取不到有效值。
        :type DbGovernPolicyIsDisable: str
        :param _SmartPolicy: 智能数据治理配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartPolicy: :class:`tencentcloud.dlc.v20210125.models.SmartPolicy`
        """
        self._DatabaseName = None
        self._TableName = None
        self._DatasourceConnectionName = None
        self._TableComment = None
        self._Type = None
        self._TableFormat = None
        self._UserAlias = None
        self._UserSubUin = None
        self._GovernPolicy = None
        self._DbGovernPolicyIsDisable = None
        self._SmartPolicy = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def TableComment(self):
        return self._TableComment

    @TableComment.setter
    def TableComment(self, TableComment):
        self._TableComment = TableComment

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TableFormat(self):
        return self._TableFormat

    @TableFormat.setter
    def TableFormat(self, TableFormat):
        self._TableFormat = TableFormat

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def UserSubUin(self):
        return self._UserSubUin

    @UserSubUin.setter
    def UserSubUin(self, UserSubUin):
        self._UserSubUin = UserSubUin

    @property
    def GovernPolicy(self):
        warnings.warn("parameter `GovernPolicy` is deprecated", DeprecationWarning) 

        return self._GovernPolicy

    @GovernPolicy.setter
    def GovernPolicy(self, GovernPolicy):
        warnings.warn("parameter `GovernPolicy` is deprecated", DeprecationWarning) 

        self._GovernPolicy = GovernPolicy

    @property
    def DbGovernPolicyIsDisable(self):
        warnings.warn("parameter `DbGovernPolicyIsDisable` is deprecated", DeprecationWarning) 

        return self._DbGovernPolicyIsDisable

    @DbGovernPolicyIsDisable.setter
    def DbGovernPolicyIsDisable(self, DbGovernPolicyIsDisable):
        warnings.warn("parameter `DbGovernPolicyIsDisable` is deprecated", DeprecationWarning) 

        self._DbGovernPolicyIsDisable = DbGovernPolicyIsDisable

    @property
    def SmartPolicy(self):
        return self._SmartPolicy

    @SmartPolicy.setter
    def SmartPolicy(self, SmartPolicy):
        self._SmartPolicy = SmartPolicy


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._TableComment = params.get("TableComment")
        self._Type = params.get("Type")
        self._TableFormat = params.get("TableFormat")
        self._UserAlias = params.get("UserAlias")
        self._UserSubUin = params.get("UserSubUin")
        if params.get("GovernPolicy") is not None:
            self._GovernPolicy = DataGovernPolicy()
            self._GovernPolicy._deserialize(params.get("GovernPolicy"))
        self._DbGovernPolicyIsDisable = params.get("DbGovernPolicyIsDisable")
        if params.get("SmartPolicy") is not None:
            self._SmartPolicy = SmartPolicy()
            self._SmartPolicy._deserialize(params.get("SmartPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfo(AbstractModel):
    """返回数据表的相关信息。

    """

    def __init__(self):
        r"""
        :param _TableBaseInfo: 数据表配置信息。
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param _DataFormat: 数据表格式。每次入参可选如下其一的KV结构，[TextFile，CSV，Json, Parquet, ORC, AVRD]。
        :type DataFormat: :class:`tencentcloud.dlc.v20210125.models.DataFormat`
        :param _Columns: 数据表列信息。
        :type Columns: list of Column
        :param _Partitions: 数据表分块信息。
        :type Partitions: list of Partition
        :param _Location: 数据存储路径。当前仅支持cos路径，格式如下：cosn://bucket-name/filepath。
        :type Location: str
        """
        self._TableBaseInfo = None
        self._DataFormat = None
        self._Columns = None
        self._Partitions = None
        self._Location = None

    @property
    def TableBaseInfo(self):
        return self._TableBaseInfo

    @TableBaseInfo.setter
    def TableBaseInfo(self, TableBaseInfo):
        self._TableBaseInfo = TableBaseInfo

    @property
    def DataFormat(self):
        return self._DataFormat

    @DataFormat.setter
    def DataFormat(self, DataFormat):
        self._DataFormat = DataFormat

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self._TableBaseInfo = TableBaseInfo()
            self._TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("DataFormat") is not None:
            self._DataFormat = DataFormat()
            self._DataFormat._deserialize(params.get("DataFormat"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = Partition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableResponseInfo(AbstractModel):
    """查询表信息对象

    """

    def __init__(self):
        r"""
        :param _TableBaseInfo: 数据表基本信息。
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param _Columns: 数据表列信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param _Partitions: 数据表分块信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of Partition
        :param _Location: 数据存储路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param _Properties: 数据表属性信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param _ModifiedTime: 数据表更新时间, 单位: ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _CreateTime: 数据表创建时间,单位: ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _InputFormat: 数据格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputFormat: str
        :param _StorageSize: 数据表存储大小（单位：Byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSize: int
        :param _RecordCount: 数据表行数
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCount: int
        :param _MapMaterializedViewName: xxxx
注意：此字段可能返回 null，表示取不到有效值。
        :type MapMaterializedViewName: str
        :param _HeatValue: 访问热点
注意：此字段可能返回 null，表示取不到有效值。
        :type HeatValue: int
        """
        self._TableBaseInfo = None
        self._Columns = None
        self._Partitions = None
        self._Location = None
        self._Properties = None
        self._ModifiedTime = None
        self._CreateTime = None
        self._InputFormat = None
        self._StorageSize = None
        self._RecordCount = None
        self._MapMaterializedViewName = None
        self._HeatValue = None

    @property
    def TableBaseInfo(self):
        return self._TableBaseInfo

    @TableBaseInfo.setter
    def TableBaseInfo(self, TableBaseInfo):
        self._TableBaseInfo = TableBaseInfo

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InputFormat(self):
        return self._InputFormat

    @InputFormat.setter
    def InputFormat(self, InputFormat):
        self._InputFormat = InputFormat

    @property
    def StorageSize(self):
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def MapMaterializedViewName(self):
        return self._MapMaterializedViewName

    @MapMaterializedViewName.setter
    def MapMaterializedViewName(self, MapMaterializedViewName):
        self._MapMaterializedViewName = MapMaterializedViewName

    @property
    def HeatValue(self):
        return self._HeatValue

    @HeatValue.setter
    def HeatValue(self, HeatValue):
        self._HeatValue = HeatValue


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self._TableBaseInfo = TableBaseInfo()
            self._TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = Partition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._Location = params.get("Location")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._ModifiedTime = params.get("ModifiedTime")
        self._CreateTime = params.get("CreateTime")
        self._InputFormat = params.get("InputFormat")
        self._StorageSize = params.get("StorageSize")
        self._RecordCount = params.get("RecordCount")
        self._MapMaterializedViewName = params.get("MapMaterializedViewName")
        self._HeatValue = params.get("HeatValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签对信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """任务类型，任务如SQL查询等。

    """

    def __init__(self):
        r"""
        :param _SQLTask: SQL查询任务
        :type SQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`
        :param _SparkSQLTask: Spark SQL查询任务
        :type SparkSQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`
        """
        self._SQLTask = None
        self._SparkSQLTask = None

    @property
    def SQLTask(self):
        return self._SQLTask

    @SQLTask.setter
    def SQLTask(self, SQLTask):
        self._SQLTask = SQLTask

    @property
    def SparkSQLTask(self):
        return self._SparkSQLTask

    @SparkSQLTask.setter
    def SparkSQLTask(self, SparkSQLTask):
        self._SparkSQLTask = SparkSQLTask


    def _deserialize(self, params):
        if params.get("SQLTask") is not None:
            self._SQLTask = SQLTask()
            self._SQLTask._deserialize(params.get("SQLTask"))
        if params.get("SparkSQLTask") is not None:
            self._SparkSQLTask = SQLTask()
            self._SparkSQLTask._deserialize(params.get("SparkSQLTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResponseInfo(AbstractModel):
    """任务实例。

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 任务所属Database的名称。
        :type DatabaseName: str
        :param _DataAmount: 任务数据量。
        :type DataAmount: int
        :param _Id: 任务Id。
        :type Id: str
        :param _UsedTime: 计算耗时，单位： ms
        :type UsedTime: int
        :param _OutputPath: 任务输出路径。
        :type OutputPath: str
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _State: 任务状态：0 初始化， 1 执行中， 2 执行成功，3 数据写入中，4 排队中。-1 执行失败，-3 已取消。
        :type State: int
        :param _SQLType: 任务SQL类型，DDL|DML等
        :type SQLType: str
        :param _SQL: 任务SQL语句
        :type SQL: str
        :param _ResultExpired: 结果是否过期。
        :type ResultExpired: bool
        :param _RowAffectInfo: 数据影响统计信息。
        :type RowAffectInfo: str
        :param _DataSet: 任务结果数据表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSet: str
        :param _Error: 失败信息, 例如：errorMessage。该字段已废弃。
        :type Error: str
        :param _Percentage: 任务执行进度num/100(%)
        :type Percentage: int
        :param _OutputMessage: 任务执行输出信息。
        :type OutputMessage: str
        :param _TaskType: 执行SQL的引擎类型
        :type TaskType: str
        :param _ProgressDetail: 任务进度明细
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgressDetail: str
        :param _UpdateTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _DataEngineId: 计算资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineId: str
        :param _OperateUin: 执行sql的子uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUin: str
        :param _DataEngineName: 计算资源名字
注意：此字段可能返回 null，表示取不到有效值。
        :type DataEngineName: str
        :param _InputType: 导入类型是本地导入还是cos
注意：此字段可能返回 null，表示取不到有效值。
        :type InputType: str
        :param _InputConf: 导入配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InputConf: str
        :param _DataNumber: 数据条数
注意：此字段可能返回 null，表示取不到有效值。
        :type DataNumber: int
        :param _CanDownload: 查询数据能不能下载
注意：此字段可能返回 null，表示取不到有效值。
        :type CanDownload: bool
        :param _UserAlias: 用户别名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param _SparkJobName: spark应用作业名
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkJobName: str
        :param _SparkJobId: spark应用作业Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkJobId: str
        :param _SparkJobFile: spark应用入口jar文件
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkJobFile: str
        :param _UiUrl: spark ui url
注意：此字段可能返回 null，表示取不到有效值。
        :type UiUrl: str
        :param _TotalTime: 任务耗时，单位： ms
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTime: int
        :param _CmdArgs: spark app job执行task的程序入口参数
注意：此字段可能返回 null，表示取不到有效值。
        :type CmdArgs: str
        :param _ImageVersion: 集群镜像大版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageVersion: str
        :param _DriverSize: driver规格：small,medium,large,xlarge；内存型(引擎类型)：m.small,m.medium,m.large,m.xlarge
注意：此字段可能返回 null，表示取不到有效值。
        :type DriverSize: str
        :param _ExecutorSize: executor规格：small,medium,large,xlarge；内存型(引擎类型)：m.small,m.medium,m.large,m.xlarge
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorSize: str
        :param _ExecutorNums: 指定executor数量，最小值为1，最大值小于集群规格
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorNums: int
        :param _ExecutorMaxNumbers: 指定executor max数量（动态配置场景下），最小值为1，最大值小于集群规格（当ExecutorMaxNumbers小于ExecutorNums时，改值设定为ExecutorNums）
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorMaxNumbers: int
        :param _CommonMetrics: 任务公共指标数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonMetrics: :class:`tencentcloud.dlc.v20210125.models.CommonMetrics`
        :param _SparkMonitorMetrics: spark任务指标数据
注意：此字段可能返回 null，表示取不到有效值。
        :type SparkMonitorMetrics: :class:`tencentcloud.dlc.v20210125.models.SparkMonitorMetrics`
        :param _PrestoMonitorMetrics: presto任务指标数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PrestoMonitorMetrics: :class:`tencentcloud.dlc.v20210125.models.PrestoMonitorMetrics`
        :param _ResultFormat: 结果文件格式：默认为csv
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultFormat: str
        :param _EngineTypeDetail: 引擎类型，SparkSQL：SparkSQL 引擎；SparkBatch：Spark作业引擎；PrestoSQL：Presto引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineTypeDetail: str
        :param _ResourceGroupName: spark引擎资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        """
        self._DatabaseName = None
        self._DataAmount = None
        self._Id = None
        self._UsedTime = None
        self._OutputPath = None
        self._CreateTime = None
        self._State = None
        self._SQLType = None
        self._SQL = None
        self._ResultExpired = None
        self._RowAffectInfo = None
        self._DataSet = None
        self._Error = None
        self._Percentage = None
        self._OutputMessage = None
        self._TaskType = None
        self._ProgressDetail = None
        self._UpdateTime = None
        self._DataEngineId = None
        self._OperateUin = None
        self._DataEngineName = None
        self._InputType = None
        self._InputConf = None
        self._DataNumber = None
        self._CanDownload = None
        self._UserAlias = None
        self._SparkJobName = None
        self._SparkJobId = None
        self._SparkJobFile = None
        self._UiUrl = None
        self._TotalTime = None
        self._CmdArgs = None
        self._ImageVersion = None
        self._DriverSize = None
        self._ExecutorSize = None
        self._ExecutorNums = None
        self._ExecutorMaxNumbers = None
        self._CommonMetrics = None
        self._SparkMonitorMetrics = None
        self._PrestoMonitorMetrics = None
        self._ResultFormat = None
        self._EngineTypeDetail = None
        self._ResourceGroupName = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DataAmount(self):
        return self._DataAmount

    @DataAmount.setter
    def DataAmount(self, DataAmount):
        self._DataAmount = DataAmount

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UsedTime(self):
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def OutputPath(self):
        return self._OutputPath

    @OutputPath.setter
    def OutputPath(self, OutputPath):
        self._OutputPath = OutputPath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def SQLType(self):
        return self._SQLType

    @SQLType.setter
    def SQLType(self, SQLType):
        self._SQLType = SQLType

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL

    @property
    def ResultExpired(self):
        return self._ResultExpired

    @ResultExpired.setter
    def ResultExpired(self, ResultExpired):
        self._ResultExpired = ResultExpired

    @property
    def RowAffectInfo(self):
        return self._RowAffectInfo

    @RowAffectInfo.setter
    def RowAffectInfo(self, RowAffectInfo):
        self._RowAffectInfo = RowAffectInfo

    @property
    def DataSet(self):
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage

    @property
    def OutputMessage(self):
        return self._OutputMessage

    @OutputMessage.setter
    def OutputMessage(self, OutputMessage):
        self._OutputMessage = OutputMessage

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ProgressDetail(self):
        return self._ProgressDetail

    @ProgressDetail.setter
    def ProgressDetail(self, ProgressDetail):
        self._ProgressDetail = ProgressDetail

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def InputConf(self):
        return self._InputConf

    @InputConf.setter
    def InputConf(self, InputConf):
        self._InputConf = InputConf

    @property
    def DataNumber(self):
        return self._DataNumber

    @DataNumber.setter
    def DataNumber(self, DataNumber):
        self._DataNumber = DataNumber

    @property
    def CanDownload(self):
        return self._CanDownload

    @CanDownload.setter
    def CanDownload(self, CanDownload):
        self._CanDownload = CanDownload

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def SparkJobName(self):
        return self._SparkJobName

    @SparkJobName.setter
    def SparkJobName(self, SparkJobName):
        self._SparkJobName = SparkJobName

    @property
    def SparkJobId(self):
        return self._SparkJobId

    @SparkJobId.setter
    def SparkJobId(self, SparkJobId):
        self._SparkJobId = SparkJobId

    @property
    def SparkJobFile(self):
        return self._SparkJobFile

    @SparkJobFile.setter
    def SparkJobFile(self, SparkJobFile):
        self._SparkJobFile = SparkJobFile

    @property
    def UiUrl(self):
        return self._UiUrl

    @UiUrl.setter
    def UiUrl(self, UiUrl):
        self._UiUrl = UiUrl

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def DriverSize(self):
        return self._DriverSize

    @DriverSize.setter
    def DriverSize(self, DriverSize):
        self._DriverSize = DriverSize

    @property
    def ExecutorSize(self):
        return self._ExecutorSize

    @ExecutorSize.setter
    def ExecutorSize(self, ExecutorSize):
        self._ExecutorSize = ExecutorSize

    @property
    def ExecutorNums(self):
        return self._ExecutorNums

    @ExecutorNums.setter
    def ExecutorNums(self, ExecutorNums):
        self._ExecutorNums = ExecutorNums

    @property
    def ExecutorMaxNumbers(self):
        return self._ExecutorMaxNumbers

    @ExecutorMaxNumbers.setter
    def ExecutorMaxNumbers(self, ExecutorMaxNumbers):
        self._ExecutorMaxNumbers = ExecutorMaxNumbers

    @property
    def CommonMetrics(self):
        return self._CommonMetrics

    @CommonMetrics.setter
    def CommonMetrics(self, CommonMetrics):
        self._CommonMetrics = CommonMetrics

    @property
    def SparkMonitorMetrics(self):
        return self._SparkMonitorMetrics

    @SparkMonitorMetrics.setter
    def SparkMonitorMetrics(self, SparkMonitorMetrics):
        self._SparkMonitorMetrics = SparkMonitorMetrics

    @property
    def PrestoMonitorMetrics(self):
        return self._PrestoMonitorMetrics

    @PrestoMonitorMetrics.setter
    def PrestoMonitorMetrics(self, PrestoMonitorMetrics):
        self._PrestoMonitorMetrics = PrestoMonitorMetrics

    @property
    def ResultFormat(self):
        return self._ResultFormat

    @ResultFormat.setter
    def ResultFormat(self, ResultFormat):
        self._ResultFormat = ResultFormat

    @property
    def EngineTypeDetail(self):
        return self._EngineTypeDetail

    @EngineTypeDetail.setter
    def EngineTypeDetail(self, EngineTypeDetail):
        self._EngineTypeDetail = EngineTypeDetail

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._DataAmount = params.get("DataAmount")
        self._Id = params.get("Id")
        self._UsedTime = params.get("UsedTime")
        self._OutputPath = params.get("OutputPath")
        self._CreateTime = params.get("CreateTime")
        self._State = params.get("State")
        self._SQLType = params.get("SQLType")
        self._SQL = params.get("SQL")
        self._ResultExpired = params.get("ResultExpired")
        self._RowAffectInfo = params.get("RowAffectInfo")
        self._DataSet = params.get("DataSet")
        self._Error = params.get("Error")
        self._Percentage = params.get("Percentage")
        self._OutputMessage = params.get("OutputMessage")
        self._TaskType = params.get("TaskType")
        self._ProgressDetail = params.get("ProgressDetail")
        self._UpdateTime = params.get("UpdateTime")
        self._DataEngineId = params.get("DataEngineId")
        self._OperateUin = params.get("OperateUin")
        self._DataEngineName = params.get("DataEngineName")
        self._InputType = params.get("InputType")
        self._InputConf = params.get("InputConf")
        self._DataNumber = params.get("DataNumber")
        self._CanDownload = params.get("CanDownload")
        self._UserAlias = params.get("UserAlias")
        self._SparkJobName = params.get("SparkJobName")
        self._SparkJobId = params.get("SparkJobId")
        self._SparkJobFile = params.get("SparkJobFile")
        self._UiUrl = params.get("UiUrl")
        self._TotalTime = params.get("TotalTime")
        self._CmdArgs = params.get("CmdArgs")
        self._ImageVersion = params.get("ImageVersion")
        self._DriverSize = params.get("DriverSize")
        self._ExecutorSize = params.get("ExecutorSize")
        self._ExecutorNums = params.get("ExecutorNums")
        self._ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        if params.get("CommonMetrics") is not None:
            self._CommonMetrics = CommonMetrics()
            self._CommonMetrics._deserialize(params.get("CommonMetrics"))
        if params.get("SparkMonitorMetrics") is not None:
            self._SparkMonitorMetrics = SparkMonitorMetrics()
            self._SparkMonitorMetrics._deserialize(params.get("SparkMonitorMetrics"))
        if params.get("PrestoMonitorMetrics") is not None:
            self._PrestoMonitorMetrics = PrestoMonitorMetrics()
            self._PrestoMonitorMetrics._deserialize(params.get("PrestoMonitorMetrics"))
        self._ResultFormat = params.get("ResultFormat")
        self._EngineTypeDetail = params.get("EngineTypeDetail")
        self._ResourceGroupName = params.get("ResourceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResultInfo(AbstractModel):
    """任务结果信息。

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一ID
        :type TaskId: str
        :param _DatasourceConnectionName: 数据源名称，当前任务执行时候选中的默认数据源
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceConnectionName: str
        :param _DatabaseName: 数据库名称，当前任务执行时候选中的默认数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param _SQL: 当前执行的SQL，一个任务包含一个SQL
        :type SQL: str
        :param _SQLType: 执行任务的类型，现在分为DDL、DML、DQL
        :type SQLType: str
        :param _State: 任务当前的状态，0：初始化 1：任务运行中 2：任务执行成功  3：数据写入中 4：排队中 -1：任务执行失败 -3：用户手动终止 。只有任务执行成功的情况下，才会返回任务执行的结果
        :type State: int
        :param _DataAmount: 扫描的数据量，单位byte
        :type DataAmount: int
        :param _UsedTime: 计算耗时，单位： ms
        :type UsedTime: int
        :param _OutputPath: 任务结果输出的COS桶地址
        :type OutputPath: str
        :param _CreateTime: 任务创建时间，时间戳
        :type CreateTime: str
        :param _OutputMessage: 任务执行信息，成功时返回success，失败时返回失败原因
        :type OutputMessage: str
        :param _RowAffectInfo: 被影响的行数
        :type RowAffectInfo: str
        :param _ResultSchema: 结果的schema信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultSchema: list of Column
        :param _ResultSet: 结果信息，反转义后，外层数组的每个元素为一行数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultSet: str
        :param _NextToken: 分页信息，如果没有更多结果数据，nextToken为空
        :type NextToken: str
        :param _Percentage: 任务执行进度num/100(%)
        :type Percentage: int
        :param _ProgressDetail: 任务进度明细
        :type ProgressDetail: str
        :param _DisplayFormat: 控制台展示格式。table：表格展示 text：文本展示
        :type DisplayFormat: str
        :param _TotalTime: 任务耗时，单位： ms
        :type TotalTime: int
        :param _QueryResultTime: 获取结果消耗的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryResultTime: float
        """
        self._TaskId = None
        self._DatasourceConnectionName = None
        self._DatabaseName = None
        self._SQL = None
        self._SQLType = None
        self._State = None
        self._DataAmount = None
        self._UsedTime = None
        self._OutputPath = None
        self._CreateTime = None
        self._OutputMessage = None
        self._RowAffectInfo = None
        self._ResultSchema = None
        self._ResultSet = None
        self._NextToken = None
        self._Percentage = None
        self._ProgressDetail = None
        self._DisplayFormat = None
        self._TotalTime = None
        self._QueryResultTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL

    @property
    def SQLType(self):
        return self._SQLType

    @SQLType.setter
    def SQLType(self, SQLType):
        self._SQLType = SQLType

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def DataAmount(self):
        return self._DataAmount

    @DataAmount.setter
    def DataAmount(self, DataAmount):
        self._DataAmount = DataAmount

    @property
    def UsedTime(self):
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def OutputPath(self):
        return self._OutputPath

    @OutputPath.setter
    def OutputPath(self, OutputPath):
        self._OutputPath = OutputPath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def OutputMessage(self):
        return self._OutputMessage

    @OutputMessage.setter
    def OutputMessage(self, OutputMessage):
        self._OutputMessage = OutputMessage

    @property
    def RowAffectInfo(self):
        return self._RowAffectInfo

    @RowAffectInfo.setter
    def RowAffectInfo(self, RowAffectInfo):
        self._RowAffectInfo = RowAffectInfo

    @property
    def ResultSchema(self):
        return self._ResultSchema

    @ResultSchema.setter
    def ResultSchema(self, ResultSchema):
        self._ResultSchema = ResultSchema

    @property
    def ResultSet(self):
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage

    @property
    def ProgressDetail(self):
        return self._ProgressDetail

    @ProgressDetail.setter
    def ProgressDetail(self, ProgressDetail):
        self._ProgressDetail = ProgressDetail

    @property
    def DisplayFormat(self):
        return self._DisplayFormat

    @DisplayFormat.setter
    def DisplayFormat(self, DisplayFormat):
        self._DisplayFormat = DisplayFormat

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def QueryResultTime(self):
        return self._QueryResultTime

    @QueryResultTime.setter
    def QueryResultTime(self, QueryResultTime):
        self._QueryResultTime = QueryResultTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._DatabaseName = params.get("DatabaseName")
        self._SQL = params.get("SQL")
        self._SQLType = params.get("SQLType")
        self._State = params.get("State")
        self._DataAmount = params.get("DataAmount")
        self._UsedTime = params.get("UsedTime")
        self._OutputPath = params.get("OutputPath")
        self._CreateTime = params.get("CreateTime")
        self._OutputMessage = params.get("OutputMessage")
        self._RowAffectInfo = params.get("RowAffectInfo")
        if params.get("ResultSchema") is not None:
            self._ResultSchema = []
            for item in params.get("ResultSchema"):
                obj = Column()
                obj._deserialize(item)
                self._ResultSchema.append(obj)
        self._ResultSet = params.get("ResultSet")
        self._NextToken = params.get("NextToken")
        self._Percentage = params.get("Percentage")
        self._ProgressDetail = params.get("ProgressDetail")
        self._DisplayFormat = params.get("DisplayFormat")
        self._TotalTime = params.get("TotalTime")
        self._QueryResultTime = params.get("QueryResultTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TasksInfo(AbstractModel):
    """批量顺序执行任务集合

    """

    def __init__(self):
        r"""
        :param _TaskType: 任务类型，SQLTask：SQL查询任务。SparkSQLTask：Spark SQL查询任务
        :type TaskType: str
        :param _FailureTolerance: 容错策略。Proceed：前面任务出错/取消后继续执行后面的任务。Terminate：前面的任务出错/取消之后终止后面任务的执行，后面的任务全部标记为已取消。
        :type FailureTolerance: str
        :param _SQL: base64加密后的SQL语句，用";"号分隔每个SQL语句，一次最多提交50个任务。严格按照前后顺序执行
        :type SQL: str
        :param _Config: 任务的配置信息，当前仅支持SparkSQLTask任务。
        :type Config: list of KVPair
        :param _Params: 任务的用户自定义参数信息
        :type Params: list of KVPair
        """
        self._TaskType = None
        self._FailureTolerance = None
        self._SQL = None
        self._Config = None
        self._Params = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def FailureTolerance(self):
        return self._FailureTolerance

    @FailureTolerance.setter
    def FailureTolerance(self, FailureTolerance):
        self._FailureTolerance = FailureTolerance

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._FailureTolerance = params.get("FailureTolerance")
        self._SQL = params.get("SQL")
        if params.get("Config") is not None:
            self._Config = []
            for item in params.get("Config"):
                obj = KVPair()
                obj._deserialize(item)
                self._Config.append(obj)
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TasksOverview(AbstractModel):
    """任务概览

    """

    def __init__(self):
        r"""
        :param _TaskQueuedCount: 正在排队的任务个数
        :type TaskQueuedCount: int
        :param _TaskInitCount: 初始化的任务个数
        :type TaskInitCount: int
        :param _TaskRunningCount: 正在执行的任务个数
        :type TaskRunningCount: int
        :param _TotalTaskCount: 当前时间范围的总任务个数
        :type TotalTaskCount: int
        """
        self._TaskQueuedCount = None
        self._TaskInitCount = None
        self._TaskRunningCount = None
        self._TotalTaskCount = None

    @property
    def TaskQueuedCount(self):
        return self._TaskQueuedCount

    @TaskQueuedCount.setter
    def TaskQueuedCount(self, TaskQueuedCount):
        self._TaskQueuedCount = TaskQueuedCount

    @property
    def TaskInitCount(self):
        return self._TaskInitCount

    @TaskInitCount.setter
    def TaskInitCount(self, TaskInitCount):
        self._TaskInitCount = TaskInitCount

    @property
    def TaskRunningCount(self):
        return self._TaskRunningCount

    @TaskRunningCount.setter
    def TaskRunningCount(self, TaskRunningCount):
        self._TaskRunningCount = TaskRunningCount

    @property
    def TotalTaskCount(self):
        return self._TotalTaskCount

    @TotalTaskCount.setter
    def TotalTaskCount(self, TotalTaskCount):
        self._TotalTaskCount = TotalTaskCount


    def _deserialize(self, params):
        self._TaskQueuedCount = params.get("TaskQueuedCount")
        self._TaskInitCount = params.get("TaskInitCount")
        self._TaskRunningCount = params.get("TaskRunningCount")
        self._TotalTaskCount = params.get("TotalTaskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextFile(AbstractModel):
    """文本格式

    """

    def __init__(self):
        r"""
        :param _Format: 文本类型，本参数取值为TextFile。
        :type Format: str
        :param _Regex: 处理文本用的正则表达式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: str
        """
        self._Format = None
        self._Regex = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Format = params.get("Format")
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindWorkGroupsFromUserRequest(AbstractModel):
    """UnbindWorkGroupsFromUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AddInfo: 解绑的工作组Id和用户Id的关联关系
        :type AddInfo: :class:`tencentcloud.dlc.v20210125.models.WorkGroupIdSetOfUserId`
        """
        self._AddInfo = None

    @property
    def AddInfo(self):
        return self._AddInfo

    @AddInfo.setter
    def AddInfo(self, AddInfo):
        self._AddInfo = AddInfo


    def _deserialize(self, params):
        if params.get("AddInfo") is not None:
            self._AddInfo = WorkGroupIdSetOfUserId()
            self._AddInfo._deserialize(params.get("AddInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindWorkGroupsFromUserResponse(AbstractModel):
    """UnbindWorkGroupsFromUser返回参数结构体

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


class UnlockMetaDataRequest(AbstractModel):
    """UnlockMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LockId: 锁ID
        :type LockId: int
        :param _DatasourceConnectionName: 数据源名称
        :type DatasourceConnectionName: str
        """
        self._LockId = None
        self._DatasourceConnectionName = None

    @property
    def LockId(self):
        return self._LockId

    @LockId.setter
    def LockId(self, LockId):
        self._LockId = LockId

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName


    def _deserialize(self, params):
        self._LockId = params.get("LockId")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockMetaDataResponse(AbstractModel):
    """UnlockMetaData返回参数结构体

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


class UpdateDataEngineConfigRequest(AbstractModel):
    """UpdateDataEngineConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineIds: 引擎ID
        :type DataEngineIds: list of str
        :param _DataEngineConfigCommand: 引擎配置命令，支持UpdateSparkSQLLakefsPath（更新原生表配置）、UpdateSparkSQLResultPath（更新结果路径配置）
        :type DataEngineConfigCommand: str
        """
        self._DataEngineIds = None
        self._DataEngineConfigCommand = None

    @property
    def DataEngineIds(self):
        return self._DataEngineIds

    @DataEngineIds.setter
    def DataEngineIds(self, DataEngineIds):
        self._DataEngineIds = DataEngineIds

    @property
    def DataEngineConfigCommand(self):
        return self._DataEngineConfigCommand

    @DataEngineConfigCommand.setter
    def DataEngineConfigCommand(self, DataEngineConfigCommand):
        self._DataEngineConfigCommand = DataEngineConfigCommand


    def _deserialize(self, params):
        self._DataEngineIds = params.get("DataEngineIds")
        self._DataEngineConfigCommand = params.get("DataEngineConfigCommand")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDataEngineConfigResponse(AbstractModel):
    """UpdateDataEngineConfig返回参数结构体

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


class UpdateDataEngineRequest(AbstractModel):
    """UpdateDataEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Size: 资源大小
        :type Size: int
        :param _MinClusters: 最小资源
        :type MinClusters: int
        :param _MaxClusters: 最大资源
        :type MaxClusters: int
        :param _AutoResume: 开启自动刷新：true：开启、false（默认）：关闭
        :type AutoResume: bool
        :param _DataEngineName: 数据引擎名称
        :type DataEngineName: str
        :param _Message: 相关信息
        :type Message: str
        :param _AutoSuspend: 是否自定挂起集群：false（默认）：不自动挂起、true：自动挂起
        :type AutoSuspend: bool
        :param _CrontabResumeSuspend: 定时启停集群策略：0（默认）：关闭定时策略、1：开启定时策略（注：定时启停策略与自动挂起策略互斥）
        :type CrontabResumeSuspend: int
        :param _CrontabResumeSuspendStrategy: 定时启停策略，复杂类型：包含启停时间、挂起集群策略
        :type CrontabResumeSuspendStrategy: :class:`tencentcloud.dlc.v20210125.models.CrontabResumeSuspendStrategy`
        :param _MaxConcurrency: 单个集群最大并发任务数，默认5
        :type MaxConcurrency: int
        :param _TolerableQueueTime: 可容忍的排队时间，默认0。当任务排队的时间超过可容忍的时间时可能会触发扩容。如果该参数为0，则表示一旦有任务排队就可能立即触发扩容。
        :type TolerableQueueTime: int
        :param _AutoSuspendTime: 集群自动挂起时间
        :type AutoSuspendTime: int
        :param _ElasticSwitch: spark jar 包年包月集群是否开启弹性
        :type ElasticSwitch: bool
        :param _ElasticLimit: spark jar 包年包月集群弹性上限
        :type ElasticLimit: int
        :param _SessionResourceTemplate: Spark批作业集群Session资源配置模板
        :type SessionResourceTemplate: :class:`tencentcloud.dlc.v20210125.models.SessionResourceTemplate`
        """
        self._Size = None
        self._MinClusters = None
        self._MaxClusters = None
        self._AutoResume = None
        self._DataEngineName = None
        self._Message = None
        self._AutoSuspend = None
        self._CrontabResumeSuspend = None
        self._CrontabResumeSuspendStrategy = None
        self._MaxConcurrency = None
        self._TolerableQueueTime = None
        self._AutoSuspendTime = None
        self._ElasticSwitch = None
        self._ElasticLimit = None
        self._SessionResourceTemplate = None

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def MinClusters(self):
        return self._MinClusters

    @MinClusters.setter
    def MinClusters(self, MinClusters):
        self._MinClusters = MinClusters

    @property
    def MaxClusters(self):
        return self._MaxClusters

    @MaxClusters.setter
    def MaxClusters(self, MaxClusters):
        self._MaxClusters = MaxClusters

    @property
    def AutoResume(self):
        return self._AutoResume

    @AutoResume.setter
    def AutoResume(self, AutoResume):
        self._AutoResume = AutoResume

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def AutoSuspend(self):
        return self._AutoSuspend

    @AutoSuspend.setter
    def AutoSuspend(self, AutoSuspend):
        self._AutoSuspend = AutoSuspend

    @property
    def CrontabResumeSuspend(self):
        return self._CrontabResumeSuspend

    @CrontabResumeSuspend.setter
    def CrontabResumeSuspend(self, CrontabResumeSuspend):
        self._CrontabResumeSuspend = CrontabResumeSuspend

    @property
    def CrontabResumeSuspendStrategy(self):
        return self._CrontabResumeSuspendStrategy

    @CrontabResumeSuspendStrategy.setter
    def CrontabResumeSuspendStrategy(self, CrontabResumeSuspendStrategy):
        self._CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy

    @property
    def MaxConcurrency(self):
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def TolerableQueueTime(self):
        return self._TolerableQueueTime

    @TolerableQueueTime.setter
    def TolerableQueueTime(self, TolerableQueueTime):
        self._TolerableQueueTime = TolerableQueueTime

    @property
    def AutoSuspendTime(self):
        return self._AutoSuspendTime

    @AutoSuspendTime.setter
    def AutoSuspendTime(self, AutoSuspendTime):
        self._AutoSuspendTime = AutoSuspendTime

    @property
    def ElasticSwitch(self):
        return self._ElasticSwitch

    @ElasticSwitch.setter
    def ElasticSwitch(self, ElasticSwitch):
        self._ElasticSwitch = ElasticSwitch

    @property
    def ElasticLimit(self):
        return self._ElasticLimit

    @ElasticLimit.setter
    def ElasticLimit(self, ElasticLimit):
        self._ElasticLimit = ElasticLimit

    @property
    def SessionResourceTemplate(self):
        return self._SessionResourceTemplate

    @SessionResourceTemplate.setter
    def SessionResourceTemplate(self, SessionResourceTemplate):
        self._SessionResourceTemplate = SessionResourceTemplate


    def _deserialize(self, params):
        self._Size = params.get("Size")
        self._MinClusters = params.get("MinClusters")
        self._MaxClusters = params.get("MaxClusters")
        self._AutoResume = params.get("AutoResume")
        self._DataEngineName = params.get("DataEngineName")
        self._Message = params.get("Message")
        self._AutoSuspend = params.get("AutoSuspend")
        self._CrontabResumeSuspend = params.get("CrontabResumeSuspend")
        if params.get("CrontabResumeSuspendStrategy") is not None:
            self._CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy()
            self._CrontabResumeSuspendStrategy._deserialize(params.get("CrontabResumeSuspendStrategy"))
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._TolerableQueueTime = params.get("TolerableQueueTime")
        self._AutoSuspendTime = params.get("AutoSuspendTime")
        self._ElasticSwitch = params.get("ElasticSwitch")
        self._ElasticLimit = params.get("ElasticLimit")
        if params.get("SessionResourceTemplate") is not None:
            self._SessionResourceTemplate = SessionResourceTemplate()
            self._SessionResourceTemplate._deserialize(params.get("SessionResourceTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDataEngineResponse(AbstractModel):
    """UpdateDataEngine返回参数结构体

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


class UpdateRowFilterRequest(AbstractModel):
    """UpdateRowFilter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 行过滤策略的id，此值可以通过DescribeUserInfo或者DescribeWorkGroupInfo接口获取
        :type PolicyId: int
        :param _Policy: 新的过滤策略。
        :type Policy: :class:`tencentcloud.dlc.v20210125.models.Policy`
        """
        self._PolicyId = None
        self._Policy = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        if params.get("Policy") is not None:
            self._Policy = Policy()
            self._Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRowFilterResponse(AbstractModel):
    """UpdateRowFilter返回参数结构体

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


class UpdateUserDataEngineConfigRequest(AbstractModel):
    """UpdateUserDataEngineConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 引擎ID
        :type DataEngineId: str
        :param _DataEngineConfigPairs: 用户自定义引擎配置项集合。该参数需要传用户需要添加的全部配置项，例如，已有配置项k1:v1，添加k2:v2，需要传[k1:v1,k2:v2]。
        :type DataEngineConfigPairs: list of DataEngineConfigPair
        :param _SessionResourceTemplate: 作业引擎资源配置模板
        :type SessionResourceTemplate: :class:`tencentcloud.dlc.v20210125.models.SessionResourceTemplate`
        """
        self._DataEngineId = None
        self._DataEngineConfigPairs = None
        self._SessionResourceTemplate = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def DataEngineConfigPairs(self):
        return self._DataEngineConfigPairs

    @DataEngineConfigPairs.setter
    def DataEngineConfigPairs(self, DataEngineConfigPairs):
        self._DataEngineConfigPairs = DataEngineConfigPairs

    @property
    def SessionResourceTemplate(self):
        return self._SessionResourceTemplate

    @SessionResourceTemplate.setter
    def SessionResourceTemplate(self, SessionResourceTemplate):
        self._SessionResourceTemplate = SessionResourceTemplate


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        if params.get("DataEngineConfigPairs") is not None:
            self._DataEngineConfigPairs = []
            for item in params.get("DataEngineConfigPairs"):
                obj = DataEngineConfigPair()
                obj._deserialize(item)
                self._DataEngineConfigPairs.append(obj)
        if params.get("SessionResourceTemplate") is not None:
            self._SessionResourceTemplate = SessionResourceTemplate()
            self._SessionResourceTemplate._deserialize(params.get("SessionResourceTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserDataEngineConfigResponse(AbstractModel):
    """UpdateUserDataEngineConfig返回参数结构体

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


class UpgradeDataEngineImageRequest(AbstractModel):
    """UpgradeDataEngineImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataEngineId: 引擎ID
        :type DataEngineId: str
        """
        self._DataEngineId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDataEngineImageResponse(AbstractModel):
    """UpgradeDataEngineImage返回参数结构体

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


class UserDetailInfo(AbstractModel):
    """用户详细信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _Type: 返回的信息类型，Group：返回的当前用户的工作组信息；DataAuth：返回的当前用户的数据权限信息；EngineAuth：返回的当前用户的引擎权限信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _UserType: 用户类型：ADMIN：管理员 COMMON：一般用户
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param _UserDescription: 用户描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDescription: str
        :param _DataPolicyInfo: 数据权限信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type DataPolicyInfo: :class:`tencentcloud.dlc.v20210125.models.Policys`
        :param _EnginePolicyInfo: 引擎权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type EnginePolicyInfo: :class:`tencentcloud.dlc.v20210125.models.Policys`
        :param _WorkGroupInfo: 绑定到该用户的工作组集合信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupInfo: :class:`tencentcloud.dlc.v20210125.models.WorkGroups`
        :param _UserAlias: 用户别名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        :param _RowFilterInfo: 行过滤集合
注意：此字段可能返回 null，表示取不到有效值。
        :type RowFilterInfo: :class:`tencentcloud.dlc.v20210125.models.Policys`
        """
        self._UserId = None
        self._Type = None
        self._UserType = None
        self._UserDescription = None
        self._DataPolicyInfo = None
        self._EnginePolicyInfo = None
        self._WorkGroupInfo = None
        self._UserAlias = None
        self._RowFilterInfo = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserDescription(self):
        return self._UserDescription

    @UserDescription.setter
    def UserDescription(self, UserDescription):
        self._UserDescription = UserDescription

    @property
    def DataPolicyInfo(self):
        return self._DataPolicyInfo

    @DataPolicyInfo.setter
    def DataPolicyInfo(self, DataPolicyInfo):
        self._DataPolicyInfo = DataPolicyInfo

    @property
    def EnginePolicyInfo(self):
        return self._EnginePolicyInfo

    @EnginePolicyInfo.setter
    def EnginePolicyInfo(self, EnginePolicyInfo):
        self._EnginePolicyInfo = EnginePolicyInfo

    @property
    def WorkGroupInfo(self):
        return self._WorkGroupInfo

    @WorkGroupInfo.setter
    def WorkGroupInfo(self, WorkGroupInfo):
        self._WorkGroupInfo = WorkGroupInfo

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def RowFilterInfo(self):
        return self._RowFilterInfo

    @RowFilterInfo.setter
    def RowFilterInfo(self, RowFilterInfo):
        self._RowFilterInfo = RowFilterInfo


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Type = params.get("Type")
        self._UserType = params.get("UserType")
        self._UserDescription = params.get("UserDescription")
        if params.get("DataPolicyInfo") is not None:
            self._DataPolicyInfo = Policys()
            self._DataPolicyInfo._deserialize(params.get("DataPolicyInfo"))
        if params.get("EnginePolicyInfo") is not None:
            self._EnginePolicyInfo = Policys()
            self._EnginePolicyInfo._deserialize(params.get("EnginePolicyInfo"))
        if params.get("WorkGroupInfo") is not None:
            self._WorkGroupInfo = WorkGroups()
            self._WorkGroupInfo._deserialize(params.get("WorkGroupInfo"))
        self._UserAlias = params.get("UserAlias")
        if params.get("RowFilterInfo") is not None:
            self._RowFilterInfo = Policys()
            self._RowFilterInfo._deserialize(params.get("RowFilterInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserIdSetOfWorkGroupId(AbstractModel):
    """绑定到同一个工作组的用户Id的集合

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 工作组Id
        :type WorkGroupId: int
        :param _UserIds: 用户Id集合，和CAM侧Uin匹配
        :type UserIds: list of str
        """
        self._WorkGroupId = None
        self._UserIds = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """授权用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id，和子用户uin相同
        :type UserId: str
        :param _UserDescription: 用户描述信息，方便区分不同用户
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDescription: str
        :param _PolicySet: 单独给用户绑定的权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicySet: list of Policy
        :param _Creator: 当前用户的创建者
        :type Creator: str
        :param _CreateTime: 创建时间，格式如2021-07-28 16:19:32
        :type CreateTime: str
        :param _WorkGroupSet: 关联的工作组集合
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupSet: list of WorkGroupMessage
        :param _IsOwner: 是否是主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOwner: bool
        :param _UserType: 用户类型。ADMIN：管理员 COMMON：普通用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param _UserAlias: 用户别名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAlias: str
        """
        self._UserId = None
        self._UserDescription = None
        self._PolicySet = None
        self._Creator = None
        self._CreateTime = None
        self._WorkGroupSet = None
        self._IsOwner = None
        self._UserType = None
        self._UserAlias = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserDescription(self):
        return self._UserDescription

    @UserDescription.setter
    def UserDescription(self, UserDescription):
        self._UserDescription = UserDescription

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def WorkGroupSet(self):
        return self._WorkGroupSet

    @WorkGroupSet.setter
    def WorkGroupSet(self, WorkGroupSet):
        self._WorkGroupSet = WorkGroupSet

    @property
    def IsOwner(self):
        return self._IsOwner

    @IsOwner.setter
    def IsOwner(self, IsOwner):
        self._IsOwner = IsOwner

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserDescription = params.get("UserDescription")
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        self._Creator = params.get("Creator")
        self._CreateTime = params.get("CreateTime")
        if params.get("WorkGroupSet") is not None:
            self._WorkGroupSet = []
            for item in params.get("WorkGroupSet"):
                obj = WorkGroupMessage()
                obj._deserialize(item)
                self._WorkGroupSet.append(obj)
        self._IsOwner = params.get("IsOwner")
        self._UserType = params.get("UserType")
        self._UserAlias = params.get("UserAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserMessage(AbstractModel):
    """用户部分信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id，和CAM侧子用户Uin匹配
        :type UserId: str
        :param _UserDescription: 用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDescription: str
        :param _Creator: 当前用户的创建者
        :type Creator: str
        :param _CreateTime: 当前用户的创建时间，形如2021-07-28 16:19:32
        :type CreateTime: str
        :param _UserAlias: 用户别名
        :type UserAlias: str
        """
        self._UserId = None
        self._UserDescription = None
        self._Creator = None
        self._CreateTime = None
        self._UserAlias = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserDescription(self):
        return self._UserDescription

    @UserDescription.setter
    def UserDescription(self, UserDescription):
        self._UserDescription = UserDescription

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserDescription = params.get("UserDescription")
        self._Creator = params.get("Creator")
        self._CreateTime = params.get("CreateTime")
        self._UserAlias = params.get("UserAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserRole(AbstractModel):
    """用户角色

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色ID
        :type RoleId: int
        :param _AppId: 用户app ID
        :type AppId: str
        :param _Uin: 用户ID
        :type Uin: str
        :param _Arn: 角色权限
        :type Arn: str
        :param _ModifyTime: 最近修改时间戳
        :type ModifyTime: int
        :param _Desc: 角色描述信息
        :type Desc: str
        :param _RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param _Creator: 创建者UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _CosPermissionList: cos授权路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPermissionList: list of CosPermission
        :param _PermissionJson: cam策略json
注意：此字段可能返回 null，表示取不到有效值。
        :type PermissionJson: str
        """
        self._RoleId = None
        self._AppId = None
        self._Uin = None
        self._Arn = None
        self._ModifyTime = None
        self._Desc = None
        self._RoleName = None
        self._Creator = None
        self._CosPermissionList = None
        self._PermissionJson = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Arn(self):
        return self._Arn

    @Arn.setter
    def Arn(self, Arn):
        self._Arn = Arn

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CosPermissionList(self):
        return self._CosPermissionList

    @CosPermissionList.setter
    def CosPermissionList(self, CosPermissionList):
        self._CosPermissionList = CosPermissionList

    @property
    def PermissionJson(self):
        return self._PermissionJson

    @PermissionJson.setter
    def PermissionJson(self, PermissionJson):
        self._PermissionJson = PermissionJson


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Arn = params.get("Arn")
        self._ModifyTime = params.get("ModifyTime")
        self._Desc = params.get("Desc")
        self._RoleName = params.get("RoleName")
        self._Creator = params.get("Creator")
        if params.get("CosPermissionList") is not None:
            self._CosPermissionList = []
            for item in params.get("CosPermissionList"):
                obj = CosPermission()
                obj._deserialize(item)
                self._CosPermissionList.append(obj)
        self._PermissionJson = params.get("PermissionJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Users(AbstractModel):
    """用户信息集合

    """

    def __init__(self):
        r"""
        :param _UserSet: 用户信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSet: list of UserMessage
        :param _TotalCount: 用户总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._UserSet = None
        self._TotalCount = None

    @property
    def UserSet(self):
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("UserSet") is not None:
            self._UserSet = []
            for item in params.get("UserSet"):
                obj = UserMessage()
                obj._deserialize(item)
                self._UserSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewBaseInfo(AbstractModel):
    """视图基本配置信息

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 该视图所属数据库名字
        :type DatabaseName: str
        :param _ViewName: 视图名称
        :type ViewName: str
        :param _UserAlias: 视图创建人昵称
        :type UserAlias: str
        :param _UserSubUin: 视图创建人ID
        :type UserSubUin: str
        """
        self._DatabaseName = None
        self._ViewName = None
        self._UserAlias = None
        self._UserSubUin = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def UserSubUin(self):
        return self._UserSubUin

    @UserSubUin.setter
    def UserSubUin(self, UserSubUin):
        self._UserSubUin = UserSubUin


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._ViewName = params.get("ViewName")
        self._UserAlias = params.get("UserAlias")
        self._UserSubUin = params.get("UserSubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewResponseInfo(AbstractModel):
    """查询视图信息对象

    """

    def __init__(self):
        r"""
        :param _ViewBaseInfo: 视图基本信息。
        :type ViewBaseInfo: :class:`tencentcloud.dlc.v20210125.models.ViewBaseInfo`
        :param _Columns: 视图列信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param _Properties: 视图属性信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param _CreateTime: 视图创建时间。
        :type CreateTime: str
        :param _ModifiedTime: 视图更新时间。
        :type ModifiedTime: str
        """
        self._ViewBaseInfo = None
        self._Columns = None
        self._Properties = None
        self._CreateTime = None
        self._ModifiedTime = None

    @property
    def ViewBaseInfo(self):
        return self._ViewBaseInfo

    @ViewBaseInfo.setter
    def ViewBaseInfo(self, ViewBaseInfo):
        self._ViewBaseInfo = ViewBaseInfo

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        if params.get("ViewBaseInfo") is not None:
            self._ViewBaseInfo = ViewBaseInfo()
            self._ViewBaseInfo._deserialize(params.get("ViewBaseInfo"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcCidrBlock(AbstractModel):
    """VPC子网信息

    """

    def __init__(self):
        r"""
        :param _CidrId: 子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CidrId: str
        :param _CidrAddr: 子网网段
注意：此字段可能返回 null，表示取不到有效值。
        :type CidrAddr: str
        """
        self._CidrId = None
        self._CidrAddr = None

    @property
    def CidrId(self):
        return self._CidrId

    @CidrId.setter
    def CidrId(self, CidrId):
        self._CidrId = CidrId

    @property
    def CidrAddr(self):
        return self._CidrAddr

    @CidrAddr.setter
    def CidrAddr(self, CidrAddr):
        self._CidrAddr = CidrAddr


    def _deserialize(self, params):
        self._CidrId = params.get("CidrId")
        self._CidrAddr = params.get("CidrAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """vpc信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc Id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcCidrBlock: vpc子网
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcCidrBlock: str
        :param _RuleId: 规则Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param _AccessGroupId: 权限组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessGroupId: str
        """
        self._VpcId = None
        self._VpcCidrBlock = None
        self._RuleId = None
        self._AccessGroupId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._RuleId = params.get("RuleId")
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkGroupDetailInfo(AbstractModel):
    """工作组详细信息

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 工作组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupId: int
        :param _WorkGroupName: 工作组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupName: str
        :param _Type: 包含的信息类型。User：用户信息；DataAuth：数据权限；EngineAuth:引擎权限
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _UserInfo: 工作组上绑定的用户集合
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: :class:`tencentcloud.dlc.v20210125.models.Users`
        :param _DataPolicyInfo: 数据权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type DataPolicyInfo: :class:`tencentcloud.dlc.v20210125.models.Policys`
        :param _EnginePolicyInfo: 引擎权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type EnginePolicyInfo: :class:`tencentcloud.dlc.v20210125.models.Policys`
        :param _WorkGroupDescription: 工作组描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupDescription: str
        :param _RowFilterInfo: 行过滤信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type RowFilterInfo: :class:`tencentcloud.dlc.v20210125.models.Policys`
        """
        self._WorkGroupId = None
        self._WorkGroupName = None
        self._Type = None
        self._UserInfo = None
        self._DataPolicyInfo = None
        self._EnginePolicyInfo = None
        self._WorkGroupDescription = None
        self._RowFilterInfo = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def WorkGroupName(self):
        return self._WorkGroupName

    @WorkGroupName.setter
    def WorkGroupName(self, WorkGroupName):
        self._WorkGroupName = WorkGroupName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def DataPolicyInfo(self):
        return self._DataPolicyInfo

    @DataPolicyInfo.setter
    def DataPolicyInfo(self, DataPolicyInfo):
        self._DataPolicyInfo = DataPolicyInfo

    @property
    def EnginePolicyInfo(self):
        return self._EnginePolicyInfo

    @EnginePolicyInfo.setter
    def EnginePolicyInfo(self, EnginePolicyInfo):
        self._EnginePolicyInfo = EnginePolicyInfo

    @property
    def WorkGroupDescription(self):
        return self._WorkGroupDescription

    @WorkGroupDescription.setter
    def WorkGroupDescription(self, WorkGroupDescription):
        self._WorkGroupDescription = WorkGroupDescription

    @property
    def RowFilterInfo(self):
        return self._RowFilterInfo

    @RowFilterInfo.setter
    def RowFilterInfo(self, RowFilterInfo):
        self._RowFilterInfo = RowFilterInfo


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        self._WorkGroupName = params.get("WorkGroupName")
        self._Type = params.get("Type")
        if params.get("UserInfo") is not None:
            self._UserInfo = Users()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("DataPolicyInfo") is not None:
            self._DataPolicyInfo = Policys()
            self._DataPolicyInfo._deserialize(params.get("DataPolicyInfo"))
        if params.get("EnginePolicyInfo") is not None:
            self._EnginePolicyInfo = Policys()
            self._EnginePolicyInfo._deserialize(params.get("EnginePolicyInfo"))
        self._WorkGroupDescription = params.get("WorkGroupDescription")
        if params.get("RowFilterInfo") is not None:
            self._RowFilterInfo = Policys()
            self._RowFilterInfo._deserialize(params.get("RowFilterInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkGroupIdSetOfUserId(AbstractModel):
    """同一个用户绑定的工作组集合

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id，和CAM侧Uin匹配
        :type UserId: str
        :param _WorkGroupIds: 工作组Id集合
        :type WorkGroupIds: list of int
        """
        self._UserId = None
        self._WorkGroupIds = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def WorkGroupIds(self):
        return self._WorkGroupIds

    @WorkGroupIds.setter
    def WorkGroupIds(self, WorkGroupIds):
        self._WorkGroupIds = WorkGroupIds


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._WorkGroupIds = params.get("WorkGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkGroupInfo(AbstractModel):
    """工作组信息

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 查询到的工作组唯一Id
        :type WorkGroupId: int
        :param _WorkGroupName: 工作组名称
        :type WorkGroupName: str
        :param _WorkGroupDescription: 工作组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupDescription: str
        :param _UserNum: 工作组关联的用户数量
        :type UserNum: int
        :param _UserSet: 工作组关联的用户集合
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSet: list of UserMessage
        :param _PolicySet: 工作组绑定的权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicySet: list of Policy
        :param _Creator: 工作组的创建人
        :type Creator: str
        :param _CreateTime: 工作组的创建时间，形如2021-07-28 16:19:32
        :type CreateTime: str
        """
        self._WorkGroupId = None
        self._WorkGroupName = None
        self._WorkGroupDescription = None
        self._UserNum = None
        self._UserSet = None
        self._PolicySet = None
        self._Creator = None
        self._CreateTime = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def WorkGroupName(self):
        return self._WorkGroupName

    @WorkGroupName.setter
    def WorkGroupName(self, WorkGroupName):
        self._WorkGroupName = WorkGroupName

    @property
    def WorkGroupDescription(self):
        return self._WorkGroupDescription

    @WorkGroupDescription.setter
    def WorkGroupDescription(self, WorkGroupDescription):
        self._WorkGroupDescription = WorkGroupDescription

    @property
    def UserNum(self):
        return self._UserNum

    @UserNum.setter
    def UserNum(self, UserNum):
        self._UserNum = UserNum

    @property
    def UserSet(self):
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

    @property
    def PolicySet(self):
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        self._WorkGroupName = params.get("WorkGroupName")
        self._WorkGroupDescription = params.get("WorkGroupDescription")
        self._UserNum = params.get("UserNum")
        if params.get("UserSet") is not None:
            self._UserSet = []
            for item in params.get("UserSet"):
                obj = UserMessage()
                obj._deserialize(item)
                self._UserSet.append(obj)
        if params.get("PolicySet") is not None:
            self._PolicySet = []
            for item in params.get("PolicySet"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicySet.append(obj)
        self._Creator = params.get("Creator")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkGroupMessage(AbstractModel):
    """工作组部分信息

    """

    def __init__(self):
        r"""
        :param _WorkGroupId: 工作组唯一Id
        :type WorkGroupId: int
        :param _WorkGroupName: 工作组名称
        :type WorkGroupName: str
        :param _WorkGroupDescription: 工作组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupDescription: str
        :param _Creator: 创建者
        :type Creator: str
        :param _CreateTime: 工作组创建的时间，形如2021-07-28 16:19:32
        :type CreateTime: str
        """
        self._WorkGroupId = None
        self._WorkGroupName = None
        self._WorkGroupDescription = None
        self._Creator = None
        self._CreateTime = None

    @property
    def WorkGroupId(self):
        return self._WorkGroupId

    @WorkGroupId.setter
    def WorkGroupId(self, WorkGroupId):
        self._WorkGroupId = WorkGroupId

    @property
    def WorkGroupName(self):
        return self._WorkGroupName

    @WorkGroupName.setter
    def WorkGroupName(self, WorkGroupName):
        self._WorkGroupName = WorkGroupName

    @property
    def WorkGroupDescription(self):
        return self._WorkGroupDescription

    @WorkGroupDescription.setter
    def WorkGroupDescription(self, WorkGroupDescription):
        self._WorkGroupDescription = WorkGroupDescription

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._WorkGroupId = params.get("WorkGroupId")
        self._WorkGroupName = params.get("WorkGroupName")
        self._WorkGroupDescription = params.get("WorkGroupDescription")
        self._Creator = params.get("Creator")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkGroups(AbstractModel):
    """工作组集合

    """

    def __init__(self):
        r"""
        :param _WorkGroupSet: 工作组信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkGroupSet: list of WorkGroupMessage
        :param _TotalCount: 工作组总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._WorkGroupSet = None
        self._TotalCount = None

    @property
    def WorkGroupSet(self):
        return self._WorkGroupSet

    @WorkGroupSet.setter
    def WorkGroupSet(self, WorkGroupSet):
        self._WorkGroupSet = WorkGroupSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("WorkGroupSet") is not None:
            self._WorkGroupSet = []
            for item in params.get("WorkGroupSet"):
                obj = WorkGroupMessage()
                obj._deserialize(item)
                self._WorkGroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        