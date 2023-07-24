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


class Account(AbstractModel):
    """数据库账号信息

    """

    def __init__(self):
        r"""
        :param _User: 新账户的名称
        :type User: str
        :param _Host: 新账户的域名
        :type Host: str
        """
        self._User = None
        self._Host = None

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountInfo(AbstractModel):
    """账号详细信息

    """

    def __init__(self):
        r"""
        :param _Notes: 账号备注信息
        :type Notes: str
        :param _Host: 账号的域名
        :type Host: str
        :param _User: 账号的名称
        :type User: str
        :param _ModifyTime: 账号信息修改时间
        :type ModifyTime: str
        :param _ModifyPasswordTime: 修改密码的时间
        :type ModifyPasswordTime: str
        :param _CreateTime: 该值已废弃
        :type CreateTime: str
        :param _MaxUserConnections: 用户最大可用实例连接数
        :type MaxUserConnections: int
        """
        self._Notes = None
        self._Host = None
        self._User = None
        self._ModifyTime = None
        self._ModifyPasswordTime = None
        self._CreateTime = None
        self._MaxUserConnections = None

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ModifyPasswordTime(self):
        return self._ModifyPasswordTime

    @ModifyPasswordTime.setter
    def ModifyPasswordTime(self, ModifyPasswordTime):
        self._ModifyPasswordTime = ModifyPasswordTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._Notes = params.get("Notes")
        self._Host = params.get("Host")
        self._User = params.get("User")
        self._ModifyTime = params.get("ModifyTime")
        self._ModifyPasswordTime = params.get("ModifyPasswordTime")
        self._CreateTime = params.get("CreateTime")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTimeWindowRequest(AbstractModel):
    """AddTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Monday: 星期一的可维护时间段，其中每一个时间段的格式形如：10:00-12:00；起始时间按半个小时对齐；最短半个小时，最长三个小时；可设置多个时间段。 一周中应至少设置一天的时间窗。下同。
        :type Monday: list of str
        :param _Tuesday: 星期二的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Tuesday: list of str
        :param _Wednesday: 星期三的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Wednesday: list of str
        :param _Thursday: 星期四的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Thursday: list of str
        :param _Friday: 星期五的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Friday: list of str
        :param _Saturday: 星期六的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Saturday: list of str
        :param _Sunday: 星期日的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Sunday: list of str
        :param _MaxDelayTime: 最大延迟阈值，仅对主实例和灾备实例有效
        :type MaxDelayTime: int
        """
        self._InstanceId = None
        self._Monday = None
        self._Tuesday = None
        self._Wednesday = None
        self._Thursday = None
        self._Friday = None
        self._Saturday = None
        self._Sunday = None
        self._MaxDelayTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Monday(self):
        return self._Monday

    @Monday.setter
    def Monday(self, Monday):
        self._Monday = Monday

    @property
    def Tuesday(self):
        return self._Tuesday

    @Tuesday.setter
    def Tuesday(self, Tuesday):
        self._Tuesday = Tuesday

    @property
    def Wednesday(self):
        return self._Wednesday

    @Wednesday.setter
    def Wednesday(self, Wednesday):
        self._Wednesday = Wednesday

    @property
    def Thursday(self):
        return self._Thursday

    @Thursday.setter
    def Thursday(self, Thursday):
        self._Thursday = Thursday

    @property
    def Friday(self):
        return self._Friday

    @Friday.setter
    def Friday(self, Friday):
        self._Friday = Friday

    @property
    def Saturday(self):
        return self._Saturday

    @Saturday.setter
    def Saturday(self, Saturday):
        self._Saturday = Saturday

    @property
    def Sunday(self):
        return self._Sunday

    @Sunday.setter
    def Sunday(self, Sunday):
        self._Sunday = Sunday

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Monday = params.get("Monday")
        self._Tuesday = params.get("Tuesday")
        self._Wednesday = params.get("Wednesday")
        self._Thursday = params.get("Thursday")
        self._Friday = params.get("Friday")
        self._Saturday = params.get("Saturday")
        self._Sunday = params.get("Sunday")
        self._MaxDelayTime = params.get("MaxDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTimeWindowResponse(AbstractModel):
    """AddTimeWindow返回参数结构体

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


class AdjustCdbProxyAddressRequest(AbstractModel):
    """AdjustCdbProxyAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _WeightMode: 权重分配模式，
系统自动分配："system"， 自定义："custom"
        :type WeightMode: str
        :param _IsKickOut: 是否开启延迟剔除，取值："true" | "false"
        :type IsKickOut: bool
        :param _MinCount: 最小保留数量，最小取值：0
        :type MinCount: int
        :param _MaxDelay: 延迟剔除阈值，最小取值：0
        :type MaxDelay: int
        :param _FailOver: 是否开启故障转移，取值："true" | "false"
        :type FailOver: bool
        :param _AutoAddRo: 是否自动添加RO，取值："true" | "false"
        :type AutoAddRo: bool
        :param _ReadOnly: 是否是只读，取值："true" | "false"
        :type ReadOnly: bool
        :param _ProxyAddressId: 代理组地址ID
        :type ProxyAddressId: str
        :param _TransSplit: 是否开启事务分离，取值："true" | "false"
        :type TransSplit: bool
        :param _ConnectionPool: 是否开启连接池
        :type ConnectionPool: bool
        :param _ProxyAllocation: 读写权重分配。如果 WeightMode 传的是 system ，则传入的权重不生效，由系统分配默认权重。
        :type ProxyAllocation: list of ProxyAllocation
        """
        self._ProxyGroupId = None
        self._WeightMode = None
        self._IsKickOut = None
        self._MinCount = None
        self._MaxDelay = None
        self._FailOver = None
        self._AutoAddRo = None
        self._ReadOnly = None
        self._ProxyAddressId = None
        self._TransSplit = None
        self._ConnectionPool = None
        self._ProxyAllocation = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def IsKickOut(self):
        return self._IsKickOut

    @IsKickOut.setter
    def IsKickOut(self, IsKickOut):
        self._IsKickOut = IsKickOut

    @property
    def MinCount(self):
        return self._MinCount

    @MinCount.setter
    def MinCount(self, MinCount):
        self._MinCount = MinCount

    @property
    def MaxDelay(self):
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def ProxyAllocation(self):
        return self._ProxyAllocation

    @ProxyAllocation.setter
    def ProxyAllocation(self, ProxyAllocation):
        self._ProxyAllocation = ProxyAllocation


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._WeightMode = params.get("WeightMode")
        self._IsKickOut = params.get("IsKickOut")
        self._MinCount = params.get("MinCount")
        self._MaxDelay = params.get("MaxDelay")
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        self._ReadOnly = params.get("ReadOnly")
        self._ProxyAddressId = params.get("ProxyAddressId")
        self._TransSplit = params.get("TransSplit")
        self._ConnectionPool = params.get("ConnectionPool")
        if params.get("ProxyAllocation") is not None:
            self._ProxyAllocation = []
            for item in params.get("ProxyAllocation"):
                obj = ProxyAllocation()
                obj._deserialize(item)
                self._ProxyAllocation.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdjustCdbProxyAddressResponse(AbstractModel):
    """AdjustCdbProxyAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class AdjustCdbProxyRequest(AbstractModel):
    """AdjustCdbProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _ProxyNodeCustom: 节点规格配置
        :type ProxyNodeCustom: list of ProxyNodeCustom
        :param _ReloadBalance: 重新负载均衡：auto(自动),manual(手动)
        :type ReloadBalance: str
        :param _UpgradeTime: 升级切换时间：nowTime(升级完成时),timeWindow(维护时间内)
        :type UpgradeTime: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._ProxyNodeCustom = None
        self._ReloadBalance = None
        self._UpgradeTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyNodeCustom(self):
        return self._ProxyNodeCustom

    @ProxyNodeCustom.setter
    def ProxyNodeCustom(self, ProxyNodeCustom):
        self._ProxyNodeCustom = ProxyNodeCustom

    @property
    def ReloadBalance(self):
        return self._ReloadBalance

    @ReloadBalance.setter
    def ReloadBalance(self, ReloadBalance):
        self._ReloadBalance = ReloadBalance

    @property
    def UpgradeTime(self):
        return self._UpgradeTime

    @UpgradeTime.setter
    def UpgradeTime(self, UpgradeTime):
        self._UpgradeTime = UpgradeTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        if params.get("ProxyNodeCustom") is not None:
            self._ProxyNodeCustom = []
            for item in params.get("ProxyNodeCustom"):
                obj = ProxyNodeCustom()
                obj._deserialize(item)
                self._ProxyNodeCustom.append(obj)
        self._ReloadBalance = params.get("ReloadBalance")
        self._UpgradeTime = params.get("UpgradeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdjustCdbProxyResponse(AbstractModel):
    """AdjustCdbProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class AggregationCondition(AbstractModel):
    """审计日志聚合条件

    """

    def __init__(self):
        r"""
        :param _AggregationField: 聚合字段。目前仅支持host-源IP、user-用户名、dbName-数据库名、sqlType-sql类型。
        :type AggregationField: str
        :param _Offset: 偏移量。
        :type Offset: int
        :param _Limit: 该聚合字段下要返回聚合桶的数量，最大100。
        :type Limit: int
        """
        self._AggregationField = None
        self._Offset = None
        self._Limit = None

    @property
    def AggregationField(self):
        return self._AggregationField

    @AggregationField.setter
    def AggregationField(self, AggregationField):
        self._AggregationField = AggregationField

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
        self._AggregationField = params.get("AggregationField")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeAuditLogsRequest(AbstractModel):
    """AnalyzeAuditLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _StartTime: 要分析的日志开始时间，格式为："2023-02-16 00:00:20"。
        :type StartTime: str
        :param _EndTime: 要分析的日志结束时间，格式为："2023-02-16 00:10:20"。
        :type EndTime: str
        :param _AggregationConditions: 聚合维度的排序条件。
        :type AggregationConditions: list of AggregationCondition
        :param _AuditLogFilter: 已废弃。该过滤条件下的审计日志结果集作为分析日志。
        :type AuditLogFilter: :class:`tencentcloud.cdb.v20170320.models.AuditLogFilter`
        :param _LogFilter: 该过滤条件下的审计日志结果集作为分析日志。
        :type LogFilter: list of InstanceAuditLogFilters
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._AggregationConditions = None
        self._AuditLogFilter = None
        self._LogFilter = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def AggregationConditions(self):
        return self._AggregationConditions

    @AggregationConditions.setter
    def AggregationConditions(self, AggregationConditions):
        self._AggregationConditions = AggregationConditions

    @property
    def AuditLogFilter(self):
        return self._AuditLogFilter

    @AuditLogFilter.setter
    def AuditLogFilter(self, AuditLogFilter):
        self._AuditLogFilter = AuditLogFilter

    @property
    def LogFilter(self):
        return self._LogFilter

    @LogFilter.setter
    def LogFilter(self, LogFilter):
        self._LogFilter = LogFilter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("AggregationConditions") is not None:
            self._AggregationConditions = []
            for item in params.get("AggregationConditions"):
                obj = AggregationCondition()
                obj._deserialize(item)
                self._AggregationConditions.append(obj)
        if params.get("AuditLogFilter") is not None:
            self._AuditLogFilter = AuditLogFilter()
            self._AuditLogFilter._deserialize(params.get("AuditLogFilter"))
        if params.get("LogFilter") is not None:
            self._LogFilter = []
            for item in params.get("LogFilter"):
                obj = InstanceAuditLogFilters()
                obj._deserialize(item)
                self._LogFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeAuditLogsResponse(AbstractModel):
    """AnalyzeAuditLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 返回的聚合桶信息集
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditLogAggregationResult
        :param _TotalCount: 扫描的日志条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditLogAggregationResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组 ID。
        :type SecurityGroupId: str
        :param _InstanceIds: 实例 ID 列表，一个或者多个实例 ID 组成的数组。
        :type InstanceIds: list of str
        :param _ForReadonlyInstance: 当传入只读实例ID时，默认操作的是对应只读组的安全组。如果需要操作只读实例ID的安全组， 需要将该入参置为True
        :type ForReadonlyInstance: bool
        """
        self._SecurityGroupId = None
        self._InstanceIds = None
        self._ForReadonlyInstance = None

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ForReadonlyInstance(self):
        return self._ForReadonlyInstance

    @ForReadonlyInstance.setter
    def ForReadonlyInstance(self, ForReadonlyInstance):
        self._ForReadonlyInstance = ForReadonlyInstance


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        self._ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

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


class AuditFilter(AbstractModel):
    """审计规则过滤条件

    """

    def __init__(self):
        r"""
        :param _Type: 过滤条件参数名称。目前支持：
SrcIp – 客户端 IP；
User – 数据库账户；
DB – 数据库名称；
        :type Type: str
        :param _Compare: 过滤条件匹配类型。目前支持：
INC – 包含；
EXC – 不包含；
EQ – 等于；
NEQ – 不等于；
        :type Compare: str
        :param _Value: 过滤条件匹配值。
        :type Value: str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLog(AbstractModel):
    """审计日志详细信息

    """

    def __init__(self):
        r"""
        :param _AffectRows: 影响行数。
        :type AffectRows: int
        :param _ErrCode: 错误码。
        :type ErrCode: int
        :param _SqlType: SQL 类型。
        :type SqlType: str
        :param _PolicyName: 审计策略名称，逐步下线。
        :type PolicyName: str
        :param _DBName: 数据库名称。
        :type DBName: str
        :param _Sql: SQL 语句。
        :type Sql: str
        :param _Host: 客户端地址。
        :type Host: str
        :param _User: 用户名。
        :type User: str
        :param _ExecTime: 执行时间，微秒。
        :type ExecTime: int
        :param _Timestamp: 时间。
        :type Timestamp: str
        :param _SentRows: 返回行数。
        :type SentRows: int
        :param _ThreadId: 线程ID。
        :type ThreadId: int
        :param _CheckRows: 扫描行数。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRows: int
        :param _CpuTime: cpu执行时间，微秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuTime: float
        :param _IoWaitTime: IO等待时间，微秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type IoWaitTime: int
        :param _LockWaitTime: 锁等待时间，微秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type LockWaitTime: int
        :param _NsTime: 开始时间，与timestamp构成一个精确到纳秒的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type NsTime: int
        :param _TrxLivingTime: 事物持续时间，微秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type TrxLivingTime: int
        """
        self._AffectRows = None
        self._ErrCode = None
        self._SqlType = None
        self._PolicyName = None
        self._DBName = None
        self._Sql = None
        self._Host = None
        self._User = None
        self._ExecTime = None
        self._Timestamp = None
        self._SentRows = None
        self._ThreadId = None
        self._CheckRows = None
        self._CpuTime = None
        self._IoWaitTime = None
        self._LockWaitTime = None
        self._NsTime = None
        self._TrxLivingTime = None

    @property
    def AffectRows(self):
        return self._AffectRows

    @AffectRows.setter
    def AffectRows(self, AffectRows):
        self._AffectRows = AffectRows

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def SqlType(self):
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ExecTime(self):
        return self._ExecTime

    @ExecTime.setter
    def ExecTime(self, ExecTime):
        self._ExecTime = ExecTime

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SentRows(self):
        return self._SentRows

    @SentRows.setter
    def SentRows(self, SentRows):
        self._SentRows = SentRows

    @property
    def ThreadId(self):
        return self._ThreadId

    @ThreadId.setter
    def ThreadId(self, ThreadId):
        self._ThreadId = ThreadId

    @property
    def CheckRows(self):
        return self._CheckRows

    @CheckRows.setter
    def CheckRows(self, CheckRows):
        self._CheckRows = CheckRows

    @property
    def CpuTime(self):
        return self._CpuTime

    @CpuTime.setter
    def CpuTime(self, CpuTime):
        self._CpuTime = CpuTime

    @property
    def IoWaitTime(self):
        return self._IoWaitTime

    @IoWaitTime.setter
    def IoWaitTime(self, IoWaitTime):
        self._IoWaitTime = IoWaitTime

    @property
    def LockWaitTime(self):
        return self._LockWaitTime

    @LockWaitTime.setter
    def LockWaitTime(self, LockWaitTime):
        self._LockWaitTime = LockWaitTime

    @property
    def NsTime(self):
        return self._NsTime

    @NsTime.setter
    def NsTime(self, NsTime):
        self._NsTime = NsTime

    @property
    def TrxLivingTime(self):
        return self._TrxLivingTime

    @TrxLivingTime.setter
    def TrxLivingTime(self, TrxLivingTime):
        self._TrxLivingTime = TrxLivingTime


    def _deserialize(self, params):
        self._AffectRows = params.get("AffectRows")
        self._ErrCode = params.get("ErrCode")
        self._SqlType = params.get("SqlType")
        self._PolicyName = params.get("PolicyName")
        self._DBName = params.get("DBName")
        self._Sql = params.get("Sql")
        self._Host = params.get("Host")
        self._User = params.get("User")
        self._ExecTime = params.get("ExecTime")
        self._Timestamp = params.get("Timestamp")
        self._SentRows = params.get("SentRows")
        self._ThreadId = params.get("ThreadId")
        self._CheckRows = params.get("CheckRows")
        self._CpuTime = params.get("CpuTime")
        self._IoWaitTime = params.get("IoWaitTime")
        self._LockWaitTime = params.get("LockWaitTime")
        self._NsTime = params.get("NsTime")
        self._TrxLivingTime = params.get("TrxLivingTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogAggregationResult(AbstractModel):
    """审计日志分析结果

    """

    def __init__(self):
        r"""
        :param _AggregationField: 聚合维度
注意：此字段可能返回 null，表示取不到有效值。
        :type AggregationField: str
        :param _Buckets: 聚合桶的结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Buckets: list of Bucket
        """
        self._AggregationField = None
        self._Buckets = None

    @property
    def AggregationField(self):
        return self._AggregationField

    @AggregationField.setter
    def AggregationField(self, AggregationField):
        self._AggregationField = AggregationField

    @property
    def Buckets(self):
        return self._Buckets

    @Buckets.setter
    def Buckets(self, Buckets):
        self._Buckets = Buckets


    def _deserialize(self, params):
        self._AggregationField = params.get("AggregationField")
        if params.get("Buckets") is not None:
            self._Buckets = []
            for item in params.get("Buckets"):
                obj = Bucket()
                obj._deserialize(item)
                self._Buckets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFile(AbstractModel):
    """审计日志文件

    """

    def __init__(self):
        r"""
        :param _FileName: 审计日志文件名称
        :type FileName: str
        :param _CreateTime: 审计日志文件创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param _Status: 文件状态值。可能返回的值为：
"creating" - 生成中;
"failed" - 创建失败;
"success" - 已生成;
        :type Status: str
        :param _FileSize: 文件大小，单位为 KB。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _DownloadUrl: 审计日志下载地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param _ErrMsg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        """
        self._FileName = None
        self._CreateTime = None
        self._Status = None
        self._FileSize = None
        self._DownloadUrl = None
        self._ErrMsg = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._FileSize = params.get("FileSize")
        self._DownloadUrl = params.get("DownloadUrl")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFilter(AbstractModel):
    """审计日志过滤条件。查询审计日志时，用户过滤返回的审计日志。

    """

    def __init__(self):
        r"""
        :param _Host: 客户端地址。
        :type Host: list of str
        :param _User: 用户名。
        :type User: list of str
        :param _DBName: 数据库名称。
        :type DBName: list of str
        :param _TableName: 表名称。
        :type TableName: list of str
        :param _PolicyName: 审计策略名称。
        :type PolicyName: list of str
        :param _Sql: SQL 语句。支持模糊匹配。
        :type Sql: str
        :param _SqlType: SQL 类型。目前支持："SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "SET", "REPLACE", "EXECUTE"。
        :type SqlType: str
        :param _ExecTime: 执行时间。单位为：ms。表示筛选执行时间大于该值的审计日志。
        :type ExecTime: int
        :param _AffectRows: 影响行数。表示筛选影响行数大于该值的审计日志。
        :type AffectRows: int
        :param _SqlTypes: SQL 类型。支持多个类型同时查询。目前支持："SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "SET", "REPLACE", "EXECUTE"。
        :type SqlTypes: list of str
        :param _Sqls: SQL 语句。支持传递多个sql语句。
        :type Sqls: list of str
        :param _AffectRowsSection: 影响行数，格式为M-N，例如：10-200
        :type AffectRowsSection: str
        :param _SentRowsSection: 返回行数，格式为M-N，例如：10-200
        :type SentRowsSection: str
        :param _ExecTimeSection: 执行时间，格式为M-N，例如：10-200
        :type ExecTimeSection: str
        :param _LockWaitTimeSection: 锁等待时间，格式为M-N，例如：10-200
        :type LockWaitTimeSection: str
        :param _IoWaitTimeSection: IO等待时间，格式为M-N，例如：10-200
        :type IoWaitTimeSection: str
        :param _TransactionLivingTimeSection: 事务持续时间，格式为M-N，例如：10-200
        :type TransactionLivingTimeSection: str
        :param _ThreadId: 线程ID
        :type ThreadId: list of str
        :param _SentRows: 返回行数。表示筛选返回行数大于该值的审计日志。
        :type SentRows: int
        :param _ErrCode: mysql错误码
        :type ErrCode: list of int
        """
        self._Host = None
        self._User = None
        self._DBName = None
        self._TableName = None
        self._PolicyName = None
        self._Sql = None
        self._SqlType = None
        self._ExecTime = None
        self._AffectRows = None
        self._SqlTypes = None
        self._Sqls = None
        self._AffectRowsSection = None
        self._SentRowsSection = None
        self._ExecTimeSection = None
        self._LockWaitTimeSection = None
        self._IoWaitTimeSection = None
        self._TransactionLivingTimeSection = None
        self._ThreadId = None
        self._SentRows = None
        self._ErrCode = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def SqlType(self):
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def ExecTime(self):
        return self._ExecTime

    @ExecTime.setter
    def ExecTime(self, ExecTime):
        self._ExecTime = ExecTime

    @property
    def AffectRows(self):
        return self._AffectRows

    @AffectRows.setter
    def AffectRows(self, AffectRows):
        self._AffectRows = AffectRows

    @property
    def SqlTypes(self):
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Sqls(self):
        return self._Sqls

    @Sqls.setter
    def Sqls(self, Sqls):
        self._Sqls = Sqls

    @property
    def AffectRowsSection(self):
        return self._AffectRowsSection

    @AffectRowsSection.setter
    def AffectRowsSection(self, AffectRowsSection):
        self._AffectRowsSection = AffectRowsSection

    @property
    def SentRowsSection(self):
        return self._SentRowsSection

    @SentRowsSection.setter
    def SentRowsSection(self, SentRowsSection):
        self._SentRowsSection = SentRowsSection

    @property
    def ExecTimeSection(self):
        return self._ExecTimeSection

    @ExecTimeSection.setter
    def ExecTimeSection(self, ExecTimeSection):
        self._ExecTimeSection = ExecTimeSection

    @property
    def LockWaitTimeSection(self):
        return self._LockWaitTimeSection

    @LockWaitTimeSection.setter
    def LockWaitTimeSection(self, LockWaitTimeSection):
        self._LockWaitTimeSection = LockWaitTimeSection

    @property
    def IoWaitTimeSection(self):
        return self._IoWaitTimeSection

    @IoWaitTimeSection.setter
    def IoWaitTimeSection(self, IoWaitTimeSection):
        self._IoWaitTimeSection = IoWaitTimeSection

    @property
    def TransactionLivingTimeSection(self):
        return self._TransactionLivingTimeSection

    @TransactionLivingTimeSection.setter
    def TransactionLivingTimeSection(self, TransactionLivingTimeSection):
        self._TransactionLivingTimeSection = TransactionLivingTimeSection

    @property
    def ThreadId(self):
        return self._ThreadId

    @ThreadId.setter
    def ThreadId(self, ThreadId):
        self._ThreadId = ThreadId

    @property
    def SentRows(self):
        return self._SentRows

    @SentRows.setter
    def SentRows(self, SentRows):
        self._SentRows = SentRows

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._User = params.get("User")
        self._DBName = params.get("DBName")
        self._TableName = params.get("TableName")
        self._PolicyName = params.get("PolicyName")
        self._Sql = params.get("Sql")
        self._SqlType = params.get("SqlType")
        self._ExecTime = params.get("ExecTime")
        self._AffectRows = params.get("AffectRows")
        self._SqlTypes = params.get("SqlTypes")
        self._Sqls = params.get("Sqls")
        self._AffectRowsSection = params.get("AffectRowsSection")
        self._SentRowsSection = params.get("SentRowsSection")
        self._ExecTimeSection = params.get("ExecTimeSection")
        self._LockWaitTimeSection = params.get("LockWaitTimeSection")
        self._IoWaitTimeSection = params.get("IoWaitTimeSection")
        self._TransactionLivingTimeSection = params.get("TransactionLivingTimeSection")
        self._ThreadId = params.get("ThreadId")
        self._SentRows = params.get("SentRows")
        self._ErrCode = params.get("ErrCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditPolicy(AbstractModel):
    """审计策略

    """

    def __init__(self):
        r"""
        :param _PolicyId: 审计策略 ID。
        :type PolicyId: str
        :param _Status: 审计策略的状态。可能返回的值为：
"creating" - 创建中;
"running" - 运行中;
"paused" - 暂停中;
"failed" - 创建失败。
        :type Status: str
        :param _InstanceId: 数据库实例 ID。
        :type InstanceId: str
        :param _CreateTime: 审计策略创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param _ModifyTime: 审计策略最后修改时间。格式为 : "2019-03-20 17:09:13"。
        :type ModifyTime: str
        :param _PolicyName: 审计策略名称。
        :type PolicyName: str
        :param _RuleId: 审计规则 ID。
        :type RuleId: str
        :param _RuleName: 审计规则名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _InstanceName: 数据库实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        """
        self._PolicyId = None
        self._Status = None
        self._InstanceId = None
        self._CreateTime = None
        self._ModifyTime = None
        self._PolicyName = None
        self._RuleId = None
        self._RuleName = None
        self._InstanceName = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._PolicyName = params.get("PolicyName")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRule(AbstractModel):
    """审计规则

    """

    def __init__(self):
        r"""
        :param _RuleId: 审计规则 Id。
        :type RuleId: str
        :param _CreateTime: 审计规则创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param _ModifyTime: 审计规则最后修改时间。格式为 : "2019-03-20 17:09:13"。
        :type ModifyTime: str
        :param _RuleName: 审计规则名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _Description: 审计规则描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _RuleFilters: 审计规则过滤条件。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleFilters: list of AuditFilter
        :param _AuditAll: 是否开启全审计。
        :type AuditAll: bool
        """
        self._RuleId = None
        self._CreateTime = None
        self._ModifyTime = None
        self._RuleName = None
        self._Description = None
        self._RuleFilters = None
        self._AuditAll = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def AuditAll(self):
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._RuleName = params.get("RuleName")
        self._Description = params.get("Description")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = AuditFilter()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._AuditAll = params.get("AuditAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRuleFilters(AbstractModel):
    """审计规则的过滤条件

    """

    def __init__(self):
        r"""
        :param _RuleFilters: 单条审计规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleFilters: list of RuleFilters
        """
        self._RuleFilters = None

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters


    def _deserialize(self, params):
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupConfig(AbstractModel):
    """ECDB第二个从库的配置信息，只有ECDB实例才有这个字段

    """

    def __init__(self):
        r"""
        :param _ReplicationMode: 第二个从库复制方式，可能的返回值：async-异步，semisync-半同步
        :type ReplicationMode: str
        :param _Zone: 第二个从库可用区的正式名称，如ap-shanghai-1
        :type Zone: str
        :param _Vip: 第二个从库内网IP地址
        :type Vip: str
        :param _Vport: 第二个从库访问端口
        :type Vport: int
        """
        self._ReplicationMode = None
        self._Zone = None
        self._Vip = None
        self._Vport = None

    @property
    def ReplicationMode(self):
        return self._ReplicationMode

    @ReplicationMode.setter
    def ReplicationMode(self, ReplicationMode):
        self._ReplicationMode = ReplicationMode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._ReplicationMode = params.get("ReplicationMode")
        self._Zone = params.get("Zone")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    """备份详细信息

    """

    def __init__(self):
        r"""
        :param _Name: 备份文件名
        :type Name: str
        :param _Size: 备份文件大小，单位：Byte
        :type Size: int
        :param _Date: 备份快照时间，时间格式：2016-03-17 02:10:37
        :type Date: str
        :param _IntranetUrl: 下载地址
        :type IntranetUrl: str
        :param _InternetUrl: 下载地址
        :type InternetUrl: str
        :param _Type: 日志具体类型。可能的值有 "logical": 逻辑冷备， "physical": 物理冷备。
        :type Type: str
        :param _BackupId: 备份子任务的ID，删除备份文件时使用
        :type BackupId: int
        :param _Status: 备份任务状态。可能的值有 "SUCCESS": 备份成功， "FAILED": 备份失败， "RUNNING": 备份进行中。
        :type Status: str
        :param _FinishTime: 备份任务的完成时间
        :type FinishTime: str
        :param _Creator: （该值将废弃，不建议使用）备份的创建者，可能的值：SYSTEM - 系统创建，Uin - 发起者Uin值。
        :type Creator: str
        :param _StartTime: 备份任务的开始时间
        :type StartTime: str
        :param _Method: 备份方法。可能的值有 "full": 全量备份， "partial": 部分备份。
        :type Method: str
        :param _Way: 备份方式。可能的值有 "manual": 手动备份， "automatic": 自动备份。
        :type Way: str
        :param _ManualBackupName: 手动备份别名
        :type ManualBackupName: str
        :param _SaveMode: 备份保留类型，save_mode_regular - 常规保存备份，save_mode_period - 定期保存备份
        :type SaveMode: str
        :param _Region: 本地备份所在地域
        :type Region: str
        :param _RemoteInfo: 异地备份详细信息
        :type RemoteInfo: list of RemoteBackupInfo
        :param _CosStorageType: 存储方式，0-常规存储，1-归档存储，默认为0
        :type CosStorageType: int
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _EncryptionFlag: 备份文件是否加密， on-加密， off-未加密
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptionFlag: str
        """
        self._Name = None
        self._Size = None
        self._Date = None
        self._IntranetUrl = None
        self._InternetUrl = None
        self._Type = None
        self._BackupId = None
        self._Status = None
        self._FinishTime = None
        self._Creator = None
        self._StartTime = None
        self._Method = None
        self._Way = None
        self._ManualBackupName = None
        self._SaveMode = None
        self._Region = None
        self._RemoteInfo = None
        self._CosStorageType = None
        self._InstanceId = None
        self._EncryptionFlag = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def IntranetUrl(self):
        return self._IntranetUrl

    @IntranetUrl.setter
    def IntranetUrl(self, IntranetUrl):
        self._IntranetUrl = IntranetUrl

    @property
    def InternetUrl(self):
        return self._InternetUrl

    @InternetUrl.setter
    def InternetUrl(self, InternetUrl):
        self._InternetUrl = InternetUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Way(self):
        return self._Way

    @Way.setter
    def Way(self, Way):
        self._Way = Way

    @property
    def ManualBackupName(self):
        return self._ManualBackupName

    @ManualBackupName.setter
    def ManualBackupName(self, ManualBackupName):
        self._ManualBackupName = ManualBackupName

    @property
    def SaveMode(self):
        return self._SaveMode

    @SaveMode.setter
    def SaveMode(self, SaveMode):
        self._SaveMode = SaveMode

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RemoteInfo(self):
        return self._RemoteInfo

    @RemoteInfo.setter
    def RemoteInfo(self, RemoteInfo):
        self._RemoteInfo = RemoteInfo

    @property
    def CosStorageType(self):
        return self._CosStorageType

    @CosStorageType.setter
    def CosStorageType(self, CosStorageType):
        self._CosStorageType = CosStorageType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EncryptionFlag(self):
        return self._EncryptionFlag

    @EncryptionFlag.setter
    def EncryptionFlag(self, EncryptionFlag):
        self._EncryptionFlag = EncryptionFlag


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Date = params.get("Date")
        self._IntranetUrl = params.get("IntranetUrl")
        self._InternetUrl = params.get("InternetUrl")
        self._Type = params.get("Type")
        self._BackupId = params.get("BackupId")
        self._Status = params.get("Status")
        self._FinishTime = params.get("FinishTime")
        self._Creator = params.get("Creator")
        self._StartTime = params.get("StartTime")
        self._Method = params.get("Method")
        self._Way = params.get("Way")
        self._ManualBackupName = params.get("ManualBackupName")
        self._SaveMode = params.get("SaveMode")
        self._Region = params.get("Region")
        if params.get("RemoteInfo") is not None:
            self._RemoteInfo = []
            for item in params.get("RemoteInfo"):
                obj = RemoteBackupInfo()
                obj._deserialize(item)
                self._RemoteInfo.append(obj)
        self._CosStorageType = params.get("CosStorageType")
        self._InstanceId = params.get("InstanceId")
        self._EncryptionFlag = params.get("EncryptionFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupItem(AbstractModel):
    """创建备份时，指定需要备份的库表信息

    """

    def __init__(self):
        r"""
        :param _Db: 需要备份的库名
        :type Db: str
        :param _Table: 需要备份的表名。 如果传该参数，表示备份该库中的指定表。如果不传该参数则备份该db库
        :type Table: str
        """
        self._Db = None
        self._Table = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupLimitVpcItem(AbstractModel):
    """备份文件限制下载来源VPC设置项

    """

    def __init__(self):
        r"""
        :param _Region: 限制下载来源的地域。目前仅支持当前地域。
        :type Region: str
        :param _VpcList: 限制下载的vpc列表。
        :type VpcList: list of str
        """
        self._Region = None
        self._VpcList = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcList = params.get("VpcList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSummaryItem(AbstractModel):
    """实例备份统计项

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AutoBackupCount: 该实例自动数据备份的个数。
        :type AutoBackupCount: int
        :param _AutoBackupVolume: 该实例自动数据备份的容量。
        :type AutoBackupVolume: int
        :param _ManualBackupCount: 该实例手动数据备份的个数。
        :type ManualBackupCount: int
        :param _ManualBackupVolume: 该实例手动数据备份的容量。
        :type ManualBackupVolume: int
        :param _DataBackupCount: 该实例总的数据备份（包含自动备份和手动备份）个数。
        :type DataBackupCount: int
        :param _DataBackupVolume: 该实例总的数据备份容量。
        :type DataBackupVolume: int
        :param _BinlogBackupCount: 该实例日志备份的个数。
        :type BinlogBackupCount: int
        :param _BinlogBackupVolume: 该实例日志备份的容量。
        :type BinlogBackupVolume: int
        :param _BackupVolume: 该实例的总备份（包含数据备份和日志备份）占用容量。
        :type BackupVolume: int
        """
        self._InstanceId = None
        self._AutoBackupCount = None
        self._AutoBackupVolume = None
        self._ManualBackupCount = None
        self._ManualBackupVolume = None
        self._DataBackupCount = None
        self._DataBackupVolume = None
        self._BinlogBackupCount = None
        self._BinlogBackupVolume = None
        self._BackupVolume = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoBackupCount(self):
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def AutoBackupVolume(self):
        return self._AutoBackupVolume

    @AutoBackupVolume.setter
    def AutoBackupVolume(self, AutoBackupVolume):
        self._AutoBackupVolume = AutoBackupVolume

    @property
    def ManualBackupCount(self):
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def ManualBackupVolume(self):
        return self._ManualBackupVolume

    @ManualBackupVolume.setter
    def ManualBackupVolume(self, ManualBackupVolume):
        self._ManualBackupVolume = ManualBackupVolume

    @property
    def DataBackupCount(self):
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def DataBackupVolume(self):
        return self._DataBackupVolume

    @DataBackupVolume.setter
    def DataBackupVolume(self, DataBackupVolume):
        self._DataBackupVolume = DataBackupVolume

    @property
    def BinlogBackupCount(self):
        return self._BinlogBackupCount

    @BinlogBackupCount.setter
    def BinlogBackupCount(self, BinlogBackupCount):
        self._BinlogBackupCount = BinlogBackupCount

    @property
    def BinlogBackupVolume(self):
        return self._BinlogBackupVolume

    @BinlogBackupVolume.setter
    def BinlogBackupVolume(self, BinlogBackupVolume):
        self._BinlogBackupVolume = BinlogBackupVolume

    @property
    def BackupVolume(self):
        return self._BackupVolume

    @BackupVolume.setter
    def BackupVolume(self, BackupVolume):
        self._BackupVolume = BackupVolume


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._AutoBackupVolume = params.get("AutoBackupVolume")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._ManualBackupVolume = params.get("ManualBackupVolume")
        self._DataBackupCount = params.get("DataBackupCount")
        self._DataBackupVolume = params.get("DataBackupVolume")
        self._BinlogBackupCount = params.get("BinlogBackupCount")
        self._BinlogBackupVolume = params.get("BinlogBackupVolume")
        self._BackupVolume = params.get("BackupVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceRoGroupLoadRequest(AbstractModel):
    """BalanceRoGroupLoad请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoGroupId: RO 组的 ID，格式如：cdbrg-c1nl9rpv。
        :type RoGroupId: str
        """
        self._RoGroupId = None

    @property
    def RoGroupId(self):
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId


    def _deserialize(self, params):
        self._RoGroupId = params.get("RoGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceRoGroupLoadResponse(AbstractModel):
    """BalanceRoGroupLoad返回参数结构体

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


class BinlogInfo(AbstractModel):
    """二进制日志信息

    """

    def __init__(self):
        r"""
        :param _Name: binlog 日志备份文件名
        :type Name: str
        :param _Size: 备份文件大小，单位：Byte
        :type Size: int
        :param _Date: 文件存储时间，时间格式：2016-03-17 02:10:37
        :type Date: str
        :param _IntranetUrl: 下载地址
        :type IntranetUrl: str
        :param _InternetUrl: 下载地址
        :type InternetUrl: str
        :param _Type: 日志具体类型，可能的值有：binlog - 二进制日志
        :type Type: str
        :param _BinlogStartTime: binlog 文件起始时间
        :type BinlogStartTime: str
        :param _BinlogFinishTime: binlog 文件截止时间
        :type BinlogFinishTime: str
        :param _Region: 本地binlog文件所在地域
        :type Region: str
        :param _Status: 备份任务状态。可能的值有 "SUCCESS": 备份成功， "FAILED": 备份失败， "RUNNING": 备份进行中。
        :type Status: str
        :param _RemoteInfo: binlog异地备份详细信息
        :type RemoteInfo: list of RemoteBackupInfo
        :param _CosStorageType: 存储方式，0-常规存储，1-归档存储，默认为0
        :type CosStorageType: int
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._Name = None
        self._Size = None
        self._Date = None
        self._IntranetUrl = None
        self._InternetUrl = None
        self._Type = None
        self._BinlogStartTime = None
        self._BinlogFinishTime = None
        self._Region = None
        self._Status = None
        self._RemoteInfo = None
        self._CosStorageType = None
        self._InstanceId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def IntranetUrl(self):
        return self._IntranetUrl

    @IntranetUrl.setter
    def IntranetUrl(self, IntranetUrl):
        self._IntranetUrl = IntranetUrl

    @property
    def InternetUrl(self):
        return self._InternetUrl

    @InternetUrl.setter
    def InternetUrl(self, InternetUrl):
        self._InternetUrl = InternetUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BinlogStartTime(self):
        return self._BinlogStartTime

    @BinlogStartTime.setter
    def BinlogStartTime(self, BinlogStartTime):
        self._BinlogStartTime = BinlogStartTime

    @property
    def BinlogFinishTime(self):
        return self._BinlogFinishTime

    @BinlogFinishTime.setter
    def BinlogFinishTime(self, BinlogFinishTime):
        self._BinlogFinishTime = BinlogFinishTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RemoteInfo(self):
        return self._RemoteInfo

    @RemoteInfo.setter
    def RemoteInfo(self, RemoteInfo):
        self._RemoteInfo = RemoteInfo

    @property
    def CosStorageType(self):
        return self._CosStorageType

    @CosStorageType.setter
    def CosStorageType(self, CosStorageType):
        self._CosStorageType = CosStorageType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Date = params.get("Date")
        self._IntranetUrl = params.get("IntranetUrl")
        self._InternetUrl = params.get("InternetUrl")
        self._Type = params.get("Type")
        self._BinlogStartTime = params.get("BinlogStartTime")
        self._BinlogFinishTime = params.get("BinlogFinishTime")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        if params.get("RemoteInfo") is not None:
            self._RemoteInfo = []
            for item in params.get("RemoteInfo"):
                obj = RemoteBackupInfo()
                obj._deserialize(item)
                self._RemoteInfo.append(obj)
        self._CosStorageType = params.get("CosStorageType")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bucket(AbstractModel):
    """聚合桶的信息

    """

    def __init__(self):
        r"""
        :param _Key: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Count: key值出现的次数。
        :type Count: int
        """
        self._Key = None
        self._Count = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbRegionSellConf(AbstractModel):
    """地域售卖配置

    """

    def __init__(self):
        r"""
        :param _RegionName: 地域中文名称
        :type RegionName: str
        :param _Area: 所属大区
        :type Area: str
        :param _IsDefaultRegion: 是否为默认地域
        :type IsDefaultRegion: int
        :param _Region: 地域名称
        :type Region: str
        :param _RegionConfig: 地域的可用区售卖配置
        :type RegionConfig: list of CdbZoneSellConf
        """
        self._RegionName = None
        self._Area = None
        self._IsDefaultRegion = None
        self._Region = None
        self._RegionConfig = None

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def IsDefaultRegion(self):
        return self._IsDefaultRegion

    @IsDefaultRegion.setter
    def IsDefaultRegion(self, IsDefaultRegion):
        self._IsDefaultRegion = IsDefaultRegion

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionConfig(self):
        return self._RegionConfig

    @RegionConfig.setter
    def RegionConfig(self, RegionConfig):
        self._RegionConfig = RegionConfig


    def _deserialize(self, params):
        self._RegionName = params.get("RegionName")
        self._Area = params.get("Area")
        self._IsDefaultRegion = params.get("IsDefaultRegion")
        self._Region = params.get("Region")
        if params.get("RegionConfig") is not None:
            self._RegionConfig = []
            for item in params.get("RegionConfig"):
                obj = CdbZoneSellConf()
                obj._deserialize(item)
                self._RegionConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbSellConfig(AbstractModel):
    """售卖配置详情

    """

    def __init__(self):
        r"""
        :param _Memory: 内存大小，单位为MB
        :type Memory: int
        :param _Cpu: CPU核心数
        :type Cpu: int
        :param _VolumeMin: 磁盘最小规格，单位为GB
        :type VolumeMin: int
        :param _VolumeMax: 磁盘最大规格，单位为GB
        :type VolumeMax: int
        :param _VolumeStep: 磁盘步长，单位为GB
        :type VolumeStep: int
        :param _Iops: 每秒IO数量
        :type Iops: int
        :param _Info: 应用场景描述
        :type Info: str
        :param _Status: 状态值，0 表示该规格对外售卖
        :type Status: int
        :param _DeviceType: 实例类型，可能的取值范围有：UNIVERSAL (通用型), EXCLUSIVE (独享型), BASIC (基础型), BASIC_V2 (基础型v2)
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param _EngineType: 引擎类型描述，可能的取值范围有：Innodb，RocksDB
        :type EngineType: str
        :param _Id: 售卖规格Id
        :type Id: int
        """
        self._Memory = None
        self._Cpu = None
        self._VolumeMin = None
        self._VolumeMax = None
        self._VolumeStep = None
        self._Iops = None
        self._Info = None
        self._Status = None
        self._DeviceType = None
        self._EngineType = None
        self._Id = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def VolumeMin(self):
        return self._VolumeMin

    @VolumeMin.setter
    def VolumeMin(self, VolumeMin):
        self._VolumeMin = VolumeMin

    @property
    def VolumeMax(self):
        return self._VolumeMax

    @VolumeMax.setter
    def VolumeMax(self, VolumeMax):
        self._VolumeMax = VolumeMax

    @property
    def VolumeStep(self):
        return self._VolumeStep

    @VolumeStep.setter
    def VolumeStep(self, VolumeStep):
        self._VolumeStep = VolumeStep

    @property
    def Iops(self):
        return self._Iops

    @Iops.setter
    def Iops(self, Iops):
        self._Iops = Iops

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Cpu = params.get("Cpu")
        self._VolumeMin = params.get("VolumeMin")
        self._VolumeMax = params.get("VolumeMax")
        self._VolumeStep = params.get("VolumeStep")
        self._Iops = params.get("Iops")
        self._Info = params.get("Info")
        self._Status = params.get("Status")
        self._DeviceType = params.get("DeviceType")
        self._EngineType = params.get("EngineType")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbSellType(AbstractModel):
    """售卖实例类型

    """

    def __init__(self):
        r"""
        :param _TypeName: 售卖实例名称。Z3是高可用类型对应规格中的DeviceType包含UNIVERSAL,EXCLUSIVE；CVM是基础版类型对应规格中的DeviceType是BASIC；TKE是基础型v2类型对应规格中的DeviceType是BASIC_V2。
        :type TypeName: str
        :param _EngineVersion: 引擎版本号
        :type EngineVersion: list of str
        :param _ConfigIds: 售卖规格Id
        :type ConfigIds: list of int
        """
        self._TypeName = None
        self._EngineVersion = None
        self._ConfigIds = None

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def ConfigIds(self):
        return self._ConfigIds

    @ConfigIds.setter
    def ConfigIds(self, ConfigIds):
        self._ConfigIds = ConfigIds


    def _deserialize(self, params):
        self._TypeName = params.get("TypeName")
        self._EngineVersion = params.get("EngineVersion")
        self._ConfigIds = params.get("ConfigIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbZoneDataResult(AbstractModel):
    """各地域可售卖的规格配置

    """

    def __init__(self):
        r"""
        :param _Configs: 售卖规格所有集合
        :type Configs: list of CdbSellConfig
        :param _Regions: 售卖地域可用区集合
        :type Regions: list of CdbRegionSellConf
        """
        self._Configs = None
        self._Regions = None

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = CdbSellConfig()
                obj._deserialize(item)
                self._Configs.append(obj)
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = CdbRegionSellConf()
                obj._deserialize(item)
                self._Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbZoneSellConf(AbstractModel):
    """可用区售卖配置

    """

    def __init__(self):
        r"""
        :param _Status: 可用区状态。可能的返回值为：1-上线；3-停售；4-不展示
        :type Status: int
        :param _ZoneName: 可用区中文名称
        :type ZoneName: str
        :param _IsCustom: 实例类型是否为自定义类型
        :type IsCustom: bool
        :param _IsSupportDr: 是否支持灾备
        :type IsSupportDr: bool
        :param _IsSupportVpc: 是否支持私有网络
        :type IsSupportVpc: bool
        :param _HourInstanceSaleMaxNum: 小时计费实例最大售卖数量
        :type HourInstanceSaleMaxNum: int
        :param _IsDefaultZone: 是否为默认可用区
        :type IsDefaultZone: bool
        :param _IsBm: 是否为黑石区
        :type IsBm: bool
        :param _PayType: 支持的付费类型。可能的返回值为：0-包年包月；1-小时计费；2-后付费
        :type PayType: list of str
        :param _ProtectMode: 数据复制类型。0-异步复制；1-半同步复制；2-强同步复制
        :type ProtectMode: list of str
        :param _Zone: 可用区名称
        :type Zone: str
        :param _ZoneConf: 多可用区信息
        :type ZoneConf: :class:`tencentcloud.cdb.v20170320.models.ZoneConf`
        :param _DrZone: 可支持的灾备可用区信息
        :type DrZone: list of str
        :param _IsSupportRemoteRo: 是否支持跨可用区只读
        :type IsSupportRemoteRo: bool
        :param _RemoteRoZone: 可支持的跨可用区只读区信息
        :type RemoteRoZone: list of str
        :param _ExClusterStatus: 独享型可用区状态。可能的返回值为：1-上线；3-停售；4-不展示
        :type ExClusterStatus: int
        :param _ExClusterRemoteRoZone: 独享型可支持的跨可用区只读区信息
        :type ExClusterRemoteRoZone: list of str
        :param _ExClusterZoneConf: 独享型多可用区信息
        :type ExClusterZoneConf: :class:`tencentcloud.cdb.v20170320.models.ZoneConf`
        :param _SellType: 售卖实例类型数组，其中configIds的值与configs结构体中的id一一对应。
        :type SellType: list of CdbSellType
        :param _ZoneId: 可用区id
        :type ZoneId: int
        :param _IsSupportIpv6: 是否支持ipv6
        :type IsSupportIpv6: bool
        :param _EngineType: 可支持的售卖数据库引擎类型
        :type EngineType: list of str
        """
        self._Status = None
        self._ZoneName = None
        self._IsCustom = None
        self._IsSupportDr = None
        self._IsSupportVpc = None
        self._HourInstanceSaleMaxNum = None
        self._IsDefaultZone = None
        self._IsBm = None
        self._PayType = None
        self._ProtectMode = None
        self._Zone = None
        self._ZoneConf = None
        self._DrZone = None
        self._IsSupportRemoteRo = None
        self._RemoteRoZone = None
        self._ExClusterStatus = None
        self._ExClusterRemoteRoZone = None
        self._ExClusterZoneConf = None
        self._SellType = None
        self._ZoneId = None
        self._IsSupportIpv6 = None
        self._EngineType = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def IsCustom(self):
        return self._IsCustom

    @IsCustom.setter
    def IsCustom(self, IsCustom):
        self._IsCustom = IsCustom

    @property
    def IsSupportDr(self):
        return self._IsSupportDr

    @IsSupportDr.setter
    def IsSupportDr(self, IsSupportDr):
        self._IsSupportDr = IsSupportDr

    @property
    def IsSupportVpc(self):
        return self._IsSupportVpc

    @IsSupportVpc.setter
    def IsSupportVpc(self, IsSupportVpc):
        self._IsSupportVpc = IsSupportVpc

    @property
    def HourInstanceSaleMaxNum(self):
        return self._HourInstanceSaleMaxNum

    @HourInstanceSaleMaxNum.setter
    def HourInstanceSaleMaxNum(self, HourInstanceSaleMaxNum):
        self._HourInstanceSaleMaxNum = HourInstanceSaleMaxNum

    @property
    def IsDefaultZone(self):
        return self._IsDefaultZone

    @IsDefaultZone.setter
    def IsDefaultZone(self, IsDefaultZone):
        self._IsDefaultZone = IsDefaultZone

    @property
    def IsBm(self):
        return self._IsBm

    @IsBm.setter
    def IsBm(self, IsBm):
        self._IsBm = IsBm

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneConf(self):
        return self._ZoneConf

    @ZoneConf.setter
    def ZoneConf(self, ZoneConf):
        self._ZoneConf = ZoneConf

    @property
    def DrZone(self):
        return self._DrZone

    @DrZone.setter
    def DrZone(self, DrZone):
        self._DrZone = DrZone

    @property
    def IsSupportRemoteRo(self):
        return self._IsSupportRemoteRo

    @IsSupportRemoteRo.setter
    def IsSupportRemoteRo(self, IsSupportRemoteRo):
        self._IsSupportRemoteRo = IsSupportRemoteRo

    @property
    def RemoteRoZone(self):
        return self._RemoteRoZone

    @RemoteRoZone.setter
    def RemoteRoZone(self, RemoteRoZone):
        self._RemoteRoZone = RemoteRoZone

    @property
    def ExClusterStatus(self):
        return self._ExClusterStatus

    @ExClusterStatus.setter
    def ExClusterStatus(self, ExClusterStatus):
        self._ExClusterStatus = ExClusterStatus

    @property
    def ExClusterRemoteRoZone(self):
        return self._ExClusterRemoteRoZone

    @ExClusterRemoteRoZone.setter
    def ExClusterRemoteRoZone(self, ExClusterRemoteRoZone):
        self._ExClusterRemoteRoZone = ExClusterRemoteRoZone

    @property
    def ExClusterZoneConf(self):
        return self._ExClusterZoneConf

    @ExClusterZoneConf.setter
    def ExClusterZoneConf(self, ExClusterZoneConf):
        self._ExClusterZoneConf = ExClusterZoneConf

    @property
    def SellType(self):
        return self._SellType

    @SellType.setter
    def SellType(self, SellType):
        self._SellType = SellType

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsSupportIpv6(self):
        return self._IsSupportIpv6

    @IsSupportIpv6.setter
    def IsSupportIpv6(self, IsSupportIpv6):
        self._IsSupportIpv6 = IsSupportIpv6

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ZoneName = params.get("ZoneName")
        self._IsCustom = params.get("IsCustom")
        self._IsSupportDr = params.get("IsSupportDr")
        self._IsSupportVpc = params.get("IsSupportVpc")
        self._HourInstanceSaleMaxNum = params.get("HourInstanceSaleMaxNum")
        self._IsDefaultZone = params.get("IsDefaultZone")
        self._IsBm = params.get("IsBm")
        self._PayType = params.get("PayType")
        self._ProtectMode = params.get("ProtectMode")
        self._Zone = params.get("Zone")
        if params.get("ZoneConf") is not None:
            self._ZoneConf = ZoneConf()
            self._ZoneConf._deserialize(params.get("ZoneConf"))
        self._DrZone = params.get("DrZone")
        self._IsSupportRemoteRo = params.get("IsSupportRemoteRo")
        self._RemoteRoZone = params.get("RemoteRoZone")
        self._ExClusterStatus = params.get("ExClusterStatus")
        self._ExClusterRemoteRoZone = params.get("ExClusterRemoteRoZone")
        if params.get("ExClusterZoneConf") is not None:
            self._ExClusterZoneConf = ZoneConf()
            self._ExClusterZoneConf._deserialize(params.get("ExClusterZoneConf"))
        if params.get("SellType") is not None:
            self._SellType = []
            for item in params.get("SellType"):
                obj = CdbSellType()
                obj._deserialize(item)
                self._SellType.append(obj)
        self._ZoneId = params.get("ZoneId")
        self._IsSupportIpv6 = params.get("IsSupportIpv6")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneItem(AbstractModel):
    """克隆任务记录。

    """

    def __init__(self):
        r"""
        :param _SrcInstanceId: 克隆任务的源实例Id。
        :type SrcInstanceId: str
        :param _DstInstanceId: 克隆任务的新产生实例Id。
        :type DstInstanceId: str
        :param _CloneJobId: 克隆任务对应的任务列表Id。
        :type CloneJobId: int
        :param _RollbackStrategy: 克隆实例使用的策略， 包括以下类型：  timepoint:指定时间点回档，  backupset: 指定备份文件回档。
        :type RollbackStrategy: str
        :param _RollbackTargetTime: 克隆实例回档的时间点。
        :type RollbackTargetTime: str
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _EndTime: 任务结束时间。
        :type EndTime: str
        :param _TaskStatus: 任务状态，包括以下状态：initial,running,wait_complete,success,failed
        :type TaskStatus: str
        :param _NewRegionId: 克隆实例所在地域Id
        :type NewRegionId: int
        :param _SrcRegionId: 源实例所在地域Id
        :type SrcRegionId: int
        """
        self._SrcInstanceId = None
        self._DstInstanceId = None
        self._CloneJobId = None
        self._RollbackStrategy = None
        self._RollbackTargetTime = None
        self._StartTime = None
        self._EndTime = None
        self._TaskStatus = None
        self._NewRegionId = None
        self._SrcRegionId = None

    @property
    def SrcInstanceId(self):
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def DstInstanceId(self):
        return self._DstInstanceId

    @DstInstanceId.setter
    def DstInstanceId(self, DstInstanceId):
        self._DstInstanceId = DstInstanceId

    @property
    def CloneJobId(self):
        return self._CloneJobId

    @CloneJobId.setter
    def CloneJobId(self, CloneJobId):
        self._CloneJobId = CloneJobId

    @property
    def RollbackStrategy(self):
        return self._RollbackStrategy

    @RollbackStrategy.setter
    def RollbackStrategy(self, RollbackStrategy):
        self._RollbackStrategy = RollbackStrategy

    @property
    def RollbackTargetTime(self):
        return self._RollbackTargetTime

    @RollbackTargetTime.setter
    def RollbackTargetTime(self, RollbackTargetTime):
        self._RollbackTargetTime = RollbackTargetTime

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
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def NewRegionId(self):
        return self._NewRegionId

    @NewRegionId.setter
    def NewRegionId(self, NewRegionId):
        self._NewRegionId = NewRegionId

    @property
    def SrcRegionId(self):
        return self._SrcRegionId

    @SrcRegionId.setter
    def SrcRegionId(self, SrcRegionId):
        self._SrcRegionId = SrcRegionId


    def _deserialize(self, params):
        self._SrcInstanceId = params.get("SrcInstanceId")
        self._DstInstanceId = params.get("DstInstanceId")
        self._CloneJobId = params.get("CloneJobId")
        self._RollbackStrategy = params.get("RollbackStrategy")
        self._RollbackTargetTime = params.get("RollbackTargetTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskStatus = params.get("TaskStatus")
        self._NewRegionId = params.get("NewRegionId")
        self._SrcRegionId = params.get("SrcRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCDBProxyRequest(AbstractModel):
    """CloseCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _OnlyCloseRW: 是否只关闭读写分离，取值："true" | "false"，默认为"false"
        :type OnlyCloseRW: bool
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._OnlyCloseRW = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def OnlyCloseRW(self):
        return self._OnlyCloseRW

    @OnlyCloseRW.setter
    def OnlyCloseRW(self, OnlyCloseRW):
        self._OnlyCloseRW = OnlyCloseRW


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._OnlyCloseRW = params.get("OnlyCloseRW")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCDBProxyResponse(AbstractModel):
    """CloseCDBProxy返回参数结构体

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


class CloseCdbProxyAddressRequest(AbstractModel):
    """CloseCdbProxyAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _ProxyAddressId: 代理组地址ID
        :type ProxyAddressId: str
        """
        self._ProxyGroupId = None
        self._ProxyAddressId = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyAddressId = params.get("ProxyAddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCdbProxyAddressResponse(AbstractModel):
    """CloseCdbProxyAddress返回参数结构体

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


class CloseWanServiceRequest(AbstractModel):
    """CloseWanService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWanServiceResponse(AbstractModel):
    """CloseWanService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """列权限信息

    """

    def __init__(self):
        r"""
        :param _Database: 数据库名
        :type Database: str
        :param _Table: 数据库表名
        :type Table: str
        :param _Column: 数据库列名
        :type Column: str
        :param _Privileges: 权限信息
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Column = None
        self._Privileges = None

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
    def Column(self):
        return self._Column

    @Column.setter
    def Column(self, Column):
        self._Column = Column

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Column = params.get("Column")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonTimeWindow(AbstractModel):
    """通用时间窗

    """

    def __init__(self):
        r"""
        :param _Monday: 周一的时间窗，格式如： 02:00-06:00
        :type Monday: str
        :param _Tuesday: 周二的时间窗，格式如： 02:00-06:00
        :type Tuesday: str
        :param _Wednesday: 周三的时间窗，格式如： 02:00-06:00
        :type Wednesday: str
        :param _Thursday: 周四的时间窗，格式如： 02:00-06:00
        :type Thursday: str
        :param _Friday: 周五的时间窗，格式如： 02:00-06:00
        :type Friday: str
        :param _Saturday: 周六的时间窗，格式如： 02:00-06:00
        :type Saturday: str
        :param _Sunday: 周日的时间窗，格式如： 02:00-06:00
        :type Sunday: str
        :param _BackupPeriodStrategy: 常规备份保留策略，weekly-按周备份，monthly-按月备份，默认为weekly
        :type BackupPeriodStrategy: str
        :param _Days: 如果设置为按月备份，需填入每月具体备份日期，相邻备份天数不得超过两天。例[1,4,7,9,11,14,17,19,22,25,28,30,31]
        :type Days: list of int
        :param _BackupPeriodTime: 月度备份时间窗，BackupPeriodStrategy为monthly时必填。格式如： 02:00-06:00
        :type BackupPeriodTime: str
        """
        self._Monday = None
        self._Tuesday = None
        self._Wednesday = None
        self._Thursday = None
        self._Friday = None
        self._Saturday = None
        self._Sunday = None
        self._BackupPeriodStrategy = None
        self._Days = None
        self._BackupPeriodTime = None

    @property
    def Monday(self):
        return self._Monday

    @Monday.setter
    def Monday(self, Monday):
        self._Monday = Monday

    @property
    def Tuesday(self):
        return self._Tuesday

    @Tuesday.setter
    def Tuesday(self, Tuesday):
        self._Tuesday = Tuesday

    @property
    def Wednesday(self):
        return self._Wednesday

    @Wednesday.setter
    def Wednesday(self, Wednesday):
        self._Wednesday = Wednesday

    @property
    def Thursday(self):
        return self._Thursday

    @Thursday.setter
    def Thursday(self, Thursday):
        self._Thursday = Thursday

    @property
    def Friday(self):
        return self._Friday

    @Friday.setter
    def Friday(self, Friday):
        self._Friday = Friday

    @property
    def Saturday(self):
        return self._Saturday

    @Saturday.setter
    def Saturday(self, Saturday):
        self._Saturday = Saturday

    @property
    def Sunday(self):
        return self._Sunday

    @Sunday.setter
    def Sunday(self, Sunday):
        self._Sunday = Sunday

    @property
    def BackupPeriodStrategy(self):
        return self._BackupPeriodStrategy

    @BackupPeriodStrategy.setter
    def BackupPeriodStrategy(self, BackupPeriodStrategy):
        self._BackupPeriodStrategy = BackupPeriodStrategy

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def BackupPeriodTime(self):
        return self._BackupPeriodTime

    @BackupPeriodTime.setter
    def BackupPeriodTime(self, BackupPeriodTime):
        self._BackupPeriodTime = BackupPeriodTime


    def _deserialize(self, params):
        self._Monday = params.get("Monday")
        self._Tuesday = params.get("Tuesday")
        self._Wednesday = params.get("Wednesday")
        self._Thursday = params.get("Thursday")
        self._Friday = params.get("Friday")
        self._Saturday = params.get("Saturday")
        self._Sunday = params.get("Sunday")
        self._BackupPeriodStrategy = params.get("BackupPeriodStrategy")
        self._Days = params.get("Days")
        self._BackupPeriodTime = params.get("BackupPeriodTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Accounts: 云数据库账号。
        :type Accounts: list of Account
        :param _Password: 新账户的密码。
        :type Password: str
        :param _Description: 备注信息。
        :type Description: str
        :param _MaxUserConnections: 新账户最大可用连接数，默认值为10240，最大可设置值为10240。
        :type MaxUserConnections: int
        """
        self._InstanceId = None
        self._Accounts = None
        self._Password = None
        self._Description = None
        self._MaxUserConnections = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateAuditLogFileRequest(AbstractModel):
    """CreateAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _Order: 排序方式。支持值包括："ASC" - 升序，"DESC" - 降序。
        :type Order: str
        :param _OrderBy: 排序字段。支持值包括：
"timestamp" - 时间戳；
"affectRows" - 影响行数；
"execTime" - 执行时间。
        :type OrderBy: str
        :param _Filter: 已废弃。
        :type Filter: :class:`tencentcloud.cdb.v20170320.models.AuditLogFilter`
        :param _LogFilter: 过滤条件。可按设置的过滤条件过滤日志。
        :type LogFilter: list of InstanceAuditLogFilters
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._OrderBy = None
        self._Filter = None
        self._LogFilter = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def LogFilter(self):
        return self._LogFilter

    @LogFilter.setter
    def LogFilter(self, LogFilter):
        self._LogFilter = LogFilter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self._Filter = AuditLogFilter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("LogFilter") is not None:
            self._LogFilter = []
            for item in params.get("LogFilter"):
                obj = InstanceAuditLogFilters()
                obj._deserialize(item)
                self._LogFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditLogFileResponse(AbstractModel):
    """CreateAuditLogFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileName: 审计日志文件名称。
        :type FileName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileName = None
        self._RequestId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._RequestId = params.get("RequestId")


class CreateAuditPolicyRequest(AbstractModel):
    """CreateAuditPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 审计策略名称。
        :type Name: str
        :param _RuleId: 审计规则 ID。
        :type RuleId: str
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _LogExpireDay: 审计日志保存时长。支持值包括：
7 - 一周
30 - 一个月；
180 - 六个月；
365 - 一年；
1095 - 三年；
1825 - 五年；
实例首次开通审计策略时，可传该值，用于设置存储日志保存天数，默认为 30 天。若实例已存在审计策略，则此参数无效，可使用 更改审计服务配置 接口修改日志存储时长。
        :type LogExpireDay: int
        """
        self._Name = None
        self._RuleId = None
        self._InstanceId = None
        self._LogExpireDay = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RuleId = params.get("RuleId")
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditPolicyResponse(AbstractModel):
    """CreateAuditPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 审计策略 ID。
        :type PolicyId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateAuditRuleRequest(AbstractModel):
    """CreateAuditRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 审计规则名称。
        :type RuleName: str
        :param _Description: 审计规则描述。
        :type Description: str
        :param _RuleFilters: 审计规则过滤条件。若设置了过滤条件，则不会开启全审计。
        :type RuleFilters: list of AuditFilter
        :param _AuditAll: 是否开启全审计。支持值包括：false – 不开启全审计，true – 开启全审计。用户未设置审计规则过滤条件时，默认开启全审计。
        :type AuditAll: bool
        """
        self._RuleName = None
        self._Description = None
        self._RuleFilters = None
        self._AuditAll = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def AuditAll(self):
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Description = params.get("Description")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = AuditFilter()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._AuditAll = params.get("AuditAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRuleResponse(AbstractModel):
    """CreateAuditRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 审计规则 ID。
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _BackupMethod: 目标备份方法，可选的值：logical - 逻辑冷备，physical - 物理冷备，snapshot - 快照备份。基础版实例仅支持快照备份。
        :type BackupMethod: str
        :param _BackupDBTableList: 需要备份的库表信息，如果不设置该参数，则默认整实例备份。在 BackupMethod=logical 逻辑备份中才可设置该参数。指定的库表必须存在，否则可能导致备份失败。
例：如果需要备份 db1 库的 tb1、tb2 表 和 db2 库。则该参数设置为 [{"Db": "db1", "Table": "tb1"}, {"Db": "db1", "Table": "tb2"}, {"Db": "db2"} ]。
        :type BackupDBTableList: list of BackupItem
        :param _ManualBackupName: 手动备份别名
        :type ManualBackupName: str
        """
        self._InstanceId = None
        self._BackupMethod = None
        self._BackupDBTableList = None
        self._ManualBackupName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupDBTableList(self):
        return self._BackupDBTableList

    @BackupDBTableList.setter
    def BackupDBTableList(self, BackupDBTableList):
        self._BackupDBTableList = BackupDBTableList

    @property
    def ManualBackupName(self):
        return self._ManualBackupName

    @ManualBackupName.setter
    def ManualBackupName(self, ManualBackupName):
        self._ManualBackupName = ManualBackupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMethod = params.get("BackupMethod")
        if params.get("BackupDBTableList") is not None:
            self._BackupDBTableList = []
            for item in params.get("BackupDBTableList"):
                obj = BackupItem()
                obj._deserialize(item)
                self._BackupDBTableList.append(obj)
        self._ManualBackupName = params.get("ManualBackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份任务 ID。
        :type BackupId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupId = None
        self._RequestId = None

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._RequestId = params.get("RequestId")


class CreateCdbProxyAddressRequest(AbstractModel):
    """CreateCdbProxyAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _WeightMode: 权重分配模式，
系统自动分配："system"， 自定义："custom"
        :type WeightMode: str
        :param _IsKickOut: 是否开启延迟剔除，取值："true" | "false"
        :type IsKickOut: bool
        :param _MinCount: 最小保留数量，最小取值：0
        :type MinCount: int
        :param _MaxDelay: 延迟剔除阈值，最小取值：0
        :type MaxDelay: int
        :param _FailOver: 是否开启故障转移，取值："true" | "false"
        :type FailOver: bool
        :param _AutoAddRo: 是否自动添加RO，取值："true" | "false"
        :type AutoAddRo: bool
        :param _ReadOnly: 是否是只读，取值："true" | "false"
        :type ReadOnly: bool
        :param _TransSplit: 是否开启事务分离，取值："true" | "false"
        :type TransSplit: bool
        :param _ProxyAllocation: 读写权重分配
        :type ProxyAllocation: list of ProxyAllocation
        :param _UniqVpcId: 私有网络ID
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有子网ID
        :type UniqSubnetId: str
        :param _ConnectionPool: 是否开启连接池
        :type ConnectionPool: bool
        :param _Desc: 描述
        :type Desc: str
        :param _Vip: IP地址
        :type Vip: str
        :param _VPort: 端口
        :type VPort: int
        :param _SecurityGroup: 安全组
        :type SecurityGroup: list of str
        :param _ConnectionPoolType: 连接池类型。可选值 transaction（事务级别连接池），connection（会话级别连接池），ConnectionPool为true时生效。
        :type ConnectionPoolType: str
        """
        self._ProxyGroupId = None
        self._WeightMode = None
        self._IsKickOut = None
        self._MinCount = None
        self._MaxDelay = None
        self._FailOver = None
        self._AutoAddRo = None
        self._ReadOnly = None
        self._TransSplit = None
        self._ProxyAllocation = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ConnectionPool = None
        self._Desc = None
        self._Vip = None
        self._VPort = None
        self._SecurityGroup = None
        self._ConnectionPoolType = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def IsKickOut(self):
        return self._IsKickOut

    @IsKickOut.setter
    def IsKickOut(self, IsKickOut):
        self._IsKickOut = IsKickOut

    @property
    def MinCount(self):
        return self._MinCount

    @MinCount.setter
    def MinCount(self, MinCount):
        self._MinCount = MinCount

    @property
    def MaxDelay(self):
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def ProxyAllocation(self):
        return self._ProxyAllocation

    @ProxyAllocation.setter
    def ProxyAllocation(self, ProxyAllocation):
        self._ProxyAllocation = ProxyAllocation

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._WeightMode = params.get("WeightMode")
        self._IsKickOut = params.get("IsKickOut")
        self._MinCount = params.get("MinCount")
        self._MaxDelay = params.get("MaxDelay")
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        self._ReadOnly = params.get("ReadOnly")
        self._TransSplit = params.get("TransSplit")
        if params.get("ProxyAllocation") is not None:
            self._ProxyAllocation = []
            for item in params.get("ProxyAllocation"):
                obj = ProxyAllocation()
                obj._deserialize(item)
                self._ProxyAllocation.append(obj)
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ConnectionPool = params.get("ConnectionPool")
        self._Desc = params.get("Desc")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._SecurityGroup = params.get("SecurityGroup")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCdbProxyAddressResponse(AbstractModel):
    """CreateCdbProxyAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateCdbProxyRequest(AbstractModel):
    """CreateCdbProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _UniqVpcId: 私有网络ID
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有子网ID
        :type UniqSubnetId: str
        :param _ProxyNodeCustom: 节点规格配置
        :type ProxyNodeCustom: list of ProxyNodeCustom
        :param _SecurityGroup: 安全组
        :type SecurityGroup: list of str
        :param _Desc: 描述
        :type Desc: str
        :param _ConnectionPoolLimit: 连接池阈值
        :type ConnectionPoolLimit: int
        """
        self._InstanceId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ProxyNodeCustom = None
        self._SecurityGroup = None
        self._Desc = None
        self._ConnectionPoolLimit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ProxyNodeCustom(self):
        return self._ProxyNodeCustom

    @ProxyNodeCustom.setter
    def ProxyNodeCustom(self, ProxyNodeCustom):
        self._ProxyNodeCustom = ProxyNodeCustom

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ConnectionPoolLimit(self):
        return self._ConnectionPoolLimit

    @ConnectionPoolLimit.setter
    def ConnectionPoolLimit(self, ConnectionPoolLimit):
        self._ConnectionPoolLimit = ConnectionPoolLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        if params.get("ProxyNodeCustom") is not None:
            self._ProxyNodeCustom = []
            for item in params.get("ProxyNodeCustom"):
                obj = ProxyNodeCustom()
                obj._deserialize(item)
                self._ProxyNodeCustom.append(obj)
        self._SecurityGroup = params.get("SecurityGroup")
        self._Desc = params.get("Desc")
        self._ConnectionPoolLimit = params.get("ConnectionPoolLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCdbProxyResponse(AbstractModel):
    """CreateCdbProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateCloneInstanceRequest(AbstractModel):
    """CreateCloneInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 克隆源实例Id。
        :type InstanceId: str
        :param _SpecifiedRollbackTime: 如果需要克隆实例回档到指定时间，则指定该值。时间格式为： yyyy-mm-dd hh:mm:ss 。
        :type SpecifiedRollbackTime: str
        :param _SpecifiedBackupId: 如果需要克隆实例回档到指定备份的时间点，则指定该值为物理备份的Id。请使用 [查询数据备份文件列表](/document/api/236/15842) 。
        :type SpecifiedBackupId: int
        :param _UniqVpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 [查询私有网络列表](/document/api/215/15778) 。
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 [查询子网列表](/document/api/215/15784)。
        :type UniqSubnetId: str
        :param _Memory: 实例内存大小，单位：MB，需要不低于克隆源实例，默认和源实例相同。
        :type Memory: int
        :param _Volume: 实例硬盘大小，单位：GB，需要不低于克隆源实例，默认和源实例相同。
        :type Volume: int
        :param _InstanceName: 新产生的克隆实例名称。
        :type InstanceName: str
        :param _SecurityGroup: 安全组参数，可使用 [查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850) 接口查询某个项目的安全组详情。
        :type SecurityGroup: list of str
        :param _ResourceTags: 实例标签信息。
        :type ResourceTags: list of TagInfo
        :param _Cpu: 实例Cpu核数，需要不低于克隆源实例，默认和源实例相同。
        :type Cpu: int
        :param _ProtectMode: 数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制。
        :type ProtectMode: int
        :param _DeployMode: 多可用区域，默认为 0，支持值包括：0 - 表示单可用区，1 - 表示多可用区。
        :type DeployMode: int
        :param _SlaveZone: 新产生的克隆实例备库 1 的可用区信息，默认同源实例 Zone 的值。
        :type SlaveZone: str
        :param _BackupZone: 备库 2 的可用区信息，默认为空，克隆强同步主实例时可指定该参数。
        :type BackupZone: str
        :param _DeviceType: 克隆实例类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例。 不指定则默认为通用型。
        :type DeviceType: str
        :param _InstanceNodes: 新克隆实例节点数。如果需要克隆出三节点实例， 请将该值设置为3 或指定 BackupZone 参数。如果需要克隆出两节点实例，请将该值设置为2。默认克隆出两节点实例。
        :type InstanceNodes: int
        :param _DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param _DryRun: 是否只预检此次请求。true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制等。如果检查不通过，则返回对应错误码；如果检查通过，则返回RequestId.默认为false：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
        :param _CageId: 金融围拢 ID 。
        :type CageId: str
        :param _ProjectId: 项目ID，默认项目ID0
        :type ProjectId: int
        """
        self._InstanceId = None
        self._SpecifiedRollbackTime = None
        self._SpecifiedBackupId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Memory = None
        self._Volume = None
        self._InstanceName = None
        self._SecurityGroup = None
        self._ResourceTags = None
        self._Cpu = None
        self._ProtectMode = None
        self._DeployMode = None
        self._SlaveZone = None
        self._BackupZone = None
        self._DeviceType = None
        self._InstanceNodes = None
        self._DeployGroupId = None
        self._DryRun = None
        self._CageId = None
        self._ProjectId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpecifiedRollbackTime(self):
        return self._SpecifiedRollbackTime

    @SpecifiedRollbackTime.setter
    def SpecifiedRollbackTime(self, SpecifiedRollbackTime):
        self._SpecifiedRollbackTime = SpecifiedRollbackTime

    @property
    def SpecifiedBackupId(self):
        return self._SpecifiedBackupId

    @SpecifiedBackupId.setter
    def SpecifiedBackupId(self, SpecifiedBackupId):
        self._SpecifiedBackupId = SpecifiedBackupId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpecifiedRollbackTime = params.get("SpecifiedRollbackTime")
        self._SpecifiedBackupId = params.get("SpecifiedBackupId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._InstanceName = params.get("InstanceName")
        self._SecurityGroup = params.get("SecurityGroup")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Cpu = params.get("Cpu")
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._SlaveZone = params.get("SlaveZone")
        self._BackupZone = params.get("BackupZone")
        self._DeviceType = params.get("DeviceType")
        self._InstanceNodes = params.get("InstanceNodes")
        self._DeployGroupId = params.get("DeployGroupId")
        self._DryRun = params.get("DryRun")
        self._CageId = params.get("CageId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloneInstanceResponse(AbstractModel):
    """CreateCloneInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateDBImportJobRequest(AbstractModel):
    """CreateDBImportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _User: 云数据库的用户名。
        :type User: str
        :param _FileName: 文件名称。该文件是指用户已上传到腾讯云的文件，仅支持.sql文件。
        :type FileName: str
        :param _Password: 云数据库实例 User 账号的密码。
        :type Password: str
        :param _DbName: 导入的目标数据库名，不传表示不指定数据库。
        :type DbName: str
        :param _CosUrl: 腾讯云COS文件链接。 用户需要指定 FileName 或者 CosUrl 其中一个。 COS文件需要是 .sql 文件。
        :type CosUrl: str
        """
        self._InstanceId = None
        self._User = None
        self._FileName = None
        self._Password = None
        self._DbName = None
        self._CosUrl = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._FileName = params.get("FileName")
        self._Password = params.get("Password")
        self._DbName = params.get("DbName")
        self._CosUrl = params.get("CosUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBImportJobResponse(AbstractModel):
    """CreateDBImportJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GoodsNum: 实例数量，默认值为 1，最小值 1，最大值为 100。
        :type GoodsNum: int
        :param _Memory: 实例内存大小，单位：MB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的内存规格。
        :type Memory: int
        :param _Volume: 实例硬盘大小，单位：GB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的硬盘范围。
        :type Volume: int
        :param _EngineVersion: MySQL 版本，值包括：5.5、5.6 、5.7 、8.0，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的实例版本。
        :type EngineVersion: str
        :param _UniqVpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 [查询私有网络列表](/document/api/215/15778) 。
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用[查询子网列表](/document/api/215/15784)。
        :type UniqSubnetId: str
        :param _ProjectId: 项目 ID，不填为默认项目。
        :type ProjectId: int
        :param _Zone: 可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的可用区。
        :type Zone: str
        :param _MasterInstanceId: 实例 ID，购买只读实例或者灾备实例时必填，该字段表示只读实例或者灾备实例的主实例 ID，请使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询云数据库实例 ID。
        :type MasterInstanceId: str
        :param _InstanceRole: 实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。
        :type InstanceRole: str
        :param _MasterRegion: 主实例地域信息，购买灾备、RO实例时，该字段必填。
        :type MasterRegion: str
        :param _Port: 自定义端口，端口支持范围：[ 1024-65535 ] 。
        :type Port: int
        :param _Password: 设置 root 帐号密码，密码规则：8 - 64 个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type Password: str
        :param _ParamList: 参数列表，参数格式如 ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过 [查询默认的可设置参数列表](https://cloud.tencent.com/document/api/236/32662) 查询支持设置的参数。
        :type ParamList: list of ParamInfo
        :param _ProtectMode: 数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type ProtectMode: int
        :param _DeployMode: 多可用区域，默认为 0，支持值包括：0 - 表示单可用区，1 - 表示多可用区，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type DeployMode: int
        :param _SlaveZone: 备库 1 的可用区信息，默认为 Zone 的值，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type SlaveZone: str
        :param _BackupZone: 备库 2 的可用区信息，默认为空，购买三节点主实例时可指定该参数。
        :type BackupZone: str
        :param _SecurityGroup: 安全组参数，可使用 [查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850) 接口查询某个项目的安全组详情。
        :type SecurityGroup: list of str
        :param _RoGroup: 只读实例信息。购买只读实例时，该参数必传。
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param _AutoRenewFlag: 购买按量计费实例该字段无意义。
        :type AutoRenewFlag: int
        :param _InstanceName: 实例名称。一次购买多个实例命名会用后缀数字区分，例instanceName=db，goodsNum=3，实例命名分别为db1，db2，db3。
        :type InstanceName: str
        :param _ResourceTags: 实例标签信息。
        :type ResourceTags: list of TagInfo
        :param _DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间在48小时内唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。 不指定则默认为通用型实例。
        :type DeviceType: str
        :param _ParamTemplateId: 参数模板id。
        :type ParamTemplateId: int
        :param _AlarmPolicyList: 告警策略id数组。腾讯云可观测平台DescribeAlarmPolicy接口返回的OriginId。
        :type AlarmPolicyList: list of int
        :param _InstanceNodes: 实例节点数。对于 RO 和 基础版实例， 该值默认为1。 如果需要购买三节点实例， 请将该值设置为3 或指定 BackupZone 参数。当购买主实例，且未指定该参数和 BackupZone 参数时，该值默认是 2， 即购买两节点实例。
        :type InstanceNodes: int
        :param _Cpu: 实例cpu核数， 如果不传将根据memory指定的内存值自动填充对应的cpu值。
        :type Cpu: int
        :param _AutoSyncFlag: 是否自动发起灾备同步功能。该参数仅对购买灾备实例生效。 可选值为：0 - 不自动发起灾备同步；1 - 自动发起灾备同步。该值默认为0。
        :type AutoSyncFlag: int
        :param _CageId: 金融围拢 ID 。
        :type CageId: str
        :param _ParamTemplateType: 默认参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模板，"HIGH_PERFORMANCE" - 高性能模板，默认值是："HIGH_STABILITY"。
        :type ParamTemplateType: str
        :param _AlarmPolicyIdList: 告警策略名数组，例如:["policy-uyoee9wg"]，AlarmPolicyList不为空时该参数无效。
        :type AlarmPolicyIdList: list of str
        :param _DryRun: 是否只预检此次请求。true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制等。如果检查不通过，则返回对应错误码；如果检查通过，则返回RequestId.默认为false：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
        :param _EngineType: 实例引擎类型，默认为"InnoDB"，支持值包括："InnoDB"，"RocksDB"。
        :type EngineType: str
        :param _Vips: 指定实例的IP列表。仅支持主实例指定，按实例顺序，不足则按未指定处理。
        :type Vips: list of str
        """
        self._GoodsNum = None
        self._Memory = None
        self._Volume = None
        self._EngineVersion = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ProjectId = None
        self._Zone = None
        self._MasterInstanceId = None
        self._InstanceRole = None
        self._MasterRegion = None
        self._Port = None
        self._Password = None
        self._ParamList = None
        self._ProtectMode = None
        self._DeployMode = None
        self._SlaveZone = None
        self._BackupZone = None
        self._SecurityGroup = None
        self._RoGroup = None
        self._AutoRenewFlag = None
        self._InstanceName = None
        self._ResourceTags = None
        self._DeployGroupId = None
        self._ClientToken = None
        self._DeviceType = None
        self._ParamTemplateId = None
        self._AlarmPolicyList = None
        self._InstanceNodes = None
        self._Cpu = None
        self._AutoSyncFlag = None
        self._CageId = None
        self._ParamTemplateType = None
        self._AlarmPolicyIdList = None
        self._DryRun = None
        self._EngineType = None
        self._Vips = None

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def MasterRegion(self):
        return self._MasterRegion

    @MasterRegion.setter
    def MasterRegion(self, MasterRegion):
        self._MasterRegion = MasterRegion

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RoGroup(self):
        return self._RoGroup

    @RoGroup.setter
    def RoGroup(self, RoGroup):
        self._RoGroup = RoGroup

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def AlarmPolicyList(self):
        return self._AlarmPolicyList

    @AlarmPolicyList.setter
    def AlarmPolicyList(self, AlarmPolicyList):
        self._AlarmPolicyList = AlarmPolicyList

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def AutoSyncFlag(self):
        return self._AutoSyncFlag

    @AutoSyncFlag.setter
    def AutoSyncFlag(self, AutoSyncFlag):
        self._AutoSyncFlag = AutoSyncFlag

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ParamTemplateType(self):
        return self._ParamTemplateType

    @ParamTemplateType.setter
    def ParamTemplateType(self, ParamTemplateType):
        self._ParamTemplateType = ParamTemplateType

    @property
    def AlarmPolicyIdList(self):
        return self._AlarmPolicyIdList

    @AlarmPolicyIdList.setter
    def AlarmPolicyIdList(self, AlarmPolicyIdList):
        self._AlarmPolicyIdList = AlarmPolicyIdList

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips


    def _deserialize(self, params):
        self._GoodsNum = params.get("GoodsNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._EngineVersion = params.get("EngineVersion")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ProjectId = params.get("ProjectId")
        self._Zone = params.get("Zone")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._InstanceRole = params.get("InstanceRole")
        self._MasterRegion = params.get("MasterRegion")
        self._Port = params.get("Port")
        self._Password = params.get("Password")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._SlaveZone = params.get("SlaveZone")
        self._BackupZone = params.get("BackupZone")
        self._SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self._RoGroup = RoGroup()
            self._RoGroup._deserialize(params.get("RoGroup"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DeployGroupId = params.get("DeployGroupId")
        self._ClientToken = params.get("ClientToken")
        self._DeviceType = params.get("DeviceType")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._AlarmPolicyList = params.get("AlarmPolicyList")
        self._InstanceNodes = params.get("InstanceNodes")
        self._Cpu = params.get("Cpu")
        self._AutoSyncFlag = params.get("AutoSyncFlag")
        self._CageId = params.get("CageId")
        self._ParamTemplateType = params.get("ParamTemplateType")
        self._AlarmPolicyIdList = params.get("AlarmPolicyIdList")
        self._DryRun = params.get("DryRun")
        self._EngineType = params.get("EngineType")
        self._Vips = params.get("Vips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealIds: 短订单 ID。
        :type DealIds: list of str
        :param _InstanceIds: 实例 ID 列表。
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealIds = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Memory: 实例内存大小，单位：MB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的内存规格。
        :type Memory: int
        :param _Volume: 实例硬盘大小，单位：GB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的硬盘范围。
        :type Volume: int
        :param _Period: 实例时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :type Period: int
        :param _GoodsNum: 实例数量，默认值为1, 最小值1，最大值为100。
        :type GoodsNum: int
        :param _Zone: 可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的可用区。
        :type Zone: str
        :param _UniqVpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 [查询私有网络列表](/document/api/215/15778) 。
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 [查询子网列表](/document/api/215/15784)。
        :type UniqSubnetId: str
        :param _ProjectId: 项目 ID，不填为默认项目。购买只读实例和灾备实例时，项目 ID 默认和主实例保持一致。
        :type ProjectId: int
        :param _Port: 自定义端口，端口支持范围：[ 1024-65535 ]。
        :type Port: int
        :param _InstanceRole: 实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。
        :type InstanceRole: str
        :param _MasterInstanceId: 实例 ID，购买只读实例时必填，该字段表示只读实例的主实例ID，请使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询云数据库实例 ID。
        :type MasterInstanceId: str
        :param _EngineVersion: MySQL 版本，值包括：5.5、5.6 和 5.7，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的实例版本。
        :type EngineVersion: str
        :param _Password: 设置 root 帐号密码，密码规则：8 - 64 个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type Password: str
        :param _ProtectMode: 数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制。
        :type ProtectMode: int
        :param _DeployMode: 多可用区域，默认为 0，支持值包括：0 - 表示单可用区，1 - 表示多可用区。
        :type DeployMode: int
        :param _SlaveZone: 备库 1 的可用区信息，默认为 Zone 的值。
        :type SlaveZone: str
        :param _ParamList: 参数列表，参数格式如 ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过 [查询默认的可设置参数列表](https://cloud.tencent.com/document/api/236/32662) 查询支持设置的参数。
        :type ParamList: list of ParamInfo
        :param _BackupZone: 备库 2 的可用区信息，默认为空，购买三节点主实例时可指定该参数。
        :type BackupZone: str
        :param _AutoRenewFlag: 自动续费标记，可选值为：0 - 不自动续费；1 - 自动续费。
        :type AutoRenewFlag: int
        :param _MasterRegion: 主实例地域信息，购买灾备、RO实例时，该字段必填。
        :type MasterRegion: str
        :param _SecurityGroup: 安全组参数，可使用 [查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850) 接口查询某个项目的安全组详情。
        :type SecurityGroup: list of str
        :param _RoGroup: 只读实例参数。购买只读实例时，该参数必传。
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param _InstanceName: 实例名称。一次购买多个实例命名会用后缀数字区分，例instnaceName=db，goodsNum=3，实例命名分别为db1，db2，db3。
        :type InstanceName: str
        :param _ResourceTags: 实例标签信息。
        :type ResourceTags: list of TagInfo
        :param _DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间在48小时内唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。 不指定则默认为通用型实例。
        :type DeviceType: str
        :param _ParamTemplateId: 参数模板id。
        :type ParamTemplateId: int
        :param _AlarmPolicyList: 告警策略id数组。云监控DescribeAlarmPolicy接口返回的OriginId。
        :type AlarmPolicyList: list of int
        :param _InstanceNodes: 实例节点数。对于 RO 和 基础版实例， 该值默认为1。 如果需要购买三节点实例， 请将该值设置为3 或指定 BackupZone 参数。当购买主实例，且未指定该参数和 BackupZone 参数时，该值默认是 2， 即购买两节点实例。
        :type InstanceNodes: int
        :param _Cpu: 实例cpu核数， 如果不传将根据memory指定的内存值自动填充对应的cpu值。
        :type Cpu: int
        :param _AutoSyncFlag: 是否自动发起灾备同步功能。该参数仅对购买灾备实例生效。 可选值为：0 - 不自动发起灾备同步；1 - 自动发起灾备同步。该值默认为0。
        :type AutoSyncFlag: int
        :param _CageId: 金融围拢 ID。
        :type CageId: str
        :param _ParamTemplateType: 默认参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模板，"HIGH_PERFORMANCE" - 高性能模板。
        :type ParamTemplateType: str
        :param _AlarmPolicyIdList: 告警策略名数组，例如:["policy-uyoee9wg"]，AlarmPolicyList不为空时该参数无效。
        :type AlarmPolicyIdList: list of str
        :param _DryRun: 是否只预检此次请求。true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制等。如果检查不通过，则返回对应错误码；如果检查通过，则返回RequestId.默认为false：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
        :param _EngineType: 实例引擎类型，默认为"InnoDB"，支持值包括："InnoDB"，"RocksDB"。
        :type EngineType: str
        :param _Vips: 指定实例的IP列表。仅支持主实例指定，按实例顺序，不足则按未指定处理。
        :type Vips: list of str
        """
        self._Memory = None
        self._Volume = None
        self._Period = None
        self._GoodsNum = None
        self._Zone = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ProjectId = None
        self._Port = None
        self._InstanceRole = None
        self._MasterInstanceId = None
        self._EngineVersion = None
        self._Password = None
        self._ProtectMode = None
        self._DeployMode = None
        self._SlaveZone = None
        self._ParamList = None
        self._BackupZone = None
        self._AutoRenewFlag = None
        self._MasterRegion = None
        self._SecurityGroup = None
        self._RoGroup = None
        self._InstanceName = None
        self._ResourceTags = None
        self._DeployGroupId = None
        self._ClientToken = None
        self._DeviceType = None
        self._ParamTemplateId = None
        self._AlarmPolicyList = None
        self._InstanceNodes = None
        self._Cpu = None
        self._AutoSyncFlag = None
        self._CageId = None
        self._ParamTemplateType = None
        self._AlarmPolicyIdList = None
        self._DryRun = None
        self._EngineType = None
        self._Vips = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def MasterRegion(self):
        return self._MasterRegion

    @MasterRegion.setter
    def MasterRegion(self, MasterRegion):
        self._MasterRegion = MasterRegion

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RoGroup(self):
        return self._RoGroup

    @RoGroup.setter
    def RoGroup(self, RoGroup):
        self._RoGroup = RoGroup

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def AlarmPolicyList(self):
        return self._AlarmPolicyList

    @AlarmPolicyList.setter
    def AlarmPolicyList(self, AlarmPolicyList):
        self._AlarmPolicyList = AlarmPolicyList

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def AutoSyncFlag(self):
        return self._AutoSyncFlag

    @AutoSyncFlag.setter
    def AutoSyncFlag(self, AutoSyncFlag):
        self._AutoSyncFlag = AutoSyncFlag

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ParamTemplateType(self):
        return self._ParamTemplateType

    @ParamTemplateType.setter
    def ParamTemplateType(self, ParamTemplateType):
        self._ParamTemplateType = ParamTemplateType

    @property
    def AlarmPolicyIdList(self):
        return self._AlarmPolicyIdList

    @AlarmPolicyIdList.setter
    def AlarmPolicyIdList(self, AlarmPolicyIdList):
        self._AlarmPolicyIdList = AlarmPolicyIdList

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._Period = params.get("Period")
        self._GoodsNum = params.get("GoodsNum")
        self._Zone = params.get("Zone")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ProjectId = params.get("ProjectId")
        self._Port = params.get("Port")
        self._InstanceRole = params.get("InstanceRole")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._EngineVersion = params.get("EngineVersion")
        self._Password = params.get("Password")
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._SlaveZone = params.get("SlaveZone")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._BackupZone = params.get("BackupZone")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._MasterRegion = params.get("MasterRegion")
        self._SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self._RoGroup = RoGroup()
            self._RoGroup._deserialize(params.get("RoGroup"))
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DeployGroupId = params.get("DeployGroupId")
        self._ClientToken = params.get("ClientToken")
        self._DeviceType = params.get("DeviceType")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._AlarmPolicyList = params.get("AlarmPolicyList")
        self._InstanceNodes = params.get("InstanceNodes")
        self._Cpu = params.get("Cpu")
        self._AutoSyncFlag = params.get("AutoSyncFlag")
        self._CageId = params.get("CageId")
        self._ParamTemplateType = params.get("ParamTemplateType")
        self._AlarmPolicyIdList = params.get("AlarmPolicyIdList")
        self._DryRun = params.get("DryRun")
        self._EngineType = params.get("EngineType")
        self._Vips = params.get("Vips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealIds: 短订单 ID。
        :type DealIds: list of str
        :param _InstanceIds: 实例 ID 列表。
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealIds = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateDatabaseRequest(AbstractModel):
    """CreateDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _DBName: 数据库名称。
        :type DBName: str
        :param _CharacterSetName: 字符集，可选值：utf8，gbk，latin1，utf8mb4。
        :type CharacterSetName: str
        """
        self._InstanceId = None
        self._DBName = None
        self._CharacterSetName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def CharacterSetName(self):
        return self._CharacterSetName

    @CharacterSetName.setter
    def CharacterSetName(self, CharacterSetName):
        self._CharacterSetName = CharacterSetName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DBName = params.get("DBName")
        self._CharacterSetName = params.get("CharacterSetName")
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


class CreateDeployGroupRequest(AbstractModel):
    """CreateDeployGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployGroupName: 置放群组名称，最长不能超过60个字符。
        :type DeployGroupName: str
        :param _Description: 置放群组描述，最长不能超过200个字符。
        :type Description: str
        :param _Affinity: 置放群组的亲和性策略，目前仅支持取值为1，策略1表示同台物理机上限制实例的个数。
        :type Affinity: list of int
        :param _LimitNum: 置放群组亲和性策略1中同台物理机上实例的限制个数。
        :type LimitNum: int
        :param _DevClass: 置放群组机型属性，可选参数：SH12+SH02、TS85。
        :type DevClass: list of str
        """
        self._DeployGroupName = None
        self._Description = None
        self._Affinity = None
        self._LimitNum = None
        self._DevClass = None

    @property
    def DeployGroupName(self):
        return self._DeployGroupName

    @DeployGroupName.setter
    def DeployGroupName(self, DeployGroupName):
        self._DeployGroupName = DeployGroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Affinity(self):
        return self._Affinity

    @Affinity.setter
    def Affinity(self, Affinity):
        self._Affinity = Affinity

    @property
    def LimitNum(self):
        return self._LimitNum

    @LimitNum.setter
    def LimitNum(self, LimitNum):
        self._LimitNum = LimitNum

    @property
    def DevClass(self):
        return self._DevClass

    @DevClass.setter
    def DevClass(self, DevClass):
        self._DevClass = DevClass


    def _deserialize(self, params):
        self._DeployGroupName = params.get("DeployGroupName")
        self._Description = params.get("Description")
        self._Affinity = params.get("Affinity")
        self._LimitNum = params.get("LimitNum")
        self._DevClass = params.get("DevClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeployGroupResponse(AbstractModel):
    """CreateDeployGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployGroupId: 置放群组ID。
        :type DeployGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployGroupId = None
        self._RequestId = None

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployGroupId = params.get("DeployGroupId")
        self._RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 参数模板名称。
        :type Name: str
        :param _Description: 参数模板描述。
        :type Description: str
        :param _EngineVersion: MySQL 版本号。
        :type EngineVersion: str
        :param _TemplateId: 源参数模板 ID。
        :type TemplateId: int
        :param _ParamList: 参数列表。
        :type ParamList: list of Parameter
        :param _TemplateType: 默认参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模板，"HIGH_PERFORMANCE" - 高性能模板。
        :type TemplateType: str
        :param _EngineType: 实例引擎类型，默认为"InnoDB"，支持值包括："InnoDB"，"RocksDB"。
        :type EngineType: str
        """
        self._Name = None
        self._Description = None
        self._EngineVersion = None
        self._TemplateId = None
        self._ParamList = None
        self._TemplateType = None
        self._EngineType = None

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
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EngineVersion = params.get("EngineVersion")
        self._TemplateId = params.get("TemplateId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._TemplateType = params.get("TemplateType")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板 ID。
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateRoInstanceIpRequest(AbstractModel):
    """CreateRoInstanceIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 只读实例ID，格式如：cdbro-3i70uj0k，与云数据库控制台页面中显示的只读实例ID相同。
        :type InstanceId: str
        :param _UniqSubnetId: 子网描述符，例如：subnet-1typ0s7d。
        :type UniqSubnetId: str
        :param _UniqVpcId: vpc描述符，例如：vpc-a23yt67j,如果传了该字段则UniqSubnetId必传
        :type UniqVpcId: str
        """
        self._InstanceId = None
        self._UniqSubnetId = None
        self._UniqVpcId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoInstanceIpResponse(AbstractModel):
    """CreateRoInstanceIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoVpcId: 只读实例的私有网络的ID。
        :type RoVpcId: int
        :param _RoSubnetId: 只读实例的子网ID。
        :type RoSubnetId: int
        :param _RoVip: 只读实例的内网IP地址。
        :type RoVip: str
        :param _RoVport: 只读实例的内网端口号。
        :type RoVport: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoVpcId = None
        self._RoSubnetId = None
        self._RoVip = None
        self._RoVport = None
        self._RequestId = None

    @property
    def RoVpcId(self):
        return self._RoVpcId

    @RoVpcId.setter
    def RoVpcId(self, RoVpcId):
        self._RoVpcId = RoVpcId

    @property
    def RoSubnetId(self):
        return self._RoSubnetId

    @RoSubnetId.setter
    def RoSubnetId(self, RoSubnetId):
        self._RoSubnetId = RoSubnetId

    @property
    def RoVip(self):
        return self._RoVip

    @RoVip.setter
    def RoVip(self, RoVip):
        self._RoVip = RoVip

    @property
    def RoVport(self):
        return self._RoVport

    @RoVport.setter
    def RoVport(self, RoVport):
        self._RoVport = RoVport

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoVpcId = params.get("RoVpcId")
        self._RoSubnetId = params.get("RoSubnetId")
        self._RoVip = params.get("RoVip")
        self._RoVport = params.get("RoVport")
        self._RequestId = params.get("RequestId")


class CustomConfig(AbstractModel):
    """proxy配置

    """

    def __init__(self):
        r"""
        :param _Device: 设备
注意：此字段可能返回 null，表示取不到有效值。
        :type Device: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _DeviceType: 设备类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param _Memory: 内存
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _Cpu: 核数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        """
        self._Device = None
        self._Type = None
        self._DeviceType = None
        self._Memory = None
        self._Cpu = None

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._Device = params.get("Device")
        self._Type = params.get("Type")
        self._DeviceType = params.get("DeviceType")
        self._Memory = params.get("Memory")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBSwitchInfo(AbstractModel):
    """云数据库切换记录

    """

    def __init__(self):
        r"""
        :param _SwitchTime: 切换时间，格式为：2017-09-03 01:34:31
        :type SwitchTime: str
        :param _SwitchType: 切换类型，可能的返回值为：TRANSFER - 数据迁移；MASTER2SLAVE - 主备切换；RECOVERY - 主从恢复
        :type SwitchType: str
        """
        self._SwitchTime = None
        self._SwitchType = None

    @property
    def SwitchTime(self):
        return self._SwitchTime

    @SwitchTime.setter
    def SwitchTime(self, SwitchTime):
        self._SwitchTime = SwitchTime

    @property
    def SwitchType(self):
        return self._SwitchType

    @SwitchType.setter
    def SwitchType(self, SwitchType):
        self._SwitchType = SwitchType


    def _deserialize(self, params):
        self._SwitchTime = params.get("SwitchTime")
        self._SwitchType = params.get("SwitchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseName(AbstractModel):
    """数据库表名

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库表名
        :type DatabaseName: str
        """
        self._DatabaseName = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    """数据库权限

    """

    def __init__(self):
        r"""
        :param _Privileges: 权限信息
        :type Privileges: list of str
        :param _Database: 数据库名
        :type Database: str
        """
        self._Privileges = None
        self._Database = None

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database


    def _deserialize(self, params):
        self._Privileges = params.get("Privileges")
        self._Database = params.get("Database")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasesWithCharacterLists(AbstractModel):
    """数据库名以及字符集

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名
        :type DatabaseName: str
        :param _CharacterSet: 字符集类型
        :type CharacterSet: str
        """
        self._DatabaseName = None
        self._CharacterSet = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def CharacterSet(self):
        return self._CharacterSet

    @CharacterSet.setter
    def CharacterSet(self, CharacterSet):
        self._CharacterSet = CharacterSet


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._CharacterSet = params.get("CharacterSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsRequest(AbstractModel):
    """DeleteAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Accounts: 云数据库账号。
        :type Accounts: list of Account
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsResponse(AbstractModel):
    """DeleteAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class DeleteAuditLogFileRequest(AbstractModel):
    """DeleteAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileName: 审计日志文件名称。
        :type FileName: str
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._FileName = None
        self._InstanceId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditLogFileResponse(AbstractModel):
    """DeleteAuditLogFile返回参数结构体

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


class DeleteAuditPolicyRequest(AbstractModel):
    """DeleteAuditPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 审计策略 ID。
        :type PolicyId: str
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._PolicyId = None
        self._InstanceId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditPolicyResponse(AbstractModel):
    """DeleteAuditPolicy返回参数结构体

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


class DeleteAuditRuleRequest(AbstractModel):
    """DeleteAuditRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 审计规则 ID。
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditRuleResponse(AbstractModel):
    """DeleteAuditRule返回参数结构体

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


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _BackupId: 备份任务 ID。该任务 ID 为 [创建云数据库备份](https://cloud.tencent.com/document/api/236/15844) 接口返回的任务 ID。
        :type BackupId: int
        """
        self._InstanceId = None
        self._BackupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup返回参数结构体

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


class DeleteDeployGroupsRequest(AbstractModel):
    """DeleteDeployGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployGroupIds: 要删除的置放群组 ID 列表。
        :type DeployGroupIds: list of str
        """
        self._DeployGroupIds = None

    @property
    def DeployGroupIds(self):
        return self._DeployGroupIds

    @DeployGroupIds.setter
    def DeployGroupIds(self, DeployGroupIds):
        self._DeployGroupIds = DeployGroupIds


    def _deserialize(self, params):
        self._DeployGroupIds = params.get("DeployGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeployGroupsResponse(AbstractModel):
    """DeleteDeployGroups返回参数结构体

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


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate返回参数结构体

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


class DeleteTimeWindowRequest(AbstractModel):
    """DeleteTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimeWindowResponse(AbstractModel):
    """DeleteTimeWindow返回参数结构体

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


class DeployGroupInfo(AbstractModel):
    """置放群组信息

    """

    def __init__(self):
        r"""
        :param _DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param _DeployGroupName: 置放群组名称。
        :type DeployGroupName: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _Quota: 置放群组实例配额，表示一个置放群组中可容纳的最大实例数目。
        :type Quota: int
        :param _Affinity: 置放群组亲和性策略，目前仅支持策略1，即在物理机纬度打散实例的分布。
注意：此字段可能返回 null，表示取不到有效值。
        :type Affinity: str
        :param _LimitNum: 置放群组亲和性策略1中，同台物理机上同个置放群组实例的限制个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitNum: int
        :param _Description: 置放群组详细信息。
        :type Description: str
        :param _DevClass: 置放群组物理机型属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type DevClass: str
        """
        self._DeployGroupId = None
        self._DeployGroupName = None
        self._CreateTime = None
        self._Quota = None
        self._Affinity = None
        self._LimitNum = None
        self._Description = None
        self._DevClass = None

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def DeployGroupName(self):
        return self._DeployGroupName

    @DeployGroupName.setter
    def DeployGroupName(self, DeployGroupName):
        self._DeployGroupName = DeployGroupName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Quota(self):
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota

    @property
    def Affinity(self):
        return self._Affinity

    @Affinity.setter
    def Affinity(self, Affinity):
        self._Affinity = Affinity

    @property
    def LimitNum(self):
        return self._LimitNum

    @LimitNum.setter
    def LimitNum(self, LimitNum):
        self._LimitNum = LimitNum

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DevClass(self):
        return self._DevClass

    @DevClass.setter
    def DevClass(self, DevClass):
        self._DevClass = DevClass


    def _deserialize(self, params):
        self._DeployGroupId = params.get("DeployGroupId")
        self._DeployGroupName = params.get("DeployGroupName")
        self._CreateTime = params.get("CreateTime")
        self._Quota = params.get("Quota")
        self._Affinity = params.get("Affinity")
        self._LimitNum = params.get("LimitNum")
        self._Description = params.get("Description")
        self._DevClass = params.get("DevClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _User: 数据库的账号名称。
        :type User: str
        :param _Host: 数据库的账号域名。
        :type Host: str
        """
        self._InstanceId = None
        self._User = None
        self._Host = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalPrivileges: 全局权限数组。
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: 数据库权限数组。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param _TablePrivileges: 数据库中的表权限数组。
        :type TablePrivileges: list of TablePrivilege
        :param _ColumnPrivileges: 数据库表中的列权限数组。
        :type ColumnPrivileges: list of ColumnPrivilege
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None
        self._ColumnPrivileges = None
        self._RequestId = None

    @property
    def GlobalPrivileges(self):
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges

    @property
    def ColumnPrivileges(self):
        return self._ColumnPrivileges

    @ColumnPrivileges.setter
    def ColumnPrivileges(self, ColumnPrivileges):
        self._ColumnPrivileges = ColumnPrivileges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self._ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self._ColumnPrivileges.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 单次请求返回的数量，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param _AccountRegexp: 匹配账号名的正则表达式，规则同 MySQL 官网。
        :type AccountRegexp: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._AccountRegexp = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def AccountRegexp(self):
        return self._AccountRegexp

    @AccountRegexp.setter
    def AccountRegexp(self, AccountRegexp):
        self._AccountRegexp = AccountRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AccountRegexp = params.get("AccountRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的账号数量。
        :type TotalCount: int
        :param _Items: 符合查询条件的账号详细信息。
        :type Items: list of AccountInfo
        :param _MaxUserConnections: 用户可设置实例最大连接数。
        :type MaxUserConnections: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._MaxUserConnections = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AccountInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._MaxUserConnections = params.get("MaxUserConnections")
        self._RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID。
        :type AsyncRequestId: str
        """
        self._AsyncRequestId = None

    @property
    def AsyncRequestId(self):
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
        :param _Status: 任务执行结果。可能的取值：INITIAL - 初始化，RUNNING - 运行中，SUCCESS - 执行成功，FAILED - 执行失败，KILLED - 已终止，REMOVED - 已删除，PAUSED - 终止中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Info: 任务执行信息描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class DescribeAuditConfigRequest(AbstractModel):
    """DescribeAuditConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditConfigResponse(AbstractModel):
    """DescribeAuditConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogExpireDay: 审计日志保存时长。目前支持的值包括：[0，7，30，180，365，1095，1825]。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogExpireDay: int
        :param _LogType: 审计日志存储类型。目前支持的值包括："storage" - 存储型。
        :type LogType: str
        :param _IsClosing: 是否正在关闭审计。目前支持的值包括："false"-否，"true"-是
        :type IsClosing: str
        :param _CreateTime: 审计服务开通时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogExpireDay = None
        self._LogType = None
        self._IsClosing = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def IsClosing(self):
        return self._IsClosing

    @IsClosing.setter
    def IsClosing(self, IsClosing):
        self._IsClosing = IsClosing

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogExpireDay = params.get("LogExpireDay")
        self._LogType = params.get("LogType")
        self._IsClosing = params.get("IsClosing")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class DescribeAuditLogFilesRequest(AbstractModel):
    """DescribeAuditLogFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Limit: 分页大小参数。默认值为 20，最小值为 1，最大值为 100。
        :type Limit: int
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _FileName: 审计日志文件名。
        :type FileName: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._FileName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogFilesResponse(AbstractModel):
    """DescribeAuditLogFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的审计日志文件个数。
        :type TotalCount: int
        :param _Items: 审计日志文件详情。
        :type Items: list of AuditLogFile
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditLogFile()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditLogsRequest(AbstractModel):
    """DescribeAuditLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _Limit: 分页参数，单次返回的数据条数。默认值为100，最大值为100。
        :type Limit: int
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _Order: 排序方式。支持值包括："ASC" - 升序，"DESC" - 降序。
        :type Order: str
        :param _OrderBy: 排序字段。支持值包括：
"timestamp" - 时间戳；
"affectRows" - 影响行数；
"execTime" - 执行时间。
        :type OrderBy: str
        :param _LogFilter: 过滤条件。可按设置的过滤条件过滤日志。
        :type LogFilter: list of InstanceAuditLogFilters
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._OrderBy = None
        self._LogFilter = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def LogFilter(self):
        return self._LogFilter

    @LogFilter.setter
    def LogFilter(self, LogFilter):
        self._LogFilter = LogFilter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        if params.get("LogFilter") is not None:
            self._LogFilter = []
            for item in params.get("LogFilter"):
                obj = InstanceAuditLogFilters()
                obj._deserialize(item)
                self._LogFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogsResponse(AbstractModel):
    """DescribeAuditLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的审计日志条数。
        :type TotalCount: int
        :param _Items: 审计日志详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditLog
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditLog()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditPoliciesRequest(AbstractModel):
    """DescribeAuditPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _PolicyId: 审计策略 ID。
        :type PolicyId: str
        :param _PolicyName: 审计策略名称。支持按审计策略名称进行模糊匹配查询。
        :type PolicyName: str
        :param _Limit: 分页大小参数。默认值为 20，最小值为 1，最大值为 100。
        :type Limit: int
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _RuleId: 审计规则 ID。可使用该审计规则 ID 查询到其关联的审计策略。
注意，参数 RuleId，InstanceId，PolicyId，PolicyName 必须至少传一个。
        :type RuleId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._PolicyId = None
        self._PolicyName = None
        self._Limit = None
        self._Offset = None
        self._RuleId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

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
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RuleId = params.get("RuleId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditPoliciesResponse(AbstractModel):
    """DescribeAuditPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的审计策略个数。
        :type TotalCount: int
        :param _Items: 审计策略详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditPolicy
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditPolicy()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditRulesRequest(AbstractModel):
    """DescribeAuditRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 审计规则 ID。
        :type RuleId: str
        :param _RuleName: 审计规则名称。支持按审计规则名称进行模糊匹配查询。
        :type RuleName: str
        :param _Limit: 分页大小参数。默认值为 20，最小值为 1，最大值为 100。
        :type Limit: int
        :param _Offset: 分页偏移量。默认值为0。
        :type Offset: int
        """
        self._RuleId = None
        self._RuleName = None
        self._Limit = None
        self._Offset = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

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
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRulesResponse(AbstractModel):
    """DescribeAuditRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的审计规则个数。
        :type TotalCount: int
        :param _Items: 审计规则详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditRule
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeMin: 自动备份开始的最早时间点，单位为时刻。例如，2 - 凌晨 2:00。（该字段已废弃，建议使用 BackupTimeWindow 字段）
        :type StartTimeMin: int
        :param _StartTimeMax: 自动备份开始的最晚时间点，单位为时刻。例如，6 - 凌晨 6:00。（该字段已废弃，建议使用 BackupTimeWindow 字段）
        :type StartTimeMax: int
        :param _BackupExpireDays: 备份文件保留时间，单位为天。
        :type BackupExpireDays: int
        :param _BackupMethod: 备份方式，可能的值为：physical - 物理备份，logical - 逻辑备份。
        :type BackupMethod: str
        :param _BinlogExpireDays: Binlog 文件保留时间，单位为天。
        :type BinlogExpireDays: int
        :param _BackupTimeWindow: 实例自动备份的时间窗。
        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
        :param _EnableBackupPeriodSave: 定期保留开关，off - 不开启定期保留策略，on - 开启定期保留策略，默认为off
        :type EnableBackupPeriodSave: str
        :param _BackupPeriodSaveDays: 定期保留最长天数，最小值：90，最大值：3650，默认值：1080
        :type BackupPeriodSaveDays: int
        :param _BackupPeriodSaveInterval: 定期保留策略周期，可取值：weekly - 周，monthly - 月， quarterly - 季度，yearly - 年，默认为monthly
        :type BackupPeriodSaveInterval: str
        :param _BackupPeriodSaveCount: 定期保留的备份数量，最小值为1，最大值不超过定期保留策略周期内常规备份个数，默认值为1
        :type BackupPeriodSaveCount: int
        :param _StartBackupPeriodSaveDate: 定期保留策略周期起始日期，格式：YYYY-MM-dd HH:mm:ss
        :type StartBackupPeriodSaveDate: str
        :param _EnableBackupArchive: 是否开启数据备份归档策略，off-关闭，on-打开，默认为off
        :type EnableBackupArchive: str
        :param _BackupArchiveDays: 数据备份归档起始天数，数据备份达到归档起始天数时进行归档，最小为180天，不得大于数据备份保留天数
        :type BackupArchiveDays: int
        :param _EnableBinlogArchive: 是否开启日志备份归档策略，off-关闭，on-打开，默认为off
        :type EnableBinlogArchive: str
        :param _BinlogArchiveDays: 日志备份归档起始天数，日志备份达到归档起始天数时进行归档，最小为180天，不得大于日志备份保留天数
        :type BinlogArchiveDays: int
        :param _EnableBackupStandby: 是否开启数据备份标准存储策略，off-关闭，on-打开，默认为off
        :type EnableBackupStandby: str
        :param _BackupStandbyDays: 数据备份标准存储起始天数，数据备份达到标准存储起始天数时进行转换，最小为30天，不得大于数据备份保留天数。如果开启备份归档，不得大于等于备份归档天数
        :type BackupStandbyDays: int
        :param _EnableBinlogStandby: 是否开启日志备份标准存储策略，off-关闭，on-打开，默认为off
        :type EnableBinlogStandby: str
        :param _BinlogStandbyDays: 日志备份标准存储起始天数，日志备份达到标准存储起始天数时进行转换，最小为30天，不得大于日志备份保留天数。如果开启备份归档，不得大于等于备份归档天数
        :type BinlogStandbyDays: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTimeMin = None
        self._StartTimeMax = None
        self._BackupExpireDays = None
        self._BackupMethod = None
        self._BinlogExpireDays = None
        self._BackupTimeWindow = None
        self._EnableBackupPeriodSave = None
        self._BackupPeriodSaveDays = None
        self._BackupPeriodSaveInterval = None
        self._BackupPeriodSaveCount = None
        self._StartBackupPeriodSaveDate = None
        self._EnableBackupArchive = None
        self._BackupArchiveDays = None
        self._EnableBinlogArchive = None
        self._BinlogArchiveDays = None
        self._EnableBackupStandby = None
        self._BackupStandbyDays = None
        self._EnableBinlogStandby = None
        self._BinlogStandbyDays = None
        self._RequestId = None

    @property
    def StartTimeMin(self):
        return self._StartTimeMin

    @StartTimeMin.setter
    def StartTimeMin(self, StartTimeMin):
        self._StartTimeMin = StartTimeMin

    @property
    def StartTimeMax(self):
        return self._StartTimeMax

    @StartTimeMax.setter
    def StartTimeMax(self, StartTimeMax):
        self._StartTimeMax = StartTimeMax

    @property
    def BackupExpireDays(self):
        return self._BackupExpireDays

    @BackupExpireDays.setter
    def BackupExpireDays(self, BackupExpireDays):
        self._BackupExpireDays = BackupExpireDays

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BinlogExpireDays(self):
        return self._BinlogExpireDays

    @BinlogExpireDays.setter
    def BinlogExpireDays(self, BinlogExpireDays):
        self._BinlogExpireDays = BinlogExpireDays

    @property
    def BackupTimeWindow(self):
        return self._BackupTimeWindow

    @BackupTimeWindow.setter
    def BackupTimeWindow(self, BackupTimeWindow):
        self._BackupTimeWindow = BackupTimeWindow

    @property
    def EnableBackupPeriodSave(self):
        return self._EnableBackupPeriodSave

    @EnableBackupPeriodSave.setter
    def EnableBackupPeriodSave(self, EnableBackupPeriodSave):
        self._EnableBackupPeriodSave = EnableBackupPeriodSave

    @property
    def BackupPeriodSaveDays(self):
        return self._BackupPeriodSaveDays

    @BackupPeriodSaveDays.setter
    def BackupPeriodSaveDays(self, BackupPeriodSaveDays):
        self._BackupPeriodSaveDays = BackupPeriodSaveDays

    @property
    def BackupPeriodSaveInterval(self):
        return self._BackupPeriodSaveInterval

    @BackupPeriodSaveInterval.setter
    def BackupPeriodSaveInterval(self, BackupPeriodSaveInterval):
        self._BackupPeriodSaveInterval = BackupPeriodSaveInterval

    @property
    def BackupPeriodSaveCount(self):
        return self._BackupPeriodSaveCount

    @BackupPeriodSaveCount.setter
    def BackupPeriodSaveCount(self, BackupPeriodSaveCount):
        self._BackupPeriodSaveCount = BackupPeriodSaveCount

    @property
    def StartBackupPeriodSaveDate(self):
        return self._StartBackupPeriodSaveDate

    @StartBackupPeriodSaveDate.setter
    def StartBackupPeriodSaveDate(self, StartBackupPeriodSaveDate):
        self._StartBackupPeriodSaveDate = StartBackupPeriodSaveDate

    @property
    def EnableBackupArchive(self):
        return self._EnableBackupArchive

    @EnableBackupArchive.setter
    def EnableBackupArchive(self, EnableBackupArchive):
        self._EnableBackupArchive = EnableBackupArchive

    @property
    def BackupArchiveDays(self):
        return self._BackupArchiveDays

    @BackupArchiveDays.setter
    def BackupArchiveDays(self, BackupArchiveDays):
        self._BackupArchiveDays = BackupArchiveDays

    @property
    def EnableBinlogArchive(self):
        return self._EnableBinlogArchive

    @EnableBinlogArchive.setter
    def EnableBinlogArchive(self, EnableBinlogArchive):
        self._EnableBinlogArchive = EnableBinlogArchive

    @property
    def BinlogArchiveDays(self):
        return self._BinlogArchiveDays

    @BinlogArchiveDays.setter
    def BinlogArchiveDays(self, BinlogArchiveDays):
        self._BinlogArchiveDays = BinlogArchiveDays

    @property
    def EnableBackupStandby(self):
        return self._EnableBackupStandby

    @EnableBackupStandby.setter
    def EnableBackupStandby(self, EnableBackupStandby):
        self._EnableBackupStandby = EnableBackupStandby

    @property
    def BackupStandbyDays(self):
        return self._BackupStandbyDays

    @BackupStandbyDays.setter
    def BackupStandbyDays(self, BackupStandbyDays):
        self._BackupStandbyDays = BackupStandbyDays

    @property
    def EnableBinlogStandby(self):
        return self._EnableBinlogStandby

    @EnableBinlogStandby.setter
    def EnableBinlogStandby(self, EnableBinlogStandby):
        self._EnableBinlogStandby = EnableBinlogStandby

    @property
    def BinlogStandbyDays(self):
        return self._BinlogStandbyDays

    @BinlogStandbyDays.setter
    def BinlogStandbyDays(self, BinlogStandbyDays):
        self._BinlogStandbyDays = BinlogStandbyDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTimeMin = params.get("StartTimeMin")
        self._StartTimeMax = params.get("StartTimeMax")
        self._BackupExpireDays = params.get("BackupExpireDays")
        self._BackupMethod = params.get("BackupMethod")
        self._BinlogExpireDays = params.get("BinlogExpireDays")
        if params.get("BackupTimeWindow") is not None:
            self._BackupTimeWindow = CommonTimeWindow()
            self._BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
        self._EnableBackupPeriodSave = params.get("EnableBackupPeriodSave")
        self._BackupPeriodSaveDays = params.get("BackupPeriodSaveDays")
        self._BackupPeriodSaveInterval = params.get("BackupPeriodSaveInterval")
        self._BackupPeriodSaveCount = params.get("BackupPeriodSaveCount")
        self._StartBackupPeriodSaveDate = params.get("StartBackupPeriodSaveDate")
        self._EnableBackupArchive = params.get("EnableBackupArchive")
        self._BackupArchiveDays = params.get("BackupArchiveDays")
        self._EnableBinlogArchive = params.get("EnableBinlogArchive")
        self._BinlogArchiveDays = params.get("BinlogArchiveDays")
        self._EnableBackupStandby = params.get("EnableBackupStandby")
        self._BackupStandbyDays = params.get("BackupStandbyDays")
        self._EnableBinlogStandby = params.get("EnableBinlogStandby")
        self._BinlogStandbyDays = params.get("BinlogStandbyDays")
        self._RequestId = params.get("RequestId")


class DescribeBackupDatabasesRequest(AbstractModel):
    """DescribeBackupDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _StartTime: 开始时间，格式为：2017-07-12 10:29:20。
        :type StartTime: str
        :param _SearchDatabase: 要查询的数据库名前缀。
        :type SearchDatabase: str
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _Limit: 分页大小，最小值为1，最大值为2000。
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._SearchDatabase = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def SearchDatabase(self):
        return self._SearchDatabase

    @SearchDatabase.setter
    def SearchDatabase(self, SearchDatabase):
        self._SearchDatabase = SearchDatabase

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
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._SearchDatabase = params.get("SearchDatabase")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDatabasesResponse(AbstractModel):
    """DescribeBackupDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的数据个数。
        :type TotalCount: int
        :param _Items: 符合查询条件的数据库数组。
        :type Items: list of DatabaseName
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DatabaseName()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupDecryptionKeyRequest(AbstractModel):
    """DescribeBackupDecryptionKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-XXXX。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _BackupId: 实例的备份ID，可通过DescribeBackups接口查询备份的ID。
        :type BackupId: int
        """
        self._InstanceId = None
        self._BackupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDecryptionKeyResponse(AbstractModel):
    """DescribeBackupDecryptionKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DecryptionKey: 备份文件解密密钥。
        :type DecryptionKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DecryptionKey = None
        self._RequestId = None

    @property
    def DecryptionKey(self):
        return self._DecryptionKey

    @DecryptionKey.setter
    def DecryptionKey(self, DecryptionKey):
        self._DecryptionKey = DecryptionKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DecryptionKey = params.get("DecryptionKey")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadRestriction请求参数结构体

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadRestriction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LimitType: NoLimit 不限制,内外网都可以下载； LimitOnlyIntranet 仅内网可下载； Customize 用户自定义vpc:ip可下载。 只有该值为 Customize 时， LimitVpc 和 LimitIp 才有意义。
        :type LimitType: str
        :param _VpcComparisonSymbol: 该参数仅支持 In， 表示 LimitVpc 指定的vpc可以下载。
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: In: 指定的ip可以下载； NotIn: 指定的ip不可以下载。
        :type IpComparisonSymbol: str
        :param _LimitVpc: 限制下载的vpc设置。
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: 限制下载的ip设置。
        :type LimitIp: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None
        self._RequestId = None

    @property
    def LimitType(self):
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        self._RequestId = params.get("RequestId")


class DescribeBackupEncryptionStatusRequest(AbstractModel):
    """DescribeBackupEncryptionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-XXXX。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupEncryptionStatusResponse(AbstractModel):
    """DescribeBackupEncryptionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EncryptionStatus: 实例是否开启了物理备份加密。可能的值有 on, off 。
        :type EncryptionStatus: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EncryptionStatus = None
        self._RequestId = None

    @property
    def EncryptionStatus(self):
        return self._EncryptionStatus

    @EncryptionStatus.setter
    def EncryptionStatus(self, EncryptionStatus):
        self._EncryptionStatus = EncryptionStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EncryptionStatus = params.get("EncryptionStatus")
        self._RequestId = params.get("RequestId")


class DescribeBackupOverviewRequest(AbstractModel):
    """DescribeBackupOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 需要查询的云数据库产品类型，目前仅支持 "mysql"。
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupOverviewResponse(AbstractModel):
    """DescribeBackupOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupCount: 用户在当前地域备份的总个数（包含数据备份和日志备份）。
        :type BackupCount: int
        :param _BackupVolume: 用户在当前地域备份的总容量
        :type BackupVolume: int
        :param _BillingVolume: 用户在当前地域备份的计费容量，即超出赠送容量的部分。
        :type BillingVolume: int
        :param _FreeVolume: 用户在当前地域获得的赠送备份容量。
        :type FreeVolume: int
        :param _RemoteBackupVolume: 用户在当前地域的异地备份总容量。
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoteBackupVolume: int
        :param _BackupArchiveVolume: 归档备份容量，包含数据备份以及日志备份。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupArchiveVolume: int
        :param _BackupStandbyVolume: 标准存储备份容量，包含数据备份以及日志备份。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStandbyVolume: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupCount = None
        self._BackupVolume = None
        self._BillingVolume = None
        self._FreeVolume = None
        self._RemoteBackupVolume = None
        self._BackupArchiveVolume = None
        self._BackupStandbyVolume = None
        self._RequestId = None

    @property
    def BackupCount(self):
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount

    @property
    def BackupVolume(self):
        return self._BackupVolume

    @BackupVolume.setter
    def BackupVolume(self, BackupVolume):
        self._BackupVolume = BackupVolume

    @property
    def BillingVolume(self):
        return self._BillingVolume

    @BillingVolume.setter
    def BillingVolume(self, BillingVolume):
        self._BillingVolume = BillingVolume

    @property
    def FreeVolume(self):
        return self._FreeVolume

    @FreeVolume.setter
    def FreeVolume(self, FreeVolume):
        self._FreeVolume = FreeVolume

    @property
    def RemoteBackupVolume(self):
        return self._RemoteBackupVolume

    @RemoteBackupVolume.setter
    def RemoteBackupVolume(self, RemoteBackupVolume):
        self._RemoteBackupVolume = RemoteBackupVolume

    @property
    def BackupArchiveVolume(self):
        return self._BackupArchiveVolume

    @BackupArchiveVolume.setter
    def BackupArchiveVolume(self, BackupArchiveVolume):
        self._BackupArchiveVolume = BackupArchiveVolume

    @property
    def BackupStandbyVolume(self):
        return self._BackupStandbyVolume

    @BackupStandbyVolume.setter
    def BackupStandbyVolume(self, BackupStandbyVolume):
        self._BackupStandbyVolume = BackupStandbyVolume

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupCount = params.get("BackupCount")
        self._BackupVolume = params.get("BackupVolume")
        self._BillingVolume = params.get("BillingVolume")
        self._FreeVolume = params.get("FreeVolume")
        self._RemoteBackupVolume = params.get("RemoteBackupVolume")
        self._BackupArchiveVolume = params.get("BackupArchiveVolume")
        self._BackupStandbyVolume = params.get("BackupStandbyVolume")
        self._RequestId = params.get("RequestId")


class DescribeBackupSummariesRequest(AbstractModel):
    """DescribeBackupSummaries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 需要查询的云数据库产品类型，目前仅支持 "mysql"。
        :type Product: str
        :param _Offset: 分页查询数据的偏移量，默认为0。
        :type Offset: int
        :param _Limit: 分页查询数据的条目限制，默认值为20。最小值为1，最大值为100。
        :type Limit: int
        :param _OrderBy: 指定按某一项排序，可选值包括： BackupVolume: 备份容量， DataBackupVolume: 数据备份容量， BinlogBackupVolume: 日志备份容量， AutoBackupVolume: 自动备份容量， ManualBackupVolume: 手动备份容量。默认按照BackupVolume排序。
        :type OrderBy: str
        :param _OrderDirection: 指定排序方向，可选值包括： ASC: 正序， DESC: 逆序。默认值为 ASC。
        :type OrderDirection: str
        """
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderDirection = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupSummariesResponse(AbstractModel):
    """DescribeBackupSummaries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 实例备份统计条目。
        :type Items: list of BackupSummaryItem
        :param _TotalCount: 实例备份统计总条目数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackupSummaryItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Offset: 偏移量，最小值为0。
        :type Offset: int
        :param _Limit: 分页大小，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param _Items: 符合查询条件的备份信息详情。
        :type Items: list of BackupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackupInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBinlogBackupOverviewRequest(AbstractModel):
    """DescribeBinlogBackupOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 需要查询的云数据库产品类型，目前仅支持 "mysql"。
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogBackupOverviewResponse(AbstractModel):
    """DescribeBinlogBackupOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BinlogBackupVolume: 总的日志备份容量，包含异地日志备份（单位为字节）。
        :type BinlogBackupVolume: int
        :param _BinlogBackupCount: 总的日志备份个数，包含异地日志备份。
        :type BinlogBackupCount: int
        :param _RemoteBinlogVolume: 异地日志备份容量（单位为字节）。
        :type RemoteBinlogVolume: int
        :param _RemoteBinlogCount: 异地日志备份个数。
        :type RemoteBinlogCount: int
        :param _BinlogArchiveVolume: 归档日志备份容量（单位为字节）。
        :type BinlogArchiveVolume: int
        :param _BinlogArchiveCount: 归档日志备份个数。
        :type BinlogArchiveCount: int
        :param _BinlogStandbyVolume: 标准存储日志备份容量（单位为字节）。
        :type BinlogStandbyVolume: int
        :param _BinlogStandbyCount: 标准存储日志备份个数。
        :type BinlogStandbyCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BinlogBackupVolume = None
        self._BinlogBackupCount = None
        self._RemoteBinlogVolume = None
        self._RemoteBinlogCount = None
        self._BinlogArchiveVolume = None
        self._BinlogArchiveCount = None
        self._BinlogStandbyVolume = None
        self._BinlogStandbyCount = None
        self._RequestId = None

    @property
    def BinlogBackupVolume(self):
        return self._BinlogBackupVolume

    @BinlogBackupVolume.setter
    def BinlogBackupVolume(self, BinlogBackupVolume):
        self._BinlogBackupVolume = BinlogBackupVolume

    @property
    def BinlogBackupCount(self):
        return self._BinlogBackupCount

    @BinlogBackupCount.setter
    def BinlogBackupCount(self, BinlogBackupCount):
        self._BinlogBackupCount = BinlogBackupCount

    @property
    def RemoteBinlogVolume(self):
        return self._RemoteBinlogVolume

    @RemoteBinlogVolume.setter
    def RemoteBinlogVolume(self, RemoteBinlogVolume):
        self._RemoteBinlogVolume = RemoteBinlogVolume

    @property
    def RemoteBinlogCount(self):
        return self._RemoteBinlogCount

    @RemoteBinlogCount.setter
    def RemoteBinlogCount(self, RemoteBinlogCount):
        self._RemoteBinlogCount = RemoteBinlogCount

    @property
    def BinlogArchiveVolume(self):
        return self._BinlogArchiveVolume

    @BinlogArchiveVolume.setter
    def BinlogArchiveVolume(self, BinlogArchiveVolume):
        self._BinlogArchiveVolume = BinlogArchiveVolume

    @property
    def BinlogArchiveCount(self):
        return self._BinlogArchiveCount

    @BinlogArchiveCount.setter
    def BinlogArchiveCount(self, BinlogArchiveCount):
        self._BinlogArchiveCount = BinlogArchiveCount

    @property
    def BinlogStandbyVolume(self):
        return self._BinlogStandbyVolume

    @BinlogStandbyVolume.setter
    def BinlogStandbyVolume(self, BinlogStandbyVolume):
        self._BinlogStandbyVolume = BinlogStandbyVolume

    @property
    def BinlogStandbyCount(self):
        return self._BinlogStandbyCount

    @BinlogStandbyCount.setter
    def BinlogStandbyCount(self, BinlogStandbyCount):
        self._BinlogStandbyCount = BinlogStandbyCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BinlogBackupVolume = params.get("BinlogBackupVolume")
        self._BinlogBackupCount = params.get("BinlogBackupCount")
        self._RemoteBinlogVolume = params.get("RemoteBinlogVolume")
        self._RemoteBinlogCount = params.get("RemoteBinlogCount")
        self._BinlogArchiveVolume = params.get("BinlogArchiveVolume")
        self._BinlogArchiveCount = params.get("BinlogArchiveCount")
        self._BinlogStandbyVolume = params.get("BinlogStandbyVolume")
        self._BinlogStandbyCount = params.get("BinlogStandbyCount")
        self._RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Offset: 偏移量，最小值为0。
        :type Offset: int
        :param _Limit: 分页大小，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param _MinStartTime: binlog最早开始时间，时间格式：2016-03-17 02:10:37
        :type MinStartTime: str
        :param _MaxStartTime: binlog最晚开始时间，时间格式：2016-03-17 02:10:37
        :type MaxStartTime: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._MinStartTime = None
        self._MaxStartTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def MinStartTime(self):
        return self._MinStartTime

    @MinStartTime.setter
    def MinStartTime(self, MinStartTime):
        self._MinStartTime = MinStartTime

    @property
    def MaxStartTime(self):
        return self._MaxStartTime

    @MaxStartTime.setter
    def MaxStartTime(self, MaxStartTime):
        self._MaxStartTime = MaxStartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MinStartTime = params.get("MinStartTime")
        self._MaxStartTime = params.get("MaxStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的日志文件总数。
        :type TotalCount: int
        :param _Items: 符合查询条件的二进制日志文件详情。
        :type Items: list of BinlogInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BinlogInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdbProxyInfoRequest(AbstractModel):
    """DescribeCdbProxyInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdbProxyInfoResponse(AbstractModel):
    """DescribeCdbProxyInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 代理组数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _ProxyInfos: 代理组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyInfos: list of ProxyGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._ProxyInfos = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProxyInfos(self):
        return self._ProxyInfos

    @ProxyInfos.setter
    def ProxyInfos(self, ProxyInfos):
        self._ProxyInfos = ProxyInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("ProxyInfos") is not None:
            self._ProxyInfos = []
            for item in params.get("ProxyInfos"):
                obj = ProxyGroupInfo()
                obj._deserialize(item)
                self._ProxyInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdbZoneConfigRequest(AbstractModel):
    """DescribeCdbZoneConfig请求参数结构体

    """


class DescribeCdbZoneConfigResponse(AbstractModel):
    """DescribeCdbZoneConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataResult: 售卖规格和地域信息集合
        :type DataResult: :class:`tencentcloud.cdb.v20170320.models.CdbZoneDataResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataResult = None
        self._RequestId = None

    @property
    def DataResult(self):
        return self._DataResult

    @DataResult.setter
    def DataResult(self, DataResult):
        self._DataResult = DataResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataResult") is not None:
            self._DataResult = CdbZoneDataResult()
            self._DataResult._deserialize(params.get("DataResult"))
        self._RequestId = params.get("RequestId")


class DescribeCloneListRequest(AbstractModel):
    """DescribeCloneList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 查询指定源实例的克隆任务列表。
        :type InstanceId: str
        :param _Offset: 分页查询时的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页查询时的每页条目数，默认值为20。
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloneListResponse(AbstractModel):
    """DescribeCloneList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足条件的条目数。
        :type TotalCount: int
        :param _Items: 克隆任务列表。
        :type Items: list of CloneItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = CloneItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBFeaturesRequest(AbstractModel):
    """DescribeDBFeatures请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBFeaturesResponse(AbstractModel):
    """DescribeDBFeatures返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSupportAudit: 是否支持数据库审计功能。
        :type IsSupportAudit: bool
        :param _AuditNeedUpgrade: 开启审计是否需要升级内核版本。
        :type AuditNeedUpgrade: bool
        :param _IsSupportEncryption: 是否支持数据库加密功能。
        :type IsSupportEncryption: bool
        :param _EncryptionNeedUpgrade: 开启加密是否需要升级内核版本。
        :type EncryptionNeedUpgrade: bool
        :param _IsRemoteRo: 是否为异地只读实例。
        :type IsRemoteRo: bool
        :param _MasterRegion: 主实例所在地域。
        :type MasterRegion: str
        :param _IsSupportUpdateSubVersion: 是否支持小版本升级。
        :type IsSupportUpdateSubVersion: bool
        :param _CurrentSubVersion: 当前内核版本。
        :type CurrentSubVersion: str
        :param _TargetSubVersion: 可供升级的内核版本。
        :type TargetSubVersion: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsSupportAudit = None
        self._AuditNeedUpgrade = None
        self._IsSupportEncryption = None
        self._EncryptionNeedUpgrade = None
        self._IsRemoteRo = None
        self._MasterRegion = None
        self._IsSupportUpdateSubVersion = None
        self._CurrentSubVersion = None
        self._TargetSubVersion = None
        self._RequestId = None

    @property
    def IsSupportAudit(self):
        return self._IsSupportAudit

    @IsSupportAudit.setter
    def IsSupportAudit(self, IsSupportAudit):
        self._IsSupportAudit = IsSupportAudit

    @property
    def AuditNeedUpgrade(self):
        return self._AuditNeedUpgrade

    @AuditNeedUpgrade.setter
    def AuditNeedUpgrade(self, AuditNeedUpgrade):
        self._AuditNeedUpgrade = AuditNeedUpgrade

    @property
    def IsSupportEncryption(self):
        return self._IsSupportEncryption

    @IsSupportEncryption.setter
    def IsSupportEncryption(self, IsSupportEncryption):
        self._IsSupportEncryption = IsSupportEncryption

    @property
    def EncryptionNeedUpgrade(self):
        return self._EncryptionNeedUpgrade

    @EncryptionNeedUpgrade.setter
    def EncryptionNeedUpgrade(self, EncryptionNeedUpgrade):
        self._EncryptionNeedUpgrade = EncryptionNeedUpgrade

    @property
    def IsRemoteRo(self):
        return self._IsRemoteRo

    @IsRemoteRo.setter
    def IsRemoteRo(self, IsRemoteRo):
        self._IsRemoteRo = IsRemoteRo

    @property
    def MasterRegion(self):
        return self._MasterRegion

    @MasterRegion.setter
    def MasterRegion(self, MasterRegion):
        self._MasterRegion = MasterRegion

    @property
    def IsSupportUpdateSubVersion(self):
        return self._IsSupportUpdateSubVersion

    @IsSupportUpdateSubVersion.setter
    def IsSupportUpdateSubVersion(self, IsSupportUpdateSubVersion):
        self._IsSupportUpdateSubVersion = IsSupportUpdateSubVersion

    @property
    def CurrentSubVersion(self):
        return self._CurrentSubVersion

    @CurrentSubVersion.setter
    def CurrentSubVersion(self, CurrentSubVersion):
        self._CurrentSubVersion = CurrentSubVersion

    @property
    def TargetSubVersion(self):
        return self._TargetSubVersion

    @TargetSubVersion.setter
    def TargetSubVersion(self, TargetSubVersion):
        self._TargetSubVersion = TargetSubVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSupportAudit = params.get("IsSupportAudit")
        self._AuditNeedUpgrade = params.get("AuditNeedUpgrade")
        self._IsSupportEncryption = params.get("IsSupportEncryption")
        self._EncryptionNeedUpgrade = params.get("EncryptionNeedUpgrade")
        self._IsRemoteRo = params.get("IsRemoteRo")
        self._MasterRegion = params.get("MasterRegion")
        self._IsSupportUpdateSubVersion = params.get("IsSupportUpdateSubVersion")
        self._CurrentSubVersion = params.get("CurrentSubVersion")
        self._TargetSubVersion = params.get("TargetSubVersion")
        self._RequestId = params.get("RequestId")


class DescribeDBImportRecordsRequest(AbstractModel):
    """DescribeDBImportRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _StartTime: 开始时间，时间格式如：2016-01-01 00:00:01。
        :type StartTime: str
        :param _EndTime: 结束时间，时间格式如：2016-01-01 23:59:59。
        :type EndTime: str
        :param _Offset: 分页参数，偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页参数，单次请求返回的数量，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
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
        


class DescribeDBImportRecordsResponse(AbstractModel):
    """DescribeDBImportRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的导入任务操作日志总数。
        :type TotalCount: int
        :param _Items: 返回的导入操作记录列表。
        :type Items: list of ImportRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ImportRecord()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceCharsetRequest(AbstractModel):
    """DescribeDBInstanceCharset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceCharsetResponse(AbstractModel):
    """DescribeDBInstanceCharset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Charset: 实例的默认字符集，如 "latin1"，"utf8" 等。
        :type Charset: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Charset = None
        self._RequestId = None

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Charset = params.get("Charset")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceConfigRequest(AbstractModel):
    """DescribeDBInstanceConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceConfigResponse(AbstractModel):
    """DescribeDBInstanceConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectMode: 主实例数据保护方式，可能的返回值：0 - 异步复制方式，1 - 半同步复制方式，2 - 强同步复制方式。
        :type ProtectMode: int
        :param _DeployMode: 主实例部署方式，可能的返回值：0 - 单可用部署，1 - 多可用区部署。
        :type DeployMode: int
        :param _Zone: 实例可用区信息，格式如 "ap-shanghai-1"。
        :type Zone: str
        :param _SlaveConfig: 备库的配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveConfig: :class:`tencentcloud.cdb.v20170320.models.SlaveConfig`
        :param _BackupConfig: 强同步实例第二备库的配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupConfig: :class:`tencentcloud.cdb.v20170320.models.BackupConfig`
        :param _Switched: 是否切换备库。
        :type Switched: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProtectMode = None
        self._DeployMode = None
        self._Zone = None
        self._SlaveConfig = None
        self._BackupConfig = None
        self._Switched = None
        self._RequestId = None

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SlaveConfig(self):
        return self._SlaveConfig

    @SlaveConfig.setter
    def SlaveConfig(self, SlaveConfig):
        self._SlaveConfig = SlaveConfig

    @property
    def BackupConfig(self):
        return self._BackupConfig

    @BackupConfig.setter
    def BackupConfig(self, BackupConfig):
        self._BackupConfig = BackupConfig

    @property
    def Switched(self):
        return self._Switched

    @Switched.setter
    def Switched(self, Switched):
        self._Switched = Switched

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._Zone = params.get("Zone")
        if params.get("SlaveConfig") is not None:
            self._SlaveConfig = SlaveConfig()
            self._SlaveConfig._deserialize(params.get("SlaveConfig"))
        if params.get("BackupConfig") is not None:
            self._BackupConfig = BackupConfig()
            self._BackupConfig._deserialize(params.get("BackupConfig"))
        self._Switched = params.get("Switched")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceGTIDRequest(AbstractModel):
    """DescribeDBInstanceGTID请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceGTIDResponse(AbstractModel):
    """DescribeDBInstanceGTID返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsGTIDOpen: GTID 是否开通的标记，可能的取值为：0 - 未开通，1 - 已开通。
        :type IsGTIDOpen: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsGTIDOpen = None
        self._RequestId = None

    @property
    def IsGTIDOpen(self):
        return self._IsGTIDOpen

    @IsGTIDOpen.setter
    def IsGTIDOpen(self, IsGTIDOpen):
        self._IsGTIDOpen = IsGTIDOpen

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsGTIDOpen = params.get("IsGTIDOpen")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceInfoRequest(AbstractModel):
    """DescribeDBInstanceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceInfoResponse(AbstractModel):
    """DescribeDBInstanceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Encryption: 是否开通加密，YES 已开通，NO 未开通。
        :type Encryption: str
        :param _KeyId: 加密使用的密钥 ID 。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param _KeyRegion: 密钥所在地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyRegion: str
        :param _DefaultKmsRegion: 当前 CDB 后端服务使用的 KMS 服务的默认地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultKmsRegion: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Encryption = None
        self._KeyId = None
        self._KeyRegion = None
        self._DefaultKmsRegion = None
        self._RequestId = None

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
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyRegion(self):
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion

    @property
    def DefaultKmsRegion(self):
        return self._DefaultKmsRegion

    @DefaultKmsRegion.setter
    def DefaultKmsRegion(self, DefaultKmsRegion):
        self._DefaultKmsRegion = DefaultKmsRegion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Encryption = params.get("Encryption")
        self._KeyId = params.get("KeyId")
        self._KeyRegion = params.get("KeyRegion")
        self._DefaultKmsRegion = params.get("DefaultKmsRegion")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceRebootTimeRequest(AbstractModel):
    """DescribeDBInstanceRebootTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceRebootTimeResponse(AbstractModel):
    """DescribeDBInstanceRebootTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param _Items: 返回的参数信息。
        :type Items: list of InstanceRebootTime
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceRebootTime()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _InstanceTypes: 实例类型，可取值：1 - 主实例，2 - 灾备实例，3 - 只读实例。
        :type InstanceTypes: list of int non-negative
        :param _Vips: 实例的内网 IP 地址。
        :type Vips: list of str
        :param _Status: 实例状态，可取值：<br>0 - 创建中<br>1 - 运行中<br>4 - 正在进行隔离操作<br>5 - 已隔离（可在回收站恢复开机）
        :type Status: list of int non-negative
        :param _Offset: 偏移量，默认值为 0。
        :type Offset: int
        :param _Limit: 单次请求返回的数量，默认值为 20，最大值为 2000。
        :type Limit: int
        :param _SecurityGroupId: 安全组 ID。当使用安全组 ID 为过滤条件时，需指定 WithSecurityGroup 参数为 1。
        :type SecurityGroupId: str
        :param _PayTypes: 付费类型，可取值：0 - 包年包月，1 - 小时计费。
        :type PayTypes: list of int non-negative
        :param _InstanceNames: 实例名称。
        :type InstanceNames: list of str
        :param _TaskStatus: 实例任务状态，可能取值：<br>0 - 没有任务<br>1 - 升级中<br>2 - 数据导入中<br>3 - 开放Slave中<br>4 - 外网访问开通中<br>5 - 批量操作执行中<br>6 - 回档中<br>7 - 外网访问关闭中<br>8 - 密码修改中<br>9 - 实例名修改中<br>10 - 重启中<br>12 - 自建迁移中<br>13 - 删除库表中<br>14 - 灾备实例创建同步中<br>15 - 升级待切换<br>16 - 升级切换中<br>17 - 升级切换完成<br>19 - 参数设置待执行
        :type TaskStatus: list of int non-negative
        :param _EngineVersions: 实例数据库引擎版本，可能取值：5.1、5.5、5.6 和 5.7。
        :type EngineVersions: list of str
        :param _VpcIds: 私有网络的 ID。
        :type VpcIds: list of int non-negative
        :param _ZoneIds: 可用区的 ID。
        :type ZoneIds: list of int non-negative
        :param _SubnetIds: 子网 ID。
        :type SubnetIds: list of int non-negative
        :param _CdbErrors: 是否锁定标记，可选值：0 - 不锁定，1 - 锁定，默认为0。
        :type CdbErrors: list of int
        :param _OrderBy: 返回结果集排序的字段，目前支持："InstanceId"，"InstanceName"，"CreateTime"，"DeadlineTime"。
        :type OrderBy: str
        :param _OrderDirection: 返回结果集排序方式，目前支持："ASC" 或者 "DESC"。
        :type OrderDirection: str
        :param _WithSecurityGroup: 是否以安全组 ID 为过滤条件。
        :type WithSecurityGroup: int
        :param _WithExCluster: 是否包含独享集群详细信息，可取值：0 - 不包含，1 - 包含。
        :type WithExCluster: int
        :param _ExClusterId: 独享集群 ID。
        :type ExClusterId: str
        :param _InstanceIds: 实例 ID。
        :type InstanceIds: list of str
        :param _InitFlag: 初始化标记，可取值：0 - 未初始化，1 - 初始化。
        :type InitFlag: int
        :param _WithDr: 是否包含灾备关系对应的实例，可取值：0 - 不包含，1 - 包含。默认取值为1。如果拉取主实例，则灾备关系的数据在DrInfo字段中， 如果拉取灾备实例， 则灾备关系的数据在MasterInfo字段中。灾备关系中只包含部分基本的数据，详细的数据需要自行调接口拉取。
        :type WithDr: int
        :param _WithRo: 是否包含只读实例，可取值：0 - 不包含，1 - 包含。默认取值为1。
        :type WithRo: int
        :param _WithMaster: 是否包含主实例，可取值：0 - 不包含，1 - 包含。默认取值为1。
        :type WithMaster: int
        :param _DeployGroupIds: 置放群组ID列表。
        :type DeployGroupIds: list of str
        :param _TagKeysForSearch: 是否以标签键为过滤条件。
        :type TagKeysForSearch: list of str
        :param _CageIds: 金融围拢 ID 。
        :type CageIds: list of str
        :param _TagValues: 标签值
        :type TagValues: list of str
        :param _UniqueVpcIds: 私有网络字符型vpcId
        :type UniqueVpcIds: list of str
        :param _UniqSubnetIds: 私有网络字符型subnetId
        :type UniqSubnetIds: list of str
        :param _Tags: 标签键值
        :type Tags: list of Tag
        :param _ProxyVips: 数据库代理 IP 。
        :type ProxyVips: list of str
        :param _ProxyIds: 数据库代理 ID 。
        :type ProxyIds: list of str
        :param _EngineTypes: 数据库引擎类型。
        :type EngineTypes: list of str
        """
        self._ProjectId = None
        self._InstanceTypes = None
        self._Vips = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._SecurityGroupId = None
        self._PayTypes = None
        self._InstanceNames = None
        self._TaskStatus = None
        self._EngineVersions = None
        self._VpcIds = None
        self._ZoneIds = None
        self._SubnetIds = None
        self._CdbErrors = None
        self._OrderBy = None
        self._OrderDirection = None
        self._WithSecurityGroup = None
        self._WithExCluster = None
        self._ExClusterId = None
        self._InstanceIds = None
        self._InitFlag = None
        self._WithDr = None
        self._WithRo = None
        self._WithMaster = None
        self._DeployGroupIds = None
        self._TagKeysForSearch = None
        self._CageIds = None
        self._TagValues = None
        self._UniqueVpcIds = None
        self._UniqSubnetIds = None
        self._Tags = None
        self._ProxyVips = None
        self._ProxyIds = None
        self._EngineTypes = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def PayTypes(self):
        return self._PayTypes

    @PayTypes.setter
    def PayTypes(self, PayTypes):
        self._PayTypes = PayTypes

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def EngineVersions(self):
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def VpcIds(self):
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def CdbErrors(self):
        return self._CdbErrors

    @CdbErrors.setter
    def CdbErrors(self, CdbErrors):
        self._CdbErrors = CdbErrors

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def WithSecurityGroup(self):
        return self._WithSecurityGroup

    @WithSecurityGroup.setter
    def WithSecurityGroup(self, WithSecurityGroup):
        self._WithSecurityGroup = WithSecurityGroup

    @property
    def WithExCluster(self):
        return self._WithExCluster

    @WithExCluster.setter
    def WithExCluster(self, WithExCluster):
        self._WithExCluster = WithExCluster

    @property
    def ExClusterId(self):
        return self._ExClusterId

    @ExClusterId.setter
    def ExClusterId(self, ExClusterId):
        self._ExClusterId = ExClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InitFlag(self):
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def WithDr(self):
        return self._WithDr

    @WithDr.setter
    def WithDr(self, WithDr):
        self._WithDr = WithDr

    @property
    def WithRo(self):
        return self._WithRo

    @WithRo.setter
    def WithRo(self, WithRo):
        self._WithRo = WithRo

    @property
    def WithMaster(self):
        return self._WithMaster

    @WithMaster.setter
    def WithMaster(self, WithMaster):
        self._WithMaster = WithMaster

    @property
    def DeployGroupIds(self):
        return self._DeployGroupIds

    @DeployGroupIds.setter
    def DeployGroupIds(self, DeployGroupIds):
        self._DeployGroupIds = DeployGroupIds

    @property
    def TagKeysForSearch(self):
        return self._TagKeysForSearch

    @TagKeysForSearch.setter
    def TagKeysForSearch(self, TagKeysForSearch):
        self._TagKeysForSearch = TagKeysForSearch

    @property
    def CageIds(self):
        return self._CageIds

    @CageIds.setter
    def CageIds(self, CageIds):
        self._CageIds = CageIds

    @property
    def TagValues(self):
        return self._TagValues

    @TagValues.setter
    def TagValues(self, TagValues):
        self._TagValues = TagValues

    @property
    def UniqueVpcIds(self):
        return self._UniqueVpcIds

    @UniqueVpcIds.setter
    def UniqueVpcIds(self, UniqueVpcIds):
        self._UniqueVpcIds = UniqueVpcIds

    @property
    def UniqSubnetIds(self):
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProxyVips(self):
        return self._ProxyVips

    @ProxyVips.setter
    def ProxyVips(self, ProxyVips):
        self._ProxyVips = ProxyVips

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def EngineTypes(self):
        return self._EngineTypes

    @EngineTypes.setter
    def EngineTypes(self, EngineTypes):
        self._EngineTypes = EngineTypes


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Vips = params.get("Vips")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._PayTypes = params.get("PayTypes")
        self._InstanceNames = params.get("InstanceNames")
        self._TaskStatus = params.get("TaskStatus")
        self._EngineVersions = params.get("EngineVersions")
        self._VpcIds = params.get("VpcIds")
        self._ZoneIds = params.get("ZoneIds")
        self._SubnetIds = params.get("SubnetIds")
        self._CdbErrors = params.get("CdbErrors")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        self._WithSecurityGroup = params.get("WithSecurityGroup")
        self._WithExCluster = params.get("WithExCluster")
        self._ExClusterId = params.get("ExClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._InitFlag = params.get("InitFlag")
        self._WithDr = params.get("WithDr")
        self._WithRo = params.get("WithRo")
        self._WithMaster = params.get("WithMaster")
        self._DeployGroupIds = params.get("DeployGroupIds")
        self._TagKeysForSearch = params.get("TagKeysForSearch")
        self._CageIds = params.get("CageIds")
        self._TagValues = params.get("TagValues")
        self._UniqueVpcIds = params.get("UniqueVpcIds")
        self._UniqSubnetIds = params.get("UniqSubnetIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ProxyVips = params.get("ProxyVips")
        self._ProxyIds = params.get("ProxyIds")
        self._EngineTypes = params.get("EngineTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param _Items: 实例详细信息列表。
        :type Items: list of InstanceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBPriceRequest(AbstractModel):
    """DescribeDBPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 实例时长，单位：月，最小值 1，最大值为 36；查询按量计费价格时，该字段无效。
        :type Period: int
        :param _Zone: 可用区信息，格式如 "ap-guangzhou-2"。具体能设置的值请通过 <a href="https://cloud.tencent.com/document/api/236/17229">DescribeDBZoneConfig</a> 接口查询。InstanceId为空时该参数为必填项。
        :type Zone: str
        :param _GoodsNum: 实例数量，默认值为 1，最小值 1，最大值为 100。InstanceId为空时该参数为必填项。
        :type GoodsNum: int
        :param _Memory: 实例内存大小，单位：MB。InstanceId为空时该参数为必填项。
        :type Memory: int
        :param _Volume: 实例硬盘大小，单位：GB。InstanceId为空时该参数为必填项。
        :type Volume: int
        :param _InstanceRole: 实例类型，默认为 master，支持值包括：master - 表示主实例，ro - 表示只读实例，dr - 表示灾备实例。InstanceId为空时该参数为必填项。
        :type InstanceRole: str
        :param _PayType: 付费类型，支持值包括：PRE_PAID - 包年包月，HOUR_PAID - 按量计费。InstanceId为空时该参数为必填项。
        :type PayType: str
        :param _ProtectMode: 数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制。
        :type ProtectMode: int
        :param _DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC_V2" - 单节点云盘版实例。 不指定则默认为通用型实例。
        :type DeviceType: str
        :param _InstanceNodes: 实例节点数。对于 RO 和 基础版实例， 该值默认为1。 如果需要询价三节点实例， 请将该值设置为3。其余主实例该值默认为2。
        :type InstanceNodes: int
        :param _Cpu: 询价实例的CPU核心数目，单位：核，为保证传入 CPU 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可售卖的核心数目，当未指定该值时，将按照 Memory 大小补全一个默认值。
        :type Cpu: int
        :param _InstanceId: 询价续费实例ID。如需查询实例续费价格，填写InstanceId和Period即可。
        :type InstanceId: str
        :param _Ladder: 按量计费阶梯。仅PayType=HOUR_PAID有效，支持值包括：1，2，3。阶梯时长见https://cloud.tencent.com/document/product/236/18335。
        :type Ladder: int
        """
        self._Period = None
        self._Zone = None
        self._GoodsNum = None
        self._Memory = None
        self._Volume = None
        self._InstanceRole = None
        self._PayType = None
        self._ProtectMode = None
        self._DeviceType = None
        self._InstanceNodes = None
        self._Cpu = None
        self._InstanceId = None
        self._Ladder = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ladder(self):
        return self._Ladder

    @Ladder.setter
    def Ladder(self, Ladder):
        self._Ladder = Ladder


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._Zone = params.get("Zone")
        self._GoodsNum = params.get("GoodsNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._InstanceRole = params.get("InstanceRole")
        self._PayType = params.get("PayType")
        self._ProtectMode = params.get("ProtectMode")
        self._DeviceType = params.get("DeviceType")
        self._InstanceNodes = params.get("InstanceNodes")
        self._Cpu = params.get("Cpu")
        self._InstanceId = params.get("InstanceId")
        self._Ladder = params.get("Ladder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPriceResponse(AbstractModel):
    """DescribeDBPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 实例价格，单位：分。
        :type Price: int
        :param _OriginalPrice: 实例原价，单位：分。
        :type OriginalPrice: int
        :param _Currency: 货币单位。CNY-人民币，USD-美元。
        :type Currency: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._OriginalPrice = None
        self._Currency = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Price = params.get("Price")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param _ForReadonlyInstance: 该值默认为False，表示当传入只读实例ID时，查询操作的是对应只读组的安全组。如果需要操作只读实例ID的安全组， 需要将该入参置为True。
        :type ForReadonlyInstance: bool
        """
        self._InstanceId = None
        self._ForReadonlyInstance = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForReadonlyInstance(self):
        return self._ForReadonlyInstance

    @ForReadonlyInstance.setter
    def ForReadonlyInstance(self, ForReadonlyInstance):
        self._ForReadonlyInstance = ForReadonlyInstance


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSwitchRecordsRequest(AbstractModel):
    """DescribeDBSwitchRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _Limit: 分页大小，默认值为 50，最小值为 1，最大值为 2000。
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSwitchRecordsResponse(AbstractModel):
    """DescribeDBSwitchRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例切换记录的总数。
        :type TotalCount: int
        :param _Items: 实例切换记录详情。
        :type Items: list of DBSwitchInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DBSwitchInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDataBackupOverviewRequest(AbstractModel):
    """DescribeDataBackupOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 需要查询的云数据库产品类型，目前仅支持 "mysql"。
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataBackupOverviewResponse(AbstractModel):
    """DescribeDataBackupOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataBackupVolume: 当前地域的数据备份总容量（包含自动备份和手动备份，单位为字节）。
        :type DataBackupVolume: int
        :param _DataBackupCount: 当前地域的数据备份总个数。
        :type DataBackupCount: int
        :param _AutoBackupVolume: 当前地域的自动备份总容量。
        :type AutoBackupVolume: int
        :param _AutoBackupCount: 当前地域的自动备份总个数。
        :type AutoBackupCount: int
        :param _ManualBackupVolume: 当前地域的手动备份总容量。
        :type ManualBackupVolume: int
        :param _ManualBackupCount: 当前地域的手动备份总个数。
        :type ManualBackupCount: int
        :param _RemoteBackupVolume: 异地备份总容量。
        :type RemoteBackupVolume: int
        :param _RemoteBackupCount: 异地备份总个数。
        :type RemoteBackupCount: int
        :param _DataBackupArchiveVolume: 当前地域归档备份总容量。
        :type DataBackupArchiveVolume: int
        :param _DataBackupArchiveCount: 当前地域归档备份总个数。
        :type DataBackupArchiveCount: int
        :param _DataBackupStandbyVolume: 当前地域标准存储备份总容量。
        :type DataBackupStandbyVolume: int
        :param _DataBackupStandbyCount: 当前地域标准存储备份总个数。
        :type DataBackupStandbyCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataBackupVolume = None
        self._DataBackupCount = None
        self._AutoBackupVolume = None
        self._AutoBackupCount = None
        self._ManualBackupVolume = None
        self._ManualBackupCount = None
        self._RemoteBackupVolume = None
        self._RemoteBackupCount = None
        self._DataBackupArchiveVolume = None
        self._DataBackupArchiveCount = None
        self._DataBackupStandbyVolume = None
        self._DataBackupStandbyCount = None
        self._RequestId = None

    @property
    def DataBackupVolume(self):
        return self._DataBackupVolume

    @DataBackupVolume.setter
    def DataBackupVolume(self, DataBackupVolume):
        self._DataBackupVolume = DataBackupVolume

    @property
    def DataBackupCount(self):
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def AutoBackupVolume(self):
        return self._AutoBackupVolume

    @AutoBackupVolume.setter
    def AutoBackupVolume(self, AutoBackupVolume):
        self._AutoBackupVolume = AutoBackupVolume

    @property
    def AutoBackupCount(self):
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def ManualBackupVolume(self):
        return self._ManualBackupVolume

    @ManualBackupVolume.setter
    def ManualBackupVolume(self, ManualBackupVolume):
        self._ManualBackupVolume = ManualBackupVolume

    @property
    def ManualBackupCount(self):
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def RemoteBackupVolume(self):
        return self._RemoteBackupVolume

    @RemoteBackupVolume.setter
    def RemoteBackupVolume(self, RemoteBackupVolume):
        self._RemoteBackupVolume = RemoteBackupVolume

    @property
    def RemoteBackupCount(self):
        return self._RemoteBackupCount

    @RemoteBackupCount.setter
    def RemoteBackupCount(self, RemoteBackupCount):
        self._RemoteBackupCount = RemoteBackupCount

    @property
    def DataBackupArchiveVolume(self):
        return self._DataBackupArchiveVolume

    @DataBackupArchiveVolume.setter
    def DataBackupArchiveVolume(self, DataBackupArchiveVolume):
        self._DataBackupArchiveVolume = DataBackupArchiveVolume

    @property
    def DataBackupArchiveCount(self):
        return self._DataBackupArchiveCount

    @DataBackupArchiveCount.setter
    def DataBackupArchiveCount(self, DataBackupArchiveCount):
        self._DataBackupArchiveCount = DataBackupArchiveCount

    @property
    def DataBackupStandbyVolume(self):
        return self._DataBackupStandbyVolume

    @DataBackupStandbyVolume.setter
    def DataBackupStandbyVolume(self, DataBackupStandbyVolume):
        self._DataBackupStandbyVolume = DataBackupStandbyVolume

    @property
    def DataBackupStandbyCount(self):
        return self._DataBackupStandbyCount

    @DataBackupStandbyCount.setter
    def DataBackupStandbyCount(self, DataBackupStandbyCount):
        self._DataBackupStandbyCount = DataBackupStandbyCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataBackupVolume = params.get("DataBackupVolume")
        self._DataBackupCount = params.get("DataBackupCount")
        self._AutoBackupVolume = params.get("AutoBackupVolume")
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._ManualBackupVolume = params.get("ManualBackupVolume")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._RemoteBackupVolume = params.get("RemoteBackupVolume")
        self._RemoteBackupCount = params.get("RemoteBackupCount")
        self._DataBackupArchiveVolume = params.get("DataBackupArchiveVolume")
        self._DataBackupArchiveCount = params.get("DataBackupArchiveCount")
        self._DataBackupStandbyVolume = params.get("DataBackupStandbyVolume")
        self._DataBackupStandbyCount = params.get("DataBackupStandbyCount")
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Offset: 偏移量，最小值为0。
        :type Offset: int
        :param _Limit: 单次请求数量，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param _DatabaseRegexp: 匹配数据库库名的正则表达式。
        :type DatabaseRegexp: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._DatabaseRegexp = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def DatabaseRegexp(self):
        return self._DatabaseRegexp

    @DatabaseRegexp.setter
    def DatabaseRegexp(self, DatabaseRegexp):
        self._DatabaseRegexp = DatabaseRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DatabaseRegexp = params.get("DatabaseRegexp")
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
        :param _TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param _Items: 返回的实例信息。
        :type Items: list of str
        :param _DatabaseList: 数据库名以及字符集
        :type DatabaseList: list of DatabasesWithCharacterLists
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._DatabaseList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def DatabaseList(self):
        return self._DatabaseList

    @DatabaseList.setter
    def DatabaseList(self, DatabaseList):
        self._DatabaseList = DatabaseList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Items = params.get("Items")
        if params.get("DatabaseList") is not None:
            self._DatabaseList = []
            for item in params.get("DatabaseList"):
                obj = DatabasesWithCharacterLists()
                obj._deserialize(item)
                self._DatabaseList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDefaultParamsRequest(AbstractModel):
    """DescribeDefaultParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineVersion: 引擎版本，目前支持 ["5.1", "5.5", "5.6", "5.7", "8.0"]
        :type EngineVersion: str
        :param _TemplateType: 默认参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模板，"HIGH_PERFORMANCE" - 高性能模板。
        :type TemplateType: str
        :param _EngineType: 参数模板引擎，默认值：InnoDB
        :type EngineType: str
        """
        self._EngineVersion = None
        self._TemplateType = None
        self._EngineType = None

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._EngineVersion = params.get("EngineVersion")
        self._TemplateType = params.get("TemplateType")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultParamsResponse(AbstractModel):
    """DescribeDefaultParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数个数。
        :type TotalCount: int
        :param _Items: 参数详情。
        :type Items: list of ParameterDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeployGroupListRequest(AbstractModel):
    """DescribeDeployGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param _DeployGroupName: 置放群组名称。
        :type DeployGroupName: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._DeployGroupId = None
        self._DeployGroupName = None
        self._Limit = None
        self._Offset = None

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def DeployGroupName(self):
        return self._DeployGroupName

    @DeployGroupName.setter
    def DeployGroupName(self, DeployGroupName):
        self._DeployGroupName = DeployGroupName

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
        self._DeployGroupId = params.get("DeployGroupId")
        self._DeployGroupName = params.get("DeployGroupName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployGroupListResponse(AbstractModel):
    """DescribeDeployGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 符合条件的记录总数。
        :type Total: int
        :param _Items: 返回列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DeployGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DeployGroupInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceMonitorInfoRequest(AbstractModel):
    """DescribeDeviceMonitorInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param _Count: 返回当天最近Count个5分钟粒度的监控数据。最小值1，最大值288，不传该参数默认返回当天所有5分钟粒度监控数据。
        :type Count: int
        """
        self._InstanceId = None
        self._Count = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceMonitorInfoResponse(AbstractModel):
    """DescribeDeviceMonitorInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Cpu: 实例CPU监控数据
        :type Cpu: :class:`tencentcloud.cdb.v20170320.models.DeviceCpuInfo`
        :param _Mem: 实例内存监控数据
        :type Mem: :class:`tencentcloud.cdb.v20170320.models.DeviceMemInfo`
        :param _Net: 实例网络监控数据
        :type Net: :class:`tencentcloud.cdb.v20170320.models.DeviceNetInfo`
        :param _Disk: 实例磁盘监控数据
        :type Disk: :class:`tencentcloud.cdb.v20170320.models.DeviceDiskInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Cpu = None
        self._Mem = None
        self._Net = None
        self._Disk = None
        self._RequestId = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Net(self):
        return self._Net

    @Net.setter
    def Net(self, Net):
        self._Net = Net

    @property
    def Disk(self):
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Cpu") is not None:
            self._Cpu = DeviceCpuInfo()
            self._Cpu._deserialize(params.get("Cpu"))
        if params.get("Mem") is not None:
            self._Mem = DeviceMemInfo()
            self._Mem._deserialize(params.get("Mem"))
        if params.get("Net") is not None:
            self._Net = DeviceNetInfo()
            self._Net._deserialize(params.get("Net"))
        if params.get("Disk") is not None:
            self._Disk = DeviceDiskInfo()
            self._Disk._deserialize(params.get("Disk"))
        self._RequestId = params.get("RequestId")


class DescribeErrorLogDataRequest(AbstractModel):
    """DescribeErrorLogData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间戳。例如 1585142640 。
        :type StartTime: int
        :param _EndTime: 结束时间戳。例如 1585142640 。
        :type EndTime: int
        :param _KeyWords: 要匹配的关键字列表，最多支持15个关键字。
        :type KeyWords: list of str
        :param _Limit: 分页的返回数量，默认为100，最大为400。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _InstType: 仅在实例为主实例或者灾备实例时生效，可选值：slave，代表拉取从机的日志。
        :type InstType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._KeyWords = None
        self._Limit = None
        self._Offset = None
        self._InstType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def KeyWords(self):
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords

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
    def InstType(self):
        return self._InstType

    @InstType.setter
    def InstType(self, InstType):
        self._InstType = InstType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._KeyWords = params.get("KeyWords")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstType = params.get("InstType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorLogDataResponse(AbstractModel):
    """DescribeErrorLogData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _Items: 返回的记录。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ErrlogItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ErrlogItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param _Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 分页大小，默认值：20。
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录数。
        :type TotalCount: int
        :param _Items: 参数修改记录。
        :type Items: list of ParamRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamRecord()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例的参数总数。
        :type TotalCount: int
        :param _Items: 参数详情。
        :type Items: list of ParameterDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLocalBinlogConfigRequest(AbstractModel):
    """DescribeLocalBinlogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalBinlogConfigResponse(AbstractModel):
    """DescribeLocalBinlogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LocalBinlogConfig: 实例binlog保留策略。
        :type LocalBinlogConfig: :class:`tencentcloud.cdb.v20170320.models.LocalBinlogConfig`
        :param _LocalBinlogConfigDefault: 该地域默认binlog保留策略。
        :type LocalBinlogConfigDefault: :class:`tencentcloud.cdb.v20170320.models.LocalBinlogConfigDefault`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LocalBinlogConfig = None
        self._LocalBinlogConfigDefault = None
        self._RequestId = None

    @property
    def LocalBinlogConfig(self):
        return self._LocalBinlogConfig

    @LocalBinlogConfig.setter
    def LocalBinlogConfig(self, LocalBinlogConfig):
        self._LocalBinlogConfig = LocalBinlogConfig

    @property
    def LocalBinlogConfigDefault(self):
        return self._LocalBinlogConfigDefault

    @LocalBinlogConfigDefault.setter
    def LocalBinlogConfigDefault(self, LocalBinlogConfigDefault):
        self._LocalBinlogConfigDefault = LocalBinlogConfigDefault

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LocalBinlogConfig") is not None:
            self._LocalBinlogConfig = LocalBinlogConfig()
            self._LocalBinlogConfig._deserialize(params.get("LocalBinlogConfig"))
        if params.get("LocalBinlogConfigDefault") is not None:
            self._LocalBinlogConfigDefault = LocalBinlogConfigDefault()
            self._LocalBinlogConfigDefault._deserialize(params.get("LocalBinlogConfigDefault"))
        self._RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板 ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplateInfoResponse(AbstractModel):
    """DescribeParamTemplateInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板 ID。
        :type TemplateId: int
        :param _Name: 参数模板名称。
        :type Name: str
        :param _EngineVersion: 参数模板对应实例版本
        :type EngineVersion: str
        :param _TotalCount: 参数模板中的参数数量
        :type TotalCount: int
        :param _Items: 参数详情
        :type Items: list of ParameterDetail
        :param _Description: 参数模板描述
        :type Description: str
        :param _TemplateType: 参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模板，"HIGH_PERFORMANCE" - 高性能模板。
        :type TemplateType: str
        :param _EngineType: 参数模板引擎。支持值包括："InnoDB"，"RocksDB"。
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._Name = None
        self._EngineVersion = None
        self._TotalCount = None
        self._Items = None
        self._Description = None
        self._TemplateType = None
        self._EngineType = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._EngineVersion = params.get("EngineVersion")
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Description = params.get("Description")
        self._TemplateType = params.get("TemplateType")
        self._EngineType = params.get("EngineType")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineVersions: 引擎版本，缺省则查询所有
        :type EngineVersions: list of str
        :param _EngineTypes: 引擎类型，缺省则查询所有
        :type EngineTypes: list of str
        :param _TemplateNames: 模板名称，缺省则查询所有
        :type TemplateNames: list of str
        :param _TemplateIds: 模板id，缺省则查询所有
        :type TemplateIds: list of int
        """
        self._EngineVersions = None
        self._EngineTypes = None
        self._TemplateNames = None
        self._TemplateIds = None

    @property
    def EngineVersions(self):
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def EngineTypes(self):
        return self._EngineTypes

    @EngineTypes.setter
    def EngineTypes(self, EngineTypes):
        self._EngineTypes = EngineTypes

    @property
    def TemplateNames(self):
        return self._TemplateNames

    @TemplateNames.setter
    def TemplateNames(self, TemplateNames):
        self._TemplateNames = TemplateNames

    @property
    def TemplateIds(self):
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds


    def _deserialize(self, params):
        self._EngineVersions = params.get("EngineVersions")
        self._EngineTypes = params.get("EngineTypes")
        self._TemplateNames = params.get("TemplateNames")
        self._TemplateIds = params.get("TemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该用户的参数模板数量。
        :type TotalCount: int
        :param _Items: 参数模板详情。
        :type Items: list of ParamTemplateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param _TotalCount: 安全组规则数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProxyCustomConfRequest(AbstractModel):
    """DescribeProxyCustomConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Offset: 分页
        :type Offset: int
        :param _Limit: 限制
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyCustomConfResponse(AbstractModel):
    """DescribeProxyCustomConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 代理配置数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _CustomConf: 代理配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomConf: :class:`tencentcloud.cdb.v20170320.models.CustomConfig`
        :param _WeightRule: 权重限制
注意：此字段可能返回 null，表示取不到有效值。
        :type WeightRule: :class:`tencentcloud.cdb.v20170320.models.Rule`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._CustomConf = None
        self._WeightRule = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CustomConf(self):
        return self._CustomConf

    @CustomConf.setter
    def CustomConf(self, CustomConf):
        self._CustomConf = CustomConf

    @property
    def WeightRule(self):
        return self._WeightRule

    @WeightRule.setter
    def WeightRule(self, WeightRule):
        self._WeightRule = WeightRule

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("CustomConf") is not None:
            self._CustomConf = CustomConfig()
            self._CustomConf._deserialize(params.get("CustomConf"))
        if params.get("WeightRule") is not None:
            self._WeightRule = Rule()
            self._WeightRule._deserialize(params.get("WeightRule"))
        self._RequestId = params.get("RequestId")


class DescribeProxySupportParamRequest(AbstractModel):
    """DescribeProxySupportParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySupportParamResponse(AbstractModel):
    """DescribeProxySupportParam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyVersion: 支持最大代理版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyVersion: str
        :param _SupportPool: 是否支持连接池
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportPool: bool
        :param _PoolMin: 连接池最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolMin: int
        :param _PoolMax: 连接池最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolMax: int
        :param _SupportTransSplit: 是否支持事务拆分
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportTransSplit: bool
        :param _SupportPoolMinVersion: 支持连接池的最小代理版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportPoolMinVersion: str
        :param _SupportTransSplitMinVersion: 支持事务拆分的最小代理版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportTransSplitMinVersion: str
        :param _SupportReadOnly: 是否支持设置只读
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportReadOnly: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyVersion = None
        self._SupportPool = None
        self._PoolMin = None
        self._PoolMax = None
        self._SupportTransSplit = None
        self._SupportPoolMinVersion = None
        self._SupportTransSplitMinVersion = None
        self._SupportReadOnly = None
        self._RequestId = None

    @property
    def ProxyVersion(self):
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def SupportPool(self):
        return self._SupportPool

    @SupportPool.setter
    def SupportPool(self, SupportPool):
        self._SupportPool = SupportPool

    @property
    def PoolMin(self):
        return self._PoolMin

    @PoolMin.setter
    def PoolMin(self, PoolMin):
        self._PoolMin = PoolMin

    @property
    def PoolMax(self):
        return self._PoolMax

    @PoolMax.setter
    def PoolMax(self, PoolMax):
        self._PoolMax = PoolMax

    @property
    def SupportTransSplit(self):
        return self._SupportTransSplit

    @SupportTransSplit.setter
    def SupportTransSplit(self, SupportTransSplit):
        self._SupportTransSplit = SupportTransSplit

    @property
    def SupportPoolMinVersion(self):
        return self._SupportPoolMinVersion

    @SupportPoolMinVersion.setter
    def SupportPoolMinVersion(self, SupportPoolMinVersion):
        self._SupportPoolMinVersion = SupportPoolMinVersion

    @property
    def SupportTransSplitMinVersion(self):
        return self._SupportTransSplitMinVersion

    @SupportTransSplitMinVersion.setter
    def SupportTransSplitMinVersion(self, SupportTransSplitMinVersion):
        self._SupportTransSplitMinVersion = SupportTransSplitMinVersion

    @property
    def SupportReadOnly(self):
        return self._SupportReadOnly

    @SupportReadOnly.setter
    def SupportReadOnly(self, SupportReadOnly):
        self._SupportReadOnly = SupportReadOnly

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyVersion = params.get("ProxyVersion")
        self._SupportPool = params.get("SupportPool")
        self._PoolMin = params.get("PoolMin")
        self._PoolMax = params.get("PoolMax")
        self._SupportTransSplit = params.get("SupportTransSplit")
        self._SupportPoolMinVersion = params.get("SupportPoolMinVersion")
        self._SupportTransSplitMinVersion = params.get("SupportTransSplitMinVersion")
        self._SupportReadOnly = params.get("SupportReadOnly")
        self._RequestId = params.get("RequestId")


class DescribeRemoteBackupConfigRequest(AbstractModel):
    """DescribeRemoteBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRemoteBackupConfigResponse(AbstractModel):
    """DescribeRemoteBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExpireDays: 异地备份保留时间，单位为天
        :type ExpireDays: int
        :param _RemoteBackupSave: 异地数据备份开关，off - 关闭异地备份，on-开启异地备份
        :type RemoteBackupSave: str
        :param _RemoteBinlogSave: 异地日志备份开关，off - 关闭异地备份，on-开启异地备份，只有在参数RemoteBackupSave为on时，RemoteBinlogSave参数才可设置为on
        :type RemoteBinlogSave: str
        :param _RemoteRegion: 用户已设置异地备份地域列表
        :type RemoteRegion: list of str
        :param _RegionList: 用户可设置异地备份地域列表
        :type RegionList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExpireDays = None
        self._RemoteBackupSave = None
        self._RemoteBinlogSave = None
        self._RemoteRegion = None
        self._RegionList = None
        self._RequestId = None

    @property
    def ExpireDays(self):
        return self._ExpireDays

    @ExpireDays.setter
    def ExpireDays(self, ExpireDays):
        self._ExpireDays = ExpireDays

    @property
    def RemoteBackupSave(self):
        return self._RemoteBackupSave

    @RemoteBackupSave.setter
    def RemoteBackupSave(self, RemoteBackupSave):
        self._RemoteBackupSave = RemoteBackupSave

    @property
    def RemoteBinlogSave(self):
        return self._RemoteBinlogSave

    @RemoteBinlogSave.setter
    def RemoteBinlogSave(self, RemoteBinlogSave):
        self._RemoteBinlogSave = RemoteBinlogSave

    @property
    def RemoteRegion(self):
        return self._RemoteRegion

    @RemoteRegion.setter
    def RemoteRegion(self, RemoteRegion):
        self._RemoteRegion = RemoteRegion

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExpireDays = params.get("ExpireDays")
        self._RemoteBackupSave = params.get("RemoteBackupSave")
        self._RemoteBinlogSave = params.get("RemoteBinlogSave")
        self._RemoteRegion = params.get("RemoteRegion")
        self._RegionList = params.get("RegionList")
        self._RequestId = params.get("RequestId")


class DescribeRoGroupsRequest(AbstractModel):
    """DescribeRoGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoGroupsResponse(AbstractModel):
    """DescribeRoGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoGroups: RO组信息数组，一个实例可关联多个RO组。
        :type RoGroups: list of RoGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoGroups = None
        self._RequestId = None

    @property
    def RoGroups(self):
        return self._RoGroups

    @RoGroups.setter
    def RoGroups(self, RoGroups):
        self._RoGroups = RoGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RoGroups") is not None:
            self._RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self._RoGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoMinScaleRequest(AbstractModel):
    """DescribeRoMinScale请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoInstanceId: 只读实例ID，格式如：cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，该参数与MasterInstanceId参数不能同时为空。
        :type RoInstanceId: str
        :param _MasterInstanceId: 主实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，该参数与RoInstanceId参数不能同时为空。注意，当传入参数包含RoInstanceId时，返回值为只读实例升级时的最小规格；当传入参数只包含MasterInstanceId时，返回值为只读实例购买时的最小规格。
        :type MasterInstanceId: str
        """
        self._RoInstanceId = None
        self._MasterInstanceId = None

    @property
    def RoInstanceId(self):
        return self._RoInstanceId

    @RoInstanceId.setter
    def RoInstanceId(self, RoInstanceId):
        self._RoInstanceId = RoInstanceId

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId


    def _deserialize(self, params):
        self._RoInstanceId = params.get("RoInstanceId")
        self._MasterInstanceId = params.get("MasterInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoMinScaleResponse(AbstractModel):
    """DescribeRoMinScale返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Memory: 内存规格大小, 单位为：MB。
        :type Memory: int
        :param _Volume: 磁盘规格大小, 单位为：GB。
        :type Volume: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Memory = None
        self._Volume = None
        self._RequestId = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._RequestId = params.get("RequestId")


class DescribeRollbackRangeTimeRequest(AbstractModel):
    """DescribeRollbackRangeTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表，单个实例 ID 的格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        :param _IsRemoteZone: 克隆实例与源实例是否在同一可用区，是:"false"，否:"true"
        :type IsRemoteZone: str
        :param _BackupRegion: 克隆实例与源实例不在同一地域时需填写克隆实例所在地域，例："ap-guangzhou"
        :type BackupRegion: str
        """
        self._InstanceIds = None
        self._IsRemoteZone = None
        self._BackupRegion = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def IsRemoteZone(self):
        return self._IsRemoteZone

    @IsRemoteZone.setter
    def IsRemoteZone(self, IsRemoteZone):
        self._IsRemoteZone = IsRemoteZone

    @property
    def BackupRegion(self):
        return self._BackupRegion

    @BackupRegion.setter
    def BackupRegion(self, BackupRegion):
        self._BackupRegion = BackupRegion


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._IsRemoteZone = params.get("IsRemoteZone")
        self._BackupRegion = params.get("BackupRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackRangeTimeResponse(AbstractModel):
    """DescribeRollbackRangeTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param _Items: 返回的参数信息。
        :type Items: list of InstanceRollbackRangeTime
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceRollbackRangeTime()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRollbackTaskDetailRequest(AbstractModel):
    """DescribeRollbackTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872)。
        :type InstanceId: str
        :param _AsyncRequestId: 异步任务 ID。
        :type AsyncRequestId: str
        :param _Limit: 分页参数，每次请求返回的记录数。默认值为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 分页偏移量。默认为 0。
        :type Offset: int
        """
        self._InstanceId = None
        self._AsyncRequestId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

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
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTaskDetailResponse(AbstractModel):
    """DescribeRollbackTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _Items: 回档任务详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of RollbackTask
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RollbackTask()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogDataRequest(AbstractModel):
    """DescribeSlowLogData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _StartTime: 开始时间戳。例如 1585142640 。
        :type StartTime: int
        :param _EndTime: 结束时间戳。例如 1585142640 。
        :type EndTime: int
        :param _UserHosts: 客户端 Host 列表。
        :type UserHosts: list of str
        :param _UserNames: 客户端 用户名 列表。
        :type UserNames: list of str
        :param _DataBases: 访问的 数据库 列表。
        :type DataBases: list of str
        :param _SortBy: 排序字段。当前支持：Timestamp,QueryTime,LockTime,RowsExamined,RowsSent 。
        :type SortBy: str
        :param _OrderBy: 升序还是降序排列。当前支持：ASC,DESC 。
        :type OrderBy: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 一次性返回的记录数量，默认为100，最大为400。
        :type Limit: int
        :param _InstType: 仅在实例为主实例或者灾备实例时生效，可选值：slave，代表拉取从机的日志。
        :type InstType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._UserHosts = None
        self._UserNames = None
        self._DataBases = None
        self._SortBy = None
        self._OrderBy = None
        self._Offset = None
        self._Limit = None
        self._InstType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def UserHosts(self):
        return self._UserHosts

    @UserHosts.setter
    def UserHosts(self, UserHosts):
        self._UserHosts = UserHosts

    @property
    def UserNames(self):
        return self._UserNames

    @UserNames.setter
    def UserNames(self, UserNames):
        self._UserNames = UserNames

    @property
    def DataBases(self):
        return self._DataBases

    @DataBases.setter
    def DataBases(self, DataBases):
        self._DataBases = DataBases

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

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
    def InstType(self):
        return self._InstType

    @InstType.setter
    def InstType(self, InstType):
        self._InstType = InstType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserHosts = params.get("UserHosts")
        self._UserNames = params.get("UserNames")
        self._DataBases = params.get("DataBases")
        self._SortBy = params.get("SortBy")
        self._OrderBy = params.get("OrderBy")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstType = params.get("InstType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogDataResponse(AbstractModel):
    """DescribeSlowLogData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _Items: 查询到的记录。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SlowLogItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SlowLogItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Offset: 偏移量，默认值为0，最小值为0。
        :type Offset: int
        :param _Limit: 分页大小，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的慢查询日志总数。
        :type TotalCount: int
        :param _Items: 符合查询条件的慢查询日志详情。
        :type Items: list of SlowLogInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SlowLogInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSupportedPrivilegesRequest(AbstractModel):
    """DescribeSupportedPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupportedPrivilegesResponse(AbstractModel):
    """DescribeSupportedPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalSupportedPrivileges: 实例支持的全局权限。
        :type GlobalSupportedPrivileges: list of str
        :param _DatabaseSupportedPrivileges: 实例支持的数据库权限。
        :type DatabaseSupportedPrivileges: list of str
        :param _TableSupportedPrivileges: 实例支持的数据库表权限。
        :type TableSupportedPrivileges: list of str
        :param _ColumnSupportedPrivileges: 实例支持的数据库列权限。
        :type ColumnSupportedPrivileges: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GlobalSupportedPrivileges = None
        self._DatabaseSupportedPrivileges = None
        self._TableSupportedPrivileges = None
        self._ColumnSupportedPrivileges = None
        self._RequestId = None

    @property
    def GlobalSupportedPrivileges(self):
        return self._GlobalSupportedPrivileges

    @GlobalSupportedPrivileges.setter
    def GlobalSupportedPrivileges(self, GlobalSupportedPrivileges):
        self._GlobalSupportedPrivileges = GlobalSupportedPrivileges

    @property
    def DatabaseSupportedPrivileges(self):
        return self._DatabaseSupportedPrivileges

    @DatabaseSupportedPrivileges.setter
    def DatabaseSupportedPrivileges(self, DatabaseSupportedPrivileges):
        self._DatabaseSupportedPrivileges = DatabaseSupportedPrivileges

    @property
    def TableSupportedPrivileges(self):
        return self._TableSupportedPrivileges

    @TableSupportedPrivileges.setter
    def TableSupportedPrivileges(self, TableSupportedPrivileges):
        self._TableSupportedPrivileges = TableSupportedPrivileges

    @property
    def ColumnSupportedPrivileges(self):
        return self._ColumnSupportedPrivileges

    @ColumnSupportedPrivileges.setter
    def ColumnSupportedPrivileges(self, ColumnSupportedPrivileges):
        self._ColumnSupportedPrivileges = ColumnSupportedPrivileges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GlobalSupportedPrivileges = params.get("GlobalSupportedPrivileges")
        self._DatabaseSupportedPrivileges = params.get("DatabaseSupportedPrivileges")
        self._TableSupportedPrivileges = params.get("TableSupportedPrivileges")
        self._ColumnSupportedPrivileges = params.get("ColumnSupportedPrivileges")
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Database: 数据库的名称。
        :type Database: str
        :param _Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 单次请求返回的数量，默认值为20，最大值为2000。
        :type Limit: int
        :param _TableRegexp: 匹配数据库表名的正则表达式，规则同 MySQL 官网
        :type TableRegexp: str
        """
        self._InstanceId = None
        self._Database = None
        self._Offset = None
        self._Limit = None
        self._TableRegexp = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

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
    def TableRegexp(self):
        return self._TableRegexp

    @TableRegexp.setter
    def TableRegexp(self, TableRegexp):
        self._TableRegexp = TableRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Database = params.get("Database")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TableRegexp = params.get("TableRegexp")
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
        :param _TotalCount: 符合查询条件的数据库表总数。
        :type TotalCount: int
        :param _Items: 返回的数据库表信息。
        :type Items: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Items = params.get("Items")
        self._RequestId = params.get("RequestId")


class DescribeTagsOfInstanceIdsRequest(AbstractModel):
    """DescribeTagsOfInstanceIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例列表。
        :type InstanceIds: list of str
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _Limit: 分页大小。
        :type Limit: int
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsOfInstanceIdsResponse(AbstractModel):
    """DescribeTagsOfInstanceIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _Limit: 分页大小。
        :type Limit: int
        :param _Rows: 实例标签信息。
        :type Rows: list of TagsInfoOfInstance
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfInstance()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param _AsyncRequestId: 异步任务请求 ID，执行云数据库相关操作返回的 AsyncRequestId。
        :type AsyncRequestId: str
        :param _TaskTypes: 任务类型，不传值则查询所有任务类型，支持的值包括：
1 - 数据库回档；
2 - SQL操作；
3 - 数据导入；
5 - 参数设置；
6 - 初始化云数据库实例；
7 - 重启云数据库实例；
8 - 开启云数据库实例GTID；
9 - 只读实例升级；
10 - 数据库批量回档；
11 - 主实例升级；
12 - 删除云数据库库表；
13 - 灾备实例提升为主。
        :type TaskTypes: list of int
        :param _TaskStatus: 任务状态，不传值则查询所有任务状态，支持的值包括：
-1 - 未定义；
0 - 初始化；
1 - 运行中；
2 - 执行成功；
3 - 执行失败；
4 - 已终止；
5 - 已删除；
6 - 已暂停。
        :type TaskStatus: list of int
        :param _StartTimeBegin: 第一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01。
        :type StartTimeBegin: str
        :param _StartTimeEnd: 最后一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01。
        :type StartTimeEnd: str
        :param _Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 单次请求返回的数量，默认值为20，最大值为100。
        :type Limit: int
        """
        self._InstanceId = None
        self._AsyncRequestId = None
        self._TaskTypes = None
        self._TaskStatus = None
        self._StartTimeBegin = None
        self._StartTimeEnd = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def StartTimeBegin(self):
        return self._StartTimeBegin

    @StartTimeBegin.setter
    def StartTimeBegin(self, StartTimeBegin):
        self._StartTimeBegin = StartTimeBegin

    @property
    def StartTimeEnd(self):
        return self._StartTimeEnd

    @StartTimeEnd.setter
    def StartTimeEnd(self, StartTimeEnd):
        self._StartTimeEnd = StartTimeEnd

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
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._TaskTypes = params.get("TaskTypes")
        self._TaskStatus = params.get("TaskStatus")
        self._StartTimeBegin = params.get("StartTimeBegin")
        self._StartTimeEnd = params.get("StartTimeEnd")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        :param _TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param _Items: 返回的实例任务信息。
        :type Items: list of TaskDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimeWindowRequest(AbstractModel):
    """DescribeTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimeWindowResponse(AbstractModel):
    """DescribeTimeWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Monday: 星期一的可维护时间列表。
        :type Monday: list of str
        :param _Tuesday: 星期二的可维护时间列表。
        :type Tuesday: list of str
        :param _Wednesday: 星期三的可维护时间列表。
        :type Wednesday: list of str
        :param _Thursday: 星期四的可维护时间列表。
        :type Thursday: list of str
        :param _Friday: 星期五的可维护时间列表。
        :type Friday: list of str
        :param _Saturday: 星期六的可维护时间列表。
        :type Saturday: list of str
        :param _Sunday: 星期日的可维护时间列表。
        :type Sunday: list of str
        :param _MaxDelayTime: 最大数据延迟阈值
        :type MaxDelayTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Monday = None
        self._Tuesday = None
        self._Wednesday = None
        self._Thursday = None
        self._Friday = None
        self._Saturday = None
        self._Sunday = None
        self._MaxDelayTime = None
        self._RequestId = None

    @property
    def Monday(self):
        return self._Monday

    @Monday.setter
    def Monday(self, Monday):
        self._Monday = Monday

    @property
    def Tuesday(self):
        return self._Tuesday

    @Tuesday.setter
    def Tuesday(self, Tuesday):
        self._Tuesday = Tuesday

    @property
    def Wednesday(self):
        return self._Wednesday

    @Wednesday.setter
    def Wednesday(self, Wednesday):
        self._Wednesday = Wednesday

    @property
    def Thursday(self):
        return self._Thursday

    @Thursday.setter
    def Thursday(self, Thursday):
        self._Thursday = Thursday

    @property
    def Friday(self):
        return self._Friday

    @Friday.setter
    def Friday(self, Friday):
        self._Friday = Friday

    @property
    def Saturday(self):
        return self._Saturday

    @Saturday.setter
    def Saturday(self, Saturday):
        self._Saturday = Saturday

    @property
    def Sunday(self):
        return self._Sunday

    @Sunday.setter
    def Sunday(self, Sunday):
        self._Sunday = Sunday

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Monday = params.get("Monday")
        self._Tuesday = params.get("Tuesday")
        self._Wednesday = params.get("Wednesday")
        self._Thursday = params.get("Thursday")
        self._Friday = params.get("Friday")
        self._Saturday = params.get("Saturday")
        self._Sunday = params.get("Sunday")
        self._MaxDelayTime = params.get("MaxDelayTime")
        self._RequestId = params.get("RequestId")


class DescribeUploadedFilesRequest(AbstractModel):
    """DescribeUploadedFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Path: 文件路径。该字段应填用户主账号的OwnerUin信息。
        :type Path: str
        :param _Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 单次请求返回的数量，默认值为20。
        :type Limit: int
        """
        self._Path = None
        self._Offset = None
        self._Limit = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

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
        self._Path = params.get("Path")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadedFilesResponse(AbstractModel):
    """DescribeUploadedFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的SQL文件总数。
        :type TotalCount: int
        :param _Items: 返回的SQL文件列表。
        :type Items: list of SqlFileInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SqlFileInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceCpuInfo(AbstractModel):
    """CPU负载

    """

    def __init__(self):
        r"""
        :param _Rate: 实例CPU平均使用率
        :type Rate: list of DeviceCpuRateInfo
        :param _Load: 实例CPU监控数据
        :type Load: list of int
        """
        self._Rate = None
        self._Load = None

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Load(self):
        return self._Load

    @Load.setter
    def Load(self, Load):
        self._Load = Load


    def _deserialize(self, params):
        if params.get("Rate") is not None:
            self._Rate = []
            for item in params.get("Rate"):
                obj = DeviceCpuRateInfo()
                obj._deserialize(item)
                self._Rate.append(obj)
        self._Load = params.get("Load")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceCpuRateInfo(AbstractModel):
    """实例CPU平均使用率

    """

    def __init__(self):
        r"""
        :param _CpuCore: Cpu核编号
        :type CpuCore: int
        :param _Rate: Cpu使用率
        :type Rate: list of int
        """
        self._CpuCore = None
        self._Rate = None

    @property
    def CpuCore(self):
        return self._CpuCore

    @CpuCore.setter
    def CpuCore(self, CpuCore):
        self._CpuCore = CpuCore

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate


    def _deserialize(self, params):
        self._CpuCore = params.get("CpuCore")
        self._Rate = params.get("Rate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDiskInfo(AbstractModel):
    """实例磁盘监控数据

    """

    def __init__(self):
        r"""
        :param _IoRatioPerSec: 平均每秒有百分之几的时间用于IO操作
        :type IoRatioPerSec: list of int
        :param _IoWaitTime: 平均每次设备I/O操作的等待时间*100，单位为毫秒。例如：该值为201，表示平均每次I/O操作等待时间为：201/100=2.1毫秒
        :type IoWaitTime: list of int
        :param _Read: 磁盘平均每秒完成的读操作次数总和*100。例如：该值为2002，表示磁盘平均每秒完成读操作为：2002/100=20.2次
        :type Read: list of int
        :param _Write: 磁盘平均每秒完成的写操作次数总和*100。例如：该值为30001，表示磁盘平均每秒完成写操作为：30001/100=300.01次
        :type Write: list of int
        :param _CapacityRatio: 磁盘空间容量，每两个一组，第一个为已使用容量，第二个为磁盘总容量
        :type CapacityRatio: list of int
        """
        self._IoRatioPerSec = None
        self._IoWaitTime = None
        self._Read = None
        self._Write = None
        self._CapacityRatio = None

    @property
    def IoRatioPerSec(self):
        return self._IoRatioPerSec

    @IoRatioPerSec.setter
    def IoRatioPerSec(self, IoRatioPerSec):
        self._IoRatioPerSec = IoRatioPerSec

    @property
    def IoWaitTime(self):
        return self._IoWaitTime

    @IoWaitTime.setter
    def IoWaitTime(self, IoWaitTime):
        self._IoWaitTime = IoWaitTime

    @property
    def Read(self):
        return self._Read

    @Read.setter
    def Read(self, Read):
        self._Read = Read

    @property
    def Write(self):
        return self._Write

    @Write.setter
    def Write(self, Write):
        self._Write = Write

    @property
    def CapacityRatio(self):
        return self._CapacityRatio

    @CapacityRatio.setter
    def CapacityRatio(self, CapacityRatio):
        self._CapacityRatio = CapacityRatio


    def _deserialize(self, params):
        self._IoRatioPerSec = params.get("IoRatioPerSec")
        self._IoWaitTime = params.get("IoWaitTime")
        self._Read = params.get("Read")
        self._Write = params.get("Write")
        self._CapacityRatio = params.get("CapacityRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceMemInfo(AbstractModel):
    """实例所在物理机内存监控信息

    """

    def __init__(self):
        r"""
        :param _Total: 总内存大小。free命令中Mem:一行total的值,单位：KB
        :type Total: list of int
        :param _Used: 已使用内存。free命令中Mem:一行used的值,单位：KB
        :type Used: list of int
        """
        self._Total = None
        self._Used = None

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


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceNetInfo(AbstractModel):
    """实例所在物理机网络监控信息

    """

    def __init__(self):
        r"""
        :param _Conn: tcp连接数
        :type Conn: list of int
        :param _PackageIn: 网卡入包量，单位：个/秒
        :type PackageIn: list of int
        :param _PackageOut: 网卡出包量，单位：个/秒
        :type PackageOut: list of int
        :param _FlowIn: 入流量，单位：kbps
        :type FlowIn: list of int
        :param _FlowOut: 出流量，单位：kbps
        :type FlowOut: list of int
        """
        self._Conn = None
        self._PackageIn = None
        self._PackageOut = None
        self._FlowIn = None
        self._FlowOut = None

    @property
    def Conn(self):
        return self._Conn

    @Conn.setter
    def Conn(self, Conn):
        self._Conn = Conn

    @property
    def PackageIn(self):
        return self._PackageIn

    @PackageIn.setter
    def PackageIn(self, PackageIn):
        self._PackageIn = PackageIn

    @property
    def PackageOut(self):
        return self._PackageOut

    @PackageOut.setter
    def PackageOut(self, PackageOut):
        self._PackageOut = PackageOut

    @property
    def FlowIn(self):
        return self._FlowIn

    @FlowIn.setter
    def FlowIn(self, FlowIn):
        self._FlowIn = FlowIn

    @property
    def FlowOut(self):
        return self._FlowOut

    @FlowOut.setter
    def FlowOut(self, FlowOut):
        self._FlowOut = FlowOut


    def _deserialize(self, params):
        self._Conn = params.get("Conn")
        self._PackageIn = params.get("PackageIn")
        self._PackageOut = params.get("PackageOut")
        self._FlowIn = params.get("FlowIn")
        self._FlowOut = params.get("FlowOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组 ID。
        :type SecurityGroupId: str
        :param _InstanceIds: 实例 ID 列表，一个或者多个实例 ID 组成的数组。
        :type InstanceIds: list of str
        :param _ForReadonlyInstance: 当传入只读实例ID时，默认操作的是对应只读组的安全组。如果需要操作只读实例ID的安全组， 需要将该入参置为True
        :type ForReadonlyInstance: bool
        """
        self._SecurityGroupId = None
        self._InstanceIds = None
        self._ForReadonlyInstance = None

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ForReadonlyInstance(self):
        return self._ForReadonlyInstance

    @ForReadonlyInstance.setter
    def ForReadonlyInstance(self, ForReadonlyInstance):
        self._ForReadonlyInstance = ForReadonlyInstance


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        self._ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

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


class DrInfo(AbstractModel):
    """灾备实例信息

    """

    def __init__(self):
        r"""
        :param _Status: 灾备实例状态
        :type Status: int
        :param _Zone: 可用区信息
        :type Zone: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Region: 地域信息
        :type Region: str
        :param _SyncStatus: 实例同步状态。可能的返回值为：
0 - 灾备未同步；
1 - 灾备同步中；
2 - 灾备同步成功；
3 - 灾备同步失败；
4 - 灾备同步修复中。
        :type SyncStatus: int
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceType: 实例类型
        :type InstanceType: int
        """
        self._Status = None
        self._Zone = None
        self._InstanceId = None
        self._Region = None
        self._SyncStatus = None
        self._InstanceName = None
        self._InstanceType = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SyncStatus(self):
        return self._SyncStatus

    @SyncStatus.setter
    def SyncStatus(self, SyncStatus):
        self._SyncStatus = SyncStatus

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Zone = params.get("Zone")
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        self._SyncStatus = params.get("SyncStatus")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrlogItem(AbstractModel):
    """结构化的错误日志详情

    """

    def __init__(self):
        r"""
        :param _Timestamp: 错误发生时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param _Content: 错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Timestamp = None
        self._Content = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportRecord(AbstractModel):
    """导入任务记录

    """

    def __init__(self):
        r"""
        :param _Status: 状态值
        :type Status: int
        :param _Code: 状态值
        :type Code: int
        :param _CostTime: 执行时间
        :type CostTime: int
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _WorkId: 后端任务ID
        :type WorkId: str
        :param _FileName: 导入文件名
        :type FileName: str
        :param _Process: 执行进度
        :type Process: int
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _FileSize: 文件大小
        :type FileSize: str
        :param _Message: 任务执行信息
        :type Message: str
        :param _JobId: 任务ID
        :type JobId: int
        :param _DbName: 导入库表名
        :type DbName: str
        :param _AsyncRequestId: 异步任务的请求ID
        :type AsyncRequestId: str
        """
        self._Status = None
        self._Code = None
        self._CostTime = None
        self._InstanceId = None
        self._WorkId = None
        self._FileName = None
        self._Process = None
        self._CreateTime = None
        self._FileSize = None
        self._Message = None
        self._JobId = None
        self._DbName = None
        self._AsyncRequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Process(self):
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._CostTime = params.get("CostTime")
        self._InstanceId = params.get("InstanceId")
        self._WorkId = params.get("WorkId")
        self._FileName = params.get("FileName")
        self._Process = params.get("Process")
        self._CreateTime = params.get("CreateTime")
        self._FileSize = params.get("FileSize")
        self._Message = params.get("Message")
        self._JobId = params.get("JobId")
        self._DbName = params.get("DbName")
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inbound(AbstractModel):
    """安全组入站规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param _CidrIp: 来源 IP 或 IP 段，例如192.168.0.0/16
        :type CidrIp: str
        :param _PortRange: 端口
        :type PortRange: str
        :param _IpProtocol: 网络协议，支持 UDP、TCP 等
        :type IpProtocol: str
        :param _Dir: 规则限定的方向，进站规则为 INPUT
        :type Dir: str
        :param _AddressModule: 地址模块
        :type AddressModule: str
        :param _Desc: 规则描述
        :type Desc: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Dir = None
        self._AddressModule = None
        self._Desc = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Dir(self):
        return self._Dir

    @Dir.setter
    def Dir(self, Dir):
        self._Dir = Dir

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Dir = params.get("Dir")
        self._AddressModule = params.get("AddressModule")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIds: list of str
        :param _NewPassword: 实例新的密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：!@#$%^*()）中的两种。
        :type NewPassword: str
        :param _Parameters: 实例的参数列表，目前支持设置“character_set_server”、“lower_case_table_names”参数。其中，“character_set_server”参数可选值为["utf8","latin1","gbk","utf8mb4"]；“lower_case_table_names”可选值为[“0”,“1”]。
        :type Parameters: list of ParamInfo
        :param _Vport: 实例的端口，取值范围为[1024, 65535]
        :type Vport: int
        """
        self._InstanceIds = None
        self._NewPassword = None
        self._Parameters = None
        self._Vport = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def NewPassword(self):
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._NewPassword = params.get("NewPassword")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._Parameters.append(obj)
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestIds: 异步任务的请求ID数组，可使用此ID查询异步任务的执行结果
        :type AsyncRequestIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestIds = None
        self._RequestId = None

    @property
    def AsyncRequestIds(self):
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeInstancesRequest(AbstractModel):
    """InquiryPriceUpgradeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param _Memory: 升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的内存规格。
        :type Memory: int
        :param _Volume: 升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的硬盘范围。
        :type Volume: int
        :param _Cpu: 升级后的核心数目，单位：核，为保证传入 CPU 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的核心数目，当未指定该值时，将按照 Memory 大小补全一个默认值。
        :type Cpu: int
        :param _ProtectMode: 数据复制方式，支持值包括：0 - 异步复制，1 - 半同步复制，2 - 强同步复制，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。
        :type ProtectMode: int
        :param _DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。 不指定则默认为通用型实例。
        :type DeviceType: str
        :param _InstanceNodes: 实例节点数。对于 RO 和 基础版实例， 该值默认为1。 如果需要询价三节点实例， 请将该值设置为3。其余主实例该值默认为2。
        :type InstanceNodes: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._Cpu = None
        self._ProtectMode = None
        self._DeviceType = None
        self._InstanceNodes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._Cpu = params.get("Cpu")
        self._ProtectMode = params.get("ProtectMode")
        self._DeviceType = params.get("DeviceType")
        self._InstanceNodes = params.get("InstanceNodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeInstancesResponse(AbstractModel):
    """InquiryPriceUpgradeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 实例价格，单位：分（人民币）。
        :type Price: int
        :param _OriginalPrice: 实例原价，单位：分（人民币）。
        :type OriginalPrice: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._OriginalPrice = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Price = params.get("Price")
        self._OriginalPrice = params.get("OriginalPrice")
        self._RequestId = params.get("RequestId")


class InstanceAuditLogFilters(AbstractModel):
    """审计日志搜索过滤器

    """

    def __init__(self):
        r"""
        :param _Type: 过滤项。sql 暂时不支持搜索。目前支持以下搜索条件：

等于、不等于、包含、不包含：
host - 客户端地址；
user - 用户名；
dbName - 数据库名称；

等于、不等于：
sqlType - SQL类型；
errCode - 错误码；
threadId - 线程ID；

范围搜索（时间类型统一为微妙）：
execTime - 执行时间；
lockWaitTime - 执行时间；
ioWaitTime - IO等待时间；
trxLivingTime - 事物持续时间；
cpuTime - cpu时间；
checkRows - 扫描行数；
affectRows - 影响行数；
sentRows - 返回行数。
        :type Type: str
        :param _Compare: 过滤条件。支持以下条件：
INC - 包含,
EXC - 不包含,
EQS - 等于,
NEQ - 不等于,
RA - 范围。
        :type Compare: str
        :param _Value: 过滤的值。
        :type Value: list of str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        r"""
        :param _WanStatus: 外网状态，可能的返回值为：0-未开通外网；1-已开通外网；2-已关闭外网
        :type WanStatus: int
        :param _Zone: 可用区信息
        :type Zone: str
        :param _InitFlag: 初始化标志，可能的返回值为：0-未初始化；1-已初始化
        :type InitFlag: int
        :param _RoVipInfo: 只读vip信息。单独开通只读实例访问的只读实例才有该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type RoVipInfo: :class:`tencentcloud.cdb.v20170320.models.RoVipInfo`
        :param _Memory: 内存容量，单位为 MB
        :type Memory: int
        :param _Status: 实例状态，可能的返回值：0-创建中；1-运行中；4-正在进行隔离操作；5-已隔离
        :type Status: int
        :param _VpcId: 私有网络 ID，例如：51102
        :type VpcId: int
        :param _SlaveInfo: 备机信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveInfo: :class:`tencentcloud.cdb.v20170320.models.SlaveInfo`
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Volume: 硬盘容量，单位为 GB
        :type Volume: int
        :param _AutoRenew: 自动续费标志，可能的返回值：0-未开通自动续费；1-已开通自动续费；2-已关闭自动续费
        :type AutoRenew: int
        :param _ProtectMode: 数据复制方式。0 - 异步复制；1 - 半同步复制；2 - 强同步复制
        :type ProtectMode: int
        :param _RoGroups: 只读组详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RoGroups: list of RoGroup
        :param _SubnetId: 子网 ID，例如：2333
        :type SubnetId: int
        :param _InstanceType: 实例类型，可能的返回值：1-主实例；2-灾备实例；3-只读实例
        :type InstanceType: int
        :param _ProjectId: 项目 ID
        :type ProjectId: int
        :param _Region: 地域信息
        :type Region: str
        :param _DeadlineTime: 实例到期时间
        :type DeadlineTime: str
        :param _DeployMode: 可用区部署方式。可能的值为：0 - 单可用区；1 - 多可用区
        :type DeployMode: int
        :param _TaskStatus: 实例任务状态。0 - 没有任务 ,1 - 升级中,2 - 数据导入中,3 - 开放Slave中,4 - 外网访问开通中,5 - 批量操作执行中,6 - 回档中,7 - 外网访问关闭中,8 - 密码修改中,9 - 实例名修改中,10 - 重启中,12 - 自建迁移中,13 - 删除库表中,14 - 灾备实例创建同步中,15 - 升级待切换,16 - 升级切换中,17 - 升级切换完成
        :type TaskStatus: int
        :param _MasterInfo: 主实例详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterInfo: :class:`tencentcloud.cdb.v20170320.models.MasterInfo`
        :param _DeviceType: 实例类型
        :type DeviceType: str
        :param _EngineVersion: 内核版本
        :type EngineVersion: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _DrInfo: 灾备实例详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DrInfo: list of DrInfo
        :param _WanDomain: 外网域名
        :type WanDomain: str
        :param _WanPort: 外网端口号
        :type WanPort: int
        :param _PayType: 付费类型，可能的返回值：0-包年包月；1-按量计费
        :type PayType: int
        :param _CreateTime: 实例创建时间
        :type CreateTime: str
        :param _Vip: 实例 IP
        :type Vip: str
        :param _Vport: 端口号
        :type Vport: int
        :param _CdbError: 磁盘写入是否被锁定（实例数据写入量已经超过磁盘配额）。0 -未被锁定 1 -已被锁定
        :type CdbError: int
        :param _UniqVpcId: 私有网络描述符，例如：“vpc-5v8wn9mg”
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网描述符，例如：“subnet-1typ0s7d”
        :type UniqSubnetId: str
        :param _PhysicalId: 物理 ID
        :type PhysicalId: str
        :param _Cpu: 核心数
        :type Cpu: int
        :param _Qps: 每秒查询数量
        :type Qps: int
        :param _ZoneName: 可用区中文名称
        :type ZoneName: str
        :param _DeviceClass: 物理机型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param _DeployGroupId: 置放群组 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployGroupId: str
        :param _ZoneId: 可用区 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _InstanceNodes: 节点数
        :type InstanceNodes: int
        :param _TagList: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of TagInfoItem
        :param _EngineType: 引擎类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineType: str
        :param _MaxDelayTime: 最大延迟阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDelayTime: int
        :param _DiskType: 实例磁盘类型，仅云盘版实例才返回该值。可能的值为 CLOUD_SSD：SSD云硬盘， CLOUD_HSSD：增强型SSD云硬盘
        :type DiskType: str
        """
        self._WanStatus = None
        self._Zone = None
        self._InitFlag = None
        self._RoVipInfo = None
        self._Memory = None
        self._Status = None
        self._VpcId = None
        self._SlaveInfo = None
        self._InstanceId = None
        self._Volume = None
        self._AutoRenew = None
        self._ProtectMode = None
        self._RoGroups = None
        self._SubnetId = None
        self._InstanceType = None
        self._ProjectId = None
        self._Region = None
        self._DeadlineTime = None
        self._DeployMode = None
        self._TaskStatus = None
        self._MasterInfo = None
        self._DeviceType = None
        self._EngineVersion = None
        self._InstanceName = None
        self._DrInfo = None
        self._WanDomain = None
        self._WanPort = None
        self._PayType = None
        self._CreateTime = None
        self._Vip = None
        self._Vport = None
        self._CdbError = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._PhysicalId = None
        self._Cpu = None
        self._Qps = None
        self._ZoneName = None
        self._DeviceClass = None
        self._DeployGroupId = None
        self._ZoneId = None
        self._InstanceNodes = None
        self._TagList = None
        self._EngineType = None
        self._MaxDelayTime = None
        self._DiskType = None

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InitFlag(self):
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def RoVipInfo(self):
        return self._RoVipInfo

    @RoVipInfo.setter
    def RoVipInfo(self, RoVipInfo):
        self._RoVipInfo = RoVipInfo

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SlaveInfo(self):
        return self._SlaveInfo

    @SlaveInfo.setter
    def SlaveInfo(self, SlaveInfo):
        self._SlaveInfo = SlaveInfo

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def RoGroups(self):
        return self._RoGroups

    @RoGroups.setter
    def RoGroups(self, RoGroups):
        self._RoGroups = RoGroups

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def MasterInfo(self):
        return self._MasterInfo

    @MasterInfo.setter
    def MasterInfo(self, MasterInfo):
        self._MasterInfo = MasterInfo

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DrInfo(self):
        return self._DrInfo

    @DrInfo.setter
    def DrInfo(self, DrInfo):
        self._DrInfo = DrInfo

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CdbError(self):
        return self._CdbError

    @CdbError.setter
    def CdbError(self, CdbError):
        self._CdbError = CdbError

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def PhysicalId(self):
        return self._PhysicalId

    @PhysicalId.setter
    def PhysicalId(self, PhysicalId):
        self._PhysicalId = PhysicalId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def DeviceClass(self):
        return self._DeviceClass

    @DeviceClass.setter
    def DeviceClass(self, DeviceClass):
        self._DeviceClass = DeviceClass

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType


    def _deserialize(self, params):
        self._WanStatus = params.get("WanStatus")
        self._Zone = params.get("Zone")
        self._InitFlag = params.get("InitFlag")
        if params.get("RoVipInfo") is not None:
            self._RoVipInfo = RoVipInfo()
            self._RoVipInfo._deserialize(params.get("RoVipInfo"))
        self._Memory = params.get("Memory")
        self._Status = params.get("Status")
        self._VpcId = params.get("VpcId")
        if params.get("SlaveInfo") is not None:
            self._SlaveInfo = SlaveInfo()
            self._SlaveInfo._deserialize(params.get("SlaveInfo"))
        self._InstanceId = params.get("InstanceId")
        self._Volume = params.get("Volume")
        self._AutoRenew = params.get("AutoRenew")
        self._ProtectMode = params.get("ProtectMode")
        if params.get("RoGroups") is not None:
            self._RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self._RoGroups.append(obj)
        self._SubnetId = params.get("SubnetId")
        self._InstanceType = params.get("InstanceType")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._DeadlineTime = params.get("DeadlineTime")
        self._DeployMode = params.get("DeployMode")
        self._TaskStatus = params.get("TaskStatus")
        if params.get("MasterInfo") is not None:
            self._MasterInfo = MasterInfo()
            self._MasterInfo._deserialize(params.get("MasterInfo"))
        self._DeviceType = params.get("DeviceType")
        self._EngineVersion = params.get("EngineVersion")
        self._InstanceName = params.get("InstanceName")
        if params.get("DrInfo") is not None:
            self._DrInfo = []
            for item in params.get("DrInfo"):
                obj = DrInfo()
                obj._deserialize(item)
                self._DrInfo.append(obj)
        self._WanDomain = params.get("WanDomain")
        self._WanPort = params.get("WanPort")
        self._PayType = params.get("PayType")
        self._CreateTime = params.get("CreateTime")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CdbError = params.get("CdbError")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._PhysicalId = params.get("PhysicalId")
        self._Cpu = params.get("Cpu")
        self._Qps = params.get("Qps")
        self._ZoneName = params.get("ZoneName")
        self._DeviceClass = params.get("DeviceClass")
        self._DeployGroupId = params.get("DeployGroupId")
        self._ZoneId = params.get("ZoneId")
        self._InstanceNodes = params.get("InstanceNodes")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfoItem()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._EngineType = params.get("EngineType")
        self._MaxDelayTime = params.get("MaxDelayTime")
        self._DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRebootTime(AbstractModel):
    """实例预期重启时间

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param _TimeInSeconds: 预期重启时间
        :type TimeInSeconds: int
        """
        self._InstanceId = None
        self._TimeInSeconds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TimeInSeconds(self):
        return self._TimeInSeconds

    @TimeInSeconds.setter
    def TimeInSeconds(self, TimeInSeconds):
        self._TimeInSeconds = TimeInSeconds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TimeInSeconds = params.get("TimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRollbackRangeTime(AbstractModel):
    """实例可回档时间范围

    """

    def __init__(self):
        r"""
        :param _Code: 查询数据库错误码
        :type Code: int
        :param _Message: 查询数据库错误信息
        :type Message: str
        :param _InstanceId: 实例ID列表，单个实例Id的格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param _Times: 可回档时间范围
        :type Times: list of RollbackTimeRange
        """
        self._Code = None
        self._Message = None
        self._InstanceId = None
        self._Times = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Times(self):
        return self._Times

    @Times.setter
    def Times(self, Times):
        self._Times = Times


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._InstanceId = params.get("InstanceId")
        if params.get("Times") is not None:
            self._Times = []
            for item in params.get("Times"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self._Times.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。(该返回字段目前已废弃，可以通过 DescribeDBInstances 接口查询实例的隔离状态)
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class LocalBinlogConfig(AbstractModel):
    """本地binlog保留配置

    """

    def __init__(self):
        r"""
        :param _SaveHours: 本地binlog保留时长，可取值范围：[72,168]。
        :type SaveHours: int
        :param _MaxUsage: 本地binlog空间使用率，可取值范围：[30,50]。
        :type MaxUsage: int
        """
        self._SaveHours = None
        self._MaxUsage = None

    @property
    def SaveHours(self):
        return self._SaveHours

    @SaveHours.setter
    def SaveHours(self, SaveHours):
        self._SaveHours = SaveHours

    @property
    def MaxUsage(self):
        return self._MaxUsage

    @MaxUsage.setter
    def MaxUsage(self, MaxUsage):
        self._MaxUsage = MaxUsage


    def _deserialize(self, params):
        self._SaveHours = params.get("SaveHours")
        self._MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalBinlogConfigDefault(AbstractModel):
    """本地binlog保留策略默认配置。

    """

    def __init__(self):
        r"""
        :param _SaveHours: 本地binlog保留时长，可取值范围：[72,168]。
        :type SaveHours: int
        :param _MaxUsage: 本地binlog空间使用率，可取值范围：[30,50]。
        :type MaxUsage: int
        """
        self._SaveHours = None
        self._MaxUsage = None

    @property
    def SaveHours(self):
        return self._SaveHours

    @SaveHours.setter
    def SaveHours(self, SaveHours):
        self._SaveHours = SaveHours

    @property
    def MaxUsage(self):
        return self._MaxUsage

    @MaxUsage.setter
    def MaxUsage(self, MaxUsage):
        self._MaxUsage = MaxUsage


    def _deserialize(self, params):
        self._SaveHours = params.get("SaveHours")
        self._MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterInfo(AbstractModel):
    """主实例信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域信息
        :type Region: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        :param _Zone: 可用区信息
        :type Zone: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ResourceId: 实例长ID
        :type ResourceId: str
        :param _Status: 实例状态
        :type Status: int
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceType: 实例类型
        :type InstanceType: int
        :param _TaskStatus: 任务状态
        :type TaskStatus: int
        :param _Memory: 内存容量
        :type Memory: int
        :param _Volume: 硬盘容量
        :type Volume: int
        :param _DeviceType: 实例机型
        :type DeviceType: str
        :param _Qps: 每秒查询数
        :type Qps: int
        :param _VpcId: 私有网络ID
        :type VpcId: int
        :param _SubnetId: 子网ID
        :type SubnetId: int
        :param _ExClusterId: 独享集群ID
        :type ExClusterId: str
        :param _ExClusterName: 独享集群名称
        :type ExClusterName: str
        """
        self._Region = None
        self._RegionId = None
        self._ZoneId = None
        self._Zone = None
        self._InstanceId = None
        self._ResourceId = None
        self._Status = None
        self._InstanceName = None
        self._InstanceType = None
        self._TaskStatus = None
        self._Memory = None
        self._Volume = None
        self._DeviceType = None
        self._Qps = None
        self._VpcId = None
        self._SubnetId = None
        self._ExClusterId = None
        self._ExClusterName = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ExClusterId(self):
        return self._ExClusterId

    @ExClusterId.setter
    def ExClusterId(self, ExClusterId):
        self._ExClusterId = ExClusterId

    @property
    def ExClusterName(self):
        return self._ExClusterName

    @ExClusterName.setter
    def ExClusterName(self, ExClusterName):
        self._ExClusterName = ExClusterName


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._InstanceId = params.get("InstanceId")
        self._ResourceId = params.get("ResourceId")
        self._Status = params.get("Status")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._TaskStatus = params.get("TaskStatus")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._DeviceType = params.get("DeviceType")
        self._Qps = params.get("Qps")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ExClusterId = params.get("ExClusterId")
        self._ExClusterName = params.get("ExClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Accounts: 云数据库账号。
        :type Accounts: list of Account
        :param _Description: 数据库账号的备注信息。
        :type Description: str
        """
        self._InstanceId = None
        self._Accounts = None
        self._Description = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAccountHostRequest(AbstractModel):
    """ModifyAccountHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _User: 账户的名称
        :type User: str
        :param _Host: 账户的旧主机
        :type Host: str
        :param _NewHost: 账户的新主机
        :type NewHost: str
        """
        self._InstanceId = None
        self._User = None
        self._Host = None
        self._NewHost = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def NewHost(self):
        return self._NewHost

    @NewHost.setter
    def NewHost(self, NewHost):
        self._NewHost = NewHost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Host = params.get("Host")
        self._NewHost = params.get("NewHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountHostResponse(AbstractModel):
    """ModifyAccountHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAccountMaxUserConnectionsRequest(AbstractModel):
    """ModifyAccountMaxUserConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Accounts: 云数据库账号。
        :type Accounts: list of Account
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _MaxUserConnections: 设置账户最大可用连接数，最大可设置值为10240。
        :type MaxUserConnections: int
        """
        self._Accounts = None
        self._InstanceId = None
        self._MaxUserConnections = None

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountMaxUserConnectionsResponse(AbstractModel):
    """ModifyAccountMaxUserConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAccountPasswordRequest(AbstractModel):
    """ModifyAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _NewPassword: 数据库账号的新密码。密码应至少包含字母、数字和字符（_+-&=!@#$%^*()）中的两种，长度为8-64个字符。
        :type NewPassword: str
        :param _Accounts: 云数据库账号。
        :type Accounts: list of Account
        """
        self._InstanceId = None
        self._NewPassword = None
        self._Accounts = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NewPassword(self):
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewPassword = params.get("NewPassword")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPasswordResponse(AbstractModel):
    """ModifyAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Accounts: 数据库的账号，包括用户名和域名。
        :type Accounts: list of Account
        :param _GlobalPrivileges: 全局权限。其中，GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER","CREATE USER","RELOAD","REPLICATION CLIENT","REPLICATION SLAVE"。
注意，ModifyAction为空时，不传该参数表示清除该权限。
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: 数据库的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，ModifyAction为空时，不传该参数表示清除该权限。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param _TablePrivileges: 数据库中表的权限。Privileges 权限的可选值为：权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，ModifyAction为空时，不传该参数表示清除该权限。
        :type TablePrivileges: list of TablePrivilege
        :param _ColumnPrivileges: 数据库表中列的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
注意，ModifyAction为空时，不传该参数表示清除该权限。
        :type ColumnPrivileges: list of ColumnPrivilege
        :param _ModifyAction: 该参数不为空时，为批量修改权限。可选值为：grant - 授予权限，revoke - 回收权限。
        :type ModifyAction: str
        """
        self._InstanceId = None
        self._Accounts = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None
        self._ColumnPrivileges = None
        self._ModifyAction = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def GlobalPrivileges(self):
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges

    @property
    def ColumnPrivileges(self):
        return self._ColumnPrivileges

    @ColumnPrivileges.setter
    def ColumnPrivileges(self, ColumnPrivileges):
        self._ColumnPrivileges = ColumnPrivileges

    @property
    def ModifyAction(self):
        return self._ModifyAction

    @ModifyAction.setter
    def ModifyAction(self, ModifyAction):
        self._ModifyAction = ModifyAction


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self._ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self._ColumnPrivileges.append(obj)
        self._ModifyAction = params.get("ModifyAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAuditConfigRequest(AbstractModel):
    """ModifyAuditConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _LogExpireDay: 审计日志保存时长。支持值包括：
7 - 一周
30 - 一个月；
180 - 六个月；
365 - 一年；
1095 - 三年；
1825 - 五年；
        :type LogExpireDay: int
        :param _CloseAudit: 是否关闭审计服务。可选值：true - 关闭审计服务；false - 不关闭审计服务。默认值为 false。
当关闭审计服务时，会删除用户的审计日志和文件，并删除该实例的所有审计策略。
CloseAudit、LogExpireDay必须至少提供一个，如果两个都提供则按照CloseAudit优先的逻辑处理。
        :type CloseAudit: bool
        :param _HighLogExpireDay: 高频审计日志保存时长。支持值包括：
7 - 一周
30 - 一个月；
180 - 六个月；
365 - 一年；
1095 - 三年；
1825 - 五年；
        :type HighLogExpireDay: int
        """
        self._InstanceId = None
        self._LogExpireDay = None
        self._CloseAudit = None
        self._HighLogExpireDay = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def CloseAudit(self):
        return self._CloseAudit

    @CloseAudit.setter
    def CloseAudit(self, CloseAudit):
        self._CloseAudit = CloseAudit

    @property
    def HighLogExpireDay(self):
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._CloseAudit = params.get("CloseAudit")
        self._HighLogExpireDay = params.get("HighLogExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditConfigResponse(AbstractModel):
    """ModifyAuditConfig返回参数结构体

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


class ModifyAuditRuleRequest(AbstractModel):
    """ModifyAuditRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 审计规则 ID。
        :type RuleId: str
        :param _RuleName: 审计规则名称。
        :type RuleName: str
        :param _Description: 审计规则描述。
        :type Description: str
        :param _RuleFilters: 审计规则过滤条件。若设置了过滤条件，则不会开启全审计。
        :type RuleFilters: list of AuditFilter
        :param _AuditAll: 是否开启全审计。支持值包括：false – 不开启全审计，true – 开启全审计。用户未设置审计规则过滤条件时，默认开启全审计。
        :type AuditAll: bool
        """
        self._RuleId = None
        self._RuleName = None
        self._Description = None
        self._RuleFilters = None
        self._AuditAll = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def AuditAll(self):
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Description = params.get("Description")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = AuditFilter()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._AuditAll = params.get("AuditAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditRuleResponse(AbstractModel):
    """ModifyAuditRule返回参数结构体

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


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        :param _AutoRenew: 自动续费标记，可取值的有：0 - 不自动续费，1 - 自动续费。
        :type AutoRenew: int
        """
        self._InstanceIds = None
        self._AutoRenew = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag返回参数结构体

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


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param _ExpireDays: 备份文件的保留时间，单位为天。最小值为7天，最大值为1830天。
        :type ExpireDays: int
        :param _StartTime: (将废弃，建议使用 BackupTimeWindow 参数) 备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 00:00-12:00，02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。
        :type StartTime: str
        :param _BackupMethod: 自动备份方式，仅支持：physical - 物理冷备
        :type BackupMethod: str
        :param _BinlogExpireDays: binlog的保留时间，单位为天。最小值为7天，最大值为1830天。该值的设置不能大于备份文件的保留时间。
        :type BinlogExpireDays: int
        :param _BackupTimeWindow: 备份时间窗，比如要设置每周二和周日 10:00-14:00之间备份，该参数如下：{"Monday": "", "Tuesday": "10:00-14:00", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": "10:00-14:00"}    （注：可以设置一周的某几天备份，但是每天的备份时间需要设置为相同的时间段。 如果设置了该字段，将忽略StartTime字段的设置）
        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
        :param _EnableBackupPeriodSave: 定期保留开关，off - 不开启定期保留策略，on - 开启定期保留策略，默认为off。首次开启定期保留策略时，BackupPeriodSaveDays，BackupPeriodSaveInterval，BackupPeriodSaveCount，StartBackupPeriodSaveDate参数为必填项，否则定期保留策略不会生效
        :type EnableBackupPeriodSave: str
        :param _EnableBackupPeriodLongTermSave: 长期保留开关,该字段功能暂未上线，可忽略。off - 不开启长期保留策略，on - 开启长期保留策略，默认为off，如果开启，则BackupPeriodSaveDays，BackupPeriodSaveInterval，BackupPeriodSaveCount参数无效
        :type EnableBackupPeriodLongTermSave: str
        :param _BackupPeriodSaveDays: 定期保留最长天数，最小值：90，最大值：3650，默认值：1080
        :type BackupPeriodSaveDays: int
        :param _BackupPeriodSaveInterval: 定期保留策略周期，可取值：weekly - 周，monthly - 月， quarterly - 季度，yearly - 年，默认为monthly
        :type BackupPeriodSaveInterval: str
        :param _BackupPeriodSaveCount: 定期保留的备份数量，最小值为1，最大值不超过定期保留策略周期内常规备份个数，默认值为1
        :type BackupPeriodSaveCount: int
        :param _StartBackupPeriodSaveDate: 定期保留策略周期起始日期，格式：YYYY-MM-dd HH:mm:ss
        :type StartBackupPeriodSaveDate: str
        :param _EnableBackupArchive: 是否开启数据备份归档策略，off-关闭，on-打开，默认为off
        :type EnableBackupArchive: str
        :param _BackupArchiveDays: 数据备份归档起始天数，数据备份达到归档起始天数时进行归档，最小为180天，不得大于数据备份保留天数
        :type BackupArchiveDays: int
        :param _BinlogArchiveDays: 日志备份归档起始天数，日志备份达到归档起始天数时进行归档，最小为180天，不得大于日志备份保留天数
        :type BinlogArchiveDays: int
        :param _EnableBinlogArchive: 是否开启日志备份归档策略，off-关闭，on-打开，默认为off
        :type EnableBinlogArchive: str
        :param _EnableBackupStandby: 是否开启数据备份标准存储策略，off-关闭，on-打开，默认为off
        :type EnableBackupStandby: str
        :param _BackupStandbyDays: 数据备份标准存储起始天数，数据备份达到标准存储起始天数时进行转换，最小为30天，不得大于数据备份保留天数。如果开启备份归档，不得大于等于备份归档天数
        :type BackupStandbyDays: int
        :param _EnableBinlogStandby: 是否开启日志备份标准存储策略，off-关闭，on-打开，默认为off
        :type EnableBinlogStandby: str
        :param _BinlogStandbyDays: 日志备份标准存储起始天数，日志备份达到标准存储起始天数时进行转换，最小为30天，不得大于日志备份保留天数。如果开启备份归档，不得大于等于备份归档天数
        :type BinlogStandbyDays: int
        """
        self._InstanceId = None
        self._ExpireDays = None
        self._StartTime = None
        self._BackupMethod = None
        self._BinlogExpireDays = None
        self._BackupTimeWindow = None
        self._EnableBackupPeriodSave = None
        self._EnableBackupPeriodLongTermSave = None
        self._BackupPeriodSaveDays = None
        self._BackupPeriodSaveInterval = None
        self._BackupPeriodSaveCount = None
        self._StartBackupPeriodSaveDate = None
        self._EnableBackupArchive = None
        self._BackupArchiveDays = None
        self._BinlogArchiveDays = None
        self._EnableBinlogArchive = None
        self._EnableBackupStandby = None
        self._BackupStandbyDays = None
        self._EnableBinlogStandby = None
        self._BinlogStandbyDays = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ExpireDays(self):
        return self._ExpireDays

    @ExpireDays.setter
    def ExpireDays(self, ExpireDays):
        self._ExpireDays = ExpireDays

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BinlogExpireDays(self):
        return self._BinlogExpireDays

    @BinlogExpireDays.setter
    def BinlogExpireDays(self, BinlogExpireDays):
        self._BinlogExpireDays = BinlogExpireDays

    @property
    def BackupTimeWindow(self):
        return self._BackupTimeWindow

    @BackupTimeWindow.setter
    def BackupTimeWindow(self, BackupTimeWindow):
        self._BackupTimeWindow = BackupTimeWindow

    @property
    def EnableBackupPeriodSave(self):
        return self._EnableBackupPeriodSave

    @EnableBackupPeriodSave.setter
    def EnableBackupPeriodSave(self, EnableBackupPeriodSave):
        self._EnableBackupPeriodSave = EnableBackupPeriodSave

    @property
    def EnableBackupPeriodLongTermSave(self):
        return self._EnableBackupPeriodLongTermSave

    @EnableBackupPeriodLongTermSave.setter
    def EnableBackupPeriodLongTermSave(self, EnableBackupPeriodLongTermSave):
        self._EnableBackupPeriodLongTermSave = EnableBackupPeriodLongTermSave

    @property
    def BackupPeriodSaveDays(self):
        return self._BackupPeriodSaveDays

    @BackupPeriodSaveDays.setter
    def BackupPeriodSaveDays(self, BackupPeriodSaveDays):
        self._BackupPeriodSaveDays = BackupPeriodSaveDays

    @property
    def BackupPeriodSaveInterval(self):
        return self._BackupPeriodSaveInterval

    @BackupPeriodSaveInterval.setter
    def BackupPeriodSaveInterval(self, BackupPeriodSaveInterval):
        self._BackupPeriodSaveInterval = BackupPeriodSaveInterval

    @property
    def BackupPeriodSaveCount(self):
        return self._BackupPeriodSaveCount

    @BackupPeriodSaveCount.setter
    def BackupPeriodSaveCount(self, BackupPeriodSaveCount):
        self._BackupPeriodSaveCount = BackupPeriodSaveCount

    @property
    def StartBackupPeriodSaveDate(self):
        return self._StartBackupPeriodSaveDate

    @StartBackupPeriodSaveDate.setter
    def StartBackupPeriodSaveDate(self, StartBackupPeriodSaveDate):
        self._StartBackupPeriodSaveDate = StartBackupPeriodSaveDate

    @property
    def EnableBackupArchive(self):
        return self._EnableBackupArchive

    @EnableBackupArchive.setter
    def EnableBackupArchive(self, EnableBackupArchive):
        self._EnableBackupArchive = EnableBackupArchive

    @property
    def BackupArchiveDays(self):
        return self._BackupArchiveDays

    @BackupArchiveDays.setter
    def BackupArchiveDays(self, BackupArchiveDays):
        self._BackupArchiveDays = BackupArchiveDays

    @property
    def BinlogArchiveDays(self):
        return self._BinlogArchiveDays

    @BinlogArchiveDays.setter
    def BinlogArchiveDays(self, BinlogArchiveDays):
        self._BinlogArchiveDays = BinlogArchiveDays

    @property
    def EnableBinlogArchive(self):
        return self._EnableBinlogArchive

    @EnableBinlogArchive.setter
    def EnableBinlogArchive(self, EnableBinlogArchive):
        self._EnableBinlogArchive = EnableBinlogArchive

    @property
    def EnableBackupStandby(self):
        return self._EnableBackupStandby

    @EnableBackupStandby.setter
    def EnableBackupStandby(self, EnableBackupStandby):
        self._EnableBackupStandby = EnableBackupStandby

    @property
    def BackupStandbyDays(self):
        return self._BackupStandbyDays

    @BackupStandbyDays.setter
    def BackupStandbyDays(self, BackupStandbyDays):
        self._BackupStandbyDays = BackupStandbyDays

    @property
    def EnableBinlogStandby(self):
        return self._EnableBinlogStandby

    @EnableBinlogStandby.setter
    def EnableBinlogStandby(self, EnableBinlogStandby):
        self._EnableBinlogStandby = EnableBinlogStandby

    @property
    def BinlogStandbyDays(self):
        return self._BinlogStandbyDays

    @BinlogStandbyDays.setter
    def BinlogStandbyDays(self, BinlogStandbyDays):
        self._BinlogStandbyDays = BinlogStandbyDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ExpireDays = params.get("ExpireDays")
        self._StartTime = params.get("StartTime")
        self._BackupMethod = params.get("BackupMethod")
        self._BinlogExpireDays = params.get("BinlogExpireDays")
        if params.get("BackupTimeWindow") is not None:
            self._BackupTimeWindow = CommonTimeWindow()
            self._BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
        self._EnableBackupPeriodSave = params.get("EnableBackupPeriodSave")
        self._EnableBackupPeriodLongTermSave = params.get("EnableBackupPeriodLongTermSave")
        self._BackupPeriodSaveDays = params.get("BackupPeriodSaveDays")
        self._BackupPeriodSaveInterval = params.get("BackupPeriodSaveInterval")
        self._BackupPeriodSaveCount = params.get("BackupPeriodSaveCount")
        self._StartBackupPeriodSaveDate = params.get("StartBackupPeriodSaveDate")
        self._EnableBackupArchive = params.get("EnableBackupArchive")
        self._BackupArchiveDays = params.get("BackupArchiveDays")
        self._BinlogArchiveDays = params.get("BinlogArchiveDays")
        self._EnableBinlogArchive = params.get("EnableBinlogArchive")
        self._EnableBackupStandby = params.get("EnableBackupStandby")
        self._BackupStandbyDays = params.get("BackupStandbyDays")
        self._EnableBinlogStandby = params.get("EnableBinlogStandby")
        self._BinlogStandbyDays = params.get("BinlogStandbyDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig返回参数结构体

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


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    """ModifyBackupDownloadRestriction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LimitType: NoLimit 不限制,内外网都可以下载； LimitOnlyIntranet 仅内网可下载； Customize 用户自定义vpc:ip可下载。 只有该值为 Customize 时，才可以设置 LimitVpc 和 LimitIp 。
        :type LimitType: str
        :param _VpcComparisonSymbol: 该参数仅支持 In， 表示 LimitVpc 指定的vpc可以下载。默认为In。
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: In: 指定的ip可以下载； NotIn: 指定的ip不可以下载。 默认为In。
        :type IpComparisonSymbol: str
        :param _LimitVpc: 限制下载的vpc设置。
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: 限制下载的ip设置
        :type LimitIp: list of str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None

    @property
    def LimitType(self):
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    """ModifyBackupDownloadRestriction返回参数结构体

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


class ModifyBackupEncryptionStatusRequest(AbstractModel):
    """ModifyBackupEncryptionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cdb-XXXX。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _EncryptionStatus: 设置实例新增的自动物理备份文件默认加密状态。可选值为 on或者off。
        :type EncryptionStatus: str
        """
        self._InstanceId = None
        self._EncryptionStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EncryptionStatus(self):
        return self._EncryptionStatus

    @EncryptionStatus.setter
    def EncryptionStatus(self, EncryptionStatus):
        self._EncryptionStatus = EncryptionStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EncryptionStatus = params.get("EncryptionStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupEncryptionStatusResponse(AbstractModel):
    """ModifyBackupEncryptionStatus返回参数结构体

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


class ModifyCdbProxyAddressDescRequest(AbstractModel):
    """ModifyCdbProxyAddressDesc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _ProxyAddressId: 代理组地址ID
        :type ProxyAddressId: str
        :param _Desc: 描述
        :type Desc: str
        """
        self._ProxyGroupId = None
        self._ProxyAddressId = None
        self._Desc = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyAddressId = params.get("ProxyAddressId")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCdbProxyAddressDescResponse(AbstractModel):
    """ModifyCdbProxyAddressDesc返回参数结构体

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


class ModifyCdbProxyAddressVipAndVPortRequest(AbstractModel):
    """ModifyCdbProxyAddressVipAndVPort请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _ProxyAddressId: 代理组地址ID
        :type ProxyAddressId: str
        :param _UniqVpcId: 私有网络ID
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有子网ID
        :type UniqSubnetId: str
        :param _Vip: IP地址
        :type Vip: str
        :param _VPort: 端口
        :type VPort: int
        :param _ReleaseDuration: 旧IP地址回收时间
        :type ReleaseDuration: int
        """
        self._ProxyGroupId = None
        self._ProxyAddressId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Vip = None
        self._VPort = None
        self._ReleaseDuration = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def ReleaseDuration(self):
        return self._ReleaseDuration

    @ReleaseDuration.setter
    def ReleaseDuration(self, ReleaseDuration):
        self._ReleaseDuration = ReleaseDuration


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyAddressId = params.get("ProxyAddressId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._ReleaseDuration = params.get("ReleaseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCdbProxyAddressVipAndVPortResponse(AbstractModel):
    """ModifyCdbProxyAddressVipAndVPort返回参数结构体

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


class ModifyCdbProxyParamRequest(AbstractModel):
    """ModifyCdbProxyParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _ConnectionPoolLimit: 连接池阈值
        :type ConnectionPoolLimit: int
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._ConnectionPoolLimit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ConnectionPoolLimit(self):
        return self._ConnectionPoolLimit

    @ConnectionPoolLimit.setter
    def ConnectionPoolLimit(self, ConnectionPoolLimit):
        self._ConnectionPoolLimit = ConnectionPoolLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ConnectionPoolLimit = params.get("ConnectionPoolLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCdbProxyParamResponse(AbstractModel):
    """ModifyCdbProxyParam返回参数结构体

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


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param _InstanceName: 修改后的实例名称。
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

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
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName返回参数结构体

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


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIds: list of str
        :param _NewProjectId: 项目的 ID。
        :type NewProjectId: int
        """
        self._InstanceIds = None
        self._NewProjectId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def NewProjectId(self):
        return self._NewProjectId

    @NewProjectId.setter
    def NewProjectId(self, NewProjectId):
        self._NewProjectId = NewProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._NewProjectId = params.get("NewProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject返回参数结构体

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


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _SecurityGroupIds: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        :param _ForReadonlyInstance: 当传入只读实例ID时，默认操作的是对应只读组的安全组。如果需要操作只读实例ID的安全组， 需要将该入参置为True
        :type ForReadonlyInstance: bool
        """
        self._InstanceId = None
        self._SecurityGroupIds = None
        self._ForReadonlyInstance = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ForReadonlyInstance(self):
        return self._ForReadonlyInstance

    @ForReadonlyInstance.setter
    def ForReadonlyInstance(self, ForReadonlyInstance):
        self._ForReadonlyInstance = ForReadonlyInstance


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

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


class ModifyDBInstanceVipVportRequest(AbstractModel):
    """ModifyDBInstanceVipVport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c2nl9rpv 或者 cdbrg-c3nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param _DstIp: 目标 IP。该参数和 DstPort 参数，两者必传一个。
        :type DstIp: str
        :param _DstPort: 目标端口，支持范围为：[1024-65535]。该参数和 DstIp 参数，两者必传一个。
        :type DstPort: int
        :param _UniqVpcId: 私有网络统一 ID。
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网统一 ID。
        :type UniqSubnetId: str
        :param _ReleaseDuration: 进行基础网络转 VPC 网络和 VPC 网络下的子网变更时，原网络中旧IP的回收时间，单位为小时，取值范围为0-168，默认值为24小时。
        :type ReleaseDuration: int
        """
        self._InstanceId = None
        self._DstIp = None
        self._DstPort = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ReleaseDuration = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DstIp(self):
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ReleaseDuration(self):
        return self._ReleaseDuration

    @ReleaseDuration.setter
    def ReleaseDuration(self, ReleaseDuration):
        self._ReleaseDuration = ReleaseDuration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ReleaseDuration = params.get("ReleaseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceVipVportResponse(AbstractModel):
    """ModifyDBInstanceVipVport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务ID。(该返回字段目前已废弃)
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例短 ID 列表。
        :type InstanceIds: list of str
        :param _ParamList: 要修改的参数列表。每一个元素是 Name 和 CurrentValue 的组合。Name 是参数名，CurrentValue 是要修改成的值。
        :type ParamList: list of Parameter
        :param _TemplateId: 模板id，ParamList和TemplateId必须至少传其中之一
        :type TemplateId: int
        :param _WaitSwitch: 执行参数调整任务的方式，默认为 0。支持值包括：0 - 立刻执行，1 - 时间窗执行；当该值为 1 时，每次只能传一个实例（InstanceIds数量为1）
        :type WaitSwitch: int
        :param _NotSyncRo: 参数是否同步到主实例下的只读实例。true 为不同步，false 为同步。默认为 false。
        :type NotSyncRo: bool
        :param _NotSyncDr: 参数是否同步到主实例下的灾备实例。true 为不同步，false 为同步。默认为 false。
        :type NotSyncDr: bool
        """
        self._InstanceIds = None
        self._ParamList = None
        self._TemplateId = None
        self._WaitSwitch = None
        self._NotSyncRo = None
        self._NotSyncDr = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch

    @property
    def NotSyncRo(self):
        return self._NotSyncRo

    @NotSyncRo.setter
    def NotSyncRo(self, NotSyncRo):
        self._NotSyncRo = NotSyncRo

    @property
    def NotSyncDr(self):
        return self._NotSyncDr

    @NotSyncDr.setter
    def NotSyncDr(self, NotSyncDr):
        self._NotSyncDr = NotSyncDr


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._TemplateId = params.get("TemplateId")
        self._WaitSwitch = params.get("WaitSwitch")
        self._NotSyncRo = params.get("NotSyncRo")
        self._NotSyncDr = params.get("NotSyncDr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务 ID，可用于查询任务进度。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyInstancePasswordComplexityRequest(AbstractModel):
    """ModifyInstancePasswordComplexity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例短 ID 列表。
        :type InstanceIds: list of str
        :param _ParamList: 要修改的参数列表。每一个元素是Name和CurrentValue的组合。Name是参数名，CurrentValue是要修改成的值。8.0版本Name支持范围：["validate_password.policy","validate_password.length","validate_password.mixed_case_count","validate_password.number_count","validate_password.special_char_count"],5.6和5.7版本支持范围：["validate_password_policy","validate_password_length","validate_password_mixed_case_count","validate_password_number_count","validate_password_special_char_count"]
        :type ParamList: list of Parameter
        """
        self._InstanceIds = None
        self._ParamList = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancePasswordComplexityResponse(AbstractModel):
    """ModifyInstancePasswordComplexity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务 ID，可用于查询任务进度。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceTagRequest(AbstractModel):
    """ModifyInstanceTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _ReplaceTags: 要增加或修改的标签。
        :type ReplaceTags: list of TagInfo
        :param _DeleteTags: 要删除的标签。
        :type DeleteTags: list of TagInfo
        """
        self._InstanceId = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReplaceTags(self):
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceTagResponse(AbstractModel):
    """ModifyInstanceTag返回参数结构体

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


class ModifyLocalBinlogConfigRequest(AbstractModel):
    """ModifyLocalBinlogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param _SaveHours: 本地binlog保留时长，可取值范围：[72,168]，当实例存在灾备实例时，可取值范围：[120,168]。
        :type SaveHours: int
        :param _MaxUsage: 本地binlog空间使用率，可取值范围：[30,50]。
        :type MaxUsage: int
        """
        self._InstanceId = None
        self._SaveHours = None
        self._MaxUsage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SaveHours(self):
        return self._SaveHours

    @SaveHours.setter
    def SaveHours(self, SaveHours):
        self._SaveHours = SaveHours

    @property
    def MaxUsage(self):
        return self._MaxUsage

    @MaxUsage.setter
    def MaxUsage(self, MaxUsage):
        self._MaxUsage = MaxUsage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SaveHours = params.get("SaveHours")
        self._MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLocalBinlogConfigResponse(AbstractModel):
    """ModifyLocalBinlogConfig返回参数结构体

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


class ModifyNameOrDescByDpIdRequest(AbstractModel):
    """ModifyNameOrDescByDpId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param _DeployGroupName: 置放群组名称，最长不能超过60个字符。置放群组名和置放群组描述不能都为空。
        :type DeployGroupName: str
        :param _Description: 置放群组描述，最长不能超过200个字符。置放群组名和置放群组描述不能都为空。
        :type Description: str
        """
        self._DeployGroupId = None
        self._DeployGroupName = None
        self._Description = None

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def DeployGroupName(self):
        return self._DeployGroupName

    @DeployGroupName.setter
    def DeployGroupName(self, DeployGroupName):
        self._DeployGroupName = DeployGroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DeployGroupId = params.get("DeployGroupId")
        self._DeployGroupName = params.get("DeployGroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNameOrDescByDpIdResponse(AbstractModel):
    """ModifyNameOrDescByDpId返回参数结构体

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


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID。
        :type TemplateId: int
        :param _Name: 模板名称，长度不超过64。
        :type Name: str
        :param _Description: 模板描述，长度不超过255。
        :type Description: str
        :param _ParamList: 参数列表。
        :type ParamList: list of Parameter
        """
        self._TemplateId = None
        self._Name = None
        self._Description = None
        self._ParamList = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

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
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate返回参数结构体

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


class ModifyRemoteBackupConfigRequest(AbstractModel):
    """ModifyRemoteBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _RemoteBackupSave: 异地数据备份开关，off - 关闭异地备份，on-开启异地备份
        :type RemoteBackupSave: str
        :param _RemoteBinlogSave: 异地日志备份开关，off - 关闭异地备份，on-开启异地备份，只有在参数RemoteBackupSave为on时，RemoteBinlogSave参数才可设置为on
        :type RemoteBinlogSave: str
        :param _RemoteRegion: 用户设置异地备份地域列表
        :type RemoteRegion: list of str
        :param _ExpireDays: 异地备份保留时间，单位为天
        :type ExpireDays: int
        """
        self._InstanceId = None
        self._RemoteBackupSave = None
        self._RemoteBinlogSave = None
        self._RemoteRegion = None
        self._ExpireDays = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RemoteBackupSave(self):
        return self._RemoteBackupSave

    @RemoteBackupSave.setter
    def RemoteBackupSave(self, RemoteBackupSave):
        self._RemoteBackupSave = RemoteBackupSave

    @property
    def RemoteBinlogSave(self):
        return self._RemoteBinlogSave

    @RemoteBinlogSave.setter
    def RemoteBinlogSave(self, RemoteBinlogSave):
        self._RemoteBinlogSave = RemoteBinlogSave

    @property
    def RemoteRegion(self):
        return self._RemoteRegion

    @RemoteRegion.setter
    def RemoteRegion(self, RemoteRegion):
        self._RemoteRegion = RemoteRegion

    @property
    def ExpireDays(self):
        return self._ExpireDays

    @ExpireDays.setter
    def ExpireDays(self, ExpireDays):
        self._ExpireDays = ExpireDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RemoteBackupSave = params.get("RemoteBackupSave")
        self._RemoteBinlogSave = params.get("RemoteBinlogSave")
        self._RemoteRegion = params.get("RemoteRegion")
        self._ExpireDays = params.get("ExpireDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRemoteBackupConfigResponse(AbstractModel):
    """ModifyRemoteBackupConfig返回参数结构体

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


class ModifyRoGroupInfoRequest(AbstractModel):
    """ModifyRoGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoGroupId: RO 组的 ID。
        :type RoGroupId: str
        :param _RoGroupInfo: RO 组的详细信息。
        :type RoGroupInfo: :class:`tencentcloud.cdb.v20170320.models.RoGroupAttr`
        :param _RoWeightValues: RO 组内实例的权重。若修改 RO 组的权重模式为用户自定义模式（custom），则必须设置该参数，且需要设置每个 RO 实例的权重值。
        :type RoWeightValues: list of RoWeightValue
        :param _IsBalanceRoLoad: 是否重新均衡 RO 组内的 RO 实例的负载。支持值包括：1 - 重新均衡负载；0 - 不重新均衡负载。默认值为 0。注意，设置为重新均衡负载时，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库。
        :type IsBalanceRoLoad: int
        :param _ReplicationDelayTime: 废弃参数，无意义。
        :type ReplicationDelayTime: int
        """
        self._RoGroupId = None
        self._RoGroupInfo = None
        self._RoWeightValues = None
        self._IsBalanceRoLoad = None
        self._ReplicationDelayTime = None

    @property
    def RoGroupId(self):
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId

    @property
    def RoGroupInfo(self):
        return self._RoGroupInfo

    @RoGroupInfo.setter
    def RoGroupInfo(self, RoGroupInfo):
        self._RoGroupInfo = RoGroupInfo

    @property
    def RoWeightValues(self):
        return self._RoWeightValues

    @RoWeightValues.setter
    def RoWeightValues(self, RoWeightValues):
        self._RoWeightValues = RoWeightValues

    @property
    def IsBalanceRoLoad(self):
        return self._IsBalanceRoLoad

    @IsBalanceRoLoad.setter
    def IsBalanceRoLoad(self, IsBalanceRoLoad):
        self._IsBalanceRoLoad = IsBalanceRoLoad

    @property
    def ReplicationDelayTime(self):
        return self._ReplicationDelayTime

    @ReplicationDelayTime.setter
    def ReplicationDelayTime(self, ReplicationDelayTime):
        self._ReplicationDelayTime = ReplicationDelayTime


    def _deserialize(self, params):
        self._RoGroupId = params.get("RoGroupId")
        if params.get("RoGroupInfo") is not None:
            self._RoGroupInfo = RoGroupAttr()
            self._RoGroupInfo._deserialize(params.get("RoGroupInfo"))
        if params.get("RoWeightValues") is not None:
            self._RoWeightValues = []
            for item in params.get("RoWeightValues"):
                obj = RoWeightValue()
                obj._deserialize(item)
                self._RoWeightValues.append(obj)
        self._IsBalanceRoLoad = params.get("IsBalanceRoLoad")
        self._ReplicationDelayTime = params.get("ReplicationDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoGroupInfoResponse(AbstractModel):
    """ModifyRoGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyTimeWindowRequest(AbstractModel):
    """ModifyTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _TimeRanges: 修改后的可维护时间段，其中每一个时间段的格式形如：10:00-12:00；起止时间按半个小时对齐；最短半个小时，最长三个小时；最多设置两个时间段；起止时间范围为：[00:00, 24:00]。
        :type TimeRanges: list of str
        :param _Weekdays: 指定修改哪一天的客户时间段，可能的取值为：monday，tuesday，wednesday，thursday，friday，saturday，sunday。如果不指定该值或者为空，则默认一周七天都修改。
        :type Weekdays: list of str
        :param _MaxDelayTime: 数据延迟阈值，仅对主实例和灾备实例有效，不传默认修改为10
        :type MaxDelayTime: int
        """
        self._InstanceId = None
        self._TimeRanges = None
        self._Weekdays = None
        self._MaxDelayTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TimeRanges(self):
        return self._TimeRanges

    @TimeRanges.setter
    def TimeRanges(self, TimeRanges):
        self._TimeRanges = TimeRanges

    @property
    def Weekdays(self):
        return self._Weekdays

    @Weekdays.setter
    def Weekdays(self, Weekdays):
        self._Weekdays = Weekdays

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TimeRanges = params.get("TimeRanges")
        self._Weekdays = params.get("Weekdays")
        self._MaxDelayTime = params.get("MaxDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTimeWindowResponse(AbstractModel):
    """ModifyTimeWindow返回参数结构体

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


class OfflineIsolatedInstancesRequest(AbstractModel):
    """OfflineIsolatedInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedInstancesResponse(AbstractModel):
    """OfflineIsolatedInstances返回参数结构体

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


class OpenAuditServiceRequest(AbstractModel):
    """OpenAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: CDB实例ID
        :type InstanceId: str
        :param _LogExpireDay: 审计日志保存时长。支持值包括：
7 - 一周
30 - 一个月；
90 - 三个月；
180 - 六个月；
365 - 一年；
1095 - 三年；
1825 - 五年；
        :type LogExpireDay: int
        :param _HighLogExpireDay: 高频审计日志保存时长。支持值包括：
7 - 一周
30 - 一个月；
        :type HighLogExpireDay: int
        :param _AuditRuleFilters: 审计规则。同RuleTemplateIds都不填是全审计。
        :type AuditRuleFilters: list of AuditRuleFilters
        :param _RuleTemplateIds: 规则模版ID。同AuditRuleFilters都不填是全审计。
        :type RuleTemplateIds: list of str
        """
        self._InstanceId = None
        self._LogExpireDay = None
        self._HighLogExpireDay = None
        self._AuditRuleFilters = None
        self._RuleTemplateIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def AuditRuleFilters(self):
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HighLogExpireDay = params.get("HighLogExpireDay")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceResponse(AbstractModel):
    """OpenAuditService返回参数结构体

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


class OpenDBInstanceEncryptionRequest(AbstractModel):
    """OpenDBInstanceEncryption请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 云数据库实例 ID。
        :type InstanceId: str
        :param _KeyId: 用户自定义密钥ID，CMK唯一标识符。该值为空时，将使用腾讯云自动生成的密钥KMS-CDB。
        :type KeyId: str
        :param _KeyRegion: 用户自定义密钥的存储地域。如：ap-guangzhou 。KeyId不为空时，该参数必填。
        :type KeyRegion: str
        """
        self._InstanceId = None
        self._KeyId = None
        self._KeyRegion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyRegion(self):
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KeyId = params.get("KeyId")
        self._KeyRegion = params.get("KeyRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBInstanceEncryptionResponse(AbstractModel):
    """OpenDBInstanceEncryption返回参数结构体

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


class OpenDBInstanceGTIDRequest(AbstractModel):
    """OpenDBInstanceGTID请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBInstanceGTIDResponse(AbstractModel):
    """OpenDBInstanceGTID返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class OpenWanServiceRequest(AbstractModel):
    """OpenWanService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWanServiceResponse(AbstractModel):
    """OpenWanService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """安全组出站规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param _CidrIp: 目的 IP 或 IP 段，例如172.16.0.0/12
        :type CidrIp: str
        :param _PortRange: 端口或者端口范围
        :type PortRange: str
        :param _IpProtocol: 网络协议，支持 UDP、TCP等
        :type IpProtocol: str
        :param _Dir: 规则限定的方向，进站规则为 OUTPUT
        :type Dir: str
        :param _AddressModule: 地址模块
        :type AddressModule: str
        :param _Desc: 规则描述
        :type Desc: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Dir = None
        self._AddressModule = None
        self._Desc = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Dir(self):
        return self._Dir

    @Dir.setter
    def Dir(self, Dir):
        self._Dir = Dir

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Dir = params.get("Dir")
        self._AddressModule = params.get("AddressModule")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    """实例参数信息

    """

    def __init__(self):
        r"""
        :param _Name: 参数名
        :type Name: str
        :param _Value: 参数值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamRecord(AbstractModel):
    """参数修改记录

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _OldValue: 参数修改前的值
        :type OldValue: str
        :param _NewValue: 参数修改后的值
        :type NewValue: str
        :param _IsSucess: 参数是否修改成功
        :type IsSucess: bool
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._ParamName = None
        self._OldValue = None
        self._NewValue = None
        self._IsSucess = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def IsSucess(self):
        return self._IsSucess

    @IsSucess.setter
    def IsSucess(self, IsSucess):
        self._IsSucess = IsSucess

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ParamName = params.get("ParamName")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        self._IsSucess = params.get("IsSucess")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateInfo(AbstractModel):
    """参数模板信息

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID
        :type TemplateId: int
        :param _Name: 参数模板名称
        :type Name: str
        :param _Description: 参数模板描述
        :type Description: str
        :param _EngineVersion: 实例引擎版本
        :type EngineVersion: str
        :param _TemplateType: 参数模板类型
        :type TemplateType: str
        :param _EngineType: 参数模板引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineType: str
        """
        self._TemplateId = None
        self._Name = None
        self._Description = None
        self._EngineVersion = None
        self._TemplateType = None
        self._EngineType = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

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
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EngineVersion = params.get("EngineVersion")
        self._TemplateType = params.get("TemplateType")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Parameter(AbstractModel):
    """数据库实例参数

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _CurrentValue: 参数值
        :type CurrentValue: str
        """
        self._Name = None
        self._CurrentValue = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CurrentValue = params.get("CurrentValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    """实例参数的详细描述

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称
        :type Name: str
        :param _ParamType: 参数类型：integer，enum，float，string，func
        :type ParamType: str
        :param _Default: 参数默认值
        :type Default: str
        :param _Description: 参数描述
        :type Description: str
        :param _CurrentValue: 参数当前值
        :type CurrentValue: str
        :param _NeedReboot: 修改参数后，是否需要重启数据库以使参数生效。可能的值包括：0-不需要重启；1-需要重启
        :type NeedReboot: int
        :param _Max: 参数允许的最大值
        :type Max: int
        :param _Min: 参数允许的最小值
        :type Min: int
        :param _EnumValue: 参数的可选枚举值。如果为非枚举参数，则为空
        :type EnumValue: list of str
        :param _MaxFunc: 参数是公式类型时，该字段有效，表示公式类型最大值
        :type MaxFunc: str
        :param _MinFunc: 参数是公式类型时，该字段有效，表示公式类型最小值
        :type MinFunc: str
        :param _IsNotSupportEdit: 参数是否不支持修改
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNotSupportEdit: bool
        """
        self._Name = None
        self._ParamType = None
        self._Default = None
        self._Description = None
        self._CurrentValue = None
        self._NeedReboot = None
        self._Max = None
        self._Min = None
        self._EnumValue = None
        self._MaxFunc = None
        self._MinFunc = None
        self._IsNotSupportEdit = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def MaxFunc(self):
        return self._MaxFunc

    @MaxFunc.setter
    def MaxFunc(self, MaxFunc):
        self._MaxFunc = MaxFunc

    @property
    def MinFunc(self):
        return self._MinFunc

    @MinFunc.setter
    def MinFunc(self, MinFunc):
        self._MinFunc = MinFunc

    @property
    def IsNotSupportEdit(self):
        return self._IsNotSupportEdit

    @IsNotSupportEdit.setter
    def IsNotSupportEdit(self, IsNotSupportEdit):
        self._IsNotSupportEdit = IsNotSupportEdit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ParamType = params.get("ParamType")
        self._Default = params.get("Default")
        self._Description = params.get("Description")
        self._CurrentValue = params.get("CurrentValue")
        self._NeedReboot = params.get("NeedReboot")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        self._MaxFunc = params.get("MaxFunc")
        self._MinFunc = params.get("MinFunc")
        self._IsNotSupportEdit = params.get("IsNotSupportEdit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyAddress(AbstractModel):
    """数据库代理地址信息

    """

    def __init__(self):
        r"""
        :param _ProxyAddressId: 代理组地址ID
        :type ProxyAddressId: str
        :param _UniqVpcId: 私有网络ID
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有子网ID
        :type UniqSubnetId: str
        :param _Vip: IP地址
        :type Vip: str
        :param _VPort: 端口
        :type VPort: int
        :param _WeightMode: 权重分配模式；
系统自动分配："system"， 自定义："custom"
注意：此字段可能返回 null，表示取不到有效值。
        :type WeightMode: str
        :param _IsKickOut: 是否开启延迟剔除，取值："true" | "false"
注意：此字段可能返回 null，表示取不到有效值。
        :type IsKickOut: bool
        :param _MinCount: 最小保留数量，最小取值：0
注意：此字段可能返回 null，表示取不到有效值。
        :type MinCount: int
        :param _MaxDelay: 延迟剔除阈值，最小取值：0
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDelay: int
        :param _AutoAddRo: 是否自动添加RO，取值："true" | "false"
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoAddRo: bool
        :param _ReadOnly: 是否是只读，取值："true" | "false"
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnly: bool
        :param _TransSplit: 是否开启事务分离
注意：此字段可能返回 null，表示取不到有效值。
        :type TransSplit: bool
        :param _FailOver: 是否开启故障转移
注意：此字段可能返回 null，表示取不到有效值。
        :type FailOver: bool
        :param _ConnectionPool: 是否开启连接池
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPool: bool
        :param _Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _ProxyAllocation: 实例读权重分配
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyAllocation: list of ProxyAllocation
        """
        self._ProxyAddressId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Vip = None
        self._VPort = None
        self._WeightMode = None
        self._IsKickOut = None
        self._MinCount = None
        self._MaxDelay = None
        self._AutoAddRo = None
        self._ReadOnly = None
        self._TransSplit = None
        self._FailOver = None
        self._ConnectionPool = None
        self._Desc = None
        self._ProxyAllocation = None

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def IsKickOut(self):
        return self._IsKickOut

    @IsKickOut.setter
    def IsKickOut(self, IsKickOut):
        self._IsKickOut = IsKickOut

    @property
    def MinCount(self):
        return self._MinCount

    @MinCount.setter
    def MinCount(self, MinCount):
        self._MinCount = MinCount

    @property
    def MaxDelay(self):
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ProxyAllocation(self):
        return self._ProxyAllocation

    @ProxyAllocation.setter
    def ProxyAllocation(self, ProxyAllocation):
        self._ProxyAllocation = ProxyAllocation


    def _deserialize(self, params):
        self._ProxyAddressId = params.get("ProxyAddressId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._WeightMode = params.get("WeightMode")
        self._IsKickOut = params.get("IsKickOut")
        self._MinCount = params.get("MinCount")
        self._MaxDelay = params.get("MaxDelay")
        self._AutoAddRo = params.get("AutoAddRo")
        self._ReadOnly = params.get("ReadOnly")
        self._TransSplit = params.get("TransSplit")
        self._FailOver = params.get("FailOver")
        self._ConnectionPool = params.get("ConnectionPool")
        self._Desc = params.get("Desc")
        if params.get("ProxyAllocation") is not None:
            self._ProxyAllocation = []
            for item in params.get("ProxyAllocation"):
                obj = ProxyAllocation()
                obj._deserialize(item)
                self._ProxyAllocation.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyAllocation(AbstractModel):
    """代理节点权重分布

    """

    def __init__(self):
        r"""
        :param _Region: 代理节点所属地域
        :type Region: str
        :param _Zone: 代理节点所属可用区
        :type Zone: str
        :param _ProxyInstance: 代理实例分布
        :type ProxyInstance: list of ProxyInst
        """
        self._Region = None
        self._Zone = None
        self._ProxyInstance = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProxyInstance(self):
        return self._ProxyInstance

    @ProxyInstance.setter
    def ProxyInstance(self, ProxyInstance):
        self._ProxyInstance = ProxyInstance


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        if params.get("ProxyInstance") is not None:
            self._ProxyInstance = []
            for item in params.get("ProxyInstance"):
                obj = ProxyInst()
                obj._deserialize(item)
                self._ProxyInstance.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupInfo(AbstractModel):
    """代理组详情

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _ProxyVersion: 代理版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyVersion: str
        :param _SupportUpgradeProxyVersion: 代理支持升级版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportUpgradeProxyVersion: str
        :param _Status: 代理状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _TaskStatus: 代理任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        :param _ProxyNode: 代理组节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNode: list of ProxyNode
        :param _ProxyAddress: 代理组地址信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyAddress: list of ProxyAddress
        :param _ConnectionPoolLimit: 连接池阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPoolLimit: int
        :param _SupportCreateProxyAddress: 支持创建地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportCreateProxyAddress: bool
        :param _SupportUpgradeProxyMysqlVersion: 支持升级代理版本所需的cdb版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportUpgradeProxyMysqlVersion: str
        """
        self._ProxyGroupId = None
        self._ProxyVersion = None
        self._SupportUpgradeProxyVersion = None
        self._Status = None
        self._TaskStatus = None
        self._ProxyNode = None
        self._ProxyAddress = None
        self._ConnectionPoolLimit = None
        self._SupportCreateProxyAddress = None
        self._SupportUpgradeProxyMysqlVersion = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyVersion(self):
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def SupportUpgradeProxyVersion(self):
        return self._SupportUpgradeProxyVersion

    @SupportUpgradeProxyVersion.setter
    def SupportUpgradeProxyVersion(self, SupportUpgradeProxyVersion):
        self._SupportUpgradeProxyVersion = SupportUpgradeProxyVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ProxyNode(self):
        return self._ProxyNode

    @ProxyNode.setter
    def ProxyNode(self, ProxyNode):
        self._ProxyNode = ProxyNode

    @property
    def ProxyAddress(self):
        return self._ProxyAddress

    @ProxyAddress.setter
    def ProxyAddress(self, ProxyAddress):
        self._ProxyAddress = ProxyAddress

    @property
    def ConnectionPoolLimit(self):
        return self._ConnectionPoolLimit

    @ConnectionPoolLimit.setter
    def ConnectionPoolLimit(self, ConnectionPoolLimit):
        self._ConnectionPoolLimit = ConnectionPoolLimit

    @property
    def SupportCreateProxyAddress(self):
        return self._SupportCreateProxyAddress

    @SupportCreateProxyAddress.setter
    def SupportCreateProxyAddress(self, SupportCreateProxyAddress):
        self._SupportCreateProxyAddress = SupportCreateProxyAddress

    @property
    def SupportUpgradeProxyMysqlVersion(self):
        return self._SupportUpgradeProxyMysqlVersion

    @SupportUpgradeProxyMysqlVersion.setter
    def SupportUpgradeProxyMysqlVersion(self, SupportUpgradeProxyMysqlVersion):
        self._SupportUpgradeProxyMysqlVersion = SupportUpgradeProxyMysqlVersion


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyVersion = params.get("ProxyVersion")
        self._SupportUpgradeProxyVersion = params.get("SupportUpgradeProxyVersion")
        self._Status = params.get("Status")
        self._TaskStatus = params.get("TaskStatus")
        if params.get("ProxyNode") is not None:
            self._ProxyNode = []
            for item in params.get("ProxyNode"):
                obj = ProxyNode()
                obj._deserialize(item)
                self._ProxyNode.append(obj)
        if params.get("ProxyAddress") is not None:
            self._ProxyAddress = []
            for item in params.get("ProxyAddress"):
                obj = ProxyAddress()
                obj._deserialize(item)
                self._ProxyAddress.append(obj)
        self._ConnectionPoolLimit = params.get("ConnectionPoolLimit")
        self._SupportCreateProxyAddress = params.get("SupportCreateProxyAddress")
        self._SupportUpgradeProxyMysqlVersion = params.get("SupportUpgradeProxyMysqlVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyInst(AbstractModel):
    """代理实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _InstanceType: 实例类型：1 master 主实例; 2 ro 只读实例; 3 dr 灾备实例; 4 sdr 小灾备实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: int
        :param _Status: 实例状态，可能的返回值：0-创建中；1-运行中；4-隔离中；5-已隔离
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Weight: 只读权重,如果权重为系统自动分配，改值不生效，只代表是否启用该实例
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _Region: 实例所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zone: 实例所属可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._Status = None
        self._Weight = None
        self._Region = None
        self._Zone = None

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
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._Status = params.get("Status")
        self._Weight = params.get("Weight")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNode(AbstractModel):
    """代理节点

    """

    def __init__(self):
        r"""
        :param _ProxyId: 代理节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyId: str
        :param _Cpu: CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Mem: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: int
        :param _Status: 节点状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Zone: 代理节点可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _Region: 代理节点地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Connection: 连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type Connection: int
        """
        self._ProxyId = None
        self._Cpu = None
        self._Mem = None
        self._Status = None
        self._Zone = None
        self._Region = None
        self._Connection = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Connection(self):
        return self._Connection

    @Connection.setter
    def Connection(self, Connection):
        self._Connection = Connection


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Status = params.get("Status")
        self._Zone = params.get("Zone")
        self._Region = params.get("Region")
        self._Connection = params.get("Connection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodeCustom(AbstractModel):
    """节点规格配置

    """

    def __init__(self):
        r"""
        :param _NodeCount: 节点个数
        :type NodeCount: int
        :param _Cpu: CPU核数
        :type Cpu: int
        :param _Mem: 内存大小
        :type Mem: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        """
        self._NodeCount = None
        self._Cpu = None
        self._Mem = None
        self._Region = None
        self._Zone = None

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._NodeCount = params.get("NodeCount")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIsolatedDBInstancesRequest(AbstractModel):
    """ReleaseIsolatedDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 数组，单个实例 ID 格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIsolatedDBInstancesResponse(AbstractModel):
    """ReleaseIsolatedDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 解隔离操作的结果集。
        :type Items: list of ReleaseResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ReleaseResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ReleaseResult(AbstractModel):
    """解隔离任务结果

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Code: 实例解隔离操作的结果值。返回值为0表示成功。
        :type Code: int
        :param _Message: 实例解隔离操作的错误信息。
        :type Message: str
        """
        self._InstanceId = None
        self._Code = None
        self._Message = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadBalanceProxyNodeRequest(AbstractModel):
    """ReloadBalanceProxyNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param _ProxyAddressId: 代理组地址ID
        :type ProxyAddressId: str
        """
        self._ProxyGroupId = None
        self._ProxyAddressId = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyAddressId = params.get("ProxyAddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadBalanceProxyNodeResponse(AbstractModel):
    """ReloadBalanceProxyNode返回参数结构体

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


class RemoteBackupInfo(AbstractModel):
    """异地备份信息

    """

    def __init__(self):
        r"""
        :param _SubBackupId: 异地备份子任务的ID
        :type SubBackupId: int
        :param _Region: 异地备份所在地域
        :type Region: str
        :param _Status: 备份任务状态。可能的值有 "SUCCESS": 备份成功， "FAILED": 备份失败， "RUNNING": 备份进行中。
        :type Status: str
        :param _StartTime: 异地备份任务的开始时间
        :type StartTime: str
        :param _FinishTime: 异地备份任务的结束时间
        :type FinishTime: str
        :param _Url: 下载地址
        :type Url: str
        """
        self._SubBackupId = None
        self._Region = None
        self._Status = None
        self._StartTime = None
        self._FinishTime = None
        self._Url = None

    @property
    def SubBackupId(self):
        return self._SubBackupId

    @SubBackupId.setter
    def SubBackupId(self, SubBackupId):
        self._SubBackupId = SubBackupId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._SubBackupId = params.get("SubBackupId")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待续费的实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872)。
        :type InstanceId: str
        :param _TimeSpan: 续费时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :type TimeSpan: int
        :param _ModifyPayType: 如果需要将按量计费实例续费为包年包月的实例，该入参的值需要指定为 "PREPAID" 。
        :type ModifyPayType: str
        """
        self._InstanceId = None
        self._TimeSpan = None
        self._ModifyPayType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ModifyPayType(self):
        return self._ModifyPayType

    @ModifyPayType.setter
    def ModifyPayType(self, ModifyPayType):
        self._ModifyPayType = ModifyPayType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TimeSpan = params.get("TimeSpan")
        self._ModifyPayType = params.get("ModifyPayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstanceResponse(AbstractModel):
    """RenewDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单 ID。
        :type DealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class ResetRootAccountRequest(AbstractModel):
    """ResetRootAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRootAccountResponse(AbstractModel):
    """ResetRootAccount返回参数结构体

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


class RestartDBInstancesRequest(AbstractModel):
    """RestartDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstancesResponse(AbstractModel):
    """RestartDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class RoGroup(AbstractModel):
    """只读组参数

    """

    def __init__(self):
        r"""
        :param _RoGroupMode: 只读组模式，可选值为：alone-系统自动分配只读组；allinone-新建只读组；join-使用现有只读组。
        :type RoGroupMode: str
        :param _RoGroupId: 只读组 ID。
        :type RoGroupId: str
        :param _RoGroupName: 只读组名称。
        :type RoGroupName: str
        :param _RoOfflineDelay: 是否启用延迟超限剔除功能，启用该功能后，只读实例与主实例的延迟超过延迟阈值，只读实例将被隔离。可选值：1-启用；0-不启用。
        :type RoOfflineDelay: int
        :param _RoMaxDelayTime: 延迟阈值。
        :type RoMaxDelayTime: int
        :param _MinRoInGroup: 最少实例保留个数，若购买只读实例数量小于设置数量将不做剔除。
        :type MinRoInGroup: int
        :param _WeightMode: 读写权重分配模式，可选值：system-系统自动分配；custom-自定义。
        :type WeightMode: str
        :param _Weight: 该字段已经废弃，无意义。查看只读实例的权重，请查看 RoInstances 字段里的 Weight 值。
        :type Weight: int
        :param _RoInstances: 只读组中的只读实例详情。
        :type RoInstances: list of RoInstanceInfo
        :param _Vip: 只读组的内网 IP。
        :type Vip: str
        :param _Vport: 只读组的内网端口号。
        :type Vport: int
        :param _UniqVpcId: 私有网络 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _RoGroupRegion: 只读组所在的地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoGroupRegion: str
        :param _RoGroupZone: 只读组所在的可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoGroupZone: str
        :param _DelayReplicationTime: 延迟复制时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayReplicationTime: int
        """
        self._RoGroupMode = None
        self._RoGroupId = None
        self._RoGroupName = None
        self._RoOfflineDelay = None
        self._RoMaxDelayTime = None
        self._MinRoInGroup = None
        self._WeightMode = None
        self._Weight = None
        self._RoInstances = None
        self._Vip = None
        self._Vport = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._RoGroupRegion = None
        self._RoGroupZone = None
        self._DelayReplicationTime = None

    @property
    def RoGroupMode(self):
        return self._RoGroupMode

    @RoGroupMode.setter
    def RoGroupMode(self, RoGroupMode):
        self._RoGroupMode = RoGroupMode

    @property
    def RoGroupId(self):
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId

    @property
    def RoGroupName(self):
        return self._RoGroupName

    @RoGroupName.setter
    def RoGroupName(self, RoGroupName):
        self._RoGroupName = RoGroupName

    @property
    def RoOfflineDelay(self):
        return self._RoOfflineDelay

    @RoOfflineDelay.setter
    def RoOfflineDelay(self, RoOfflineDelay):
        self._RoOfflineDelay = RoOfflineDelay

    @property
    def RoMaxDelayTime(self):
        return self._RoMaxDelayTime

    @RoMaxDelayTime.setter
    def RoMaxDelayTime(self, RoMaxDelayTime):
        self._RoMaxDelayTime = RoMaxDelayTime

    @property
    def MinRoInGroup(self):
        return self._MinRoInGroup

    @MinRoInGroup.setter
    def MinRoInGroup(self, MinRoInGroup):
        self._MinRoInGroup = MinRoInGroup

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def RoInstances(self):
        return self._RoInstances

    @RoInstances.setter
    def RoInstances(self, RoInstances):
        self._RoInstances = RoInstances

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def RoGroupRegion(self):
        return self._RoGroupRegion

    @RoGroupRegion.setter
    def RoGroupRegion(self, RoGroupRegion):
        self._RoGroupRegion = RoGroupRegion

    @property
    def RoGroupZone(self):
        return self._RoGroupZone

    @RoGroupZone.setter
    def RoGroupZone(self, RoGroupZone):
        self._RoGroupZone = RoGroupZone

    @property
    def DelayReplicationTime(self):
        return self._DelayReplicationTime

    @DelayReplicationTime.setter
    def DelayReplicationTime(self, DelayReplicationTime):
        self._DelayReplicationTime = DelayReplicationTime


    def _deserialize(self, params):
        self._RoGroupMode = params.get("RoGroupMode")
        self._RoGroupId = params.get("RoGroupId")
        self._RoGroupName = params.get("RoGroupName")
        self._RoOfflineDelay = params.get("RoOfflineDelay")
        self._RoMaxDelayTime = params.get("RoMaxDelayTime")
        self._MinRoInGroup = params.get("MinRoInGroup")
        self._WeightMode = params.get("WeightMode")
        self._Weight = params.get("Weight")
        if params.get("RoInstances") is not None:
            self._RoInstances = []
            for item in params.get("RoInstances"):
                obj = RoInstanceInfo()
                obj._deserialize(item)
                self._RoInstances.append(obj)
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._RoGroupRegion = params.get("RoGroupRegion")
        self._RoGroupZone = params.get("RoGroupZone")
        self._DelayReplicationTime = params.get("DelayReplicationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoGroupAttr(AbstractModel):
    """RO 组的配置信息

    """

    def __init__(self):
        r"""
        :param _RoGroupName: RO 组名称。
        :type RoGroupName: str
        :param _RoMaxDelayTime: RO 实例最大延迟阈值。单位为秒，最小值为 1。注意，RO 组必须设置了开启实例延迟剔除策略，该值才有效。
        :type RoMaxDelayTime: int
        :param _RoOfflineDelay: 是否开启实例延迟剔除。支持的值包括：1 - 开启；0 - 不开启。注意，若设置开启实例延迟剔除，则必须设置延迟阈值（RoMaxDelayTime）参数。
        :type RoOfflineDelay: int
        :param _MinRoInGroup: 最少保留实例数。可设置为小于或等于该 RO 组下 RO 实例个数的任意值。注意，若设置值大于 RO 实例数量将不做剔除；若设置为 0，所有实例延迟超限都会被剔除。
        :type MinRoInGroup: int
        :param _WeightMode: 权重模式。支持值包括："system" - 系统自动分配； "custom" - 用户自定义设置。注意，若设置 "custom" 模式，则必须设置 RO 实例权重配置（RoWeightValues）参数。
        :type WeightMode: str
        :param _ReplicationDelayTime: 延迟复制时间。
        :type ReplicationDelayTime: int
        """
        self._RoGroupName = None
        self._RoMaxDelayTime = None
        self._RoOfflineDelay = None
        self._MinRoInGroup = None
        self._WeightMode = None
        self._ReplicationDelayTime = None

    @property
    def RoGroupName(self):
        return self._RoGroupName

    @RoGroupName.setter
    def RoGroupName(self, RoGroupName):
        self._RoGroupName = RoGroupName

    @property
    def RoMaxDelayTime(self):
        return self._RoMaxDelayTime

    @RoMaxDelayTime.setter
    def RoMaxDelayTime(self, RoMaxDelayTime):
        self._RoMaxDelayTime = RoMaxDelayTime

    @property
    def RoOfflineDelay(self):
        return self._RoOfflineDelay

    @RoOfflineDelay.setter
    def RoOfflineDelay(self, RoOfflineDelay):
        self._RoOfflineDelay = RoOfflineDelay

    @property
    def MinRoInGroup(self):
        return self._MinRoInGroup

    @MinRoInGroup.setter
    def MinRoInGroup(self, MinRoInGroup):
        self._MinRoInGroup = MinRoInGroup

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def ReplicationDelayTime(self):
        return self._ReplicationDelayTime

    @ReplicationDelayTime.setter
    def ReplicationDelayTime(self, ReplicationDelayTime):
        self._ReplicationDelayTime = ReplicationDelayTime


    def _deserialize(self, params):
        self._RoGroupName = params.get("RoGroupName")
        self._RoMaxDelayTime = params.get("RoMaxDelayTime")
        self._RoOfflineDelay = params.get("RoOfflineDelay")
        self._MinRoInGroup = params.get("MinRoInGroup")
        self._WeightMode = params.get("WeightMode")
        self._ReplicationDelayTime = params.get("ReplicationDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoInstanceInfo(AbstractModel):
    """RO实例的详细信息

    """

    def __init__(self):
        r"""
        :param _MasterInstanceId: RO组对应的主实例的ID
        :type MasterInstanceId: str
        :param _RoStatus: RO实例在RO组内的状态，可能的值：online-在线，offline-下线
        :type RoStatus: str
        :param _OfflineTime: RO实例在RO组内上一次下线的时间
        :type OfflineTime: str
        :param _Weight: RO实例在RO组内的权重
        :type Weight: int
        :param _Region: RO实例所在区域名称，如ap-shanghai
        :type Region: str
        :param _Zone: RO可用区的正式名称，如ap-shanghai-1
        :type Zone: str
        :param _InstanceId: RO实例ID，格式如：cdbro-c1nl9rpv
        :type InstanceId: str
        :param _Status: RO实例状态，可能返回值：0-创建中，1-运行中，3-异地RO（仅在使用DescribeDBInstances查询主实例信息时，返回值中异地RO的状态恒等于3，其他场景下无此值），4-删除中
        :type Status: int
        :param _InstanceType: 实例类型，可能返回值：1-主实例，2-灾备实例，3-只读实例
        :type InstanceType: int
        :param _InstanceName: RO实例名称
        :type InstanceName: str
        :param _HourFeeStatus: 按量计费状态，可能的取值：1-正常，2-欠费
        :type HourFeeStatus: int
        :param _TaskStatus: RO实例任务状态，可能返回值：<br>0-没有任务<br>1-升级中<br>2-数据导入中<br>3-开放Slave中<br>4-外网访问开通中<br>5-批量操作执行中<br>6-回档中<br>7-外网访问关闭中<br>8-密码修改中<br>9-实例名修改中<br>10-重启中<br>12-自建迁移中<br>13-删除库表中<br>14-灾备实例创建同步中
        :type TaskStatus: int
        :param _Memory: RO实例内存大小，单位：MB
        :type Memory: int
        :param _Volume: RO实例硬盘大小，单位：GB
        :type Volume: int
        :param _Qps: 每次查询数量
        :type Qps: int
        :param _Vip: RO实例的内网IP地址
        :type Vip: str
        :param _Vport: RO实例访问端口
        :type Vport: int
        :param _VpcId: RO实例所在私有网络ID
        :type VpcId: int
        :param _SubnetId: RO实例所在私有网络子网ID
        :type SubnetId: int
        :param _DeviceType: RO实例规格描述，目前可取值 CUSTOM
        :type DeviceType: str
        :param _EngineVersion: RO实例数据库引擎版本，可能返回值：5.1、5.5、5.6、5.7、8.0
        :type EngineVersion: str
        :param _DeadlineTime: RO实例到期时间，时间格式：yyyy-mm-dd hh:mm:ss，如实例为按量计费模式，则此字段值为0000-00-00 00:00:00
        :type DeadlineTime: str
        :param _PayType: RO实例计费类型，可能返回值：0-包年包月，1-按量计费，2-后付费月结
        :type PayType: int
        """
        self._MasterInstanceId = None
        self._RoStatus = None
        self._OfflineTime = None
        self._Weight = None
        self._Region = None
        self._Zone = None
        self._InstanceId = None
        self._Status = None
        self._InstanceType = None
        self._InstanceName = None
        self._HourFeeStatus = None
        self._TaskStatus = None
        self._Memory = None
        self._Volume = None
        self._Qps = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._DeviceType = None
        self._EngineVersion = None
        self._DeadlineTime = None
        self._PayType = None

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def RoStatus(self):
        return self._RoStatus

    @RoStatus.setter
    def RoStatus(self, RoStatus):
        self._RoStatus = RoStatus

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def HourFeeStatus(self):
        return self._HourFeeStatus

    @HourFeeStatus.setter
    def HourFeeStatus(self, HourFeeStatus):
        self._HourFeeStatus = HourFeeStatus

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType


    def _deserialize(self, params):
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._RoStatus = params.get("RoStatus")
        self._OfflineTime = params.get("OfflineTime")
        self._Weight = params.get("Weight")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._InstanceType = params.get("InstanceType")
        self._InstanceName = params.get("InstanceName")
        self._HourFeeStatus = params.get("HourFeeStatus")
        self._TaskStatus = params.get("TaskStatus")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._Qps = params.get("Qps")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DeviceType = params.get("DeviceType")
        self._EngineVersion = params.get("EngineVersion")
        self._DeadlineTime = params.get("DeadlineTime")
        self._PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoVipInfo(AbstractModel):
    """只读vip信息

    """

    def __init__(self):
        r"""
        :param _RoVipStatus: 只读vip状态
        :type RoVipStatus: int
        :param _RoSubnetId: 只读vip的子网
        :type RoSubnetId: int
        :param _RoVpcId: 只读vip的私有网络
        :type RoVpcId: int
        :param _RoVport: 只读vip的端口号
        :type RoVport: int
        :param _RoVip: 只读vip
        :type RoVip: str
        """
        self._RoVipStatus = None
        self._RoSubnetId = None
        self._RoVpcId = None
        self._RoVport = None
        self._RoVip = None

    @property
    def RoVipStatus(self):
        return self._RoVipStatus

    @RoVipStatus.setter
    def RoVipStatus(self, RoVipStatus):
        self._RoVipStatus = RoVipStatus

    @property
    def RoSubnetId(self):
        return self._RoSubnetId

    @RoSubnetId.setter
    def RoSubnetId(self, RoSubnetId):
        self._RoSubnetId = RoSubnetId

    @property
    def RoVpcId(self):
        return self._RoVpcId

    @RoVpcId.setter
    def RoVpcId(self, RoVpcId):
        self._RoVpcId = RoVpcId

    @property
    def RoVport(self):
        return self._RoVport

    @RoVport.setter
    def RoVport(self, RoVport):
        self._RoVport = RoVport

    @property
    def RoVip(self):
        return self._RoVip

    @RoVip.setter
    def RoVip(self, RoVip):
        self._RoVip = RoVip


    def _deserialize(self, params):
        self._RoVipStatus = params.get("RoVipStatus")
        self._RoSubnetId = params.get("RoSubnetId")
        self._RoVpcId = params.get("RoVpcId")
        self._RoVport = params.get("RoVport")
        self._RoVip = params.get("RoVip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoWeightValue(AbstractModel):
    """RO 实例的权重值

    """

    def __init__(self):
        r"""
        :param _InstanceId: RO 实例 ID。
        :type InstanceId: str
        :param _Weight: 权重值。取值范围为 [0, 100]。
        :type Weight: int
        """
        self._InstanceId = None
        self._Weight = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackDBName(AbstractModel):
    """用于回档的数据库名

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 回档前的原数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param _NewDatabaseName: 回档后的新数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type NewDatabaseName: str
        """
        self._DatabaseName = None
        self._NewDatabaseName = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def NewDatabaseName(self):
        return self._NewDatabaseName

    @NewDatabaseName.setter
    def NewDatabaseName(self, NewDatabaseName):
        self._NewDatabaseName = NewDatabaseName


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._NewDatabaseName = params.get("NewDatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstancesInfo(AbstractModel):
    """用于回档的实例详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 云数据库实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Strategy: 回档策略。可选值为：table、db、full；默认值为full。table - 极速回档模式，仅导入所选中表级别的备份和binlog，如有跨表操作，且关联表未被同时选中，将会导致回档失败，该模式下参数Databases必须为空；db - 快速模式，仅导入所选中库级别的备份和binlog，如有跨库操作，且关联库未被同时选中，将会导致回档失败；full - 普通回档模式，将导入整个实例的备份和binlog，速度较慢。
        :type Strategy: str
        :param _RollbackTime: 数据库回档时间，时间格式为：yyyy-mm-dd hh:mm:ss
        :type RollbackTime: str
        :param _Databases: 待回档的数据库信息，表示整库回档
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of RollbackDBName
        :param _Tables: 待回档的数据库表信息，表示按表回档
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of RollbackTables
        """
        self._InstanceId = None
        self._Strategy = None
        self._RollbackTime = None
        self._Databases = None
        self._Tables = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def RollbackTime(self):
        return self._RollbackTime

    @RollbackTime.setter
    def RollbackTime(self, RollbackTime):
        self._RollbackTime = RollbackTime

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Strategy = params.get("Strategy")
        self._RollbackTime = params.get("RollbackTime")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = RollbackDBName()
                obj._deserialize(item)
                self._Databases.append(obj)
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = RollbackTables()
                obj._deserialize(item)
                self._Tables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTableName(AbstractModel):
    """用于回档的数据库表名

    """

    def __init__(self):
        r"""
        :param _TableName: 回档前的原数据库表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param _NewTableName: 回档后的新数据库表名
注意：此字段可能返回 null，表示取不到有效值。
        :type NewTableName: str
        """
        self._TableName = None
        self._NewTableName = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._NewTableName = params.get("NewTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTables(AbstractModel):
    """用于回档的数据库表详情

    """

    def __init__(self):
        r"""
        :param _Database: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Table: 数据库表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: list of RollbackTableName
        """
        self._Database = None
        self._Table = None

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


    def _deserialize(self, params):
        self._Database = params.get("Database")
        if params.get("Table") is not None:
            self._Table = []
            for item in params.get("Table"):
                obj = RollbackTableName()
                obj._deserialize(item)
                self._Table.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTask(AbstractModel):
    """回档任务详情

    """

    def __init__(self):
        r"""
        :param _Info: 任务执行信息描述。
        :type Info: str
        :param _Status: 任务执行结果。可能的取值：INITIAL - 初始化，RUNNING - 运行中，SUCCESS - 执行成功，FAILED - 执行失败，KILLED - 已终止，REMOVED - 已删除，PAUSED - 终止中。
        :type Status: str
        :param _Progress: 任务执行进度。取值范围为[0, 100]。
        :type Progress: int
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _EndTime: 任务结束时间。
        :type EndTime: str
        :param _Detail: 回档任务详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of RollbackInstancesInfo
        """
        self._Info = None
        self._Status = None
        self._Progress = None
        self._StartTime = None
        self._EndTime = None
        self._Detail = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Info = params.get("Info")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTimeRange(AbstractModel):
    """可回档时间范围

    """

    def __init__(self):
        r"""
        :param _Begin: 实例可回档开始时间，时间格式：2016-10-29 01:06:04
        :type Begin: str
        :param _End: 实例可回档结束时间，时间格式：2016-11-02 11:44:47
        :type End: str
        """
        self._Begin = None
        self._End = None

    @property
    def Begin(self):
        return self._Begin

    @Begin.setter
    def Begin(self, Begin):
        self._Begin = Begin

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Begin = params.get("Begin")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """权重分配规则

    """

    def __init__(self):
        r"""
        :param _LessThan: 划分上限
注意：此字段可能返回 null，表示取不到有效值。
        :type LessThan: int
        :param _Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        """
        self._LessThan = None
        self._Weight = None

    @property
    def LessThan(self):
        return self._LessThan

    @LessThan.setter
    def LessThan(self, LessThan):
        self._LessThan = LessThan

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._LessThan = params.get("LessThan")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleFilters(AbstractModel):
    """审计规则的规则过滤条件

    """

    def __init__(self):
        r"""
        :param _Type: 审计规则过滤条件的参数名称。可选值：host – 客户端 IP；user – 数据库账户；dbName – 数据库名称；sqlType-SQL类型；sql-sql语句；affectRows -影响行数；sentRows-返回行数；checkRows-扫描行数；execTime-执行时间。
        :type Type: str
        :param _Compare: 审计规则过滤条件的匹配类型。可选值：INC – 包含；EXC – 不包含；EQS – 等于；NEQ – 不等于；REG-正则；GT-大于；LT-小于。
        :type Compare: str
        :param _Value: 审计规则过滤条件的匹配值。sqlType条件的Value需在以下选择"alter", "changeuser", "create", "delete", "drop", "execute", "insert", "login", "logout", "other", "replace", "select", "set", "update"。
        :type Value: list of str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _Inbound: 入站规则
        :type Inbound: list of Inbound
        :param _Outbound: 出站规则
        :type Outbound: list of Outbound
        :param _SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._Inbound = None
        self._Outbound = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Inbound(self):
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveConfig(AbstractModel):
    """从库的配置信息

    """

    def __init__(self):
        r"""
        :param _ReplicationMode: 从库复制方式，可能的返回值：aysnc-异步，semisync-半同步
        :type ReplicationMode: str
        :param _Zone: 从库可用区的正式名称，如ap-shanghai-1
        :type Zone: str
        """
        self._ReplicationMode = None
        self._Zone = None

    @property
    def ReplicationMode(self):
        return self._ReplicationMode

    @ReplicationMode.setter
    def ReplicationMode(self, ReplicationMode):
        self._ReplicationMode = ReplicationMode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._ReplicationMode = params.get("ReplicationMode")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveInfo(AbstractModel):
    """备机信息

    """

    def __init__(self):
        r"""
        :param _First: 第一备机信息
        :type First: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`
        :param _Second: 第二备机信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Second: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`
        """
        self._First = None
        self._Second = None

    @property
    def First(self):
        return self._First

    @First.setter
    def First(self, First):
        self._First = First

    @property
    def Second(self):
        return self._Second

    @Second.setter
    def Second(self, Second):
        self._Second = Second


    def _deserialize(self, params):
        if params.get("First") is not None:
            self._First = SlaveInstanceInfo()
            self._First._deserialize(params.get("First"))
        if params.get("Second") is not None:
            self._Second = SlaveInstanceInfo()
            self._Second._deserialize(params.get("Second"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveInstanceInfo(AbstractModel):
    """备机信息

    """

    def __init__(self):
        r"""
        :param _Vport: 端口号
        :type Vport: int
        :param _Region: 地域信息
        :type Region: str
        :param _Vip: 虚拟 IP 信息
        :type Vip: str
        :param _Zone: 可用区信息
        :type Zone: str
        """
        self._Vport = None
        self._Region = None
        self._Vip = None
        self._Zone = None

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Vport = params.get("Vport")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogInfo(AbstractModel):
    """慢查询日志详情

    """

    def __init__(self):
        r"""
        :param _Name: 备份文件名
        :type Name: str
        :param _Size: 备份文件大小，单位：Byte
        :type Size: int
        :param _Date: 备份快照时间，时间格式：2016-03-17 02:10:37
        :type Date: str
        :param _IntranetUrl: 内网下载地址
        :type IntranetUrl: str
        :param _InternetUrl: 外网下载地址
        :type InternetUrl: str
        :param _Type: 日志具体类型，可能的值：slowlog - 慢日志
        :type Type: str
        """
        self._Name = None
        self._Size = None
        self._Date = None
        self._IntranetUrl = None
        self._InternetUrl = None
        self._Type = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def IntranetUrl(self):
        return self._IntranetUrl

    @IntranetUrl.setter
    def IntranetUrl(self, IntranetUrl):
        self._IntranetUrl = IntranetUrl

    @property
    def InternetUrl(self):
        return self._InternetUrl

    @InternetUrl.setter
    def InternetUrl(self, InternetUrl):
        self._InternetUrl = InternetUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Date = params.get("Date")
        self._IntranetUrl = params.get("IntranetUrl")
        self._InternetUrl = params.get("InternetUrl")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogItem(AbstractModel):
    """结构化的慢日志详情

    """

    def __init__(self):
        r"""
        :param _Timestamp: Sql的执行时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param _QueryTime: Sql的执行时长（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryTime: float
        :param _SqlText: Sql语句。
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlText: str
        :param _UserHost: 客户端地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserHost: str
        :param _UserName: 用户名。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Database: 数据库名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _LockTime: 锁时长（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type LockTime: float
        :param _RowsExamined: 扫描行数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RowsExamined: int
        :param _RowsSent: 结果集行数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RowsSent: int
        :param _SqlTemplate: Sql模板。
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlTemplate: str
        :param _Md5: Sql语句的md5。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        """
        self._Timestamp = None
        self._QueryTime = None
        self._SqlText = None
        self._UserHost = None
        self._UserName = None
        self._Database = None
        self._LockTime = None
        self._RowsExamined = None
        self._RowsSent = None
        self._SqlTemplate = None
        self._Md5 = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def UserHost(self):
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def LockTime(self):
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def RowsExamined(self):
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsSent(self):
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def SqlTemplate(self):
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._QueryTime = params.get("QueryTime")
        self._SqlText = params.get("SqlText")
        self._UserHost = params.get("UserHost")
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._LockTime = params.get("LockTime")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsSent = params.get("RowsSent")
        self._SqlTemplate = params.get("SqlTemplate")
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SqlFileInfo(AbstractModel):
    """sql文件信息

    """

    def __init__(self):
        r"""
        :param _UploadTime: 上传时间
        :type UploadTime: str
        :param _UploadInfo: 上传进度
        :type UploadInfo: :class:`tencentcloud.cdb.v20170320.models.UploadInfo`
        :param _FileName: 文件名
        :type FileName: str
        :param _FileSize: 文件大小，单位为Bytes
        :type FileSize: int
        :param _IsUploadFinished: 上传是否完成标志，可选值：0 - 未完成，1 - 已完成
        :type IsUploadFinished: int
        :param _FileId: 文件ID
        :type FileId: str
        """
        self._UploadTime = None
        self._UploadInfo = None
        self._FileName = None
        self._FileSize = None
        self._IsUploadFinished = None
        self._FileId = None

    @property
    def UploadTime(self):
        return self._UploadTime

    @UploadTime.setter
    def UploadTime(self, UploadTime):
        self._UploadTime = UploadTime

    @property
    def UploadInfo(self):
        return self._UploadInfo

    @UploadInfo.setter
    def UploadInfo(self, UploadInfo):
        self._UploadInfo = UploadInfo

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def IsUploadFinished(self):
        return self._IsUploadFinished

    @IsUploadFinished.setter
    def IsUploadFinished(self, IsUploadFinished):
        self._IsUploadFinished = IsUploadFinished

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._UploadTime = params.get("UploadTime")
        if params.get("UploadInfo") is not None:
            self._UploadInfo = UploadInfo()
            self._UploadInfo._deserialize(params.get("UploadInfo"))
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._IsUploadFinished = params.get("IsUploadFinished")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBatchRollbackRequest(AbstractModel):
    """StartBatchRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 用于回档的实例详情信息。
        :type Instances: list of RollbackInstancesInfo
        """
        self._Instances = None

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBatchRollbackResponse(AbstractModel):
    """StartBatchRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class StartReplicationRequest(AbstractModel):
    """StartReplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。仅支持只读实例。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartReplicationResponse(AbstractModel):
    """StartReplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class StopDBImportJobRequest(AbstractModel):
    """StopDBImportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID。
        :type AsyncRequestId: str
        """
        self._AsyncRequestId = None

    @property
    def AsyncRequestId(self):
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
        


class StopDBImportJobResponse(AbstractModel):
    """StopDBImportJob返回参数结构体

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


class StopReplicationRequest(AbstractModel):
    """StopReplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。仅支持只读实例。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopReplicationResponse(AbstractModel):
    """StopReplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class StopRollbackRequest(AbstractModel):
    """StopRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 撤销回档任务对应的实例Id。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRollbackResponse(AbstractModel):
    """StopRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 执行请求的异步任务ID
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class SwitchCDBProxyRequest(AbstractModel):
    """SwitchCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ProxyGroupId: 数据库代理ID
        :type ProxyGroupId: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchCDBProxyResponse(AbstractModel):
    """SwitchCDBProxy返回参数结构体

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


class SwitchDBInstanceMasterSlaveRequest(AbstractModel):
    """SwitchDBInstanceMasterSlave请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _DstSlave: 目标从实例。可选值："first" - 第一备机；"second" - 第二备机。默认值为 "first"，仅多可用区实例支持设置为 "second"。
        :type DstSlave: str
        :param _ForceSwitch: 是否强制切换。默认为 False。注意，若设置强制切换为 True，实例存在丢失数据的风险，请谨慎使用。
        :type ForceSwitch: bool
        :param _WaitSwitch: 是否时间窗内切换。默认为 False，即不在时间窗内切换。注意，如果设置了 ForceSwitch 参数为 True，则该参数不生效。
        :type WaitSwitch: bool
        """
        self._InstanceId = None
        self._DstSlave = None
        self._ForceSwitch = None
        self._WaitSwitch = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DstSlave(self):
        return self._DstSlave

    @DstSlave.setter
    def DstSlave(self, DstSlave):
        self._DstSlave = DstSlave

    @property
    def ForceSwitch(self):
        return self._ForceSwitch

    @ForceSwitch.setter
    def ForceSwitch(self, ForceSwitch):
        self._ForceSwitch = ForceSwitch

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DstSlave = params.get("DstSlave")
        self._ForceSwitch = params.get("ForceSwitch")
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceMasterSlaveResponse(AbstractModel):
    """SwitchDBInstanceMasterSlave返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务 ID。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class SwitchDrInstanceToMasterRequest(AbstractModel):
    """SwitchDrInstanceToMaster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 灾备实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDrInstanceToMasterResponse(AbstractModel):
    """SwitchDrInstanceToMaster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class SwitchForUpgradeRequest(AbstractModel):
    """SwitchForUpgrade请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchForUpgradeResponse(AbstractModel):
    """SwitchForUpgrade返回参数结构体

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


class TablePrivilege(AbstractModel):
    """数据库表权限

    """

    def __init__(self):
        r"""
        :param _Database: 数据库名
        :type Database: str
        :param _Table: 数据库表名
        :type Table: str
        :param _Privileges: 权限信息
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Privileges = None

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
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签结构

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
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
        


class TagInfo(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: list of str
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
        


class TagInfoItem(AbstractModel):
    """标签信息

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
        


class TagInfoUnit(AbstractModel):
    """tag信息单元

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
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
        


class TagsInfoOfInstance(AbstractModel):
    """实例的标签信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Tags: 标签信息
        :type Tags: list of TagInfoUnit
        """
        self._InstanceId = None
        self._Tags = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """实例任务详情

    """

    def __init__(self):
        r"""
        :param _Code: 错误码。
        :type Code: int
        :param _Message: 错误信息。
        :type Message: str
        :param _JobId: 实例任务 ID。
        :type JobId: int
        :param _Progress: 实例任务进度。
        :type Progress: int
        :param _TaskStatus: 实例任务状态，可能的值包括：
"UNDEFINED" - 未定义；
"INITIAL" - 初始化；
"RUNNING" - 运行中；
"SUCCEED" - 执行成功；
"FAILED" - 执行失败；
"KILLED" - 已终止；
"REMOVED" - 已删除；
"PAUSED" - 已暂停。
"WAITING" - 等待中（可撤销）
        :type TaskStatus: str
        :param _TaskType: 实例任务类型，可能的值包括：
"ROLLBACK" - 数据库回档；
"SQL OPERATION" - SQL操作；
"IMPORT DATA" - 数据导入；
"MODIFY PARAM" - 参数设置；
"INITIAL" - 初始化云数据库实例；
"REBOOT" - 重启云数据库实例；
"OPEN GTID" - 开启云数据库实例GTID；
"UPGRADE RO" - 只读实例升级；
"BATCH ROLLBACK" - 数据库批量回档；
"UPGRADE MASTER" - 主实例升级；
"DROP TABLES" - 删除云数据库库表；
"SWITCH DR TO MASTER" - 灾备实例提升为主。
        :type TaskType: str
        :param _StartTime: 实例任务开始时间。
        :type StartTime: str
        :param _EndTime: 实例任务结束时间。
        :type EndTime: str
        :param _InstanceIds: 任务关联的实例 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param _AsyncRequestId: 异步任务的请求 ID。
        :type AsyncRequestId: str
        """
        self._Code = None
        self._Message = None
        self._JobId = None
        self._Progress = None
        self._TaskStatus = None
        self._TaskType = None
        self._StartTime = None
        self._EndTime = None
        self._InstanceIds = None
        self._AsyncRequestId = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._JobId = params.get("JobId")
        self._Progress = params.get("Progress")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskType = params.get("TaskType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceIds = params.get("InstanceIds")
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeCDBProxyVersionRequest(AbstractModel):
    """UpgradeCDBProxyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ProxyGroupId: 数据库代理ID
        :type ProxyGroupId: str
        :param _SrcProxyVersion: 数据库代理当前版本
        :type SrcProxyVersion: str
        :param _DstProxyVersion: 数据库代理升级版本
        :type DstProxyVersion: str
        :param _UpgradeTime: 升级时间 ：nowTime（升级完成时）timeWindow（实例维护时间）
        :type UpgradeTime: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._SrcProxyVersion = None
        self._DstProxyVersion = None
        self._UpgradeTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def SrcProxyVersion(self):
        return self._SrcProxyVersion

    @SrcProxyVersion.setter
    def SrcProxyVersion(self, SrcProxyVersion):
        self._SrcProxyVersion = SrcProxyVersion

    @property
    def DstProxyVersion(self):
        return self._DstProxyVersion

    @DstProxyVersion.setter
    def DstProxyVersion(self, DstProxyVersion):
        self._DstProxyVersion = DstProxyVersion

    @property
    def UpgradeTime(self):
        return self._UpgradeTime

    @UpgradeTime.setter
    def UpgradeTime(self, UpgradeTime):
        self._UpgradeTime = UpgradeTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._SrcProxyVersion = params.get("SrcProxyVersion")
        self._DstProxyVersion = params.get("DstProxyVersion")
        self._UpgradeTime = params.get("UpgradeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeCDBProxyVersionResponse(AbstractModel):
    """UpgradeCDBProxyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步处理ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceEngineVersionRequest(AbstractModel):
    """UpgradeDBInstanceEngineVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param _EngineVersion: 主实例数据库引擎版本，支持值包括：5.6 和 5.7。
        :type EngineVersion: str
        :param _WaitSwitch: 切换访问新实例的方式，默认为 0。支持值包括：0 - 立刻切换，1 - 时间窗切换；当该值为 1 时，升级过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口 [切换访问新实例](https://cloud.tencent.com/document/product/236/15864) 触发该流程。
        :type WaitSwitch: int
        :param _UpgradeSubversion: 是否是内核子版本升级，支持的值：1 - 升级内核子版本；0 - 升级数据库引擎版本。
        :type UpgradeSubversion: int
        :param _MaxDelayTime: 延迟阈值。取值范围1~10
        :type MaxDelayTime: int
        """
        self._InstanceId = None
        self._EngineVersion = None
        self._WaitSwitch = None
        self._UpgradeSubversion = None
        self._MaxDelayTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch

    @property
    def UpgradeSubversion(self):
        return self._UpgradeSubversion

    @UpgradeSubversion.setter
    def UpgradeSubversion(self, UpgradeSubversion):
        self._UpgradeSubversion = UpgradeSubversion

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EngineVersion = params.get("EngineVersion")
        self._WaitSwitch = params.get("WaitSwitch")
        self._UpgradeSubversion = params.get("UpgradeSubversion")
        self._MaxDelayTime = params.get("MaxDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceEngineVersionResponse(AbstractModel):
    """UpgradeDBInstanceEngineVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务 ID，可使用 [查询异步任务的执行结果](https://cloud.tencent.com/document/api/236/20410) 获取其执行情况。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param _Memory: 升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的内存规格。
        :type Memory: int
        :param _Volume: 升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的硬盘范围。
        :type Volume: int
        :param _ProtectMode: 数据复制方式，支持值包括：0 - 异步复制，1 - 半同步复制，2 - 强同步复制，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。
        :type ProtectMode: int
        :param _DeployMode: 部署模式，默认为 0，支持值包括：0 - 单可用区部署，1 - 多可用区部署，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。
        :type DeployMode: int
        :param _SlaveZone: 备库1的可用区信息，默认和实例的 Zone 参数一致，升级主实例为多可用区部署时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。可通过 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口查询支持的可用区。
        :type SlaveZone: str
        :param _EngineVersion: 主实例数据库引擎版本，支持值包括：5.5、5.6 和 5.7。
        :type EngineVersion: str
        :param _WaitSwitch: 切换访问新实例的方式，默认为 0。支持值包括：0 - 立刻切换，1 - 时间窗切换；当该值为 1 时，升级过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口 [切换访问新实例](https://cloud.tencent.com/document/product/236/15864) 触发该流程。
        :type WaitSwitch: int
        :param _BackupZone: 备库 2 的可用区信息，默认为空，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。
        :type BackupZone: str
        :param _InstanceRole: 实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。
        :type InstanceRole: str
        :param _DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。
        :type DeviceType: str
        :param _Cpu: 升级后的实例cpu核数，如果不传将根据 Memory 指定的内存值自动填充最小允许规格的cpu值。
        :type Cpu: int
        :param _FastUpgrade: 是否极速变配。0-普通升级，1-极速变配，2 极速优先。选择极速变配会根据资源状况校验是否可以进行极速变配，满足条件则进行极速变配，不满足条件会返回报错信息。
        :type FastUpgrade: int
        :param _MaxDelayTime: 延迟阈值。取值范围1~10，默认值为10。
        :type MaxDelayTime: int
        :param _CrossCluster: 是否跨区迁移。0-普通迁移，1-跨区迁移，默认值为0。该值为1时支持变更实例主节点可用区。
        :type CrossCluster: int
        :param _ZoneId: 主节点可用区，该值仅在跨区迁移时生效。仅支持同地域下的可用区进行迁移。
        :type ZoneId: str
        :param _RoTransType: 针对跨集群搬迁场景，选择同可用区RO的处理逻辑。together-同可用区RO跟随主实例迁移至目标可用区（默认选项），severally-同可用区RO保持原部署模式、不迁移至目标可用区。
        :type RoTransType: str
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._ProtectMode = None
        self._DeployMode = None
        self._SlaveZone = None
        self._EngineVersion = None
        self._WaitSwitch = None
        self._BackupZone = None
        self._InstanceRole = None
        self._DeviceType = None
        self._Cpu = None
        self._FastUpgrade = None
        self._MaxDelayTime = None
        self._CrossCluster = None
        self._ZoneId = None
        self._RoTransType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def FastUpgrade(self):
        return self._FastUpgrade

    @FastUpgrade.setter
    def FastUpgrade(self, FastUpgrade):
        self._FastUpgrade = FastUpgrade

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime

    @property
    def CrossCluster(self):
        return self._CrossCluster

    @CrossCluster.setter
    def CrossCluster(self, CrossCluster):
        self._CrossCluster = CrossCluster

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoTransType(self):
        return self._RoTransType

    @RoTransType.setter
    def RoTransType(self, RoTransType):
        self._RoTransType = RoTransType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._SlaveZone = params.get("SlaveZone")
        self._EngineVersion = params.get("EngineVersion")
        self._WaitSwitch = params.get("WaitSwitch")
        self._BackupZone = params.get("BackupZone")
        self._InstanceRole = params.get("InstanceRole")
        self._DeviceType = params.get("DeviceType")
        self._Cpu = params.get("Cpu")
        self._FastUpgrade = params.get("FastUpgrade")
        self._MaxDelayTime = params.get("MaxDelayTime")
        self._CrossCluster = params.get("CrossCluster")
        self._ZoneId = params.get("ZoneId")
        self._RoTransType = params.get("RoTransType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealIds: 订单 ID。
        :type DealIds: list of str
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealIds = None
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class UploadInfo(AbstractModel):
    """文件上传描述

    """

    def __init__(self):
        r"""
        :param _AllSliceNum: 文件所有分片数
        :type AllSliceNum: int
        :param _CompleteNum: 已完成分片数
        :type CompleteNum: int
        """
        self._AllSliceNum = None
        self._CompleteNum = None

    @property
    def AllSliceNum(self):
        return self._AllSliceNum

    @AllSliceNum.setter
    def AllSliceNum(self, AllSliceNum):
        self._AllSliceNum = AllSliceNum

    @property
    def CompleteNum(self):
        return self._CompleteNum

    @CompleteNum.setter
    def CompleteNum(self, CompleteNum):
        self._CompleteNum = CompleteNum


    def _deserialize(self, params):
        self._AllSliceNum = params.get("AllSliceNum")
        self._CompleteNum = params.get("CompleteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyRootAccountRequest(AbstractModel):
    """VerifyRootAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param _Password: 实例 ROOT 账号的密码。
        :type Password: str
        """
        self._InstanceId = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyRootAccountResponse(AbstractModel):
    """VerifyRootAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ZoneConf(AbstractModel):
    """多可用区信息

    """

    def __init__(self):
        r"""
        :param _DeployMode: 可用区部署方式，可能的值为：0-单可用区；1-多可用区
        :type DeployMode: list of int
        :param _MasterZone: 主实例所在的可用区
        :type MasterZone: list of str
        :param _SlaveZone: 实例为多可用区部署时，备库1所在的可用区
        :type SlaveZone: list of str
        :param _BackupZone: 实例为多可用区部署时，备库2所在的可用区
        :type BackupZone: list of str
        """
        self._DeployMode = None
        self._MasterZone = None
        self._SlaveZone = None
        self._BackupZone = None

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone


    def _deserialize(self, params):
        self._DeployMode = params.get("DeployMode")
        self._MasterZone = params.get("MasterZone")
        self._SlaveZone = params.get("SlaveZone")
        self._BackupZone = params.get("BackupZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        