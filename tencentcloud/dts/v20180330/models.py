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


class ActivateSubscribeRequest(AbstractModel):
    """ActivateSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID。
        :type SubscribeId: str
        :param _InstanceId: 数据库实例ID
        :type InstanceId: str
        :param _SubscribeObjectType: 数据订阅类型0-全实例订阅，1数据订阅，2结构订阅，3数据订阅与结构订阅
        :type SubscribeObjectType: int
        :param _Objects: 订阅对象
        :type Objects: :class:`tencentcloud.dts.v20180330.models.SubscribeObject`
        :param _UniqSubnetId: 数据订阅服务所在子网。默认为数据库实例所在的子网内。
        :type UniqSubnetId: str
        :param _Vport: 订阅服务端口；默认为7507
        :type Vport: int
        """
        self._SubscribeId = None
        self._InstanceId = None
        self._SubscribeObjectType = None
        self._Objects = None
        self._UniqSubnetId = None
        self._Vport = None

    @property
    def SubscribeId(self):
        """订阅实例ID。
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def InstanceId(self):
        """数据库实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SubscribeObjectType(self):
        """数据订阅类型0-全实例订阅，1数据订阅，2结构订阅，3数据订阅与结构订阅
        :rtype: int
        """
        return self._SubscribeObjectType

    @SubscribeObjectType.setter
    def SubscribeObjectType(self, SubscribeObjectType):
        self._SubscribeObjectType = SubscribeObjectType

    @property
    def Objects(self):
        """订阅对象
        :rtype: :class:`tencentcloud.dts.v20180330.models.SubscribeObject`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def UniqSubnetId(self):
        """数据订阅服务所在子网。默认为数据库实例所在的子网内。
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Vport(self):
        """订阅服务端口；默认为7507
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._InstanceId = params.get("InstanceId")
        self._SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self._Objects = SubscribeObject()
            self._Objects._deserialize(params.get("Objects"))
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateSubscribeResponse(AbstractModel):
    """ActivateSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 配置数据订阅任务ID。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """配置数据订阅任务ID。
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

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
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        :param _CompleteMode: 完成任务的方式,仅支持旧版MySQL迁移任务。waitForSync-等待主从差距为0才停止,immediately-立即完成，不会等待主从差距一致。默认为waitForSync
        :type CompleteMode: str
        """
        self._JobId = None
        self._CompleteMode = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompleteMode(self):
        """完成任务的方式,仅支持旧版MySQL迁移任务。waitForSync-等待主从差距为0才停止,immediately-立即完成，不会等待主从差距一致。默认为waitForSync
        :rtype: str
        """
        return self._CompleteMode

    @CompleteMode.setter
    def CompleteMode(self, CompleteMode):
        self._CompleteMode = CompleteMode


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompleteMode = params.get("CompleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob返回参数结构体

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


class ConsistencyParams(AbstractModel):
    """抽样检验时的抽样参数

    """

    def __init__(self):
        r"""
        :param _SelectRowsPerTable: 数据内容检测参数。表中选出用来数据对比的行，占表的总行数的百分比。取值范围是整数[1-100]
        :type SelectRowsPerTable: int
        :param _TablesSelectAll: 数据内容检测参数。迁移库表中，要进行数据内容检测的表，占所有表的百分比。取值范围是整数[1-100]
        :type TablesSelectAll: int
        :param _TablesSelectCount: 数据数量检测，检测表行数是否一致。迁移库表中，要进行数据数量检测的表，占所有表的百分比。取值范围是整数[1-100]
        :type TablesSelectCount: int
        """
        self._SelectRowsPerTable = None
        self._TablesSelectAll = None
        self._TablesSelectCount = None

    @property
    def SelectRowsPerTable(self):
        """数据内容检测参数。表中选出用来数据对比的行，占表的总行数的百分比。取值范围是整数[1-100]
        :rtype: int
        """
        return self._SelectRowsPerTable

    @SelectRowsPerTable.setter
    def SelectRowsPerTable(self, SelectRowsPerTable):
        self._SelectRowsPerTable = SelectRowsPerTable

    @property
    def TablesSelectAll(self):
        """数据内容检测参数。迁移库表中，要进行数据内容检测的表，占所有表的百分比。取值范围是整数[1-100]
        :rtype: int
        """
        return self._TablesSelectAll

    @TablesSelectAll.setter
    def TablesSelectAll(self, TablesSelectAll):
        self._TablesSelectAll = TablesSelectAll

    @property
    def TablesSelectCount(self):
        """数据数量检测，检测表行数是否一致。迁移库表中，要进行数据数量检测的表，占所有表的百分比。取值范围是整数[1-100]
        :rtype: int
        """
        return self._TablesSelectCount

    @TablesSelectCount.setter
    def TablesSelectCount(self, TablesSelectCount):
        self._TablesSelectCount = TablesSelectCount


    def _deserialize(self, params):
        self._SelectRowsPerTable = params.get("SelectRowsPerTable")
        self._TablesSelectAll = params.get("TablesSelectAll")
        self._TablesSelectCount = params.get("TablesSelectCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob返回参数结构体

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


class CreateMigrateJobRequest(AbstractModel):
    """CreateMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobName: 数据迁移任务名称
        :type JobName: str
        :param _MigrateOption: 迁移任务配置选项
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param _SrcDatabaseType: 源实例数据库类型，目前支持：mysql，redis，mongodb，postgresql，mariadb，percona，sqlserver 不同地域数据库类型的具体支持情况，请参考控制台创建迁移页面。
        :type SrcDatabaseType: str
        :param _SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例),cdb(腾讯云数据库实例),ccn(云联网实例)
        :type SrcAccessType: str
        :param _SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param _DstDatabaseType: 目标实例数据库类型，目前支持：mysql，redis，mongodb，postgresql，mariadb，percona，sqlserver，cynosdbmysql。不同地域数据库类型的具体支持情况，请参考控制台创建迁移页面。
        :type DstDatabaseType: str
        :param _DstAccessType: 目标实例接入类型，目前支持：cdb（腾讯云数据库实例）
        :type DstAccessType: str
        :param _DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param _DatabaseInfo: 需要迁移的源数据库表信息，用json格式的字符串描述。当MigrateOption.MigrateObject配置为2（指定库表迁移）时必填。
对于database-table两级结构的数据库：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
对于database-schema-table三级结构：
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]
        :type DatabaseInfo: str
        :param _Tags: 迁移实例的tag
        :type Tags: list of TagItem
        :param _SrcNodeType: 源实例类型: ""或者"simple":主从节点，"cluster": 集群节点
        :type SrcNodeType: str
        :param _SrcInfoMulti: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfoMulti: list of SrcInfo
        """
        self._JobName = None
        self._MigrateOption = None
        self._SrcDatabaseType = None
        self._SrcAccessType = None
        self._SrcInfo = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._DstInfo = None
        self._DatabaseInfo = None
        self._Tags = None
        self._SrcNodeType = None
        self._SrcInfoMulti = None

    @property
    def JobName(self):
        """数据迁移任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def MigrateOption(self):
        """迁移任务配置选项
        :rtype: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        """
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcDatabaseType(self):
        """源实例数据库类型，目前支持：mysql，redis，mongodb，postgresql，mariadb，percona，sqlserver 不同地域数据库类型的具体支持情况，请参考控制台创建迁移页面。
        :rtype: str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        """源实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例),cdb(腾讯云数据库实例),ccn(云联网实例)
        :rtype: str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        """源实例信息，具体内容跟迁移任务类型相关
        :rtype: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstDatabaseType(self):
        """目标实例数据库类型，目前支持：mysql，redis，mongodb，postgresql，mariadb，percona，sqlserver，cynosdbmysql。不同地域数据库类型的具体支持情况，请参考控制台创建迁移页面。
        :rtype: str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        """目标实例接入类型，目前支持：cdb（腾讯云数据库实例）
        :rtype: str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        """目标实例信息
        :rtype: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DatabaseInfo(self):
        """需要迁移的源数据库表信息，用json格式的字符串描述。当MigrateOption.MigrateObject配置为2（指定库表迁移）时必填。
对于database-table两级结构的数据库：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
对于database-schema-table三级结构：
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]
        :rtype: str
        """
        return self._DatabaseInfo

    @DatabaseInfo.setter
    def DatabaseInfo(self, DatabaseInfo):
        self._DatabaseInfo = DatabaseInfo

    @property
    def Tags(self):
        """迁移实例的tag
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SrcNodeType(self):
        """源实例类型: ""或者"simple":主从节点，"cluster": 集群节点
        :rtype: str
        """
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def SrcInfoMulti(self):
        """源实例信息，具体内容跟迁移任务类型相关
        :rtype: list of SrcInfo
        """
        return self._SrcInfoMulti

    @SrcInfoMulti.setter
    def SrcInfoMulti(self, SrcInfoMulti):
        self._SrcInfoMulti = SrcInfoMulti


    def _deserialize(self, params):
        self._JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._DatabaseInfo = params.get("DatabaseInfo")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SrcNodeType = params.get("SrcNodeType")
        if params.get("SrcInfoMulti") is not None:
            self._SrcInfoMulti = []
            for item in params.get("SrcInfoMulti"):
                obj = SrcInfo()
                obj._deserialize(item)
                self._SrcInfoMulti.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateJobResponse(AbstractModel):
    """CreateMigrateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 订阅的数据库类型，目前支持的有 mysql
        :type Product: str
        :param _PayType: 实例付费类型，1小时计费，0包年包月
        :type PayType: int
        :param _Duration: 购买时长。PayType为0时必填。单位为月，最大支持120
        :type Duration: int
        :param _Count: 购买数量,默认为1，最大为10
        :type Count: int
        :param _AutoRenew: 是否自动续费，0表示不自动续费，1表示自动续费，默认为0。小时计费实例设置该标识无效。
        :type AutoRenew: int
        :param _Tags: 实例资源标签
        :type Tags: list of TagItem
        :param _Name: 用户自定义实例名
        :type Name: str
        """
        self._Product = None
        self._PayType = None
        self._Duration = None
        self._Count = None
        self._AutoRenew = None
        self._Tags = None
        self._Name = None

    @property
    def Product(self):
        """订阅的数据库类型，目前支持的有 mysql
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def PayType(self):
        """实例付费类型，1小时计费，0包年包月
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Duration(self):
        """购买时长。PayType为0时必填。单位为月，最大支持120
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Count(self):
        """购买数量,默认为1，最大为10
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AutoRenew(self):
        """是否自动续费，0表示不自动续费，1表示自动续费，默认为0。小时计费实例设置该标识无效。
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Tags(self):
        """实例资源标签
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Name(self):
        """用户自定义实例名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._PayType = params.get("PayType")
        self._Duration = params.get("Duration")
        self._Count = params.get("Count")
        self._AutoRenew = params.get("AutoRenew")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeIds: 数据订阅实例的ID数组
        :type SubscribeIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscribeIds = None
        self._RequestId = None

    @property
    def SubscribeIds(self):
        """数据订阅实例的ID数组
        :rtype: list of str
        """
        return self._SubscribeIds

    @SubscribeIds.setter
    def SubscribeIds(self, SubscribeIds):
        self._SubscribeIds = SubscribeIds

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
        self._SubscribeIds = params.get("SubscribeIds")
        self._RequestId = params.get("RequestId")


class DeleteMigrateJobRequest(AbstractModel):
    """DeleteMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMigrateJobResponse(AbstractModel):
    """DeleteMigrateJob返回参数结构体

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


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 任务 ID
        :type AsyncRequestId: str
        """
        self._AsyncRequestId = None

    @property
    def AsyncRequestId(self):
        """任务 ID
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Info: 任务执行结果信息
        :type Info: str
        :param _Status: 任务执行状态，可能的值有：success，failed，running
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Info = None
        self._Status = None
        self._RequestId = None

    @property
    def Info(self):
        """任务执行结果信息
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Status(self):
        """任务执行状态，可能的值有：success，failed，running
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
        self._Info = params.get("Info")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeMigrateCheckJobRequest(AbstractModel):
    """DescribeMigrateCheckJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateCheckJobResponse(AbstractModel):
    """DescribeMigrateCheckJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 校验任务状态：unavailable(当前不可用), starting(开始中)，running(校验中)，finished(校验完成)
        :type Status: str
        :param _ErrorCode: 任务的错误码
        :type ErrorCode: int
        :param _ErrorMessage: 任务的错误信息
        :type ErrorMessage: str
        :param _Progress: Check任务总进度,如："30"表示30%
        :type Progress: str
        :param _CheckFlag: 校验是否通过,0-未通过，1-校验通过, 3-未校验
        :type CheckFlag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._Progress = None
        self._CheckFlag = None
        self._RequestId = None

    @property
    def Status(self):
        """校验任务状态：unavailable(当前不可用), starting(开始中)，running(校验中)，finished(校验完成)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        """任务的错误码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        """任务的错误信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def Progress(self):
        """Check任务总进度,如："30"表示30%
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CheckFlag(self):
        """校验是否通过,0-未通过，1-校验通过, 3-未校验
        :rtype: int
        """
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

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
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._Progress = params.get("Progress")
        self._CheckFlag = params.get("CheckFlag")
        self._RequestId = params.get("RequestId")


class DescribeMigrateJobsRequest(AbstractModel):
    """DescribeMigrateJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        :param _JobName: 数据迁移任务名称
        :type JobName: str
        :param _Order: 排序字段，可以取值为JobId、Status、JobName、MigrateType、RunMode、CreateTime
        :type Order: str
        :param _OrderSeq: 排序方式，升序为ASC，降序为DESC
        :type OrderSeq: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回实例数量，默认20，有效区间[1,100]
        :type Limit: int
        :param _TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        """
        self._JobId = None
        self._JobName = None
        self._Order = None
        self._OrderSeq = None
        self._Offset = None
        self._Limit = None
        self._TagFilters = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """数据迁移任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Order(self):
        """排序字段，可以取值为JobId、Status、JobName、MigrateType、RunMode、CreateTime
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderSeq(self):
        """排序方式，升序为ASC，降序为DESC
        :rtype: str
        """
        return self._OrderSeq

    @OrderSeq.setter
    def OrderSeq(self, OrderSeq):
        self._OrderSeq = OrderSeq

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回实例数量，默认20，有效区间[1,100]
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagFilters(self):
        """标签过滤条件
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Order = params.get("Order")
        self._OrderSeq = params.get("OrderSeq")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateJobsResponse(AbstractModel):
    """DescribeMigrateJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务数目
        :type TotalCount: int
        :param _JobList: 任务详情数组
        :type JobList: list of MigrateJobInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """任务数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobList(self):
        """任务详情数组
        :rtype: list of MigrateJobInfo
        """
        return self._JobList

    @JobList.setter
    def JobList(self, JobList):
        self._JobList = JobList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self._JobList = []
            for item in params.get("JobList"):
                obj = MigrateJobInfo()
                obj._deserialize(item)
                self._JobList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeConfRequest(AbstractModel):
    """DescribeSubscribeConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """订阅实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeConfResponse(AbstractModel):
    """DescribeSubscribeConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID
        :type SubscribeId: str
        :param _SubscribeName: 订阅实例名称
        :type SubscribeName: str
        :param _ChannelId: 订阅通道
        :type ChannelId: str
        :param _Product: 订阅数据库类型
        :type Product: str
        :param _InstanceId: 被订阅的实例
        :type InstanceId: str
        :param _InstanceStatus: 被订阅的实例的状态，可能的值有running,offline,isolate
        :type InstanceStatus: str
        :param _SubsStatus: 订阅实例状态，可能的值有unconfigure-未配置，configuring-配置中，configured-已配置
        :type SubsStatus: str
        :param _Status: 订阅实例生命周期状态，可能的值有：normal-正常，isolating-隔离中，isolated-已隔离，offlining-下线中
        :type Status: str
        :param _CreateTime: 订阅实例创建时间
        :type CreateTime: str
        :param _IsolateTime: 订阅实例被隔离时间
        :type IsolateTime: str
        :param _ExpireTime: 订阅实例到期时间
        :type ExpireTime: str
        :param _OfflineTime: 订阅实例下线时间
        :type OfflineTime: str
        :param _ConsumeStartTime: 订阅实例消费时间起点。
        :type ConsumeStartTime: str
        :param _PayType: 订阅实例计费类型，1-小时计费，0-包年包月
        :type PayType: int
        :param _Vip: 订阅通道Vip
        :type Vip: str
        :param _Vport: 订阅通道Port
        :type Vport: int
        :param _UniqVpcId: 订阅通道所在VpcId
        :type UniqVpcId: str
        :param _UniqSubnetId: 订阅通道所在SubnetId
        :type UniqSubnetId: str
        :param _SdkConsumedTime: 当前SDK消费时间位点
        :type SdkConsumedTime: str
        :param _SdkHost: 订阅SDK IP地址
        :type SdkHost: str
        :param _SubscribeObjectType: 订阅对象类型0-全实例订阅，1-DDL数据订阅，2-DML结构订阅，3-DDL数据订阅+DML结构订阅
        :type SubscribeObjectType: int
        :param _SubscribeObjects: 订阅对象，当SubscribeObjectType 为0时，此字段为空数组
        :type SubscribeObjects: list of SubscribeObject
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _Region: 地域
        :type Region: str
        :param _Tags: 订阅实例的标签
        :type Tags: list of TagItem
        :param _AutoRenewFlag: 自动续费标识,0-不自动续费，1-自动续费
        :type AutoRenewFlag: int
        :param _SubscribeVersion: 数据订阅版本。老版订阅填txdts，kafka版填kafka
        :type SubscribeVersion: str
        :param _Errors: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of SubsErr
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._ChannelId = None
        self._Product = None
        self._InstanceId = None
        self._InstanceStatus = None
        self._SubsStatus = None
        self._Status = None
        self._CreateTime = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._ConsumeStartTime = None
        self._PayType = None
        self._Vip = None
        self._Vport = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._SdkConsumedTime = None
        self._SdkHost = None
        self._SubscribeObjectType = None
        self._SubscribeObjects = None
        self._ModifyTime = None
        self._Region = None
        self._Tags = None
        self._AutoRenewFlag = None
        self._SubscribeVersion = None
        self._Errors = None
        self._RequestId = None

    @property
    def SubscribeId(self):
        """订阅实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """订阅实例名称
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def ChannelId(self):
        """订阅通道
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Product(self):
        """订阅数据库类型
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """被订阅的实例
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """被订阅的实例的状态，可能的值有running,offline,isolate
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SubsStatus(self):
        """订阅实例状态，可能的值有unconfigure-未配置，configuring-配置中，configured-已配置
        :rtype: str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def Status(self):
        """订阅实例生命周期状态，可能的值有：normal-正常，isolating-隔离中，isolated-已隔离，offlining-下线中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """订阅实例创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsolateTime(self):
        """订阅实例被隔离时间
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        """订阅实例到期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        """订阅实例下线时间
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def ConsumeStartTime(self):
        """订阅实例消费时间起点。
        :rtype: str
        """
        return self._ConsumeStartTime

    @ConsumeStartTime.setter
    def ConsumeStartTime(self, ConsumeStartTime):
        self._ConsumeStartTime = ConsumeStartTime

    @property
    def PayType(self):
        """订阅实例计费类型，1-小时计费，0-包年包月
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Vip(self):
        """订阅通道Vip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """订阅通道Port
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def UniqVpcId(self):
        """订阅通道所在VpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """订阅通道所在SubnetId
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def SdkConsumedTime(self):
        """当前SDK消费时间位点
        :rtype: str
        """
        return self._SdkConsumedTime

    @SdkConsumedTime.setter
    def SdkConsumedTime(self, SdkConsumedTime):
        self._SdkConsumedTime = SdkConsumedTime

    @property
    def SdkHost(self):
        """订阅SDK IP地址
        :rtype: str
        """
        return self._SdkHost

    @SdkHost.setter
    def SdkHost(self, SdkHost):
        self._SdkHost = SdkHost

    @property
    def SubscribeObjectType(self):
        """订阅对象类型0-全实例订阅，1-DDL数据订阅，2-DML结构订阅，3-DDL数据订阅+DML结构订阅
        :rtype: int
        """
        return self._SubscribeObjectType

    @SubscribeObjectType.setter
    def SubscribeObjectType(self, SubscribeObjectType):
        self._SubscribeObjectType = SubscribeObjectType

    @property
    def SubscribeObjects(self):
        """订阅对象，当SubscribeObjectType 为0时，此字段为空数组
        :rtype: list of SubscribeObject
        """
        return self._SubscribeObjects

    @SubscribeObjects.setter
    def SubscribeObjects(self, SubscribeObjects):
        self._SubscribeObjects = SubscribeObjects

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
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        """订阅实例的标签
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRenewFlag(self):
        """自动续费标识,0-不自动续费，1-自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SubscribeVersion(self):
        """数据订阅版本。老版订阅填txdts，kafka版填kafka
        :rtype: str
        """
        return self._SubscribeVersion

    @SubscribeVersion.setter
    def SubscribeVersion(self, SubscribeVersion):
        self._SubscribeVersion = SubscribeVersion

    @property
    def Errors(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SubsErr
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

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
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._ChannelId = params.get("ChannelId")
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._SubsStatus = params.get("SubsStatus")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._ConsumeStartTime = params.get("ConsumeStartTime")
        self._PayType = params.get("PayType")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._SdkConsumedTime = params.get("SdkConsumedTime")
        self._SdkHost = params.get("SdkHost")
        self._SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("SubscribeObjects") is not None:
            self._SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self._SubscribeObjects.append(obj)
        self._ModifyTime = params.get("ModifyTime")
        self._Region = params.get("Region")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SubscribeVersion = params.get("SubscribeVersion")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SubsErr()
                obj._deserialize(item)
                self._Errors.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribesRequest(AbstractModel):
    """DescribeSubscribes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅的实例ID
        :type SubscribeId: str
        :param _SubscribeName: 数据订阅的实例名称
        :type SubscribeName: str
        :param _InstanceId: 绑定数据库实例的ID
        :type InstanceId: str
        :param _ChannelId: 数据订阅实例的通道ID
        :type ChannelId: str
        :param _PayType: 计费模式筛选，可能的值：0-包年包月，1-按量计费
        :type PayType: str
        :param _Product: 订阅的数据库产品，如mysql
        :type Product: str
        :param _Status: 数据订阅实例的状态，creating - 创建中，normal - 正常运行，isolating - 隔离中，isolated - 已隔离，offlining - 下线中
        :type Status: list of str
        :param _SubsStatus: 数据订阅实例的配置状态，unconfigure - 未配置， configuring - 配置中，configured - 已配置
        :type SubsStatus: list of str
        :param _Offset: 返回记录的起始偏移量，默认为0。请输入非负整数
        :type Offset: int
        :param _Limit: 单次返回的记录数量，默认20。请输入1到100的整数
        :type Limit: int
        :param _OrderDirection: 排序方向，可选的值为"DESC"和"ASC"，默认为"DESC"，按创建时间逆序排序
        :type OrderDirection: str
        :param _TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        :param _SubscribeVersion: 订阅实例版本;txdts-旧版数据订阅，kafka-kafka版本数据订阅
        :type SubscribeVersion: str
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._InstanceId = None
        self._ChannelId = None
        self._PayType = None
        self._Product = None
        self._Status = None
        self._SubsStatus = None
        self._Offset = None
        self._Limit = None
        self._OrderDirection = None
        self._TagFilters = None
        self._SubscribeVersion = None

    @property
    def SubscribeId(self):
        """数据订阅的实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """数据订阅的实例名称
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def InstanceId(self):
        """绑定数据库实例的ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChannelId(self):
        """数据订阅实例的通道ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def PayType(self):
        """计费模式筛选，可能的值：0-包年包月，1-按量计费
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Product(self):
        """订阅的数据库产品，如mysql
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Status(self):
        """数据订阅实例的状态，creating - 创建中，normal - 正常运行，isolating - 隔离中，isolated - 已隔离，offlining - 下线中
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubsStatus(self):
        """数据订阅实例的配置状态，unconfigure - 未配置， configuring - 配置中，configured - 已配置
        :rtype: list of str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def Offset(self):
        """返回记录的起始偏移量，默认为0。请输入非负整数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """单次返回的记录数量，默认20。请输入1到100的整数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderDirection(self):
        """排序方向，可选的值为"DESC"和"ASC"，默认为"DESC"，按创建时间逆序排序
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def TagFilters(self):
        """标签过滤条件
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def SubscribeVersion(self):
        """订阅实例版本;txdts-旧版数据订阅，kafka-kafka版本数据订阅
        :rtype: str
        """
        return self._SubscribeVersion

    @SubscribeVersion.setter
    def SubscribeVersion(self, SubscribeVersion):
        self._SubscribeVersion = SubscribeVersion


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._InstanceId = params.get("InstanceId")
        self._ChannelId = params.get("ChannelId")
        self._PayType = params.get("PayType")
        self._Product = params.get("Product")
        self._Status = params.get("Status")
        self._SubsStatus = params.get("SubsStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderDirection = params.get("OrderDirection")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._SubscribeVersion = params.get("SubscribeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribesResponse(AbstractModel):
    """DescribeSubscribes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param _Items: 数据订阅实例的信息列表
        :type Items: list of SubscribeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合查询条件的实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """数据订阅实例的信息列表
        :rtype: list of SubscribeInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SubscribeInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """目的实例信息，具体内容跟迁移任务类型相关

    """

    def __init__(self):
        r"""
        :param _Region: 目标实例地域，如ap-guangzhou
        :type Region: str
        :param _InstanceId: 目标实例ID，如cdb-jd92ijd8
        :type InstanceId: str
        :param _Ip: 目标实例vip。已废弃，无需填写
        :type Ip: str
        :param _Port: 目标实例vport。已废弃，无需填写
        :type Port: int
        :param _ReadOnly: 目前只对MySQL有效。当为整实例迁移时，1-只读，0-可读写。
        :type ReadOnly: int
        :param _User: 目标数据库账号
        :type User: str
        :param _Password: 目标数据库密码
        :type Password: str
        """
        self._Region = None
        self._InstanceId = None
        self._Ip = None
        self._Port = None
        self._ReadOnly = None
        self._User = None
        self._Password = None

    @property
    def Region(self):
        """目标实例地域，如ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        """目标实例ID，如cdb-jd92ijd8
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        warnings.warn("parameter `Ip` is deprecated", DeprecationWarning) 

        """目标实例vip。已废弃，无需填写
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        warnings.warn("parameter `Ip` is deprecated", DeprecationWarning) 

        self._Ip = Ip

    @property
    def Port(self):
        warnings.warn("parameter `Port` is deprecated", DeprecationWarning) 

        """目标实例vport。已废弃，无需填写
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        warnings.warn("parameter `Port` is deprecated", DeprecationWarning) 

        self._Port = Port

    @property
    def ReadOnly(self):
        """目前只对MySQL有效。当为整实例迁移时，1-只读，0-可读写。
        :rtype: int
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def User(self):
        """目标数据库账号
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """目标数据库密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._ReadOnly = params.get("ReadOnly")
        self._User = params.get("User")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfo(AbstractModel):
    """迁移任务错误信息及提示

    """

    def __init__(self):
        r"""
        :param _ErrorLog: 具体的报错日志, 包含错误码和错误信息
        :type ErrorLog: str
        :param _HelpDoc: 报错对应的帮助文档Ur
        :type HelpDoc: str
        """
        self._ErrorLog = None
        self._HelpDoc = None

    @property
    def ErrorLog(self):
        """具体的报错日志, 包含错误码和错误信息
        :rtype: str
        """
        return self._ErrorLog

    @ErrorLog.setter
    def ErrorLog(self, ErrorLog):
        self._ErrorLog = ErrorLog

    @property
    def HelpDoc(self):
        """报错对应的帮助文档Ur
        :rtype: str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc


    def _deserialize(self, params):
        self._ErrorLog = params.get("ErrorLog")
        self._HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSubscribeRequest(AbstractModel):
    """IsolateSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """订阅实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSubscribeResponse(AbstractModel):
    """IsolateSubscribe返回参数结构体

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


class MigrateDetailInfo(AbstractModel):
    """描述详细迁移过程

    """

    def __init__(self):
        r"""
        :param _StepAll: 总步骤数
        :type StepAll: int
        :param _StepNow: 当前步骤
        :type StepNow: int
        :param _Progress: 总进度,如："10"
        :type Progress: str
        :param _CurrentStepProgress: 当前步骤进度,如:"1"
        :type CurrentStepProgress: str
        :param _MasterSlaveDistance: 主从差距，MB；在增量同步阶段有效，目前支持产品为：redis和mysql
        :type MasterSlaveDistance: int
        :param _SecondsBehindMaster: 主从差距，秒；在增量同步阶段有效，目前支持产品为：mysql
        :type SecondsBehindMaster: int
        :param _StepInfo: 步骤信息
        :type StepInfo: list of MigrateStepDetailInfo
        """
        self._StepAll = None
        self._StepNow = None
        self._Progress = None
        self._CurrentStepProgress = None
        self._MasterSlaveDistance = None
        self._SecondsBehindMaster = None
        self._StepInfo = None

    @property
    def StepAll(self):
        """总步骤数
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """当前步骤
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Progress(self):
        """总进度,如："10"
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CurrentStepProgress(self):
        """当前步骤进度,如:"1"
        :rtype: str
        """
        return self._CurrentStepProgress

    @CurrentStepProgress.setter
    def CurrentStepProgress(self, CurrentStepProgress):
        self._CurrentStepProgress = CurrentStepProgress

    @property
    def MasterSlaveDistance(self):
        """主从差距，MB；在增量同步阶段有效，目前支持产品为：redis和mysql
        :rtype: int
        """
        return self._MasterSlaveDistance

    @MasterSlaveDistance.setter
    def MasterSlaveDistance(self, MasterSlaveDistance):
        self._MasterSlaveDistance = MasterSlaveDistance

    @property
    def SecondsBehindMaster(self):
        """主从差距，秒；在增量同步阶段有效，目前支持产品为：mysql
        :rtype: int
        """
        return self._SecondsBehindMaster

    @SecondsBehindMaster.setter
    def SecondsBehindMaster(self, SecondsBehindMaster):
        self._SecondsBehindMaster = SecondsBehindMaster

    @property
    def StepInfo(self):
        """步骤信息
        :rtype: list of MigrateStepDetailInfo
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo


    def _deserialize(self, params):
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._Progress = params.get("Progress")
        self._CurrentStepProgress = params.get("CurrentStepProgress")
        self._MasterSlaveDistance = params.get("MasterSlaveDistance")
        self._SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self._StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrateStepDetailInfo()
                obj._deserialize(item)
                self._StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateJobInfo(AbstractModel):
    """迁移任务详情

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        :param _JobName: 数据迁移任务名称
        :type JobName: str
        :param _MigrateOption: 迁移任务配置选项
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param _SrcDatabaseType: 源实例数据库类型:mysql，redis，mongodb，postgresql，mariadb，percona
        :type SrcDatabaseType: str
        :param _SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),cdb(腾讯云数据库实例),ccn(云联网实例)
        :type SrcAccessType: str
        :param _SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param _DstDatabaseType: 目标实例数据库类型:mysql，redis，mongodb，postgresql，mariadb，percona
        :type DstDatabaseType: str
        :param _DstAccessType: 目标实例接入类型，目前支持：cdb(腾讯云数据库实例)
        :type DstAccessType: str
        :param _DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param _DatabaseInfo: 需要迁移的源数据库表信息，如果需要迁移的是整个实例，该字段为[]
        :type DatabaseInfo: str
        :param _CreateTime: 任务创建(提交)时间
        :type CreateTime: str
        :param _StartTime: 任务开始执行时间
        :type StartTime: str
        :param _EndTime: 任务执行结束时间
        :type EndTime: str
        :param _Status: 任务状态,取值为：1-创建中(Creating),3-校验中(Checking)4-校验通过(CheckPass),5-校验不通过（CheckNotPass）,7-任务运行(Running),8-准备完成（ReadyComplete）,9-任务成功（Success）,10-任务失败（Failed）,11-撤销中（Stopping）,12-完成中（Completing）,23-未知状态（Unknown）
        :type Status: int
        :param _Detail: 任务详情
        :type Detail: :class:`tencentcloud.dts.v20180330.models.MigrateDetailInfo`
        :param _ErrorInfo: 任务错误信息提示，当任务发生错误时，不为null或者空值
        :type ErrorInfo: list of ErrorInfo
        :param _Tags: 标签
        :type Tags: list of TagItem
        :param _SrcInfoMulti: 源实例为集群时且接入为非cdb时源实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInfoMulti: list of SrcInfo
        """
        self._JobId = None
        self._JobName = None
        self._MigrateOption = None
        self._SrcDatabaseType = None
        self._SrcAccessType = None
        self._SrcInfo = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._DstInfo = None
        self._DatabaseInfo = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Detail = None
        self._ErrorInfo = None
        self._Tags = None
        self._SrcInfoMulti = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """数据迁移任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def MigrateOption(self):
        """迁移任务配置选项
        :rtype: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        """
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcDatabaseType(self):
        """源实例数据库类型:mysql，redis，mongodb，postgresql，mariadb，percona
        :rtype: str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        """源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),cdb(腾讯云数据库实例),ccn(云联网实例)
        :rtype: str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        """源实例信息，具体内容跟迁移任务类型相关
        :rtype: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstDatabaseType(self):
        """目标实例数据库类型:mysql，redis，mongodb，postgresql，mariadb，percona
        :rtype: str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        """目标实例接入类型，目前支持：cdb(腾讯云数据库实例)
        :rtype: str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        """目标实例信息
        :rtype: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DatabaseInfo(self):
        """需要迁移的源数据库表信息，如果需要迁移的是整个实例，该字段为[]
        :rtype: str
        """
        return self._DatabaseInfo

    @DatabaseInfo.setter
    def DatabaseInfo(self, DatabaseInfo):
        self._DatabaseInfo = DatabaseInfo

    @property
    def CreateTime(self):
        """任务创建(提交)时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """任务开始执行时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务执行结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """任务状态,取值为：1-创建中(Creating),3-校验中(Checking)4-校验通过(CheckPass),5-校验不通过（CheckNotPass）,7-任务运行(Running),8-准备完成（ReadyComplete）,9-任务成功（Success）,10-任务失败（Failed）,11-撤销中（Stopping）,12-完成中（Completing）,23-未知状态（Unknown）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Detail(self):
        """任务详情
        :rtype: :class:`tencentcloud.dts.v20180330.models.MigrateDetailInfo`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def ErrorInfo(self):
        """任务错误信息提示，当任务发生错误时，不为null或者空值
        :rtype: list of ErrorInfo
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Tags(self):
        """标签
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SrcInfoMulti(self):
        """源实例为集群时且接入为非cdb时源实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SrcInfo
        """
        return self._SrcInfoMulti

    @SrcInfoMulti.setter
    def SrcInfoMulti(self, SrcInfoMulti):
        self._SrcInfoMulti = SrcInfoMulti


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._DatabaseInfo = params.get("DatabaseInfo")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        if params.get("Detail") is not None:
            self._Detail = MigrateDetailInfo()
            self._Detail._deserialize(params.get("Detail"))
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfo()
                obj._deserialize(item)
                self._ErrorInfo.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("SrcInfoMulti") is not None:
            self._SrcInfoMulti = []
            for item in params.get("SrcInfoMulti"):
                obj = SrcInfo()
                obj._deserialize(item)
                self._SrcInfoMulti.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOption(AbstractModel):
    """迁移任务配置选项

    """

    def __init__(self):
        r"""
        :param _RunMode: 任务运行模式，值包括：1-立即执行，2-定时执行
        :type RunMode: int
        :param _ExpectTime: 期望执行时间，当runMode=2时，该字段必填，时间格式：yyyy-mm-dd hh:mm:ss
        :type ExpectTime: str
        :param _MigrateType: 数据迁移类型，值包括：1-结构迁移,2-全量迁移,3-全量+增量迁移
        :type MigrateType: int
        :param _MigrateObject: 迁移对象，1-整个实例，2-指定库表
        :type MigrateObject: int
        :param _ConsistencyType: 抽样数据一致性检测参数，1-未配置,2-全量检测,3-抽样检测, 4-仅校验不一致表,5-不检测
        :type ConsistencyType: int
        :param _IsOverrideRoot: 是否用源库Root账户覆盖目标库，值包括：0-不覆盖，1-覆盖，选择库表或者结构迁移时应该为0
        :type IsOverrideRoot: int
        :param _ExternParams: 不同数据库用到的额外参数.以JSON格式描述. 
Redis可定义如下的参数: 
{ 
	"ClientOutputBufferHardLimit":512, 	从机缓冲区的硬性容量限制(MB) 
	"ClientOutputBufferSoftLimit":512, 	从机缓冲区的软性容量限制(MB) 
	"ClientOutputBufferPersistTime":60, 从机缓冲区的软性限制持续时间(秒) 
	"ReplBacklogSize":512, 	环形缓冲区容量限制(MB) 
	"ReplTimeout":120，		复制超时时间(秒) 
}
MongoDB可定义如下的参数: 
{
	'SrcAuthDatabase':'admin', 
	'SrcAuthFlag': "1", 
	'SrcAuthMechanism':"SCRAM-SHA-1"
}
MySQL暂不支持额外参数设置。
        :type ExternParams: str
        :param _ConsistencyParams: 仅用于“抽样数据一致性检测”，ConsistencyType配置为抽样检测时，必选
        :type ConsistencyParams: :class:`tencentcloud.dts.v20180330.models.ConsistencyParams`
        """
        self._RunMode = None
        self._ExpectTime = None
        self._MigrateType = None
        self._MigrateObject = None
        self._ConsistencyType = None
        self._IsOverrideRoot = None
        self._ExternParams = None
        self._ConsistencyParams = None

    @property
    def RunMode(self):
        """任务运行模式，值包括：1-立即执行，2-定时执行
        :rtype: int
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectTime(self):
        """期望执行时间，当runMode=2时，该字段必填，时间格式：yyyy-mm-dd hh:mm:ss
        :rtype: str
        """
        return self._ExpectTime

    @ExpectTime.setter
    def ExpectTime(self, ExpectTime):
        self._ExpectTime = ExpectTime

    @property
    def MigrateType(self):
        """数据迁移类型，值包括：1-结构迁移,2-全量迁移,3-全量+增量迁移
        :rtype: int
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def MigrateObject(self):
        """迁移对象，1-整个实例，2-指定库表
        :rtype: int
        """
        return self._MigrateObject

    @MigrateObject.setter
    def MigrateObject(self, MigrateObject):
        self._MigrateObject = MigrateObject

    @property
    def ConsistencyType(self):
        """抽样数据一致性检测参数，1-未配置,2-全量检测,3-抽样检测, 4-仅校验不一致表,5-不检测
        :rtype: int
        """
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def IsOverrideRoot(self):
        """是否用源库Root账户覆盖目标库，值包括：0-不覆盖，1-覆盖，选择库表或者结构迁移时应该为0
        :rtype: int
        """
        return self._IsOverrideRoot

    @IsOverrideRoot.setter
    def IsOverrideRoot(self, IsOverrideRoot):
        self._IsOverrideRoot = IsOverrideRoot

    @property
    def ExternParams(self):
        """不同数据库用到的额外参数.以JSON格式描述. 
Redis可定义如下的参数: 
{ 
	"ClientOutputBufferHardLimit":512, 	从机缓冲区的硬性容量限制(MB) 
	"ClientOutputBufferSoftLimit":512, 	从机缓冲区的软性容量限制(MB) 
	"ClientOutputBufferPersistTime":60, 从机缓冲区的软性限制持续时间(秒) 
	"ReplBacklogSize":512, 	环形缓冲区容量限制(MB) 
	"ReplTimeout":120，		复制超时时间(秒) 
}
MongoDB可定义如下的参数: 
{
	'SrcAuthDatabase':'admin', 
	'SrcAuthFlag': "1", 
	'SrcAuthMechanism':"SCRAM-SHA-1"
}
MySQL暂不支持额外参数设置。
        :rtype: str
        """
        return self._ExternParams

    @ExternParams.setter
    def ExternParams(self, ExternParams):
        self._ExternParams = ExternParams

    @property
    def ConsistencyParams(self):
        """仅用于“抽样数据一致性检测”，ConsistencyType配置为抽样检测时，必选
        :rtype: :class:`tencentcloud.dts.v20180330.models.ConsistencyParams`
        """
        return self._ConsistencyParams

    @ConsistencyParams.setter
    def ConsistencyParams(self, ConsistencyParams):
        self._ConsistencyParams = ConsistencyParams


    def _deserialize(self, params):
        self._RunMode = params.get("RunMode")
        self._ExpectTime = params.get("ExpectTime")
        self._MigrateType = params.get("MigrateType")
        self._MigrateObject = params.get("MigrateObject")
        self._ConsistencyType = params.get("ConsistencyType")
        self._IsOverrideRoot = params.get("IsOverrideRoot")
        self._ExternParams = params.get("ExternParams")
        if params.get("ConsistencyParams") is not None:
            self._ConsistencyParams = ConsistencyParams()
            self._ConsistencyParams._deserialize(params.get("ConsistencyParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateStepDetailInfo(AbstractModel):
    """迁移中的步骤信息

    """

    def __init__(self):
        r"""
        :param _StepNo: 步骤序列
        :type StepNo: int
        :param _StepName: 步骤展现名称
        :type StepName: str
        :param _StepId: 步骤英文标识
        :type StepId: str
        :param _Status: 步骤状态:0-默认值,1-成功,2-失败,3-执行中,4-未执行
        :type Status: int
        :param _StartTime: 当前步骤开始的时间，格式为"yyyy-mm-dd hh:mm:ss"，该字段不存在或者为空是无意义
        :type StartTime: str
        """
        self._StepNo = None
        self._StepName = None
        self._StepId = None
        self._Status = None
        self._StartTime = None

    @property
    def StepNo(self):
        """步骤序列
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        """步骤展现名称
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        """步骤英文标识
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        """步骤状态:0-默认值,1-成功,2-失败,3-执行中,4-未执行
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        """当前步骤开始的时间，格式为"yyyy-mm-dd hh:mm:ss"，该字段不存在或者为空是无意义
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobRequest(AbstractModel):
    """ModifyMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 待修改的数据迁移任务ID
        :type JobId: str
        :param _JobName: 数据迁移任务名称
        :type JobName: str
        :param _MigrateOption: 迁移任务配置选项
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param _SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例),cdb(云上CDB实例)
        :type SrcAccessType: str
        :param _SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param _DstAccessType: 目标实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例)，cdb(云上CDB实例). 目前只支持cdb.
        :type DstAccessType: str
        :param _DstInfo: 目标实例信息, 其中目标实例地域不允许修改.
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param _DatabaseInfo: 当选择'指定库表'迁移的时候, 需要设置待迁移的源数据库表信息,用符合json数组格式的字符串描述, 如下所例。

对于database-table两级结构的数据库：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
对于database-schema-table三级结构：
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]

如果是'整个实例'的迁移模式,不需设置该字段
        :type DatabaseInfo: str
        :param _SrcNodeType: 源实例类型: ""或者"simple":主从节点，"cluster": 集群节点
        :type SrcNodeType: str
        :param _SrcInfoMulti: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfoMulti: list of SrcInfo
        """
        self._JobId = None
        self._JobName = None
        self._MigrateOption = None
        self._SrcAccessType = None
        self._SrcInfo = None
        self._DstAccessType = None
        self._DstInfo = None
        self._DatabaseInfo = None
        self._SrcNodeType = None
        self._SrcInfoMulti = None

    @property
    def JobId(self):
        """待修改的数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """数据迁移任务名称
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def MigrateOption(self):
        """迁移任务配置选项
        :rtype: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        """
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcAccessType(self):
        """源实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例),cdb(云上CDB实例)
        :rtype: str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        """源实例信息，具体内容跟迁移任务类型相关
        :rtype: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstAccessType(self):
        """目标实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例)，cdb(云上CDB实例). 目前只支持cdb.
        :rtype: str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        """目标实例信息, 其中目标实例地域不允许修改.
        :rtype: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DatabaseInfo(self):
        """当选择'指定库表'迁移的时候, 需要设置待迁移的源数据库表信息,用符合json数组格式的字符串描述, 如下所例。

对于database-table两级结构的数据库：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
对于database-schema-table三级结构：
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]

如果是'整个实例'的迁移模式,不需设置该字段
        :rtype: str
        """
        return self._DatabaseInfo

    @DatabaseInfo.setter
    def DatabaseInfo(self, DatabaseInfo):
        self._DatabaseInfo = DatabaseInfo

    @property
    def SrcNodeType(self):
        """源实例类型: ""或者"simple":主从节点，"cluster": 集群节点
        :rtype: str
        """
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def SrcInfoMulti(self):
        """源实例信息，具体内容跟迁移任务类型相关
        :rtype: list of SrcInfo
        """
        return self._SrcInfoMulti

    @SrcInfoMulti.setter
    def SrcInfoMulti(self, SrcInfoMulti):
        self._SrcInfoMulti = SrcInfoMulti


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        self._SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = SrcInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = DstInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._DatabaseInfo = params.get("DatabaseInfo")
        self._SrcNodeType = params.get("SrcNodeType")
        if params.get("SrcInfoMulti") is not None:
            self._SrcInfoMulti = []
            for item in params.get("SrcInfoMulti"):
                obj = SrcInfo()
                obj._deserialize(item)
                self._SrcInfoMulti.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobResponse(AbstractModel):
    """ModifyMigrateJob返回参数结构体

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


class ModifySubscribeAutoRenewFlagRequest(AbstractModel):
    """ModifySubscribeAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 订阅实例ID，例如：subs-8uey736k
        :type SubscribeId: str
        :param _AutoRenewFlag: 自动续费标识。1-自动续费，0-不自动续费
        :type AutoRenewFlag: int
        """
        self._SubscribeId = None
        self._AutoRenewFlag = None

    @property
    def SubscribeId(self):
        """订阅实例ID，例如：subs-8uey736k
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def AutoRenewFlag(self):
        """自动续费标识。1-自动续费，0-不自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeAutoRenewFlagResponse(AbstractModel):
    """ModifySubscribeAutoRenewFlag返回参数结构体

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


class ModifySubscribeConsumeTimeRequest(AbstractModel):
    """ModifySubscribeConsumeTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param _ConsumeStartTime: 消费时间起点，也即是指定订阅数据的时间起点，时间格式如：Y-m-d h:m:s，取值范围为过去24小时之内
        :type ConsumeStartTime: str
        """
        self._SubscribeId = None
        self._ConsumeStartTime = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def ConsumeStartTime(self):
        """消费时间起点，也即是指定订阅数据的时间起点，时间格式如：Y-m-d h:m:s，取值范围为过去24小时之内
        :rtype: str
        """
        return self._ConsumeStartTime

    @ConsumeStartTime.setter
    def ConsumeStartTime(self, ConsumeStartTime):
        self._ConsumeStartTime = ConsumeStartTime


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._ConsumeStartTime = params.get("ConsumeStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeConsumeTimeResponse(AbstractModel):
    """ModifySubscribeConsumeTime返回参数结构体

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


class ModifySubscribeNameRequest(AbstractModel):
    """ModifySubscribeName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param _SubscribeName: 数据订阅实例的名称，长度限制为[1,60]
        :type SubscribeName: str
        """
        self._SubscribeId = None
        self._SubscribeName = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """数据订阅实例的名称，长度限制为[1,60]
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeNameResponse(AbstractModel):
    """ModifySubscribeName返回参数结构体

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


class ModifySubscribeObjectsRequest(AbstractModel):
    """ModifySubscribeObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param _SubscribeObjectType: 数据订阅的类型，可选的值有：0 - 全实例订阅；1 - 数据订阅；2 - 结构订阅；3 - 数据订阅+结构订阅
        :type SubscribeObjectType: int
        :param _Objects: 订阅的数据库表信息
        :type Objects: list of SubscribeObject
        """
        self._SubscribeId = None
        self._SubscribeObjectType = None
        self._Objects = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeObjectType(self):
        """数据订阅的类型，可选的值有：0 - 全实例订阅；1 - 数据订阅；2 - 结构订阅；3 - 数据订阅+结构订阅
        :rtype: int
        """
        return self._SubscribeObjectType

    @SubscribeObjectType.setter
    def SubscribeObjectType(self, SubscribeObjectType):
        self._SubscribeObjectType = SubscribeObjectType

    @property
    def Objects(self):
        """订阅的数据库表信息
        :rtype: list of SubscribeObject
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self._Objects = []
            for item in params.get("Objects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self._Objects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeObjectsResponse(AbstractModel):
    """ModifySubscribeObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的ID
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """异步任务的ID
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

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
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifySubscribeVipVportRequest(AbstractModel):
    """ModifySubscribeVipVport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param _DstUniqSubnetId: 指定目的子网，如果传此参数，DstIp必须在目的子网内
        :type DstUniqSubnetId: str
        :param _DstIp: 目标IP，与DstPort至少传一个
        :type DstIp: str
        :param _DstPort: 目标PORT，支持范围为：[1025-65535]
        :type DstPort: int
        """
        self._SubscribeId = None
        self._DstUniqSubnetId = None
        self._DstIp = None
        self._DstPort = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def DstUniqSubnetId(self):
        """指定目的子网，如果传此参数，DstIp必须在目的子网内
        :rtype: str
        """
        return self._DstUniqSubnetId

    @DstUniqSubnetId.setter
    def DstUniqSubnetId(self, DstUniqSubnetId):
        self._DstUniqSubnetId = DstUniqSubnetId

    @property
    def DstIp(self):
        """目标IP，与DstPort至少传一个
        :rtype: str
        """
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        """目标PORT，支持范围为：[1025-65535]
        :rtype: int
        """
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._DstUniqSubnetId = params.get("DstUniqSubnetId")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeVipVportResponse(AbstractModel):
    """ModifySubscribeVipVport返回参数结构体

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


class OfflineIsolatedSubscribeRequest(AbstractModel):
    """OfflineIsolatedSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedSubscribeResponse(AbstractModel):
    """OfflineIsolatedSubscribe返回参数结构体

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


class ResetSubscribeRequest(AbstractModel):
    """ResetSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """数据订阅实例的ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetSubscribeResponse(AbstractModel):
    """ResetSubscribe返回参数结构体

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


class SrcInfo(AbstractModel):
    """源实例信息

    """

    def __init__(self):
        r"""
        :param _AccessKey: 阿里云AccessKey。源库是阿里云RDS5.6适用
        :type AccessKey: str
        :param _Ip: 实例的IP地址
        :type Ip: str
        :param _Port: 实例的端口
        :type Port: int
        :param _User: 实例的用户名
        :type User: str
        :param _Password: 实例的密码
        :type Password: str
        :param _RdsInstanceId: 阿里云RDS实例ID。源库是阿里云RDS5.6/5.6适用
        :type RdsInstanceId: str
        :param _CvmInstanceId: CVM实例短ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要传递此字段
        :type CvmInstanceId: str
        :param _UniqDcgId: 专线网关ID，格式如：dcg-0rxtqqxb
        :type UniqDcgId: str
        :param _VpcId: 私有网络ID，格式如：vpc-92jblxto
        :type VpcId: str
        :param _SubnetId: 私有网络下的子网ID，格式如：subnet-3paxmkdz
        :type SubnetId: str
        :param _UniqVpnGwId: VPN网关ID，格式如：vpngw-9ghexg7q
        :type UniqVpnGwId: str
        :param _InstanceId: 数据库实例ID，格式如：cdb-powiqx8q
        :type InstanceId: str
        :param _Region: 地域英文名，如：ap-guangzhou
        :type Region: str
        :param _Supplier: 当实例为RDS实例时，填写为aliyun, 其他情况均填写others
        :type Supplier: str
        :param _CcnId: 云联网ID，如：ccn-afp6kltc
        :type CcnId: str
        :param _EngineVersion: 数据库版本，当实例为RDS实例时才有效，格式如：5.6或者5.7，默认为5.6
        :type EngineVersion: str
        """
        self._AccessKey = None
        self._Ip = None
        self._Port = None
        self._User = None
        self._Password = None
        self._RdsInstanceId = None
        self._CvmInstanceId = None
        self._UniqDcgId = None
        self._VpcId = None
        self._SubnetId = None
        self._UniqVpnGwId = None
        self._InstanceId = None
        self._Region = None
        self._Supplier = None
        self._CcnId = None
        self._EngineVersion = None

    @property
    def AccessKey(self):
        """阿里云AccessKey。源库是阿里云RDS5.6适用
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def Ip(self):
        """实例的IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """实例的端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        """实例的用户名
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """实例的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RdsInstanceId(self):
        """阿里云RDS实例ID。源库是阿里云RDS5.6/5.6适用
        :rtype: str
        """
        return self._RdsInstanceId

    @RdsInstanceId.setter
    def RdsInstanceId(self, RdsInstanceId):
        self._RdsInstanceId = RdsInstanceId

    @property
    def CvmInstanceId(self):
        """CVM实例短ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要传递此字段
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        """专线网关ID，格式如：dcg-0rxtqqxb
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def VpcId(self):
        """私有网络ID，格式如：vpc-92jblxto
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络下的子网ID，格式如：subnet-3paxmkdz
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def UniqVpnGwId(self):
        """VPN网关ID，格式如：vpngw-9ghexg7q
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def InstanceId(self):
        """数据库实例ID，格式如：cdb-powiqx8q
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Region(self):
        """地域英文名，如：ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Supplier(self):
        """当实例为RDS实例时，填写为aliyun, 其他情况均填写others
        :rtype: str
        """
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def CcnId(self):
        """云联网ID，如：ccn-afp6kltc
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def EngineVersion(self):
        """数据库版本，当实例为RDS实例时才有效，格式如：5.6或者5.7，默认为5.6
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion


    def _deserialize(self, params):
        self._AccessKey = params.get("AccessKey")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._RdsInstanceId = params.get("RdsInstanceId")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        self._Supplier = params.get("Supplier")
        self._CcnId = params.get("CcnId")
        self._EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob返回参数结构体

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


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 数据迁移任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """数据迁移任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob返回参数结构体

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


class SubsErr(AbstractModel):
    """查询订阅配置的错误信息

    """

    def __init__(self):
        r"""
        :param _Message: 错误信息
        :type Message: str
        """
        self._Message = None

    @property
    def Message(self):
        """错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeInfo(AbstractModel):
    """订阅实例信息

    """

    def __init__(self):
        r"""
        :param _SubscribeId: 数据订阅的实例ID
        :type SubscribeId: str
        :param _SubscribeName: 数据订阅实例的名称
        :type SubscribeName: str
        :param _ChannelId: 数据订阅实例绑定的通道ID。kafka版订阅就是kafka topic
        :type ChannelId: str
        :param _Product: 订阅实例的类型，目前支持 cynosdbmysql,mariadb,mongodb,mysql,percona,tdpg,tdsqlpercona(tdsqlmysql)
        :type Product: str
        :param _InstanceId: 数据订阅实例绑定的数据库实例ID
        :type InstanceId: str
        :param _InstanceStatus: 云数据库状态：running 运行中，isolated 已隔离，offline 已下线。如果不是云上，此值为空
        :type InstanceStatus: str
        :param _SubsStatus: 数据订阅状态，可能的值为：未启动 notStarted, 校验中 checking, 校验不通过 checkNotPass, 校验通过 checkPass, 启动中 starting, 运行中 running, 异常出错 error
        :type SubsStatus: str
        :param _ModifyTime: 上次修改时间，时间格式如：Y-m-d h:m:s
        :type ModifyTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsolateTime: 隔离时间，时间格式如：Y-m-d h:m:s
        :type IsolateTime: str
        :param _ExpireTime: 包年包月任务的到期时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :type ExpireTime: str
        :param _OfflineTime: 下线时间
        :type OfflineTime: str
        :param _ConsumeStartTime: 最近一次修改的消费时间起点，如果从未修改则为零值
        :type ConsumeStartTime: str
        :param _AutoRenewFlag: 自动续费标识。只有当 PayType=0，该值才有意义。枚举值：0-不自动续费，1-自动续费
        :type AutoRenewFlag: int
        :param _Region: 数据订阅实例所属地域
        :type Region: str
        :param _PayType: 计费方式，0 - 包年包月，1 - 按量计费
        :type PayType: int
        :param _Vip: 旧版订阅通道的vip
        :type Vip: str
        :param _Vport: 数据订阅实例的Vport
        :type Vport: int
        :param _UniqVpcId: 数据订阅实例Vip所在VPC的唯一ID
        :type UniqVpcId: str
        :param _UniqSubnetId: 数据订阅实例Vip所在子网的唯一ID
        :type UniqSubnetId: str
        :param _Status: 数据订阅生命周期状态，可能的值为：正常 normal, 隔离中 isolating, 已隔离 isolated, 下线中 offlining, 按量转包年包月中 post2PrePayIng
        :type Status: str
        :param _SdkConsumedTime: SDK最后一条确认消息的时间戳，如果SDK一直消费，也可以作为SDK当前消费时间点
        :type SdkConsumedTime: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param _SubscribeVersion: 订阅实例版本；txdts-旧版数据订阅,kafka-kafka版本数据订阅
        :type SubscribeVersion: str
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._ChannelId = None
        self._Product = None
        self._InstanceId = None
        self._InstanceStatus = None
        self._SubsStatus = None
        self._ModifyTime = None
        self._CreateTime = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._ConsumeStartTime = None
        self._AutoRenewFlag = None
        self._Region = None
        self._PayType = None
        self._Vip = None
        self._Vport = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Status = None
        self._SdkConsumedTime = None
        self._Tags = None
        self._SubscribeVersion = None

    @property
    def SubscribeId(self):
        """数据订阅的实例ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """数据订阅实例的名称
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def ChannelId(self):
        """数据订阅实例绑定的通道ID。kafka版订阅就是kafka topic
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Product(self):
        """订阅实例的类型，目前支持 cynosdbmysql,mariadb,mongodb,mysql,percona,tdpg,tdsqlpercona(tdsqlmysql)
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """数据订阅实例绑定的数据库实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """云数据库状态：running 运行中，isolated 已隔离，offline 已下线。如果不是云上，此值为空
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SubsStatus(self):
        """数据订阅状态，可能的值为：未启动 notStarted, 校验中 checking, 校验不通过 checkNotPass, 校验通过 checkPass, 启动中 starting, 运行中 running, 异常出错 error
        :rtype: str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def ModifyTime(self):
        """上次修改时间，时间格式如：Y-m-d h:m:s
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

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
    def IsolateTime(self):
        """隔离时间，时间格式如：Y-m-d h:m:s
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        """包年包月任务的到期时间，时间格式如：Y-m-d h:m:s。默认：0000-00-00 00:00:00
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        """下线时间
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def ConsumeStartTime(self):
        """最近一次修改的消费时间起点，如果从未修改则为零值
        :rtype: str
        """
        return self._ConsumeStartTime

    @ConsumeStartTime.setter
    def ConsumeStartTime(self, ConsumeStartTime):
        self._ConsumeStartTime = ConsumeStartTime

    @property
    def AutoRenewFlag(self):
        """自动续费标识。只有当 PayType=0，该值才有意义。枚举值：0-不自动续费，1-自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Region(self):
        """数据订阅实例所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayType(self):
        """计费方式，0 - 包年包月，1 - 按量计费
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Vip(self):
        """旧版订阅通道的vip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """数据订阅实例的Vport
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def UniqVpcId(self):
        """数据订阅实例Vip所在VPC的唯一ID
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """数据订阅实例Vip所在子网的唯一ID
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Status(self):
        """数据订阅生命周期状态，可能的值为：正常 normal, 隔离中 isolating, 已隔离 isolated, 下线中 offlining, 按量转包年包月中 post2PrePayIng
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SdkConsumedTime(self):
        """SDK最后一条确认消息的时间戳，如果SDK一直消费，也可以作为SDK当前消费时间点
        :rtype: str
        """
        return self._SdkConsumedTime

    @SdkConsumedTime.setter
    def SdkConsumedTime(self, SdkConsumedTime):
        self._SdkConsumedTime = SdkConsumedTime

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SubscribeVersion(self):
        """订阅实例版本；txdts-旧版数据订阅,kafka-kafka版本数据订阅
        :rtype: str
        """
        return self._SubscribeVersion

    @SubscribeVersion.setter
    def SubscribeVersion(self, SubscribeVersion):
        self._SubscribeVersion = SubscribeVersion


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._ChannelId = params.get("ChannelId")
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._SubsStatus = params.get("SubsStatus")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._ConsumeStartTime = params.get("ConsumeStartTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Region = params.get("Region")
        self._PayType = params.get("PayType")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Status = params.get("Status")
        self._SdkConsumedTime = params.get("SdkConsumedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SubscribeVersion = params.get("SubscribeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeObject(AbstractModel):
    """数据订阅的对象

    """

    def __init__(self):
        r"""
        :param _ObjectsType: 数据订阅对象的类型，0-数据库，1-数据库内的表
        :type ObjectsType: int
        :param _DatabaseName: 订阅数据库的名称
        :type DatabaseName: str
        :param _TableNames: 订阅数据库中表名称数组
        :type TableNames: list of str
        """
        self._ObjectsType = None
        self._DatabaseName = None
        self._TableNames = None

    @property
    def ObjectsType(self):
        """数据订阅对象的类型，0-数据库，1-数据库内的表
        :rtype: int
        """
        return self._ObjectsType

    @ObjectsType.setter
    def ObjectsType(self, ObjectsType):
        self._ObjectsType = ObjectsType

    @property
    def DatabaseName(self):
        """订阅数据库的名称
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableNames(self):
        """订阅数据库中表名称数组
        :rtype: list of str
        """
        return self._TableNames

    @TableNames.setter
    def TableNames(self, TableNames):
        self._TableNames = TableNames


    def _deserialize(self, params):
        self._ObjectsType = params.get("ObjectsType")
        self._DatabaseName = params.get("DatabaseName")
        self._TableNames = params.get("TableNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """标签过滤

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键值
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键值
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
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
        


class TagItem(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键值
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键值
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
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
        