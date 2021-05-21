# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class AlarmEvent(AbstractModel):
    """告警事件

    """

    def __init__(self):
        """
        :param EventName: 事件名
        :type EventName: str
        :param Description: 展示的事件名
        :type Description: str
        :param Namespace: 告警策略类型
        :type Namespace: str
        """
        self.EventName = None
        self.Description = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        self.Description = params.get("Description")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmHistory(AbstractModel):
    """告警历史数据

    """

    def __init__(self):
        """
        :param AlarmId: 告警历史Id
        :type AlarmId: str
        :param MonitorType: 监控类型
        :type MonitorType: str
        :param Namespace: 策略类型
        :type Namespace: str
        :param AlarmObject: 告警对象
        :type AlarmObject: str
        :param Content: 告警内容
        :type Content: str
        :param FirstOccurTime: 时间戳，首次出现时间
        :type FirstOccurTime: int
        :param LastOccurTime: 时间戳，最后出现时间
        :type LastOccurTime: int
        :param AlarmStatus: 告警状态，ALARM=未恢复 OK=已恢复 NO_CONF=已失效 NO_DATA=数据不足
        :type AlarmStatus: str
        :param PolicyId: 告警策略 Id
        :type PolicyId: str
        :param PolicyName: 策略名称
        :type PolicyName: str
        :param VPC: 基础产品告警的告警对象所属网络
        :type VPC: str
        :param ProjectId: 项目 Id
        :type ProjectId: int
        :param ProjectName: 项目名字
        :type ProjectName: str
        :param InstanceGroup: 告警对象所属实例组
        :type InstanceGroup: list of InstanceGroups
        :param ReceiverUids: 接收人列表
        :type ReceiverUids: list of int
        :param ReceiverGroups: 接收组列表
        :type ReceiverGroups: list of int
        :param NoticeWays: 告警渠道列表 SMS=短信 EMAIL=邮件 CALL=电话 WECHAT=微信
        :type NoticeWays: list of str
        :param OriginId: 可用于实例、实例组的绑定和解绑接口（[BindingPolicyObject](https://cloud.tencent.com/document/product/248/40421)、[UnBindingAllPolicyObject](https://cloud.tencent.com/document/product/248/40568)、[UnBindingPolicyObject](https://cloud.tencent.com/document/product/248/40567)）的策略 ID
        :type OriginId: str
        :param AlarmType: 告警类型
        :type AlarmType: str
        :param EventId: 事件Id
        :type EventId: int
        :param Region: 地域
        :type Region: str
        :param PolicyExists: 策略是否存在 0=不存在 1=存在
        :type PolicyExists: int
        :param MetricsInfo: 指标信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricsInfo: list of AlarmHistoryMetric
        """
        self.AlarmId = None
        self.MonitorType = None
        self.Namespace = None
        self.AlarmObject = None
        self.Content = None
        self.FirstOccurTime = None
        self.LastOccurTime = None
        self.AlarmStatus = None
        self.PolicyId = None
        self.PolicyName = None
        self.VPC = None
        self.ProjectId = None
        self.ProjectName = None
        self.InstanceGroup = None
        self.ReceiverUids = None
        self.ReceiverGroups = None
        self.NoticeWays = None
        self.OriginId = None
        self.AlarmType = None
        self.EventId = None
        self.Region = None
        self.PolicyExists = None
        self.MetricsInfo = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.MonitorType = params.get("MonitorType")
        self.Namespace = params.get("Namespace")
        self.AlarmObject = params.get("AlarmObject")
        self.Content = params.get("Content")
        self.FirstOccurTime = params.get("FirstOccurTime")
        self.LastOccurTime = params.get("LastOccurTime")
        self.AlarmStatus = params.get("AlarmStatus")
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.VPC = params.get("VPC")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroups()
                obj._deserialize(item)
                self.InstanceGroup.append(obj)
        self.ReceiverUids = params.get("ReceiverUids")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.NoticeWays = params.get("NoticeWays")
        self.OriginId = params.get("OriginId")
        self.AlarmType = params.get("AlarmType")
        self.EventId = params.get("EventId")
        self.Region = params.get("Region")
        self.PolicyExists = params.get("PolicyExists")
        if params.get("MetricsInfo") is not None:
            self.MetricsInfo = []
            for item in params.get("MetricsInfo"):
                obj = AlarmHistoryMetric()
                obj._deserialize(item)
                self.MetricsInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmHistoryMetric(AbstractModel):
    """告警历史的指标信息

    """

    def __init__(self):
        """
        :param QceNamespace: 云产品监控类型查询数据使用的命名空间
        :type QceNamespace: str
        :param MetricName: 指标名
        :type MetricName: str
        :param Period: 统计周期
        :type Period: int
        :param Value: 触发告警的数值
        :type Value: str
        :param Description: 指标的展示名
        :type Description: str
        """
        self.QceNamespace = None
        self.MetricName = None
        self.Period = None
        self.Value = None
        self.Description = None


    def _deserialize(self, params):
        self.QceNamespace = params.get("QceNamespace")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.Value = params.get("Value")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmNotice(AbstractModel):
    """告警通知模板详情

    """

    def __init__(self):
        """
        :param Id: 告警通知模板 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Name: 告警通知模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param UpdatedAt: 上次修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param UpdatedBy: 上次修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedBy: str
        :param NoticeType: 告警通知类型 ALARM=未恢复通知 OK=已恢复通知 ALL=全部通知
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeType: str
        :param UserNotices: 用户通知列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserNotices: list of UserNotice
        :param URLNotices: 回调通知列表
注意：此字段可能返回 null，表示取不到有效值。
        :type URLNotices: list of URLNotice
        :param IsPreset: 是否是系统预设通知模板 0=否 1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPreset: int
        :param NoticeLanguage: 通知语言 zh-CN=中文 en-US=英文
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeLanguage: str
        :param PolicyIds: 告警通知模板绑定的告警策略ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyIds: list of str
        """
        self.Id = None
        self.Name = None
        self.UpdatedAt = None
        self.UpdatedBy = None
        self.NoticeType = None
        self.UserNotices = None
        self.URLNotices = None
        self.IsPreset = None
        self.NoticeLanguage = None
        self.PolicyIds = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.UpdatedAt = params.get("UpdatedAt")
        self.UpdatedBy = params.get("UpdatedBy")
        self.NoticeType = params.get("NoticeType")
        if params.get("UserNotices") is not None:
            self.UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self.UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self.URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self.URLNotices.append(obj)
        self.IsPreset = params.get("IsPreset")
        self.NoticeLanguage = params.get("NoticeLanguage")
        self.PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmPolicy(AbstractModel):
    """告警策略详情

    """

    def __init__(self):
        """
        :param PolicyId: 告警策略 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: str
        :param PolicyName: 告警策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param MonitorType: 监控类型 MT_QCE=云产品监控
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorType: str
        :param Enable: 启停状态 0=停用 1=启用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param UseSum: 策略组绑定的实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type UseSum: int
        :param ProjectId: 项目 Id -1=无项目 0=默认项目
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param ProjectName: 项目名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param Namespace: 告警策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param ConditionTemplateId: 触发条件模板 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionTemplateId: str
        :param Condition: 指标触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param EventCondition: 事件触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param NoticeIds: 通知规则 id 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeIds: list of str
        :param Notices: 通知规则 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Notices: list of AlarmNotice
        :param TriggerTasks: 触发任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param ConditionsTemp: 模板策略组
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.ConditionsTemp`
        :param LastEditUin: 最后编辑的用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type LastEditUin: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param InsertTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: int
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: list of str
        :param NamespaceShowName: namespace显示名字
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceShowName: str
        :param IsDefault: 是否默认策略，1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: int
        :param CanSetDefault: 能否设置默认策略，1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type CanSetDefault: int
        :param InstanceGroupId: 实例分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupId: int
        :param InstanceSum: 实例分组总实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSum: int
        :param InstanceGroupName: 实例分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupName: str
        :param RuleType: 触发条件类型 STATIC=静态阈值 DYNAMIC=动态类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param OriginId: 用于实例、实例组绑定和解绑接口（BindingPolicyObject、UnBindingAllPolicyObject、UnBindingPolicyObject）的策略 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginId: str
        :param TagInstances: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInstances: list of TagInstance
        """
        self.PolicyId = None
        self.PolicyName = None
        self.Remark = None
        self.MonitorType = None
        self.Enable = None
        self.UseSum = None
        self.ProjectId = None
        self.ProjectName = None
        self.Namespace = None
        self.ConditionTemplateId = None
        self.Condition = None
        self.EventCondition = None
        self.NoticeIds = None
        self.Notices = None
        self.TriggerTasks = None
        self.ConditionsTemp = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.InsertTime = None
        self.Region = None
        self.NamespaceShowName = None
        self.IsDefault = None
        self.CanSetDefault = None
        self.InstanceGroupId = None
        self.InstanceSum = None
        self.InstanceGroupName = None
        self.RuleType = None
        self.OriginId = None
        self.TagInstances = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Remark = params.get("Remark")
        self.MonitorType = params.get("MonitorType")
        self.Enable = params.get("Enable")
        self.UseSum = params.get("UseSum")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.Namespace = params.get("Namespace")
        self.ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self.Condition = AlarmPolicyCondition()
            self.Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self.EventCondition = AlarmPolicyEventCondition()
            self.EventCondition._deserialize(params.get("EventCondition"))
        self.NoticeIds = params.get("NoticeIds")
        if params.get("Notices") is not None:
            self.Notices = []
            for item in params.get("Notices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self.Notices.append(obj)
        if params.get("TriggerTasks") is not None:
            self.TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self.TriggerTasks.append(obj)
        if params.get("ConditionsTemp") is not None:
            self.ConditionsTemp = ConditionsTemp()
            self.ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.Region = params.get("Region")
        self.NamespaceShowName = params.get("NamespaceShowName")
        self.IsDefault = params.get("IsDefault")
        self.CanSetDefault = params.get("CanSetDefault")
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.InstanceSum = params.get("InstanceSum")
        self.InstanceGroupName = params.get("InstanceGroupName")
        self.RuleType = params.get("RuleType")
        self.OriginId = params.get("OriginId")
        if params.get("TagInstances") is not None:
            self.TagInstances = []
            for item in params.get("TagInstances"):
                obj = TagInstance()
                obj._deserialize(item)
                self.TagInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmPolicyCondition(AbstractModel):
    """告警策略指标触发条件

    """

    def __init__(self):
        """
        :param IsUnionRule: 指标触发与或条件，0=或，1=与
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        :param Rules: 告警触发条件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of AlarmPolicyRule
        """
        self.IsUnionRule = None
        self.Rules = None


    def _deserialize(self, params):
        self.IsUnionRule = params.get("IsUnionRule")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = AlarmPolicyRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmPolicyEventCondition(AbstractModel):
    """告警策略事件触发条件

    """

    def __init__(self):
        """
        :param Rules: 告警触发条件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of AlarmPolicyRule
        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = AlarmPolicyRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmPolicyFilter(AbstractModel):
    """告警策略过滤条件

    """

    def __init__(self):
        """
        :param Type: 过滤条件类型 DIMENSION=使用 Dimensions 做过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Dimensions: AlarmPolicyDimension 二维数组序列化后的json字符串，一维数组之间互为或关系，一维数组内的元素互为与关系
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: str
        """
        self.Type = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmPolicyRule(AbstractModel):
    """告警策略触发条件

    """

    def __init__(self):
        """
        :param MetricName: 指标名或事件名，支持的指标可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询，支持的事件可以从 [DescribeAlarmEvents](https://cloud.tencent.com/document/product/248/51284) 查询 。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param Period: 秒数 统计周期，支持的值可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询。
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        :param Operator: 英文运算符
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
        :param Value: 阈值，支持的范围可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param ContinuePeriod: 周期数 持续通知周期 1=持续1个周期 2=持续2个周期...，支持的值可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinuePeriod: int
        :param NoticeFrequency: 秒数 告警间隔  0=不重复 300=每5分钟告警一次 600=每10分钟告警一次 900=每15分钟告警一次 1800=每30分钟告警一次 3600=每1小时告警一次 7200=每2小时告警一次 10800=每3小时告警一次 21600=每6小时告警一次 43200=每12小时告警一次 86400=每1天告警一次
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeFrequency: int
        :param IsPowerNotice: 告警频率是否指数增长 0=否 1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPowerNotice: int
        :param Filter: 对于单个触发规则的过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param Description: 指标展示名，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Unit: 单位，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param RuleType: 触发条件类型 STATIC=静态阈值 DYNAMIC=动态阈值。创建或编辑策略时，如不填则默认为 STATIC。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        """
        self.MetricName = None
        self.Period = None
        self.Operator = None
        self.Value = None
        self.ContinuePeriod = None
        self.NoticeFrequency = None
        self.IsPowerNotice = None
        self.Filter = None
        self.Description = None
        self.Unit = None
        self.RuleType = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        self.ContinuePeriod = params.get("ContinuePeriod")
        self.NoticeFrequency = params.get("NoticeFrequency")
        self.IsPowerNotice = params.get("IsPowerNotice")
        if params.get("Filter") is not None:
            self.Filter = AlarmPolicyFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.Description = params.get("Description")
        self.Unit = params.get("Unit")
        self.RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AlarmPolicyTriggerTask(AbstractModel):
    """告警策略触发任务

    """

    def __init__(self):
        """
        :param Type: 触发任务类型 AS=弹性伸缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param TaskConfig: 用 json 表示配置信息 {"Key1":"Value1","Key2":"Value2"}
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskConfig: str
        """
        self.Type = None
        self.TaskConfig = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TaskConfig = params.get("TaskConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BindingPolicyObjectDimension(AbstractModel):
    """策略绑定实例维度信息

    """

    def __init__(self):
        """
        :param Region: 地域名
        :type Region: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param Dimensions: 实例的维度信息，格式为
{"unInstanceId":"ins-00jvv9mo"}。不同云产品的维度信息不同，详见
[指标维度信息Dimensions列表](https://cloud.tencent.com/document/product/248/50397)
        :type Dimensions: str
        :param EventDimensions: 事件维度信息
        :type EventDimensions: str
        """
        self.Region = None
        self.RegionId = None
        self.Dimensions = None
        self.EventDimensions = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.Dimensions = params.get("Dimensions")
        self.EventDimensions = params.get("EventDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BindingPolicyObjectRequest(AbstractModel):
    """BindingPolicyObject请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 策略组id，如传入 PolicyId 则该字段会被忽略可传入任意值如 0
        :type GroupId: int
        :param Module: 必填。固定值"monitor"
        :type Module: str
        :param InstanceGroupId: 实例分组ID
        :type InstanceGroupId: int
        :param Dimensions: 需要绑定的对象维度信息
        :type Dimensions: list of BindingPolicyObjectDimension
        :param PolicyId: 告警策略ID，使用此字段时 GroupId 会被忽略
        :type PolicyId: str
        """
        self.GroupId = None
        self.Module = None
        self.InstanceGroupId = None
        self.Dimensions = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Module = params.get("Module")
        self.InstanceGroupId = params.get("InstanceGroupId")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = BindingPolicyObjectDimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BindingPolicyObjectResponse(AbstractModel):
    """BindingPolicyObject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CommonNamespace(AbstractModel):
    """统一的命名空间信息

    """

    def __init__(self):
        """
        :param Id: 命名空间标示
        :type Id: str
        :param Name: 命名空间名称
        :type Name: str
        :param Value: 命名空间值
        :type Value: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param Config: 配置信息
        :type Config: str
        :param AvailableRegions: 支持地域列表
        :type AvailableRegions: list of str
        :param SortId: 排序Id
        :type SortId: int
        :param DashboardId: Dashboard中的唯一表示
        :type DashboardId: str
        """
        self.Id = None
        self.Name = None
        self.Value = None
        self.ProductName = None
        self.Config = None
        self.AvailableRegions = None
        self.SortId = None
        self.DashboardId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.ProductName = params.get("ProductName")
        self.Config = params.get("Config")
        self.AvailableRegions = params.get("AvailableRegions")
        self.SortId = params.get("SortId")
        self.DashboardId = params.get("DashboardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ConditionsTemp(AbstractModel):
    """告警条件模版

    """

    def __init__(self):
        """
        :param TemplateName: 模版名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param Condition: 指标触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param EventCondition: 事件触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        """
        self.TemplateName = None
        self.Condition = None
        self.EventCondition = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        if params.get("Condition") is not None:
            self.Condition = AlarmPolicyCondition()
            self.Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self.EventCondition = AlarmPolicyEventCondition()
            self.EventCondition._deserialize(params.get("EventCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAlarmNoticeRequest(AbstractModel):
    """CreateAlarmNotice请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        :param Name: 通知模板名称 60字符以内
        :type Name: str
        :param NoticeType: 通知类型 ALARM=未恢复通知 OK=已恢复通知 ALL=都通知
        :type NoticeType: str
        :param NoticeLanguage: 通知语言 zh-CN=中文 en-US=英文
        :type NoticeLanguage: str
        :param UserNotices: 用户通知 最多5个
        :type UserNotices: list of UserNotice
        :param URLNotices: 回调通知 最多3个
        :type URLNotices: list of URLNotice
        """
        self.Module = None
        self.Name = None
        self.NoticeType = None
        self.NoticeLanguage = None
        self.UserNotices = None
        self.URLNotices = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Name = params.get("Name")
        self.NoticeType = params.get("NoticeType")
        self.NoticeLanguage = params.get("NoticeLanguage")
        if params.get("UserNotices") is not None:
            self.UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self.UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self.URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self.URLNotices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAlarmNoticeResponse(AbstractModel):
    """CreateAlarmNotice返回参数结构体

    """

    def __init__(self):
        """
        :param NoticeId: 告警通知模板ID
        :type NoticeId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NoticeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NoticeId = params.get("NoticeId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAlarmPolicyRequest(AbstractModel):
    """CreateAlarmPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param PolicyName: 策略名称，不超过20字符
        :type PolicyName: str
        :param MonitorType: 监控类型 MT_QCE=云产品监控
        :type MonitorType: str
        :param Namespace: 告警策略类型，由 [DescribeAllNamespaces](https://cloud.tencent.com/document/product/248/48683) 获得，例如 cvm_device
        :type Namespace: str
        :param Remark: 备注，不超过100字符，仅支持中英文、数字、下划线、-
        :type Remark: str
        :param Enable: 是否启用 0=停用 1=启用，可不传 默认为1
        :type Enable: int
        :param ProjectId: 项目 Id，对于区分项目的产品必须传入非 -1 的值。 -1=无项目 0=默认项目，如不传 默认为 -1。支持的项目 Id 可以在控制台 [账号中心-项目管理](https://console.cloud.tencent.com/project) 中查看。
        :type ProjectId: int
        :param ConditionTemplateId: 触发条件模板 Id ，可不传
        :type ConditionTemplateId: int
        :param Condition: 指标触发条件，支持的指标可以从 [DescribeAlarmMetrics](https://cloud.tencent.com/document/product/248/51283) 查询。
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param EventCondition: 事件触发条件，支持的事件可以从 [DescribeAlarmEvents](https://cloud.tencent.com/document/product/248/51284) 查询。
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param NoticeIds: 通知规则 Id 列表，由 [DescribeAlarmNotices](https://cloud.tencent.com/document/product/248/51280) 获得
        :type NoticeIds: list of str
        :param TriggerTasks: 触发任务列表
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        """
        self.Module = None
        self.PolicyName = None
        self.MonitorType = None
        self.Namespace = None
        self.Remark = None
        self.Enable = None
        self.ProjectId = None
        self.ConditionTemplateId = None
        self.Condition = None
        self.EventCondition = None
        self.NoticeIds = None
        self.TriggerTasks = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyName = params.get("PolicyName")
        self.MonitorType = params.get("MonitorType")
        self.Namespace = params.get("Namespace")
        self.Remark = params.get("Remark")
        self.Enable = params.get("Enable")
        self.ProjectId = params.get("ProjectId")
        self.ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self.Condition = AlarmPolicyCondition()
            self.Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self.EventCondition = AlarmPolicyEventCondition()
            self.EventCondition._deserialize(params.get("EventCondition"))
        self.NoticeIds = params.get("NoticeIds")
        if params.get("TriggerTasks") is not None:
            self.TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self.TriggerTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAlarmPolicyResponse(AbstractModel):
    """CreateAlarmPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param PolicyId: 告警策略 ID
        :type PolicyId: str
        :param OriginId: 可用于实例、实例组的绑定和解绑接口（[BindingPolicyObject](https://cloud.tencent.com/document/product/248/40421)、[UnBindingAllPolicyObject](https://cloud.tencent.com/document/product/248/40568)、[UnBindingPolicyObject](https://cloud.tencent.com/document/product/248/40567)）的策略 ID
        :type OriginId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAlertRuleRequest(AbstractModel):
    """CreateAlertRule请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param RuleName: 规则名称
        :type RuleName: str
        :param Expr: 规则表达式
        :type Expr: str
        :param Receivers: 告警通知模板 ID 列表
        :type Receivers: list of str
        :param RuleState: 规则状态码，取值如下：
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param Duration: 规则报警持续时间
        :type Duration: str
        :param Labels: 标签列表
        :type Labels: list of PrometheusRuleKV
        :param Annotations: 注释列表
        :type Annotations: list of PrometheusRuleKV
        :param Type: 报警策略模板分类
        :type Type: str
        """
        self.InstanceId = None
        self.RuleName = None
        self.Expr = None
        self.Receivers = None
        self.RuleState = None
        self.Duration = None
        self.Labels = None
        self.Annotations = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RuleName = params.get("RuleName")
        self.Expr = params.get("Expr")
        self.Receivers = params.get("Receivers")
        self.RuleState = params.get("RuleState")
        self.Duration = params.get("Duration")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Annotations.append(obj)
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAlertRuleResponse(AbstractModel):
    """CreateAlertRule返回参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePolicyGroupCondition(AbstractModel):
    """创建策略传入的阈值告警条件

    """

    def __init__(self):
        """
        :param MetricId: 指标Id
        :type MetricId: int
        :param AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param CalcType: 比较类型，1表示大于，2表示大于等于，3表示小于，4表示小于等于，5表示相等，6表示不相等。如果指标有配置默认比较类型值可以不填。
        :type CalcType: int
        :param CalcValue: 比较的值，如果指标不必须CalcValue可不填
        :type CalcValue: float
        :param CalcPeriod: 数据聚合周期(单位秒)，若指标有默认值可不填
        :type CalcPeriod: int
        :param ContinuePeriod: 持续几个检测周期触发规则会告警
        :type ContinuePeriod: int
        :param RuleId: 如果通过模版创建，需要传入模版中该指标的对应RuleId
        :type RuleId: int
        """
        self.MetricId = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.CalcType = None
        self.CalcValue = None
        self.CalcPeriod = None
        self.ContinuePeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.MetricId = params.get("MetricId")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.CalcPeriod = params.get("CalcPeriod")
        self.ContinuePeriod = params.get("ContinuePeriod")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePolicyGroupEventCondition(AbstractModel):
    """创建策略传入的事件告警条件

    """

    def __init__(self):
        """
        :param EventId: 告警事件的Id
        :type EventId: int
        :param AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param RuleId: 如果通过模版创建，需要传入模版中该指标的对应RuleId
        :type RuleId: int
        """
        self.EventId = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePolicyGroupRequest(AbstractModel):
    """CreatePolicyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 组策略名称
        :type GroupName: str
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param ViewName: 策略组所属视图的名称，若通过模版创建，可不传入
        :type ViewName: str
        :param ProjectId: 策略组所属项目Id，会进行鉴权操作
        :type ProjectId: int
        :param ConditionTempGroupId: 模版策略组Id, 通过模版创建时才需要传
        :type ConditionTempGroupId: int
        :param IsShielded: 是否屏蔽策略组，0表示不屏蔽，1表示屏蔽。不填默认为0
        :type IsShielded: int
        :param Remark: 策略组的备注信息
        :type Remark: str
        :param InsertTime: 插入时间，戳格式为Unix时间戳，不填则按后台处理时间填充
        :type InsertTime: int
        :param Conditions: 策略组中的阈值告警规则
        :type Conditions: list of CreatePolicyGroupCondition
        :param EventConditions: 策略组中的事件告警规则
        :type EventConditions: list of CreatePolicyGroupEventCondition
        :param BackEndCall: 是否为后端调用。当且仅当值为1时，后台拉取策略模版中的规则填充入Conditions以及EventConditions字段
        :type BackEndCall: int
        :param IsUnionRule: 指标告警规则的且或关系，0表示或规则(满足任意规则就告警)，1表示且规则(满足所有规则才告警)
        :type IsUnionRule: int
        """
        self.GroupName = None
        self.Module = None
        self.ViewName = None
        self.ProjectId = None
        self.ConditionTempGroupId = None
        self.IsShielded = None
        self.Remark = None
        self.InsertTime = None
        self.Conditions = None
        self.EventConditions = None
        self.BackEndCall = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.Module = params.get("Module")
        self.ViewName = params.get("ViewName")
        self.ProjectId = params.get("ProjectId")
        self.ConditionTempGroupId = params.get("ConditionTempGroupId")
        self.IsShielded = params.get("IsShielded")
        self.Remark = params.get("Remark")
        self.InsertTime = params.get("InsertTime")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = CreatePolicyGroupCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = CreatePolicyGroupEventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        self.BackEndCall = params.get("BackEndCall")
        self.IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePolicyGroupResponse(AbstractModel):
    """CreatePolicyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 创建成功的策略组Id
        :type GroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateServiceDiscoveryRequest(AbstractModel):
    """CreateServiceDiscovery请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param KubeClusterId: <li>类型为TKE：对应集成的腾讯云容器服务集群 ID</li>
        :type KubeClusterId: str
        :param KubeType: 用户 Kubernetes 集群类型：
<li> 1 = 容器服务集群(TKE) </li>
        :type KubeType: int
        :param Type: 服务发现类型，取值如下：
<li> 1 = ServiceMonitor</li>
<li> 2 = PodMonitor</li>
<li> 3 = JobMonitor</li>
        :type Type: int
        :param Yaml: 服务发现配置信息
        :type Yaml: str
        """
        self.InstanceId = None
        self.KubeClusterId = None
        self.KubeType = None
        self.Type = None
        self.Yaml = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeClusterId = params.get("KubeClusterId")
        self.KubeType = params.get("KubeType")
        self.Type = params.get("Type")
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateServiceDiscoveryResponse(AbstractModel):
    """CreateServiceDiscovery返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceDiscovery: 创建成功之后，返回对应服务发现信息
        :type ServiceDiscovery: :class:`tencentcloud.monitor.v20180724.models.ServiceDiscoveryItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceDiscovery = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceDiscovery") is not None:
            self.ServiceDiscovery = ServiceDiscoveryItem()
            self.ServiceDiscovery._deserialize(params.get("ServiceDiscovery"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DataPoint(AbstractModel):
    """监控数据点

    """

    def __init__(self):
        """
        :param Dimensions: 实例对象维度组合
        :type Dimensions: list of Dimension
        :param Timestamps: 时间戳数组，表示那些时间点有数据，缺失的时间戳，没有数据点，可以理解为掉点了
        :type Timestamps: list of float
        :param Values: 监控值数组，该数组和Timestamps一一对应
        :type Values: list of float
        """
        self.Dimensions = None
        self.Timestamps = None
        self.Values = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.Timestamps = params.get("Timestamps")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAlarmNoticesRequest(AbstractModel):
    """DeleteAlarmNotices请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        :param NoticeIds: 告警通知模板id列表
        :type NoticeIds: list of str
        """
        self.Module = None
        self.NoticeIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.NoticeIds = params.get("NoticeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAlarmNoticesResponse(AbstractModel):
    """DeleteAlarmNotices返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAlarmPolicyRequest(AbstractModel):
    """DeleteAlarmPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定值 monitor
        :type Module: str
        :param PolicyIds: 告警策略 ID 列表
        :type PolicyIds: list of str
        """
        self.Module = None
        self.PolicyIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAlarmPolicyResponse(AbstractModel):
    """DeleteAlarmPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAlertRulesRequest(AbstractModel):
    """DeleteAlertRules请求参数结构体

    """

    def __init__(self):
        """
        :param RuleIds: 规则 ID 列表
        :type RuleIds: list of str
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        """
        self.RuleIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.RuleIds = params.get("RuleIds")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAlertRulesResponse(AbstractModel):
    """DeleteAlertRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePolicyGroupRequest(AbstractModel):
    """DeletePolicyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param GroupId: 策略组id
        :type GroupId: list of int
        """
        self.Module = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePolicyGroupResponse(AbstractModel):
    """DeletePolicyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteServiceDiscoveryRequest(AbstractModel):
    """DeleteServiceDiscovery请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param KubeClusterId: <li>类型是 TKE，为对应的腾讯云容器服务集群 ID</li>
        :type KubeClusterId: str
        :param KubeType: 用户 Kubernetes 集群类型：
<li> 1 = 容器服务集群(TKE) </li>
        :type KubeType: int
        :param Type: 服务发现类型，取值如下：
<li> 1 = ServiceMonitor</li>
<li> 2 = PodMonitor</li>
<li> 3 = PodMonitor</li>
        :type Type: int
        :param Yaml: 服务发现配置信息
        :type Yaml: str
        """
        self.InstanceId = None
        self.KubeClusterId = None
        self.KubeType = None
        self.Type = None
        self.Yaml = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeClusterId = params.get("KubeClusterId")
        self.KubeType = params.get("KubeType")
        self.Type = params.get("Type")
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteServiceDiscoveryResponse(AbstractModel):
    """DeleteServiceDiscovery返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccidentEventListAlarms(AbstractModel):
    """DescribeAccidentEventList接口的出参类型

    """

    def __init__(self):
        """
        :param BusinessTypeDesc: 事件分类
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessTypeDesc: str
        :param AccidentTypeDesc: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AccidentTypeDesc: str
        :param BusinessID: 事件分类的ID，1表示服务问题，2表示其他订阅
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessID: int
        :param EventStatus: 事件状态的ID，0表示已恢复，1表示未恢复
注意：此字段可能返回 null，表示取不到有效值。
        :type EventStatus: int
        :param AffectResource: 影响的对象
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectResource: str
        :param Region: 事件的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param OccurTime: 事件发生的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OccurTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.BusinessTypeDesc = None
        self.AccidentTypeDesc = None
        self.BusinessID = None
        self.EventStatus = None
        self.AffectResource = None
        self.Region = None
        self.OccurTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.BusinessTypeDesc = params.get("BusinessTypeDesc")
        self.AccidentTypeDesc = params.get("AccidentTypeDesc")
        self.BusinessID = params.get("BusinessID")
        self.EventStatus = params.get("EventStatus")
        self.AffectResource = params.get("AffectResource")
        self.Region = params.get("Region")
        self.OccurTime = params.get("OccurTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccidentEventListRequest(AbstractModel):
    """DescribeAccidentEventList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 接口模块名，当前接口取值monitor
        :type Module: str
        :param StartTime: 起始时间，默认一天前的时间戳
        :type StartTime: int
        :param EndTime: 结束时间，默认当前时间戳
        :type EndTime: int
        :param Limit: 分页参数，每页返回的数量，取值1~100，默认20
        :type Limit: int
        :param Offset: 分页参数，页偏移量，从0开始计数，默认0
        :type Offset: int
        :param UpdateTimeOrder: 根据UpdateTime排序的规则，取值asc或desc
        :type UpdateTimeOrder: str
        :param OccurTimeOrder: 根据OccurTime排序的规则，取值asc或desc（优先根据UpdateTimeOrder排序）
        :type OccurTimeOrder: str
        :param AccidentType: 根据事件类型过滤，1表示服务问题，2表示其他订阅
        :type AccidentType: list of int
        :param AccidentEvent: 根据事件过滤，1表示云服务器存储问题，2表示云服务器网络连接问题，3表示云服务器运行异常，202表示运营商网络抖动
        :type AccidentEvent: list of int
        :param AccidentStatus: 根据事件状态过滤，0表示已恢复，1表示未恢复
        :type AccidentStatus: list of int
        :param AccidentRegion: 根据事件地域过滤，gz表示广州，sh表示上海等
        :type AccidentRegion: list of str
        :param AffectResource: 根据影响资源过滤，比如ins-19a06bka
        :type AffectResource: str
        """
        self.Module = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.UpdateTimeOrder = None
        self.OccurTimeOrder = None
        self.AccidentType = None
        self.AccidentEvent = None
        self.AccidentStatus = None
        self.AccidentRegion = None
        self.AffectResource = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.UpdateTimeOrder = params.get("UpdateTimeOrder")
        self.OccurTimeOrder = params.get("OccurTimeOrder")
        self.AccidentType = params.get("AccidentType")
        self.AccidentEvent = params.get("AccidentEvent")
        self.AccidentStatus = params.get("AccidentStatus")
        self.AccidentRegion = params.get("AccidentRegion")
        self.AffectResource = params.get("AffectResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccidentEventListResponse(AbstractModel):
    """DescribeAccidentEventList返回参数结构体

    """

    def __init__(self):
        """
        :param Alarms: 平台事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Alarms: list of DescribeAccidentEventListAlarms
        :param Total: 平台事件的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Alarms = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeAccidentEventListAlarms()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmEventsRequest(AbstractModel):
    """DescribeAlarmEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定值 monitor
        :type Module: str
        :param Namespace: 告警策略类型，由 DescribeAllNamespaces 获得，例如 cvm_device
        :type Namespace: str
        """
        self.Module = None
        self.Namespace = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmEventsResponse(AbstractModel):
    """DescribeAlarmEvents返回参数结构体

    """

    def __init__(self):
        """
        :param Events: 告警事件列表
        :type Events: list of AlarmEvent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = AlarmEvent()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmHistoriesRequest(AbstractModel):
    """DescribeAlarmHistories请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param PageNumber: 页数，从 1 开始计数，默认 1
        :type PageNumber: int
        :param PageSize: 每页的数量，取值1~100，默认20
        :type PageSize: int
        :param Order: 默认按首次出现时间倒序排列 "ASC"=正序 "DESC"=逆序
        :type Order: str
        :param StartTime: 起始时间，默认一天前的时间戳。对应 `FirstOccurTime` 告警首次出现时间，告警历史的 `FirstOccurTime` 晚于 `StartTime` 才可能被搜索到。
        :type StartTime: int
        :param EndTime: 结束时间，默认当前时间戳。对应 `FirstOccurTime` 告警首次出现时间，告警历史的 `FirstOccurTime` 早于 `EndTime` 才可能被搜索到。
        :type EndTime: int
        :param MonitorTypes: 根据监控类型过滤 不选默认查所有类型 "MT_QCE"=云产品监控
        :type MonitorTypes: list of str
        :param AlarmObject: 根据告警对象过滤 字符串模糊搜索
        :type AlarmObject: str
        :param AlarmStatus: 根据告警状态过滤 ALARM=未恢复 OK=已恢复 NO_CONF=已失效 NO_DATA=数据不足，不选默认查所有
        :type AlarmStatus: list of str
        :param ProjectIds: 根据项目ID过滤，-1=无项目 0=默认项目
可在此页面查询 [项目管理](https://console.cloud.tencent.com/project)
        :type ProjectIds: list of int
        :param InstanceGroupIds: 根据实例组ID过滤
        :type InstanceGroupIds: list of int
        :param Namespaces: 根据策略类型过滤，策略类型是监控类型之下的概念，在这里两者都需要传入，例如 `[{"MonitorType": "MT_QCE", "Namespace": "cvm_device"}]`
可使用 [查询所有名字空间 DescribeAllNamespaces](https://cloud.tencent.com/document/product/248/48683) 接口查询
        :type Namespaces: list of MonitorTypeNamespace
        :param MetricNames: 根据指标名过滤
        :type MetricNames: list of str
        :param PolicyName: 根据策略名称模糊搜索
        :type PolicyName: str
        :param Content: 根据告警内容模糊搜索
        :type Content: str
        :param ReceiverUids: 根据接收人搜索，可以使用“访问管理”的 [拉取子用户 ListUsers](https://cloud.tencent.com/document/product/598/34587) 接口获取用户列表 或 [查询子用户 GetUser](https://cloud.tencent.com/document/product/598/34590) 接口查询子用户详情，此处填入返回结果中的 `Uid` 字段
        :type ReceiverUids: list of int
        :param ReceiverGroups: 根据接收组搜索，可以使用“访问管理”的 [查询用户组列表 ListGroups](https://cloud.tencent.com/document/product/598/34589) 接口获取用户组列表 或 [列出用户关联的用户组 ListGroupsForUser](https://cloud.tencent.com/document/product/598/34588) 查询某个子用户所在的用户组列表 ，此处填入返回结果中的 `GroupId ` 字段
        :type ReceiverGroups: list of int
        :param PolicyIds: 根据告警策略 Id 列表搜索
        :type PolicyIds: list of str
        """
        self.Module = None
        self.PageNumber = None
        self.PageSize = None
        self.Order = None
        self.StartTime = None
        self.EndTime = None
        self.MonitorTypes = None
        self.AlarmObject = None
        self.AlarmStatus = None
        self.ProjectIds = None
        self.InstanceGroupIds = None
        self.Namespaces = None
        self.MetricNames = None
        self.PolicyName = None
        self.Content = None
        self.ReceiverUids = None
        self.ReceiverGroups = None
        self.PolicyIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.Order = params.get("Order")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MonitorTypes = params.get("MonitorTypes")
        self.AlarmObject = params.get("AlarmObject")
        self.AlarmStatus = params.get("AlarmStatus")
        self.ProjectIds = params.get("ProjectIds")
        self.InstanceGroupIds = params.get("InstanceGroupIds")
        if params.get("Namespaces") is not None:
            self.Namespaces = []
            for item in params.get("Namespaces"):
                obj = MonitorTypeNamespace()
                obj._deserialize(item)
                self.Namespaces.append(obj)
        self.MetricNames = params.get("MetricNames")
        self.PolicyName = params.get("PolicyName")
        self.Content = params.get("Content")
        self.ReceiverUids = params.get("ReceiverUids")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmHistoriesResponse(AbstractModel):
    """DescribeAlarmHistories返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param Histories: 告警历史列表
        :type Histories: list of AlarmHistory
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Histories = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Histories") is not None:
            self.Histories = []
            for item in params.get("Histories"):
                obj = AlarmHistory()
                obj._deserialize(item)
                self.Histories.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmMetricsRequest(AbstractModel):
    """DescribeAlarmMetrics请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param MonitorType: 监控类型过滤 "MT_QCE"=云产品监控
        :type MonitorType: str
        :param Namespace: 告警策略类型，由 DescribeAllNamespaces 获得，例如 cvm_device
        :type Namespace: str
        """
        self.Module = None
        self.MonitorType = None
        self.Namespace = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.MonitorType = params.get("MonitorType")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmMetricsResponse(AbstractModel):
    """DescribeAlarmMetrics返回参数结构体

    """

    def __init__(self):
        """
        :param Metrics: 告警指标列表
        :type Metrics: list of Metric
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Metrics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = Metric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmNoticeCallbacksRequest(AbstractModel):
    """DescribeAlarmNoticeCallbacks请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        """
        self.Module = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmNoticeCallbacksResponse(AbstractModel):
    """DescribeAlarmNoticeCallbacks返回参数结构体

    """

    def __init__(self):
        """
        :param URLNotices: 告警回调通知
注意：此字段可能返回 null，表示取不到有效值。
        :type URLNotices: list of URLNotice
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.URLNotices = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("URLNotices") is not None:
            self.URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self.URLNotices.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmNoticeRequest(AbstractModel):
    """DescribeAlarmNotice请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        :param NoticeId: 告警通知模板 id
        :type NoticeId: str
        """
        self.Module = None
        self.NoticeId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.NoticeId = params.get("NoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmNoticeResponse(AbstractModel):
    """DescribeAlarmNotice返回参数结构体

    """

    def __init__(self):
        """
        :param Notice: 告警通知模板详细信息
        :type Notice: :class:`tencentcloud.monitor.v20180724.models.AlarmNotice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Notice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Notice") is not None:
            self.Notice = AlarmNotice()
            self.Notice._deserialize(params.get("Notice"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        :param PageNumber: 页码 最小为1
        :type PageNumber: int
        :param PageSize: 分页大小 1～200
        :type PageSize: int
        :param Order: 按更新时间排序方式 ASC=正序 DESC=倒序
        :type Order: str
        :param OwnerUid: 主账号 uid 用于创建预设通知
        :type OwnerUid: int
        :param Name: 告警通知模板名称 用来模糊搜索
        :type Name: str
        :param ReceiverType: 根据接收人过滤告警通知模板需要选定通知用户类型 USER=用户 GROUP=用户组 传空=不按接收人过滤
        :type ReceiverType: str
        :param UserIds: 接收对象列表
        :type UserIds: list of int
        :param GroupIds: 接收组列表
        :type GroupIds: list of int
        """
        self.Module = None
        self.PageNumber = None
        self.PageSize = None
        self.Order = None
        self.OwnerUid = None
        self.Name = None
        self.ReceiverType = None
        self.UserIds = None
        self.GroupIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.Order = params.get("Order")
        self.OwnerUid = params.get("OwnerUid")
        self.Name = params.get("Name")
        self.ReceiverType = params.get("ReceiverType")
        self.UserIds = params.get("UserIds")
        self.GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 告警通知模板总数
        :type TotalCount: int
        :param Notices: 告警通知模板列表
        :type Notices: list of AlarmNotice
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Notices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Notices") is not None:
            self.Notices = []
            for item in params.get("Notices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self.Notices.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmPoliciesRequest(AbstractModel):
    """DescribeAlarmPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param PageNumber: 页数，从 1 开始计数，默认 1
        :type PageNumber: int
        :param PageSize: 每页的数量，取值1~100，默认20
        :type PageSize: int
        :param PolicyName: 按策略名称模糊搜索
        :type PolicyName: str
        :param MonitorTypes: 根据监控类型过滤 不选默认查所有类型 "MT_QCE"=云产品监控
        :type MonitorTypes: list of str
        :param Namespaces: 根据命名空间过滤，不同策略类型的值详见
[策略类型列表](https://cloud.tencent.com/document/product/248/50397)
        :type Namespaces: list of str
        :param Dimensions: 告警对象列表，JSON 字符串。外层数组，对应多个实例，内层为对象的维度。例如“云服务器-基础监控”可写为：
`[ {"Dimensions": {"unInstanceId": "ins-qr8d555g"}}, {"Dimensions": {"unInstanceId": "ins-qr8d555h"}} ]`
具体也可以参考下方的示例 2。

不同云产品参数示例详见 [维度信息Dimensions列表](https://cloud.tencent.com/document/product/248/50397)
        :type Dimensions: str
        :param ReceiverUids: 根据接收人搜索，可以使用“访问管理”的 [拉取子用户 ListUsers](https://cloud.tencent.com/document/product/598/34587) 接口获取用户列表 或 [查询子用户 GetUser](https://cloud.tencent.com/document/product/598/34590) 接口查询子用户详情，此处填入返回结果中的 `Uid` 字段
        :type ReceiverUids: list of int
        :param ReceiverGroups: 根据接收组搜索，可以使用“访问管理”的 [查询用户组列表 ListGroups](https://cloud.tencent.com/document/product/598/34589) 接口获取用户组列表 或 [列出用户关联的用户组 ListGroupsForUser](https://cloud.tencent.com/document/product/598/34588) 查询某个子用户所在的用户组列表 ，此处填入返回结果中的 `GroupId ` 字段
        :type ReceiverGroups: list of int
        :param PolicyType: 根据默认策略筛选 不传展示全部策略 DEFAULT=展示默认策略 NOT_DEFAULT=展示非默认策略
        :type PolicyType: list of str
        :param Field: 排序字段，例如按照最后修改时间排序，Field: "UpdateTime"
        :type Field: str
        :param Order: 排序顺序：升序：ASC  降序：DESC
        :type Order: str
        :param ProjectIds: 策略所属项目的id数组，可在此页面查看
[项目管理](https://console.cloud.tencent.com/project)
        :type ProjectIds: list of int
        :param NoticeIds: 通知模版的id列表，可查询通知模版列表获取。
可使用 [查询通知模板列表](https://cloud.tencent.com/document/product/248/51280) 接口查询。
        :type NoticeIds: list of str
        :param RuleTypes: 根据触发条件筛选 不传展示全部策略 STATIC=展示静态阈值策略 DYNAMIC=展示动态阈值策略
        :type RuleTypes: list of str
        :param Enable: 告警启停筛选，[1]：启用   [0]：停止，全部[0, 1]
        :type Enable: list of int
        :param NotBindingNoticeRule: 传 1 查询未配置通知规则的告警策略；不传或传其他数值，查询所有策略。
        :type NotBindingNoticeRule: int
        """
        self.Module = None
        self.PageNumber = None
        self.PageSize = None
        self.PolicyName = None
        self.MonitorTypes = None
        self.Namespaces = None
        self.Dimensions = None
        self.ReceiverUids = None
        self.ReceiverGroups = None
        self.PolicyType = None
        self.Field = None
        self.Order = None
        self.ProjectIds = None
        self.NoticeIds = None
        self.RuleTypes = None
        self.Enable = None
        self.NotBindingNoticeRule = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.PolicyName = params.get("PolicyName")
        self.MonitorTypes = params.get("MonitorTypes")
        self.Namespaces = params.get("Namespaces")
        self.Dimensions = params.get("Dimensions")
        self.ReceiverUids = params.get("ReceiverUids")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.PolicyType = params.get("PolicyType")
        self.Field = params.get("Field")
        self.Order = params.get("Order")
        self.ProjectIds = params.get("ProjectIds")
        self.NoticeIds = params.get("NoticeIds")
        self.RuleTypes = params.get("RuleTypes")
        self.Enable = params.get("Enable")
        self.NotBindingNoticeRule = params.get("NotBindingNoticeRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmPoliciesResponse(AbstractModel):
    """DescribeAlarmPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 策略总数
        :type TotalCount: int
        :param Policies: 策略数组
        :type Policies: list of AlarmPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Policies = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Policies") is not None:
            self.Policies = []
            for item in params.get("Policies"):
                obj = AlarmPolicy()
                obj._deserialize(item)
                self.Policies.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmPolicyRequest(AbstractModel):
    """DescribeAlarmPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param PolicyId: 告警策略ID
        :type PolicyId: str
        """
        self.Module = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlarmPolicyResponse(AbstractModel):
    """DescribeAlarmPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Policy: 策略详情
        :type Policy: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicy`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Policy = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self.Policy = AlarmPolicy()
            self.Policy._deserialize(params.get("Policy"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlertRulesRequest(AbstractModel):
    """DescribeAlertRules请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param Offset: 偏移量，默认为 0
        :type Offset: int
        :param RuleId: 规则 ID
        :type RuleId: str
        :param RuleState: 规则状态码，取值如下：
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param RuleName: 规则名称
        :type RuleName: str
        :param Type: 报警策略模板分类
        :type Type: str
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.RuleId = None
        self.RuleState = None
        self.RuleName = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RuleId = params.get("RuleId")
        self.RuleState = params.get("RuleState")
        self.RuleName = params.get("RuleName")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAlertRulesResponse(AbstractModel):
    """DescribeAlertRules返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 报警规则数量
        :type TotalCount: int
        :param AlertRuleSet: 报警规则详情
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRuleSet: list of PrometheusRuleSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AlertRuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AlertRuleSet") is not None:
            self.AlertRuleSet = []
            for item in params.get("AlertRuleSet"):
                obj = PrometheusRuleSet()
                obj._deserialize(item)
                self.AlertRuleSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAllNamespacesRequest(AbstractModel):
    """DescribeAllNamespaces请求参数结构体

    """

    def __init__(self):
        """
        :param SceneType: 根据使用场景过滤 "ST_DASHBOARD"=Dashboard类型 或 "ST_ALARM"=告警类型
        :type SceneType: str
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param MonitorTypes: 根据监控类型过滤 不填默认查所有类型 "MT_QCE"=云产品监控
        :type MonitorTypes: list of str
        :param Ids: 根据namespace的Id过滤 不填默认查询所有
        :type Ids: list of str
        """
        self.SceneType = None
        self.Module = None
        self.MonitorTypes = None
        self.Ids = None


    def _deserialize(self, params):
        self.SceneType = params.get("SceneType")
        self.Module = params.get("Module")
        self.MonitorTypes = params.get("MonitorTypes")
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAllNamespacesResponse(AbstractModel):
    """DescribeAllNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param QceNamespaces: 云产品的告警策略类型，已废弃
        :type QceNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`
        :param CustomNamespaces: 其他告警策略类型，已废弃
        :type CustomNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`
        :param QceNamespacesNew: 云产品的告警策略类型
        :type QceNamespacesNew: list of CommonNamespace
        :param CustomNamespacesNew: 其他告警策略类型，暂不支持
        :type CustomNamespacesNew: list of CommonNamespace
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QceNamespaces = None
        self.CustomNamespaces = None
        self.QceNamespacesNew = None
        self.CustomNamespacesNew = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QceNamespaces") is not None:
            self.QceNamespaces = CommonNamespace()
            self.QceNamespaces._deserialize(params.get("QceNamespaces"))
        if params.get("CustomNamespaces") is not None:
            self.CustomNamespaces = CommonNamespace()
            self.CustomNamespaces._deserialize(params.get("CustomNamespaces"))
        if params.get("QceNamespacesNew") is not None:
            self.QceNamespacesNew = []
            for item in params.get("QceNamespacesNew"):
                obj = CommonNamespace()
                obj._deserialize(item)
                self.QceNamespacesNew.append(obj)
        if params.get("CustomNamespacesNew") is not None:
            self.CustomNamespacesNew = []
            for item in params.get("CustomNamespacesNew"):
                obj = CommonNamespace()
                obj._deserialize(item)
                self.CustomNamespacesNew.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 业务命名空间，各个云产品的业务命名空间不同。如需获取业务命名空间，请前往各产品监控指标文档，例如云服务器的命名空间，可参见 [云服务器监控指标](https://cloud.tencent.com/document/product/248/6843)
        :type Namespace: str
        :param MetricName: 指标名，各个云产品的指标名不同。如需获取指标名，请前往各产品监控指标文档，例如云服务器的指标名，可参见 [云服务器监控指标](https://cloud.tencent.com/document/product/248/6843)
        :type MetricName: str
        """
        self.Namespace = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBaseMetricsResponse(AbstractModel):
    """DescribeBaseMetrics返回参数结构体

    """

    def __init__(self):
        """
        :param MetricSet: 查询得到的指标描述列表
        :type MetricSet: list of MetricSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self.MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricSet()
                obj._deserialize(item)
                self.MetricSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBasicAlarmListAlarms(AbstractModel):
    """DescribeBasicAlarmList返回的Alarms

    """

    def __init__(self):
        """
        :param Id: 该条告警的ID
        :type Id: int
        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param Status: 告警状态ID，0表示未恢复；1表示已恢复；2,3,5表示数据不足；4表示已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param AlarmStatus: 告警状态，ALARM表示未恢复；OK表示已恢复；NO_DATA表示数据不足；NO_CONF表示已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmStatus: str
        :param GroupId: 策略组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param GroupName: 策略组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param FirstOccurTime: 发生时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOccurTime: str
        :param Duration: 持续时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param LastOccurTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOccurTime: str
        :param Content: 告警内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param ObjName: 告警对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjName: str
        :param ObjId: 告警对象ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjId: str
        :param ViewName: 策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        :param Vpc: VPC，只有CVM有
注意：此字段可能返回 null，表示取不到有效值。
        :type Vpc: str
        :param MetricId: 指标ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricId: int
        :param MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param AlarmType: 告警类型，0表示指标告警，2表示产品事件告警，3表示平台事件告警
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmType: int
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Dimensions: 告警对象维度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: str
        :param NotifyWay: 通知方式
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyWay: list of str
        :param InstanceGroup: 所属实例组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroup: list of InstanceGroup
        """
        self.Id = None
        self.ProjectId = None
        self.ProjectName = None
        self.Status = None
        self.AlarmStatus = None
        self.GroupId = None
        self.GroupName = None
        self.FirstOccurTime = None
        self.Duration = None
        self.LastOccurTime = None
        self.Content = None
        self.ObjName = None
        self.ObjId = None
        self.ViewName = None
        self.Vpc = None
        self.MetricId = None
        self.MetricName = None
        self.AlarmType = None
        self.Region = None
        self.Dimensions = None
        self.NotifyWay = None
        self.InstanceGroup = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.Status = params.get("Status")
        self.AlarmStatus = params.get("AlarmStatus")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.FirstOccurTime = params.get("FirstOccurTime")
        self.Duration = params.get("Duration")
        self.LastOccurTime = params.get("LastOccurTime")
        self.Content = params.get("Content")
        self.ObjName = params.get("ObjName")
        self.ObjId = params.get("ObjId")
        self.ViewName = params.get("ViewName")
        self.Vpc = params.get("Vpc")
        self.MetricId = params.get("MetricId")
        self.MetricName = params.get("MetricName")
        self.AlarmType = params.get("AlarmType")
        self.Region = params.get("Region")
        self.Dimensions = params.get("Dimensions")
        self.NotifyWay = params.get("NotifyWay")
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroup()
                obj._deserialize(item)
                self.InstanceGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBasicAlarmListRequest(AbstractModel):
    """DescribeBasicAlarmList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 接口模块名，当前取值monitor
        :type Module: str
        :param StartTime: 起始时间，默认一天前的时间戳
        :type StartTime: int
        :param EndTime: 结束时间，默认当前时间戳
        :type EndTime: int
        :param Limit: 分页参数，每页返回的数量，取值1~100，默认20
        :type Limit: int
        :param Offset: 分页参数，页偏移量，从0开始计数，默认0
        :type Offset: int
        :param OccurTimeOrder: 根据发生时间排序，取值ASC或DESC
        :type OccurTimeOrder: str
        :param ProjectIds: 根据项目ID过滤
        :type ProjectIds: list of int
        :param ViewNames: 根据策略类型过滤
        :type ViewNames: list of str
        :param AlarmStatus: 根据告警状态过滤
        :type AlarmStatus: list of int
        :param ObjLike: 根据告警对象过滤
        :type ObjLike: str
        :param InstanceGroupIds: 根据实例组ID过滤
        :type InstanceGroupIds: list of int
        :param MetricNames: 根据指标名过滤
        :type MetricNames: list of str
        """
        self.Module = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.OccurTimeOrder = None
        self.ProjectIds = None
        self.ViewNames = None
        self.AlarmStatus = None
        self.ObjLike = None
        self.InstanceGroupIds = None
        self.MetricNames = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OccurTimeOrder = params.get("OccurTimeOrder")
        self.ProjectIds = params.get("ProjectIds")
        self.ViewNames = params.get("ViewNames")
        self.AlarmStatus = params.get("AlarmStatus")
        self.ObjLike = params.get("ObjLike")
        self.InstanceGroupIds = params.get("InstanceGroupIds")
        self.MetricNames = params.get("MetricNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBasicAlarmListResponse(AbstractModel):
    """DescribeBasicAlarmList返回参数结构体

    """

    def __init__(self):
        """
        :param Alarms: 告警列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Alarms: list of DescribeBasicAlarmListAlarms
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Alarms = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeBasicAlarmListAlarms()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBindingPolicyObjectListDimension(AbstractModel):
    """DescribeBindingPolicyObjectList接口的Dimension

    """

    def __init__(self):
        """
        :param RegionId: 地域id
        :type RegionId: int
        :param Region: 地域简称
        :type Region: str
        :param Dimensions: 维度组合json字符串
        :type Dimensions: str
        :param EventDimensions: 事件维度组合json字符串
        :type EventDimensions: str
        """
        self.RegionId = None
        self.Region = None
        self.Dimensions = None
        self.EventDimensions = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Region = params.get("Region")
        self.Dimensions = params.get("Dimensions")
        self.EventDimensions = params.get("EventDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBindingPolicyObjectListInstance(AbstractModel):
    """查询策略绑定对象列表接口返回的对象实例信息

    """

    def __init__(self):
        """
        :param UniqueId: 对象唯一id
        :type UniqueId: str
        :param Dimensions: 表示对象实例的维度集合，jsonObj字符串
        :type Dimensions: str
        :param IsShielded: 对象是否被屏蔽，0表示未屏蔽，1表示被屏蔽
        :type IsShielded: int
        :param Region: 对象所在的地域
        :type Region: str
        """
        self.UniqueId = None
        self.Dimensions = None
        self.IsShielded = None
        self.Region = None


    def _deserialize(self, params):
        self.UniqueId = params.get("UniqueId")
        self.Dimensions = params.get("Dimensions")
        self.IsShielded = params.get("IsShielded")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBindingPolicyObjectListInstanceGroup(AbstractModel):
    """DescribeBindingPolicyObjectList返回的是实例分组信息

    """

    def __init__(self):
        """
        :param InstanceGroupId: 实例分组id
        :type InstanceGroupId: int
        :param ViewName: 告警策略类型名称
        :type ViewName: str
        :param LastEditUin: 最后编辑uin
        :type LastEditUin: str
        :param GroupName: 实例分组名称
        :type GroupName: str
        :param InstanceSum: 实例数量
        :type InstanceSum: int
        :param UpdateTime: 更新时间
        :type UpdateTime: int
        :param InsertTime: 创建时间
        :type InsertTime: int
        :param Regions: 实例所在的地域集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Regions: list of str
        """
        self.InstanceGroupId = None
        self.ViewName = None
        self.LastEditUin = None
        self.GroupName = None
        self.InstanceSum = None
        self.UpdateTime = None
        self.InsertTime = None
        self.Regions = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.GroupName = params.get("GroupName")
        self.InstanceSum = params.get("InstanceSum")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBindingPolicyObjectListRequest(AbstractModel):
    """DescribeBindingPolicyObjectList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param GroupId: 策略组id
        :type GroupId: int
        :param Limit: 分页参数，每页返回的数量，取值1~100，默认20
        :type Limit: int
        :param Offset: 分页参数，页偏移量，从0开始计数，默认0
        :type Offset: int
        :param Dimensions: 筛选对象的维度信息
        :type Dimensions: list of DescribeBindingPolicyObjectListDimension
        """
        self.Module = None
        self.GroupId = None
        self.Limit = None
        self.Offset = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeBindingPolicyObjectListDimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBindingPolicyObjectListResponse(AbstractModel):
    """DescribeBindingPolicyObjectList返回参数结构体

    """

    def __init__(self):
        """
        :param List: 绑定的对象实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DescribeBindingPolicyObjectListInstance
        :param Total: 绑定的对象实例总数
        :type Total: int
        :param NoShieldedSum: 未屏蔽的对象实例数
        :type NoShieldedSum: int
        :param InstanceGroup: 绑定的实例分组信息，没有绑定实例分组则为空
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListInstanceGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.NoShieldedSum = None
        self.InstanceGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DescribeBindingPolicyObjectListInstance()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.NoShieldedSum = params.get("NoShieldedSum")
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = DescribeBindingPolicyObjectListInstanceGroup()
            self.InstanceGroup._deserialize(params.get("InstanceGroup"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMonitorTypesRequest(AbstractModel):
    """DescribeMonitorTypes请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定值 monitor
        :type Module: str
        """
        self.Module = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMonitorTypesResponse(AbstractModel):
    """DescribeMonitorTypes返回参数结构体

    """

    def __init__(self):
        """
        :param MonitorTypes: 监控类型，云产品监控为 MT_QCE
        :type MonitorTypes: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MonitorTypes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MonitorTypes = params.get("MonitorTypes")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListCondition(AbstractModel):
    """DescribePolicyConditionList策略条件

    """

    def __init__(self):
        """
        :param PolicyViewName: 策略视图名称
        :type PolicyViewName: str
        :param EventMetrics: 事件告警条件
注意：此字段可能返回 null，表示取不到有效值。
        :type EventMetrics: list of DescribePolicyConditionListEventMetric
        :param IsSupportMultiRegion: 是否支持多地域
        :type IsSupportMultiRegion: bool
        :param Metrics: 指标告警条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of DescribePolicyConditionListMetric
        :param Name: 策略类型名称
        :type Name: str
        :param SortId: 排序id
        :type SortId: int
        :param SupportDefault: 是否支持默认策略
        :type SupportDefault: bool
        :param SupportRegions: 支持该策略类型的地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportRegions: list of str
        """
        self.PolicyViewName = None
        self.EventMetrics = None
        self.IsSupportMultiRegion = None
        self.Metrics = None
        self.Name = None
        self.SortId = None
        self.SupportDefault = None
        self.SupportRegions = None


    def _deserialize(self, params):
        self.PolicyViewName = params.get("PolicyViewName")
        if params.get("EventMetrics") is not None:
            self.EventMetrics = []
            for item in params.get("EventMetrics"):
                obj = DescribePolicyConditionListEventMetric()
                obj._deserialize(item)
                self.EventMetrics.append(obj)
        self.IsSupportMultiRegion = params.get("IsSupportMultiRegion")
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = DescribePolicyConditionListMetric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.Name = params.get("Name")
        self.SortId = params.get("SortId")
        self.SupportDefault = params.get("SupportDefault")
        self.SupportRegions = params.get("SupportRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListConfigManual(AbstractModel):
    """DescribePolicyConditionList.ConfigManual

    """

    def __init__(self):
        """
        :param CalcType: 检测方式
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcType`
        :param CalcValue: 检测阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcValue: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcValue`
        :param ContinueTime: 持续时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueTime: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualContinueTime`
        :param Period: 数据周期
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriod`
        :param PeriodNum: 持续周期个数
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodNum: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriodNum`
        :param StatType: 聚合方式
注意：此字段可能返回 null，表示取不到有效值。
        :type StatType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualStatType`
        """
        self.CalcType = None
        self.CalcValue = None
        self.ContinueTime = None
        self.Period = None
        self.PeriodNum = None
        self.StatType = None


    def _deserialize(self, params):
        if params.get("CalcType") is not None:
            self.CalcType = DescribePolicyConditionListConfigManualCalcType()
            self.CalcType._deserialize(params.get("CalcType"))
        if params.get("CalcValue") is not None:
            self.CalcValue = DescribePolicyConditionListConfigManualCalcValue()
            self.CalcValue._deserialize(params.get("CalcValue"))
        if params.get("ContinueTime") is not None:
            self.ContinueTime = DescribePolicyConditionListConfigManualContinueTime()
            self.ContinueTime._deserialize(params.get("ContinueTime"))
        if params.get("Period") is not None:
            self.Period = DescribePolicyConditionListConfigManualPeriod()
            self.Period._deserialize(params.get("Period"))
        if params.get("PeriodNum") is not None:
            self.PeriodNum = DescribePolicyConditionListConfigManualPeriodNum()
            self.PeriodNum._deserialize(params.get("PeriodNum"))
        if params.get("StatType") is not None:
            self.StatType = DescribePolicyConditionListConfigManualStatType()
            self.StatType._deserialize(params.get("StatType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListConfigManualCalcType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcType

    """

    def __init__(self):
        """
        :param Keys: CalcType 取值
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param Need: 是否必须
        :type Need: bool
        """
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListConfigManualCalcValue(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcValue

    """

    def __init__(self):
        """
        :param Default: 默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: str
        :param Fixed: 固定值
注意：此字段可能返回 null，表示取不到有效值。
        :type Fixed: str
        :param Max: 最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: str
        :param Min: 最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: str
        :param Need: 是否必须
        :type Need: bool
        """
        self.Default = None
        self.Fixed = None
        self.Max = None
        self.Min = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Fixed = params.get("Fixed")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListConfigManualContinueTime(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.ContinueTime

    """

    def __init__(self):
        """
        :param Default: 默认持续时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: int
        :param Keys: 可选持续时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param Need: 是否必须
        :type Need: bool
        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListConfigManualPeriod(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.Period

    """

    def __init__(self):
        """
        :param Default: 默认周期，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: int
        :param Keys: 可选周期，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param Need: 是否必须
        :type Need: bool
        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListConfigManualPeriodNum(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.PeriodNum

    """

    def __init__(self):
        """
        :param Default: 默认周期数
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: int
        :param Keys: 可选周期数
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param Need: 是否必须
        :type Need: bool
        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListConfigManualStatType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.StatType

    """

    def __init__(self):
        """
        :param P5: 数据聚合方式，周期5秒
注意：此字段可能返回 null，表示取不到有效值。
        :type P5: str
        :param P10: 数据聚合方式，周期10秒
注意：此字段可能返回 null，表示取不到有效值。
        :type P10: str
        :param P60: 数据聚合方式，周期1分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type P60: str
        :param P300: 数据聚合方式，周期5分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type P300: str
        :param P600: 数据聚合方式，周期10分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type P600: str
        :param P1800: 数据聚合方式，周期30分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type P1800: str
        :param P3600: 数据聚合方式，周期1小时
注意：此字段可能返回 null，表示取不到有效值。
        :type P3600: str
        :param P86400: 数据聚合方式，周期1天
注意：此字段可能返回 null，表示取不到有效值。
        :type P86400: str
        """
        self.P5 = None
        self.P10 = None
        self.P60 = None
        self.P300 = None
        self.P600 = None
        self.P1800 = None
        self.P3600 = None
        self.P86400 = None


    def _deserialize(self, params):
        self.P5 = params.get("P5")
        self.P10 = params.get("P10")
        self.P60 = params.get("P60")
        self.P300 = params.get("P300")
        self.P600 = params.get("P600")
        self.P1800 = params.get("P1800")
        self.P3600 = params.get("P3600")
        self.P86400 = params.get("P86400")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListEventMetric(AbstractModel):
    """DescribePolicyConditionList.EventMetric

    """

    def __init__(self):
        """
        :param EventId: 事件id
        :type EventId: int
        :param EventShowName: 事件名称
        :type EventShowName: str
        :param NeedRecovered: 是否需要恢复
        :type NeedRecovered: bool
        :param Type: 事件类型，预留字段，当前固定取值为2
        :type Type: int
        """
        self.EventId = None
        self.EventShowName = None
        self.NeedRecovered = None
        self.Type = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.EventShowName = params.get("EventShowName")
        self.NeedRecovered = params.get("NeedRecovered")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListMetric(AbstractModel):
    """指标告警配置

    """

    def __init__(self):
        """
        :param ConfigManual: 指标配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigManual: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManual`
        :param MetricId: 指标id
        :type MetricId: int
        :param MetricShowName: 指标名称
        :type MetricShowName: str
        :param MetricUnit: 指标单位
        :type MetricUnit: str
        """
        self.ConfigManual = None
        self.MetricId = None
        self.MetricShowName = None
        self.MetricUnit = None


    def _deserialize(self, params):
        if params.get("ConfigManual") is not None:
            self.ConfigManual = DescribePolicyConditionListConfigManual()
            self.ConfigManual._deserialize(params.get("ConfigManual"))
        self.MetricId = params.get("MetricId")
        self.MetricShowName = params.get("MetricShowName")
        self.MetricUnit = params.get("MetricUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListRequest(AbstractModel):
    """DescribePolicyConditionList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        """
        self.Module = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyConditionListResponse(AbstractModel):
    """DescribePolicyConditionList返回参数结构体

    """

    def __init__(self):
        """
        :param Conditions: 告警策略条件列表
        :type Conditions: list of DescribePolicyConditionListCondition
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Conditions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyConditionListCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupInfoCallback(AbstractModel):
    """查询策略输出的用户回调信息

    """

    def __init__(self):
        """
        :param CallbackUrl: 用户回调接口地址
        :type CallbackUrl: str
        :param ValidFlag: 用户回调接口状态，0表示未验证，1表示已验证，2表示存在url但没有通过验证
        :type ValidFlag: int
        :param VerifyCode: 用户回调接口验证码
        :type VerifyCode: str
        """
        self.CallbackUrl = None
        self.ValidFlag = None
        self.VerifyCode = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.ValidFlag = params.get("ValidFlag")
        self.VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupInfoCondition(AbstractModel):
    """查询策略输出的阈值告警条件

    """

    def __init__(self):
        """
        :param MetricShowName: 指标名称
        :type MetricShowName: str
        :param Period: 数据聚合周期(单位秒)
        :type Period: int
        :param MetricId: 指标id
        :type MetricId: int
        :param RuleId: 阈值规则id
        :type RuleId: int
        :param Unit: 指标单位
        :type Unit: str
        :param AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param CalcType: 比较类型，1表示大于，2表示大于等于，3表示小于，4表示小于等于，5表示相等，6表示不相等，7表示日同比上涨，8表示日同比下降，9表示周同比上涨，10表示周同比下降，11表示周期环比上涨，12表示周期环比下降
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcType: int
        :param CalcValue: 检测阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type CalcValue: str
        :param ContinueTime: 持续多长时间触发规则会告警(单位秒)
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinueTime: int
        :param MetricName: 告警指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        """
        self.MetricShowName = None
        self.Period = None
        self.MetricId = None
        self.RuleId = None
        self.Unit = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.CalcType = None
        self.CalcValue = None
        self.ContinueTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.MetricShowName = params.get("MetricShowName")
        self.Period = params.get("Period")
        self.MetricId = params.get("MetricId")
        self.RuleId = params.get("RuleId")
        self.Unit = params.get("Unit")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.ContinueTime = params.get("ContinueTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupInfoConditionTpl(AbstractModel):
    """查询策略输出的模板策略组信息

    """

    def __init__(self):
        """
        :param GroupId: 策略组id
        :type GroupId: int
        :param GroupName: 策略组名称
        :type GroupName: str
        :param ViewName: 策略类型
        :type ViewName: str
        :param Remark: 策略组说明
        :type Remark: str
        :param LastEditUin: 最后编辑的用户uin
        :type LastEditUin: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param InsertTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: int
        :param IsUnionRule: 是否且规则
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        """
        self.GroupId = None
        self.GroupName = None
        self.ViewName = None
        self.Remark = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.InsertTime = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ViewName = params.get("ViewName")
        self.Remark = params.get("Remark")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupInfoEventCondition(AbstractModel):
    """查询策略输出的事件告警条件

    """

    def __init__(self):
        """
        :param EventId: 事件id
        :type EventId: int
        :param RuleId: 事件告警规则id
        :type RuleId: int
        :param EventShowName: 事件名称
        :type EventShowName: str
        :param AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        """
        self.EventId = None
        self.RuleId = None
        self.EventShowName = None
        self.AlarmNotifyPeriod = None
        self.AlarmNotifyType = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.RuleId = params.get("RuleId")
        self.EventShowName = params.get("EventShowName")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupInfoReceiverInfo(AbstractModel):
    """查询策略输出的告警接收人信息

    """

    def __init__(self):
        """
        :param ReceiverGroupList: 告警接收组id列表
        :type ReceiverGroupList: list of int
        :param ReceiverUserList: 告警接收人id列表
        :type ReceiverUserList: list of int
        :param StartTime: 告警时间段开始时间。范围[0,86400)，作为unix时间戳转成北京时间后去掉日期，例如7200表示"10:0:0"
        :type StartTime: int
        :param EndTime: 告警时间段结束时间。含义同StartTime
        :type EndTime: int
        :param ReceiverType: 接收类型。“group”(接收组)或“user”(接收人)
        :type ReceiverType: str
        :param NotifyWay: 告警通知方式。可选 "SMS","SITE","EMAIL","CALL","WECHAT"
        :type NotifyWay: list of str
        :param UidList: 电话告警接收者uid
注意：此字段可能返回 null，表示取不到有效值。
        :type UidList: list of int
        :param RoundNumber: 电话告警轮数
        :type RoundNumber: int
        :param RoundInterval: 电话告警每轮间隔（秒）
        :type RoundInterval: int
        :param PersonInterval: 电话告警对个人间隔（秒）
        :type PersonInterval: int
        :param NeedSendNotice: 是否需要电话告警触达提示。0不需要，1需要
        :type NeedSendNotice: int
        :param SendFor: 电话告警通知时机。可选"OCCUR"(告警时通知),"RECOVER"(恢复时通知)
        :type SendFor: list of str
        :param RecoverNotify: 恢复通知方式。可选"SMS"
        :type RecoverNotify: list of str
        :param ReceiveLanguage: 告警发送语言
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiveLanguage: str
        """
        self.ReceiverGroupList = None
        self.ReceiverUserList = None
        self.StartTime = None
        self.EndTime = None
        self.ReceiverType = None
        self.NotifyWay = None
        self.UidList = None
        self.RoundNumber = None
        self.RoundInterval = None
        self.PersonInterval = None
        self.NeedSendNotice = None
        self.SendFor = None
        self.RecoverNotify = None
        self.ReceiveLanguage = None


    def _deserialize(self, params):
        self.ReceiverGroupList = params.get("ReceiverGroupList")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReceiverType = params.get("ReceiverType")
        self.NotifyWay = params.get("NotifyWay")
        self.UidList = params.get("UidList")
        self.RoundNumber = params.get("RoundNumber")
        self.RoundInterval = params.get("RoundInterval")
        self.PersonInterval = params.get("PersonInterval")
        self.NeedSendNotice = params.get("NeedSendNotice")
        self.SendFor = params.get("SendFor")
        self.RecoverNotify = params.get("RecoverNotify")
        self.ReceiveLanguage = params.get("ReceiveLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupInfoRequest(AbstractModel):
    """DescribePolicyGroupInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param GroupId: 策略组id
        :type GroupId: int
        """
        self.Module = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupInfoResponse(AbstractModel):
    """DescribePolicyGroupInfo返回参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 策略组名称
        :type GroupName: str
        :param ProjectId: 策略组所属的项目id
        :type ProjectId: int
        :param IsDefault: 是否为默认策略，0表示非默认策略，1表示默认策略
        :type IsDefault: int
        :param ViewName: 策略类型
        :type ViewName: str
        :param Remark: 策略说明
        :type Remark: str
        :param ShowName: 策略类型名称
        :type ShowName: str
        :param LastEditUin: 最近编辑的用户uin
        :type LastEditUin: str
        :param UpdateTime: 最近编辑时间
        :type UpdateTime: str
        :param Region: 该策略支持的地域
        :type Region: list of str
        :param DimensionGroup: 策略类型的维度列表
        :type DimensionGroup: list of str
        :param ConditionsConfig: 阈值规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionsConfig: list of DescribePolicyGroupInfoCondition
        :param EventConfig: 产品事件规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventConfig: list of DescribePolicyGroupInfoEventCondition
        :param ReceiverInfos: 用户接收人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param Callback: 用户回调信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Callback: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoCallback`
        :param ConditionsTemp: 模板策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param CanSetDefault: 是否可以设置成默认策略
        :type CanSetDefault: bool
        :param IsUnionRule: 是否且规则
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupName = None
        self.ProjectId = None
        self.IsDefault = None
        self.ViewName = None
        self.Remark = None
        self.ShowName = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.Region = None
        self.DimensionGroup = None
        self.ConditionsConfig = None
        self.EventConfig = None
        self.ReceiverInfos = None
        self.Callback = None
        self.ConditionsTemp = None
        self.CanSetDefault = None
        self.IsUnionRule = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.ProjectId = params.get("ProjectId")
        self.IsDefault = params.get("IsDefault")
        self.ViewName = params.get("ViewName")
        self.Remark = params.get("Remark")
        self.ShowName = params.get("ShowName")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.Region = params.get("Region")
        self.DimensionGroup = params.get("DimensionGroup")
        if params.get("ConditionsConfig") is not None:
            self.ConditionsConfig = []
            for item in params.get("ConditionsConfig"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self.ConditionsConfig.append(obj)
        if params.get("EventConfig") is not None:
            self.EventConfig = []
            for item in params.get("EventConfig"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self.EventConfig.append(obj)
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        if params.get("Callback") is not None:
            self.Callback = DescribePolicyGroupInfoCallback()
            self.Callback._deserialize(params.get("Callback"))
        if params.get("ConditionsTemp") is not None:
            self.ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self.ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self.CanSetDefault = params.get("CanSetDefault")
        self.IsUnionRule = params.get("IsUnionRule")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupListGroup(AbstractModel):
    """DescribePolicyGroupList.Group

    """

    def __init__(self):
        """
        :param GroupId: 策略组id
        :type GroupId: int
        :param GroupName: 策略组名称
        :type GroupName: str
        :param IsOpen: 是否开启
        :type IsOpen: bool
        :param ViewName: 策略视图名称
        :type ViewName: str
        :param LastEditUin: 最近编辑的用户uin
        :type LastEditUin: str
        :param UpdateTime: 最后修改时间
        :type UpdateTime: int
        :param InsertTime: 创建时间
        :type InsertTime: int
        :param UseSum: 策略组绑定的实例数
        :type UseSum: int
        :param NoShieldedSum: 策略组绑定的未屏蔽实例数
        :type NoShieldedSum: int
        :param IsDefault: 是否为默认策略，0表示非默认策略，1表示默认策略
        :type IsDefault: int
        :param CanSetDefault: 是否可以设置成默认策略
        :type CanSetDefault: bool
        :param ParentGroupId: 父策略组id
        :type ParentGroupId: int
        :param Remark: 策略组备注
        :type Remark: str
        :param ProjectId: 策略组所属项目id
        :type ProjectId: int
        :param Conditions: 阈值规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of DescribePolicyGroupInfoCondition
        :param EventConditions: 产品事件规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventConditions: list of DescribePolicyGroupInfoEventCondition
        :param ReceiverInfos: 用户接收人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param ConditionsTemp: 模板策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param InstanceGroup: 策略组绑定的实例组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListGroupInstanceGroup`
        :param IsUnionRule: 且或规则标识, 0表示或规则(任意一条规则满足阈值条件就告警), 1表示且规则(所有规则都满足阈值条件才告警)
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        """
        self.GroupId = None
        self.GroupName = None
        self.IsOpen = None
        self.ViewName = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.InsertTime = None
        self.UseSum = None
        self.NoShieldedSum = None
        self.IsDefault = None
        self.CanSetDefault = None
        self.ParentGroupId = None
        self.Remark = None
        self.ProjectId = None
        self.Conditions = None
        self.EventConditions = None
        self.ReceiverInfos = None
        self.ConditionsTemp = None
        self.InstanceGroup = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.IsOpen = params.get("IsOpen")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.UseSum = params.get("UseSum")
        self.NoShieldedSum = params.get("NoShieldedSum")
        self.IsDefault = params.get("IsDefault")
        self.CanSetDefault = params.get("CanSetDefault")
        self.ParentGroupId = params.get("ParentGroupId")
        self.Remark = params.get("Remark")
        self.ProjectId = params.get("ProjectId")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        if params.get("ConditionsTemp") is not None:
            self.ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self.ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = DescribePolicyGroupListGroupInstanceGroup()
            self.InstanceGroup._deserialize(params.get("InstanceGroup"))
        self.IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupListGroupInstanceGroup(AbstractModel):
    """DescribePolicyGroupList接口策略组绑定的实例分组信息

    """

    def __init__(self):
        """
        :param InstanceGroupId: 实例分组名称id
        :type InstanceGroupId: int
        :param ViewName: 策略类型视图名称
        :type ViewName: str
        :param LastEditUin: 最近编辑的用户uin
        :type LastEditUin: str
        :param GroupName: 实例分组名称
        :type GroupName: str
        :param InstanceSum: 实例数量
        :type InstanceSum: int
        :param UpdateTime: 更新时间
        :type UpdateTime: int
        :param InsertTime: 创建时间
        :type InsertTime: int
        """
        self.InstanceGroupId = None
        self.ViewName = None
        self.LastEditUin = None
        self.GroupName = None
        self.InstanceSum = None
        self.UpdateTime = None
        self.InsertTime = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.GroupName = params.get("GroupName")
        self.InstanceSum = params.get("InstanceSum")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupListRequest(AbstractModel):
    """DescribePolicyGroupList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param Limit: 分页参数，每页返回的数量，取值1~100
        :type Limit: int
        :param Offset: 分页参数，页偏移量，从0开始计数
        :type Offset: int
        :param Like: 按策略名搜索
        :type Like: str
        :param InstanceGroupId: 实例分组id
        :type InstanceGroupId: int
        :param UpdateTimeOrder: 按更新时间排序, asc 或者 desc
        :type UpdateTimeOrder: str
        :param ProjectIds: 项目id列表
        :type ProjectIds: list of int
        :param ViewNames: 告警策略类型列表
        :type ViewNames: list of str
        :param FilterUnuseReceiver: 是否过滤无接收人策略组, 1表示过滤, 0表示不过滤
        :type FilterUnuseReceiver: int
        :param Receivers: 过滤条件, 接收组列表
        :type Receivers: list of str
        :param ReceiverUserList: 过滤条件, 接收人列表
        :type ReceiverUserList: list of str
        :param Dimensions: 维度组合字段(json字符串), 例如[[{"name":"unInstanceId","value":"ins-6e4b2aaa"}]]
        :type Dimensions: str
        :param ConditionTempGroupId: 模板策略组id, 多个id用逗号分隔
        :type ConditionTempGroupId: str
        :param ReceiverType: 过滤条件, 接收人或者接收组, user表示接收人, group表示接收组
        :type ReceiverType: str
        :param IsOpen: 过滤条件，告警策略是否已启动或停止
        :type IsOpen: bool
        """
        self.Module = None
        self.Limit = None
        self.Offset = None
        self.Like = None
        self.InstanceGroupId = None
        self.UpdateTimeOrder = None
        self.ProjectIds = None
        self.ViewNames = None
        self.FilterUnuseReceiver = None
        self.Receivers = None
        self.ReceiverUserList = None
        self.Dimensions = None
        self.ConditionTempGroupId = None
        self.ReceiverType = None
        self.IsOpen = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Like = params.get("Like")
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.UpdateTimeOrder = params.get("UpdateTimeOrder")
        self.ProjectIds = params.get("ProjectIds")
        self.ViewNames = params.get("ViewNames")
        self.FilterUnuseReceiver = params.get("FilterUnuseReceiver")
        self.Receivers = params.get("Receivers")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.Dimensions = params.get("Dimensions")
        self.ConditionTempGroupId = params.get("ConditionTempGroupId")
        self.ReceiverType = params.get("ReceiverType")
        self.IsOpen = params.get("IsOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePolicyGroupListResponse(AbstractModel):
    """DescribePolicyGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param GroupList: 策略组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of DescribePolicyGroupListGroup
        :param Total: 策略组总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = DescribePolicyGroupListGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductEventListDimensions(AbstractModel):
    """DescribeProductEventList的入参Dimensions

    """

    def __init__(self):
        """
        :param Name: 维度名
        :type Name: str
        :param Value: 维度值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductEventListEvents(AbstractModel):
    """DescribeProductEventList返回的Events

    """

    def __init__(self):
        """
        :param EventId: 事件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: int
        :param EventCName: 事件中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCName: str
        :param EventEName: 事件英文名
注意：此字段可能返回 null，表示取不到有效值。
        :type EventEName: str
        :param EventName: 事件简称
注意：此字段可能返回 null，表示取不到有效值。
        :type EventName: str
        :param ProductCName: 产品中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCName: str
        :param ProductEName: 产品英文名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductEName: str
        :param ProductName: 产品简称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param SupportAlarm: 是否支持告警
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportAlarm: int
        :param Type: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param Dimensions: 实例对象信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: list of DescribeProductEventListEventsDimensions
        :param AdditionMsg: 实例对象附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AdditionMsg: list of DescribeProductEventListEventsDimensions
        :param IsAlarmConfig: 是否配置告警
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAlarmConfig: int
        :param GroupInfo: 策略信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupInfo: list of DescribeProductEventListEventsGroupInfo
        :param ViewName: 显示名称ViewName
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewName: str
        """
        self.EventId = None
        self.EventCName = None
        self.EventEName = None
        self.EventName = None
        self.ProductCName = None
        self.ProductEName = None
        self.ProductName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Status = None
        self.SupportAlarm = None
        self.Type = None
        self.StartTime = None
        self.UpdateTime = None
        self.Dimensions = None
        self.AdditionMsg = None
        self.IsAlarmConfig = None
        self.GroupInfo = None
        self.ViewName = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.EventCName = params.get("EventCName")
        self.EventEName = params.get("EventEName")
        self.EventName = params.get("EventName")
        self.ProductCName = params.get("ProductCName")
        self.ProductEName = params.get("ProductEName")
        self.ProductName = params.get("ProductName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.SupportAlarm = params.get("SupportAlarm")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        if params.get("AdditionMsg") is not None:
            self.AdditionMsg = []
            for item in params.get("AdditionMsg"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self.AdditionMsg.append(obj)
        self.IsAlarmConfig = params.get("IsAlarmConfig")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = DescribeProductEventListEventsGroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductEventListEventsDimensions(AbstractModel):
    """DescribeProductEventList返回的Events的Dimensions

    """

    def __init__(self):
        """
        :param Key: 维度名（英文）
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Name: 维度名（中文）
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 维度值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductEventListEventsGroupInfo(AbstractModel):
    """DescribeProductEventList返回的Events里的GroupInfo

    """

    def __init__(self):
        """
        :param GroupId: 策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param GroupName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductEventListOverView(AbstractModel):
    """DescribeProductEventList返回的OverView对象

    """

    def __init__(self):
        """
        :param StatusChangeAmount: 状态变更的事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusChangeAmount: int
        :param UnConfigAlarmAmount: 告警状态未配置的事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnConfigAlarmAmount: int
        :param UnNormalEventAmount: 异常事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnNormalEventAmount: int
        :param UnRecoverAmount: 未恢复的事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnRecoverAmount: int
        """
        self.StatusChangeAmount = None
        self.UnConfigAlarmAmount = None
        self.UnNormalEventAmount = None
        self.UnRecoverAmount = None


    def _deserialize(self, params):
        self.StatusChangeAmount = params.get("StatusChangeAmount")
        self.UnConfigAlarmAmount = params.get("UnConfigAlarmAmount")
        self.UnNormalEventAmount = params.get("UnNormalEventAmount")
        self.UnRecoverAmount = params.get("UnRecoverAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductEventListRequest(AbstractModel):
    """DescribeProductEventList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 接口模块名，固定值"monitor"
        :type Module: str
        :param ProductName: 产品类型过滤，比如"cvm"表示云服务器
        :type ProductName: list of str
        :param EventName: 事件名称过滤，比如"guest_reboot"表示机器重启
        :type EventName: list of str
        :param InstanceId: 影响对象，比如"ins-19708ino"
        :type InstanceId: list of str
        :param Dimensions: 维度过滤，比如外网IP:10.0.0.1
        :type Dimensions: list of DescribeProductEventListDimensions
        :param RegionList: 产品事件地域过滤参数，比如gz，各地域缩写可参见[地域列表](https://cloud.tencent.com/document/product/248/50863)
        :type RegionList: list of str
        :param Type: 事件类型过滤，取值范围["status_change","abnormal"]，分别表示状态变更、异常事件
        :type Type: list of str
        :param Status: 事件状态过滤，取值范围["recover","alarm","-"]，分别表示已恢复、未恢复、无状态
        :type Status: list of str
        :param Project: 项目ID过滤
        :type Project: list of str
        :param IsAlarmConfig: 告警状态配置过滤，1表示已配置，0表示未配置
        :type IsAlarmConfig: int
        :param TimeOrder: 按更新时间排序，ASC表示升序，DESC表示降序，默认DESC
        :type TimeOrder: str
        :param StartTime: 起始时间，默认一天前的时间戳
        :type StartTime: int
        :param EndTime: 结束时间，默认当前时间戳
        :type EndTime: int
        :param Offset: 页偏移量，默认0
        :type Offset: int
        :param Limit: 每页返回的数量，默认20
        :type Limit: int
        """
        self.Module = None
        self.ProductName = None
        self.EventName = None
        self.InstanceId = None
        self.Dimensions = None
        self.RegionList = None
        self.Type = None
        self.Status = None
        self.Project = None
        self.IsAlarmConfig = None
        self.TimeOrder = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.ProductName = params.get("ProductName")
        self.EventName = params.get("EventName")
        self.InstanceId = params.get("InstanceId")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListDimensions()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.RegionList = params.get("RegionList")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Project = params.get("Project")
        self.IsAlarmConfig = params.get("IsAlarmConfig")
        self.TimeOrder = params.get("TimeOrder")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductEventListResponse(AbstractModel):
    """DescribeProductEventList返回参数结构体

    """

    def __init__(self):
        """
        :param Events: 事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of DescribeProductEventListEvents
        :param OverView: 事件统计
        :type OverView: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListOverView`
        :param Total: 事件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.OverView = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = DescribeProductEventListEvents()
                obj._deserialize(item)
                self.Events.append(obj)
        if params.get("OverView") is not None:
            self.OverView = DescribeProductEventListOverView()
            self.OverView._deserialize(params.get("OverView"))
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductListRequest(AbstractModel):
    """DescribeProductList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定传值monitor
        :type Module: str
        :param Order: 排序方式：DESC/ASC（区分大小写），默认值DESC
        :type Order: str
        :param Offset: 分页查询的偏移量，默认值0
        :type Offset: int
        :param Limit: 分页查询的每页数据量，默认值20
        :type Limit: int
        """
        self.Module = None
        self.Order = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Order = params.get("Order")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductListResponse(AbstractModel):
    """DescribeProductList返回参数结构体

    """

    def __init__(self):
        """
        :param ProductList: 产品信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductList: list of ProductSimple
        :param TotalCount: 产品总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProductList") is not None:
            self.ProductList = []
            for item in params.get("ProductList"):
                obj = ProductSimple()
                obj._deserialize(item)
                self.ProductList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeServiceDiscoveryRequest(AbstractModel):
    """DescribeServiceDiscovery请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param KubeClusterId: <li>类型是 TKE，为对应的腾讯云容器服务集群 ID</li>
        :type KubeClusterId: str
        :param KubeType: 用户 Kubernetes 集群类型：
<li> 1 = 容器服务集群(TKE) </li>
        :type KubeType: int
        """
        self.InstanceId = None
        self.KubeClusterId = None
        self.KubeType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeClusterId = params.get("KubeClusterId")
        self.KubeType = params.get("KubeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeServiceDiscoveryResponse(AbstractModel):
    """DescribeServiceDiscovery返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceDiscoverySet: 返回服务发现列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDiscoverySet: list of ServiceDiscoveryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceDiscoverySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceDiscoverySet") is not None:
            self.ServiceDiscoverySet = []
            for item in params.get("ServiceDiscoverySet"):
                obj = ServiceDiscoveryItem()
                obj._deserialize(item)
                self.ServiceDiscoverySet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStatisticDataRequest(AbstractModel):
    """DescribeStatisticData请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 所属模块，固定值，为monitor
        :type Module: str
        :param Namespace: 命名空间，目前只支持QCE/TKE
        :type Namespace: str
        :param MetricNames: 指标名列表
        :type MetricNames: list of str
        :param Conditions: 维度条件，操作符支持=、in
        :type Conditions: list of MidQueryCondition
        :param Period: 统计粒度。默认取值为300，单位为s
        :type Period: int
        :param StartTime: 起始时间，默认为当前时间，如2020-12-08T19:51:23+08:00
        :type StartTime: str
        :param EndTime: 结束时间，默认为当前时间，如2020-12-08T19:51:23+08:00
        :type EndTime: str
        :param GroupBys: 按指定维度groupBy
        :type GroupBys: list of str
        """
        self.Module = None
        self.Namespace = None
        self.MetricNames = None
        self.Conditions = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.GroupBys = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Namespace = params.get("Namespace")
        self.MetricNames = params.get("MetricNames")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = MidQueryCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.GroupBys = params.get("GroupBys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStatisticDataResponse(AbstractModel):
    """DescribeStatisticData返回参数结构体

    """

    def __init__(self):
        """
        :param Period: 统计周期
        :type Period: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Data: 监控数据
        :type Data: list of MetricData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Dimension(AbstractModel):
    """实例对象的维度组合

    """

    def __init__(self):
        """
        :param Name: 实例维度名称
        :type Name: str
        :param Value: 实例维度值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DimensionsDesc(AbstractModel):
    """维度信息

    """

    def __init__(self):
        """
        :param Dimensions: 维度名数组
        :type Dimensions: list of str
        """
        self.Dimensions = None


    def _deserialize(self, params):
        self.Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间，如QCE/CVM。各个云产品的详细命名空间说明请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档
        :type Namespace: str
        :param MetricName: 指标名称，如CPUUsage，仅支持单指标拉取。各个云产品的详细指标说明请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的指标英文名即为MetricName
        :type MetricName: str
        :param Instances: 实例对象的维度组合，格式为key-value键值对形式的集合。如[{"Name":"InstanceId","Value":"ins-j0hk02zo"}]。各个云产品的维度请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的维度列即为维度组合的key,value为key对应的值
        :type Instances: list of Instance
        :param Period: 监控统计周期，如60。默认为取值为300，单位为s。每个指标支持的统计周期不一定相同，各个云产品支持的统计周期请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的统计周期列即为支持的统计周期
        :type Period: int
        :param StartTime: 起始时间，如2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param EndTime: 结束时间，如2018-09-22T20:51:23+08:00，默认为当前时间。 EndTime不能小于StartTime
        :type EndTime: str
        """
        self.Namespace = None
        self.MetricName = None
        self.Instances = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData返回参数结构体

    """

    def __init__(self):
        """
        :param Period: 统计周期
        :type Period: int
        :param MetricName: 指标名
        :type MetricName: str
        :param DataPoints: 数据点数组
        :type DataPoints: list of DataPoint
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Period = None
        self.MetricName = None
        self.DataPoints = None
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.MetricName = params.get("MetricName")
        if params.get("DataPoints") is not None:
            self.DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self.DataPoints.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Instance(AbstractModel):
    """实例维度组合数组

    """

    def __init__(self):
        """
        :param Dimensions: 实例的维度组合
        :type Dimensions: list of Dimension
        """
        self.Dimensions = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceGroup(AbstractModel):
    """DescribeBasicAlarmList返回的Alarms里的InstanceGroup

    """

    def __init__(self):
        """
        :param InstanceGroupId: 实例组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupId: int
        :param InstanceGroupName: 实例组名
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupName: str
        """
        self.InstanceGroupId = None
        self.InstanceGroupName = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.InstanceGroupName = params.get("InstanceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceGroups(AbstractModel):
    """告警对象所属实例组

    """

    def __init__(self):
        """
        :param Id: 实例组 Id
        :type Id: int
        :param Name: 实例组名称
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Metric(AbstractModel):
    """指标，可用于设置告警、查询数据

    """

    def __init__(self):
        """
        :param Namespace: 告警策略类型
        :type Namespace: str
        :param MetricName: 指标名
        :type MetricName: str
        :param Description: 指标展示名
        :type Description: str
        :param Min: 最小值
        :type Min: float
        :param Max: 最大值
        :type Max: float
        :param Dimensions: 维度列表
        :type Dimensions: list of str
        :param Unit: 单位
        :type Unit: str
        :param MetricConfig: 指标配置
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricConfig: :class:`tencentcloud.monitor.v20180724.models.MetricConfig`
        """
        self.Namespace = None
        self.MetricName = None
        self.Description = None
        self.Min = None
        self.Max = None
        self.Dimensions = None
        self.Unit = None
        self.MetricConfig = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        self.Description = params.get("Description")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.Dimensions = params.get("Dimensions")
        self.Unit = params.get("Unit")
        if params.get("MetricConfig") is not None:
            self.MetricConfig = MetricConfig()
            self.MetricConfig._deserialize(params.get("MetricConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MetricConfig(AbstractModel):
    """指标配置

    """

    def __init__(self):
        """
        :param Operator: 允许使用的运算符
        :type Operator: list of str
        :param Period: 允许配置的数据周期，以秒为单位
        :type Period: list of int
        :param ContinuePeriod: 允许配置的持续周期个数
        :type ContinuePeriod: list of int
        """
        self.Operator = None
        self.Period = None
        self.ContinuePeriod = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Period = params.get("Period")
        self.ContinuePeriod = params.get("ContinuePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MetricData(AbstractModel):
    """DescribeMetricData接口出参

    """

    def __init__(self):
        """
        :param MetricName: 指标名
        :type MetricName: str
        :param Points: 监控数据点
        :type Points: list of MetricDataPoint
        """
        self.MetricName = None
        self.Points = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self.Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MetricDataPoint(AbstractModel):
    """DescribeMetricData出参

    """

    def __init__(self):
        """
        :param Dimensions: 实例对象维度组合
        :type Dimensions: list of Dimension
        :param Values: 数据点列表
        :type Values: list of Point
        """
        self.Dimensions = None
        self.Values = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = Point()
                obj._deserialize(item)
                self.Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MetricDatum(AbstractModel):
    """指标名称和值的封装

    """

    def __init__(self):
        """
        :param MetricName: 指标名称
        :type MetricName: str
        :param Value: 指标的值
        :type Value: int
        """
        self.MetricName = None
        self.Value = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MetricObjectMeaning(AbstractModel):
    """指标数据的解释

    """

    def __init__(self):
        """
        :param En: 指标英文解释
        :type En: str
        :param Zh: 指标中文解释
        :type Zh: str
        """
        self.En = None
        self.Zh = None


    def _deserialize(self, params):
        self.En = params.get("En")
        self.Zh = params.get("Zh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MetricSet(AbstractModel):
    """对业务指标的单位及支持统计周期的描述

    """

    def __init__(self):
        """
        :param Namespace: 命名空间，每个云产品会有一个命名空间
        :type Namespace: str
        :param MetricName: 指标名称
        :type MetricName: str
        :param Unit: 指标使用的单位
        :type Unit: str
        :param UnitCname: 指标使用的单位
        :type UnitCname: str
        :param Period: 指标支持的统计周期，单位是秒，如60、300
        :type Period: list of int
        :param Periods: 统计周期内指标方式
        :type Periods: list of PeriodsSt
        :param Meaning: 统计指标含义解释
        :type Meaning: :class:`tencentcloud.monitor.v20180724.models.MetricObjectMeaning`
        :param Dimensions: 维度描述信息
        :type Dimensions: list of DimensionsDesc
        """
        self.Namespace = None
        self.MetricName = None
        self.Unit = None
        self.UnitCname = None
        self.Period = None
        self.Periods = None
        self.Meaning = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        self.Unit = params.get("Unit")
        self.UnitCname = params.get("UnitCname")
        self.Period = params.get("Period")
        if params.get("Periods") is not None:
            self.Periods = []
            for item in params.get("Periods"):
                obj = PeriodsSt()
                obj._deserialize(item)
                self.Periods.append(obj)
        if params.get("Meaning") is not None:
            self.Meaning = MetricObjectMeaning()
            self.Meaning._deserialize(params.get("Meaning"))
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionsDesc()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MidQueryCondition(AbstractModel):
    """DescribeMidDimensionValueList的查询条件

    """

    def __init__(self):
        """
        :param Key: 维度
        :type Key: str
        :param Operator: 操作符，支持等于(eq)、不等于(ne)，以及in
        :type Operator: str
        :param Value: 维度值，当Op是eq、ne时，只使用第一个元素
        :type Value: list of str
        """
        self.Key = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmNoticeRequest(AbstractModel):
    """ModifyAlarmNotice请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        :param Name: 告警通知规则名称 60字符以内
        :type Name: str
        :param NoticeType: 通知类型 ALARM=未恢复通知 OK=已恢复通知 ALL=都通知
        :type NoticeType: str
        :param NoticeLanguage: 通知语言 zh-CN=中文 en-US=英文
        :type NoticeLanguage: str
        :param NoticeId: 告警通知模板 ID
        :type NoticeId: str
        :param UserNotices: 用户通知 最多5个
        :type UserNotices: list of UserNotice
        :param URLNotices: 回调通知 最多3个
        :type URLNotices: list of URLNotice
        """
        self.Module = None
        self.Name = None
        self.NoticeType = None
        self.NoticeLanguage = None
        self.NoticeId = None
        self.UserNotices = None
        self.URLNotices = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Name = params.get("Name")
        self.NoticeType = params.get("NoticeType")
        self.NoticeLanguage = params.get("NoticeLanguage")
        self.NoticeId = params.get("NoticeId")
        if params.get("UserNotices") is not None:
            self.UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self.UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self.URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self.URLNotices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmNoticeResponse(AbstractModel):
    """ModifyAlarmNotice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyConditionRequest(AbstractModel):
    """ModifyAlarmPolicyCondition请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定值 monitor
        :type Module: str
        :param PolicyId: 告警策略 ID
        :type PolicyId: str
        :param ConditionTemplateId: 触发条件模板 Id，可不传
        :type ConditionTemplateId: int
        :param Condition: 指标触发条件
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param EventCondition: 事件触发条件
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        """
        self.Module = None
        self.PolicyId = None
        self.ConditionTemplateId = None
        self.Condition = None
        self.EventCondition = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self.Condition = AlarmPolicyCondition()
            self.Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self.EventCondition = AlarmPolicyEventCondition()
            self.EventCondition._deserialize(params.get("EventCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyConditionResponse(AbstractModel):
    """ModifyAlarmPolicyCondition返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyInfoRequest(AbstractModel):
    """ModifyAlarmPolicyInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        :param PolicyId: 告警策略 ID
        :type PolicyId: str
        :param Key: 要修改的字段 NAME=策略名称 REMARK=策略备注
        :type Key: str
        :param Value: 修改后的值
        :type Value: str
        """
        self.Module = None
        self.PolicyId = None
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyInfoResponse(AbstractModel):
    """ModifyAlarmPolicyInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyNoticeRequest(AbstractModel):
    """ModifyAlarmPolicyNotice请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        :param PolicyId: 告警策略 ID
        :type PolicyId: str
        :param NoticeIds: 告警通知模板 ID 列表
        :type NoticeIds: list of str
        """
        self.Module = None
        self.PolicyId = None
        self.NoticeIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.NoticeIds = params.get("NoticeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyNoticeResponse(AbstractModel):
    """ModifyAlarmPolicyNotice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyStatusRequest(AbstractModel):
    """ModifyAlarmPolicyStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定值 monitor
        :type Module: str
        :param PolicyId: 告警策略 ID
        :type PolicyId: str
        :param Enable: 启停状态 0=停用 1=启用
        :type Enable: int
        """
        self.Module = None
        self.PolicyId = None
        self.Enable = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyStatusResponse(AbstractModel):
    """ModifyAlarmPolicyStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyTasksRequest(AbstractModel):
    """ModifyAlarmPolicyTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，这里填“monitor”
        :type Module: str
        :param PolicyId: 告警策略 ID
        :type PolicyId: str
        :param TriggerTasks: 告警策略触发任务列表，空数据代表解绑
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        """
        self.Module = None
        self.PolicyId = None
        self.TriggerTasks = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        if params.get("TriggerTasks") is not None:
            self.TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self.TriggerTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmPolicyTasksResponse(AbstractModel):
    """ModifyAlarmPolicyTasks返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmReceiversRequest(AbstractModel):
    """ModifyAlarmReceivers请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 需要修改接收人的策略组Id
        :type GroupId: int
        :param Module: 必填。固定为“monitor”
        :type Module: str
        :param ReceiverInfos: 新接收人信息, 没有填写则删除所有接收人
        :type ReceiverInfos: list of ReceiverInfo
        """
        self.GroupId = None
        self.Module = None
        self.ReceiverInfos = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Module = params.get("Module")
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = ReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAlarmReceiversResponse(AbstractModel):
    """ModifyAlarmReceivers返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPolicyGroupCondition(AbstractModel):
    """修改告警策略组传入的指标阈值条件

    """

    def __init__(self):
        """
        :param MetricId: 指标id
        :type MetricId: int
        :param CalcType: 比较类型，1表示大于，2表示大于等于，3表示小于，4表示小于等于，5表示相等，6表示不相等
        :type CalcType: int
        :param CalcValue: 检测阈值
        :type CalcValue: str
        :param CalcPeriod: 检测指标的数据周期
        :type CalcPeriod: int
        :param ContinuePeriod: 持续周期个数
        :type ContinuePeriod: int
        :param AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param RuleId: 规则id，不填表示新增，填写了ruleId表示在已存在的规则基础上进行修改
        :type RuleId: int
        """
        self.MetricId = None
        self.CalcType = None
        self.CalcValue = None
        self.CalcPeriod = None
        self.ContinuePeriod = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.MetricId = params.get("MetricId")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.CalcPeriod = params.get("CalcPeriod")
        self.ContinuePeriod = params.get("ContinuePeriod")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPolicyGroupEventCondition(AbstractModel):
    """修改告警策略组传入的事件告警条件

    """

    def __init__(self):
        """
        :param EventId: 事件id
        :type EventId: int
        :param AlarmNotifyType: 告警发送收敛类型。0连续告警，1指数告警
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: 告警发送周期单位秒。<0 不触发, 0 只触发一次, >0 每隔triggerTime秒触发一次
        :type AlarmNotifyPeriod: int
        :param RuleId: 规则id，不填表示新增，填写了ruleId表示在已存在的规则基础上进行修改
        :type RuleId: int
        """
        self.EventId = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPolicyGroupRequest(AbstractModel):
    """ModifyPolicyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param GroupId: 策略组id
        :type GroupId: int
        :param ViewName: 告警类型
        :type ViewName: str
        :param GroupName: 策略组名称
        :type GroupName: str
        :param IsUnionRule: 指标告警条件的且或关系，1表示且告警，所有指标告警条件都达到才告警，0表示或告警，任意指标告警条件达到都告警
        :type IsUnionRule: int
        :param Conditions: 指标告警条件规则，不填表示删除已有的所有指标告警条件规则
        :type Conditions: list of ModifyPolicyGroupCondition
        :param EventConditions: 事件告警条件，不填表示删除已有的事件告警条件
        :type EventConditions: list of ModifyPolicyGroupEventCondition
        :param ConditionTempGroupId: 模板策略组id
        :type ConditionTempGroupId: int
        """
        self.Module = None
        self.GroupId = None
        self.ViewName = None
        self.GroupName = None
        self.IsUnionRule = None
        self.Conditions = None
        self.EventConditions = None
        self.ConditionTempGroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.ViewName = params.get("ViewName")
        self.GroupName = params.get("GroupName")
        self.IsUnionRule = params.get("IsUnionRule")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ModifyPolicyGroupCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = ModifyPolicyGroupEventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        self.ConditionTempGroupId = params.get("ConditionTempGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPolicyGroupResponse(AbstractModel):
    """ModifyPolicyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 策略组id
        :type GroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MonitorTypeNamespace(AbstractModel):
    """策略类型

    """

    def __init__(self):
        """
        :param MonitorType: 监控类型
        :type MonitorType: str
        :param Namespace: 策略类型值
        :type Namespace: str
        """
        self.MonitorType = None
        self.Namespace = None


    def _deserialize(self, params):
        self.MonitorType = params.get("MonitorType")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PeriodsSt(AbstractModel):
    """周期内的统计方式

    """

    def __init__(self):
        """
        :param Period: 周期
        :type Period: str
        :param StatType: 统计方式
        :type StatType: list of str
        """
        self.Period = None
        self.StatType = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.StatType = params.get("StatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Point(AbstractModel):
    """监控数据点

    """

    def __init__(self):
        """
        :param Timestamp: 该监控数据点生成的时间点
        :type Timestamp: int
        :param Value: 监控数据点的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        """
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ProductSimple(AbstractModel):
    """云监控支持的产品简要信息

    """

    def __init__(self):
        """
        :param Namespace: 命名空间
        :type Namespace: str
        :param ProductName: 产品中文名称
        :type ProductName: str
        :param ProductEnName: 产品英文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductEnName: str
        """
        self.Namespace = None
        self.ProductName = None
        self.ProductEnName = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.ProductName = params.get("ProductName")
        self.ProductEnName = params.get("ProductEnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusRuleKV(AbstractModel):
    """prometheus 报警规则 KV 参数

    """

    def __init__(self):
        """
        :param Key: 键
        :type Key: str
        :param Value: 值
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusRuleSet(AbstractModel):
    """prometheus 报警规则集

    """

    def __init__(self):
        """
        :param RuleId: 规则 ID
        :type RuleId: str
        :param RuleName: 规则名称
        :type RuleName: str
        :param RuleState: 规则状态码
        :type RuleState: int
        :param Type: 规则类别
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Labels: 规则标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of PrometheusRuleKV
        :param Annotations: 规则注释列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotations: list of PrometheusRuleKV
        :param Expr: 规则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type Expr: str
        :param Duration: 规则报警持续时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param Receivers: 报警接收组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Receivers: list of str
        :param Health: 规则运行健康状态，取值如下：
<li>unknown 未知状态</li>
<li>pending 加载中</li>
<li>ok 运行正常</li>
<li>err 运行错误</li>
        :type Health: str
        :param CreatedAt: 规则创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 规则更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self.RuleId = None
        self.RuleName = None
        self.RuleState = None
        self.Type = None
        self.Labels = None
        self.Annotations = None
        self.Expr = None
        self.Duration = None
        self.Receivers = None
        self.Health = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RuleState = params.get("RuleState")
        self.Type = params.get("Type")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Annotations.append(obj)
        self.Expr = params.get("Expr")
        self.Duration = params.get("Duration")
        self.Receivers = params.get("Receivers")
        self.Health = params.get("Health")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PutMonitorDataRequest(AbstractModel):
    """PutMonitorData请求参数结构体

    """

    def __init__(self):
        """
        :param Metrics: 一组指标和数据
        :type Metrics: list of MetricDatum
        :param AnnounceIp: 上报时自行指定的 IP
        :type AnnounceIp: str
        :param AnnounceTimestamp: 上报时自行指定的时间戳
        :type AnnounceTimestamp: int
        :param AnnounceInstance: 上报时自行指定的 IP 或 产品实例ID
        :type AnnounceInstance: str
        """
        self.Metrics = None
        self.AnnounceIp = None
        self.AnnounceTimestamp = None
        self.AnnounceInstance = None


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = MetricDatum()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.AnnounceIp = params.get("AnnounceIp")
        self.AnnounceTimestamp = params.get("AnnounceTimestamp")
        self.AnnounceInstance = params.get("AnnounceInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PutMonitorDataResponse(AbstractModel):
    """PutMonitorData返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReceiverInfo(AbstractModel):
    """接收人信息

    """

    def __init__(self):
        """
        :param StartTime: 告警时间段开始时间。范围[0,86400)，作为unix时间戳转成北京时间后去掉日期，例如7200表示"10:0:0"
        :type StartTime: int
        :param EndTime: 告警时间段结束时间。含义同StartTime
        :type EndTime: int
        :param NotifyWay: 告警通知方式。可选 "SMS","SITE","EMAIL","CALL","WECHAT"
        :type NotifyWay: list of str
        :param ReceiverType: 接收人类型。“group” 或 “user”
        :type ReceiverType: str
        :param Id: ReceiverId
        :type Id: int
        :param SendFor: 电话告警通知时机。可选"OCCUR"(告警时通知),"RECOVER"(恢复时通知)
        :type SendFor: list of str
        :param UidList: 电话告警接收者uid
        :type UidList: list of int
        :param RoundNumber: 电话告警轮数
        :type RoundNumber: int
        :param PersonInterval: 电话告警对个人间隔（秒）
        :type PersonInterval: int
        :param RoundInterval: 电话告警每轮间隔（秒）
        :type RoundInterval: int
        :param RecoverNotify: 恢复通知方式。可选"SMS"
        :type RecoverNotify: list of str
        :param NeedSendNotice: 是否需要电话告警触达提示。0不需要，1需要
        :type NeedSendNotice: int
        :param ReceiverGroupList: 接收组列表。通过平台接口查询到的接收组id列表
        :type ReceiverGroupList: list of int
        :param ReceiverUserList: 接收人列表。通过平台接口查询到的接收人id列表
        :type ReceiverUserList: list of int
        :param ReceiveLanguage: 告警接收语言，枚举值（zh-CN，en-US）
        :type ReceiveLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.NotifyWay = None
        self.ReceiverType = None
        self.Id = None
        self.SendFor = None
        self.UidList = None
        self.RoundNumber = None
        self.PersonInterval = None
        self.RoundInterval = None
        self.RecoverNotify = None
        self.NeedSendNotice = None
        self.ReceiverGroupList = None
        self.ReceiverUserList = None
        self.ReceiveLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NotifyWay = params.get("NotifyWay")
        self.ReceiverType = params.get("ReceiverType")
        self.Id = params.get("Id")
        self.SendFor = params.get("SendFor")
        self.UidList = params.get("UidList")
        self.RoundNumber = params.get("RoundNumber")
        self.PersonInterval = params.get("PersonInterval")
        self.RoundInterval = params.get("RoundInterval")
        self.RecoverNotify = params.get("RecoverNotify")
        self.NeedSendNotice = params.get("NeedSendNotice")
        self.ReceiverGroupList = params.get("ReceiverGroupList")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.ReceiveLanguage = params.get("ReceiveLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendCustomAlarmMsgRequest(AbstractModel):
    """SendCustomAlarmMsg请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 接口模块名，当前取值monitor
        :type Module: str
        :param PolicyId: 消息策略ID，在云监控自定义消息页面配置
        :type PolicyId: str
        :param Msg: 用户想要发送的自定义消息内容
        :type Msg: str
        """
        self.Module = None
        self.PolicyId = None
        self.Msg = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.Msg = params.get("Msg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendCustomAlarmMsgResponse(AbstractModel):
    """SendCustomAlarmMsg返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ServiceDiscoveryItem(AbstractModel):
    """Prometheus 服务发现信息

    """

    def __init__(self):
        """
        :param Name: 服务发现名称
        :type Name: str
        :param Namespace: 服务发现属于的 Namespace
        :type Namespace: str
        :param Kind: 服务发现类型: ServiceMonitor/PodMonitor
        :type Kind: str
        :param NamespaceSelector: Namespace 选取方式
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceSelector: str
        :param Selector: Label 选取方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Selector: str
        :param Endpoints: Endpoints 信息（PodMonitor 不含该参数）
        :type Endpoints: str
        :param Yaml: 服务发现对应的配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        """
        self.Name = None
        self.Namespace = None
        self.Kind = None
        self.NamespaceSelector = None
        self.Selector = None
        self.Endpoints = None
        self.Yaml = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.Kind = params.get("Kind")
        self.NamespaceSelector = params.get("NamespaceSelector")
        self.Selector = params.get("Selector")
        self.Endpoints = params.get("Endpoints")
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetDefaultAlarmPolicyRequest(AbstractModel):
    """SetDefaultAlarmPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定值 monitor
        :type Module: str
        :param PolicyId: 告警策略 ID
        :type PolicyId: str
        """
        self.Module = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetDefaultAlarmPolicyResponse(AbstractModel):
    """SetDefaultAlarmPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TagInstance(AbstractModel):
    """策略列表详情标签返回体

    """

    def __init__(self):
        """
        :param Key: 标签Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 标签Value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param InstanceSum: 实例个数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSum: int
        :param ServiceType: 产品类型，如：cvm
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param BindingStatus: 绑定状态，2：绑定成功，1：绑定中
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingStatus: int
        :param TagStatus: 标签状态，2：标签存在，1：标签不存在
注意：此字段可能返回 null，表示取不到有效值。
        :type TagStatus: int
        """
        self.Key = None
        self.Value = None
        self.InstanceSum = None
        self.ServiceType = None
        self.RegionId = None
        self.BindingStatus = None
        self.TagStatus = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.InstanceSum = params.get("InstanceSum")
        self.ServiceType = params.get("ServiceType")
        self.RegionId = params.get("RegionId")
        self.BindingStatus = params.get("BindingStatus")
        self.TagStatus = params.get("TagStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class URLNotice(AbstractModel):
    """云监控告警通知模板 - 回调通知详情

    """

    def __init__(self):
        """
        :param URL: 回调 url（限长256字符）
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param IsValid: 是否通过验证 0=否 1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsValid: int
        :param ValidationCode: 验证码
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidationCode: str
        """
        self.URL = None
        self.IsValid = None
        self.ValidationCode = None


    def _deserialize(self, params):
        self.URL = params.get("URL")
        self.IsValid = params.get("IsValid")
        self.ValidationCode = params.get("ValidationCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UnBindingAllPolicyObjectRequest(AbstractModel):
    """UnBindingAllPolicyObject请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param GroupId: 策略组id，如传入 PolicyId 则该字段被忽略可传入任意值如 0
        :type GroupId: int
        :param PolicyId: 告警策略ID，使用此字段时 GroupId 会被忽略
        :type PolicyId: str
        """
        self.Module = None
        self.GroupId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UnBindingAllPolicyObjectResponse(AbstractModel):
    """UnBindingAllPolicyObject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UnBindingPolicyObjectRequest(AbstractModel):
    """UnBindingPolicyObject请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param GroupId: 策略组id，如传入 PolicyId 则该字段被忽略可传入任意值如 0
        :type GroupId: int
        :param UniqueId: 待删除对象实例的唯一id列表，UniqueId从调用[获取已绑定对象列表接口](https://cloud.tencent.com/document/api/248/40570)的出参的List中得到
        :type UniqueId: list of str
        :param InstanceGroupId: 实例分组id，如果按实例分组删除的话UniqueId参数是无效的
        :type InstanceGroupId: int
        :param PolicyId: 告警策略ID，使用此字段时 GroupId 会被忽略
        :type PolicyId: str
        """
        self.Module = None
        self.GroupId = None
        self.UniqueId = None
        self.InstanceGroupId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.UniqueId = params.get("UniqueId")
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UnBindingPolicyObjectResponse(AbstractModel):
    """UnBindingPolicyObject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateAlertRuleRequest(AbstractModel):
    """UpdateAlertRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: Prometheus 报警规则 ID
        :type RuleId: str
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param RuleState: 规则状态码，取值如下：
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
默认状态码为 2 启用。
        :type RuleState: int
        :param RuleName: 报警规则名称
        :type RuleName: str
        :param Expr: 报警规则表达式
        :type Expr: str
        :param Duration: 报警规则持续时间
        :type Duration: str
        :param Receivers: 报警规则接收组列表
        :type Receivers: list of str
        :param Labels: 报警规则标签列表
        :type Labels: list of PrometheusRuleKV
        :param Annotations: 报警规则注释列表
        :type Annotations: list of PrometheusRuleKV
        :param Type: 报警策略模板分类
        :type Type: str
        """
        self.RuleId = None
        self.InstanceId = None
        self.RuleState = None
        self.RuleName = None
        self.Expr = None
        self.Duration = None
        self.Receivers = None
        self.Labels = None
        self.Annotations = None
        self.Type = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.InstanceId = params.get("InstanceId")
        self.RuleState = params.get("RuleState")
        self.RuleName = params.get("RuleName")
        self.Expr = params.get("Expr")
        self.Duration = params.get("Duration")
        self.Receivers = params.get("Receivers")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Annotations.append(obj)
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateAlertRuleResponse(AbstractModel):
    """UpdateAlertRule返回参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则 ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateAlertRuleStateRequest(AbstractModel):
    """UpdateAlertRuleState请求参数结构体

    """

    def __init__(self):
        """
        :param RuleIds: 规则 ID 列表
        :type RuleIds: list of str
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param RuleState: 规则状态码，取值如下：
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
默认状态码为 2 启用。
        :type RuleState: int
        """
        self.RuleIds = None
        self.InstanceId = None
        self.RuleState = None


    def _deserialize(self, params):
        self.RuleIds = params.get("RuleIds")
        self.InstanceId = params.get("InstanceId")
        self.RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateAlertRuleStateResponse(AbstractModel):
    """UpdateAlertRuleState返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateServiceDiscoveryRequest(AbstractModel):
    """UpdateServiceDiscovery请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: Prometheus 实例 ID
        :type InstanceId: str
        :param KubeClusterId: <li>类型是 TKE，为对应的腾讯云容器服务集群 ID</li>
        :type KubeClusterId: str
        :param KubeType: 用户 Kubernetes 集群类型：
<li> 1 = 容器服务集群(TKE) </li>
        :type KubeType: int
        :param Type: 服务发现类型，取值如下：
<li> 1 = ServiceMonitor</li>
<li> 2 = PodMonitor</li>
<li> 3 = JobMonitor</li>
        :type Type: int
        :param Yaml: 服务发现配置信息
        :type Yaml: str
        """
        self.InstanceId = None
        self.KubeClusterId = None
        self.KubeType = None
        self.Type = None
        self.Yaml = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeClusterId = params.get("KubeClusterId")
        self.KubeType = params.get("KubeType")
        self.Type = params.get("Type")
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateServiceDiscoveryResponse(AbstractModel):
    """UpdateServiceDiscovery返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceDiscovery: 更新成功之后，返回对应服务发现的信息
        :type ServiceDiscovery: :class:`tencentcloud.monitor.v20180724.models.ServiceDiscoveryItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceDiscovery = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceDiscovery") is not None:
            self.ServiceDiscovery = ServiceDiscoveryItem()
            self.ServiceDiscovery._deserialize(params.get("ServiceDiscovery"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UserNotice(AbstractModel):
    """云监控告警通知模板 - 用户通知详情

    """

    def __init__(self):
        """
        :param ReceiverType: 接收者类型 USER=用户 GROUP=用户组
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverType: str
        :param StartTime: 通知开始时间 00:00:00 开始的秒数（取值范围0-86399）
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param EndTime: 通知结束时间 00:00:00 开始的秒数（取值范围0-86399）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param NoticeWay: 通知渠道列表 EMAIL=邮件 SMS=短信 CALL=电话 WECHAT=微信
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeWay: list of str
        :param UserIds: 用户 uid 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIds: list of int
        :param GroupIds: 用户组 group id 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupIds: list of int
        :param PhoneOrder: 电话轮询列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneOrder: list of int
        :param PhoneCircleTimes: 电话轮询次数 （取值范围1-5）
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCircleTimes: int
        :param PhoneInnerInterval: 单次轮询内拨打间隔 秒数 （取值范围60-900）
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneInnerInterval: int
        :param PhoneCircleInterval: 两次轮询间隔 秒数（取值范围60-900）
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCircleInterval: int
        :param NeedPhoneArriveNotice: 是否需要触达通知 0=否 1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type NeedPhoneArriveNotice: int
        """
        self.ReceiverType = None
        self.StartTime = None
        self.EndTime = None
        self.NoticeWay = None
        self.UserIds = None
        self.GroupIds = None
        self.PhoneOrder = None
        self.PhoneCircleTimes = None
        self.PhoneInnerInterval = None
        self.PhoneCircleInterval = None
        self.NeedPhoneArriveNotice = None


    def _deserialize(self, params):
        self.ReceiverType = params.get("ReceiverType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NoticeWay = params.get("NoticeWay")
        self.UserIds = params.get("UserIds")
        self.GroupIds = params.get("GroupIds")
        self.PhoneOrder = params.get("PhoneOrder")
        self.PhoneCircleTimes = params.get("PhoneCircleTimes")
        self.PhoneInnerInterval = params.get("PhoneInnerInterval")
        self.PhoneCircleInterval = params.get("PhoneCircleInterval")
        self.NeedPhoneArriveNotice = params.get("NeedPhoneArriveNotice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        