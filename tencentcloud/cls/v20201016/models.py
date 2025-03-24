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


class AddMachineGroupInfoRequest(AbstractModel):
    """AddMachineGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _MachineGroupType: 机器组类型
目前type支持 ip 和 label
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        self._GroupId = None
        self._MachineGroupType = None

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MachineGroupType(self):
        """机器组类型
目前type支持 ip 和 label
        :rtype: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMachineGroupInfoResponse(AbstractModel):
    """AddMachineGroupInfo返回参数结构体

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


class AdvanceFilterRuleInfo(AbstractModel):
    """高级过滤规则

    """

    def __init__(self):
        r"""
        :param _Key: 过滤字段
        :type Key: str
        :param _Rule: 过滤规则，0:等于，1:字段存在，2:字段不存在
        :type Rule: int
        :param _Value: 过滤值
        :type Value: str
        """
        self._Key = None
        self._Rule = None
        self._Value = None

    @property
    def Key(self):
        """过滤字段
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Rule(self):
        """过滤规则，0:等于，1:字段存在，2:字段不存在
        :rtype: int
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Value(self):
        """过滤值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Rule = params.get("Rule")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmAnalysisConfig(AbstractModel):
    """告警多维分析一些配置信息

    """

    def __init__(self):
        r"""
        :param _Key: 键。支持以下key：
SyntaxRule：语法规则，value支持 0：Lucene语法；1： CQL语法。
QueryIndex：执行语句序号。value支持  -1：自定义； 1：执行语句1； 2：执行语句2。
CustomQuery：检索语句。 QueryIndex为-1时有效且必填，value示例： "* | select count(*) as count"。
Fields：字段。value支持 __SOURCE__；__FILENAME__；__HOSTNAME__；__TIMESTAMP__；__INDEX_STATUS__；__PKG_LOGID__；__TOPIC__。
Format：显示形式。value支持 1：每条日志一行；2：每条日志每个字段一行。
Limit：最大日志条数。 value示例： 5。
        :type Key: str
        :param _Value: 值。
键对应值如下：
SyntaxRule：语法规则，value支持 0：Lucene语法；1： CQL语法。
QueryIndex：执行语句序号。value支持  -1：自定义； 1：执行语句1； 2：执行语句2。
CustomQuery：检索语句。 QueryIndex为-1时有效且必填，value示例： "* | select count(*) as count"。
Fields：字段。value支持 __SOURCE__；__FILENAME__；__HOSTNAME__；__TIMESTAMP__；__INDEX_STATUS__；__PKG_LOGID__；__TOPIC__。
Format：显示形式。value支持 1：每条日志一行；2：每条日志每个字段一行。
Limit：最大日志条数。 value示例： 5。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """键。支持以下key：
SyntaxRule：语法规则，value支持 0：Lucene语法；1： CQL语法。
QueryIndex：执行语句序号。value支持  -1：自定义； 1：执行语句1； 2：执行语句2。
CustomQuery：检索语句。 QueryIndex为-1时有效且必填，value示例： "* | select count(*) as count"。
Fields：字段。value支持 __SOURCE__；__FILENAME__；__HOSTNAME__；__TIMESTAMP__；__INDEX_STATUS__；__PKG_LOGID__；__TOPIC__。
Format：显示形式。value支持 1：每条日志一行；2：每条日志每个字段一行。
Limit：最大日志条数。 value示例： 5。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """值。
键对应值如下：
SyntaxRule：语法规则，value支持 0：Lucene语法；1： CQL语法。
QueryIndex：执行语句序号。value支持  -1：自定义； 1：执行语句1； 2：执行语句2。
CustomQuery：检索语句。 QueryIndex为-1时有效且必填，value示例： "* | select count(*) as count"。
Fields：字段。value支持 __SOURCE__；__FILENAME__；__HOSTNAME__；__TIMESTAMP__；__INDEX_STATUS__；__PKG_LOGID__；__TOPIC__。
Format：显示形式。value支持 1：每条日志一行；2：每条日志每个字段一行。
Limit：最大日志条数。 value示例： 5。
        :rtype: str
        """
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
        


class AlarmClassification(AbstractModel):
    """告警分类信息

    """

    def __init__(self):
        r"""
        :param _Key: 分类键
        :type Key: str
        :param _Value: 分类值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """分类键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """分类值
        :rtype: str
        """
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
        


class AlarmInfo(AbstractModel):
    """告警策略描述

    """

    def __init__(self):
        r"""
        :param _Name: 告警策略名称。
        :type Name: str
        :param _AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTargetInfo
        :param _MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _Condition: 单触发条件。与MultiConditions参数互斥。
        :type Condition: str
        :param _TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为10。
        :type TriggerCount: int
        :param _AlarmPeriod: 告警重复的周期。单位是min。取值范围是0~1440。
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param _Status: 开启状态。
        :type Status: bool
        :param _AlarmId: 告警策略ID。
        :type AlarmId: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 最近更新时间。
        :type UpdateTime: str
        :param _MessageTemplate: 自定义通知模板
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageTemplate: str
        :param _CallBack: 自定义回调模板
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: 多维分析设置
        :type Analysis: list of AnalysisDimensional
        :param _GroupTriggerStatus: 分组触发状态。true：开启，false：关闭（默认）
        :type GroupTriggerStatus: bool
        :param _GroupTriggerCondition: 分组触发条件。
        :type GroupTriggerCondition: list of str
        :param _MonitorObjectType: 监控对象类型。0:执行语句共用监控对象;1:每个执行语句单独选择监控对象。 
        :type MonitorObjectType: int
        :param _AlarmLevel: 告警级别。0:警告(Warn);1:提醒(Info);2:紧急 (Critical)。
        :type AlarmLevel: int
        :param _Classifications: 告警附加分类字段。
        :type Classifications: list of AlarmClassification
        :param _MultiConditions: 多触发条件。与
Condition互斥。
        :type MultiConditions: list of MultiCondition
        """
        self._Name = None
        self._AlarmTargets = None
        self._MonitorTime = None
        self._Condition = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._Status = None
        self._AlarmId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None
        self._GroupTriggerStatus = None
        self._GroupTriggerCondition = None
        self._MonitorObjectType = None
        self._AlarmLevel = None
        self._Classifications = None
        self._MultiConditions = None

    @property
    def Name(self):
        """告警策略名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmTargets(self):
        """监控对象列表。
        :rtype: list of AlarmTargetInfo
        """
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def MonitorTime(self):
        """监控任务运行时间点。
        :rtype: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        """
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def Condition(self):
        """单触发条件。与MultiConditions参数互斥。
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def TriggerCount(self):
        """持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为10。
        :rtype: int
        """
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        """告警重复的周期。单位是min。取值范围是0~1440。
        :rtype: int
        """
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        """关联的告警通知模板列表。
        :rtype: list of str
        """
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def Status(self):
        """开启状态。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmId(self):
        """告警策略ID。
        :rtype: str
        """
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最近更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MessageTemplate(self):
        """自定义通知模板
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        """自定义回调模板
        :rtype: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        """
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        """多维分析设置
        :rtype: list of AnalysisDimensional
        """
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def GroupTriggerStatus(self):
        """分组触发状态。true：开启，false：关闭（默认）
        :rtype: bool
        """
        return self._GroupTriggerStatus

    @GroupTriggerStatus.setter
    def GroupTriggerStatus(self, GroupTriggerStatus):
        self._GroupTriggerStatus = GroupTriggerStatus

    @property
    def GroupTriggerCondition(self):
        """分组触发条件。
        :rtype: list of str
        """
        return self._GroupTriggerCondition

    @GroupTriggerCondition.setter
    def GroupTriggerCondition(self, GroupTriggerCondition):
        self._GroupTriggerCondition = GroupTriggerCondition

    @property
    def MonitorObjectType(self):
        """监控对象类型。0:执行语句共用监控对象;1:每个执行语句单独选择监控对象。 
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def AlarmLevel(self):
        """告警级别。0:警告(Warn);1:提醒(Info);2:紧急 (Critical)。
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def Classifications(self):
        """告警附加分类字段。
        :rtype: list of AlarmClassification
        """
        return self._Classifications

    @Classifications.setter
    def Classifications(self, Classifications):
        self._Classifications = Classifications

    @property
    def MultiConditions(self):
        """多触发条件。与
Condition互斥。
        :rtype: list of MultiCondition
        """
        return self._MultiConditions

    @MultiConditions.setter
    def MultiConditions(self, MultiConditions):
        self._MultiConditions = MultiConditions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTargetInfo()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._Condition = params.get("Condition")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        self._Status = params.get("Status")
        self._AlarmId = params.get("AlarmId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        self._GroupTriggerStatus = params.get("GroupTriggerStatus")
        self._GroupTriggerCondition = params.get("GroupTriggerCondition")
        self._MonitorObjectType = params.get("MonitorObjectType")
        self._AlarmLevel = params.get("AlarmLevel")
        if params.get("Classifications") is not None:
            self._Classifications = []
            for item in params.get("Classifications"):
                obj = AlarmClassification()
                obj._deserialize(item)
                self._Classifications.append(obj)
        if params.get("MultiConditions") is not None:
            self._MultiConditions = []
            for item in params.get("MultiConditions"):
                obj = MultiCondition()
                obj._deserialize(item)
                self._MultiConditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotice(AbstractModel):
    """告警通知渠道组详细配置

    """

    def __init__(self):
        r"""
        :param _Name: 告警通知渠道组名称。
        :type Name: str
        :param _Tags: 告警通知渠道组绑定的标签信息。
        :type Tags: list of Tag
        :param _Type: 告警模板的类型。可选值：
<br><li> Trigger - 告警触发</li>
<br><li> Recovery - 告警恢复</li>
<br><li> All - 告警触发和告警恢复</li>
        :type Type: str
        :param _NoticeReceivers: 告警通知模板接收者信息。
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: 告警通知模板回调信息。
        :type WebCallbacks: list of WebCallback
        :param _AlarmNoticeId: 告警通知模板ID。
        :type AlarmNoticeId: str
        :param _NoticeRules: 通知规则。
        :type NoticeRules: list of NoticeRule
        :param _AlarmShieldStatus: 免登录操作告警开关。
参数值： 1：关闭 2：开启（默认开启）
        :type AlarmShieldStatus: int
        :param _JumpDomain: 调用链接域名。http:// 或者 https:// 开头，不能/结尾
        :type JumpDomain: str
        :param _AlarmNoticeDeliverConfig: 投递相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmNoticeDeliverConfig: :class:`tencentcloud.cls.v20201016.models.AlarmNoticeDeliverConfig`
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 最近更新时间。
        :type UpdateTime: str
        """
        self._Name = None
        self._Tags = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None
        self._AlarmNoticeId = None
        self._NoticeRules = None
        self._AlarmShieldStatus = None
        self._JumpDomain = None
        self._AlarmNoticeDeliverConfig = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Name(self):
        """告警通知渠道组名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        """告警通知渠道组绑定的标签信息。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Type(self):
        """告警模板的类型。可选值：
<br><li> Trigger - 告警触发</li>
<br><li> Recovery - 告警恢复</li>
<br><li> All - 告警触发和告警恢复</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeReceivers(self):
        """告警通知模板接收者信息。
        :rtype: list of NoticeReceiver
        """
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        """告警通知模板回调信息。
        :rtype: list of WebCallback
        """
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks

    @property
    def AlarmNoticeId(self):
        """告警通知模板ID。
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def NoticeRules(self):
        """通知规则。
        :rtype: list of NoticeRule
        """
        return self._NoticeRules

    @NoticeRules.setter
    def NoticeRules(self, NoticeRules):
        self._NoticeRules = NoticeRules

    @property
    def AlarmShieldStatus(self):
        """免登录操作告警开关。
参数值： 1：关闭 2：开启（默认开启）
        :rtype: int
        """
        return self._AlarmShieldStatus

    @AlarmShieldStatus.setter
    def AlarmShieldStatus(self, AlarmShieldStatus):
        self._AlarmShieldStatus = AlarmShieldStatus

    @property
    def JumpDomain(self):
        """调用链接域名。http:// 或者 https:// 开头，不能/结尾
        :rtype: str
        """
        return self._JumpDomain

    @JumpDomain.setter
    def JumpDomain(self, JumpDomain):
        self._JumpDomain = JumpDomain

    @property
    def AlarmNoticeDeliverConfig(self):
        """投递相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.AlarmNoticeDeliverConfig`
        """
        return self._AlarmNoticeDeliverConfig

    @AlarmNoticeDeliverConfig.setter
    def AlarmNoticeDeliverConfig(self, AlarmNoticeDeliverConfig):
        self._AlarmNoticeDeliverConfig = AlarmNoticeDeliverConfig

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最近更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        if params.get("NoticeRules") is not None:
            self._NoticeRules = []
            for item in params.get("NoticeRules"):
                obj = NoticeRule()
                obj._deserialize(item)
                self._NoticeRules.append(obj)
        self._AlarmShieldStatus = params.get("AlarmShieldStatus")
        self._JumpDomain = params.get("JumpDomain")
        if params.get("AlarmNoticeDeliverConfig") is not None:
            self._AlarmNoticeDeliverConfig = AlarmNoticeDeliverConfig()
            self._AlarmNoticeDeliverConfig._deserialize(params.get("AlarmNoticeDeliverConfig"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNoticeDeliverConfig(AbstractModel):
    """通知渠道投递日志配置信息

    """

    def __init__(self):
        r"""
        :param _DeliverConfig: 通知渠道投递日志配置信息。
        :type DeliverConfig: :class:`tencentcloud.cls.v20201016.models.DeliverConfig`
        :param _ErrMsg: 投递失败原因。
        :type ErrMsg: str
        """
        self._DeliverConfig = None
        self._ErrMsg = None

    @property
    def DeliverConfig(self):
        """通知渠道投递日志配置信息。
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeliverConfig`
        """
        return self._DeliverConfig

    @DeliverConfig.setter
    def DeliverConfig(self, DeliverConfig):
        self._DeliverConfig = DeliverConfig

    @property
    def ErrMsg(self):
        """投递失败原因。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        if params.get("DeliverConfig") is not None:
            self._DeliverConfig = DeliverConfig()
            self._DeliverConfig._deserialize(params.get("DeliverConfig"))
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmShieldInfo(AbstractModel):
    """告警屏蔽任务配置

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: 通知渠道组Id
        :type AlarmNoticeId: str
        :param _TaskId: 屏蔽规则id
        :type TaskId: str
        :param _StartTime: 屏蔽开始时间（秒级时间戳）。
        :type StartTime: int
        :param _EndTime: 屏蔽结束时间（秒级时间戳）。
        :type EndTime: int
        :param _Type: 屏蔽类型。1：屏蔽所有通知，2：按照Rule参数屏蔽匹配规则的通知。
        :type Type: int
        :param _Rule: 屏蔽规则，当Type为2时必填。规则填写方式详见[产品文档](https://cloud.tencent.com/document/product/614/103178#rule)。
        :type Rule: str
        :param _Reason: 屏蔽原因。
        :type Reason: str
        :param _Source: 规则创建来源。
1. 控制台，2.api，3.告警通知
        :type Source: int
        :param _Operator: 操作者。
        :type Operator: str
        :param _Status: 规则状态。
0：暂未生效，1：生效中，2：已失效
        :type Status: int
        :param _CreateTime: 规则创建时间。
        :type CreateTime: int
        :param _UpdateTime: 规则更新时间。
        :type UpdateTime: int
        """
        self._AlarmNoticeId = None
        self._TaskId = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Rule = None
        self._Reason = None
        self._Source = None
        self._Operator = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def AlarmNoticeId(self):
        """通知渠道组Id
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def TaskId(self):
        """屏蔽规则id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def StartTime(self):
        """屏蔽开始时间（秒级时间戳）。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """屏蔽结束时间（秒级时间戳）。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        """屏蔽类型。1：屏蔽所有通知，2：按照Rule参数屏蔽匹配规则的通知。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Rule(self):
        """屏蔽规则，当Type为2时必填。规则填写方式详见[产品文档](https://cloud.tencent.com/document/product/614/103178#rule)。
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Reason(self):
        """屏蔽原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Source(self):
        """规则创建来源。
1. 控制台，2.api，3.告警通知
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Operator(self):
        """操作者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Status(self):
        """规则状态。
0：暂未生效，1：生效中，2：已失效
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """规则创建时间。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """规则更新时间。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._TaskId = params.get("TaskId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Rule = params.get("Rule")
        self._Reason = params.get("Reason")
        self._Source = params.get("Source")
        self._Operator = params.get("Operator")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTarget(AbstractModel):
    """告警对象

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID。
        :type TopicId: str
        :param _Query: 查询语句。
        :type Query: str
        :param _Number: 告警对象序号；从1开始递增。
        :type Number: int
        :param _StartTimeOffset: 查询范围起始时间相对于告警执行时间的偏移，单位为分钟，取值为非正，最大值为0，最小值为-1440。
        :type StartTimeOffset: int
        :param _EndTimeOffset: 查询范围终止时间相对于告警执行时间的偏移，单位为分钟，取值为非正，须大于StartTimeOffset，最大值为0，最小值为-1440。
        :type EndTimeOffset: int
        :param _LogsetId: 日志集ID。
        :type LogsetId: str
        :param _SyntaxRule: 检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :type SyntaxRule: int
        """
        self._TopicId = None
        self._Query = None
        self._Number = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._LogsetId = None
        self._SyntaxRule = None

    @property
    def TopicId(self):
        """日志主题ID。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Query(self):
        """查询语句。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Number(self):
        """告警对象序号；从1开始递增。
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def StartTimeOffset(self):
        """查询范围起始时间相对于告警执行时间的偏移，单位为分钟，取值为非正，最大值为0，最小值为-1440。
        :rtype: int
        """
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        """查询范围终止时间相对于告警执行时间的偏移，单位为分钟，取值为非正，须大于StartTimeOffset，最大值为0，最小值为-1440。
        :rtype: int
        """
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def LogsetId(self):
        """日志集ID。
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def SyntaxRule(self):
        """检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Query = params.get("Query")
        self._Number = params.get("Number")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._LogsetId = params.get("LogsetId")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTargetInfo(AbstractModel):
    """告警对象

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID。
        :type LogsetId: str
        :param _LogsetName: 日志集名称。
        :type LogsetName: str
        :param _TopicId: 日志主题ID。
        :type TopicId: str
        :param _TopicName: 日志主题名称。
        :type TopicName: str
        :param _Query: 查询语句。
        :type Query: str
        :param _Number: 告警对象序号。
        :type Number: int
        :param _StartTimeOffset: 查询范围起始时间相对于告警执行时间的偏移，单位为分钟，取值为非正，最大值为0，最小值为-1440。
        :type StartTimeOffset: int
        :param _EndTimeOffset: 查询范围终止时间相对于告警执行时间的偏移，单位为分钟，取值为非正，须大于StartTimeOffset，最大值为0，最小值为-1440。
        :type EndTimeOffset: int
        :param _SyntaxRule: 检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :type SyntaxRule: int
        :param _BizType: 主题类型。
0: 日志主题，1: 指标主题
        :type BizType: int
        """
        self._LogsetId = None
        self._LogsetName = None
        self._TopicId = None
        self._TopicName = None
        self._Query = None
        self._Number = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._SyntaxRule = None
        self._BizType = None

    @property
    def LogsetId(self):
        """日志集ID。
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        """日志集名称。
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicId(self):
        """日志主题ID。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """日志主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Query(self):
        """查询语句。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Number(self):
        """告警对象序号。
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def StartTimeOffset(self):
        """查询范围起始时间相对于告警执行时间的偏移，单位为分钟，取值为非正，最大值为0，最小值为-1440。
        :rtype: int
        """
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        """查询范围终止时间相对于告警执行时间的偏移，单位为分钟，取值为非正，须大于StartTimeOffset，最大值为0，最小值为-1440。
        :rtype: int
        """
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def SyntaxRule(self):
        """检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule

    @property
    def BizType(self):
        """主题类型。
0: 日志主题，1: 指标主题
        :rtype: int
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Query = params.get("Query")
        self._Number = params.get("Number")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._SyntaxRule = params.get("SyntaxRule")
        self._BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertHistoryNotice(AbstractModel):
    """告警通知渠道组详情

    """

    def __init__(self):
        r"""
        :param _Name: 通知渠道组名称
        :type Name: str
        :param _AlarmNoticeId: 通知渠道组ID
        :type AlarmNoticeId: str
        """
        self._Name = None
        self._AlarmNoticeId = None

    @property
    def Name(self):
        """通知渠道组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmNoticeId(self):
        """通知渠道组ID
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertHistoryRecord(AbstractModel):
    """告警历史详情

    """

    def __init__(self):
        r"""
        :param _RecordId: 告警历史ID
        :type RecordId: str
        :param _AlarmId: 告警策略ID
        :type AlarmId: str
        :param _AlarmName: 告警策略名称
        :type AlarmName: str
        :param _TopicId: 监控对象ID
        :type TopicId: str
        :param _TopicName: 监控对象名称
        :type TopicName: str
        :param _Region: 监控对象所属地域
        :type Region: str
        :param _Trigger: 触发条件
        :type Trigger: str
        :param _TriggerCount: 持续周期，持续满足触发条件TriggerCount个周期后，再进行告警
        :type TriggerCount: int
        :param _AlarmPeriod: 告警通知发送频率，单位为分钟
        :type AlarmPeriod: int
        :param _Notices: 通知渠道组
        :type Notices: list of AlertHistoryNotice
        :param _Duration: 告警持续时间，单位为分钟
        :type Duration: int
        :param _Status: 告警状态，0代表未恢复，1代表已恢复，2代表已失效
        :type Status: int
        :param _CreateTime: 告警发生时间，毫秒级Unix时间戳
        :type CreateTime: int
        :param _GroupTriggerCondition: 告警分组触发时对应的分组信息
        :type GroupTriggerCondition: list of GroupTriggerConditionInfo
        :param _AlarmLevel: 告警级别，0代表警告(Warn)，1代表提醒(Info)，2代表紧急 (Critical)
        :type AlarmLevel: int
        :param _MonitorObjectType: 监控对象类型。
0:执行语句共用监控对象; 1:每个执行语句单独选择监控对象。 
        :type MonitorObjectType: int
        """
        self._RecordId = None
        self._AlarmId = None
        self._AlarmName = None
        self._TopicId = None
        self._TopicName = None
        self._Region = None
        self._Trigger = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._Notices = None
        self._Duration = None
        self._Status = None
        self._CreateTime = None
        self._GroupTriggerCondition = None
        self._AlarmLevel = None
        self._MonitorObjectType = None

    @property
    def RecordId(self):
        """告警历史ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def AlarmId(self):
        """告警策略ID
        :rtype: str
        """
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def AlarmName(self):
        """告警策略名称
        :rtype: str
        """
        return self._AlarmName

    @AlarmName.setter
    def AlarmName(self, AlarmName):
        self._AlarmName = AlarmName

    @property
    def TopicId(self):
        """监控对象ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """监控对象名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Region(self):
        """监控对象所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Trigger(self):
        """触发条件
        :rtype: str
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def TriggerCount(self):
        """持续周期，持续满足触发条件TriggerCount个周期后，再进行告警
        :rtype: int
        """
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        """告警通知发送频率，单位为分钟
        :rtype: int
        """
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def Notices(self):
        """通知渠道组
        :rtype: list of AlertHistoryNotice
        """
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def Duration(self):
        """告警持续时间，单位为分钟
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Status(self):
        """告警状态，0代表未恢复，1代表已恢复，2代表已失效
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """告警发生时间，毫秒级Unix时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GroupTriggerCondition(self):
        """告警分组触发时对应的分组信息
        :rtype: list of GroupTriggerConditionInfo
        """
        return self._GroupTriggerCondition

    @GroupTriggerCondition.setter
    def GroupTriggerCondition(self, GroupTriggerCondition):
        self._GroupTriggerCondition = GroupTriggerCondition

    @property
    def AlarmLevel(self):
        """告警级别，0代表警告(Warn)，1代表提醒(Info)，2代表紧急 (Critical)
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def MonitorObjectType(self):
        """监控对象类型。
0:执行语句共用监控对象; 1:每个执行语句单独选择监控对象。 
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._AlarmId = params.get("AlarmId")
        self._AlarmName = params.get("AlarmName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Region = params.get("Region")
        self._Trigger = params.get("Trigger")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = AlertHistoryNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        self._Duration = params.get("Duration")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        if params.get("GroupTriggerCondition") is not None:
            self._GroupTriggerCondition = []
            for item in params.get("GroupTriggerCondition"):
                obj = GroupTriggerConditionInfo()
                obj._deserialize(item)
                self._GroupTriggerCondition.append(obj)
        self._AlarmLevel = params.get("AlarmLevel")
        self._MonitorObjectType = params.get("MonitorObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisDimensional(AbstractModel):
    """多维分析的分析维度

    """

    def __init__(self):
        r"""
        :param _Name: 分析名称
        :type Name: str
        :param _Type: 分析类型：query，field ，original
        :type Type: str
        :param _Content: 分析内容
        :type Content: str
        :param _ConfigInfo: 多维分析配置。

当Analysis的Type字段为query（自定义）时，支持
{
"Key": "SyntaxRule",  // 语法规则
"Value": "1"  //0：Lucene语法 ，1： CQL语法
}

当Analysis的Type字段为field（top5）时,  支持
 {
    "Key": "QueryIndex",
    "Value": "-1" //  -1：自定义， 1：执行语句1， 2：执行语句2
},{
    "Key": "CustomQuery", //检索语句。 QueryIndex为-1时有效且必填
    "Value": "* | select count(*) as count"
},{
    "Key": "SyntaxRule", // 查不到这个字段也是老语法（Lucene）
    "Value": "0"//0:Lucene, 1:CQL
}       

当Analysis的Type字段为original（原始日志）时,  支持
{
    "Key": "Fields",
    "Value": "__SOURCE__,__HOSTNAME__,__TIMESTAMP__,__PKG_LOGID__,__TAG__.pod_ip"
}, {
    "Key": "QueryIndex",
    "Value": "-1" //  -1：自定义， 1：执行语句1， 2：执行语句2
},{
    "Key": "CustomQuery", //  //检索语句。 QueryIndex为-1时有效且必填
    "Value": "* | select count(*) as count"
},{
    "Key": "Format", //显示形式。1：每条日志一行，2：每条日志每个字段一行
    "Value": "2"
},
{
    "Key": "Limit", //最大日志条数
    "Value": "5"
},{
    "Key": "SyntaxRule", // 查不到这个字段也是老语法
    "Value": "0"//0:Lucene, 1:CQL
}
        :type ConfigInfo: list of AlarmAnalysisConfig
        """
        self._Name = None
        self._Type = None
        self._Content = None
        self._ConfigInfo = None

    @property
    def Name(self):
        """分析名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """分析类型：query，field ，original
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Content(self):
        """分析内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ConfigInfo(self):
        """多维分析配置。

当Analysis的Type字段为query（自定义）时，支持
{
"Key": "SyntaxRule",  // 语法规则
"Value": "1"  //0：Lucene语法 ，1： CQL语法
}

当Analysis的Type字段为field（top5）时,  支持
 {
    "Key": "QueryIndex",
    "Value": "-1" //  -1：自定义， 1：执行语句1， 2：执行语句2
},{
    "Key": "CustomQuery", //检索语句。 QueryIndex为-1时有效且必填
    "Value": "* | select count(*) as count"
},{
    "Key": "SyntaxRule", // 查不到这个字段也是老语法（Lucene）
    "Value": "0"//0:Lucene, 1:CQL
}       

当Analysis的Type字段为original（原始日志）时,  支持
{
    "Key": "Fields",
    "Value": "__SOURCE__,__HOSTNAME__,__TIMESTAMP__,__PKG_LOGID__,__TAG__.pod_ip"
}, {
    "Key": "QueryIndex",
    "Value": "-1" //  -1：自定义， 1：执行语句1， 2：执行语句2
},{
    "Key": "CustomQuery", //  //检索语句。 QueryIndex为-1时有效且必填
    "Value": "* | select count(*) as count"
},{
    "Key": "Format", //显示形式。1：每条日志一行，2：每条日志每个字段一行
    "Value": "2"
},
{
    "Key": "Limit", //最大日志条数
    "Value": "5"
},{
    "Key": "SyntaxRule", // 查不到这个字段也是老语法
    "Value": "0"//0:Lucene, 1:CQL
}
        :rtype: list of AlarmAnalysisConfig
        """
        return self._ConfigInfo

    @ConfigInfo.setter
    def ConfigInfo(self, ConfigInfo):
        self._ConfigInfo = ConfigInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Content = params.get("Content")
        if params.get("ConfigInfo") is not None:
            self._ConfigInfo = []
            for item in params.get("ConfigInfo"):
                obj = AlarmAnalysisConfig()
                obj._deserialize(item)
                self._ConfigInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnonymousInfo(AbstractModel):
    """免鉴权信息

    """

    def __init__(self):
        r"""
        :param _Operations: 操作列表，支持trackLog(JS/HTTP上传日志  )和realtimeProducer(kafka协议上传日志)
        :type Operations: list of str
        :param _Conditions: 条件列表
        :type Conditions: list of ConditionInfo
        """
        self._Operations = None
        self._Conditions = None

    @property
    def Operations(self):
        """操作列表，支持trackLog(JS/HTTP上传日志  )和realtimeProducer(kafka协议上传日志)
        :rtype: list of str
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

    @property
    def Conditions(self):
        """条件列表
        :rtype: list of ConditionInfo
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._Operations = params.get("Operations")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = ConditionInfo()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupRequest(AbstractModel):
    """ApplyConfigToMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集配置ID
        :type ConfigId: str
        :param _GroupId: 机器组ID
        :type GroupId: str
        """
        self._ConfigId = None
        self._GroupId = None

    @property
    def ConfigId(self):
        """采集配置ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupResponse(AbstractModel):
    """ApplyConfigToMachineGroup返回参数结构体

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


class CallBackInfo(AbstractModel):
    """回调配置

    """

    def __init__(self):
        r"""
        :param _Body: 回调时的Body。
可将各类告警变量放在请求内容中，详见[帮助文档](https://cloud.tencent.com/document/product/614/74718)。
如下示例：

```
{
"TopicId": "{{ .QueryLog[0][0].topicId }}",
"key": "{{.Alarm}}",
"time": "{{ .QueryLog[0][0].time }}",
"log": "{{ .QueryLog[0][0].content.__CONTENT__ }}",
"namespace": "{{ .QueryLog[0][0].content.__TAG__.namespace }}"
}
```
        :type Body: str
        :param _Headers: 回调时的HTTP请求头部字段。
例如：下面请求头部字段来告知服务器请求主体的内容类型为JSON。
```
"Content-Type: application/json"
```
        :type Headers: list of str
        """
        self._Body = None
        self._Headers = None

    @property
    def Body(self):
        """回调时的Body。
可将各类告警变量放在请求内容中，详见[帮助文档](https://cloud.tencent.com/document/product/614/74718)。
如下示例：

```
{
"TopicId": "{{ .QueryLog[0][0].topicId }}",
"key": "{{.Alarm}}",
"time": "{{ .QueryLog[0][0].time }}",
"log": "{{ .QueryLog[0][0].content.__CONTENT__ }}",
"namespace": "{{ .QueryLog[0][0].content.__TAG__.namespace }}"
}
```
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Headers(self):
        """回调时的HTTP请求头部字段。
例如：下面请求头部字段来告知服务器请求主体的内容类型为JSON。
```
"Content-Type: application/json"
```
        :rtype: list of str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._Headers = params.get("Headers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckFunctionRequest(AbstractModel):
    """CheckFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EtlContent: 用户输入的加工语句
        :type EtlContent: str
        :param _DstResources: 加工任务目的topic_id以及别名
        :type DstResources: list of DataTransformResouceInfo
        :param _FuncType: 数据加工目标主题的类型. 1 固定主题 2动态创建
        :type FuncType: int
        """
        self._EtlContent = None
        self._DstResources = None
        self._FuncType = None

    @property
    def EtlContent(self):
        """用户输入的加工语句
        :rtype: str
        """
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent

    @property
    def DstResources(self):
        """加工任务目的topic_id以及别名
        :rtype: list of DataTransformResouceInfo
        """
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources

    @property
    def FuncType(self):
        """数据加工目标主题的类型. 1 固定主题 2动态创建
        :rtype: int
        """
        return self._FuncType

    @FuncType.setter
    def FuncType(self, FuncType):
        self._FuncType = FuncType


    def _deserialize(self, params):
        self._EtlContent = params.get("EtlContent")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        self._FuncType = params.get("FuncType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckFunctionResponse(AbstractModel):
    """CheckFunction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 失败错误码
        :type ErrorCode: int
        :param _ErrorMsg: 失败错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        """失败错误码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        """失败错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class CheckRechargeKafkaServerRequest(AbstractModel):
    """CheckRechargeKafkaServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KafkaType: 导入Kafka类型，0: 腾讯云CKafka；1: 用户自建Kafka。
        :type KafkaType: int
        :param _KafkaInstance: 腾讯云CKafka实例ID。
KafkaType为0时，KafkaInstance必填
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址。
KafkaType为1时，ServerAddr必填
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接，默认值false。当KafkaType为1用户自建kafka时生效。
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议。KafkaType参数为1并且IsEncryptionAddr参数为true时必填。
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        """
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None

    @property
    def KafkaType(self):
        """导入Kafka类型，0: 腾讯云CKafka；1: 用户自建Kafka。
        :rtype: int
        """
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        """腾讯云CKafka实例ID。
KafkaType为0时，KafkaInstance必填
        :rtype: str
        """
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        """服务地址。
KafkaType为1时，ServerAddr必填
        :rtype: str
        """
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        """ServerAddr是否为加密连接，默认值false。当KafkaType为1用户自建kafka时生效。
        :rtype: bool
        """
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        """加密访问协议。KafkaType参数为1并且IsEncryptionAddr参数为true时必填。
        :rtype: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRechargeKafkaServerResponse(AbstractModel):
    """CheckRechargeKafkaServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: Kafka集群可访问状态，0：可正常访问 ...
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Kafka集群可访问状态，0：可正常访问 ...
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class Ckafka(AbstractModel):
    """CKafka的描述-需要投递到的kafka信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: Ckafka 的 InstanceId
        :type InstanceId: str
        :param _TopicName: Ckafka 的 TopicName
        :type TopicName: str
        :param _Vip: Ckafka 的 Vip
        :type Vip: str
        :param _Vport: Ckafka 的 Vport
        :type Vport: str
        :param _InstanceName: Ckafka 的 InstanceName
        :type InstanceName: str
        :param _TopicId: Ckafka 的 TopicId
        :type TopicId: str
        """
        self._InstanceId = None
        self._TopicName = None
        self._Vip = None
        self._Vport = None
        self._InstanceName = None
        self._TopicId = None

    @property
    def InstanceId(self):
        """Ckafka 的 InstanceId
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """Ckafka 的 TopicName
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Vip(self):
        """Ckafka 的 Vip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Ckafka 的 Vport
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def InstanceName(self):
        """Ckafka 的 InstanceName
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def TopicId(self):
        """Ckafka 的 TopicId
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._InstanceName = params.get("InstanceName")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseKafkaConsumerRequest(AbstractModel):
    """CloseKafkaConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTopicId: 日志主题ID
        :type FromTopicId: str
        """
        self._FromTopicId = None

    @property
    def FromTopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._FromTopicId

    @FromTopicId.setter
    def FromTopicId(self, FromTopicId):
        self._FromTopicId = FromTopicId


    def _deserialize(self, params):
        self._FromTopicId = params.get("FromTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseKafkaConsumerResponse(AbstractModel):
    """CloseKafkaConsumer返回参数结构体

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


class CollectConfig(AbstractModel):
    """采集配置信息

    """

    def __init__(self):
        r"""
        :param _Name: 指定采集类型的采集配置名称信息。
<li>当CollectInfo中Type为0：表示元数据配置，name为元数据名称。
目前支持"container_id"，"container_name"，"image_name"，"namespace"，"pod_uid"，"pod_name"，"pod_ip"。
</li>
<li>当CollectInfo中Type为1：指定pod label，name为指定pod label名称。</li>
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """指定采集类型的采集配置名称信息。
<li>当CollectInfo中Type为0：表示元数据配置，name为元数据名称。
目前支持"container_id"，"container_name"，"image_name"，"namespace"，"pod_uid"，"pod_name"，"pod_ip"。
</li>
<li>当CollectInfo中Type为1：指定pod label，name为指定pod label名称。</li>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CollectInfo(AbstractModel):
    """采集配置信息

    """

    def __init__(self):
        r"""
        :param _Type: 采集类型，必填字段。
<li>0：元数据配置。</li>
<li>1：指定Pod Label。</li>
        :type Type: int
        :param _CollectConfigs: 指定采集类型的采集配置信息。
<li>当Type为0时，CollectConfigs不允许为空。</li>
<li>当Type为1时，CollectConfigs为空时，表示选择所有Pod Label；否则CollectConfigs为指定Pod Label。</li>
        :type CollectConfigs: list of CollectConfig
        """
        self._Type = None
        self._CollectConfigs = None

    @property
    def Type(self):
        """采集类型，必填字段。
<li>0：元数据配置。</li>
<li>1：指定Pod Label。</li>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CollectConfigs(self):
        """指定采集类型的采集配置信息。
<li>当Type为0时，CollectConfigs不允许为空。</li>
<li>当Type为1时，CollectConfigs为空时，表示选择所有Pod Label；否则CollectConfigs为指定Pod Label。</li>
        :rtype: list of CollectConfig
        """
        return self._CollectConfigs

    @CollectConfigs.setter
    def CollectConfigs(self, CollectConfigs):
        self._CollectConfigs = CollectConfigs


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("CollectConfigs") is not None:
            self._CollectConfigs = []
            for item in params.get("CollectConfigs"):
                obj = CollectConfig()
                obj._deserialize(item)
                self._CollectConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Column(AbstractModel):
    """日志分析的列属性

    """

    def __init__(self):
        r"""
        :param _Name: 列的名字
        :type Name: str
        :param _Type: 列的属性
        :type Type: str
        """
        self._Name = None
        self._Type = None

    @property
    def Name(self):
        """列的名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """列的属性
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressInfo(AbstractModel):
    """投递日志的压缩配置

    """

    def __init__(self):
        r"""
        :param _Format: 压缩格式，支持gzip、lzop、snappy和none不压缩
        :type Format: str
        """
        self._Format = None

    @property
    def Format(self):
        """压缩格式，支持gzip、lzop、snappy和none不压缩
        :rtype: str
        """
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
        


class ConditionInfo(AbstractModel):
    """免鉴权条件信息

    """

    def __init__(self):
        r"""
        :param _Attributes: 条件属性，目前只支持VpcID
        :type Attributes: str
        :param _Rule: 条件规则，1:等于，2:不等于
        :type Rule: int
        :param _ConditionValue: 对应条件属性的值
        :type ConditionValue: str
        """
        self._Attributes = None
        self._Rule = None
        self._ConditionValue = None

    @property
    def Attributes(self):
        """条件属性，目前只支持VpcID
        :rtype: str
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

    @property
    def Rule(self):
        """条件规则，1:等于，2:不等于
        :rtype: int
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def ConditionValue(self):
        """对应条件属性的值
        :rtype: str
        """
        return self._ConditionValue

    @ConditionValue.setter
    def ConditionValue(self, ConditionValue):
        self._ConditionValue = ConditionValue


    def _deserialize(self, params):
        self._Attributes = params.get("Attributes")
        self._Rule = params.get("Rule")
        self._ConditionValue = params.get("ConditionValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigExtraInfo(AbstractModel):
    """特殊采集规则配置信息

    """

    def __init__(self):
        r"""
        :param _ConfigExtraId: 采集规则扩展配置ID
        :type ConfigExtraId: str
        :param _Name: 采集规则名称
        :type Name: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Type: 类型：container_stdout、container_file、host_file
        :type Type: str
        :param _HostFile: 节点文件配置信息
        :type HostFile: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        :param _ContainerFile: 容器文件路径信息
        :type ContainerFile: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        :param _ContainerStdout: 容器标准输出信息
        :type ContainerStdout: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        :param _LogFormat: 日志格式化方式
        :type LogFormat: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
        :type LogType: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludePaths: list of ExcludePathInfo
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UserDefineRule: 用户自定义解析字符串
        :type UserDefineRule: str
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _ConfigFlag: 自建采集配置标
        :type ConfigFlag: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _LogsetName: 日志集name
        :type LogsetName: str
        :param _TopicName: 日志主题name
        :type TopicName: str
        :param _CollectInfos: 采集相关配置信息。详情见 CollectInfo复杂类型配置。
        :type CollectInfos: list of CollectInfo
        :param _AdvancedConfig: 高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
样例：{"ClsAgentFileTimeout":0,"ClsAgentMaxDepth":10,"ClsAgentParseFailMerge":true}
        :type AdvancedConfig: str
        """
        self._ConfigExtraId = None
        self._Name = None
        self._TopicId = None
        self._Type = None
        self._HostFile = None
        self._ContainerFile = None
        self._ContainerStdout = None
        self._LogFormat = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UpdateTime = None
        self._CreateTime = None
        self._UserDefineRule = None
        self._GroupId = None
        self._ConfigFlag = None
        self._LogsetId = None
        self._LogsetName = None
        self._TopicName = None
        self._CollectInfos = None
        self._AdvancedConfig = None

    @property
    def ConfigExtraId(self):
        """采集规则扩展配置ID
        :rtype: str
        """
        return self._ConfigExtraId

    @ConfigExtraId.setter
    def ConfigExtraId(self, ConfigExtraId):
        self._ConfigExtraId = ConfigExtraId

    @property
    def Name(self):
        """采集规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Type(self):
        """类型：container_stdout、container_file、host_file
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HostFile(self):
        """节点文件配置信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        """
        return self._HostFile

    @HostFile.setter
    def HostFile(self, HostFile):
        self._HostFile = HostFile

    @property
    def ContainerFile(self):
        """容器文件路径信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        """
        return self._ContainerFile

    @ContainerFile.setter
    def ContainerFile(self, ContainerFile):
        self._ContainerFile = ContainerFile

    @property
    def ContainerStdout(self):
        """容器标准输出信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        """
        return self._ContainerStdout

    @ContainerStdout.setter
    def ContainerStdout(self, ContainerStdout):
        self._ContainerStdout = ContainerStdout

    @property
    def LogFormat(self):
        """日志格式化方式
        :rtype: str
        """
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def LogType(self):
        """采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表极简日志，multiline_log代表多行日志，fullregex_log代表完整正则，默认为minimalist_log
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        """提取规则，如果设置了ExtractRule，则必须设置LogType
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        """采集黑名单路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ExcludePathInfo
        """
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
    def UserDefineRule(self):
        """用户自定义解析字符串
        :rtype: str
        """
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ConfigFlag(self):
        """自建采集配置标
        :rtype: str
        """
        return self._ConfigFlag

    @ConfigFlag.setter
    def ConfigFlag(self, ConfigFlag):
        self._ConfigFlag = ConfigFlag

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        """日志集name
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicName(self):
        """日志主题name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def CollectInfos(self):
        """采集相关配置信息。详情见 CollectInfo复杂类型配置。
        :rtype: list of CollectInfo
        """
        return self._CollectInfos

    @CollectInfos.setter
    def CollectInfos(self, CollectInfos):
        self._CollectInfos = CollectInfos

    @property
    def AdvancedConfig(self):
        """高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
样例：{"ClsAgentFileTimeout":0,"ClsAgentMaxDepth":10,"ClsAgentParseFailMerge":true}
        :rtype: str
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._ConfigExtraId = params.get("ConfigExtraId")
        self._Name = params.get("Name")
        self._TopicId = params.get("TopicId")
        self._Type = params.get("Type")
        if params.get("HostFile") is not None:
            self._HostFile = HostFileInfo()
            self._HostFile._deserialize(params.get("HostFile"))
        if params.get("ContainerFile") is not None:
            self._ContainerFile = ContainerFileInfo()
            self._ContainerFile._deserialize(params.get("ContainerFile"))
        if params.get("ContainerStdout") is not None:
            self._ContainerStdout = ContainerStdoutInfo()
            self._ContainerStdout._deserialize(params.get("ContainerStdout"))
        self._LogFormat = params.get("LogFormat")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._UserDefineRule = params.get("UserDefineRule")
        self._GroupId = params.get("GroupId")
        self._ConfigFlag = params.get("ConfigFlag")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicName = params.get("TopicName")
        if params.get("CollectInfos") is not None:
            self._CollectInfos = []
            for item in params.get("CollectInfos"):
                obj = CollectInfo()
                obj._deserialize(item)
                self._CollectInfos.append(obj)
        self._AdvancedConfig = params.get("AdvancedConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigInfo(AbstractModel):
    """采集规则配置信息

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集规则配置ID
        :type ConfigId: str
        :param _Name: 采集规则配置名称
        :type Name: str
        :param _LogFormat: 日志格式化方式
        :type LogFormat: str
        :param _Path: 日志采集路径
        :type Path: str
        :param _LogType: 采集的日志类型。
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）；
- service_syslog代表：syslog 采集（详见[采集 Syslog](https://cloud.tencent.com/document/product/614/81454)）；
- windows_event_log代表：Windows事件日志（详见[采集 Windows 事件日志](https://cloud.tencent.com/document/product/614/96678)）。
        :type LogType: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludePaths: list of ExcludePathInfo
        :param _Output: 采集配置所属日志主题ID即TopicId
        :type Output: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UserDefineRule: 用户自定义解析字符串，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)。
        :type UserDefineRule: str
        :param _AdvancedConfig: 高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
样例：
`{\"ClsAgentFileTimeout\":0,\"ClsAgentMaxDepth\":10,\"ClsAgentParseFailMerge\":true}`

控制台默认占位值：`{\"ClsAgentDefault\":0}`
        :type AdvancedConfig: str
        """
        self._ConfigId = None
        self._Name = None
        self._LogFormat = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._Output = None
        self._UpdateTime = None
        self._CreateTime = None
        self._UserDefineRule = None
        self._AdvancedConfig = None

    @property
    def ConfigId(self):
        """采集规则配置ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Name(self):
        """采集规则配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LogFormat(self):
        """日志格式化方式
        :rtype: str
        """
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def Path(self):
        """日志采集路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        """采集的日志类型。
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）；
- service_syslog代表：syslog 采集（详见[采集 Syslog](https://cloud.tencent.com/document/product/614/81454)）；
- windows_event_log代表：Windows事件日志（详见[采集 Windows 事件日志](https://cloud.tencent.com/document/product/614/96678)）。
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        """提取规则，如果设置了ExtractRule，则必须设置LogType
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        """采集黑名单路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ExcludePathInfo
        """
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def Output(self):
        """采集配置所属日志主题ID即TopicId
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
    def UserDefineRule(self):
        """用户自定义解析字符串，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)。
        :rtype: str
        """
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def AdvancedConfig(self):
        """高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
样例：
`{\"ClsAgentFileTimeout\":0,\"ClsAgentMaxDepth\":10,\"ClsAgentParseFailMerge\":true}`

控制台默认占位值：`{\"ClsAgentDefault\":0}`
        :rtype: str
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._Name = params.get("Name")
        self._LogFormat = params.get("LogFormat")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._Output = params.get("Output")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._UserDefineRule = params.get("UserDefineRule")
        self._AdvancedConfig = params.get("AdvancedConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsoleSharingConfig(AbstractModel):
    """控制台分享配置

    """

    def __init__(self):
        r"""
        :param _Name: 分享链接名称
        :type Name: str
        :param _Type: 仪表盘: 1; 检索页:2
        :type Type: int
        :param _DurationMilliseconds: 分享链接有效期，单位：毫秒，最长支持30天
        :type DurationMilliseconds: int
        :param _Resources: 允许访问的资源列表，目前仅支持一个Resource
        :type Resources: list of str
        :param _Domain: 分享链接域名，可选范围
- 公网匿名分享：填写clsshare.com
- datasight内网匿名分享(若开启)：datasight内网域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _VerifyCode: 分享链接加密访问验证码。支持0-9和a-z(不区分大小写)在内的6个字符，可为空，代表免验证码访问
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyCode: str
        :param _StartTime: 默认查询范围的开始时间点，支持绝对时间(13位Unix时间戳)或相对时间表达式
        :type StartTime: str
        :param _EndTime: 默认查询范围的结束时间点，支持绝对时间(13位Unix时间戳)或相对时间表达式。注意，结束时间点要大于开始时间点
        :type EndTime: str
        :param _NowTime: 仅当StartTime/EndTime为相对时间时使用，基于NowTime计算绝对时间，默认为创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type NowTime: int
        :param _Params: 默认的检索分析语句，仅当Type为2时使用
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of ConsoleSharingParam
        :param _IsLockTimeRange: 是否允许访问者自行修改检索分析时间范围。默认不锁定（false）
        :type IsLockTimeRange: bool
        :param _IsLockQuery: 是否允许访问者自行修改日志检索语句。在检索页分享中表示检索语句锁定状态；在仪表盘中表示过滤变量锁定状态。默认不锁定（false）
        :type IsLockQuery: bool
        :param _IsSupportLogExport: 检索页分享是否允许访问者下载日志，默认不允许（false）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportLogExport: bool
        """
        self._Name = None
        self._Type = None
        self._DurationMilliseconds = None
        self._Resources = None
        self._Domain = None
        self._VerifyCode = None
        self._StartTime = None
        self._EndTime = None
        self._NowTime = None
        self._Params = None
        self._IsLockTimeRange = None
        self._IsLockQuery = None
        self._IsSupportLogExport = None

    @property
    def Name(self):
        """分享链接名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """仪表盘: 1; 检索页:2
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DurationMilliseconds(self):
        """分享链接有效期，单位：毫秒，最长支持30天
        :rtype: int
        """
        return self._DurationMilliseconds

    @DurationMilliseconds.setter
    def DurationMilliseconds(self, DurationMilliseconds):
        self._DurationMilliseconds = DurationMilliseconds

    @property
    def Resources(self):
        """允许访问的资源列表，目前仅支持一个Resource
        :rtype: list of str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Domain(self):
        """分享链接域名，可选范围
- 公网匿名分享：填写clsshare.com
- datasight内网匿名分享(若开启)：datasight内网域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def VerifyCode(self):
        """分享链接加密访问验证码。支持0-9和a-z(不区分大小写)在内的6个字符，可为空，代表免验证码访问
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode

    @property
    def StartTime(self):
        """默认查询范围的开始时间点，支持绝对时间(13位Unix时间戳)或相对时间表达式
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """默认查询范围的结束时间点，支持绝对时间(13位Unix时间戳)或相对时间表达式。注意，结束时间点要大于开始时间点
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NowTime(self):
        """仅当StartTime/EndTime为相对时间时使用，基于NowTime计算绝对时间，默认为创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NowTime

    @NowTime.setter
    def NowTime(self, NowTime):
        self._NowTime = NowTime

    @property
    def Params(self):
        """默认的检索分析语句，仅当Type为2时使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConsoleSharingParam
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def IsLockTimeRange(self):
        """是否允许访问者自行修改检索分析时间范围。默认不锁定（false）
        :rtype: bool
        """
        return self._IsLockTimeRange

    @IsLockTimeRange.setter
    def IsLockTimeRange(self, IsLockTimeRange):
        self._IsLockTimeRange = IsLockTimeRange

    @property
    def IsLockQuery(self):
        """是否允许访问者自行修改日志检索语句。在检索页分享中表示检索语句锁定状态；在仪表盘中表示过滤变量锁定状态。默认不锁定（false）
        :rtype: bool
        """
        return self._IsLockQuery

    @IsLockQuery.setter
    def IsLockQuery(self, IsLockQuery):
        self._IsLockQuery = IsLockQuery

    @property
    def IsSupportLogExport(self):
        """检索页分享是否允许访问者下载日志，默认不允许（false）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsSupportLogExport

    @IsSupportLogExport.setter
    def IsSupportLogExport(self, IsSupportLogExport):
        self._IsSupportLogExport = IsSupportLogExport


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._DurationMilliseconds = params.get("DurationMilliseconds")
        self._Resources = params.get("Resources")
        self._Domain = params.get("Domain")
        self._VerifyCode = params.get("VerifyCode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NowTime = params.get("NowTime")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = ConsoleSharingParam()
                obj._deserialize(item)
                self._Params.append(obj)
        self._IsLockTimeRange = params.get("IsLockTimeRange")
        self._IsLockQuery = params.get("IsLockQuery")
        self._IsSupportLogExport = params.get("IsSupportLogExport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsoleSharingParam(AbstractModel):
    """控制台分享链接params参数

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class ConsumerContent(AbstractModel):
    """投递任务出入参 Content

    """

    def __init__(self):
        r"""
        :param _EnableTag: 是否投递 TAG 信息。
当EnableTag为true时，表示投递TAG元信息。
        :type EnableTag: bool
        :param _MetaFields: 需要投递的元数据列表，目前仅支持：\_\_SOURCE\_\_，\_\_FILENAME\_\_，\_\_TIMESTAMP\_\_，\_\_HOSTNAME\_\_和\_\_PKGID\_\_
        :type MetaFields: list of str
        :param _TagJsonNotTiled: 当EnableTag为true时，必须填写TagJsonNotTiled字段。
TagJsonNotTiled用于标识tag信息是否json平铺。

TagJsonNotTiled为true时不平铺，示例：
TAG信息：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`
不平铺：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`

TagJsonNotTiled为false时平铺，示例：
TAG信息：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`
平铺：`{"__TAG__.fieldA":200,"__TAG__.fieldB":"text"}`
        :type TagJsonNotTiled: bool
        :param _TimestampAccuracy: 投递时间戳精度，可选项 [1：秒；2：毫秒] ，默认是1。
        :type TimestampAccuracy: int
        :param _JsonType: 投递Json格式。
JsonType为0：和原始日志一致，不转义。示例：
日志原文：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`
投递到Ckafka：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`

JsonType为1：转义。示例：
日志原文：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`
投递到Ckafka：`{"a":"aa","b":"{\"b1\":\"b1b1\", \"c1\":\"c1c1\"}"}`
        :type JsonType: int
        """
        self._EnableTag = None
        self._MetaFields = None
        self._TagJsonNotTiled = None
        self._TimestampAccuracy = None
        self._JsonType = None

    @property
    def EnableTag(self):
        """是否投递 TAG 信息。
当EnableTag为true时，表示投递TAG元信息。
        :rtype: bool
        """
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        """需要投递的元数据列表，目前仅支持：\_\_SOURCE\_\_，\_\_FILENAME\_\_，\_\_TIMESTAMP\_\_，\_\_HOSTNAME\_\_和\_\_PKGID\_\_
        :rtype: list of str
        """
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def TagJsonNotTiled(self):
        """当EnableTag为true时，必须填写TagJsonNotTiled字段。
TagJsonNotTiled用于标识tag信息是否json平铺。

TagJsonNotTiled为true时不平铺，示例：
TAG信息：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`
不平铺：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`

TagJsonNotTiled为false时平铺，示例：
TAG信息：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`
平铺：`{"__TAG__.fieldA":200,"__TAG__.fieldB":"text"}`
        :rtype: bool
        """
        return self._TagJsonNotTiled

    @TagJsonNotTiled.setter
    def TagJsonNotTiled(self, TagJsonNotTiled):
        self._TagJsonNotTiled = TagJsonNotTiled

    @property
    def TimestampAccuracy(self):
        """投递时间戳精度，可选项 [1：秒；2：毫秒] ，默认是1。
        :rtype: int
        """
        return self._TimestampAccuracy

    @TimestampAccuracy.setter
    def TimestampAccuracy(self, TimestampAccuracy):
        self._TimestampAccuracy = TimestampAccuracy

    @property
    def JsonType(self):
        """投递Json格式。
JsonType为0：和原始日志一致，不转义。示例：
日志原文：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`
投递到Ckafka：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`

JsonType为1：转义。示例：
日志原文：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`
投递到Ckafka：`{"a":"aa","b":"{\"b1\":\"b1b1\", \"c1\":\"c1c1\"}"}`
        :rtype: int
        """
        return self._JsonType

    @JsonType.setter
    def JsonType(self, JsonType):
        self._JsonType = JsonType


    def _deserialize(self, params):
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._TagJsonNotTiled = params.get("TagJsonNotTiled")
        self._TimestampAccuracy = params.get("TimestampAccuracy")
        self._JsonType = params.get("JsonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerFileInfo(AbstractModel):
    """自建k8s-容器文件路径信息

    """

    def __init__(self):
        r"""
        :param _Namespace: namespace可以多个，用分隔号分割,例如A,B
        :type Namespace: str
        :param _Container: 容器名称
        :type Container: str
        :param _LogPath: 日志文件夹
        :type LogPath: str
        :param _FilePattern: 日志名称
        :type FilePattern: str
        :param _FilePaths: 日志文件信息
        :type FilePaths: list of FilePathInfo
        :param _IncludeLabels: pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeLabels: list of str
        :param _WorkLoad: 工作负载信息
        :type WorkLoad: :class:`tencentcloud.cls.v20201016.models.ContainerWorkLoadInfo`
        :param _ExcludeNamespace: 需要排除的namespace可以多个，用分隔号分割,例如A,B
        :type ExcludeNamespace: str
        :param _ExcludeLabels: 需要排除的pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeLabels: list of str
        :param _CustomLabels: metadata信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLabels: list of str
        """
        self._Namespace = None
        self._Container = None
        self._LogPath = None
        self._FilePattern = None
        self._FilePaths = None
        self._IncludeLabels = None
        self._WorkLoad = None
        self._ExcludeNamespace = None
        self._ExcludeLabels = None
        self._CustomLabels = None

    @property
    def Namespace(self):
        """namespace可以多个，用分隔号分割,例如A,B
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Container(self):
        """容器名称
        :rtype: str
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def LogPath(self):
        """日志文件夹
        :rtype: str
        """
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def FilePattern(self):
        """日志名称
        :rtype: str
        """
        return self._FilePattern

    @FilePattern.setter
    def FilePattern(self, FilePattern):
        self._FilePattern = FilePattern

    @property
    def FilePaths(self):
        """日志文件信息
        :rtype: list of FilePathInfo
        """
        return self._FilePaths

    @FilePaths.setter
    def FilePaths(self, FilePaths):
        self._FilePaths = FilePaths

    @property
    def IncludeLabels(self):
        """pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IncludeLabels

    @IncludeLabels.setter
    def IncludeLabels(self, IncludeLabels):
        self._IncludeLabels = IncludeLabels

    @property
    def WorkLoad(self):
        """工作负载信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContainerWorkLoadInfo`
        """
        return self._WorkLoad

    @WorkLoad.setter
    def WorkLoad(self, WorkLoad):
        self._WorkLoad = WorkLoad

    @property
    def ExcludeNamespace(self):
        """需要排除的namespace可以多个，用分隔号分割,例如A,B
        :rtype: str
        """
        return self._ExcludeNamespace

    @ExcludeNamespace.setter
    def ExcludeNamespace(self, ExcludeNamespace):
        self._ExcludeNamespace = ExcludeNamespace

    @property
    def ExcludeLabels(self):
        """需要排除的pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ExcludeLabels

    @ExcludeLabels.setter
    def ExcludeLabels(self, ExcludeLabels):
        self._ExcludeLabels = ExcludeLabels

    @property
    def CustomLabels(self):
        """metadata信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CustomLabels

    @CustomLabels.setter
    def CustomLabels(self, CustomLabels):
        self._CustomLabels = CustomLabels


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Container = params.get("Container")
        self._LogPath = params.get("LogPath")
        self._FilePattern = params.get("FilePattern")
        if params.get("FilePaths") is not None:
            self._FilePaths = []
            for item in params.get("FilePaths"):
                obj = FilePathInfo()
                obj._deserialize(item)
                self._FilePaths.append(obj)
        self._IncludeLabels = params.get("IncludeLabels")
        if params.get("WorkLoad") is not None:
            self._WorkLoad = ContainerWorkLoadInfo()
            self._WorkLoad._deserialize(params.get("WorkLoad"))
        self._ExcludeNamespace = params.get("ExcludeNamespace")
        self._ExcludeLabels = params.get("ExcludeLabels")
        self._CustomLabels = params.get("CustomLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerStdoutInfo(AbstractModel):
    """自建k8s-容器标准输出信息

    """

    def __init__(self):
        r"""
        :param _AllContainers: 是否所有容器
        :type AllContainers: bool
        :param _Container: container为空表所有的，不为空采集指定的容器
        :type Container: str
        :param _Namespace: namespace可以多个，用分隔号分割,例如A,B；为空或者没有这个字段，表示所有namespace
        :type Namespace: str
        :param _IncludeLabels: pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeLabels: list of str
        :param _WorkLoads: 工作负载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkLoads: list of ContainerWorkLoadInfo
        :param _ExcludeNamespace: 需要排除的namespace可以多个，用分隔号分割,例如A,B
        :type ExcludeNamespace: str
        :param _ExcludeLabels: 需要排除的pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeLabels: list of str
        :param _CustomLabels: metadata信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLabels: list of str
        """
        self._AllContainers = None
        self._Container = None
        self._Namespace = None
        self._IncludeLabels = None
        self._WorkLoads = None
        self._ExcludeNamespace = None
        self._ExcludeLabels = None
        self._CustomLabels = None

    @property
    def AllContainers(self):
        """是否所有容器
        :rtype: bool
        """
        return self._AllContainers

    @AllContainers.setter
    def AllContainers(self, AllContainers):
        self._AllContainers = AllContainers

    @property
    def Container(self):
        """container为空表所有的，不为空采集指定的容器
        :rtype: str
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def Namespace(self):
        """namespace可以多个，用分隔号分割,例如A,B；为空或者没有这个字段，表示所有namespace
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def IncludeLabels(self):
        """pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IncludeLabels

    @IncludeLabels.setter
    def IncludeLabels(self, IncludeLabels):
        self._IncludeLabels = IncludeLabels

    @property
    def WorkLoads(self):
        """工作负载信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ContainerWorkLoadInfo
        """
        return self._WorkLoads

    @WorkLoads.setter
    def WorkLoads(self, WorkLoads):
        self._WorkLoads = WorkLoads

    @property
    def ExcludeNamespace(self):
        """需要排除的namespace可以多个，用分隔号分割,例如A,B
        :rtype: str
        """
        return self._ExcludeNamespace

    @ExcludeNamespace.setter
    def ExcludeNamespace(self, ExcludeNamespace):
        self._ExcludeNamespace = ExcludeNamespace

    @property
    def ExcludeLabels(self):
        """需要排除的pod标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ExcludeLabels

    @ExcludeLabels.setter
    def ExcludeLabels(self, ExcludeLabels):
        self._ExcludeLabels = ExcludeLabels

    @property
    def CustomLabels(self):
        """metadata信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CustomLabels

    @CustomLabels.setter
    def CustomLabels(self, CustomLabels):
        self._CustomLabels = CustomLabels


    def _deserialize(self, params):
        self._AllContainers = params.get("AllContainers")
        self._Container = params.get("Container")
        self._Namespace = params.get("Namespace")
        self._IncludeLabels = params.get("IncludeLabels")
        if params.get("WorkLoads") is not None:
            self._WorkLoads = []
            for item in params.get("WorkLoads"):
                obj = ContainerWorkLoadInfo()
                obj._deserialize(item)
                self._WorkLoads.append(obj)
        self._ExcludeNamespace = params.get("ExcludeNamespace")
        self._ExcludeLabels = params.get("ExcludeLabels")
        self._CustomLabels = params.get("CustomLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerWorkLoadInfo(AbstractModel):
    """自建k8s-工作负载信息

    """

    def __init__(self):
        r"""
        :param _Kind: 工作负载的类型
        :type Kind: str
        :param _Name: 工作负载的名称
        :type Name: str
        :param _Container: 容器名
        :type Container: str
        :param _Namespace: 命名空间
        :type Namespace: str
        """
        self._Kind = None
        self._Name = None
        self._Container = None
        self._Namespace = None

    @property
    def Kind(self):
        """工作负载的类型
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        """工作负载的名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Container(self):
        """容器名
        :rtype: str
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def Namespace(self):
        """命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        self._Container = params.get("Container")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentInfo(AbstractModel):
    """投递日志的内容格式配置

    """

    def __init__(self):
        r"""
        :param _Format: 内容格式，支持json、csv
        :type Format: str
        :param _Csv: csv格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Csv: :class:`tencentcloud.cls.v20201016.models.CsvInfo`
        :param _Json: json格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: :class:`tencentcloud.cls.v20201016.models.JsonInfo`
        :param _Parquet: parquet格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Parquet: :class:`tencentcloud.cls.v20201016.models.ParquetInfo`
        """
        self._Format = None
        self._Csv = None
        self._Json = None
        self._Parquet = None

    @property
    def Format(self):
        """内容格式，支持json、csv
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Csv(self):
        """csv格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.CsvInfo`
        """
        return self._Csv

    @Csv.setter
    def Csv(self, Csv):
        self._Csv = Csv

    @property
    def Json(self):
        """json格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.JsonInfo`
        """
        return self._Json

    @Json.setter
    def Json(self, Json):
        self._Json = Json

    @property
    def Parquet(self):
        """parquet格式内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.ParquetInfo`
        """
        return self._Parquet

    @Parquet.setter
    def Parquet(self, Parquet):
        self._Parquet = Parquet


    def _deserialize(self, params):
        self._Format = params.get("Format")
        if params.get("Csv") is not None:
            self._Csv = CsvInfo()
            self._Csv._deserialize(params.get("Csv"))
        if params.get("Json") is not None:
            self._Json = JsonInfo()
            self._Json._deserialize(params.get("Json"))
        if params.get("Parquet") is not None:
            self._Parquet = ParquetInfo()
            self._Parquet._deserialize(params.get("Parquet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosRechargeInfo(AbstractModel):
    """cos导入配置信息

    """

    def __init__(self):
        r"""
        :param _Id: COS导入配置ID
        :type Id: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _Name: COS导入任务名称
        :type Name: str
        :param _Bucket: COS存储桶
        :type Bucket: str
        :param _BucketRegion: COS存储桶所在地域
        :type BucketRegion: str
        :param _Prefix: COS文件所在文件夹的前缀
        :type Prefix: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表单行全文；
默认为minimalist_log
        :type LogType: str
        :param _Status: 状态   status 0: 已创建, 1: 运行中, 2: 已停止, 3: 已完成, 4: 运行失败。
        :type Status: int
        :param _Enable: 是否启用:   0： 未启用  ， 1：启用
        :type Enable: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Progress: 进度条百分值
        :type Progress: int
        :param _Compress: supported: "", "gzip", "lzop", "snappy”; 默认空
        :type Compress: str
        :param _ExtractRuleInfo: 见： ExtractRuleInfo 结构描述
        :type ExtractRuleInfo: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _TaskType: COS导入任务类型。1：一次性导入任务；2：持续性导入任务。
        :type TaskType: int
        :param _Metadata: 元数据。支持 bucket，object。
        :type Metadata: list of str
        """
        self._Id = None
        self._TopicId = None
        self._LogsetId = None
        self._Name = None
        self._Bucket = None
        self._BucketRegion = None
        self._Prefix = None
        self._LogType = None
        self._Status = None
        self._Enable = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Progress = None
        self._Compress = None
        self._ExtractRuleInfo = None
        self._TaskType = None
        self._Metadata = None

    @property
    def Id(self):
        """COS导入配置ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Name(self):
        """COS导入任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Bucket(self):
        """COS存储桶
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def BucketRegion(self):
        """COS存储桶所在地域
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def Prefix(self):
        """COS文件所在文件夹的前缀
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def LogType(self):
        """采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表单行全文；
默认为minimalist_log
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Status(self):
        """状态   status 0: 已创建, 1: 运行中, 2: 已停止, 3: 已完成, 4: 运行失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        """是否启用:   0： 未启用  ， 1：启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

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
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Progress(self):
        """进度条百分值
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Compress(self):
        """supported: "", "gzip", "lzop", "snappy”; 默认空
        :rtype: str
        """
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def ExtractRuleInfo(self):
        """见： ExtractRuleInfo 结构描述
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRuleInfo

    @ExtractRuleInfo.setter
    def ExtractRuleInfo(self, ExtractRuleInfo):
        self._ExtractRuleInfo = ExtractRuleInfo

    @property
    def TaskType(self):
        """COS导入任务类型。1：一次性导入任务；2：持续性导入任务。
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Metadata(self):
        """元数据。支持 bucket，object。
        :rtype: list of str
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Name = params.get("Name")
        self._Bucket = params.get("Bucket")
        self._BucketRegion = params.get("BucketRegion")
        self._Prefix = params.get("Prefix")
        self._LogType = params.get("LogType")
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Progress = params.get("Progress")
        self._Compress = params.get("Compress")
        if params.get("ExtractRuleInfo") is not None:
            self._ExtractRuleInfo = ExtractRuleInfo()
            self._ExtractRuleInfo._deserialize(params.get("ExtractRuleInfo"))
        self._TaskType = params.get("TaskType")
        self._Metadata = params.get("Metadata")
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
        :param _Name: 通知渠道组名称。
        :type Name: str
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的通知渠道组。最大支持50个标签键值对，并且不能有重复的键值对。
        :type Tags: list of Tag
        :param _Type: 【简易模式】（简易模式/告警模式二选一，分别配置相应参数）
需要发送通知的告警类型。可选值：
- Trigger - 告警触发
- Recovery - 告警恢复
- All - 告警触发和告警恢复
        :type Type: str
        :param _NoticeReceivers: 【简易模式】（简易模式/告警模式二选一，分别配置相应参数）
通知接收对象。
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: 【简易模式】（简易模式/告警模式二选一，分别配置相应参数）
接口回调信息（包括企业微信、钉钉、飞书）。
        :type WebCallbacks: list of WebCallback
        :param _NoticeRules: 【高级模式】（简易模式/告警模式二选一，分别配置相应参数）
通知规则。
        :type NoticeRules: list of NoticeRule
        :param _JumpDomain: 查询数据链接。http:// 或者 https:// 开头，不能/结尾
        :type JumpDomain: str
        :param _DeliverStatus: 投递日志开关。可取值如下：
1：关闭（默认值）；
2：开启 
投递日志开关开启时， DeliverConfig参数必填。
        :type DeliverStatus: int
        :param _DeliverConfig: 投递日志配置参数。当DeliverStatus开启时，必填。
        :type DeliverConfig: :class:`tencentcloud.cls.v20201016.models.DeliverConfig`
        :param _AlarmShieldStatus: 免登录操作告警开关。可取值如下：
-      1：关闭
-      2：开启（默认值）
        :type AlarmShieldStatus: int
        """
        self._Name = None
        self._Tags = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None
        self._NoticeRules = None
        self._JumpDomain = None
        self._DeliverStatus = None
        self._DeliverConfig = None
        self._AlarmShieldStatus = None

    @property
    def Name(self):
        """通知渠道组名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        """标签描述列表，通过指定该参数可以同时绑定标签到相应的通知渠道组。最大支持50个标签键值对，并且不能有重复的键值对。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Type(self):
        """【简易模式】（简易模式/告警模式二选一，分别配置相应参数）
需要发送通知的告警类型。可选值：
- Trigger - 告警触发
- Recovery - 告警恢复
- All - 告警触发和告警恢复
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeReceivers(self):
        """【简易模式】（简易模式/告警模式二选一，分别配置相应参数）
通知接收对象。
        :rtype: list of NoticeReceiver
        """
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        """【简易模式】（简易模式/告警模式二选一，分别配置相应参数）
接口回调信息（包括企业微信、钉钉、飞书）。
        :rtype: list of WebCallback
        """
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks

    @property
    def NoticeRules(self):
        """【高级模式】（简易模式/告警模式二选一，分别配置相应参数）
通知规则。
        :rtype: list of NoticeRule
        """
        return self._NoticeRules

    @NoticeRules.setter
    def NoticeRules(self, NoticeRules):
        self._NoticeRules = NoticeRules

    @property
    def JumpDomain(self):
        """查询数据链接。http:// 或者 https:// 开头，不能/结尾
        :rtype: str
        """
        return self._JumpDomain

    @JumpDomain.setter
    def JumpDomain(self, JumpDomain):
        self._JumpDomain = JumpDomain

    @property
    def DeliverStatus(self):
        """投递日志开关。可取值如下：
1：关闭（默认值）；
2：开启 
投递日志开关开启时， DeliverConfig参数必填。
        :rtype: int
        """
        return self._DeliverStatus

    @DeliverStatus.setter
    def DeliverStatus(self, DeliverStatus):
        self._DeliverStatus = DeliverStatus

    @property
    def DeliverConfig(self):
        """投递日志配置参数。当DeliverStatus开启时，必填。
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeliverConfig`
        """
        return self._DeliverConfig

    @DeliverConfig.setter
    def DeliverConfig(self, DeliverConfig):
        self._DeliverConfig = DeliverConfig

    @property
    def AlarmShieldStatus(self):
        """免登录操作告警开关。可取值如下：
-      1：关闭
-      2：开启（默认值）
        :rtype: int
        """
        return self._AlarmShieldStatus

    @AlarmShieldStatus.setter
    def AlarmShieldStatus(self, AlarmShieldStatus):
        self._AlarmShieldStatus = AlarmShieldStatus


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        if params.get("NoticeRules") is not None:
            self._NoticeRules = []
            for item in params.get("NoticeRules"):
                obj = NoticeRule()
                obj._deserialize(item)
                self._NoticeRules.append(obj)
        self._JumpDomain = params.get("JumpDomain")
        self._DeliverStatus = params.get("DeliverStatus")
        if params.get("DeliverConfig") is not None:
            self._DeliverConfig = DeliverConfig()
            self._DeliverConfig._deserialize(params.get("DeliverConfig"))
        self._AlarmShieldStatus = params.get("AlarmShieldStatus")
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
        :param _AlarmNoticeId: 告警模板ID
        :type AlarmNoticeId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmNoticeId = None
        self._RequestId = None

    @property
    def AlarmNoticeId(self):
        """告警模板ID
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

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
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._RequestId = params.get("RequestId")


class CreateAlarmRequest(AbstractModel):
    """CreateAlarm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 告警策略名称
        :type Name: str
        :param _AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTarget
        :param _MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为2000。
        :type TriggerCount: int
        :param _AlarmPeriod: 告警重复的周期，单位是分钟。取值范围是0~1440。
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param _Condition: 触发条件
 注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。

        :type Condition: str
        :param _AlarmLevel: 告警级别
0:警告(Warn); 1:提醒(Info); 2:紧急 (Critical)。
注意:  
- 不填则默认为0。
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。
        :type AlarmLevel: int
        :param _MultiConditions: 多触发条件
 注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。



        :type MultiConditions: list of MultiCondition
        :param _Status: 是否开启告警策略。
默认值为true
        :type Status: bool
        :param _Enable: 该参数已废弃，请使用Status参数控制是否开启告警策略。
        :type Enable: bool
        :param _MessageTemplate: 用户自定义告警内容
        :type MessageTemplate: str
        :param _CallBack: 用户自定义回调
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: 多维分析
        :type Analysis: list of AnalysisDimensional
        :param _GroupTriggerStatus: 分组触发状态。
默认值false
        :type GroupTriggerStatus: bool
        :param _GroupTriggerCondition: 分组触发条件。
        :type GroupTriggerCondition: list of str
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的告警策略。

最大支持10个标签键值对，并且不能有重复的键值对。
        :type Tags: list of Tag
        :param _MonitorObjectType: 监控对象类型。0:执行语句共用监控对象; 1:每个执行语句单独选择监控对象。 
不填则默认为0。
当值为1时，AlarmTargets元素个数不能超过10个，AlarmTargets中的Number必须是从1开始的连续正整数，不能重复。

        :type MonitorObjectType: int
        :param _Classifications: 告警附加分类信息列表。
Classifications元素个数不能超过20个。
Classifications元素的Key不能为空，不能重复，长度不能超过50个字符，符合正则 `^[a-z]([a-z0-9_]{0,49})$`。
Classifications元素的Value长度不能超过200个字符。
        :type Classifications: list of AlarmClassification
        """
        self._Name = None
        self._AlarmTargets = None
        self._MonitorTime = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._Condition = None
        self._AlarmLevel = None
        self._MultiConditions = None
        self._Status = None
        self._Enable = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None
        self._GroupTriggerStatus = None
        self._GroupTriggerCondition = None
        self._Tags = None
        self._MonitorObjectType = None
        self._Classifications = None

    @property
    def Name(self):
        """告警策略名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmTargets(self):
        """监控对象列表。
        :rtype: list of AlarmTarget
        """
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def MonitorTime(self):
        """监控任务运行时间点。
        :rtype: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        """
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def TriggerCount(self):
        """持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为2000。
        :rtype: int
        """
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        """告警重复的周期，单位是分钟。取值范围是0~1440。
        :rtype: int
        """
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        """关联的告警通知模板列表。
        :rtype: list of str
        """
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def Condition(self):
        """触发条件
 注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。

        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def AlarmLevel(self):
        """告警级别
0:警告(Warn); 1:提醒(Info); 2:紧急 (Critical)。
注意:  
- 不填则默认为0。
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def MultiConditions(self):
        """多触发条件
 注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。



        :rtype: list of MultiCondition
        """
        return self._MultiConditions

    @MultiConditions.setter
    def MultiConditions(self, MultiConditions):
        self._MultiConditions = MultiConditions

    @property
    def Status(self):
        """是否开启告警策略。
默认值为true
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        """该参数已废弃，请使用Status参数控制是否开启告警策略。
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def MessageTemplate(self):
        """用户自定义告警内容
        :rtype: str
        """
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        """用户自定义回调
        :rtype: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        """
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        """多维分析
        :rtype: list of AnalysisDimensional
        """
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def GroupTriggerStatus(self):
        """分组触发状态。
默认值false
        :rtype: bool
        """
        return self._GroupTriggerStatus

    @GroupTriggerStatus.setter
    def GroupTriggerStatus(self, GroupTriggerStatus):
        self._GroupTriggerStatus = GroupTriggerStatus

    @property
    def GroupTriggerCondition(self):
        """分组触发条件。
        :rtype: list of str
        """
        return self._GroupTriggerCondition

    @GroupTriggerCondition.setter
    def GroupTriggerCondition(self, GroupTriggerCondition):
        self._GroupTriggerCondition = GroupTriggerCondition

    @property
    def Tags(self):
        """标签描述列表，通过指定该参数可以同时绑定标签到相应的告警策略。

最大支持10个标签键值对，并且不能有重复的键值对。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MonitorObjectType(self):
        """监控对象类型。0:执行语句共用监控对象; 1:每个执行语句单独选择监控对象。 
不填则默认为0。
当值为1时，AlarmTargets元素个数不能超过10个，AlarmTargets中的Number必须是从1开始的连续正整数，不能重复。

        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def Classifications(self):
        """告警附加分类信息列表。
Classifications元素个数不能超过20个。
Classifications元素的Key不能为空，不能重复，长度不能超过50个字符，符合正则 `^[a-z]([a-z0-9_]{0,49})$`。
Classifications元素的Value长度不能超过200个字符。
        :rtype: list of AlarmClassification
        """
        return self._Classifications

    @Classifications.setter
    def Classifications(self, Classifications):
        self._Classifications = Classifications


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        self._Condition = params.get("Condition")
        self._AlarmLevel = params.get("AlarmLevel")
        if params.get("MultiConditions") is not None:
            self._MultiConditions = []
            for item in params.get("MultiConditions"):
                obj = MultiCondition()
                obj._deserialize(item)
                self._MultiConditions.append(obj)
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        self._GroupTriggerStatus = params.get("GroupTriggerStatus")
        self._GroupTriggerCondition = params.get("GroupTriggerCondition")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._MonitorObjectType = params.get("MonitorObjectType")
        if params.get("Classifications") is not None:
            self._Classifications = []
            for item in params.get("Classifications"):
                obj = AlarmClassification()
                obj._deserialize(item)
                self._Classifications.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmResponse(AbstractModel):
    """CreateAlarm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmId: 告警策略ID。
        :type AlarmId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmId = None
        self._RequestId = None

    @property
    def AlarmId(self):
        """告警策略ID。
        :rtype: str
        """
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

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
        self._AlarmId = params.get("AlarmId")
        self._RequestId = params.get("RequestId")


class CreateAlarmShieldRequest(AbstractModel):
    """CreateAlarmShield请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: 通知渠道组id。
        :type AlarmNoticeId: str
        :param _StartTime: 屏蔽开始时间（秒级时间戳）。
        :type StartTime: int
        :param _EndTime: 屏蔽结束时间（秒级时间戳）。
        :type EndTime: int
        :param _Type: 屏蔽类型。1：屏蔽所有通知，2：按照Rule参数屏蔽匹配规则的通知。
        :type Type: int
        :param _Reason: 屏蔽原因。
        :type Reason: str
        :param _Rule: 屏蔽规则，当Type为2时必填。规则填写方式详见[产品文档](https://cloud.tencent.com/document/product/614/103178#rule)。
        :type Rule: str
        """
        self._AlarmNoticeId = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Reason = None
        self._Rule = None

    @property
    def AlarmNoticeId(self):
        """通知渠道组id。
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def StartTime(self):
        """屏蔽开始时间（秒级时间戳）。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """屏蔽结束时间（秒级时间戳）。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        """屏蔽类型。1：屏蔽所有通知，2：按照Rule参数屏蔽匹配规则的通知。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Reason(self):
        """屏蔽原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Rule(self):
        """屏蔽规则，当Type为2时必填。规则填写方式详见[产品文档](https://cloud.tencent.com/document/product/614/103178#rule)。
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Reason = params.get("Reason")
        self._Rule = params.get("Rule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmShieldResponse(AbstractModel):
    """CreateAlarmShield返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 屏蔽规则ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """屏蔽规则ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateConfigExtraRequest(AbstractModel):
    """CreateConfigExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 采集配置规程名称，最长63个字符，只能包含小写字符、数字及分隔符（“-”），且必须以小写字符开头，数字或小写字符结尾
        :type Name: str
        :param _TopicId: 日志主题id
        :type TopicId: str
        :param _Type: 日志源类型。支持 container_stdout：容器标准输出；container_file：容器文件路径；host_file：节点文件路径。
        :type Type: str
        :param _LogType: 采集的日志类型，默认为minimalist_log。支持以下类型：
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）。
        :type LogType: str
        :param _ConfigFlag: 采集配置标记。
- 目前只支持label_k8s，用于标记自建k8s集群使用的采集配置

        :type ConfigFlag: str
        :param _LogsetId: 日志集id
        :type LogsetId: str
        :param _LogsetName: 日志集name
        :type LogsetName: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _HostFile: 节点文件路径类型配置。
        :type HostFile: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        :param _ContainerFile: 容器文件路径类型配置。
        :type ContainerFile: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        :param _ContainerStdout: 容器标准输出类型配置。
        :type ContainerStdout: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        :param _LogFormat: 日志格式化方式，用于容器采集场景。 - 已废弃
- stdout-docker-json：用于docker容器采集场景
- stdout-containerd：用于containerd容器采集场景
        :type LogFormat: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param _UserDefineRule: 组合解析采集规则，用于复杂场景下的日志采集。
- 取值参考：[使用组合解析提取模式采集日志
](https://cloud.tencent.com/document/product/614/61310)
        :type UserDefineRule: str
        :param _GroupId: 绑定的机器组id
        :type GroupId: str
        :param _GroupIds: 绑定的机器组id列表
        :type GroupIds: list of str
        :param _CollectInfos: 采集相关配置信息。详情见CollectInfo复杂类型配置。
        :type CollectInfos: list of CollectInfo
        :param _AdvancedConfig: 高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
- ClsAgentDefault(自定义默认值，无特殊含义，用于清空其他选项)，建议取值0

        :type AdvancedConfig: str
        """
        self._Name = None
        self._TopicId = None
        self._Type = None
        self._LogType = None
        self._ConfigFlag = None
        self._LogsetId = None
        self._LogsetName = None
        self._TopicName = None
        self._HostFile = None
        self._ContainerFile = None
        self._ContainerStdout = None
        self._LogFormat = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UserDefineRule = None
        self._GroupId = None
        self._GroupIds = None
        self._CollectInfos = None
        self._AdvancedConfig = None

    @property
    def Name(self):
        """采集配置规程名称，最长63个字符，只能包含小写字符、数字及分隔符（“-”），且必须以小写字符开头，数字或小写字符结尾
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicId(self):
        """日志主题id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Type(self):
        """日志源类型。支持 container_stdout：容器标准输出；container_file：容器文件路径；host_file：节点文件路径。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LogType(self):
        """采集的日志类型，默认为minimalist_log。支持以下类型：
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）。
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ConfigFlag(self):
        """采集配置标记。
- 目前只支持label_k8s，用于标记自建k8s集群使用的采集配置

        :rtype: str
        """
        return self._ConfigFlag

    @ConfigFlag.setter
    def ConfigFlag(self, ConfigFlag):
        self._ConfigFlag = ConfigFlag

    @property
    def LogsetId(self):
        """日志集id
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        """日志集name
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicName(self):
        """日志主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def HostFile(self):
        """节点文件路径类型配置。
        :rtype: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        """
        return self._HostFile

    @HostFile.setter
    def HostFile(self, HostFile):
        self._HostFile = HostFile

    @property
    def ContainerFile(self):
        """容器文件路径类型配置。
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        """
        return self._ContainerFile

    @ContainerFile.setter
    def ContainerFile(self, ContainerFile):
        self._ContainerFile = ContainerFile

    @property
    def ContainerStdout(self):
        """容器标准输出类型配置。
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        """
        return self._ContainerStdout

    @ContainerStdout.setter
    def ContainerStdout(self, ContainerStdout):
        self._ContainerStdout = ContainerStdout

    @property
    def LogFormat(self):
        """日志格式化方式，用于容器采集场景。 - 已废弃
- stdout-docker-json：用于docker容器采集场景
- stdout-containerd：用于containerd容器采集场景
        :rtype: str
        """
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def ExtractRule(self):
        """提取规则，如果设置了ExtractRule，则必须设置LogType
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        """采集黑名单路径列表
        :rtype: list of ExcludePathInfo
        """
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UserDefineRule(self):
        """组合解析采集规则，用于复杂场景下的日志采集。
- 取值参考：[使用组合解析提取模式采集日志
](https://cloud.tencent.com/document/product/614/61310)
        :rtype: str
        """
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def GroupId(self):
        """绑定的机器组id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupIds(self):
        """绑定的机器组id列表
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def CollectInfos(self):
        """采集相关配置信息。详情见CollectInfo复杂类型配置。
        :rtype: list of CollectInfo
        """
        return self._CollectInfos

    @CollectInfos.setter
    def CollectInfos(self, CollectInfos):
        self._CollectInfos = CollectInfos

    @property
    def AdvancedConfig(self):
        """高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
- ClsAgentDefault(自定义默认值，无特殊含义，用于清空其他选项)，建议取值0

        :rtype: str
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TopicId = params.get("TopicId")
        self._Type = params.get("Type")
        self._LogType = params.get("LogType")
        self._ConfigFlag = params.get("ConfigFlag")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicName = params.get("TopicName")
        if params.get("HostFile") is not None:
            self._HostFile = HostFileInfo()
            self._HostFile._deserialize(params.get("HostFile"))
        if params.get("ContainerFile") is not None:
            self._ContainerFile = ContainerFileInfo()
            self._ContainerFile._deserialize(params.get("ContainerFile"))
        if params.get("ContainerStdout") is not None:
            self._ContainerStdout = ContainerStdoutInfo()
            self._ContainerStdout._deserialize(params.get("ContainerStdout"))
        self._LogFormat = params.get("LogFormat")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UserDefineRule = params.get("UserDefineRule")
        self._GroupId = params.get("GroupId")
        self._GroupIds = params.get("GroupIds")
        if params.get("CollectInfos") is not None:
            self._CollectInfos = []
            for item in params.get("CollectInfos"):
                obj = CollectInfo()
                obj._deserialize(item)
                self._CollectInfos.append(obj)
        self._AdvancedConfig = params.get("AdvancedConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigExtraResponse(AbstractModel):
    """CreateConfigExtra返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigExtraId: 采集配置扩展信息ID
        :type ConfigExtraId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigExtraId = None
        self._RequestId = None

    @property
    def ConfigExtraId(self):
        """采集配置扩展信息ID
        :rtype: str
        """
        return self._ConfigExtraId

    @ConfigExtraId.setter
    def ConfigExtraId(self, ConfigExtraId):
        self._ConfigExtraId = ConfigExtraId

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
        self._ConfigExtraId = params.get("ConfigExtraId")
        self._RequestId = params.get("RequestId")


class CreateConfigRequest(AbstractModel):
    """CreateConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 采集配置名称
        :type Name: str
        :param _Output: 采集配置所属日志主题ID即TopicId
        :type Output: str
        :param _Path: 日志采集路径，包含文件名，支持多个路径，多个路径之间英文逗号分隔，文件采集情况下必填
        :type Path: str
        :param _LogType: 采集的日志类型，默认为minimalist_log。支持以下类型：
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）；
- service_syslog代表：syslog 采集（详见[采集 Syslog](https://cloud.tencent.com/document/product/614/81454)）；
- windows_event_log代表：Windows事件日志（详见[采集 Windows 事件日志](https://cloud.tencent.com/document/product/614/96678)）。
        :type LogType: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param _UserDefineRule: 用户自定义采集规则，Json格式序列化的字符串。当LogType为user_define_log时，必填。
        :type UserDefineRule: str
        :param _AdvancedConfig: 高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
样例：
`{\"ClsAgentFileTimeout\":0,\"ClsAgentMaxDepth\":10,\"ClsAgentParseFailMerge\":true}`

控制台默认占位值：`{\"ClsAgentDefault\":0}`
        :type AdvancedConfig: str
        """
        self._Name = None
        self._Output = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UserDefineRule = None
        self._AdvancedConfig = None

    @property
    def Name(self):
        """采集配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Output(self):
        """采集配置所属日志主题ID即TopicId
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Path(self):
        """日志采集路径，包含文件名，支持多个路径，多个路径之间英文逗号分隔，文件采集情况下必填
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        """采集的日志类型，默认为minimalist_log。支持以下类型：
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）；
- service_syslog代表：syslog 采集（详见[采集 Syslog](https://cloud.tencent.com/document/product/614/81454)）；
- windows_event_log代表：Windows事件日志（详见[采集 Windows 事件日志](https://cloud.tencent.com/document/product/614/96678)）。
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        """提取规则，如果设置了ExtractRule，则必须设置LogType
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        """采集黑名单路径列表
        :rtype: list of ExcludePathInfo
        """
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UserDefineRule(self):
        """用户自定义采集规则，Json格式序列化的字符串。当LogType为user_define_log时，必填。
        :rtype: str
        """
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def AdvancedConfig(self):
        """高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
样例：
`{\"ClsAgentFileTimeout\":0,\"ClsAgentMaxDepth\":10,\"ClsAgentParseFailMerge\":true}`

控制台默认占位值：`{\"ClsAgentDefault\":0}`
        :rtype: str
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Output = params.get("Output")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UserDefineRule = params.get("UserDefineRule")
        self._AdvancedConfig = params.get("AdvancedConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigResponse(AbstractModel):
    """CreateConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集配置ID
        :type ConfigId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigId = None
        self._RequestId = None

    @property
    def ConfigId(self):
        """采集配置ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

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
        self._ConfigId = params.get("ConfigId")
        self._RequestId = params.get("RequestId")


class CreateConsoleSharingRequest(AbstractModel):
    """CreateConsoleSharing请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SharingConfig: 免密分享配置
        :type SharingConfig: :class:`tencentcloud.cls.v20201016.models.ConsoleSharingConfig`
        """
        self._SharingConfig = None

    @property
    def SharingConfig(self):
        """免密分享配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.ConsoleSharingConfig`
        """
        return self._SharingConfig

    @SharingConfig.setter
    def SharingConfig(self, SharingConfig):
        self._SharingConfig = SharingConfig


    def _deserialize(self, params):
        if params.get("SharingConfig") is not None:
            self._SharingConfig = ConsoleSharingConfig()
            self._SharingConfig._deserialize(params.get("SharingConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsoleSharingResponse(AbstractModel):
    """CreateConsoleSharing返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SharingUrl: 免密分享链接
        :type SharingUrl: str
        :param _SharingId: 免密分享链接ID
        :type SharingId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SharingUrl = None
        self._SharingId = None
        self._RequestId = None

    @property
    def SharingUrl(self):
        """免密分享链接
        :rtype: str
        """
        return self._SharingUrl

    @SharingUrl.setter
    def SharingUrl(self, SharingUrl):
        self._SharingUrl = SharingUrl

    @property
    def SharingId(self):
        """免密分享链接ID
        :rtype: str
        """
        return self._SharingId

    @SharingId.setter
    def SharingId(self, SharingId):
        self._SharingId = SharingId

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
        self._SharingUrl = params.get("SharingUrl")
        self._SharingId = params.get("SharingId")
        self._RequestId = params.get("RequestId")


class CreateConsumerRequest(AbstractModel):
    """CreateConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递任务绑定的日志主题 ID
        :type TopicId: str
        :param _NeedContent: 是否投递日志的元数据信息，默认为 true。
当NeedContent为true时：字段Content有效。
当NeedContent为false时：字段Content无效。
        :type NeedContent: bool
        :param _Content: 如果需要投递元数据信息，元数据信息的描述
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka的描述
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: 投递时压缩方式，取值0，2，3。[0：NONE；2：SNAPPY；3：LZ4]
        :type Compression: int
        """
        self._TopicId = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None

    @property
    def TopicId(self):
        """投递任务绑定的日志主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def NeedContent(self):
        """是否投递日志的元数据信息，默认为 true。
当NeedContent为true时：字段Content有效。
当NeedContent为false时：字段Content无效。
        :rtype: bool
        """
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        """如果需要投递元数据信息，元数据信息的描述
        :rtype: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        """CKafka的描述
        :rtype: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        """
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        """投递时压缩方式，取值0，2，3。[0：NONE；2：SNAPPY；3：LZ4]
        :rtype: int
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerResponse(AbstractModel):
    """CreateConsumer返回参数结构体

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


class CreateCosRechargeRequest(AbstractModel):
    """CreateCosRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题 ID
        :type TopicId: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _Name: 投递任务名称
        :type Name: str
        :param _Bucket: COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。
        :type Bucket: str
        :param _BucketRegion: COS存储桶所在地域，详见产品支持的[地域列表](https://cloud.tencent.com/document/product/436/6224)。
        :type BucketRegion: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表单行全文；
默认为minimalist_log
        :type LogType: str
        :param _Prefix: COS文件所在文件夹的前缀。默认为空，投递存储桶下所有的文件。
        :type Prefix: str
        :param _Compress: supported: "", "gzip", "lzop", "snappy"; 默认空
        :type Compress: str
        :param _ExtractRuleInfo: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRuleInfo: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _TaskType: COS导入任务类型。1：一次性导入任务；2：持续性导入任务。默认为1：一次性导入任务
        :type TaskType: int
        :param _Metadata: 元数据。
        :type Metadata: list of str
        """
        self._TopicId = None
        self._LogsetId = None
        self._Name = None
        self._Bucket = None
        self._BucketRegion = None
        self._LogType = None
        self._Prefix = None
        self._Compress = None
        self._ExtractRuleInfo = None
        self._TaskType = None
        self._Metadata = None

    @property
    def TopicId(self):
        """日志主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Name(self):
        """投递任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Bucket(self):
        """COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def BucketRegion(self):
        """COS存储桶所在地域，详见产品支持的[地域列表](https://cloud.tencent.com/document/product/436/6224)。
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def LogType(self):
        """采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表单行全文；
默认为minimalist_log
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Prefix(self):
        """COS文件所在文件夹的前缀。默认为空，投递存储桶下所有的文件。
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def Compress(self):
        """supported: "", "gzip", "lzop", "snappy"; 默认空
        :rtype: str
        """
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def ExtractRuleInfo(self):
        """提取规则，如果设置了ExtractRule，则必须设置LogType
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRuleInfo

    @ExtractRuleInfo.setter
    def ExtractRuleInfo(self, ExtractRuleInfo):
        self._ExtractRuleInfo = ExtractRuleInfo

    @property
    def TaskType(self):
        """COS导入任务类型。1：一次性导入任务；2：持续性导入任务。默认为1：一次性导入任务
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Metadata(self):
        """元数据。
        :rtype: list of str
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Name = params.get("Name")
        self._Bucket = params.get("Bucket")
        self._BucketRegion = params.get("BucketRegion")
        self._LogType = params.get("LogType")
        self._Prefix = params.get("Prefix")
        self._Compress = params.get("Compress")
        if params.get("ExtractRuleInfo") is not None:
            self._ExtractRuleInfo = ExtractRuleInfo()
            self._ExtractRuleInfo._deserialize(params.get("ExtractRuleInfo"))
        self._TaskType = params.get("TaskType")
        self._Metadata = params.get("Metadata")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosRechargeResponse(AbstractModel):
    """CreateCosRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: COS导入任务id
        :type Id: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """COS导入任务id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateDashboardSubscribeRequest(AbstractModel):
    """CreateDashboardSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 仪表盘订阅名称。
        :type Name: str
        :param _DashboardId: 仪表盘id。
        :type DashboardId: str
        :param _Cron: 订阅时间cron表达式，格式为：{秒数} {分钟} {小时} {日期} {月份} {星期}；（有效数据为：{分钟} {小时} {日期} {月份} {星期}）。<br><li/>{秒数} 取值范围： 0 ~ 59 <br><li/>{分钟} 取值范围： 0 ~ 59  <br><li/>{小时} 取值范围： 0 ~ 23  <br><li/>{日期} 取值范围： 1 ~ 31 AND (dayOfMonth最后一天： L) <br><li/>{月份} 取值范围： 1 ~ 12 <br><li/>{星期} 取值范围： 0 ~ 6 【0:星期日， 6星期六】
        :type Cron: str
        :param _SubscribeData: 仪表盘订阅数据。
        :type SubscribeData: :class:`tencentcloud.cls.v20201016.models.DashboardSubscribeData`
        """
        self._Name = None
        self._DashboardId = None
        self._Cron = None
        self._SubscribeData = None

    @property
    def Name(self):
        """仪表盘订阅名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DashboardId(self):
        """仪表盘id。
        :rtype: str
        """
        return self._DashboardId

    @DashboardId.setter
    def DashboardId(self, DashboardId):
        self._DashboardId = DashboardId

    @property
    def Cron(self):
        """订阅时间cron表达式，格式为：{秒数} {分钟} {小时} {日期} {月份} {星期}；（有效数据为：{分钟} {小时} {日期} {月份} {星期}）。<br><li/>{秒数} 取值范围： 0 ~ 59 <br><li/>{分钟} 取值范围： 0 ~ 59  <br><li/>{小时} 取值范围： 0 ~ 23  <br><li/>{日期} 取值范围： 1 ~ 31 AND (dayOfMonth最后一天： L) <br><li/>{月份} 取值范围： 1 ~ 12 <br><li/>{星期} 取值范围： 0 ~ 6 【0:星期日， 6星期六】
        :rtype: str
        """
        return self._Cron

    @Cron.setter
    def Cron(self, Cron):
        self._Cron = Cron

    @property
    def SubscribeData(self):
        """仪表盘订阅数据。
        :rtype: :class:`tencentcloud.cls.v20201016.models.DashboardSubscribeData`
        """
        return self._SubscribeData

    @SubscribeData.setter
    def SubscribeData(self, SubscribeData):
        self._SubscribeData = SubscribeData


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DashboardId = params.get("DashboardId")
        self._Cron = params.get("Cron")
        if params.get("SubscribeData") is not None:
            self._SubscribeData = DashboardSubscribeData()
            self._SubscribeData._deserialize(params.get("SubscribeData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDashboardSubscribeResponse(AbstractModel):
    """CreateDashboardSubscribe返回参数结构体

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


class CreateDataTransformRequest(AbstractModel):
    """CreateDataTransform请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FuncType: 任务类型. 1: 指定主题；2:动态创建。详情请参考[创建加工任务文档](https://cloud.tencent.com/document/product/614/63940)。
        :type FuncType: int
        :param _SrcTopicId: 源日志主题
        :type SrcTopicId: str
        :param _Name: 加工任务名称
        :type Name: str
        :param _EtlContent: 加工语句。 当FuncType为2时，EtlContent必须使用[log_auto_output](https://cloud.tencent.com/document/product/614/70733#b3c58797-4825-4807-bef4-68106e25024f) 

其他参考文档：

- [创建加工任务](https://cloud.tencent.com/document/product/614/63940) 
-  [函数总览](https://cloud.tencent.com/document/product/614/70395)
        :type EtlContent: str
        :param _TaskType: 加工类型。
1：使用源日志主题中的随机数据，进行加工预览；2：使用用户自定义测试数据，进行加工预览；3：创建真实加工任务。
        :type TaskType: int
        :param _DstResources: 加工任务目的topic_id以及别名,当FuncType=1时，该参数必填，当FuncType=2时，无需填写。
        :type DstResources: list of DataTransformResouceInfo
        :param _EnableFlag: 任务启动状态.   默认为1:开启,  2:关闭
        :type EnableFlag: int
        :param _PreviewLogStatistics: 用于预览加工结果的测试数据
        :type PreviewLogStatistics: list of PreviewLogStatistic
        :param _DataTransformType: 数据加工类型。0：标准加工任务； 1：前置加工任务。前置加工任务将采集的日志处理完成后，再写入日志主题。
        :type DataTransformType: int
        """
        self._FuncType = None
        self._SrcTopicId = None
        self._Name = None
        self._EtlContent = None
        self._TaskType = None
        self._DstResources = None
        self._EnableFlag = None
        self._PreviewLogStatistics = None
        self._DataTransformType = None

    @property
    def FuncType(self):
        """任务类型. 1: 指定主题；2:动态创建。详情请参考[创建加工任务文档](https://cloud.tencent.com/document/product/614/63940)。
        :rtype: int
        """
        return self._FuncType

    @FuncType.setter
    def FuncType(self, FuncType):
        self._FuncType = FuncType

    @property
    def SrcTopicId(self):
        """源日志主题
        :rtype: str
        """
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def Name(self):
        """加工任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EtlContent(self):
        """加工语句。 当FuncType为2时，EtlContent必须使用[log_auto_output](https://cloud.tencent.com/document/product/614/70733#b3c58797-4825-4807-bef4-68106e25024f) 

其他参考文档：

- [创建加工任务](https://cloud.tencent.com/document/product/614/63940) 
-  [函数总览](https://cloud.tencent.com/document/product/614/70395)
        :rtype: str
        """
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent

    @property
    def TaskType(self):
        """加工类型。
1：使用源日志主题中的随机数据，进行加工预览；2：使用用户自定义测试数据，进行加工预览；3：创建真实加工任务。
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def DstResources(self):
        """加工任务目的topic_id以及别名,当FuncType=1时，该参数必填，当FuncType=2时，无需填写。
        :rtype: list of DataTransformResouceInfo
        """
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources

    @property
    def EnableFlag(self):
        """任务启动状态.   默认为1:开启,  2:关闭
        :rtype: int
        """
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def PreviewLogStatistics(self):
        """用于预览加工结果的测试数据
        :rtype: list of PreviewLogStatistic
        """
        return self._PreviewLogStatistics

    @PreviewLogStatistics.setter
    def PreviewLogStatistics(self, PreviewLogStatistics):
        self._PreviewLogStatistics = PreviewLogStatistics

    @property
    def DataTransformType(self):
        """数据加工类型。0：标准加工任务； 1：前置加工任务。前置加工任务将采集的日志处理完成后，再写入日志主题。
        :rtype: int
        """
        return self._DataTransformType

    @DataTransformType.setter
    def DataTransformType(self, DataTransformType):
        self._DataTransformType = DataTransformType


    def _deserialize(self, params):
        self._FuncType = params.get("FuncType")
        self._SrcTopicId = params.get("SrcTopicId")
        self._Name = params.get("Name")
        self._EtlContent = params.get("EtlContent")
        self._TaskType = params.get("TaskType")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        self._EnableFlag = params.get("EnableFlag")
        if params.get("PreviewLogStatistics") is not None:
            self._PreviewLogStatistics = []
            for item in params.get("PreviewLogStatistics"):
                obj = PreviewLogStatistic()
                obj._deserialize(item)
                self._PreviewLogStatistics.append(obj)
        self._DataTransformType = params.get("DataTransformType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataTransformResponse(AbstractModel):
    """CreateDataTransform返回参数结构体

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
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateDeliverCloudFunctionRequest(AbstractModel):
    """CreateDeliverCloudFunction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递规则属于的 topic id
        :type TopicId: str
        :param _FunctionName: 投递的云函数名字。仅支持[事件函数](https://cloud.tencent.com/document/product/583/9694#scf-.E4.BA.8B.E4.BB.B6.E5.87.BD.E6.95.B0) （[函数类型选型](https://cloud.tencent.com/document/product/583/73483)）
        :type FunctionName: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Qualifier: 函数版本
        :type Qualifier: str
        :param _Timeout: 投递最长等待时间，单位：秒
        :type Timeout: int
        :param _MaxMsgNum: 投递最大消息数
        :type MaxMsgNum: int
        """
        self._TopicId = None
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None
        self._Timeout = None
        self._MaxMsgNum = None

    @property
    def TopicId(self):
        """投递规则属于的 topic id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def FunctionName(self):
        """投递的云函数名字。仅支持[事件函数](https://cloud.tencent.com/document/product/583/9694#scf-.E4.BA.8B.E4.BB.B6.E5.87.BD.E6.95.B0) （[函数类型选型](https://cloud.tencent.com/document/product/583/73483)）
        :rtype: str
        """
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        """命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        """函数版本
        :rtype: str
        """
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Timeout(self):
        """投递最长等待时间，单位：秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def MaxMsgNum(self):
        """投递最大消息数
        :rtype: int
        """
        return self._MaxMsgNum

    @MaxMsgNum.setter
    def MaxMsgNum(self, MaxMsgNum):
        self._MaxMsgNum = MaxMsgNum


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        self._Timeout = params.get("Timeout")
        self._MaxMsgNum = params.get("MaxMsgNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeliverCloudFunctionResponse(AbstractModel):
    """CreateDeliverCloudFunction返回参数结构体

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


class CreateExportRequest(AbstractModel):
    """CreateExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Count: 日志导出数量,  最大值5000万
        :type Count: int
        :param _Query: 日志导出检索语句，不支持<a href="https://cloud.tencent.com/document/product/614/44061" target="_blank">[SQL语句]</a>
        :type Query: str
        :param _From: 日志导出起始时间，毫秒时间戳
        :type From: int
        :param _To: 日志导出结束时间，毫秒时间戳
        :type To: int
        :param _Order: 日志导出时间排序。desc，asc，默认为desc
        :type Order: str
        :param _Format: 日志导出数据格式。json，csv，默认为json
        :type Format: str
        :param _SyntaxRule: 语法规则,  默认值为0。
0：Lucene语法，1：CQL语法。
        :type SyntaxRule: int
        :param _DerivedFields: 导出字段
        :type DerivedFields: list of str
        """
        self._TopicId = None
        self._Count = None
        self._Query = None
        self._From = None
        self._To = None
        self._Order = None
        self._Format = None
        self._SyntaxRule = None
        self._DerivedFields = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Count(self):
        """日志导出数量,  最大值5000万
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Query(self):
        """日志导出检索语句，不支持<a href="https://cloud.tencent.com/document/product/614/44061" target="_blank">[SQL语句]</a>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def From(self):
        """日志导出起始时间，毫秒时间戳
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """日志导出结束时间，毫秒时间戳
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Order(self):
        """日志导出时间排序。desc，asc，默认为desc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Format(self):
        """日志导出数据格式。json，csv，默认为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def SyntaxRule(self):
        """语法规则,  默认值为0。
0：Lucene语法，1：CQL语法。
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule

    @property
    def DerivedFields(self):
        """导出字段
        :rtype: list of str
        """
        return self._DerivedFields

    @DerivedFields.setter
    def DerivedFields(self, DerivedFields):
        self._DerivedFields = DerivedFields


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Count = params.get("Count")
        self._Query = params.get("Query")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Order = params.get("Order")
        self._Format = params.get("Format")
        self._SyntaxRule = params.get("SyntaxRule")
        self._DerivedFields = params.get("DerivedFields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExportResponse(AbstractModel):
    """CreateExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportId: 日志导出ID。
        :type ExportId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExportId = None
        self._RequestId = None

    @property
    def ExportId(self):
        """日志导出ID。
        :rtype: str
        """
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

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
        self._ExportId = params.get("ExportId")
        self._RequestId = params.get("RequestId")


class CreateIndexRequest(AbstractModel):
    """CreateIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Rule: 索引规则
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _Status: 是否生效，默认为true
        :type Status: bool
        :param _IncludeInternalFields: 内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引，默认为false，推荐设置为true
* false:不包含
* true:包含
        :type IncludeInternalFields: bool
        :param _MetadataFlag: 元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引，默认为0，推荐设置为1
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
        :type MetadataFlag: int
        """
        self._TopicId = None
        self._Rule = None
        self._Status = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Rule(self):
        """索引规则
        :rtype: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Status(self):
        """是否生效，默认为true
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IncludeInternalFields(self):
        """内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引，默认为false，推荐设置为true
* false:不包含
* true:包含
        :rtype: bool
        """
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        """元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引，默认为0，推荐设置为1
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
        :rtype: int
        """
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._Status = params.get("Status")
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    """CreateIndex返回参数结构体

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


class CreateKafkaRechargeRequest(AbstractModel):
    """CreateKafkaRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 导入CLS目标topic ID
        :type TopicId: str
        :param _Name: Kafka导入配置名称
        :type Name: str
        :param _KafkaType: 导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
        :type KafkaType: int
        :param _UserKafkaTopics: 用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :type UserKafkaTopics: str
        :param _Offset: 导入数据位置，-2:最早（默认），-1：最晚
        :type Offset: int
        :param _LogRechargeRule: 日志导入规则。
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        :param _KafkaInstance: 腾讯云CKafka实例ID，KafkaType为0时必填。
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址，KafkaType为1时必填。
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接，KafkaType为1时必填。
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议。
KafkaType为1并且IsEncryptionAddr为true时Protocol必填。
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _ConsumerGroupName: 用户Kafka消费组名称
        :type ConsumerGroupName: str
        """
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._UserKafkaTopics = None
        self._Offset = None
        self._LogRechargeRule = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._ConsumerGroupName = None

    @property
    def TopicId(self):
        """导入CLS目标topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        """Kafka导入配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        """导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
        :rtype: int
        """
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def UserKafkaTopics(self):
        """用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :rtype: str
        """
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def Offset(self):
        """导入数据位置，-2:最早（默认），-1：最晚
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def LogRechargeRule(self):
        """日志导入规则。
        :rtype: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule

    @property
    def KafkaInstance(self):
        """腾讯云CKafka实例ID，KafkaType为0时必填。
        :rtype: str
        """
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        """服务地址，KafkaType为1时必填。
        :rtype: str
        """
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        """ServerAddr是否为加密连接，KafkaType为1时必填。
        :rtype: bool
        """
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        """加密访问协议。
KafkaType为1并且IsEncryptionAddr为true时Protocol必填。
        :rtype: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ConsumerGroupName(self):
        """用户Kafka消费组名称
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._Offset = params.get("Offset")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKafkaRechargeResponse(AbstractModel):
    """CreateKafkaRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Kafka导入配置ID
        :type Id: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """Kafka导入配置ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateLogsetRequest(AbstractModel):
    """CreateLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetName: 日志集名字，不能重名
        :type LogsetName: str
        :param _Tags: 标签描述列表。最大支持10个标签键值对，并且不能有重复的键值对
        :type Tags: list of Tag
        """
        self._LogsetName = None
        self._Tags = None

    @property
    def LogsetName(self):
        """日志集名字，不能重名
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def Tags(self):
        """标签描述列表。最大支持10个标签键值对，并且不能有重复的键值对
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._LogsetName = params.get("LogsetName")
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
        


class CreateLogsetResponse(AbstractModel):
    """CreateLogset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogsetId = None
        self._RequestId = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

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
        self._LogsetId = params.get("LogsetId")
        self._RequestId = params.get("RequestId")


class CreateMachineGroupRequest(AbstractModel):
    """CreateMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 机器组名字，不能重复
        :type GroupName: str
        :param _MachineGroupType: 创建机器组类型。取值如下：
- Type：ip，Values中为ip字符串列表创建机器组
- Type：label，Values中为标签字符串列表创建机器组
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的机器组。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :type Tags: list of Tag
        :param _AutoUpdate: 是否开启机器组自动更新。默认false
        :type AutoUpdate: bool
        :param _UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
        :type UpdateStartTime: str
        :param _UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
        :type UpdateEndTime: str
        :param _ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费。默认false
        :type ServiceLogging: bool
        :param _DelayCleanupTime: 机器组中机器离线清理时间。单位：天
        :type DelayCleanupTime: int
        :param _MetaTags: 机器组元数据信息列表
        :type MetaTags: list of MetaTagInfo
        :param _OSType: 系统类型，取值如下：
- 0：Linux （默认值）
- 1：Windows
        :type OSType: int
        """
        self._GroupName = None
        self._MachineGroupType = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._DelayCleanupTime = None
        self._MetaTags = None
        self._OSType = None

    @property
    def GroupName(self):
        """机器组名字，不能重复
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        """创建机器组类型。取值如下：
- Type：ip，Values中为ip字符串列表创建机器组
- Type：label，Values中为标签字符串列表创建机器组
        :rtype: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

    @property
    def Tags(self):
        """标签描述列表，通过指定该参数可以同时绑定标签到相应的机器组。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        """是否开启机器组自动更新。默认false
        :rtype: bool
        """
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        """升级开始时间，建议业务低峰期升级LogListener
        :rtype: str
        """
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        """升级结束时间，建议业务低峰期升级LogListener
        :rtype: str
        """
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        """是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费。默认false
        :rtype: bool
        """
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def DelayCleanupTime(self):
        """机器组中机器离线清理时间。单位：天
        :rtype: int
        """
        return self._DelayCleanupTime

    @DelayCleanupTime.setter
    def DelayCleanupTime(self, DelayCleanupTime):
        self._DelayCleanupTime = DelayCleanupTime

    @property
    def MetaTags(self):
        """机器组元数据信息列表
        :rtype: list of MetaTagInfo
        """
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags

    @property
    def OSType(self):
        """系统类型，取值如下：
- 0：Linux （默认值）
- 1：Windows
        :rtype: int
        """
        return self._OSType

    @OSType.setter
    def OSType(self, OSType):
        self._OSType = OSType


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        self._DelayCleanupTime = params.get("DelayCleanupTime")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        self._OSType = params.get("OSType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMachineGroupResponse(AbstractModel):
    """CreateMachineGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateNoticeContentRequest(AbstractModel):
    """CreateNoticeContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 模板名称。
        :type Name: str
        :param _Type: 模板内容语言。0：中文1：英文
        :type Type: int
        :param _NoticeContents: 模板详细配置。
        :type NoticeContents: list of NoticeContent
        """
        self._Name = None
        self._Type = None
        self._NoticeContents = None

    @property
    def Name(self):
        """模板名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """模板内容语言。0：中文1：英文
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeContents(self):
        """模板详细配置。
        :rtype: list of NoticeContent
        """
        return self._NoticeContents

    @NoticeContents.setter
    def NoticeContents(self, NoticeContents):
        self._NoticeContents = NoticeContents


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeContents") is not None:
            self._NoticeContents = []
            for item in params.get("NoticeContents"):
                obj = NoticeContent()
                obj._deserialize(item)
                self._NoticeContents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNoticeContentResponse(AbstractModel):
    """CreateNoticeContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeContentId: 通知内容配置ID
        :type NoticeContentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NoticeContentId = None
        self._RequestId = None

    @property
    def NoticeContentId(self):
        """通知内容配置ID
        :rtype: str
        """
        return self._NoticeContentId

    @NoticeContentId.setter
    def NoticeContentId(self, NoticeContentId):
        self._NoticeContentId = NoticeContentId

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
        self._NoticeContentId = params.get("NoticeContentId")
        self._RequestId = params.get("RequestId")


class CreateScheduledSqlRequest(AbstractModel):
    """CreateScheduledSql请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcTopicId: 源日志主题
        :type SrcTopicId: str
        :param _Name: 任务名称
        :type Name: str
        :param _EnableFlag: 任务启动状态.  1开启,  2关闭
        :type EnableFlag: int
        :param _DstResource: 定时SQL分析目标日志主题
        :type DstResource: :class:`tencentcloud.cls.v20201016.models.ScheduledSqlResouceInfo`
        :param _ScheduledSqlContent: 查询语句
        :type ScheduledSqlContent: str
        :param _ProcessStartTime: 调度开始时间,Unix时间戳，单位ms
        :type ProcessStartTime: int
        :param _ProcessType: 调度类型，1:持续运行 2:指定时间范围
        :type ProcessType: int
        :param _ProcessPeriod: 调度周期(分钟)
        :type ProcessPeriod: int
        :param _ProcessTimeWindow: 单次查询的时间窗口,如果您的目标主题为指标主题，建议该参数的大小不超过30分钟，否则可能转指标失败。 
        :type ProcessTimeWindow: str
        :param _ProcessDelay: 执行延迟(秒)
        :type ProcessDelay: int
        :param _SrcTopicRegion: 源topicId的地域信息
        :type SrcTopicRegion: str
        :param _ProcessEndTime: 调度结束时间，当ProcessType=2时为必传字段, Unix时间戳，单位ms
        :type ProcessEndTime: int
        :param _SyntaxRule: 查询语法规则。 默认值为0。0：Lucene语法，1：CQL语法  
        :type SyntaxRule: int
        """
        self._SrcTopicId = None
        self._Name = None
        self._EnableFlag = None
        self._DstResource = None
        self._ScheduledSqlContent = None
        self._ProcessStartTime = None
        self._ProcessType = None
        self._ProcessPeriod = None
        self._ProcessTimeWindow = None
        self._ProcessDelay = None
        self._SrcTopicRegion = None
        self._ProcessEndTime = None
        self._SyntaxRule = None

    @property
    def SrcTopicId(self):
        """源日志主题
        :rtype: str
        """
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnableFlag(self):
        """任务启动状态.  1开启,  2关闭
        :rtype: int
        """
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def DstResource(self):
        """定时SQL分析目标日志主题
        :rtype: :class:`tencentcloud.cls.v20201016.models.ScheduledSqlResouceInfo`
        """
        return self._DstResource

    @DstResource.setter
    def DstResource(self, DstResource):
        self._DstResource = DstResource

    @property
    def ScheduledSqlContent(self):
        """查询语句
        :rtype: str
        """
        return self._ScheduledSqlContent

    @ScheduledSqlContent.setter
    def ScheduledSqlContent(self, ScheduledSqlContent):
        self._ScheduledSqlContent = ScheduledSqlContent

    @property
    def ProcessStartTime(self):
        """调度开始时间,Unix时间戳，单位ms
        :rtype: int
        """
        return self._ProcessStartTime

    @ProcessStartTime.setter
    def ProcessStartTime(self, ProcessStartTime):
        self._ProcessStartTime = ProcessStartTime

    @property
    def ProcessType(self):
        """调度类型，1:持续运行 2:指定时间范围
        :rtype: int
        """
        return self._ProcessType

    @ProcessType.setter
    def ProcessType(self, ProcessType):
        self._ProcessType = ProcessType

    @property
    def ProcessPeriod(self):
        """调度周期(分钟)
        :rtype: int
        """
        return self._ProcessPeriod

    @ProcessPeriod.setter
    def ProcessPeriod(self, ProcessPeriod):
        self._ProcessPeriod = ProcessPeriod

    @property
    def ProcessTimeWindow(self):
        """单次查询的时间窗口,如果您的目标主题为指标主题，建议该参数的大小不超过30分钟，否则可能转指标失败。 
        :rtype: str
        """
        return self._ProcessTimeWindow

    @ProcessTimeWindow.setter
    def ProcessTimeWindow(self, ProcessTimeWindow):
        self._ProcessTimeWindow = ProcessTimeWindow

    @property
    def ProcessDelay(self):
        """执行延迟(秒)
        :rtype: int
        """
        return self._ProcessDelay

    @ProcessDelay.setter
    def ProcessDelay(self, ProcessDelay):
        self._ProcessDelay = ProcessDelay

    @property
    def SrcTopicRegion(self):
        """源topicId的地域信息
        :rtype: str
        """
        return self._SrcTopicRegion

    @SrcTopicRegion.setter
    def SrcTopicRegion(self, SrcTopicRegion):
        self._SrcTopicRegion = SrcTopicRegion

    @property
    def ProcessEndTime(self):
        """调度结束时间，当ProcessType=2时为必传字段, Unix时间戳，单位ms
        :rtype: int
        """
        return self._ProcessEndTime

    @ProcessEndTime.setter
    def ProcessEndTime(self, ProcessEndTime):
        self._ProcessEndTime = ProcessEndTime

    @property
    def SyntaxRule(self):
        """查询语法规则。 默认值为0。0：Lucene语法，1：CQL语法  
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._SrcTopicId = params.get("SrcTopicId")
        self._Name = params.get("Name")
        self._EnableFlag = params.get("EnableFlag")
        if params.get("DstResource") is not None:
            self._DstResource = ScheduledSqlResouceInfo()
            self._DstResource._deserialize(params.get("DstResource"))
        self._ScheduledSqlContent = params.get("ScheduledSqlContent")
        self._ProcessStartTime = params.get("ProcessStartTime")
        self._ProcessType = params.get("ProcessType")
        self._ProcessPeriod = params.get("ProcessPeriod")
        self._ProcessTimeWindow = params.get("ProcessTimeWindow")
        self._ProcessDelay = params.get("ProcessDelay")
        self._SrcTopicRegion = params.get("SrcTopicRegion")
        self._ProcessEndTime = params.get("ProcessEndTime")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScheduledSqlResponse(AbstractModel):
    """CreateScheduledSql返回参数结构体

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
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateShipperRequest(AbstractModel):
    """CreateShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 创建的投递规则所属的日志主题ID
        :type TopicId: str
        :param _Bucket: COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。
        :type Bucket: str
        :param _Prefix: 投递规则投递的新的目录前缀。
- 仅支持0-9A-Za-z-_/
- 最大支持256个字符
        :type Prefix: str
        :param _ShipperName: 投递规则的名字
        :type ShipperName: str
        :param _Interval: 投递的时间间隔，单位 秒，默认300，范围 300-900
        :type Interval: int
        :param _MaxSize: 投递的文件的最大值，单位 MB，默认256，范围 5-256
        :type MaxSize: int
        :param _FilterRules: 投递日志的过滤规则，匹配的日志进行投递，各rule之间是and关系，最多5个，数组为空则表示不过滤而全部投递
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param _Compress: 投递日志的压缩配置
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: 投递日志的内容格式配置
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _FilenameMode: 投递文件命名配置，0：随机数命名，1：投递时间命名，默认0（随机数命名）
        :type FilenameMode: int
        :param _StartTime: 投递数据范围的开始时间点（秒级时间戳），不能超出日志主题的生命周期起点。
如果用户不填写，默认为用户新建投递任务的时间。
        :type StartTime: int
        :param _EndTime: 投递数据范围的结束时间点（秒级时间戳），不能填写未来时间。
如果用户不填写，默认为持续投递，即无限。
        :type EndTime: int
        :param _StorageType: cos桶存储类型。支持：STANDARD_IA、ARCHIVE、DEEP_ARCHIVE、STANDARD、MAZ_STANDARD、MAZ_STANDARD_IA、INTELLIGENT_TIERING。

1. STANDARD_IA：低频存储；
2. ARCHIVE：归档存储；
3. DEEP_ARCHIVE：深度归档存储；
4. STANDARD：标准存储；
5. MAZ_STANDARD：标准存储（多 AZ）；
6. MAZ_STANDARD_IA：低频存储（多 AZ）；
7. INTELLIGENT_TIERING：智能分层存储。
        :type StorageType: str
        """
        self._TopicId = None
        self._Bucket = None
        self._Prefix = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._FilenameMode = None
        self._StartTime = None
        self._EndTime = None
        self._StorageType = None

    @property
    def TopicId(self):
        """创建的投递规则所属的日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Bucket(self):
        """COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        """投递规则投递的新的目录前缀。
- 仅支持0-9A-Za-z-_/
- 最大支持256个字符
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def ShipperName(self):
        """投递规则的名字
        :rtype: str
        """
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        """投递的时间间隔，单位 秒，默认300，范围 300-900
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        """投递的文件的最大值，单位 MB，默认256，范围 5-256
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def FilterRules(self):
        """投递日志的过滤规则，匹配的日志进行投递，各rule之间是and关系，最多5个，数组为空则表示不过滤而全部投递
        :rtype: list of FilterRuleInfo
        """
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        """投递日志的分区规则，支持strftime的时间格式表示
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        """投递日志的压缩配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        """
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        """投递日志的内容格式配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FilenameMode(self):
        """投递文件命名配置，0：随机数命名，1：投递时间命名，默认0（随机数命名）
        :rtype: int
        """
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode

    @property
    def StartTime(self):
        """投递数据范围的开始时间点（秒级时间戳），不能超出日志主题的生命周期起点。
如果用户不填写，默认为用户新建投递任务的时间。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """投递数据范围的结束时间点（秒级时间戳），不能填写未来时间。
如果用户不填写，默认为持续投递，即无限。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StorageType(self):
        """cos桶存储类型。支持：STANDARD_IA、ARCHIVE、DEEP_ARCHIVE、STANDARD、MAZ_STANDARD、MAZ_STANDARD_IA、INTELLIGENT_TIERING。

1. STANDARD_IA：低频存储；
2. ARCHIVE：归档存储；
3. DEEP_ARCHIVE：深度归档存储；
4. STANDARD：标准存储；
5. MAZ_STANDARD：标准存储（多 AZ）；
6. MAZ_STANDARD_IA：低频存储（多 AZ）；
7. INTELLIGENT_TIERING：智能分层存储。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._FilenameMode = params.get("FilenameMode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShipperResponse(AbstractModel):
    """CreateShipper返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递任务ID
        :type ShipperId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ShipperId = None
        self._RequestId = None

    @property
    def ShipperId(self):
        """投递任务ID
        :rtype: str
        """
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

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
        self._ShipperId = params.get("ShipperId")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _PartitionCount: 日志主题分区个数。默认创建1个，最大支持创建10个分区。
        :type PartitionCount: int
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :type Tags: list of Tag
        :param _AutoSplit: 是否开启自动分裂，默认值为true
        :type AutoSplit: bool
        :param _MaxSplitPartitions: 开启自动分裂后，每个主题能够允许的最大分区数，默认值为50
        :type MaxSplitPartitions: int
        :param _StorageType: 日志主题的存储类型，可选值 hot（标准存储），cold（低频存储）；默认为hot。
        :type StorageType: str
        :param _Period: 存储时间，单位天。
- 日志接入标准存储时，支持1至3600天，值为3640时代表永久保存。
- 日志接入低频存储时，支持7至3600天，值为3640时代表永久保存。
        :type Period: int
        :param _Describes: 日志主题描述
        :type Describes: str
        :param _HotPeriod: 0：关闭日志沉降。
非0：开启日志沉降后标准存储的天数，HotPeriod需要大于等于7，且小于Period。
仅在StorageType为 hot 时生效。
        :type HotPeriod: int
        :param _TopicId: 主题自定义ID，格式为：用户自定义部分-APPID。未填写该参数时将自动生成ID。
- 用户自定义部分仅支持小写字母、数字和-，且不能以-开头和结尾，长度为3至40字符
- APPID可在https://console.cloud.tencent.com/developer页面查询
        :type TopicId: str
        :param _IsWebTracking: 免鉴权开关。 false：关闭； true：开启。默认为false。
开启后将支持指定操作匿名访问该日志主题。详情请参见[日志主题](https://cloud.tencent.com/document/product/614/41035)。
        :type IsWebTracking: bool
        :param _Extends: 日志主题扩展信息
        :type Extends: :class:`tencentcloud.cls.v20201016.models.TopicExtendInfo`
        """
        self._LogsetId = None
        self._TopicName = None
        self._PartitionCount = None
        self._Tags = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._StorageType = None
        self._Period = None
        self._Describes = None
        self._HotPeriod = None
        self._TopicId = None
        self._IsWebTracking = None
        self._Extends = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicName(self):
        """日志主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionCount(self):
        """日志主题分区个数。默认创建1个，最大支持创建10个分区。
        :rtype: int
        """
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def Tags(self):
        """标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，同一个资源只能绑定到同一个标签键下。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoSplit(self):
        """是否开启自动分裂，默认值为true
        :rtype: bool
        """
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        """开启自动分裂后，每个主题能够允许的最大分区数，默认值为50
        :rtype: int
        """
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def StorageType(self):
        """日志主题的存储类型，可选值 hot（标准存储），cold（低频存储）；默认为hot。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Period(self):
        """存储时间，单位天。
- 日志接入标准存储时，支持1至3600天，值为3640时代表永久保存。
- 日志接入低频存储时，支持7至3600天，值为3640时代表永久保存。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Describes(self):
        """日志主题描述
        :rtype: str
        """
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        """0：关闭日志沉降。
非0：开启日志沉降后标准存储的天数，HotPeriod需要大于等于7，且小于Period。
仅在StorageType为 hot 时生效。
        :rtype: int
        """
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod

    @property
    def TopicId(self):
        """主题自定义ID，格式为：用户自定义部分-APPID。未填写该参数时将自动生成ID。
- 用户自定义部分仅支持小写字母、数字和-，且不能以-开头和结尾，长度为3至40字符
- APPID可在https://console.cloud.tencent.com/developer页面查询
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def IsWebTracking(self):
        """免鉴权开关。 false：关闭； true：开启。默认为false。
开启后将支持指定操作匿名访问该日志主题。详情请参见[日志主题](https://cloud.tencent.com/document/product/614/41035)。
        :rtype: bool
        """
        return self._IsWebTracking

    @IsWebTracking.setter
    def IsWebTracking(self, IsWebTracking):
        self._IsWebTracking = IsWebTracking

    @property
    def Extends(self):
        """日志主题扩展信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.TopicExtendInfo`
        """
        return self._Extends

    @Extends.setter
    def Extends(self, Extends):
        self._Extends = Extends


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicName = params.get("TopicName")
        self._PartitionCount = params.get("PartitionCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._StorageType = params.get("StorageType")
        self._Period = params.get("Period")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        self._TopicId = params.get("TopicId")
        self._IsWebTracking = params.get("IsWebTracking")
        if params.get("Extends") is not None:
            self._Extends = TopicExtendInfo()
            self._Extends._deserialize(params.get("Extends"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

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
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class CreateWebCallbackRequest(AbstractModel):
    """CreateWebCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 通知内容名称。
        :type Name: str
        :param _Type: 渠道类型。

WeCom:企业微信;DingTalk:钉钉;Lark:飞书;Http:自定义回调。
        :type Type: str
        :param _Webhook: Webhook地址。
        :type Webhook: str
        :param _Method: 请求方式。 支持POST、PUT。

当Type为Http时，必填。
        :type Method: str
        :param _Key: 秘钥。
        :type Key: str
        """
        self._Name = None
        self._Type = None
        self._Webhook = None
        self._Method = None
        self._Key = None

    @property
    def Name(self):
        """通知内容名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """渠道类型。

WeCom:企业微信;DingTalk:钉钉;Lark:飞书;Http:自定义回调。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Webhook(self):
        """Webhook地址。
        :rtype: str
        """
        return self._Webhook

    @Webhook.setter
    def Webhook(self, Webhook):
        self._Webhook = Webhook

    @property
    def Method(self):
        """请求方式。 支持POST、PUT。

当Type为Http时，必填。
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Key(self):
        """秘钥。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Webhook = params.get("Webhook")
        self._Method = params.get("Method")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWebCallbackResponse(AbstractModel):
    """CreateWebCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WebCallbackId: 回调配置ID。
        :type WebCallbackId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WebCallbackId = None
        self._RequestId = None

    @property
    def WebCallbackId(self):
        """回调配置ID。
        :rtype: str
        """
        return self._WebCallbackId

    @WebCallbackId.setter
    def WebCallbackId(self, WebCallbackId):
        self._WebCallbackId = WebCallbackId

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
        self._WebCallbackId = params.get("WebCallbackId")
        self._RequestId = params.get("RequestId")


class CsvInfo(AbstractModel):
    """csv内容描述

    """

    def __init__(self):
        r"""
        :param _PrintKey: csv首行是否打印key
        :type PrintKey: bool
        :param _Keys: 每列key的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        :param _Delimiter: 各字段间的分隔符
        :type Delimiter: str
        :param _EscapeChar: 若字段内容中包含分隔符，则使用该转义符包裹改字段，只能填写单引号、双引号、空字符串
        :type EscapeChar: str
        :param _NonExistingField: 对于上面指定的不存在字段使用该内容填充
        :type NonExistingField: str
        """
        self._PrintKey = None
        self._Keys = None
        self._Delimiter = None
        self._EscapeChar = None
        self._NonExistingField = None

    @property
    def PrintKey(self):
        """csv首行是否打印key
        :rtype: bool
        """
        return self._PrintKey

    @PrintKey.setter
    def PrintKey(self, PrintKey):
        self._PrintKey = PrintKey

    @property
    def Keys(self):
        """每列key的名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Delimiter(self):
        """各字段间的分隔符
        :rtype: str
        """
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def EscapeChar(self):
        """若字段内容中包含分隔符，则使用该转义符包裹改字段，只能填写单引号、双引号、空字符串
        :rtype: str
        """
        return self._EscapeChar

    @EscapeChar.setter
    def EscapeChar(self, EscapeChar):
        self._EscapeChar = EscapeChar

    @property
    def NonExistingField(self):
        """对于上面指定的不存在字段使用该内容填充
        :rtype: str
        """
        return self._NonExistingField

    @NonExistingField.setter
    def NonExistingField(self, NonExistingField):
        self._NonExistingField = NonExistingField


    def _deserialize(self, params):
        self._PrintKey = params.get("PrintKey")
        self._Keys = params.get("Keys")
        self._Delimiter = params.get("Delimiter")
        self._EscapeChar = params.get("EscapeChar")
        self._NonExistingField = params.get("NonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DashboardInfo(AbstractModel):
    """仪表盘信息

    """

    def __init__(self):
        r"""
        :param _DashboardId: 仪表盘id
        :type DashboardId: str
        :param _DashboardName: 仪表盘名字
        :type DashboardName: str
        :param _Data: 仪表盘数据
        :type Data: str
        :param _CreateTime: 创建仪表盘的时间
        :type CreateTime: str
        :param _AssumerUin: AssumerUin非空则表示创建该日志主题的服务方Uin
        :type AssumerUin: int
        :param _RoleName: RoleName非空则表示创建该日志主题的服务方使用的角色
        :type RoleName: str
        :param _AssumerName: AssumerName非空则表示创建该日志主题的服务方名称
        :type AssumerName: str
        :param _Tags: 日志主题绑定的标签信息
        :type Tags: list of Tag
        :param _DashboardRegion: 仪表盘所在地域： 为了兼容老的地域。
        :type DashboardRegion: str
        :param _UpdateTime: 修改仪表盘的时间
        :type UpdateTime: str
        :param _DashboardTopicInfos: 仪表盘对应的topic相关信息
        :type DashboardTopicInfos: list of DashboardTopicInfo
        """
        self._DashboardId = None
        self._DashboardName = None
        self._Data = None
        self._CreateTime = None
        self._AssumerUin = None
        self._RoleName = None
        self._AssumerName = None
        self._Tags = None
        self._DashboardRegion = None
        self._UpdateTime = None
        self._DashboardTopicInfos = None

    @property
    def DashboardId(self):
        """仪表盘id
        :rtype: str
        """
        return self._DashboardId

    @DashboardId.setter
    def DashboardId(self, DashboardId):
        self._DashboardId = DashboardId

    @property
    def DashboardName(self):
        """仪表盘名字
        :rtype: str
        """
        return self._DashboardName

    @DashboardName.setter
    def DashboardName(self, DashboardName):
        self._DashboardName = DashboardName

    @property
    def Data(self):
        """仪表盘数据
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CreateTime(self):
        """创建仪表盘的时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AssumerUin(self):
        """AssumerUin非空则表示创建该日志主题的服务方Uin
        :rtype: int
        """
        return self._AssumerUin

    @AssumerUin.setter
    def AssumerUin(self, AssumerUin):
        self._AssumerUin = AssumerUin

    @property
    def RoleName(self):
        """RoleName非空则表示创建该日志主题的服务方使用的角色
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def AssumerName(self):
        """AssumerName非空则表示创建该日志主题的服务方名称
        :rtype: str
        """
        return self._AssumerName

    @AssumerName.setter
    def AssumerName(self, AssumerName):
        self._AssumerName = AssumerName

    @property
    def Tags(self):
        """日志主题绑定的标签信息
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DashboardRegion(self):
        """仪表盘所在地域： 为了兼容老的地域。
        :rtype: str
        """
        return self._DashboardRegion

    @DashboardRegion.setter
    def DashboardRegion(self, DashboardRegion):
        self._DashboardRegion = DashboardRegion

    @property
    def UpdateTime(self):
        """修改仪表盘的时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DashboardTopicInfos(self):
        """仪表盘对应的topic相关信息
        :rtype: list of DashboardTopicInfo
        """
        return self._DashboardTopicInfos

    @DashboardTopicInfos.setter
    def DashboardTopicInfos(self, DashboardTopicInfos):
        self._DashboardTopicInfos = DashboardTopicInfos


    def _deserialize(self, params):
        self._DashboardId = params.get("DashboardId")
        self._DashboardName = params.get("DashboardName")
        self._Data = params.get("Data")
        self._CreateTime = params.get("CreateTime")
        self._AssumerUin = params.get("AssumerUin")
        self._RoleName = params.get("RoleName")
        self._AssumerName = params.get("AssumerName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DashboardRegion = params.get("DashboardRegion")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("DashboardTopicInfos") is not None:
            self._DashboardTopicInfos = []
            for item in params.get("DashboardTopicInfos"):
                obj = DashboardTopicInfo()
                obj._deserialize(item)
                self._DashboardTopicInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DashboardNoticeMode(AbstractModel):
    """仪表盘订阅通知方式

    """

    def __init__(self):
        r"""
        :param _ReceiverType: 仪表盘通知方式。<br>
<li/>Uin：腾讯云用户<br>
<li/>Group：腾讯云用户组<br>
<li/>Email：自定义Email<br>
<li/>WeCom: 企业微信回调
        :type ReceiverType: str
        :param _Values: 知方式对应的值。
<br> <li/> 当ReceiverType不是 Wecom 时，Values必填。
        :type Values: list of str
        :param _ReceiverChannels: 仪表盘通知渠道。
<br><li/> 支持：["Email","Sms","WeChat","Phone"]。
<br><li/> 当ReceiverType是 Email 或 Wecom 时，ReceiverChannels不能赋值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverChannels: list of str
        :param _Url: 回调Url。
<br><li/> 当ReceiverType是 Wecom 时，Url必填。
<br><li/> 当ReceiverType不是 Wecom 时，Url不能填写。
        :type Url: str
        """
        self._ReceiverType = None
        self._Values = None
        self._ReceiverChannels = None
        self._Url = None

    @property
    def ReceiverType(self):
        """仪表盘通知方式。<br>
<li/>Uin：腾讯云用户<br>
<li/>Group：腾讯云用户组<br>
<li/>Email：自定义Email<br>
<li/>WeCom: 企业微信回调
        :rtype: str
        """
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def Values(self):
        """知方式对应的值。
<br> <li/> 当ReceiverType不是 Wecom 时，Values必填。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ReceiverChannels(self):
        """仪表盘通知渠道。
<br><li/> 支持：["Email","Sms","WeChat","Phone"]。
<br><li/> 当ReceiverType是 Email 或 Wecom 时，ReceiverChannels不能赋值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ReceiverChannels

    @ReceiverChannels.setter
    def ReceiverChannels(self, ReceiverChannels):
        self._ReceiverChannels = ReceiverChannels

    @property
    def Url(self):
        """回调Url。
<br><li/> 当ReceiverType是 Wecom 时，Url必填。
<br><li/> 当ReceiverType不是 Wecom 时，Url不能填写。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._ReceiverType = params.get("ReceiverType")
        self._Values = params.get("Values")
        self._ReceiverChannels = params.get("ReceiverChannels")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DashboardSubscribeData(AbstractModel):
    """仪表盘订阅相关数据

    """

    def __init__(self):
        r"""
        :param _NoticeModes: 仪表盘订阅通知方式。
        :type NoticeModes: list of DashboardNoticeMode
        :param _DashboardTime: 仪表盘订阅时间，为空标识取仪表盘默认的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DashboardTime: list of str
        :param _TemplateVariables: 仪表盘订阅模板变量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateVariables: list of DashboardTemplateVariable
        :param _Timezone: 时区。参考：https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#SHANGHAI
        :type Timezone: str
        :param _SubscribeLanguage: 语言。 zh 中文、en`英文。
        :type SubscribeLanguage: str
        :param _JumpDomain: 调用链接域名。http:// 或者 https:// 开头，不能/结尾
        :type JumpDomain: str
        :param _JumpUrl: 自定义跳转链接。
        :type JumpUrl: str
        """
        self._NoticeModes = None
        self._DashboardTime = None
        self._TemplateVariables = None
        self._Timezone = None
        self._SubscribeLanguage = None
        self._JumpDomain = None
        self._JumpUrl = None

    @property
    def NoticeModes(self):
        """仪表盘订阅通知方式。
        :rtype: list of DashboardNoticeMode
        """
        return self._NoticeModes

    @NoticeModes.setter
    def NoticeModes(self, NoticeModes):
        self._NoticeModes = NoticeModes

    @property
    def DashboardTime(self):
        """仪表盘订阅时间，为空标识取仪表盘默认的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DashboardTime

    @DashboardTime.setter
    def DashboardTime(self, DashboardTime):
        self._DashboardTime = DashboardTime

    @property
    def TemplateVariables(self):
        """仪表盘订阅模板变量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DashboardTemplateVariable
        """
        return self._TemplateVariables

    @TemplateVariables.setter
    def TemplateVariables(self, TemplateVariables):
        self._TemplateVariables = TemplateVariables

    @property
    def Timezone(self):
        """时区。参考：https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#SHANGHAI
        :rtype: str
        """
        return self._Timezone

    @Timezone.setter
    def Timezone(self, Timezone):
        self._Timezone = Timezone

    @property
    def SubscribeLanguage(self):
        """语言。 zh 中文、en`英文。
        :rtype: str
        """
        return self._SubscribeLanguage

    @SubscribeLanguage.setter
    def SubscribeLanguage(self, SubscribeLanguage):
        self._SubscribeLanguage = SubscribeLanguage

    @property
    def JumpDomain(self):
        """调用链接域名。http:// 或者 https:// 开头，不能/结尾
        :rtype: str
        """
        return self._JumpDomain

    @JumpDomain.setter
    def JumpDomain(self, JumpDomain):
        self._JumpDomain = JumpDomain

    @property
    def JumpUrl(self):
        """自定义跳转链接。
        :rtype: str
        """
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl


    def _deserialize(self, params):
        if params.get("NoticeModes") is not None:
            self._NoticeModes = []
            for item in params.get("NoticeModes"):
                obj = DashboardNoticeMode()
                obj._deserialize(item)
                self._NoticeModes.append(obj)
        self._DashboardTime = params.get("DashboardTime")
        if params.get("TemplateVariables") is not None:
            self._TemplateVariables = []
            for item in params.get("TemplateVariables"):
                obj = DashboardTemplateVariable()
                obj._deserialize(item)
                self._TemplateVariables.append(obj)
        self._Timezone = params.get("Timezone")
        self._SubscribeLanguage = params.get("SubscribeLanguage")
        self._JumpDomain = params.get("JumpDomain")
        self._JumpUrl = params.get("JumpUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DashboardTemplateVariable(AbstractModel):
    """仪表盘订阅模板变量

    """

    def __init__(self):
        r"""
        :param _Key: key的值
        :type Key: str
        :param _Values: key对应的values取值values
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        """key的值
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        """key对应的values取值values
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DashboardTopicInfo(AbstractModel):
    """仪表盘关联的topic信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题id
        :type TopicId: str
        :param _Region: topic所在的地域
        :type Region: str
        """
        self._TopicId = None
        self._Region = None

    @property
    def TopicId(self):
        """主题id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Region(self):
        """topic所在的地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataTransformResouceInfo(AbstractModel):
    """数据加工的资源信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 目标主题id
        :type TopicId: str
        :param _Alias: 别名
        :type Alias: str
        """
        self._TopicId = None
        self._Alias = None

    @property
    def TopicId(self):
        """目标主题id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Alias(self):
        """别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataTransformTaskInfo(AbstractModel):
    """数据加工任务基本详情

    """

    def __init__(self):
        r"""
        :param _Name: 数据加工任务名称
        :type Name: str
        :param _TaskId: 数据加工任务id
        :type TaskId: str
        :param _EnableFlag: 任务启用状态，默认为1，正常开启,  2关闭
        :type EnableFlag: int
        :param _Type: 加工任务类型，1： DSL， 2：SQL
        :type Type: int
        :param _SrcTopicId: 源日志主题
        :type SrcTopicId: str
        :param _Status: 当前加工任务状态（1准备中/2运行中/3停止中/4已停止）
        :type Status: int
        :param _CreateTime: 加工任务创建时间
        :type CreateTime: str
        :param _UpdateTime: 最近修改时间
        :type UpdateTime: str
        :param _LastEnableTime: 最后启用时间，如果需要重建集群，修改该时间
        :type LastEnableTime: str
        :param _SrcTopicName: 日志主题名称
        :type SrcTopicName: str
        :param _LogsetId: 日志集id
        :type LogsetId: str
        :param _DstResources: 加工任务目的topic_id以及别名
        :type DstResources: list of DataTransformResouceInfo
        :param _EtlContent: 加工逻辑函数。
        :type EtlContent: str
        :param _DataTransformType: 数据加工类型。0：标准加工任务；1：前置加工任务。
        :type DataTransformType: int
        :param _KeepFailureLog: 保留失败日志状态。 1:不保留，2:保留
        :type KeepFailureLog: int
        :param _FailureLogKey: 失败日志的字段名称
        :type FailureLogKey: str
        """
        self._Name = None
        self._TaskId = None
        self._EnableFlag = None
        self._Type = None
        self._SrcTopicId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LastEnableTime = None
        self._SrcTopicName = None
        self._LogsetId = None
        self._DstResources = None
        self._EtlContent = None
        self._DataTransformType = None
        self._KeepFailureLog = None
        self._FailureLogKey = None

    @property
    def Name(self):
        """数据加工任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaskId(self):
        """数据加工任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def EnableFlag(self):
        """任务启用状态，默认为1，正常开启,  2关闭
        :rtype: int
        """
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def Type(self):
        """加工任务类型，1： DSL， 2：SQL
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SrcTopicId(self):
        """源日志主题
        :rtype: str
        """
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def Status(self):
        """当前加工任务状态（1准备中/2运行中/3停止中/4已停止）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """加工任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最近修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LastEnableTime(self):
        """最后启用时间，如果需要重建集群，修改该时间
        :rtype: str
        """
        return self._LastEnableTime

    @LastEnableTime.setter
    def LastEnableTime(self, LastEnableTime):
        self._LastEnableTime = LastEnableTime

    @property
    def SrcTopicName(self):
        """日志主题名称
        :rtype: str
        """
        return self._SrcTopicName

    @SrcTopicName.setter
    def SrcTopicName(self, SrcTopicName):
        self._SrcTopicName = SrcTopicName

    @property
    def LogsetId(self):
        """日志集id
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def DstResources(self):
        """加工任务目的topic_id以及别名
        :rtype: list of DataTransformResouceInfo
        """
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources

    @property
    def EtlContent(self):
        """加工逻辑函数。
        :rtype: str
        """
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent

    @property
    def DataTransformType(self):
        """数据加工类型。0：标准加工任务；1：前置加工任务。
        :rtype: int
        """
        return self._DataTransformType

    @DataTransformType.setter
    def DataTransformType(self, DataTransformType):
        self._DataTransformType = DataTransformType

    @property
    def KeepFailureLog(self):
        """保留失败日志状态。 1:不保留，2:保留
        :rtype: int
        """
        return self._KeepFailureLog

    @KeepFailureLog.setter
    def KeepFailureLog(self, KeepFailureLog):
        self._KeepFailureLog = KeepFailureLog

    @property
    def FailureLogKey(self):
        """失败日志的字段名称
        :rtype: str
        """
        return self._FailureLogKey

    @FailureLogKey.setter
    def FailureLogKey(self, FailureLogKey):
        self._FailureLogKey = FailureLogKey


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TaskId = params.get("TaskId")
        self._EnableFlag = params.get("EnableFlag")
        self._Type = params.get("Type")
        self._SrcTopicId = params.get("SrcTopicId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LastEnableTime = params.get("LastEnableTime")
        self._SrcTopicName = params.get("SrcTopicName")
        self._LogsetId = params.get("LogsetId")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        self._EtlContent = params.get("EtlContent")
        self._DataTransformType = params.get("DataTransformType")
        self._KeepFailureLog = params.get("KeepFailureLog")
        self._FailureLogKey = params.get("FailureLogKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeRequest(AbstractModel):
    """DeleteAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: 通知渠道组ID
        :type AlarmNoticeId: str
        """
        self._AlarmNoticeId = None

    @property
    def AlarmNoticeId(self):
        """通知渠道组ID
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeResponse(AbstractModel):
    """DeleteAlarmNotice返回参数结构体

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


class DeleteAlarmRequest(AbstractModel):
    """DeleteAlarm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmId: 告警策略ID。
        :type AlarmId: str
        """
        self._AlarmId = None

    @property
    def AlarmId(self):
        """告警策略ID。
        :rtype: str
        """
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmResponse(AbstractModel):
    """DeleteAlarm返回参数结构体

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


class DeleteAlarmShieldRequest(AbstractModel):
    """DeleteAlarmShield请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 屏蔽规则id。
        :type TaskId: str
        :param _AlarmNoticeId: 通知渠道组id。
        :type AlarmNoticeId: str
        """
        self._TaskId = None
        self._AlarmNoticeId = None

    @property
    def TaskId(self):
        """屏蔽规则id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def AlarmNoticeId(self):
        """通知渠道组id。
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmShieldResponse(AbstractModel):
    """DeleteAlarmShield返回参数结构体

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


class DeleteConfigExtraRequest(AbstractModel):
    """DeleteConfigExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigExtraId: 特殊采集规则扩展配置ID
        :type ConfigExtraId: str
        """
        self._ConfigExtraId = None

    @property
    def ConfigExtraId(self):
        """特殊采集规则扩展配置ID
        :rtype: str
        """
        return self._ConfigExtraId

    @ConfigExtraId.setter
    def ConfigExtraId(self, ConfigExtraId):
        self._ConfigExtraId = ConfigExtraId


    def _deserialize(self, params):
        self._ConfigExtraId = params.get("ConfigExtraId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigExtraResponse(AbstractModel):
    """DeleteConfigExtra返回参数结构体

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


class DeleteConfigFromMachineGroupRequest(AbstractModel):
    """DeleteConfigFromMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _ConfigId: 采集配置ID
        :type ConfigId: str
        """
        self._GroupId = None
        self._ConfigId = None

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ConfigId(self):
        """采集配置ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigFromMachineGroupResponse(AbstractModel):
    """DeleteConfigFromMachineGroup返回参数结构体

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


class DeleteConfigRequest(AbstractModel):
    """DeleteConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集规则配置ID
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        """采集规则配置ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigResponse(AbstractModel):
    """DeleteConfig返回参数结构体

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


class DeleteConsoleSharingRequest(AbstractModel):
    """DeleteConsoleSharing请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SharingId: 免密分享Id
        :type SharingId: str
        """
        self._SharingId = None

    @property
    def SharingId(self):
        """免密分享Id
        :rtype: str
        """
        return self._SharingId

    @SharingId.setter
    def SharingId(self, SharingId):
        self._SharingId = SharingId


    def _deserialize(self, params):
        self._SharingId = params.get("SharingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsoleSharingResponse(AbstractModel):
    """DeleteConsoleSharing返回参数结构体

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


class DeleteConsumerRequest(AbstractModel):
    """DeleteConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递任务绑定的日志主题 ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        """投递任务绑定的日志主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsumerResponse(AbstractModel):
    """DeleteConsumer返回参数结构体

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


class DeleteDashboardSubscribeRequest(AbstractModel):
    """DeleteDashboardSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 仪表盘订阅记录id。
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """仪表盘订阅记录id。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDashboardSubscribeResponse(AbstractModel):
    """DeleteDashboardSubscribe返回参数结构体

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


class DeleteDataTransformRequest(AbstractModel):
    """DeleteDataTransform请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 数据加工任务id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """数据加工任务id
        :rtype: str
        """
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
        


class DeleteDataTransformResponse(AbstractModel):
    """DeleteDataTransform返回参数结构体

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


class DeleteExportRequest(AbstractModel):
    """DeleteExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportId: 日志导出ID
        :type ExportId: str
        """
        self._ExportId = None

    @property
    def ExportId(self):
        """日志导出ID
        :rtype: str
        """
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId


    def _deserialize(self, params):
        self._ExportId = params.get("ExportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExportResponse(AbstractModel):
    """DeleteExport返回参数结构体

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


class DeleteIndexRequest(AbstractModel):
    """DeleteIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    """DeleteIndex返回参数结构体

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


class DeleteKafkaRechargeRequest(AbstractModel):
    """DeleteKafkaRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Kafka导入配置ID
        :type Id: str
        :param _TopicId: 导入CLS目标topic ID
        :type TopicId: str
        """
        self._Id = None
        self._TopicId = None

    @property
    def Id(self):
        """Kafka导入配置ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        """导入CLS目标topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKafkaRechargeResponse(AbstractModel):
    """DeleteKafkaRecharge返回参数结构体

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


class DeleteLogsetRequest(AbstractModel):
    """DeleteLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        """
        self._LogsetId = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogsetResponse(AbstractModel):
    """DeleteLogset返回参数结构体

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


class DeleteMachineGroupInfoRequest(AbstractModel):
    """DeleteMachineGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _MachineGroupType: 机器组类型
目前type支持 ip 和 label
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        self._GroupId = None
        self._MachineGroupType = None

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MachineGroupType(self):
        """机器组类型
目前type支持 ip 和 label
        :rtype: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineGroupInfoResponse(AbstractModel):
    """DeleteMachineGroupInfo返回参数结构体

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


class DeleteMachineGroupRequest(AbstractModel):
    """DeleteMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineGroupResponse(AbstractModel):
    """DeleteMachineGroup返回参数结构体

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


class DeleteNoticeContentRequest(AbstractModel):
    """DeleteNoticeContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeContentId: 通知内容模板ID
        :type NoticeContentId: str
        """
        self._NoticeContentId = None

    @property
    def NoticeContentId(self):
        """通知内容模板ID
        :rtype: str
        """
        return self._NoticeContentId

    @NoticeContentId.setter
    def NoticeContentId(self, NoticeContentId):
        self._NoticeContentId = NoticeContentId


    def _deserialize(self, params):
        self._NoticeContentId = params.get("NoticeContentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNoticeContentResponse(AbstractModel):
    """DeleteNoticeContent返回参数结构体

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


class DeleteScheduledSqlRequest(AbstractModel):
    """DeleteScheduledSql请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _SrcTopicId: 源日志主题ID
        :type SrcTopicId: str
        """
        self._TaskId = None
        self._SrcTopicId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SrcTopicId(self):
        """源日志主题ID
        :rtype: str
        """
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SrcTopicId = params.get("SrcTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScheduledSqlResponse(AbstractModel):
    """DeleteScheduledSql返回参数结构体

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


class DeleteShipperRequest(AbstractModel):
    """DeleteShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        """
        self._ShipperId = None

    @property
    def ShipperId(self):
        """投递规则ID
        :rtype: str
        """
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShipperResponse(AbstractModel):
    """DeleteShipper返回参数结构体

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


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

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


class DeleteWebCallbackRequest(AbstractModel):
    """DeleteWebCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WebCallbackId: 告警渠道回调配置ID。
        :type WebCallbackId: str
        """
        self._WebCallbackId = None

    @property
    def WebCallbackId(self):
        """告警渠道回调配置ID。
        :rtype: str
        """
        return self._WebCallbackId

    @WebCallbackId.setter
    def WebCallbackId(self, WebCallbackId):
        self._WebCallbackId = WebCallbackId


    def _deserialize(self, params):
        self._WebCallbackId = params.get("WebCallbackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWebCallbackResponse(AbstractModel):
    """DeleteWebCallback返回参数结构体

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


class DeliverConfig(AbstractModel):
    """投递配置入参

    """

    def __init__(self):
        r"""
        :param _Region: 地域信息。

示例：
 ap-guangzhou  广州地域；
ap-nanjing 南京地域。

详细信息请查看官网：

https://cloud.tencent.com/document/product/614/18940
        :type Region: str
        :param _TopicId: 日志主题ID。
        :type TopicId: str
        :param _Scope: 投递数据范围。

0: 全部日志, 包括告警策略日常周期执行的所有日志，也包括告警策略变更产生的日志，默认值

1:仅告警触发及恢复日志
        :type Scope: int
        """
        self._Region = None
        self._TopicId = None
        self._Scope = None

    @property
    def Region(self):
        """地域信息。

示例：
 ap-guangzhou  广州地域；
ap-nanjing 南京地域。

详细信息请查看官网：

https://cloud.tencent.com/document/product/614/18940
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TopicId(self):
        """日志主题ID。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Scope(self):
        """投递数据范围。

0: 全部日志, 包括告警策略日常周期执行的所有日志，也包括告警策略变更产生的日志，默认值

1:仅告警触发及恢复日志
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._TopicId = params.get("TopicId")
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li> name
按照【通知渠道组名称】进行过滤。
类型：String
必选：否</li>
<li> alarmNoticeId
按照【通知渠道组ID】进行过滤。
类型：String
必选：否</li>
<li> uid
按照【接收用户ID】进行过滤。
类型：String
必选：否</li>
<li> groupId
按照【接收用户组ID】进行过滤。
类型：String
必选：否</li>

<li> deliverFlag
按照【投递状态】进行过滤。
类型：String
必选：否
可选值： "1":未启用,  "2": 已启用, "3":投递异常</li>

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """<li> name
按照【通知渠道组名称】进行过滤。
类型：String
必选：否</li>
<li> alarmNoticeId
按照【通知渠道组ID】进行过滤。
类型：String
必选：否</li>
<li> uid
按照【接收用户ID】进行过滤。
类型：String
必选：否</li>
<li> groupId
按照【接收用户组ID】进行过滤。
类型：String
必选：否</li>

<li> deliverFlag
按照【投递状态】进行过滤。
类型：String
必选：否
可选值： "1":未启用,  "2": 已启用, "3":投递异常</li>

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
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
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNotices: 告警通知模板列表。
        :type AlarmNotices: list of AlarmNotice
        :param _TotalCount: 符合条件的告警通知模板总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmNotices = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AlarmNotices(self):
        """告警通知模板列表。
        :rtype: list of AlarmNotice
        """
        return self._AlarmNotices

    @AlarmNotices.setter
    def AlarmNotices(self, AlarmNotices):
        self._AlarmNotices = AlarmNotices

    @property
    def TotalCount(self):
        """符合条件的告警通知模板总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("AlarmNotices") is not None:
            self._AlarmNotices = []
            for item in params.get("AlarmNotices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self._AlarmNotices.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAlarmShieldsRequest(AbstractModel):
    """DescribeAlarmShields请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: 通知渠道组id。
        :type AlarmNoticeId: str
        :param _Filters: - taskId:按照【规则id】进行过滤。类型：String  必选：否
- status:按照【规则状态】进行过滤。类型：String。 支持 0:暂未生效，1:生效中，2:已失效。 必选：否
每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self._AlarmNoticeId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def AlarmNoticeId(self):
        """通知渠道组id。
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def Filters(self):
        """- taskId:按照【规则id】进行过滤。类型：String  必选：否
- status:按照【规则状态】进行过滤。类型：String。 支持 0:暂未生效，1:生效中，2:已失效。 必选：否
每次请求的Filters的上限为10，Filter.Values的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
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
        


class DescribeAlarmShieldsResponse(AbstractModel):
    """DescribeAlarmShields返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的规则总数目
        :type TotalCount: int
        :param _AlarmShields: 告警屏蔽规则详情
        :type AlarmShields: list of AlarmShieldInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AlarmShields = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的规则总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AlarmShields(self):
        """告警屏蔽规则详情
        :rtype: list of AlarmShieldInfo
        """
        return self._AlarmShields

    @AlarmShields.setter
    def AlarmShields(self, AlarmShields):
        self._AlarmShields = AlarmShields

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
        if params.get("AlarmShields") is not None:
            self._AlarmShields = []
            for item in params.get("AlarmShields"):
                obj = AlarmShieldInfo()
                obj._deserialize(item)
                self._AlarmShields.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmsRequest(AbstractModel):
    """DescribeAlarms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: name
- 按照【告警策略名称】进行过滤。
- 类型：String
- 必选：否

alarmId
- 按照【告警策略ID】进行过滤。
- 类型：String
- 必选：否

topicId
- 按照【监控对象的日志主题ID】进行过滤。
- 类型：String
- 必选：否

enable
- 按照【启用状态】进行过滤。
- 类型：String
- 备注：enable参数值范围: 1, t, T, TRUE, true, True, 0, f, F, FALSE, false, False。 其它值将返回参数错误信息.
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """name
- 按照【告警策略名称】进行过滤。
- 类型：String
- 必选：否

alarmId
- 按照【告警策略ID】进行过滤。
- 类型：String
- 必选：否

topicId
- 按照【监控对象的日志主题ID】进行过滤。
- 类型：String
- 必选：否

enable
- 按照【启用状态】进行过滤。
- 类型：String
- 备注：enable参数值范围: 1, t, T, TRUE, true, True, 0, f, F, FALSE, false, False。 其它值将返回参数错误信息.
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
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
        


class DescribeAlarmsResponse(AbstractModel):
    """DescribeAlarms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Alarms: 告警策略列表。
        :type Alarms: list of AlarmInfo
        :param _TotalCount: 符合查询条件的告警策略数目。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Alarms = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Alarms(self):
        """告警策略列表。
        :rtype: list of AlarmInfo
        """
        return self._Alarms

    @Alarms.setter
    def Alarms(self, Alarms):
        self._Alarms = Alarms

    @property
    def TotalCount(self):
        """符合查询条件的告警策略数目。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Alarms") is not None:
            self._Alarms = []
            for item in params.get("Alarms"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self._Alarms.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAlertRecordHistoryRequest(AbstractModel):
    """DescribeAlertRecordHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 查询时间范围启始时间，毫秒级unix时间戳
        :type From: int
        :param _To: 查询时间范围结束时间，毫秒级unix时间戳
        :type To: int
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，最大值100。
        :type Limit: int
        :param _Filters: - alertId：按照告警策略ID进行过滤。类型：String 必选：否
- topicId：按照监控对象ID进行过滤。类型：String 必选：否
- status：按照告警状态进行过滤。类型：String 必选：否，0代表未恢复，1代表已恢复，2代表已失效
- alarmLevel：按照告警等级进行过滤。类型：String 必选：否，0代表警告，1代表提醒，2代表紧急

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        """
        self._From = None
        self._To = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def From(self):
        """查询时间范围启始时间，毫秒级unix时间戳
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """查询时间范围结束时间，毫秒级unix时间戳
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，最大值100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """- alertId：按照告警策略ID进行过滤。类型：String 必选：否
- topicId：按照监控对象ID进行过滤。类型：String 必选：否
- status：按照告警状态进行过滤。类型：String 必选：否，0代表未恢复，1代表已恢复，2代表已失效
- alarmLevel：按照告警等级进行过滤。类型：String 必选：否，0代表警告，1代表提醒，2代表紧急

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
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
        


class DescribeAlertRecordHistoryResponse(AbstractModel):
    """DescribeAlertRecordHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 告警历史总数
        :type TotalCount: int
        :param _Records: 告警历史详情
        :type Records: list of AlertHistoryRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Records = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """告警历史总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Records(self):
        """告警历史详情
        :rtype: list of AlertHistoryRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = AlertHistoryRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigExtrasRequest(AbstractModel):
    """DescribeConfigExtras请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤器，支持如下选项：
name
- 按照【特殊采集配置名称】进行模糊匹配过滤。
- 类型：String

configExtraId
- 按照【特殊采集配置ID】进行过滤。
- 类型：String

topicId
- 按照【日志主题】进行过滤。
- 类型：String

machineGroupId
- 按照【机器组ID】进行过滤。
- 类型：String

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """过滤器，支持如下选项：
name
- 按照【特殊采集配置名称】进行模糊匹配过滤。
- 类型：String

configExtraId
- 按照【特殊采集配置ID】进行过滤。
- 类型：String

topicId
- 按照【日志主题】进行过滤。
- 类型：String

machineGroupId
- 按照【机器组ID】进行过滤。
- 类型：String

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页的限制数目，默认值为20，最大值100
        :rtype: int
        """
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
        


class DescribeConfigExtrasResponse(AbstractModel):
    """DescribeConfigExtras返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Configs: 采集配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of ConfigExtraInfo
        :param _TotalCount: 过滤到的总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Configs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Configs(self):
        """采集配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConfigExtraInfo
        """
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def TotalCount(self):
        """过滤到的总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigExtraInfo()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConfigMachineGroupsRequest(AbstractModel):
    """DescribeConfigMachineGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集配置ID
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        """采集配置ID
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMachineGroupsResponse(AbstractModel):
    """DescribeConfigMachineGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineGroups: 采集规则配置绑定的机器组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineGroups: list of MachineGroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MachineGroups = None
        self._RequestId = None

    @property
    def MachineGroups(self):
        """采集规则配置绑定的机器组列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MachineGroupInfo
        """
        return self._MachineGroups

    @MachineGroups.setter
    def MachineGroups(self, MachineGroups):
        self._MachineGroups = MachineGroups

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
        if params.get("MachineGroups") is not None:
            self._MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self._MachineGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigsRequest(AbstractModel):
    """DescribeConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: configName
- 按照【采集配置名称】进行模糊匹配过滤。
- 类型：String
- 必选：否

configId
- 按照【采集配置ID】进行过滤。
- 类型：String
- 必选：否

topicId
- 按照【日志主题】进行过滤。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """configName
- 按照【采集配置名称】进行模糊匹配过滤。
- 类型：String
- 必选：否

configId
- 按照【采集配置ID】进行过滤。
- 类型：String
- 必选：否

topicId
- 按照【日志主题】进行过滤。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页的限制数目，默认值为20，最大值100
        :rtype: int
        """
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
        


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Configs: 采集配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of ConfigInfo
        :param _TotalCount: 过滤到的总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Configs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Configs(self):
        """采集配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConfigInfo
        """
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def TotalCount(self):
        """过滤到的总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConsoleSharingListRequest(AbstractModel):
    """DescribeConsoleSharingList请求参数结构体

    """


class DescribeConsoleSharingListResponse(AbstractModel):
    """DescribeConsoleSharingList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 分页的总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """分页的总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._RequestId = params.get("RequestId")


class DescribeConsumerRequest(AbstractModel):
    """DescribeConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递任务绑定的日志主题 ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        """投递任务绑定的日志主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerResponse(AbstractModel):
    """DescribeConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Effective: 投递任务是否生效
        :type Effective: bool
        :param _NeedContent: 是否投递日志的元数据信息
        :type NeedContent: bool
        :param _Content: 如果需要投递元数据信息，元数据信息的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka的描述
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: 压缩方式[0:NONE；2:SNAPPY；3:LZ4]
        :type Compression: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Effective = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None
        self._RequestId = None

    @property
    def Effective(self):
        """投递任务是否生效
        :rtype: bool
        """
        return self._Effective

    @Effective.setter
    def Effective(self, Effective):
        self._Effective = Effective

    @property
    def NeedContent(self):
        """是否投递日志的元数据信息
        :rtype: bool
        """
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        """如果需要投递元数据信息，元数据信息的描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        """CKafka的描述
        :rtype: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        """
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        """压缩方式[0:NONE；2:SNAPPY；3:LZ4]
        :rtype: int
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

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
        self._Effective = params.get("Effective")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        self._RequestId = params.get("RequestId")


class DescribeCosRechargesRequest(AbstractModel):
    """DescribeCosRecharges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题 ID
        :type TopicId: str
        :param _Status: 状态   status 0: 已创建, 1: 运行中, 2: 已停止, 3: 已完成, 4: 运行失败。
        :type Status: int
        :param _Enable: 是否启用:   0： 未启用  ， 1：启用
        :type Enable: int
        """
        self._TopicId = None
        self._Status = None
        self._Enable = None

    @property
    def TopicId(self):
        """日志主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        """状态   status 0: 已创建, 1: 运行中, 2: 已停止, 3: 已完成, 4: 运行失败。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        """是否启用:   0： 未启用  ， 1：启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCosRechargesResponse(AbstractModel):
    """DescribeCosRecharges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 见: CosRechargeInfo 结构描述
        :type Data: list of CosRechargeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """见: CosRechargeInfo 结构描述
        :rtype: list of CosRechargeInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CosRechargeInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDashboardSubscribesRequest(AbstractModel):
    """DescribeDashboardSubscribes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <br><li/> dashboardId：按照【仪表盘id】进行过滤。类型：String必选：否<br><br><li/> 每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """<br><li/> dashboardId：按照【仪表盘id】进行过滤。类型：String必选：否<br><br><li/> 每次请求的Filters的上限为10，Filter.Values的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
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
        


class DescribeDashboardSubscribesResponse(AbstractModel):
    """DescribeDashboardSubscribes返回参数结构体

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


class DescribeDashboardsRequest(AbstractModel):
    """DescribeDashboards请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        :param _Filters: - dashboardId 按照【仪表盘id】进行过滤，类型：String， 必选：否。
- dashboardName 按照【仪表盘名字】进行模糊搜索过滤，类型：String，必选：否。
- dashboardRegion 按照【仪表盘地域】进行过滤，为了兼容老的仪表盘，通过云API创建的仪表盘没有地域属性，类型：String，必选：否。
- tagKey 按照【标签键】进行过滤，类型：String，必选：否。
- tag:tagKey 按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换，类型：String，必选：否，使用请参考[示例2](https://cloud.tencent.com/document/api/614/95636#4.-.E7.A4.BA.E4.BE.8B)。

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _TopicIdRegionFilter: 按照topicId和regionId过滤。
        :type TopicIdRegionFilter: list of TopicIdAndRegion
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TopicIdRegionFilter = None

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """- dashboardId 按照【仪表盘id】进行过滤，类型：String， 必选：否。
- dashboardName 按照【仪表盘名字】进行模糊搜索过滤，类型：String，必选：否。
- dashboardRegion 按照【仪表盘地域】进行过滤，为了兼容老的仪表盘，通过云API创建的仪表盘没有地域属性，类型：String，必选：否。
- tagKey 按照【标签键】进行过滤，类型：String，必选：否。
- tag:tagKey 按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换，类型：String，必选：否，使用请参考[示例2](https://cloud.tencent.com/document/api/614/95636#4.-.E7.A4.BA.E4.BE.8B)。

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TopicIdRegionFilter(self):
        """按照topicId和regionId过滤。
        :rtype: list of TopicIdAndRegion
        """
        return self._TopicIdRegionFilter

    @TopicIdRegionFilter.setter
    def TopicIdRegionFilter(self, TopicIdRegionFilter):
        self._TopicIdRegionFilter = TopicIdRegionFilter


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TopicIdRegionFilter") is not None:
            self._TopicIdRegionFilter = []
            for item in params.get("TopicIdRegionFilter"):
                obj = TopicIdAndRegion()
                obj._deserialize(item)
                self._TopicIdRegionFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDashboardsResponse(AbstractModel):
    """DescribeDashboards返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 仪表盘的数量
        :type TotalCount: int
        :param _DashboardInfos: 仪表盘详细明细
        :type DashboardInfos: list of DashboardInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DashboardInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """仪表盘的数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DashboardInfos(self):
        """仪表盘详细明细
        :rtype: list of DashboardInfo
        """
        return self._DashboardInfos

    @DashboardInfos.setter
    def DashboardInfos(self, DashboardInfos):
        self._DashboardInfos = DashboardInfos

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
        if params.get("DashboardInfos") is not None:
            self._DashboardInfos = []
            for item in params.get("DashboardInfos"):
                obj = DashboardInfo()
                obj._deserialize(item)
                self._DashboardInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDataTransformInfoRequest(AbstractModel):
    """DescribeDataTransformInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: - taskName
按照【加工任务名称】进行过滤。
类型：String
必选：否

- taskId
按照【加工任务id】进行过滤。
类型：String
必选：否

- topicId
按照【源topicId】进行过滤。
类型：String
必选：否
- status
按照【 任务运行状态】进行过滤。 1：准备中，2：运行中，3：停止中，4：已停止
类型：String
必选：否
- hasServiceLog
按照【是否开启服务日志】进行过滤。 1：未开启，2：已开启
类型：String
必选：否
- dstTopicType
按照【目标topic类型】进行过滤。  1：固定，2：动态
类型：String
必选：否

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        :param _Type: 默认值为2.   1: 获取单个任务的详细信息 2：获取任务列表
        :type Type: int
        :param _TaskId: Type为1， 此参数必填
        :type TaskId: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Type = None
        self._TaskId = None

    @property
    def Filters(self):
        """- taskName
按照【加工任务名称】进行过滤。
类型：String
必选：否

- taskId
按照【加工任务id】进行过滤。
类型：String
必选：否

- topicId
按照【源topicId】进行过滤。
类型：String
必选：否
- status
按照【 任务运行状态】进行过滤。 1：准备中，2：运行中，3：停止中，4：已停止
类型：String
必选：否
- hasServiceLog
按照【是否开启服务日志】进行过滤。 1：未开启，2：已开启
类型：String
必选：否
- dstTopicType
按照【目标topic类型】进行过滤。  1：固定，2：动态
类型：String
必选：否

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Type(self):
        """默认值为2.   1: 获取单个任务的详细信息 2：获取任务列表
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TaskId(self):
        """Type为1， 此参数必填
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Type = params.get("Type")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataTransformInfoResponse(AbstractModel):
    """DescribeDataTransformInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataTransformTaskInfos: 数据加工任务列表信息
        :type DataTransformTaskInfos: list of DataTransformTaskInfo
        :param _TotalCount: 任务总次数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataTransformTaskInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DataTransformTaskInfos(self):
        """数据加工任务列表信息
        :rtype: list of DataTransformTaskInfo
        """
        return self._DataTransformTaskInfos

    @DataTransformTaskInfos.setter
    def DataTransformTaskInfos(self, DataTransformTaskInfos):
        self._DataTransformTaskInfos = DataTransformTaskInfos

    @property
    def TotalCount(self):
        """任务总次数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("DataTransformTaskInfos") is not None:
            self._DataTransformTaskInfos = []
            for item in params.get("DataTransformTaskInfos"):
                obj = DataTransformTaskInfo()
                obj._deserialize(item)
                self._DataTransformTaskInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeExportsRequest(AbstractModel):
    """DescribeExports请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._TopicId = None
        self._Offset = None
        self._Limit = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Offset(self):
        """分页的偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportsResponse(AbstractModel):
    """DescribeExports返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Exports: 日志导出列表
        :type Exports: list of ExportInfo
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Exports = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Exports(self):
        """日志导出列表
        :rtype: list of ExportInfo
        """
        return self._Exports

    @Exports.setter
    def Exports(self, Exports):
        self._Exports = Exports

    @property
    def TotalCount(self):
        """总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Exports") is not None:
            self._Exports = []
            for item in params.get("Exports"):
                obj = ExportInfo()
                obj._deserialize(item)
                self._Exports.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIndexRequest(AbstractModel):
    """DescribeIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexResponse(AbstractModel):
    """DescribeIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Status: 是否生效
        :type Status: bool
        :param _Rule: 索引配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _ModifyTime: 索引修改时间，初始值为索引创建时间。
        :type ModifyTime: str
        :param _IncludeInternalFields: 内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引
* false:不包含
* true:包含
        :type IncludeInternalFields: bool
        :param _MetadataFlag: 元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
        :type MetadataFlag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicId = None
        self._Status = None
        self._Rule = None
        self._ModifyTime = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None
        self._RequestId = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        """是否生效
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rule(self):
        """索引配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def ModifyTime(self):
        """索引修改时间，初始值为索引创建时间。
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def IncludeInternalFields(self):
        """内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引
* false:不包含
* true:包含
        :rtype: bool
        """
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        """元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
        :rtype: int
        """
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag

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
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._ModifyTime = params.get("ModifyTime")
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        self._RequestId = params.get("RequestId")


class DescribeKafkaConsumerRequest(AbstractModel):
    """DescribeKafkaConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTopicId: 日志主题ID
        :type FromTopicId: str
        """
        self._FromTopicId = None

    @property
    def FromTopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._FromTopicId

    @FromTopicId.setter
    def FromTopicId(self, FromTopicId):
        self._FromTopicId = FromTopicId


    def _deserialize(self, params):
        self._FromTopicId = params.get("FromTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKafkaConsumerResponse(AbstractModel):
    """DescribeKafkaConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: Kafka协议消费是否打开
        :type Status: bool
        :param _TopicID: KafkaConsumer 消费时使用的Topic参数
        :type TopicID: str
        :param _Compression: 压缩方式[0:NONE；2:SNAPPY；3:LZ4]
        :type Compression: int
        :param _ConsumerContent: kafka协议消费数据格式
        :type ConsumerContent: :class:`tencentcloud.cls.v20201016.models.KafkaConsumerContent`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._TopicID = None
        self._Compression = None
        self._ConsumerContent = None
        self._RequestId = None

    @property
    def Status(self):
        """Kafka协议消费是否打开
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TopicID(self):
        """KafkaConsumer 消费时使用的Topic参数
        :rtype: str
        """
        return self._TopicID

    @TopicID.setter
    def TopicID(self, TopicID):
        self._TopicID = TopicID

    @property
    def Compression(self):
        """压缩方式[0:NONE；2:SNAPPY；3:LZ4]
        :rtype: int
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def ConsumerContent(self):
        """kafka协议消费数据格式
        :rtype: :class:`tencentcloud.cls.v20201016.models.KafkaConsumerContent`
        """
        return self._ConsumerContent

    @ConsumerContent.setter
    def ConsumerContent(self, ConsumerContent):
        self._ConsumerContent = ConsumerContent

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
        self._TopicID = params.get("TopicID")
        self._Compression = params.get("Compression")
        if params.get("ConsumerContent") is not None:
            self._ConsumerContent = KafkaConsumerContent()
            self._ConsumerContent._deserialize(params.get("ConsumerContent"))
        self._RequestId = params.get("RequestId")


class DescribeKafkaRechargesRequest(AbstractModel):
    """DescribeKafkaRecharges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题 ID
        :type TopicId: str
        :param _Id: 导入配置ID
        :type Id: str
        :param _Status: 状态   status 1: 运行中, 2: 暂停...
        :type Status: int
        """
        self._TopicId = None
        self._Id = None
        self._Status = None

    @property
    def TopicId(self):
        """日志主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Id(self):
        """导入配置ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """状态   status 1: 运行中, 2: 暂停...
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKafkaRechargesResponse(AbstractModel):
    """DescribeKafkaRecharges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Infos: KafkaRechargeInfo 信息列表
        :type Infos: list of KafkaRechargeInfo
        :param _TotalCount: Kafka导入信息总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Infos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Infos(self):
        """KafkaRechargeInfo 信息列表
        :rtype: list of KafkaRechargeInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def TotalCount(self):
        """Kafka导入信息总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = KafkaRechargeInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLogContextRequest(AbstractModel):
    """DescribeLogContext请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 要查询的日志主题ID
        :type TopicId: str
        :param _BTime: 日志时间,  即SearchLog接口返回信息中Results结构体中的Time，需按照 UTC+8 时区将该毫秒级Unix时间戳转换为 YYYY-mm-dd HH:MM:SS.FFF 格式的字符串。
        :type BTime: str
        :param _PkgId: 日志包序号，即SearchLog接口返回信息中Results结构体中的PkgId。
        :type PkgId: str
        :param _PkgLogId: 日志包内一条日志的序号，即SearchLog接口返回信息中Results结构中的PkgLogId。
        :type PkgLogId: int
        :param _PrevLogs: 前${PrevLogs}条日志，默认值10。
        :type PrevLogs: int
        :param _NextLogs: 后${NextLogs}条日志，默认值10。
        :type NextLogs: int
        :param _Query: 检索语句，对日志上下文进行过滤，最大长度为12KB
语句由 <a href="https://cloud.tencent.com/document/product/614/47044" target="_blank">[检索条件]</a>构成，不支持SQL语句
        :type Query: str
        :param _From: 上下文检索的开始时间，单位：毫秒级时间戳
注意：
- From为空时，表示上下文检索的开始时间不做限制
- From和To非空时，From < To
- 暂时仅支持上海 / 弗吉尼亚/ 新加坡地域
        :type From: int
        :param _To: 上下文检索的结束时间，单位：毫秒级时间戳。
注意：
- To为空时，表示上下文检索的结束时间不做限制
- From和To非空时，From < To
- 暂时仅支持上海 / 弗吉尼亚/ 新加坡地域
        :type To: int
        """
        self._TopicId = None
        self._BTime = None
        self._PkgId = None
        self._PkgLogId = None
        self._PrevLogs = None
        self._NextLogs = None
        self._Query = None
        self._From = None
        self._To = None

    @property
    def TopicId(self):
        """要查询的日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def BTime(self):
        """日志时间,  即SearchLog接口返回信息中Results结构体中的Time，需按照 UTC+8 时区将该毫秒级Unix时间戳转换为 YYYY-mm-dd HH:MM:SS.FFF 格式的字符串。
        :rtype: str
        """
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime

    @property
    def PkgId(self):
        """日志包序号，即SearchLog接口返回信息中Results结构体中的PkgId。
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        """日志包内一条日志的序号，即SearchLog接口返回信息中Results结构中的PkgLogId。
        :rtype: int
        """
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def PrevLogs(self):
        """前${PrevLogs}条日志，默认值10。
        :rtype: int
        """
        return self._PrevLogs

    @PrevLogs.setter
    def PrevLogs(self, PrevLogs):
        self._PrevLogs = PrevLogs

    @property
    def NextLogs(self):
        """后${NextLogs}条日志，默认值10。
        :rtype: int
        """
        return self._NextLogs

    @NextLogs.setter
    def NextLogs(self, NextLogs):
        self._NextLogs = NextLogs

    @property
    def Query(self):
        """检索语句，对日志上下文进行过滤，最大长度为12KB
语句由 <a href="https://cloud.tencent.com/document/product/614/47044" target="_blank">[检索条件]</a>构成，不支持SQL语句
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def From(self):
        """上下文检索的开始时间，单位：毫秒级时间戳
注意：
- From为空时，表示上下文检索的开始时间不做限制
- From和To非空时，From < To
- 暂时仅支持上海 / 弗吉尼亚/ 新加坡地域
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """上下文检索的结束时间，单位：毫秒级时间戳。
注意：
- To为空时，表示上下文检索的结束时间不做限制
- From和To非空时，From < To
- 暂时仅支持上海 / 弗吉尼亚/ 新加坡地域
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._BTime = params.get("BTime")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._PrevLogs = params.get("PrevLogs")
        self._NextLogs = params.get("NextLogs")
        self._Query = params.get("Query")
        self._From = params.get("From")
        self._To = params.get("To")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogContextResponse(AbstractModel):
    """DescribeLogContext返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogContextInfos: 日志上下文信息集合
        :type LogContextInfos: list of LogContextInfo
        :param _PrevOver: 上文日志是否已经返回完成（当PrevOver为false，表示有上文日志还未全部返回）。
        :type PrevOver: bool
        :param _NextOver: 下文日志是否已经返回完成（当NextOver为false，表示有下文日志还未全部返回）。
        :type NextOver: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogContextInfos = None
        self._PrevOver = None
        self._NextOver = None
        self._RequestId = None

    @property
    def LogContextInfos(self):
        """日志上下文信息集合
        :rtype: list of LogContextInfo
        """
        return self._LogContextInfos

    @LogContextInfos.setter
    def LogContextInfos(self, LogContextInfos):
        self._LogContextInfos = LogContextInfos

    @property
    def PrevOver(self):
        """上文日志是否已经返回完成（当PrevOver为false，表示有上文日志还未全部返回）。
        :rtype: bool
        """
        return self._PrevOver

    @PrevOver.setter
    def PrevOver(self, PrevOver):
        self._PrevOver = PrevOver

    @property
    def NextOver(self):
        """下文日志是否已经返回完成（当NextOver为false，表示有下文日志还未全部返回）。
        :rtype: bool
        """
        return self._NextOver

    @NextOver.setter
    def NextOver(self, NextOver):
        self._NextOver = NextOver

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
        if params.get("LogContextInfos") is not None:
            self._LogContextInfos = []
            for item in params.get("LogContextInfos"):
                obj = LogContextInfo()
                obj._deserialize(item)
                self._LogContextInfos.append(obj)
        self._PrevOver = params.get("PrevOver")
        self._NextOver = params.get("NextOver")
        self._RequestId = params.get("RequestId")


class DescribeLogHistogramRequest(AbstractModel):
    """DescribeLogHistogram请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param _To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param _Query: 查询语句
        :type Query: str
        :param _TopicId: 要查询的日志主题ID
        :type TopicId: str
        :param _Interval: 时间间隔: 单位ms  限制性条件：(To-From) / interval <= 200
        :type Interval: int
        :param _SyntaxRule: 检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :type SyntaxRule: int
        """
        self._From = None
        self._To = None
        self._Query = None
        self._TopicId = None
        self._Interval = None
        self._SyntaxRule = None

    @property
    def From(self):
        """要查询的日志的起始时间，Unix时间戳，单位ms
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """要查询的日志的结束时间，Unix时间戳，单位ms
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        """查询语句
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def TopicId(self):
        """要查询的日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Interval(self):
        """时间间隔: 单位ms  限制性条件：(To-From) / interval <= 200
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def SyntaxRule(self):
        """检索语法规则，默认值为0。
0：Lucene语法，1：CQL语法。
详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._TopicId = params.get("TopicId")
        self._Interval = params.get("Interval")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogHistogramResponse(AbstractModel):
    """DescribeLogHistogram返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Interval: 统计周期： 单位ms
        :type Interval: int
        :param _TotalCount: 命中关键字的日志总条数
        :type TotalCount: int
        :param _HistogramInfos: 周期内统计结果详情
        :type HistogramInfos: list of HistogramInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Interval = None
        self._TotalCount = None
        self._HistogramInfos = None
        self._RequestId = None

    @property
    def Interval(self):
        """统计周期： 单位ms
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def TotalCount(self):
        """命中关键字的日志总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HistogramInfos(self):
        """周期内统计结果详情
        :rtype: list of HistogramInfo
        """
        return self._HistogramInfos

    @HistogramInfos.setter
    def HistogramInfos(self, HistogramInfos):
        self._HistogramInfos = HistogramInfos

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
        self._Interval = params.get("Interval")
        self._TotalCount = params.get("TotalCount")
        if params.get("HistogramInfos") is not None:
            self._HistogramInfos = []
            for item in params.get("HistogramInfos"):
                obj = HistogramInfo()
                obj._deserialize(item)
                self._HistogramInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogsetsRequest(AbstractModel):
    """DescribeLogsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: logsetName
- 按照【日志集名称】进行过滤。
- 类型：String
- 必选：否

logsetId
- 按照【日志集ID】进行过滤。
- 类型：String
- 必选：否

tagKey
- 按照【标签键】进行过滤。
- 类型：String
- 必选：否

tag:tagKey
- 按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """logsetName
- 按照【日志集名称】进行过滤。
- 类型：String
- 必选：否

logsetId
- 按照【日志集ID】进行过滤。
- 类型：String
- 必选：否

tagKey
- 按照【标签键】进行过滤。
- 类型：String
- 必选：否

tag:tagKey
- 按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页的限制数目，默认值为20，最大值100
        :rtype: int
        """
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
        


class DescribeLogsetsResponse(AbstractModel):
    """DescribeLogsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 分页的总数目
        :type TotalCount: int
        :param _Logsets: 日志集列表
        :type Logsets: list of LogsetInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Logsets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """分页的总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Logsets(self):
        """日志集列表
        :rtype: list of LogsetInfo
        """
        return self._Logsets

    @Logsets.setter
    def Logsets(self, Logsets):
        self._Logsets = Logsets

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
        if params.get("Logsets") is not None:
            self._Logsets = []
            for item in params.get("Logsets"):
                obj = LogsetInfo()
                obj._deserialize(item)
                self._Logsets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineGroupConfigsRequest(AbstractModel):
    """DescribeMachineGroupConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineGroupConfigsResponse(AbstractModel):
    """DescribeMachineGroupConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Configs: 采集规则配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of ConfigInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Configs = None
        self._RequestId = None

    @property
    def Configs(self):
        """采集规则配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConfigInfo
        """
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

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
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineGroupsRequest(AbstractModel):
    """DescribeMachineGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: machineGroupName
- 按照【机器组名称】进行过滤。
- 类型：String
- 必选：否

machineGroupId
- 按照【机器组ID】进行过滤。
- 类型：String
- 必选：否

osType
- 按照【操作系统类型】进行过滤。
- 类型：Int
- 必选：否

tagKey
- 按照【标签键】进行过滤。
- 类型：String
- 必选：否

tag:tagKey
- 按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """machineGroupName
- 按照【机器组名称】进行过滤。
- 类型：String
- 必选：否

machineGroupId
- 按照【机器组ID】进行过滤。
- 类型：String
- 必选：否

osType
- 按照【操作系统类型】进行过滤。
- 类型：Int
- 必选：否

tagKey
- 按照【标签键】进行过滤。
- 类型：String
- 必选：否

tag:tagKey
- 按照【标签键值对】进行过滤。tagKey使用具体的标签键进行替换。
- 类型：String
- 必选：否

每次请求的Filters的上限为10，Filter.Values的上限为5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页的限制数目，默认值为20，最大值100
        :rtype: int
        """
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
        


class DescribeMachineGroupsResponse(AbstractModel):
    """DescribeMachineGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineGroups: 机器组信息列表
        :type MachineGroups: list of MachineGroupInfo
        :param _TotalCount: 分页的总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MachineGroups = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def MachineGroups(self):
        """机器组信息列表
        :rtype: list of MachineGroupInfo
        """
        return self._MachineGroups

    @MachineGroups.setter
    def MachineGroups(self, MachineGroups):
        self._MachineGroups = MachineGroups

    @property
    def TotalCount(self):
        """分页的总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("MachineGroups") is not None:
            self._MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self._MachineGroups.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 查询的机器组ID
        :type GroupId: str
        :param _Filters: ip
- 按照【ip】进行过滤。
- 类型：String
- 必选：否

instance
- 按照【instance】进行过滤。
- 类型：String
- 必选：否

version
- 按照【LogListener版本】进行过滤。
- 类型：String
- 必选：否

status
- 按照【状态】进行过滤。
- 类型：String
- 必选：否
- 可选值：0：离线，1：正常

offlineTime
- 按照【机器离线时间】进行过滤。
- 类型：String
- 必选：否
- - 可选值：0：无离线时间，12：12小时内，24：一天内，48：两天内，99：两天前

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量。
        :type Offset: int
        :param _Limit: 分页单页限制数目。最大支持100
        :type Limit: int
        """
        self._GroupId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def GroupId(self):
        """查询的机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Filters(self):
        """ip
- 按照【ip】进行过滤。
- 类型：String
- 必选：否

instance
- 按照【instance】进行过滤。
- 类型：String
- 必选：否

version
- 按照【LogListener版本】进行过滤。
- 类型：String
- 必选：否

status
- 按照【状态】进行过滤。
- 类型：String
- 必选：否
- 可选值：0：离线，1：正常

offlineTime
- 按照【机器离线时间】进行过滤。
- 类型：String
- 必选：否
- - 可选值：0：无离线时间，12：12小时内，24：一天内，48：两天内，99：两天前

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目。最大支持100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
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
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Machines: 机器状态信息组
        :type Machines: list of MachineInfo
        :param _AutoUpdate: 机器组是否开启自动升级功能。 0：未开启自动升级；1：开启了自动升级。
        :type AutoUpdate: int
        :param _UpdateStartTime: 机器组自动升级功能预设开始时间
        :type UpdateStartTime: str
        :param _UpdateEndTime: 机器组自动升级功能预设结束时间
        :type UpdateEndTime: str
        :param _LatestAgentVersion: 当前用户可用最新的Loglistener版本
        :type LatestAgentVersion: str
        :param _ServiceLogging: 是否开启服务日志
        :type ServiceLogging: bool
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Machines = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._LatestAgentVersion = None
        self._ServiceLogging = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Machines(self):
        """机器状态信息组
        :rtype: list of MachineInfo
        """
        return self._Machines

    @Machines.setter
    def Machines(self, Machines):
        self._Machines = Machines

    @property
    def AutoUpdate(self):
        """机器组是否开启自动升级功能。 0：未开启自动升级；1：开启了自动升级。
        :rtype: int
        """
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        """机器组自动升级功能预设开始时间
        :rtype: str
        """
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        """机器组自动升级功能预设结束时间
        :rtype: str
        """
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def LatestAgentVersion(self):
        """当前用户可用最新的Loglistener版本
        :rtype: str
        """
        return self._LatestAgentVersion

    @LatestAgentVersion.setter
    def LatestAgentVersion(self, LatestAgentVersion):
        self._LatestAgentVersion = LatestAgentVersion

    @property
    def ServiceLogging(self):
        """是否开启服务日志
        :rtype: bool
        """
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def TotalCount(self):
        """总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Machines") is not None:
            self._Machines = []
            for item in params.get("Machines"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._Machines.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._LatestAgentVersion = params.get("LatestAgentVersion")
        self._ServiceLogging = params.get("ServiceLogging")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNoticeContentsRequest(AbstractModel):
    """DescribeNoticeContents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li> name
按照【通知内容模板名称】进行过滤。
类型：String
必选：否
</li>
<li> noticeContentId
按照【通知内容模板ID】进行过滤。
类型：String
必选：否
</li>
每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """<li> name
按照【通知内容模板名称】进行过滤。
类型：String
必选：否
</li>
<li> noticeContentId
按照【通知内容模板ID】进行过滤。
类型：String
必选：否
</li>
每次请求的Filters的上限为10，Filter.Values的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
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
        


class DescribeNoticeContentsResponse(AbstractModel):
    """DescribeNoticeContents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeContents: 通知内容模板列表。
        :type NoticeContents: list of NoticeContentTemplate
        :param _TotalCount: 符合条件的通知内容模板总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NoticeContents = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NoticeContents(self):
        """通知内容模板列表。
        :rtype: list of NoticeContentTemplate
        """
        return self._NoticeContents

    @NoticeContents.setter
    def NoticeContents(self, NoticeContents):
        self._NoticeContents = NoticeContents

    @property
    def TotalCount(self):
        """符合条件的通知内容模板总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("NoticeContents") is not None:
            self._NoticeContents = []
            for item in params.get("NoticeContents"):
                obj = NoticeContentTemplate()
                obj._deserialize(item)
                self._NoticeContents.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePartitionsRequest(AbstractModel):
    """DescribePartitions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePartitionsResponse(AbstractModel):
    """DescribePartitions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 分区列表
        :type Partitions: list of PartitionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        """分区列表
        :rtype: list of PartitionInfo
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

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
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScheduledSqlInfoRequest(AbstractModel):
    """DescribeScheduledSqlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        :param _Name: 任务名称。
        :type Name: str
        :param _TaskId: 任务id。
        :type TaskId: str
        :param _Filters: <li>srcTopicName按照【源日志主题名称】进行过滤，模糊匹配。类型：String。必选：否</li>
<li>dstTopicName按照【目标日志主题名称】进行过滤，模糊匹配。类型：String。必选：否</li>
<li>srcTopicId按照【源日志主题ID】进行过滤。类型：String。必选：否</li>
<li>dstTopicId按照【目标日志主题ID】进行过滤。类型：String。必选：否</li>
<li>bizType按照【主题类型】进行过滤，0：日志主题；1：指标主题。类型：String。必选：否</li>
<li>status按照【任务状态】进行过滤，1：运行；2：停止。类型：String。必选：否</li>
<li>taskName按照【任务名称】进行过滤，模糊匹配。类型：String。必选：否</li>
<li>taskId按照【任务ID】进行过滤，模糊匹配。类型：String。必选：否</li>

        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Name = None
        self._TaskId = None
        self._Filters = None

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Name(self):
        """任务名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaskId(self):
        """任务id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Filters(self):
        """<li>srcTopicName按照【源日志主题名称】进行过滤，模糊匹配。类型：String。必选：否</li>
<li>dstTopicName按照【目标日志主题名称】进行过滤，模糊匹配。类型：String。必选：否</li>
<li>srcTopicId按照【源日志主题ID】进行过滤。类型：String。必选：否</li>
<li>dstTopicId按照【目标日志主题ID】进行过滤。类型：String。必选：否</li>
<li>bizType按照【主题类型】进行过滤，0：日志主题；1：指标主题。类型：String。必选：否</li>
<li>status按照【任务状态】进行过滤，1：运行；2：停止。类型：String。必选：否</li>
<li>taskName按照【任务名称】进行过滤，模糊匹配。类型：String。必选：否</li>
<li>taskId按照【任务ID】进行过滤，模糊匹配。类型：String。必选：否</li>

        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Name = params.get("Name")
        self._TaskId = params.get("TaskId")
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
        


class DescribeScheduledSqlInfoResponse(AbstractModel):
    """DescribeScheduledSqlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScheduledSqlTaskInfos: ScheduledSQL任务列表信息
        :type ScheduledSqlTaskInfos: list of ScheduledSqlTaskInfo
        :param _TotalCount: 任务总次数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScheduledSqlTaskInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ScheduledSqlTaskInfos(self):
        """ScheduledSQL任务列表信息
        :rtype: list of ScheduledSqlTaskInfo
        """
        return self._ScheduledSqlTaskInfos

    @ScheduledSqlTaskInfos.setter
    def ScheduledSqlTaskInfos(self, ScheduledSqlTaskInfos):
        self._ScheduledSqlTaskInfos = ScheduledSqlTaskInfos

    @property
    def TotalCount(self):
        """任务总次数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ScheduledSqlTaskInfos") is not None:
            self._ScheduledSqlTaskInfos = []
            for item in params.get("ScheduledSqlTaskInfos"):
                obj = ScheduledSqlTaskInfo()
                obj._deserialize(item)
                self._ScheduledSqlTaskInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeShipperTasksRequest(AbstractModel):
    """DescribeShipperTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        :param _StartTime: 查询的开始时间戳，支持最近3天的查询， 毫秒。
StartTime必须小于EndTime
        :type StartTime: int
        :param _EndTime: 查询的结束时间戳， 毫秒。
StartTime必须小于EndTime
        :type EndTime: int
        """
        self._ShipperId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ShipperId(self):
        """投递规则ID
        :rtype: str
        """
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def StartTime(self):
        """查询的开始时间戳，支持最近3天的查询， 毫秒。
StartTime必须小于EndTime
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询的结束时间戳， 毫秒。
StartTime必须小于EndTime
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShipperTasksResponse(AbstractModel):
    """DescribeShipperTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 投递任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ShipperTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        """投递任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ShipperTaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ShipperTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShippersRequest(AbstractModel):
    """DescribeShippers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: - shipperName：按照【投递规则名称】进行过滤。
    类型：String。
    必选：否
- shipperId：按照【投递规则ID】进行过滤。
    类型：String。
    必选：否
- topicId：按照【日志主题】进行过滤。
    类型：String。
    必选：否
- taskStatus
按照【任务运行状态】进行过滤。 支持`0`：停止，`1`：运行中，`2`：异常
类型：String
必选：否

每次请求的Filters的上限为10，Filter.Values的上限为10。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页的限制数目，默认值为20，最大值100
        :type Limit: int
        :param _PreciseSearch: 控制Filters相关字段是否为精确匹配。  0: 默认值，shipperName模糊匹配 1: shipperName 精确匹配
        :type PreciseSearch: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._PreciseSearch = None

    @property
    def Filters(self):
        """- shipperName：按照【投递规则名称】进行过滤。
    类型：String。
    必选：否
- shipperId：按照【投递规则ID】进行过滤。
    类型：String。
    必选：否
- topicId：按照【日志主题】进行过滤。
    类型：String。
    必选：否
- taskStatus
按照【任务运行状态】进行过滤。 支持`0`：停止，`1`：运行中，`2`：异常
类型：String
必选：否

每次请求的Filters的上限为10，Filter.Values的上限为10。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页的限制数目，默认值为20，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PreciseSearch(self):
        """控制Filters相关字段是否为精确匹配。  0: 默认值，shipperName模糊匹配 1: shipperName 精确匹配
        :rtype: int
        """
        return self._PreciseSearch

    @PreciseSearch.setter
    def PreciseSearch(self, PreciseSearch):
        self._PreciseSearch = PreciseSearch


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PreciseSearch = params.get("PreciseSearch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShippersResponse(AbstractModel):
    """DescribeShippers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Shippers: 投递规则列表
        :type Shippers: list of ShipperInfo
        :param _TotalCount: 本次查询获取到的总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Shippers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Shippers(self):
        """投递规则列表
        :rtype: list of ShipperInfo
        """
        return self._Shippers

    @Shippers.setter
    def Shippers(self, Shippers):
        self._Shippers = Shippers

    @property
    def TotalCount(self):
        """本次查询获取到的总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Shippers") is not None:
            self._Shippers = []
            for item in params.get("Shippers"):
                obj = ShipperInfo()
                obj._deserialize(item)
                self._Shippers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <ul><li>topicName 按照【日志主题名称】进行过滤，默认为模糊匹配，可使用 PreciseSearch 参数设置为精确匹配。类型：String。必选：否</li>
<li>logsetName 按照【日志集名称】进行过滤，默认为模糊匹配，可使用 PreciseSearch 参数设置为精确匹配。类型：String。必选：否</li>
<li>topicId 按照【日志主题ID】进行过滤。类型：String。必选：否</li>
<li>logsetId 按照【日志集ID】进行过滤，可通过调用 DescribeLogsets 查询已创建的日志集列表或登录控制台进行查看；也可以调用 CreateLogset 创建新的日志集。类型：String。必选：否</li>
<li>tagKey 按照【标签键】进行过滤。类型：String。必选：否</li>
<li>tag:tagKey 按照【标签键值对】进行过滤。tagKey 使用具体的标签键进行替换，例如 tag:exampleKey。类型：String。必选：否</li>
<li>storageType 按照【日志主题的存储类型】进行过滤。可选值 hot（标准存储），cold（低频存储）类型：String。必选：否</li></ul>
注意：每次请求的 Filters 的上限为10，Filter.Values 的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        :param _PreciseSearch: 控制Filters相关字段是否为精确匹配。
<ul><li>0: 默认值，topicName 和 logsetName 模糊匹配</li>
<li>1: topicName   精确匹配</li>
<li>2: logsetName精确匹配</li>
<li>3: topicName 和logsetName 都精确匹配</li></ul>
        :type PreciseSearch: int
        :param _BizType: 主题类型
- 0:日志主题，默认值
- 1:指标主题
        :type BizType: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._PreciseSearch = None
        self._BizType = None

    @property
    def Filters(self):
        """<ul><li>topicName 按照【日志主题名称】进行过滤，默认为模糊匹配，可使用 PreciseSearch 参数设置为精确匹配。类型：String。必选：否</li>
<li>logsetName 按照【日志集名称】进行过滤，默认为模糊匹配，可使用 PreciseSearch 参数设置为精确匹配。类型：String。必选：否</li>
<li>topicId 按照【日志主题ID】进行过滤。类型：String。必选：否</li>
<li>logsetId 按照【日志集ID】进行过滤，可通过调用 DescribeLogsets 查询已创建的日志集列表或登录控制台进行查看；也可以调用 CreateLogset 创建新的日志集。类型：String。必选：否</li>
<li>tagKey 按照【标签键】进行过滤。类型：String。必选：否</li>
<li>tag:tagKey 按照【标签键值对】进行过滤。tagKey 使用具体的标签键进行替换，例如 tag:exampleKey。类型：String。必选：否</li>
<li>storageType 按照【日志主题的存储类型】进行过滤。可选值 hot（标准存储），cold（低频存储）类型：String。必选：否</li></ul>
注意：每次请求的 Filters 的上限为10，Filter.Values 的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PreciseSearch(self):
        """控制Filters相关字段是否为精确匹配。
<ul><li>0: 默认值，topicName 和 logsetName 模糊匹配</li>
<li>1: topicName   精确匹配</li>
<li>2: logsetName精确匹配</li>
<li>3: topicName 和logsetName 都精确匹配</li></ul>
        :rtype: int
        """
        return self._PreciseSearch

    @PreciseSearch.setter
    def PreciseSearch(self, PreciseSearch):
        self._PreciseSearch = PreciseSearch

    @property
    def BizType(self):
        """主题类型
- 0:日志主题，默认值
- 1:指标主题
        :rtype: int
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PreciseSearch = params.get("PreciseSearch")
        self._BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Topics: 日志主题列表
        :type Topics: list of TopicInfo
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Topics = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Topics(self):
        """日志主题列表
        :rtype: list of TopicInfo
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def TotalCount(self):
        """总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWebCallbacksRequest(AbstractModel):
    """DescribeWebCallbacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: - name
按照【告警渠道回调配置名称】进行过滤。
类型：String
必选：否

- webCallbackId
按照【告警渠道回调配置ID】进行过滤。
类型：String
必选：否

- type
按照【告警渠道回调配置渠道类型】进行过滤。
类型：String
必选：否

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :type Filters: list of Filter
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """- name
按照【告警渠道回调配置名称】进行过滤。
类型：String
必选：否

- webCallbackId
按照【告警渠道回调配置ID】进行过滤。
类型：String
必选：否

- type
按照【告警渠道回调配置渠道类型】进行过滤。
类型：String
必选：否

每次请求的Filters的上限为10，Filter.Values的上限为100。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单页限制数目，默认值为20，最大值100。
        :rtype: int
        """
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
        


class DescribeWebCallbacksResponse(AbstractModel):
    """DescribeWebCallbacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WebCallbacks: 告警渠道回调配置列表。
        :type WebCallbacks: list of WebCallbackInfo
        :param _TotalCount: 符合条件的通知内容配置总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WebCallbacks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WebCallbacks(self):
        """告警渠道回调配置列表。
        :rtype: list of WebCallbackInfo
        """
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks

    @property
    def TotalCount(self):
        """符合条件的通知内容配置总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallbackInfo()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DynamicIndex(AbstractModel):
    """键值索引自动配置，启用后自动将日志内的字段添加到键值索引中，包括日志中后续新增的字段。

    """

    def __init__(self):
        r"""
        :param _Status: 键值索引自动配置开关
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        """键值索引自动配置开关
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EscalateNoticeInfo(AbstractModel):
    """升级通知

    """

    def __init__(self):
        r"""
        :param _NoticeReceivers: 告警通知模板接收者信息。
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: 告警通知模板回调信息。
        :type WebCallbacks: list of WebCallback
        :param _Escalate: 告警升级开关。`true`：开启告警升级、`false`：关闭告警升级，默认：false
        :type Escalate: bool
        :param _Interval: 告警升级间隔。单位：分钟，范围`[1，14400]`
        :type Interval: int
        :param _Type: 升级条件。`1`：无人认领且未恢复、`2`：未恢复，默认为1
- 无人认领且未恢复：告警没有恢复并且没有人认领则升级
- 未恢复：当前告警持续未恢复则升级

        :type Type: int
        :param _EscalateNotice: 告警升级后下一个环节的通知渠道配置，最多可配置5个环节。
        :type EscalateNotice: :class:`tencentcloud.cls.v20201016.models.EscalateNoticeInfo`
        """
        self._NoticeReceivers = None
        self._WebCallbacks = None
        self._Escalate = None
        self._Interval = None
        self._Type = None
        self._EscalateNotice = None

    @property
    def NoticeReceivers(self):
        """告警通知模板接收者信息。
        :rtype: list of NoticeReceiver
        """
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        """告警通知模板回调信息。
        :rtype: list of WebCallback
        """
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks

    @property
    def Escalate(self):
        """告警升级开关。`true`：开启告警升级、`false`：关闭告警升级，默认：false
        :rtype: bool
        """
        return self._Escalate

    @Escalate.setter
    def Escalate(self, Escalate):
        self._Escalate = Escalate

    @property
    def Interval(self):
        """告警升级间隔。单位：分钟，范围`[1，14400]`
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Type(self):
        """升级条件。`1`：无人认领且未恢复、`2`：未恢复，默认为1
- 无人认领且未恢复：告警没有恢复并且没有人认领则升级
- 未恢复：当前告警持续未恢复则升级

        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EscalateNotice(self):
        """告警升级后下一个环节的通知渠道配置，最多可配置5个环节。
        :rtype: :class:`tencentcloud.cls.v20201016.models.EscalateNoticeInfo`
        """
        return self._EscalateNotice

    @EscalateNotice.setter
    def EscalateNotice(self, EscalateNotice):
        self._EscalateNotice = EscalateNotice


    def _deserialize(self, params):
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        self._Escalate = params.get("Escalate")
        self._Interval = params.get("Interval")
        self._Type = params.get("Type")
        if params.get("EscalateNotice") is not None:
            self._EscalateNotice = EscalateNoticeInfo()
            self._EscalateNotice._deserialize(params.get("EscalateNotice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventLog(AbstractModel):
    """Windows事件日志采集配置

    """

    def __init__(self):
        r"""
        :param _EventChannel: 事件通道，支持Application，Security，Setup，System，ALL

        :type EventChannel: str
        :param _TimeType: 时间类型，1:用户自定义，2:当前时间
        :type TimeType: int
        :param _Timestamp: 时间，用户选择自定义时间类型时，需要指定时间
        :type Timestamp: int
        :param _EventIDs: 事件ID过滤列表
	
选填，为空表示不做过滤
支持正向过滤单个值（例：20）或范围（例：0-20），也支持反向过滤单个值(例：-20)
多个过滤项之间可由逗号隔开，例：1-200,-100表示采集1-200范围内除了100以外的事件日志
        :type EventIDs: list of str
        """
        self._EventChannel = None
        self._TimeType = None
        self._Timestamp = None
        self._EventIDs = None

    @property
    def EventChannel(self):
        """事件通道，支持Application，Security，Setup，System，ALL

        :rtype: str
        """
        return self._EventChannel

    @EventChannel.setter
    def EventChannel(self, EventChannel):
        self._EventChannel = EventChannel

    @property
    def TimeType(self):
        """时间类型，1:用户自定义，2:当前时间
        :rtype: int
        """
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def Timestamp(self):
        """时间，用户选择自定义时间类型时，需要指定时间
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def EventIDs(self):
        """事件ID过滤列表
	
选填，为空表示不做过滤
支持正向过滤单个值（例：20）或范围（例：0-20），也支持反向过滤单个值(例：-20)
多个过滤项之间可由逗号隔开，例：1-200,-100表示采集1-200范围内除了100以外的事件日志
        :rtype: list of str
        """
        return self._EventIDs

    @EventIDs.setter
    def EventIDs(self, EventIDs):
        self._EventIDs = EventIDs


    def _deserialize(self, params):
        self._EventChannel = params.get("EventChannel")
        self._TimeType = params.get("TimeType")
        self._Timestamp = params.get("Timestamp")
        self._EventIDs = params.get("EventIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExcludePathInfo(AbstractModel):
    """黑名单path信息

    """

    def __init__(self):
        r"""
        :param _Type: 类型，选填File或Path
        :type Type: str
        :param _Value: Type对应的具体内容
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        """类型，选填File或Path
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        """Type对应的具体内容
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInfo(AbstractModel):
    """日志导出信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _ExportId: 日志导出任务ID
        :type ExportId: str
        :param _Query: 日志导出查询语句
        :type Query: str
        :param _FileName: 日志导出文件名
        :type FileName: str
        :param _FileSize: 日志文件大小
        :type FileSize: int
        :param _Order: 日志导出时间排序
        :type Order: str
        :param _Format: 日志导出格式
        :type Format: str
        :param _Count: 日志导出数量
        :type Count: int
        :param _Status: 日志下载状态。Processing:导出正在进行中，Completed:导出完成，Failed:导出失败，Expired:日志导出已过期(三天有效期), Queuing 排队中
        :type Status: str
        :param _From: 日志导出起始时间
        :type From: int
        :param _To: 日志导出结束时间
        :type To: int
        :param _CosPath: 日志导出路径,有效期一个小时，请尽快使用该路径下载。
        :type CosPath: str
        :param _CreateTime: 日志导出创建时间
        :type CreateTime: str
        :param _SyntaxRule: 语法规则。 默认值为0。
0：Lucene语法，1：CQL语法。
        :type SyntaxRule: int
        :param _DerivedFields: 导出字段
        :type DerivedFields: list of str
        """
        self._TopicId = None
        self._ExportId = None
        self._Query = None
        self._FileName = None
        self._FileSize = None
        self._Order = None
        self._Format = None
        self._Count = None
        self._Status = None
        self._From = None
        self._To = None
        self._CosPath = None
        self._CreateTime = None
        self._SyntaxRule = None
        self._DerivedFields = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def ExportId(self):
        """日志导出任务ID
        :rtype: str
        """
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

    @property
    def Query(self):
        """日志导出查询语句
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def FileName(self):
        """日志导出文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """日志文件大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Order(self):
        """日志导出时间排序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Format(self):
        """日志导出格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Count(self):
        """日志导出数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Status(self):
        """日志下载状态。Processing:导出正在进行中，Completed:导出完成，Failed:导出失败，Expired:日志导出已过期(三天有效期), Queuing 排队中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def From(self):
        """日志导出起始时间
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """日志导出结束时间
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def CosPath(self):
        """日志导出路径,有效期一个小时，请尽快使用该路径下载。
        :rtype: str
        """
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath

    @property
    def CreateTime(self):
        """日志导出创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SyntaxRule(self):
        """语法规则。 默认值为0。
0：Lucene语法，1：CQL语法。
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule

    @property
    def DerivedFields(self):
        """导出字段
        :rtype: list of str
        """
        return self._DerivedFields

    @DerivedFields.setter
    def DerivedFields(self, DerivedFields):
        self._DerivedFields = DerivedFields


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._ExportId = params.get("ExportId")
        self._Query = params.get("Query")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._Order = params.get("Order")
        self._Format = params.get("Format")
        self._Count = params.get("Count")
        self._Status = params.get("Status")
        self._From = params.get("From")
        self._To = params.get("To")
        self._CosPath = params.get("CosPath")
        self._CreateTime = params.get("CreateTime")
        self._SyntaxRule = params.get("SyntaxRule")
        self._DerivedFields = params.get("DerivedFields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtractRuleInfo(AbstractModel):
    """日志提取规则

    """

    def __init__(self):
        r"""
        :param _TimeKey: 时间字段的key名字，TikeKey和TimeFormat必须成对出现
        :type TimeKey: str
        :param _TimeFormat: 时间字段的格式，参考c语言的strftime函数对于时间的格式说明输出参数
        :type TimeFormat: str
        :param _Delimiter: 分隔符类型日志的分隔符，只有LogType为delimiter_log时有效
        :type Delimiter: str
        :param _LogRegex: 整条日志匹配规则，只有LogType为fullregex_log时有效
        :type LogRegex: str
        :param _BeginRegex: 行首匹配规则，只有LogType为multiline_log或fullregex_log时有效
        :type BeginRegex: str
        :param _Keys: 取的每个字段的key名字，为空的key代表丢弃这个字段，只有LogType为delimiter_log时有效，json_log的日志使用json本身的key。限制100个。
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of str
        :param _FilterKeyRegex: 日志过滤规则列表（旧版），需要过滤日志的key，及其对应的regex。
 注意：2.9.3及以上版本LogListener ，建议使用AdvanceFilterRules配置日志过滤规则。

        :type FilterKeyRegex: list of KeyRegexInfo
        :param _UnMatchUpLoadSwitch: 解析失败日志是否上传，true表示上传，false表示不上传
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchUpLoadSwitch: bool
        :param _UnMatchLogKey: 失败日志的key，当UnMatchUpLoadSwitch为true时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UnMatchLogKey: str
        :param _Backtracking: 增量采集模式下的回溯数据量，默认：-1（全量采集）；其他非负数表示增量采集（从最新的位置，往前采集${Backtracking}字节（Byte）的日志）最大支持1073741824（1G）。
注意：
- COS导入不支持此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Backtracking: int
        :param _IsGBK: 是否为Gbk编码。 0：否；1：是。
注意
- 目前取0值时，表示UTF-8编码
- COS导入不支持此字段。
        :type IsGBK: int
        :param _JsonStandard: 是否为标准json。  0：否； 1：是。
- 标准json指采集器使用业界标准开源解析器进行json解析，非标json指采集器使用CLS自研json解析器进行解析，两种解析器没有本质区别，建议客户使用标准json进行解析。
注意：此字段可能返回 null，表示取不到有效值。
        :type JsonStandard: int
        :param _Protocol: syslog传输协议，取值为tcp或者udp，只有在LogType为service_syslog时生效，其余类型无需填写。
注意：
- 该字段适用于：创建采集规则配置、修改采集规则配置。
- COS导入不支持此字段。
        :type Protocol: str
        :param _Address: syslog系统日志采集指定采集器监听的地址和端口 ，形式：[ip]:[port]，只有在LogType为service_syslog时生效，其余类型无需填写。
注意：
- 该字段适用于：创建采集规则配置、修改采集规则配置。
- COS导入不支持此字段。
        :type Address: str
        :param _ParseProtocol: rfc3164：指定系统日志采集使用RFC3164协议解析日志。
rfc5424：指定系统日志采集使用RFC5424协议解析日志。
auto：自动匹配rfc3164或者rfc5424其中一种协议。
只有在LogType为service_syslog时生效，其余类型无需填写。
注意：
- 该字段适用于：创建采集规则配置、修改采集规则配置
- COS导入不支持此字段。
        :type ParseProtocol: str
        :param _MetadataType: 元数据类型。0: 不使用元数据信息；1:使用机器组元数据；2:使用用户自定义元数据；3:使用采集配置路径。
注意：
- COS导入不支持此字段。
        :type MetadataType: int
        :param _PathRegex: 采集配置路径正则表达式。

```
请用"()"标识路径中目标字段对应的正则表达式，解析时将"()"视为捕获组，并以__TAG__.{i}:{目标字段}的形式与日志一起上报，其中i为捕获组的序号。
若不希望以序号为键名，可以通过命名捕获组"(?<{键名}>{正则})"自定义键名，并以__TAG__.{键名}:{目标字段}的形式与日志一起上报。最多支持5个捕获组
```

注意：
- MetadataType为3时必填。
- COS导入不支持此字段。
        :type PathRegex: str
        :param _MetaTags: 用户自定义元数据信息。
注意：
- MetadataType为2时必填。
- COS导入不支持此字段。
        :type MetaTags: list of MetaTagInfo
        :param _EventLogRules: Windows事件日志采集规则，只有在LogType为windows_event_log时生效，其余类型无需填写。
        :type EventLogRules: list of EventLog
        :param _AdvanceFilterRules: 日志过滤规则列表（新版）。
注意：
- 2.9.3以下版本LogListener不支持， 请使用FilterKeyRegex配置日志过滤规则。
- 自建k8s采集配置（CreateConfigExtra、ModifyConfigExtra）不支持此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceFilterRules: list of AdvanceFilterRuleInfo
        """
        self._TimeKey = None
        self._TimeFormat = None
        self._Delimiter = None
        self._LogRegex = None
        self._BeginRegex = None
        self._Keys = None
        self._FilterKeyRegex = None
        self._UnMatchUpLoadSwitch = None
        self._UnMatchLogKey = None
        self._Backtracking = None
        self._IsGBK = None
        self._JsonStandard = None
        self._Protocol = None
        self._Address = None
        self._ParseProtocol = None
        self._MetadataType = None
        self._PathRegex = None
        self._MetaTags = None
        self._EventLogRules = None
        self._AdvanceFilterRules = None

    @property
    def TimeKey(self):
        """时间字段的key名字，TikeKey和TimeFormat必须成对出现
        :rtype: str
        """
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeFormat(self):
        """时间字段的格式，参考c语言的strftime函数对于时间的格式说明输出参数
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def Delimiter(self):
        """分隔符类型日志的分隔符，只有LogType为delimiter_log时有效
        :rtype: str
        """
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def LogRegex(self):
        """整条日志匹配规则，只有LogType为fullregex_log时有效
        :rtype: str
        """
        return self._LogRegex

    @LogRegex.setter
    def LogRegex(self, LogRegex):
        self._LogRegex = LogRegex

    @property
    def BeginRegex(self):
        """行首匹配规则，只有LogType为multiline_log或fullregex_log时有效
        :rtype: str
        """
        return self._BeginRegex

    @BeginRegex.setter
    def BeginRegex(self, BeginRegex):
        self._BeginRegex = BeginRegex

    @property
    def Keys(self):
        """取的每个字段的key名字，为空的key代表丢弃这个字段，只有LogType为delimiter_log时有效，json_log的日志使用json本身的key。限制100个。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def FilterKeyRegex(self):
        """日志过滤规则列表（旧版），需要过滤日志的key，及其对应的regex。
 注意：2.9.3及以上版本LogListener ，建议使用AdvanceFilterRules配置日志过滤规则。

        :rtype: list of KeyRegexInfo
        """
        return self._FilterKeyRegex

    @FilterKeyRegex.setter
    def FilterKeyRegex(self, FilterKeyRegex):
        self._FilterKeyRegex = FilterKeyRegex

    @property
    def UnMatchUpLoadSwitch(self):
        """解析失败日志是否上传，true表示上传，false表示不上传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._UnMatchUpLoadSwitch

    @UnMatchUpLoadSwitch.setter
    def UnMatchUpLoadSwitch(self, UnMatchUpLoadSwitch):
        self._UnMatchUpLoadSwitch = UnMatchUpLoadSwitch

    @property
    def UnMatchLogKey(self):
        """失败日志的key，当UnMatchUpLoadSwitch为true时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UnMatchLogKey

    @UnMatchLogKey.setter
    def UnMatchLogKey(self, UnMatchLogKey):
        self._UnMatchLogKey = UnMatchLogKey

    @property
    def Backtracking(self):
        """增量采集模式下的回溯数据量，默认：-1（全量采集）；其他非负数表示增量采集（从最新的位置，往前采集${Backtracking}字节（Byte）的日志）最大支持1073741824（1G）。
注意：
- COS导入不支持此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Backtracking

    @Backtracking.setter
    def Backtracking(self, Backtracking):
        self._Backtracking = Backtracking

    @property
    def IsGBK(self):
        """是否为Gbk编码。 0：否；1：是。
注意
- 目前取0值时，表示UTF-8编码
- COS导入不支持此字段。
        :rtype: int
        """
        return self._IsGBK

    @IsGBK.setter
    def IsGBK(self, IsGBK):
        self._IsGBK = IsGBK

    @property
    def JsonStandard(self):
        """是否为标准json。  0：否； 1：是。
- 标准json指采集器使用业界标准开源解析器进行json解析，非标json指采集器使用CLS自研json解析器进行解析，两种解析器没有本质区别，建议客户使用标准json进行解析。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JsonStandard

    @JsonStandard.setter
    def JsonStandard(self, JsonStandard):
        self._JsonStandard = JsonStandard

    @property
    def Protocol(self):
        """syslog传输协议，取值为tcp或者udp，只有在LogType为service_syslog时生效，其余类型无需填写。
注意：
- 该字段适用于：创建采集规则配置、修改采集规则配置。
- COS导入不支持此字段。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Address(self):
        """syslog系统日志采集指定采集器监听的地址和端口 ，形式：[ip]:[port]，只有在LogType为service_syslog时生效，其余类型无需填写。
注意：
- 该字段适用于：创建采集规则配置、修改采集规则配置。
- COS导入不支持此字段。
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ParseProtocol(self):
        """rfc3164：指定系统日志采集使用RFC3164协议解析日志。
rfc5424：指定系统日志采集使用RFC5424协议解析日志。
auto：自动匹配rfc3164或者rfc5424其中一种协议。
只有在LogType为service_syslog时生效，其余类型无需填写。
注意：
- 该字段适用于：创建采集规则配置、修改采集规则配置
- COS导入不支持此字段。
        :rtype: str
        """
        return self._ParseProtocol

    @ParseProtocol.setter
    def ParseProtocol(self, ParseProtocol):
        self._ParseProtocol = ParseProtocol

    @property
    def MetadataType(self):
        """元数据类型。0: 不使用元数据信息；1:使用机器组元数据；2:使用用户自定义元数据；3:使用采集配置路径。
注意：
- COS导入不支持此字段。
        :rtype: int
        """
        return self._MetadataType

    @MetadataType.setter
    def MetadataType(self, MetadataType):
        self._MetadataType = MetadataType

    @property
    def PathRegex(self):
        """采集配置路径正则表达式。

```
请用"()"标识路径中目标字段对应的正则表达式，解析时将"()"视为捕获组，并以__TAG__.{i}:{目标字段}的形式与日志一起上报，其中i为捕获组的序号。
若不希望以序号为键名，可以通过命名捕获组"(?<{键名}>{正则})"自定义键名，并以__TAG__.{键名}:{目标字段}的形式与日志一起上报。最多支持5个捕获组
```

注意：
- MetadataType为3时必填。
- COS导入不支持此字段。
        :rtype: str
        """
        return self._PathRegex

    @PathRegex.setter
    def PathRegex(self, PathRegex):
        self._PathRegex = PathRegex

    @property
    def MetaTags(self):
        """用户自定义元数据信息。
注意：
- MetadataType为2时必填。
- COS导入不支持此字段。
        :rtype: list of MetaTagInfo
        """
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags

    @property
    def EventLogRules(self):
        """Windows事件日志采集规则，只有在LogType为windows_event_log时生效，其余类型无需填写。
        :rtype: list of EventLog
        """
        return self._EventLogRules

    @EventLogRules.setter
    def EventLogRules(self, EventLogRules):
        self._EventLogRules = EventLogRules

    @property
    def AdvanceFilterRules(self):
        """日志过滤规则列表（新版）。
注意：
- 2.9.3以下版本LogListener不支持， 请使用FilterKeyRegex配置日志过滤规则。
- 自建k8s采集配置（CreateConfigExtra、ModifyConfigExtra）不支持此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AdvanceFilterRuleInfo
        """
        return self._AdvanceFilterRules

    @AdvanceFilterRules.setter
    def AdvanceFilterRules(self, AdvanceFilterRules):
        self._AdvanceFilterRules = AdvanceFilterRules


    def _deserialize(self, params):
        self._TimeKey = params.get("TimeKey")
        self._TimeFormat = params.get("TimeFormat")
        self._Delimiter = params.get("Delimiter")
        self._LogRegex = params.get("LogRegex")
        self._BeginRegex = params.get("BeginRegex")
        self._Keys = params.get("Keys")
        if params.get("FilterKeyRegex") is not None:
            self._FilterKeyRegex = []
            for item in params.get("FilterKeyRegex"):
                obj = KeyRegexInfo()
                obj._deserialize(item)
                self._FilterKeyRegex.append(obj)
        self._UnMatchUpLoadSwitch = params.get("UnMatchUpLoadSwitch")
        self._UnMatchLogKey = params.get("UnMatchLogKey")
        self._Backtracking = params.get("Backtracking")
        self._IsGBK = params.get("IsGBK")
        self._JsonStandard = params.get("JsonStandard")
        self._Protocol = params.get("Protocol")
        self._Address = params.get("Address")
        self._ParseProtocol = params.get("ParseProtocol")
        self._MetadataType = params.get("MetadataType")
        self._PathRegex = params.get("PathRegex")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        if params.get("EventLogRules") is not None:
            self._EventLogRules = []
            for item in params.get("EventLogRules"):
                obj = EventLog()
                obj._deserialize(item)
                self._EventLogRules.append(obj)
        if params.get("AdvanceFilterRules") is not None:
            self._AdvanceFilterRules = []
            for item in params.get("AdvanceFilterRules"):
                obj = AdvanceFilterRuleInfo()
                obj._deserialize(item)
                self._AdvanceFilterRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilePathInfo(AbstractModel):
    """文件路径信息

    """

    def __init__(self):
        r"""
        :param _Path: 文件路径
        :type Path: str
        :param _File: 文件名称
        :type File: str
        """
        self._Path = None
        self._File = None

    @property
    def Path(self):
        """文件路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def File(self):
        """文件名称
        :rtype: str
        """
        return self._File

    @File.setter
    def File(self, File):
        self._File = File


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param _Key: 需要过滤的字段。
        :type Key: str
        :param _Values: 需要过滤的值。
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        """需要过滤的字段。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        """需要过滤的值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterRuleInfo(AbstractModel):
    """投递日志的过滤规则

    """

    def __init__(self):
        r"""
        :param _Key: 过滤规则Key
        :type Key: str
        :param _Regex: 过滤规则
        :type Regex: str
        :param _Value: 过滤规则Value
        :type Value: str
        """
        self._Key = None
        self._Regex = None
        self._Value = None

    @property
    def Key(self):
        """过滤规则Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Regex(self):
        """过滤规则
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def Value(self):
        """过滤规则Value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Regex = params.get("Regex")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FullTextInfo(AbstractModel):
    """全文索引配置

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param _Tokenizer: 全文索引的分词符，其中的每个字符代表一个分词符；
仅支持英文符号、\n\t\r及转义符\；
注意：\n\t\r本身已被转义，直接使用双引号包裹即可作为入参，无需再次转义。使用API Explorer进行调试时请使用JSON参数输入方式，以避免\n\t\r被重复转义
        :type Tokenizer: str
        :param _ContainZH: 是否包含中文
        :type ContainZH: bool
        """
        self._CaseSensitive = None
        self._Tokenizer = None
        self._ContainZH = None

    @property
    def CaseSensitive(self):
        """是否大小写敏感
        :rtype: bool
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def Tokenizer(self):
        """全文索引的分词符，其中的每个字符代表一个分词符；
仅支持英文符号、\n\t\r及转义符\；
注意：\n\t\r本身已被转义，直接使用双引号包裹即可作为入参，无需再次转义。使用API Explorer进行调试时请使用JSON参数输入方式，以避免\n\t\r被重复转义
        :rtype: str
        """
        return self._Tokenizer

    @Tokenizer.setter
    def Tokenizer(self, Tokenizer):
        self._Tokenizer = Tokenizer

    @property
    def ContainZH(self):
        """是否包含中文
        :rtype: bool
        """
        return self._ContainZH

    @ContainZH.setter
    def ContainZH(self, ContainZH):
        self._ContainZH = ContainZH


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        self._Tokenizer = params.get("Tokenizer")
        self._ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogRequest(AbstractModel):
    """GetAlarmLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 要查询的执行详情的起始时间，Unix时间戳，单位ms。
        :type From: int
        :param _To: 要查询的执行详情的结束时间，Unix时间戳，单位ms。
        :type To: int
        :param _Query: 查询过滤条件，例如：
- 按告警策略ID查询：`alert_id:"alarm-0745ec00-e605-xxxx-b50b-54afe61fc971"`
- 按监控对象ID查询：`monitored_object:"823d8bfa-76a7-xxxx-8399-8cda74d4009b" `
- 按告警策略ID及监控对象ID查询：`alert_id:"alarm-0745ec00-e605-xxxx-b50b-54afe61fc971" AND monitored_object:"823d8bfa-76a7-xxxx-8399-8cda74d4009b"`
- 按告警策略ID及监控对象ID查询支持SQL语句：`(alert_id:"alarm-5ce45495-09e8-4d58-xxxx-768134bf330c") AND (monitored_object:"3c514e84-6f1f-46ec-xxxx-05de6163f7fe") AND NOT condition_evaluate_result: "Skip" AND condition_evaluate_result:[* TO *] | SELECT count(*) as top50StatisticsTotalCount, count_if(condition_evaluate_result='ProcessError') as top50StatisticsFailureCount, count_if(notification_send_result!='NotSend') as top50NoticeTotalCount, count_if(notification_send_result='SendPartFail' or notification_send_result='SendFail') as top50NoticeFailureCount, alert_id, alert_name, monitored_object, topic_type, happen_threshold, alert_threshold, notify_template group by alert_id, alert_name, monitored_object,topic_type, happen_threshold, alert_threshold, notify_template order by top50StatisticsTotalCount desc limit 1`
        :type Query: str
        :param _Limit: 单次查询返回的执行详情条数，最大值为1000
        :type Limit: int
        :param _Context: 透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时。
注意：
* 透传该参数时，请勿修改除该参数外的其它参数
* 仅当检索分析语句(Query)不包含SQL时有效，SQL获取后续结果参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>
        :type Context: str
        :param _Sort: 原始日志是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果排序方式参考<a href="https://cloud.tencent.com/document/product/614/58978" target="_blank">SQL ORDER BY语法</a>
        :type Sort: str
        :param _UseNewAnalysis: true：代表使用新的检索结果返回方式，输出参数AnalysisRecords和Columns有效；
false：代表使用老的检索结果返回方式，输出AnalysisResults和ColNames有效；
两种返回方式在编码格式上有少量区别，建议使用true。
        :type UseNewAnalysis: bool
        """
        self._From = None
        self._To = None
        self._Query = None
        self._Limit = None
        self._Context = None
        self._Sort = None
        self._UseNewAnalysis = None

    @property
    def From(self):
        """要查询的执行详情的起始时间，Unix时间戳，单位ms。
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """要查询的执行详情的结束时间，Unix时间戳，单位ms。
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        """查询过滤条件，例如：
- 按告警策略ID查询：`alert_id:"alarm-0745ec00-e605-xxxx-b50b-54afe61fc971"`
- 按监控对象ID查询：`monitored_object:"823d8bfa-76a7-xxxx-8399-8cda74d4009b" `
- 按告警策略ID及监控对象ID查询：`alert_id:"alarm-0745ec00-e605-xxxx-b50b-54afe61fc971" AND monitored_object:"823d8bfa-76a7-xxxx-8399-8cda74d4009b"`
- 按告警策略ID及监控对象ID查询支持SQL语句：`(alert_id:"alarm-5ce45495-09e8-4d58-xxxx-768134bf330c") AND (monitored_object:"3c514e84-6f1f-46ec-xxxx-05de6163f7fe") AND NOT condition_evaluate_result: "Skip" AND condition_evaluate_result:[* TO *] | SELECT count(*) as top50StatisticsTotalCount, count_if(condition_evaluate_result='ProcessError') as top50StatisticsFailureCount, count_if(notification_send_result!='NotSend') as top50NoticeTotalCount, count_if(notification_send_result='SendPartFail' or notification_send_result='SendFail') as top50NoticeFailureCount, alert_id, alert_name, monitored_object, topic_type, happen_threshold, alert_threshold, notify_template group by alert_id, alert_name, monitored_object,topic_type, happen_threshold, alert_threshold, notify_template order by top50StatisticsTotalCount desc limit 1`
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Limit(self):
        """单次查询返回的执行详情条数，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        """透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时。
注意：
* 透传该参数时，请勿修改除该参数外的其它参数
* 仅当检索分析语句(Query)不包含SQL时有效，SQL获取后续结果参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        """原始日志是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果排序方式参考<a href="https://cloud.tencent.com/document/product/614/58978" target="_blank">SQL ORDER BY语法</a>
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def UseNewAnalysis(self):
        """true：代表使用新的检索结果返回方式，输出参数AnalysisRecords和Columns有效；
false：代表使用老的检索结果返回方式，输出AnalysisResults和ColNames有效；
两种返回方式在编码格式上有少量区别，建议使用true。
        :rtype: bool
        """
        return self._UseNewAnalysis

    @UseNewAnalysis.setter
    def UseNewAnalysis(self, UseNewAnalysis):
        self._UseNewAnalysis = UseNewAnalysis


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        self._UseNewAnalysis = params.get("UseNewAnalysis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogResponse(AbstractModel):
    """GetAlarmLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 加载后续详情的Context
        :type Context: str
        :param _ListOver: 指定时间范围内的告警执行详情是否完整返回
        :type ListOver: bool
        :param _Analysis: 返回的结果是否为SQL分析结果
        :type Analysis: bool
        :param _ColNames: 分析结果的列名，如果Query语句有SQL查询，则返回查询字段的列名；
否则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param _Results: 执行详情查询结果。
当Query字段无SQL语句时，返回查询结果。
当Query字段有SQL语句时，可能返回null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of LogInfo
        :param _AnalysisResults: 执行详情统计分析结果。当Query字段有SQL语句时，返回SQL统计结果，否则可能返回null。

注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of LogItems
        :param _AnalysisRecords: 执行详情统计分析结果；UseNewAnalysis为true有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisRecords: list of str
        :param _Columns: 分析结果的列名， UseNewAnalysis为true有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Analysis = None
        self._ColNames = None
        self._Results = None
        self._AnalysisResults = None
        self._AnalysisRecords = None
        self._Columns = None
        self._RequestId = None

    @property
    def Context(self):
        """加载后续详情的Context
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        """指定时间范围内的告警执行详情是否完整返回
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Analysis(self):
        """返回的结果是否为SQL分析结果
        :rtype: bool
        """
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def ColNames(self):
        """分析结果的列名，如果Query语句有SQL查询，则返回查询字段的列名；
否则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ColNames

    @ColNames.setter
    def ColNames(self, ColNames):
        self._ColNames = ColNames

    @property
    def Results(self):
        """执行详情查询结果。
当Query字段无SQL语句时，返回查询结果。
当Query字段有SQL语句时，可能返回null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogInfo
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def AnalysisResults(self):
        """执行详情统计分析结果。当Query字段有SQL语句时，返回SQL统计结果，否则可能返回null。

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogItems
        """
        return self._AnalysisResults

    @AnalysisResults.setter
    def AnalysisResults(self, AnalysisResults):
        self._AnalysisResults = AnalysisResults

    @property
    def AnalysisRecords(self):
        """执行详情统计分析结果；UseNewAnalysis为true有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AnalysisRecords

    @AnalysisRecords.setter
    def AnalysisRecords(self, AnalysisRecords):
        self._AnalysisRecords = AnalysisRecords

    @property
    def Columns(self):
        """分析结果的列名， UseNewAnalysis为true有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Column
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

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
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        self._Analysis = params.get("Analysis")
        self._ColNames = params.get("ColNames")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Results.append(obj)
        if params.get("AnalysisResults") is not None:
            self._AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self._AnalysisResults.append(obj)
        self._AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._RequestId = params.get("RequestId")


class GroupTriggerConditionInfo(AbstractModel):
    """分组触发条件

    """

    def __init__(self):
        r"""
        :param _Key: 分组触发字段名称
        :type Key: str
        :param _Value: 分组触发字段值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """分组触发字段名称
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """分组触发字段值
        :rtype: str
        """
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
        


class HighLightItem(AbstractModel):
    """日志内容高亮描述信息

    """

    def __init__(self):
        r"""
        :param _Key: 高亮的日志Key
        :type Key: str
        :param _Values: 高亮的语法
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        """高亮的日志Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        """高亮的语法
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistogramInfo(AbstractModel):
    """直方图详细信息

    """

    def __init__(self):
        r"""
        :param _Count: 统计周期内的日志条数
        :type Count: int
        :param _BTime: 按 period 取整后的 unix timestamp： 单位毫秒
        :type BTime: int
        """
        self._Count = None
        self._BTime = None

    @property
    def Count(self):
        """统计周期内的日志条数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def BTime(self):
        """按 period 取整后的 unix timestamp： 单位毫秒
        :rtype: int
        """
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._BTime = params.get("BTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostFileInfo(AbstractModel):
    """自建k8s-节点文件配置信息

    """

    def __init__(self):
        r"""
        :param _LogPath: 日志文件夹
        :type LogPath: str
        :param _FilePattern: 日志文件名
        :type FilePattern: str
        :param _CustomLabels: metadata信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLabels: list of str
        """
        self._LogPath = None
        self._FilePattern = None
        self._CustomLabels = None

    @property
    def LogPath(self):
        """日志文件夹
        :rtype: str
        """
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def FilePattern(self):
        """日志文件名
        :rtype: str
        """
        return self._FilePattern

    @FilePattern.setter
    def FilePattern(self, FilePattern):
        self._FilePattern = FilePattern

    @property
    def CustomLabels(self):
        """metadata信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CustomLabels

    @CustomLabels.setter
    def CustomLabels(self, CustomLabels):
        self._CustomLabels = CustomLabels


    def _deserialize(self, params):
        self._LogPath = params.get("LogPath")
        self._FilePattern = params.get("FilePattern")
        self._CustomLabels = params.get("CustomLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JsonInfo(AbstractModel):
    """JSON类型描述

    """

    def __init__(self):
        r"""
        :param _EnableTag: 启用标志
        :type EnableTag: bool
        :param _MetaFields: 元数据信息列表, 可选值为 __SOURCE__、__FILENAME__、__TIMESTAMP__、__HOSTNAME__。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaFields: list of str
        :param _JsonType: 投递Json格式，0：字符串方式投递；1:以结构化方式投递
        :type JsonType: int
        """
        self._EnableTag = None
        self._MetaFields = None
        self._JsonType = None

    @property
    def EnableTag(self):
        """启用标志
        :rtype: bool
        """
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        """元数据信息列表, 可选值为 __SOURCE__、__FILENAME__、__TIMESTAMP__、__HOSTNAME__。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def JsonType(self):
        """投递Json格式，0：字符串方式投递；1:以结构化方式投递
        :rtype: int
        """
        return self._JsonType

    @JsonType.setter
    def JsonType(self, JsonType):
        self._JsonType = JsonType


    def _deserialize(self, params):
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._JsonType = params.get("JsonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaConsumerContent(AbstractModel):
    """kafka协议消费内容

    """

    def __init__(self):
        r"""
        :param _Format: 消费数据格式。 0：原始内容；1：JSON。
        :type Format: int
        :param _EnableTag: 是否投递 TAG 信息
Format为0时，此字段不需要赋值
        :type EnableTag: bool
        :param _MetaFields: 元数据信息列表, 可选值为：\_\_SOURCE\_\_、\_\_FILENAME\_\_
、\_\_TIMESTAMP\_\_、\_\_HOSTNAME\_\_、\_\_PKGID\_\_
Format为0时，此字段不需要赋值
        :type MetaFields: list of str
        :param _TagTransaction: tag数据处理方式：1:不平铺（默认值）；2:平铺。

不平铺示例：
TAG信息：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`
不平铺：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`

平铺示例：
TAG信息：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`
平铺：`{"__TAG__.fieldA":200,"__TAG__.fieldB":"text"}`
        :type TagTransaction: int
        :param _JsonType: 消费数据Json格式：
1：不转义（默认格式）
2：转义

投递Json格式。
JsonType为1：和原始日志一致，不转义。示例：
日志原文：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`
投递到Ckafka：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`

JsonType为2：转义。示例：
日志原文：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`
投递到Ckafka：`{"a":"aa","b":"{\"b1\":\"b1b1\", \"c1\":\"c1c1\"}"}`
        :type JsonType: int
        """
        self._Format = None
        self._EnableTag = None
        self._MetaFields = None
        self._TagTransaction = None
        self._JsonType = None

    @property
    def Format(self):
        """消费数据格式。 0：原始内容；1：JSON。
        :rtype: int
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def EnableTag(self):
        """是否投递 TAG 信息
Format为0时，此字段不需要赋值
        :rtype: bool
        """
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        """元数据信息列表, 可选值为：\_\_SOURCE\_\_、\_\_FILENAME\_\_
、\_\_TIMESTAMP\_\_、\_\_HOSTNAME\_\_、\_\_PKGID\_\_
Format为0时，此字段不需要赋值
        :rtype: list of str
        """
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def TagTransaction(self):
        """tag数据处理方式：1:不平铺（默认值）；2:平铺。

不平铺示例：
TAG信息：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`
不平铺：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`

平铺示例：
TAG信息：`{"__TAG__":{"fieldA":200,"fieldB":"text"}}`
平铺：`{"__TAG__.fieldA":200,"__TAG__.fieldB":"text"}`
        :rtype: int
        """
        return self._TagTransaction

    @TagTransaction.setter
    def TagTransaction(self, TagTransaction):
        self._TagTransaction = TagTransaction

    @property
    def JsonType(self):
        """消费数据Json格式：
1：不转义（默认格式）
2：转义

投递Json格式。
JsonType为1：和原始日志一致，不转义。示例：
日志原文：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`
投递到Ckafka：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`

JsonType为2：转义。示例：
日志原文：`{"a":"aa", "b":{"b1":"b1b1", "c1":"c1c1"}}`
投递到Ckafka：`{"a":"aa","b":"{\"b1\":\"b1b1\", \"c1\":\"c1c1\"}"}`
        :rtype: int
        """
        return self._JsonType

    @JsonType.setter
    def JsonType(self, JsonType):
        self._JsonType = JsonType


    def _deserialize(self, params):
        self._Format = params.get("Format")
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._TagTransaction = params.get("TagTransaction")
        self._JsonType = params.get("JsonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaProtocolInfo(AbstractModel):
    """Kafka访问协议

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议类型，支持的协议类型包括 plaintext、sasl_plaintext 或 sasl_ssl。建议使用 sasl_ssl，此协议会进行连接加密同时需要用户认证。
入参必填
        :type Protocol: str
        :param _Mechanism: 加密类型，支持 PLAIN、SCRAM-SHA-256 或 SCRAM-SHA-512。
当Protocol为sasl_plaintext或sasl_ssl时必填
        :type Mechanism: str
        :param _UserName: 用户名。
当Protocol为sasl_plaintext或sasl_ssl时必填
        :type UserName: str
        :param _Password: 用户密码。
当Protocol为sasl_plaintext或sasl_ssl时必填
        :type Password: str
        """
        self._Protocol = None
        self._Mechanism = None
        self._UserName = None
        self._Password = None

    @property
    def Protocol(self):
        """协议类型，支持的协议类型包括 plaintext、sasl_plaintext 或 sasl_ssl。建议使用 sasl_ssl，此协议会进行连接加密同时需要用户认证。
入参必填
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Mechanism(self):
        """加密类型，支持 PLAIN、SCRAM-SHA-256 或 SCRAM-SHA-512。
当Protocol为sasl_plaintext或sasl_ssl时必填
        :rtype: str
        """
        return self._Mechanism

    @Mechanism.setter
    def Mechanism(self, Mechanism):
        self._Mechanism = Mechanism

    @property
    def UserName(self):
        """用户名。
当Protocol为sasl_plaintext或sasl_ssl时必填
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """用户密码。
当Protocol为sasl_plaintext或sasl_ssl时必填
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Mechanism = params.get("Mechanism")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaRechargeInfo(AbstractModel):
    """Kafka导入配置信息

    """

    def __init__(self):
        r"""
        :param _Id: Kafka数据订阅配置的ID。
        :type Id: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Name: Kafka导入任务名称
        :type Name: str
        :param _KafkaType: 导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
        :type KafkaType: int
        :param _KafkaInstance: 腾讯云CKafka实例ID，KafkaType为0时必填
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接	
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议，IsEncryptionAddr参数为true时必填
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _UserKafkaTopics: 用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :type UserKafkaTopics: str
        :param _ConsumerGroupName: 用户Kafka消费组名称	
        :type ConsumerGroupName: str
        :param _Status: 状态 ，1：运行中；2：暂停。
        :type Status: int
        :param _Offset: 导入数据位置，-2:最早（默认），-1：最晚
        :type Offset: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _LogRechargeRule: 日志导入规则
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._UserKafkaTopics = None
        self._ConsumerGroupName = None
        self._Status = None
        self._Offset = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LogRechargeRule = None

    @property
    def Id(self):
        """Kafka数据订阅配置的ID。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        """Kafka导入任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        """导入Kafka类型，0: 腾讯云CKafka，1: 用户自建Kafka
        :rtype: int
        """
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        """腾讯云CKafka实例ID，KafkaType为0时必填
        :rtype: str
        """
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        """服务地址
        :rtype: str
        """
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        """ServerAddr是否为加密连接	
        :rtype: bool
        """
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        """加密访问协议，IsEncryptionAddr参数为true时必填
        :rtype: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UserKafkaTopics(self):
        """用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :rtype: str
        """
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def ConsumerGroupName(self):
        """用户Kafka消费组名称	
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def Status(self):
        """状态 ，1：运行中；2：暂停。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        """导入数据位置，-2:最早（默认），-1：最晚
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

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
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LogRechargeRule(self):
        """日志导入规则
        :rtype: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyRegexInfo(AbstractModel):
    """需要过滤日志的key，及其对应的regex

    """

    def __init__(self):
        r"""
        :param _Key: 需要过滤日志的key
        :type Key: str
        :param _Regex: key对应的过滤规则regex
        :type Regex: str
        """
        self._Key = None
        self._Regex = None

    @property
    def Key(self):
        """需要过滤日志的key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Regex(self):
        """key对应的过滤规则regex
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueInfo(AbstractModel):
    """键值或者元字段索引的字段信息

    """

    def __init__(self):
        r"""
        :param _Key: 需要配置键值或者元字段索引的字段名称，仅支持字母、数字、下划线和-./@，且不能以下划线开头

注意：
1，元字段（tag）的Key无需额外添加`__TAG__.`前缀，与上传日志时对应的字段Key一致即可，腾讯云控制台展示时将自动添加`__TAG__.`前缀
2，键值索引（KeyValue）及元字段索引（Tag）中的Key总数不能超过300
3，Key的层级不能超过10层，例如a.b.c.d.e.f.g.h.j.k
4，不允许同时包含json父子级字段，例如a及a.b
        :type Key: str
        :param _Value: 字段的索引描述信息
        :type Value: :class:`tencentcloud.cls.v20201016.models.ValueInfo`
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """需要配置键值或者元字段索引的字段名称，仅支持字母、数字、下划线和-./@，且不能以下划线开头

注意：
1，元字段（tag）的Key无需额外添加`__TAG__.`前缀，与上传日志时对应的字段Key一致即可，腾讯云控制台展示时将自动添加`__TAG__.`前缀
2，键值索引（KeyValue）及元字段索引（Tag）中的Key总数不能超过300
3，Key的层级不能超过10层，例如a.b.c.d.e.f.g.h.j.k
4，不允许同时包含json父子级字段，例如a及a.b
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """字段的索引描述信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.ValueInfo`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = ValueInfo()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogContextInfo(AbstractModel):
    """日志上下文信息

    """

    def __init__(self):
        r"""
        :param _Source: 日志来源设备
        :type Source: str
        :param _Filename: 采集路径
        :type Filename: str
        :param _Content: 日志内容
        :type Content: str
        :param _PkgId: 日志包序号
        :type PkgId: str
        :param _PkgLogId: 日志包内一条日志的序号
        :type PkgLogId: int
        :param _BTime: 日志时间戳
        :type BTime: int
        :param _HostName: 日志来源主机名称
        :type HostName: str
        :param _RawLog: 原始日志(仅在日志创建索引异常时有值)
        :type RawLog: str
        :param _IndexStatus: 日志创建索引异常原因(仅在日志创建索引异常时有值)
        :type IndexStatus: str
        :param _HighLights: 日志内容的高亮描述信息
        :type HighLights: list of HighLightItem
        """
        self._Source = None
        self._Filename = None
        self._Content = None
        self._PkgId = None
        self._PkgLogId = None
        self._BTime = None
        self._HostName = None
        self._RawLog = None
        self._IndexStatus = None
        self._HighLights = None

    @property
    def Source(self):
        """日志来源设备
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Filename(self):
        """采集路径
        :rtype: str
        """
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def Content(self):
        """日志内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def PkgId(self):
        """日志包序号
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        """日志包内一条日志的序号
        :rtype: int
        """
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def BTime(self):
        """日志时间戳
        :rtype: int
        """
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime

    @property
    def HostName(self):
        """日志来源主机名称
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RawLog(self):
        """原始日志(仅在日志创建索引异常时有值)
        :rtype: str
        """
        return self._RawLog

    @RawLog.setter
    def RawLog(self, RawLog):
        self._RawLog = RawLog

    @property
    def IndexStatus(self):
        """日志创建索引异常原因(仅在日志创建索引异常时有值)
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus

    @property
    def HighLights(self):
        """日志内容的高亮描述信息
        :rtype: list of HighLightItem
        """
        return self._HighLights

    @HighLights.setter
    def HighLights(self, HighLights):
        self._HighLights = HighLights


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Filename = params.get("Filename")
        self._Content = params.get("Content")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._BTime = params.get("BTime")
        self._HostName = params.get("HostName")
        self._RawLog = params.get("RawLog")
        self._IndexStatus = params.get("IndexStatus")
        if params.get("HighLights") is not None:
            self._HighLights = []
            for item in params.get("HighLights"):
                obj = HighLightItem()
                obj._deserialize(item)
                self._HighLights.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """日志结果信息

    """

    def __init__(self):
        r"""
        :param _Time: 日志时间，单位ms
        :type Time: int
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _Source: 日志来源IP
        :type Source: str
        :param _FileName: 日志文件名称
        :type FileName: str
        :param _PkgId: 日志上报请求包的ID
        :type PkgId: str
        :param _PkgLogId: 请求包内日志的ID
        :type PkgLogId: str
        :param _LogJson: 日志内容的Json序列化字符串
        :type LogJson: str
        :param _HostName: 日志来源主机名称
        :type HostName: str
        :param _RawLog: 原始日志(仅在日志创建索引异常时有值)
        :type RawLog: str
        :param _IndexStatus: 日志创建索引异常原因(仅在日志创建索引异常时有值)
        :type IndexStatus: str
        """
        self._Time = None
        self._TopicId = None
        self._TopicName = None
        self._Source = None
        self._FileName = None
        self._PkgId = None
        self._PkgLogId = None
        self._LogJson = None
        self._HostName = None
        self._RawLog = None
        self._IndexStatus = None

    @property
    def Time(self):
        """日志时间，单位ms
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """日志主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Source(self):
        """日志来源IP
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def FileName(self):
        """日志文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def PkgId(self):
        """日志上报请求包的ID
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        """请求包内日志的ID
        :rtype: str
        """
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def LogJson(self):
        """日志内容的Json序列化字符串
        :rtype: str
        """
        return self._LogJson

    @LogJson.setter
    def LogJson(self, LogJson):
        self._LogJson = LogJson

    @property
    def HostName(self):
        """日志来源主机名称
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RawLog(self):
        """原始日志(仅在日志创建索引异常时有值)
        :rtype: str
        """
        return self._RawLog

    @RawLog.setter
    def RawLog(self, RawLog):
        self._RawLog = RawLog

    @property
    def IndexStatus(self):
        """日志创建索引异常原因(仅在日志创建索引异常时有值)
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Source = params.get("Source")
        self._FileName = params.get("FileName")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._LogJson = params.get("LogJson")
        self._HostName = params.get("HostName")
        self._RawLog = params.get("RawLog")
        self._IndexStatus = params.get("IndexStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogItem(AbstractModel):
    """日志中的KV对

    """

    def __init__(self):
        r"""
        :param _Key: 日志Key
        :type Key: str
        :param _Value: 日志Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """日志Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """日志Value
        :rtype: str
        """
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
        


class LogItems(AbstractModel):
    """LogItem的数组

    """

    def __init__(self):
        r"""
        :param _Data: 分析结果返回的KV数据对
        :type Data: list of LogItem
        """
        self._Data = None

    @property
    def Data(self):
        """分析结果返回的KV数据对
        :rtype: list of LogItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = LogItem()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogRechargeRuleInfo(AbstractModel):
    """日志导入规则

    """

    def __init__(self):
        r"""
        :param _RechargeType: 导入类型，支持json_log：json格式日志，minimalist_log: 单行全文，fullregex_log: 单行完全正则
        :type RechargeType: str
        :param _EncodingFormat: 解析编码格式，0: UTF-8（默认值），1: GBK
        :type EncodingFormat: int
        :param _DefaultTimeSwitch: 使用默认时间，true：开启（默认值）， flase：关闭
        :type DefaultTimeSwitch: bool
        :param _LogRegex: 整条日志匹配规则，只有RechargeType为fullregex_log时有效
        :type LogRegex: str
        :param _UnMatchLogSwitch: 解析失败日志是否上传，true表示上传，false表示不上传
        :type UnMatchLogSwitch: bool
        :param _UnMatchLogKey: 解析失败日志的键名称
        :type UnMatchLogKey: str
        :param _UnMatchLogTimeSrc: 解析失败日志时间来源，0: 系统当前时间，1: Kafka消息时间戳
        :type UnMatchLogTimeSrc: int
        :param _DefaultTimeSrc: 默认时间来源，0: 系统当前时间，1: Kafka消息时间戳
        :type DefaultTimeSrc: int
        :param _TimeKey: 时间字段
        :type TimeKey: str
        :param _TimeRegex: 时间提取正则表达式
        :type TimeRegex: str
        :param _TimeFormat: 时间字段格式
        :type TimeFormat: str
        :param _TimeZone: 时间字段时区
        :type TimeZone: str
        :param _Metadata: 元数据信息，Kafka导入支持kafka_topic,kafka_partition,kafka_offset,kafka_timestamp
        :type Metadata: list of str
        :param _Keys: 日志Key列表，RechargeType为full_regex_log时必填
        :type Keys: list of str
        :param _ParseArray: json解析模式，开启首层数据解析
        :type ParseArray: bool
        """
        self._RechargeType = None
        self._EncodingFormat = None
        self._DefaultTimeSwitch = None
        self._LogRegex = None
        self._UnMatchLogSwitch = None
        self._UnMatchLogKey = None
        self._UnMatchLogTimeSrc = None
        self._DefaultTimeSrc = None
        self._TimeKey = None
        self._TimeRegex = None
        self._TimeFormat = None
        self._TimeZone = None
        self._Metadata = None
        self._Keys = None
        self._ParseArray = None

    @property
    def RechargeType(self):
        """导入类型，支持json_log：json格式日志，minimalist_log: 单行全文，fullregex_log: 单行完全正则
        :rtype: str
        """
        return self._RechargeType

    @RechargeType.setter
    def RechargeType(self, RechargeType):
        self._RechargeType = RechargeType

    @property
    def EncodingFormat(self):
        """解析编码格式，0: UTF-8（默认值），1: GBK
        :rtype: int
        """
        return self._EncodingFormat

    @EncodingFormat.setter
    def EncodingFormat(self, EncodingFormat):
        self._EncodingFormat = EncodingFormat

    @property
    def DefaultTimeSwitch(self):
        """使用默认时间，true：开启（默认值）， flase：关闭
        :rtype: bool
        """
        return self._DefaultTimeSwitch

    @DefaultTimeSwitch.setter
    def DefaultTimeSwitch(self, DefaultTimeSwitch):
        self._DefaultTimeSwitch = DefaultTimeSwitch

    @property
    def LogRegex(self):
        """整条日志匹配规则，只有RechargeType为fullregex_log时有效
        :rtype: str
        """
        return self._LogRegex

    @LogRegex.setter
    def LogRegex(self, LogRegex):
        self._LogRegex = LogRegex

    @property
    def UnMatchLogSwitch(self):
        """解析失败日志是否上传，true表示上传，false表示不上传
        :rtype: bool
        """
        return self._UnMatchLogSwitch

    @UnMatchLogSwitch.setter
    def UnMatchLogSwitch(self, UnMatchLogSwitch):
        self._UnMatchLogSwitch = UnMatchLogSwitch

    @property
    def UnMatchLogKey(self):
        """解析失败日志的键名称
        :rtype: str
        """
        return self._UnMatchLogKey

    @UnMatchLogKey.setter
    def UnMatchLogKey(self, UnMatchLogKey):
        self._UnMatchLogKey = UnMatchLogKey

    @property
    def UnMatchLogTimeSrc(self):
        """解析失败日志时间来源，0: 系统当前时间，1: Kafka消息时间戳
        :rtype: int
        """
        return self._UnMatchLogTimeSrc

    @UnMatchLogTimeSrc.setter
    def UnMatchLogTimeSrc(self, UnMatchLogTimeSrc):
        self._UnMatchLogTimeSrc = UnMatchLogTimeSrc

    @property
    def DefaultTimeSrc(self):
        """默认时间来源，0: 系统当前时间，1: Kafka消息时间戳
        :rtype: int
        """
        return self._DefaultTimeSrc

    @DefaultTimeSrc.setter
    def DefaultTimeSrc(self, DefaultTimeSrc):
        self._DefaultTimeSrc = DefaultTimeSrc

    @property
    def TimeKey(self):
        """时间字段
        :rtype: str
        """
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeRegex(self):
        """时间提取正则表达式
        :rtype: str
        """
        return self._TimeRegex

    @TimeRegex.setter
    def TimeRegex(self, TimeRegex):
        self._TimeRegex = TimeRegex

    @property
    def TimeFormat(self):
        """时间字段格式
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def TimeZone(self):
        """时间字段时区
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def Metadata(self):
        """元数据信息，Kafka导入支持kafka_topic,kafka_partition,kafka_offset,kafka_timestamp
        :rtype: list of str
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def Keys(self):
        """日志Key列表，RechargeType为full_regex_log时必填
        :rtype: list of str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def ParseArray(self):
        """json解析模式，开启首层数据解析
        :rtype: bool
        """
        return self._ParseArray

    @ParseArray.setter
    def ParseArray(self, ParseArray):
        self._ParseArray = ParseArray


    def _deserialize(self, params):
        self._RechargeType = params.get("RechargeType")
        self._EncodingFormat = params.get("EncodingFormat")
        self._DefaultTimeSwitch = params.get("DefaultTimeSwitch")
        self._LogRegex = params.get("LogRegex")
        self._UnMatchLogSwitch = params.get("UnMatchLogSwitch")
        self._UnMatchLogKey = params.get("UnMatchLogKey")
        self._UnMatchLogTimeSrc = params.get("UnMatchLogTimeSrc")
        self._DefaultTimeSrc = params.get("DefaultTimeSrc")
        self._TimeKey = params.get("TimeKey")
        self._TimeRegex = params.get("TimeRegex")
        self._TimeFormat = params.get("TimeFormat")
        self._TimeZone = params.get("TimeZone")
        self._Metadata = params.get("Metadata")
        self._Keys = params.get("Keys")
        self._ParseArray = params.get("ParseArray")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogsetInfo(AbstractModel):
    """日志集相关信息

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _LogsetName: 日志集名称
        :type LogsetName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AssumerName: 云产品标识，日志集由其它云产品创建时，该字段会显示云产品名称，例如CDN、TKE
        :type AssumerName: str
        :param _Tags: 日志集绑定的标签
        :type Tags: list of Tag
        :param _TopicCount: 日志集下日志主题的数目
        :type TopicCount: int
        :param _RoleName: 若AssumerName非空，则表示创建该日志集的服务方角色
        :type RoleName: str
        """
        self._LogsetId = None
        self._LogsetName = None
        self._CreateTime = None
        self._AssumerName = None
        self._Tags = None
        self._TopicCount = None
        self._RoleName = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        """日志集名称
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

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
    def AssumerName(self):
        """云产品标识，日志集由其它云产品创建时，该字段会显示云产品名称，例如CDN、TKE
        :rtype: str
        """
        return self._AssumerName

    @AssumerName.setter
    def AssumerName(self, AssumerName):
        self._AssumerName = AssumerName

    @property
    def Tags(self):
        """日志集绑定的标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TopicCount(self):
        """日志集下日志主题的数目
        :rtype: int
        """
        return self._TopicCount

    @TopicCount.setter
    def TopicCount(self, TopicCount):
        self._TopicCount = TopicCount

    @property
    def RoleName(self):
        """若AssumerName非空，则表示创建该日志集的服务方角色
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._CreateTime = params.get("CreateTime")
        self._AssumerName = params.get("AssumerName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TopicCount = params.get("TopicCount")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupInfo(AbstractModel):
    """机器组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _GroupName: 机器组名称
        :type GroupName: str
        :param _MachineGroupType: 机器组类型
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Tags: 机器组绑定的标签列表
        :type Tags: list of Tag
        :param _AutoUpdate: 是否开启机器组自动更新
        :type AutoUpdate: str
        :param _UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
        :type UpdateStartTime: str
        :param _UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
        :type UpdateEndTime: str
        :param _ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
        :type ServiceLogging: bool
        :param _DelayCleanupTime: 机器组中机器离线定期清理时间
        :type DelayCleanupTime: int
        :param _MetaTags: 机器组元数据信息列表
        :type MetaTags: list of MetaTagInfo
        :param _OSType: 操作系统类型，0: Linux，1: windows
        :type OSType: int
        """
        self._GroupId = None
        self._GroupName = None
        self._MachineGroupType = None
        self._CreateTime = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._DelayCleanupTime = None
        self._MetaTags = None
        self._OSType = None

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """机器组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        """机器组类型
        :rtype: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

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
    def Tags(self):
        """机器组绑定的标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        """是否开启机器组自动更新
        :rtype: str
        """
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        """升级开始时间，建议业务低峰期升级LogListener
        :rtype: str
        """
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        """升级结束时间，建议业务低峰期升级LogListener
        :rtype: str
        """
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        """是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
        :rtype: bool
        """
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def DelayCleanupTime(self):
        """机器组中机器离线定期清理时间
        :rtype: int
        """
        return self._DelayCleanupTime

    @DelayCleanupTime.setter
    def DelayCleanupTime(self, DelayCleanupTime):
        self._DelayCleanupTime = DelayCleanupTime

    @property
    def MetaTags(self):
        """机器组元数据信息列表
        :rtype: list of MetaTagInfo
        """
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags

    @property
    def OSType(self):
        """操作系统类型，0: Linux，1: windows
        :rtype: int
        """
        return self._OSType

    @OSType.setter
    def OSType(self, OSType):
        self._OSType = OSType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        self._CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        self._DelayCleanupTime = params.get("DelayCleanupTime")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        self._OSType = params.get("OSType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupTypeInfo(AbstractModel):
    """机器组类型描述

    """

    def __init__(self):
        r"""
        :param _Type: 机器组类型。支持 ip 和 label。
- ip：表示该机器组Values中存的是采集机器的ip地址
- label：表示该机器组Values中存储的是机器的标签
        :type Type: str
        :param _Values: 机器描述列表。
        :type Values: list of str
        """
        self._Type = None
        self._Values = None

    @property
    def Type(self):
        """机器组类型。支持 ip 和 label。
- ip：表示该机器组Values中存的是采集机器的ip地址
- label：表示该机器组Values中存储的是机器的标签
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Values(self):
        """机器描述列表。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineInfo(AbstractModel):
    """机器状态信息

    """

    def __init__(self):
        r"""
        :param _Ip: 机器的IP
        :type Ip: str
        :param _InstanceID: 机器实例ID
        :type InstanceID: str
        :param _Status: 机器状态，0:异常，1:正常
        :type Status: int
        :param _OfflineTime: 机器离线时间，空为正常，异常返回具体时间
        :type OfflineTime: str
        :param _AutoUpdate: 机器是否开启自动升级。0:关闭，1:开启
        :type AutoUpdate: int
        :param _Version: 机器当前版本号。
        :type Version: str
        :param _UpdateStatus: 机器升级功能状态。 0：升级成功；1：升级中；-1：升级失败。
        :type UpdateStatus: int
        :param _ErrCode: 机器升级结果标识。
0：成功；1200：升级成功；其他值表示异常。
        :type ErrCode: int
        :param _ErrMsg: 机器升级结果信息。
“ok”：成功；“update success”：升级成功；其他值为失败原因。
        :type ErrMsg: str
        """
        self._Ip = None
        self._InstanceID = None
        self._Status = None
        self._OfflineTime = None
        self._AutoUpdate = None
        self._Version = None
        self._UpdateStatus = None
        self._ErrCode = None
        self._ErrMsg = None

    @property
    def Ip(self):
        """机器的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def InstanceID(self):
        """机器实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Status(self):
        """机器状态，0:异常，1:正常
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OfflineTime(self):
        """机器离线时间，空为正常，异常返回具体时间
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def AutoUpdate(self):
        """机器是否开启自动升级。0:关闭，1:开启
        :rtype: int
        """
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def Version(self):
        """机器当前版本号。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UpdateStatus(self):
        """机器升级功能状态。 0：升级成功；1：升级中；-1：升级失败。
        :rtype: int
        """
        return self._UpdateStatus

    @UpdateStatus.setter
    def UpdateStatus(self, UpdateStatus):
        self._UpdateStatus = UpdateStatus

    @property
    def ErrCode(self):
        """机器升级结果标识。
0：成功；1200：升级成功；其他值表示异常。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """机器升级结果信息。
“ok”：成功；“update success”：升级成功；其他值为失败原因。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._InstanceID = params.get("InstanceID")
        self._Status = params.get("Status")
        self._OfflineTime = params.get("OfflineTime")
        self._AutoUpdate = params.get("AutoUpdate")
        self._Version = params.get("Version")
        self._UpdateStatus = params.get("UpdateStatus")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionRequest(AbstractModel):
    """MergePartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _PartitionId: 合并的PartitionId（找到下一个分区InclusiveBeginKey与入参PartitionId对应的ExclusiveEndKey相等，且找到的分区必须是读写分区（Staus:readwrite），入参PartitionId与找到的PartitionId设置为只读分区（Status:readonly）,再新建一个新的读写分区） 。[获取分区列表](https://cloud.tencent.com/document/product/614/56469)

1. 入参PartitionId只能是读写分区（Status的值有readonly，readwrite），且能找到入参PartitionId的下一个可读写分区（找到下一个分区InclusiveBeginKey与入参PartitionId对应的ExclusiveEndKey相等）；
2. 入参PartitionId不能是最后一个分区（PartitionId的ExclusiveEndKey不能是ffffffffffffffffffffffffffffffff）；
3. topic的分区数量是有限制的（默认50个），合并之后不能超过最大分区，否则不能合并。
        :type PartitionId: int
        """
        self._TopicId = None
        self._PartitionId = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionId(self):
        """合并的PartitionId（找到下一个分区InclusiveBeginKey与入参PartitionId对应的ExclusiveEndKey相等，且找到的分区必须是读写分区（Staus:readwrite），入参PartitionId与找到的PartitionId设置为只读分区（Status:readonly）,再新建一个新的读写分区） 。[获取分区列表](https://cloud.tencent.com/document/product/614/56469)

1. 入参PartitionId只能是读写分区（Status的值有readonly，readwrite），且能找到入参PartitionId的下一个可读写分区（找到下一个分区InclusiveBeginKey与入参PartitionId对应的ExclusiveEndKey相等）；
2. 入参PartitionId不能是最后一个分区（PartitionId的ExclusiveEndKey不能是ffffffffffffffffffffffffffffffff）；
3. topic的分区数量是有限制的（默认50个），合并之后不能超过最大分区，否则不能合并。
        :rtype: int
        """
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionResponse(AbstractModel):
    """MergePartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 合并结果集
        :type Partitions: list of PartitionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        """合并结果集
        :rtype: list of PartitionInfo
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

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
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class MetaTagInfo(AbstractModel):
    """元数据信息

    """

    def __init__(self):
        r"""
        :param _Key: 元数据key
        :type Key: str
        :param _Value: 元数据value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """元数据key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """元数据value
        :rtype: str
        """
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
        


class MetricLabel(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param _Key: 指标名称
        :type Key: str
        :param _Value: 指标内容
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """指标名称
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """指标内容
        :rtype: str
        """
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
        


class ModifyAlarmNoticeRequest(AbstractModel):
    """ModifyAlarmNotice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: 通知渠道组ID。
        :type AlarmNoticeId: str
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的通知渠道组。最大支持10个标签键值对，并且不能有重复的键值对。
        :type Tags: list of Tag
        :param _Name: 通知渠道组名称。
        :type Name: str
        :param _Type: 通知类型。可选值：
<li> Trigger - 告警触发</li>
<li> Recovery - 告警恢复</li>
<li> All - 告警触发和告警恢复</li>
        :type Type: str
        :param _NoticeReceivers: 通知接收对象。
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: 接口回调信息（包括企业微信等）。
        :type WebCallbacks: list of WebCallback
        :param _NoticeRules: 通知规则。

注意: 

- Type、NoticeReceivers和WebCallbacks是一组配置，NoticeRules是另一组配置，2组配置互斥。
- 传其中一组数据，则另一组数据置空。
        :type NoticeRules: list of NoticeRule
        :param _JumpDomain: 调用链接域名。http:// 或者 https:// 开头，不能/结尾
        :type JumpDomain: str
        :param _DeliverStatus: 投递日志开关。

参数值：
1：关闭；

2：开启 

        :type DeliverStatus: int
        :param _DeliverConfig: 投递日志配置。
        :type DeliverConfig: :class:`tencentcloud.cls.v20201016.models.DeliverConfig`
        :param _AlarmShieldStatus: 免登录操作告警开关。

参数值： 
        1：关闭
        2：开启（默认开启）
        :type AlarmShieldStatus: int
        """
        self._AlarmNoticeId = None
        self._Tags = None
        self._Name = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None
        self._NoticeRules = None
        self._JumpDomain = None
        self._DeliverStatus = None
        self._DeliverConfig = None
        self._AlarmShieldStatus = None

    @property
    def AlarmNoticeId(self):
        """通知渠道组ID。
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def Tags(self):
        """标签描述列表，通过指定该参数可以同时绑定标签到相应的通知渠道组。最大支持10个标签键值对，并且不能有重复的键值对。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Name(self):
        """通知渠道组名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """通知类型。可选值：
<li> Trigger - 告警触发</li>
<li> Recovery - 告警恢复</li>
<li> All - 告警触发和告警恢复</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeReceivers(self):
        """通知接收对象。
        :rtype: list of NoticeReceiver
        """
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        """接口回调信息（包括企业微信等）。
        :rtype: list of WebCallback
        """
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks

    @property
    def NoticeRules(self):
        """通知规则。

注意: 

- Type、NoticeReceivers和WebCallbacks是一组配置，NoticeRules是另一组配置，2组配置互斥。
- 传其中一组数据，则另一组数据置空。
        :rtype: list of NoticeRule
        """
        return self._NoticeRules

    @NoticeRules.setter
    def NoticeRules(self, NoticeRules):
        self._NoticeRules = NoticeRules

    @property
    def JumpDomain(self):
        """调用链接域名。http:// 或者 https:// 开头，不能/结尾
        :rtype: str
        """
        return self._JumpDomain

    @JumpDomain.setter
    def JumpDomain(self, JumpDomain):
        self._JumpDomain = JumpDomain

    @property
    def DeliverStatus(self):
        """投递日志开关。

参数值：
1：关闭；

2：开启 

        :rtype: int
        """
        return self._DeliverStatus

    @DeliverStatus.setter
    def DeliverStatus(self, DeliverStatus):
        self._DeliverStatus = DeliverStatus

    @property
    def DeliverConfig(self):
        """投递日志配置。
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeliverConfig`
        """
        return self._DeliverConfig

    @DeliverConfig.setter
    def DeliverConfig(self, DeliverConfig):
        self._DeliverConfig = DeliverConfig

    @property
    def AlarmShieldStatus(self):
        """免登录操作告警开关。

参数值： 
        1：关闭
        2：开启（默认开启）
        :rtype: int
        """
        return self._AlarmShieldStatus

    @AlarmShieldStatus.setter
    def AlarmShieldStatus(self, AlarmShieldStatus):
        self._AlarmShieldStatus = AlarmShieldStatus


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        if params.get("NoticeRules") is not None:
            self._NoticeRules = []
            for item in params.get("NoticeRules"):
                obj = NoticeRule()
                obj._deserialize(item)
                self._NoticeRules.append(obj)
        self._JumpDomain = params.get("JumpDomain")
        self._DeliverStatus = params.get("DeliverStatus")
        if params.get("DeliverConfig") is not None:
            self._DeliverConfig = DeliverConfig()
            self._DeliverConfig._deserialize(params.get("DeliverConfig"))
        self._AlarmShieldStatus = params.get("AlarmShieldStatus")
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
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAlarmRequest(AbstractModel):
    """ModifyAlarm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmId: 告警策略ID。
        :type AlarmId: str
        :param _Name: 告警策略名称
        :type Name: str
        :param _MonitorTime: 监控任务运行时间点。
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _Condition: 触发条件。

注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。
        :type Condition: str
        :param _AlarmLevel: 告警级别。

0:警告(Warn);1:提醒(Info);2:紧急 (Critical)

注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。
        :type AlarmLevel: int
        :param _MultiConditions: 多触发条件。 

注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。
        :type MultiConditions: list of MultiCondition
        :param _TriggerCount: 持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为2000。
        :type TriggerCount: int
        :param _AlarmPeriod: 告警重复的周期。单位是分钟。取值范围是0~1440。
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: 关联的告警通知模板列表。
        :type AlarmNoticeIds: list of str
        :param _AlarmTargets: 监控对象列表。
        :type AlarmTargets: list of AlarmTarget
        :param _Status: 是否开启告警策略。
        :type Status: bool
        :param _Enable: 该参数已废弃，请使用Status参数控制是否开启告警策略。
        :type Enable: bool
        :param _MessageTemplate: 用户自定义告警内容
        :type MessageTemplate: str
        :param _CallBack: 用户自定义回调
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: 多维分析
        :type Analysis: list of AnalysisDimensional
        :param _GroupTriggerStatus: 分组触发状态。true：开启，false：关闭（默认）
        :type GroupTriggerStatus: bool
        :param _GroupTriggerCondition: 分组触发条件。
        :type GroupTriggerCondition: list of str
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的告警策略。最大支持10个标签键值对，并且不能有重复的键值对。
        :type Tags: list of Tag
        :param _MonitorObjectType: 监控对象类型。0:执行语句共用监控对象; 1:每个执行语句单独选择监控对象。 
当值为1时，AlarmTargets元素个数不能超过10个，AlarmTargets中的Number必须是从1开始的连续正整数，不能重复。

        :type MonitorObjectType: int
        :param _Classifications: 告警附加分类信息列表。
Classifications元素个数不能超过20个。
Classifications元素的Key不能为空，不能重复，长度不能超过50个字符，符合正则 `^[a-z]([a-z0-9_]{0,49})$`。
Classifications元素的Value长度不能超过200个字符。
        :type Classifications: list of AlarmClassification
        """
        self._AlarmId = None
        self._Name = None
        self._MonitorTime = None
        self._Condition = None
        self._AlarmLevel = None
        self._MultiConditions = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._AlarmTargets = None
        self._Status = None
        self._Enable = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None
        self._GroupTriggerStatus = None
        self._GroupTriggerCondition = None
        self._Tags = None
        self._MonitorObjectType = None
        self._Classifications = None

    @property
    def AlarmId(self):
        """告警策略ID。
        :rtype: str
        """
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def Name(self):
        """告警策略名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MonitorTime(self):
        """监控任务运行时间点。
        :rtype: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        """
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def Condition(self):
        """触发条件。

注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def AlarmLevel(self):
        """告警级别。

0:警告(Warn);1:提醒(Info);2:紧急 (Critical)

注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def MultiConditions(self):
        """多触发条件。 

注意:  
- Condition和AlarmLevel是一组配置，MultiConditions是另一组配置，2组配置互斥。
        :rtype: list of MultiCondition
        """
        return self._MultiConditions

    @MultiConditions.setter
    def MultiConditions(self, MultiConditions):
        self._MultiConditions = MultiConditions

    @property
    def TriggerCount(self):
        """持续周期。持续满足触发条件TriggerCount个周期后，再进行告警；最小值为1，最大值为2000。
        :rtype: int
        """
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        """告警重复的周期。单位是分钟。取值范围是0~1440。
        :rtype: int
        """
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        """关联的告警通知模板列表。
        :rtype: list of str
        """
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def AlarmTargets(self):
        """监控对象列表。
        :rtype: list of AlarmTarget
        """
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def Status(self):
        """是否开启告警策略。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        """该参数已废弃，请使用Status参数控制是否开启告警策略。
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def MessageTemplate(self):
        """用户自定义告警内容
        :rtype: str
        """
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        """用户自定义回调
        :rtype: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        """
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        """多维分析
        :rtype: list of AnalysisDimensional
        """
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def GroupTriggerStatus(self):
        """分组触发状态。true：开启，false：关闭（默认）
        :rtype: bool
        """
        return self._GroupTriggerStatus

    @GroupTriggerStatus.setter
    def GroupTriggerStatus(self, GroupTriggerStatus):
        self._GroupTriggerStatus = GroupTriggerStatus

    @property
    def GroupTriggerCondition(self):
        """分组触发条件。
        :rtype: list of str
        """
        return self._GroupTriggerCondition

    @GroupTriggerCondition.setter
    def GroupTriggerCondition(self, GroupTriggerCondition):
        self._GroupTriggerCondition = GroupTriggerCondition

    @property
    def Tags(self):
        """标签描述列表，通过指定该参数可以同时绑定标签到相应的告警策略。最大支持10个标签键值对，并且不能有重复的键值对。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MonitorObjectType(self):
        """监控对象类型。0:执行语句共用监控对象; 1:每个执行语句单独选择监控对象。 
当值为1时，AlarmTargets元素个数不能超过10个，AlarmTargets中的Number必须是从1开始的连续正整数，不能重复。

        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def Classifications(self):
        """告警附加分类信息列表。
Classifications元素个数不能超过20个。
Classifications元素的Key不能为空，不能重复，长度不能超过50个字符，符合正则 `^[a-z]([a-z0-9_]{0,49})$`。
Classifications元素的Value长度不能超过200个字符。
        :rtype: list of AlarmClassification
        """
        return self._Classifications

    @Classifications.setter
    def Classifications(self, Classifications):
        self._Classifications = Classifications


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        self._Name = params.get("Name")
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._Condition = params.get("Condition")
        self._AlarmLevel = params.get("AlarmLevel")
        if params.get("MultiConditions") is not None:
            self._MultiConditions = []
            for item in params.get("MultiConditions"):
                obj = MultiCondition()
                obj._deserialize(item)
                self._MultiConditions.append(obj)
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        self._GroupTriggerStatus = params.get("GroupTriggerStatus")
        self._GroupTriggerCondition = params.get("GroupTriggerCondition")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._MonitorObjectType = params.get("MonitorObjectType")
        if params.get("Classifications") is not None:
            self._Classifications = []
            for item in params.get("Classifications"):
                obj = AlarmClassification()
                obj._deserialize(item)
                self._Classifications.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmResponse(AbstractModel):
    """ModifyAlarm返回参数结构体

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


class ModifyAlarmShieldRequest(AbstractModel):
    """ModifyAlarmShield请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 屏蔽规则ID。
        :type TaskId: str
        :param _AlarmNoticeId: 通知渠道组id。
        :type AlarmNoticeId: str
        :param _StartTime: 屏蔽开始时间（秒级时间戳）。
        :type StartTime: int
        :param _EndTime: 屏蔽结束时间（秒级时间戳）。
        :type EndTime: int
        :param _Type: 屏蔽类型。1：屏蔽所有通知，2：按照Rule参数屏蔽匹配规则的通知。
        :type Type: int
        :param _Rule: 屏蔽规则，当Type为2时必填。规则填写方式详见[产品文档](https://cloud.tencent.com/document/product/614/103178#rule)。
        :type Rule: str
        :param _Reason: 屏蔽原因。
        :type Reason: str
        :param _Status: 规则状态。只有规则状态为生效中（status:1）时，才能将其修改为已失效（status:2）。
        :type Status: int
        """
        self._TaskId = None
        self._AlarmNoticeId = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Rule = None
        self._Reason = None
        self._Status = None

    @property
    def TaskId(self):
        """屏蔽规则ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def AlarmNoticeId(self):
        """通知渠道组id。
        :rtype: str
        """
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def StartTime(self):
        """屏蔽开始时间（秒级时间戳）。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """屏蔽结束时间（秒级时间戳）。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        """屏蔽类型。1：屏蔽所有通知，2：按照Rule参数屏蔽匹配规则的通知。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Rule(self):
        """屏蔽规则，当Type为2时必填。规则填写方式详见[产品文档](https://cloud.tencent.com/document/product/614/103178#rule)。
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Reason(self):
        """屏蔽原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Status(self):
        """规则状态。只有规则状态为生效中（status:1）时，才能将其修改为已失效（status:2）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Rule = params.get("Rule")
        self._Reason = params.get("Reason")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmShieldResponse(AbstractModel):
    """ModifyAlarmShield返回参数结构体

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


class ModifyConfigExtraRequest(AbstractModel):
    """ModifyConfigExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigExtraId: 采集配置扩展信息id
        :type ConfigExtraId: str
        :param _Name: 采集配置规程名称，最长63个字符，只能包含小写字符、数字及分隔符（“-”），且必须以小写字符开头，数字或小写字符结尾
        :type Name: str
        :param _TopicId: 日志主题id
        :type TopicId: str
        :param _HostFile: 节点文件配置信息
        :type HostFile: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        :param _ContainerFile: 采集配置标记。
- 目前只支持label_k8s，用于标记自建k8s集群使用的采集配置
        :type ContainerFile: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        :param _ContainerStdout: 容器标准输出信息
        :type ContainerStdout: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        :param _LogType: 采集的日志类型，默认为minimalist_log。支持以下类型：
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）。
        :type LogType: str
        :param _LogFormat: 日志格式化方式，用于容器采集场景。目前已经废弃
- stdout-docker-json：用于docker容器采集场景
- stdout-containerd：用于containerd容器采集场景
        :type LogFormat: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param _UserDefineRule: 组合解析采集规则，用于复杂场景下的日志采集。
- 取值参考：[使用组合解析提取模式采集日志
](https://cloud.tencent.com/document/product/614/61310)
        :type UserDefineRule: str
        :param _Type: 类型：container_stdout、container_file、host_file
        :type Type: str
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _ConfigFlag: 自建采集配置标
        :type ConfigFlag: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _LogsetName: 日志集name
        :type LogsetName: str
        :param _TopicName: 日志主题name
        :type TopicName: str
        :param _AdvancedConfig: 高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
- ClsAgentDefault(自定义默认值，无特殊含义，用于清空其他选项)，建议取值0

        :type AdvancedConfig: str
        """
        self._ConfigExtraId = None
        self._Name = None
        self._TopicId = None
        self._HostFile = None
        self._ContainerFile = None
        self._ContainerStdout = None
        self._LogType = None
        self._LogFormat = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UserDefineRule = None
        self._Type = None
        self._GroupId = None
        self._ConfigFlag = None
        self._LogsetId = None
        self._LogsetName = None
        self._TopicName = None
        self._AdvancedConfig = None

    @property
    def ConfigExtraId(self):
        """采集配置扩展信息id
        :rtype: str
        """
        return self._ConfigExtraId

    @ConfigExtraId.setter
    def ConfigExtraId(self, ConfigExtraId):
        self._ConfigExtraId = ConfigExtraId

    @property
    def Name(self):
        """采集配置规程名称，最长63个字符，只能包含小写字符、数字及分隔符（“-”），且必须以小写字符开头，数字或小写字符结尾
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicId(self):
        """日志主题id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def HostFile(self):
        """节点文件配置信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.HostFileInfo`
        """
        return self._HostFile

    @HostFile.setter
    def HostFile(self, HostFile):
        self._HostFile = HostFile

    @property
    def ContainerFile(self):
        """采集配置标记。
- 目前只支持label_k8s，用于标记自建k8s集群使用的采集配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContainerFileInfo`
        """
        return self._ContainerFile

    @ContainerFile.setter
    def ContainerFile(self, ContainerFile):
        self._ContainerFile = ContainerFile

    @property
    def ContainerStdout(self):
        """容器标准输出信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContainerStdoutInfo`
        """
        return self._ContainerStdout

    @ContainerStdout.setter
    def ContainerStdout(self, ContainerStdout):
        self._ContainerStdout = ContainerStdout

    @property
    def LogType(self):
        """采集的日志类型，默认为minimalist_log。支持以下类型：
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）。
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def LogFormat(self):
        """日志格式化方式，用于容器采集场景。目前已经废弃
- stdout-docker-json：用于docker容器采集场景
- stdout-containerd：用于containerd容器采集场景
        :rtype: str
        """
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def ExtractRule(self):
        """提取规则，如果设置了ExtractRule，则必须设置LogType
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        """采集黑名单路径列表
        :rtype: list of ExcludePathInfo
        """
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UserDefineRule(self):
        """组合解析采集规则，用于复杂场景下的日志采集。
- 取值参考：[使用组合解析提取模式采集日志
](https://cloud.tencent.com/document/product/614/61310)
        :rtype: str
        """
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def Type(self):
        """类型：container_stdout、container_file、host_file
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ConfigFlag(self):
        """自建采集配置标
        :rtype: str
        """
        return self._ConfigFlag

    @ConfigFlag.setter
    def ConfigFlag(self, ConfigFlag):
        self._ConfigFlag = ConfigFlag

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        """日志集name
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def TopicName(self):
        """日志主题name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def AdvancedConfig(self):
        """高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
- ClsAgentDefault(自定义默认值，无特殊含义，用于清空其他选项)，建议取值0

        :rtype: str
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._ConfigExtraId = params.get("ConfigExtraId")
        self._Name = params.get("Name")
        self._TopicId = params.get("TopicId")
        if params.get("HostFile") is not None:
            self._HostFile = HostFileInfo()
            self._HostFile._deserialize(params.get("HostFile"))
        if params.get("ContainerFile") is not None:
            self._ContainerFile = ContainerFileInfo()
            self._ContainerFile._deserialize(params.get("ContainerFile"))
        if params.get("ContainerStdout") is not None:
            self._ContainerStdout = ContainerStdoutInfo()
            self._ContainerStdout._deserialize(params.get("ContainerStdout"))
        self._LogType = params.get("LogType")
        self._LogFormat = params.get("LogFormat")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UserDefineRule = params.get("UserDefineRule")
        self._Type = params.get("Type")
        self._GroupId = params.get("GroupId")
        self._ConfigFlag = params.get("ConfigFlag")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicName = params.get("TopicName")
        self._AdvancedConfig = params.get("AdvancedConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigExtraResponse(AbstractModel):
    """ModifyConfigExtra返回参数结构体

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


class ModifyConfigRequest(AbstractModel):
    """ModifyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigId: 采集规则配置ID，通过[获取采集规则配置](https://cloud.tencent.com/document/product/614/58616)返回信息获取。
        :type ConfigId: str
        :param _Name: 采集规则配置名称
        :type Name: str
        :param _Path: 日志采集路径，包含文件名
        :type Path: str
        :param _LogType: 采集的日志类型。支持以下类型：
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）；
- service_syslog代表：syslog 采集（详见[采集 Syslog](https://cloud.tencent.com/document/product/614/81454)）；
- windows_event_log代表：Windows事件日志（详见[采集 Windows 事件日志](https://cloud.tencent.com/document/product/614/96678)）。


        :type LogType: str
        :param _ExtractRule: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: 采集黑名单路径列表
        :type ExcludePaths: list of ExcludePathInfo
        :param _Output: 采集配置关联的日志主题（TopicId）
        :type Output: str
        :param _UserDefineRule: 用户自定义解析字符串，Json格式序列化的字符串。
        :type UserDefineRule: str
        :param _AdvancedConfig: 高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
样例：
`{\"ClsAgentFileTimeout\":0,\"ClsAgentMaxDepth\":10,\"ClsAgentParseFailMerge\":true}`
        :type AdvancedConfig: str
        """
        self._ConfigId = None
        self._Name = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._Output = None
        self._UserDefineRule = None
        self._AdvancedConfig = None

    @property
    def ConfigId(self):
        """采集规则配置ID，通过[获取采集规则配置](https://cloud.tencent.com/document/product/614/58616)返回信息获取。
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Name(self):
        """采集规则配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Path(self):
        """日志采集路径，包含文件名
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        """采集的日志类型。支持以下类型：
- json_log代表：JSON-文件日志（详见[使用 JSON 提取模式采集日志](https://cloud.tencent.com/document/product/614/17419)）；
- delimiter_log代表：分隔符-文件日志（详见[使用分隔符提取模式采集日志](https://cloud.tencent.com/document/product/614/17420)）；
- minimalist_log代表：单行全文-文件日志（详见[使用单行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17421)）；
- fullregex_log代表：单行完全正则-文件日志（详见[使用单行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52365)）；
- multiline_log代表：多行全文-文件日志（详见[使用多行全文提取模式采集日志](https://cloud.tencent.com/document/product/614/17422)）；
- multiline_fullregex_log代表：多行完全正则-文件日志（详见[使用多行-完全正则提取模式采集日志](https://cloud.tencent.com/document/product/614/52366)）；
- user_define_log代表：组合解析（适用于多格式嵌套的日志，详见[使用组合解析提取模式采集日志](https://cloud.tencent.com/document/product/614/61310)）；
- service_syslog代表：syslog 采集（详见[采集 Syslog](https://cloud.tencent.com/document/product/614/81454)）；
- windows_event_log代表：Windows事件日志（详见[采集 Windows 事件日志](https://cloud.tencent.com/document/product/614/96678)）。


        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        """提取规则，如果设置了ExtractRule，则必须设置LogType
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        """采集黑名单路径列表
        :rtype: list of ExcludePathInfo
        """
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def Output(self):
        """采集配置关联的日志主题（TopicId）
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def UserDefineRule(self):
        """用户自定义解析字符串，Json格式序列化的字符串。
        :rtype: str
        """
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def AdvancedConfig(self):
        """高级采集配置。 Json字符串， Key/Value定义为如下：
- ClsAgentFileTimeout(超时属性), 取值范围: 大于等于0的整数， 0为不超时
- ClsAgentMaxDepth(最大目录深度)，取值范围: 大于等于0的整数
- ClsAgentParseFailMerge(合并解析失败日志)，取值范围: true或false
样例：
`{\"ClsAgentFileTimeout\":0,\"ClsAgentMaxDepth\":10,\"ClsAgentParseFailMerge\":true}`
        :rtype: str
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._Name = params.get("Name")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._Output = params.get("Output")
        self._UserDefineRule = params.get("UserDefineRule")
        self._AdvancedConfig = params.get("AdvancedConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigResponse(AbstractModel):
    """ModifyConfig返回参数结构体

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


class ModifyConsoleSharingRequest(AbstractModel):
    """ModifyConsoleSharing请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SharingId: 免密分享链接Id
        :type SharingId: str
        :param _DurationMilliseconds: 指定分享链接有效期，单位：毫秒，最长可设定有效期为30天
        :type DurationMilliseconds: int
        """
        self._SharingId = None
        self._DurationMilliseconds = None

    @property
    def SharingId(self):
        """免密分享链接Id
        :rtype: str
        """
        return self._SharingId

    @SharingId.setter
    def SharingId(self, SharingId):
        self._SharingId = SharingId

    @property
    def DurationMilliseconds(self):
        """指定分享链接有效期，单位：毫秒，最长可设定有效期为30天
        :rtype: int
        """
        return self._DurationMilliseconds

    @DurationMilliseconds.setter
    def DurationMilliseconds(self, DurationMilliseconds):
        self._DurationMilliseconds = DurationMilliseconds


    def _deserialize(self, params):
        self._SharingId = params.get("SharingId")
        self._DurationMilliseconds = params.get("DurationMilliseconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsoleSharingResponse(AbstractModel):
    """ModifyConsoleSharing返回参数结构体

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


class ModifyConsumerRequest(AbstractModel):
    """ModifyConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 投递任务绑定的日志主题 ID
        :type TopicId: str
        :param _Effective: 投递任务是否生效，默认不生效
        :type Effective: bool
        :param _NeedContent: 是否投递日志的元数据信息，默认为 true。
当NeedContent为true时：字段Content有效。
当NeedContent为false时：字段Content无效。
        :type NeedContent: bool
        :param _Content: 如果需要投递元数据信息，元数据信息的描述
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka的描述
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: 投递时压缩方式，取值0，2，3。[0：NONE；2：SNAPPY；3：LZ4]
        :type Compression: int
        """
        self._TopicId = None
        self._Effective = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None

    @property
    def TopicId(self):
        """投递任务绑定的日志主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Effective(self):
        """投递任务是否生效，默认不生效
        :rtype: bool
        """
        return self._Effective

    @Effective.setter
    def Effective(self, Effective):
        self._Effective = Effective

    @property
    def NeedContent(self):
        """是否投递日志的元数据信息，默认为 true。
当NeedContent为true时：字段Content有效。
当NeedContent为false时：字段Content无效。
        :rtype: bool
        """
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        """如果需要投递元数据信息，元数据信息的描述
        :rtype: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        """CKafka的描述
        :rtype: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        """
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        """投递时压缩方式，取值0，2，3。[0：NONE；2：SNAPPY；3：LZ4]
        :rtype: int
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Effective = params.get("Effective")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerResponse(AbstractModel):
    """ModifyConsumer返回参数结构体

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


class ModifyCosRechargeRequest(AbstractModel):
    """ModifyCosRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: COS导入配置Id
        :type Id: str
        :param _TopicId: 日志主题Id
        :type TopicId: str
        :param _Name: COS导入任务名称
        :type Name: str
        :param _Enable: 任务状态   0： 停用 ， 1：启用
        :type Enable: int
        :param _Bucket: COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。	
        :type Bucket: str
        :param _BucketRegion: COS存储桶所在地域，详见产品支持的[地域列表](https://cloud.tencent.com/document/product/436/6224)。
        :type BucketRegion: str
        :param _Prefix: COS文件所在文件夹的前缀。为空串时投递存储桶下所有的文件。
        :type Prefix: str
        :param _LogType: 采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表单行全文； 默认为minimalist_log
        :type LogType: str
        :param _Compress: 解析格式。supported: "", "gzip", "lzop", "snappy"; 默认空
        :type Compress: str
        :param _ExtractRuleInfo: 提取规则，如果设置了ExtractRule，则必须设置LogType
        :type ExtractRuleInfo: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _TaskType: COS导入任务类型。1：一次性导入任务；2：持续性导入任务。
        :type TaskType: int
        :param _Metadata: 元数据。支持 bucket，object。
        :type Metadata: list of str
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._Enable = None
        self._Bucket = None
        self._BucketRegion = None
        self._Prefix = None
        self._LogType = None
        self._Compress = None
        self._ExtractRuleInfo = None
        self._TaskType = None
        self._Metadata = None

    @property
    def Id(self):
        """COS导入配置Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        """日志主题Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        """COS导入任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Enable(self):
        """任务状态   0： 停用 ， 1：启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Bucket(self):
        """COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。	
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def BucketRegion(self):
        """COS存储桶所在地域，详见产品支持的[地域列表](https://cloud.tencent.com/document/product/436/6224)。
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def Prefix(self):
        """COS文件所在文件夹的前缀。为空串时投递存储桶下所有的文件。
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def LogType(self):
        """采集的日志类型，json_log代表json格式日志，delimiter_log代表分隔符格式日志，minimalist_log代表单行全文； 默认为minimalist_log
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Compress(self):
        """解析格式。supported: "", "gzip", "lzop", "snappy"; 默认空
        :rtype: str
        """
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def ExtractRuleInfo(self):
        """提取规则，如果设置了ExtractRule，则必须设置LogType
        :rtype: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        return self._ExtractRuleInfo

    @ExtractRuleInfo.setter
    def ExtractRuleInfo(self, ExtractRuleInfo):
        self._ExtractRuleInfo = ExtractRuleInfo

    @property
    def TaskType(self):
        """COS导入任务类型。1：一次性导入任务；2：持续性导入任务。
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Metadata(self):
        """元数据。支持 bucket，object。
        :rtype: list of str
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._Enable = params.get("Enable")
        self._Bucket = params.get("Bucket")
        self._BucketRegion = params.get("BucketRegion")
        self._Prefix = params.get("Prefix")
        self._LogType = params.get("LogType")
        self._Compress = params.get("Compress")
        if params.get("ExtractRuleInfo") is not None:
            self._ExtractRuleInfo = ExtractRuleInfo()
            self._ExtractRuleInfo._deserialize(params.get("ExtractRuleInfo"))
        self._TaskType = params.get("TaskType")
        self._Metadata = params.get("Metadata")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCosRechargeResponse(AbstractModel):
    """ModifyCosRecharge返回参数结构体

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


class ModifyDashboardSubscribeRequest(AbstractModel):
    """ModifyDashboardSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 仪表盘订阅id。
        :type Id: int
        :param _DashboardId: 仪表盘id。
        :type DashboardId: str
        :param _Name: 仪表盘订阅名称。
        :type Name: str
        :param _Cron: 订阅时间cron表达式，格式为：{秒数} {分钟} {小时} {日期} {月份} {星期}；（有效数据为：{分钟} {小时} {日期} {月份} {星期}）。
        :type Cron: str
        :param _SubscribeData: 仪表盘订阅数据。
        :type SubscribeData: :class:`tencentcloud.cls.v20201016.models.DashboardSubscribeData`
        """
        self._Id = None
        self._DashboardId = None
        self._Name = None
        self._Cron = None
        self._SubscribeData = None

    @property
    def Id(self):
        """仪表盘订阅id。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DashboardId(self):
        """仪表盘id。
        :rtype: str
        """
        return self._DashboardId

    @DashboardId.setter
    def DashboardId(self, DashboardId):
        self._DashboardId = DashboardId

    @property
    def Name(self):
        """仪表盘订阅名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Cron(self):
        """订阅时间cron表达式，格式为：{秒数} {分钟} {小时} {日期} {月份} {星期}；（有效数据为：{分钟} {小时} {日期} {月份} {星期}）。
        :rtype: str
        """
        return self._Cron

    @Cron.setter
    def Cron(self, Cron):
        self._Cron = Cron

    @property
    def SubscribeData(self):
        """仪表盘订阅数据。
        :rtype: :class:`tencentcloud.cls.v20201016.models.DashboardSubscribeData`
        """
        return self._SubscribeData

    @SubscribeData.setter
    def SubscribeData(self, SubscribeData):
        self._SubscribeData = SubscribeData


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DashboardId = params.get("DashboardId")
        self._Name = params.get("Name")
        self._Cron = params.get("Cron")
        if params.get("SubscribeData") is not None:
            self._SubscribeData = DashboardSubscribeData()
            self._SubscribeData._deserialize(params.get("SubscribeData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDashboardSubscribeResponse(AbstractModel):
    """ModifyDashboardSubscribe返回参数结构体

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


class ModifyDataTransformRequest(AbstractModel):
    """ModifyDataTransform请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 加工任务id
        :type TaskId: str
        :param _Name: 加工任务名称
        :type Name: str
        :param _EtlContent: 加工语句。 当FuncType为2时，EtlContent必须使用[log_auto_output](https://cloud.tencent.com/document/product/614/70733#b3c58797-4825-4807-bef4-68106e25024f) 

其他参考文档：

- [创建加工任务](https://cloud.tencent.com/document/product/614/63940) 
-  [函数总览](https://cloud.tencent.com/document/product/614/70395)
        :type EtlContent: str
        :param _EnableFlag: 任务启动状态. 默认为1，开启,  2关闭
        :type EnableFlag: int
        :param _DstResources: 加工任务目的topic_id以及别名
        :type DstResources: list of DataTransformResouceInfo
        :param _HasServicesLog: 是否开启投递服务日志。1关闭，2开启
        :type HasServicesLog: int
        """
        self._TaskId = None
        self._Name = None
        self._EtlContent = None
        self._EnableFlag = None
        self._DstResources = None
        self._HasServicesLog = None

    @property
    def TaskId(self):
        """加工任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """加工任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EtlContent(self):
        """加工语句。 当FuncType为2时，EtlContent必须使用[log_auto_output](https://cloud.tencent.com/document/product/614/70733#b3c58797-4825-4807-bef4-68106e25024f) 

其他参考文档：

- [创建加工任务](https://cloud.tencent.com/document/product/614/63940) 
-  [函数总览](https://cloud.tencent.com/document/product/614/70395)
        :rtype: str
        """
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent

    @property
    def EnableFlag(self):
        """任务启动状态. 默认为1，开启,  2关闭
        :rtype: int
        """
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def DstResources(self):
        """加工任务目的topic_id以及别名
        :rtype: list of DataTransformResouceInfo
        """
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources

    @property
    def HasServicesLog(self):
        """是否开启投递服务日志。1关闭，2开启
        :rtype: int
        """
        return self._HasServicesLog

    @HasServicesLog.setter
    def HasServicesLog(self, HasServicesLog):
        self._HasServicesLog = HasServicesLog


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._EtlContent = params.get("EtlContent")
        self._EnableFlag = params.get("EnableFlag")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        self._HasServicesLog = params.get("HasServicesLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataTransformResponse(AbstractModel):
    """ModifyDataTransform返回参数结构体

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


class ModifyIndexRequest(AbstractModel):
    """ModifyIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Status: 默认不生效
        :type Status: bool
        :param _Rule: 索引规则
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _IncludeInternalFields: 内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引，默认为false，推荐设置为true
* false:不包含
* true:包含
        :type IncludeInternalFields: bool
        :param _MetadataFlag: 元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引，默认为0，推荐设置为1
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
        :type MetadataFlag: int
        """
        self._TopicId = None
        self._Status = None
        self._Rule = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        """默认不生效
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rule(self):
        """索引规则
        :rtype: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def IncludeInternalFields(self):
        """内置保留字段（`__FILENAME__`，`__HOSTNAME__`及`__SOURCE__`）是否包含至全文索引，默认为false，推荐设置为true
* false:不包含
* true:包含
        :rtype: bool
        """
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        """元数据字段（前缀为`__TAG__`的字段）是否包含至全文索引，默认为0，推荐设置为1
* 0:仅包含开启键值索引的元数据字段
* 1:包含所有元数据字段
* 2:不包含任何元数据字段
        :rtype: int
        """
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIndexResponse(AbstractModel):
    """ModifyIndex返回参数结构体

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


class ModifyKafkaConsumerRequest(AbstractModel):
    """ModifyKafkaConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTopicId: 日志主题ID
        :type FromTopicId: str
        :param _Compression: 压缩方式[0:NONE；2:SNAPPY；3:LZ4]
        :type Compression: int
        :param _ConsumerContent: kafka协议消费数据格式
        :type ConsumerContent: :class:`tencentcloud.cls.v20201016.models.KafkaConsumerContent`
        """
        self._FromTopicId = None
        self._Compression = None
        self._ConsumerContent = None

    @property
    def FromTopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._FromTopicId

    @FromTopicId.setter
    def FromTopicId(self, FromTopicId):
        self._FromTopicId = FromTopicId

    @property
    def Compression(self):
        """压缩方式[0:NONE；2:SNAPPY；3:LZ4]
        :rtype: int
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def ConsumerContent(self):
        """kafka协议消费数据格式
        :rtype: :class:`tencentcloud.cls.v20201016.models.KafkaConsumerContent`
        """
        return self._ConsumerContent

    @ConsumerContent.setter
    def ConsumerContent(self, ConsumerContent):
        self._ConsumerContent = ConsumerContent


    def _deserialize(self, params):
        self._FromTopicId = params.get("FromTopicId")
        self._Compression = params.get("Compression")
        if params.get("ConsumerContent") is not None:
            self._ConsumerContent = KafkaConsumerContent()
            self._ConsumerContent._deserialize(params.get("ConsumerContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKafkaConsumerResponse(AbstractModel):
    """ModifyKafkaConsumer返回参数结构体

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


class ModifyKafkaRechargeRequest(AbstractModel):
    """ModifyKafkaRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Kafka导入配置ID
        :type Id: str
        :param _TopicId: 导入CLS目标topic ID
        :type TopicId: str
        :param _Name: Kafka导入配置名称
        :type Name: str
        :param _KafkaType: 导入Kafka类型，0：腾讯云CKafka：1：用户自建Kafka。
        :type KafkaType: int
        :param _KafkaInstance: 腾讯云CKafka实例ID，KafkaType为0时必填。
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址，KafkaType为1时必填。
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接，KafkaType为1时必填。
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议，KafkaType参数为1并且IsEncryptionAddr参数为true时必填。
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _UserKafkaTopics: 用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :type UserKafkaTopics: str
        :param _ConsumerGroupName: 用户Kafka消费组名称
        :type ConsumerGroupName: str
        :param _LogRechargeRule: 日志导入规则
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        :param _StatusControl: 导入控制，1：暂停；2：继续。
        :type StatusControl: int
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._UserKafkaTopics = None
        self._ConsumerGroupName = None
        self._LogRechargeRule = None
        self._StatusControl = None

    @property
    def Id(self):
        """Kafka导入配置ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        """导入CLS目标topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        """Kafka导入配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        """导入Kafka类型，0：腾讯云CKafka：1：用户自建Kafka。
        :rtype: int
        """
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        """腾讯云CKafka实例ID，KafkaType为0时必填。
        :rtype: str
        """
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        """服务地址，KafkaType为1时必填。
        :rtype: str
        """
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        """ServerAddr是否为加密连接，KafkaType为1时必填。
        :rtype: bool
        """
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        """加密访问协议，KafkaType参数为1并且IsEncryptionAddr参数为true时必填。
        :rtype: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UserKafkaTopics(self):
        """用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开
        :rtype: str
        """
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def ConsumerGroupName(self):
        """用户Kafka消费组名称
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def LogRechargeRule(self):
        """日志导入规则
        :rtype: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule

    @property
    def StatusControl(self):
        """导入控制，1：暂停；2：继续。
        :rtype: int
        """
        return self._StatusControl

    @StatusControl.setter
    def StatusControl(self, StatusControl):
        self._StatusControl = StatusControl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        self._StatusControl = params.get("StatusControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKafkaRechargeResponse(AbstractModel):
    """ModifyKafkaRecharge返回参数结构体

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


class ModifyLogsetRequest(AbstractModel):
    """ModifyLogset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _LogsetName: 日志集名称
        :type LogsetName: str
        :param _Tags: 日志集的绑定的标签键值对。最大支持10个标签键值对，同一个资源只能同时绑定一个标签键。
        :type Tags: list of Tag
        """
        self._LogsetId = None
        self._LogsetName = None
        self._Tags = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        """日志集名称
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def Tags(self):
        """日志集的绑定的标签键值对。最大支持10个标签键值对，同一个资源只能同时绑定一个标签键。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
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
        


class ModifyLogsetResponse(AbstractModel):
    """ModifyLogset返回参数结构体

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


class ModifyMachineGroupRequest(AbstractModel):
    """ModifyMachineGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 机器组ID
        :type GroupId: str
        :param _GroupName: 机器组名称
        :type GroupName: str
        :param _MachineGroupType: 机器组类型。Type：ip，Values中为ip字符串列表机器组；Type：label，Values中为标签字符串列表机器组。
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _AutoUpdate: 是否开启机器组自动更新
        :type AutoUpdate: bool
        :param _UpdateStartTime: 升级开始时间，建议业务低峰期升级LogListener
        :type UpdateStartTime: str
        :param _UpdateEndTime: 升级结束时间，建议业务低峰期升级LogListener
        :type UpdateEndTime: str
        :param _ServiceLogging: 是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
        :type ServiceLogging: bool
        :param _DelayCleanupTime: 机器组中机器定期离线清理时间。单位：天
        :type DelayCleanupTime: int
        :param _MetaTags: 机器组元数据信息列表
        :type MetaTags: list of MetaTagInfo
        """
        self._GroupId = None
        self._GroupName = None
        self._MachineGroupType = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._DelayCleanupTime = None
        self._MetaTags = None

    @property
    def GroupId(self):
        """机器组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """机器组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        """机器组类型。Type：ip，Values中为ip字符串列表机器组；Type：label，Values中为标签字符串列表机器组。
        :rtype: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        """是否开启机器组自动更新
        :rtype: bool
        """
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        """升级开始时间，建议业务低峰期升级LogListener
        :rtype: str
        """
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        """升级结束时间，建议业务低峰期升级LogListener
        :rtype: str
        """
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        """是否开启服务日志，用于记录因Loglistener 服务自身产生的log，开启后，会创建内部日志集cls_service_logging和日志主题loglistener_status,loglistener_alarm,loglistener_business，不产生计费
        :rtype: bool
        """
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def DelayCleanupTime(self):
        """机器组中机器定期离线清理时间。单位：天
        :rtype: int
        """
        return self._DelayCleanupTime

    @DelayCleanupTime.setter
    def DelayCleanupTime(self, DelayCleanupTime):
        self._DelayCleanupTime = DelayCleanupTime

    @property
    def MetaTags(self):
        """机器组元数据信息列表
        :rtype: list of MetaTagInfo
        """
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        self._DelayCleanupTime = params.get("DelayCleanupTime")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMachineGroupResponse(AbstractModel):
    """ModifyMachineGroup返回参数结构体

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


class ModifyNoticeContentRequest(AbstractModel):
    """ModifyNoticeContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeContentId: 通知内容模板ID。
        :type NoticeContentId: str
        :param _Name: 通知内容模板名称。
        :type Name: str
        :param _Type: 通知内容语言。

0：中文 1：英文
        :type Type: int
        :param _NoticeContents: 通知内容模板详细信息。
        :type NoticeContents: list of NoticeContent
        """
        self._NoticeContentId = None
        self._Name = None
        self._Type = None
        self._NoticeContents = None

    @property
    def NoticeContentId(self):
        """通知内容模板ID。
        :rtype: str
        """
        return self._NoticeContentId

    @NoticeContentId.setter
    def NoticeContentId(self, NoticeContentId):
        self._NoticeContentId = NoticeContentId

    @property
    def Name(self):
        """通知内容模板名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """通知内容语言。

0：中文 1：英文
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeContents(self):
        """通知内容模板详细信息。
        :rtype: list of NoticeContent
        """
        return self._NoticeContents

    @NoticeContents.setter
    def NoticeContents(self, NoticeContents):
        self._NoticeContents = NoticeContents


    def _deserialize(self, params):
        self._NoticeContentId = params.get("NoticeContentId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeContents") is not None:
            self._NoticeContents = []
            for item in params.get("NoticeContents"):
                obj = NoticeContent()
                obj._deserialize(item)
                self._NoticeContents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNoticeContentResponse(AbstractModel):
    """ModifyNoticeContent返回参数结构体

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


class ModifyScheduledSqlRequest(AbstractModel):
    """ModifyScheduledSql请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _SrcTopicId: 源日志主题
        :type SrcTopicId: str
        :param _EnableFlag: 任务启动状态.   1开启,  2关闭
        :type EnableFlag: int
        :param _DstResource: 定时SQL分析的目标日志主题
        :type DstResource: :class:`tencentcloud.cls.v20201016.models.ScheduledSqlResouceInfo`
        :param _ScheduledSqlContent: 查询语句
        :type ScheduledSqlContent: str
        :param _ProcessPeriod: 调度周期(分钟)
        :type ProcessPeriod: int
        :param _ProcessTimeWindow: 单次查询的时间窗口. 例子中为近15分钟
        :type ProcessTimeWindow: str
        :param _ProcessDelay: 执行延迟(秒)
        :type ProcessDelay: int
        :param _SrcTopicRegion: 源topicId的地域信息
        :type SrcTopicRegion: str
        :param _Name: 任务名称
        :type Name: str
        :param _SyntaxRule: 语法规则。 默认值为0。 0：Lucene语法，1：CQL语法
        :type SyntaxRule: int
        """
        self._TaskId = None
        self._SrcTopicId = None
        self._EnableFlag = None
        self._DstResource = None
        self._ScheduledSqlContent = None
        self._ProcessPeriod = None
        self._ProcessTimeWindow = None
        self._ProcessDelay = None
        self._SrcTopicRegion = None
        self._Name = None
        self._SyntaxRule = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SrcTopicId(self):
        """源日志主题
        :rtype: str
        """
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def EnableFlag(self):
        """任务启动状态.   1开启,  2关闭
        :rtype: int
        """
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def DstResource(self):
        """定时SQL分析的目标日志主题
        :rtype: :class:`tencentcloud.cls.v20201016.models.ScheduledSqlResouceInfo`
        """
        return self._DstResource

    @DstResource.setter
    def DstResource(self, DstResource):
        self._DstResource = DstResource

    @property
    def ScheduledSqlContent(self):
        """查询语句
        :rtype: str
        """
        return self._ScheduledSqlContent

    @ScheduledSqlContent.setter
    def ScheduledSqlContent(self, ScheduledSqlContent):
        self._ScheduledSqlContent = ScheduledSqlContent

    @property
    def ProcessPeriod(self):
        """调度周期(分钟)
        :rtype: int
        """
        return self._ProcessPeriod

    @ProcessPeriod.setter
    def ProcessPeriod(self, ProcessPeriod):
        self._ProcessPeriod = ProcessPeriod

    @property
    def ProcessTimeWindow(self):
        """单次查询的时间窗口. 例子中为近15分钟
        :rtype: str
        """
        return self._ProcessTimeWindow

    @ProcessTimeWindow.setter
    def ProcessTimeWindow(self, ProcessTimeWindow):
        self._ProcessTimeWindow = ProcessTimeWindow

    @property
    def ProcessDelay(self):
        """执行延迟(秒)
        :rtype: int
        """
        return self._ProcessDelay

    @ProcessDelay.setter
    def ProcessDelay(self, ProcessDelay):
        self._ProcessDelay = ProcessDelay

    @property
    def SrcTopicRegion(self):
        """源topicId的地域信息
        :rtype: str
        """
        return self._SrcTopicRegion

    @SrcTopicRegion.setter
    def SrcTopicRegion(self, SrcTopicRegion):
        self._SrcTopicRegion = SrcTopicRegion

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SyntaxRule(self):
        """语法规则。 默认值为0。 0：Lucene语法，1：CQL语法
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SrcTopicId = params.get("SrcTopicId")
        self._EnableFlag = params.get("EnableFlag")
        if params.get("DstResource") is not None:
            self._DstResource = ScheduledSqlResouceInfo()
            self._DstResource._deserialize(params.get("DstResource"))
        self._ScheduledSqlContent = params.get("ScheduledSqlContent")
        self._ProcessPeriod = params.get("ProcessPeriod")
        self._ProcessTimeWindow = params.get("ProcessTimeWindow")
        self._ProcessDelay = params.get("ProcessDelay")
        self._SrcTopicRegion = params.get("SrcTopicRegion")
        self._Name = params.get("Name")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyScheduledSqlResponse(AbstractModel):
    """ModifyScheduledSql返回参数结构体

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


class ModifyShipperRequest(AbstractModel):
    """ModifyShipper请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        :param _Bucket: COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。
        :type Bucket: str
        :param _Prefix: 投递规则投递的新的目录前缀。
- 仅支持0-9A-Za-z-_/
- 最大支持256个字符
        :type Prefix: str
        :param _Status: 投递规则的开关状态。true：开启投递任务；false：关闭投递任务。
        :type Status: bool
        :param _ShipperName: 投递规则的名字
        :type ShipperName: str
        :param _Interval: 投递的时间间隔，单位 秒，默认300，范围 300-900
        :type Interval: int
        :param _MaxSize: 投递的文件的最大值，单位 MB，默认256，范围 5-256
        :type MaxSize: int
        :param _FilterRules: 投递日志的过滤规则，匹配的日志进行投递，各rule之间是and关系，最多5个，数组为空则表示不过滤而全部投递
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param _Compress: 投递日志的压缩配置
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: 投递日志的内容格式配置
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _FilenameMode: 投递文件命名配置，0：随机数命名，1：投递时间命名。
        :type FilenameMode: int
        :param _StorageType: cos桶存储类型。支持：STANDARD_IA、ARCHIVE、DEEP_ARCHIVE、STANDARD、MAZ_STANDARD、MAZ_STANDARD_IA、INTELLIGENT_TIERING。

1. STANDARD_IA：低频存储；
2. ARCHIVE：归档存储；
3. DEEP_ARCHIVE：深度归档存储；
4. STANDARD：标准存储；
5. MAZ_STANDARD：标准存储（多 AZ）；
6. MAZ_STANDARD_IA：低频存储（多 AZ）；
7. INTELLIGENT_TIERING：智能分层存储。
        :type StorageType: str
        """
        self._ShipperId = None
        self._Bucket = None
        self._Prefix = None
        self._Status = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._FilenameMode = None
        self._StorageType = None

    @property
    def ShipperId(self):
        """投递规则ID
        :rtype: str
        """
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def Bucket(self):
        """COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        """投递规则投递的新的目录前缀。
- 仅支持0-9A-Za-z-_/
- 最大支持256个字符
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def Status(self):
        """投递规则的开关状态。true：开启投递任务；false：关闭投递任务。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ShipperName(self):
        """投递规则的名字
        :rtype: str
        """
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        """投递的时间间隔，单位 秒，默认300，范围 300-900
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        """投递的文件的最大值，单位 MB，默认256，范围 5-256
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def FilterRules(self):
        """投递日志的过滤规则，匹配的日志进行投递，各rule之间是and关系，最多5个，数组为空则表示不过滤而全部投递
        :rtype: list of FilterRuleInfo
        """
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        """投递日志的分区规则，支持strftime的时间格式表示
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        """投递日志的压缩配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        """
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        """投递日志的内容格式配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FilenameMode(self):
        """投递文件命名配置，0：随机数命名，1：投递时间命名。
        :rtype: int
        """
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode

    @property
    def StorageType(self):
        """cos桶存储类型。支持：STANDARD_IA、ARCHIVE、DEEP_ARCHIVE、STANDARD、MAZ_STANDARD、MAZ_STANDARD_IA、INTELLIGENT_TIERING。

1. STANDARD_IA：低频存储；
2. ARCHIVE：归档存储；
3. DEEP_ARCHIVE：深度归档存储；
4. STANDARD：标准存储；
5. MAZ_STANDARD：标准存储（多 AZ）；
6. MAZ_STANDARD_IA：低频存储（多 AZ）；
7. INTELLIGENT_TIERING：智能分层存储。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._Status = params.get("Status")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._FilenameMode = params.get("FilenameMode")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyShipperResponse(AbstractModel):
    """ModifyShipper返回参数结构体

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


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _Tags: 标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，并且不能有重复的键值对。
        :type Tags: list of Tag
        :param _Status: 主题是否开启采集，true：开启采集；false：关闭采集。
控制台目前不支持修改此参数。
        :type Status: bool
        :param _AutoSplit: 是否开启自动分裂
        :type AutoSplit: bool
        :param _MaxSplitPartitions: 若开启最大分裂，该主题能够能够允许的最大分区数
        :type MaxSplitPartitions: int
        :param _Period: 生命周期，单位天，标准存储取值范围1\~3600，低频存储取值范围7\~3600。取值为3640时代表永久保存
        :type Period: int
        :param _Describes: 日志主题描述
        :type Describes: str
        :param _HotPeriod: 0：关闭日志沉降。
非0：开启日志沉降后标准存储的天数。HotPeriod需要大于等于7，且小于Period。仅在StorageType为 hot 时生效
        :type HotPeriod: int
        :param _IsWebTracking: 免鉴权开关。 false：关闭； true：开启。
开启后将支持指定操作匿名访问该日志主题。详情请参见[日志主题](https://cloud.tencent.com/document/product/614/41035)。
        :type IsWebTracking: bool
        :param _Extends: 日志主题扩展信息
        :type Extends: :class:`tencentcloud.cls.v20201016.models.TopicExtendInfo`
        :param _PartitionCount: 日志主题分区数量
        :type PartitionCount: int
        :param _CancelTopicAsyncTaskID: 取消切换存储任务的id
        :type CancelTopicAsyncTaskID: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Tags = None
        self._Status = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._Period = None
        self._Describes = None
        self._HotPeriod = None
        self._IsWebTracking = None
        self._Extends = None
        self._PartitionCount = None
        self._CancelTopicAsyncTaskID = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """日志主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Tags(self):
        """标签描述列表，通过指定该参数可以同时绑定标签到相应的日志主题。最大支持10个标签键值对，并且不能有重复的键值对。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        """主题是否开启采集，true：开启采集；false：关闭采集。
控制台目前不支持修改此参数。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AutoSplit(self):
        """是否开启自动分裂
        :rtype: bool
        """
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        """若开启最大分裂，该主题能够能够允许的最大分区数
        :rtype: int
        """
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def Period(self):
        """生命周期，单位天，标准存储取值范围1\~3600，低频存储取值范围7\~3600。取值为3640时代表永久保存
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Describes(self):
        """日志主题描述
        :rtype: str
        """
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        """0：关闭日志沉降。
非0：开启日志沉降后标准存储的天数。HotPeriod需要大于等于7，且小于Period。仅在StorageType为 hot 时生效
        :rtype: int
        """
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod

    @property
    def IsWebTracking(self):
        """免鉴权开关。 false：关闭； true：开启。
开启后将支持指定操作匿名访问该日志主题。详情请参见[日志主题](https://cloud.tencent.com/document/product/614/41035)。
        :rtype: bool
        """
        return self._IsWebTracking

    @IsWebTracking.setter
    def IsWebTracking(self, IsWebTracking):
        self._IsWebTracking = IsWebTracking

    @property
    def Extends(self):
        """日志主题扩展信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.TopicExtendInfo`
        """
        return self._Extends

    @Extends.setter
    def Extends(self, Extends):
        self._Extends = Extends

    @property
    def PartitionCount(self):
        """日志主题分区数量
        :rtype: int
        """
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def CancelTopicAsyncTaskID(self):
        """取消切换存储任务的id
        :rtype: str
        """
        return self._CancelTopicAsyncTaskID

    @CancelTopicAsyncTaskID.setter
    def CancelTopicAsyncTaskID(self, CancelTopicAsyncTaskID):
        self._CancelTopicAsyncTaskID = CancelTopicAsyncTaskID


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._Period = params.get("Period")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        self._IsWebTracking = params.get("IsWebTracking")
        if params.get("Extends") is not None:
            self._Extends = TopicExtendInfo()
            self._Extends._deserialize(params.get("Extends"))
        self._PartitionCount = params.get("PartitionCount")
        self._CancelTopicAsyncTaskID = params.get("CancelTopicAsyncTaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic返回参数结构体

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


class ModifyWebCallbackRequest(AbstractModel):
    """ModifyWebCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WebCallbackId: 告警渠道回调配置ID。
        :type WebCallbackId: str
        :param _Name: 告警渠道回调配置名称。
        :type Name: str
        :param _Type: 渠道类型

WeCom:企业微信;DingTalk:钉钉;Lark:飞书;Http:自定义回调;
        :type Type: str
        :param _Webhook: 回调地址。
        :type Webhook: str
        :param _Method: 请求方式。

支持POST、PUT。

注意：当Type为Http时，必填。
        :type Method: str
        :param _Key: 秘钥信息。
        :type Key: str
        """
        self._WebCallbackId = None
        self._Name = None
        self._Type = None
        self._Webhook = None
        self._Method = None
        self._Key = None

    @property
    def WebCallbackId(self):
        """告警渠道回调配置ID。
        :rtype: str
        """
        return self._WebCallbackId

    @WebCallbackId.setter
    def WebCallbackId(self, WebCallbackId):
        self._WebCallbackId = WebCallbackId

    @property
    def Name(self):
        """告警渠道回调配置名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """渠道类型

WeCom:企业微信;DingTalk:钉钉;Lark:飞书;Http:自定义回调;
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Webhook(self):
        """回调地址。
        :rtype: str
        """
        return self._Webhook

    @Webhook.setter
    def Webhook(self, Webhook):
        self._Webhook = Webhook

    @property
    def Method(self):
        """请求方式。

支持POST、PUT。

注意：当Type为Http时，必填。
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Key(self):
        """秘钥信息。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._WebCallbackId = params.get("WebCallbackId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Webhook = params.get("Webhook")
        self._Method = params.get("Method")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebCallbackResponse(AbstractModel):
    """ModifyWebCallback返回参数结构体

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


class MonitorTime(AbstractModel):
    """告警策略中监控任务的执行时间点

    """

    def __init__(self):
        r"""
        :param _Type: 执行周期， 可选值：`Period`、`Fixed`、`Cron`。

- Period：固定频率
- Fixed：固定时间
- Cron：Cron表达式
        :type Type: str
        :param _Time: 执行的周期，或者定制执行的时间节点。单位为分钟，取值范围为1~1440。
当type为`Period`,`Fixed`时，time字段生效。
        :type Time: int
        :param _CronExpression: 执行的周期cron表达式。示例：`"*/1 * * * *"` 从左到右每个field的含义 Minutes field, Hours field,Day of month field,Month field,Day of week field， 不支持秒级别。
当type为`Cron`时，CronExpression字段生效。
        :type CronExpression: str
        """
        self._Type = None
        self._Time = None
        self._CronExpression = None

    @property
    def Type(self):
        """执行周期， 可选值：`Period`、`Fixed`、`Cron`。

- Period：固定频率
- Fixed：固定时间
- Cron：Cron表达式
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        """执行的周期，或者定制执行的时间节点。单位为分钟，取值范围为1~1440。
当type为`Period`,`Fixed`时，time字段生效。
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def CronExpression(self):
        """执行的周期cron表达式。示例：`"*/1 * * * *"` 从左到右每个field的含义 Minutes field, Hours field,Day of month field,Month field,Day of week field， 不支持秒级别。
当type为`Cron`时，CronExpression字段生效。
        :rtype: str
        """
        return self._CronExpression

    @CronExpression.setter
    def CronExpression(self, CronExpression):
        self._CronExpression = CronExpression


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        self._CronExpression = params.get("CronExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiCondition(AbstractModel):
    """多触发条件。

    """

    def __init__(self):
        r"""
        :param _Condition: 触发条件。
        :type Condition: str
        :param _AlarmLevel: 告警级别。0:警告(Warn); 1:提醒(Info); 2:紧急 (Critical)。

- 不填则默认为0。
        :type AlarmLevel: int
        """
        self._Condition = None
        self._AlarmLevel = None

    @property
    def Condition(self):
        """触发条件。
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def AlarmLevel(self):
        """告警级别。0:警告(Warn); 1:提醒(Info); 2:紧急 (Critical)。

- 不填则默认为0。
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel


    def _deserialize(self, params):
        self._Condition = params.get("Condition")
        self._AlarmLevel = params.get("AlarmLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiTopicSearchInformation(AbstractModel):
    """多日志主题检索相关信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 要检索分析的日志主题ID
        :type TopicId: str
        :param _Context: 透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时
        :type Context: str
        """
        self._TopicId = None
        self._Context = None

    @property
    def TopicId(self):
        """要检索分析的日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Context(self):
        """透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeContent(AbstractModel):
    """通知内容模板详细配置

    """

    def __init__(self):
        r"""
        :param _Type: 渠道类型

Email:邮件;Sms:短信;WeChat:微信;Phone:电话;WeCom:企业微信;DingTalk:钉钉;Lark:飞书;Http:自定义回调;
        :type Type: str
        :param _TriggerContent: 告警触发通知内容模板。
        :type TriggerContent: :class:`tencentcloud.cls.v20201016.models.NoticeContentInfo`
        :param _RecoveryContent: 告警恢复通知内容模板。
        :type RecoveryContent: :class:`tencentcloud.cls.v20201016.models.NoticeContentInfo`
        """
        self._Type = None
        self._TriggerContent = None
        self._RecoveryContent = None

    @property
    def Type(self):
        """渠道类型

Email:邮件;Sms:短信;WeChat:微信;Phone:电话;WeCom:企业微信;DingTalk:钉钉;Lark:飞书;Http:自定义回调;
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TriggerContent(self):
        """告警触发通知内容模板。
        :rtype: :class:`tencentcloud.cls.v20201016.models.NoticeContentInfo`
        """
        return self._TriggerContent

    @TriggerContent.setter
    def TriggerContent(self, TriggerContent):
        self._TriggerContent = TriggerContent

    @property
    def RecoveryContent(self):
        """告警恢复通知内容模板。
        :rtype: :class:`tencentcloud.cls.v20201016.models.NoticeContentInfo`
        """
        return self._RecoveryContent

    @RecoveryContent.setter
    def RecoveryContent(self, RecoveryContent):
        self._RecoveryContent = RecoveryContent


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("TriggerContent") is not None:
            self._TriggerContent = NoticeContentInfo()
            self._TriggerContent._deserialize(params.get("TriggerContent"))
        if params.get("RecoveryContent") is not None:
            self._RecoveryContent = NoticeContentInfo()
            self._RecoveryContent._deserialize(params.get("RecoveryContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeContentInfo(AbstractModel):
    """通知模板内容

    """

    def __init__(self):
        r"""
        :param _Title: 通知内容模板标题信息。
部分通知渠道类型不支持“标题”，请参照腾讯云控制台页面。
        :type Title: str
        :param _Content: 通知内容模板正文信息。
        :type Content: str
        :param _Headers: 请求头（Request Headers）：在HTTP请求中，请求头包含了客户端向服务器发送的附加信息，如用户代理、授权凭证、期望的响应格式等。
仅“自定义回调”支持该配置。
        :type Headers: list of str
        """
        self._Title = None
        self._Content = None
        self._Headers = None

    @property
    def Title(self):
        """通知内容模板标题信息。
部分通知渠道类型不支持“标题”，请参照腾讯云控制台页面。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        """通知内容模板正文信息。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Headers(self):
        """请求头（Request Headers）：在HTTP请求中，请求头包含了客户端向服务器发送的附加信息，如用户代理、授权凭证、期望的响应格式等。
仅“自定义回调”支持该配置。
        :rtype: list of str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        self._Headers = params.get("Headers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeContentTemplate(AbstractModel):
    """通知内容模板信息

    """

    def __init__(self):
        r"""
        :param _NoticeContentId: 通知内容模板ID。
        :type NoticeContentId: str
        :param _Name: 通知内容模板名称
        :type Name: str
        :param _Type: 语言类型。

0： 中文
1： 英文
        :type Type: int
        :param _NoticeContents: 通知内容模板信息。
        :type NoticeContents: list of NoticeContent
        :param _Flag: 通知内容模板标记。

0： 用户自定义
1： 系统内置
        :type Flag: int
        :param _Uin: 创建者主账号。
        :type Uin: int
        :param _SubUin: 创建/修改者子账号。
        :type SubUin: int
        :param _CreateTime: 创建时间 秒级时间戳。
        :type CreateTime: int
        :param _UpdateTime: 更新时间 秒级时间戳。
        :type UpdateTime: int
        """
        self._NoticeContentId = None
        self._Name = None
        self._Type = None
        self._NoticeContents = None
        self._Flag = None
        self._Uin = None
        self._SubUin = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def NoticeContentId(self):
        """通知内容模板ID。
        :rtype: str
        """
        return self._NoticeContentId

    @NoticeContentId.setter
    def NoticeContentId(self, NoticeContentId):
        self._NoticeContentId = NoticeContentId

    @property
    def Name(self):
        """通知内容模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """语言类型。

0： 中文
1： 英文
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NoticeContents(self):
        """通知内容模板信息。
        :rtype: list of NoticeContent
        """
        return self._NoticeContents

    @NoticeContents.setter
    def NoticeContents(self, NoticeContents):
        self._NoticeContents = NoticeContents

    @property
    def Flag(self):
        """通知内容模板标记。

0： 用户自定义
1： 系统内置
        :rtype: int
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Uin(self):
        """创建者主账号。
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        """创建/修改者子账号。
        :rtype: int
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def CreateTime(self):
        """创建时间 秒级时间戳。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间 秒级时间戳。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._NoticeContentId = params.get("NoticeContentId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeContents") is not None:
            self._NoticeContents = []
            for item in params.get("NoticeContents"):
                obj = NoticeContent()
                obj._deserialize(item)
                self._NoticeContents.append(obj)
        self._Flag = params.get("Flag")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeReceiver(AbstractModel):
    """告警通知接收者信息

    """

    def __init__(self):
        r"""
        :param _ReceiverType: 接受者类型。可选值：
-  Uin - 用户ID
- Group - 用户组ID
暂不支持其余接收者类型。
        :type ReceiverType: str
        :param _ReceiverIds: 接收者。
当ReceiverType为Uin时，ReceiverIds的值为用户uid。[子用户信息查询](https://cloud.tencent.com/document/api/598/53486)
当ReceiverType为Group时，ReceiverIds的值为用户组id。[CAM用户组](https://cloud.tencent.com/document/product/598/34589)
        :type ReceiverIds: list of int
        :param _ReceiverChannels: 通知接收渠道。
- Email - 邮件
- Sms - 短信
- WeChat - 微信
- Phone - 电话
        :type ReceiverChannels: list of str
        :param _NoticeContentId: 通知内容模板ID，使用Default-zh引用默认模板（中文），使用Default-en引用DefaultTemplate(English)。
        :type NoticeContentId: str
        :param _StartTime: 允许接收信息的开始时间。格式：`15:04:05`。必填
        :type StartTime: str
        :param _EndTime: 允许接收信息的结束时间。格式：`15:04:05`。必填
        :type EndTime: str
        :param _Index: 位序。

- 入参时无效。
- 出参时有效。
        :type Index: int
        """
        self._ReceiverType = None
        self._ReceiverIds = None
        self._ReceiverChannels = None
        self._NoticeContentId = None
        self._StartTime = None
        self._EndTime = None
        self._Index = None

    @property
    def ReceiverType(self):
        """接受者类型。可选值：
-  Uin - 用户ID
- Group - 用户组ID
暂不支持其余接收者类型。
        :rtype: str
        """
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def ReceiverIds(self):
        """接收者。
当ReceiverType为Uin时，ReceiverIds的值为用户uid。[子用户信息查询](https://cloud.tencent.com/document/api/598/53486)
当ReceiverType为Group时，ReceiverIds的值为用户组id。[CAM用户组](https://cloud.tencent.com/document/product/598/34589)
        :rtype: list of int
        """
        return self._ReceiverIds

    @ReceiverIds.setter
    def ReceiverIds(self, ReceiverIds):
        self._ReceiverIds = ReceiverIds

    @property
    def ReceiverChannels(self):
        """通知接收渠道。
- Email - 邮件
- Sms - 短信
- WeChat - 微信
- Phone - 电话
        :rtype: list of str
        """
        return self._ReceiverChannels

    @ReceiverChannels.setter
    def ReceiverChannels(self, ReceiverChannels):
        self._ReceiverChannels = ReceiverChannels

    @property
    def NoticeContentId(self):
        """通知内容模板ID，使用Default-zh引用默认模板（中文），使用Default-en引用DefaultTemplate(English)。
        :rtype: str
        """
        return self._NoticeContentId

    @NoticeContentId.setter
    def NoticeContentId(self, NoticeContentId):
        self._NoticeContentId = NoticeContentId

    @property
    def StartTime(self):
        """允许接收信息的开始时间。格式：`15:04:05`。必填
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """允许接收信息的结束时间。格式：`15:04:05`。必填
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Index(self):
        """位序。

- 入参时无效。
- 出参时有效。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._ReceiverType = params.get("ReceiverType")
        self._ReceiverIds = params.get("ReceiverIds")
        self._ReceiverChannels = params.get("ReceiverChannels")
        self._NoticeContentId = params.get("NoticeContentId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeRule(AbstractModel):
    """通知规则

    """

    def __init__(self):
        r"""
        :param _Rule: 匹配规则 JSON串。
**rule规则树格式为嵌套结构体JSON字符串**
`{"Value":"AND","Type":"Operation","Children":[{"Value":"OR","Type":"Operation","Children":[{"Type":"Condition","Value":"Level","Children":[{"Value":"In","Type":"Compare"},{"Value":"[1,0]","Type":"Value"}]},{"Type":"Condition","Value":"Level","Children":[{"Value":"NotIn","Type":"Compare"},{"Value":"[2]","Type":"Value"}]}]}]}`

**rule规则树限制规则如下**：
- 顶层rule中Type可取值：`Condition`，`Operation`
- Type为`Operation`的子节点支持的Type可取值：`Condition`，`Operation`
- Type为`Condition`的子节点支持的Type可取值：`String`，`Compare`，`Array`，`TimeRange`，`Value`，`Key`
- 其他Type无子节点
- 当rule Type为`Operation`时，value可取值：`AND`，`OR`
- 当rule Type为`Condition`时，value不可为空，子节点个数不能小于2
    - 当子节点Type为  `Compare` 时，value可取值：`>`，`<`，`>=`，`<=`，`=`，`!=`，`Between`，`NotBetween`，`=~`，`!=~`，`In`，`NotIn`
    - value为`Between`，`NotBetween`时，下一个子节点value必须是长度为2的数组
    - value为`=~`，`!=~`时，下一个子节点value必须是一个正则表达式
    - value为`In`，`NotIn`时， 下一个子节点value必须是一个数组

**业务参数含义**：
- Type：Condition 表示是规则条件，Value：Level 表示告警等级
    - 子节点Type支持`Compare`，Value支持`In`，`NotIn`
    - 下一个子节点value支持的值：0（警告），1（提醒），2 （紧急）
以下示例表示：告警等级属于提醒
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"Level\",\"Children\":[{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[1]\",\"Type\":\"Value\"}]}]}`

- Type：Condition 表示是规则条件，Value：NotifyType 表示通知类型
    - 子节点Type支持`Compare`，Value支持`In`，`NotIn`
    - 下一个子节点value支持的值：1（告警通知），2 （恢复通知）
以下示例表示：通知类型属于告警通知或通知类型不属于恢复通知
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"NotifyType\",\"Children\":[{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[1]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"NotifyType\",\"Children\":[{\"Value\":\"NotIn\",\"Type\":\"Compare\"},{\"Value\":\"[2]\",\"Type\":\"Value\"}]}]}]}`

- Type：Condition 表示是规则条件，Value：AlarmID 表示告警策略
    - 子节点Type支持`Compare`，Value支持`In`，`NotIn`
    - 下一个子节点value支持的值：告警策略id数组
以下示例表示：告警策略属于alarm-53af048c-254b-4c73-bb48-xxx,alarm-6dfa8bc5-08da-4d64-b6cb-xxx或告警策略不属于alarm-1036314c-1e49-4cee-a8fb-xxx
`"{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"AlarmID\",\"Children\":[{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"alarm-53af048c-254b-4c73-bb48-xxx\\\",\\\"alarm-6dfa8bc5-08da-4d64-b6cb-xxx\\\"]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"AlarmID\",\"Children\":[{\"Value\":\"NotIn\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"alarm-1036314c-1e49-4cee-a8fb-xxx\\\"]\",\"Type\":\"Value\"}]}]}]}"`

- Type：Condition 表示是规则条件，Value：AlarmName 表示告警策略名称
    - 子节点Type支持`Compare`，Value支持`=~`，`!=~`
    - 下一个子节点value支持的值：必须是正则表达式
以下示例表示：告警策略名称正则匹配^test$或告警策略名称正则不匹配^hahaha$
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"AlarmName\",\"Children\":[{\"Value\":\"=~\",\"Type\":\"Compare\"},{\"Value\":\"^test$\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"AlarmName\",\"Children\":[{\"Value\":\"!=~\",\"Type\":\"Compare\"},{\"Value\":\"^hahaha$\",\"Type\":\"Value\"}]}]}]}`

- Type：Condition 表示是规则条件，Value：Label 表示告警分类字段
    - 子节点Type支持`Compare`，Value支持`In`，`NotIn`，`=~`，`!=~`
    - 下一个子节点value支持的值：`In`，`NotIn` 时value是数组，`=~`，`!=~`时value是正则表达式
以下示例表示：告警分类字段key1属于v1或告警分类字段key2不属于v2或告警分类字段key3正则匹配^test$或告警分类字段key4正则不匹配^hahaha$
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"Label\",\"Children\":[{\"Value\":\"key1\",\"Type\":\"Key\"},{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"v1\\\"]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Label\",\"Children\":[{\"Value\":\"key2\",\"Type\":\"Key\"},{\"Value\":\"NotIn\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"v2\\\"]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Label\",\"Children\":[{\"Value\":\"key3\",\"Type\":\"Key\"},{\"Value\":\"=~\",\"Type\":\"Compare\"},{\"Value\":\"^test$\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Label\",\"Children\":[{\"Value\":\"key4\",\"Type\":\"Key\"},{\"Value\":\"!=~\",\"Type\":\"Compare\"},{\"Value\":\"^hahaha$\",\"Type\":\"Value\"}]}]}]}`

- Type：Condition 表示是规则条件，Value：NotifyTime 表示通知时间
    - 子节点Type支持`Compare`，Value支持`Between `，`NotBetween `
    - 下一个子节点value支持的值：长度为2，格式为`14:20:36`的字符串数组
以下示例表示：通知时间在指定范围内14:18:36至14:33:36或通知时间不在指定范围内14:20:36至14:30:36
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"NotifyTime\",\"Children\":[{\"Value\":\"Between\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"14:18:36\\\",\\\"14:33:36\\\"]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"NotifyTime\",\"Children\":[{\"Value\":\"NotBetween\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"14:20:36\\\",\\\"14:30:36\\\"]\",\"Type\":\"Value\"}]}]}]}`

- Type：Condition 表示是规则条件，Value：Duration 表示告警持续时间
    - 子节点Type支持`Compare`，Value支持`>`，`<`，`>=`，`<=`
    - 下一个子节点value支持的值：整型值单位分钟
以下示例表示：告警持续时间大于1分钟或告警持续时间大于等于2分钟或告警持续时间小于3分钟或告警持续时间小于等于4分钟
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"Duration\",\"Children\":[{\"Value\":\">\",\"Type\":\"Compare\"},{\"Value\":1,\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Duration\",\"Children\":[{\"Value\":\">=\",\"Type\":\"Compare\"},{\"Value\":2,\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Duration\",\"Children\":[{\"Value\":\"<\",\"Type\":\"Compare\"},{\"Value\":3,\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Duration\",\"Children\":[{\"Value\":\"<=\",\"Type\":\"Compare\"},{\"Value\":4,\"Type\":\"Value\"}]}]}]}`
        :type Rule: str
        :param _NoticeReceivers: 告警通知接收者信息。
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: 告警通知模板回调信息，包括企业微信、钉钉、飞书。
        :type WebCallbacks: list of WebCallback
        :param _Escalate: 告警升级开关。`true`：开启告警升级、`false`：关闭告警升级，默认：false
        :type Escalate: bool
        :param _Type: 告警升级条件。`1`：无人认领且未恢复、`2`：未恢复，默认为1
- 无人认领且未恢复：告警没有恢复并且没有人认领则升级
- 未恢复：当前告警持续未恢复则升级

        :type Type: int
        :param _Interval: 告警升级间隔。单位：分钟，范围`[1，14400]`
        :type Interval: int
        :param _EscalateNotice: 告警升级后下一个环节的通知渠道配置
        :type EscalateNotice: :class:`tencentcloud.cls.v20201016.models.EscalateNoticeInfo`
        """
        self._Rule = None
        self._NoticeReceivers = None
        self._WebCallbacks = None
        self._Escalate = None
        self._Type = None
        self._Interval = None
        self._EscalateNotice = None

    @property
    def Rule(self):
        """匹配规则 JSON串。
**rule规则树格式为嵌套结构体JSON字符串**
`{"Value":"AND","Type":"Operation","Children":[{"Value":"OR","Type":"Operation","Children":[{"Type":"Condition","Value":"Level","Children":[{"Value":"In","Type":"Compare"},{"Value":"[1,0]","Type":"Value"}]},{"Type":"Condition","Value":"Level","Children":[{"Value":"NotIn","Type":"Compare"},{"Value":"[2]","Type":"Value"}]}]}]}`

**rule规则树限制规则如下**：
- 顶层rule中Type可取值：`Condition`，`Operation`
- Type为`Operation`的子节点支持的Type可取值：`Condition`，`Operation`
- Type为`Condition`的子节点支持的Type可取值：`String`，`Compare`，`Array`，`TimeRange`，`Value`，`Key`
- 其他Type无子节点
- 当rule Type为`Operation`时，value可取值：`AND`，`OR`
- 当rule Type为`Condition`时，value不可为空，子节点个数不能小于2
    - 当子节点Type为  `Compare` 时，value可取值：`>`，`<`，`>=`，`<=`，`=`，`!=`，`Between`，`NotBetween`，`=~`，`!=~`，`In`，`NotIn`
    - value为`Between`，`NotBetween`时，下一个子节点value必须是长度为2的数组
    - value为`=~`，`!=~`时，下一个子节点value必须是一个正则表达式
    - value为`In`，`NotIn`时， 下一个子节点value必须是一个数组

**业务参数含义**：
- Type：Condition 表示是规则条件，Value：Level 表示告警等级
    - 子节点Type支持`Compare`，Value支持`In`，`NotIn`
    - 下一个子节点value支持的值：0（警告），1（提醒），2 （紧急）
以下示例表示：告警等级属于提醒
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"Level\",\"Children\":[{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[1]\",\"Type\":\"Value\"}]}]}`

- Type：Condition 表示是规则条件，Value：NotifyType 表示通知类型
    - 子节点Type支持`Compare`，Value支持`In`，`NotIn`
    - 下一个子节点value支持的值：1（告警通知），2 （恢复通知）
以下示例表示：通知类型属于告警通知或通知类型不属于恢复通知
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"NotifyType\",\"Children\":[{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[1]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"NotifyType\",\"Children\":[{\"Value\":\"NotIn\",\"Type\":\"Compare\"},{\"Value\":\"[2]\",\"Type\":\"Value\"}]}]}]}`

- Type：Condition 表示是规则条件，Value：AlarmID 表示告警策略
    - 子节点Type支持`Compare`，Value支持`In`，`NotIn`
    - 下一个子节点value支持的值：告警策略id数组
以下示例表示：告警策略属于alarm-53af048c-254b-4c73-bb48-xxx,alarm-6dfa8bc5-08da-4d64-b6cb-xxx或告警策略不属于alarm-1036314c-1e49-4cee-a8fb-xxx
`"{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"AlarmID\",\"Children\":[{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"alarm-53af048c-254b-4c73-bb48-xxx\\\",\\\"alarm-6dfa8bc5-08da-4d64-b6cb-xxx\\\"]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"AlarmID\",\"Children\":[{\"Value\":\"NotIn\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"alarm-1036314c-1e49-4cee-a8fb-xxx\\\"]\",\"Type\":\"Value\"}]}]}]}"`

- Type：Condition 表示是规则条件，Value：AlarmName 表示告警策略名称
    - 子节点Type支持`Compare`，Value支持`=~`，`!=~`
    - 下一个子节点value支持的值：必须是正则表达式
以下示例表示：告警策略名称正则匹配^test$或告警策略名称正则不匹配^hahaha$
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"AlarmName\",\"Children\":[{\"Value\":\"=~\",\"Type\":\"Compare\"},{\"Value\":\"^test$\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"AlarmName\",\"Children\":[{\"Value\":\"!=~\",\"Type\":\"Compare\"},{\"Value\":\"^hahaha$\",\"Type\":\"Value\"}]}]}]}`

- Type：Condition 表示是规则条件，Value：Label 表示告警分类字段
    - 子节点Type支持`Compare`，Value支持`In`，`NotIn`，`=~`，`!=~`
    - 下一个子节点value支持的值：`In`，`NotIn` 时value是数组，`=~`，`!=~`时value是正则表达式
以下示例表示：告警分类字段key1属于v1或告警分类字段key2不属于v2或告警分类字段key3正则匹配^test$或告警分类字段key4正则不匹配^hahaha$
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"Label\",\"Children\":[{\"Value\":\"key1\",\"Type\":\"Key\"},{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"v1\\\"]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Label\",\"Children\":[{\"Value\":\"key2\",\"Type\":\"Key\"},{\"Value\":\"NotIn\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"v2\\\"]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Label\",\"Children\":[{\"Value\":\"key3\",\"Type\":\"Key\"},{\"Value\":\"=~\",\"Type\":\"Compare\"},{\"Value\":\"^test$\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Label\",\"Children\":[{\"Value\":\"key4\",\"Type\":\"Key\"},{\"Value\":\"!=~\",\"Type\":\"Compare\"},{\"Value\":\"^hahaha$\",\"Type\":\"Value\"}]}]}]}`

- Type：Condition 表示是规则条件，Value：NotifyTime 表示通知时间
    - 子节点Type支持`Compare`，Value支持`Between `，`NotBetween `
    - 下一个子节点value支持的值：长度为2，格式为`14:20:36`的字符串数组
以下示例表示：通知时间在指定范围内14:18:36至14:33:36或通知时间不在指定范围内14:20:36至14:30:36
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"NotifyTime\",\"Children\":[{\"Value\":\"Between\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"14:18:36\\\",\\\"14:33:36\\\"]\",\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"NotifyTime\",\"Children\":[{\"Value\":\"NotBetween\",\"Type\":\"Compare\"},{\"Value\":\"[\\\"14:20:36\\\",\\\"14:30:36\\\"]\",\"Type\":\"Value\"}]}]}]}`

- Type：Condition 表示是规则条件，Value：Duration 表示告警持续时间
    - 子节点Type支持`Compare`，Value支持`>`，`<`，`>=`，`<=`
    - 下一个子节点value支持的值：整型值单位分钟
以下示例表示：告警持续时间大于1分钟或告警持续时间大于等于2分钟或告警持续时间小于3分钟或告警持续时间小于等于4分钟
`{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Value\":\"OR\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"Duration\",\"Children\":[{\"Value\":\">\",\"Type\":\"Compare\"},{\"Value\":1,\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Duration\",\"Children\":[{\"Value\":\">=\",\"Type\":\"Compare\"},{\"Value\":2,\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Duration\",\"Children\":[{\"Value\":\"<\",\"Type\":\"Compare\"},{\"Value\":3,\"Type\":\"Value\"}]},{\"Type\":\"Condition\",\"Value\":\"Duration\",\"Children\":[{\"Value\":\"<=\",\"Type\":\"Compare\"},{\"Value\":4,\"Type\":\"Value\"}]}]}]}`
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def NoticeReceivers(self):
        """告警通知接收者信息。
        :rtype: list of NoticeReceiver
        """
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        """告警通知模板回调信息，包括企业微信、钉钉、飞书。
        :rtype: list of WebCallback
        """
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks

    @property
    def Escalate(self):
        """告警升级开关。`true`：开启告警升级、`false`：关闭告警升级，默认：false
        :rtype: bool
        """
        return self._Escalate

    @Escalate.setter
    def Escalate(self, Escalate):
        self._Escalate = Escalate

    @property
    def Type(self):
        """告警升级条件。`1`：无人认领且未恢复、`2`：未恢复，默认为1
- 无人认领且未恢复：告警没有恢复并且没有人认领则升级
- 未恢复：当前告警持续未恢复则升级

        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Interval(self):
        """告警升级间隔。单位：分钟，范围`[1，14400]`
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def EscalateNotice(self):
        """告警升级后下一个环节的通知渠道配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.EscalateNoticeInfo`
        """
        return self._EscalateNotice

    @EscalateNotice.setter
    def EscalateNotice(self, EscalateNotice):
        self._EscalateNotice = EscalateNotice


    def _deserialize(self, params):
        self._Rule = params.get("Rule")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        self._Escalate = params.get("Escalate")
        self._Type = params.get("Type")
        self._Interval = params.get("Interval")
        if params.get("EscalateNotice") is not None:
            self._EscalateNotice = EscalateNoticeInfo()
            self._EscalateNotice._deserialize(params.get("EscalateNotice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenKafkaConsumerRequest(AbstractModel):
    """OpenKafkaConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTopicId: 日志主题ID
        :type FromTopicId: str
        :param _Compression: 压缩方式[0:NONE；2:SNAPPY；3:LZ4]，默认：0
        :type Compression: int
        :param _ConsumerContent: kafka协议消费数据格式
        :type ConsumerContent: :class:`tencentcloud.cls.v20201016.models.KafkaConsumerContent`
        """
        self._FromTopicId = None
        self._Compression = None
        self._ConsumerContent = None

    @property
    def FromTopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._FromTopicId

    @FromTopicId.setter
    def FromTopicId(self, FromTopicId):
        self._FromTopicId = FromTopicId

    @property
    def Compression(self):
        """压缩方式[0:NONE；2:SNAPPY；3:LZ4]，默认：0
        :rtype: int
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def ConsumerContent(self):
        """kafka协议消费数据格式
        :rtype: :class:`tencentcloud.cls.v20201016.models.KafkaConsumerContent`
        """
        return self._ConsumerContent

    @ConsumerContent.setter
    def ConsumerContent(self, ConsumerContent):
        self._ConsumerContent = ConsumerContent


    def _deserialize(self, params):
        self._FromTopicId = params.get("FromTopicId")
        self._Compression = params.get("Compression")
        if params.get("ConsumerContent") is not None:
            self._ConsumerContent = KafkaConsumerContent()
            self._ConsumerContent._deserialize(params.get("ConsumerContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenKafkaConsumerResponse(AbstractModel):
    """OpenKafkaConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicID: KafkaConsumer 消费时使用的Topic参数
        :type TopicID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicID = None
        self._RequestId = None

    @property
    def TopicID(self):
        """KafkaConsumer 消费时使用的Topic参数
        :rtype: str
        """
        return self._TopicID

    @TopicID.setter
    def TopicID(self, TopicID):
        self._TopicID = TopicID

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
        self._TopicID = params.get("TopicID")
        self._RequestId = params.get("RequestId")


class ParquetInfo(AbstractModel):
    """Parquet内容

    """

    def __init__(self):
        r"""
        :param _ParquetKeyInfo: ParquetKeyInfo数组
        :type ParquetKeyInfo: list of ParquetKeyInfo
        """
        self._ParquetKeyInfo = None

    @property
    def ParquetKeyInfo(self):
        """ParquetKeyInfo数组
        :rtype: list of ParquetKeyInfo
        """
        return self._ParquetKeyInfo

    @ParquetKeyInfo.setter
    def ParquetKeyInfo(self, ParquetKeyInfo):
        self._ParquetKeyInfo = ParquetKeyInfo


    def _deserialize(self, params):
        if params.get("ParquetKeyInfo") is not None:
            self._ParquetKeyInfo = []
            for item in params.get("ParquetKeyInfo"):
                obj = ParquetKeyInfo()
                obj._deserialize(item)
                self._ParquetKeyInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParquetKeyInfo(AbstractModel):
    """Parquet内容描述

    """

    def __init__(self):
        r"""
        :param _KeyName: 键值名称
        :type KeyName: str
        :param _KeyType: 数据类型，目前支持6种类型：string、boolean、int32、int64、float、double
        :type KeyType: str
        :param _KeyNonExistingField: 解析失败赋值信息
        :type KeyNonExistingField: str
        """
        self._KeyName = None
        self._KeyType = None
        self._KeyNonExistingField = None

    @property
    def KeyName(self):
        """键值名称
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def KeyType(self):
        """数据类型，目前支持6种类型：string、boolean、int32、int64、float、double
        :rtype: str
        """
        return self._KeyType

    @KeyType.setter
    def KeyType(self, KeyType):
        self._KeyType = KeyType

    @property
    def KeyNonExistingField(self):
        """解析失败赋值信息
        :rtype: str
        """
        return self._KeyNonExistingField

    @KeyNonExistingField.setter
    def KeyNonExistingField(self, KeyNonExistingField):
        self._KeyNonExistingField = KeyNonExistingField


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._KeyType = params.get("KeyType")
        self._KeyNonExistingField = params.get("KeyNonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionInfo(AbstractModel):
    """日志主题分区信息

    """

    def __init__(self):
        r"""
        :param _PartitionId: 分区ID
        :type PartitionId: int
        :param _Status: 分区的状态（readwrite或者是readonly）
        :type Status: str
        :param _InclusiveBeginKey: 分区哈希键起始key
        :type InclusiveBeginKey: str
        :param _ExclusiveEndKey: 分区哈希键结束key
        :type ExclusiveEndKey: str
        :param _CreateTime: 分区创建时间
        :type CreateTime: str
        :param _LastWriteTime: 只读分区数据停止写入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastWriteTime: str
        """
        self._PartitionId = None
        self._Status = None
        self._InclusiveBeginKey = None
        self._ExclusiveEndKey = None
        self._CreateTime = None
        self._LastWriteTime = None

    @property
    def PartitionId(self):
        """分区ID
        :rtype: int
        """
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId

    @property
    def Status(self):
        """分区的状态（readwrite或者是readonly）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InclusiveBeginKey(self):
        """分区哈希键起始key
        :rtype: str
        """
        return self._InclusiveBeginKey

    @InclusiveBeginKey.setter
    def InclusiveBeginKey(self, InclusiveBeginKey):
        self._InclusiveBeginKey = InclusiveBeginKey

    @property
    def ExclusiveEndKey(self):
        """分区哈希键结束key
        :rtype: str
        """
        return self._ExclusiveEndKey

    @ExclusiveEndKey.setter
    def ExclusiveEndKey(self, ExclusiveEndKey):
        self._ExclusiveEndKey = ExclusiveEndKey

    @property
    def CreateTime(self):
        """分区创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastWriteTime(self):
        """只读分区数据停止写入时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastWriteTime

    @LastWriteTime.setter
    def LastWriteTime(self, LastWriteTime):
        self._LastWriteTime = LastWriteTime


    def _deserialize(self, params):
        self._PartitionId = params.get("PartitionId")
        self._Status = params.get("Status")
        self._InclusiveBeginKey = params.get("InclusiveBeginKey")
        self._ExclusiveEndKey = params.get("ExclusiveEndKey")
        self._CreateTime = params.get("CreateTime")
        self._LastWriteTime = params.get("LastWriteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewKafkaRechargeRequest(AbstractModel):
    """PreviewKafkaRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PreviewType: 预览类型，1：源数据预览；2：导出结果预览。
        :type PreviewType: int
        :param _KafkaType: 导入Kafka类型，0：腾讯云CKafka；1：用户自建Kafka。
        :type KafkaType: int
        :param _UserKafkaTopics: 用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开。
最多支持100个。
        :type UserKafkaTopics: str
        :param _Offset: 导入数据位置，-2：最早；-1：最晚。
        :type Offset: int
        :param _KafkaInstance: 腾讯云CKafka实例ID，当KafkaType为0时参数KafkaInstance有效且必填。
        :type KafkaInstance: str
        :param _ServerAddr: 服务地址。
KafkaType为1时ServerAddr必填。
        :type ServerAddr: str
        :param _IsEncryptionAddr: ServerAddr是否为加密连接。
KafkaType为1时有效。
        :type IsEncryptionAddr: bool
        :param _Protocol: 加密访问协议。
KafkaType为1并且IsEncryptionAddr为true时Protocol必填。
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _ConsumerGroupName: 用户Kafka消费组
        :type ConsumerGroupName: str
        :param _LogRechargeRule: 日志导入规则
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        self._PreviewType = None
        self._KafkaType = None
        self._UserKafkaTopics = None
        self._Offset = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._ConsumerGroupName = None
        self._LogRechargeRule = None

    @property
    def PreviewType(self):
        """预览类型，1：源数据预览；2：导出结果预览。
        :rtype: int
        """
        return self._PreviewType

    @PreviewType.setter
    def PreviewType(self, PreviewType):
        self._PreviewType = PreviewType

    @property
    def KafkaType(self):
        """导入Kafka类型，0：腾讯云CKafka；1：用户自建Kafka。
        :rtype: int
        """
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def UserKafkaTopics(self):
        """用户需要导入的Kafka相关topic列表，多个topic之间使用半角逗号隔开。
最多支持100个。
        :rtype: str
        """
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def Offset(self):
        """导入数据位置，-2：最早；-1：最晚。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def KafkaInstance(self):
        """腾讯云CKafka实例ID，当KafkaType为0时参数KafkaInstance有效且必填。
        :rtype: str
        """
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        """服务地址。
KafkaType为1时ServerAddr必填。
        :rtype: str
        """
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        """ServerAddr是否为加密连接。
KafkaType为1时有效。
        :rtype: bool
        """
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        """加密访问协议。
KafkaType为1并且IsEncryptionAddr为true时Protocol必填。
        :rtype: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ConsumerGroupName(self):
        """用户Kafka消费组
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def LogRechargeRule(self):
        """日志导入规则
        :rtype: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule


    def _deserialize(self, params):
        self._PreviewType = params.get("PreviewType")
        self._KafkaType = params.get("KafkaType")
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._Offset = params.get("Offset")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewKafkaRechargeResponse(AbstractModel):
    """PreviewKafkaRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogSample: 日志样例，PreviewType为2时返回
        :type LogSample: str
        :param _LogData: 日志预览结果
        :type LogData: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogSample = None
        self._LogData = None
        self._RequestId = None

    @property
    def LogSample(self):
        """日志样例，PreviewType为2时返回
        :rtype: str
        """
        return self._LogSample

    @LogSample.setter
    def LogSample(self, LogSample):
        self._LogSample = LogSample

    @property
    def LogData(self):
        """日志预览结果
        :rtype: str
        """
        return self._LogData

    @LogData.setter
    def LogData(self, LogData):
        self._LogData = LogData

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
        self._LogSample = params.get("LogSample")
        self._LogData = params.get("LogData")
        self._RequestId = params.get("RequestId")


class PreviewLogStatistic(AbstractModel):
    """预览数据详情

    """

    def __init__(self):
        r"""
        :param _LogContent: 日志内容
        :type LogContent: str
        :param _LineNum: 行号。从0开始
        :type LineNum: int
        :param _DstTopicId: 目标日志主题
        :type DstTopicId: str
        :param _FailReason: 失败错误信息， 空字符串""表示正常
        :type FailReason: str
        :param _Time: 日志时间，格式：`2024-05-07 17:13:17.105`

- 入参时无效
- 出参时有效，为日志中的时间格式
        :type Time: str
        :param _DstTopicName: 目标topic-name
注意：此字段可能返回 null，表示取不到有效值。
        :type DstTopicName: str
        """
        self._LogContent = None
        self._LineNum = None
        self._DstTopicId = None
        self._FailReason = None
        self._Time = None
        self._DstTopicName = None

    @property
    def LogContent(self):
        """日志内容
        :rtype: str
        """
        return self._LogContent

    @LogContent.setter
    def LogContent(self, LogContent):
        self._LogContent = LogContent

    @property
    def LineNum(self):
        """行号。从0开始
        :rtype: int
        """
        return self._LineNum

    @LineNum.setter
    def LineNum(self, LineNum):
        self._LineNum = LineNum

    @property
    def DstTopicId(self):
        """目标日志主题
        :rtype: str
        """
        return self._DstTopicId

    @DstTopicId.setter
    def DstTopicId(self, DstTopicId):
        self._DstTopicId = DstTopicId

    @property
    def FailReason(self):
        """失败错误信息， 空字符串""表示正常
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Time(self):
        """日志时间，格式：`2024-05-07 17:13:17.105`

- 入参时无效
- 出参时有效，为日志中的时间格式
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def DstTopicName(self):
        warnings.warn("parameter `DstTopicName` is deprecated", DeprecationWarning) 

        """目标topic-name
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DstTopicName

    @DstTopicName.setter
    def DstTopicName(self, DstTopicName):
        warnings.warn("parameter `DstTopicName` is deprecated", DeprecationWarning) 

        self._DstTopicName = DstTopicName


    def _deserialize(self, params):
        self._LogContent = params.get("LogContent")
        self._LineNum = params.get("LineNum")
        self._DstTopicId = params.get("DstTopicId")
        self._FailReason = params.get("FailReason")
        self._Time = params.get("Time")
        self._DstTopicName = params.get("DstTopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMetricRequest(AbstractModel):
    """QueryMetric请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 查询语句，使用PromQL语法	
        :type Query: str
        :param _TopicId: 指标主题ID
        :type TopicId: str
        :param _Time: 查询时间，秒级Unix时间戳。为空时代表当前时间戳。

        :type Time: int
        """
        self._Query = None
        self._TopicId = None
        self._Time = None

    @property
    def Query(self):
        """查询语句，使用PromQL语法	
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def TopicId(self):
        """指标主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Time(self):
        """查询时间，秒级Unix时间戳。为空时代表当前时间戳。

        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._TopicId = params.get("TopicId")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMetricResponse(AbstractModel):
    """QueryMetric返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultType: 指标查询结果类型
        :type ResultType: str
        :param _Result: 指标查询结果
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultType = None
        self._Result = None
        self._RequestId = None

    @property
    def ResultType(self):
        """指标查询结果类型
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def Result(self):
        """指标查询结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._ResultType = params.get("ResultType")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class QueryRangeMetricRequest(AbstractModel):
    """QueryRangeMetric请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 指标主题ID
        :type TopicId: str
        :param _Query: 查询语句，使用PromQL语法
        :type Query: str
        :param _Start: 查询起始时间，秒级Unix时间戳
        :type Start: int
        :param _End: 查询结束时间，秒级Unix时间戳
        :type End: int
        :param _Step: 查询时间间隔，单位秒
        :type Step: int
        """
        self._TopicId = None
        self._Query = None
        self._Start = None
        self._End = None
        self._Step = None

    @property
    def TopicId(self):
        """指标主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Query(self):
        """查询语句，使用PromQL语法
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Start(self):
        """查询起始时间，秒级Unix时间戳
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        """查询结束时间，秒级Unix时间戳
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End

    @property
    def Step(self):
        """查询时间间隔，单位秒
        :rtype: int
        """
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Query = params.get("Query")
        self._Start = params.get("Start")
        self._End = params.get("End")
        self._Step = params.get("Step")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRangeMetricResponse(AbstractModel):
    """QueryRangeMetric返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultType: 指标查询结果类型
        :type ResultType: str
        :param _Result: 指标查询结果
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultType = None
        self._Result = None
        self._RequestId = None

    @property
    def ResultType(self):
        """指标查询结果类型
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def Result(self):
        """指标查询结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._ResultType = params.get("ResultType")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RetryShipperTaskRequest(AbstractModel):
    """RetryShipperTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        :param _TaskId: 投递任务ID
        :type TaskId: str
        """
        self._ShipperId = None
        self._TaskId = None

    @property
    def ShipperId(self):
        """投递规则ID
        :rtype: str
        """
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TaskId(self):
        """投递任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryShipperTaskResponse(AbstractModel):
    """RetryShipperTask返回参数结构体

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


class RuleInfo(AbstractModel):
    """索引规则，FullText、KeyValue、Tag参数必须输入一个有效参数

    """

    def __init__(self):
        r"""
        :param _FullText: 全文索引配置, 为空时代表未开启全文索引
注意：此字段可能返回 null，表示取不到有效值。
        :type FullText: :class:`tencentcloud.cls.v20201016.models.FullTextInfo`
        :param _KeyValue: 键值索引配置，为空时代表未开启键值索引
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValue: :class:`tencentcloud.cls.v20201016.models.RuleKeyValueInfo`
        :param _Tag: 元字段索引配置，为空时代表未开启元字段索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: :class:`tencentcloud.cls.v20201016.models.RuleTagInfo`
        :param _DynamicIndex: 键值索引自动配置，为空时代表未开启该功能。
启用后自动将日志内的字段添加到键值索引中，包括日志中后续新增的字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicIndex: :class:`tencentcloud.cls.v20201016.models.DynamicIndex`
        """
        self._FullText = None
        self._KeyValue = None
        self._Tag = None
        self._DynamicIndex = None

    @property
    def FullText(self):
        """全文索引配置, 为空时代表未开启全文索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.FullTextInfo`
        """
        return self._FullText

    @FullText.setter
    def FullText(self, FullText):
        self._FullText = FullText

    @property
    def KeyValue(self):
        """键值索引配置，为空时代表未开启键值索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.RuleKeyValueInfo`
        """
        return self._KeyValue

    @KeyValue.setter
    def KeyValue(self, KeyValue):
        self._KeyValue = KeyValue

    @property
    def Tag(self):
        """元字段索引配置，为空时代表未开启元字段索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.RuleTagInfo`
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def DynamicIndex(self):
        """键值索引自动配置，为空时代表未开启该功能。
启用后自动将日志内的字段添加到键值索引中，包括日志中后续新增的字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.DynamicIndex`
        """
        return self._DynamicIndex

    @DynamicIndex.setter
    def DynamicIndex(self, DynamicIndex):
        self._DynamicIndex = DynamicIndex


    def _deserialize(self, params):
        if params.get("FullText") is not None:
            self._FullText = FullTextInfo()
            self._FullText._deserialize(params.get("FullText"))
        if params.get("KeyValue") is not None:
            self._KeyValue = RuleKeyValueInfo()
            self._KeyValue._deserialize(params.get("KeyValue"))
        if params.get("Tag") is not None:
            self._Tag = RuleTagInfo()
            self._Tag._deserialize(params.get("Tag"))
        if params.get("DynamicIndex") is not None:
            self._DynamicIndex = DynamicIndex()
            self._DynamicIndex._deserialize(params.get("DynamicIndex"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleKeyValueInfo(AbstractModel):
    """键值索引配置

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param _KeyValues: 需要建立索引的键值对信息
        :type KeyValues: list of KeyValueInfo
        """
        self._CaseSensitive = None
        self._KeyValues = None

    @property
    def CaseSensitive(self):
        """是否大小写敏感
        :rtype: bool
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def KeyValues(self):
        """需要建立索引的键值对信息
        :rtype: list of KeyValueInfo
        """
        return self._KeyValues

    @KeyValues.setter
    def KeyValues(self, KeyValues):
        self._KeyValues = KeyValues


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self._KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self._KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTagInfo(AbstractModel):
    """元字段索引配置

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
        :type CaseSensitive: bool
        :param _KeyValues: 元字段索引配置中的字段信息
        :type KeyValues: list of KeyValueInfo
        """
        self._CaseSensitive = None
        self._KeyValues = None

    @property
    def CaseSensitive(self):
        """是否大小写敏感
        :rtype: bool
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def KeyValues(self):
        """元字段索引配置中的字段信息
        :rtype: list of KeyValueInfo
        """
        return self._KeyValues

    @KeyValues.setter
    def KeyValues(self, KeyValues):
        self._KeyValues = KeyValues


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self._KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self._KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledSqlResouceInfo(AbstractModel):
    """ScheduledSql的资源信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 目标主题id
        :type TopicId: str
        :param _Region: 主题的地域信息
        :type Region: str
        :param _BizType: 主题类型：0为日志主题，1为指标主题
        :type BizType: int
        :param _MetricName: 指标名称。当BizType为1时，MetricName需要填写
        :type MetricName: str
        :param _MetricNames: 指标名称
BizType为1时，优先使用MetricNames字段多指标只能填充到MetricNames字段，单指标建议填充到MetricName字段
        :type MetricNames: list of str
        :param _MetricLabels: 指标维度，不接受时间类型。
        :type MetricLabels: list of str
        :param _CustomTime: 指标时间戳，默认值为SQL查询时间范围的左侧时间点，您也可以指定其他字段（类型为uinx时间、TimeStamp，精度毫秒）为指标时间戳。
        :type CustomTime: str
        :param _CustomMetricLabels: 除了MetricLabels，您还可以使用该参数，为指标补充静态的维度。
维度名以字母或下划线开头，后面可以跟字母、数字或下划线，长度小于等于1024 字节
        :type CustomMetricLabels: list of MetricLabel
        """
        self._TopicId = None
        self._Region = None
        self._BizType = None
        self._MetricName = None
        self._MetricNames = None
        self._MetricLabels = None
        self._CustomTime = None
        self._CustomMetricLabels = None

    @property
    def TopicId(self):
        """目标主题id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Region(self):
        """主题的地域信息
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BizType(self):
        """主题类型：0为日志主题，1为指标主题
        :rtype: int
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def MetricName(self):
        """指标名称。当BizType为1时，MetricName需要填写
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricNames(self):
        """指标名称
BizType为1时，优先使用MetricNames字段多指标只能填充到MetricNames字段，单指标建议填充到MetricName字段
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def MetricLabels(self):
        """指标维度，不接受时间类型。
        :rtype: list of str
        """
        return self._MetricLabels

    @MetricLabels.setter
    def MetricLabels(self, MetricLabels):
        self._MetricLabels = MetricLabels

    @property
    def CustomTime(self):
        """指标时间戳，默认值为SQL查询时间范围的左侧时间点，您也可以指定其他字段（类型为uinx时间、TimeStamp，精度毫秒）为指标时间戳。
        :rtype: str
        """
        return self._CustomTime

    @CustomTime.setter
    def CustomTime(self, CustomTime):
        self._CustomTime = CustomTime

    @property
    def CustomMetricLabels(self):
        """除了MetricLabels，您还可以使用该参数，为指标补充静态的维度。
维度名以字母或下划线开头，后面可以跟字母、数字或下划线，长度小于等于1024 字节
        :rtype: list of MetricLabel
        """
        return self._CustomMetricLabels

    @CustomMetricLabels.setter
    def CustomMetricLabels(self, CustomMetricLabels):
        self._CustomMetricLabels = CustomMetricLabels


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Region = params.get("Region")
        self._BizType = params.get("BizType")
        self._MetricName = params.get("MetricName")
        self._MetricNames = params.get("MetricNames")
        self._MetricLabels = params.get("MetricLabels")
        self._CustomTime = params.get("CustomTime")
        if params.get("CustomMetricLabels") is not None:
            self._CustomMetricLabels = []
            for item in params.get("CustomMetricLabels"):
                obj = MetricLabel()
                obj._deserialize(item)
                self._CustomMetricLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledSqlTaskInfo(AbstractModel):
    """ScheduledSql任务详情

    """

    def __init__(self):
        r"""
        :param _TaskId: ScheduledSql任务id
        :type TaskId: str
        :param _Name: ScheduledSql任务名称
        :type Name: str
        :param _SrcTopicId: 源日志主题id
        :type SrcTopicId: str
        :param _SrcTopicName: 源日志主题名称
        :type SrcTopicName: str
        :param _DstResource: 定时SQL分析目标主题
        :type DstResource: :class:`tencentcloud.cls.v20201016.models.ScheduledSqlResouceInfo`
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _UpdateTime: 任务更新时间
        :type UpdateTime: str
        :param _Status: 任务状态，1:运行 2:停止 3:异常-找不到源日志主题 4:异常-找不到目标主题

5: 访问权限问题 6:内部故障 7:其他故障
        :type Status: int
        :param _EnableFlag: 任务启用状态，1开启,  2关闭
        :type EnableFlag: int
        :param _ScheduledSqlContent: 查询语句
        :type ScheduledSqlContent: str
        :param _ProcessStartTime: 调度开始时间
        :type ProcessStartTime: str
        :param _ProcessType: 调度类型，1:持续运行 2:指定时间范围
        :type ProcessType: int
        :param _ProcessEndTime: 调度结束时间，当process_type=2时为必传字段
        :type ProcessEndTime: str
        :param _ProcessPeriod: 调度周期(分钟)
        :type ProcessPeriod: int
        :param _ProcessTimeWindow: 查询的时间窗口. @m-15m, @m，意为近15分钟
        :type ProcessTimeWindow: str
        :param _ProcessDelay: 执行延迟(秒)
        :type ProcessDelay: int
        :param _SrcTopicRegion: 源topicId的地域信息
        :type SrcTopicRegion: str
        :param _SyntaxRule: 语法规则，0：Lucene语法，1：CQL语法
        :type SyntaxRule: int
        :param _HasServicesLog: 是否开启投递服务日志。1：关闭，2：开启。
        :type HasServicesLog: int
        """
        self._TaskId = None
        self._Name = None
        self._SrcTopicId = None
        self._SrcTopicName = None
        self._DstResource = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._EnableFlag = None
        self._ScheduledSqlContent = None
        self._ProcessStartTime = None
        self._ProcessType = None
        self._ProcessEndTime = None
        self._ProcessPeriod = None
        self._ProcessTimeWindow = None
        self._ProcessDelay = None
        self._SrcTopicRegion = None
        self._SyntaxRule = None
        self._HasServicesLog = None

    @property
    def TaskId(self):
        """ScheduledSql任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """ScheduledSql任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SrcTopicId(self):
        """源日志主题id
        :rtype: str
        """
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def SrcTopicName(self):
        """源日志主题名称
        :rtype: str
        """
        return self._SrcTopicName

    @SrcTopicName.setter
    def SrcTopicName(self, SrcTopicName):
        self._SrcTopicName = SrcTopicName

    @property
    def DstResource(self):
        """定时SQL分析目标主题
        :rtype: :class:`tencentcloud.cls.v20201016.models.ScheduledSqlResouceInfo`
        """
        return self._DstResource

    @DstResource.setter
    def DstResource(self, DstResource):
        self._DstResource = DstResource

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """任务更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """任务状态，1:运行 2:停止 3:异常-找不到源日志主题 4:异常-找不到目标主题

5: 访问权限问题 6:内部故障 7:其他故障
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EnableFlag(self):
        """任务启用状态，1开启,  2关闭
        :rtype: int
        """
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def ScheduledSqlContent(self):
        """查询语句
        :rtype: str
        """
        return self._ScheduledSqlContent

    @ScheduledSqlContent.setter
    def ScheduledSqlContent(self, ScheduledSqlContent):
        self._ScheduledSqlContent = ScheduledSqlContent

    @property
    def ProcessStartTime(self):
        """调度开始时间
        :rtype: str
        """
        return self._ProcessStartTime

    @ProcessStartTime.setter
    def ProcessStartTime(self, ProcessStartTime):
        self._ProcessStartTime = ProcessStartTime

    @property
    def ProcessType(self):
        """调度类型，1:持续运行 2:指定时间范围
        :rtype: int
        """
        return self._ProcessType

    @ProcessType.setter
    def ProcessType(self, ProcessType):
        self._ProcessType = ProcessType

    @property
    def ProcessEndTime(self):
        """调度结束时间，当process_type=2时为必传字段
        :rtype: str
        """
        return self._ProcessEndTime

    @ProcessEndTime.setter
    def ProcessEndTime(self, ProcessEndTime):
        self._ProcessEndTime = ProcessEndTime

    @property
    def ProcessPeriod(self):
        """调度周期(分钟)
        :rtype: int
        """
        return self._ProcessPeriod

    @ProcessPeriod.setter
    def ProcessPeriod(self, ProcessPeriod):
        self._ProcessPeriod = ProcessPeriod

    @property
    def ProcessTimeWindow(self):
        """查询的时间窗口. @m-15m, @m，意为近15分钟
        :rtype: str
        """
        return self._ProcessTimeWindow

    @ProcessTimeWindow.setter
    def ProcessTimeWindow(self, ProcessTimeWindow):
        self._ProcessTimeWindow = ProcessTimeWindow

    @property
    def ProcessDelay(self):
        """执行延迟(秒)
        :rtype: int
        """
        return self._ProcessDelay

    @ProcessDelay.setter
    def ProcessDelay(self, ProcessDelay):
        self._ProcessDelay = ProcessDelay

    @property
    def SrcTopicRegion(self):
        """源topicId的地域信息
        :rtype: str
        """
        return self._SrcTopicRegion

    @SrcTopicRegion.setter
    def SrcTopicRegion(self, SrcTopicRegion):
        self._SrcTopicRegion = SrcTopicRegion

    @property
    def SyntaxRule(self):
        """语法规则，0：Lucene语法，1：CQL语法
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule

    @property
    def HasServicesLog(self):
        """是否开启投递服务日志。1：关闭，2：开启。
        :rtype: int
        """
        return self._HasServicesLog

    @HasServicesLog.setter
    def HasServicesLog(self, HasServicesLog):
        self._HasServicesLog = HasServicesLog


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._SrcTopicId = params.get("SrcTopicId")
        self._SrcTopicName = params.get("SrcTopicName")
        if params.get("DstResource") is not None:
            self._DstResource = ScheduledSqlResouceInfo()
            self._DstResource._deserialize(params.get("DstResource"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._EnableFlag = params.get("EnableFlag")
        self._ScheduledSqlContent = params.get("ScheduledSqlContent")
        self._ProcessStartTime = params.get("ProcessStartTime")
        self._ProcessType = params.get("ProcessType")
        self._ProcessEndTime = params.get("ProcessEndTime")
        self._ProcessPeriod = params.get("ProcessPeriod")
        self._ProcessTimeWindow = params.get("ProcessTimeWindow")
        self._ProcessDelay = params.get("ProcessDelay")
        self._SrcTopicRegion = params.get("SrcTopicRegion")
        self._SyntaxRule = params.get("SyntaxRule")
        self._HasServicesLog = params.get("HasServicesLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchCosRechargeInfoRequest(AbstractModel):
    """SearchCosRechargeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题 ID
        :type TopicId: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _Name: 投递任务名称
        :type Name: str
        :param _Bucket: COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。
        :type Bucket: str
        :param _BucketRegion: COS存储桶所在地域，详见产品支持的[地域列表](https://cloud.tencent.com/document/product/436/6224)。
        :type BucketRegion: str
        :param _Prefix: COS文件所在文件夹的前缀。默认为空，投递存储桶下所有的文件。
        :type Prefix: str
        :param _Compress: 压缩模式:   "", "gzip", "lzop", "snappy";   默认""
        :type Compress: str
        """
        self._TopicId = None
        self._LogsetId = None
        self._Name = None
        self._Bucket = None
        self._BucketRegion = None
        self._Prefix = None
        self._Compress = None

    @property
    def TopicId(self):
        """日志主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Name(self):
        """投递任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Bucket(self):
        """COS存储桶，详见产品支持的[存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def BucketRegion(self):
        """COS存储桶所在地域，详见产品支持的[地域列表](https://cloud.tencent.com/document/product/436/6224)。
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def Prefix(self):
        """COS文件所在文件夹的前缀。默认为空，投递存储桶下所有的文件。
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def Compress(self):
        """压缩模式:   "", "gzip", "lzop", "snappy";   默认""
        :rtype: str
        """
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Name = params.get("Name")
        self._Bucket = params.get("Bucket")
        self._BucketRegion = params.get("BucketRegion")
        self._Prefix = params.get("Prefix")
        self._Compress = params.get("Compress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchCosRechargeInfoResponse(AbstractModel):
    """SearchCosRechargeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 匹配到的存储桶下的某个文件的前几行数据
        :type Data: list of str
        :param _Sum: 匹配到的存储桶下的文件个数
        :type Sum: int
        :param _Path: 当前预览文件路径
        :type Path: str
        :param _Msg: 预览获取数据失败原因
        :type Msg: str
        :param _Status: 状态
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Sum = None
        self._Path = None
        self._Msg = None
        self._Status = None
        self._RequestId = None

    @property
    def Data(self):
        """匹配到的存储桶下的某个文件的前几行数据
        :rtype: list of str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Sum(self):
        """匹配到的存储桶下的文件个数
        :rtype: int
        """
        return self._Sum

    @Sum.setter
    def Sum(self, Sum):
        self._Sum = Sum

    @property
    def Path(self):
        """当前预览文件路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Msg(self):
        """预览获取数据失败原因
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Status(self):
        """状态
        :rtype: int
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
        self._Data = params.get("Data")
        self._Sum = params.get("Sum")
        self._Path = params.get("Path")
        self._Msg = params.get("Msg")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class SearchDashboardSubscribeRequest(AbstractModel):
    """SearchDashboardSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DashboardId: 仪表盘id。
        :type DashboardId: str
        :param _SubscribeData: 仪表盘订阅数据。
        :type SubscribeData: :class:`tencentcloud.cls.v20201016.models.DashboardSubscribeData`
        :param _Id: 仪表盘订阅Id。
        :type Id: int
        :param _Name: 仪表盘订阅名称。
        :type Name: str
        """
        self._DashboardId = None
        self._SubscribeData = None
        self._Id = None
        self._Name = None

    @property
    def DashboardId(self):
        """仪表盘id。
        :rtype: str
        """
        return self._DashboardId

    @DashboardId.setter
    def DashboardId(self, DashboardId):
        self._DashboardId = DashboardId

    @property
    def SubscribeData(self):
        """仪表盘订阅数据。
        :rtype: :class:`tencentcloud.cls.v20201016.models.DashboardSubscribeData`
        """
        return self._SubscribeData

    @SubscribeData.setter
    def SubscribeData(self, SubscribeData):
        self._SubscribeData = SubscribeData

    @property
    def Id(self):
        """仪表盘订阅Id。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """仪表盘订阅名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DashboardId = params.get("DashboardId")
        if params.get("SubscribeData") is not None:
            self._SubscribeData = DashboardSubscribeData()
            self._SubscribeData._deserialize(params.get("SubscribeData"))
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchDashboardSubscribeResponse(AbstractModel):
    """SearchDashboardSubscribe返回参数结构体

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


class SearchLogErrors(AbstractModel):
    """多日志主题检索错误信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _ErrorCodeStr: 错误码
        :type ErrorCodeStr: str
        """
        self._TopicId = None
        self._ErrorMsg = None
        self._ErrorCodeStr = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def ErrorMsg(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ErrorCodeStr(self):
        """错误码
        :rtype: str
        """
        return self._ErrorCodeStr

    @ErrorCodeStr.setter
    def ErrorCodeStr(self, ErrorCodeStr):
        self._ErrorCodeStr = ErrorCodeStr


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._ErrorCodeStr = params.get("ErrorCodeStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogInfos(AbstractModel):
    """多日志主题检索topic信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Period: 日志存储生命周期
        :type Period: int
        :param _Context: 透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时
        :type Context: str
        """
        self._TopicId = None
        self._Period = None
        self._Context = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Period(self):
        """日志存储生命周期
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Context(self):
        """透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Period = params.get("Period")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogRequest(AbstractModel):
    """SearchLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 要检索分析的日志的起始时间，Unix时间戳（毫秒）
        :type From: int
        :param _To: 要检索分析的日志的结束时间，Unix时间戳（毫秒）
        :type To: int
        :param _Query: 检索分析语句，最大长度为12KB
语句由 <a href="https://cloud.tencent.com/document/product/614/47044" target="_blank">[检索条件]</a> | <a href="https://cloud.tencent.com/document/product/614/44061" target="_blank">[SQL语句]</a>构成，无需对日志进行统计分析时，可省略其中的管道符<code> | </code>及SQL语句
使用*或空字符串可查询所有日志
        :type Query: str
        :param _SyntaxRule: 检索语法规则，默认值为0，推荐使用1 。

- 0：Lucene语法
- 1：CQL语法（日志服务专用检索语法，控制台默认也使用该语法规则）。

详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :type SyntaxRule: int
        :param _TopicId: - 要检索分析的日志主题ID，仅能指定一个日志主题。
- 如需同时检索多个日志主题，请使用Topics参数。
- TopicId 和 Topics 不能同时使用，在一次请求中有且只能选择一个。
        :type TopicId: str
        :param _Topics: - 要检索分析的日志主题列表，最大支持50个日志主题。
- 检索单个日志主题时请使用TopicId。
- TopicId 和 Topics 不能同时使用，在一次请求中有且只能选择一个。
        :type Topics: list of MultiTopicSearchInformation
        :param _Sort: 原始日志是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果排序方式参考<a href="https://cloud.tencent.com/document/product/614/58978" target="_blank">SQL ORDER BY语法</a>
        :type Sort: str
        :param _Limit: 表示单次查询返回的原始日志条数，默认为100，最大值为1000。
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果条数指定方式参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>

可通过两种方式获取后续更多日志：
* Context:透传上次接口返回的Context值，获取后续更多日志，总计最多可获取1万条原始日志
* Offset:偏移量，表示从第几行开始返回原始日志，无日志条数限制
        :type Limit: int
        :param _Offset: 查询原始日志的偏移量，表示从第几行开始返回原始日志，默认为0。 
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* 不能与Context参数同时使用
* 仅适用于单日志主题检索
        :type Offset: int
        :param _Context: 透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时。
注意：
* 透传该参数时，请勿修改除该参数外的其它参数
* 仅适用于单日志主题检索，检索多个日志主题时，请使用Topics中的Context
* 仅当检索分析语句(Query)不包含SQL时有效，SQL获取后续结果参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>
        :type Context: str
        :param _SamplingRate: 执行统计分析（Query中包含SQL）时，是否对原始日志先进行采样，再进行统计分析。
0：自动采样;
0～1：按指定采样率采样，例如0.02;
1：不采样，即精确分析
默认值为1
        :type SamplingRate: float
        :param _UseNewAnalysis: 为true代表使用新的检索结果返回方式，输出参数AnalysisRecords和Columns有效
为false时代表使用老的检索结果返回方式, 输出AnalysisResults和ColNames有效
两种返回方式在编码格式上有少量区别，建议使用true
        :type UseNewAnalysis: bool
        """
        self._From = None
        self._To = None
        self._Query = None
        self._SyntaxRule = None
        self._TopicId = None
        self._Topics = None
        self._Sort = None
        self._Limit = None
        self._Offset = None
        self._Context = None
        self._SamplingRate = None
        self._UseNewAnalysis = None

    @property
    def From(self):
        """要检索分析的日志的起始时间，Unix时间戳（毫秒）
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """要检索分析的日志的结束时间，Unix时间戳（毫秒）
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        """检索分析语句，最大长度为12KB
语句由 <a href="https://cloud.tencent.com/document/product/614/47044" target="_blank">[检索条件]</a> | <a href="https://cloud.tencent.com/document/product/614/44061" target="_blank">[SQL语句]</a>构成，无需对日志进行统计分析时，可省略其中的管道符<code> | </code>及SQL语句
使用*或空字符串可查询所有日志
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def SyntaxRule(self):
        """检索语法规则，默认值为0，推荐使用1 。

- 0：Lucene语法
- 1：CQL语法（日志服务专用检索语法，控制台默认也使用该语法规则）。

详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule

    @property
    def TopicId(self):
        """- 要检索分析的日志主题ID，仅能指定一个日志主题。
- 如需同时检索多个日志主题，请使用Topics参数。
- TopicId 和 Topics 不能同时使用，在一次请求中有且只能选择一个。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Topics(self):
        """- 要检索分析的日志主题列表，最大支持50个日志主题。
- 检索单个日志主题时请使用TopicId。
- TopicId 和 Topics 不能同时使用，在一次请求中有且只能选择一个。
        :rtype: list of MultiTopicSearchInformation
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def Sort(self):
        """原始日志是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果排序方式参考<a href="https://cloud.tencent.com/document/product/614/58978" target="_blank">SQL ORDER BY语法</a>
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Limit(self):
        """表示单次查询返回的原始日志条数，默认为100，最大值为1000。
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果条数指定方式参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>

可通过两种方式获取后续更多日志：
* Context:透传上次接口返回的Context值，获取后续更多日志，总计最多可获取1万条原始日志
* Offset:偏移量，表示从第几行开始返回原始日志，无日志条数限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询原始日志的偏移量，表示从第几行开始返回原始日志，默认为0。 
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* 不能与Context参数同时使用
* 仅适用于单日志主题检索
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Context(self):
        """透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时。
注意：
* 透传该参数时，请勿修改除该参数外的其它参数
* 仅适用于单日志主题检索，检索多个日志主题时，请使用Topics中的Context
* 仅当检索分析语句(Query)不包含SQL时有效，SQL获取后续结果参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def SamplingRate(self):
        """执行统计分析（Query中包含SQL）时，是否对原始日志先进行采样，再进行统计分析。
0：自动采样;
0～1：按指定采样率采样，例如0.02;
1：不采样，即精确分析
默认值为1
        :rtype: float
        """
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def UseNewAnalysis(self):
        """为true代表使用新的检索结果返回方式，输出参数AnalysisRecords和Columns有效
为false时代表使用老的检索结果返回方式, 输出AnalysisResults和ColNames有效
两种返回方式在编码格式上有少量区别，建议使用true
        :rtype: bool
        """
        return self._UseNewAnalysis

    @UseNewAnalysis.setter
    def UseNewAnalysis(self, UseNewAnalysis):
        self._UseNewAnalysis = UseNewAnalysis


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._SyntaxRule = params.get("SyntaxRule")
        self._TopicId = params.get("TopicId")
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = MultiTopicSearchInformation()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._Sort = params.get("Sort")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Context = params.get("Context")
        self._SamplingRate = params.get("SamplingRate")
        self._UseNewAnalysis = params.get("UseNewAnalysis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogResponse(AbstractModel):
    """SearchLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时。
注意：
* 仅适用于单日志主题检索，检索多个日志主题时，请使用Topics中的Context
        :type Context: str
        :param _ListOver: 符合检索条件的日志是否已全部返回，如未全部返回可使用Context参数获取后续更多日志
注意：仅当检索分析语句(Query)不包含SQL时有效
        :type ListOver: bool
        :param _Analysis: 返回的是否为统计分析（即SQL）结果
        :type Analysis: bool
        :param _Results: 匹配检索条件的原始日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of LogInfo
        :param _ColNames: 日志统计分析结果的列名
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param _AnalysisResults: 日志统计分析结果
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of LogItems
        :param _AnalysisRecords: 日志统计分析结果
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisRecords: list of str
        :param _Columns: 日志统计分析结果的列属性
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param _SamplingRate: 本次统计分析使用的采样率
        :type SamplingRate: float
        :param _Topics: 使用多日志主题检索时，各个日志主题的基本信息，例如报错信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: :class:`tencentcloud.cls.v20201016.models.SearchLogTopics`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Analysis = None
        self._Results = None
        self._ColNames = None
        self._AnalysisResults = None
        self._AnalysisRecords = None
        self._Columns = None
        self._SamplingRate = None
        self._Topics = None
        self._RequestId = None

    @property
    def Context(self):
        """透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时。
注意：
* 仅适用于单日志主题检索，检索多个日志主题时，请使用Topics中的Context
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        """符合检索条件的日志是否已全部返回，如未全部返回可使用Context参数获取后续更多日志
注意：仅当检索分析语句(Query)不包含SQL时有效
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Analysis(self):
        """返回的是否为统计分析（即SQL）结果
        :rtype: bool
        """
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def Results(self):
        """匹配检索条件的原始日志
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogInfo
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def ColNames(self):
        """日志统计分析结果的列名
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ColNames

    @ColNames.setter
    def ColNames(self, ColNames):
        self._ColNames = ColNames

    @property
    def AnalysisResults(self):
        """日志统计分析结果
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogItems
        """
        return self._AnalysisResults

    @AnalysisResults.setter
    def AnalysisResults(self, AnalysisResults):
        self._AnalysisResults = AnalysisResults

    @property
    def AnalysisRecords(self):
        """日志统计分析结果
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AnalysisRecords

    @AnalysisRecords.setter
    def AnalysisRecords(self, AnalysisRecords):
        self._AnalysisRecords = AnalysisRecords

    @property
    def Columns(self):
        """日志统计分析结果的列属性
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Column
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def SamplingRate(self):
        """本次统计分析使用的采样率
        :rtype: float
        """
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def Topics(self):
        """使用多日志主题检索时，各个日志主题的基本信息，例如报错信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.SearchLogTopics`
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

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
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        self._Analysis = params.get("Analysis")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Results.append(obj)
        self._ColNames = params.get("ColNames")
        if params.get("AnalysisResults") is not None:
            self._AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self._AnalysisResults.append(obj)
        self._AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._SamplingRate = params.get("SamplingRate")
        if params.get("Topics") is not None:
            self._Topics = SearchLogTopics()
            self._Topics._deserialize(params.get("Topics"))
        self._RequestId = params.get("RequestId")


class SearchLogTopics(AbstractModel):
    """多主题检索返回信息

    """

    def __init__(self):
        r"""
        :param _Errors: 多日志主题检索对应的错误信息
        :type Errors: list of SearchLogErrors
        :param _Infos: 多日志主题检索各日志主题信息
        :type Infos: list of SearchLogInfos
        """
        self._Errors = None
        self._Infos = None

    @property
    def Errors(self):
        """多日志主题检索对应的错误信息
        :rtype: list of SearchLogErrors
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Infos(self):
        """多日志主题检索各日志主题信息
        :rtype: list of SearchLogInfos
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos


    def _deserialize(self, params):
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SearchLogErrors()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = SearchLogInfos()
                obj._deserialize(item)
                self._Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipperInfo(AbstractModel):
    """投递规则

    """

    def __init__(self):
        r"""
        :param _ShipperId: 投递规则ID
        :type ShipperId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Bucket: 投递的bucket地址
        :type Bucket: str
        :param _Prefix: 投递的前缀目录
        :type Prefix: str
        :param _ShipperName: 投递规则的名字
        :type ShipperName: str
        :param _Interval: 投递的时间间隔，单位 秒
        :type Interval: int
        :param _MaxSize: 投递的文件的最大值，单位 MB
        :type MaxSize: int
        :param _Status: 是否生效
        :type Status: bool
        :param _FilterRules: 投递日志的过滤规则
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: 投递日志的分区规则，支持strftime的时间格式表示
        :type Partition: str
        :param _Compress: 投递日志的压缩配置
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: 投递日志的内容格式配置
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _CreateTime: 投递日志的创建时间
        :type CreateTime: str
        :param _FilenameMode: 投递文件命名配置，0：随机数命名，1：投递时间命名，默认0（随机数命名）
        :type FilenameMode: int
        :param _StartTime: 投递数据范围的开始时间点
        :type StartTime: int
        :param _EndTime: 投递数据范围的结束时间点
        :type EndTime: int
        :param _Progress: 历史数据投递的进度（仅当用户选择的数据内中历史数据时才有效）
        :type Progress: float
        :param _RemainTime: 历史数据全部投递完成剩余的时间（仅当用户选择的数据中有历史数据时才有效）
        :type RemainTime: int
        :param _HistoryStatus: 历史任务状态：
0：实时任务
1：任务准备中
2：任务运行中
3：任务运行异常
4：任务运行结束
        :type HistoryStatus: int
        :param _StorageType: cos桶类型
        :type StorageType: str
        """
        self._ShipperId = None
        self._TopicId = None
        self._Bucket = None
        self._Prefix = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._Status = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._CreateTime = None
        self._FilenameMode = None
        self._StartTime = None
        self._EndTime = None
        self._Progress = None
        self._RemainTime = None
        self._HistoryStatus = None
        self._StorageType = None

    @property
    def ShipperId(self):
        """投递规则ID
        :rtype: str
        """
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Bucket(self):
        """投递的bucket地址
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        """投递的前缀目录
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def ShipperName(self):
        """投递规则的名字
        :rtype: str
        """
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        """投递的时间间隔，单位 秒
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        """投递的文件的最大值，单位 MB
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def Status(self):
        """是否生效
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FilterRules(self):
        """投递日志的过滤规则
        :rtype: list of FilterRuleInfo
        """
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        """投递日志的分区规则，支持strftime的时间格式表示
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        """投递日志的压缩配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        """
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        """投递日志的内容格式配置
        :rtype: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CreateTime(self):
        """投递日志的创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FilenameMode(self):
        """投递文件命名配置，0：随机数命名，1：投递时间命名，默认0（随机数命名）
        :rtype: int
        """
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode

    @property
    def StartTime(self):
        """投递数据范围的开始时间点
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """投递数据范围的结束时间点
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Progress(self):
        """历史数据投递的进度（仅当用户选择的数据内中历史数据时才有效）
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RemainTime(self):
        """历史数据全部投递完成剩余的时间（仅当用户选择的数据中有历史数据时才有效）
        :rtype: int
        """
        return self._RemainTime

    @RemainTime.setter
    def RemainTime(self, RemainTime):
        self._RemainTime = RemainTime

    @property
    def HistoryStatus(self):
        """历史任务状态：
0：实时任务
1：任务准备中
2：任务运行中
3：任务运行异常
4：任务运行结束
        :rtype: int
        """
        return self._HistoryStatus

    @HistoryStatus.setter
    def HistoryStatus(self, HistoryStatus):
        self._HistoryStatus = HistoryStatus

    @property
    def StorageType(self):
        """cos桶类型
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._TopicId = params.get("TopicId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        self._Status = params.get("Status")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._CreateTime = params.get("CreateTime")
        self._FilenameMode = params.get("FilenameMode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Progress = params.get("Progress")
        self._RemainTime = params.get("RemainTime")
        self._HistoryStatus = params.get("HistoryStatus")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipperTaskInfo(AbstractModel):
    """投递任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 投递任务ID
        :type TaskId: str
        :param _ShipperId: 投递信息ID
        :type ShipperId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _RangeStart: 本批投递的日志的开始时间戳，毫秒
        :type RangeStart: int
        :param _RangeEnd: 本批投递的日志的结束时间戳， 毫秒
        :type RangeEnd: int
        :param _StartTime: 本次投递任务的开始时间戳， 毫秒
        :type StartTime: int
        :param _EndTime: 本次投递任务的结束时间戳， 毫秒
        :type EndTime: int
        :param _Status: 本次投递的结果，"success","running","failed"
        :type Status: str
        :param _Message: 结果的详细信息
        :type Message: str
        """
        self._TaskId = None
        self._ShipperId = None
        self._TopicId = None
        self._RangeStart = None
        self._RangeEnd = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Message = None

    @property
    def TaskId(self):
        """投递任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ShipperId(self):
        """投递信息ID
        :rtype: str
        """
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RangeStart(self):
        """本批投递的日志的开始时间戳，毫秒
        :rtype: int
        """
        return self._RangeStart

    @RangeStart.setter
    def RangeStart(self, RangeStart):
        self._RangeStart = RangeStart

    @property
    def RangeEnd(self):
        """本批投递的日志的结束时间戳， 毫秒
        :rtype: int
        """
        return self._RangeEnd

    @RangeEnd.setter
    def RangeEnd(self, RangeEnd):
        self._RangeEnd = RangeEnd

    @property
    def StartTime(self):
        """本次投递任务的开始时间戳， 毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """本次投递任务的结束时间戳， 毫秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """本次投递的结果，"success","running","failed"
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        """结果的详细信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ShipperId = params.get("ShipperId")
        self._TopicId = params.get("TopicId")
        self._RangeStart = params.get("RangeStart")
        self._RangeEnd = params.get("RangeEnd")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionRequest(AbstractModel):
    """SplitPartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _PartitionId: 待分裂分区ID
        :type PartitionId: int
        :param _SplitKey: 分区切分的哈希key的位置，只在Number=2时有意义
        :type SplitKey: str
        :param _Number: 分区分裂个数(可选)，默认等于2
        :type Number: int
        """
        self._TopicId = None
        self._PartitionId = None
        self._SplitKey = None
        self._Number = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionId(self):
        """待分裂分区ID
        :rtype: int
        """
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId

    @property
    def SplitKey(self):
        """分区切分的哈希key的位置，只在Number=2时有意义
        :rtype: str
        """
        return self._SplitKey

    @SplitKey.setter
    def SplitKey(self, SplitKey):
        self._SplitKey = SplitKey

    @property
    def Number(self):
        """分区分裂个数(可选)，默认等于2
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._PartitionId = params.get("PartitionId")
        self._SplitKey = params.get("SplitKey")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionResponse(AbstractModel):
    """SplitPartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 分裂结果集
        :type Partitions: list of PartitionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        """分裂结果集
        :rtype: list of PartitionInfo
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

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
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """创建资源实例时同时绑定的标签对说明

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
        """标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值
        :rtype: str
        """
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
        


class TopicExtendInfo(AbstractModel):
    """日志主题扩展信息

    """

    def __init__(self):
        r"""
        :param _AnonymousAccess: 日志主题免鉴权配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AnonymousAccess: :class:`tencentcloud.cls.v20201016.models.AnonymousInfo`
        """
        self._AnonymousAccess = None

    @property
    def AnonymousAccess(self):
        """日志主题免鉴权配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cls.v20201016.models.AnonymousInfo`
        """
        return self._AnonymousAccess

    @AnonymousAccess.setter
    def AnonymousAccess(self, AnonymousAccess):
        self._AnonymousAccess = AnonymousAccess


    def _deserialize(self, params):
        if params.get("AnonymousAccess") is not None:
            self._AnonymousAccess = AnonymousInfo()
            self._AnonymousAccess._deserialize(params.get("AnonymousAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicIdAndRegion(AbstractModel):
    """仪表盘 topic与地域信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题id
        :type TopicId: str
        :param _RegionId: 日志主题id所在的地域id。

id,地域,简称信息如下：
- 1,   广州,ap-guangzhou
- 4,   上海,ap-shanghai
- 5,   中国香港,ap-hongkong
- 7,   上海金融,ap-shanghai-fsi
- 8,   北京,ap-beijing
- 9,   新加坡,ap-singapore
- 11,  深圳金融,ap-shenzhen-fsi
- 15,  硅谷,na-siliconvalley
- 16,  成都,ap-chengdu
- 17,  法兰克福,eu-frankfurt
- 18,  首尔,ap-seoul
- 19,  重庆,ap-chongqing
- 22,  弗吉尼亚,na-ashburn
- 23,  曼谷,ap-bangkok
- 25,  东京,ap-tokyo
- 33,  南京,ap-nanjing
- 46,  北京金融,ap-beijing-fsi
- 72,  雅加达,ap-jakarta
- 74,  圣保罗,sa-saopaulo
        :type RegionId: int
        """
        self._TopicId = None
        self._RegionId = None

    @property
    def TopicId(self):
        """日志主题id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RegionId(self):
        """日志主题id所在的地域id。

id,地域,简称信息如下：
- 1,   广州,ap-guangzhou
- 4,   上海,ap-shanghai
- 5,   中国香港,ap-hongkong
- 7,   上海金融,ap-shanghai-fsi
- 8,   北京,ap-beijing
- 9,   新加坡,ap-singapore
- 11,  深圳金融,ap-shenzhen-fsi
- 15,  硅谷,na-siliconvalley
- 16,  成都,ap-chengdu
- 17,  法兰克福,eu-frankfurt
- 18,  首尔,ap-seoul
- 19,  重庆,ap-chongqing
- 22,  弗吉尼亚,na-ashburn
- 23,  曼谷,ap-bangkok
- 25,  东京,ap-tokyo
- 33,  南京,ap-nanjing
- 46,  北京金融,ap-beijing-fsi
- 72,  雅加达,ap-jakarta
- 74,  圣保罗,sa-saopaulo
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInfo(AbstractModel):
    """主题基本信息

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicId: 主题ID
        :type TopicId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _PartitionCount: 主题分区个数
        :type PartitionCount: int
        :param _Index: 主题是否开启索引（主题类型需为日志主题）
        :type Index: bool
        :param _AssumerName: 云产品标识，主题由其它云产品创建时，该字段会显示云产品名称，例如CDN、TKE
        :type AssumerName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Status: 主题是否开启采集，true：开启采集；false：关闭采集。
创建日志主题时默认开启，可通过SDK调用ModifyTopic修改此字段。
控制台目前不支持修改此参数。
        :type Status: bool
        :param _Tags: 主题绑定的标签信息
        :type Tags: list of Tag
        :param _AutoSplit: 该主题是否开启自动分裂
        :type AutoSplit: bool
        :param _MaxSplitPartitions: 若开启自动分裂的话，该主题能够允许的最大分区数
        :type MaxSplitPartitions: int
        :param _StorageType: 主题的存储类型

- hot: 标准存储
- cold: 低频存储
        :type StorageType: str
        :param _Period: 生命周期，单位天，可取值范围1~3600。取值为3640时代表永久保存
        :type Period: int
        :param _SubAssumerName: 云产品二级标识，日志主题由其它云产品创建时，该字段会显示云产品名称及其日志类型的二级分类，例如TKE-Audit、TKE-Event。部分云产品仅有云产品标识(AssumerName)，无该字段。
        :type SubAssumerName: str
        :param _Describes: 主题描述
        :type Describes: str
        :param _HotPeriod: 开启日志沉降，标准存储的生命周期， hotPeriod < Period。
标准存储为 hotPeriod, 低频存储则为 Period-hotPeriod。（主题类型需为日志主题）
HotPeriod=0为没有开启日志沉降。
        :type HotPeriod: int
        :param _BizType: 主题类型。
- 0: 日志主题 
- 1: 指标主题
        :type BizType: int
        :param _IsWebTracking: 免鉴权开关。 false：关闭； true：开启。
开启后将支持指定操作匿名访问该日志主题。详情请参见[日志主题](https://cloud.tencent.com/document/product/614/41035)。
        :type IsWebTracking: bool
        :param _Extends: 日志主题扩展信息
        :type Extends: :class:`tencentcloud.cls.v20201016.models.TopicExtendInfo`
        :param _TopicAsyncTaskID: 异步迁移任务ID
        :type TopicAsyncTaskID: str
        :param _MigrationStatus: 异步迁移状态
        :type MigrationStatus: int
        :param _EffectiveDate: 异步迁移完成后，预计生效日期
        :type EffectiveDate: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._TopicName = None
        self._PartitionCount = None
        self._Index = None
        self._AssumerName = None
        self._CreateTime = None
        self._Status = None
        self._Tags = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._StorageType = None
        self._Period = None
        self._SubAssumerName = None
        self._Describes = None
        self._HotPeriod = None
        self._BizType = None
        self._IsWebTracking = None
        self._Extends = None
        self._TopicAsyncTaskID = None
        self._MigrationStatus = None
        self._EffectiveDate = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        """主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionCount(self):
        """主题分区个数
        :rtype: int
        """
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def Index(self):
        """主题是否开启索引（主题类型需为日志主题）
        :rtype: bool
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AssumerName(self):
        """云产品标识，主题由其它云产品创建时，该字段会显示云产品名称，例如CDN、TKE
        :rtype: str
        """
        return self._AssumerName

    @AssumerName.setter
    def AssumerName(self, AssumerName):
        self._AssumerName = AssumerName

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
    def Status(self):
        """主题是否开启采集，true：开启采集；false：关闭采集。
创建日志主题时默认开启，可通过SDK调用ModifyTopic修改此字段。
控制台目前不支持修改此参数。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        """主题绑定的标签信息
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoSplit(self):
        """该主题是否开启自动分裂
        :rtype: bool
        """
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        """若开启自动分裂的话，该主题能够允许的最大分区数
        :rtype: int
        """
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def StorageType(self):
        """主题的存储类型

- hot: 标准存储
- cold: 低频存储
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Period(self):
        """生命周期，单位天，可取值范围1~3600。取值为3640时代表永久保存
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SubAssumerName(self):
        """云产品二级标识，日志主题由其它云产品创建时，该字段会显示云产品名称及其日志类型的二级分类，例如TKE-Audit、TKE-Event。部分云产品仅有云产品标识(AssumerName)，无该字段。
        :rtype: str
        """
        return self._SubAssumerName

    @SubAssumerName.setter
    def SubAssumerName(self, SubAssumerName):
        self._SubAssumerName = SubAssumerName

    @property
    def Describes(self):
        """主题描述
        :rtype: str
        """
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        """开启日志沉降，标准存储的生命周期， hotPeriod < Period。
标准存储为 hotPeriod, 低频存储则为 Period-hotPeriod。（主题类型需为日志主题）
HotPeriod=0为没有开启日志沉降。
        :rtype: int
        """
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod

    @property
    def BizType(self):
        """主题类型。
- 0: 日志主题 
- 1: 指标主题
        :rtype: int
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def IsWebTracking(self):
        """免鉴权开关。 false：关闭； true：开启。
开启后将支持指定操作匿名访问该日志主题。详情请参见[日志主题](https://cloud.tencent.com/document/product/614/41035)。
        :rtype: bool
        """
        return self._IsWebTracking

    @IsWebTracking.setter
    def IsWebTracking(self, IsWebTracking):
        self._IsWebTracking = IsWebTracking

    @property
    def Extends(self):
        """日志主题扩展信息
        :rtype: :class:`tencentcloud.cls.v20201016.models.TopicExtendInfo`
        """
        return self._Extends

    @Extends.setter
    def Extends(self, Extends):
        self._Extends = Extends

    @property
    def TopicAsyncTaskID(self):
        """异步迁移任务ID
        :rtype: str
        """
        return self._TopicAsyncTaskID

    @TopicAsyncTaskID.setter
    def TopicAsyncTaskID(self, TopicAsyncTaskID):
        self._TopicAsyncTaskID = TopicAsyncTaskID

    @property
    def MigrationStatus(self):
        """异步迁移状态
        :rtype: int
        """
        return self._MigrationStatus

    @MigrationStatus.setter
    def MigrationStatus(self, MigrationStatus):
        self._MigrationStatus = MigrationStatus

    @property
    def EffectiveDate(self):
        """异步迁移完成后，预计生效日期
        :rtype: str
        """
        return self._EffectiveDate

    @EffectiveDate.setter
    def EffectiveDate(self, EffectiveDate):
        self._EffectiveDate = EffectiveDate


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._PartitionCount = params.get("PartitionCount")
        self._Index = params.get("Index")
        self._AssumerName = params.get("AssumerName")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._StorageType = params.get("StorageType")
        self._Period = params.get("Period")
        self._SubAssumerName = params.get("SubAssumerName")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        self._BizType = params.get("BizType")
        self._IsWebTracking = params.get("IsWebTracking")
        if params.get("Extends") is not None:
            self._Extends = TopicExtendInfo()
            self._Extends._deserialize(params.get("Extends"))
        self._TopicAsyncTaskID = params.get("TopicAsyncTaskID")
        self._MigrationStatus = params.get("MigrationStatus")
        self._EffectiveDate = params.get("EffectiveDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogRequest(AbstractModel):
    """UploadLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题id
        :type TopicId: str
        :param _HashKey: 该参数已废弃，请勿使用
        :type HashKey: str
        :param _CompressType: 压缩方法
        :type CompressType: str
        """
        self._TopicId = None
        self._HashKey = None
        self._CompressType = None

    @property
    def TopicId(self):
        """主题id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def HashKey(self):
        warnings.warn("parameter `HashKey` is deprecated", DeprecationWarning) 

        """该参数已废弃，请勿使用
        :rtype: str
        """
        return self._HashKey

    @HashKey.setter
    def HashKey(self, HashKey):
        warnings.warn("parameter `HashKey` is deprecated", DeprecationWarning) 

        self._HashKey = HashKey

    @property
    def CompressType(self):
        """压缩方法
        :rtype: str
        """
        return self._CompressType

    @CompressType.setter
    def CompressType(self, CompressType):
        self._CompressType = CompressType


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._HashKey = params.get("HashKey")
        self._CompressType = params.get("CompressType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogResponse(AbstractModel):
    """UploadLog返回参数结构体

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


class ValueInfo(AbstractModel):
    """需要开启键值索引的字段的索引描述信息

    """

    def __init__(self):
        r"""
        :param _Type: 字段类型，目前支持的类型有：long、text、double
        :type Type: str
        :param _Tokenizer: 字段的分词符，其中的每个字符代表一个分词符；
仅支持英文符号、\n\t\r及转义符\；
long及double类型字段需为空；
注意：\n\t\r本身已被转义，直接使用双引号包裹即可作为入参，无需再次转义。使用API Explorer进行调试时请使用JSON参数输入方式，以避免\n\t\r被重复转义
        :type Tokenizer: str
        :param _SqlFlag: 字段是否开启分析功能
        :type SqlFlag: bool
        :param _ContainZH: 是否包含中文，long及double类型字段需为false
        :type ContainZH: bool
        """
        self._Type = None
        self._Tokenizer = None
        self._SqlFlag = None
        self._ContainZH = None

    @property
    def Type(self):
        """字段类型，目前支持的类型有：long、text、double
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tokenizer(self):
        """字段的分词符，其中的每个字符代表一个分词符；
仅支持英文符号、\n\t\r及转义符\；
long及double类型字段需为空；
注意：\n\t\r本身已被转义，直接使用双引号包裹即可作为入参，无需再次转义。使用API Explorer进行调试时请使用JSON参数输入方式，以避免\n\t\r被重复转义
        :rtype: str
        """
        return self._Tokenizer

    @Tokenizer.setter
    def Tokenizer(self, Tokenizer):
        self._Tokenizer = Tokenizer

    @property
    def SqlFlag(self):
        """字段是否开启分析功能
        :rtype: bool
        """
        return self._SqlFlag

    @SqlFlag.setter
    def SqlFlag(self, SqlFlag):
        self._SqlFlag = SqlFlag

    @property
    def ContainZH(self):
        """是否包含中文，long及double类型字段需为false
        :rtype: bool
        """
        return self._ContainZH

    @ContainZH.setter
    def ContainZH(self, ContainZH):
        self._ContainZH = ContainZH


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Tokenizer = params.get("Tokenizer")
        self._SqlFlag = params.get("SqlFlag")
        self._ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebCallback(AbstractModel):
    """回调地址

    """

    def __init__(self):
        r"""
        :param _CallbackType: 回调的类型。可选值：
- Http
- WeCom
- DingTalk
- Lark
        :type CallbackType: str
        :param _Url: 回调地址，最大支持1024个字节。
也可使用WebCallbackId引用集成配置中的URL，此时该字段请填写为空字符串。
        :type Url: str
        :param _WebCallbackId: 集成配置ID。
        :type WebCallbackId: str
        :param _Method: 回调方法。可选值：
- POST（默认值）
- PUT

注意：
- 参数CallbackType为Http时为必选，其它回调方式无需填写。
        :type Method: str
        :param _NoticeContentId: 通知内容模板ID，使用Default-zh引用默认模板（中文），使用Default-en引用DefaultTemplate(English)。
        :type NoticeContentId: str
        :param _RemindType: 提醒类型。

0：不提醒；1：指定人；2：所有人
        :type RemindType: int
        :param _Mobiles: 电话列表。
        :type Mobiles: list of str
        :param _UserIds: 用户ID列表。
        :type UserIds: list of str
        :param _Headers: 该参数已废弃，请使用NoticeContentId。
        :type Headers: list of str
        :param _Body: 该参数已废弃，请使用NoticeContentId。
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        :param _Index: 序号。
- 入参无效。
- 出参有效。
        :type Index: int
        """
        self._CallbackType = None
        self._Url = None
        self._WebCallbackId = None
        self._Method = None
        self._NoticeContentId = None
        self._RemindType = None
        self._Mobiles = None
        self._UserIds = None
        self._Headers = None
        self._Body = None
        self._Index = None

    @property
    def CallbackType(self):
        """回调的类型。可选值：
- Http
- WeCom
- DingTalk
- Lark
        :rtype: str
        """
        return self._CallbackType

    @CallbackType.setter
    def CallbackType(self, CallbackType):
        self._CallbackType = CallbackType

    @property
    def Url(self):
        """回调地址，最大支持1024个字节。
也可使用WebCallbackId引用集成配置中的URL，此时该字段请填写为空字符串。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def WebCallbackId(self):
        """集成配置ID。
        :rtype: str
        """
        return self._WebCallbackId

    @WebCallbackId.setter
    def WebCallbackId(self, WebCallbackId):
        self._WebCallbackId = WebCallbackId

    @property
    def Method(self):
        """回调方法。可选值：
- POST（默认值）
- PUT

注意：
- 参数CallbackType为Http时为必选，其它回调方式无需填写。
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def NoticeContentId(self):
        """通知内容模板ID，使用Default-zh引用默认模板（中文），使用Default-en引用DefaultTemplate(English)。
        :rtype: str
        """
        return self._NoticeContentId

    @NoticeContentId.setter
    def NoticeContentId(self, NoticeContentId):
        self._NoticeContentId = NoticeContentId

    @property
    def RemindType(self):
        """提醒类型。

0：不提醒；1：指定人；2：所有人
        :rtype: int
        """
        return self._RemindType

    @RemindType.setter
    def RemindType(self, RemindType):
        self._RemindType = RemindType

    @property
    def Mobiles(self):
        """电话列表。
        :rtype: list of str
        """
        return self._Mobiles

    @Mobiles.setter
    def Mobiles(self, Mobiles):
        self._Mobiles = Mobiles

    @property
    def UserIds(self):
        """用户ID列表。
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def Headers(self):
        """该参数已废弃，请使用NoticeContentId。
        :rtype: list of str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Body(self):
        """该参数已废弃，请使用NoticeContentId。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Index(self):
        """序号。
- 入参无效。
- 出参有效。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._CallbackType = params.get("CallbackType")
        self._Url = params.get("Url")
        self._WebCallbackId = params.get("WebCallbackId")
        self._Method = params.get("Method")
        self._NoticeContentId = params.get("NoticeContentId")
        self._RemindType = params.get("RemindType")
        self._Mobiles = params.get("Mobiles")
        self._UserIds = params.get("UserIds")
        self._Headers = params.get("Headers")
        self._Body = params.get("Body")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebCallbackInfo(AbstractModel):
    """告警渠道回调配置信息

    """

    def __init__(self):
        r"""
        :param _WebCallbackId: 告警渠道回调配置id。
        :type WebCallbackId: str
        :param _Name: 告警渠道回调配置名称。
        :type Name: str
        :param _Type: 渠道类型

WeCom:企业微信;DingTalk:钉钉;Lark:飞书;Http:自定义回调;
        :type Type: str
        :param _Webhook: 回调地址。
        :type Webhook: str
        :param _Method: 请求方式。
        :type Method: str
        :param _Key: 秘钥信息。
        :type Key: str
        :param _Uin: 主账号。
        :type Uin: int
        :param _SubUin: 子账号。
        :type SubUin: int
        :param _CreateTime: 创建时间。秒级时间戳
        :type CreateTime: int
        :param _UpdateTime: 更新时间。秒级时间戳
        :type UpdateTime: int
        """
        self._WebCallbackId = None
        self._Name = None
        self._Type = None
        self._Webhook = None
        self._Method = None
        self._Key = None
        self._Uin = None
        self._SubUin = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def WebCallbackId(self):
        """告警渠道回调配置id。
        :rtype: str
        """
        return self._WebCallbackId

    @WebCallbackId.setter
    def WebCallbackId(self, WebCallbackId):
        self._WebCallbackId = WebCallbackId

    @property
    def Name(self):
        """告警渠道回调配置名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """渠道类型

WeCom:企业微信;DingTalk:钉钉;Lark:飞书;Http:自定义回调;
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Webhook(self):
        """回调地址。
        :rtype: str
        """
        return self._Webhook

    @Webhook.setter
    def Webhook(self, Webhook):
        self._Webhook = Webhook

    @property
    def Method(self):
        """请求方式。
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Key(self):
        """秘钥信息。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Uin(self):
        """主账号。
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        """子账号。
        :rtype: int
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def CreateTime(self):
        """创建时间。秒级时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间。秒级时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._WebCallbackId = params.get("WebCallbackId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Webhook = params.get("Webhook")
        self._Method = params.get("Method")
        self._Key = params.get("Key")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        