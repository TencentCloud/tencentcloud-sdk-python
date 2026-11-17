# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class BackupColumnItem(AbstractModel):
    r"""备份列对象

    """

    def __init__(self):
        r"""
        :param _ColumnName: 列名。
        :type ColumnName: str
        :param _NewColumnName: 重命名后的列名。
        :type NewColumnName: str
        """
        self._ColumnName = None
        self._NewColumnName = None

    @property
    def ColumnName(self):
        r"""列名。
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def NewColumnName(self):
        r"""重命名后的列名。
        :rtype: str
        """
        return self._NewColumnName

    @NewColumnName.setter
    def NewColumnName(self, NewColumnName):
        self._NewColumnName = NewColumnName


    def _deserialize(self, params):
        self._ColumnName = params.get("ColumnName")
        self._NewColumnName = params.get("NewColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupEndpoint(AbstractModel):
    r"""备份源实例详情

    """

    def __init__(self):
        r"""
        :param _DatabaseType: 数据库类型。目前支持的值["mysql", "mariadb", "percona"]。注意，该值必须和备份计划的类型一致。
        :type DatabaseType: str
        :param _AccessType: 实例接入类型，支持的值包括：
"extranet" - 外网;
"cvm" - cvm自建实例;
"dcg" - 专线接入;
"vpncloud" - 云vpn接入;
"cdb" - 腾讯云数据库实例;
"ccn" - 云联网接入。
        :type AccessType: str
        :param _UserName: 用户名。
        :type UserName: str
        :param _Password: 登录密码。
        :type Password: str
        :param _Region: 接入地域。
        :type Region: str
        :param _Supplier: 服务提供商，支持的值包括["aliyun", "aws", "others"]。
        :type Supplier: str
        :param _Ip: 实例 Ip。
        :type Ip: str
        :param _Port: 实例端口号。
        :type Port: int
        :param _InstanceId: 云数据库实例ID，格式如：cdb-qcloudtest。
        :type InstanceId: str
        :param _CvmInstanceId: CVM 实例ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要填写该字段。
        :type CvmInstanceId: str
        :param _UniqDcgId: 专线网关ID，格式如：dcg-0rxtqqxb。
        :type UniqDcgId: str
        :param _UniqVpnGwId: VPN网关ID，格式如：vpngw-9ghexg7q。
        :type UniqVpnGwId: str
        :param _VpcId: 私有网络ID，格式如：vpc-92jblxto。
        :type VpcId: str
        :param _SubnetId: 子网ID，格式如：subnet-3paxmkdz。
        :type SubnetId: str
        :param _CcnId: 云联网ID，如：ccn-afp6kltc。
        :type CcnId: str
        :param _EngineVersion: 数据库版本，当实例为 RDS 或 AWS 实例时才有效，格式如：5.6或者5.7，默认为5.6。
        :type EngineVersion: str
        :param _DBKernel: mariadb三引擎版本。
        :type DBKernel: str
        """
        self._DatabaseType = None
        self._AccessType = None
        self._UserName = None
        self._Password = None
        self._Region = None
        self._Supplier = None
        self._Ip = None
        self._Port = None
        self._InstanceId = None
        self._CvmInstanceId = None
        self._UniqDcgId = None
        self._UniqVpnGwId = None
        self._VpcId = None
        self._SubnetId = None
        self._CcnId = None
        self._EngineVersion = None
        self._DBKernel = None

    @property
    def DatabaseType(self):
        r"""数据库类型。目前支持的值["mysql", "mariadb", "percona"]。注意，该值必须和备份计划的类型一致。
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def AccessType(self):
        r"""实例接入类型，支持的值包括：
"extranet" - 外网;
"cvm" - cvm自建实例;
"dcg" - 专线接入;
"vpncloud" - 云vpn接入;
"cdb" - 腾讯云数据库实例;
"ccn" - 云联网接入。
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def UserName(self):
        r"""用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""登录密码。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Region(self):
        r"""接入地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Supplier(self):
        r"""服务提供商，支持的值包括["aliyun", "aws", "others"]。
        :rtype: str
        """
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def Ip(self):
        r"""实例 Ip。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""实例端口号。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        r"""云数据库实例ID，格式如：cdb-qcloudtest。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmInstanceId(self):
        r"""CVM 实例ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要填写该字段。
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        r"""专线网关ID，格式如：dcg-0rxtqqxb。
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def UniqVpnGwId(self):
        r"""VPN网关ID，格式如：vpngw-9ghexg7q。
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def VpcId(self):
        r"""私有网络ID，格式如：vpc-92jblxto。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID，格式如：subnet-3paxmkdz。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CcnId(self):
        r"""云联网ID，如：ccn-afp6kltc。
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def EngineVersion(self):
        r"""数据库版本，当实例为 RDS 或 AWS 实例时才有效，格式如：5.6或者5.7，默认为5.6。
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def DBKernel(self):
        r"""mariadb三引擎版本。
        :rtype: str
        """
        return self._DBKernel

    @DBKernel.setter
    def DBKernel(self, DBKernel):
        self._DBKernel = DBKernel


    def _deserialize(self, params):
        self._DatabaseType = params.get("DatabaseType")
        self._AccessType = params.get("AccessType")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Region = params.get("Region")
        self._Supplier = params.get("Supplier")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CcnId = params.get("CcnId")
        self._EngineVersion = params.get("EngineVersion")
        self._DBKernel = params.get("DBKernel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFile(AbstractModel):
    r"""增量备份文件信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名。
        :type FileName: str
        :param _BackupSetId: 备份集 ID。
        :type BackupSetId: str
        :param _Status: 文件状态。取值：
- notReady：未就绪
- backuping：备份中
- finished：备份完成
- failed：备份失败
        :type Status: str
        :param _SourceInfo: 源库连接信息。云数据库实例为实例 ID，其余为 ip:port。
        :type SourceInfo: str
        :param _StartTime: 开始时间。格式为 YYYY-MM-DD hh:mm:ss。
        :type StartTime: str
        :param _EndTime: 结束时间。格式为 YYYY-MM-DD hh:mm:ss，备份集尚未结束时返回 0000-00-00 00:00:00。
        :type EndTime: str
        :param _ExpireTime: 过期时间。格式为 YYYY-MM-DD hh:mm:ss。
        :type ExpireTime: str
        :param _BackupSize: 文件大小，单位：字节。
        :type BackupSize: int
        :param _BackupMethod: 备份方式。取值：logical（逻辑备份）。
        :type BackupMethod: str
        :param _StorageType: 存储类型。取值：DBSStorage（内置存储）。
        :type StorageType: str
        :param _RetentionType: 存储策略类型。取值：
- standard：标准存储
- tiered：分级存储
        :type RetentionType: str
        :param _ResourceDetail: 备份集存储详情。
        :type ResourceDetail: :class:`tencentcloud.dbs.v20211108.models.ResourceDetail`
        :param _BackupPool: 备份池。
        :type BackupPool: str
        :param _AllowedActions: 当前状态下允许的操作。取值：download。
        :type AllowedActions: list of str
        :param _AllActions: 支持的全部操作。
        :type AllActions: list of str
        :param _LastModified: 文件最后修改时间。格式为 YYYY-MM-DD hh:mm:ss。
        :type LastModified: str
        """
        self._FileName = None
        self._BackupSetId = None
        self._Status = None
        self._SourceInfo = None
        self._StartTime = None
        self._EndTime = None
        self._ExpireTime = None
        self._BackupSize = None
        self._BackupMethod = None
        self._StorageType = None
        self._RetentionType = None
        self._ResourceDetail = None
        self._BackupPool = None
        self._AllowedActions = None
        self._AllActions = None
        self._LastModified = None

    @property
    def FileName(self):
        r"""文件名。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def BackupSetId(self):
        r"""备份集 ID。
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def Status(self):
        r"""文件状态。取值：
- notReady：未就绪
- backuping：备份中
- finished：备份完成
- failed：备份失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceInfo(self):
        r"""源库连接信息。云数据库实例为实例 ID，其余为 ip:port。
        :rtype: str
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo

    @property
    def StartTime(self):
        r"""开始时间。格式为 YYYY-MM-DD hh:mm:ss。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。格式为 YYYY-MM-DD hh:mm:ss，备份集尚未结束时返回 0000-00-00 00:00:00。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExpireTime(self):
        r"""过期时间。格式为 YYYY-MM-DD hh:mm:ss。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def BackupSize(self):
        r"""文件大小，单位：字节。
        :rtype: int
        """
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def BackupMethod(self):
        r"""备份方式。取值：logical（逻辑备份）。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def StorageType(self):
        r"""存储类型。取值：DBSStorage（内置存储）。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def RetentionType(self):
        r"""存储策略类型。取值：
