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


class AlarmConditionFilter(AbstractModel):
    """策略过滤条件

    """

    def __init__(self):
        r"""
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Expression: 表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type Expression: str
        :param _Dimensions: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: str
        """
        self._Type = None
        self._Expression = None
        self._Dimensions = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Expression(self):
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Expression = params.get("Expression")
        self._Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmEvent(AbstractModel):
    """告警事件

    """

    def __init__(self):
        r"""
        :param _EventName: 事件名
        :type EventName: str
        :param _Description: 展示的事件名
        :type Description: str
        :param _Namespace: 告警策略类型
        :type Namespace: str
        """
        self._EventName = None
        self._Description = None
        self._Namespace = None

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        self._Description = params.get("Description")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmGroupByItem(AbstractModel):
    """聚合条件

    """

    def __init__(self):
        r"""
        :param _Id: Item Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Id = None
        self._Name = None

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


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHierarchicalNotice(AbstractModel):
    """通知模板ID及通知等级列表，["Remind","Serious"]表示该通知模板仅接收提醒和严重类别的告警

    """

    def __init__(self):
        r"""
        :param _NoticeId: 通知模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeId: str
        :param _Classification: 通知等级列表，["Remind","Serious"]表示该通知模板仅接收提醒和严重类别的告警
注意：此字段可能返回 null，表示取不到有效值。
        :type Classification: list of str
        :param _PolicyId: 模板对应的策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: str
        """
        self._NoticeId = None
        self._Classification = None
        self._PolicyId = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def Classification(self):
        return self._Classification

    @Classification.setter
    def Classification(self, Classification):
        self._Classification = Classification

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._Classification = params.get("Classification")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHierarchicalValue(AbstractModel):
    """告警分级阈值配置

    """

    def __init__(self):
        r"""
        :param _Remind: 提醒等级阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type Remind: str
        :param _Warn: 警告等级阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type Warn: str
        :param _Serious: 严重等级阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type Serious: str
        """
        self._Remind = None
        self._Warn = None
        self._Serious = None

    @property
    def Remind(self):
        return self._Remind

    @Remind.setter
    def Remind(self, Remind):
        self._Remind = Remind

    @property
    def Warn(self):
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        self._Warn = Warn

    @property
    def Serious(self):
        return self._Serious

    @Serious.setter
    def Serious(self, Serious):
        self._Serious = Serious


    def _deserialize(self, params):
        self._Remind = params.get("Remind")
        self._Warn = params.get("Warn")
        self._Serious = params.get("Serious")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHistory(AbstractModel):
    """告警历史数据

    """

    def __init__(self):
        r"""
        :param _AlarmId: 告警历史Id
        :type AlarmId: str
        :param _MonitorType: 监控类型
        :type MonitorType: str
        :param _Namespace: 策略类型
        :type Namespace: str
        :param _AlarmObject: 告警对象
        :type AlarmObject: str
        :param _Content: 告警内容
        :type Content: str
        :param _FirstOccurTime: 时间戳，首次出现时间
        :type FirstOccurTime: int
        :param _LastOccurTime: 时间戳，最后出现时间
        :type LastOccurTime: int
        :param _AlarmStatus: 告警状态，ALARM=未恢复 OK=已恢复 NO_CONF=已失效 NO_DATA=数据不足
        :type AlarmStatus: str
        :param _PolicyId: 告警策略 Id
        :type PolicyId: str
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _VPC: 基础产品告警的告警对象所属网络
        :type VPC: str
        :param _ProjectId: 项目 Id
        :type ProjectId: int
        :param _ProjectName: 项目名字
        :type ProjectName: str
        :param _InstanceGroup: 告警对象所属实例组
        :type InstanceGroup: list of InstanceGroups
        :param _ReceiverUids: 接收人列表
        :type ReceiverUids: list of int
        :param _ReceiverGroups: 接收组列表
        :type ReceiverGroups: list of int
        :param _NoticeWays: 告警渠道列表 SMS=短信 EMAIL=邮件 CALL=电话 WECHAT=微信
        :type NoticeWays: list of str
        :param _OriginId: 可用于实例、实例组的绑定和解绑接口（[BindingPolicyObject](https://cloud.tencent.com/document/product/248/40421)、[UnBindingAllPolicyObject](https://cloud.tencent.com/document/product/248/40568)、[UnBindingPolicyObject](https://cloud.tencent.com/document/product/248/40567)）的策略 ID
        :type OriginId: str
        :param _AlarmType: 告警类型
        :type AlarmType: str
        :param _EventId: 事件Id
        :type EventId: int
        :param _Region: 地域
        :type Region: str
        :param _PolicyExists: 策略是否存在 0=不存在 1=存在
        :type PolicyExists: int
        :param _MetricsInfo: 指标信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricsInfo: list of AlarmHistoryMetric
        :param _Dimensions: 告警实例的维度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: str
        :param _AlarmLevel: 告警等级
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmLevel: str
        :param _ShieldFlag: 是否有配置告警屏蔽规则
注意：此字段可能返回 null，表示取不到有效值。
        :type ShieldFlag: int
        :param _AlarmShieldingType: 屏蔽类型（英文）
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmShieldingType: str
        :param _AlarmShieldingTime: 屏蔽时间（英文）
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmShieldingTime: str
        :param _AlarmShieldingShowType: 屏蔽类型（中文）
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmShieldingShowType: str
        :param _AlarmShieldingShowTime: 屏蔽时间（中文）
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmShieldingShowTime: str
        :param _AlarmShieldReason: 屏蔽原因
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmShieldReason: str
        :param _InternalDimensions: 告警实例的维度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalDimensions: str
        :param _MetricName: 指标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _PolicyPermissions: 策略是否有权限
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyPermissions: int
        """
        self._AlarmId = None
        self._MonitorType = None
        self._Namespace = None
        self._AlarmObject = None
        self._Content = None
        self._FirstOccurTime = None
        self._LastOccurTime = None
        self._AlarmStatus = None
        self._PolicyId = None
        self._PolicyName = None
        self._VPC = None
        self._ProjectId = None
        self._ProjectName = None
        self._InstanceGroup = None
        self._ReceiverUids = None
        self._ReceiverGroups = None
        self._NoticeWays = None
        self._OriginId = None
        self._AlarmType = None
        self._EventId = None
        self._Region = None
        self._PolicyExists = None
        self._MetricsInfo = None
        self._Dimensions = None
        self._AlarmLevel = None
        self._ShieldFlag = None
        self._AlarmShieldingType = None
        self._AlarmShieldingTime = None
        self._AlarmShieldingShowType = None
        self._AlarmShieldingShowTime = None
        self._AlarmShieldReason = None
        self._InternalDimensions = None
        self._MetricName = None
        self._PolicyPermissions = None

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def AlarmObject(self):
        return self._AlarmObject

    @AlarmObject.setter
    def AlarmObject(self, AlarmObject):
        self._AlarmObject = AlarmObject

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FirstOccurTime(self):
        return self._FirstOccurTime

    @FirstOccurTime.setter
    def FirstOccurTime(self, FirstOccurTime):
        self._FirstOccurTime = FirstOccurTime

    @property
    def LastOccurTime(self):
        return self._LastOccurTime

    @LastOccurTime.setter
    def LastOccurTime(self, LastOccurTime):
        self._LastOccurTime = LastOccurTime

    @property
    def AlarmStatus(self):
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

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
    def VPC(self):
        return self._VPC

    @VPC.setter
    def VPC(self, VPC):
        self._VPC = VPC

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
    def InstanceGroup(self):
        return self._InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, InstanceGroup):
        self._InstanceGroup = InstanceGroup

    @property
    def ReceiverUids(self):
        return self._ReceiverUids

    @ReceiverUids.setter
    def ReceiverUids(self, ReceiverUids):
        self._ReceiverUids = ReceiverUids

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def NoticeWays(self):
        return self._NoticeWays

    @NoticeWays.setter
    def NoticeWays(self, NoticeWays):
        self._NoticeWays = NoticeWays

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PolicyExists(self):
        return self._PolicyExists

    @PolicyExists.setter
    def PolicyExists(self, PolicyExists):
        self._PolicyExists = PolicyExists

    @property
    def MetricsInfo(self):
        return self._MetricsInfo

    @MetricsInfo.setter
    def MetricsInfo(self, MetricsInfo):
        self._MetricsInfo = MetricsInfo

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def ShieldFlag(self):
        return self._ShieldFlag

    @ShieldFlag.setter
    def ShieldFlag(self, ShieldFlag):
        self._ShieldFlag = ShieldFlag

    @property
    def AlarmShieldingType(self):
        return self._AlarmShieldingType

    @AlarmShieldingType.setter
    def AlarmShieldingType(self, AlarmShieldingType):
        self._AlarmShieldingType = AlarmShieldingType

    @property
    def AlarmShieldingTime(self):
        return self._AlarmShieldingTime

    @AlarmShieldingTime.setter
    def AlarmShieldingTime(self, AlarmShieldingTime):
        self._AlarmShieldingTime = AlarmShieldingTime

    @property
    def AlarmShieldingShowType(self):
        return self._AlarmShieldingShowType

    @AlarmShieldingShowType.setter
    def AlarmShieldingShowType(self, AlarmShieldingShowType):
        self._AlarmShieldingShowType = AlarmShieldingShowType

    @property
    def AlarmShieldingShowTime(self):
        return self._AlarmShieldingShowTime

    @AlarmShieldingShowTime.setter
    def AlarmShieldingShowTime(self, AlarmShieldingShowTime):
        self._AlarmShieldingShowTime = AlarmShieldingShowTime

    @property
    def AlarmShieldReason(self):
        return self._AlarmShieldReason

    @AlarmShieldReason.setter
    def AlarmShieldReason(self, AlarmShieldReason):
        self._AlarmShieldReason = AlarmShieldReason

    @property
    def InternalDimensions(self):
        return self._InternalDimensions

    @InternalDimensions.setter
    def InternalDimensions(self, InternalDimensions):
        self._InternalDimensions = InternalDimensions

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def PolicyPermissions(self):
        return self._PolicyPermissions

    @PolicyPermissions.setter
    def PolicyPermissions(self, PolicyPermissions):
        self._PolicyPermissions = PolicyPermissions


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        self._MonitorType = params.get("MonitorType")
        self._Namespace = params.get("Namespace")
        self._AlarmObject = params.get("AlarmObject")
        self._Content = params.get("Content")
        self._FirstOccurTime = params.get("FirstOccurTime")
        self._LastOccurTime = params.get("LastOccurTime")
        self._AlarmStatus = params.get("AlarmStatus")
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._VPC = params.get("VPC")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        if params.get("InstanceGroup") is not None:
            self._InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroups()
                obj._deserialize(item)
                self._InstanceGroup.append(obj)
        self._ReceiverUids = params.get("ReceiverUids")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._NoticeWays = params.get("NoticeWays")
        self._OriginId = params.get("OriginId")
        self._AlarmType = params.get("AlarmType")
        self._EventId = params.get("EventId")
        self._Region = params.get("Region")
        self._PolicyExists = params.get("PolicyExists")
        if params.get("MetricsInfo") is not None:
            self._MetricsInfo = []
            for item in params.get("MetricsInfo"):
                obj = AlarmHistoryMetric()
                obj._deserialize(item)
                self._MetricsInfo.append(obj)
        self._Dimensions = params.get("Dimensions")
        self._AlarmLevel = params.get("AlarmLevel")
        self._ShieldFlag = params.get("ShieldFlag")
        self._AlarmShieldingType = params.get("AlarmShieldingType")
        self._AlarmShieldingTime = params.get("AlarmShieldingTime")
        self._AlarmShieldingShowType = params.get("AlarmShieldingShowType")
        self._AlarmShieldingShowTime = params.get("AlarmShieldingShowTime")
        self._AlarmShieldReason = params.get("AlarmShieldReason")
        self._InternalDimensions = params.get("InternalDimensions")
        self._MetricName = params.get("MetricName")
        self._PolicyPermissions = params.get("PolicyPermissions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHistoryMetric(AbstractModel):
    """告警历史的指标信息

    """

    def __init__(self):
        r"""
        :param _QceNamespace: 云产品监控类型查询数据使用的命名空间
        :type QceNamespace: str
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Period: 统计周期
        :type Period: int
        :param _Value: 触发告警的数值
        :type Value: str
        :param _Description: 指标的展示名
        :type Description: str
        """
        self._QceNamespace = None
        self._MetricName = None
        self._Period = None
        self._Value = None
        self._Description = None

    @property
    def QceNamespace(self):
        return self._QceNamespace

    @QceNamespace.setter
    def QceNamespace(self, QceNamespace):
        self._QceNamespace = QceNamespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._QceNamespace = params.get("QceNamespace")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._Value = params.get("Value")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotice(AbstractModel):
    """告警通知模板详情

    """

    def __init__(self):
        r"""
        :param _Id: 告警通知模板 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 告警通知模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _UpdatedAt: 上次修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _UpdatedBy: 上次修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedBy: str
        :param _NoticeType: 告警通知类型 ALARM=未恢复通知 OK=已恢复通知 ALL=全部通知
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeType: str
        :param _UserNotices: 用户通知列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserNotices: list of UserNotice
        :param _URLNotices: 回调通知列表
注意：此字段可能返回 null，表示取不到有效值。
        :type URLNotices: list of URLNotice
        :param _IsPreset: 是否是系统预设通知模板 0=否 1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPreset: int
        :param _NoticeLanguage: 通知语言 zh-CN=中文 en-US=英文
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeLanguage: str
        :param _PolicyIds: 告警通知模板绑定的告警策略ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyIds: list of str
        :param _AMPConsumerId: 后台 amp consumer id
注意：此字段可能返回 null，表示取不到有效值。
        :type AMPConsumerId: str
        :param _CLSNotices: 推送cls渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type CLSNotices: list of CLSNotice
        :param _Tags: 通知模板绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._Id = None
        self._Name = None
        self._UpdatedAt = None
        self._UpdatedBy = None
        self._NoticeType = None
        self._UserNotices = None
        self._URLNotices = None
        self._IsPreset = None
        self._NoticeLanguage = None
        self._PolicyIds = None
        self._AMPConsumerId = None
        self._CLSNotices = None
        self._Tags = None

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
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def UpdatedBy(self):
        return self._UpdatedBy

    @UpdatedBy.setter
    def UpdatedBy(self, UpdatedBy):
        self._UpdatedBy = UpdatedBy

    @property
    def NoticeType(self):
        return self._NoticeType

    @NoticeType.setter
    def NoticeType(self, NoticeType):
        self._NoticeType = NoticeType

    @property
    def UserNotices(self):
        return self._UserNotices

    @UserNotices.setter
    def UserNotices(self, UserNotices):
        self._UserNotices = UserNotices

    @property
    def URLNotices(self):
        return self._URLNotices

    @URLNotices.setter
    def URLNotices(self, URLNotices):
        self._URLNotices = URLNotices

    @property
    def IsPreset(self):
        return self._IsPreset

    @IsPreset.setter
    def IsPreset(self, IsPreset):
        self._IsPreset = IsPreset

    @property
    def NoticeLanguage(self):
        return self._NoticeLanguage

    @NoticeLanguage.setter
    def NoticeLanguage(self, NoticeLanguage):
        self._NoticeLanguage = NoticeLanguage

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def AMPConsumerId(self):
        return self._AMPConsumerId

    @AMPConsumerId.setter
    def AMPConsumerId(self, AMPConsumerId):
        self._AMPConsumerId = AMPConsumerId

    @property
    def CLSNotices(self):
        return self._CLSNotices

    @CLSNotices.setter
    def CLSNotices(self, CLSNotices):
        self._CLSNotices = CLSNotices

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._UpdatedAt = params.get("UpdatedAt")
        self._UpdatedBy = params.get("UpdatedBy")
        self._NoticeType = params.get("NoticeType")
        if params.get("UserNotices") is not None:
            self._UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self._UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self._URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self._URLNotices.append(obj)
        self._IsPreset = params.get("IsPreset")
        self._NoticeLanguage = params.get("NoticeLanguage")
        self._PolicyIds = params.get("PolicyIds")
        self._AMPConsumerId = params.get("AMPConsumerId")
        if params.get("CLSNotices") is not None:
            self._CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self._CLSNotices.append(obj)
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
        


class AlarmPolicy(AbstractModel):
    """告警策略详情

    """

    def __init__(self):
        r"""
        :param _PolicyId: 告警策略 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: str
        :param _PolicyName: 告警策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _MonitorType: 监控类型 MT_QCE=云产品监控
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorType: str
        :param _Enable: 启停状态 0=停用 1=启用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param _UseSum: 策略组绑定的实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type UseSum: int
        :param _ProjectId: 项目 Id -1=无项目 0=默认项目
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _ProjectName: 项目名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _Namespace: 告警策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _ConditionTemplateId: 触发条件模板 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionTemplateId: str
        :param _Condition: 指标触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param _EventCondition: 事件触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param _NoticeIds: 通知规则 id 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeIds: list of str
        :param _Notices: 通知规则 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Notices: list of AlarmNotice
        :param _TriggerTasks: 触发任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param _ConditionsTemp: 模板策略组
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.ConditionsTemp`
        :param _LastEditUin: 最后编辑的用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type LastEditUin: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _InsertTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: int
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: list of str
        :param _NamespaceShowName: namespace显示名字
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceShowName: str
        :param _IsDefault: 是否默认策略，1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: int
        :param _CanSetDefault: 能否设置默认策略，1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type CanSetDefault: int
        :param _InstanceGroupId: 实例分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupId: int
        :param _InstanceSum: 实例分组总实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSum: int
        :param _InstanceGroupName: 实例分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupName: str
        :param _RuleType: 触发条件类型 STATIC=静态阈值 DYNAMIC=动态类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _OriginId: 用于实例、实例组绑定和解绑接口（BindingPolicyObject、UnBindingAllPolicyObject、UnBindingPolicyObject）的策略 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginId: str
        :param _TagInstances: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInstances: list of TagInstance
        :param _Filter: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmConditionFilter`
        :param _GroupBy: 聚合条件
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupBy: list of AlarmGroupByItem
        :param _FilterDimensionsParam: 策略关联的过滤维度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterDimensionsParam: str
        :param _IsOneClick: 是否为一键告警策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOneClick: int
        :param _OneClickStatus: 一键告警策略是否开启
注意：此字段可能返回 null，表示取不到有效值。
        :type OneClickStatus: int
        :param _AdvancedMetricNumber: 高级指标数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedMetricNumber: int
        :param _IsBindAll: 策略是否是全部对象策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBindAll: int
        :param _Tags: 策略标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _IsSupportAlarmTag: 是否支持告警标签
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportAlarmTag: int
        :param _TagOperation: 多标签交/并集关系
注意：此字段可能返回 null，表示取不到有效值。
        :type TagOperation: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._Remark = None
        self._MonitorType = None
        self._Enable = None
        self._UseSum = None
        self._ProjectId = None
        self._ProjectName = None
        self._Namespace = None
        self._ConditionTemplateId = None
        self._Condition = None
        self._EventCondition = None
        self._NoticeIds = None
        self._Notices = None
        self._TriggerTasks = None
        self._ConditionsTemp = None
        self._LastEditUin = None
        self._UpdateTime = None
        self._InsertTime = None
        self._Region = None
        self._NamespaceShowName = None
        self._IsDefault = None
        self._CanSetDefault = None
        self._InstanceGroupId = None
        self._InstanceSum = None
        self._InstanceGroupName = None
        self._RuleType = None
        self._OriginId = None
        self._TagInstances = None
        self._Filter = None
        self._GroupBy = None
        self._FilterDimensionsParam = None
        self._IsOneClick = None
        self._OneClickStatus = None
        self._AdvancedMetricNumber = None
        self._IsBindAll = None
        self._Tags = None
        self._IsSupportAlarmTag = None
        self._TagOperation = None

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
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def UseSum(self):
        return self._UseSum

    @UseSum.setter
    def UseSum(self, UseSum):
        self._UseSum = UseSum

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
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ConditionTemplateId(self):
        return self._ConditionTemplateId

    @ConditionTemplateId.setter
    def ConditionTemplateId(self, ConditionTemplateId):
        self._ConditionTemplateId = ConditionTemplateId

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def EventCondition(self):
        return self._EventCondition

    @EventCondition.setter
    def EventCondition(self, EventCondition):
        self._EventCondition = EventCondition

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def Notices(self):
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def TriggerTasks(self):
        return self._TriggerTasks

    @TriggerTasks.setter
    def TriggerTasks(self, TriggerTasks):
        self._TriggerTasks = TriggerTasks

    @property
    def ConditionsTemp(self):
        return self._ConditionsTemp

    @ConditionsTemp.setter
    def ConditionsTemp(self, ConditionsTemp):
        self._ConditionsTemp = ConditionsTemp

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def NamespaceShowName(self):
        return self._NamespaceShowName

    @NamespaceShowName.setter
    def NamespaceShowName(self, NamespaceShowName):
        self._NamespaceShowName = NamespaceShowName

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def CanSetDefault(self):
        return self._CanSetDefault

    @CanSetDefault.setter
    def CanSetDefault(self, CanSetDefault):
        self._CanSetDefault = CanSetDefault

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def InstanceSum(self):
        return self._InstanceSum

    @InstanceSum.setter
    def InstanceSum(self, InstanceSum):
        self._InstanceSum = InstanceSum

    @property
    def InstanceGroupName(self):
        return self._InstanceGroupName

    @InstanceGroupName.setter
    def InstanceGroupName(self, InstanceGroupName):
        self._InstanceGroupName = InstanceGroupName

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def TagInstances(self):
        return self._TagInstances

    @TagInstances.setter
    def TagInstances(self, TagInstances):
        self._TagInstances = TagInstances

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def FilterDimensionsParam(self):
        return self._FilterDimensionsParam

    @FilterDimensionsParam.setter
    def FilterDimensionsParam(self, FilterDimensionsParam):
        self._FilterDimensionsParam = FilterDimensionsParam

    @property
    def IsOneClick(self):
        return self._IsOneClick

    @IsOneClick.setter
    def IsOneClick(self, IsOneClick):
        self._IsOneClick = IsOneClick

    @property
    def OneClickStatus(self):
        return self._OneClickStatus

    @OneClickStatus.setter
    def OneClickStatus(self, OneClickStatus):
        self._OneClickStatus = OneClickStatus

    @property
    def AdvancedMetricNumber(self):
        return self._AdvancedMetricNumber

    @AdvancedMetricNumber.setter
    def AdvancedMetricNumber(self, AdvancedMetricNumber):
        self._AdvancedMetricNumber = AdvancedMetricNumber

    @property
    def IsBindAll(self):
        return self._IsBindAll

    @IsBindAll.setter
    def IsBindAll(self, IsBindAll):
        self._IsBindAll = IsBindAll

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsSupportAlarmTag(self):
        return self._IsSupportAlarmTag

    @IsSupportAlarmTag.setter
    def IsSupportAlarmTag(self, IsSupportAlarmTag):
        self._IsSupportAlarmTag = IsSupportAlarmTag

    @property
    def TagOperation(self):
        return self._TagOperation

    @TagOperation.setter
    def TagOperation(self, TagOperation):
        self._TagOperation = TagOperation


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Remark = params.get("Remark")
        self._MonitorType = params.get("MonitorType")
        self._Enable = params.get("Enable")
        self._UseSum = params.get("UseSum")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Namespace = params.get("Namespace")
        self._ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self._Condition = AlarmPolicyCondition()
            self._Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self._EventCondition = AlarmPolicyEventCondition()
            self._EventCondition._deserialize(params.get("EventCondition"))
        self._NoticeIds = params.get("NoticeIds")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        if params.get("TriggerTasks") is not None:
            self._TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self._TriggerTasks.append(obj)
        if params.get("ConditionsTemp") is not None:
            self._ConditionsTemp = ConditionsTemp()
            self._ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self._LastEditUin = params.get("LastEditUin")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        self._Region = params.get("Region")
        self._NamespaceShowName = params.get("NamespaceShowName")
        self._IsDefault = params.get("IsDefault")
        self._CanSetDefault = params.get("CanSetDefault")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._InstanceSum = params.get("InstanceSum")
        self._InstanceGroupName = params.get("InstanceGroupName")
        self._RuleType = params.get("RuleType")
        self._OriginId = params.get("OriginId")
        if params.get("TagInstances") is not None:
            self._TagInstances = []
            for item in params.get("TagInstances"):
                obj = TagInstance()
                obj._deserialize(item)
                self._TagInstances.append(obj)
        if params.get("Filter") is not None:
            self._Filter = AlarmConditionFilter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("GroupBy") is not None:
            self._GroupBy = []
            for item in params.get("GroupBy"):
                obj = AlarmGroupByItem()
                obj._deserialize(item)
                self._GroupBy.append(obj)
        self._FilterDimensionsParam = params.get("FilterDimensionsParam")
        self._IsOneClick = params.get("IsOneClick")
        self._OneClickStatus = params.get("OneClickStatus")
        self._AdvancedMetricNumber = params.get("AdvancedMetricNumber")
        self._IsBindAll = params.get("IsBindAll")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsSupportAlarmTag = params.get("IsSupportAlarmTag")
        self._TagOperation = params.get("TagOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyCondition(AbstractModel):
    """告警策略指标触发条件

    """

    def __init__(self):
        r"""
        :param _IsUnionRule: 告警触发条件的判断方式. 0: 任意; 1: 全部; 2: 复合. 当取值为2的时候为复合告警，与参数 ComplexExpression 配合使用.
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        :param _Rules: 告警触发条件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of AlarmPolicyRule
        :param _ComplexExpression: 复合告警触发条件的判断表达式，当 IsUnionRule 取值为2的时候有效. 其作用是描述多个触发条件需要满足表达式求值为True时才算是满足告警条件.
注意：此字段可能返回 null，表示取不到有效值。
        :type ComplexExpression: str
        """
        self._IsUnionRule = None
        self._Rules = None
        self._ComplexExpression = None

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ComplexExpression(self):
        return self._ComplexExpression

    @ComplexExpression.setter
    def ComplexExpression(self, ComplexExpression):
        self._ComplexExpression = ComplexExpression


    def _deserialize(self, params):
        self._IsUnionRule = params.get("IsUnionRule")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = AlarmPolicyRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._ComplexExpression = params.get("ComplexExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyEventCondition(AbstractModel):
    """告警策略事件触发条件

    """

    def __init__(self):
        r"""
        :param _Rules: 告警触发条件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of AlarmPolicyRule
        """
        self._Rules = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = AlarmPolicyRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyFilter(AbstractModel):
    """告警策略过滤条件

    """

    def __init__(self):
        r"""
        :param _Type: 过滤条件类型 DIMENSION=使用 Dimensions 做过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Dimensions: AlarmPolicyDimension 二维数组序列化后的json字符串，一维数组之间互为或关系，一维数组内的元素互为与关系
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: str
        """
        self._Type = None
        self._Dimensions = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyRule(AbstractModel):
    """告警策略触发条件

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名或事件名，支持的指标可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询，支持的事件可以从 [DescribeAlarmEvents](https://cloud.tencent.com/document/product/248/51284) 查询 。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _Period: 秒数 统计周期，支持的值可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询。
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        :param _Operator: 英文运算符
intelligent=无阈值智能检测
eq=等于
ge=大于等于
gt=大于
le=小于等于
lt=小于
ne=不等于
day_increase=天同比增长
day_decrease=天同比下降
day_wave=天同比波动
week_increase=周同比增长
week_decrease=周同比下降
week_wave=周同比波动
cycle_increase=环比增长
cycle_decrease=环比下降
cycle_wave=环比波动
re=正则匹配
支持的值可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询。
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _Value: 阈值，支持的范围可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _ContinuePeriod: 周期数 持续通知周期 1=持续1个周期 2=持续2个周期...，支持的值可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinuePeriod: int
        :param _NoticeFrequency: 秒数 告警间隔  0=不重复 300=每5分钟告警一次 600=每10分钟告警一次 900=每15分钟告警一次 1800=每30分钟告警一次 3600=每1小时告警一次 7200=每2小时告警一次 10800=每3小时告警一次 21600=每6小时告警一次 43200=每12小时告警一次 86400=每1天告警一次
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeFrequency: int
        :param _IsPowerNotice: 告警频率是否指数增长 0=否 1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPowerNotice: int
        :param _Filter: 对于单个触发规则的过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param _Description: 指标展示名，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Unit: 单位，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _RuleType: 触发条件类型 STATIC=静态阈值 DYNAMIC=动态阈值。创建或编辑策略时，如不填则默认为 STATIC。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _IsAdvanced: 是否为高级指标，0否，1是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAdvanced: int
        :param _IsOpen: 高级指标是否开通，0否，1是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOpen: int
        :param _ProductId: 集成中心产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _ValueMax: 最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueMax: float
        :param _ValueMin: 最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueMin: float
        :param _HierarchicalValue: 告警分级阈值配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HierarchicalValue: :class:`tencentcloud.monitor.v20180724.models.AlarmHierarchicalValue`
        :param _IsLatenessMetric: 是否延迟指标
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLatenessMetric: int
        """
        self._MetricName = None
        self._Period = None
        self._Operator = None
        self._Value = None
        self._ContinuePeriod = None
        self._NoticeFrequency = None
        self._IsPowerNotice = None
        self._Filter = None
        self._Description = None
        self._Unit = None
        self._RuleType = None
        self._IsAdvanced = None
        self._IsOpen = None
        self._ProductId = None
        self._ValueMax = None
        self._ValueMin = None
        self._HierarchicalValue = None
        self._IsLatenessMetric = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ContinuePeriod(self):
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod

    @property
    def NoticeFrequency(self):
        return self._NoticeFrequency

    @NoticeFrequency.setter
    def NoticeFrequency(self, NoticeFrequency):
        self._NoticeFrequency = NoticeFrequency

    @property
    def IsPowerNotice(self):
        return self._IsPowerNotice

    @IsPowerNotice.setter
    def IsPowerNotice(self, IsPowerNotice):
        self._IsPowerNotice = IsPowerNotice

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def IsAdvanced(self):
        return self._IsAdvanced

    @IsAdvanced.setter
    def IsAdvanced(self, IsAdvanced):
        self._IsAdvanced = IsAdvanced

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ValueMax(self):
        return self._ValueMax

    @ValueMax.setter
    def ValueMax(self, ValueMax):
        self._ValueMax = ValueMax

    @property
    def ValueMin(self):
        return self._ValueMin

    @ValueMin.setter
    def ValueMin(self, ValueMin):
        self._ValueMin = ValueMin

    @property
    def HierarchicalValue(self):
        return self._HierarchicalValue

    @HierarchicalValue.setter
    def HierarchicalValue(self, HierarchicalValue):
        self._HierarchicalValue = HierarchicalValue

    @property
    def IsLatenessMetric(self):
        return self._IsLatenessMetric

    @IsLatenessMetric.setter
    def IsLatenessMetric(self, IsLatenessMetric):
        self._IsLatenessMetric = IsLatenessMetric


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        self._ContinuePeriod = params.get("ContinuePeriod")
        self._NoticeFrequency = params.get("NoticeFrequency")
        self._IsPowerNotice = params.get("IsPowerNotice")
        if params.get("Filter") is not None:
            self._Filter = AlarmPolicyFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._Description = params.get("Description")
        self._Unit = params.get("Unit")
        self._RuleType = params.get("RuleType")
        self._IsAdvanced = params.get("IsAdvanced")
        self._IsOpen = params.get("IsOpen")
        self._ProductId = params.get("ProductId")
        self._ValueMax = params.get("ValueMax")
        self._ValueMin = params.get("ValueMin")
        if params.get("HierarchicalValue") is not None:
            self._HierarchicalValue = AlarmHierarchicalValue()
            self._HierarchicalValue._deserialize(params.get("HierarchicalValue"))
        self._IsLatenessMetric = params.get("IsLatenessMetric")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyTriggerTask(AbstractModel):
    """告警策略触发任务

    """

    def __init__(self):
        r"""
        :param _Type: 触发任务类型 AS=弹性伸缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _TaskConfig: 用 json 表示配置信息 {"Key1":"Value1","Key2":"Value2"}
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskConfig: str
        """
        self._Type = None
        self._TaskConfig = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TaskConfig(self):
        return self._TaskConfig

    @TaskConfig.setter
    def TaskConfig(self, TaskConfig):
        self._TaskConfig = TaskConfig


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TaskConfig = params.get("TaskConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindPrometheusManagedGrafanaRequest(AbstractModel):
    """BindPrometheusManagedGrafana请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _GrafanaId: Grafana 可视化服务实例 ID
        :type GrafanaId: str
        """
        self._InstanceId = None
        self._GrafanaId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GrafanaId(self):
        return self._GrafanaId

    @GrafanaId.setter
    def GrafanaId(self, GrafanaId):
        self._GrafanaId = GrafanaId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GrafanaId = params.get("GrafanaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindPrometheusManagedGrafanaResponse(AbstractModel):
    """BindPrometheusManagedGrafana返回参数结构体

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


class BindingPolicyObjectDimension(AbstractModel):
    """策略绑定实例维度信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域名
        :type Region: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _Dimensions: 实例的维度信息，格式为
{"unInstanceId":"ins-00jvv9mo"}。不同云产品的维度信息不同，详见
[指标维度信息Dimensions列表](https://cloud.tencent.com/document/product/248/50397)
        :type Dimensions: str
        :param _EventDimensions: 事件维度信息
        :type EventDimensions: str
        """
        self._Region = None
        self._RegionId = None
        self._Dimensions = None
        self._EventDimensions = None

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
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def EventDimensions(self):
        return self._EventDimensions

    @EventDimensions.setter
    def EventDimensions(self, EventDimensions):
        self._EventDimensions = EventDimensions


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._Dimensions = params.get("Dimensions")
        self._EventDimensions = params.get("EventDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingPolicyObjectRequest(AbstractModel):
    """BindingPolicyObject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 必填。固定值"monitor"
        :type Module: str
        :param _GroupId: 策略组id，例如 4739573。逐渐弃用，建议使用 PolicyId 参数
        :type GroupId: int
        :param _PolicyId: 告警策略ID，例如“policy-gh892hg0”。PolicyId 参数与 GroupId 参数至少要填一个，否则会报参数错误，建议使用该参数。若两者同时存在则以该参数为准
        :type PolicyId: str
        :param _InstanceGroupId: 实例分组ID
        :type InstanceGroupId: int
        :param _Dimensions: 需要绑定的对象维度信息
        :type Dimensions: list of BindingPolicyObjectDimension
        :param _EbSubject: 事件配置的告警
        :type EbSubject: str
        :param _EbEventFlag: 是否配置了事件告警
        :type EbEventFlag: int
        """
        self._Module = None
        self._GroupId = None
        self._PolicyId = None
        self._InstanceGroupId = None
        self._Dimensions = None
        self._EbSubject = None
        self._EbEventFlag = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject

    @property
    def EbEventFlag(self):
        return self._EbEventFlag

    @EbEventFlag.setter
    def EbEventFlag(self, EbEventFlag):
        self._EbEventFlag = EbEventFlag


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._PolicyId = params.get("PolicyId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = BindingPolicyObjectDimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._EbSubject = params.get("EbSubject")
        self._EbEventFlag = params.get("EbEventFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingPolicyObjectResponse(AbstractModel):
    """BindingPolicyObject返回参数结构体

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


class BindingPolicyTagRequest(AbstractModel):
    """BindingPolicyTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定取值 monitor
        :type Module: str
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _GroupId: 用于实例、实例组绑定和解绑接口（BindingPolicyObject、UnBindingAllPolicyObject、UnBindingPolicyObject）的策略 ID
        :type GroupId: str
        :param _ServiceType: 产品类型
        :type ServiceType: str
        :param _Tag: 策略标签
        :type Tag: :class:`tencentcloud.monitor.v20180724.models.PolicyTag`
        :param _InstanceGroupId: 实例分组ID
        :type InstanceGroupId: int
        :param _BatchTag: 批量绑定标签
        :type BatchTag: list of PolicyTag
        :param _EbEventFlag: 是否同步eb
        :type EbEventFlag: int
        :param _EbSubject: 事件配置的告警
        :type EbSubject: str
        :param _TagOperation: 标识标签取交/并集关系
        :type TagOperation: str
        """
        self._Module = None
        self._PolicyId = None
        self._GroupId = None
        self._ServiceType = None
        self._Tag = None
        self._InstanceGroupId = None
        self._BatchTag = None
        self._EbEventFlag = None
        self._EbSubject = None
        self._TagOperation = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def BatchTag(self):
        return self._BatchTag

    @BatchTag.setter
    def BatchTag(self, BatchTag):
        self._BatchTag = BatchTag

    @property
    def EbEventFlag(self):
        return self._EbEventFlag

    @EbEventFlag.setter
    def EbEventFlag(self, EbEventFlag):
        self._EbEventFlag = EbEventFlag

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject

    @property
    def TagOperation(self):
        return self._TagOperation

    @TagOperation.setter
    def TagOperation(self, TagOperation):
        self._TagOperation = TagOperation


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._GroupId = params.get("GroupId")
        self._ServiceType = params.get("ServiceType")
        if params.get("Tag") is not None:
            self._Tag = PolicyTag()
            self._Tag._deserialize(params.get("Tag"))
        self._InstanceGroupId = params.get("InstanceGroupId")
        if params.get("BatchTag") is not None:
            self._BatchTag = []
            for item in params.get("BatchTag"):
                obj = PolicyTag()
                obj._deserialize(item)
                self._BatchTag.append(obj)
        self._EbEventFlag = params.get("EbEventFlag")
        self._EbSubject = params.get("EbSubject")
        self._TagOperation = params.get("TagOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingPolicyTagResponse(AbstractModel):
    """BindingPolicyTag返回参数结构体

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


class CLSNotice(AbstractModel):
    """告警通知中的推送CLS操作

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _LogSetId: 日志集Id
        :type LogSetId: str
        :param _TopicId: 主题Id
        :type TopicId: str
        :param _Enable: 启停状态，可不传，默认启用。0=停用，1=启用
        :type Enable: int
        """
        self._Region = None
        self._LogSetId = None
        self._TopicId = None
        self._Enable = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._LogSetId = params.get("LogSetId")
        self._TopicId = params.get("TopicId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CleanGrafanaInstanceRequest(AbstractModel):
    """CleanGrafanaInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
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
        


class CleanGrafanaInstanceResponse(AbstractModel):
    """CleanGrafanaInstance返回参数结构体

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


class CommonNamespace(AbstractModel):
    """统一的命名空间信息

    """

    def __init__(self):
        r"""
        :param _Id: 命名空间标示
        :type Id: str
        :param _Name: 命名空间名称
        :type Name: str
        :param _Value: 命名空间值
        :type Value: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _Config: 配置信息
        :type Config: str
        :param _AvailableRegions: 支持地域列表
        :type AvailableRegions: list of str
        :param _SortId: 排序Id
        :type SortId: int
        :param _DashboardId: Dashboard中的唯一表示
        :type DashboardId: str
        """
        self._Id = None
        self._Name = None
        self._Value = None
        self._ProductName = None
        self._Config = None
        self._AvailableRegions = None
        self._SortId = None
        self._DashboardId = None

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
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def AvailableRegions(self):
        return self._AvailableRegions

    @AvailableRegions.setter
    def AvailableRegions(self, AvailableRegions):
        self._AvailableRegions = AvailableRegions

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def DashboardId(self):
        return self._DashboardId

    @DashboardId.setter
    def DashboardId(self, DashboardId):
        self._DashboardId = DashboardId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._ProductName = params.get("ProductName")
        self._Config = params.get("Config")
        self._AvailableRegions = params.get("AvailableRegions")
        self._SortId = params.get("SortId")
        self._DashboardId = params.get("DashboardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonNamespaceNew(AbstractModel):
    """策略类型信息

    """

    def __init__(self):
        r"""
        :param _Id: 命名空间标示
        :type Id: str
        :param _Name: 命名空间名称
        :type Name: str
        :param _MonitorType: 监控类型
        :type MonitorType: str
        :param _Dimensions: 维度信息
        :type Dimensions: list of DimensionNew
        """
        self._Id = None
        self._Name = None
        self._MonitorType = None
        self._Dimensions = None

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
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MonitorType = params.get("MonitorType")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionNew()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Condition(AbstractModel):
    """告警条件

    """

    def __init__(self):
        r"""
        :param _AlarmNotifyPeriod: 告警通知频率
        :type AlarmNotifyPeriod: int
        :param _AlarmNotifyType: 重复通知策略预定义（0 - 只告警一次， 1 - 指数告警，2 - 连接告警）
        :type AlarmNotifyType: int
        :param _CalcType: 检测方式
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcType: str
        :param _CalcValue: 检测值
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcValue: str
        :param _ContinueTime: 持续时间，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueTime: str
        :param _MetricID: 指标ID
        :type MetricID: int
        :param _MetricDisplayName: 指标展示名称（对外）
        :type MetricDisplayName: str
        :param _Period: 周期
        :type Period: int
        :param _RuleID: 规则ID
        :type RuleID: int
        :param _Unit: 指标单位
        :type Unit: str
        :param _IsAdvanced: 是否为高级指标，0：否；1：是
        :type IsAdvanced: int
        :param _IsOpen: 是否开通高级指标，0：否；1：是
        :type IsOpen: int
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _HierarchicalValue: 告警分级阈值配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HierarchicalValue: :class:`tencentcloud.monitor.v20180724.models.AlarmHierarchicalValue`
        """
        self._AlarmNotifyPeriod = None
        self._AlarmNotifyType = None
        self._CalcType = None
        self._CalcValue = None
        self._ContinueTime = None
        self._MetricID = None
        self._MetricDisplayName = None
        self._Period = None
        self._RuleID = None
        self._Unit = None
        self._IsAdvanced = None
        self._IsOpen = None
        self._ProductId = None
        self._HierarchicalValue = None

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def ContinueTime(self):
        return self._ContinueTime

    @ContinueTime.setter
    def ContinueTime(self, ContinueTime):
        self._ContinueTime = ContinueTime

    @property
    def MetricID(self):
        return self._MetricID

    @MetricID.setter
    def MetricID(self, MetricID):
        self._MetricID = MetricID

    @property
    def MetricDisplayName(self):
        return self._MetricDisplayName

    @MetricDisplayName.setter
    def MetricDisplayName(self, MetricDisplayName):
        self._MetricDisplayName = MetricDisplayName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def IsAdvanced(self):
        return self._IsAdvanced

    @IsAdvanced.setter
    def IsAdvanced(self, IsAdvanced):
        self._IsAdvanced = IsAdvanced

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def HierarchicalValue(self):
        return self._HierarchicalValue

    @HierarchicalValue.setter
    def HierarchicalValue(self, HierarchicalValue):
        self._HierarchicalValue = HierarchicalValue


    def _deserialize(self, params):
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._CalcType = params.get("CalcType")
        self._CalcValue = params.get("CalcValue")
        self._ContinueTime = params.get("ContinueTime")
        self._MetricID = params.get("MetricID")
        self._MetricDisplayName = params.get("MetricDisplayName")
        self._Period = params.get("Period")
        self._RuleID = params.get("RuleID")
        self._Unit = params.get("Unit")
        self._IsAdvanced = params.get("IsAdvanced")
        self._IsOpen = params.get("IsOpen")
        self._ProductId = params.get("ProductId")
        if params.get("HierarchicalValue") is not None:
            self._HierarchicalValue = AlarmHierarchicalValue()
            self._HierarchicalValue._deserialize(params.get("HierarchicalValue"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionsTemp(AbstractModel):
    """告警条件模板

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param _Condition: 指标触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param _EventCondition: 事件触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        """
        self._TemplateName = None
        self._Condition = None
        self._EventCondition = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def EventCondition(self):
        return self._EventCondition

    @EventCondition.setter
    def EventCondition(self, EventCondition):
        self._EventCondition = EventCondition


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("Condition") is not None:
            self._Condition = AlarmPolicyCondition()
            self._Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self._EventCondition = AlarmPolicyEventCondition()
            self._EventCondition._deserialize(params.get("EventCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeRequest(AbstractModel):
    """CreateAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”
        :type Module: str
        :param _Name: 通知模板名称 60字符以内
        :type Name: str
        :param _NoticeType: 通知类型 ALARM=未恢复通知 OK=已恢复通知 ALL=都通知
        :type NoticeType: str
        :param _NoticeLanguage: 通知语言 zh-CN=中文 en-US=英文
        :type NoticeLanguage: str
        :param _UserNotices: 用户通知 最多5个
        :type UserNotices: list of UserNotice
        :param _URLNotices: 回调通知 最多6个
        :type URLNotices: list of URLNotice
        :param _CLSNotices: 推送CLS日志服务的操作 最多1个
        :type CLSNotices: list of CLSNotice
        :param _Tags: 模板绑定的标签
        :type Tags: list of Tag
        """
        self._Module = None
        self._Name = None
        self._NoticeType = None
        self._NoticeLanguage = None
        self._UserNotices = None
        self._URLNotices = None
        self._CLSNotices = None
        self._Tags = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NoticeType(self):
        return self._NoticeType

    @NoticeType.setter
    def NoticeType(self, NoticeType):
        self._NoticeType = NoticeType

    @property
    def NoticeLanguage(self):
        return self._NoticeLanguage

    @NoticeLanguage.setter
    def NoticeLanguage(self, NoticeLanguage):
        self._NoticeLanguage = NoticeLanguage

    @property
    def UserNotices(self):
        return self._UserNotices

    @UserNotices.setter
    def UserNotices(self, UserNotices):
        self._UserNotices = UserNotices

    @property
    def URLNotices(self):
        return self._URLNotices

    @URLNotices.setter
    def URLNotices(self, URLNotices):
        self._URLNotices = URLNotices

    @property
    def CLSNotices(self):
        return self._CLSNotices

    @CLSNotices.setter
    def CLSNotices(self, CLSNotices):
        self._CLSNotices = CLSNotices

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Name = params.get("Name")
        self._NoticeType = params.get("NoticeType")
        self._NoticeLanguage = params.get("NoticeLanguage")
        if params.get("UserNotices") is not None:
            self._UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self._UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self._URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self._URLNotices.append(obj)
        if params.get("CLSNotices") is not None:
            self._CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self._CLSNotices.append(obj)
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
        


class CreateAlarmNoticeResponse(AbstractModel):
    """CreateAlarmNotice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeId: 告警通知模板ID
        :type NoticeId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NoticeId = None
        self._RequestId = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._RequestId = params.get("RequestId")


class CreateAlarmPolicyRequest(AbstractModel):
    """CreateAlarmPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _PolicyName: 策略名称，不超过60字符
        :type PolicyName: str
        :param _MonitorType: 监控类型 MT_QCE=云产品监控
        :type MonitorType: str
        :param _Namespace: 告警策略类型，由 [DescribeAllNamespaces](https://cloud.tencent.com/document/product/248/48683) 获得。对于云产品监控，取接口出参的 QceNamespacesNew.N.Id，例如 cvm_device
        :type Namespace: str
        :param _Remark: 备注，不超过100字符，仅支持中英文、数字、下划线、-
        :type Remark: str
        :param _Enable: 是否启用 0=停用 1=启用，可不传 默认为1
        :type Enable: int
        :param _ProjectId: 项目 Id，对于区分项目的产品必须传入非 -1 的值。 -1=无项目 0=默认项目，如不传 默认为 -1。支持的项目 Id 可以在控制台 [账号中心-项目管理](https://console.cloud.tencent.com/project) 中查看。
        :type ProjectId: int
        :param _ConditionTemplateId: 触发条件模板 Id，该参数与 Condition 参数二选一。如果策略绑定触发条件模板，则传该参数；否则不传该参数，而是传 Condition 参数。触发条件模板 Id 可以从 [DescribeConditionsTemplateList](https://cloud.tencent.com/document/api/248/70250) 接口获取。
        :type ConditionTemplateId: int
        :param _Condition: 指标触发条件，支持的指标可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询。
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param _EventCondition: 事件触发条件，支持的事件可以从 [DescribeAlarmEvents](https://cloud.tencent.com/document/product/248/51284) 查询。
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param _NoticeIds: 通知规则 Id 列表，由 [DescribeAlarmNotices](https://cloud.tencent.com/document/product/248/51280) 获得
        :type NoticeIds: list of str
        :param _TriggerTasks: 触发任务列表
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param _Filter: 全局过滤条件
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param _GroupBy: 聚合维度列表，指定按哪些维度 key 来做 group by
        :type GroupBy: list of str
        :param _Tags: 模板绑定的标签
        :type Tags: list of Tag
        :param _LogAlarmReqInfo: 日志告警信息
        :type LogAlarmReqInfo: :class:`tencentcloud.monitor.v20180724.models.LogAlarmReq`
        :param _HierarchicalNotices: 告警分级通知规则配置
        :type HierarchicalNotices: list of AlarmHierarchicalNotice
        :param _MigrateFlag: 迁移策略专用字段，0-走鉴权逻辑，1-跳过鉴权逻辑
        :type MigrateFlag: int
        :param _EbSubject: 事件配置的告警
        :type EbSubject: str
        """
        self._Module = None
        self._PolicyName = None
        self._MonitorType = None
        self._Namespace = None
        self._Remark = None
        self._Enable = None
        self._ProjectId = None
        self._ConditionTemplateId = None
        self._Condition = None
        self._EventCondition = None
        self._NoticeIds = None
        self._TriggerTasks = None
        self._Filter = None
        self._GroupBy = None
        self._Tags = None
        self._LogAlarmReqInfo = None
        self._HierarchicalNotices = None
        self._MigrateFlag = None
        self._EbSubject = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ConditionTemplateId(self):
        return self._ConditionTemplateId

    @ConditionTemplateId.setter
    def ConditionTemplateId(self, ConditionTemplateId):
        self._ConditionTemplateId = ConditionTemplateId

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def EventCondition(self):
        return self._EventCondition

    @EventCondition.setter
    def EventCondition(self, EventCondition):
        self._EventCondition = EventCondition

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def TriggerTasks(self):
        return self._TriggerTasks

    @TriggerTasks.setter
    def TriggerTasks(self, TriggerTasks):
        self._TriggerTasks = TriggerTasks

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LogAlarmReqInfo(self):
        return self._LogAlarmReqInfo

    @LogAlarmReqInfo.setter
    def LogAlarmReqInfo(self, LogAlarmReqInfo):
        self._LogAlarmReqInfo = LogAlarmReqInfo

    @property
    def HierarchicalNotices(self):
        return self._HierarchicalNotices

    @HierarchicalNotices.setter
    def HierarchicalNotices(self, HierarchicalNotices):
        self._HierarchicalNotices = HierarchicalNotices

    @property
    def MigrateFlag(self):
        return self._MigrateFlag

    @MigrateFlag.setter
    def MigrateFlag(self, MigrateFlag):
        self._MigrateFlag = MigrateFlag

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyName = params.get("PolicyName")
        self._MonitorType = params.get("MonitorType")
        self._Namespace = params.get("Namespace")
        self._Remark = params.get("Remark")
        self._Enable = params.get("Enable")
        self._ProjectId = params.get("ProjectId")
        self._ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self._Condition = AlarmPolicyCondition()
            self._Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self._EventCondition = AlarmPolicyEventCondition()
            self._EventCondition._deserialize(params.get("EventCondition"))
        self._NoticeIds = params.get("NoticeIds")
        if params.get("TriggerTasks") is not None:
            self._TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self._TriggerTasks.append(obj)
        if params.get("Filter") is not None:
            self._Filter = AlarmPolicyFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._GroupBy = params.get("GroupBy")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("LogAlarmReqInfo") is not None:
            self._LogAlarmReqInfo = LogAlarmReq()
            self._LogAlarmReqInfo._deserialize(params.get("LogAlarmReqInfo"))
        if params.get("HierarchicalNotices") is not None:
            self._HierarchicalNotices = []
            for item in params.get("HierarchicalNotices"):
                obj = AlarmHierarchicalNotice()
                obj._deserialize(item)
                self._HierarchicalNotices.append(obj)
        self._MigrateFlag = params.get("MigrateFlag")
        self._EbSubject = params.get("EbSubject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmPolicyResponse(AbstractModel):
    """CreateAlarmPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 告警策略 ID
        :type PolicyId: str
        :param _OriginId: 可用于实例、实例组的绑定和解绑接口（[BindingPolicyObject](https://cloud.tencent.com/document/product/248/40421)、[UnBindingAllPolicyObject](https://cloud.tencent.com/document/product/248/40568)、[UnBindingPolicyObject](https://cloud.tencent.com/document/product/248/40567)）的策略 ID
        :type OriginId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._OriginId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._OriginId = params.get("OriginId")
        self._RequestId = params.get("RequestId")


class CreateAlertRuleRequest(AbstractModel):
    """CreateAlertRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID，例如：prom-abcd1234
        :type InstanceId: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _Expr: 规则表达式，可参考<a href="https://cloud.tencent.com/document/product/1416/56008">告警规则说明</a>
        :type Expr: str
        :param _Receivers: 告警通知模板 ID 列表
        :type Receivers: list of str
        :param _RuleState: 规则状态码，取值如下：
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param _Duration: 规则报警持续时间
        :type Duration: str
        :param _Labels: 标签列表
        :type Labels: list of PrometheusRuleKV
        :param _Annotations: 注释列表。

告警对象和告警消息是 Prometheus Rule Annotations 的特殊字段，需要通过 annotations 来传递，对应的 Key 分别为summary/description。
        :type Annotations: list of PrometheusRuleKV
        :param _Type: 报警策略模板分类
        :type Type: str
        """
        self._InstanceId = None
        self._RuleName = None
        self._Expr = None
        self._Receivers = None
        self._RuleState = None
        self._Duration = None
        self._Labels = None
        self._Annotations = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Expr(self):
        return self._Expr

    @Expr.setter
    def Expr(self, Expr):
        self._Expr = Expr

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RuleName = params.get("RuleName")
        self._Expr = params.get("Expr")
        self._Receivers = params.get("Receivers")
        self._RuleState = params.get("RuleState")
        self._Duration = params.get("Duration")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlertRuleResponse(AbstractModel):
    """CreateAlertRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateExporterIntegrationRequest(AbstractModel):
    """CreateExporterIntegration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Kind: 类型(可通过 DescribePrometheusIntegrations 接口获取，取每一项中的 ExporterType 字段)
        :type Kind: str
        :param _Content: 集成配置
        :type Content: str
        :param _KubeType: Kubernetes 集群类型，可不填，取值如下：
<li> 1= 容器集群(TKE) </li>
<li> 2=弹性集群(EKS) </li>
<li> 3= Prometheus管理的弹性集群(MEKS) </li>
        :type KubeType: int
        :param _ClusterId: 集群 ID，可不填
        :type ClusterId: str
        """
        self._InstanceId = None
        self._Kind = None
        self._Content = None
        self._KubeType = None
        self._ClusterId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        self._KubeType = params.get("KubeType")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExporterIntegrationResponse(AbstractModel):
    """CreateExporterIntegration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Names: 返回创建成功的集成名称列表
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


class CreateGrafanaInstanceRequest(AbstractModel):
    """CreateGrafanaInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _VpcId: VPC ID (私有网络 ID)
        :type VpcId: str
        :param _SubnetIds: 子网 ID 数组(VPC ID下的子网 ID，只取第一个)
        :type SubnetIds: list of str
        :param _EnableInternet: 是否启用外网
        :type EnableInternet: bool
        :param _GrafanaInitPassword: Grafana 初始密码(国际站用户必填，国内站用户可不填，不填时会生成随机密码并给主账号发送通知)
        :type GrafanaInitPassword: str
        :param _TagSpecification: 标签
        :type TagSpecification: list of PrometheusTag
        :param _AutoVoucher: 是否自动选择代金券，默认为 false
        :type AutoVoucher: bool
        """
        self._InstanceName = None
        self._VpcId = None
        self._SubnetIds = None
        self._EnableInternet = None
        self._GrafanaInitPassword = None
        self._TagSpecification = None
        self._AutoVoucher = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def EnableInternet(self):
        return self._EnableInternet

    @EnableInternet.setter
    def EnableInternet(self, EnableInternet):
        self._EnableInternet = EnableInternet

    @property
    def GrafanaInitPassword(self):
        return self._GrafanaInitPassword

    @GrafanaInitPassword.setter
    def GrafanaInitPassword(self, GrafanaInitPassword):
        self._GrafanaInitPassword = GrafanaInitPassword

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._EnableInternet = params.get("EnableInternet")
        self._GrafanaInitPassword = params.get("GrafanaInitPassword")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaInstanceResponse(AbstractModel):
    """CreateGrafanaInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateGrafanaIntegrationRequest(AbstractModel):
    """CreateGrafanaIntegration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _Kind: 集成类型(接口DescribeGrafanaIntegrationOverviews返回的集成信息中的Code字段)
        :type Kind: str
        :param _Content: 集成配置
        :type Content: str
        """
        self._InstanceId = None
        self._Kind = None
        self._Content = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaIntegrationResponse(AbstractModel):
    """CreateGrafanaIntegration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntegrationId: 集成 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type IntegrationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntegrationId = None
        self._RequestId = None

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IntegrationId = params.get("IntegrationId")
        self._RequestId = params.get("RequestId")


class CreateGrafanaNotificationChannelRequest(AbstractModel):
    """CreateGrafanaNotificationChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _ChannelName: 告警通道名称，例如：test
        :type ChannelName: str
        :param _Receivers: 接受告警通道 ID 数组，值为告警管理/基础配置/通知模板中的模板 ID 
        :type Receivers: list of str
        :param _OrgId: 默认为1，建议使用 OrganizationIds
        :type OrgId: int
        :param _ExtraOrgIds: 额外组织 ID 数组，已废弃，请使用 OrganizationIds
        :type ExtraOrgIds: list of str
        :param _OrganizationIds: 生效的所有组织 ID 数组，默认为 ["1"]
        :type OrganizationIds: list of str
        """
        self._InstanceId = None
        self._ChannelName = None
        self._Receivers = None
        self._OrgId = None
        self._ExtraOrgIds = None
        self._OrganizationIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def ExtraOrgIds(self):
        return self._ExtraOrgIds

    @ExtraOrgIds.setter
    def ExtraOrgIds(self, ExtraOrgIds):
        self._ExtraOrgIds = ExtraOrgIds

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._OrgId = params.get("OrgId")
        self._ExtraOrgIds = params.get("ExtraOrgIds")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaNotificationChannelResponse(AbstractModel):
    """CreateGrafanaNotificationChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ChannelId = None
        self._RequestId = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._RequestId = params.get("RequestId")


class CreatePolicyGroupCondition(AbstractModel):
    """创建策略传入的阈值告警条件

    """

    def __init__(self):
        r"""
        :param _MetricId: 指标Id
        :type MetricId: int
        :param _AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param _CalcType: 比较类型，1表示大于，2表示大于等于，3表示小于，4表示小于等于，5表示相等，6表示不相等。如果指标有配置默认比较类型值可以不填。
        :type CalcType: int
        :param _CalcValue: 比较的值，如果指标不必须CalcValue可不填
        :type CalcValue: float
        :param _CalcPeriod: 数据聚合周期(单位秒)，若指标有默认值可不填
        :type CalcPeriod: int
        :param _ContinuePeriod: 持续几个检测周期触发规则会告警
        :type ContinuePeriod: int
        :param _RuleId: 如果通过模板创建，需要传入模板中该指标的对应RuleId
        :type RuleId: int
        """
        self._MetricId = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._CalcType = None
        self._CalcValue = None
        self._CalcPeriod = None
        self._ContinuePeriod = None
        self._RuleId = None

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def CalcPeriod(self):
        return self._CalcPeriod

    @CalcPeriod.setter
    def CalcPeriod(self, CalcPeriod):
        self._CalcPeriod = CalcPeriod

    @property
    def ContinuePeriod(self):
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._MetricId = params.get("MetricId")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._CalcType = params.get("CalcType")
        self._CalcValue = params.get("CalcValue")
        self._CalcPeriod = params.get("CalcPeriod")
        self._ContinuePeriod = params.get("ContinuePeriod")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupEventCondition(AbstractModel):
    """创建策略传入的事件告警条件

    """

    def __init__(self):
        r"""
        :param _EventId: 告警事件的Id
        :type EventId: int
        :param _AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param _RuleId: 如果通过模板创建，需要传入模板中该指标的对应RuleId
        :type RuleId: int
        """
        self._EventId = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._RuleId = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupRequest(AbstractModel):
    """CreatePolicyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 组策略名称
        :type GroupName: str
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _ViewName: 策略组所属视图的名称，若通过模板创建，可不传入
        :type ViewName: str
        :param _ProjectId: 策略组所属项目Id，会进行鉴权操作
        :type ProjectId: int
        :param _ConditionTempGroupId: 模板策略组Id, 通过模板创建时才需要传
        :type ConditionTempGroupId: int
        :param _IsShielded: 是否屏蔽策略组，0表示不屏蔽，1表示屏蔽。不填默认为0
        :type IsShielded: int
        :param _Remark: 策略组的备注信息
        :type Remark: str
        :param _InsertTime: 插入时间，戳格式为Unix时间戳，不填则按后台处理时间填充
        :type InsertTime: int
        :param _Conditions: 策略组中的阈值告警规则
        :type Conditions: list of CreatePolicyGroupCondition
        :param _EventConditions: 策略组中的事件告警规则
        :type EventConditions: list of CreatePolicyGroupEventCondition
        :param _BackEndCall: 是否为后端调用。当且仅当值为1时，后台拉取策略模板中的规则填充入Conditions以及EventConditions字段
        :type BackEndCall: int
        :param _IsUnionRule: 指标告警规则的且或关系，0表示或规则(满足任意规则就告警)，1表示且规则(满足所有规则才告警)
        :type IsUnionRule: int
        """
        self._GroupName = None
        self._Module = None
        self._ViewName = None
        self._ProjectId = None
        self._ConditionTempGroupId = None
        self._IsShielded = None
        self._Remark = None
        self._InsertTime = None
        self._Conditions = None
        self._EventConditions = None
        self._BackEndCall = None
        self._IsUnionRule = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ConditionTempGroupId(self):
        return self._ConditionTempGroupId

    @ConditionTempGroupId.setter
    def ConditionTempGroupId(self, ConditionTempGroupId):
        self._ConditionTempGroupId = ConditionTempGroupId

    @property
    def IsShielded(self):
        return self._IsShielded

    @IsShielded.setter
    def IsShielded(self, IsShielded):
        self._IsShielded = IsShielded

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def EventConditions(self):
        return self._EventConditions

    @EventConditions.setter
    def EventConditions(self, EventConditions):
        self._EventConditions = EventConditions

    @property
    def BackEndCall(self):
        return self._BackEndCall

    @BackEndCall.setter
    def BackEndCall(self, BackEndCall):
        self._BackEndCall = BackEndCall

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Module = params.get("Module")
        self._ViewName = params.get("ViewName")
        self._ProjectId = params.get("ProjectId")
        self._ConditionTempGroupId = params.get("ConditionTempGroupId")
        self._IsShielded = params.get("IsShielded")
        self._Remark = params.get("Remark")
        self._InsertTime = params.get("InsertTime")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = CreatePolicyGroupCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self._EventConditions = []
            for item in params.get("EventConditions"):
                obj = CreatePolicyGroupEventCondition()
                obj._deserialize(item)
                self._EventConditions.append(obj)
        self._BackEndCall = params.get("BackEndCall")
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupResponse(AbstractModel):
    """CreatePolicyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 创建成功的策略组Id
        :type GroupId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreatePrometheusAgentRequest(AbstractModel):
    """CreatePrometheusAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Name: Agent 名称
        :type Name: str
        """
        self._InstanceId = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAgentResponse(AbstractModel):
    """CreatePrometheusAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: 创建成功的 Agent Id
        :type AgentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._RequestId = None

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._RequestId = params.get("RequestId")


class CreatePrometheusAlertGroupRequest(AbstractModel):
    """CreatePrometheusAlertGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: prometheus实例ID
        :type InstanceId: str
        :param _GroupName: 告警分组名称，不能与其他告警分组重名
        :type GroupName: str
        :param _GroupState: 告警分组状态：
2 -- 启用
3 -- 禁用
不为空时会覆盖 `Rules`字段下所有告警规则状态

        :type GroupState: int
        :param _AMPReceivers: 云监控告警通知模板ID列表，形如Consumer-xxxx或notice-xxxx
        :type AMPReceivers: list of str
        :param _CustomReceiver: 自定义告警通知模板
        :type CustomReceiver: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertCustomReceiver`
        :param _RepeatInterval: 告警通知周期（收敛时间），为空默认1h
        :type RepeatInterval: str
        :param _Rules: 要创建的告警规则列表
        :type Rules: list of PrometheusAlertGroupRuleSet
        """
        self._InstanceId = None
        self._GroupName = None
        self._GroupState = None
        self._AMPReceivers = None
        self._CustomReceiver = None
        self._RepeatInterval = None
        self._Rules = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupState(self):
        return self._GroupState

    @GroupState.setter
    def GroupState(self, GroupState):
        self._GroupState = GroupState

    @property
    def AMPReceivers(self):
        return self._AMPReceivers

    @AMPReceivers.setter
    def AMPReceivers(self, AMPReceivers):
        self._AMPReceivers = AMPReceivers

    @property
    def CustomReceiver(self):
        return self._CustomReceiver

    @CustomReceiver.setter
    def CustomReceiver(self, CustomReceiver):
        self._CustomReceiver = CustomReceiver

    @property
    def RepeatInterval(self):
        return self._RepeatInterval

    @RepeatInterval.setter
    def RepeatInterval(self, RepeatInterval):
        self._RepeatInterval = RepeatInterval

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupName = params.get("GroupName")
        self._GroupState = params.get("GroupState")
        self._AMPReceivers = params.get("AMPReceivers")
        if params.get("CustomReceiver") is not None:
            self._CustomReceiver = PrometheusAlertCustomReceiver()
            self._CustomReceiver._deserialize(params.get("CustomReceiver"))
        self._RepeatInterval = params.get("RepeatInterval")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertGroupRuleSet()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAlertGroupResponse(AbstractModel):
    """CreatePrometheusAlertGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 创建的告警分组ID，满足正则表达式`alert-[a-z0-9]{8}`
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreatePrometheusAlertPolicyRequest(AbstractModel):
    """CreatePrometheusAlertPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _AlertRule: 告警配置
        :type AlertRule: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertPolicyItem`
        """
        self._InstanceId = None
        self._AlertRule = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertRule(self):
        return self._AlertRule

    @AlertRule.setter
    def AlertRule(self, AlertRule):
        self._AlertRule = AlertRule


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self._AlertRule = PrometheusAlertPolicyItem()
            self._AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAlertPolicyResponse(AbstractModel):
    """CreatePrometheusAlertPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 告警id
        :type Id: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreatePrometheusClusterAgentRequest(AbstractModel):
    """CreatePrometheusClusterAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Agents: agent列表
        :type Agents: list of PrometheusClusterAgentBasic
        """
        self._InstanceId = None
        self._Agents = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Agents(self):
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = PrometheusClusterAgentBasic()
                obj._deserialize(item)
                self._Agents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusClusterAgentResponse(AbstractModel):
    """CreatePrometheusClusterAgent返回参数结构体

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


class CreatePrometheusConfigRequest(AbstractModel):
    """CreatePrometheusConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ClusterType: 集群类型
        :type ClusterType: str
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ServiceMonitors: ServiceMonitors配置
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: PodMonitors配置
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: prometheus原生Job配置
        :type RawJobs: list of PrometheusConfigItem
        """
        self._InstanceId = None
        self._ClusterType = None
        self._ClusterId = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusConfigResponse(AbstractModel):
    """CreatePrometheusConfig返回参数结构体

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


class CreatePrometheusGlobalNotificationRequest(AbstractModel):
    """CreatePrometheusGlobalNotification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID(可通过 DescribePrometheusInstances 接口获取)
        :type InstanceId: str
        :param _Notification: 告警通知渠道
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        """
        self._InstanceId = None
        self._Notification = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotificationItem()
            self._Notification._deserialize(params.get("Notification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusGlobalNotificationResponse(AbstractModel):
    """CreatePrometheusGlobalNotification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 全局告警通知渠道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreatePrometheusMultiTenantInstancePostPayModeRequest(AbstractModel):
    """CreatePrometheusMultiTenantInstancePostPayMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _VpcId: VPC ID(可通过 vpc:DescribeVpcs 接口获取，与实例同地域)
        :type VpcId: str
        :param _SubnetId: 子网 ID(可通过 vpc:DescribeSubnets 接口获取)
        :type SubnetId: str
        :param _DataRetentionTime: 数据存储时间（单位天），限制值为15, 30, 45, 90, 180, 365, 730之一
        :type DataRetentionTime: int
        :param _Zone: 可用区(与子网同可用区)
        :type Zone: str
        :param _TagSpecification: 实例的标签
        :type TagSpecification: list of PrometheusTag
        :param _GrafanaInstanceId: 需要关联的 Grafana 实例
        :type GrafanaInstanceId: str
        """
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._DataRetentionTime = None
        self._Zone = None
        self._TagSpecification = None
        self._GrafanaInstanceId = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

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
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def GrafanaInstanceId(self):
        return self._GrafanaInstanceId

    @GrafanaInstanceId.setter
    def GrafanaInstanceId(self, GrafanaInstanceId):
        self._GrafanaInstanceId = GrafanaInstanceId


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DataRetentionTime = params.get("DataRetentionTime")
        self._Zone = params.get("Zone")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._GrafanaInstanceId = params.get("GrafanaInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusMultiTenantInstancePostPayModeResponse(AbstractModel):
    """CreatePrometheusMultiTenantInstancePostPayMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreatePrometheusRecordRuleYamlRequest(AbstractModel):
    """CreatePrometheusRecordRuleYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Content: yaml的内容
        :type Content: str
        :param _Name: 规则名称
        :type Name: str
        """
        self._InstanceId = None
        self._Content = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Content = params.get("Content")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusRecordRuleYamlResponse(AbstractModel):
    """CreatePrometheusRecordRuleYaml返回参数结构体

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


class CreatePrometheusScrapeJobRequest(AbstractModel):
    """CreatePrometheusScrapeJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _AgentId: Agent ID(可通过DescribePrometheusAgents 接口获取)
        :type AgentId: str
        :param _Config: 抓取任务配置
        :type Config: str
        """
        self._InstanceId = None
        self._AgentId = None
        self._Config = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusScrapeJobResponse(AbstractModel):
    """CreatePrometheusScrapeJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 成功创建抓取任务 Id
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreatePrometheusTempRequest(AbstractModel):
    """CreatePrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 模板设置
        :type Template: :class:`tencentcloud.monitor.v20180724.models.PrometheusTemp`
        """
        self._Template = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = PrometheusTemp()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusTempResponse(AbstractModel):
    """CreatePrometheusTemp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板Id
        :type TemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateRecordingRuleRequest(AbstractModel):
    """CreateRecordingRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 聚合规则名称
        :type Name: str
        :param _Group: 聚合规则组内容，格式为 yaml，通过 base64 进行编码。
        :type Group: str
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _RuleState: 规则状态码，取值如下：
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
默认状态码为 2 启用。
        :type RuleState: int
        """
        self._Name = None
        self._Group = None
        self._InstanceId = None
        self._RuleState = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Group = params.get("Group")
        self._InstanceId = params.get("InstanceId")
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordingRuleResponse(AbstractModel):
    """CreateRecordingRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateSSOAccountRequest(AbstractModel):
    """CreateSSOAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _UserId: 用户账号 ID ，例如：10000000
        :type UserId: str
        :param _Role: 权限(只取数组中的第一个，其中 Organization 暂未使用，可不填)
        :type Role: list of GrafanaAccountRole
        :param _Notes: 备注
        :type Notes: str
        """
        self._InstanceId = None
        self._UserId = None
        self._Role = None
        self._Notes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        if params.get("Role") is not None:
            self._Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self._Role.append(obj)
        self._Notes = params.get("Notes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSSOAccountResponse(AbstractModel):
    """CreateSSOAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 已添加的用户 UIN
        :type UserId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class CreateServiceDiscoveryRequest(AbstractModel):
    """CreateServiceDiscovery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _KubeClusterId: <li>类型为TKE：对应集成的腾讯云容器服务集群 ID</li>
        :type KubeClusterId: str
        :param _KubeType: 用户 Kubernetes 集群类型：
<li> 1 = 容器服务集群(TKE) </li>
        :type KubeType: int
        :param _Type: 服务发现类型，取值如下：
<li> 1 = ServiceMonitor</li>
<li> 2 = PodMonitor</li>
<li> 3 = JobMonitor</li>
        :type Type: int
        :param _Yaml: 服务发现配置信息，YAML 格式，[具体YAML参数内容请参考](https://cloud.tencent.com/document/product/1416/55995#service-monitor)
        :type Yaml: str
        """
        self._InstanceId = None
        self._KubeClusterId = None
        self._KubeType = None
        self._Type = None
        self._Yaml = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeClusterId(self):
        return self._KubeClusterId

    @KubeClusterId.setter
    def KubeClusterId(self, KubeClusterId):
        self._KubeClusterId = KubeClusterId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeClusterId = params.get("KubeClusterId")
        self._KubeType = params.get("KubeType")
        self._Type = params.get("Type")
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceDiscoveryResponse(AbstractModel):
    """CreateServiceDiscovery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceDiscovery: 创建成功之后，返回对应服务发现信息
        :type ServiceDiscovery: :class:`tencentcloud.monitor.v20180724.models.ServiceDiscoveryItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceDiscovery = None
        self._RequestId = None

    @property
    def ServiceDiscovery(self):
        return self._ServiceDiscovery

    @ServiceDiscovery.setter
    def ServiceDiscovery(self, ServiceDiscovery):
        self._ServiceDiscovery = ServiceDiscovery

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceDiscovery") is not None:
            self._ServiceDiscovery = ServiceDiscoveryItem()
            self._ServiceDiscovery._deserialize(params.get("ServiceDiscovery"))
        self._RequestId = params.get("RequestId")


class DataPoint(AbstractModel):
    """监控数据点

    """

    def __init__(self):
        r"""
        :param _Dimensions: 实例对象维度组合
        :type Dimensions: list of Dimension
        :param _Timestamps: 时间戳数组，表示那些时间点有数据，缺失的时间戳，没有数据点，可以理解为掉点了
        :type Timestamps: list of float
        :param _Values: 监控值数组，该数组和Timestamps一一对应
        :type Values: list of float
        :param _MaxValues: 监控值数组，该数组和Timestamps一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxValues: list of float
        :param _MinValues: 监控值数组，该数组和Timestamps一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type MinValues: list of float
        :param _AvgValues: 监控值数组，该数组和Timestamps一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgValues: list of float
        """
        self._Dimensions = None
        self._Timestamps = None
        self._Values = None
        self._MaxValues = None
        self._MinValues = None
        self._AvgValues = None

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Timestamps(self):
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def MaxValues(self):
        return self._MaxValues

    @MaxValues.setter
    def MaxValues(self, MaxValues):
        self._MaxValues = MaxValues

    @property
    def MinValues(self):
        return self._MinValues

    @MinValues.setter
    def MinValues(self, MinValues):
        self._MinValues = MinValues

    @property
    def AvgValues(self):
        return self._AvgValues

    @AvgValues.setter
    def AvgValues(self, AvgValues):
        self._AvgValues = AvgValues


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        self._MaxValues = params.get("MaxValues")
        self._MinValues = params.get("MinValues")
        self._AvgValues = params.get("AvgValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticesRequest(AbstractModel):
    """DeleteAlarmNotices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”
        :type Module: str
        :param _NoticeIds: 告警通知模板id列表
        :type NoticeIds: list of str
        :param _NoticeBindPolicys: 通知模板与策略绑定关系
        :type NoticeBindPolicys: list of NoticeBindPolicys
        """
        self._Module = None
        self._NoticeIds = None
        self._NoticeBindPolicys = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def NoticeBindPolicys(self):
        return self._NoticeBindPolicys

    @NoticeBindPolicys.setter
    def NoticeBindPolicys(self, NoticeBindPolicys):
        self._NoticeBindPolicys = NoticeBindPolicys


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._NoticeIds = params.get("NoticeIds")
        if params.get("NoticeBindPolicys") is not None:
            self._NoticeBindPolicys = []
            for item in params.get("NoticeBindPolicys"):
                obj = NoticeBindPolicys()
                obj._deserialize(item)
                self._NoticeBindPolicys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticesResponse(AbstractModel):
    """DeleteAlarmNotices返回参数结构体

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


class DeleteAlarmPolicyRequest(AbstractModel):
    """DeleteAlarmPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定值 monitor
        :type Module: str
        :param _PolicyIds: 告警策略 ID 列表
        :type PolicyIds: list of str
        :param _PromInsIds: prom的实例id
        :type PromInsIds: list of str
        """
        self._Module = None
        self._PolicyIds = None
        self._PromInsIds = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def PromInsIds(self):
        return self._PromInsIds

    @PromInsIds.setter
    def PromInsIds(self, PromInsIds):
        self._PromInsIds = PromInsIds


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyIds = params.get("PolicyIds")
        self._PromInsIds = params.get("PromInsIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmPolicyResponse(AbstractModel):
    """DeleteAlarmPolicy返回参数结构体

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


class DeleteAlertRulesRequest(AbstractModel):
    """DeleteAlertRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIds: 规则 ID 列表
        :type RuleIds: list of str
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        """
        self._RuleIds = None
        self._InstanceId = None

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlertRulesResponse(AbstractModel):
    """DeleteAlertRules返回参数结构体

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


class DeleteExporterIntegrationRequest(AbstractModel):
    """DeleteExporterIntegration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Kind: 类型(可通过 DescribeExporterIntegrations获取)
        :type Kind: str
        :param _Name: 名字
        :type Name: str
        :param _KubeType: Kubernetes 集群类型，取值如下：
<li> 1= 容器集群(TKE) </li>
<li> 2=弹性集群(EKS) </li>
<li> 3= Prometheus管理的弹性集群(MEKS) </li>
        :type KubeType: int
        :param _ClusterId: 集群 ID，可不填
        :type ClusterId: str
        """
        self._InstanceId = None
        self._Kind = None
        self._Name = None
        self._KubeType = None
        self._ClusterId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        self._KubeType = params.get("KubeType")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExporterIntegrationResponse(AbstractModel):
    """DeleteExporterIntegration返回参数结构体

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


class DeleteGrafanaInstanceRequest(AbstractModel):
    """DeleteGrafanaInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIDs: 实例ID数组
        :type InstanceIDs: list of str
        """
        self._InstanceIDs = None

    @property
    def InstanceIDs(self):
        return self._InstanceIDs

    @InstanceIDs.setter
    def InstanceIDs(self, InstanceIDs):
        self._InstanceIDs = InstanceIDs


    def _deserialize(self, params):
        self._InstanceIDs = params.get("InstanceIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaInstanceResponse(AbstractModel):
    """DeleteGrafanaInstance返回参数结构体

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


class DeleteGrafanaIntegrationRequest(AbstractModel):
    """DeleteGrafanaIntegration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
        :type InstanceId: str
        :param _IntegrationId: 集成 ID，可在实例详情-云产品集成-集成列表查看。例如：integration-abcd1234
        :type IntegrationId: str
        """
        self._InstanceId = None
        self._IntegrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IntegrationId = params.get("IntegrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaIntegrationResponse(AbstractModel):
    """DeleteGrafanaIntegration返回参数结构体

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


class DeleteGrafanaNotificationChannelRequest(AbstractModel):
    """DeleteGrafanaNotificationChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelIDs: 通道 ID 数组。例如：nchannel-abcd1234，通过 DescribeGrafanaChannels 获取
        :type ChannelIDs: list of str
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        """
        self._ChannelIDs = None
        self._InstanceId = None

    @property
    def ChannelIDs(self):
        return self._ChannelIDs

    @ChannelIDs.setter
    def ChannelIDs(self, ChannelIDs):
        self._ChannelIDs = ChannelIDs

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ChannelIDs = params.get("ChannelIDs")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaNotificationChannelResponse(AbstractModel):
    """DeleteGrafanaNotificationChannel返回参数结构体

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


class DeletePolicyGroupRequest(AbstractModel):
    """DeletePolicyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _GroupId: 策略组id,即1.0的告警策略id,可以从策略详情获取
        :type GroupId: list of int
        """
        self._Module = None
        self._GroupId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyGroupResponse(AbstractModel):
    """DeletePolicyGroup返回参数结构体

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


class DeletePrometheusAlertGroupsRequest(AbstractModel):
    """DeletePrometheusAlertGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: prometheus实例id
        :type InstanceId: str
        :param _GroupIds: 需要删除的告警分组ID，形如alert-xxxxx
        :type GroupIds: list of str
        """
        self._InstanceId = None
        self._GroupIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusAlertGroupsResponse(AbstractModel):
    """DeletePrometheusAlertGroups返回参数结构体

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


class DeletePrometheusAlertPolicyRequest(AbstractModel):
    """DeletePrometheusAlertPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID(可通过 DescribePrometheusInstances 接口获取)
        :type InstanceId: str
        :param _AlertIds: 告警策略ID列表(可通过 DescribePrometheusAlertPolicy 接口获取)
        :type AlertIds: list of str
        :param _Names: 告警策略名称(可通过 DescribePrometheusAlertPolicy 接口获取)，名称完全相同的告警策略才会删除
        :type Names: list of str
        """
        self._InstanceId = None
        self._AlertIds = None
        self._Names = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertIds(self):
        return self._AlertIds

    @AlertIds.setter
    def AlertIds(self, AlertIds):
        self._AlertIds = AlertIds

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AlertIds = params.get("AlertIds")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusAlertPolicyResponse(AbstractModel):
    """DeletePrometheusAlertPolicy返回参数结构体

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


class DeletePrometheusClusterAgentRequest(AbstractModel):
    """DeletePrometheusClusterAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agents: agent列表
        :type Agents: list of PrometheusAgentInfo
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._Agents = None
        self._InstanceId = None

    @property
    def Agents(self):
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = PrometheusAgentInfo()
                obj._deserialize(item)
                self._Agents.append(obj)
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusClusterAgentResponse(AbstractModel):
    """DeletePrometheusClusterAgent返回参数结构体

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


class DeletePrometheusConfigRequest(AbstractModel):
    """DeletePrometheusConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ClusterType: 集群类型
        :type ClusterType: str
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ServiceMonitors: 要删除的ServiceMonitor名字列表
        :type ServiceMonitors: list of str
        :param _PodMonitors: 要删除的PodMonitor名字列表
        :type PodMonitors: list of str
        :param _RawJobs: 要删除的RawJobs名字列表
        :type RawJobs: list of str
        """
        self._InstanceId = None
        self._ClusterType = None
        self._ClusterId = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._ServiceMonitors = params.get("ServiceMonitors")
        self._PodMonitors = params.get("PodMonitors")
        self._RawJobs = params.get("RawJobs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusConfigResponse(AbstractModel):
    """DeletePrometheusConfig返回参数结构体

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


class DeletePrometheusRecordRuleYamlRequest(AbstractModel):
    """DeletePrometheusRecordRuleYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Names: 聚合规则列表
        :type Names: list of str
        """
        self._InstanceId = None
        self._Names = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusRecordRuleYamlResponse(AbstractModel):
    """DeletePrometheusRecordRuleYaml返回参数结构体

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


class DeletePrometheusScrapeJobsRequest(AbstractModel):
    """DeletePrometheusScrapeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _AgentId: Agent ID(可通过 DescribePrometheusAgents 接口获取)
        :type AgentId: str
        :param _JobIds: 任务 ID 列表(可通过 DescribePrometheusScrapeJobs 接口获取)
        :type JobIds: list of str
        """
        self._InstanceId = None
        self._AgentId = None
        self._JobIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        self._JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusScrapeJobsResponse(AbstractModel):
    """DeletePrometheusScrapeJobs返回参数结构体

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


class DeletePrometheusTempRequest(AbstractModel):
    """DeletePrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
        :type TemplateId: str
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
        


class DeletePrometheusTempResponse(AbstractModel):
    """DeletePrometheusTemp返回参数结构体

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


class DeletePrometheusTempSyncRequest(AbstractModel):
    """DeletePrometheusTempSync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
        :type TemplateId: str
        :param _Targets: 取消同步的对象列表
        :type Targets: list of PrometheusTemplateSyncTarget
        """
        self._TemplateId = None
        self._Targets = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTempSyncResponse(AbstractModel):
    """DeletePrometheusTempSync返回参数结构体

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


class DeleteRecordingRulesRequest(AbstractModel):
    """DeleteRecordingRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIds: 规则 ID 列表(规则 ID 可通过 DescribeRecordingRules 接口获取)
        :type RuleIds: list of str
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        """
        self._RuleIds = None
        self._InstanceId = None

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordingRulesResponse(AbstractModel):
    """DeleteRecordingRules返回参数结构体

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


class DeleteSSOAccountRequest(AbstractModel):
    """DeleteSSOAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _UserId: 用户账号 ID ，例如：10000000
        :type UserId: str
        """
        self._InstanceId = None
        self._UserId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSSOAccountResponse(AbstractModel):
    """DeleteSSOAccount返回参数结构体

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


class DeleteServiceDiscoveryRequest(AbstractModel):
    """DeleteServiceDiscovery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID，例如：prom-sdfk2342a
        :type InstanceId: str
        :param _KubeClusterId: <li>类型是 TKE，为对应的腾讯云容器服务集群 ID</li>
        :type KubeClusterId: str
        :param _KubeType: 用户 Kubernetes 集群类型：
<li> 1 = 容器服务集群(TKE) </li>
        :type KubeType: int
        :param _Type: 服务发现类型，取值如下：
<li> 1 = ServiceMonitor</li>
<li> 2 = PodMonitor</li>
<li> 3 = PodMonitor</li>
        :type Type: int
        :param _Yaml: 服务发现配置信息，YAML 格式，[具体YAML参数内容请参考](https://cloud.tencent.com/document/product/1416/55995#service-monitor)
        :type Yaml: str
        """
        self._InstanceId = None
        self._KubeClusterId = None
        self._KubeType = None
        self._Type = None
        self._Yaml = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeClusterId(self):
        return self._KubeClusterId

    @KubeClusterId.setter
    def KubeClusterId(self, KubeClusterId):
        self._KubeClusterId = KubeClusterId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeClusterId = params.get("KubeClusterId")
        self._KubeType = params.get("KubeType")
        self._Type = params.get("Type")
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceDiscoveryResponse(AbstractModel):
    """DeleteServiceDiscovery返回参数结构体

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


class DescribeAccidentEventListAlarms(AbstractModel):
    """DescribeAccidentEventList接口的出参类型

    """

    def __init__(self):
        r"""
        :param _BusinessTypeDesc: 事件分类
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessTypeDesc: str
        :param _AccidentTypeDesc: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AccidentTypeDesc: str
        :param _BusinessID: 事件分类的ID，1表示服务问题，2表示其他订阅
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessID: int
        :param _EventStatus: 事件状态的ID，0表示已恢复，1表示未恢复
注意：此字段可能返回 null，表示取不到有效值。
        :type EventStatus: int
        :param _AffectResource: 影响的对象
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectResource: str
        :param _Region: 事件的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _OccurTime: 事件发生的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OccurTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._BusinessTypeDesc = None
        self._AccidentTypeDesc = None
        self._BusinessID = None
        self._EventStatus = None
        self._AffectResource = None
        self._Region = None
        self._OccurTime = None
        self._UpdateTime = None

    @property
    def BusinessTypeDesc(self):
        return self._BusinessTypeDesc

    @BusinessTypeDesc.setter
    def BusinessTypeDesc(self, BusinessTypeDesc):
        self._BusinessTypeDesc = BusinessTypeDesc

    @property
    def AccidentTypeDesc(self):
        return self._AccidentTypeDesc

    @AccidentTypeDesc.setter
    def AccidentTypeDesc(self, AccidentTypeDesc):
        self._AccidentTypeDesc = AccidentTypeDesc

    @property
    def BusinessID(self):
        return self._BusinessID

    @BusinessID.setter
    def BusinessID(self, BusinessID):
        self._BusinessID = BusinessID

    @property
    def EventStatus(self):
        return self._EventStatus

    @EventStatus.setter
    def EventStatus(self, EventStatus):
        self._EventStatus = EventStatus

    @property
    def AffectResource(self):
        return self._AffectResource

    @AffectResource.setter
    def AffectResource(self, AffectResource):
        self._AffectResource = AffectResource

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def OccurTime(self):
        return self._OccurTime

    @OccurTime.setter
    def OccurTime(self, OccurTime):
        self._OccurTime = OccurTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._BusinessTypeDesc = params.get("BusinessTypeDesc")
        self._AccidentTypeDesc = params.get("AccidentTypeDesc")
        self._BusinessID = params.get("BusinessID")
        self._EventStatus = params.get("EventStatus")
        self._AffectResource = params.get("AffectResource")
        self._Region = params.get("Region")
        self._OccurTime = params.get("OccurTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccidentEventListRequest(AbstractModel):
    """DescribeAccidentEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 接口模块名，当前接口取值monitor
        :type Module: str
        :param _StartTime: 起始时间，默认一天前的时间戳
        :type StartTime: int
        :param _EndTime: 结束时间，默认当前时间戳
        :type EndTime: int
        :param _Limit: 分页参数，每页返回的数量，取值1~100，默认20
        :type Limit: int
        :param _Offset: 分页参数，页偏移量，从0开始计数，默认0
        :type Offset: int
        :param _UpdateTimeOrder: 根据UpdateTime排序的规则，取值asc或desc
        :type UpdateTimeOrder: str
        :param _OccurTimeOrder: 根据OccurTime排序的规则，取值asc或desc（优先根据UpdateTimeOrder排序）
        :type OccurTimeOrder: str
        :param _AccidentType: 根据事件类型过滤，1表示服务问题，2表示其他订阅
        :type AccidentType: list of int
        :param _AccidentEvent: 根据事件过滤，1表示云服务器存储问题，2表示云服务器网络连接问题，3表示云服务器运行异常，202表示运营商网络抖动
        :type AccidentEvent: list of int
        :param _AccidentStatus: 根据事件状态过滤，0表示已恢复，1表示未恢复
        :type AccidentStatus: list of int
        :param _AccidentRegion: 根据事件地域过滤，gz表示广州，sh表示上海等
        :type AccidentRegion: list of str
        :param _AffectResource: 根据影响资源过滤，比如ins-19a06bka
        :type AffectResource: str
        """
        self._Module = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._UpdateTimeOrder = None
        self._OccurTimeOrder = None
        self._AccidentType = None
        self._AccidentEvent = None
        self._AccidentStatus = None
        self._AccidentRegion = None
        self._AffectResource = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

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
    def UpdateTimeOrder(self):
        return self._UpdateTimeOrder

    @UpdateTimeOrder.setter
    def UpdateTimeOrder(self, UpdateTimeOrder):
        self._UpdateTimeOrder = UpdateTimeOrder

    @property
    def OccurTimeOrder(self):
        return self._OccurTimeOrder

    @OccurTimeOrder.setter
    def OccurTimeOrder(self, OccurTimeOrder):
        self._OccurTimeOrder = OccurTimeOrder

    @property
    def AccidentType(self):
        return self._AccidentType

    @AccidentType.setter
    def AccidentType(self, AccidentType):
        self._AccidentType = AccidentType

    @property
    def AccidentEvent(self):
        return self._AccidentEvent

    @AccidentEvent.setter
    def AccidentEvent(self, AccidentEvent):
        self._AccidentEvent = AccidentEvent

    @property
    def AccidentStatus(self):
        return self._AccidentStatus

    @AccidentStatus.setter
    def AccidentStatus(self, AccidentStatus):
        self._AccidentStatus = AccidentStatus

    @property
    def AccidentRegion(self):
        return self._AccidentRegion

    @AccidentRegion.setter
    def AccidentRegion(self, AccidentRegion):
        self._AccidentRegion = AccidentRegion

    @property
    def AffectResource(self):
        return self._AffectResource

    @AffectResource.setter
    def AffectResource(self, AffectResource):
        self._AffectResource = AffectResource


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._UpdateTimeOrder = params.get("UpdateTimeOrder")
        self._OccurTimeOrder = params.get("OccurTimeOrder")
        self._AccidentType = params.get("AccidentType")
        self._AccidentEvent = params.get("AccidentEvent")
        self._AccidentStatus = params.get("AccidentStatus")
        self._AccidentRegion = params.get("AccidentRegion")
        self._AffectResource = params.get("AffectResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccidentEventListResponse(AbstractModel):
    """DescribeAccidentEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Alarms: 平台事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Alarms: list of DescribeAccidentEventListAlarms
        :param _Total: 平台事件的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Alarms = None
        self._Total = None
        self._RequestId = None

    @property
    def Alarms(self):
        return self._Alarms

    @Alarms.setter
    def Alarms(self, Alarms):
        self._Alarms = Alarms

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
        if params.get("Alarms") is not None:
            self._Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeAccidentEventListAlarms()
                obj._deserialize(item)
                self._Alarms.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAlarmEventsRequest(AbstractModel):
    """DescribeAlarmEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定值 monitor
        :type Module: str
        :param _Namespace: 告警策略类型，由 DescribeAllNamespaces 获得，例如 cvm_device
        :type Namespace: str
        :param _MonitorType: 监控类型，如 MT_QCE。如果不填默认为 MT_QCE。
        :type MonitorType: str
        """
        self._Module = None
        self._Namespace = None
        self._MonitorType = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Namespace = params.get("Namespace")
        self._MonitorType = params.get("MonitorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmEventsResponse(AbstractModel):
    """DescribeAlarmEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 告警事件列表
        :type Events: list of AlarmEvent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

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
                obj = AlarmEvent()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmHistoriesRequest(AbstractModel):
    """DescribeAlarmHistories请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _PageNumber: 页数，从 1 开始计数，默认 1
        :type PageNumber: int
        :param _PageSize: 每页的数量，取值1~100，默认20
        :type PageSize: int
        :param _Order: 默认按首次出现时间倒序排列 "ASC"=正序 "DESC"=逆序
        :type Order: str
        :param _StartTime: 起始时间，默认一天前的时间戳。对应 `FirstOccurTime` 告警首次出现时间，告警历史的 `FirstOccurTime` 晚于 `StartTime` 才可能被搜索到。
        :type StartTime: int
        :param _EndTime: 结束时间，默认当前时间戳。对应 `FirstOccurTime` 告警首次出现时间，告警历史的 `FirstOccurTime` 早于 `EndTime` 才可能被搜索到。
        :type EndTime: int
        :param _MonitorTypes: 根据监控类型过滤，不选默认查所有类型。"MT_QCE"=云产品监控，支持的枚举值有："MT_QCE"=云产品监控；"MT_TAW"=应用性能监控；"MT_RUM"=前端性能监控；"MT_PROBE"=云拨测，"MT_TRTC"=实时音视频，
"MT_RUMAPP"=终端性能监控
        :type MonitorTypes: list of str
        :param _AlarmObject: 根据告警对象过滤 字符串模糊搜索
        :type AlarmObject: str
        :param _AlarmStatus: 根据告警状态过滤 ALARM=未恢复 OK=已恢复 NO_CONF=已失效 NO_DATA=数据不足，不选默认查所有
        :type AlarmStatus: list of str
        :param _ProjectIds: 根据项目ID过滤，-1=无项目 0=默认项目
可在此页面查询 [项目管理](https://console.cloud.tencent.com/project)
        :type ProjectIds: list of int
        :param _InstanceGroupIds: 根据实例组ID过滤
        :type InstanceGroupIds: list of int
        :param _Namespaces: 根据策略类型过滤，策略类型是监控类型之下的概念，在这里两者都需要传入，例如 `[{"MonitorType": "MT_QCE", "Namespace": "cvm_device"}]`
可使用 [查询所有名字空间 DescribeAllNamespaces](https://cloud.tencent.com/document/product/248/48683) 接口查询
        :type Namespaces: list of MonitorTypeNamespace
        :param _MetricNames: 根据指标名过滤
        :type MetricNames: list of str
        :param _PolicyName: 根据策略名称模糊搜索,不支持大小写区分
        :type PolicyName: str
        :param _Content: 根据告警内容模糊搜索
        :type Content: str
        :param _ReceiverUids: 根据接收人搜索，可以使用“访问管理”的 [拉取子用户 ListUsers](https://cloud.tencent.com/document/product/598/34587) 接口获取用户列表 或 [查询子用户 GetUser](https://cloud.tencent.com/document/product/598/34590) 接口查询子用户详情，此处填入返回结果中的 `Uid` 字段
        :type ReceiverUids: list of int
        :param _ReceiverGroups: 根据接收组搜索，可以使用“访问管理”的 [查询用户组列表 ListGroups](https://cloud.tencent.com/document/product/598/34589) 接口获取用户组列表 或 [列出用户关联的用户组 ListGroupsForUser](https://cloud.tencent.com/document/product/598/34588) 查询某个子用户所在的用户组列表 ，此处填入返回结果中的 `GroupId ` 字段
        :type ReceiverGroups: list of int
        :param _PolicyIds: 根据告警策略 Id 列表搜索
        :type PolicyIds: list of str
        :param _AlarmLevels: 告警等级,取值范围：Remind、Serious、Warn
        :type AlarmLevels: list of str
        :param _ConvergenceHistoryIDs: 收敛历史的唯一id
        :type ConvergenceHistoryIDs: list of str
        :param _AlarmTypes: 告警类型
        :type AlarmTypes: list of str
        """
        self._Module = None
        self._PageNumber = None
        self._PageSize = None
        self._Order = None
        self._StartTime = None
        self._EndTime = None
        self._MonitorTypes = None
        self._AlarmObject = None
        self._AlarmStatus = None
        self._ProjectIds = None
        self._InstanceGroupIds = None
        self._Namespaces = None
        self._MetricNames = None
        self._PolicyName = None
        self._Content = None
        self._ReceiverUids = None
        self._ReceiverGroups = None
        self._PolicyIds = None
        self._AlarmLevels = None
        self._ConvergenceHistoryIDs = None
        self._AlarmTypes = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

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
    def MonitorTypes(self):
        return self._MonitorTypes

    @MonitorTypes.setter
    def MonitorTypes(self, MonitorTypes):
        self._MonitorTypes = MonitorTypes

    @property
    def AlarmObject(self):
        return self._AlarmObject

    @AlarmObject.setter
    def AlarmObject(self, AlarmObject):
        self._AlarmObject = AlarmObject

    @property
    def AlarmStatus(self):
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def InstanceGroupIds(self):
        return self._InstanceGroupIds

    @InstanceGroupIds.setter
    def InstanceGroupIds(self, InstanceGroupIds):
        self._InstanceGroupIds = InstanceGroupIds

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReceiverUids(self):
        return self._ReceiverUids

    @ReceiverUids.setter
    def ReceiverUids(self, ReceiverUids):
        self._ReceiverUids = ReceiverUids

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def AlarmLevels(self):
        return self._AlarmLevels

    @AlarmLevels.setter
    def AlarmLevels(self, AlarmLevels):
        self._AlarmLevels = AlarmLevels

    @property
    def ConvergenceHistoryIDs(self):
        return self._ConvergenceHistoryIDs

    @ConvergenceHistoryIDs.setter
    def ConvergenceHistoryIDs(self, ConvergenceHistoryIDs):
        self._ConvergenceHistoryIDs = ConvergenceHistoryIDs

    @property
    def AlarmTypes(self):
        return self._AlarmTypes

    @AlarmTypes.setter
    def AlarmTypes(self, AlarmTypes):
        self._AlarmTypes = AlarmTypes


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Order = params.get("Order")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MonitorTypes = params.get("MonitorTypes")
        self._AlarmObject = params.get("AlarmObject")
        self._AlarmStatus = params.get("AlarmStatus")
        self._ProjectIds = params.get("ProjectIds")
        self._InstanceGroupIds = params.get("InstanceGroupIds")
        if params.get("Namespaces") is not None:
            self._Namespaces = []
            for item in params.get("Namespaces"):
                obj = MonitorTypeNamespace()
                obj._deserialize(item)
                self._Namespaces.append(obj)
        self._MetricNames = params.get("MetricNames")
        self._PolicyName = params.get("PolicyName")
        self._Content = params.get("Content")
        self._ReceiverUids = params.get("ReceiverUids")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._PolicyIds = params.get("PolicyIds")
        self._AlarmLevels = params.get("AlarmLevels")
        self._ConvergenceHistoryIDs = params.get("ConvergenceHistoryIDs")
        self._AlarmTypes = params.get("AlarmTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmHistoriesResponse(AbstractModel):
    """DescribeAlarmHistories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Histories: 告警历史列表
        :type Histories: list of AlarmHistory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Histories = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Histories(self):
        return self._Histories

    @Histories.setter
    def Histories(self, Histories):
        self._Histories = Histories

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Histories") is not None:
            self._Histories = []
            for item in params.get("Histories"):
                obj = AlarmHistory()
                obj._deserialize(item)
                self._Histories.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmMetricsRequest(AbstractModel):
    """DescribeAlarmMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _MonitorType: 监控类型过滤 "MT_QCE"=云产品监控
        :type MonitorType: str
        :param _Namespace: 告警策略类型，由 DescribeAllNamespaces 获得，例如 cvm_device
        :type Namespace: str
        """
        self._Module = None
        self._MonitorType = None
        self._Namespace = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._MonitorType = params.get("MonitorType")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmMetricsResponse(AbstractModel):
    """DescribeAlarmMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metrics: 告警指标列表
        :type Metrics: list of Metric
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metrics = None
        self._RequestId = None

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = Metric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmNoticeCallbacksRequest(AbstractModel):
    """DescribeAlarmNoticeCallbacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”
        :type Module: str
        """
        self._Module = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        self._Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticeCallbacksResponse(AbstractModel):
    """DescribeAlarmNoticeCallbacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _URLNotices: 告警回调通知
注意：此字段可能返回 null，表示取不到有效值。
        :type URLNotices: list of URLNotice
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._URLNotices = None
        self._RequestId = None

    @property
    def URLNotices(self):
        return self._URLNotices

    @URLNotices.setter
    def URLNotices(self, URLNotices):
        self._URLNotices = URLNotices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("URLNotices") is not None:
            self._URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self._URLNotices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmNoticeRequest(AbstractModel):
    """DescribeAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”
        :type Module: str
        :param _NoticeId: 告警通知模板 id
        :type NoticeId: str
        """
        self._Module = None
        self._NoticeId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._NoticeId = params.get("NoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticeResponse(AbstractModel):
    """DescribeAlarmNotice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Notice: 告警通知模板详细信息
        :type Notice: :class:`tencentcloud.monitor.v20180724.models.AlarmNotice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Notice = None
        self._RequestId = None

    @property
    def Notice(self):
        return self._Notice

    @Notice.setter
    def Notice(self, Notice):
        self._Notice = Notice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Notice") is not None:
            self._Notice = AlarmNotice()
            self._Notice._deserialize(params.get("Notice"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”
        :type Module: str
        :param _PageNumber: 页码 最小为1
        :type PageNumber: int
        :param _PageSize: 分页大小 1～200
        :type PageSize: int
        :param _Order: 按更新时间排序方式 ASC=正序 DESC=倒序
        :type Order: str
        :param _OwnerUid: 主账号 uid 用于创建预设通知
        :type OwnerUid: int
        :param _Name: 告警通知模板名称 用来模糊搜索
        :type Name: str
        :param _ReceiverType: 根据接收人过滤告警通知模板需要选定通知用户类型 USER=用户 GROUP=用户组 传空=不按接收人过滤
        :type ReceiverType: str
        :param _UserIds: 接收对象列表
        :type UserIds: list of int
        :param _GroupIds: 接收组列表
        :type GroupIds: list of int
        :param _NoticeIds: 根据通知模板 id 过滤，空数组/不传则不过滤
        :type NoticeIds: list of str
        :param _Tags: 模板根据标签过滤
        :type Tags: list of Tag
        :param _OnCallFormIDs: 值班列表
        :type OnCallFormIDs: list of str
        """
        self._Module = None
        self._PageNumber = None
        self._PageSize = None
        self._Order = None
        self._OwnerUid = None
        self._Name = None
        self._ReceiverType = None
        self._UserIds = None
        self._GroupIds = None
        self._NoticeIds = None
        self._Tags = None
        self._OnCallFormIDs = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OwnerUid(self):
        return self._OwnerUid

    @OwnerUid.setter
    def OwnerUid(self, OwnerUid):
        self._OwnerUid = OwnerUid

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def OnCallFormIDs(self):
        return self._OnCallFormIDs

    @OnCallFormIDs.setter
    def OnCallFormIDs(self, OnCallFormIDs):
        self._OnCallFormIDs = OnCallFormIDs


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Order = params.get("Order")
        self._OwnerUid = params.get("OwnerUid")
        self._Name = params.get("Name")
        self._ReceiverType = params.get("ReceiverType")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._NoticeIds = params.get("NoticeIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._OnCallFormIDs = params.get("OnCallFormIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 告警通知模板总数
        :type TotalCount: int
        :param _Notices: 告警通知模板列表
        :type Notices: list of AlarmNotice
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Notices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Notices(self):
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmPoliciesRequest(AbstractModel):
    """DescribeAlarmPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _PageNumber: 页数，从 1 开始计数，默认 1
        :type PageNumber: int
        :param _PageSize: 每页的数量，取值1~100，默认20
        :type PageSize: int
        :param _PolicyName: 按策略名称模糊搜索
        :type PolicyName: str
        :param _MonitorTypes: 根据监控类型过滤 不选默认查所有类型 "MT_QCE"=云产品监控,当Dimension不为空时，该项为必填项
        :type MonitorTypes: list of str
        :param _Namespaces: 根据命名空间过滤，不同策略类型的值详见
[策略类型列表](https://cloud.tencent.com/document/product/248/50397)当Dimension不为空时，该项为必填项
        :type Namespaces: list of str
        :param _Dimensions: 告警对象列表，JSON 字符串。外层数组，对应多个实例，内层为对象的维度。例如“云服务器-基础监控”可写为：
`[ {"Dimensions": {"unInstanceId": "ins-qr8d555g"}}, {"Dimensions": {"unInstanceId": "ins-qr8d555h"}} ]`
具体也可以参考下方的示例 2。

不同云产品参数示例详见 [维度信息Dimensions列表](https://cloud.tencent.com/document/product/248/50397)

注意：如果NeedCorrespondence传入1，即需要返回策略与实例对应关系，请传入不多于20个告警对象维度，否则容易请求超时
        :type Dimensions: str
        :param _ReceiverUids: 根据接收人搜索，可以使用“访问管理”的 [拉取子用户 ListUsers](https://cloud.tencent.com/document/product/598/34587) 接口获取用户列表 或 [查询子用户 GetUser](https://cloud.tencent.com/document/product/598/34590) 接口查询子用户详情，此处填入返回结果中的 `Uid` 字段
        :type ReceiverUids: list of int
        :param _ReceiverGroups: 根据接收组搜索，可以使用“访问管理”的 [查询用户组列表 ListGroups](https://cloud.tencent.com/document/product/598/34589) 接口获取用户组列表 或 [列出用户关联的用户组 ListGroupsForUser](https://cloud.tencent.com/document/product/598/34588) 查询某个子用户所在的用户组列表 ，此处填入返回结果中的 `GroupId ` 字段
        :type ReceiverGroups: list of int
        :param _PolicyType: 根据默认策略筛选 不传展示全部策略 DEFAULT=展示默认策略 NOT_DEFAULT=展示非默认策略
        :type PolicyType: list of str
        :param _Field: 排序字段，例如按照最后修改时间排序，Field: "UpdateTime"
        :type Field: str
        :param _Order: 排序顺序：升序：ASC  降序：DESC
        :type Order: str
        :param _ProjectIds: 策略所属项目的id数组，可在此页面查看
[项目管理](https://console.cloud.tencent.com/project)
        :type ProjectIds: list of int
        :param _NoticeIds: 通知模板的id列表，可查询通知模板列表获取。
可使用 [查询通知模板列表](https://cloud.tencent.com/document/product/248/51280) 接口查询。
        :type NoticeIds: list of str
        :param _RuleTypes: 根据触发条件筛选 不传展示全部策略 STATIC=展示静态阈值策略 DYNAMIC=展示动态阈值策略
        :type RuleTypes: list of str
        :param _Enable: 告警启停筛选，[1]：启用   [0]：停止，全部[0, 1]
        :type Enable: list of int
        :param _NotBindingNoticeRule: 传 1 查询未配置通知规则的告警策略；不传或传其他数值，查询所有策略。
        :type NotBindingNoticeRule: int
        :param _InstanceGroupId: 实例分组id
        :type InstanceGroupId: int
        :param _NeedCorrespondence: 是否需要策略与入参过滤维度参数的对应关系，1：是  0：否，默认为0
        :type NeedCorrespondence: int
        :param _TriggerTasks: 按照触发任务（例如弹性伸缩）过滤策略。最多10个
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param _OneClickPolicyType: 根据一键告警策略筛选 不传展示全部策略 ONECLICK=展示一键告警策略 NOT_ONECLICK=展示非一键告警策略
        :type OneClickPolicyType: list of str
        :param _NotBindAll: 返回结果过滤掉绑定全部对象的策略，1代表需要过滤，0则无需过滤
        :type NotBindAll: int
        :param _NotInstanceGroup: 返回结果过滤掉关联实例为实例分组的策略，1代表需要过滤，0则无需过滤
        :type NotInstanceGroup: int
        :param _Tags: 策略根据标签过滤
        :type Tags: list of Tag
        :param _PromInsId: prom实例id，自定义指标策略时会用到
        :type PromInsId: str
        :param _ReceiverOnCallFormIDs: 根据排班表搜索
        :type ReceiverOnCallFormIDs: list of str
        """
        self._Module = None
        self._PageNumber = None
        self._PageSize = None
        self._PolicyName = None
        self._MonitorTypes = None
        self._Namespaces = None
        self._Dimensions = None
        self._ReceiverUids = None
        self._ReceiverGroups = None
        self._PolicyType = None
        self._Field = None
        self._Order = None
        self._ProjectIds = None
        self._NoticeIds = None
        self._RuleTypes = None
        self._Enable = None
        self._NotBindingNoticeRule = None
        self._InstanceGroupId = None
        self._NeedCorrespondence = None
        self._TriggerTasks = None
        self._OneClickPolicyType = None
        self._NotBindAll = None
        self._NotInstanceGroup = None
        self._Tags = None
        self._PromInsId = None
        self._ReceiverOnCallFormIDs = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def MonitorTypes(self):
        return self._MonitorTypes

    @MonitorTypes.setter
    def MonitorTypes(self, MonitorTypes):
        self._MonitorTypes = MonitorTypes

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def ReceiverUids(self):
        return self._ReceiverUids

    @ReceiverUids.setter
    def ReceiverUids(self, ReceiverUids):
        self._ReceiverUids = ReceiverUids

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def RuleTypes(self):
        return self._RuleTypes

    @RuleTypes.setter
    def RuleTypes(self, RuleTypes):
        self._RuleTypes = RuleTypes

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def NotBindingNoticeRule(self):
        return self._NotBindingNoticeRule

    @NotBindingNoticeRule.setter
    def NotBindingNoticeRule(self, NotBindingNoticeRule):
        self._NotBindingNoticeRule = NotBindingNoticeRule

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def NeedCorrespondence(self):
        return self._NeedCorrespondence

    @NeedCorrespondence.setter
    def NeedCorrespondence(self, NeedCorrespondence):
        self._NeedCorrespondence = NeedCorrespondence

    @property
    def TriggerTasks(self):
        return self._TriggerTasks

    @TriggerTasks.setter
    def TriggerTasks(self, TriggerTasks):
        self._TriggerTasks = TriggerTasks

    @property
    def OneClickPolicyType(self):
        return self._OneClickPolicyType

    @OneClickPolicyType.setter
    def OneClickPolicyType(self, OneClickPolicyType):
        self._OneClickPolicyType = OneClickPolicyType

    @property
    def NotBindAll(self):
        return self._NotBindAll

    @NotBindAll.setter
    def NotBindAll(self, NotBindAll):
        self._NotBindAll = NotBindAll

    @property
    def NotInstanceGroup(self):
        return self._NotInstanceGroup

    @NotInstanceGroup.setter
    def NotInstanceGroup(self, NotInstanceGroup):
        self._NotInstanceGroup = NotInstanceGroup

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PromInsId(self):
        return self._PromInsId

    @PromInsId.setter
    def PromInsId(self, PromInsId):
        self._PromInsId = PromInsId

    @property
    def ReceiverOnCallFormIDs(self):
        return self._ReceiverOnCallFormIDs

    @ReceiverOnCallFormIDs.setter
    def ReceiverOnCallFormIDs(self, ReceiverOnCallFormIDs):
        self._ReceiverOnCallFormIDs = ReceiverOnCallFormIDs


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._PolicyName = params.get("PolicyName")
        self._MonitorTypes = params.get("MonitorTypes")
        self._Namespaces = params.get("Namespaces")
        self._Dimensions = params.get("Dimensions")
        self._ReceiverUids = params.get("ReceiverUids")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._PolicyType = params.get("PolicyType")
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        self._ProjectIds = params.get("ProjectIds")
        self._NoticeIds = params.get("NoticeIds")
        self._RuleTypes = params.get("RuleTypes")
        self._Enable = params.get("Enable")
        self._NotBindingNoticeRule = params.get("NotBindingNoticeRule")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._NeedCorrespondence = params.get("NeedCorrespondence")
        if params.get("TriggerTasks") is not None:
            self._TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self._TriggerTasks.append(obj)
        self._OneClickPolicyType = params.get("OneClickPolicyType")
        self._NotBindAll = params.get("NotBindAll")
        self._NotInstanceGroup = params.get("NotInstanceGroup")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PromInsId = params.get("PromInsId")
        self._ReceiverOnCallFormIDs = params.get("ReceiverOnCallFormIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmPoliciesResponse(AbstractModel):
    """DescribeAlarmPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 策略总数
        :type TotalCount: int
        :param _Policies: 策略数组
        :type Policies: list of AlarmPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Policies = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Policies(self):
        return self._Policies

    @Policies.setter
    def Policies(self, Policies):
        self._Policies = Policies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Policies") is not None:
            self._Policies = []
            for item in params.get("Policies"):
                obj = AlarmPolicy()
                obj._deserialize(item)
                self._Policies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmPolicyRequest(AbstractModel):
    """DescribeAlarmPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _PolicyId: 告警策略ID
        :type PolicyId: str
        """
        self._Module = None
        self._PolicyId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmPolicyResponse(AbstractModel):
    """DescribeAlarmPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Policy: 策略详情
        :type Policy: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicy`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Policy = None
        self._RequestId = None

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self._Policy = AlarmPolicy()
            self._Policy._deserialize(params.get("Policy"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmSmsQuotaQuota(AbstractModel):
    """DescribeAlarmSmsQuota接口的配额信息

    """

    def __init__(self):
        r"""
        :param _Type: 配额类型
        :type Type: str
        :param _Name: 配额名称
        :type Name: str
        :param _FreeLeft: 免费配额剩余量
        :type FreeLeft: int
        :param _PurchaseLeft: 付费配额剩余量
        :type PurchaseLeft: int
        :param _Used: 已使用量
        :type Used: int
        """
        self._Type = None
        self._Name = None
        self._FreeLeft = None
        self._PurchaseLeft = None
        self._Used = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FreeLeft(self):
        return self._FreeLeft

    @FreeLeft.setter
    def FreeLeft(self, FreeLeft):
        self._FreeLeft = FreeLeft

    @property
    def PurchaseLeft(self):
        return self._PurchaseLeft

    @PurchaseLeft.setter
    def PurchaseLeft(self, PurchaseLeft):
        self._PurchaseLeft = PurchaseLeft

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._FreeLeft = params.get("FreeLeft")
        self._PurchaseLeft = params.get("PurchaseLeft")
        self._Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmSmsQuotaRequest(AbstractModel):
    """DescribeAlarmSmsQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        """
        self._Module = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        self._Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmSmsQuotaResponse(AbstractModel):
    """DescribeAlarmSmsQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 配额总数
        :type Total: int
        :param _Used: 总使用量
        :type Used: int
        :param _QuotaList: 短信配额信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaList: list of DescribeAlarmSmsQuotaQuota
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Used = None
        self._QuotaList = None
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
    def QuotaList(self):
        return self._QuotaList

    @QuotaList.setter
    def QuotaList(self, QuotaList):
        self._QuotaList = QuotaList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        if params.get("QuotaList") is not None:
            self._QuotaList = []
            for item in params.get("QuotaList"):
                obj = DescribeAlarmSmsQuotaQuota()
                obj._deserialize(item)
                self._QuotaList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlertRulesRequest(AbstractModel):
    """DescribeAlertRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _RuleState: 规则状态码，取值如下：
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _Type: 报警策略模板分类
        :type Type: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._RuleId = None
        self._RuleState = None
        self._RuleName = None
        self._Type = None

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
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RuleId = params.get("RuleId")
        self._RuleState = params.get("RuleState")
        self._RuleName = params.get("RuleName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertRulesResponse(AbstractModel):
    """DescribeAlertRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 报警规则数量
        :type TotalCount: int
        :param _AlertRuleSet: 报警规则详情
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRuleSet: list of PrometheusRuleSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AlertRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AlertRuleSet(self):
        return self._AlertRuleSet

    @AlertRuleSet.setter
    def AlertRuleSet(self, AlertRuleSet):
        self._AlertRuleSet = AlertRuleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AlertRuleSet") is not None:
            self._AlertRuleSet = []
            for item in params.get("AlertRuleSet"):
                obj = PrometheusRuleSet()
                obj._deserialize(item)
                self._AlertRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllNamespacesRequest(AbstractModel):
    """DescribeAllNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneType: 根据使用场景过滤 目前仅有"ST_ALARM"=告警类型
        :type SceneType: str
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _MonitorTypes: 根据监控类型过滤 不填默认查所有类型 "MT_QCE"=云产品监控
        :type MonitorTypes: list of str
        :param _Ids: 根据namespace的Id过滤 不填默认查询所有
        :type Ids: list of str
        """
        self._SceneType = None
        self._Module = None
        self._MonitorTypes = None
        self._Ids = None

    @property
    def SceneType(self):
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def MonitorTypes(self):
        return self._MonitorTypes

    @MonitorTypes.setter
    def MonitorTypes(self, MonitorTypes):
        self._MonitorTypes = MonitorTypes

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._SceneType = params.get("SceneType")
        self._Module = params.get("Module")
        self._MonitorTypes = params.get("MonitorTypes")
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllNamespacesResponse(AbstractModel):
    """DescribeAllNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QceNamespaces: 云产品的告警策略类型，已废弃
        :type QceNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`
        :param _CustomNamespaces: 其他告警策略类型，已废弃
        :type CustomNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`
        :param _QceNamespacesNew: 云产品的告警策略类型
        :type QceNamespacesNew: list of CommonNamespace
        :param _CustomNamespacesNew: 其他告警策略类型，暂不支持
        :type CustomNamespacesNew: list of CommonNamespace
        :param _CommonNamespaces: 通用告警策略类型(包括：应用性能监控，前端性能监控，云拨测)
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonNamespaces: list of CommonNamespaceNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QceNamespaces = None
        self._CustomNamespaces = None
        self._QceNamespacesNew = None
        self._CustomNamespacesNew = None
        self._CommonNamespaces = None
        self._RequestId = None

    @property
    def QceNamespaces(self):
        return self._QceNamespaces

    @QceNamespaces.setter
    def QceNamespaces(self, QceNamespaces):
        self._QceNamespaces = QceNamespaces

    @property
    def CustomNamespaces(self):
        return self._CustomNamespaces

    @CustomNamespaces.setter
    def CustomNamespaces(self, CustomNamespaces):
        self._CustomNamespaces = CustomNamespaces

    @property
    def QceNamespacesNew(self):
        return self._QceNamespacesNew

    @QceNamespacesNew.setter
    def QceNamespacesNew(self, QceNamespacesNew):
        self._QceNamespacesNew = QceNamespacesNew

    @property
    def CustomNamespacesNew(self):
        return self._CustomNamespacesNew

    @CustomNamespacesNew.setter
    def CustomNamespacesNew(self, CustomNamespacesNew):
        self._CustomNamespacesNew = CustomNamespacesNew

    @property
    def CommonNamespaces(self):
        return self._CommonNamespaces

    @CommonNamespaces.setter
    def CommonNamespaces(self, CommonNamespaces):
        self._CommonNamespaces = CommonNamespaces

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QceNamespaces") is not None:
            self._QceNamespaces = CommonNamespace()
            self._QceNamespaces._deserialize(params.get("QceNamespaces"))
        if params.get("CustomNamespaces") is not None:
            self._CustomNamespaces = CommonNamespace()
            self._CustomNamespaces._deserialize(params.get("CustomNamespaces"))
        if params.get("QceNamespacesNew") is not None:
            self._QceNamespacesNew = []
            for item in params.get("QceNamespacesNew"):
                obj = CommonNamespace()
                obj._deserialize(item)
                self._QceNamespacesNew.append(obj)
        if params.get("CustomNamespacesNew") is not None:
            self._CustomNamespacesNew = []
            for item in params.get("CustomNamespacesNew"):
                obj = CommonNamespace()
                obj._deserialize(item)
                self._CustomNamespacesNew.append(obj)
        if params.get("CommonNamespaces") is not None:
            self._CommonNamespaces = []
            for item in params.get("CommonNamespaces"):
                obj = CommonNamespaceNew()
                obj._deserialize(item)
                self._CommonNamespaces.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 业务命名空间，各个云产品的业务命名空间不同。如需获取业务命名空间，请前往各产品监控指标文档，例如云服务器的命名空间，可参见 [云服务器监控指标](https://cloud.tencent.com/document/product/248/6843)
        :type Namespace: str
        :param _MetricName: 指标名，各个云产品的指标名不同。如需获取指标名，请前往各产品监控指标文档，例如云服务器的指标名，可参见 [云服务器监控指标](https://cloud.tencent.com/document/product/248/6843)
        :type MetricName: str
        :param _Dimensions: 可选参数，按照维度过滤
        :type Dimensions: list of str
        """
        self._Namespace = None
        self._MetricName = None
        self._Dimensions = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        self._Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaseMetricsResponse(AbstractModel):
    """DescribeBaseMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricSet: 查询得到的指标描述列表
        :type MetricSet: list of MetricSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricSet = None
        self._RequestId = None

    @property
    def MetricSet(self):
        return self._MetricSet

    @MetricSet.setter
    def MetricSet(self, MetricSet):
        self._MetricSet = MetricSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self._MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricSet()
                obj._deserialize(item)
                self._MetricSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBasicAlarmListAlarms(AbstractModel):
    """DescribeBasicAlarmList返回的Alarms

    """

    def __init__(self):
        r"""
        :param _Id: 该条告警的ID
        :type Id: int
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _Status: 告警状态ID，0表示未恢复；1表示已恢复；2,3,5表示数据不足；4表示已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _AlarmStatus: 告警状态，ALARM表示未恢复；OK表示已恢复；NO_DATA表示数据不足；NO_CONF表示已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmStatus: str
        :param _GroupId: 策略组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param _GroupName: 策略组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _FirstOccurTime: 发生时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOccurTime: str
        :param _Duration: 持续时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _LastOccurTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOccurTime: str
        :param _Content: 告警内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _ObjName: 告警对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjName: str
        :param _ObjId: 告警对象ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjId: str
        :param _ViewName: 策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        :param _Vpc: VPC，只有CVM有
注意：此字段可能返回 null，表示取不到有效值。
        :type Vpc: str
        :param _MetricId: 指标ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricId: int
        :param _MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _AlarmType: 告警类型，0表示指标告警，2表示产品事件告警，3表示平台事件告警
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmType: int
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Dimensions: 告警对象维度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: str
        :param _NotifyWay: 通知方式
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyWay: list of str
        :param _InstanceGroup: 所属实例组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroup: list of InstanceGroup
        """
        self._Id = None
        self._ProjectId = None
        self._ProjectName = None
        self._Status = None
        self._AlarmStatus = None
        self._GroupId = None
        self._GroupName = None
        self._FirstOccurTime = None
        self._Duration = None
        self._LastOccurTime = None
        self._Content = None
        self._ObjName = None
        self._ObjId = None
        self._ViewName = None
        self._Vpc = None
        self._MetricId = None
        self._MetricName = None
        self._AlarmType = None
        self._Region = None
        self._Dimensions = None
        self._NotifyWay = None
        self._InstanceGroup = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmStatus(self):
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def FirstOccurTime(self):
        return self._FirstOccurTime

    @FirstOccurTime.setter
    def FirstOccurTime(self, FirstOccurTime):
        self._FirstOccurTime = FirstOccurTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def LastOccurTime(self):
        return self._LastOccurTime

    @LastOccurTime.setter
    def LastOccurTime(self, LastOccurTime):
        self._LastOccurTime = LastOccurTime

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ObjName(self):
        return self._ObjName

    @ObjName.setter
    def ObjName(self, ObjName):
        self._ObjName = ObjName

    @property
    def ObjId(self):
        return self._ObjId

    @ObjId.setter
    def ObjId(self, ObjId):
        self._ObjId = ObjId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def InstanceGroup(self):
        return self._InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, InstanceGroup):
        self._InstanceGroup = InstanceGroup


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Status = params.get("Status")
        self._AlarmStatus = params.get("AlarmStatus")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._FirstOccurTime = params.get("FirstOccurTime")
        self._Duration = params.get("Duration")
        self._LastOccurTime = params.get("LastOccurTime")
        self._Content = params.get("Content")
        self._ObjName = params.get("ObjName")
        self._ObjId = params.get("ObjId")
        self._ViewName = params.get("ViewName")
        self._Vpc = params.get("Vpc")
        self._MetricId = params.get("MetricId")
        self._MetricName = params.get("MetricName")
        self._AlarmType = params.get("AlarmType")
        self._Region = params.get("Region")
        self._Dimensions = params.get("Dimensions")
        self._NotifyWay = params.get("NotifyWay")
        if params.get("InstanceGroup") is not None:
            self._InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroup()
                obj._deserialize(item)
                self._InstanceGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicAlarmListRequest(AbstractModel):
    """DescribeBasicAlarmList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 接口模块名，当前取值monitor
        :type Module: str
        :param _StartTime: 起始时间，默认一天前的时间戳
        :type StartTime: int
        :param _EndTime: 结束时间，默认当前时间戳
        :type EndTime: int
        :param _Limit: 分页参数，每页返回的数量，取值1~100，默认20
        :type Limit: int
        :param _Offset: 分页参数，页偏移量，从0开始计数，默认0
        :type Offset: int
        :param _OccurTimeOrder: 根据发生时间排序，取值ASC或DESC
        :type OccurTimeOrder: str
        :param _ProjectIds: 根据项目ID过滤
        :type ProjectIds: list of int
        :param _ViewNames: 根据策略类型过滤
        :type ViewNames: list of str
        :param _AlarmStatus: 根据告警状态过滤
        :type AlarmStatus: list of int
        :param _ObjLike: 根据告警对象过滤
        :type ObjLike: str
        :param _InstanceGroupIds: 根据实例组ID过滤
        :type InstanceGroupIds: list of int
        :param _MetricNames: 根据指标名过滤
        :type MetricNames: list of str
        """
        self._Module = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._OccurTimeOrder = None
        self._ProjectIds = None
        self._ViewNames = None
        self._AlarmStatus = None
        self._ObjLike = None
        self._InstanceGroupIds = None
        self._MetricNames = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

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
    def OccurTimeOrder(self):
        return self._OccurTimeOrder

    @OccurTimeOrder.setter
    def OccurTimeOrder(self, OccurTimeOrder):
        self._OccurTimeOrder = OccurTimeOrder

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ViewNames(self):
        return self._ViewNames

    @ViewNames.setter
    def ViewNames(self, ViewNames):
        self._ViewNames = ViewNames

    @property
    def AlarmStatus(self):
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

    @property
    def ObjLike(self):
        return self._ObjLike

    @ObjLike.setter
    def ObjLike(self, ObjLike):
        self._ObjLike = ObjLike

    @property
    def InstanceGroupIds(self):
        return self._InstanceGroupIds

    @InstanceGroupIds.setter
    def InstanceGroupIds(self, InstanceGroupIds):
        self._InstanceGroupIds = InstanceGroupIds

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OccurTimeOrder = params.get("OccurTimeOrder")
        self._ProjectIds = params.get("ProjectIds")
        self._ViewNames = params.get("ViewNames")
        self._AlarmStatus = params.get("AlarmStatus")
        self._ObjLike = params.get("ObjLike")
        self._InstanceGroupIds = params.get("InstanceGroupIds")
        self._MetricNames = params.get("MetricNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicAlarmListResponse(AbstractModel):
    """DescribeBasicAlarmList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Alarms: 告警列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Alarms: list of DescribeBasicAlarmListAlarms
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Warning: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Warning: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Alarms = None
        self._Total = None
        self._Warning = None
        self._RequestId = None

    @property
    def Alarms(self):
        return self._Alarms

    @Alarms.setter
    def Alarms(self, Alarms):
        self._Alarms = Alarms

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Warning(self):
        return self._Warning

    @Warning.setter
    def Warning(self, Warning):
        self._Warning = Warning

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self._Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeBasicAlarmListAlarms()
                obj._deserialize(item)
                self._Alarms.append(obj)
        self._Total = params.get("Total")
        self._Warning = params.get("Warning")
        self._RequestId = params.get("RequestId")


class DescribeBindingPolicyObjectListDimension(AbstractModel):
    """DescribeBindingPolicyObjectList接口的Dimension

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域id
        :type RegionId: int
        :param _Region: 地域简称
        :type Region: str
        :param _Dimensions: 维度组合json字符串
        :type Dimensions: str
        :param _EventDimensions: 事件维度组合json字符串
        :type EventDimensions: str
        """
        self._RegionId = None
        self._Region = None
        self._Dimensions = None
        self._EventDimensions = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def EventDimensions(self):
        return self._EventDimensions

    @EventDimensions.setter
    def EventDimensions(self, EventDimensions):
        self._EventDimensions = EventDimensions


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Region = params.get("Region")
        self._Dimensions = params.get("Dimensions")
        self._EventDimensions = params.get("EventDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListInstance(AbstractModel):
    """查询策略绑定对象列表接口返回的对象实例信息

    """

    def __init__(self):
        r"""
        :param _UniqueId: 对象唯一id
        :type UniqueId: str
        :param _Dimensions: 表示对象实例的维度集合，jsonObj字符串
        :type Dimensions: str
        :param _IsShielded: 对象是否被屏蔽，0表示未屏蔽，1表示被屏蔽
        :type IsShielded: int
        :param _Region: 对象所在的地域
        :type Region: str
        """
        self._UniqueId = None
        self._Dimensions = None
        self._IsShielded = None
        self._Region = None

    @property
    def UniqueId(self):
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def IsShielded(self):
        return self._IsShielded

    @IsShielded.setter
    def IsShielded(self, IsShielded):
        self._IsShielded = IsShielded

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._UniqueId = params.get("UniqueId")
        self._Dimensions = params.get("Dimensions")
        self._IsShielded = params.get("IsShielded")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListInstanceGroup(AbstractModel):
    """DescribeBindingPolicyObjectList返回的是实例分组信息

    """

    def __init__(self):
        r"""
        :param _InstanceGroupId: 实例分组id
        :type InstanceGroupId: int
        :param _ViewName: 告警策略类型名称
        :type ViewName: str
        :param _LastEditUin: 最后编辑uin
        :type LastEditUin: str
        :param _GroupName: 实例分组名称
        :type GroupName: str
        :param _InstanceSum: 实例数量
        :type InstanceSum: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        :param _InsertTime: 创建时间
        :type InsertTime: int
        :param _Regions: 实例所在的地域集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Regions: list of str
        """
        self._InstanceGroupId = None
        self._ViewName = None
        self._LastEditUin = None
        self._GroupName = None
        self._InstanceSum = None
        self._UpdateTime = None
        self._InsertTime = None
        self._Regions = None

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceSum(self):
        return self._InstanceSum

    @InstanceSum.setter
    def InstanceSum(self, InstanceSum):
        self._InstanceSum = InstanceSum

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._ViewName = params.get("ViewName")
        self._LastEditUin = params.get("LastEditUin")
        self._GroupName = params.get("GroupName")
        self._InstanceSum = params.get("InstanceSum")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListRequest(AbstractModel):
    """DescribeBindingPolicyObjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _GroupId: 策略组id，如果有形如 policy-xxxx 的 id，请填到 PolicyId 字段中，本字段填 0
        :type GroupId: int
        :param _PolicyId: 告警策略id，形如 policy-xxxx，如果填入，则GroupId可以填0
        :type PolicyId: str
        :param _Limit: 每次返回的数量，取值1~100，默认20
        :type Limit: int
        :param _Offset: 偏移量，从0开始计数，默认0。举例来说，参数 Offset=0&Limit=20 返回第 0 到 19 项，Offset=20&Limit=20 返回第 20 到 39 项，以此类推
        :type Offset: int
        :param _Dimensions: 筛选对象的维度信息
        :type Dimensions: list of DescribeBindingPolicyObjectListDimension
        """
        self._Module = None
        self._GroupId = None
        self._PolicyId = None
        self._Limit = None
        self._Offset = None
        self._Dimensions = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._PolicyId = params.get("PolicyId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeBindingPolicyObjectListDimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListResponse(AbstractModel):
    """DescribeBindingPolicyObjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 绑定的对象实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DescribeBindingPolicyObjectListInstance
        :param _Total: 绑定的对象实例总数
        :type Total: int
        :param _NoShieldedSum: 未屏蔽的对象实例数
        :type NoShieldedSum: int
        :param _InstanceGroup: 绑定的实例分组信息，没有绑定实例分组则为空
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListInstanceGroup`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._NoShieldedSum = None
        self._InstanceGroup = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def NoShieldedSum(self):
        return self._NoShieldedSum

    @NoShieldedSum.setter
    def NoShieldedSum(self, NoShieldedSum):
        self._NoShieldedSum = NoShieldedSum

    @property
    def InstanceGroup(self):
        return self._InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, InstanceGroup):
        self._InstanceGroup = InstanceGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DescribeBindingPolicyObjectListInstance()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._NoShieldedSum = params.get("NoShieldedSum")
        if params.get("InstanceGroup") is not None:
            self._InstanceGroup = DescribeBindingPolicyObjectListInstanceGroup()
            self._InstanceGroup._deserialize(params.get("InstanceGroup"))
        self._RequestId = params.get("RequestId")


class DescribeClusterAgentCreatingProgressRequest(AbstractModel):
    """DescribeClusterAgentCreatingProgress请求参数结构体

    """


class DescribeClusterAgentCreatingProgressResponse(AbstractModel):
    """DescribeClusterAgentCreatingProgress返回参数结构体

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


class DescribeConditionsTemplateListRequest(AbstractModel):
    """DescribeConditionsTemplateList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _ViewName: 视图名，由 [DescribeAllNamespaces](https://cloud.tencent.com/document/product/248/48683) 获得。对于云产品监控，取接口出参的 QceNamespacesNew.N.Id，例如 cvm_device
        :type ViewName: str
        :param _GroupName: 根据触发条件模板名称过滤查询
        :type GroupName: str
        :param _GroupID: 根据触发条件模板ID过滤查询
        :type GroupID: str
        :param _Limit: 分页参数，每页返回的数量，取值1~100，默认20
        :type Limit: int
        :param _Offset: 分页参数，页偏移量，从0开始计数，默认0
        :type Offset: int
        :param _UpdateTimeOrder: 指定按更新时间的排序方式，asc=升序, desc=降序
        :type UpdateTimeOrder: str
        :param _PolicyCountOrder: 指定按绑定策略数目的排序方式，asc=升序, desc=降序
        :type PolicyCountOrder: str
        """
        self._Module = None
        self._ViewName = None
        self._GroupName = None
        self._GroupID = None
        self._Limit = None
        self._Offset = None
        self._UpdateTimeOrder = None
        self._PolicyCountOrder = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupID(self):
        return self._GroupID

    @GroupID.setter
    def GroupID(self, GroupID):
        self._GroupID = GroupID

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
    def UpdateTimeOrder(self):
        return self._UpdateTimeOrder

    @UpdateTimeOrder.setter
    def UpdateTimeOrder(self, UpdateTimeOrder):
        self._UpdateTimeOrder = UpdateTimeOrder

    @property
    def PolicyCountOrder(self):
        return self._PolicyCountOrder

    @PolicyCountOrder.setter
    def PolicyCountOrder(self, PolicyCountOrder):
        self._PolicyCountOrder = PolicyCountOrder


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._ViewName = params.get("ViewName")
        self._GroupName = params.get("GroupName")
        self._GroupID = params.get("GroupID")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._UpdateTimeOrder = params.get("UpdateTimeOrder")
        self._PolicyCountOrder = params.get("PolicyCountOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConditionsTemplateListResponse(AbstractModel):
    """DescribeConditionsTemplateList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 模板总数
        :type Total: int
        :param _TemplateGroupList: 模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateGroupList: list of TemplateGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._TemplateGroupList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TemplateGroupList(self):
        return self._TemplateGroupList

    @TemplateGroupList.setter
    def TemplateGroupList(self, TemplateGroupList):
        self._TemplateGroupList = TemplateGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("TemplateGroupList") is not None:
            self._TemplateGroupList = []
            for item in params.get("TemplateGroupList"):
                obj = TemplateGroup()
                obj._deserialize(item)
                self._TemplateGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDNSConfigRequest(AbstractModel):
    """DescribeDNSConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
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
        


class DescribeDNSConfigResponse(AbstractModel):
    """DescribeDNSConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NameServers: DNS 服务器数组
        :type NameServers: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NameServers = None
        self._RequestId = None

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NameServers = params.get("NameServers")
        self._RequestId = params.get("RequestId")


class DescribeExporterIntegrationsRequest(AbstractModel):
    """DescribeExporterIntegrations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _KubeType: Kubernetes 集群类型，可不填。取值如下：
<li> 1= 容器集群(TKE) </li>
<li> 2=弹性集群(EKS) </li>
<li> 3= Prometheus管理的弹性集群(MEKS) </li>
        :type KubeType: int
        :param _ClusterId: 集群 ID，可不填
        :type ClusterId: str
        :param _Kind: 类型(不填返回全部集成。可通过 DescribePrometheusIntegrations 接口获取，取每一项中的 ExporterType 字段)
        :type Kind: str
        :param _Name: 名字
        :type Name: str
        """
        self._InstanceId = None
        self._KubeType = None
        self._ClusterId = None
        self._Kind = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeType = params.get("KubeType")
        self._ClusterId = params.get("ClusterId")
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExporterIntegrationsResponse(AbstractModel):
    """DescribeExporterIntegrations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntegrationSet: 集成配置列表
        :type IntegrationSet: list of IntegrationConfiguration
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntegrationSet = None
        self._RequestId = None

    @property
    def IntegrationSet(self):
        return self._IntegrationSet

    @IntegrationSet.setter
    def IntegrationSet(self, IntegrationSet):
        self._IntegrationSet = IntegrationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IntegrationSet") is not None:
            self._IntegrationSet = []
            for item in params.get("IntegrationSet"):
                obj = IntegrationConfiguration()
                obj._deserialize(item)
                self._IntegrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaChannelsRequest(AbstractModel):
    """DescribeGrafanaChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
        :type InstanceId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 查询数量
        :type Limit: int
        :param _ChannelName: 告警通道名称，例如：test
        :type ChannelName: str
        :param _ChannelIds: 告警通道 ID，例如：nchannel-abcd1234
        :type ChannelIds: list of str
        :param _ChannelState: 告警通道状态(不用填写，目前只有可用和删除状态，默认只能查询可用的告警通道)
        :type ChannelState: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._ChannelName = None
        self._ChannelIds = None
        self._ChannelState = None

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
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ChannelIds(self):
        return self._ChannelIds

    @ChannelIds.setter
    def ChannelIds(self, ChannelIds):
        self._ChannelIds = ChannelIds

    @property
    def ChannelState(self):
        return self._ChannelState

    @ChannelState.setter
    def ChannelState(self, ChannelState):
        self._ChannelState = ChannelState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ChannelName = params.get("ChannelName")
        self._ChannelIds = params.get("ChannelIds")
        self._ChannelState = params.get("ChannelState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaChannelsResponse(AbstractModel):
    """DescribeGrafanaChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotificationChannelSet: 告警通道数组
        :type NotificationChannelSet: list of GrafanaChannel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotificationChannelSet = None
        self._RequestId = None

    @property
    def NotificationChannelSet(self):
        return self._NotificationChannelSet

    @NotificationChannelSet.setter
    def NotificationChannelSet(self, NotificationChannelSet):
        self._NotificationChannelSet = NotificationChannelSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotificationChannelSet") is not None:
            self._NotificationChannelSet = []
            for item in params.get("NotificationChannelSet"):
                obj = GrafanaChannel()
                obj._deserialize(item)
                self._NotificationChannelSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaConfigRequest(AbstractModel):
    """DescribeGrafanaConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
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
        


class DescribeGrafanaConfigResponse(AbstractModel):
    """DescribeGrafanaConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Config: JSON 编码后的字符串
        :type Config: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Config = None
        self._RequestId = None

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Config = params.get("Config")
        self._RequestId = params.get("RequestId")


class DescribeGrafanaEnvironmentsRequest(AbstractModel):
    """DescribeGrafanaEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
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
        


class DescribeGrafanaEnvironmentsResponse(AbstractModel):
    """DescribeGrafanaEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Envs: 环境变量字符串
        :type Envs: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Envs = None
        self._RequestId = None

    @property
    def Envs(self):
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Envs = params.get("Envs")
        self._RequestId = params.get("RequestId")


class DescribeGrafanaInstancesRequest(AbstractModel):
    """DescribeGrafanaInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 查询数量
        :type Limit: int
        :param _InstanceIds: Grafana 实例 ID 数组
        :type InstanceIds: list of str
        :param _InstanceName: Grafana 实例名，支持前缀模糊搜索
        :type InstanceName: str
        :param _InstanceStatus: 查询状态
        :type InstanceStatus: list of int
        :param _TagFilters: 标签过滤数组
        :type TagFilters: list of PrometheusTag
        """
        self._Offset = None
        self._Limit = None
        self._InstanceIds = None
        self._InstanceName = None
        self._InstanceStatus = None
        self._TagFilters = None

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceName = params.get("InstanceName")
        self._InstanceStatus = params.get("InstanceStatus")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaInstancesResponse(AbstractModel):
    """DescribeGrafanaInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: 已废弃，请使用 Instances
        :type InstanceSet: list of GrafanaInstanceInfo
        :param _TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param _Instances: 实例列表
        :type Instances: list of GrafanaInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = GrafanaInstanceInfo()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = GrafanaInstanceInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaIntegrationsRequest(AbstractModel):
    """DescribeGrafanaIntegrations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _IntegrationId: 集成 ID
        :type IntegrationId: str
        :param _Kind: 类型
        :type Kind: str
        """
        self._InstanceId = None
        self._IntegrationId = None
        self._Kind = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IntegrationId = params.get("IntegrationId")
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaIntegrationsResponse(AbstractModel):
    """DescribeGrafanaIntegrations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntegrationSet: 集成数组
        :type IntegrationSet: list of GrafanaIntegrationConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntegrationSet = None
        self._RequestId = None

    @property
    def IntegrationSet(self):
        return self._IntegrationSet

    @IntegrationSet.setter
    def IntegrationSet(self, IntegrationSet):
        self._IntegrationSet = IntegrationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IntegrationSet") is not None:
            self._IntegrationSet = []
            for item in params.get("IntegrationSet"):
                obj = GrafanaIntegrationConfig()
                obj._deserialize(item)
                self._IntegrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaNotificationChannelsRequest(AbstractModel):
    """DescribeGrafanaNotificationChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
        :type InstanceId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 查询数量
        :type Limit: int
        :param _ChannelName: 告警通道名称，例如：test
        :type ChannelName: str
        :param _ChannelIDs: 告警通道 ID，例如：nchannel-abcd1234
        :type ChannelIDs: list of str
        :param _ChannelState: 告警通道状态
        :type ChannelState: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._ChannelName = None
        self._ChannelIDs = None
        self._ChannelState = None

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
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ChannelIDs(self):
        return self._ChannelIDs

    @ChannelIDs.setter
    def ChannelIDs(self, ChannelIDs):
        self._ChannelIDs = ChannelIDs

    @property
    def ChannelState(self):
        return self._ChannelState

    @ChannelState.setter
    def ChannelState(self, ChannelState):
        self._ChannelState = ChannelState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ChannelName = params.get("ChannelName")
        self._ChannelIDs = params.get("ChannelIDs")
        self._ChannelState = params.get("ChannelState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaNotificationChannelsResponse(AbstractModel):
    """DescribeGrafanaNotificationChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotificationChannelSet: 告警通道数组
        :type NotificationChannelSet: list of GrafanaNotificationChannel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotificationChannelSet = None
        self._RequestId = None

    @property
    def NotificationChannelSet(self):
        return self._NotificationChannelSet

    @NotificationChannelSet.setter
    def NotificationChannelSet(self, NotificationChannelSet):
        self._NotificationChannelSet = NotificationChannelSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotificationChannelSet") is not None:
            self._NotificationChannelSet = []
            for item in params.get("NotificationChannelSet"):
                obj = GrafanaNotificationChannel()
                obj._deserialize(item)
                self._NotificationChannelSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaWhiteListRequest(AbstractModel):
    """DescribeGrafanaWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
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
        


class DescribeGrafanaWhiteListResponse(AbstractModel):
    """DescribeGrafanaWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WhiteList: 数组
        :type WhiteList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WhiteList = None
        self._RequestId = None

    @property
    def WhiteList(self):
        return self._WhiteList

    @WhiteList.setter
    def WhiteList(self, WhiteList):
        self._WhiteList = WhiteList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WhiteList = params.get("WhiteList")
        self._RequestId = params.get("RequestId")


class DescribeInstalledPluginsRequest(AbstractModel):
    """DescribeInstalledPlugins请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-kleu3gt0
        :type InstanceId: str
        :param _PluginId: 按插件 ID 过滤，例如：grafana-piechart-panel，可通过接口 DescribeInstalledPlugins 查看已安装的插件 ID
        :type PluginId: str
        """
        self._InstanceId = None
        self._PluginId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PluginId = params.get("PluginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstalledPluginsResponse(AbstractModel):
    """DescribeInstalledPlugins返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginSet: 插件列表
        :type PluginSet: list of GrafanaPlugin
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PluginSet = None
        self._RequestId = None

    @property
    def PluginSet(self):
        return self._PluginSet

    @PluginSet.setter
    def PluginSet(self, PluginSet):
        self._PluginSet = PluginSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PluginSet") is not None:
            self._PluginSet = []
            for item in params.get("PluginSet"):
                obj = GrafanaPlugin()
                obj._deserialize(item)
                self._PluginSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMonitorResourceInfoRequest(AbstractModel):
    """DescribeMonitorResourceInfo请求参数结构体

    """


class DescribeMonitorResourceInfoResponse(AbstractModel):
    """DescribeMonitorResourceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PhoneAlarmNumber: 电话告警数量
        :type PhoneAlarmNumber: int
        :param _AdvancedMetricNumber: 高级指标数量
        :type AdvancedMetricNumber: int
        :param _APIUsageNumber: API调用量
        :type APIUsageNumber: int
        :param _AlarmSMSNumber: 告警短信数量
        :type AlarmSMSNumber: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PhoneAlarmNumber = None
        self._AdvancedMetricNumber = None
        self._APIUsageNumber = None
        self._AlarmSMSNumber = None
        self._RequestId = None

    @property
    def PhoneAlarmNumber(self):
        return self._PhoneAlarmNumber

    @PhoneAlarmNumber.setter
    def PhoneAlarmNumber(self, PhoneAlarmNumber):
        self._PhoneAlarmNumber = PhoneAlarmNumber

    @property
    def AdvancedMetricNumber(self):
        return self._AdvancedMetricNumber

    @AdvancedMetricNumber.setter
    def AdvancedMetricNumber(self, AdvancedMetricNumber):
        self._AdvancedMetricNumber = AdvancedMetricNumber

    @property
    def APIUsageNumber(self):
        return self._APIUsageNumber

    @APIUsageNumber.setter
    def APIUsageNumber(self, APIUsageNumber):
        self._APIUsageNumber = APIUsageNumber

    @property
    def AlarmSMSNumber(self):
        return self._AlarmSMSNumber

    @AlarmSMSNumber.setter
    def AlarmSMSNumber(self, AlarmSMSNumber):
        self._AlarmSMSNumber = AlarmSMSNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PhoneAlarmNumber = params.get("PhoneAlarmNumber")
        self._AdvancedMetricNumber = params.get("AdvancedMetricNumber")
        self._APIUsageNumber = params.get("APIUsageNumber")
        self._AlarmSMSNumber = params.get("AlarmSMSNumber")
        self._RequestId = params.get("RequestId")


class DescribeMonitorTypesRequest(AbstractModel):
    """DescribeMonitorTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定值 monitor
        :type Module: str
        """
        self._Module = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        self._Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorTypesResponse(AbstractModel):
    """DescribeMonitorTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorTypes: 监控类型，云产品监控为 MT_QCE
        :type MonitorTypes: list of str
        :param _MonitorTypeInfos: 监控类型详情
        :type MonitorTypeInfos: list of MonitorTypeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorTypes = None
        self._MonitorTypeInfos = None
        self._RequestId = None

    @property
    def MonitorTypes(self):
        return self._MonitorTypes

    @MonitorTypes.setter
    def MonitorTypes(self, MonitorTypes):
        self._MonitorTypes = MonitorTypes

    @property
    def MonitorTypeInfos(self):
        return self._MonitorTypeInfos

    @MonitorTypeInfos.setter
    def MonitorTypeInfos(self, MonitorTypeInfos):
        self._MonitorTypeInfos = MonitorTypeInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MonitorTypes = params.get("MonitorTypes")
        if params.get("MonitorTypeInfos") is not None:
            self._MonitorTypeInfos = []
            for item in params.get("MonitorTypeInfos"):
                obj = MonitorTypeInfo()
                obj._deserialize(item)
                self._MonitorTypeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePhoneAlarmFlowTotalCountRequest(AbstractModel):
    """DescribePhoneAlarmFlowTotalCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 默认monitor
        :type Module: str
        :param _QueryTime: unix时间戳，单位：s
        :type QueryTime: int
        """
        self._Module = None
        self._QueryTime = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._QueryTime = params.get("QueryTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePhoneAlarmFlowTotalCountResponse(AbstractModel):
    """DescribePhoneAlarmFlowTotalCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 电话流水总数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribePluginOverviewsRequest(AbstractModel):
    """DescribePluginOverviews请求参数结构体

    """


class DescribePluginOverviewsResponse(AbstractModel):
    """DescribePluginOverviews返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginSet: 插件列表
        :type PluginSet: list of GrafanaPlugin
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PluginSet = None
        self._RequestId = None

    @property
    def PluginSet(self):
        return self._PluginSet

    @PluginSet.setter
    def PluginSet(self, PluginSet):
        self._PluginSet = PluginSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PluginSet") is not None:
            self._PluginSet = []
            for item in params.get("PluginSet"):
                obj = GrafanaPlugin()
                obj._deserialize(item)
                self._PluginSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePolicyConditionListCondition(AbstractModel):
    """DescribePolicyConditionList策略条件

    """

    def __init__(self):
        r"""
        :param _PolicyViewName: 策略视图名称
        :type PolicyViewName: str
        :param _EventMetrics: 事件告警条件
注意：此字段可能返回 null，表示取不到有效值。
        :type EventMetrics: list of DescribePolicyConditionListEventMetric
        :param _IsSupportMultiRegion: 是否支持多地域
        :type IsSupportMultiRegion: bool
        :param _Metrics: 指标告警条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of DescribePolicyConditionListMetric
        :param _Name: 策略类型名称
        :type Name: str
        :param _SortId: 排序id
        :type SortId: int
        :param _SupportDefault: 是否支持默认策略
        :type SupportDefault: bool
        :param _SupportRegions: 支持该策略类型的地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportRegions: list of str
        :param _DeprecatingInfo: 弃用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DeprecatingInfo: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListResponseDeprecatingInfo`
        """
        self._PolicyViewName = None
        self._EventMetrics = None
        self._IsSupportMultiRegion = None
        self._Metrics = None
        self._Name = None
        self._SortId = None
        self._SupportDefault = None
        self._SupportRegions = None
        self._DeprecatingInfo = None

    @property
    def PolicyViewName(self):
        return self._PolicyViewName

    @PolicyViewName.setter
    def PolicyViewName(self, PolicyViewName):
        self._PolicyViewName = PolicyViewName

    @property
    def EventMetrics(self):
        return self._EventMetrics

    @EventMetrics.setter
    def EventMetrics(self, EventMetrics):
        self._EventMetrics = EventMetrics

    @property
    def IsSupportMultiRegion(self):
        return self._IsSupportMultiRegion

    @IsSupportMultiRegion.setter
    def IsSupportMultiRegion(self, IsSupportMultiRegion):
        self._IsSupportMultiRegion = IsSupportMultiRegion

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def SupportDefault(self):
        return self._SupportDefault

    @SupportDefault.setter
    def SupportDefault(self, SupportDefault):
        self._SupportDefault = SupportDefault

    @property
    def SupportRegions(self):
        return self._SupportRegions

    @SupportRegions.setter
    def SupportRegions(self, SupportRegions):
        self._SupportRegions = SupportRegions

    @property
    def DeprecatingInfo(self):
        return self._DeprecatingInfo

    @DeprecatingInfo.setter
    def DeprecatingInfo(self, DeprecatingInfo):
        self._DeprecatingInfo = DeprecatingInfo


    def _deserialize(self, params):
        self._PolicyViewName = params.get("PolicyViewName")
        if params.get("EventMetrics") is not None:
            self._EventMetrics = []
            for item in params.get("EventMetrics"):
                obj = DescribePolicyConditionListEventMetric()
                obj._deserialize(item)
                self._EventMetrics.append(obj)
        self._IsSupportMultiRegion = params.get("IsSupportMultiRegion")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = DescribePolicyConditionListMetric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._Name = params.get("Name")
        self._SortId = params.get("SortId")
        self._SupportDefault = params.get("SupportDefault")
        self._SupportRegions = params.get("SupportRegions")
        if params.get("DeprecatingInfo") is not None:
            self._DeprecatingInfo = DescribePolicyConditionListResponseDeprecatingInfo()
            self._DeprecatingInfo._deserialize(params.get("DeprecatingInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManual(AbstractModel):
    """DescribePolicyConditionList.ConfigManual

    """

    def __init__(self):
        r"""
        :param _CalcType: 检测方式
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcType`
        :param _CalcValue: 检测阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcValue: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcValue`
        :param _ContinueTime: 持续时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueTime: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualContinueTime`
        :param _Period: 数据周期
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriod`
        :param _PeriodNum: 持续周期个数
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodNum: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriodNum`
        :param _StatType: 聚合方式
注意：此字段可能返回 null，表示取不到有效值。
        :type StatType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualStatType`
        """
        self._CalcType = None
        self._CalcValue = None
        self._ContinueTime = None
        self._Period = None
        self._PeriodNum = None
        self._StatType = None

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def ContinueTime(self):
        return self._ContinueTime

    @ContinueTime.setter
    def ContinueTime(self, ContinueTime):
        self._ContinueTime = ContinueTime

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def PeriodNum(self):
        return self._PeriodNum

    @PeriodNum.setter
    def PeriodNum(self, PeriodNum):
        self._PeriodNum = PeriodNum

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType


    def _deserialize(self, params):
        if params.get("CalcType") is not None:
            self._CalcType = DescribePolicyConditionListConfigManualCalcType()
            self._CalcType._deserialize(params.get("CalcType"))
        if params.get("CalcValue") is not None:
            self._CalcValue = DescribePolicyConditionListConfigManualCalcValue()
            self._CalcValue._deserialize(params.get("CalcValue"))
        if params.get("ContinueTime") is not None:
            self._ContinueTime = DescribePolicyConditionListConfigManualContinueTime()
            self._ContinueTime._deserialize(params.get("ContinueTime"))
        if params.get("Period") is not None:
            self._Period = DescribePolicyConditionListConfigManualPeriod()
            self._Period._deserialize(params.get("Period"))
        if params.get("PeriodNum") is not None:
            self._PeriodNum = DescribePolicyConditionListConfigManualPeriodNum()
            self._PeriodNum._deserialize(params.get("PeriodNum"))
        if params.get("StatType") is not None:
            self._StatType = DescribePolicyConditionListConfigManualStatType()
            self._StatType._deserialize(params.get("StatType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualCalcType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcType

    """

    def __init__(self):
        r"""
        :param _Keys: CalcType 取值
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param _Need: 是否必须
        :type Need: bool
        """
        self._Keys = None
        self._Need = None

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Keys = params.get("Keys")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualCalcValue(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcValue

    """

    def __init__(self):
        r"""
        :param _Default: 默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: str
        :param _Fixed: 固定值
注意：此字段可能返回 null，表示取不到有效值。
        :type Fixed: str
        :param _Max: 最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: str
        :param _Min: 最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: str
        :param _Need: 是否必须
        :type Need: bool
        """
        self._Default = None
        self._Fixed = None
        self._Max = None
        self._Min = None
        self._Need = None

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Fixed(self):
        return self._Fixed

    @Fixed.setter
    def Fixed(self, Fixed):
        self._Fixed = Fixed

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
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Fixed = params.get("Fixed")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualContinueTime(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.ContinueTime

    """

    def __init__(self):
        r"""
        :param _Default: 默认持续时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: int
        :param _Keys: 可选持续时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param _Need: 是否必须
        :type Need: bool
        """
        self._Default = None
        self._Keys = None
        self._Need = None

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Keys = params.get("Keys")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualPeriod(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.Period

    """

    def __init__(self):
        r"""
        :param _Default: 默认周期，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: int
        :param _Keys: 可选周期，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param _Need: 是否必须
        :type Need: bool
        """
        self._Default = None
        self._Keys = None
        self._Need = None

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Keys = params.get("Keys")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualPeriodNum(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.PeriodNum

    """

    def __init__(self):
        r"""
        :param _Default: 默认周期数
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: int
        :param _Keys: 可选周期数
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param _Need: 是否必须
        :type Need: bool
        """
        self._Default = None
        self._Keys = None
        self._Need = None

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Keys = params.get("Keys")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualStatType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.StatType

    """

    def __init__(self):
        r"""
        :param _P5: 数据聚合方式，周期5秒
注意：此字段可能返回 null，表示取不到有效值。
        :type P5: str
        :param _P10: 数据聚合方式，周期10秒
注意：此字段可能返回 null，表示取不到有效值。
        :type P10: str
        :param _P60: 数据聚合方式，周期1分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type P60: str
        :param _P300: 数据聚合方式，周期5分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type P300: str
        :param _P600: 数据聚合方式，周期10分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type P600: str
        :param _P1800: 数据聚合方式，周期30分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type P1800: str
        :param _P3600: 数据聚合方式，周期1小时
注意：此字段可能返回 null，表示取不到有效值。
        :type P3600: str
        :param _P86400: 数据聚合方式，周期1天
注意：此字段可能返回 null，表示取不到有效值。
        :type P86400: str
        """
        self._P5 = None
        self._P10 = None
        self._P60 = None
        self._P300 = None
        self._P600 = None
        self._P1800 = None
        self._P3600 = None
        self._P86400 = None

    @property
    def P5(self):
        return self._P5

    @P5.setter
    def P5(self, P5):
        self._P5 = P5

    @property
    def P10(self):
        return self._P10

    @P10.setter
    def P10(self, P10):
        self._P10 = P10

    @property
    def P60(self):
        return self._P60

    @P60.setter
    def P60(self, P60):
        self._P60 = P60

    @property
    def P300(self):
        return self._P300

    @P300.setter
    def P300(self, P300):
        self._P300 = P300

    @property
    def P600(self):
        return self._P600

    @P600.setter
    def P600(self, P600):
        self._P600 = P600

    @property
    def P1800(self):
        return self._P1800

    @P1800.setter
    def P1800(self, P1800):
        self._P1800 = P1800

    @property
    def P3600(self):
        return self._P3600

    @P3600.setter
    def P3600(self, P3600):
        self._P3600 = P3600

    @property
    def P86400(self):
        return self._P86400

    @P86400.setter
    def P86400(self, P86400):
        self._P86400 = P86400


    def _deserialize(self, params):
        self._P5 = params.get("P5")
        self._P10 = params.get("P10")
        self._P60 = params.get("P60")
        self._P300 = params.get("P300")
        self._P600 = params.get("P600")
        self._P1800 = params.get("P1800")
        self._P3600 = params.get("P3600")
        self._P86400 = params.get("P86400")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListEventMetric(AbstractModel):
    """DescribePolicyConditionList.EventMetric

    """

    def __init__(self):
        r"""
        :param _EventId: 事件id
        :type EventId: int
        :param _EventShowName: 事件名称
        :type EventShowName: str
        :param _NeedRecovered: 是否需要恢复
        :type NeedRecovered: bool
        :param _Type: 事件类型，预留字段，当前固定取值为2
        :type Type: int
        """
        self._EventId = None
        self._EventShowName = None
        self._NeedRecovered = None
        self._Type = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def EventShowName(self):
        return self._EventShowName

    @EventShowName.setter
    def EventShowName(self, EventShowName):
        self._EventShowName = EventShowName

    @property
    def NeedRecovered(self):
        return self._NeedRecovered

    @NeedRecovered.setter
    def NeedRecovered(self, NeedRecovered):
        self._NeedRecovered = NeedRecovered

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._EventShowName = params.get("EventShowName")
        self._NeedRecovered = params.get("NeedRecovered")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListMetric(AbstractModel):
    """指标告警配置

    """

    def __init__(self):
        r"""
        :param _ConfigManual: 指标配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigManual: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManual`
        :param _MetricId: 指标id
        :type MetricId: int
        :param _MetricShowName: 指标名称
        :type MetricShowName: str
        :param _MetricUnit: 指标单位
        :type MetricUnit: str
        """
        self._ConfigManual = None
        self._MetricId = None
        self._MetricShowName = None
        self._MetricUnit = None

    @property
    def ConfigManual(self):
        return self._ConfigManual

    @ConfigManual.setter
    def ConfigManual(self, ConfigManual):
        self._ConfigManual = ConfigManual

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def MetricShowName(self):
        return self._MetricShowName

    @MetricShowName.setter
    def MetricShowName(self, MetricShowName):
        self._MetricShowName = MetricShowName

    @property
    def MetricUnit(self):
        return self._MetricUnit

    @MetricUnit.setter
    def MetricUnit(self, MetricUnit):
        self._MetricUnit = MetricUnit


    def _deserialize(self, params):
        if params.get("ConfigManual") is not None:
            self._ConfigManual = DescribePolicyConditionListConfigManual()
            self._ConfigManual._deserialize(params.get("ConfigManual"))
        self._MetricId = params.get("MetricId")
        self._MetricShowName = params.get("MetricShowName")
        self._MetricUnit = params.get("MetricUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListRequest(AbstractModel):
    """DescribePolicyConditionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        """
        self._Module = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        self._Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListResponse(AbstractModel):
    """DescribePolicyConditionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Conditions: 告警策略条件列表
        :type Conditions: list of DescribePolicyConditionListCondition
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Conditions = None
        self._RequestId = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyConditionListCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePolicyConditionListResponseDeprecatingInfo(AbstractModel):
    """DescribePolicyConditionListResponseDeprecatingInfo

    """

    def __init__(self):
        r"""
        :param _Hidden: 是否隐藏
注意：此字段可能返回 null，表示取不到有效值。
        :type Hidden: bool
        :param _NewViewNames: 新视图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NewViewNames: list of str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._Hidden = None
        self._NewViewNames = None
        self._Description = None

    @property
    def Hidden(self):
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden

    @property
    def NewViewNames(self):
        return self._NewViewNames

    @NewViewNames.setter
    def NewViewNames(self, NewViewNames):
        self._NewViewNames = NewViewNames

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Hidden = params.get("Hidden")
        self._NewViewNames = params.get("NewViewNames")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoCallback(AbstractModel):
    """查询策略输出的用户回调信息

    """

    def __init__(self):
        r"""
        :param _CallbackUrl: 用户回调接口地址
        :type CallbackUrl: str
        :param _ValidFlag: 用户回调接口状态，0表示未验证，1表示已验证，2表示存在url但没有通过验证
        :type ValidFlag: int
        :param _VerifyCode: 用户回调接口验证码
        :type VerifyCode: str
        """
        self._CallbackUrl = None
        self._ValidFlag = None
        self._VerifyCode = None

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def ValidFlag(self):
        return self._ValidFlag

    @ValidFlag.setter
    def ValidFlag(self, ValidFlag):
        self._ValidFlag = ValidFlag

    @property
    def VerifyCode(self):
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode


    def _deserialize(self, params):
        self._CallbackUrl = params.get("CallbackUrl")
        self._ValidFlag = params.get("ValidFlag")
        self._VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoCondition(AbstractModel):
    """查询策略输出的阈值告警条件

    """

    def __init__(self):
        r"""
        :param _MetricShowName: 指标名称
        :type MetricShowName: str
        :param _Period: 数据聚合周期(单位秒)
        :type Period: int
        :param _MetricId: 指标id
        :type MetricId: int
        :param _RuleId: 阈值规则id
        :type RuleId: int
        :param _Unit: 指标单位
        :type Unit: str
        :param _AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param _CalcType: 比较类型，1表示大于，2表示大于等于，3表示小于，4表示小于等于，5表示相等，6表示不相等，7表示日同比上涨，8表示日同比下降，9表示周同比上涨，10表示周同比下降，11表示周期环比上涨，12表示周期环比下降
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcType: int
        :param _CalcValue: 检测阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcValue: str
        :param _ContinueTime: 持续多长时间触发规则会告警(单位秒)
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueTime: int
        :param _MetricName: 告警指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        """
        self._MetricShowName = None
        self._Period = None
        self._MetricId = None
        self._RuleId = None
        self._Unit = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._CalcType = None
        self._CalcValue = None
        self._ContinueTime = None
        self._MetricName = None

    @property
    def MetricShowName(self):
        return self._MetricShowName

    @MetricShowName.setter
    def MetricShowName(self, MetricShowName):
        self._MetricShowName = MetricShowName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def ContinueTime(self):
        return self._ContinueTime

    @ContinueTime.setter
    def ContinueTime(self, ContinueTime):
        self._ContinueTime = ContinueTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName


    def _deserialize(self, params):
        self._MetricShowName = params.get("MetricShowName")
        self._Period = params.get("Period")
        self._MetricId = params.get("MetricId")
        self._RuleId = params.get("RuleId")
        self._Unit = params.get("Unit")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._CalcType = params.get("CalcType")
        self._CalcValue = params.get("CalcValue")
        self._ContinueTime = params.get("ContinueTime")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoConditionTpl(AbstractModel):
    """查询策略输出的模板策略组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 策略组id
        :type GroupId: int
        :param _GroupName: 策略组名称
        :type GroupName: str
        :param _ViewName: 策略类型
        :type ViewName: str
        :param _Remark: 策略组说明
        :type Remark: str
        :param _LastEditUin: 最后编辑的用户uin
        :type LastEditUin: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _InsertTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: int
        :param _IsUnionRule: 是否且规则
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        """
        self._GroupId = None
        self._GroupName = None
        self._ViewName = None
        self._Remark = None
        self._LastEditUin = None
        self._UpdateTime = None
        self._InsertTime = None
        self._IsUnionRule = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ViewName = params.get("ViewName")
        self._Remark = params.get("Remark")
        self._LastEditUin = params.get("LastEditUin")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoEventCondition(AbstractModel):
    """查询策略输出的事件告警条件

    """

    def __init__(self):
        r"""
        :param _EventId: 事件id
        :type EventId: int
        :param _RuleId: 事件告警规则id
        :type RuleId: int
        :param _EventShowName: 事件名称
        :type EventShowName: str
        :param _AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param _AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        """
        self._EventId = None
        self._RuleId = None
        self._EventShowName = None
        self._AlarmNotifyPeriod = None
        self._AlarmNotifyType = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def EventShowName(self):
        return self._EventShowName

    @EventShowName.setter
    def EventShowName(self, EventShowName):
        self._EventShowName = EventShowName

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._RuleId = params.get("RuleId")
        self._EventShowName = params.get("EventShowName")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoReceiverInfo(AbstractModel):
    """查询策略输出的告警接收人信息

    """

    def __init__(self):
        r"""
        :param _ReceiverGroupList: 告警接收组id列表
        :type ReceiverGroupList: list of int
        :param _ReceiverUserList: 告警接收人id列表
        :type ReceiverUserList: list of int
        :param _StartTime: 告警时间段开始时间。范围[0,86400)，作为 UNIX 时间戳转成北京时间后去掉日期，例如7200表示"10:0:0"
        :type StartTime: int
        :param _EndTime: 告警时间段结束时间。含义同StartTime
        :type EndTime: int
        :param _ReceiverType: 接收类型。“group”(接收组)或“user”(接收人)
        :type ReceiverType: str
        :param _NotifyWay: 告警通知方式。可选 "SMS","SITE","EMAIL","CALL","WECHAT"
        :type NotifyWay: list of str
        :param _UidList: 电话告警接收者uid
注意：此字段可能返回 null，表示取不到有效值。
        :type UidList: list of int
        :param _RoundNumber: 电话告警轮数
        :type RoundNumber: int
        :param _RoundInterval: 电话告警每轮间隔（秒）
        :type RoundInterval: int
        :param _PersonInterval: 电话告警对个人间隔（秒）
        :type PersonInterval: int
        :param _NeedSendNotice: 是否需要电话告警触达提示。0不需要，1需要
        :type NeedSendNotice: int
        :param _SendFor: 电话告警通知时机。可选"OCCUR"(告警时通知),"RECOVER"(恢复时通知)
        :type SendFor: list of str
        :param _RecoverNotify: 恢复通知方式。可选"SMS"
        :type RecoverNotify: list of str
        :param _ReceiveLanguage: 告警发送语言
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiveLanguage: str
        """
        self._ReceiverGroupList = None
        self._ReceiverUserList = None
        self._StartTime = None
        self._EndTime = None
        self._ReceiverType = None
        self._NotifyWay = None
        self._UidList = None
        self._RoundNumber = None
        self._RoundInterval = None
        self._PersonInterval = None
        self._NeedSendNotice = None
        self._SendFor = None
        self._RecoverNotify = None
        self._ReceiveLanguage = None

    @property
    def ReceiverGroupList(self):
        return self._ReceiverGroupList

    @ReceiverGroupList.setter
    def ReceiverGroupList(self, ReceiverGroupList):
        self._ReceiverGroupList = ReceiverGroupList

    @property
    def ReceiverUserList(self):
        return self._ReceiverUserList

    @ReceiverUserList.setter
    def ReceiverUserList(self, ReceiverUserList):
        self._ReceiverUserList = ReceiverUserList

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
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def UidList(self):
        return self._UidList

    @UidList.setter
    def UidList(self, UidList):
        self._UidList = UidList

    @property
    def RoundNumber(self):
        return self._RoundNumber

    @RoundNumber.setter
    def RoundNumber(self, RoundNumber):
        self._RoundNumber = RoundNumber

    @property
    def RoundInterval(self):
        return self._RoundInterval

    @RoundInterval.setter
    def RoundInterval(self, RoundInterval):
        self._RoundInterval = RoundInterval

    @property
    def PersonInterval(self):
        return self._PersonInterval

    @PersonInterval.setter
    def PersonInterval(self, PersonInterval):
        self._PersonInterval = PersonInterval

    @property
    def NeedSendNotice(self):
        return self._NeedSendNotice

    @NeedSendNotice.setter
    def NeedSendNotice(self, NeedSendNotice):
        self._NeedSendNotice = NeedSendNotice

    @property
    def SendFor(self):
        return self._SendFor

    @SendFor.setter
    def SendFor(self, SendFor):
        self._SendFor = SendFor

    @property
    def RecoverNotify(self):
        return self._RecoverNotify

    @RecoverNotify.setter
    def RecoverNotify(self, RecoverNotify):
        self._RecoverNotify = RecoverNotify

    @property
    def ReceiveLanguage(self):
        return self._ReceiveLanguage

    @ReceiveLanguage.setter
    def ReceiveLanguage(self, ReceiveLanguage):
        self._ReceiveLanguage = ReceiveLanguage


    def _deserialize(self, params):
        self._ReceiverGroupList = params.get("ReceiverGroupList")
        self._ReceiverUserList = params.get("ReceiverUserList")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReceiverType = params.get("ReceiverType")
        self._NotifyWay = params.get("NotifyWay")
        self._UidList = params.get("UidList")
        self._RoundNumber = params.get("RoundNumber")
        self._RoundInterval = params.get("RoundInterval")
        self._PersonInterval = params.get("PersonInterval")
        self._NeedSendNotice = params.get("NeedSendNotice")
        self._SendFor = params.get("SendFor")
        self._RecoverNotify = params.get("RecoverNotify")
        self._ReceiveLanguage = params.get("ReceiveLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoRequest(AbstractModel):
    """DescribePolicyGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _GroupId: 策略组id
        :type GroupId: int
        """
        self._Module = None
        self._GroupId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoResponse(AbstractModel):
    """DescribePolicyGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 策略组名称
        :type GroupName: str
        :param _ProjectId: 策略组所属的项目id
        :type ProjectId: int
        :param _IsDefault: 是否为默认策略，0表示非默认策略，1表示默认策略
        :type IsDefault: int
        :param _ViewName: 策略类型
        :type ViewName: str
        :param _Remark: 策略说明
        :type Remark: str
        :param _ShowName: 策略类型名称
        :type ShowName: str
        :param _LastEditUin: 最近编辑的用户uin
        :type LastEditUin: str
        :param _UpdateTime: 最近编辑时间
        :type UpdateTime: str
        :param _Region: 该策略支持的地域
        :type Region: list of str
        :param _DimensionGroup: 策略类型的维度列表
        :type DimensionGroup: list of str
        :param _ConditionsConfig: 阈值规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionsConfig: list of DescribePolicyGroupInfoCondition
        :param _EventConfig: 产品事件规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventConfig: list of DescribePolicyGroupInfoEventCondition
        :param _ReceiverInfos: 用户接收人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param _Callback: 用户回调信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Callback: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoCallback`
        :param _ConditionsTemp: 模板策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param _CanSetDefault: 是否可以设置成默认策略
        :type CanSetDefault: bool
        :param _IsUnionRule: 是否且规则
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupName = None
        self._ProjectId = None
        self._IsDefault = None
        self._ViewName = None
        self._Remark = None
        self._ShowName = None
        self._LastEditUin = None
        self._UpdateTime = None
        self._Region = None
        self._DimensionGroup = None
        self._ConditionsConfig = None
        self._EventConfig = None
        self._ReceiverInfos = None
        self._Callback = None
        self._ConditionsTemp = None
        self._CanSetDefault = None
        self._IsUnionRule = None
        self._RequestId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ShowName(self):
        return self._ShowName

    @ShowName.setter
    def ShowName(self, ShowName):
        self._ShowName = ShowName

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DimensionGroup(self):
        return self._DimensionGroup

    @DimensionGroup.setter
    def DimensionGroup(self, DimensionGroup):
        self._DimensionGroup = DimensionGroup

    @property
    def ConditionsConfig(self):
        return self._ConditionsConfig

    @ConditionsConfig.setter
    def ConditionsConfig(self, ConditionsConfig):
        self._ConditionsConfig = ConditionsConfig

    @property
    def EventConfig(self):
        return self._EventConfig

    @EventConfig.setter
    def EventConfig(self, EventConfig):
        self._EventConfig = EventConfig

    @property
    def ReceiverInfos(self):
        return self._ReceiverInfos

    @ReceiverInfos.setter
    def ReceiverInfos(self, ReceiverInfos):
        self._ReceiverInfos = ReceiverInfos

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def ConditionsTemp(self):
        return self._ConditionsTemp

    @ConditionsTemp.setter
    def ConditionsTemp(self, ConditionsTemp):
        self._ConditionsTemp = ConditionsTemp

    @property
    def CanSetDefault(self):
        return self._CanSetDefault

    @CanSetDefault.setter
    def CanSetDefault(self, CanSetDefault):
        self._CanSetDefault = CanSetDefault

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._ProjectId = params.get("ProjectId")
        self._IsDefault = params.get("IsDefault")
        self._ViewName = params.get("ViewName")
        self._Remark = params.get("Remark")
        self._ShowName = params.get("ShowName")
        self._LastEditUin = params.get("LastEditUin")
        self._UpdateTime = params.get("UpdateTime")
        self._Region = params.get("Region")
        self._DimensionGroup = params.get("DimensionGroup")
        if params.get("ConditionsConfig") is not None:
            self._ConditionsConfig = []
            for item in params.get("ConditionsConfig"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self._ConditionsConfig.append(obj)
        if params.get("EventConfig") is not None:
            self._EventConfig = []
            for item in params.get("EventConfig"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self._EventConfig.append(obj)
        if params.get("ReceiverInfos") is not None:
            self._ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self._ReceiverInfos.append(obj)
        if params.get("Callback") is not None:
            self._Callback = DescribePolicyGroupInfoCallback()
            self._Callback._deserialize(params.get("Callback"))
        if params.get("ConditionsTemp") is not None:
            self._ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self._ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self._CanSetDefault = params.get("CanSetDefault")
        self._IsUnionRule = params.get("IsUnionRule")
        self._RequestId = params.get("RequestId")


class DescribePolicyGroupListGroup(AbstractModel):
    """DescribePolicyGroupList.Group

    """

    def __init__(self):
        r"""
        :param _GroupId: 策略组id
        :type GroupId: int
        :param _GroupName: 策略组名称
        :type GroupName: str
        :param _IsOpen: 是否开启
        :type IsOpen: bool
        :param _ViewName: 策略视图名称
        :type ViewName: str
        :param _LastEditUin: 最近编辑的用户uin
        :type LastEditUin: str
        :param _UpdateTime: 最后修改时间
        :type UpdateTime: int
        :param _InsertTime: 创建时间
        :type InsertTime: int
        :param _UseSum: 策略组绑定的实例数
        :type UseSum: int
        :param _NoShieldedSum: 策略组绑定的未屏蔽实例数
        :type NoShieldedSum: int
        :param _IsDefault: 是否为默认策略，0表示非默认策略，1表示默认策略
        :type IsDefault: int
        :param _CanSetDefault: 是否可以设置成默认策略
        :type CanSetDefault: bool
        :param _ParentGroupId: 父策略组id
        :type ParentGroupId: int
        :param _Remark: 策略组备注
        :type Remark: str
        :param _ProjectId: 策略组所属项目id
        :type ProjectId: int
        :param _Conditions: 阈值规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of DescribePolicyGroupInfoCondition
        :param _EventConditions: 产品事件规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventConditions: list of DescribePolicyGroupInfoEventCondition
        :param _ReceiverInfos: 用户接收人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param _ConditionsTemp: 模板策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param _InstanceGroup: 策略组绑定的实例组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListGroupInstanceGroup`
        :param _IsUnionRule: 且或规则标识, 0表示或规则(任意一条规则满足阈值条件就告警), 1表示且规则(所有规则都满足阈值条件才告警)
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        """
        self._GroupId = None
        self._GroupName = None
        self._IsOpen = None
        self._ViewName = None
        self._LastEditUin = None
        self._UpdateTime = None
        self._InsertTime = None
        self._UseSum = None
        self._NoShieldedSum = None
        self._IsDefault = None
        self._CanSetDefault = None
        self._ParentGroupId = None
        self._Remark = None
        self._ProjectId = None
        self._Conditions = None
        self._EventConditions = None
        self._ReceiverInfos = None
        self._ConditionsTemp = None
        self._InstanceGroup = None
        self._IsUnionRule = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def UseSum(self):
        return self._UseSum

    @UseSum.setter
    def UseSum(self, UseSum):
        self._UseSum = UseSum

    @property
    def NoShieldedSum(self):
        return self._NoShieldedSum

    @NoShieldedSum.setter
    def NoShieldedSum(self, NoShieldedSum):
        self._NoShieldedSum = NoShieldedSum

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def CanSetDefault(self):
        return self._CanSetDefault

    @CanSetDefault.setter
    def CanSetDefault(self, CanSetDefault):
        self._CanSetDefault = CanSetDefault

    @property
    def ParentGroupId(self):
        return self._ParentGroupId

    @ParentGroupId.setter
    def ParentGroupId(self, ParentGroupId):
        self._ParentGroupId = ParentGroupId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def EventConditions(self):
        return self._EventConditions

    @EventConditions.setter
    def EventConditions(self, EventConditions):
        self._EventConditions = EventConditions

    @property
    def ReceiverInfos(self):
        return self._ReceiverInfos

    @ReceiverInfos.setter
    def ReceiverInfos(self, ReceiverInfos):
        self._ReceiverInfos = ReceiverInfos

    @property
    def ConditionsTemp(self):
        return self._ConditionsTemp

    @ConditionsTemp.setter
    def ConditionsTemp(self, ConditionsTemp):
        self._ConditionsTemp = ConditionsTemp

    @property
    def InstanceGroup(self):
        return self._InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, InstanceGroup):
        self._InstanceGroup = InstanceGroup

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._IsOpen = params.get("IsOpen")
        self._ViewName = params.get("ViewName")
        self._LastEditUin = params.get("LastEditUin")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        self._UseSum = params.get("UseSum")
        self._NoShieldedSum = params.get("NoShieldedSum")
        self._IsDefault = params.get("IsDefault")
        self._CanSetDefault = params.get("CanSetDefault")
        self._ParentGroupId = params.get("ParentGroupId")
        self._Remark = params.get("Remark")
        self._ProjectId = params.get("ProjectId")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self._EventConditions = []
            for item in params.get("EventConditions"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self._EventConditions.append(obj)
        if params.get("ReceiverInfos") is not None:
            self._ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self._ReceiverInfos.append(obj)
        if params.get("ConditionsTemp") is not None:
            self._ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self._ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        if params.get("InstanceGroup") is not None:
            self._InstanceGroup = DescribePolicyGroupListGroupInstanceGroup()
            self._InstanceGroup._deserialize(params.get("InstanceGroup"))
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListGroupInstanceGroup(AbstractModel):
    """DescribePolicyGroupList接口策略组绑定的实例分组信息

    """

    def __init__(self):
        r"""
        :param _InstanceGroupId: 实例分组名称id
        :type InstanceGroupId: int
        :param _ViewName: 策略类型视图名称
        :type ViewName: str
        :param _LastEditUin: 最近编辑的用户uin
        :type LastEditUin: str
        :param _GroupName: 实例分组名称
        :type GroupName: str
        :param _InstanceSum: 实例数量
        :type InstanceSum: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        :param _InsertTime: 创建时间
        :type InsertTime: int
        """
        self._InstanceGroupId = None
        self._ViewName = None
        self._LastEditUin = None
        self._GroupName = None
        self._InstanceSum = None
        self._UpdateTime = None
        self._InsertTime = None

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceSum(self):
        return self._InstanceSum

    @InstanceSum.setter
    def InstanceSum(self, InstanceSum):
        self._InstanceSum = InstanceSum

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime


    def _deserialize(self, params):
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._ViewName = params.get("ViewName")
        self._LastEditUin = params.get("LastEditUin")
        self._GroupName = params.get("GroupName")
        self._InstanceSum = params.get("InstanceSum")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListRequest(AbstractModel):
    """DescribePolicyGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _Limit: 分页参数，每页返回的数量，取值1~100
        :type Limit: int
        :param _Offset: 分页参数，页偏移量，从0开始计数
        :type Offset: int
        :param _Like: 按策略名搜索
        :type Like: str
        :param _InstanceGroupId: 实例分组id
        :type InstanceGroupId: int
        :param _UpdateTimeOrder: 按更新时间排序, asc 或者 desc
        :type UpdateTimeOrder: str
        :param _ProjectIds: 项目id列表
        :type ProjectIds: list of int
        :param _ViewNames: 告警策略类型列表
        :type ViewNames: list of str
        :param _FilterUnuseReceiver: 是否过滤无接收人策略组, 1表示过滤, 0表示不过滤
        :type FilterUnuseReceiver: int
        :param _Receivers: 过滤条件, 接收组列表
        :type Receivers: list of str
        :param _ReceiverUserList: 过滤条件, 接收人列表
        :type ReceiverUserList: list of str
        :param _Dimensions: 维度组合字段(json字符串), 例如[[{"name":"unInstanceId","value":"ins-6e4b2aaa"}]]
        :type Dimensions: str
        :param _ConditionTempGroupId: 模板策略组id, 多个id用逗号分隔
        :type ConditionTempGroupId: str
        :param _ReceiverType: 过滤条件, 接收人或者接收组, user表示接收人, group表示接收组
        :type ReceiverType: str
        :param _IsOpen: 过滤条件，告警策略是否已启动或停止
        :type IsOpen: bool
        """
        self._Module = None
        self._Limit = None
        self._Offset = None
        self._Like = None
        self._InstanceGroupId = None
        self._UpdateTimeOrder = None
        self._ProjectIds = None
        self._ViewNames = None
        self._FilterUnuseReceiver = None
        self._Receivers = None
        self._ReceiverUserList = None
        self._Dimensions = None
        self._ConditionTempGroupId = None
        self._ReceiverType = None
        self._IsOpen = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

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
    def Like(self):
        return self._Like

    @Like.setter
    def Like(self, Like):
        self._Like = Like

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def UpdateTimeOrder(self):
        return self._UpdateTimeOrder

    @UpdateTimeOrder.setter
    def UpdateTimeOrder(self, UpdateTimeOrder):
        self._UpdateTimeOrder = UpdateTimeOrder

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ViewNames(self):
        return self._ViewNames

    @ViewNames.setter
    def ViewNames(self, ViewNames):
        self._ViewNames = ViewNames

    @property
    def FilterUnuseReceiver(self):
        return self._FilterUnuseReceiver

    @FilterUnuseReceiver.setter
    def FilterUnuseReceiver(self, FilterUnuseReceiver):
        self._FilterUnuseReceiver = FilterUnuseReceiver

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def ReceiverUserList(self):
        return self._ReceiverUserList

    @ReceiverUserList.setter
    def ReceiverUserList(self, ReceiverUserList):
        self._ReceiverUserList = ReceiverUserList

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def ConditionTempGroupId(self):
        return self._ConditionTempGroupId

    @ConditionTempGroupId.setter
    def ConditionTempGroupId(self, ConditionTempGroupId):
        self._ConditionTempGroupId = ConditionTempGroupId

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Like = params.get("Like")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._UpdateTimeOrder = params.get("UpdateTimeOrder")
        self._ProjectIds = params.get("ProjectIds")
        self._ViewNames = params.get("ViewNames")
        self._FilterUnuseReceiver = params.get("FilterUnuseReceiver")
        self._Receivers = params.get("Receivers")
        self._ReceiverUserList = params.get("ReceiverUserList")
        self._Dimensions = params.get("Dimensions")
        self._ConditionTempGroupId = params.get("ConditionTempGroupId")
        self._ReceiverType = params.get("ReceiverType")
        self._IsOpen = params.get("IsOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListResponse(AbstractModel):
    """DescribePolicyGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupList: 策略组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of DescribePolicyGroupListGroup
        :param _Total: 策略组总数
        :type Total: int
        :param _Warning: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Warning: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupList = None
        self._Total = None
        self._Warning = None
        self._RequestId = None

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Warning(self):
        return self._Warning

    @Warning.setter
    def Warning(self, Warning):
        self._Warning = Warning

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = DescribePolicyGroupListGroup()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._Total = params.get("Total")
        self._Warning = params.get("Warning")
        self._RequestId = params.get("RequestId")


class DescribeProductEventListDimensions(AbstractModel):
    """DescribeProductEventList的入参Dimensions

    """

    def __init__(self):
        r"""
        :param _Name: 维度名
        :type Name: str
        :param _Value: 维度值
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
        


class DescribeProductEventListEvents(AbstractModel):
    """DescribeProductEventList返回的Events

    """

    def __init__(self):
        r"""
        :param _EventId: 事件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: int
        :param _EventCName: 事件中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCName: str
        :param _EventEName: 事件英文名
注意：此字段可能返回 null，表示取不到有效值。
        :type EventEName: str
        :param _EventName: 事件简称
注意：此字段可能返回 null，表示取不到有效值。
        :type EventName: str
        :param _ProductCName: 产品中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCName: str
        :param _ProductEName: 产品英文名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductEName: str
        :param _ProductName: 产品简称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _SupportAlarm: 是否支持告警
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportAlarm: int
        :param _Type: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _Dimensions: 实例对象信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: list of DescribeProductEventListEventsDimensions
        :param _AdditionMsg: 实例对象附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AdditionMsg: list of DescribeProductEventListEventsDimensions
        :param _IsAlarmConfig: 是否配置告警
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAlarmConfig: int
        :param _GroupInfo: 策略信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupInfo: list of DescribeProductEventListEventsGroupInfo
        :param _ViewName: 显示名称ViewName
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        """
        self._EventId = None
        self._EventCName = None
        self._EventEName = None
        self._EventName = None
        self._ProductCName = None
        self._ProductEName = None
        self._ProductName = None
        self._InstanceId = None
        self._InstanceName = None
        self._ProjectId = None
        self._Region = None
        self._Status = None
        self._SupportAlarm = None
        self._Type = None
        self._StartTime = None
        self._UpdateTime = None
        self._Dimensions = None
        self._AdditionMsg = None
        self._IsAlarmConfig = None
        self._GroupInfo = None
        self._ViewName = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def EventCName(self):
        return self._EventCName

    @EventCName.setter
    def EventCName(self, EventCName):
        self._EventCName = EventCName

    @property
    def EventEName(self):
        return self._EventEName

    @EventEName.setter
    def EventEName(self, EventEName):
        self._EventEName = EventEName

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def ProductCName(self):
        return self._ProductCName

    @ProductCName.setter
    def ProductCName(self, ProductCName):
        self._ProductCName = ProductCName

    @property
    def ProductEName(self):
        return self._ProductEName

    @ProductEName.setter
    def ProductEName(self, ProductEName):
        self._ProductEName = ProductEName

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SupportAlarm(self):
        return self._SupportAlarm

    @SupportAlarm.setter
    def SupportAlarm(self, SupportAlarm):
        self._SupportAlarm = SupportAlarm

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
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def AdditionMsg(self):
        return self._AdditionMsg

    @AdditionMsg.setter
    def AdditionMsg(self, AdditionMsg):
        self._AdditionMsg = AdditionMsg

    @property
    def IsAlarmConfig(self):
        return self._IsAlarmConfig

    @IsAlarmConfig.setter
    def IsAlarmConfig(self, IsAlarmConfig):
        self._IsAlarmConfig = IsAlarmConfig

    @property
    def GroupInfo(self):
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._EventCName = params.get("EventCName")
        self._EventEName = params.get("EventEName")
        self._EventName = params.get("EventName")
        self._ProductCName = params.get("ProductCName")
        self._ProductEName = params.get("ProductEName")
        self._ProductName = params.get("ProductName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._SupportAlarm = params.get("SupportAlarm")
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        if params.get("AdditionMsg") is not None:
            self._AdditionMsg = []
            for item in params.get("AdditionMsg"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self._AdditionMsg.append(obj)
        self._IsAlarmConfig = params.get("IsAlarmConfig")
        if params.get("GroupInfo") is not None:
            self._GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = DescribeProductEventListEventsGroupInfo()
                obj._deserialize(item)
                self._GroupInfo.append(obj)
        self._ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListEventsDimensions(AbstractModel):
    """DescribeProductEventList返回的Events的Dimensions

    """

    def __init__(self):
        r"""
        :param _Key: 维度名（英文）
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Name: 维度名（中文）
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 维度值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Name = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

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
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListEventsGroupInfo(AbstractModel):
    """DescribeProductEventList返回的Events里的GroupInfo

    """

    def __init__(self):
        r"""
        :param _GroupId: 策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param _GroupName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self._GroupId = None
        self._GroupName = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListOverView(AbstractModel):
    """DescribeProductEventList返回的OverView对象

    """

    def __init__(self):
        r"""
        :param _StatusChangeAmount: 状态变更的事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusChangeAmount: int
        :param _UnConfigAlarmAmount: 告警状态未配置的事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnConfigAlarmAmount: int
        :param _UnNormalEventAmount: 异常事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnNormalEventAmount: int
        :param _UnRecoverAmount: 未恢复的事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnRecoverAmount: int
        """
        self._StatusChangeAmount = None
        self._UnConfigAlarmAmount = None
        self._UnNormalEventAmount = None
        self._UnRecoverAmount = None

    @property
    def StatusChangeAmount(self):
        return self._StatusChangeAmount

    @StatusChangeAmount.setter
    def StatusChangeAmount(self, StatusChangeAmount):
        self._StatusChangeAmount = StatusChangeAmount

    @property
    def UnConfigAlarmAmount(self):
        return self._UnConfigAlarmAmount

    @UnConfigAlarmAmount.setter
    def UnConfigAlarmAmount(self, UnConfigAlarmAmount):
        self._UnConfigAlarmAmount = UnConfigAlarmAmount

    @property
    def UnNormalEventAmount(self):
        return self._UnNormalEventAmount

    @UnNormalEventAmount.setter
    def UnNormalEventAmount(self, UnNormalEventAmount):
        self._UnNormalEventAmount = UnNormalEventAmount

    @property
    def UnRecoverAmount(self):
        return self._UnRecoverAmount

    @UnRecoverAmount.setter
    def UnRecoverAmount(self, UnRecoverAmount):
        self._UnRecoverAmount = UnRecoverAmount


    def _deserialize(self, params):
        self._StatusChangeAmount = params.get("StatusChangeAmount")
        self._UnConfigAlarmAmount = params.get("UnConfigAlarmAmount")
        self._UnNormalEventAmount = params.get("UnNormalEventAmount")
        self._UnRecoverAmount = params.get("UnRecoverAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListRequest(AbstractModel):
    """DescribeProductEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 接口模块名，固定值"monitor"
        :type Module: str
        :param _ProductName: 产品类型过滤，例如"cvm"表示云服务器
        :type ProductName: list of str
        :param _EventName: 事件名称过滤，例如"guest_reboot"表示机器重启
        :type EventName: list of str
        :param _InstanceId: 影响对象，例如"ins-19708ino"
        :type InstanceId: list of str
        :param _Dimensions: 维度过滤，例如外网IP:10.0.0.1
        :type Dimensions: list of DescribeProductEventListDimensions
        :param _RegionList: 产品事件地域过滤参数，例如gz，各地域缩写可参见[地域列表](https://cloud.tencent.com/document/product/248/50863)
        :type RegionList: list of str
        :param _Type: 事件类型过滤，取值范围["status_change","abnormal"]，分别表示状态变更、异常事件
        :type Type: list of str
        :param _Status: 事件状态过滤，取值范围["recover","alarm","-"]，分别表示已恢复、未恢复、无状态
        :type Status: list of str
        :param _Project: 项目ID过滤
        :type Project: list of str
        :param _IsAlarmConfig: 告警状态配置过滤，1表示已配置，0表示未配置
        :type IsAlarmConfig: int
        :param _TimeOrder: 按更新时间排序，ASC表示升序，DESC表示降序，默认DESC
        :type TimeOrder: str
        :param _StartTime: 起始时间，默认一天前的时间戳
        :type StartTime: int
        :param _EndTime: 结束时间，默认当前时间戳
        :type EndTime: int
        :param _Offset: 页偏移量，默认0
        :type Offset: int
        :param _Limit: 每页返回的数量，默认20
        :type Limit: int
        """
        self._Module = None
        self._ProductName = None
        self._EventName = None
        self._InstanceId = None
        self._Dimensions = None
        self._RegionList = None
        self._Type = None
        self._Status = None
        self._Project = None
        self._IsAlarmConfig = None
        self._TimeOrder = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

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
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def IsAlarmConfig(self):
        return self._IsAlarmConfig

    @IsAlarmConfig.setter
    def IsAlarmConfig(self, IsAlarmConfig):
        self._IsAlarmConfig = IsAlarmConfig

    @property
    def TimeOrder(self):
        return self._TimeOrder

    @TimeOrder.setter
    def TimeOrder(self, TimeOrder):
        self._TimeOrder = TimeOrder

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
        self._Module = params.get("Module")
        self._ProductName = params.get("ProductName")
        self._EventName = params.get("EventName")
        self._InstanceId = params.get("InstanceId")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListDimensions()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._RegionList = params.get("RegionList")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Project = params.get("Project")
        self._IsAlarmConfig = params.get("IsAlarmConfig")
        self._TimeOrder = params.get("TimeOrder")
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
        


class DescribeProductEventListResponse(AbstractModel):
    """DescribeProductEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of DescribeProductEventListEvents
        :param _OverView: 事件统计
        :type OverView: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListOverView`
        :param _Total: 事件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._OverView = None
        self._Total = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def OverView(self):
        return self._OverView

    @OverView.setter
    def OverView(self, OverView):
        self._OverView = OverView

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
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = DescribeProductEventListEvents()
                obj._deserialize(item)
                self._Events.append(obj)
        if params.get("OverView") is not None:
            self._OverView = DescribeProductEventListOverView()
            self._OverView._deserialize(params.get("OverView"))
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProductListRequest(AbstractModel):
    """DescribeProductList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定传值monitor
        :type Module: str
        :param _Order: 排序方式：DESC/ASC（区分大小写），默认值DESC
        :type Order: str
        :param _Offset: 分页查询的偏移量，默认值0
        :type Offset: int
        :param _Limit: 分页查询的每页数据量，默认值20
        :type Limit: int
        """
        self._Module = None
        self._Order = None
        self._Offset = None
        self._Limit = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

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
        self._Module = params.get("Module")
        self._Order = params.get("Order")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductListResponse(AbstractModel):
    """DescribeProductList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductList: 产品信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductList: list of ProductSimple
        :param _TotalCount: 产品总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProductList(self):
        return self._ProductList

    @ProductList.setter
    def ProductList(self, ProductList):
        self._ProductList = ProductList

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
        if params.get("ProductList") is not None:
            self._ProductList = []
            for item in params.get("ProductList"):
                obj = ProductSimple()
                obj._deserialize(item)
                self._ProductList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrometheusAgentInstancesRequest(AbstractModel):
    """DescribePrometheusAgentInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
可以是tke, eks, edge的集群id
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentInstancesResponse(AbstractModel):
    """DescribePrometheusAgentInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 关联该集群的实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._RequestId = None

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Instances = params.get("Instances")
        self._RequestId = params.get("RequestId")


class DescribePrometheusAgentsRequest(AbstractModel):
    """DescribePrometheusAgents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Name: Agent 名称
        :type Name: str
        :param _AgentIds: Agent ID 列表
        :type AgentIds: list of str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        """
        self._InstanceId = None
        self._Name = None
        self._AgentIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AgentIds(self):
        return self._AgentIds

    @AgentIds.setter
    def AgentIds(self, AgentIds):
        self._AgentIds = AgentIds

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
        self._Name = params.get("Name")
        self._AgentIds = params.get("AgentIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentsResponse(AbstractModel):
    """DescribePrometheusAgents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentSet: Agent 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentSet: list of PrometheusAgent
        :param _TotalCount: Agent 总量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AgentSet(self):
        return self._AgentSet

    @AgentSet.setter
    def AgentSet(self, AgentSet):
        self._AgentSet = AgentSet

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
        if params.get("AgentSet") is not None:
            self._AgentSet = []
            for item in params.get("AgentSet"):
                obj = PrometheusAgent()
                obj._deserialize(item)
                self._AgentSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrometheusAlertGroupsRequest(AbstractModel):
    """DescribePrometheusAlertGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _GroupId: 告警分组ID，形如alert-xxxx。
查询给定ID的告警分组
        :type GroupId: str
        :param _GroupName: 告警分组名称。
查询名称中包含给定字符串的告警分组
        :type GroupName: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._GroupId = None
        self._GroupName = None

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
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAlertGroupsResponse(AbstractModel):
    """DescribePrometheusAlertGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlertGroupSet: 告警分组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertGroupSet: list of PrometheusAlertGroupSet
        :param _TotalCount: 告警分组总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlertGroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AlertGroupSet(self):
        return self._AlertGroupSet

    @AlertGroupSet.setter
    def AlertGroupSet(self, AlertGroupSet):
        self._AlertGroupSet = AlertGroupSet

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
        if params.get("AlertGroupSet") is not None:
            self._AlertGroupSet = []
            for item in params.get("AlertGroupSet"):
                obj = PrometheusAlertGroupSet()
                obj._deserialize(item)
                self._AlertGroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrometheusAlertPolicyRequest(AbstractModel):
    """DescribePrometheusAlertPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Offset: 分页偏移量，默认为0。 示例值：1
        :type Offset: int
        :param _Limit: 分页返回数量，默认为20，最大值为100
        :type Limit: int
        :param _Filters: 仅支持按Name, Values字段过滤:
- Name = Name 
  按照给定的告警规则名称列表匹配
- Name = ID
  按照给定的告警规则ID列表匹配
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
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
        


class DescribePrometheusAlertPolicyResponse(AbstractModel):
    """DescribePrometheusAlertPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlertRules: 告警详情
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRules: list of PrometheusAlertPolicyItem
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlertRules = None
        self._Total = None
        self._RequestId = None

    @property
    def AlertRules(self):
        return self._AlertRules

    @AlertRules.setter
    def AlertRules(self, AlertRules):
        self._AlertRules = AlertRules

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
        if params.get("AlertRules") is not None:
            self._AlertRules = []
            for item in params.get("AlertRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self._AlertRules.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusClusterAgentsRequest(AbstractModel):
    """DescribePrometheusClusterAgents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _ClusterIds: 用于通过集群id过滤被绑定集群
        :type ClusterIds: list of str
        :param _ClusterTypes: 用于通过集群类型过滤被绑定集群
        :type ClusterTypes: list of str
        :param _ClusterName: 用于通过名称搜索被绑定集群
        :type ClusterName: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._ClusterIds = None
        self._ClusterTypes = None
        self._ClusterName = None

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
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def ClusterTypes(self):
        return self._ClusterTypes

    @ClusterTypes.setter
    def ClusterTypes(self, ClusterTypes):
        self._ClusterTypes = ClusterTypes

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterIds = params.get("ClusterIds")
        self._ClusterTypes = params.get("ClusterTypes")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusClusterAgentsResponse(AbstractModel):
    """DescribePrometheusClusterAgents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Agents: 被关联集群信息
        :type Agents: list of PrometheusAgentOverview
        :param _Total: 被关联集群总量
        :type Total: int
        :param _IsFirstBind: 是否为首次绑定，如果是首次绑定则需要安装预聚合规则
        :type IsFirstBind: bool
        :param _ImageNeedUpdate: 实例组件是否需要更新镜像版本
        :type ImageNeedUpdate: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Agents = None
        self._Total = None
        self._IsFirstBind = None
        self._ImageNeedUpdate = None
        self._RequestId = None

    @property
    def Agents(self):
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def IsFirstBind(self):
        return self._IsFirstBind

    @IsFirstBind.setter
    def IsFirstBind(self, IsFirstBind):
        self._IsFirstBind = IsFirstBind

    @property
    def ImageNeedUpdate(self):
        return self._ImageNeedUpdate

    @ImageNeedUpdate.setter
    def ImageNeedUpdate(self, ImageNeedUpdate):
        self._ImageNeedUpdate = ImageNeedUpdate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = PrometheusAgentOverview()
                obj._deserialize(item)
                self._Agents.append(obj)
        self._Total = params.get("Total")
        self._IsFirstBind = params.get("IsFirstBind")
        self._ImageNeedUpdate = params.get("ImageNeedUpdate")
        self._RequestId = params.get("RequestId")


class DescribePrometheusConfigRequest(AbstractModel):
    """DescribePrometheusConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ClusterType: 集群类型
        :type ClusterType: str
        """
        self._InstanceId = None
        self._ClusterId = None
        self._ClusterType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusConfigResponse(AbstractModel):
    """DescribePrometheusConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Config: 全局配置
        :type Config: str
        :param _ServiceMonitors: ServiceMonitor配置
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: PodMonitor配置
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: 原生Job
        :type RawJobs: list of PrometheusConfigItem
        :param _Probes: Probes
        :type Probes: list of PrometheusConfigItem
        :param _ImageNeedUpdate: 实例组件是否需要升级
        :type ImageNeedUpdate: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Config = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._Probes = None
        self._ImageNeedUpdate = None
        self._RequestId = None

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def Probes(self):
        return self._Probes

    @Probes.setter
    def Probes(self, Probes):
        self._Probes = Probes

    @property
    def ImageNeedUpdate(self):
        return self._ImageNeedUpdate

    @ImageNeedUpdate.setter
    def ImageNeedUpdate(self, ImageNeedUpdate):
        self._ImageNeedUpdate = ImageNeedUpdate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Config = params.get("Config")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        if params.get("Probes") is not None:
            self._Probes = []
            for item in params.get("Probes"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._Probes.append(obj)
        self._ImageNeedUpdate = params.get("ImageNeedUpdate")
        self._RequestId = params.get("RequestId")


class DescribePrometheusGlobalConfigRequest(AbstractModel):
    """DescribePrometheusGlobalConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例级别抓取配置
        :type InstanceId: str
        :param _DisableStatistics: 是否禁用统计
        :type DisableStatistics: bool
        """
        self._InstanceId = None
        self._DisableStatistics = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DisableStatistics(self):
        return self._DisableStatistics

    @DisableStatistics.setter
    def DisableStatistics(self, DisableStatistics):
        self._DisableStatistics = DisableStatistics


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DisableStatistics = params.get("DisableStatistics")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusGlobalConfigResponse(AbstractModel):
    """DescribePrometheusGlobalConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Config: 配置内容
        :type Config: str
        :param _ServiceMonitors: ServiceMonitors列表以及对应targets信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: PodMonitors列表以及对应targets信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: RawJobs列表以及对应targets信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RawJobs: list of PrometheusConfigItem
        :param _Probes: Probes列表以及对应targets信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Probes: list of PrometheusConfigItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Config = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._Probes = None
        self._RequestId = None

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def Probes(self):
        return self._Probes

    @Probes.setter
    def Probes(self, Probes):
        self._Probes = Probes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Config = params.get("Config")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        if params.get("Probes") is not None:
            self._Probes = []
            for item in params.get("Probes"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._Probes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusGlobalNotificationRequest(AbstractModel):
    """DescribePrometheusGlobalNotification请求参数结构体

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
        


class DescribePrometheusGlobalNotificationResponse(AbstractModel):
    """DescribePrometheusGlobalNotification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Notification: 全局告警通知渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Notification = None
        self._RequestId = None

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotificationItem()
            self._Notification._deserialize(params.get("Notification"))
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstanceDetailRequest(AbstractModel):
    """DescribePrometheusInstanceDetail请求参数结构体

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
        


class DescribePrometheusInstanceDetailResponse(AbstractModel):
    """DescribePrometheusInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: 子网 ID
        :type SubnetId: str
        :param _InstanceStatus: 实例业务状态。取值范围：

1：正在创建
2：运行中
3：异常
4：重建中
5：销毁中
6：已停服
8：欠费停服中
9：欠费已停服
        :type InstanceStatus: int
        :param _ChargeStatus: 计费状态

1：正常
2：过期
3：销毁
4：分配中
5：分配失败
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeStatus: int
        :param _EnableGrafana: 是否开启 Grafana
0：不开启
1：开启
        :type EnableGrafana: int
        :param _GrafanaURL: Grafana 面板 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaURL: str
        :param _InstanceChargeType: 实例计费模式。取值范围：

2：包年包月
3：按量
        :type InstanceChargeType: int
        :param _SpecName: 规格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _DataRetentionTime: 存储周期
注意：此字段可能返回 null，表示取不到有效值。
        :type DataRetentionTime: int
        :param _ExpireTime: 购买的实例过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _AutoRenewFlag: 自动续费标记

0：不自动续费
1：开启自动续费
2：禁止自动续费
-1：无效
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceStatus = None
        self._ChargeStatus = None
        self._EnableGrafana = None
        self._GrafanaURL = None
        self._InstanceChargeType = None
        self._SpecName = None
        self._DataRetentionTime = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
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
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def EnableGrafana(self):
        return self._EnableGrafana

    @EnableGrafana.setter
    def EnableGrafana(self, EnableGrafana):
        self._EnableGrafana = EnableGrafana

    @property
    def GrafanaURL(self):
        return self._GrafanaURL

    @GrafanaURL.setter
    def GrafanaURL(self, GrafanaURL):
        self._GrafanaURL = GrafanaURL

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._ChargeStatus = params.get("ChargeStatus")
        self._EnableGrafana = params.get("EnableGrafana")
        self._GrafanaURL = params.get("GrafanaURL")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SpecName = params.get("SpecName")
        self._DataRetentionTime = params.get("DataRetentionTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstanceInitStatusRequest(AbstractModel):
    """DescribePrometheusInstanceInitStatus请求参数结构体

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
        


class DescribePrometheusInstanceInitStatusResponse(AbstractModel):
    """DescribePrometheusInstanceInitStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 实例初始化状态，取值：
uninitialized 未初始化 
initializing 初始化中
running 初始化完成，运行中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Steps: 初始化任务步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type Steps: list of TaskStepInfo
        :param _EksClusterId: 实例eks集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EksClusterId: str
        :param _SecurityGroupId: eks集群内pod的安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Steps = None
        self._EksClusterId = None
        self._SecurityGroupId = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Steps(self):
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def EksClusterId(self):
        return self._EksClusterId

    @EksClusterId.setter
    def EksClusterId(self, EksClusterId):
        self._EksClusterId = EksClusterId

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._EksClusterId = params.get("EksClusterId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstanceUsageRequest(AbstractModel):
    """DescribePrometheusInstanceUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：prom-xxxxxxxx。
        :type InstanceIds: list of str
        :param _StartCalcDate: 开始时间
        :type StartCalcDate: str
        :param _EndCalcDate: 结束时间
        :type EndCalcDate: str
        """
        self._InstanceIds = None
        self._StartCalcDate = None
        self._EndCalcDate = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def StartCalcDate(self):
        return self._StartCalcDate

    @StartCalcDate.setter
    def StartCalcDate(self, StartCalcDate):
        self._StartCalcDate = StartCalcDate

    @property
    def EndCalcDate(self):
        return self._EndCalcDate

    @EndCalcDate.setter
    def EndCalcDate(self, EndCalcDate):
        self._EndCalcDate = EndCalcDate


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._StartCalcDate = params.get("StartCalcDate")
        self._EndCalcDate = params.get("EndCalcDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceUsageResponse(AbstractModel):
    """DescribePrometheusInstanceUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsageSet: 用量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UsageSet: list of PrometheusInstanceTenantUsage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsageSet = None
        self._RequestId = None

    @property
    def UsageSet(self):
        return self._UsageSet

    @UsageSet.setter
    def UsageSet(self, UsageSet):
        self._UsageSet = UsageSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UsageSet") is not None:
            self._UsageSet = []
            for item in params.get("UsageSet"):
                obj = PrometheusInstanceTenantUsage()
                obj._deserialize(item)
                self._UsageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstancesOverviewRequest(AbstractModel):
    """DescribePrometheusInstancesOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _Filters: 过滤实例，目前支持：
ID: 通过实例ID来过滤 
Name: 通过实例名称来过滤
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
        


class DescribePrometheusInstancesOverviewResponse(AbstractModel):
    """DescribePrometheusInstancesOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 实例列表
        :type Instances: list of PrometheusInstancesOverview
        :param _Total: 实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._Total = None
        self._RequestId = None

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = PrometheusInstancesOverview()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstancesRequest(AbstractModel):
    """DescribePrometheusInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：prom-xxxxxxxx。请求的实例的上限为100。
        :type InstanceIds: list of str
        :param _InstanceStatus: 按照【实例状态】进行过滤。
<ul>
<li>1：正在创建</li>
<li>2：运行中</li>
<li>3：异常</li>
<li>4：重建中</li>
<li>5：销毁中</li>
<li>6：已停服</li>
<li>8：欠费停服中</li>
<li>9：欠费已停服</li>
</ul>
        :type InstanceStatus: list of int
        :param _InstanceName: 按照【实例名称】进行过滤。
        :type InstanceName: str
        :param _Zones: 按照【可用区】进行过滤。可用区形如：ap-guangzhou-1。
        :type Zones: list of str
        :param _TagFilters: 按照【标签键值对】进行过滤。tag-key使用具体的标签键进行替换。
        :type TagFilters: list of PrometheusTag
        :param _IPv4Address: 按照【实例的IPv4地址】进行过滤。
        :type IPv4Address: list of str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _InstanceChargeType: 按照【计费类型】进行过滤。
<li>2：包年包月</li>
<li>3：按量</li>
        :type InstanceChargeType: int
        """
        self._InstanceIds = None
        self._InstanceStatus = None
        self._InstanceName = None
        self._Zones = None
        self._TagFilters = None
        self._IPv4Address = None
        self._Limit = None
        self._Offset = None
        self._InstanceChargeType = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def IPv4Address(self):
        return self._IPv4Address

    @IPv4Address.setter
    def IPv4Address(self, IPv4Address):
        self._IPv4Address = IPv4Address

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
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceStatus = params.get("InstanceStatus")
        self._InstanceName = params.get("InstanceName")
        self._Zones = params.get("Zones")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._IPv4Address = params.get("IPv4Address")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstancesResponse(AbstractModel):
    """DescribePrometheusInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: 实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSet: list of PrometheusInstancesItem
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = PrometheusInstancesItem()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrometheusRecordRulesRequest(AbstractModel):
    """DescribePrometheusRecordRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 仅支持按Name, Values字段过滤。
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
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
        


class DescribePrometheusRecordRulesResponse(AbstractModel):
    """DescribePrometheusRecordRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 聚合规则
        :type Records: list of PrometheusRecordRuleYamlItem
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._Total = None
        self._RequestId = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = PrometheusRecordRuleYamlItem()
                obj._deserialize(item)
                self._Records.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusRegionsRequest(AbstractModel):
    """DescribePrometheusRegions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PayMode: 1-预付费，2-后付费，3-全地域（不填默认全地域）
        :type PayMode: int
        """
        self._PayMode = None

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusRegionsResponse(AbstractModel):
    """DescribePrometheusRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 区域列表
        :type RegionSet: list of PrometheusRegionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = PrometheusRegionItem()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusScrapeJobsRequest(AbstractModel):
    """DescribePrometheusScrapeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _AgentId: Agent ID
        :type AgentId: str
        :param _Name: 任务名
        :type Name: str
        :param _JobIds: 任务 ID 列表
        :type JobIds: list of str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        """
        self._InstanceId = None
        self._AgentId = None
        self._Name = None
        self._JobIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

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
        self._AgentId = params.get("AgentId")
        self._Name = params.get("Name")
        self._JobIds = params.get("JobIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusScrapeJobsResponse(AbstractModel):
    """DescribePrometheusScrapeJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScrapeJobSet: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ScrapeJobSet: list of PrometheusScrapeJob
        :param _TotalCount: 任务总量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScrapeJobSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ScrapeJobSet(self):
        return self._ScrapeJobSet

    @ScrapeJobSet.setter
    def ScrapeJobSet(self, ScrapeJobSet):
        self._ScrapeJobSet = ScrapeJobSet

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
        if params.get("ScrapeJobSet") is not None:
            self._ScrapeJobSet = []
            for item in params.get("ScrapeJobSet"):
                obj = PrometheusScrapeJob()
                obj._deserialize(item)
                self._ScrapeJobSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrometheusTargetsTMPRequest(AbstractModel):
    """DescribePrometheusTargetsTMP请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ClusterId: 集成容器服务填绑定的集群id；
集成中心填 non-cluster
        :type ClusterId: str
        :param _ClusterType: 集群类型(可不填)
        :type ClusterType: str
        :param _Filters: 过滤条件，支持Name=ServiceMonitor/PodMonitor/Probe/RawJob/Job, Value为采集配置名称；Name=Health, Value=up, down, unknown；Name=EndPoint, Value为EndPoint地址
        :type Filters: list of Filter
        :param _Offset: targets分页偏移量，默认为0
        :type Offset: int
        :param _Limit: targets返回数量，默认为20，最大值200
        :type Limit: int
        """
        self._InstanceId = None
        self._ClusterId = None
        self._ClusterType = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterType = params.get("ClusterType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTargetsTMPResponse(AbstractModel):
    """DescribePrometheusTargetsTMP返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Jobs: 所有Job的targets信息
        :type Jobs: list of PrometheusJobTargets
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Jobs = None
        self._RequestId = None

    @property
    def Jobs(self):
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = PrometheusJobTargets()
                obj._deserialize(item)
                self._Jobs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusTempRequest(AbstractModel):
    """DescribePrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 仅支持按Name, Values字段过滤:
* Name = Name
  按照给定的模板名称列表匹配
* Name = ID
  按照给定的模板ID列表匹配
* Name = Describe
  按照给定的模板描述列表匹配
* Name = Level
  按照给定的模板维度(instance, cluster)列表匹配
        :type Filters: list of Filter
        :param _Offset: 分页偏移量，默认为0
        :type Offset: int
        :param _Limit: 分页返回数量，默认为20，最大值为100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTempResponse(AbstractModel):
    """DescribePrometheusTemp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 模板列表
        :type Templates: list of PrometheusTemp
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._Total = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

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
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = PrometheusTemp()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusTempSyncRequest(AbstractModel):
    """DescribePrometheusTempSync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: str
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
        


class DescribePrometheusTempSyncResponse(AbstractModel):
    """DescribePrometheusTempSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Targets: 同步目标详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of PrometheusTemplateSyncTarget
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Targets = None
        self._RequestId = None

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusZonesRequest(AbstractModel):
    """DescribePrometheusZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域 ID（RegionId 和 RegionName 只需要填一个）
        :type RegionId: int
        :param _RegionName: 地域名（RegionId 和 RegionName 只需要填一个）
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusZonesResponse(AbstractModel):
    """DescribePrometheusZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneSet: 区域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneSet: list of PrometheusZoneItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneSet = None
        self._RequestId = None

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = PrometheusZoneItem()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordingRulesRequest(AbstractModel):
    """DescribeRecordingRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _RuleState: 规则状态码，取值如下：
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param _Name: 规则名称
        :type Name: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._RuleId = None
        self._RuleState = None
        self._Name = None

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
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RuleId = params.get("RuleId")
        self._RuleState = params.get("RuleState")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordingRulesResponse(AbstractModel):
    """DescribeRecordingRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 规则组数量
        :type TotalCount: int
        :param _RecordingRuleSet: 规则组详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordingRuleSet: list of RecordingRuleSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordingRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordingRuleSet(self):
        return self._RecordingRuleSet

    @RecordingRuleSet.setter
    def RecordingRuleSet(self, RecordingRuleSet):
        self._RecordingRuleSet = RecordingRuleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordingRuleSet") is not None:
            self._RecordingRuleSet = []
            for item in params.get("RecordingRuleSet"):
                obj = RecordingRuleSet()
                obj._deserialize(item)
                self._RecordingRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSSOAccountRequest(AbstractModel):
    """DescribeSSOAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _UserId: 填写对应的账号 ID，将会按账号 ID 进行过滤，例如：10000
        :type UserId: str
        """
        self._InstanceId = None
        self._UserId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSSOAccountResponse(AbstractModel):
    """DescribeSSOAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountSet: 授权账号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountSet: list of GrafanaAccountInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountSet = None
        self._RequestId = None

    @property
    def AccountSet(self):
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccountSet") is not None:
            self._AccountSet = []
            for item in params.get("AccountSet"):
                obj = GrafanaAccountInfo()
                obj._deserialize(item)
                self._AccountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceDiscoveryRequest(AbstractModel):
    """DescribeServiceDiscovery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _KubeClusterId: <li>类型是 TKE，为对应的腾讯云容器服务集群 ID</li>
        :type KubeClusterId: str
        :param _KubeType: 用户 Kubernetes 集群类型：
<li> 1 = 容器服务集群(TKE) </li>
        :type KubeType: int
        """
        self._InstanceId = None
        self._KubeClusterId = None
        self._KubeType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeClusterId(self):
        return self._KubeClusterId

    @KubeClusterId.setter
    def KubeClusterId(self, KubeClusterId):
        self._KubeClusterId = KubeClusterId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeClusterId = params.get("KubeClusterId")
        self._KubeType = params.get("KubeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceDiscoveryResponse(AbstractModel):
    """DescribeServiceDiscovery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceDiscoverySet: 返回服务发现列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDiscoverySet: list of ServiceDiscoveryItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceDiscoverySet = None
        self._RequestId = None

    @property
    def ServiceDiscoverySet(self):
        return self._ServiceDiscoverySet

    @ServiceDiscoverySet.setter
    def ServiceDiscoverySet(self, ServiceDiscoverySet):
        self._ServiceDiscoverySet = ServiceDiscoverySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceDiscoverySet") is not None:
            self._ServiceDiscoverySet = []
            for item in params.get("ServiceDiscoverySet"):
                obj = ServiceDiscoveryItem()
                obj._deserialize(item)
                self._ServiceDiscoverySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStatisticDataRequest(AbstractModel):
    """DescribeStatisticData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 所属模块，固定值，为monitor
        :type Module: str
        :param _Namespace: 命名空间，目前支持QCE/TKE2(Conditions必填),QCE/KEEWIDB,QCE/CAMP
        :type Namespace: str
        :param _MetricNames: 指标名列表，相关指标信息可参考对应 [云产品指标文档](https://cloud.tencent.com/document/product/248/62458)
        :type MetricNames: list of str
        :param _Conditions: 维度条件，操作符支持=、in，详情请参考对应 [指标维度信息](https://cloud.tencent.com/document/product/248/53821)
        :type Conditions: list of MidQueryCondition
        :param _Period: 统计粒度。默认取值为300，单位为s；可选的值为60、300、3600、86400
受存储时长限制，统计粒度与统计的时间范围有关：
60s：EndTime-StartTime<12小时，且StartTime距当前时间不能超过15天；
300s：EndTime-StartTime<3天，且StartTime距当前时间不能超过31天；
3600s：EndTime-StartTime<30天，且StartTime距当前时间不能超过93天；
86400s：EndTime-StartTime<186天，且StartTime距当前时间不能超过186天。
        :type Period: int
        :param _StartTime: 起始时间，默认为当前时间，如2020-12-08T19:51:23+08:00
        :type StartTime: str
        :param _EndTime: 结束时间，默认为当前时间，如2020-12-08T19:51:23+08:00
        :type EndTime: str
        :param _GroupBys: 按指定维度groupBy
        :type GroupBys: list of str
        """
        self._Module = None
        self._Namespace = None
        self._MetricNames = None
        self._Conditions = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._GroupBys = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def GroupBys(self):
        return self._GroupBys

    @GroupBys.setter
    def GroupBys(self, GroupBys):
        self._GroupBys = GroupBys


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Namespace = params.get("Namespace")
        self._MetricNames = params.get("MetricNames")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = MidQueryCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._GroupBys = params.get("GroupBys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatisticDataResponse(AbstractModel):
    """DescribeStatisticData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 统计周期
        :type Period: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Data: 监控数据
        :type Data: list of MetricData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._RequestId = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyPrometheusInstanceRequest(AbstractModel):
    """DestroyPrometheusInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，该实例必须先被 terminate
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
        


class DestroyPrometheusInstanceResponse(AbstractModel):
    """DestroyPrometheusInstance返回参数结构体

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


class Dimension(AbstractModel):
    """实例对象的维度组合

    """

    def __init__(self):
        r"""
        :param _Name: 实例维度名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 实例维度值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class DimensionNew(AbstractModel):
    """策略类型的维度信息

    """

    def __init__(self):
        r"""
        :param _Key: 维度 key 标示，后台英文名
        :type Key: str
        :param _Name: 维度 key 名称，中英文前台展示名
        :type Name: str
        :param _IsRequired: 是否必选
        :type IsRequired: bool
        :param _Operators: 支持的操作符列表
        :type Operators: list of Operator
        :param _IsMultiple: 是否支持多选
        :type IsMultiple: bool
        :param _IsMutable: 创建后是否可以修改
        :type IsMutable: bool
        :param _IsVisible: 是否展示给用户
        :type IsVisible: bool
        :param _CanFilterPolicy: 能否用来过滤策略列表
        :type CanFilterPolicy: bool
        :param _CanFilterHistory: 能否用来过滤告警历史
        :type CanFilterHistory: bool
        :param _CanGroupBy: 能否作为聚合维度
        :type CanGroupBy: bool
        :param _MustGroupBy: 是否必须作为聚合维度
        :type MustGroupBy: bool
        :param _ShowValueReplace: 前端翻译要替换的 key
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowValueReplace: str
        """
        self._Key = None
        self._Name = None
        self._IsRequired = None
        self._Operators = None
        self._IsMultiple = None
        self._IsMutable = None
        self._IsVisible = None
        self._CanFilterPolicy = None
        self._CanFilterHistory = None
        self._CanGroupBy = None
        self._MustGroupBy = None
        self._ShowValueReplace = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsRequired(self):
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def Operators(self):
        return self._Operators

    @Operators.setter
    def Operators(self, Operators):
        self._Operators = Operators

    @property
    def IsMultiple(self):
        return self._IsMultiple

    @IsMultiple.setter
    def IsMultiple(self, IsMultiple):
        self._IsMultiple = IsMultiple

    @property
    def IsMutable(self):
        return self._IsMutable

    @IsMutable.setter
    def IsMutable(self, IsMutable):
        self._IsMutable = IsMutable

    @property
    def IsVisible(self):
        return self._IsVisible

    @IsVisible.setter
    def IsVisible(self, IsVisible):
        self._IsVisible = IsVisible

    @property
    def CanFilterPolicy(self):
        return self._CanFilterPolicy

    @CanFilterPolicy.setter
    def CanFilterPolicy(self, CanFilterPolicy):
        self._CanFilterPolicy = CanFilterPolicy

    @property
    def CanFilterHistory(self):
        return self._CanFilterHistory

    @CanFilterHistory.setter
    def CanFilterHistory(self, CanFilterHistory):
        self._CanFilterHistory = CanFilterHistory

    @property
    def CanGroupBy(self):
        return self._CanGroupBy

    @CanGroupBy.setter
    def CanGroupBy(self, CanGroupBy):
        self._CanGroupBy = CanGroupBy

    @property
    def MustGroupBy(self):
        return self._MustGroupBy

    @MustGroupBy.setter
    def MustGroupBy(self, MustGroupBy):
        self._MustGroupBy = MustGroupBy

    @property
    def ShowValueReplace(self):
        return self._ShowValueReplace

    @ShowValueReplace.setter
    def ShowValueReplace(self, ShowValueReplace):
        self._ShowValueReplace = ShowValueReplace


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        self._IsRequired = params.get("IsRequired")
        if params.get("Operators") is not None:
            self._Operators = []
            for item in params.get("Operators"):
                obj = Operator()
                obj._deserialize(item)
                self._Operators.append(obj)
        self._IsMultiple = params.get("IsMultiple")
        self._IsMutable = params.get("IsMutable")
        self._IsVisible = params.get("IsVisible")
        self._CanFilterPolicy = params.get("CanFilterPolicy")
        self._CanFilterHistory = params.get("CanFilterHistory")
        self._CanGroupBy = params.get("CanGroupBy")
        self._MustGroupBy = params.get("MustGroupBy")
        self._ShowValueReplace = params.get("ShowValueReplace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DimensionsDesc(AbstractModel):
    """维度信息

    """

    def __init__(self):
        r"""
        :param _Dimensions: 维度名数组
        :type Dimensions: list of str
        """
        self._Dimensions = None

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaInternetRequest(AbstractModel):
    """EnableGrafanaInternet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: Grafana 实例 ID，例如：grafana-kleu3gt0
        :type InstanceID: str
        :param _EnableInternet: 开启或关闭公网访问，true为开启，false 为不开启
        :type EnableInternet: bool
        """
        self._InstanceID = None
        self._EnableInternet = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def EnableInternet(self):
        return self._EnableInternet

    @EnableInternet.setter
    def EnableInternet(self, EnableInternet):
        self._EnableInternet = EnableInternet


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._EnableInternet = params.get("EnableInternet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaInternetResponse(AbstractModel):
    """EnableGrafanaInternet返回参数结构体

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


class EnableGrafanaSSORequest(AbstractModel):
    """EnableGrafanaSSO请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnableSSO: 是否开启 SSO，true为开启，false 为不开启
        :type EnableSSO: bool
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        """
        self._EnableSSO = None
        self._InstanceId = None

    @property
    def EnableSSO(self):
        return self._EnableSSO

    @EnableSSO.setter
    def EnableSSO(self, EnableSSO):
        self._EnableSSO = EnableSSO

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._EnableSSO = params.get("EnableSSO")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaSSOResponse(AbstractModel):
    """EnableGrafanaSSO返回参数结构体

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


class EnableSSOCamCheckRequest(AbstractModel):
    """EnableSSOCamCheck请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _EnableSSOCamCheck: 是否开启 cam 鉴权，true为开启，false 为不开启
        :type EnableSSOCamCheck: bool
        """
        self._InstanceId = None
        self._EnableSSOCamCheck = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EnableSSOCamCheck(self):
        return self._EnableSSOCamCheck

    @EnableSSOCamCheck.setter
    def EnableSSOCamCheck(self, EnableSSOCamCheck):
        self._EnableSSOCamCheck = EnableSSOCamCheck


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EnableSSOCamCheck = params.get("EnableSSOCamCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableSSOCamCheckResponse(AbstractModel):
    """EnableSSOCamCheck返回参数结构体

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


class EventCondition(AbstractModel):
    """事件告警条件

    """

    def __init__(self):
        r"""
        :param _AlarmNotifyPeriod: 告警通知频率
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmNotifyPeriod: str
        :param _AlarmNotifyType: 重复通知策略预定义（0 - 只告警一次， 1 - 指数告警，2 - 连接告警）
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmNotifyType: str
        :param _EventID: 事件ID
        :type EventID: str
        :param _EventDisplayName: 事件展示名称（对外）
        :type EventDisplayName: str
        :param _RuleID: 规则ID
        :type RuleID: str
        :param _MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        """
        self._AlarmNotifyPeriod = None
        self._AlarmNotifyType = None
        self._EventID = None
        self._EventDisplayName = None
        self._RuleID = None
        self._MetricName = None

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def EventID(self):
        return self._EventID

    @EventID.setter
    def EventID(self, EventID):
        self._EventID = EventID

    @property
    def EventDisplayName(self):
        return self._EventDisplayName

    @EventDisplayName.setter
    def EventDisplayName(self, EventDisplayName):
        self._EventDisplayName = EventDisplayName

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName


    def _deserialize(self, params):
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._EventID = params.get("EventID")
        self._EventDisplayName = params.get("EventDisplayName")
        self._RuleID = params.get("RuleID")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤参数

    """

    def __init__(self):
        r"""
        :param _Type: 过滤方式（=, !=, in）
        :type Type: str
        :param _Key: 过滤维度名
        :type Key: str
        :param _Value: 过滤值，in过滤方式用逗号分割多个值
        :type Value: str
        :param _Name: 过滤条件名称
        :type Name: str
        :param _Values: 过滤条件取值范围
        :type Values: list of str
        """
        self._Type = None
        self._Key = None
        self._Value = None
        self._Name = None
        self._Values = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
        self._Type = params.get("Type")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间，如QCE/CVM。各个云产品的详细命名空间说明请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档
        :type Namespace: str
        :param _MetricName: 指标名称，如CPUUsage，仅支持单指标拉取。各个云产品的详细指标说明请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的指标英文名即为MetricName
        :type MetricName: str
        :param _Instances: 实例对象的维度组合，格式为key-value键值对形式的集合。不同类型的实例字段完全不同，如CVM为[{"Name":"InstanceId","Value":"ins-j0hk02zo"}]，Ckafka为[{"Name":"instanceId","Value":"ckafka-l49k54dd"}]，COS为[{"Name":"appid","Value":"1258344699"},{"Name":"bucket","Value":"rig-1258344699"}]。各个云产品的维度请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的维度列即为维度组合的key，value为key对应的值。单请求最多支持批量拉取10个实例的监控数据。
        :type Instances: list of Instance
        :param _Period: 监控统计周期，如60。默认为取值为300，单位为s。每个指标支持的统计周期不一定相同，各个云产品支持的统计周期请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的统计周期列即为支持的统计周期。单请求的数据点数限制为1440个。
        :type Period: int
        :param _StartTime: 起始时间，如2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param _EndTime: 结束时间，如2018-09-22T20:51:23+08:00，默认为当前时间。 EndTime不能小于StartTime
        :type EndTime: str
        :param _SpecifyStatistics: 返回多种统计方式数据。avg, max, min (1,2,4)可以自由组合
        :type SpecifyStatistics: int
        """
        self._Namespace = None
        self._MetricName = None
        self._Instances = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._SpecifyStatistics = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def SpecifyStatistics(self):
        return self._SpecifyStatistics

    @SpecifyStatistics.setter
    def SpecifyStatistics(self, SpecifyStatistics):
        self._SpecifyStatistics = SpecifyStatistics


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SpecifyStatistics = params.get("SpecifyStatistics")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 统计周期
        :type Period: int
        :param _MetricName: 指标名
        :type MetricName: str
        :param _DataPoints: 数据点数组
        :type DataPoints: list of DataPoint
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Msg: 返回信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Period = None
        self._MetricName = None
        self._DataPoints = None
        self._StartTime = None
        self._EndTime = None
        self._Msg = None
        self._RequestId = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def DataPoints(self):
        return self._DataPoints

    @DataPoints.setter
    def DataPoints(self, DataPoints):
        self._DataPoints = DataPoints

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
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._MetricName = params.get("MetricName")
        if params.get("DataPoints") is not None:
            self._DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self._DataPoints.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class GetPrometheusAgentManagementCommandRequest(AbstractModel):
    """GetPrometheusAgentManagementCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _AgentId: Prometheus Agent ID
        :type AgentId: str
        """
        self._InstanceId = None
        self._AgentId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPrometheusAgentManagementCommandResponse(AbstractModel):
    """GetPrometheusAgentManagementCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Command: Agent 管理命令
        :type Command: :class:`tencentcloud.monitor.v20180724.models.ManagementCommand`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Command = None
        self._RequestId = None

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Command") is not None:
            self._Command = ManagementCommand()
            self._Command._deserialize(params.get("Command"))
        self._RequestId = params.get("RequestId")


class GrafanaAccountInfo(AbstractModel):
    """Grafana可视化服务 授权账户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户账号ID
        :type UserId: str
        :param _Role: 用户权限
        :type Role: list of GrafanaAccountRole
        :param _Notes: 备注
        :type Notes: str
        :param _CreateAt: 创建时间
        :type CreateAt: str
        :param _InstanceId: 实例 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Uin: 用户主账号 UIN
        :type Uin: str
        """
        self._UserId = None
        self._Role = None
        self._Notes = None
        self._CreateAt = None
        self._InstanceId = None
        self._Uin = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        if params.get("Role") is not None:
            self._Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self._Role.append(obj)
        self._Notes = params.get("Notes")
        self._CreateAt = params.get("CreateAt")
        self._InstanceId = params.get("InstanceId")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaAccountRole(AbstractModel):
    """Grafana可视化服务 账号权限

    """

    def __init__(self):
        r"""
        :param _Organization: 组织
        :type Organization: str
        :param _Role: 权限(Admin、Editor、Viewer)
        :type Role: str
        """
        self._Organization = None
        self._Role = None

    @property
    def Organization(self):
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._Organization = params.get("Organization")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaChannel(AbstractModel):
    """Grafana 告警渠道

    """

    def __init__(self):
        r"""
        :param _ChannelId: 渠道 ID
        :type ChannelId: str
        :param _ChannelName: 渠道名
        :type ChannelName: str
        :param _Receivers: 告警通道模板 ID 数组
        :type Receivers: list of str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _OrganizationIds: 告警渠道的所有生效组织
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationIds: list of str
        """
        self._ChannelId = None
        self._ChannelName = None
        self._Receivers = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._OrganizationIds = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaInstanceInfo(AbstractModel):
    """查询 Grafana 实例时的实例类型

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Region: 地域
        :type Region: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetIds: 子网 ID 数组
        :type SubnetIds: list of str
        :param _InternetUrl: Grafana 公网地址
        :type InternetUrl: str
        :param _InternalUrl: Grafana 内网地址
        :type InternalUrl: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _InstanceStatus: 运行状态（1:正在创建；2:运行中；3:异常；4:重启中；5:停机中； 6:已停机； 7: 已删除）
        :type InstanceStatus: int
        :param _TagSpecification: 实例的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: list of PrometheusTag
        :param _Zone: 实例的可用区
        :type Zone: str
        :param _InstanceChargeType: 计费模式（1:包年包月）
        :type InstanceChargeType: int
        :param _VpcName: VPC 名称
        :type VpcName: str
        :param _SubnetName: 子网名称
        :type SubnetName: str
        :param _RegionId: 地域 ID
        :type RegionId: int
        :param _RootUrl: 可访问此实例的完整 URL
        :type RootUrl: str
        :param _EnableSSO: 是否开启 SSO
        :type EnableSSO: bool
        :param _Version: 版本号
        :type Version: str
        :param _EnableSSOCamCheck: SSO登录时是否开启cam鉴权
        :type EnableSSOCamCheck: bool
        """
        self._InstanceName = None
        self._InstanceId = None
        self._Region = None
        self._VpcId = None
        self._SubnetIds = None
        self._InternetUrl = None
        self._InternalUrl = None
        self._CreatedAt = None
        self._InstanceStatus = None
        self._TagSpecification = None
        self._Zone = None
        self._InstanceChargeType = None
        self._VpcName = None
        self._SubnetName = None
        self._RegionId = None
        self._RootUrl = None
        self._EnableSSO = None
        self._Version = None
        self._EnableSSOCamCheck = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

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
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def InternetUrl(self):
        return self._InternetUrl

    @InternetUrl.setter
    def InternetUrl(self, InternetUrl):
        self._InternetUrl = InternetUrl

    @property
    def InternalUrl(self):
        return self._InternalUrl

    @InternalUrl.setter
    def InternalUrl(self, InternalUrl):
        self._InternalUrl = InternalUrl

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RootUrl(self):
        return self._RootUrl

    @RootUrl.setter
    def RootUrl(self, RootUrl):
        self._RootUrl = RootUrl

    @property
    def EnableSSO(self):
        return self._EnableSSO

    @EnableSSO.setter
    def EnableSSO(self, EnableSSO):
        self._EnableSSO = EnableSSO

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def EnableSSOCamCheck(self):
        return self._EnableSSOCamCheck

    @EnableSSOCamCheck.setter
    def EnableSSOCamCheck(self, EnableSSOCamCheck):
        self._EnableSSOCamCheck = EnableSSOCamCheck


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._InternetUrl = params.get("InternetUrl")
        self._InternalUrl = params.get("InternalUrl")
        self._CreatedAt = params.get("CreatedAt")
        self._InstanceStatus = params.get("InstanceStatus")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._Zone = params.get("Zone")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        self._RegionId = params.get("RegionId")
        self._RootUrl = params.get("RootUrl")
        self._EnableSSO = params.get("EnableSSO")
        self._Version = params.get("Version")
        self._EnableSSOCamCheck = params.get("EnableSSOCamCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaIntegrationConfig(AbstractModel):
    """Grafana 集成实例配置

    """

    def __init__(self):
        r"""
        :param _IntegrationId: 集成 ID
        :type IntegrationId: str
        :param _Kind: 集成类型
        :type Kind: str
        :param _Content: 集成内容
        :type Content: str
        :param _Description: 集成描述
        :type Description: str
        :param _GrafanaURL: Grafana 跳转地址
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaURL: str
        """
        self._IntegrationId = None
        self._Kind = None
        self._Content = None
        self._Description = None
        self._GrafanaURL = None

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GrafanaURL(self):
        return self._GrafanaURL

    @GrafanaURL.setter
    def GrafanaURL(self, GrafanaURL):
        self._GrafanaURL = GrafanaURL


    def _deserialize(self, params):
        self._IntegrationId = params.get("IntegrationId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        self._Description = params.get("Description")
        self._GrafanaURL = params.get("GrafanaURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaNotificationChannel(AbstractModel):
    """Grafana 告警渠道

    """

    def __init__(self):
        r"""
        :param _ChannelId: 渠道 ID
        :type ChannelId: str
        :param _ChannelName: 渠道名
        :type ChannelName: str
        :param _Receivers: 告警通道模板 ID 数组
        :type Receivers: list of str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _OrgId: 默认生效组织，已废弃，请使用 OrganizationIds
        :type OrgId: str
        :param _ExtraOrgIds: 额外生效组织，已废弃，请使用 OrganizationIds
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraOrgIds: list of str
        :param _OrgIds: 生效组织，已废弃，请使用 OrganizationIds
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgIds: list of str
        :param _OrganizationIds: 告警渠道的所有生效组织
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationIds: list of str
        """
        self._ChannelId = None
        self._ChannelName = None
        self._Receivers = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._OrgId = None
        self._ExtraOrgIds = None
        self._OrgIds = None
        self._OrganizationIds = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def ExtraOrgIds(self):
        return self._ExtraOrgIds

    @ExtraOrgIds.setter
    def ExtraOrgIds(self, ExtraOrgIds):
        self._ExtraOrgIds = ExtraOrgIds

    @property
    def OrgIds(self):
        return self._OrgIds

    @OrgIds.setter
    def OrgIds(self, OrgIds):
        self._OrgIds = OrgIds

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._OrgId = params.get("OrgId")
        self._ExtraOrgIds = params.get("ExtraOrgIds")
        self._OrgIds = params.get("OrgIds")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaPlugin(AbstractModel):
    """Grafana 插件

    """

    def __init__(self):
        r"""
        :param _PluginId: Grafana 插件 ID
        :type PluginId: str
        :param _Version: Grafana 插件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self._PluginId = None
        self._Version = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallPluginsRequest(AbstractModel):
    """InstallPlugins请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Plugins: 插件信息(可通过 DescribePluginOverviews 接口获取)
        :type Plugins: list of GrafanaPlugin
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        """
        self._Plugins = None
        self._InstanceId = None

    @property
    def Plugins(self):
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = GrafanaPlugin()
                obj._deserialize(item)
                self._Plugins.append(obj)
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallPluginsResponse(AbstractModel):
    """InstallPlugins返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginIds: 已安装插件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PluginIds = None
        self._RequestId = None

    @property
    def PluginIds(self):
        return self._PluginIds

    @PluginIds.setter
    def PluginIds(self, PluginIds):
        self._PluginIds = PluginIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PluginIds = params.get("PluginIds")
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """实例维度组合数组

    """

    def __init__(self):
        r"""
        :param _Dimensions: 实例的维度组合
        :type Dimensions: list of Dimension
        """
        self._Dimensions = None

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceGroup(AbstractModel):
    """DescribeBasicAlarmList返回的Alarms里的InstanceGroup

    """

    def __init__(self):
        r"""
        :param _InstanceGroupId: 实例组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupId: int
        :param _InstanceGroupName: 实例组名
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupName: str
        """
        self._InstanceGroupId = None
        self._InstanceGroupName = None

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def InstanceGroupName(self):
        return self._InstanceGroupName

    @InstanceGroupName.setter
    def InstanceGroupName(self, InstanceGroupName):
        self._InstanceGroupName = InstanceGroupName


    def _deserialize(self, params):
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._InstanceGroupName = params.get("InstanceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceGroups(AbstractModel):
    """告警对象所属实例组

    """

    def __init__(self):
        r"""
        :param _Id: 实例组 Id
        :type Id: int
        :param _Name: 实例组名称
        :type Name: str
        """
        self._Id = None
        self._Name = None

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


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationConfiguration(AbstractModel):
    """export 集成配置

    """

    def __init__(self):
        r"""
        :param _Name: 名字
        :type Name: str
        :param _Kind: 类型
        :type Kind: str
        :param _Content: 内容
        :type Content: str
        :param _Status: 状态
        :type Status: int
        :param _Category: 实例类型
        :type Category: str
        :param _InstanceDesc: 实例描述
        :type InstanceDesc: str
        :param _GrafanaDashboardURL: dashboard 的 URL
        :type GrafanaDashboardURL: str
        """
        self._Name = None
        self._Kind = None
        self._Content = None
        self._Status = None
        self._Category = None
        self._InstanceDesc = None
        self._GrafanaDashboardURL = None

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
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def InstanceDesc(self):
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc

    @property
    def GrafanaDashboardURL(self):
        return self._GrafanaDashboardURL

    @GrafanaDashboardURL.setter
    def GrafanaDashboardURL(self, GrafanaDashboardURL):
        self._GrafanaDashboardURL = GrafanaDashboardURL


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        self._Status = params.get("Status")
        self._Category = params.get("Category")
        self._InstanceDesc = params.get("InstanceDesc")
        self._GrafanaDashboardURL = params.get("GrafanaDashboardURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """k8s中标签，一般以数组的方式存在

    """

    def __init__(self):
        r"""
        :param _Name: map表中的Name
        :type Name: str
        :param _Value: map表中的Value
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
        


class LogAlarmReq(AbstractModel):
    """日志告警请求信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: apm实例id
        :type InstanceId: str
        :param _Filter: 检索条件信息
        :type Filter: list of LogFilterInfo
        :param _AlarmMerge: 告警合并开启/暂停
        :type AlarmMerge: str
        :param _AlarmMergeTime: 告警合并时间
        :type AlarmMergeTime: str
        """
        self._InstanceId = None
        self._Filter = None
        self._AlarmMerge = None
        self._AlarmMergeTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def AlarmMerge(self):
        return self._AlarmMerge

    @AlarmMerge.setter
    def AlarmMerge(self, AlarmMerge):
        self._AlarmMerge = AlarmMerge

    @property
    def AlarmMergeTime(self):
        return self._AlarmMergeTime

    @AlarmMergeTime.setter
    def AlarmMergeTime(self, AlarmMergeTime):
        self._AlarmMergeTime = AlarmMergeTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = LogFilterInfo()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._AlarmMerge = params.get("AlarmMerge")
        self._AlarmMergeTime = params.get("AlarmMergeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogFilterInfo(AbstractModel):
    """日志告警检索条件结构体

    """

    def __init__(self):
        r"""
        :param _Key: 字段名
        :type Key: str
        :param _Operator: 比较符号
        :type Operator: str
        :param _Value: 字段值
        :type Value: str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagementCommand(AbstractModel):
    """Prometheus Agent 管理命令行

    """

    def __init__(self):
        r"""
        :param _Install: Agent 安装命令
注意：此字段可能返回 null，表示取不到有效值。
        :type Install: str
        :param _Restart: Agent 重启命令
注意：此字段可能返回 null，表示取不到有效值。
        :type Restart: str
        :param _Stop: Agent 停止命令
注意：此字段可能返回 null，表示取不到有效值。
        :type Stop: str
        :param _StatusCheck: Agent 状态检测命令
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCheck: str
        :param _LogCheck: Agent 日志检测命令
注意：此字段可能返回 null，表示取不到有效值。
        :type LogCheck: str
        """
        self._Install = None
        self._Restart = None
        self._Stop = None
        self._StatusCheck = None
        self._LogCheck = None

    @property
    def Install(self):
        return self._Install

    @Install.setter
    def Install(self, Install):
        self._Install = Install

    @property
    def Restart(self):
        return self._Restart

    @Restart.setter
    def Restart(self, Restart):
        self._Restart = Restart

    @property
    def Stop(self):
        return self._Stop

    @Stop.setter
    def Stop(self, Stop):
        self._Stop = Stop

    @property
    def StatusCheck(self):
        return self._StatusCheck

    @StatusCheck.setter
    def StatusCheck(self, StatusCheck):
        self._StatusCheck = StatusCheck

    @property
    def LogCheck(self):
        return self._LogCheck

    @LogCheck.setter
    def LogCheck(self, LogCheck):
        self._LogCheck = LogCheck


    def _deserialize(self, params):
        self._Install = params.get("Install")
        self._Restart = params.get("Restart")
        self._Stop = params.get("Stop")
        self._StatusCheck = params.get("StatusCheck")
        self._LogCheck = params.get("LogCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Metric(AbstractModel):
    """指标，可用于设置告警、查询数据

    """

    def __init__(self):
        r"""
        :param _Namespace: 告警策略类型
        :type Namespace: str
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Description: 指标展示名
        :type Description: str
        :param _Min: 最小值
        :type Min: float
        :param _Max: 最大值
        :type Max: float
        :param _Dimensions: 维度列表
        :type Dimensions: list of str
        :param _Unit: 单位
        :type Unit: str
        :param _MetricConfig: 指标配置
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricConfig: :class:`tencentcloud.monitor.v20180724.models.MetricConfig`
        :param _IsAdvanced: 是否为高级指标。1是 0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAdvanced: int
        :param _IsOpen: 高级指标是否开通。1是 0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOpen: int
        :param _ProductId: 集成中心产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: int
        :param _Operators: 匹配运算符
注意：此字段可能返回 null，表示取不到有效值。
        :type Operators: list of Operator
        :param _Periods: 指标触发
注意：此字段可能返回 null，表示取不到有效值。
        :type Periods: list of int
        :param _IsLatenessMetric: 是否延迟指标
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLatenessMetric: int
        """
        self._Namespace = None
        self._MetricName = None
        self._Description = None
        self._Min = None
        self._Max = None
        self._Dimensions = None
        self._Unit = None
        self._MetricConfig = None
        self._IsAdvanced = None
        self._IsOpen = None
        self._ProductId = None
        self._Operators = None
        self._Periods = None
        self._IsLatenessMetric = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def MetricConfig(self):
        return self._MetricConfig

    @MetricConfig.setter
    def MetricConfig(self, MetricConfig):
        self._MetricConfig = MetricConfig

    @property
    def IsAdvanced(self):
        return self._IsAdvanced

    @IsAdvanced.setter
    def IsAdvanced(self, IsAdvanced):
        self._IsAdvanced = IsAdvanced

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Operators(self):
        return self._Operators

    @Operators.setter
    def Operators(self, Operators):
        self._Operators = Operators

    @property
    def Periods(self):
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def IsLatenessMetric(self):
        return self._IsLatenessMetric

    @IsLatenessMetric.setter
    def IsLatenessMetric(self, IsLatenessMetric):
        self._IsLatenessMetric = IsLatenessMetric


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        self._Description = params.get("Description")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._Dimensions = params.get("Dimensions")
        self._Unit = params.get("Unit")
        if params.get("MetricConfig") is not None:
            self._MetricConfig = MetricConfig()
            self._MetricConfig._deserialize(params.get("MetricConfig"))
        self._IsAdvanced = params.get("IsAdvanced")
        self._IsOpen = params.get("IsOpen")
        self._ProductId = params.get("ProductId")
        if params.get("Operators") is not None:
            self._Operators = []
            for item in params.get("Operators"):
                obj = Operator()
                obj._deserialize(item)
                self._Operators.append(obj)
        self._Periods = params.get("Periods")
        self._IsLatenessMetric = params.get("IsLatenessMetric")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricConfig(AbstractModel):
    """指标配置

    """

    def __init__(self):
        r"""
        :param _Operator: 允许使用的运算符
        :type Operator: list of str
        :param _Period: 允许配置的数据周期，以秒为单位
        :type Period: list of int
        :param _ContinuePeriod: 允许配置的持续周期个数
        :type ContinuePeriod: list of int
        """
        self._Operator = None
        self._Period = None
        self._ContinuePeriod = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ContinuePeriod(self):
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        self._Period = params.get("Period")
        self._ContinuePeriod = params.get("ContinuePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """DescribeMetricData接口出参

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Points: 监控数据点
        :type Points: list of MetricDataPoint
        """
        self._MetricName = None
        self._Points = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self._Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDataPoint(AbstractModel):
    """DescribeMetricData出参

    """

    def __init__(self):
        r"""
        :param _Dimensions: 实例对象维度组合
        :type Dimensions: list of Dimension
        :param _Values: 数据点列表
        :type Values: list of Point
        """
        self._Dimensions = None
        self._Values = None

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = Point()
                obj._deserialize(item)
                self._Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricObjectMeaning(AbstractModel):
    """指标数据的解释

    """

    def __init__(self):
        r"""
        :param _En: 指标英文解释
        :type En: str
        :param _Zh: 指标中文解释
        :type Zh: str
        """
        self._En = None
        self._Zh = None

    @property
    def En(self):
        return self._En

    @En.setter
    def En(self, En):
        self._En = En

    @property
    def Zh(self):
        return self._Zh

    @Zh.setter
    def Zh(self, Zh):
        self._Zh = Zh


    def _deserialize(self, params):
        self._En = params.get("En")
        self._Zh = params.get("Zh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricSet(AbstractModel):
    """对业务指标的单位及支持统计周期的描述

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间，每个云产品会有一个命名空间
        :type Namespace: str
        :param _MetricName: 指标名称
        :type MetricName: str
        :param _Unit: 指标使用的单位
        :type Unit: str
        :param _UnitCname: 指标使用的单位
        :type UnitCname: str
        :param _Period: 指标支持的统计周期，单位是秒，如60、300
        :type Period: list of int
        :param _Periods: 统计周期内指标方式
        :type Periods: list of PeriodsSt
        :param _Meaning: 统计指标含义解释
        :type Meaning: :class:`tencentcloud.monitor.v20180724.models.MetricObjectMeaning`
        :param _Dimensions: 维度描述信息
        :type Dimensions: list of DimensionsDesc
        :param _MetricCName: 指标中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricCName: str
        :param _MetricEName: 指标英文名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricEName: str
        """
        self._Namespace = None
        self._MetricName = None
        self._Unit = None
        self._UnitCname = None
        self._Period = None
        self._Periods = None
        self._Meaning = None
        self._Dimensions = None
        self._MetricCName = None
        self._MetricEName = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def UnitCname(self):
        return self._UnitCname

    @UnitCname.setter
    def UnitCname(self, UnitCname):
        self._UnitCname = UnitCname

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Periods(self):
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def Meaning(self):
        return self._Meaning

    @Meaning.setter
    def Meaning(self, Meaning):
        self._Meaning = Meaning

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def MetricCName(self):
        return self._MetricCName

    @MetricCName.setter
    def MetricCName(self, MetricCName):
        self._MetricCName = MetricCName

    @property
    def MetricEName(self):
        return self._MetricEName

    @MetricEName.setter
    def MetricEName(self, MetricEName):
        self._MetricEName = MetricEName


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        self._Unit = params.get("Unit")
        self._UnitCname = params.get("UnitCname")
        self._Period = params.get("Period")
        if params.get("Periods") is not None:
            self._Periods = []
            for item in params.get("Periods"):
                obj = PeriodsSt()
                obj._deserialize(item)
                self._Periods.append(obj)
        if params.get("Meaning") is not None:
            self._Meaning = MetricObjectMeaning()
            self._Meaning._deserialize(params.get("Meaning"))
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionsDesc()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._MetricCName = params.get("MetricCName")
        self._MetricEName = params.get("MetricEName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MidQueryCondition(AbstractModel):
    """DescribeMidDimensionValueList的查询条件

    """

    def __init__(self):
        r"""
        :param _Key: 维度
        :type Key: str
        :param _Operator: 操作符，支持等于(eq)、不等于(ne)，以及in
        :type Operator: str
        :param _Value: 维度值，当Op是eq、ne时，只使用第一个元素
        :type Value: list of str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmNoticeRequest(AbstractModel):
    """ModifyAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”
        :type Module: str
        :param _Name: 告警通知规则名称 60字符以内
        :type Name: str
        :param _NoticeType: 通知类型 ALARM=未恢复通知 OK=已恢复通知 ALL=都通知
        :type NoticeType: str
        :param _NoticeLanguage: 通知语言 zh-CN=中文 en-US=英文
        :type NoticeLanguage: str
        :param _NoticeId: 告警通知模板 ID
        :type NoticeId: str
        :param _UserNotices: 用户通知 最多5个
        :type UserNotices: list of UserNotice
        :param _URLNotices: 回调通知 最多6个
        :type URLNotices: list of URLNotice
        :param _CLSNotices: 告警通知推送到CLS服务 最多1个
        :type CLSNotices: list of CLSNotice
        :param _PolicyIds: 告警通知模板绑定的告警策略ID列表
        :type PolicyIds: list of str
        """
        self._Module = None
        self._Name = None
        self._NoticeType = None
        self._NoticeLanguage = None
        self._NoticeId = None
        self._UserNotices = None
        self._URLNotices = None
        self._CLSNotices = None
        self._PolicyIds = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NoticeType(self):
        return self._NoticeType

    @NoticeType.setter
    def NoticeType(self, NoticeType):
        self._NoticeType = NoticeType

    @property
    def NoticeLanguage(self):
        return self._NoticeLanguage

    @NoticeLanguage.setter
    def NoticeLanguage(self, NoticeLanguage):
        self._NoticeLanguage = NoticeLanguage

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def UserNotices(self):
        return self._UserNotices

    @UserNotices.setter
    def UserNotices(self, UserNotices):
        self._UserNotices = UserNotices

    @property
    def URLNotices(self):
        return self._URLNotices

    @URLNotices.setter
    def URLNotices(self, URLNotices):
        self._URLNotices = URLNotices

    @property
    def CLSNotices(self):
        return self._CLSNotices

    @CLSNotices.setter
    def CLSNotices(self, CLSNotices):
        self._CLSNotices = CLSNotices

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Name = params.get("Name")
        self._NoticeType = params.get("NoticeType")
        self._NoticeLanguage = params.get("NoticeLanguage")
        self._NoticeId = params.get("NoticeId")
        if params.get("UserNotices") is not None:
            self._UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self._UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self._URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self._URLNotices.append(obj)
        if params.get("CLSNotices") is not None:
            self._CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self._CLSNotices.append(obj)
        self._PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmNoticeResponse(AbstractModel):
    """ModifyAlarmNotice返回参数结构体

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


class ModifyAlarmPolicyConditionRequest(AbstractModel):
    """ModifyAlarmPolicyCondition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定值 monitor
        :type Module: str
        :param _PolicyId: 告警策略 ID
        :type PolicyId: str
        :param _ConditionTemplateId: 触发条件模板 Id，可不传
        :type ConditionTemplateId: int
        :param _Condition: 指标触发条件
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param _EventCondition: 事件触发条件
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param _Filter: 全局过滤条件
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param _GroupBy: 聚合维度列表，指定按哪些维度 key 来做 group by
        :type GroupBy: list of str
        :param _LogAlarmReqInfo: 日志告警创建请求参数信息
        :type LogAlarmReqInfo: :class:`tencentcloud.monitor.v20180724.models.LogAlarmReq`
        :param _NoticeIds: 模板id，专供prom使用
        :type NoticeIds: list of str
        :param _Enable: 启停状态，0=停用，1=启用
        :type Enable: int
        :param _PolicyName: 专供prom策略名称
        :type PolicyName: str
        :param _EbSubject: 事件配置的告警
        :type EbSubject: str
        """
        self._Module = None
        self._PolicyId = None
        self._ConditionTemplateId = None
        self._Condition = None
        self._EventCondition = None
        self._Filter = None
        self._GroupBy = None
        self._LogAlarmReqInfo = None
        self._NoticeIds = None
        self._Enable = None
        self._PolicyName = None
        self._EbSubject = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def ConditionTemplateId(self):
        return self._ConditionTemplateId

    @ConditionTemplateId.setter
    def ConditionTemplateId(self, ConditionTemplateId):
        self._ConditionTemplateId = ConditionTemplateId

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def EventCondition(self):
        return self._EventCondition

    @EventCondition.setter
    def EventCondition(self, EventCondition):
        self._EventCondition = EventCondition

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def LogAlarmReqInfo(self):
        return self._LogAlarmReqInfo

    @LogAlarmReqInfo.setter
    def LogAlarmReqInfo(self, LogAlarmReqInfo):
        self._LogAlarmReqInfo = LogAlarmReqInfo

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self._Condition = AlarmPolicyCondition()
            self._Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self._EventCondition = AlarmPolicyEventCondition()
            self._EventCondition._deserialize(params.get("EventCondition"))
        if params.get("Filter") is not None:
            self._Filter = AlarmPolicyFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._GroupBy = params.get("GroupBy")
        if params.get("LogAlarmReqInfo") is not None:
            self._LogAlarmReqInfo = LogAlarmReq()
            self._LogAlarmReqInfo._deserialize(params.get("LogAlarmReqInfo"))
        self._NoticeIds = params.get("NoticeIds")
        self._Enable = params.get("Enable")
        self._PolicyName = params.get("PolicyName")
        self._EbSubject = params.get("EbSubject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyConditionResponse(AbstractModel):
    """ModifyAlarmPolicyCondition返回参数结构体

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


class ModifyAlarmPolicyInfoRequest(AbstractModel):
    """ModifyAlarmPolicyInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”
        :type Module: str
        :param _PolicyId: 告警策略 ID
        :type PolicyId: str
        :param _Key: 要修改的字段 NAME=策略名称 REMARK=策略备注
        :type Key: str
        :param _Value: 修改后的值
        :type Value: str
        """
        self._Module = None
        self._PolicyId = None
        self._Key = None
        self._Value = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyInfoResponse(AbstractModel):
    """ModifyAlarmPolicyInfo返回参数结构体

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


class ModifyAlarmPolicyNoticeRequest(AbstractModel):
    """ModifyAlarmPolicyNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”。
        :type Module: str
        :param _PolicyId: 告警策略 ID，如果该参数与PolicyIds参数同时存在，则以PolicyIds为准。
        :type PolicyId: str
        :param _NoticeIds: 告警通知模板 ID 列表。
        :type NoticeIds: list of str
        :param _PolicyIds: 告警策略ID数组，支持给多个告警策略批量绑定通知模板。最多30个。
        :type PolicyIds: list of str
        :param _HierarchicalNotices: 告警分级通知规则配置
        :type HierarchicalNotices: list of AlarmHierarchicalNotice
        """
        self._Module = None
        self._PolicyId = None
        self._NoticeIds = None
        self._PolicyIds = None
        self._HierarchicalNotices = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def HierarchicalNotices(self):
        return self._HierarchicalNotices

    @HierarchicalNotices.setter
    def HierarchicalNotices(self, HierarchicalNotices):
        self._HierarchicalNotices = HierarchicalNotices


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._NoticeIds = params.get("NoticeIds")
        self._PolicyIds = params.get("PolicyIds")
        if params.get("HierarchicalNotices") is not None:
            self._HierarchicalNotices = []
            for item in params.get("HierarchicalNotices"):
                obj = AlarmHierarchicalNotice()
                obj._deserialize(item)
                self._HierarchicalNotices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyNoticeResponse(AbstractModel):
    """ModifyAlarmPolicyNotice返回参数结构体

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


class ModifyAlarmPolicyStatusRequest(AbstractModel):
    """ModifyAlarmPolicyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定值 monitor
        :type Module: str
        :param _PolicyId: 告警策略 ID
        :type PolicyId: str
        :param _Enable: 启停状态 0=停用 1=启用
        :type Enable: int
        """
        self._Module = None
        self._PolicyId = None
        self._Enable = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyStatusResponse(AbstractModel):
    """ModifyAlarmPolicyStatus返回参数结构体

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


class ModifyAlarmPolicyTasksRequest(AbstractModel):
    """ModifyAlarmPolicyTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，这里填“monitor”
        :type Module: str
        :param _PolicyId: 告警策略 ID
        :type PolicyId: str
        :param _TriggerTasks: 告警策略触发任务列表，空数据代表解绑
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        """
        self._Module = None
        self._PolicyId = None
        self._TriggerTasks = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def TriggerTasks(self):
        return self._TriggerTasks

    @TriggerTasks.setter
    def TriggerTasks(self, TriggerTasks):
        self._TriggerTasks = TriggerTasks


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        if params.get("TriggerTasks") is not None:
            self._TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self._TriggerTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyTasksResponse(AbstractModel):
    """ModifyAlarmPolicyTasks返回参数结构体

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


class ModifyAlarmReceiversRequest(AbstractModel):
    """ModifyAlarmReceivers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 需要修改接收人的策略组Id
        :type GroupId: int
        :param _Module: 必填。固定为“monitor”
        :type Module: str
        :param _ReceiverInfos: 新接收人信息, 没有填写则删除所有接收人
        :type ReceiverInfos: list of ReceiverInfo
        """
        self._GroupId = None
        self._Module = None
        self._ReceiverInfos = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ReceiverInfos(self):
        return self._ReceiverInfos

    @ReceiverInfos.setter
    def ReceiverInfos(self, ReceiverInfos):
        self._ReceiverInfos = ReceiverInfos


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Module = params.get("Module")
        if params.get("ReceiverInfos") is not None:
            self._ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = ReceiverInfo()
                obj._deserialize(item)
                self._ReceiverInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmReceiversResponse(AbstractModel):
    """ModifyAlarmReceivers返回参数结构体

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


class ModifyGrafanaInstanceRequest(AbstractModel):
    """ModifyGrafanaInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _InstanceName: Grafana 实例名称，例如：test
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
        


class ModifyGrafanaInstanceResponse(AbstractModel):
    """ModifyGrafanaInstance返回参数结构体

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


class ModifyPolicyGroupCondition(AbstractModel):
    """修改告警策略组传入的指标阈值条件

    """

    def __init__(self):
        r"""
        :param _MetricId: 指标id
        :type MetricId: int
        :param _CalcType: 比较类型，1表示大于，2表示大于等于，3表示小于，4表示小于等于，5表示相等，6表示不相等
        :type CalcType: int
        :param _CalcValue: 检测阈值
        :type CalcValue: str
        :param _CalcPeriod: 检测指标的数据周期
        :type CalcPeriod: int
        :param _ContinuePeriod: 持续周期个数
        :type ContinuePeriod: int
        :param _AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param _RuleId: 规则id，不填表示新增，填写了ruleId表示在已存在的规则基础上进行修改
        :type RuleId: int
        """
        self._MetricId = None
        self._CalcType = None
        self._CalcValue = None
        self._CalcPeriod = None
        self._ContinuePeriod = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._RuleId = None

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def CalcPeriod(self):
        return self._CalcPeriod

    @CalcPeriod.setter
    def CalcPeriod(self, CalcPeriod):
        self._CalcPeriod = CalcPeriod

    @property
    def ContinuePeriod(self):
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._MetricId = params.get("MetricId")
        self._CalcType = params.get("CalcType")
        self._CalcValue = params.get("CalcValue")
        self._CalcPeriod = params.get("CalcPeriod")
        self._ContinuePeriod = params.get("ContinuePeriod")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupEventCondition(AbstractModel):
    """修改告警策略组传入的事件告警条件

    """

    def __init__(self):
        r"""
        :param _EventId: 事件id
        :type EventId: int
        :param _AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param _RuleId: 规则id，不填表示新增，填写了ruleId表示在已存在的规则基础上进行修改
        :type RuleId: int
        """
        self._EventId = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._RuleId = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupRequest(AbstractModel):
    """ModifyPolicyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _GroupId: 策略组id
        :type GroupId: int
        :param _ViewName: 告警类型
        :type ViewName: str
        :param _GroupName: 策略组名称
        :type GroupName: str
        :param _IsUnionRule: 指标告警条件的且或关系，1表示且告警，所有指标告警条件都达到才告警，0表示或告警，任意指标告警条件达到都告警
        :type IsUnionRule: int
        :param _Conditions: 指标告警条件规则，不填表示删除已有的所有指标告警条件规则
        :type Conditions: list of ModifyPolicyGroupCondition
        :param _EventConditions: 事件告警条件，不填表示删除已有的事件告警条件
        :type EventConditions: list of ModifyPolicyGroupEventCondition
        :param _ConditionTempGroupId: 模板策略组id
        :type ConditionTempGroupId: int
        """
        self._Module = None
        self._GroupId = None
        self._ViewName = None
        self._GroupName = None
        self._IsUnionRule = None
        self._Conditions = None
        self._EventConditions = None
        self._ConditionTempGroupId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def EventConditions(self):
        return self._EventConditions

    @EventConditions.setter
    def EventConditions(self, EventConditions):
        self._EventConditions = EventConditions

    @property
    def ConditionTempGroupId(self):
        return self._ConditionTempGroupId

    @ConditionTempGroupId.setter
    def ConditionTempGroupId(self, ConditionTempGroupId):
        self._ConditionTempGroupId = ConditionTempGroupId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._ViewName = params.get("ViewName")
        self._GroupName = params.get("GroupName")
        self._IsUnionRule = params.get("IsUnionRule")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = ModifyPolicyGroupCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self._EventConditions = []
            for item in params.get("EventConditions"):
                obj = ModifyPolicyGroupEventCondition()
                obj._deserialize(item)
                self._EventConditions.append(obj)
        self._ConditionTempGroupId = params.get("ConditionTempGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupResponse(AbstractModel):
    """ModifyPolicyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 策略组id
        :type GroupId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class ModifyPrometheusAgentExternalLabelsRequest(AbstractModel):
    """ModifyPrometheusAgentExternalLabels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ExternalLabels: 新的external_labels
        :type ExternalLabels: list of Label
        """
        self._InstanceId = None
        self._ClusterId = None
        self._ExternalLabels = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ExternalLabels(self):
        return self._ExternalLabels

    @ExternalLabels.setter
    def ExternalLabels(self, ExternalLabels):
        self._ExternalLabels = ExternalLabels


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        if params.get("ExternalLabels") is not None:
            self._ExternalLabels = []
            for item in params.get("ExternalLabels"):
                obj = Label()
                obj._deserialize(item)
                self._ExternalLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusAgentExternalLabelsResponse(AbstractModel):
    """ModifyPrometheusAgentExternalLabels返回参数结构体

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


class ModifyPrometheusAlertPolicyRequest(AbstractModel):
    """ModifyPrometheusAlertPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _AlertRule: 告警配置，[具体参考](https://cloud.tencent.com/document/api/248/30354#PrometheusAlertPolicyItem)
        :type AlertRule: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertPolicyItem`
        """
        self._InstanceId = None
        self._AlertRule = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertRule(self):
        return self._AlertRule

    @AlertRule.setter
    def AlertRule(self, AlertRule):
        self._AlertRule = AlertRule


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self._AlertRule = PrometheusAlertPolicyItem()
            self._AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusAlertPolicyResponse(AbstractModel):
    """ModifyPrometheusAlertPolicy返回参数结构体

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


class ModifyPrometheusConfigRequest(AbstractModel):
    """ModifyPrometheusConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ClusterType: 集群类型
        :type ClusterType: str
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ServiceMonitors: ServiceMonitors配置
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: PodMonitors配置
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: prometheus原生Job配置
        :type RawJobs: list of PrometheusConfigItem
        :param _UpdateImage: 0: 更新实例组件镜像版本；
1: 不更新实例组件镜像版本
        :type UpdateImage: int
        """
        self._InstanceId = None
        self._ClusterType = None
        self._ClusterId = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._UpdateImage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def UpdateImage(self):
        return self._UpdateImage

    @UpdateImage.setter
    def UpdateImage(self, UpdateImage):
        self._UpdateImage = UpdateImage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        self._UpdateImage = params.get("UpdateImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusConfigResponse(AbstractModel):
    """ModifyPrometheusConfig返回参数结构体

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


class ModifyPrometheusGlobalNotificationRequest(AbstractModel):
    """ModifyPrometheusGlobalNotification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Notification: 告警通知渠道
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        """
        self._InstanceId = None
        self._Notification = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotificationItem()
            self._Notification._deserialize(params.get("Notification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusGlobalNotificationResponse(AbstractModel):
    """ModifyPrometheusGlobalNotification返回参数结构体

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


class ModifyPrometheusInstanceAttributesRequest(AbstractModel):
    """ModifyPrometheusInstanceAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _DataRetentionTime: 数据存储时间（单位天），限制值为15, 30, 45, 90, 180, 365, 730之一
        :type DataRetentionTime: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._DataRetentionTime = None

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
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._DataRetentionTime = params.get("DataRetentionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusInstanceAttributesResponse(AbstractModel):
    """ModifyPrometheusInstanceAttributes返回参数结构体

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


class ModifyPrometheusRecordRuleYamlRequest(AbstractModel):
    """ModifyPrometheusRecordRuleYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Name: 聚合实例名称
        :type Name: str
        :param _Content: 新的内容
        :type Content: str
        """
        self._InstanceId = None
        self._Name = None
        self._Content = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusRecordRuleYamlResponse(AbstractModel):
    """ModifyPrometheusRecordRuleYaml返回参数结构体

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


class ModifyPrometheusTempRequest(AbstractModel):
    """ModifyPrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: str
        :param _Template: 修改内容
        :type Template: :class:`tencentcloud.monitor.v20180724.models.PrometheusTempModify`
        """
        self._TemplateId = None
        self._Template = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Template") is not None:
            self._Template = PrometheusTempModify()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusTempResponse(AbstractModel):
    """ModifyPrometheusTemp返回参数结构体

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


class MonitorTypeInfo(AbstractModel):
    """监控类型详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 监控类型ID
        :type Id: str
        :param _Name: 监控类型
        :type Name: str
        :param _SortId: 排列顺序
        :type SortId: int
        """
        self._Id = None
        self._Name = None
        self._SortId = None

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
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._SortId = params.get("SortId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorTypeNamespace(AbstractModel):
    """策略类型

    """

    def __init__(self):
        r"""
        :param _MonitorType: 监控类型
        :type MonitorType: str
        :param _Namespace: 策略类型值
        :type Namespace: str
        """
        self._MonitorType = None
        self._Namespace = None

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._MonitorType = params.get("MonitorType")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeBindPolicys(AbstractModel):
    """通知模板与策略绑定关系

    """

    def __init__(self):
        r"""
        :param _NoticeId: 告警通知模板 ID
        :type NoticeId: str
        :param _PolicyIds: 告警通知模板绑定的告警策略ID列表
        :type PolicyIds: list of str
        """
        self._NoticeId = None
        self._PolicyIds = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operator(AbstractModel):
    """维度支持的操作符信息

    """

    def __init__(self):
        r"""
        :param _Id: 运算符标识
        :type Id: str
        :param _Name: 运算符展示名
        :type Name: str
        """
        self._Id = None
        self._Name = None

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


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeriodsSt(AbstractModel):
    """周期内的统计方式

    """

    def __init__(self):
        r"""
        :param _Period: 周期
        :type Period: str
        :param _StatType: 统计方式
        :type StatType: list of str
        """
        self._Period = None
        self._StatType = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._StatType = params.get("StatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """监控数据点

    """

    def __init__(self):
        r"""
        :param _Timestamp: 该监控数据点生成的时间点
        :type Timestamp: int
        :param _Value: 监控数据点的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        """
        self._Timestamp = None
        self._Value = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyGroup(AbstractModel):
    """策略组信息

    """

    def __init__(self):
        r"""
        :param _CanSetDefault: 是否可设为默认告警策略
        :type CanSetDefault: bool
        :param _GroupID: 告警策略组ID
        :type GroupID: int
        :param _GroupName: 告警策略组名称
        :type GroupName: str
        :param _InsertTime: 创建时间
        :type InsertTime: int
        :param _IsDefault: 是否为默认告警策略
        :type IsDefault: int
        :param _Enable: 告警策略启用状态
        :type Enable: bool
        :param _LastEditUin: 最后修改人UIN
        :type LastEditUin: int
        :param _NoShieldedInstanceCount: 未屏蔽的实例数
        :type NoShieldedInstanceCount: int
        :param _ParentGroupID: 父策略组ID
        :type ParentGroupID: int
        :param _ProjectID: 所属项目ID
        :type ProjectID: int
        :param _ReceiverInfos: 告警接收对象信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverInfos: list of PolicyGroupReceiverInfo
        :param _Remark: 备注信息
        :type Remark: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: int
        :param _TotalInstanceCount: 总绑定实例数
        :type TotalInstanceCount: int
        :param _ViewName: 视图
        :type ViewName: str
        :param _IsUnionRule: 是否为与关系规则
        :type IsUnionRule: int
        """
        self._CanSetDefault = None
        self._GroupID = None
        self._GroupName = None
        self._InsertTime = None
        self._IsDefault = None
        self._Enable = None
        self._LastEditUin = None
        self._NoShieldedInstanceCount = None
        self._ParentGroupID = None
        self._ProjectID = None
        self._ReceiverInfos = None
        self._Remark = None
        self._UpdateTime = None
        self._TotalInstanceCount = None
        self._ViewName = None
        self._IsUnionRule = None

    @property
    def CanSetDefault(self):
        return self._CanSetDefault

    @CanSetDefault.setter
    def CanSetDefault(self, CanSetDefault):
        self._CanSetDefault = CanSetDefault

    @property
    def GroupID(self):
        return self._GroupID

    @GroupID.setter
    def GroupID(self, GroupID):
        self._GroupID = GroupID

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def NoShieldedInstanceCount(self):
        return self._NoShieldedInstanceCount

    @NoShieldedInstanceCount.setter
    def NoShieldedInstanceCount(self, NoShieldedInstanceCount):
        self._NoShieldedInstanceCount = NoShieldedInstanceCount

    @property
    def ParentGroupID(self):
        return self._ParentGroupID

    @ParentGroupID.setter
    def ParentGroupID(self, ParentGroupID):
        self._ParentGroupID = ParentGroupID

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ReceiverInfos(self):
        return self._ReceiverInfos

    @ReceiverInfos.setter
    def ReceiverInfos(self, ReceiverInfos):
        self._ReceiverInfos = ReceiverInfos

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TotalInstanceCount(self):
        return self._TotalInstanceCount

    @TotalInstanceCount.setter
    def TotalInstanceCount(self, TotalInstanceCount):
        self._TotalInstanceCount = TotalInstanceCount

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        self._CanSetDefault = params.get("CanSetDefault")
        self._GroupID = params.get("GroupID")
        self._GroupName = params.get("GroupName")
        self._InsertTime = params.get("InsertTime")
        self._IsDefault = params.get("IsDefault")
        self._Enable = params.get("Enable")
        self._LastEditUin = params.get("LastEditUin")
        self._NoShieldedInstanceCount = params.get("NoShieldedInstanceCount")
        self._ParentGroupID = params.get("ParentGroupID")
        self._ProjectID = params.get("ProjectID")
        if params.get("ReceiverInfos") is not None:
            self._ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = PolicyGroupReceiverInfo()
                obj._deserialize(item)
                self._ReceiverInfos.append(obj)
        self._Remark = params.get("Remark")
        self._UpdateTime = params.get("UpdateTime")
        self._TotalInstanceCount = params.get("TotalInstanceCount")
        self._ViewName = params.get("ViewName")
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyGroupReceiverInfo(AbstractModel):
    """2018版策略模板列表接收人信息

    """

    def __init__(self):
        r"""
        :param _EndTime: 有效时段结束时间
        :type EndTime: int
        :param _NeedSendNotice: 是否需要发送通知
        :type NeedSendNotice: int
        :param _NotifyWay: 告警接收渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyWay: list of str
        :param _PersonInterval: 电话告警对个人间隔（秒）
        :type PersonInterval: int
        :param _ReceiverGroupList: 消息接收组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverGroupList: list of int
        :param _ReceiverType: 接受者类型
        :type ReceiverType: str
        :param _ReceiverUserList: 接收人列表。通过平台接口查询到的接收人id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverUserList: list of int
        :param _RecoverNotify: 告警恢复通知方式
注意：此字段可能返回 null，表示取不到有效值。
        :type RecoverNotify: list of str
        :param _RoundInterval: 电话告警每轮间隔（秒）
        :type RoundInterval: int
        :param _RoundNumber: 电话告警轮数
        :type RoundNumber: int
        :param _SendFor: 电话告警通知时机。可选"OCCUR"(告警时通知),"RECOVER"(恢复时通知)
注意：此字段可能返回 null，表示取不到有效值。
        :type SendFor: list of str
        :param _StartTime: 有效时段开始时间
        :type StartTime: int
        :param _UIDList: 电话告警接收者uid
注意：此字段可能返回 null，表示取不到有效值。
        :type UIDList: list of int
        """
        self._EndTime = None
        self._NeedSendNotice = None
        self._NotifyWay = None
        self._PersonInterval = None
        self._ReceiverGroupList = None
        self._ReceiverType = None
        self._ReceiverUserList = None
        self._RecoverNotify = None
        self._RoundInterval = None
        self._RoundNumber = None
        self._SendFor = None
        self._StartTime = None
        self._UIDList = None

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedSendNotice(self):
        return self._NeedSendNotice

    @NeedSendNotice.setter
    def NeedSendNotice(self, NeedSendNotice):
        self._NeedSendNotice = NeedSendNotice

    @property
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def PersonInterval(self):
        return self._PersonInterval

    @PersonInterval.setter
    def PersonInterval(self, PersonInterval):
        self._PersonInterval = PersonInterval

    @property
    def ReceiverGroupList(self):
        return self._ReceiverGroupList

    @ReceiverGroupList.setter
    def ReceiverGroupList(self, ReceiverGroupList):
        self._ReceiverGroupList = ReceiverGroupList

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def ReceiverUserList(self):
        return self._ReceiverUserList

    @ReceiverUserList.setter
    def ReceiverUserList(self, ReceiverUserList):
        self._ReceiverUserList = ReceiverUserList

    @property
    def RecoverNotify(self):
        return self._RecoverNotify

    @RecoverNotify.setter
    def RecoverNotify(self, RecoverNotify):
        self._RecoverNotify = RecoverNotify

    @property
    def RoundInterval(self):
        return self._RoundInterval

    @RoundInterval.setter
    def RoundInterval(self, RoundInterval):
        self._RoundInterval = RoundInterval

    @property
    def RoundNumber(self):
        return self._RoundNumber

    @RoundNumber.setter
    def RoundNumber(self, RoundNumber):
        self._RoundNumber = RoundNumber

    @property
    def SendFor(self):
        return self._SendFor

    @SendFor.setter
    def SendFor(self, SendFor):
        self._SendFor = SendFor

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def UIDList(self):
        return self._UIDList

    @UIDList.setter
    def UIDList(self, UIDList):
        self._UIDList = UIDList


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._NeedSendNotice = params.get("NeedSendNotice")
        self._NotifyWay = params.get("NotifyWay")
        self._PersonInterval = params.get("PersonInterval")
        self._ReceiverGroupList = params.get("ReceiverGroupList")
        self._ReceiverType = params.get("ReceiverType")
        self._ReceiverUserList = params.get("ReceiverUserList")
        self._RecoverNotify = params.get("RecoverNotify")
        self._RoundInterval = params.get("RoundInterval")
        self._RoundNumber = params.get("RoundNumber")
        self._SendFor = params.get("SendFor")
        self._StartTime = params.get("StartTime")
        self._UIDList = params.get("UIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyTag(AbstractModel):
    """策略标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签Key
        :type Key: str
        :param _Value: 标签Value
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
        


class ProductSimple(AbstractModel):
    """云产品监控支持的产品简要信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _ProductName: 产品中文名称
        :type ProductName: str
        :param _ProductEnName: 产品英文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductEnName: str
        """
        self._Namespace = None
        self._ProductName = None
        self._ProductEnName = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductEnName(self):
        return self._ProductEnName

    @ProductEnName.setter
    def ProductEnName(self, ProductEnName):
        self._ProductEnName = ProductEnName


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._ProductName = params.get("ProductName")
        self._ProductEnName = params.get("ProductEnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAgent(AbstractModel):
    """prometheus agent

    """

    def __init__(self):
        r"""
        :param _Name: Agent 名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AgentId: Agent ID
        :type AgentId: str
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Ipv4: Agent IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv4: str
        :param _HeartbeatTime: 心跳时间
注意：此字段可能返回 null，表示取不到有效值。
        :type HeartbeatTime: str
        :param _LastError: 最近一次错误
注意：此字段可能返回 null，表示取不到有效值。
        :type LastError: str
        :param _AgentVersion: Agent 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentVersion: str
        :param _Status: Agent 状态
        :type Status: int
        """
        self._Name = None
        self._AgentId = None
        self._InstanceId = None
        self._Ipv4 = None
        self._HeartbeatTime = None
        self._LastError = None
        self._AgentVersion = None
        self._Status = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ipv4(self):
        return self._Ipv4

    @Ipv4.setter
    def Ipv4(self, Ipv4):
        self._Ipv4 = Ipv4

    @property
    def HeartbeatTime(self):
        return self._HeartbeatTime

    @HeartbeatTime.setter
    def HeartbeatTime(self, HeartbeatTime):
        self._HeartbeatTime = HeartbeatTime

    @property
    def LastError(self):
        return self._LastError

    @LastError.setter
    def LastError(self, LastError):
        self._LastError = LastError

    @property
    def AgentVersion(self):
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AgentId = params.get("AgentId")
        self._InstanceId = params.get("InstanceId")
        self._Ipv4 = params.get("Ipv4")
        self._HeartbeatTime = params.get("HeartbeatTime")
        self._LastError = params.get("LastError")
        self._AgentVersion = params.get("AgentVersion")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAgentInfo(AbstractModel):
    """托管Prometheus agent信息

    """

    def __init__(self):
        r"""
        :param _ClusterType: 集群类型。可填入tke、eks、tkeedge、tdcc，分别代表标准集群、弹性集群、边缘集群、注册集群
        :type ClusterType: str
        :param _ClusterId: 集成容器服务中关联的集群ID
        :type ClusterId: str
        :param _Describe: 该参数未使用，不需要填写
        :type Describe: str
        """
        self._ClusterType = None
        self._ClusterId = None
        self._Describe = None

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe


    def _deserialize(self, params):
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAgentOverview(AbstractModel):
    """托管prometheus agent概览

    """

    def __init__(self):
        r"""
        :param _ClusterType: 集群类型
        :type ClusterType: str
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Status: agent状态
normal = 正常
abnormal = 异常
        :type Status: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _ExternalLabels: 额外labels
本集群的所有指标都会带上这几个label
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalLabels: list of Label
        :param _Region: 集群所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _VpcId: 集群所在VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _FailedReason: 记录关联等操作的失败信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReason: str
        :param _Name: agent名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _EnableExternal: 是否已开启公网访问，true 开启，false 未开启
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableExternal: bool
        :param _DesiredAgentNum: 采集agent期望pod数
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredAgentNum: int
        :param _ReadyAgentNum: 采集agent已正常启动pod数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadyAgentNum: int
        """
        self._ClusterType = None
        self._ClusterId = None
        self._Status = None
        self._ClusterName = None
        self._ExternalLabels = None
        self._Region = None
        self._VpcId = None
        self._FailedReason = None
        self._Name = None
        self._EnableExternal = None
        self._DesiredAgentNum = None
        self._ReadyAgentNum = None

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ExternalLabels(self):
        return self._ExternalLabels

    @ExternalLabels.setter
    def ExternalLabels(self, ExternalLabels):
        self._ExternalLabels = ExternalLabels

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def FailedReason(self):
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnableExternal(self):
        return self._EnableExternal

    @EnableExternal.setter
    def EnableExternal(self, EnableExternal):
        self._EnableExternal = EnableExternal

    @property
    def DesiredAgentNum(self):
        return self._DesiredAgentNum

    @DesiredAgentNum.setter
    def DesiredAgentNum(self, DesiredAgentNum):
        self._DesiredAgentNum = DesiredAgentNum

    @property
    def ReadyAgentNum(self):
        return self._ReadyAgentNum

    @ReadyAgentNum.setter
    def ReadyAgentNum(self, ReadyAgentNum):
        self._ReadyAgentNum = ReadyAgentNum


    def _deserialize(self, params):
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._Status = params.get("Status")
        self._ClusterName = params.get("ClusterName")
        if params.get("ExternalLabels") is not None:
            self._ExternalLabels = []
            for item in params.get("ExternalLabels"):
                obj = Label()
                obj._deserialize(item)
                self._ExternalLabels.append(obj)
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._FailedReason = params.get("FailedReason")
        self._Name = params.get("Name")
        self._EnableExternal = params.get("EnableExternal")
        self._DesiredAgentNum = params.get("DesiredAgentNum")
        self._ReadyAgentNum = params.get("ReadyAgentNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertAllowTimeRange(AbstractModel):
    """Prometheus自定义告警通知时间段

    """

    def __init__(self):
        r"""
        :param _Start: 从0点开始的秒数
注意：此字段可能返回 null，表示取不到有效值。
        :type Start: str
        :param _End: 从0点开始的秒数
注意：此字段可能返回 null，表示取不到有效值。
        :type End: str
        """
        self._Start = None
        self._End = None

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertCustomReceiver(AbstractModel):
    """Prometheus告警自定义通知模板

    """

    def __init__(self):
        r"""
        :param _Type: 自定义通知类型
alertmanager -- vpc内自建alertmanager
webhook -- vpc内webhook地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Url: alertmanager/webhook地址。（prometheus实例同vpc内ip）
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _AllowedTimeRanges: 允许发送告警的时间范围
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowedTimeRanges: list of PrometheusAlertAllowTimeRange
        :param _ClusterId: alertmanager所在的内网集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterType: alertmanager所在的内网集群类型(tke/eks/tdcc)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        """
        self._Type = None
        self._Url = None
        self._AllowedTimeRanges = None
        self._ClusterId = None
        self._ClusterType = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AllowedTimeRanges(self):
        return self._AllowedTimeRanges

    @AllowedTimeRanges.setter
    def AllowedTimeRanges(self, AllowedTimeRanges):
        self._AllowedTimeRanges = AllowedTimeRanges

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        if params.get("AllowedTimeRanges") is not None:
            self._AllowedTimeRanges = []
            for item in params.get("AllowedTimeRanges"):
                obj = PrometheusAlertAllowTimeRange()
                obj._deserialize(item)
                self._AllowedTimeRanges.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertGroupRuleSet(AbstractModel):
    """告警分组内告警规则信息

    """

    def __init__(self):
        r"""
        :param _RuleName: 告警规则名称，同一告警分组下不允许重名
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _Labels: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of PrometheusRuleKV
        :param _Annotations: 注释列表

告警对象和告警消息是 Prometheus Rule Annotations 的特殊字段，需要通过 annotations 来传递，对应的 Key 分别为summary/description。
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotations: list of PrometheusRuleKV
        :param _Duration: 规则报警持续时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _Expr: 规则表达式，可参考<a href="https://cloud.tencent.com/document/product/1416/56008">告警规则说明</a>
注意：此字段可能返回 null，表示取不到有效值。
        :type Expr: str
        :param _State: 告警规则状态:
2-启用
3-禁用
为空默认启用
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        """
        self._RuleName = None
        self._Labels = None
        self._Annotations = None
        self._Duration = None
        self._Expr = None
        self._State = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Expr(self):
        return self._Expr

    @Expr.setter
    def Expr(self, Expr):
        self._Expr = Expr

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._Duration = params.get("Duration")
        self._Expr = params.get("Expr")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertGroupSet(AbstractModel):
    """Prometheus告警规则分组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 告警分组ID，满足正则表达式`alert-[a-z0-9]{8}`
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 告警分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _AMPReceivers: 云监控告警模板ID ，返回告警模板转换后的notice ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AMPReceivers: list of str
        :param _CustomReceiver: 自定义告警模板
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomReceiver: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertCustomReceiver`
        :param _RepeatInterval: 告警通知间隔
注意：此字段可能返回 null，表示取不到有效值。
        :type RepeatInterval: str
        :param _TemplateId: 若告警分组通过模板创建，则返回模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _Rules: 分组内告警规则详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of PrometheusAlertGroupRuleSet
        :param _CreatedAt: 分组创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 分组更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self._GroupId = None
        self._GroupName = None
        self._AMPReceivers = None
        self._CustomReceiver = None
        self._RepeatInterval = None
        self._TemplateId = None
        self._Rules = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def AMPReceivers(self):
        return self._AMPReceivers

    @AMPReceivers.setter
    def AMPReceivers(self, AMPReceivers):
        self._AMPReceivers = AMPReceivers

    @property
    def CustomReceiver(self):
        return self._CustomReceiver

    @CustomReceiver.setter
    def CustomReceiver(self, CustomReceiver):
        self._CustomReceiver = CustomReceiver

    @property
    def RepeatInterval(self):
        return self._RepeatInterval

    @RepeatInterval.setter
    def RepeatInterval(self, RepeatInterval):
        self._RepeatInterval = RepeatInterval

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._AMPReceivers = params.get("AMPReceivers")
        if params.get("CustomReceiver") is not None:
            self._CustomReceiver = PrometheusAlertCustomReceiver()
            self._CustomReceiver._deserialize(params.get("CustomReceiver"))
        self._RepeatInterval = params.get("RepeatInterval")
        self._TemplateId = params.get("TemplateId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertGroupRuleSet()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertManagerConfig(AbstractModel):
    """告警渠道使用自建alertmanager的配置

    """

    def __init__(self):
        r"""
        :param _Url: alertmanager url
        :type Url: str
        :param _ClusterType: alertmanager部署所在集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param _ClusterId: alertmanager部署所在集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self._Url = None
        self._ClusterType = None
        self._ClusterId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertPolicyItem(AbstractModel):
    """托管prometheus告警策略实例

    """

    def __init__(self):
        r"""
        :param _Name: 策略名称
        :type Name: str
        :param _Rules: 规则列表
        :type Rules: list of PrometheusAlertRule
        :param _Id: 告警策略 id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _TemplateId: 如果该告警来自模板下发，则TemplateId为模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _Notification: 告警渠道，模板中使用可能返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        :param _UpdatedAt: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _ClusterId: 如果告警策略来源于用户集群CRD资源定义，则ClusterId为所属集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self._Name = None
        self._Rules = None
        self._Id = None
        self._TemplateId = None
        self._Notification = None
        self._UpdatedAt = None
        self._ClusterId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Id = params.get("Id")
        self._TemplateId = params.get("TemplateId")
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotificationItem()
            self._Notification._deserialize(params.get("Notification"))
        self._UpdatedAt = params.get("UpdatedAt")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRule(AbstractModel):
    """Prometheus告警规则

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _Rule: prometheus语句
        :type Rule: str
        :param _Labels: 额外标签
        :type Labels: list of Label
        :param _Template: 告警发送模板
        :type Template: str
        :param _For: 持续时间
        :type For: str
        :param _Describe: 该条规则的描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _Annotations: 参考prometheus rule中的annotations
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotations: list of Label
        :param _RuleState: 告警规则状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleState: int
        """
        self._Name = None
        self._Rule = None
        self._Labels = None
        self._Template = None
        self._For = None
        self._Describe = None
        self._Annotations = None
        self._RuleState = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def For(self):
        return self._For

    @For.setter
    def For(self, For):
        self._For = For

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Rule = params.get("Rule")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._Template = params.get("Template")
        self._For = params.get("For")
        self._Describe = params.get("Describe")
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Label()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusClusterAgentBasic(AbstractModel):
    """与腾讯云可观测平台融合托管 Prometheus 实例，关联集群基础信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _ClusterType: 集群类型。可填入tke、eks、tkeedge、tdcc，分别代表标准集群、弹性集群、边缘集群、注册集群
        :type ClusterType: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _EnableExternal: 是否开启公网CLB
        :type EnableExternal: bool
        :param _InClusterPodConfig: 集群内部署组件的pod配置
        :type InClusterPodConfig: :class:`tencentcloud.monitor.v20180724.models.PrometheusClusterAgentPodConfig`
        :param _ExternalLabels: 该集群采集的所有指标都会带上这些labels
        :type ExternalLabels: list of Label
        :param _NotInstallBasicScrape: 是否安装默认采集配置
        :type NotInstallBasicScrape: bool
        :param _NotScrape: 是否采集指标，true代表drop所有指标，false代表采集默认指标
        :type NotScrape: bool
        :param _OpenDefaultRecord: 是否开启默认预聚合规则
        :type OpenDefaultRecord: bool
        """
        self._Region = None
        self._ClusterType = None
        self._ClusterId = None
        self._EnableExternal = None
        self._InClusterPodConfig = None
        self._ExternalLabels = None
        self._NotInstallBasicScrape = None
        self._NotScrape = None
        self._OpenDefaultRecord = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnableExternal(self):
        return self._EnableExternal

    @EnableExternal.setter
    def EnableExternal(self, EnableExternal):
        self._EnableExternal = EnableExternal

    @property
    def InClusterPodConfig(self):
        return self._InClusterPodConfig

    @InClusterPodConfig.setter
    def InClusterPodConfig(self, InClusterPodConfig):
        self._InClusterPodConfig = InClusterPodConfig

    @property
    def ExternalLabels(self):
        return self._ExternalLabels

    @ExternalLabels.setter
    def ExternalLabels(self, ExternalLabels):
        self._ExternalLabels = ExternalLabels

    @property
    def NotInstallBasicScrape(self):
        return self._NotInstallBasicScrape

    @NotInstallBasicScrape.setter
    def NotInstallBasicScrape(self, NotInstallBasicScrape):
        self._NotInstallBasicScrape = NotInstallBasicScrape

    @property
    def NotScrape(self):
        return self._NotScrape

    @NotScrape.setter
    def NotScrape(self, NotScrape):
        self._NotScrape = NotScrape

    @property
    def OpenDefaultRecord(self):
        return self._OpenDefaultRecord

    @OpenDefaultRecord.setter
    def OpenDefaultRecord(self, OpenDefaultRecord):
        self._OpenDefaultRecord = OpenDefaultRecord


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._EnableExternal = params.get("EnableExternal")
        if params.get("InClusterPodConfig") is not None:
            self._InClusterPodConfig = PrometheusClusterAgentPodConfig()
            self._InClusterPodConfig._deserialize(params.get("InClusterPodConfig"))
        if params.get("ExternalLabels") is not None:
            self._ExternalLabels = []
            for item in params.get("ExternalLabels"):
                obj = Label()
                obj._deserialize(item)
                self._ExternalLabels.append(obj)
        self._NotInstallBasicScrape = params.get("NotInstallBasicScrape")
        self._NotScrape = params.get("NotScrape")
        self._OpenDefaultRecord = params.get("OpenDefaultRecord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusClusterAgentPodConfig(AbstractModel):
    """关联集群时在集群内部署组件的pod额外配置

    """

    def __init__(self):
        r"""
        :param _HostNet: 是否使用HostNetWork
        :type HostNet: bool
        :param _NodeSelector: 指定pod运行节点
        :type NodeSelector: list of Label
        :param _Tolerations: 容忍污点
        :type Tolerations: list of Toleration
        """
        self._HostNet = None
        self._NodeSelector = None
        self._Tolerations = None

    @property
    def HostNet(self):
        return self._HostNet

    @HostNet.setter
    def HostNet(self, HostNet):
        self._HostNet = HostNet

    @property
    def NodeSelector(self):
        return self._NodeSelector

    @NodeSelector.setter
    def NodeSelector(self, NodeSelector):
        self._NodeSelector = NodeSelector

    @property
    def Tolerations(self):
        return self._Tolerations

    @Tolerations.setter
    def Tolerations(self, Tolerations):
        self._Tolerations = Tolerations


    def _deserialize(self, params):
        self._HostNet = params.get("HostNet")
        if params.get("NodeSelector") is not None:
            self._NodeSelector = []
            for item in params.get("NodeSelector"):
                obj = Label()
                obj._deserialize(item)
                self._NodeSelector.append(obj)
        if params.get("Tolerations") is not None:
            self._Tolerations = []
            for item in params.get("Tolerations"):
                obj = Toleration()
                obj._deserialize(item)
                self._Tolerations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusConfigItem(AbstractModel):
    """prometheus配置

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Config: 配置内容
        :type Config: str
        :param _TemplateId: 用于出参，如果该配置来至模板，则为模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _Targets: 目标数
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: :class:`tencentcloud.monitor.v20180724.models.Targets`
        """
        self._Name = None
        self._Config = None
        self._TemplateId = None
        self._Targets = None

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
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Config = params.get("Config")
        self._TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self._Targets = Targets()
            self._Targets._deserialize(params.get("Targets"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstanceGrantInfo(AbstractModel):
    """实例的授权信息

    """

    def __init__(self):
        r"""
        :param _HasChargeOperation: 是否有计费操作权限(1=有，2=无)
        :type HasChargeOperation: int
        :param _HasVpcDisplay: 是否显示VPC信息的权限(1=有，2=无)
        :type HasVpcDisplay: int
        :param _HasGrafanaStatusChange: 是否可修改Grafana的状态(1=有，2=无)
        :type HasGrafanaStatusChange: int
        :param _HasAgentManage: 是否有管理agent的权限(1=有，2=无)
        :type HasAgentManage: int
        :param _HasTkeManage: 是否有管理TKE集成的权限(1=有，2=无)
        :type HasTkeManage: int
        :param _HasApiOperation: 是否显示API等信息(1=有, 2=无)
        :type HasApiOperation: int
        """
        self._HasChargeOperation = None
        self._HasVpcDisplay = None
        self._HasGrafanaStatusChange = None
        self._HasAgentManage = None
        self._HasTkeManage = None
        self._HasApiOperation = None

    @property
    def HasChargeOperation(self):
        return self._HasChargeOperation

    @HasChargeOperation.setter
    def HasChargeOperation(self, HasChargeOperation):
        self._HasChargeOperation = HasChargeOperation

    @property
    def HasVpcDisplay(self):
        return self._HasVpcDisplay

    @HasVpcDisplay.setter
    def HasVpcDisplay(self, HasVpcDisplay):
        self._HasVpcDisplay = HasVpcDisplay

    @property
    def HasGrafanaStatusChange(self):
        return self._HasGrafanaStatusChange

    @HasGrafanaStatusChange.setter
    def HasGrafanaStatusChange(self, HasGrafanaStatusChange):
        self._HasGrafanaStatusChange = HasGrafanaStatusChange

    @property
    def HasAgentManage(self):
        return self._HasAgentManage

    @HasAgentManage.setter
    def HasAgentManage(self, HasAgentManage):
        self._HasAgentManage = HasAgentManage

    @property
    def HasTkeManage(self):
        return self._HasTkeManage

    @HasTkeManage.setter
    def HasTkeManage(self, HasTkeManage):
        self._HasTkeManage = HasTkeManage

    @property
    def HasApiOperation(self):
        return self._HasApiOperation

    @HasApiOperation.setter
    def HasApiOperation(self, HasApiOperation):
        self._HasApiOperation = HasApiOperation


    def _deserialize(self, params):
        self._HasChargeOperation = params.get("HasChargeOperation")
        self._HasVpcDisplay = params.get("HasVpcDisplay")
        self._HasGrafanaStatusChange = params.get("HasGrafanaStatusChange")
        self._HasAgentManage = params.get("HasAgentManage")
        self._HasTkeManage = params.get("HasTkeManage")
        self._HasApiOperation = params.get("HasApiOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstanceTenantUsage(AbstractModel):
    """Prometheus用量信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _CalcDate: 计费周期
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcDate: str
        :param _Total: 总用量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: float
        :param _Basic: 基础指标用量
注意：此字段可能返回 null，表示取不到有效值。
        :type Basic: float
        :param _Fee: 付费指标用量
注意：此字段可能返回 null，表示取不到有效值。
        :type Fee: float
        """
        self._InstanceId = None
        self._CalcDate = None
        self._Total = None
        self._Basic = None
        self._Fee = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CalcDate(self):
        return self._CalcDate

    @CalcDate.setter
    def CalcDate(self, CalcDate):
        self._CalcDate = CalcDate

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Basic(self):
        return self._Basic

    @Basic.setter
    def Basic(self, Basic):
        self._Basic = Basic

    @property
    def Fee(self):
        return self._Fee

    @Fee.setter
    def Fee(self, Fee):
        self._Fee = Fee


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CalcDate = params.get("CalcDate")
        self._Total = params.get("Total")
        self._Basic = params.get("Basic")
        self._Fee = params.get("Fee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstancesItem(AbstractModel):
    """Prometheus 服务响应体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _InstanceChargeType: 实例计费模式。取值范围：
<ul>
<li>2：包年包月</li>
<li>3：按量</li>
</ul>
        :type InstanceChargeType: int
        :param _RegionId: 地域 ID
        :type RegionId: int
        :param _Zone: 可用区
        :type Zone: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: 子网 ID
        :type SubnetId: str
        :param _DataRetentionTime: 存储周期
注意：此字段可能返回 null，表示取不到有效值。
        :type DataRetentionTime: int
        :param _InstanceStatus: 实例业务状态。取值范围：
<ul>
<li>1：正在创建</li>
<li>2：运行中</li>
<li>3：异常</li>
<li>4：重建中</li>
<li>5：销毁中</li>
<li>6：已停服</li>
<li>8：欠费停服中</li>
<li>9：欠费已停服</li>
</ul>
        :type InstanceStatus: int
        :param _GrafanaURL: Grafana 面板 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaURL: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _EnableGrafana: 是否开启 Grafana
<li>0：不开启</li>
<li>1：开启</li>
        :type EnableGrafana: int
        :param _IPv4Address: 实例IPV4地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv4Address: str
        :param _TagSpecification: 实例关联的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: list of PrometheusTag
        :param _ExpireTime: 购买的实例过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _ChargeStatus: 计费状态
<ul>
<li>1：正常</li>
<li>2：过期</li>
<li>3：销毁</li>
<li>4：分配中</li>
<li>5：分配失败</li>
</ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeStatus: int
        :param _SpecName: 规格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _AutoRenewFlag: 自动续费标记
<ul>
<li>0：不自动续费</li>
<li>1：开启自动续费</li>
<li>2：禁止自动续费</li>
<li>-1：无效</li>
</ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _IsNearExpire: 是否快过期
<ul>
<li>0：否</li>
<li>1：快过期</li>
</ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNearExpire: int
        :param _AuthToken: 数据写入需要的 Token
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthToken: str
        :param _RemoteWrite: Prometheus Remote Write 的地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoteWrite: str
        :param _ApiRootPath: Prometheus HTTP Api 根地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiRootPath: str
        :param _ProxyAddress: Proxy 的地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyAddress: str
        :param _GrafanaStatus: Grafana 运行状态
<ul>
<li>1：正在创建</li>
<li>2：运行中</li>
<li>3：异常</li>
<li>4：重启中</li>
<li>5：销毁中</li>
<li>6：已停机</li>
<li>7：已删除</li>
</ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaStatus: int
        :param _GrafanaIpWhiteList: Grafana IP 白名单列表，使用英文分号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaIpWhiteList: str
        :param _Grant: 实例的授权信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Grant: :class:`tencentcloud.monitor.v20180724.models.PrometheusInstanceGrantInfo`
        :param _GrafanaInstanceId: 绑定的 Grafana 实例 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaInstanceId: str
        :param _AlertRuleLimit: 告警规则限制
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRuleLimit: int
        :param _RecordingRuleLimit: 预聚合规则限制
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordingRuleLimit: int
        :param _MigrationType: 迁移状态，0-不在迁移中，1-迁移中、原实例，2-迁移中、目标实例
注意：此字段可能返回 null，表示取不到有效值。
        :type MigrationType: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._RegionId = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._DataRetentionTime = None
        self._InstanceStatus = None
        self._GrafanaURL = None
        self._CreatedAt = None
        self._EnableGrafana = None
        self._IPv4Address = None
        self._TagSpecification = None
        self._ExpireTime = None
        self._ChargeStatus = None
        self._SpecName = None
        self._AutoRenewFlag = None
        self._IsNearExpire = None
        self._AuthToken = None
        self._RemoteWrite = None
        self._ApiRootPath = None
        self._ProxyAddress = None
        self._GrafanaStatus = None
        self._GrafanaIpWhiteList = None
        self._Grant = None
        self._GrafanaInstanceId = None
        self._AlertRuleLimit = None
        self._RecordingRuleLimit = None
        self._MigrationType = None

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
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def GrafanaURL(self):
        return self._GrafanaURL

    @GrafanaURL.setter
    def GrafanaURL(self, GrafanaURL):
        self._GrafanaURL = GrafanaURL

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def EnableGrafana(self):
        return self._EnableGrafana

    @EnableGrafana.setter
    def EnableGrafana(self, EnableGrafana):
        self._EnableGrafana = EnableGrafana

    @property
    def IPv4Address(self):
        return self._IPv4Address

    @IPv4Address.setter
    def IPv4Address(self, IPv4Address):
        self._IPv4Address = IPv4Address

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def IsNearExpire(self):
        return self._IsNearExpire

    @IsNearExpire.setter
    def IsNearExpire(self, IsNearExpire):
        self._IsNearExpire = IsNearExpire

    @property
    def AuthToken(self):
        return self._AuthToken

    @AuthToken.setter
    def AuthToken(self, AuthToken):
        self._AuthToken = AuthToken

    @property
    def RemoteWrite(self):
        return self._RemoteWrite

    @RemoteWrite.setter
    def RemoteWrite(self, RemoteWrite):
        self._RemoteWrite = RemoteWrite

    @property
    def ApiRootPath(self):
        return self._ApiRootPath

    @ApiRootPath.setter
    def ApiRootPath(self, ApiRootPath):
        self._ApiRootPath = ApiRootPath

    @property
    def ProxyAddress(self):
        return self._ProxyAddress

    @ProxyAddress.setter
    def ProxyAddress(self, ProxyAddress):
        self._ProxyAddress = ProxyAddress

    @property
    def GrafanaStatus(self):
        return self._GrafanaStatus

    @GrafanaStatus.setter
    def GrafanaStatus(self, GrafanaStatus):
        self._GrafanaStatus = GrafanaStatus

    @property
    def GrafanaIpWhiteList(self):
        return self._GrafanaIpWhiteList

    @GrafanaIpWhiteList.setter
    def GrafanaIpWhiteList(self, GrafanaIpWhiteList):
        self._GrafanaIpWhiteList = GrafanaIpWhiteList

    @property
    def Grant(self):
        return self._Grant

    @Grant.setter
    def Grant(self, Grant):
        self._Grant = Grant

    @property
    def GrafanaInstanceId(self):
        return self._GrafanaInstanceId

    @GrafanaInstanceId.setter
    def GrafanaInstanceId(self, GrafanaInstanceId):
        self._GrafanaInstanceId = GrafanaInstanceId

    @property
    def AlertRuleLimit(self):
        return self._AlertRuleLimit

    @AlertRuleLimit.setter
    def AlertRuleLimit(self, AlertRuleLimit):
        self._AlertRuleLimit = AlertRuleLimit

    @property
    def RecordingRuleLimit(self):
        return self._RecordingRuleLimit

    @RecordingRuleLimit.setter
    def RecordingRuleLimit(self, RecordingRuleLimit):
        self._RecordingRuleLimit = RecordingRuleLimit

    @property
    def MigrationType(self):
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._RegionId = params.get("RegionId")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DataRetentionTime = params.get("DataRetentionTime")
        self._InstanceStatus = params.get("InstanceStatus")
        self._GrafanaURL = params.get("GrafanaURL")
        self._CreatedAt = params.get("CreatedAt")
        self._EnableGrafana = params.get("EnableGrafana")
        self._IPv4Address = params.get("IPv4Address")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._ExpireTime = params.get("ExpireTime")
        self._ChargeStatus = params.get("ChargeStatus")
        self._SpecName = params.get("SpecName")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._IsNearExpire = params.get("IsNearExpire")
        self._AuthToken = params.get("AuthToken")
        self._RemoteWrite = params.get("RemoteWrite")
        self._ApiRootPath = params.get("ApiRootPath")
        self._ProxyAddress = params.get("ProxyAddress")
        self._GrafanaStatus = params.get("GrafanaStatus")
        self._GrafanaIpWhiteList = params.get("GrafanaIpWhiteList")
        if params.get("Grant") is not None:
            self._Grant = PrometheusInstanceGrantInfo()
            self._Grant._deserialize(params.get("Grant"))
        self._GrafanaInstanceId = params.get("GrafanaInstanceId")
        self._AlertRuleLimit = params.get("AlertRuleLimit")
        self._RecordingRuleLimit = params.get("RecordingRuleLimit")
        self._MigrationType = params.get("MigrationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstancesOverview(AbstractModel):
    """托管prometheusV2实例概览

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _InstanceStatus: 运行状态（1:正在创建；2:运行中；3:异常；4:重启中；5:销毁中； 6:已停机； 7: 已删除）
        :type InstanceStatus: int
        :param _ChargeStatus: 计费状态（1:正常；2:过期; 3:销毁; 4:分配中; 5:分配失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeStatus: int
        :param _EnableGrafana: 是否开启 Grafana（0:不开启，1:开启）
        :type EnableGrafana: int
        :param _GrafanaURL: Grafana 面板 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaURL: str
        :param _InstanceChargeType: 实例付费类型（1:试用版；2:预付费）
        :type InstanceChargeType: int
        :param _SpecName: 规格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _DataRetentionTime: 存储周期
注意：此字段可能返回 null，表示取不到有效值。
        :type DataRetentionTime: int
        :param _ExpireTime: 购买的实例过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _AutoRenewFlag: 自动续费标记(0:不自动续费；1:开启自动续费；2:禁止自动续费；-1:无效)
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _BoundTotal: 绑定集群总数
        :type BoundTotal: int
        :param _BoundNormal: 绑定集群正常状态总数
        :type BoundNormal: int
        :param _ResourcePackageStatus: 资源包状态，0-无可用资源包，1-有可用资源包
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourcePackageStatus: int
        :param _ResourcePackageSpecName: 资源包规格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourcePackageSpecName: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceStatus = None
        self._ChargeStatus = None
        self._EnableGrafana = None
        self._GrafanaURL = None
        self._InstanceChargeType = None
        self._SpecName = None
        self._DataRetentionTime = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._BoundTotal = None
        self._BoundNormal = None
        self._ResourcePackageStatus = None
        self._ResourcePackageSpecName = None

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
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def EnableGrafana(self):
        return self._EnableGrafana

    @EnableGrafana.setter
    def EnableGrafana(self, EnableGrafana):
        self._EnableGrafana = EnableGrafana

    @property
    def GrafanaURL(self):
        return self._GrafanaURL

    @GrafanaURL.setter
    def GrafanaURL(self, GrafanaURL):
        self._GrafanaURL = GrafanaURL

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def BoundTotal(self):
        return self._BoundTotal

    @BoundTotal.setter
    def BoundTotal(self, BoundTotal):
        self._BoundTotal = BoundTotal

    @property
    def BoundNormal(self):
        return self._BoundNormal

    @BoundNormal.setter
    def BoundNormal(self, BoundNormal):
        self._BoundNormal = BoundNormal

    @property
    def ResourcePackageStatus(self):
        return self._ResourcePackageStatus

    @ResourcePackageStatus.setter
    def ResourcePackageStatus(self, ResourcePackageStatus):
        self._ResourcePackageStatus = ResourcePackageStatus

    @property
    def ResourcePackageSpecName(self):
        return self._ResourcePackageSpecName

    @ResourcePackageSpecName.setter
    def ResourcePackageSpecName(self, ResourcePackageSpecName):
        self._ResourcePackageSpecName = ResourcePackageSpecName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._ChargeStatus = params.get("ChargeStatus")
        self._EnableGrafana = params.get("EnableGrafana")
        self._GrafanaURL = params.get("GrafanaURL")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SpecName = params.get("SpecName")
        self._DataRetentionTime = params.get("DataRetentionTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._BoundTotal = params.get("BoundTotal")
        self._BoundNormal = params.get("BoundNormal")
        self._ResourcePackageStatus = params.get("ResourcePackageStatus")
        self._ResourcePackageSpecName = params.get("ResourcePackageSpecName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusJobTargets(AbstractModel):
    """prometheus一个job的targets

    """

    def __init__(self):
        r"""
        :param _Targets: 该Job的targets列表
        :type Targets: list of PrometheusTarget
        :param _JobName: job的名称
        :type JobName: str
        :param _Total: targets总数
        :type Total: int
        :param _Up: 健康的target总数
        :type Up: int
        """
        self._Targets = None
        self._JobName = None
        self._Total = None
        self._Up = None

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Up(self):
        return self._Up

    @Up.setter
    def Up(self, Up):
        self._Up = Up


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._JobName = params.get("JobName")
        self._Total = params.get("Total")
        self._Up = params.get("Up")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusNotificationItem(AbstractModel):
    """告警通知渠道配置

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否启用
        :type Enabled: bool
        :param _Type: 通道类型，默认为amp，支持以下
amp
webhook
alertmanager
        :type Type: str
        :param _WebHook: 如果Type为webhook, 则该字段为必填项
注意：此字段可能返回 null，表示取不到有效值。
        :type WebHook: str
        :param _AlertManager: 如果Type为alertmanager, 则该字段为必填项
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertManager: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertManagerConfig`
        :param _RepeatInterval: 收敛时间
        :type RepeatInterval: str
        :param _TimeRangeStart: 生效起始时间
        :type TimeRangeStart: str
        :param _TimeRangeEnd: 生效结束时间
        :type TimeRangeEnd: str
        :param _NotifyWay: 告警通知方式。目前有SMS、EMAIL、CALL、WECHAT方式。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyWay: list of str
        :param _ReceiverGroups: 告警接收组（用户组）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverGroups: list of str
        :param _PhoneNotifyOrder: 电话告警顺序。
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNotifyOrder: list of int non-negative
        :param _PhoneCircleTimes: 电话告警次数。
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCircleTimes: int
        :param _PhoneInnerInterval: 电话告警轮内间隔。单位：秒
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneInnerInterval: int
        :param _PhoneCircleInterval: 电话告警轮外间隔。单位：秒
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCircleInterval: int
        :param _PhoneArriveNotice: 电话告警触达通知
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneArriveNotice: bool
        """
        self._Enabled = None
        self._Type = None
        self._WebHook = None
        self._AlertManager = None
        self._RepeatInterval = None
        self._TimeRangeStart = None
        self._TimeRangeEnd = None
        self._NotifyWay = None
        self._ReceiverGroups = None
        self._PhoneNotifyOrder = None
        self._PhoneCircleTimes = None
        self._PhoneInnerInterval = None
        self._PhoneCircleInterval = None
        self._PhoneArriveNotice = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WebHook(self):
        return self._WebHook

    @WebHook.setter
    def WebHook(self, WebHook):
        self._WebHook = WebHook

    @property
    def AlertManager(self):
        return self._AlertManager

    @AlertManager.setter
    def AlertManager(self, AlertManager):
        self._AlertManager = AlertManager

    @property
    def RepeatInterval(self):
        return self._RepeatInterval

    @RepeatInterval.setter
    def RepeatInterval(self, RepeatInterval):
        self._RepeatInterval = RepeatInterval

    @property
    def TimeRangeStart(self):
        return self._TimeRangeStart

    @TimeRangeStart.setter
    def TimeRangeStart(self, TimeRangeStart):
        self._TimeRangeStart = TimeRangeStart

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def PhoneNotifyOrder(self):
        return self._PhoneNotifyOrder

    @PhoneNotifyOrder.setter
    def PhoneNotifyOrder(self, PhoneNotifyOrder):
        self._PhoneNotifyOrder = PhoneNotifyOrder

    @property
    def PhoneCircleTimes(self):
        return self._PhoneCircleTimes

    @PhoneCircleTimes.setter
    def PhoneCircleTimes(self, PhoneCircleTimes):
        self._PhoneCircleTimes = PhoneCircleTimes

    @property
    def PhoneInnerInterval(self):
        return self._PhoneInnerInterval

    @PhoneInnerInterval.setter
    def PhoneInnerInterval(self, PhoneInnerInterval):
        self._PhoneInnerInterval = PhoneInnerInterval

    @property
    def PhoneCircleInterval(self):
        return self._PhoneCircleInterval

    @PhoneCircleInterval.setter
    def PhoneCircleInterval(self, PhoneCircleInterval):
        self._PhoneCircleInterval = PhoneCircleInterval

    @property
    def PhoneArriveNotice(self):
        return self._PhoneArriveNotice

    @PhoneArriveNotice.setter
    def PhoneArriveNotice(self, PhoneArriveNotice):
        self._PhoneArriveNotice = PhoneArriveNotice


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Type = params.get("Type")
        self._WebHook = params.get("WebHook")
        if params.get("AlertManager") is not None:
            self._AlertManager = PrometheusAlertManagerConfig()
            self._AlertManager._deserialize(params.get("AlertManager"))
        self._RepeatInterval = params.get("RepeatInterval")
        self._TimeRangeStart = params.get("TimeRangeStart")
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        self._NotifyWay = params.get("NotifyWay")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._PhoneNotifyOrder = params.get("PhoneNotifyOrder")
        self._PhoneCircleTimes = params.get("PhoneCircleTimes")
        self._PhoneInnerInterval = params.get("PhoneInnerInterval")
        self._PhoneCircleInterval = params.get("PhoneCircleInterval")
        self._PhoneArriveNotice = params.get("PhoneArriveNotice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRecordRuleYamlItem(AbstractModel):
    """prometheus聚合规则实例详情，包含所属集群ID

    """

    def __init__(self):
        r"""
        :param _Name: 实例名称
        :type Name: str
        :param _UpdateTime: 最近更新时间
        :type UpdateTime: str
        :param _TemplateId: Yaml内容
        :type TemplateId: str
        :param _Content: 如果该聚合规则来至模板，则TemplateId为模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _ClusterId: 该聚合规则如果来源于用户集群crd资源定义，则ClusterId为所属集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Id: id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Count: 规则数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._Name = None
        self._UpdateTime = None
        self._TemplateId = None
        self._Content = None
        self._ClusterId = None
        self._Status = None
        self._Id = None
        self._Count = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._UpdateTime = params.get("UpdateTime")
        self._TemplateId = params.get("TemplateId")
        self._Content = params.get("Content")
        self._ClusterId = params.get("ClusterId")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRegionItem(AbstractModel):
    """DescribePrometheusRegions 响应结构体

    """

    def __init__(self):
        r"""
        :param _Region: 区域
        :type Region: str
        :param _RegionId: 区域 ID
        :type RegionId: int
        :param _RegionState: 区域状态( 0: 不可用；1: 可用)
        :type RegionState: int
        :param _RegionName: 区域名(中文)
        :type RegionName: str
        :param _RegionShortName: 区域名(英文缩写)
        :type RegionShortName: str
        :param _Area: 区域所在大区名
        :type Area: str
        :param _RegionPayMode: 1-仅支持预付费，2-仅支持后付费，3-支持两种计费模式实例
        :type RegionPayMode: int
        """
        self._Region = None
        self._RegionId = None
        self._RegionState = None
        self._RegionName = None
        self._RegionShortName = None
        self._Area = None
        self._RegionPayMode = None

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
    def RegionState(self):
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionShortName(self):
        return self._RegionShortName

    @RegionShortName.setter
    def RegionShortName(self, RegionShortName):
        self._RegionShortName = RegionShortName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def RegionPayMode(self):
        return self._RegionPayMode

    @RegionPayMode.setter
    def RegionPayMode(self, RegionPayMode):
        self._RegionPayMode = RegionPayMode


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._RegionState = params.get("RegionState")
        self._RegionName = params.get("RegionName")
        self._RegionShortName = params.get("RegionShortName")
        self._Area = params.get("Area")
        self._RegionPayMode = params.get("RegionPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRuleKV(AbstractModel):
    """prometheus 报警规则 KV 参数

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
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
        


class PrometheusRuleSet(AbstractModel):
    """prometheus 报警规则集

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _RuleState: 规则状态码
        :type RuleState: int
        :param _Type: 规则类别
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Labels: 规则标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of PrometheusRuleKV
        :param _Annotations: 规则注释列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotations: list of PrometheusRuleKV
        :param _Expr: 规则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type Expr: str
        :param _Duration: 规则报警持续时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _Receivers: 报警接收组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Receivers: list of str
        :param _Health: 规则运行健康状态，取值如下：
<li>unknown 未知状态</li>
<li>pending 加载中</li>
<li>ok 运行正常</li>
<li>err 运行错误</li>
        :type Health: str
        :param _CreatedAt: 规则创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 规则更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self._RuleId = None
        self._RuleName = None
        self._RuleState = None
        self._Type = None
        self._Labels = None
        self._Annotations = None
        self._Expr = None
        self._Duration = None
        self._Receivers = None
        self._Health = None
        self._CreatedAt = None
        self._UpdatedAt = None

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
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Expr(self):
        return self._Expr

    @Expr.setter
    def Expr(self, Expr):
        self._Expr = Expr

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def Health(self):
        return self._Health

    @Health.setter
    def Health(self, Health):
        self._Health = Health

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RuleState = params.get("RuleState")
        self._Type = params.get("Type")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._Expr = params.get("Expr")
        self._Duration = params.get("Duration")
        self._Receivers = params.get("Receivers")
        self._Health = params.get("Health")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusScrapeJob(AbstractModel):
    """Prometheus 抓取任务

    """

    def __init__(self):
        r"""
        :param _Name: 任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AgentId: Agent ID
        :type AgentId: str
        :param _JobId: 任务 ID
        :type JobId: str
        :param _Config: 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: str
        """
        self._Name = None
        self._AgentId = None
        self._JobId = None
        self._Config = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AgentId = params.get("AgentId")
        self._JobId = params.get("JobId")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTag(AbstractModel):
    """Prometheus 托管服务标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签的健值
        :type Key: str
        :param _Value: 标签对应的值
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
        


class PrometheusTarget(AbstractModel):
    """prometheus一个抓取目标的信息

    """


class PrometheusTemp(AbstractModel):
    """模板实例

    """

    def __init__(self):
        r"""
        :param _Name: 模板名称
        :type Name: str
        :param _Level: 模板维度，支持以下类型
instance 实例级别
cluster 集群级别
        :type Level: str
        :param _Describe: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _RecordRules: 当Level为instance时有效，
模板中的聚合规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordRules: list of PrometheusConfigItem
        :param _ServiceMonitors: 当Level为cluster时有效，
模板中的ServiceMonitor规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: 当Level为cluster时有效，
模板中的PodMonitors规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: 当Level为cluster时有效，
模板中的RawJobs规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RawJobs: list of PrometheusConfigItem
        :param _TemplateId: 模板的ID, 用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _UpdateTime: 最近更新时间，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Version: 当前版本，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _IsDefault: 是否系统提供的默认模板，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        :param _AlertDetailRules: 当Level为instance时有效，
模板中的告警配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertDetailRules: list of PrometheusAlertPolicyItem
        :param _TargetsTotal: 关联实例数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetsTotal: int
        """
        self._Name = None
        self._Level = None
        self._Describe = None
        self._RecordRules = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._TemplateId = None
        self._UpdateTime = None
        self._Version = None
        self._IsDefault = None
        self._AlertDetailRules = None
        self._TargetsTotal = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def RecordRules(self):
        return self._RecordRules

    @RecordRules.setter
    def RecordRules(self, RecordRules):
        self._RecordRules = RecordRules

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def AlertDetailRules(self):
        return self._AlertDetailRules

    @AlertDetailRules.setter
    def AlertDetailRules(self, AlertDetailRules):
        self._AlertDetailRules = AlertDetailRules

    @property
    def TargetsTotal(self):
        return self._TargetsTotal

    @TargetsTotal.setter
    def TargetsTotal(self, TargetsTotal):
        self._TargetsTotal = TargetsTotal


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._Describe = params.get("Describe")
        if params.get("RecordRules") is not None:
            self._RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RecordRules.append(obj)
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        self._TemplateId = params.get("TemplateId")
        self._UpdateTime = params.get("UpdateTime")
        self._Version = params.get("Version")
        self._IsDefault = params.get("IsDefault")
        if params.get("AlertDetailRules") is not None:
            self._AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self._AlertDetailRules.append(obj)
        self._TargetsTotal = params.get("TargetsTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTempModify(AbstractModel):
    """云原生Prometheus模板可修改项

    """

    def __init__(self):
        r"""
        :param _Name: 修改名称
        :type Name: str
        :param _Describe: 修改描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _ServiceMonitors: 当Level为cluster时有效，
模板中的ServiceMonitor规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: 当Level为cluster时有效，
模板中的PodMonitors规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: 当Level为cluster时有效，
模板中的RawJobs规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RawJobs: list of PrometheusConfigItem
        :param _RecordRules: 当Level为instance时有效，
模板中的聚合规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordRules: list of PrometheusConfigItem
        :param _AlertDetailRules: 修改内容，只有当模板类型是Alert时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertDetailRules: list of PrometheusAlertPolicyItem
        """
        self._Name = None
        self._Describe = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._RecordRules = None
        self._AlertDetailRules = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def RecordRules(self):
        return self._RecordRules

    @RecordRules.setter
    def RecordRules(self, RecordRules):
        self._RecordRules = RecordRules

    @property
    def AlertDetailRules(self):
        return self._AlertDetailRules

    @AlertDetailRules.setter
    def AlertDetailRules(self, AlertDetailRules):
        self._AlertDetailRules = AlertDetailRules


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Describe = params.get("Describe")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        if params.get("RecordRules") is not None:
            self._RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RecordRules.append(obj)
        if params.get("AlertDetailRules") is not None:
            self._AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self._AlertDetailRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemplateSyncTarget(AbstractModel):
    """云原生Prometheus模板同步目标

    """

    def __init__(self):
        r"""
        :param _Region: 目标所在地域
        :type Region: str
        :param _InstanceId: 目标实例
        :type InstanceId: str
        :param _ClusterId: 集群id，只有当采集模板的Level为cluster的时候需要
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _SyncTime: 最后一次同步时间， 用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncTime: str
        :param _Version: 当前使用的模板版本，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _ClusterType: 集群类型，只有当采集模板的Level为cluster的时候需要
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param _InstanceName: 用于出参，实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _ClusterName: 用于出参，集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        """
        self._Region = None
        self._InstanceId = None
        self._ClusterId = None
        self._SyncTime = None
        self._Version = None
        self._ClusterType = None
        self._InstanceName = None
        self._ClusterName = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SyncTime(self):
        return self._SyncTime

    @SyncTime.setter
    def SyncTime(self, SyncTime):
        self._SyncTime = SyncTime

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        self._SyncTime = params.get("SyncTime")
        self._Version = params.get("Version")
        self._ClusterType = params.get("ClusterType")
        self._InstanceName = params.get("InstanceName")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusZoneItem(AbstractModel):
    """PrometheusZoneItem 响应结构体内的地域信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _ZoneId: 可用区 ID
        :type ZoneId: int
        :param _ZoneState: 可用区状态( 0: 不可用；1: 可用)
        :type ZoneState: int
        :param _RegionId: 地域 ID
        :type RegionId: int
        :param _ZoneName: 可用区名（目前为中文）
        :type ZoneName: str
        :param _ZoneResourceState: 可用区资源状态(0:资源不足，不可使用；1:资源足够)
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneResourceState: int
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneState = None
        self._RegionId = None
        self._ZoneName = None
        self._ZoneResourceState = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneResourceState(self):
        return self._ZoneResourceState

    @ZoneResourceState.setter
    def ZoneResourceState(self, ZoneResourceState):
        self._ZoneResourceState = ZoneResourceState


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        self._RegionId = params.get("RegionId")
        self._ZoneName = params.get("ZoneName")
        self._ZoneResourceState = params.get("ZoneResourceState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiverInfo(AbstractModel):
    """接收人信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 告警时间段开始时间。范围[0,86400)，作为 UNIX 时间戳转成北京时间后去掉日期，例如7200表示"10:0:0"
        :type StartTime: int
        :param _EndTime: 告警时间段结束时间。含义同StartTime
        :type EndTime: int
        :param _NotifyWay: 告警通知方式。可选 "SMS","SITE","EMAIL","CALL","WECHAT"
        :type NotifyWay: list of str
        :param _ReceiverType: 接收人类型。“group” 或 “user”
        :type ReceiverType: str
        :param _Id: ReceiverId
        :type Id: int
        :param _SendFor: 电话告警通知时机。可选"OCCUR"(告警时通知),"RECOVER"(恢复时通知)
        :type SendFor: list of str
        :param _UidList: 电话告警接收者 UID
        :type UidList: list of int
        :param _RoundNumber: 电话告警轮数
        :type RoundNumber: int
        :param _PersonInterval: 电话告警对个人间隔（秒）
        :type PersonInterval: int
        :param _RoundInterval: 电话告警每轮间隔（秒）
        :type RoundInterval: int
        :param _RecoverNotify: 恢复通知方式。可选"SMS"
        :type RecoverNotify: list of str
        :param _NeedSendNotice: 是否需要电话告警触达提示。0不需要，1需要
        :type NeedSendNotice: int
        :param _ReceiverGroupList: 接收组列表。通过平台接口查询到的接收组 ID 列表
        :type ReceiverGroupList: list of int
        :param _ReceiverUserList: 接收人列表。通过平台接口查询到的接收人 ID 列表
        :type ReceiverUserList: list of int
        :param _ReceiveLanguage: 告警接收语言，枚举值（zh-CN，en-US）
        :type ReceiveLanguage: str
        """
        self._StartTime = None
        self._EndTime = None
        self._NotifyWay = None
        self._ReceiverType = None
        self._Id = None
        self._SendFor = None
        self._UidList = None
        self._RoundNumber = None
        self._PersonInterval = None
        self._RoundInterval = None
        self._RecoverNotify = None
        self._NeedSendNotice = None
        self._ReceiverGroupList = None
        self._ReceiverUserList = None
        self._ReceiveLanguage = None

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
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SendFor(self):
        return self._SendFor

    @SendFor.setter
    def SendFor(self, SendFor):
        self._SendFor = SendFor

    @property
    def UidList(self):
        return self._UidList

    @UidList.setter
    def UidList(self, UidList):
        self._UidList = UidList

    @property
    def RoundNumber(self):
        return self._RoundNumber

    @RoundNumber.setter
    def RoundNumber(self, RoundNumber):
        self._RoundNumber = RoundNumber

    @property
    def PersonInterval(self):
        return self._PersonInterval

    @PersonInterval.setter
    def PersonInterval(self, PersonInterval):
        self._PersonInterval = PersonInterval

    @property
    def RoundInterval(self):
        return self._RoundInterval

    @RoundInterval.setter
    def RoundInterval(self, RoundInterval):
        self._RoundInterval = RoundInterval

    @property
    def RecoverNotify(self):
        return self._RecoverNotify

    @RecoverNotify.setter
    def RecoverNotify(self, RecoverNotify):
        self._RecoverNotify = RecoverNotify

    @property
    def NeedSendNotice(self):
        return self._NeedSendNotice

    @NeedSendNotice.setter
    def NeedSendNotice(self, NeedSendNotice):
        self._NeedSendNotice = NeedSendNotice

    @property
    def ReceiverGroupList(self):
        return self._ReceiverGroupList

    @ReceiverGroupList.setter
    def ReceiverGroupList(self, ReceiverGroupList):
        self._ReceiverGroupList = ReceiverGroupList

    @property
    def ReceiverUserList(self):
        return self._ReceiverUserList

    @ReceiverUserList.setter
    def ReceiverUserList(self, ReceiverUserList):
        self._ReceiverUserList = ReceiverUserList

    @property
    def ReceiveLanguage(self):
        return self._ReceiveLanguage

    @ReceiveLanguage.setter
    def ReceiveLanguage(self, ReceiveLanguage):
        self._ReceiveLanguage = ReceiveLanguage


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NotifyWay = params.get("NotifyWay")
        self._ReceiverType = params.get("ReceiverType")
        self._Id = params.get("Id")
        self._SendFor = params.get("SendFor")
        self._UidList = params.get("UidList")
        self._RoundNumber = params.get("RoundNumber")
        self._PersonInterval = params.get("PersonInterval")
        self._RoundInterval = params.get("RoundInterval")
        self._RecoverNotify = params.get("RecoverNotify")
        self._NeedSendNotice = params.get("NeedSendNotice")
        self._ReceiverGroupList = params.get("ReceiverGroupList")
        self._ReceiverUserList = params.get("ReceiverUserList")
        self._ReceiveLanguage = params.get("ReceiveLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordingRuleSet(AbstractModel):
    """Prometheus 聚合规则响应结构体内信息

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _RuleState: 规则状态码
        :type RuleState: int
        :param _Name: 分组名称
        :type Name: str
        :param _Group: 规则内容组
        :type Group: str
        :param _Total: 规则数量
        :type Total: int
        :param _CreatedAt: 规则创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 规则最近更新时间
        :type UpdatedAt: str
        :param _RuleName: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        """
        self._RuleId = None
        self._RuleState = None
        self._Name = None
        self._Group = None
        self._Total = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._RuleName = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleState = params.get("RuleState")
        self._Name = params.get("Name")
        self._Group = params.get("Group")
        self._Total = params.get("Total")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeGrafanaInstanceRequest(AbstractModel):
    """ResumeGrafanaInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
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
        


class ResumeGrafanaInstanceResponse(AbstractModel):
    """ResumeGrafanaInstance返回参数结构体

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


class RunPrometheusInstanceRequest(AbstractModel):
    """RunPrometheusInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SubnetId: 子网ID，默认使用实例所用子网初始化，也可通过该参数传递新的子网ID初始化
        :type SubnetId: str
        """
        self._InstanceId = None
        self._SubnetId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunPrometheusInstanceResponse(AbstractModel):
    """RunPrometheusInstance返回参数结构体

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


class ServiceDiscoveryItem(AbstractModel):
    """Prometheus 服务发现信息

    """

    def __init__(self):
        r"""
        :param _Name: 服务发现名称
        :type Name: str
        :param _Namespace: 服务发现属于的 Namespace
        :type Namespace: str
        :param _Kind: 服务发现类型: ServiceMonitor/PodMonitor
        :type Kind: str
        :param _NamespaceSelector: Namespace 选取方式
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceSelector: str
        :param _Selector: Label 选取方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Selector: str
        :param _Endpoints: Endpoints 信息（PodMonitor 不含该参数）
        :type Endpoints: str
        :param _Yaml: 服务发现对应的配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        """
        self._Name = None
        self._Namespace = None
        self._Kind = None
        self._NamespaceSelector = None
        self._Selector = None
        self._Endpoints = None
        self._Yaml = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def NamespaceSelector(self):
        return self._NamespaceSelector

    @NamespaceSelector.setter
    def NamespaceSelector(self, NamespaceSelector):
        self._NamespaceSelector = NamespaceSelector

    @property
    def Selector(self):
        return self._Selector

    @Selector.setter
    def Selector(self, Selector):
        self._Selector = Selector

    @property
    def Endpoints(self):
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Kind = params.get("Kind")
        self._NamespaceSelector = params.get("NamespaceSelector")
        self._Selector = params.get("Selector")
        self._Endpoints = params.get("Endpoints")
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultAlarmPolicyRequest(AbstractModel):
    """SetDefaultAlarmPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定值 monitor
        :type Module: str
        :param _PolicyId: 告警策略 ID
        :type PolicyId: str
        """
        self._Module = None
        self._PolicyId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultAlarmPolicyResponse(AbstractModel):
    """SetDefaultAlarmPolicy返回参数结构体

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


class SyncPrometheusTempRequest(AbstractModel):
    """SyncPrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 实例id
        :type TemplateId: str
        :param _Targets: 同步目标
        :type Targets: list of PrometheusTemplateSyncTarget
        """
        self._TemplateId = None
        self._Targets = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPrometheusTempResponse(AbstractModel):
    """SyncPrometheusTemp返回参数结构体

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


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签key
        :type Key: str
        :param _Value: 标签value
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
        


class TagInstance(AbstractModel):
    """策略列表详情标签返回体

    """

    def __init__(self):
        r"""
        :param _Key: 标签Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 标签Value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _InstanceSum: 实例个数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSum: int
        :param _ServiceType: 产品类型，如：cvm
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _BindingStatus: 绑定状态，2：绑定成功，1：绑定中
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingStatus: int
        :param _TagStatus: 标签状态，2：标签存在，1：标签不存在
注意：此字段可能返回 null，表示取不到有效值。
        :type TagStatus: int
        """
        self._Key = None
        self._Value = None
        self._InstanceSum = None
        self._ServiceType = None
        self._RegionId = None
        self._BindingStatus = None
        self._TagStatus = None

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

    @property
    def InstanceSum(self):
        return self._InstanceSum

    @InstanceSum.setter
    def InstanceSum(self, InstanceSum):
        self._InstanceSum = InstanceSum

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def BindingStatus(self):
        return self._BindingStatus

    @BindingStatus.setter
    def BindingStatus(self, BindingStatus):
        self._BindingStatus = BindingStatus

    @property
    def TagStatus(self):
        return self._TagStatus

    @TagStatus.setter
    def TagStatus(self, TagStatus):
        self._TagStatus = TagStatus


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._InstanceSum = params.get("InstanceSum")
        self._ServiceType = params.get("ServiceType")
        self._RegionId = params.get("RegionId")
        self._BindingStatus = params.get("BindingStatus")
        self._TagStatus = params.get("TagStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Targets(AbstractModel):
    """抓取目标数

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Up: 在线数
注意：此字段可能返回 null，表示取不到有效值。
        :type Up: int
        :param _Down: 不在线数
注意：此字段可能返回 null，表示取不到有效值。
        :type Down: int
        :param _Unknown: 未知状态数
注意：此字段可能返回 null，表示取不到有效值。
        :type Unknown: int
        """
        self._Total = None
        self._Up = None
        self._Down = None
        self._Unknown = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Up(self):
        return self._Up

    @Up.setter
    def Up(self, Up):
        self._Up = Up

    @property
    def Down(self):
        return self._Down

    @Down.setter
    def Down(self, Down):
        self._Down = Down

    @property
    def Unknown(self):
        return self._Unknown

    @Unknown.setter
    def Unknown(self, Unknown):
        self._Unknown = Unknown


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Up = params.get("Up")
        self._Down = params.get("Down")
        self._Unknown = params.get("Unknown")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStepInfo(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        r"""
        :param _Step: 步骤名称
        :type Step: str
        :param _LifeState: 生命周期
pending : 步骤未开始
running: 步骤执行中
success: 步骤成功完成
failed: 步骤失败
        :type LifeState: str
        :param _StartAt: 步骤开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartAt: str
        :param _EndAt: 步骤结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndAt: str
        :param _FailedMsg: 若步骤生命周期为failed,则此字段显示错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMsg: str
        """
        self._Step = None
        self._LifeState = None
        self._StartAt = None
        self._EndAt = None
        self._FailedMsg = None

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

    @property
    def FailedMsg(self):
        return self._FailedMsg

    @FailedMsg.setter
    def FailedMsg(self, FailedMsg):
        self._FailedMsg = FailedMsg


    def _deserialize(self, params):
        self._Step = params.get("Step")
        self._LifeState = params.get("LifeState")
        self._StartAt = params.get("StartAt")
        self._EndAt = params.get("EndAt")
        self._FailedMsg = params.get("FailedMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroup(AbstractModel):
    """模板列表

    """

    def __init__(self):
        r"""
        :param _Conditions: 指标告警规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of Condition
        :param _EventConditions: 事件告警规则
注意：此字段可能返回 null，表示取不到有效值。
        :type EventConditions: list of EventCondition
        :param _PolicyGroups: 关联告警策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyGroups: list of PolicyGroup
        :param _GroupID: 模板策略组ID
        :type GroupID: int
        :param _GroupName: 模板策略组名称
        :type GroupName: str
        :param _InsertTime: 创建时间
        :type InsertTime: int
        :param _LastEditUin: 最后修改人UIN
        :type LastEditUin: int
        :param _Remark: 备注
        :type Remark: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: int
        :param _ViewName: 视图
        :type ViewName: str
        :param _IsUnionRule: 是否为与关系
        :type IsUnionRule: int
        """
        self._Conditions = None
        self._EventConditions = None
        self._PolicyGroups = None
        self._GroupID = None
        self._GroupName = None
        self._InsertTime = None
        self._LastEditUin = None
        self._Remark = None
        self._UpdateTime = None
        self._ViewName = None
        self._IsUnionRule = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def EventConditions(self):
        return self._EventConditions

    @EventConditions.setter
    def EventConditions(self, EventConditions):
        self._EventConditions = EventConditions

    @property
    def PolicyGroups(self):
        return self._PolicyGroups

    @PolicyGroups.setter
    def PolicyGroups(self, PolicyGroups):
        self._PolicyGroups = PolicyGroups

    @property
    def GroupID(self):
        return self._GroupID

    @GroupID.setter
    def GroupID(self, GroupID):
        self._GroupID = GroupID

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = Condition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self._EventConditions = []
            for item in params.get("EventConditions"):
                obj = EventCondition()
                obj._deserialize(item)
                self._EventConditions.append(obj)
        if params.get("PolicyGroups") is not None:
            self._PolicyGroups = []
            for item in params.get("PolicyGroups"):
                obj = PolicyGroup()
                obj._deserialize(item)
                self._PolicyGroups.append(obj)
        self._GroupID = params.get("GroupID")
        self._GroupName = params.get("GroupName")
        self._InsertTime = params.get("InsertTime")
        self._LastEditUin = params.get("LastEditUin")
        self._Remark = params.get("Remark")
        self._UpdateTime = params.get("UpdateTime")
        self._ViewName = params.get("ViewName")
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminatePrometheusInstancesRequest(AbstractModel):
    """TerminatePrometheusInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表
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
        


class TerminatePrometheusInstancesResponse(AbstractModel):
    """TerminatePrometheusInstances返回参数结构体

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


class Toleration(AbstractModel):
    """kubernetes Taint

    """

    def __init__(self):
        r"""
        :param _Key: 容忍应用到的 taint key
        :type Key: str
        :param _Operator: 键与值的关系
        :type Operator: str
        :param _Effect: 要匹配的污点效果
        :type Effect: str
        """
        self._Key = None
        self._Operator = None
        self._Effect = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Effect = params.get("Effect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class URLNotice(AbstractModel):
    """告警通知模板 - 回调通知详情

    """

    def __init__(self):
        r"""
        :param _URL: 回调 url（限长256字符）
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param _IsValid: 是否通过验证 0=否 1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsValid: int
        :param _ValidationCode: 验证码
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidationCode: str
        :param _StartTime: 通知开始时间 一天开始的秒数
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _EndTime: 通知结束时间 一天开始的秒数
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _Weekday: 通知周期 1-7表示周一到周日
注意：此字段可能返回 null，表示取不到有效值。
        :type Weekday: list of int
        """
        self._URL = None
        self._IsValid = None
        self._ValidationCode = None
        self._StartTime = None
        self._EndTime = None
        self._Weekday = None

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def IsValid(self):
        return self._IsValid

    @IsValid.setter
    def IsValid(self, IsValid):
        self._IsValid = IsValid

    @property
    def ValidationCode(self):
        return self._ValidationCode

    @ValidationCode.setter
    def ValidationCode(self, ValidationCode):
        self._ValidationCode = ValidationCode

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
    def Weekday(self):
        return self._Weekday

    @Weekday.setter
    def Weekday(self, Weekday):
        self._Weekday = Weekday


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._IsValid = params.get("IsValid")
        self._ValidationCode = params.get("ValidationCode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Weekday = params.get("Weekday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingAllPolicyObjectRequest(AbstractModel):
    """UnBindingAllPolicyObject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _GroupId: 策略组id，如传入 PolicyId 则该字段被忽略可传入任意值如 0
        :type GroupId: int
        :param _PolicyId: 告警策略ID，使用此字段时 GroupId 会被忽略
        :type PolicyId: str
        :param _EbSubject: 事件配置的告警
        :type EbSubject: str
        :param _EbEventFlag: 是否配置了事件告警
        :type EbEventFlag: int
        """
        self._Module = None
        self._GroupId = None
        self._PolicyId = None
        self._EbSubject = None
        self._EbEventFlag = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject

    @property
    def EbEventFlag(self):
        return self._EbEventFlag

    @EbEventFlag.setter
    def EbEventFlag(self, EbEventFlag):
        self._EbEventFlag = EbEventFlag


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._PolicyId = params.get("PolicyId")
        self._EbSubject = params.get("EbSubject")
        self._EbEventFlag = params.get("EbEventFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingAllPolicyObjectResponse(AbstractModel):
    """UnBindingAllPolicyObject返回参数结构体

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


class UnBindingPolicyObjectRequest(AbstractModel):
    """UnBindingPolicyObject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 固定值，为"monitor"
        :type Module: str
        :param _GroupId: 策略组id，如传入 PolicyId 则该字段被忽略可传入任意值如 0
        :type GroupId: int
        :param _UniqueId: 待删除对象实例的唯一id列表，UniqueId从调用[获取已绑定对象列表接口](https://cloud.tencent.com/document/api/248/40570)的出参的List中得到
        :type UniqueId: list of str
        :param _InstanceGroupId: 实例分组id，如果按实例分组删除的话UniqueId参数是无效的
        :type InstanceGroupId: int
        :param _PolicyId: 告警策略ID，使用此字段时 GroupId 会被忽略
        :type PolicyId: str
        :param _EbSubject: 事件配置的告警
        :type EbSubject: str
        :param _EbEventFlag: 是否配置了事件告警
        :type EbEventFlag: int
        """
        self._Module = None
        self._GroupId = None
        self._UniqueId = None
        self._InstanceGroupId = None
        self._PolicyId = None
        self._EbSubject = None
        self._EbEventFlag = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UniqueId(self):
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject

    @property
    def EbEventFlag(self):
        return self._EbEventFlag

    @EbEventFlag.setter
    def EbEventFlag(self, EbEventFlag):
        self._EbEventFlag = EbEventFlag


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._UniqueId = params.get("UniqueId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._PolicyId = params.get("PolicyId")
        self._EbSubject = params.get("EbSubject")
        self._EbEventFlag = params.get("EbEventFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingPolicyObjectResponse(AbstractModel):
    """UnBindingPolicyObject返回参数结构体

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


class UnbindPrometheusManagedGrafanaRequest(AbstractModel):
    """UnbindPrometheusManagedGrafana请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _GrafanaId: Grafana 实例 ID
        :type GrafanaId: str
        """
        self._InstanceId = None
        self._GrafanaId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GrafanaId(self):
        return self._GrafanaId

    @GrafanaId.setter
    def GrafanaId(self, GrafanaId):
        self._GrafanaId = GrafanaId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GrafanaId = params.get("GrafanaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindPrometheusManagedGrafanaResponse(AbstractModel):
    """UnbindPrometheusManagedGrafana返回参数结构体

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


class UninstallGrafanaDashboardRequest(AbstractModel):
    """UninstallGrafanaDashboard请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _IntegrationCodes: Prometheus 集成项 Code，删除对应的 Dashboard，Code 如下：
<li>spring_mvc</li>
<li>mysql</li>
<li>go</li>
<li>redis</li>
<li>jvm</li>
<li>pgsql</li>
<li>mongo</li>
<li>kafka</li>
<li>es</li>
<li>flink</li>
<li>blackbox</li>
<li>consule</li>
<li>memcached</li>
<li>zk</li>
<li>tps</li>
<li>istio</li>
<li>etcd</li>
        :type IntegrationCodes: list of str
        """
        self._InstanceId = None
        self._IntegrationCodes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IntegrationCodes(self):
        return self._IntegrationCodes

    @IntegrationCodes.setter
    def IntegrationCodes(self, IntegrationCodes):
        self._IntegrationCodes = IntegrationCodes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IntegrationCodes = params.get("IntegrationCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallGrafanaDashboardResponse(AbstractModel):
    """UninstallGrafanaDashboard返回参数结构体

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


class UninstallGrafanaPluginsRequest(AbstractModel):
    """UninstallGrafanaPlugins请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginIds: 插件 ID 数组，例如"PluginIds": [ "grafana-clock-panel" ]，可通过 DescribePluginOverviews 获取 PluginId
        :type PluginIds: list of str
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefg
        :type InstanceId: str
        """
        self._PluginIds = None
        self._InstanceId = None

    @property
    def PluginIds(self):
        return self._PluginIds

    @PluginIds.setter
    def PluginIds(self, PluginIds):
        self._PluginIds = PluginIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._PluginIds = params.get("PluginIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallGrafanaPluginsResponse(AbstractModel):
    """UninstallGrafanaPlugins返回参数结构体

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


class UpdateAlertRuleRequest(AbstractModel):
    """UpdateAlertRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: Prometheus 高警规则 ID
        :type RuleId: str
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _RuleState: 规则状态码，取值如下：
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
默认状态码为 2 启用。
        :type RuleState: int
        :param _RuleName: 告警规则名称
        :type RuleName: str
        :param _Expr: 告警规则表达式
        :type Expr: str
        :param _Duration: 告警规则持续时间
        :type Duration: str
        :param _Receivers: 告警规则接收组列表(当前规则绑定的接收组列表可通过 DescribeAlertRules 接口获取；用户已有的接收组列表可通过 DescribeAlarmNotices 接口获取)
        :type Receivers: list of str
        :param _Labels: 报警规则标签列表
        :type Labels: list of PrometheusRuleKV
        :param _Annotations: 报警规则注释列表。

告警对象和告警消息是 Prometheus Rule Annotations 的特殊字段，需要通过 annotations 来传递，对应的 Key 分别为summary/description。
        :type Annotations: list of PrometheusRuleKV
        :param _Type: 报警策略模板分类(自定义，可不填)
        :type Type: str
        """
        self._RuleId = None
        self._InstanceId = None
        self._RuleState = None
        self._RuleName = None
        self._Expr = None
        self._Duration = None
        self._Receivers = None
        self._Labels = None
        self._Annotations = None
        self._Type = None

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
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Expr(self):
        return self._Expr

    @Expr.setter
    def Expr(self, Expr):
        self._Expr = Expr

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._InstanceId = params.get("InstanceId")
        self._RuleState = params.get("RuleState")
        self._RuleName = params.get("RuleName")
        self._Expr = params.get("Expr")
        self._Duration = params.get("Duration")
        self._Receivers = params.get("Receivers")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertRuleResponse(AbstractModel):
    """UpdateAlertRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UpdateAlertRuleStateRequest(AbstractModel):
    """UpdateAlertRuleState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIds: 规则 ID 列表
        :type RuleIds: list of str
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _RuleState: 规则状态码，取值如下：
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
默认状态码为 2 启用。
        :type RuleState: int
        """
        self._RuleIds = None
        self._InstanceId = None
        self._RuleState = None

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        self._InstanceId = params.get("InstanceId")
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertRuleStateResponse(AbstractModel):
    """UpdateAlertRuleState返回参数结构体

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


class UpdateDNSConfigRequest(AbstractModel):
    """UpdateDNSConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
        :type InstanceId: str
        :param _NameServers: DNS 数组
        :type NameServers: list of str
        """
        self._InstanceId = None
        self._NameServers = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NameServers = params.get("NameServers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDNSConfigResponse(AbstractModel):
    """UpdateDNSConfig返回参数结构体

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


class UpdateExporterIntegrationRequest(AbstractModel):
    """UpdateExporterIntegration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _Kind: 类型(可通过 DescribeExporterIntegrations 获取对应集成的 Kind)
        :type Kind: str
        :param _Content: 配置内容(可通过 DescribeExporterIntegrations 接口获取对应集成的 Content，并在此基础上做修改)
        :type Content: str
        :param _KubeType: Kubernetes 集群类型，可不填。取值如下：
<li> 1= 容器集群(TKE) </li>
<li> 2=弹性集群(EKS) </li>
<li> 3= Prometheus管理的弹性集群(MEKS) </li>
        :type KubeType: int
        :param _ClusterId: 集群 ID，可不填
        :type ClusterId: str
        """
        self._InstanceId = None
        self._Kind = None
        self._Content = None
        self._KubeType = None
        self._ClusterId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        self._KubeType = params.get("KubeType")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateExporterIntegrationResponse(AbstractModel):
    """UpdateExporterIntegration返回参数结构体

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


class UpdateGrafanaConfigRequest(AbstractModel):
    """UpdateGrafanaConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Config: JSON 编码后的字符串，如 "{"server":{"root_url":"http://custom.domain"}}"
        :type Config: str
        """
        self._InstanceId = None
        self._Config = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaConfigResponse(AbstractModel):
    """UpdateGrafanaConfig返回参数结构体

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


class UpdateGrafanaEnvironmentsRequest(AbstractModel):
    """UpdateGrafanaEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
        :type InstanceId: str
        :param _Envs: JSON 序列化后的环境变量字符串，如 "{\"key1\":\"key2\"}"

        :type Envs: str
        """
        self._InstanceId = None
        self._Envs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Envs(self):
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Envs = params.get("Envs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaEnvironmentsResponse(AbstractModel):
    """UpdateGrafanaEnvironments返回参数结构体

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


class UpdateGrafanaIntegrationRequest(AbstractModel):
    """UpdateGrafanaIntegration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntegrationId: 集成 ID，可在实例详情-云产品集成-集成列表查看。例如：integration-abcd1234
        :type IntegrationId: str
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
        :type InstanceId: str
        :param _Kind: 集成类型，可在实例详情-云产品集成-集成列表查看。例如：tencent-cloud-prometheus
        :type Kind: str
        :param _Content: 集成内容，请查看示例
        :type Content: str
        """
        self._IntegrationId = None
        self._InstanceId = None
        self._Kind = None
        self._Content = None

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._IntegrationId = params.get("IntegrationId")
        self._InstanceId = params.get("InstanceId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaIntegrationResponse(AbstractModel):
    """UpdateGrafanaIntegration返回参数结构体

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


class UpdateGrafanaNotificationChannelRequest(AbstractModel):
    """UpdateGrafanaNotificationChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道 ID，例如：nchannel-abcd1234
        :type ChannelId: str
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
        :type InstanceId: str
        :param _Receivers: 接受告警通道 ID 数组
        :type Receivers: list of str
        :param _ChannelName: 告警通道名称，已废弃，名称不可修改。
        :type ChannelName: str
        :param _ExtraOrgIds: 已废弃，请使用 OrganizationIds
        :type ExtraOrgIds: list of str
        :param _OrganizationIds: 生效的组织 ID 数组
        :type OrganizationIds: list of str
        """
        self._ChannelId = None
        self._InstanceId = None
        self._Receivers = None
        self._ChannelName = None
        self._ExtraOrgIds = None
        self._OrganizationIds = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ExtraOrgIds(self):
        return self._ExtraOrgIds

    @ExtraOrgIds.setter
    def ExtraOrgIds(self, ExtraOrgIds):
        self._ExtraOrgIds = ExtraOrgIds

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._InstanceId = params.get("InstanceId")
        self._Receivers = params.get("Receivers")
        self._ChannelName = params.get("ChannelName")
        self._ExtraOrgIds = params.get("ExtraOrgIds")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaNotificationChannelResponse(AbstractModel):
    """UpdateGrafanaNotificationChannel返回参数结构体

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


class UpdateGrafanaWhiteListRequest(AbstractModel):
    """UpdateGrafanaWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _Whitelist: 白名单数组，输入白名单 IP 或 CIDR，如：127.0.0.1或127.0.0.1/24
如有多个 IP 可换行输入
        :type Whitelist: list of str
        """
        self._InstanceId = None
        self._Whitelist = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Whitelist(self):
        return self._Whitelist

    @Whitelist.setter
    def Whitelist(self, Whitelist):
        self._Whitelist = Whitelist


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaWhiteListResponse(AbstractModel):
    """UpdateGrafanaWhiteList返回参数结构体

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


class UpdatePrometheusAgentStatusRequest(AbstractModel):
    """UpdatePrometheusAgentStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _AgentIds: Agent ID 列表，例如：agent-abcd1234，可在控制台 Agent 管理中获取
        :type AgentIds: list of str
        :param _Status: 要更新的状态
<li> 1= 开启 </li>
<li> 2= 关闭 </li>
        :type Status: int
        """
        self._InstanceId = None
        self._AgentIds = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentIds(self):
        return self._AgentIds

    @AgentIds.setter
    def AgentIds(self, AgentIds):
        self._AgentIds = AgentIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentIds = params.get("AgentIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrometheusAgentStatusResponse(AbstractModel):
    """UpdatePrometheusAgentStatus返回参数结构体

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


class UpdatePrometheusAlertGroupRequest(AbstractModel):
    """UpdatePrometheusAlertGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: prometheus实例ID
        :type InstanceId: str
        :param _GroupId: 告警分组ID，形如alert-xxxx
        :type GroupId: str
        :param _GroupName: 告警分组名称，不能与其他告警分组重名
        :type GroupName: str
        :param _GroupState: 告警分组状态：
2 -- 启用
3 -- 禁用
不为空时会覆盖 `Rules`字段下所有告警规则状态
        :type GroupState: int
        :param _AMPReceivers: 云监控告警通知模板ID列表，形如Consumer-xxxx或notice-xxxx
        :type AMPReceivers: list of str
        :param _CustomReceiver: 自定义告警通知模板
        :type CustomReceiver: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertCustomReceiver`
        :param _RepeatInterval: 告警通知周期（收敛时间），为空默认1h
        :type RepeatInterval: str
        :param _Rules: 要创建的告警规则列表
        :type Rules: list of PrometheusAlertGroupRuleSet
        """
        self._InstanceId = None
        self._GroupId = None
        self._GroupName = None
        self._GroupState = None
        self._AMPReceivers = None
        self._CustomReceiver = None
        self._RepeatInterval = None
        self._Rules = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupState(self):
        return self._GroupState

    @GroupState.setter
    def GroupState(self, GroupState):
        self._GroupState = GroupState

    @property
    def AMPReceivers(self):
        return self._AMPReceivers

    @AMPReceivers.setter
    def AMPReceivers(self, AMPReceivers):
        self._AMPReceivers = AMPReceivers

    @property
    def CustomReceiver(self):
        return self._CustomReceiver

    @CustomReceiver.setter
    def CustomReceiver(self, CustomReceiver):
        self._CustomReceiver = CustomReceiver

    @property
    def RepeatInterval(self):
        return self._RepeatInterval

    @RepeatInterval.setter
    def RepeatInterval(self, RepeatInterval):
        self._RepeatInterval = RepeatInterval

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupState = params.get("GroupState")
        self._AMPReceivers = params.get("AMPReceivers")
        if params.get("CustomReceiver") is not None:
            self._CustomReceiver = PrometheusAlertCustomReceiver()
            self._CustomReceiver._deserialize(params.get("CustomReceiver"))
        self._RepeatInterval = params.get("RepeatInterval")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertGroupRuleSet()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrometheusAlertGroupResponse(AbstractModel):
    """UpdatePrometheusAlertGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 更新的告警分组ID，满足正则表达式`alert-[a-z0-9]{8}`
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class UpdatePrometheusAlertGroupStateRequest(AbstractModel):
    """UpdatePrometheusAlertGroupState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _GroupIds: 告警分组ID列表，形如alert-xxxx
        :type GroupIds: list of str
        :param _GroupState: 告警分组状态
2 -- 启用
3 -- 禁用
        :type GroupState: int
        """
        self._InstanceId = None
        self._GroupIds = None
        self._GroupState = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def GroupState(self):
        return self._GroupState

    @GroupState.setter
    def GroupState(self, GroupState):
        self._GroupState = GroupState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupIds = params.get("GroupIds")
        self._GroupState = params.get("GroupState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrometheusAlertGroupStateResponse(AbstractModel):
    """UpdatePrometheusAlertGroupState返回参数结构体

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


class UpdatePrometheusScrapeJobRequest(AbstractModel):
    """UpdatePrometheusScrapeJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID(可通过 DescribePrometheusInstances 接口获取)
        :type InstanceId: str
        :param _AgentId: Agent ID(可通过DescribePrometheusAgents 接口获取)
        :type AgentId: str
        :param _JobId: 抓取任务 ID(可通过 DescribePrometheusScrapeJobs 接口获取)
        :type JobId: str
        :param _Config: 抓取任务配置
        :type Config: str
        """
        self._InstanceId = None
        self._AgentId = None
        self._JobId = None
        self._Config = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        self._JobId = params.get("JobId")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrometheusScrapeJobResponse(AbstractModel):
    """UpdatePrometheusScrapeJob返回参数结构体

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


class UpdateRecordingRuleRequest(AbstractModel):
    """UpdateRecordingRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 聚合规则名称
        :type Name: str
        :param _Group: 聚合规则组内容，格式为 yaml，通过 base64 进行编码。
        :type Group: str
        :param _InstanceId: Prometheus 实例 ID(可通过 DescribePrometheusInstances 接口获取)
        :type InstanceId: str
        :param _RuleId: Prometheus 聚合规则 ID(可通过 DescribeRecordingRules 接口获取)
        :type RuleId: str
        :param _RuleState: 规则状态码，取值如下：
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
默认状态码为 2 启用。
        :type RuleState: int
        """
        self._Name = None
        self._Group = None
        self._InstanceId = None
        self._RuleId = None
        self._RuleState = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Group = params.get("Group")
        self._InstanceId = params.get("InstanceId")
        self._RuleId = params.get("RuleId")
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordingRuleResponse(AbstractModel):
    """UpdateRecordingRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UpdateSSOAccountRequest(AbstractModel):
    """UpdateSSOAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-abcdefgh
        :type InstanceId: str
        :param _UserId: 用户账号 ID ，例如：10000000
        :type UserId: str
        :param _Role: 权限
        :type Role: list of GrafanaAccountRole
        :param _Notes: 备注
        :type Notes: str
        """
        self._InstanceId = None
        self._UserId = None
        self._Role = None
        self._Notes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        if params.get("Role") is not None:
            self._Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self._Role.append(obj)
        self._Notes = params.get("Notes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSSOAccountResponse(AbstractModel):
    """UpdateSSOAccount返回参数结构体

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


class UpdateServiceDiscoveryRequest(AbstractModel):
    """UpdateServiceDiscovery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param _KubeClusterId: <li>类型是 TKE，为对应的腾讯云容器服务集群 ID</li>
        :type KubeClusterId: str
        :param _KubeType: 用户 Kubernetes 集群类型：
<li> 1 = 容器服务集群(TKE) </li>
        :type KubeType: int
        :param _Type: 服务发现类型，取值如下：
<li> 1 = ServiceMonitor</li>
<li> 2 = PodMonitor</li>
<li> 3 = JobMonitor</li>
        :type Type: int
        :param _Yaml: 服务发现配置信息，YAML 格式，[具体YAML参数内容请参考](https://cloud.tencent.com/document/product/1416/55995#service-monitor)
        :type Yaml: str
        """
        self._InstanceId = None
        self._KubeClusterId = None
        self._KubeType = None
        self._Type = None
        self._Yaml = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeClusterId(self):
        return self._KubeClusterId

    @KubeClusterId.setter
    def KubeClusterId(self, KubeClusterId):
        self._KubeClusterId = KubeClusterId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeClusterId = params.get("KubeClusterId")
        self._KubeType = params.get("KubeType")
        self._Type = params.get("Type")
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServiceDiscoveryResponse(AbstractModel):
    """UpdateServiceDiscovery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceDiscovery: 更新成功之后，返回对应服务发现的信息
        :type ServiceDiscovery: :class:`tencentcloud.monitor.v20180724.models.ServiceDiscoveryItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceDiscovery = None
        self._RequestId = None

    @property
    def ServiceDiscovery(self):
        return self._ServiceDiscovery

    @ServiceDiscovery.setter
    def ServiceDiscovery(self, ServiceDiscovery):
        self._ServiceDiscovery = ServiceDiscovery

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceDiscovery") is not None:
            self._ServiceDiscovery = ServiceDiscoveryItem()
            self._ServiceDiscovery._deserialize(params.get("ServiceDiscovery"))
        self._RequestId = params.get("RequestId")


class UpgradeGrafanaDashboardRequest(AbstractModel):
    """UpgradeGrafanaDashboard请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _IntegrationCodes: Prometheus 集成项 Code，升级对应的 Dashboard，取值如下：<li>qcloud</li><li>cvm_process_exporter</li><li>cvm_node_exporter</li><li>cvm</li><li>tps</li><li>nginx-ingress</li><li>nvidia-gpu</li><li>cdwch</li><li>emr</li><li>apache</li><li>rocketmq</li><li>rabbitmq</li><li>spring_mvc</li><li>mysql</li><li>mssql</li><li>go</li><li>redis</li><li>jvm</li><li>pgsql</li><li>ceph</li><li>docker</li><li>nginx</li><li>oracledb</li><li>mongo</li><li>kafka</li><li>es</li><li>flink</li><li>blackbox</li><li>consule</li><li>memcached</li><li>zk</li><li>tps</li><li>istio</li><li>etcd</li><li>pts</li><li>kong</li>
        :type IntegrationCodes: list of str
        """
        self._InstanceId = None
        self._IntegrationCodes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IntegrationCodes(self):
        return self._IntegrationCodes

    @IntegrationCodes.setter
    def IntegrationCodes(self, IntegrationCodes):
        self._IntegrationCodes = IntegrationCodes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IntegrationCodes = params.get("IntegrationCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeGrafanaDashboardResponse(AbstractModel):
    """UpgradeGrafanaDashboard返回参数结构体

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


class UpgradeGrafanaInstanceRequest(AbstractModel):
    """UpgradeGrafanaInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Grafana 实例 ID，例如：grafana-12345678
        :type InstanceId: str
        :param _Alias: 版本别名，目前固定为 v9.1.5
        :type Alias: str
        """
        self._InstanceId = None
        self._Alias = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeGrafanaInstanceResponse(AbstractModel):
    """UpgradeGrafanaInstance返回参数结构体

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


class UserNotice(AbstractModel):
    """告警通知模板 - 用户通知详情

    """

    def __init__(self):
        r"""
        :param _ReceiverType: 接收者类型 USER=用户 GROUP=用户组
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverType: str
        :param _StartTime: 通知开始时间 00:00:00 开始的秒数（取值范围0-86399）
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _EndTime: 通知结束时间 00:00:00 开始的秒数（取值范围0-86399）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _NoticeWay: 通知渠道列表 EMAIL=邮件 SMS=短信 CALL=电话 WECHAT=微信 RTX=企业微信
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeWay: list of str
        :param _UserIds: 用户 uid 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIds: list of int
        :param _GroupIds: 用户组 group id 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupIds: list of int
        :param _PhoneOrder: 电话轮询列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneOrder: list of int
        :param _PhoneCircleTimes: 电话轮询次数 （取值范围1-5）
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCircleTimes: int
        :param _PhoneInnerInterval: 单次轮询内拨打间隔 秒数 （取值范围60-900）
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneInnerInterval: int
        :param _PhoneCircleInterval: 两次轮询间隔 秒数（取值范围60-900）
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCircleInterval: int
        :param _NeedPhoneArriveNotice: 是否需要触达通知 0=否 1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type NeedPhoneArriveNotice: int
        :param _PhoneCallType: 电话拨打类型 SYNC=同时拨打 CIRCLE=轮询拨打 不指定时默认是轮询
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCallType: str
        :param _Weekday: 通知周期 1-7表示周一到周日
注意：此字段可能返回 null，表示取不到有效值。
        :type Weekday: list of int
        :param _OnCallFormIDs: 值班表id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OnCallFormIDs: list of str
        :param _VoiceConfirmKey: 电话按键确认
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceConfirmKey: str
        """
        self._ReceiverType = None
        self._StartTime = None
        self._EndTime = None
        self._NoticeWay = None
        self._UserIds = None
        self._GroupIds = None
        self._PhoneOrder = None
        self._PhoneCircleTimes = None
        self._PhoneInnerInterval = None
        self._PhoneCircleInterval = None
        self._NeedPhoneArriveNotice = None
        self._PhoneCallType = None
        self._Weekday = None
        self._OnCallFormIDs = None
        self._VoiceConfirmKey = None

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

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
    def NoticeWay(self):
        return self._NoticeWay

    @NoticeWay.setter
    def NoticeWay(self, NoticeWay):
        self._NoticeWay = NoticeWay

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def PhoneOrder(self):
        return self._PhoneOrder

    @PhoneOrder.setter
    def PhoneOrder(self, PhoneOrder):
        self._PhoneOrder = PhoneOrder

    @property
    def PhoneCircleTimes(self):
        return self._PhoneCircleTimes

    @PhoneCircleTimes.setter
    def PhoneCircleTimes(self, PhoneCircleTimes):
        self._PhoneCircleTimes = PhoneCircleTimes

    @property
    def PhoneInnerInterval(self):
        return self._PhoneInnerInterval

    @PhoneInnerInterval.setter
    def PhoneInnerInterval(self, PhoneInnerInterval):
        self._PhoneInnerInterval = PhoneInnerInterval

    @property
    def PhoneCircleInterval(self):
        return self._PhoneCircleInterval

    @PhoneCircleInterval.setter
    def PhoneCircleInterval(self, PhoneCircleInterval):
        self._PhoneCircleInterval = PhoneCircleInterval

    @property
    def NeedPhoneArriveNotice(self):
        return self._NeedPhoneArriveNotice

    @NeedPhoneArriveNotice.setter
    def NeedPhoneArriveNotice(self, NeedPhoneArriveNotice):
        self._NeedPhoneArriveNotice = NeedPhoneArriveNotice

    @property
    def PhoneCallType(self):
        return self._PhoneCallType

    @PhoneCallType.setter
    def PhoneCallType(self, PhoneCallType):
        self._PhoneCallType = PhoneCallType

    @property
    def Weekday(self):
        return self._Weekday

    @Weekday.setter
    def Weekday(self, Weekday):
        self._Weekday = Weekday

    @property
    def OnCallFormIDs(self):
        return self._OnCallFormIDs

    @OnCallFormIDs.setter
    def OnCallFormIDs(self, OnCallFormIDs):
        self._OnCallFormIDs = OnCallFormIDs

    @property
    def VoiceConfirmKey(self):
        return self._VoiceConfirmKey

    @VoiceConfirmKey.setter
    def VoiceConfirmKey(self, VoiceConfirmKey):
        self._VoiceConfirmKey = VoiceConfirmKey


    def _deserialize(self, params):
        self._ReceiverType = params.get("ReceiverType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NoticeWay = params.get("NoticeWay")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._PhoneOrder = params.get("PhoneOrder")
        self._PhoneCircleTimes = params.get("PhoneCircleTimes")
        self._PhoneInnerInterval = params.get("PhoneInnerInterval")
        self._PhoneCircleInterval = params.get("PhoneCircleInterval")
        self._NeedPhoneArriveNotice = params.get("NeedPhoneArriveNotice")
        self._PhoneCallType = params.get("PhoneCallType")
        self._Weekday = params.get("Weekday")
        self._OnCallFormIDs = params.get("OnCallFormIDs")
        self._VoiceConfirmKey = params.get("VoiceConfirmKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        