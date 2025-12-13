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
        