- standard：标准存储
- tiered：分级存储
        :rtype: str
        """
        return self._RetentionType

    @RetentionType.setter
    def RetentionType(self, RetentionType):
        self._RetentionType = RetentionType

    @property
    def ResourceDetail(self):
        r"""备份集存储详情。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.ResourceDetail`
        """
        return self._ResourceDetail

    @ResourceDetail.setter
    def ResourceDetail(self, ResourceDetail):
        self._ResourceDetail = ResourceDetail

    @property
    def BackupPool(self):
        r"""备份池。
        :rtype: str
        """
        return self._BackupPool

    @BackupPool.setter
    def BackupPool(self, BackupPool):
        self._BackupPool = BackupPool

    @property
    def AllowedActions(self):
        r"""当前状态下允许的操作。取值：download。
        :rtype: list of str
        """
        return self._AllowedActions

    @AllowedActions.setter
    def AllowedActions(self, AllowedActions):
        self._AllowedActions = AllowedActions

    @property
    def AllActions(self):
        r"""支持的全部操作。
        :rtype: list of str
        """
        return self._AllActions

    @AllActions.setter
    def AllActions(self, AllActions):
        self._AllActions = AllActions

    @property
    def LastModified(self):
        r"""文件最后修改时间。格式为 YYYY-MM-DD hh:mm:ss。
        :rtype: str
        """
        return self._LastModified

    @LastModified.setter
    def LastModified(self, LastModified):
        self._LastModified = LastModified


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._BackupSetId = params.get("BackupSetId")
        self._Status = params.get("Status")
        self._SourceInfo = params.get("SourceInfo")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExpireTime = params.get("ExpireTime")
        self._BackupSize = params.get("BackupSize")
        self._BackupMethod = params.get("BackupMethod")
        self._StorageType = params.get("StorageType")
        self._RetentionType = params.get("RetentionType")
        if params.get("ResourceDetail") is not None:
            self._ResourceDetail = ResourceDetail()
            self._ResourceDetail._deserialize(params.get("ResourceDetail"))
        self._BackupPool = params.get("BackupPool")
        self._AllowedActions = params.get("AllowedActions")
        self._AllActions = params.get("AllActions")
        self._LastModified = params.get("LastModified")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupObject(AbstractModel):
    r"""备份对象

    """

    def __init__(self):
        r"""
        :param _ObjectMode: 备份对象类型，可能的取值为:
"all" - 整实例;
"partial" - 部分对象。
        :type ObjectMode: str
        :param _ObjectItems: 备份对象详情，当 ObjectMode 为 partial, 即选择部分对象备份时，该字段不能为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectItems: list of BackupObjectItem
        """
        self._ObjectMode = None
        self._ObjectItems = None

    @property
    def ObjectMode(self):
        r"""备份对象类型，可能的取值为:
"all" - 整实例;
"partial" - 部分对象。
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def ObjectItems(self):
        r"""备份对象详情，当 ObjectMode 为 partial, 即选择部分对象备份时，该字段不能为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BackupObjectItem
        """
        return self._ObjectItems

    @ObjectItems.setter
    def ObjectItems(self, ObjectItems):
        self._ObjectItems = ObjectItems


    def _deserialize(self, params):
        self._ObjectMode = params.get("ObjectMode")
        if params.get("ObjectItems") is not None:
            self._ObjectItems = []
            for item in params.get("ObjectItems"):
                obj = BackupObjectItem()
                obj._deserialize(item)
                self._ObjectItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupObjectItem(AbstractModel):
    r"""备份对象详情

    """

    def __init__(self):
        r"""
        :param _DBName: 库名。
        :type DBName: str
        :param _NewDBName: 重命名后的库名。
        :type NewDBName: str
        :param _SchemaName: schema 名。
        :type SchemaName: str
        :param _NewSchemaName: 重命名后的 schema 名。
        :type NewSchemaName: str
        :param _DbMode: 库选择模式，可能的取值为：
"all" - 当前对象下的所有对象;
"partial" - 当前对象下的部分对象。
        :type DbMode: str
        :param _TableMode: 表选择模式，可能的取值为:
"all" - 当前对象下的所有对象;
"partial" - 当前对象下的部分对象。
        :type TableMode: str
        :param _Tables: 表对象详情。当 TableMode 为 partial，即选择部分表备份时，此参数需要填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of BackupTableItem
        """
        self._DBName = None
        self._NewDBName = None
        self._SchemaName = None
        self._NewSchemaName = None
        self._DbMode = None
        self._TableMode = None
        self._Tables = None

    @property
    def DBName(self):
        r"""库名。
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def NewDBName(self):
        r"""重命名后的库名。
        :rtype: str
        """
        return self._NewDBName

    @NewDBName.setter
    def NewDBName(self, NewDBName):
        self._NewDBName = NewDBName

    @property
    def SchemaName(self):
        r"""schema 名。
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def NewSchemaName(self):
        r"""重命名后的 schema 名。
        :rtype: str
        """
        return self._NewSchemaName

    @NewSchemaName.setter
    def NewSchemaName(self, NewSchemaName):
        self._NewSchemaName = NewSchemaName

    @property
    def DbMode(self):
        r"""库选择模式，可能的取值为：
"all" - 当前对象下的所有对象;
"partial" - 当前对象下的部分对象。
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def TableMode(self):
        r"""表选择模式，可能的取值为:
"all" - 当前对象下的所有对象;
"partial" - 当前对象下的部分对象。
        :rtype: str
        """
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        r"""表对象详情。当 TableMode 为 partial，即选择部分表备份时，此参数需要填写。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BackupTableItem
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._NewDBName = params.get("NewDBName")
        self._SchemaName = params.get("SchemaName")
        self._NewSchemaName = params.get("NewSchemaName")
        self._DbMode = params.get("DbMode")
        self._TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = BackupTableItem()
                obj._deserialize(item)
                self._Tables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPeriod(AbstractModel):
    r"""备份周期描述

    """

    def __init__(self):
        r"""
        :param _PeriodType: 全量备份频率。目前仅支持"Weekly" - 每星期
        :type PeriodType: str
        :param _Day: 全量备份周期。取值范围为：["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]。
        :type Day: list of str
        """
        self._PeriodType = None
        self._Day = None

    @property
    def PeriodType(self):
        r"""全量备份频率。目前仅支持"Weekly" - 每星期
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def Day(self):
        r"""全量备份周期。取值范围为：["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]。
        :rtype: list of str
        """
        return self._Day

    @Day.setter
    def Day(self, Day):
        self._Day = Day


    def _deserialize(self, params):
        self._PeriodType = params.get("PeriodType")
        self._Day = params.get("Day")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPeriodItem(AbstractModel):
    r"""备份周期描述

    """

    def __init__(self):
        r"""
        :param _PeriodType: 全量备份频率。目前仅支持"Weekly" - 每星期
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodType: str
        :param _Day: 全量备份周期。取值范围为：["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]。
注意：此字段可能返回 null，表示取不到有效值。
        :type Day: list of str
        """
        self._PeriodType = None
        self._Day = None

    @property
    def PeriodType(self):
        r"""全量备份频率。目前仅支持"Weekly" - 每星期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType

    @property
    def Day(self):
        r"""全量备份周期。取值范围为：["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Day

    @Day.setter
    def Day(self, Day):
        self._Day = Day


    def _deserialize(self, params):
        self._PeriodType = params.get("PeriodType")
        self._Day = params.get("Day")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPlanInfo(AbstractModel):
    r"""备份计划信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域信息。
        :type Region: str
        :param _BackupPlanId: 备份计划 ID。
        :type BackupPlanId: str
        :param _BackupPlanName: 备份计划名称。
        :type BackupPlanName: str
        :param _Status: 备份计划状态。可能的取值为：
"notStarted" - 未启动;
"checking" - 校验中;
"checkPass" - 校验通过;
"checkNotPass" - 校验未通过;
"running" - 运行中;
"fullBacking" - 全量备份中;
"isolating" - 隔离中;
"isolated" - 已隔离;
"offlining" - 下线中;
"offlined" - 已下线;
"paused" - 已暂停。
        :type Status: str
        :param _DatabaseType: 数据库类型。
        :type DatabaseType: str
        :param _AccessType: 访问类型。可能的取值为：
"extranet" - 外网;
"cvm" - cvm 自建实例;
"dcg" - 专线接入;
"vpncloud" - 云vpn接入;
"cdb" - 腾讯云数据库实例;
"ccn" - 云联网。
        :type AccessType: str
        :param _SourceInfo: 源实例信息。
        :type SourceInfo: list of str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _ExpireTime: 到期时间。
        :type ExpireTime: str
        :param _OfflineTime: 下线时间。
        :type OfflineTime: str
        :param _InstanceClass: 实例规格类型。可能的取值为：["micro", "small", "medium", "large", "xlarge"]。
        :type InstanceClass: str
        :param _BackupMethod: 备份方式。可能的取值为：
"logical" - 逻辑备份;
"physical" - 物理备份。
        :type BackupMethod: str
        :param _Tags: 标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AutoRenewFlag: 自动续费标记。可能的取值为：
0 - 未开启自动续费;
1 - 已开启自动续费;
2 - 已关闭自动续费。
        :type AutoRenewFlag: int
        :param _EnableIncrement: 是否开启增量备份标记。
        :type EnableIncrement: bool
        :param _PayType: 付费类型。可能的取值为：
"prePay" - 预付费类型;
"postPay" - 后付费类型。
        :type PayType: str
        :param _SetSourceInfo: 源端信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SetSourceInfo: list of str
        """
        self._Region = None
        self._BackupPlanId = None
        self._BackupPlanName = None
        self._Status = None
        self._DatabaseType = None
        self._AccessType = None
        self._SourceInfo = None
        self._CreateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._InstanceClass = None
        self._BackupMethod = None
        self._Tags = None
        self._AutoRenewFlag = None
        self._EnableIncrement = None
        self._PayType = None
        self._SetSourceInfo = None

    @property
    def Region(self):
        r"""地域信息。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId

    @property
    def BackupPlanName(self):
        r"""备份计划名称。
        :rtype: str
        """
        return self._BackupPlanName

    @BackupPlanName.setter
    def BackupPlanName(self, BackupPlanName):
        self._BackupPlanName = BackupPlanName

    @property
    def Status(self):
        r"""备份计划状态。可能的取值为：
"notStarted" - 未启动;
"checking" - 校验中;
"checkPass" - 校验通过;
"checkNotPass" - 校验未通过;
"running" - 运行中;
"fullBacking" - 全量备份中;
"isolating" - 隔离中;
"isolated" - 已隔离;
"offlining" - 下线中;
"offlined" - 已下线;
"paused" - 已暂停。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DatabaseType(self):
        r"""数据库类型。
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def AccessType(self):
        r"""访问类型。可能的取值为：
"extranet" - 外网;
"cvm" - cvm 自建实例;
"dcg" - 专线接入;
"vpncloud" - 云vpn接入;
"cdb" - 腾讯云数据库实例;
"ccn" - 云联网。
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def SourceInfo(self):
        r"""源实例信息。
        :rtype: list of str
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""到期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        r"""下线时间。
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def InstanceClass(self):
        r"""实例规格类型。可能的取值为：["micro", "small", "medium", "large", "xlarge"]。
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def BackupMethod(self):
        r"""备份方式。可能的取值为：
"logical" - 逻辑备份;
"physical" - 物理备份。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def Tags(self):
        r"""标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRenewFlag(self):
        r"""自动续费标记。可能的取值为：
0 - 未开启自动续费;
1 - 已开启自动续费;
2 - 已关闭自动续费。
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def EnableIncrement(self):
        r"""是否开启增量备份标记。
        :rtype: bool
        """
        return self._EnableIncrement

    @EnableIncrement.setter
    def EnableIncrement(self, EnableIncrement):
        self._EnableIncrement = EnableIncrement

    @property
    def PayType(self):
        r"""付费类型。可能的取值为：
"prePay" - 预付费类型;
"postPay" - 后付费类型。
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def SetSourceInfo(self):
        r"""源端信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SetSourceInfo

    @SetSourceInfo.setter
    def SetSourceInfo(self, SetSourceInfo):
        self._SetSourceInfo = SetSourceInfo


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._BackupPlanId = params.get("BackupPlanId")
        self._BackupPlanName = params.get("BackupPlanName")
        self._Status = params.get("Status")
        self._DatabaseType = params.get("DatabaseType")
        self._AccessType = params.get("AccessType")
        self._SourceInfo = params.get("SourceInfo")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._InstanceClass = params.get("InstanceClass")
        self._BackupMethod = params.get("BackupMethod")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._EnableIncrement = params.get("EnableIncrement")
        self._PayType = params.get("PayType")
        self._SetSourceInfo = params.get("SetSourceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPlanPayInfo(AbstractModel):
    r"""备份计划付费信息

    """

    def __init__(self):
        r"""
        :param _InstanceClass: 实例规格。
        :type InstanceClass: str
        :param _PayType: 付费方式。取值：
- postPay：后付费
- prePay：预付费
        :type PayType: str
        :param _FreeSpace: 免费额度，单位：字节。取值为 -1 表示不限量。
        :type FreeSpace: int
        :param _TotalChargeSpace: 本月计费空间，单位：字节。
        :type TotalChargeSpace: int
        :param _FullChargeSpace: 全量计费空间，单位：字节。
        :type FullChargeSpace: int
        :param _IncrementChargeSpace: 增量计费空间，单位：字节。
        :type IncrementChargeSpace: int
        :param _FullBackupSetSize: 本月全量备份集大小，单位：字节。
        :type FullBackupSetSize: int
        :param _IncrementBackupSetSize: 本月增量备份集大小，单位：字节。
        :type IncrementBackupSetSize: int
        :param _CreateTime: 创建时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00。
        :type CreateTime: str
        :param _TimeRange: 统计周期，格式为“开始时间 - 结束时间”。
        :type TimeRange: str
        """
        self._InstanceClass = None
        self._PayType = None
        self._FreeSpace = None
        self._TotalChargeSpace = None
        self._FullChargeSpace = None
        self._IncrementChargeSpace = None
        self._FullBackupSetSize = None
        self._IncrementBackupSetSize = None
        self._CreateTime = None
        self._TimeRange = None

    @property
    def InstanceClass(self):
        r"""实例规格。
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def PayType(self):
        r"""付费方式。取值：
- postPay：后付费
- prePay：预付费
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def FreeSpace(self):
        r"""免费额度，单位：字节。取值为 -1 表示不限量。
        :rtype: int
        """
        return self._FreeSpace

    @FreeSpace.setter
    def FreeSpace(self, FreeSpace):
        self._FreeSpace = FreeSpace

    @property
    def TotalChargeSpace(self):
        r"""本月计费空间，单位：字节。
        :rtype: int
        """
        return self._TotalChargeSpace

    @TotalChargeSpace.setter
    def TotalChargeSpace(self, TotalChargeSpace):
        self._TotalChargeSpace = TotalChargeSpace

    @property
    def FullChargeSpace(self):
        r"""全量计费空间，单位：字节。
        :rtype: int
        """
        return self._FullChargeSpace

    @FullChargeSpace.setter
    def FullChargeSpace(self, FullChargeSpace):
        self._FullChargeSpace = FullChargeSpace

    @property
    def IncrementChargeSpace(self):
        r"""增量计费空间，单位：字节。
        :rtype: int
        """
        return self._IncrementChargeSpace

    @IncrementChargeSpace.setter
    def IncrementChargeSpace(self, IncrementChargeSpace):
        self._IncrementChargeSpace = IncrementChargeSpace

    @property
    def FullBackupSetSize(self):
        r"""本月全量备份集大小，单位：字节。
        :rtype: int
        """
        return self._FullBackupSetSize

    @FullBackupSetSize.setter
    def FullBackupSetSize(self, FullBackupSetSize):
        self._FullBackupSetSize = FullBackupSetSize

    @property
    def IncrementBackupSetSize(self):
        r"""本月增量备份集大小，单位：字节。
        :rtype: int
        """
        return self._IncrementBackupSetSize

    @IncrementBackupSetSize.setter
    def IncrementBackupSetSize(self, IncrementBackupSetSize):
        self._IncrementBackupSetSize = IncrementBackupSetSize

    @property
    def CreateTime(self):
        r"""创建时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TimeRange(self):
        r"""统计周期，格式为“开始时间 - 结束时间”。
        :rtype: str
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange


    def _deserialize(self, params):
        self._InstanceClass = params.get("InstanceClass")
        self._PayType = params.get("PayType")
        self._FreeSpace = params.get("FreeSpace")
        self._TotalChargeSpace = params.get("TotalChargeSpace")
        self._FullChargeSpace = params.get("FullChargeSpace")
        self._IncrementChargeSpace = params.get("IncrementChargeSpace")
        self._FullBackupSetSize = params.get("FullBackupSetSize")
        self._IncrementBackupSetSize = params.get("IncrementBackupSetSize")
        self._CreateTime = params.get("CreateTime")
        self._TimeRange = params.get("TimeRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupProgress(AbstractModel):
    r"""备份进度信息

    """

    def __init__(self):
        r"""
        :param _FullBackupStatus: 全量备份状态。
        :type FullBackupStatus: str
        :param _IncrementBackupStatus: 增量备份状态。
        :type IncrementBackupStatus: str
        :param _LastBackupTime: 上次备份执行时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未执行过备份时为空字符串。
        :type LastBackupTime: str
        :param _NextBackupTime: 下次备份执行时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未确定时为空字符串。
        :type NextBackupTime: str
        :param _LastRestoreTime: 上次恢复时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未执行过恢复时为空字符串。
        :type LastRestoreTime: str
        :param _LastRestoreStatus: 上次恢复任务状态。
        :type LastRestoreStatus: str
        :param _CurrentBackupJobStatus: 当前备份作业状态。
        :type CurrentBackupJobStatus: str
        """
        self._FullBackupStatus = None
        self._IncrementBackupStatus = None
        self._LastBackupTime = None
        self._NextBackupTime = None
        self._LastRestoreTime = None
        self._LastRestoreStatus = None
        self._CurrentBackupJobStatus = None

    @property
    def FullBackupStatus(self):
        r"""全量备份状态。
        :rtype: str
        """
        return self._FullBackupStatus

    @FullBackupStatus.setter
    def FullBackupStatus(self, FullBackupStatus):
        self._FullBackupStatus = FullBackupStatus

    @property
    def IncrementBackupStatus(self):
        r"""增量备份状态。
        :rtype: str
        """
        return self._IncrementBackupStatus

    @IncrementBackupStatus.setter
    def IncrementBackupStatus(self, IncrementBackupStatus):
        self._IncrementBackupStatus = IncrementBackupStatus

    @property
    def LastBackupTime(self):
        r"""上次备份执行时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未执行过备份时为空字符串。
        :rtype: str
        """
        return self._LastBackupTime

    @LastBackupTime.setter
    def LastBackupTime(self, LastBackupTime):
        self._LastBackupTime = LastBackupTime

    @property
    def NextBackupTime(self):
        r"""下次备份执行时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未确定时为空字符串。
        :rtype: str
        """
        return self._NextBackupTime

    @NextBackupTime.setter
    def NextBackupTime(self, NextBackupTime):
        self._NextBackupTime = NextBackupTime

    @property
    def LastRestoreTime(self):
        r"""上次恢复时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未执行过恢复时为空字符串。
        :rtype: str
        """
        return self._LastRestoreTime

    @LastRestoreTime.setter
    def LastRestoreTime(self, LastRestoreTime):
        self._LastRestoreTime = LastRestoreTime

    @property
    def LastRestoreStatus(self):
        r"""上次恢复任务状态。
        :rtype: str
        """
        return self._LastRestoreStatus

    @LastRestoreStatus.setter
    def LastRestoreStatus(self, LastRestoreStatus):
        self._LastRestoreStatus = LastRestoreStatus

    @property
    def CurrentBackupJobStatus(self):
        r"""当前备份作业状态。
        :rtype: str
        """
        return self._CurrentBackupJobStatus

    @CurrentBackupJobStatus.setter
    def CurrentBackupJobStatus(self, CurrentBackupJobStatus):
        self._CurrentBackupJobStatus = CurrentBackupJobStatus


    def _deserialize(self, params):
        self._FullBackupStatus = params.get("FullBackupStatus")
        self._IncrementBackupStatus = params.get("IncrementBackupStatus")
        self._LastBackupTime = params.get("LastBackupTime")
        self._NextBackupTime = params.get("NextBackupTime")
        self._LastRestoreTime = params.get("LastRestoreTime")
        self._LastRestoreStatus = params.get("LastRestoreStatus")
        self._CurrentBackupJobStatus = params.get("CurrentBackupJobStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSetOption(AbstractModel):
    r"""备份集加密信息

    """

    def __init__(self):
        r"""
        :param _Encryption: <p>存储加密方式。取值：<br>&quot;UnEncrypted&quot; - 非加密存储;<br>&quot;SSE-COS&quot; - 内置加密存储;<br>&quot;SSE-KMS&quot; - KMS 加密存储。</p>
        :type Encryption: str
        """
        self._Encryption = None

    @property
    def Encryption(self):
        r"""<p>存储加密方式。取值：<br>&quot;UnEncrypted&quot; - 非加密存储;<br>&quot;SSE-COS&quot; - 内置加密存储;<br>&quot;SSE-KMS&quot; - KMS 加密存储。</p>
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupStrategy(AbstractModel):
    r"""备份策略

    """

    def __init__(self):
        r"""
        :param _BackupStartTime: 全量备份开始时间。周期性的全量备份将在当天该时间开始。
        :type BackupStartTime: str
        :param _StorageStrategy: 存储策略。
        :type StorageStrategy: :class:`tencentcloud.dbs.v20211108.models.StorageStrategy`
        :param _BackupPeriod: 备份周期。
        :type BackupPeriod: :class:`tencentcloud.dbs.v20211108.models.BackupPeriod`
        :param _BackupMethod: 备份方法。目前仅支持 "logical" - 逻辑备份。
        :type BackupMethod: str
        :param _StrategyType: 备份周期。支持的值包括：
"period" - 周期性备份；
"single" - 单次备份。
默认值为"period"。
        :type StrategyType: str
        :param _EnableIncrement: 是否开启增量备份。可能的取值为["true", "false"]。默认值为"true"。
        :type EnableIncrement: bool
        """
        self._BackupStartTime = None
        self._StorageStrategy = None
        self._BackupPeriod = None
        self._BackupMethod = None
        self._StrategyType = None
        self._EnableIncrement = None

    @property
    def BackupStartTime(self):
        r"""全量备份开始时间。周期性的全量备份将在当天该时间开始。
        :rtype: str
        """
        return self._BackupStartTime

    @BackupStartTime.setter
    def BackupStartTime(self, BackupStartTime):
        self._BackupStartTime = BackupStartTime

    @property
    def StorageStrategy(self):
        r"""存储策略。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.StorageStrategy`
        """
        return self._StorageStrategy

    @StorageStrategy.setter
    def StorageStrategy(self, StorageStrategy):
        self._StorageStrategy = StorageStrategy

    @property
    def BackupPeriod(self):
        r"""备份周期。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupPeriod`
        """
        return self._BackupPeriod

    @BackupPeriod.setter
    def BackupPeriod(self, BackupPeriod):
        self._BackupPeriod = BackupPeriod

    @property
    def BackupMethod(self):
        r"""备份方法。目前仅支持 "logical" - 逻辑备份。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def StrategyType(self):
        r"""备份周期。支持的值包括：
"period" - 周期性备份；
"single" - 单次备份。
默认值为"period"。
        :rtype: str
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def EnableIncrement(self):
        r"""是否开启增量备份。可能的取值为["true", "false"]。默认值为"true"。
        :rtype: bool
        """
        return self._EnableIncrement

    @EnableIncrement.setter
    def EnableIncrement(self, EnableIncrement):
        self._EnableIncrement = EnableIncrement


    def _deserialize(self, params):
        self._BackupStartTime = params.get("BackupStartTime")
        if params.get("StorageStrategy") is not None:
            self._StorageStrategy = StorageStrategy()
            self._StorageStrategy._deserialize(params.get("StorageStrategy"))
        if params.get("BackupPeriod") is not None:
            self._BackupPeriod = BackupPeriod()
            self._BackupPeriod._deserialize(params.get("BackupPeriod"))
        self._BackupMethod = params.get("BackupMethod")
        self._StrategyType = params.get("StrategyType")
        self._EnableIncrement = params.get("EnableIncrement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupStrategyItem(AbstractModel):
    r"""备份策略

    """

    def __init__(self):
        r"""
        :param _BackupStartTime: 全量备份开始时间。周期性的全量备份将在当天该时间开始，格式：HH:mm（24 小时制），如 02:00。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStartTime: str
        :param _StorageStrategy: 存储策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageStrategy: :class:`tencentcloud.dbs.v20211108.models.StorageStrategyItem`
        :param _BackupPeriod: 备份周期。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupPeriod: :class:`tencentcloud.dbs.v20211108.models.BackupPeriodItem`
        :param _BackupMethod: 备份方法。目前仅支持 "logical" - 逻辑备份。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupMethod: str
        :param _StrategyType: 备份周期。支持的值包括：
"period" - 周期性备份；
"single" - 单次备份。
默认值为"period"。
        :type StrategyType: str
        :param _EnableIncrement: 是否开启增量备份。可能的取值为["true", "false"]。默认值为"true"。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableIncrement: bool
        """
        self._BackupStartTime = None
        self._StorageStrategy = None
        self._BackupPeriod = None
        self._BackupMethod = None
        self._StrategyType = None
        self._EnableIncrement = None

    @property
    def BackupStartTime(self):
        r"""全量备份开始时间。周期性的全量备份将在当天该时间开始，格式：HH:mm（24 小时制），如 02:00。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupStartTime

    @BackupStartTime.setter
    def BackupStartTime(self, BackupStartTime):
        self._BackupStartTime = BackupStartTime

    @property
    def StorageStrategy(self):
        r"""存储策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.StorageStrategyItem`
        """
        return self._StorageStrategy

    @StorageStrategy.setter
    def StorageStrategy(self, StorageStrategy):
        self._StorageStrategy = StorageStrategy

    @property
    def BackupPeriod(self):
        r"""备份周期。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupPeriodItem`
        """
        return self._BackupPeriod

    @BackupPeriod.setter
    def BackupPeriod(self, BackupPeriod):
        self._BackupPeriod = BackupPeriod

    @property
    def BackupMethod(self):
        r"""备份方法。目前仅支持 "logical" - 逻辑备份。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def StrategyType(self):
        r"""备份周期。支持的值包括：
"period" - 周期性备份；
"single" - 单次备份。
默认值为"period"。
        :rtype: str
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def EnableIncrement(self):
        r"""是否开启增量备份。可能的取值为["true", "false"]。默认值为"true"。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableIncrement

    @EnableIncrement.setter
    def EnableIncrement(self, EnableIncrement):
        self._EnableIncrement = EnableIncrement


    def _deserialize(self, params):
        self._BackupStartTime = params.get("BackupStartTime")
        if params.get("StorageStrategy") is not None:
            self._StorageStrategy = StorageStrategyItem()
            self._StorageStrategy._deserialize(params.get("StorageStrategy"))
        if params.get("BackupPeriod") is not None:
            self._BackupPeriod = BackupPeriodItem()
            self._BackupPeriod._deserialize(params.get("BackupPeriod"))
        self._BackupMethod = params.get("BackupMethod")
        self._StrategyType = params.get("StrategyType")
        self._EnableIncrement = params.get("EnableIncrement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupTableItem(AbstractModel):
    r"""备份表对象

    """

    def __init__(self):
        r"""
        :param _TableName: 表名。
        :type TableName: str
        :param _NewTableName: 重命名后的表名。
        :type NewTableName: str
        :param _Columns: 列对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of BackupColumnItem
        """
        self._TableName = None
        self._NewTableName = None
        self._Columns = None

    @property
    def TableName(self):
        r"""表名。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        r"""重命名后的表名。
        :rtype: str
        """
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName

    @property
    def Columns(self):
        r"""列对象。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BackupColumnItem
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._NewTableName = params.get("NewTableName")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = BackupColumnItem()
                obj._deserialize(item)
                self._Columns.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureBackupPlanRequest(AbstractModel):
    r"""ConfigureBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。
        :type BackupPlanId: str
        :param _BackupPlanName: 备份计划名称。支持数字、英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@,且长度不能超过60。
        :type BackupPlanName: str
        :param _UpperParallel: 全量备份并发数上限。
        :type UpperParallel: int
        :param _SourceEndPoint: 备份源实例信息。
        :type SourceEndPoint: :class:`tencentcloud.dbs.v20211108.models.BackupEndpoint`
        :param _BackupObject: 备份对象信息。
        :type BackupObject: :class:`tencentcloud.dbs.v20211108.models.BackupObject`
        :param _BackupStrategy: 备份策略。
        :type BackupStrategy: :class:`tencentcloud.dbs.v20211108.models.BackupStrategy`
        :param _PlainText: 加密信息。当需要使用SSE-KMS需要传入该值，你可以通过 KMS 的 GenerateDataKey 接口生成。
        :type PlainText: str
        """
        self._BackupPlanId = None
        self._BackupPlanName = None
        self._UpperParallel = None
        self._SourceEndPoint = None
        self._BackupObject = None
        self._BackupStrategy = None
        self._PlainText = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId

    @property
    def BackupPlanName(self):
        r"""备份计划名称。支持数字、英文大小写字母、中文以及特殊字符_-./()（）[]+=：:@,且长度不能超过60。
        :rtype: str
        """
        return self._BackupPlanName

    @BackupPlanName.setter
    def BackupPlanName(self, BackupPlanName):
        self._BackupPlanName = BackupPlanName

    @property
    def UpperParallel(self):
        r"""全量备份并发数上限。
        :rtype: int
        """
        return self._UpperParallel

    @UpperParallel.setter
    def UpperParallel(self, UpperParallel):
        self._UpperParallel = UpperParallel

    @property
    def SourceEndPoint(self):
        r"""备份源实例信息。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupEndpoint`
        """
        return self._SourceEndPoint

    @SourceEndPoint.setter
    def SourceEndPoint(self, SourceEndPoint):
        self._SourceEndPoint = SourceEndPoint

    @property
    def BackupObject(self):
        r"""备份对象信息。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupObject`
        """
        return self._BackupObject

    @BackupObject.setter
    def BackupObject(self, BackupObject):
        self._BackupObject = BackupObject

    @property
    def BackupStrategy(self):
        r"""备份策略。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupStrategy`
        """
        return self._BackupStrategy

    @BackupStrategy.setter
    def BackupStrategy(self, BackupStrategy):
        self._BackupStrategy = BackupStrategy

    @property
    def PlainText(self):
        r"""加密信息。当需要使用SSE-KMS需要传入该值，你可以通过 KMS 的 GenerateDataKey 接口生成。
        :rtype: str
        """
        return self._PlainText

    @PlainText.setter
    def PlainText(self, PlainText):
        self._PlainText = PlainText


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        self._BackupPlanName = params.get("BackupPlanName")
        self._UpperParallel = params.get("UpperParallel")
        if params.get("SourceEndPoint") is not None:
            self._SourceEndPoint = BackupEndpoint()
            self._SourceEndPoint._deserialize(params.get("SourceEndPoint"))
        if params.get("BackupObject") is not None:
            self._BackupObject = BackupObject()
            self._BackupObject._deserialize(params.get("BackupObject"))
        if params.get("BackupStrategy") is not None:
            self._BackupStrategy = BackupStrategy()
            self._BackupStrategy._deserialize(params.get("BackupStrategy"))
        self._PlainText = params.get("PlainText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureBackupPlanResponse(AbstractModel):
    r"""ConfigureBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ConnectTestResult(AbstractModel):
    r"""连通性检测结果

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务 ID</p>
        :type TaskId: int
        :param _Status: <p>任务状态</p>
        :type Status: str
        :param _IsPass: <p>是否通过。0 表示未通过，1 表示通过。</p>
        :type IsPass: int
        :param _Addr: <p>源端地址</p>
        :type Addr: str
        :param _SNatIp: <p>源地址转换IP</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SNatIp: str
        :param _TestItems: <p>检测结果集</p>
        :type TestItems: list of TestItem
        """
        self._TaskId = None
        self._Status = None
        self._IsPass = None
        self._Addr = None
        self._SNatIp = None
        self._TestItems = None

    @property
    def TaskId(self):
        r"""<p>任务 ID</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""<p>任务状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsPass(self):
        r"""<p>是否通过。0 表示未通过，1 表示通过。</p>
        :rtype: int
        """
        return self._IsPass

    @IsPass.setter
    def IsPass(self, IsPass):
        self._IsPass = IsPass

    @property
    def Addr(self):
        r"""<p>源端地址</p>
        :rtype: str
        """
        return self._Addr

    @Addr.setter
    def Addr(self, Addr):
        self._Addr = Addr

    @property
    def SNatIp(self):
        r"""<p>源地址转换IP</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SNatIp

    @SNatIp.setter
    def SNatIp(self, SNatIp):
        self._SNatIp = SNatIp

    @property
    def TestItems(self):
        r"""<p>检测结果集</p>
        :rtype: list of TestItem
        """
        return self._TestItems

    @TestItems.setter
    def TestItems(self, TestItems):
        self._TestItems = TestItems


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._IsPass = params.get("IsPass")
        self._Addr = params.get("Addr")
        self._SNatIp = params.get("SNatIp")
        if params.get("TestItems") is not None:
            self._TestItems = []
            for item in params.get("TestItems"):
                obj = TestItem()
                obj._deserialize(item)
                self._TestItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupPlanRequest(AbstractModel):
    r"""CreateBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseType: 源端数据库类型。当前支持值为: ["mysql","cynosdbmysql","percona","mariadb","tdsqlmysql"]。
        :type DatabaseType: str
        :param _BackupMethod: 备份方式。当前仅支持"logical"，即逻辑备份。
        :type BackupMethod: str
        :param _InstanceClass: 规格。当前支持值为: ["micro","small","medium","large","xlarge"]。默认为"small"。
        :type InstanceClass: str
        :param _Period: 购买时长，单位为月，默认值为1。
        :type Period: int
        :param _PayType: 计费模式。当前仅支持"prepay"，即包年包月。
        :type PayType: str
        :param _Count: 购买数量。取值范围为[1, 10]，默认值为1。
        :type Count: int
        :param _AutoRenew: 自动续费标识。1 - 开启自动续费；0 - 不开启自动续费。
        :type AutoRenew: int
        :param _Tags: 标签值。
        :type Tags: list of Tag
        """
        self._DatabaseType = None
        self._BackupMethod = None
        self._InstanceClass = None
        self._Period = None
        self._PayType = None
        self._Count = None
        self._AutoRenew = None
        self._Tags = None

    @property
    def DatabaseType(self):
        r"""源端数据库类型。当前支持值为: ["mysql","cynosdbmysql","percona","mariadb","tdsqlmysql"]。
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def BackupMethod(self):
        r"""备份方式。当前仅支持"logical"，即逻辑备份。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def InstanceClass(self):
        r"""规格。当前支持值为: ["micro","small","medium","large","xlarge"]。默认为"small"。
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def Period(self):
        r"""购买时长，单位为月，默认值为1。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def PayType(self):
        r"""计费模式。当前仅支持"prepay"，即包年包月。
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Count(self):
        r"""购买数量。取值范围为[1, 10]，默认值为1。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AutoRenew(self):
        r"""自动续费标识。1 - 开启自动续费；0 - 不开启自动续费。
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Tags(self):
        r"""标签值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DatabaseType = params.get("DatabaseType")
        self._BackupMethod = params.get("BackupMethod")
        self._InstanceClass = params.get("InstanceClass")
        self._Period = params.get("Period")
        self._PayType = params.get("PayType")
        self._Count = params.get("Count")
        self._AutoRenew = params.get("AutoRenew")
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
        


class CreateBackupPlanResponse(AbstractModel):
    r"""CreateBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单参数。
        :type OrderId: str
        :param _BackupPlanIds: 备份计划 ID 列表。单次最多返回 10 个。
        :type BackupPlanIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._BackupPlanIds = None
        self._RequestId = None

    @property
    def OrderId(self):
        r"""订单参数。
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def BackupPlanIds(self):
        r"""备份计划 ID 列表。单次最多返回 10 个。
        :rtype: list of str
        """
        return self._BackupPlanIds

    @BackupPlanIds.setter
    def BackupPlanIds(self, BackupPlanIds):
        self._BackupPlanIds = BackupPlanIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._BackupPlanIds = params.get("BackupPlanIds")
        self._RequestId = params.get("RequestId")


class CreateConnectTestJobRequest(AbstractModel):
    r"""CreateConnectTestJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoint: 备份源实例信息。
        :type Endpoint: :class:`tencentcloud.dbs.v20211108.models.BackupEndpoint`
        """
        self._Endpoint = None

    @property
    def Endpoint(self):
        r"""备份源实例信息。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupEndpoint`
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


    def _deserialize(self, params):
        if params.get("Endpoint") is not None:
            self._Endpoint = BackupEndpoint()
            self._Endpoint._deserialize(params.get("Endpoint"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectTestJobResponse(AbstractModel):
    r"""CreateConnectTestJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnTaskId: 连通性任务 ID。
        :type ConnTaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConnTaskId = None
        self._RequestId = None

    @property
    def ConnTaskId(self):
        r"""连通性任务 ID。
        :rtype: str
        """
        return self._ConnTaskId

    @ConnTaskId.setter
    def ConnTaskId(self, ConnTaskId):
        self._ConnTaskId = ConnTaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConnTaskId = params.get("ConnTaskId")
        self._RequestId = params.get("RequestId")


class DeleteBackupPlanRequest(AbstractModel):
    r"""DeleteBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。可通过 DescribeBackupPlans 接口获取。
        :type BackupPlanId: str
        """
        self._BackupPlanId = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。可通过 DescribeBackupPlans 接口获取。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupPlanResponse(AbstractModel):
    r"""DeleteBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeBackupCheckJobRequest(AbstractModel):
    r"""DescribeBackupCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。
        :type BackupPlanId: str
        """
        self._BackupPlanId = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupCheckJobResponse(AbstractModel):
    r"""DescribeBackupCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 校验任务状态。可能的取值为："finished" - 已完成; "running" - 进行中。
        :type Status: str
        :param _Progress: 任务进度。取值范围为[0, 100]，表示任务完成的百分比。例如：30表示任务完成30%。
        :type Progress: int
        :param _CheckFlag: 校验是否通过标记。可能的取值为："1" - 校验通过;"0" - 校验未通过。
        :type CheckFlag: int
        :param _ErrMessage: 错误信息。
        :type ErrMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Progress = None
        self._CheckFlag = None
        self._ErrMessage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""校验任务状态。可能的取值为："finished" - 已完成; "running" - 进行中。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        r"""任务进度。取值范围为[0, 100]，表示任务完成的百分比。例如：30表示任务完成30%。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CheckFlag(self):
        r"""校验是否通过标记。可能的取值为："1" - 校验通过;"0" - 校验未通过。
        :rtype: int
        """
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def ErrMessage(self):
        r"""错误信息。
        :rtype: str
        """
        return self._ErrMessage

    @ErrMessage.setter
    def ErrMessage(self, ErrMessage):
        self._ErrMessage = ErrMessage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._CheckFlag = params.get("CheckFlag")
        self._ErrMessage = params.get("ErrMessage")
        self._RequestId = params.get("RequestId")


class DescribeBackupPlanDetailRequest(AbstractModel):
    r"""DescribeBackupPlanDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: <p>备份计划 ID。可通过 DescribeBackupPlans 接口获取。</p>
        :type BackupPlanId: str
        """
        self._BackupPlanId = None

    @property
    def BackupPlanId(self):
        r"""<p>备份计划 ID。可通过 DescribeBackupPlans 接口获取。</p>
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupPlanDetailResponse(AbstractModel):
    r"""DescribeBackupPlanDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Region: <p>地域。</p>
        :type Region: str
        :param _BackupPlanId: <p>备份计划 ID。</p>
        :type BackupPlanId: str
        :param _BackupPlanName: <p>备份计划名称。</p>
        :type BackupPlanName: str
        :param _Status: <p>备份计划状态。取值：</p><ul><li>creating：创建中</li><li>notStarted：未启动</li><li>notConfigured：未配置</li><li>checkNotPass：校验未通过</li><li>checkPass：校验通过</li><li>checking：校验中</li><li>readyRun：待运行</li><li>running：运行中</li><li>fullBacking：全量备份中</li><li>paused：已暂停</li><li>isolating：隔离中</li><li>isolated：已隔离</li><li>offlining：下线中</li><li>offlined：已下线</li><li>completed：已完成</li></ul>
        :type Status: str
        :param _SourceEndPoint: <p>源库连接信息列表。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceEndPoint: list of Endpoint
        :param _BackupObject: <p>备份对象信息。</p>
        :type BackupObject: :class:`tencentcloud.dbs.v20211108.models.BackupObject`
        :param _BackupStrategy: <p>备份策略。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStrategy: :class:`tencentcloud.dbs.v20211108.models.BackupStrategyItem`
        :param _Progress: <p>备份进度信息。</p>
        :type Progress: :class:`tencentcloud.dbs.v20211108.models.BackupProgress`
        :param _ErrorInfo: <p>错误异常信息。</p>
        :type ErrorInfo: :class:`tencentcloud.dbs.v20211108.models.ErrorInfo`
        :param _CreateTime: <p>创建时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00。</p>
        :type CreateTime: str
        :param _ExpireTime: <p>到期时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，后付费计划无到期时间时为空字符串。</p>
        :type ExpireTime: str
        :param _OfflineTime: <p>下线时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未下线时为空字符串。</p>
        :type OfflineTime: str
        :param _AutoRenewFlag: <p>自动续费标识。取值：</p><ul><li>0：不自动续费</li><li>1：自动续费</li></ul>
        :type AutoRenewFlag: int
        :param _SourceInfo: <p>主节点连接信息。云数据库实例为实例 ID，云服务器自建为实例 ID:端口，其余为 ip:port。</p>
        :type SourceInfo: list of str
        :param _SetSourceInfo: <p>从节点连接信息，格式同 SourceInfo。</p>
        :type SetSourceInfo: list of str
        :param _Tags: <p>标签信息列表。未绑定标签时返回 null。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param _LastBackupJobTime: <p>上次备份作业时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未执行过备份作业时为空字符串。</p>
        :type LastBackupJobTime: str
        :param _LastFullBackupJobStatus: <p>上次全量备份作业状态。</p>
        :type LastFullBackupJobStatus: str
        :param _LastIncBackupJobStatus: <p>上次增量备份作业状态。</p>
        :type LastIncBackupJobStatus: str
        :param _NextBackupJobTime: <p>下次备份作业时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未确定时为空字符串。</p>
        :type NextBackupJobTime: str
        :param _LastRestoreJobTime: <p>上次恢复作业时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未执行过恢复作业时为空字符串。</p>
        :type LastRestoreJobTime: str
        :param _LastRestoreJobStatus: <p>上次恢复作业状态。</p>
        :type LastRestoreJobStatus: str
        :param _PayInfo: <p>付费信息。</p>
        :type PayInfo: :class:`tencentcloud.dbs.v20211108.models.BackupPlanPayInfo`
        :param _UpperParallel: <p>全量备份并行数上限。</p>
        :type UpperParallel: int
        :param _UpperBandwidth: <p>带宽上限，单位：MB/s。</p>
        :type UpperBandwidth: int
        :param _AllowedActions: <p>当前状态下允许的操作。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowedActions: list of str
        :param _RestoreRange: <p>可恢复时间范围。</p>
        :type RestoreRange: :class:`tencentcloud.dbs.v20211108.models.RestoreRange`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Region = None
        self._BackupPlanId = None
        self._BackupPlanName = None
        self._Status = None
        self._SourceEndPoint = None
        self._BackupObject = None
        self._BackupStrategy = None
        self._Progress = None
        self._ErrorInfo = None
        self._CreateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._AutoRenewFlag = None
        self._SourceInfo = None
        self._SetSourceInfo = None
        self._Tags = None
        self._LastBackupJobTime = None
        self._LastFullBackupJobStatus = None
        self._LastIncBackupJobStatus = None
        self._NextBackupJobTime = None
        self._LastRestoreJobTime = None
        self._LastRestoreJobStatus = None
        self._PayInfo = None
        self._UpperParallel = None
        self._UpperBandwidth = None
        self._AllowedActions = None
        self._RestoreRange = None
        self._RequestId = None

    @property
    def Region(self):
        r"""<p>地域。</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BackupPlanId(self):
        r"""<p>备份计划 ID。</p>
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId

    @property
    def BackupPlanName(self):
        r"""<p>备份计划名称。</p>
        :rtype: str
        """
        return self._BackupPlanName

    @BackupPlanName.setter
    def BackupPlanName(self, BackupPlanName):
        self._BackupPlanName = BackupPlanName

    @property
    def Status(self):
        r"""<p>备份计划状态。取值：</p><ul><li>creating：创建中</li><li>notStarted：未启动</li><li>notConfigured：未配置</li><li>checkNotPass：校验未通过</li><li>checkPass：校验通过</li><li>checking：校验中</li><li>readyRun：待运行</li><li>running：运行中</li><li>fullBacking：全量备份中</li><li>paused：已暂停</li><li>isolating：隔离中</li><li>isolated：已隔离</li><li>offlining：下线中</li><li>offlined：已下线</li><li>completed：已完成</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceEndPoint(self):
        r"""<p>源库连接信息列表。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Endpoint
        """
        return self._SourceEndPoint

    @SourceEndPoint.setter
    def SourceEndPoint(self, SourceEndPoint):
        self._SourceEndPoint = SourceEndPoint

    @property
    def BackupObject(self):
        r"""<p>备份对象信息。</p>
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupObject`
        """
        return self._BackupObject

    @BackupObject.setter
    def BackupObject(self, BackupObject):
        self._BackupObject = BackupObject

    @property
    def BackupStrategy(self):
        r"""<p>备份策略。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupStrategyItem`
        """
        return self._BackupStrategy

    @BackupStrategy.setter
    def BackupStrategy(self, BackupStrategy):
        self._BackupStrategy = BackupStrategy

    @property
    def Progress(self):
        r"""<p>备份进度信息。</p>
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupProgress`
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def ErrorInfo(self):
        r"""<p>错误异常信息。</p>
        :rtype: :class:`tencentcloud.dbs.v20211108.models.ErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def CreateTime(self):
        r"""<p>创建时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00。</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""<p>到期时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，后付费计划无到期时间时为空字符串。</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        r"""<p>下线时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未下线时为空字符串。</p>
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def AutoRenewFlag(self):
        r"""<p>自动续费标识。取值：</p><ul><li>0：不自动续费</li><li>1：自动续费</li></ul>
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SourceInfo(self):
        r"""<p>主节点连接信息。云数据库实例为实例 ID，云服务器自建为实例 ID:端口，其余为 ip:port。</p>
        :rtype: list of str
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo

    @property
    def SetSourceInfo(self):
        r"""<p>从节点连接信息，格式同 SourceInfo。</p>
        :rtype: list of str
        """
        return self._SetSourceInfo

    @SetSourceInfo.setter
    def SetSourceInfo(self, SetSourceInfo):
        self._SetSourceInfo = SetSourceInfo

    @property
    def Tags(self):
        r"""<p>标签信息列表。未绑定标签时返回 null。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LastBackupJobTime(self):
        r"""<p>上次备份作业时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未执行过备份作业时为空字符串。</p>
        :rtype: str
        """
        return self._LastBackupJobTime

    @LastBackupJobTime.setter
    def LastBackupJobTime(self, LastBackupJobTime):
        self._LastBackupJobTime = LastBackupJobTime

    @property
    def LastFullBackupJobStatus(self):
        r"""<p>上次全量备份作业状态。</p>
        :rtype: str
        """
        return self._LastFullBackupJobStatus

    @LastFullBackupJobStatus.setter
    def LastFullBackupJobStatus(self, LastFullBackupJobStatus):
        self._LastFullBackupJobStatus = LastFullBackupJobStatus

    @property
    def LastIncBackupJobStatus(self):
        r"""<p>上次增量备份作业状态。</p>
        :rtype: str
        """
        return self._LastIncBackupJobStatus

    @LastIncBackupJobStatus.setter
    def LastIncBackupJobStatus(self, LastIncBackupJobStatus):
        self._LastIncBackupJobStatus = LastIncBackupJobStatus

    @property
    def NextBackupJobTime(self):
        r"""<p>下次备份作业时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未确定时为空字符串。</p>
        :rtype: str
        """
        return self._NextBackupJobTime

    @NextBackupJobTime.setter
    def NextBackupJobTime(self, NextBackupJobTime):
        self._NextBackupJobTime = NextBackupJobTime

    @property
    def LastRestoreJobTime(self):
        r"""<p>上次恢复作业时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，尚未执行过恢复作业时为空字符串。</p>
        :rtype: str
        """
        return self._LastRestoreJobTime

    @LastRestoreJobTime.setter
    def LastRestoreJobTime(self, LastRestoreJobTime):
        self._LastRestoreJobTime = LastRestoreJobTime

    @property
    def LastRestoreJobStatus(self):
        r"""<p>上次恢复作业状态。</p>
        :rtype: str
        """
        return self._LastRestoreJobStatus

    @LastRestoreJobStatus.setter
    def LastRestoreJobStatus(self, LastRestoreJobStatus):
        self._LastRestoreJobStatus = LastRestoreJobStatus

    @property
    def PayInfo(self):
        r"""<p>付费信息。</p>
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupPlanPayInfo`
        """
        return self._PayInfo

    @PayInfo.setter
    def PayInfo(self, PayInfo):
        self._PayInfo = PayInfo

    @property
    def UpperParallel(self):
        r"""<p>全量备份并行数上限。</p>
        :rtype: int
        """
        return self._UpperParallel

    @UpperParallel.setter
    def UpperParallel(self, UpperParallel):
        self._UpperParallel = UpperParallel

    @property
    def UpperBandwidth(self):
        r"""<p>带宽上限，单位：MB/s。</p>
        :rtype: int
        """
        return self._UpperBandwidth

    @UpperBandwidth.setter
    def UpperBandwidth(self, UpperBandwidth):
        self._UpperBandwidth = UpperBandwidth

    @property
    def AllowedActions(self):
        r"""<p>当前状态下允许的操作。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AllowedActions

    @AllowedActions.setter
    def AllowedActions(self, AllowedActions):
        self._AllowedActions = AllowedActions

    @property
    def RestoreRange(self):
        r"""<p>可恢复时间范围。</p>
        :rtype: :class:`tencentcloud.dbs.v20211108.models.RestoreRange`
        """
        return self._RestoreRange

    @RestoreRange.setter
    def RestoreRange(self, RestoreRange):
        self._RestoreRange = RestoreRange

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._BackupPlanId = params.get("BackupPlanId")
        self._BackupPlanName = params.get("BackupPlanName")
        self._Status = params.get("Status")
        if params.get("SourceEndPoint") is not None:
            self._SourceEndPoint = []
            for item in params.get("SourceEndPoint"):
                obj = Endpoint()
                obj._deserialize(item)
                self._SourceEndPoint.append(obj)
        if params.get("BackupObject") is not None:
            self._BackupObject = BackupObject()
            self._BackupObject._deserialize(params.get("BackupObject"))
        if params.get("BackupStrategy") is not None:
            self._BackupStrategy = BackupStrategyItem()
            self._BackupStrategy._deserialize(params.get("BackupStrategy"))
        if params.get("Progress") is not None:
            self._Progress = BackupProgress()
            self._Progress._deserialize(params.get("Progress"))
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SourceInfo = params.get("SourceInfo")
        self._SetSourceInfo = params.get("SetSourceInfo")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._LastBackupJobTime = params.get("LastBackupJobTime")
        self._LastFullBackupJobStatus = params.get("LastFullBackupJobStatus")
        self._LastIncBackupJobStatus = params.get("LastIncBackupJobStatus")
        self._NextBackupJobTime = params.get("NextBackupJobTime")
        self._LastRestoreJobTime = params.get("LastRestoreJobTime")
        self._LastRestoreJobStatus = params.get("LastRestoreJobStatus")
        if params.get("PayInfo") is not None:
            self._PayInfo = BackupPlanPayInfo()
            self._PayInfo._deserialize(params.get("PayInfo"))
        self._UpperParallel = params.get("UpperParallel")
        self._UpperBandwidth = params.get("UpperBandwidth")
        self._AllowedActions = params.get("AllowedActions")
        if params.get("RestoreRange") is not None:
            self._RestoreRange = RestoreRange()
            self._RestoreRange._deserialize(params.get("RestoreRange"))
        self._RequestId = params.get("RequestId")


class DescribeBackupPlansRequest(AbstractModel):
    r"""DescribeBackupPlans请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 过滤条件，备份计划 ID。
        :type BackupPlanId: str
        :param _Status: 过滤条件，备份计划状态。
        :type Status: list of str
        :param _DatabaseType: 过滤条件，数据库类型。
        :type DatabaseType: list of str
        :param _AccessType: 过滤条件，接入访问类型。
        :type AccessType: list of str
        :param _BackupPlanName: 过滤条件，备份计划名称。
        :type BackupPlanName: str
        :param _TagFilters: 过滤条件，标签键值。
        :type TagFilters: list of TagFilter
        :param _Limit: 分页参数。取值范围为(0, 100]，默认值为20。
        :type Limit: int
        :param _Offset: 分页参数。默认值为0。
        :type Offset: int
        """
        self._BackupPlanId = None
        self._Status = None
        self._DatabaseType = None
        self._AccessType = None
        self._BackupPlanName = None
        self._TagFilters = None
        self._Limit = None
        self._Offset = None

    @property
    def BackupPlanId(self):
        r"""过滤条件，备份计划 ID。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId

    @property
    def Status(self):
        r"""过滤条件，备份计划状态。
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DatabaseType(self):
        r"""过滤条件，数据库类型。
        :rtype: list of str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def AccessType(self):
        r"""过滤条件，接入访问类型。
        :rtype: list of str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def BackupPlanName(self):
        r"""过滤条件，备份计划名称。
        :rtype: str
        """
        return self._BackupPlanName

    @BackupPlanName.setter
    def BackupPlanName(self, BackupPlanName):
        self._BackupPlanName = BackupPlanName

    @property
    def TagFilters(self):
        r"""过滤条件，标签键值。
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def Limit(self):
        r"""分页参数。取值范围为(0, 100]，默认值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页参数。默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        self._Status = params.get("Status")
        self._DatabaseType = params.get("DatabaseType")
        self._AccessType = params.get("AccessType")
        self._BackupPlanName = params.get("BackupPlanName")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupPlansResponse(AbstractModel):
    r"""DescribeBackupPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 备份计划数量。
        :type TotalCount: int
        :param _Items: 备份计划详情。
        :type Items: list of BackupPlanInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""备份计划数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""备份计划详情。
        :rtype: list of BackupPlanInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackupPlanInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConnectTestResultRequest(AbstractModel):
    r"""DescribeConnectTestResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: <p>连通性检测任务 ID。</p>
        :type TaskIds: list of int
        """
        self._TaskIds = None

    @property
    def TaskIds(self):
        r"""<p>连通性检测任务 ID。</p>
        :rtype: list of int
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConnectTestResultResponse(AbstractModel):
    r"""DescribeConnectTestResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>任务总数。</p>
        :type TotalCount: int
        :param _Items: <p>检测结果详情。</p>
        :type Items: list of ConnectTestResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>任务总数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""<p>检测结果详情。</p>
        :rtype: list of ConnectTestResult
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConnectTestResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFullBackupSetDetailRequest(AbstractModel):
    r"""DescribeFullBackupSetDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupSetId: <p>全量备份集 ID。可通过 DescribeFullBackupSets 接口获取。</p>
        :type BackupSetId: str
        """
        self._BackupSetId = None

    @property
    def BackupSetId(self):
        r"""<p>全量备份集 ID。可通过 DescribeFullBackupSets 接口获取。</p>
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId


    def _deserialize(self, params):
        self._BackupSetId = params.get("BackupSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFullBackupSetDetailResponse(AbstractModel):
    r"""DescribeFullBackupSetDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupSet: <p>全量备份集详情。</p>
        :type BackupSet: :class:`tencentcloud.dbs.v20211108.models.FullBackupSetDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupSet = None
        self._RequestId = None

    @property
    def BackupSet(self):
        r"""<p>全量备份集详情。</p>
        :rtype: :class:`tencentcloud.dbs.v20211108.models.FullBackupSetDetail`
        """
        return self._BackupSet

    @BackupSet.setter
    def BackupSet(self, BackupSet):
        self._BackupSet = BackupSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackupSet") is not None:
            self._BackupSet = FullBackupSetDetail()
            self._BackupSet._deserialize(params.get("BackupSet"))
        self._RequestId = params.get("RequestId")


class DescribeIncrementBackupSetFilesRequest(AbstractModel):
    r"""DescribeIncrementBackupSetFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupSetId: 增量备份集 ID。可通过 DescribeIncrementBackupSets 接口获取。
        :type BackupSetId: str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 10。
        :type Limit: int
        """
        self._BackupSetId = None
        self._Offset = None
        self._Limit = None

    @property
    def BackupSetId(self):
        r"""增量备份集 ID。可通过 DescribeIncrementBackupSets 接口获取。
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为 10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._BackupSetId = params.get("BackupSetId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIncrementBackupSetFilesResponse(AbstractModel):
    r"""DescribeIncrementBackupSetFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 文件总数。
        :type TotalCount: int
        :param _BackupFiles: 增量备份文件列表。
        :type BackupFiles: list of BackupFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupFiles = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""文件总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupFiles(self):
        r"""增量备份文件列表。
        :rtype: list of BackupFile
        """
        return self._BackupFiles

    @BackupFiles.setter
    def BackupFiles(self, BackupFiles):
        self._BackupFiles = BackupFiles

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupFiles") is not None:
            self._BackupFiles = []
            for item in params.get("BackupFiles"):
                obj = BackupFile()
                obj._deserialize(item)
                self._BackupFiles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIncrementBackupSetsRequest(AbstractModel):
    r"""DescribeIncrementBackupSets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。
        :type BackupPlanId: str
        :param _BackupSetId: 过滤条件，备份集 ID。
        :type BackupSetId: str
        :param _Limit: 分页参数。取值范围为(0, 100]，默认值为20。
        :type Limit: int
        :param _Offset: 分页参数。默认值为0。
        :type Offset: int
        """
        self._BackupPlanId = None
        self._BackupSetId = None
        self._Limit = None
        self._Offset = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId

    @property
    def BackupSetId(self):
        r"""过滤条件，备份集 ID。
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def Limit(self):
        r"""分页参数。取值范围为(0, 100]，默认值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页参数。默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        self._BackupSetId = params.get("BackupSetId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIncrementBackupSetsResponse(AbstractModel):
    r"""DescribeIncrementBackupSets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 增量备份集数量。
        :type TotalCount: int
        :param _Items: 增量备份集信息。
        :type Items: list of IncrementBackup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""增量备份集数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""增量备份集信息。
        :rtype: list of IncrementBackup
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = IncrementBackup()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyBackupPlanByUserRequest(AbstractModel):
    r"""DestroyBackupPlanByUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。可通过 DescribeBackupPlans 接口获取。
        :type BackupPlanId: str
        """
        self._BackupPlanId = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。可通过 DescribeBackupPlans 接口获取。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyBackupPlanByUserResponse(AbstractModel):
    r"""DestroyBackupPlanByUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Endpoint(AbstractModel):
    r"""备份源实例详情

    """

    def __init__(self):
        r"""
        :param _Role: 节点角色。取值：
"master" - 主节点;
"slave" - 从节点。
        :type Role: str
        :param _DatabaseType: 数据库类型。目前支持的值["mysql", "mariadb", "percona"]。注意，该值必须和备份计划的类型一致。
        :type DatabaseType: str
        :param _AccessType: 实例接入类型，支持的值包括：
"extranet" - 外网;
"cvm" - cvm自建实例;
"dcg" - 专线接入;
"vpncloud" - 云vpn接入;
"cdb" - 腾讯云数据库实例;
"ccn" - 云联网接入。
        :type AccessType: str
        :param _Ip: 实例 Ip。
        :type Ip: str
        :param _Port: 实例端口号。
        :type Port: int
        :param _UserName: 用户名。
        :type UserName: str
        :param _Password: 登录密码。
        :type Password: str
        :param _InstanceId: 云数据库实例ID，格式如：cdb-qcloudtest。
        :type InstanceId: str
        :param _CvmInstanceId: CVM 实例ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要填写该字段。
        :type CvmInstanceId: str
        :param _UniqDcgId: 专线网关ID，格式如：dcg-0rxtqqxb。
        :type UniqDcgId: str
        :param _UniqVpnGwId: VPN网关ID，格式如：vpngw-9ghexg7q。
        :type UniqVpnGwId: str
        :param _VpcId: 私有网络ID，格式如：vpc-92jblxto。
        :type VpcId: str
        :param _SubnetId: 子网ID，格式如：subnet-3paxmkdz。
        :type SubnetId: str
        :param _CcnId: 云联网ID，如：ccn-afp6kltc。
        :type CcnId: str
        :param _Region: 接入地域。
        :type Region: str
        :param _Supplier: 服务提供商，支持的值包括["aliyun", "aws", "others"]。
        :type Supplier: str
        :param _EngineVersion: 数据库版本，当实例为 RDS 或 AWS 实例时才有效，格式如：5.6或者5.7，默认为5.6。
        :type EngineVersion: str
        :param _DBKernel: mariadb三引擎版本。
        :type DBKernel: str
        """
        self._Role = None
        self._DatabaseType = None
        self._AccessType = None
        self._Ip = None
        self._Port = None
        self._UserName = None
        self._Password = None
        self._InstanceId = None
        self._CvmInstanceId = None
        self._UniqDcgId = None
        self._UniqVpnGwId = None
        self._VpcId = None
        self._SubnetId = None
        self._CcnId = None
        self._Region = None
        self._Supplier = None
        self._EngineVersion = None
        self._DBKernel = None

    @property
    def Role(self):
        r"""节点角色。取值：
"master" - 主节点;
"slave" - 从节点。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def DatabaseType(self):
        r"""数据库类型。目前支持的值["mysql", "mariadb", "percona"]。注意，该值必须和备份计划的类型一致。
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def AccessType(self):
        r"""实例接入类型，支持的值包括：
"extranet" - 外网;
"cvm" - cvm自建实例;
"dcg" - 专线接入;
"vpncloud" - 云vpn接入;
"cdb" - 腾讯云数据库实例;
"ccn" - 云联网接入。
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Ip(self):
        r"""实例 Ip。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""实例端口号。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        r"""用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""登录密码。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InstanceId(self):
        r"""云数据库实例ID，格式如：cdb-qcloudtest。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmInstanceId(self):
        r"""CVM 实例ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要填写该字段。
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        r"""专线网关ID，格式如：dcg-0rxtqqxb。
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def UniqVpnGwId(self):
        r"""VPN网关ID，格式如：vpngw-9ghexg7q。
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def VpcId(self):
        r"""私有网络ID，格式如：vpc-92jblxto。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID，格式如：subnet-3paxmkdz。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CcnId(self):
        r"""云联网ID，如：ccn-afp6kltc。
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def Region(self):
        r"""接入地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Supplier(self):
        r"""服务提供商，支持的值包括["aliyun", "aws", "others"]。
        :rtype: str
        """
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def EngineVersion(self):
        r"""数据库版本，当实例为 RDS 或 AWS 实例时才有效，格式如：5.6或者5.7，默认为5.6。
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def DBKernel(self):
        r"""mariadb三引擎版本。
        :rtype: str
        """
        return self._DBKernel

    @DBKernel.setter
    def DBKernel(self, DBKernel):
        self._DBKernel = DBKernel


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._DatabaseType = params.get("DatabaseType")
        self._AccessType = params.get("AccessType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._InstanceId = params.get("InstanceId")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CcnId = params.get("CcnId")
        self._Region = params.get("Region")
        self._Supplier = params.get("Supplier")
        self._EngineVersion = params.get("EngineVersion")
        self._DBKernel = params.get("DBKernel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfo(AbstractModel):
    r"""错误异常信息

    """

    def __init__(self):
        r"""
        :param _ErrorType: 错误类型。
        :type ErrorType: str
        :param _ErrorMsg: 错误信息。
        :type ErrorMsg: str
        """
        self._ErrorType = None
        self._ErrorMsg = None

    @property
    def ErrorType(self):
        r"""错误类型。
        :rtype: str
        """
        return self._ErrorType

    @ErrorType.setter
    def ErrorType(self, ErrorType):
        self._ErrorType = ErrorType

    @property
    def ErrorMsg(self):
        r"""错误信息。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._ErrorType = params.get("ErrorType")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FullBackupErrorMessage(AbstractModel):
    r"""全量备份错误信息

    """

    def __init__(self):
        r"""
        :param _Title: 错误标题。
        :type Title: str
        :param _Message: 错误详情。
        :type Message: str
        """
        self._Title = None
        self._Message = None

    @property
    def Title(self):
        r"""错误标题。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Message(self):
        r"""错误详情。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FullBackupProgress(AbstractModel):
    r"""全量备份进度

    """

    def __init__(self):
        r"""
        :param _SchemaProgress: 结构备份进度，取值范围为 0 - 100，单位：百分比。
        :type SchemaProgress: int
        :param _DataProgress: 数据备份进度，取值范围为 0 - 100，单位：百分比。
        :type DataProgress: int
        """
        self._SchemaProgress = None
        self._DataProgress = None

    @property
    def SchemaProgress(self):
        r"""结构备份进度，取值范围为 0 - 100，单位：百分比。
        :rtype: int
        """
        return self._SchemaProgress

    @SchemaProgress.setter
    def SchemaProgress(self, SchemaProgress):
        self._SchemaProgress = SchemaProgress

    @property
    def DataProgress(self):
        r"""数据备份进度，取值范围为 0 - 100，单位：百分比。
        :rtype: int
        """
        return self._DataProgress

    @DataProgress.setter
    def DataProgress(self, DataProgress):
        self._DataProgress = DataProgress


    def _deserialize(self, params):
        self._SchemaProgress = params.get("SchemaProgress")
        self._DataProgress = params.get("DataProgress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FullBackupSetDetail(AbstractModel):
    r"""全量备份集详情

    """

    def __init__(self):
        r"""
        :param _BackupSetId: <p>备份集 ID。</p>
        :type BackupSetId: str
        :param _SourceInfo: <p>源实例信息。</p>
        :type SourceInfo: str
        :param _Status: <p>备份集状态。可能的取值为："running" - 运行中;"finished" - 已完成;"failed" - 已失败;"stopped" - 已终止。</p>
        :type Status: str
        :param _StartTime: <p>创建时间。格式为 YYYY-MM-DD hh:mm:ss。</p>
        :type StartTime: str
        :param _EndTime: <p>结束时间。格式为 YYYY-MM-DD hh:mm:ss，备份集尚未结束时返回 0000-00-00 00:00:00。</p>
        :type EndTime: str
        :param _ExpireTime: <p>过期时间。格式为 YYYY-MM-DD hh:mm:ss。</p>
        :type ExpireTime: str
        :param _BackupSize: <p>备份集大小，单位为 Bytes。</p>
        :type BackupSize: int
        :param _BackupMethod: <p>备份方式。可能的取值为："logical" - 逻辑备份；"physical" - 物理备份。</p>
        :type BackupMethod: str
        :param _StorageType: <p>存储类型。目前仅支持 "DBSStorage"，即 DBS 内置存储。</p>
        :type StorageType: str
        :param _BackupPool: <p>备份池类型。目前仅支持 "DefaultPool"，即默认存储池。</p>
        :type BackupPool: str
        :param _RetentionType: <p>备份集存储类型。支持的取值范围为："standard" - 标准存储；"tiered" - 分级存储。</p>
        :type RetentionType: str
        :param _ResourceDetail: <p>备份集存储状态详情。</p>
        :type ResourceDetail: :class:`tencentcloud.dbs.v20211108.models.ResourceDetail`
        :param _SourceEndpoint: 备份源实例信息。
        :type SourceEndpoint: :class:`tencentcloud.dbs.v20211108.models.Endpoint`
        :param _BackupObject: 备份对象。
        :type BackupObject: :class:`tencentcloud.dbs.v20211108.models.BackupObject`
        :param _Progress: 备份进度。
        :type Progress: :class:`tencentcloud.dbs.v20211108.models.FullBackupProgress`
        :param _ErrorMessage: 备份错误信息。备份失败时有值。
        :type ErrorMessage: :class:`tencentcloud.dbs.v20211108.models.FullBackupErrorMessage`
        :param _BackupSetOption: 备份集加密信息。
        :type BackupSetOption: :class:`tencentcloud.dbs.v20211108.models.BackupSetOption`
        """
        self._BackupSetId = None
        self._SourceInfo = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._ExpireTime = None
        self._BackupSize = None
        self._BackupMethod = None
        self._StorageType = None
        self._BackupPool = None
        self._RetentionType = None
        self._ResourceDetail = None
        self._SourceEndpoint = None
        self._BackupObject = None
        self._Progress = None
        self._ErrorMessage = None
        self._BackupSetOption = None

    @property
    def BackupSetId(self):
        r"""<p>备份集 ID。</p>
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def SourceInfo(self):
        r"""<p>源实例信息。</p>
        :rtype: str
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo

    @property
    def Status(self):
        r"""<p>备份集状态。可能的取值为："running" - 运行中;"finished" - 已完成;"failed" - 已失败;"stopped" - 已终止。</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""<p>创建时间。格式为 YYYY-MM-DD hh:mm:ss。</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>结束时间。格式为 YYYY-MM-DD hh:mm:ss，备份集尚未结束时返回 0000-00-00 00:00:00。</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExpireTime(self):
        r"""<p>过期时间。格式为 YYYY-MM-DD hh:mm:ss。</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def BackupSize(self):
        r"""<p>备份集大小，单位为 Bytes。</p>
        :rtype: int
        """
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def BackupMethod(self):
        r"""<p>备份方式。可能的取值为："logical" - 逻辑备份；"physical" - 物理备份。</p>
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def StorageType(self):
        r"""<p>存储类型。目前仅支持 "DBSStorage"，即 DBS 内置存储。</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def BackupPool(self):
        r"""<p>备份池类型。目前仅支持 "DefaultPool"，即默认存储池。</p>
        :rtype: str
        """
        return self._BackupPool

    @BackupPool.setter
    def BackupPool(self, BackupPool):
        self._BackupPool = BackupPool

    @property
    def RetentionType(self):
        r"""<p>备份集存储类型。支持的取值范围为："standard" - 标准存储；"tiered" - 分级存储。</p>
        :rtype: str
        """
        return self._RetentionType

    @RetentionType.setter
    def RetentionType(self, RetentionType):
        self._RetentionType = RetentionType

    @property
    def ResourceDetail(self):
        r"""<p>备份集存储状态详情。</p>
        :rtype: :class:`tencentcloud.dbs.v20211108.models.ResourceDetail`
        """
        return self._ResourceDetail

    @ResourceDetail.setter
    def ResourceDetail(self, ResourceDetail):
        self._ResourceDetail = ResourceDetail

    @property
    def SourceEndpoint(self):
        r"""备份源实例信息。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.Endpoint`
        """
        return self._SourceEndpoint

    @SourceEndpoint.setter
    def SourceEndpoint(self, SourceEndpoint):
        self._SourceEndpoint = SourceEndpoint

    @property
    def BackupObject(self):
        r"""备份对象。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupObject`
        """
        return self._BackupObject

    @BackupObject.setter
    def BackupObject(self, BackupObject):
        self._BackupObject = BackupObject

    @property
    def Progress(self):
        r"""备份进度。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.FullBackupProgress`
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def ErrorMessage(self):
        r"""备份错误信息。备份失败时有值。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.FullBackupErrorMessage`
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def BackupSetOption(self):
        r"""备份集加密信息。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupSetOption`
        """
        return self._BackupSetOption

    @BackupSetOption.setter
    def BackupSetOption(self, BackupSetOption):
        self._BackupSetOption = BackupSetOption


    def _deserialize(self, params):
        self._BackupSetId = params.get("BackupSetId")
        self._SourceInfo = params.get("SourceInfo")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExpireTime = params.get("ExpireTime")
        self._BackupSize = params.get("BackupSize")
        self._BackupMethod = params.get("BackupMethod")
        self._StorageType = params.get("StorageType")
        self._BackupPool = params.get("BackupPool")
        self._RetentionType = params.get("RetentionType")
        if params.get("ResourceDetail") is not None:
            self._ResourceDetail = ResourceDetail()
            self._ResourceDetail._deserialize(params.get("ResourceDetail"))
        if params.get("SourceEndpoint") is not None:
            self._SourceEndpoint = Endpoint()
            self._SourceEndpoint._deserialize(params.get("SourceEndpoint"))
        if params.get("BackupObject") is not None:
            self._BackupObject = BackupObject()
            self._BackupObject._deserialize(params.get("BackupObject"))
        if params.get("Progress") is not None:
            self._Progress = FullBackupProgress()
            self._Progress._deserialize(params.get("Progress"))
        if params.get("ErrorMessage") is not None:
            self._ErrorMessage = FullBackupErrorMessage()
            self._ErrorMessage._deserialize(params.get("ErrorMessage"))
        if params.get("BackupSetOption") is not None:
            self._BackupSetOption = BackupSetOption()
            self._BackupSetOption._deserialize(params.get("BackupSetOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementBackup(AbstractModel):
    r"""增量备份集信息

    """

    def __init__(self):
        r"""
        :param _BackupSetId: 备份集 ID。
        :type BackupSetId: str
        :param _SourceInfo: 源实例信息。
        :type SourceInfo: str
        :param _Status: 备份集状态。可能的取值为：
"running" - 运行中;
"finished" - 已完成;
"failed" - 已失败;
"stopped" - 已终止。
        :type Status: str
        :param _StartTime: 开始时间。格式为 YYYY-MM-DD hh:mm:ss。
        :type StartTime: str
        :param _EndTime: 结束时间。格式为 YYYY-MM-DD hh:mm:ss，备份集尚未结束时返回 0000-00-00 00:00:00。
        :type EndTime: str
        :param _ExpireTime: 过期时间。格式为 YYYY-MM-DD hh:mm:ss，备份集尚未生成过期时间时返回空字符串。
        :type ExpireTime: str
        :param _FileCount: 备份集文件个数。
        :type FileCount: int
        :param _BackupMethod: 备份方式。可能的取值为：
"logical" - 逻辑备份；
"physical" - 物理备份。
        :type BackupMethod: str
        :param _StorageType: 存储类型。目前仅支持 "DBSStorage"，即 DBS 内置存储。
        :type StorageType: str
        :param _BackupPool: 备份池类型。目前仅支持 "DefaultPool"，即默认存储池。
        :type BackupPool: str
        :param _RetentionType: 备份集存储类型。支持的取值范围为："standard" - 标准存储；"tiered" - 分级存储。
        :type RetentionType: str
        :param _ResourceDetail: 备份集存储状态详情。
        :type ResourceDetail: :class:`tencentcloud.dbs.v20211108.models.ResourceItemDetail`
        """
        self._BackupSetId = None
        self._SourceInfo = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._ExpireTime = None
        self._FileCount = None
        self._BackupMethod = None
        self._StorageType = None
        self._BackupPool = None
        self._RetentionType = None
        self._ResourceDetail = None

    @property
    def BackupSetId(self):
        r"""备份集 ID。
        :rtype: str
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def SourceInfo(self):
        r"""源实例信息。
        :rtype: str
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo

    @property
    def Status(self):
        r"""备份集状态。可能的取值为：
"running" - 运行中;
"finished" - 已完成;
"failed" - 已失败;
"stopped" - 已终止。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""开始时间。格式为 YYYY-MM-DD hh:mm:ss。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。格式为 YYYY-MM-DD hh:mm:ss，备份集尚未结束时返回 0000-00-00 00:00:00。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExpireTime(self):
        r"""过期时间。格式为 YYYY-MM-DD hh:mm:ss，备份集尚未生成过期时间时返回空字符串。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileCount(self):
        r"""备份集文件个数。
        :rtype: int
        """
        return self._FileCount

    @FileCount.setter
    def FileCount(self, FileCount):
        self._FileCount = FileCount

    @property
    def BackupMethod(self):
        r"""备份方式。可能的取值为：
"logical" - 逻辑备份；
"physical" - 物理备份。
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def StorageType(self):
        r"""存储类型。目前仅支持 "DBSStorage"，即 DBS 内置存储。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def BackupPool(self):
        r"""备份池类型。目前仅支持 "DefaultPool"，即默认存储池。
        :rtype: str
        """
        return self._BackupPool

    @BackupPool.setter
    def BackupPool(self, BackupPool):
        self._BackupPool = BackupPool

    @property
    def RetentionType(self):
        r"""备份集存储类型。支持的取值范围为："standard" - 标准存储；"tiered" - 分级存储。
        :rtype: str
        """
        return self._RetentionType

    @RetentionType.setter
    def RetentionType(self, RetentionType):
        self._RetentionType = RetentionType

    @property
    def ResourceDetail(self):
        r"""备份集存储状态详情。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.ResourceItemDetail`
        """
        return self._ResourceDetail

    @ResourceDetail.setter
    def ResourceDetail(self, ResourceDetail):
        self._ResourceDetail = ResourceDetail


    def _deserialize(self, params):
        self._BackupSetId = params.get("BackupSetId")
        self._SourceInfo = params.get("SourceInfo")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExpireTime = params.get("ExpireTime")
        self._FileCount = params.get("FileCount")
        self._BackupMethod = params.get("BackupMethod")
        self._StorageType = params.get("StorageType")
        self._BackupPool = params.get("BackupPool")
        self._RetentionType = params.get("RetentionType")
        if params.get("ResourceDetail") is not None:
            self._ResourceDetail = ResourceItemDetail()
            self._ResourceDetail._deserialize(params.get("ResourceDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupPlanSourceInfoRequest(AbstractModel):
    r"""ModifyBackupPlanSourceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。
        :type BackupPlanId: str
        :param _SourceEndPoint: 新的备份源实例信息。
        :type SourceEndPoint: :class:`tencentcloud.dbs.v20211108.models.BackupEndpoint`
        :param _BackupPlanName: 新的备份名称。
        :type BackupPlanName: str
        :param _BackupObject: 新的备份对象信息。
        :type BackupObject: :class:`tencentcloud.dbs.v20211108.models.BackupObject`
        :param _BackupNow: 是否立即启动新的备份任务。支持的取值为：1 - 立即启动；0 - 按备份策略配置的时间启动。
        :type BackupNow: int
        """
        self._BackupPlanId = None
        self._SourceEndPoint = None
        self._BackupPlanName = None
        self._BackupObject = None
        self._BackupNow = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId

    @property
    def SourceEndPoint(self):
        r"""新的备份源实例信息。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupEndpoint`
        """
        return self._SourceEndPoint

    @SourceEndPoint.setter
    def SourceEndPoint(self, SourceEndPoint):
        self._SourceEndPoint = SourceEndPoint

    @property
    def BackupPlanName(self):
        r"""新的备份名称。
        :rtype: str
        """
        return self._BackupPlanName

    @BackupPlanName.setter
    def BackupPlanName(self, BackupPlanName):
        self._BackupPlanName = BackupPlanName

    @property
    def BackupObject(self):
        r"""新的备份对象信息。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.BackupObject`
        """
        return self._BackupObject

    @BackupObject.setter
    def BackupObject(self, BackupObject):
        self._BackupObject = BackupObject

    @property
    def BackupNow(self):
        r"""是否立即启动新的备份任务。支持的取值为：1 - 立即启动；0 - 按备份策略配置的时间启动。
        :rtype: int
        """
        return self._BackupNow

    @BackupNow.setter
    def BackupNow(self, BackupNow):
        self._BackupNow = BackupNow


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        if params.get("SourceEndPoint") is not None:
            self._SourceEndPoint = BackupEndpoint()
            self._SourceEndPoint._deserialize(params.get("SourceEndPoint"))
        self._BackupPlanName = params.get("BackupPlanName")
        if params.get("BackupObject") is not None:
            self._BackupObject = BackupObject()
            self._BackupObject._deserialize(params.get("BackupObject"))
        self._BackupNow = params.get("BackupNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupPlanSourceInfoResponse(AbstractModel):
    r"""ModifyBackupPlanSourceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResourceDetail(AbstractModel):
    r"""备份集状态详情

    """

    def __init__(self):
        r"""
        :param _TieredType: <p>当前存储状态。可能的取值为："standard" - 标准存储；"lowFrequency" - 低频存储；"archive" - 归档存储；"deepArchive" - 深度归档存储；</p>
        :type TieredType: str
        :param _StayTime: <p>存储时长。备份集已保留的时长，单位为小时。</p>
        :type StayTime: float
        """
        self._TieredType = None
        self._StayTime = None

    @property
    def TieredType(self):
        r"""<p>当前存储状态。可能的取值为："standard" - 标准存储；"lowFrequency" - 低频存储；"archive" - 归档存储；"deepArchive" - 深度归档存储；</p>
        :rtype: str
        """
        return self._TieredType

    @TieredType.setter
    def TieredType(self, TieredType):
        self._TieredType = TieredType

    @property
    def StayTime(self):
        r"""<p>存储时长。备份集已保留的时长，单位为小时。</p>
        :rtype: float
        """
        return self._StayTime

    @StayTime.setter
    def StayTime(self, StayTime):
        self._StayTime = StayTime


    def _deserialize(self, params):
        self._TieredType = params.get("TieredType")
        self._StayTime = params.get("StayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceItemDetail(AbstractModel):
    r"""备份集状态详情

    """

    def __init__(self):
        r"""
        :param _TieredType: <p>当前存储状态。可能的取值为："standard" - 标准存储；"lowFrequency" - 低频存储；"archive" - 归档存储；"deepArchive" - 深度归档存储；</p>
        :type TieredType: str
        :param _StayTime: <p>存储时长。备份集已保留的时长，单位为小时。</p>
        :type StayTime: float
        """
        self._TieredType = None
        self._StayTime = None

    @property
    def TieredType(self):
        r"""<p>当前存储状态。可能的取值为："standard" - 标准存储；"lowFrequency" - 低频存储；"archive" - 归档存储；"deepArchive" - 深度归档存储；</p>
        :rtype: str
        """
        return self._TieredType

    @TieredType.setter
    def TieredType(self, TieredType):
        self._TieredType = TieredType

    @property
    def StayTime(self):
        r"""<p>存储时长。备份集已保留的时长，单位为小时。</p>
        :rtype: float
        """
        return self._StayTime

    @StayTime.setter
    def StayTime(self, StayTime):
        self._StayTime = StayTime


    def _deserialize(self, params):
        self._TieredType = params.get("TieredType")
        self._StayTime = params.get("StayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreRange(AbstractModel):
    r"""可恢复时间范围

    """

    def __init__(self):
        r"""
        :param _StartTime: 可恢复起始时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，无可恢复时间范围时为空字符串。
        :type StartTime: str
        :param _EndTime: 可恢复结束时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，无可恢复时间范围时为空字符串。
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""可恢复起始时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，无可恢复时间范围时为空字符串。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""可恢复结束时间。格式为 YYYY-MM-DD HH:mm:ss，如 2024-01-01 00:00:00，无可恢复时间范围时为空字符串。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeBackupPlanRequest(AbstractModel):
    r"""ResumeBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。可通过 DescribeBackupPlans 接口获取。
        :type BackupPlanId: str
        :param _BackupNow: 恢复后是否立即发起一次备份。取值：
- 0：不立即备份，默认值
- 1：立即备份
        :type BackupNow: int
        """
        self._BackupPlanId = None
        self._BackupNow = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。可通过 DescribeBackupPlans 接口获取。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId

    @property
    def BackupNow(self):
        r"""恢复后是否立即发起一次备份。取值：
- 0：不立即备份，默认值
- 1：立即备份
        :rtype: int
        """
        return self._BackupNow

    @BackupNow.setter
    def BackupNow(self, BackupNow):
        self._BackupNow = BackupNow


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        self._BackupNow = params.get("BackupNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeBackupPlanResponse(AbstractModel):
    r"""ResumeBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartBackupCheckJobRequest(AbstractModel):
    r"""StartBackupCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。
        :type BackupPlanId: str
        """
        self._BackupPlanId = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupCheckJobResponse(AbstractModel):
    r"""StartBackupCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartBackupPlanRequest(AbstractModel):
    r"""StartBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。
        :type BackupPlanId: str
        """
        self._BackupPlanId = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBackupPlanResponse(AbstractModel):
    r"""StartBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopBackupPlanRequest(AbstractModel):
    r"""StopBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupPlanId: 备份计划 ID。可通过 DescribeBackupPlans 接口获取。
        :type BackupPlanId: str
        """
        self._BackupPlanId = None

    @property
    def BackupPlanId(self):
        r"""备份计划 ID。可通过 DescribeBackupPlans 接口获取。
        :rtype: str
        """
        return self._BackupPlanId

    @BackupPlanId.setter
    def BackupPlanId(self, BackupPlanId):
        self._BackupPlanId = BackupPlanId


    def _deserialize(self, params):
        self._BackupPlanId = params.get("BackupPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopBackupPlanResponse(AbstractModel):
    r"""StopBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StorageStrategy(AbstractModel):
    r"""备份存储策略。

    """

    def __init__(self):
        r"""
        :param _StorageType: 存储类型。目前仅支持 "system" - DBS 内置存储。默认值为 "system"。
        :type StorageType: str
        :param _Encryption: 加密方式。可能的取值为：
"UnEncrypted" - 非加密存储;
"SSE-COS" - 内置加密存储;
当该参数用作入参时，默认值为 "UnEncrypted"。
        :type Encryption: str
        :param _BackupRetentionPeriod: 日志保留时间，单位为天。取值范围为[7, 3650]，默认值为 30。
        :type BackupRetentionPeriod: int
        """
        self._StorageType = None
        self._Encryption = None
        self._BackupRetentionPeriod = None

    @property
    def StorageType(self):
        r"""存储类型。目前仅支持 "system" - DBS 内置存储。默认值为 "system"。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Encryption(self):
        r"""加密方式。可能的取值为：
"UnEncrypted" - 非加密存储;
"SSE-COS" - 内置加密存储;
当该参数用作入参时，默认值为 "UnEncrypted"。
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def BackupRetentionPeriod(self):
        r"""日志保留时间，单位为天。取值范围为[7, 3650]，默认值为 30。
        :rtype: int
        """
        return self._BackupRetentionPeriod

    @BackupRetentionPeriod.setter
    def BackupRetentionPeriod(self, BackupRetentionPeriod):
        self._BackupRetentionPeriod = BackupRetentionPeriod


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._Encryption = params.get("Encryption")
        self._BackupRetentionPeriod = params.get("BackupRetentionPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageStrategyItem(AbstractModel):
    r"""备份存储策略。

    """

    def __init__(self):
        r"""
        :param _StorageType: 存储类型。目前仅支持 "system" - DBS 内置存储。默认值为 "system"。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param _Encryption: 加密方式。可能的取值为：
"UnEncrypted" - 非加密存储;
"SSE-COS" - 内置加密存储;
当该参数用作入参时，默认值为 "UnEncrypted"。
注意：此字段可能返回 null，表示取不到有效值。
        :type Encryption: str
        :param _BackupRetentionPeriod: 日志保留时间，单位为天。取值范围为[7, 3650]，默认值为 30。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupRetentionPeriod: int
        :param _FullStorageStrategy: 全量备份存储策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type FullStorageStrategy: :class:`tencentcloud.dbs.v20211108.models.StorageStrategySingle`
        :param _IncStorageStrategy: 增量备份存储策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type IncStorageStrategy: :class:`tencentcloud.dbs.v20211108.models.StorageStrategySingle`
        """
        self._StorageType = None
        self._Encryption = None
        self._BackupRetentionPeriod = None
        self._FullStorageStrategy = None
        self._IncStorageStrategy = None

    @property
    def StorageType(self):
        r"""存储类型。目前仅支持 "system" - DBS 内置存储。默认值为 "system"。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Encryption(self):
        r"""加密方式。可能的取值为：
"UnEncrypted" - 非加密存储;
"SSE-COS" - 内置加密存储;
当该参数用作入参时，默认值为 "UnEncrypted"。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def BackupRetentionPeriod(self):
        r"""日志保留时间，单位为天。取值范围为[7, 3650]，默认值为 30。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BackupRetentionPeriod

    @BackupRetentionPeriod.setter
    def BackupRetentionPeriod(self, BackupRetentionPeriod):
        self._BackupRetentionPeriod = BackupRetentionPeriod

    @property
    def FullStorageStrategy(self):
        r"""全量备份存储策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.StorageStrategySingle`
        """
        return self._FullStorageStrategy

    @FullStorageStrategy.setter
    def FullStorageStrategy(self, FullStorageStrategy):
        self._FullStorageStrategy = FullStorageStrategy

    @property
    def IncStorageStrategy(self):
        r"""增量备份存储策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.StorageStrategySingle`
        """
        return self._IncStorageStrategy

    @IncStorageStrategy.setter
    def IncStorageStrategy(self, IncStorageStrategy):
        self._IncStorageStrategy = IncStorageStrategy


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._Encryption = params.get("Encryption")
        self._BackupRetentionPeriod = params.get("BackupRetentionPeriod")
        if params.get("FullStorageStrategy") is not None:
            self._FullStorageStrategy = StorageStrategySingle()
            self._FullStorageStrategy._deserialize(params.get("FullStorageStrategy"))
        if params.get("IncStorageStrategy") is not None:
            self._IncStorageStrategy = StorageStrategySingle()
            self._IncStorageStrategy._deserialize(params.get("IncStorageStrategy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageStrategySingle(AbstractModel):
    r"""存储策略

    """

    def __init__(self):
        r"""
        :param _RetentionType: 存储策略类型。取值：
- standard：标准存储
- tiered：分级存储
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionType: str
        :param _RetentionPeriod: 备份保留天数，取值范围为 7 - 3650。
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionPeriod: int
        :param _TieredStrategy: 分级存储策略。RetentionType 为 tiered 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TieredStrategy: :class:`tencentcloud.dbs.v20211108.models.StorageTieredStrategy`
        """
        self._RetentionType = None
        self._RetentionPeriod = None
        self._TieredStrategy = None

    @property
    def RetentionType(self):
        r"""存储策略类型。取值：
- standard：标准存储
- tiered：分级存储
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RetentionType

    @RetentionType.setter
    def RetentionType(self, RetentionType):
        self._RetentionType = RetentionType

    @property
    def RetentionPeriod(self):
        r"""备份保留天数，取值范围为 7 - 3650。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetentionPeriod

    @RetentionPeriod.setter
    def RetentionPeriod(self, RetentionPeriod):
        self._RetentionPeriod = RetentionPeriod

    @property
    def TieredStrategy(self):
        r"""分级存储策略。RetentionType 为 tiered 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbs.v20211108.models.StorageTieredStrategy`
        """
        return self._TieredStrategy

    @TieredStrategy.setter
    def TieredStrategy(self, TieredStrategy):
        self._TieredStrategy = TieredStrategy


    def _deserialize(self, params):
        self._RetentionType = params.get("RetentionType")
        self._RetentionPeriod = params.get("RetentionPeriod")
        if params.get("TieredStrategy") is not None:
            self._TieredStrategy = StorageTieredStrategy()
            self._TieredStrategy._deserialize(params.get("TieredStrategy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageTieredStrategy(AbstractModel):
    r"""分级存储策略

    """

    def __init__(self):
        r"""
        :param _DayToLowFrequency: 低频存储
注意：此字段可能返回 null，表示取不到有效值。
        :type DayToLowFrequency: int
        :param _DayToArchive: 归档存储
注意：此字段可能返回 null，表示取不到有效值。
        :type DayToArchive: int
        :param _DayToDeepArchive: 深度归档存储
注意：此字段可能返回 null，表示取不到有效值。
        :type DayToDeepArchive: int
        """
        self._DayToLowFrequency = None
        self._DayToArchive = None
        self._DayToDeepArchive = None

    @property
    def DayToLowFrequency(self):
        r"""低频存储
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DayToLowFrequency

    @DayToLowFrequency.setter
    def DayToLowFrequency(self, DayToLowFrequency):
        self._DayToLowFrequency = DayToLowFrequency

    @property
    def DayToArchive(self):
        r"""归档存储
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DayToArchive

    @DayToArchive.setter
    def DayToArchive(self, DayToArchive):
        self._DayToArchive = DayToArchive

    @property
    def DayToDeepArchive(self):
        r"""深度归档存储
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DayToDeepArchive

    @DayToDeepArchive.setter
    def DayToDeepArchive(self, DayToDeepArchive):
        self._DayToDeepArchive = DayToDeepArchive


    def _deserialize(self, params):
        self._DayToLowFrequency = params.get("DayToLowFrequency")
        self._DayToArchive = params.get("DayToArchive")
        self._DayToDeepArchive = params.get("DayToDeepArchive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键。
        :type TagKey: str
        :param _TagValue: 标签值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值。
        :rtype: str
        """
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
        


class TagFilter(AbstractModel):
    r"""标签过滤条件

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键。
        :type TagKey: str
        :param _TagValue: 标签值。
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值。
        :rtype: list of str
        """
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
        


class TagInfo(AbstractModel):
    r"""标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键。
        :type TagKey: str
        :param _TagValue: 标签值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值。
        :rtype: str
        """
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
        


class TestItem(AbstractModel):
    r"""检测步骤详情

    """

    def __init__(self):
        r"""
        :param _TestName: <p>检测步骤名称</p>
        :type TestName: str
        :param _Code: <p>错误码</p>
        :type Code: int
        :param _Message: <p>错误信息</p>
        :type Message: str
        """
        self._TestName = None
        self._Code = None
        self._Message = None

    @property
    def TestName(self):
        r"""<p>检测步骤名称</p>
        :rtype: str
        """
        return self._TestName

    @TestName.setter
    def TestName(self, TestName):
        self._TestName = TestName

    @property
    def Code(self):
        r"""<p>错误码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._TestName = params.get("TestName")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        