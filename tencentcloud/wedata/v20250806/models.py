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


class AlarmGroup(AbstractModel):
    r"""告警规则接收人配置

    """

    def __init__(self):
        r"""
        :param _AlarmEscalationRecipientIds: 告警升级人ID列表
若告警接收人或上级升级人未在告警间隔时间内确认告警，则会发送告警给下一级升级人。
        :type AlarmEscalationRecipientIds: list of str
        :param _AlarmEscalationInterval: 告警升级间隔
        :type AlarmEscalationInterval: int
        :param _NotificationFatigue: 告警通知疲劳配置
        :type NotificationFatigue: :class:`tencentcloud.wedata.v20250806.models.NotificationFatigue`
        :param _AlarmWays: 告警渠道 1.邮件，2.短信，3.微信，4.语音，5.企业微信，6.Http，7.企业微信群 8 飞书群 9 钉钉群 10 Slack群 11 Teams群（默认1.邮件） 7.企业微信群 8 飞书群 9 钉钉群 10 Slack群 11 Teams群 只能选择一个渠道
        :type AlarmWays: list of str
        :param _WebHooks: 企业微信群/飞书群/钉钉群 /Slack群/Teams群的webhook地址列表
        :type WebHooks: list of AlarmWayWebHook
        :param _AlarmRecipientType: 告警接收人类型：1.指定人员，2.任务责任人，3.值班表（默认1.指定人员）
        :type AlarmRecipientType: int
        :param _AlarmRecipientIds: 根据AlarmRecipientType的类型该列表具有不同的业务id 1（指定人员）: 告警接收人id列表 2（任务责任人）：无需配置 3（值班表）：值班表id列表
        :type AlarmRecipientIds: list of str
        """
        self._AlarmEscalationRecipientIds = None
        self._AlarmEscalationInterval = None
        self._NotificationFatigue = None
        self._AlarmWays = None
        self._WebHooks = None
        self._AlarmRecipientType = None
        self._AlarmRecipientIds = None

    @property
    def AlarmEscalationRecipientIds(self):
        r"""告警升级人ID列表
若告警接收人或上级升级人未在告警间隔时间内确认告警，则会发送告警给下一级升级人。
        :rtype: list of str
        """
        return self._AlarmEscalationRecipientIds

    @AlarmEscalationRecipientIds.setter
    def AlarmEscalationRecipientIds(self, AlarmEscalationRecipientIds):
        self._AlarmEscalationRecipientIds = AlarmEscalationRecipientIds

    @property
    def AlarmEscalationInterval(self):
        r"""告警升级间隔
        :rtype: int
        """
        return self._AlarmEscalationInterval

    @AlarmEscalationInterval.setter
    def AlarmEscalationInterval(self, AlarmEscalationInterval):
        self._AlarmEscalationInterval = AlarmEscalationInterval

    @property
    def NotificationFatigue(self):
        r"""告警通知疲劳配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.NotificationFatigue`
        """
        return self._NotificationFatigue

    @NotificationFatigue.setter
    def NotificationFatigue(self, NotificationFatigue):
        self._NotificationFatigue = NotificationFatigue

    @property
    def AlarmWays(self):
        r"""告警渠道 1.邮件，2.短信，3.微信，4.语音，5.企业微信，6.Http，7.企业微信群 8 飞书群 9 钉钉群 10 Slack群 11 Teams群（默认1.邮件） 7.企业微信群 8 飞书群 9 钉钉群 10 Slack群 11 Teams群 只能选择一个渠道
        :rtype: list of str
        """
        return self._AlarmWays

    @AlarmWays.setter
    def AlarmWays(self, AlarmWays):
        self._AlarmWays = AlarmWays

    @property
    def WebHooks(self):
        r"""企业微信群/飞书群/钉钉群 /Slack群/Teams群的webhook地址列表
        :rtype: list of AlarmWayWebHook
        """
        return self._WebHooks

    @WebHooks.setter
    def WebHooks(self, WebHooks):
        self._WebHooks = WebHooks

    @property
    def AlarmRecipientType(self):
        r"""告警接收人类型：1.指定人员，2.任务责任人，3.值班表（默认1.指定人员）
        :rtype: int
        """
        return self._AlarmRecipientType

    @AlarmRecipientType.setter
    def AlarmRecipientType(self, AlarmRecipientType):
        self._AlarmRecipientType = AlarmRecipientType

    @property
    def AlarmRecipientIds(self):
        r"""根据AlarmRecipientType的类型该列表具有不同的业务id 1（指定人员）: 告警接收人id列表 2（任务责任人）：无需配置 3（值班表）：值班表id列表
        :rtype: list of str
        """
        return self._AlarmRecipientIds

    @AlarmRecipientIds.setter
    def AlarmRecipientIds(self, AlarmRecipientIds):
        self._AlarmRecipientIds = AlarmRecipientIds


    def _deserialize(self, params):
        self._AlarmEscalationRecipientIds = params.get("AlarmEscalationRecipientIds")
        self._AlarmEscalationInterval = params.get("AlarmEscalationInterval")
        if params.get("NotificationFatigue") is not None:
            self._NotificationFatigue = NotificationFatigue()
            self._NotificationFatigue._deserialize(params.get("NotificationFatigue"))
        self._AlarmWays = params.get("AlarmWays")
        if params.get("WebHooks") is not None:
            self._WebHooks = []
            for item in params.get("WebHooks"):
                obj = AlarmWayWebHook()
                obj._deserialize(item)
                self._WebHooks.append(obj)
        self._AlarmRecipientType = params.get("AlarmRecipientType")
        self._AlarmRecipientIds = params.get("AlarmRecipientIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmMessage(AbstractModel):
    r"""告警信息

    """

    def __init__(self):
        r"""
        :param _AlarmMessageId: 告警消息Id
        :type AlarmMessageId: int
        :param _AlarmTime: 告警时间，同一条告警可能发送多次，只显示最新的告警时间
        :type AlarmTime: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _CurRunDate: 任务的实例数据时间
        :type CurRunDate: str
        :param _AlarmReason: 告警原因
        :type AlarmReason: str
        :param _AlarmLevel: 告警级别，1.普通， 2.重要，3.紧急
        :type AlarmLevel: int
        :param _AlarmRuleId: 告警规则Id
        :type AlarmRuleId: str
        :param _AlarmWays: 告警渠道 1.邮件，2.短信，3.微信，4.语音，5.企业微信，6.Http，7.企业微信群， 8.飞书群，9.钉钉群，10.Slack群,11.Teams群（默认1.邮件），7.企业微信群，8.飞书群，9.钉钉群，10.Slack群，11.Teams群 
        :type AlarmWays: list of str
        :param _AlarmRecipients: 告警接收人
        :type AlarmRecipients: list of str
        """
        self._AlarmMessageId = None
        self._AlarmTime = None
        self._TaskName = None
        self._TaskId = None
        self._CurRunDate = None
        self._AlarmReason = None
        self._AlarmLevel = None
        self._AlarmRuleId = None
        self._AlarmWays = None
        self._AlarmRecipients = None

    @property
    def AlarmMessageId(self):
        r"""告警消息Id
        :rtype: int
        """
        return self._AlarmMessageId

    @AlarmMessageId.setter
    def AlarmMessageId(self, AlarmMessageId):
        self._AlarmMessageId = AlarmMessageId

    @property
    def AlarmTime(self):
        r"""告警时间，同一条告警可能发送多次，只显示最新的告警时间
        :rtype: str
        """
        return self._AlarmTime

    @AlarmTime.setter
    def AlarmTime(self, AlarmTime):
        self._AlarmTime = AlarmTime

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CurRunDate(self):
        r"""任务的实例数据时间
        :rtype: str
        """
        return self._CurRunDate

    @CurRunDate.setter
    def CurRunDate(self, CurRunDate):
        self._CurRunDate = CurRunDate

    @property
    def AlarmReason(self):
        r"""告警原因
        :rtype: str
        """
        return self._AlarmReason

    @AlarmReason.setter
    def AlarmReason(self, AlarmReason):
        self._AlarmReason = AlarmReason

    @property
    def AlarmLevel(self):
        r"""告警级别，1.普通， 2.重要，3.紧急
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmRuleId(self):
        r"""告警规则Id
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId

    @property
    def AlarmWays(self):
        r"""告警渠道 1.邮件，2.短信，3.微信，4.语音，5.企业微信，6.Http，7.企业微信群， 8.飞书群，9.钉钉群，10.Slack群,11.Teams群（默认1.邮件），7.企业微信群，8.飞书群，9.钉钉群，10.Slack群，11.Teams群 
        :rtype: list of str
        """
        return self._AlarmWays

    @AlarmWays.setter
    def AlarmWays(self, AlarmWays):
        self._AlarmWays = AlarmWays

    @property
    def AlarmRecipients(self):
        r"""告警接收人
        :rtype: list of str
        """
        return self._AlarmRecipients

    @AlarmRecipients.setter
    def AlarmRecipients(self, AlarmRecipients):
        self._AlarmRecipients = AlarmRecipients


    def _deserialize(self, params):
        self._AlarmMessageId = params.get("AlarmMessageId")
        self._AlarmTime = params.get("AlarmTime")
        self._TaskName = params.get("TaskName")
        self._TaskId = params.get("TaskId")
        self._CurRunDate = params.get("CurRunDate")
        self._AlarmReason = params.get("AlarmReason")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmRuleId = params.get("AlarmRuleId")
        self._AlarmWays = params.get("AlarmWays")
        self._AlarmRecipients = params.get("AlarmRecipients")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmQuietInterval(AbstractModel):
    r"""告警免打扰时间区间

    """

    def __init__(self):
        r"""
        :param _DaysOfWeek: ISO标准，1表示周一，7表示周日。
        :type DaysOfWeek: list of int non-negative
        :param _StartTime: 开始时间，精度时分秒，格式 HH:mm:ss
        :type StartTime: str
        :param _EndTime: 结束时间，精度时分秒，格式 HH:mm:ss
        :type EndTime: str
        """
        self._DaysOfWeek = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DaysOfWeek(self):
        r"""ISO标准，1表示周一，7表示周日。
        :rtype: list of int non-negative
        """
        return self._DaysOfWeek

    @DaysOfWeek.setter
    def DaysOfWeek(self, DaysOfWeek):
        self._DaysOfWeek = DaysOfWeek

    @property
    def StartTime(self):
        r"""开始时间，精度时分秒，格式 HH:mm:ss
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，精度时分秒，格式 HH:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DaysOfWeek = params.get("DaysOfWeek")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmRuleData(AbstractModel):
    r"""告警规则详情

    """

    def __init__(self):
        r"""
        :param _AlarmRuleId: 告警规则id
        :type AlarmRuleId: str
        :param _AlarmRuleName: 告警规则名称
        :type AlarmRuleName: str
        :param _Description: 告警规则描述
        :type Description: str
        :param _MonitorObjectType: 监控对象类型,
任务维度监控： 可按照任务/工作流/项目来配置：1.任务、2.工作流、3.项目（默认为1.任务） 
项目维度监控： 项目整体任务波动告警， 7：项目波动监控告警
        :type MonitorObjectType: int
        :param _MonitorObjectIds: 根据MonitorType 的设置传入不同的业务id，如下1（任务）： MonitorObjectIds为任务id列表2（工作流）： MonitorObjectIds 为工作流id列表(工作流id可从接口ListWorkflows获取)3（项目）： MonitorObjectIds为项目id列表
        :type MonitorObjectIds: list of str
        :param _AlarmTypes: 告警规则监控类型
failure：失败告警 ；overtime：超时告警 success：成功告警; backTrackingOrRerunSuccess: 补录重跑成功告警 backTrackingOrRerunFailure：补录重跑失败告警；
项目波动告警
projectFailureInstanceUpwardFluctuationAlarm： 当天失败实例数向上波动率超过阀值告警；
projectSuccessInstanceDownwardFluctuationAlarm：当天成功实例数向下波动率超过阀值告警；

离线集成任务对账告警：
reconciliationFailure： 离线对账任务失败告警
reconciliationOvertime： 离线对账任务运行超时告警
reconciliationMismatch： 数据对账任务不一致条数超过阀值告警

        :type AlarmTypes: list of str
        :param _Status: 告警规则是否启用
0-- 禁用 1--启用
        :type Status: int
        :param _AlarmRuleDetail: 告警规则配置信息 成功告警无需配置；失败告警可以配置首次失败告警或者所有重试失败告警；超时配置需要配置超时类型及超时阀值；项目波动告警需要配置波动率及防抖周期配置
        :type AlarmRuleDetail: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        :param _AlarmLevel: 告警级别 1.普通、2.重要、3.紧急
        :type AlarmLevel: int
        :param _OwnerUin: 告警规则创建人uid
        :type OwnerUin: str
        :param _BundleId: bundle 客户端绑定的告警规则:  为空是正常的告警规则，不为空则是对应bundle客户端绑定的规则
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _BundleInfo: bundleId不为空 则表示绑定的bundle客户端名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleInfo: str
        :param _AlarmGroups: 告警接收人配置列表
        :type AlarmGroups: list of AlarmGroup
        """
        self._AlarmRuleId = None
        self._AlarmRuleName = None
        self._Description = None
        self._MonitorObjectType = None
        self._MonitorObjectIds = None
        self._AlarmTypes = None
        self._Status = None
        self._AlarmRuleDetail = None
        self._AlarmLevel = None
        self._OwnerUin = None
        self._BundleId = None
        self._BundleInfo = None
        self._AlarmGroups = None

    @property
    def AlarmRuleId(self):
        r"""告警规则id
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId

    @property
    def AlarmRuleName(self):
        r"""告警规则名称
        :rtype: str
        """
        return self._AlarmRuleName

    @AlarmRuleName.setter
    def AlarmRuleName(self, AlarmRuleName):
        self._AlarmRuleName = AlarmRuleName

    @property
    def Description(self):
        r"""告警规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MonitorObjectType(self):
        r"""监控对象类型,
任务维度监控： 可按照任务/工作流/项目来配置：1.任务、2.工作流、3.项目（默认为1.任务） 
项目维度监控： 项目整体任务波动告警， 7：项目波动监控告警
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def MonitorObjectIds(self):
        r"""根据MonitorType 的设置传入不同的业务id，如下1（任务）： MonitorObjectIds为任务id列表2（工作流）： MonitorObjectIds 为工作流id列表(工作流id可从接口ListWorkflows获取)3（项目）： MonitorObjectIds为项目id列表
        :rtype: list of str
        """
        return self._MonitorObjectIds

    @MonitorObjectIds.setter
    def MonitorObjectIds(self, MonitorObjectIds):
        self._MonitorObjectIds = MonitorObjectIds

    @property
    def AlarmTypes(self):
        r"""告警规则监控类型
failure：失败告警 ；overtime：超时告警 success：成功告警; backTrackingOrRerunSuccess: 补录重跑成功告警 backTrackingOrRerunFailure：补录重跑失败告警；
项目波动告警
projectFailureInstanceUpwardFluctuationAlarm： 当天失败实例数向上波动率超过阀值告警；
projectSuccessInstanceDownwardFluctuationAlarm：当天成功实例数向下波动率超过阀值告警；

离线集成任务对账告警：
reconciliationFailure： 离线对账任务失败告警
reconciliationOvertime： 离线对账任务运行超时告警
reconciliationMismatch： 数据对账任务不一致条数超过阀值告警

        :rtype: list of str
        """
        return self._AlarmTypes

    @AlarmTypes.setter
    def AlarmTypes(self, AlarmTypes):
        self._AlarmTypes = AlarmTypes

    @property
    def Status(self):
        r"""告警规则是否启用
0-- 禁用 1--启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmRuleDetail(self):
        r"""告警规则配置信息 成功告警无需配置；失败告警可以配置首次失败告警或者所有重试失败告警；超时配置需要配置超时类型及超时阀值；项目波动告警需要配置波动率及防抖周期配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        """
        return self._AlarmRuleDetail

    @AlarmRuleDetail.setter
    def AlarmRuleDetail(self, AlarmRuleDetail):
        self._AlarmRuleDetail = AlarmRuleDetail

    @property
    def AlarmLevel(self):
        r"""告警级别 1.普通、2.重要、3.紧急
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def OwnerUin(self):
        r"""告警规则创建人uid
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def BundleId(self):
        r"""bundle 客户端绑定的告警规则:  为空是正常的告警规则，不为空则是对应bundle客户端绑定的规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""bundleId不为空 则表示绑定的bundle客户端名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def AlarmGroups(self):
        r"""告警接收人配置列表
        :rtype: list of AlarmGroup
        """
        return self._AlarmGroups

    @AlarmGroups.setter
    def AlarmGroups(self, AlarmGroups):
        self._AlarmGroups = AlarmGroups


    def _deserialize(self, params):
        self._AlarmRuleId = params.get("AlarmRuleId")
        self._AlarmRuleName = params.get("AlarmRuleName")
        self._Description = params.get("Description")
        self._MonitorObjectType = params.get("MonitorObjectType")
        self._MonitorObjectIds = params.get("MonitorObjectIds")
        self._AlarmTypes = params.get("AlarmTypes")
        self._Status = params.get("Status")
        if params.get("AlarmRuleDetail") is not None:
            self._AlarmRuleDetail = AlarmRuleDetail()
            self._AlarmRuleDetail._deserialize(params.get("AlarmRuleDetail"))
        self._AlarmLevel = params.get("AlarmLevel")
        self._OwnerUin = params.get("OwnerUin")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        if params.get("AlarmGroups") is not None:
            self._AlarmGroups = []
            for item in params.get("AlarmGroups"):
                obj = AlarmGroup()
                obj._deserialize(item)
                self._AlarmGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmRuleDetail(AbstractModel):
    r"""告警规则详细配置

    """

    def __init__(self):
        r"""
        :param _Trigger: 失败触发时机 

1 – 首次失败触发
2 --所有重试完成触发 (默认)
注意：此字段可能返回 null，表示取不到有效值。
        :type Trigger: int
        :param _DataBackfillOrRerunTrigger: 补录重跑触发时机

1 –  首次失败触发
2 – 所有重试完成触发
注意：此字段可能返回 null，表示取不到有效值。
        :type DataBackfillOrRerunTrigger: int
        :param _TimeOutExtInfo: 周期实例超时配置明细
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOutExtInfo: list of TimeOutStrategyInfo
        :param _DataBackfillOrRerunTimeOutExtInfo: 重跑补录实例超时配置明细
注意：此字段可能返回 null，表示取不到有效值。
        :type DataBackfillOrRerunTimeOutExtInfo: list of TimeOutStrategyInfo
        :param _ProjectInstanceStatisticsAlarmInfoList: 项目波动告警配置明细
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectInstanceStatisticsAlarmInfoList: list of ProjectInstanceStatisticsAlarmInfo
        :param _ReconciliationExtInfo: 离线集成对账告警配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReconciliationExtInfo: list of ReconciliationStrategyInfo
        """
        self._Trigger = None
        self._DataBackfillOrRerunTrigger = None
        self._TimeOutExtInfo = None
        self._DataBackfillOrRerunTimeOutExtInfo = None
        self._ProjectInstanceStatisticsAlarmInfoList = None
        self._ReconciliationExtInfo = None

    @property
    def Trigger(self):
        r"""失败触发时机 

1 – 首次失败触发
2 --所有重试完成触发 (默认)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def DataBackfillOrRerunTrigger(self):
        r"""补录重跑触发时机

1 –  首次失败触发
2 – 所有重试完成触发
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DataBackfillOrRerunTrigger

    @DataBackfillOrRerunTrigger.setter
    def DataBackfillOrRerunTrigger(self, DataBackfillOrRerunTrigger):
        self._DataBackfillOrRerunTrigger = DataBackfillOrRerunTrigger

    @property
    def TimeOutExtInfo(self):
        r"""周期实例超时配置明细
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TimeOutStrategyInfo
        """
        return self._TimeOutExtInfo

    @TimeOutExtInfo.setter
    def TimeOutExtInfo(self, TimeOutExtInfo):
        self._TimeOutExtInfo = TimeOutExtInfo

    @property
    def DataBackfillOrRerunTimeOutExtInfo(self):
        r"""重跑补录实例超时配置明细
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TimeOutStrategyInfo
        """
        return self._DataBackfillOrRerunTimeOutExtInfo

    @DataBackfillOrRerunTimeOutExtInfo.setter
    def DataBackfillOrRerunTimeOutExtInfo(self, DataBackfillOrRerunTimeOutExtInfo):
        self._DataBackfillOrRerunTimeOutExtInfo = DataBackfillOrRerunTimeOutExtInfo

    @property
    def ProjectInstanceStatisticsAlarmInfoList(self):
        r"""项目波动告警配置明细
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProjectInstanceStatisticsAlarmInfo
        """
        return self._ProjectInstanceStatisticsAlarmInfoList

    @ProjectInstanceStatisticsAlarmInfoList.setter
    def ProjectInstanceStatisticsAlarmInfoList(self, ProjectInstanceStatisticsAlarmInfoList):
        self._ProjectInstanceStatisticsAlarmInfoList = ProjectInstanceStatisticsAlarmInfoList

    @property
    def ReconciliationExtInfo(self):
        r"""离线集成对账告警配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ReconciliationStrategyInfo
        """
        return self._ReconciliationExtInfo

    @ReconciliationExtInfo.setter
    def ReconciliationExtInfo(self, ReconciliationExtInfo):
        self._ReconciliationExtInfo = ReconciliationExtInfo


    def _deserialize(self, params):
        self._Trigger = params.get("Trigger")
        self._DataBackfillOrRerunTrigger = params.get("DataBackfillOrRerunTrigger")
        if params.get("TimeOutExtInfo") is not None:
            self._TimeOutExtInfo = []
            for item in params.get("TimeOutExtInfo"):
                obj = TimeOutStrategyInfo()
                obj._deserialize(item)
                self._TimeOutExtInfo.append(obj)
        if params.get("DataBackfillOrRerunTimeOutExtInfo") is not None:
            self._DataBackfillOrRerunTimeOutExtInfo = []
            for item in params.get("DataBackfillOrRerunTimeOutExtInfo"):
                obj = TimeOutStrategyInfo()
                obj._deserialize(item)
                self._DataBackfillOrRerunTimeOutExtInfo.append(obj)
        if params.get("ProjectInstanceStatisticsAlarmInfoList") is not None:
            self._ProjectInstanceStatisticsAlarmInfoList = []
            for item in params.get("ProjectInstanceStatisticsAlarmInfoList"):
                obj = ProjectInstanceStatisticsAlarmInfo()
                obj._deserialize(item)
                self._ProjectInstanceStatisticsAlarmInfoList.append(obj)
        if params.get("ReconciliationExtInfo") is not None:
            self._ReconciliationExtInfo = []
            for item in params.get("ReconciliationExtInfo"):
                obj = ReconciliationStrategyInfo()
                obj._deserialize(item)
                self._ReconciliationExtInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmWayWebHook(AbstractModel):
    r"""告警渠道 企业微信群/钉钉群/飞书群 等webhook地址配置

    """

    def __init__(self):
        r"""
        :param _AlarmWay: 告警渠道值
7.企业微信群,8 飞书群 9 钉钉群 10 Slack群 11 Teams群
        :type AlarmWay: str
        :param _WebHooks: 告警群的webhook地址列表
        :type WebHooks: list of str
        """
        self._AlarmWay = None
        self._WebHooks = None

    @property
    def AlarmWay(self):
        r"""告警渠道值
7.企业微信群,8 飞书群 9 钉钉群 10 Slack群 11 Teams群
        :rtype: str
        """
        return self._AlarmWay

    @AlarmWay.setter
    def AlarmWay(self, AlarmWay):
        self._AlarmWay = AlarmWay

    @property
    def WebHooks(self):
        r"""告警群的webhook地址列表
        :rtype: list of str
        """
        return self._WebHooks

    @WebHooks.setter
    def WebHooks(self, WebHooks):
        self._WebHooks = WebHooks


    def _deserialize(self, params):
        self._AlarmWay = params.get("AlarmWay")
        self._WebHooks = params.get("WebHooks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackfillInstance(AbstractModel):
    r"""单次补录实例详情

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _CurRunDate: 实例数据时间
        :type CurRunDate: str
        :param _State: 执行状态
        :type State: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CostTime: 执行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: str
        """
        self._TaskName = None
        self._TaskId = None
        self._CurRunDate = None
        self._State = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CurRunDate(self):
        r"""实例数据时间
        :rtype: str
        """
        return self._CurRunDate

    @CurRunDate.setter
    def CurRunDate(self, CurRunDate):
        self._CurRunDate = CurRunDate

    @property
    def State(self):
        r"""执行状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def StartTime(self):
        r"""开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CostTime(self):
        r"""执行时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskId = params.get("TaskId")
        self._CurRunDate = params.get("CurRunDate")
        self._State = params.get("State")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackfillInstanceCollection(AbstractModel):
    r"""补录计划的所有实例

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页页码
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _Items: 补录实例列表
        :type Items: list of BackfillInstance
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPageNumber = None
        self._TotalCount = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""分页页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def TotalCount(self):
        r"""记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""补录实例列表
        :rtype: list of BackfillInstance
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackfillInstance()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChildDependencyConfigPage(AbstractModel):
    r"""任务下游依赖详情分页

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _PageNumber: 页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _Items: 分页数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OpsTaskDepend
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._Items = None

    @property
    def TotalCount(self):
        r"""结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Items(self):
        r"""分页数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OpsTaskDepend
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OpsTaskDepend()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeFile(AbstractModel):
    r"""数据探索脚本业务处理实体

    """

    def __init__(self):
        r"""
        :param _CodeFileId: 脚本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeFileId: str
        :param _CodeFileName: 脚本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeFileName: str
        :param _OwnerUin: 脚本所有者 uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _CodeFileConfig: 脚本配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeFileConfig: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        :param _CodeFileContent: 脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeFileContent: str
        :param _UpdateUserUin: 最近一次操作人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserUin: str
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _UpdateTime: 更新时间 yyyy-MM-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _CreateTime: 创建时间 yyyy-MM-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _AccessScope: 权限范围：SHARED, PRIVATE
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessScope: str
        :param _Path: 节点全路径，/aaa/bbb/ccc.ipynb，由各个节点的名称组成
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
        self._CodeFileId = None
        self._CodeFileName = None
        self._OwnerUin = None
        self._CodeFileConfig = None
        self._CodeFileContent = None
        self._UpdateUserUin = None
        self._ProjectId = None
        self._UpdateTime = None
        self._CreateTime = None
        self._AccessScope = None
        self._Path = None

    @property
    def CodeFileId(self):
        r"""脚本ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId

    @property
    def CodeFileName(self):
        r"""脚本名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CodeFileName

    @CodeFileName.setter
    def CodeFileName(self, CodeFileName):
        self._CodeFileName = CodeFileName

    @property
    def OwnerUin(self):
        r"""脚本所有者 uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CodeFileConfig(self):
        r"""脚本配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        """
        return self._CodeFileConfig

    @CodeFileConfig.setter
    def CodeFileConfig(self, CodeFileConfig):
        self._CodeFileConfig = CodeFileConfig

    @property
    def CodeFileContent(self):
        r"""脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CodeFileContent

    @CodeFileContent.setter
    def CodeFileContent(self, CodeFileContent):
        self._CodeFileContent = CodeFileContent

    @property
    def UpdateUserUin(self):
        r"""最近一次操作人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def ProjectId(self):
        r"""项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UpdateTime(self):
        r"""更新时间 yyyy-MM-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        r"""创建时间 yyyy-MM-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AccessScope(self):
        r"""权限范围：SHARED, PRIVATE
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def Path(self):
        r"""节点全路径，/aaa/bbb/ccc.ipynb，由各个节点的名称组成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._CodeFileId = params.get("CodeFileId")
        self._CodeFileName = params.get("CodeFileName")
        self._OwnerUin = params.get("OwnerUin")
        if params.get("CodeFileConfig") is not None:
            self._CodeFileConfig = CodeFileConfig()
            self._CodeFileConfig._deserialize(params.get("CodeFileConfig"))
        self._CodeFileContent = params.get("CodeFileContent")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._ProjectId = params.get("ProjectId")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._AccessScope = params.get("AccessScope")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeFileConfig(AbstractModel):
    r"""数据探索脚本配置

    """

    def __init__(self):
        r"""
        :param _Params: 高级运行参数,变量替换，map-json String,String
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: str
        :param _NotebookSessionInfo: notebook kernel session信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookSessionInfo: :class:`tencentcloud.wedata.v20250806.models.NotebookSessionInfo`
        """
        self._Params = None
        self._NotebookSessionInfo = None

    @property
    def Params(self):
        r"""高级运行参数,变量替换，map-json String,String
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def NotebookSessionInfo(self):
        r"""notebook kernel session信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.NotebookSessionInfo`
        """
        return self._NotebookSessionInfo

    @NotebookSessionInfo.setter
    def NotebookSessionInfo(self, NotebookSessionInfo):
        self._NotebookSessionInfo = NotebookSessionInfo


    def _deserialize(self, params):
        self._Params = params.get("Params")
        if params.get("NotebookSessionInfo") is not None:
            self._NotebookSessionInfo = NotebookSessionInfo()
            self._NotebookSessionInfo._deserialize(params.get("NotebookSessionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeFolderNode(AbstractModel):
    r"""数据探索脚本文件树节点

    """

    def __init__(self):
        r"""
        :param _Id: 唯一标识
        :type Id: str
        :param _Title: 名称
        :type Title: str
        :param _Type: 类型 folder，script
        :type Type: str
        :param _IsLeaf: 是否叶子节点
        :type IsLeaf: bool
        :param _Params: 业务参数	
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: str
        :param _AccessScope: 权限范围: SHARED, PRIVATE
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessScope: str
        :param _Path: 节点路径
        :type Path: str
        :param _OwnerUin: 目录/文件责任人uin
        :type OwnerUin: str
        :param _CreateUserUin: 创建人
        :type CreateUserUin: str
        :param _NodePermission: 当前用户对节点拥有的权限	
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePermission: str
        :param _Children: 子节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of CodeFolderNode
        """
        self._Id = None
        self._Title = None
        self._Type = None
        self._IsLeaf = None
        self._Params = None
        self._AccessScope = None
        self._Path = None
        self._OwnerUin = None
        self._CreateUserUin = None
        self._NodePermission = None
        self._Children = None

    @property
    def Id(self):
        r"""唯一标识
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Title(self):
        r"""名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Type(self):
        r"""类型 folder，script
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsLeaf(self):
        r"""是否叶子节点
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf

    @property
    def Params(self):
        r"""业务参数	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def AccessScope(self):
        r"""权限范围: SHARED, PRIVATE
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def Path(self):
        r"""节点路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def OwnerUin(self):
        r"""目录/文件责任人uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateUserUin(self):
        r"""创建人
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def NodePermission(self):
        r"""当前用户对节点拥有的权限	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodePermission

    @NodePermission.setter
    def NodePermission(self, NodePermission):
        self._NodePermission = NodePermission

    @property
    def Children(self):
        r"""子节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CodeFolderNode
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Title = params.get("Title")
        self._Type = params.get("Type")
        self._IsLeaf = params.get("IsLeaf")
        self._Params = params.get("Params")
        self._AccessScope = params.get("AccessScope")
        self._Path = params.get("Path")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateUserUin = params.get("CreateUserUin")
        self._NodePermission = params.get("NodePermission")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = CodeFolderNode()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeStudioFileActionResult(AbstractModel):
    r"""CodeStudio文件对象操作结果

    """

    def __init__(self):
        r"""
        :param _Status: 成功true，失败false
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        :param _CodeFileId: 文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeFileId: str
        """
        self._Status = None
        self._CodeFileId = None

    @property
    def Status(self):
        r"""成功true，失败false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CodeFileId(self):
        r"""文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CodeFileId = params.get("CodeFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeStudioFolderActionResult(AbstractModel):
    r"""CodeStudio文件夹对象操作结果

    """

    def __init__(self):
        r"""
        :param _Status: 成功true，失败false
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        :param _FolderId: 文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        """
        self._Status = None
        self._FolderId = None

    @property
    def Status(self):
        r"""成功true，失败false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FolderId(self):
        r"""文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeStudioFolderResult(AbstractModel):
    r"""CodeStudio文件夹对象操作结果

    """

    def __init__(self):
        r"""
        :param _FolderId: 文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        """
        self._FolderId = None

    @property
    def FolderId(self):
        r"""文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmRuleData(AbstractModel):
    r"""创建告警规则响应结果

    """

    def __init__(self):
        r"""
        :param _AlarmRuleId: 告警规则唯一id
        :type AlarmRuleId: str
        """
        self._AlarmRuleId = None

    @property
    def AlarmRuleId(self):
        r"""告警规则唯一id
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId


    def _deserialize(self, params):
        self._AlarmRuleId = params.get("AlarmRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeFileRequest(AbstractModel):
    r"""CreateCodeFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _CodeFileName: 代码文件名称
        :type CodeFileName: str
        :param _ParentFolderPath: 父文件夹path，例如/aaa/bbb/ccc，路径头需带斜杠，根目录传/
        :type ParentFolderPath: str
        :param _CodeFileConfig: 代码文件配置
        :type CodeFileConfig: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        :param _CodeFileContent: 代码文件内容
        :type CodeFileContent: str
        """
        self._ProjectId = None
        self._CodeFileName = None
        self._ParentFolderPath = None
        self._CodeFileConfig = None
        self._CodeFileContent = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeFileName(self):
        r"""代码文件名称
        :rtype: str
        """
        return self._CodeFileName

    @CodeFileName.setter
    def CodeFileName(self, CodeFileName):
        self._CodeFileName = CodeFileName

    @property
    def ParentFolderPath(self):
        r"""父文件夹path，例如/aaa/bbb/ccc，路径头需带斜杠，根目录传/
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def CodeFileConfig(self):
        r"""代码文件配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        """
        return self._CodeFileConfig

    @CodeFileConfig.setter
    def CodeFileConfig(self, CodeFileConfig):
        self._CodeFileConfig = CodeFileConfig

    @property
    def CodeFileContent(self):
        r"""代码文件内容
        :rtype: str
        """
        return self._CodeFileContent

    @CodeFileContent.setter
    def CodeFileContent(self, CodeFileContent):
        self._CodeFileContent = CodeFileContent


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CodeFileName = params.get("CodeFileName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        if params.get("CodeFileConfig") is not None:
            self._CodeFileConfig = CodeFileConfig()
            self._CodeFileConfig._deserialize(params.get("CodeFileConfig"))
        self._CodeFileContent = params.get("CodeFileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeFileResponse(AbstractModel):
    r"""CreateCodeFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeFile()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateCodeFolderRequest(AbstractModel):
    r"""CreateCodeFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _FolderName: 文件夹名称
        :type FolderName: str
        :param _ParentFolderPath: 父文件夹path，例如/aaa/bbb/ccc，路径头需带斜杠，根目录传/
        :type ParentFolderPath: str
        """
        self._ProjectId = None
        self._FolderName = None
        self._ParentFolderPath = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderName(self):
        r"""文件夹名称
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def ParentFolderPath(self):
        r"""父文件夹path，例如/aaa/bbb/ccc，路径头需带斜杠，根目录传/
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderName = params.get("FolderName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeFolderResponse(AbstractModel):
    r"""CreateCodeFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 成功true，失败false
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""成功true，失败false
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeStudioFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDataBackfillPlanRequest(AbstractModel):
    r"""CreateDataBackfillPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目Id
        :type ProjectId: str
        :param _TaskIds: 补录任务集合
        :type TaskIds: list of str
        :param _DataBackfillRangeList: 补录任务的数据时间配置
        :type DataBackfillRangeList: list of DataBackfillRange
        :param _TimeZone: 时区，默认UTC+8
        :type TimeZone: str
        :param _DataBackfillPlanName: 数据补录计划名称，不填则由系统随机生成一串字符
        :type DataBackfillPlanName: str
        :param _CheckParentType: 检查父任务类型，取值范围：- NONE-全部不检查- ALL-检查全部上游父任务- MAKE_SCOPE-只在（当前补录计划）选中任务中检查,默认NONE不检查
        :type CheckParentType: str
        :param _SkipEventListening: 补录是否忽略事件依赖,默认true
        :type SkipEventListening: bool
        :param _RedefineSelfWorkflowDependency: 自定义的工作流自依赖，yes或者no；如果不配置，则使用工作流原有自依赖
        :type RedefineSelfWorkflowDependency: str
        :param _RedefineParallelNum: 自定义实例运行并发度, 如果不配置，则使用任务原有自依赖
        :type RedefineParallelNum: int
        :param _SchedulerResourceGroupId: 调度资源组id，为空则表示使用任务原有调度执行资源组
        :type SchedulerResourceGroupId: str
        :param _IntegrationResourceGroupId: 集成任务资源组id，为空则表示使用任务原有调度执行资源组
        :type IntegrationResourceGroupId: str
        :param _RedefineParamList: 自定义参数，可以重新指定任务的参数，方便补录实例执行新的逻辑
        :type RedefineParamList: list of KVPair
        :param _DataTimeOrder: 补录是实例数据时间顺序，生效必须满足2个条件:
1. 必须同周期任务
2. 优先按依赖关系执行，无依赖关系影响的情况下按配置执行顺序执行
 
可选值
- NORMAL: 不设置
- ORDER: 顺序
- REVERSE: 逆序
不设置默认为NORMAL
        :type DataTimeOrder: str
        :param _RedefineCycleType: 补录实例重新生成周期，如果设置会重新指定补录任务实例的生成周期，目前只会将天实例转换成每月1号生成的实例
* MONTH_CYCLE: 月
        :type RedefineCycleType: str
        """
        self._ProjectId = None
        self._TaskIds = None
        self._DataBackfillRangeList = None
        self._TimeZone = None
        self._DataBackfillPlanName = None
        self._CheckParentType = None
        self._SkipEventListening = None
        self._RedefineSelfWorkflowDependency = None
        self._RedefineParallelNum = None
        self._SchedulerResourceGroupId = None
        self._IntegrationResourceGroupId = None
        self._RedefineParamList = None
        self._DataTimeOrder = None
        self._RedefineCycleType = None

    @property
    def ProjectId(self):
        r"""所属项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskIds(self):
        r"""补录任务集合
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def DataBackfillRangeList(self):
        r"""补录任务的数据时间配置
        :rtype: list of DataBackfillRange
        """
        return self._DataBackfillRangeList

    @DataBackfillRangeList.setter
    def DataBackfillRangeList(self, DataBackfillRangeList):
        self._DataBackfillRangeList = DataBackfillRangeList

    @property
    def TimeZone(self):
        r"""时区，默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def DataBackfillPlanName(self):
        r"""数据补录计划名称，不填则由系统随机生成一串字符
        :rtype: str
        """
        return self._DataBackfillPlanName

    @DataBackfillPlanName.setter
    def DataBackfillPlanName(self, DataBackfillPlanName):
        self._DataBackfillPlanName = DataBackfillPlanName

    @property
    def CheckParentType(self):
        r"""检查父任务类型，取值范围：- NONE-全部不检查- ALL-检查全部上游父任务- MAKE_SCOPE-只在（当前补录计划）选中任务中检查,默认NONE不检查
        :rtype: str
        """
        return self._CheckParentType

    @CheckParentType.setter
    def CheckParentType(self, CheckParentType):
        self._CheckParentType = CheckParentType

    @property
    def SkipEventListening(self):
        r"""补录是否忽略事件依赖,默认true
        :rtype: bool
        """
        return self._SkipEventListening

    @SkipEventListening.setter
    def SkipEventListening(self, SkipEventListening):
        self._SkipEventListening = SkipEventListening

    @property
    def RedefineSelfWorkflowDependency(self):
        r"""自定义的工作流自依赖，yes或者no；如果不配置，则使用工作流原有自依赖
        :rtype: str
        """
        return self._RedefineSelfWorkflowDependency

    @RedefineSelfWorkflowDependency.setter
    def RedefineSelfWorkflowDependency(self, RedefineSelfWorkflowDependency):
        self._RedefineSelfWorkflowDependency = RedefineSelfWorkflowDependency

    @property
    def RedefineParallelNum(self):
        r"""自定义实例运行并发度, 如果不配置，则使用任务原有自依赖
        :rtype: int
        """
        return self._RedefineParallelNum

    @RedefineParallelNum.setter
    def RedefineParallelNum(self, RedefineParallelNum):
        self._RedefineParallelNum = RedefineParallelNum

    @property
    def SchedulerResourceGroupId(self):
        r"""调度资源组id，为空则表示使用任务原有调度执行资源组
        :rtype: str
        """
        return self._SchedulerResourceGroupId

    @SchedulerResourceGroupId.setter
    def SchedulerResourceGroupId(self, SchedulerResourceGroupId):
        self._SchedulerResourceGroupId = SchedulerResourceGroupId

    @property
    def IntegrationResourceGroupId(self):
        r"""集成任务资源组id，为空则表示使用任务原有调度执行资源组
        :rtype: str
        """
        return self._IntegrationResourceGroupId

    @IntegrationResourceGroupId.setter
    def IntegrationResourceGroupId(self, IntegrationResourceGroupId):
        self._IntegrationResourceGroupId = IntegrationResourceGroupId

    @property
    def RedefineParamList(self):
        r"""自定义参数，可以重新指定任务的参数，方便补录实例执行新的逻辑
        :rtype: list of KVPair
        """
        return self._RedefineParamList

    @RedefineParamList.setter
    def RedefineParamList(self, RedefineParamList):
        self._RedefineParamList = RedefineParamList

    @property
    def DataTimeOrder(self):
        r"""补录是实例数据时间顺序，生效必须满足2个条件:
1. 必须同周期任务
2. 优先按依赖关系执行，无依赖关系影响的情况下按配置执行顺序执行
 
可选值
- NORMAL: 不设置
- ORDER: 顺序
- REVERSE: 逆序
不设置默认为NORMAL
        :rtype: str
        """
        return self._DataTimeOrder

    @DataTimeOrder.setter
    def DataTimeOrder(self, DataTimeOrder):
        self._DataTimeOrder = DataTimeOrder

    @property
    def RedefineCycleType(self):
        r"""补录实例重新生成周期，如果设置会重新指定补录任务实例的生成周期，目前只会将天实例转换成每月1号生成的实例
* MONTH_CYCLE: 月
        :rtype: str
        """
        return self._RedefineCycleType

    @RedefineCycleType.setter
    def RedefineCycleType(self, RedefineCycleType):
        self._RedefineCycleType = RedefineCycleType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskIds = params.get("TaskIds")
        if params.get("DataBackfillRangeList") is not None:
            self._DataBackfillRangeList = []
            for item in params.get("DataBackfillRangeList"):
                obj = DataBackfillRange()
                obj._deserialize(item)
                self._DataBackfillRangeList.append(obj)
        self._TimeZone = params.get("TimeZone")
        self._DataBackfillPlanName = params.get("DataBackfillPlanName")
        self._CheckParentType = params.get("CheckParentType")
        self._SkipEventListening = params.get("SkipEventListening")
        self._RedefineSelfWorkflowDependency = params.get("RedefineSelfWorkflowDependency")
        self._RedefineParallelNum = params.get("RedefineParallelNum")
        self._SchedulerResourceGroupId = params.get("SchedulerResourceGroupId")
        self._IntegrationResourceGroupId = params.get("IntegrationResourceGroupId")
        if params.get("RedefineParamList") is not None:
            self._RedefineParamList = []
            for item in params.get("RedefineParamList"):
                obj = KVPair()
                obj._deserialize(item)
                self._RedefineParamList.append(obj)
        self._DataTimeOrder = params.get("DataTimeOrder")
        self._RedefineCycleType = params.get("RedefineCycleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataBackfillPlanResponse(AbstractModel):
    r"""CreateDataBackfillPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据补录计划创建结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateDataReplenishmentPlan`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""数据补录计划创建结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateDataReplenishmentPlan`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateDataReplenishmentPlan()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDataReplenishmentPlan(AbstractModel):
    r"""创建数据补录计划结果

    """

    def __init__(self):
        r"""
        :param _DataBackfillPlanId: 补录计划Id
        :type DataBackfillPlanId: str
        """
        self._DataBackfillPlanId = None

    @property
    def DataBackfillPlanId(self):
        r"""补录计划Id
        :rtype: str
        """
        return self._DataBackfillPlanId

    @DataBackfillPlanId.setter
    def DataBackfillPlanId(self, DataBackfillPlanId):
        self._DataBackfillPlanId = DataBackfillPlanId


    def _deserialize(self, params):
        self._DataBackfillPlanId = params.get("DataBackfillPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFolderResult(AbstractModel):
    r"""创建文件夹结果

    """

    def __init__(self):
        r"""
        :param _FolderId: 创建成功的文件夹ID。如果创建失败则报错。
        :type FolderId: str
        """
        self._FolderId = None

    @property
    def FolderId(self):
        r"""创建成功的文件夹ID。如果创建失败则报错。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpsAlarmRuleRequest(AbstractModel):
    r"""CreateOpsAlarmRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _AlarmRuleName: 告警规则名称
        :type AlarmRuleName: str
        :param _MonitorObjectIds: 监控对象业务id列表，根据MonitorType 的设置传入不同的业务id，如下1（任务）： MonitorObjectIds为任务id列表2（工作流）： MonitorObjectIds 为工作流id列表(工作流id可从接口ListWorkflows获取)3（项目）：  MonitorObjectIds为项目id列表
        :type MonitorObjectIds: list of str
        :param _AlarmTypes: 告警规则监控类型 failure：失败告警 ；overtime：超时告警 success：成功告警; backTrackingOrRerunSuccess: 补录重跑成功告警 backTrackingOrRerunFailure：补录重跑失败告警； 
项目波动告警 projectFailureInstanceUpwardFluctuationAlarm： 当天失败实例数向上波动率超过阀值告警； projectSuccessInstanceDownwardFluctuationAlarm：当天成功实例数向下波动率超过阀值告警； 
离线集成任务对账告警： reconciliationFailure： 离线对账任务失败告警 reconciliationOvertime： 离线对账任务运行超时告警 reconciliationMismatch： 数据对账任务不一致条数超过阀值告警
        :type AlarmTypes: list of str
        :param _AlarmGroups: 告警接收人配置信息
        :type AlarmGroups: list of AlarmGroup
        :param _MonitorObjectType: 监控对象类型, 
任务维度监控： 可按照任务/工作流/项目来配置：1.任务、2.工作流、3.项目（默认为1.任务）
项目维度监控： 项目整体任务波动告警，  7：项目波动监控告警
        :type MonitorObjectType: int
        :param _AlarmRuleDetail: 告警规则配置信息
成功告警无需配置；失败告警可以配置首次失败告警或者所有重试失败告警；超时配置需要配置超时类型及超时阀值；项目波动告警需要配置波动率及防抖周期配置
        :type AlarmRuleDetail: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        :param _AlarmLevel: 告警级别 1.普通、2.重要、3.紧急（默认1.普通）
        :type AlarmLevel: int
        :param _Description: 告警规则描述
        :type Description: str
        """
        self._ProjectId = None
        self._AlarmRuleName = None
        self._MonitorObjectIds = None
        self._AlarmTypes = None
        self._AlarmGroups = None
        self._MonitorObjectType = None
        self._AlarmRuleDetail = None
        self._AlarmLevel = None
        self._Description = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmRuleName(self):
        r"""告警规则名称
        :rtype: str
        """
        return self._AlarmRuleName

    @AlarmRuleName.setter
    def AlarmRuleName(self, AlarmRuleName):
        self._AlarmRuleName = AlarmRuleName

    @property
    def MonitorObjectIds(self):
        r"""监控对象业务id列表，根据MonitorType 的设置传入不同的业务id，如下1（任务）： MonitorObjectIds为任务id列表2（工作流）： MonitorObjectIds 为工作流id列表(工作流id可从接口ListWorkflows获取)3（项目）：  MonitorObjectIds为项目id列表
        :rtype: list of str
        """
        return self._MonitorObjectIds

    @MonitorObjectIds.setter
    def MonitorObjectIds(self, MonitorObjectIds):
        self._MonitorObjectIds = MonitorObjectIds

    @property
    def AlarmTypes(self):
        r"""告警规则监控类型 failure：失败告警 ；overtime：超时告警 success：成功告警; backTrackingOrRerunSuccess: 补录重跑成功告警 backTrackingOrRerunFailure：补录重跑失败告警； 
项目波动告警 projectFailureInstanceUpwardFluctuationAlarm： 当天失败实例数向上波动率超过阀值告警； projectSuccessInstanceDownwardFluctuationAlarm：当天成功实例数向下波动率超过阀值告警； 
离线集成任务对账告警： reconciliationFailure： 离线对账任务失败告警 reconciliationOvertime： 离线对账任务运行超时告警 reconciliationMismatch： 数据对账任务不一致条数超过阀值告警
        :rtype: list of str
        """
        return self._AlarmTypes

    @AlarmTypes.setter
    def AlarmTypes(self, AlarmTypes):
        self._AlarmTypes = AlarmTypes

    @property
    def AlarmGroups(self):
        r"""告警接收人配置信息
        :rtype: list of AlarmGroup
        """
        return self._AlarmGroups

    @AlarmGroups.setter
    def AlarmGroups(self, AlarmGroups):
        self._AlarmGroups = AlarmGroups

    @property
    def MonitorObjectType(self):
        r"""监控对象类型, 
任务维度监控： 可按照任务/工作流/项目来配置：1.任务、2.工作流、3.项目（默认为1.任务）
项目维度监控： 项目整体任务波动告警，  7：项目波动监控告警
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def AlarmRuleDetail(self):
        r"""告警规则配置信息
成功告警无需配置；失败告警可以配置首次失败告警或者所有重试失败告警；超时配置需要配置超时类型及超时阀值；项目波动告警需要配置波动率及防抖周期配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        """
        return self._AlarmRuleDetail

    @AlarmRuleDetail.setter
    def AlarmRuleDetail(self, AlarmRuleDetail):
        self._AlarmRuleDetail = AlarmRuleDetail

    @property
    def AlarmLevel(self):
        r"""告警级别 1.普通、2.重要、3.紧急（默认1.普通）
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def Description(self):
        r"""告警规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmRuleName = params.get("AlarmRuleName")
        self._MonitorObjectIds = params.get("MonitorObjectIds")
        self._AlarmTypes = params.get("AlarmTypes")
        if params.get("AlarmGroups") is not None:
            self._AlarmGroups = []
            for item in params.get("AlarmGroups"):
                obj = AlarmGroup()
                obj._deserialize(item)
                self._AlarmGroups.append(obj)
        self._MonitorObjectType = params.get("MonitorObjectType")
        if params.get("AlarmRuleDetail") is not None:
            self._AlarmRuleDetail = AlarmRuleDetail()
            self._AlarmRuleDetail._deserialize(params.get("AlarmRuleDetail"))
        self._AlarmLevel = params.get("AlarmLevel")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpsAlarmRuleResponse(AbstractModel):
    r"""CreateOpsAlarmRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 告警规则唯一id
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateAlarmRuleData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""告警规则唯一id
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateAlarmRuleData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateAlarmRuleData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateResourceFileRequest(AbstractModel):
    r"""CreateResourceFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ResourceName: 资源文件名称, 尽可能和上传文件名保持一致
        :type ResourceName: str
        :param _BucketName: cos存储桶名称, 可从GetResourceCosPath接口获取
        :type BucketName: str
        :param _CosRegion: BucketName桶对应的cos存储桶区域
        :type CosRegion: str
        :param _ParentFolderPath: 项目中资源文件上传的路径, 取值示例: /wedata/qxxxm/, 根目录,请使用/即可
        :type ParentFolderPath: str
        :param _ResourceFile: - 上传文件及手填两种方式只能选择其一，如果两者均提供，取值顺序为文件>手填值
-   手填值必须是存在的cos路径, /datastudio/resource/ 为固定前缀, projectId 为项目ID,需传入具体值, parentFolderPath为父文件夹路径, name为文件名, 手填值取值示例:     /datastudio/resource/projectId/parentFolderPath/name 

        :type ResourceFile: str
        :param _BundleId: bundle客户端ID
        :type BundleId: str
        :param _BundleInfo: bundle客户端信息
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._ResourceName = None
        self._BucketName = None
        self._CosRegion = None
        self._ParentFolderPath = None
        self._ResourceFile = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceName(self):
        r"""资源文件名称, 尽可能和上传文件名保持一致
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def BucketName(self):
        r"""cos存储桶名称, 可从GetResourceCosPath接口获取
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def CosRegion(self):
        r"""BucketName桶对应的cos存储桶区域
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def ParentFolderPath(self):
        r"""项目中资源文件上传的路径, 取值示例: /wedata/qxxxm/, 根目录,请使用/即可
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def ResourceFile(self):
        r"""- 上传文件及手填两种方式只能选择其一，如果两者均提供，取值顺序为文件>手填值
-   手填值必须是存在的cos路径, /datastudio/resource/ 为固定前缀, projectId 为项目ID,需传入具体值, parentFolderPath为父文件夹路径, name为文件名, 手填值取值示例:     /datastudio/resource/projectId/parentFolderPath/name 

        :rtype: str
        """
        return self._ResourceFile

    @ResourceFile.setter
    def ResourceFile(self, ResourceFile):
        self._ResourceFile = ResourceFile

    @property
    def BundleId(self):
        r"""bundle客户端ID
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""bundle客户端信息
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceName = params.get("ResourceName")
        self._BucketName = params.get("BucketName")
        self._CosRegion = params.get("CosRegion")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._ResourceFile = params.get("ResourceFile")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceFileResponse(AbstractModel):
    r"""CreateResourceFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建资源文件结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFileResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""创建资源文件结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFileResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateResourceFileResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateResourceFileResult(AbstractModel):
    r"""创建资源文件结果

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源文件ID
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        r"""资源文件ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceFolderRequest(AbstractModel):
    r"""CreateResourceFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ParentFolderPath: 父文件夹绝对路径, 取值示例 /wedata/test, 根目录,请使用/即可
        :type ParentFolderPath: str
        :param _FolderName: 文件夹名称
        :type FolderName: str
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""父文件夹绝对路径, 取值示例 /wedata/test, 根目录,请使用/即可
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def FolderName(self):
        r"""文件夹名称
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceFolderResponse(AbstractModel):
    r"""CreateResourceFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建文件夹结果，如果创建失败则报错。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateFolderResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""创建文件夹结果，如果创建失败则报错。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateSQLFolderRequest(AbstractModel):
    r"""CreateSQLFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FolderName: 文件夹名称
        :type FolderName: str
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _ParentFolderPath: 父文件夹path，/aaa/bbb/ccc，路径头需带斜杠，查询根目录传/
        :type ParentFolderPath: str
        :param _AccessScope: 权限范围：SHARED, PRIVATE
        :type AccessScope: str
        """
        self._FolderName = None
        self._ProjectId = None
        self._ParentFolderPath = None
        self._AccessScope = None

    @property
    def FolderName(self):
        r"""文件夹名称
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""父文件夹path，/aaa/bbb/ccc，路径头需带斜杠，查询根目录传/
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def AccessScope(self):
        r"""权限范围：SHARED, PRIVATE
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope


    def _deserialize(self, params):
        self._FolderName = params.get("FolderName")
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._AccessScope = params.get("AccessScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSQLFolderResponse(AbstractModel):
    r"""CreateSQLFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 成功true，失败false
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SqlCreateResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""成功true，失败false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SqlCreateResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SqlCreateResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateSQLScriptRequest(AbstractModel):
    r"""CreateSQLScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScriptName: 脚本名称
        :type ScriptName: str
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _ParentFolderPath: 父文件夹path，/aaa/bbb/ccc，根目录为空字符串或/
        :type ParentFolderPath: str
        :param _ScriptConfig: 数据探索脚本配置
        :type ScriptConfig: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        :param _ScriptContent: 脚本内容，如有值，则要将内容进行base64编码
        :type ScriptContent: str
        :param _AccessScope: 权限范围：SHARED, PRIVATE
        :type AccessScope: str
        """
        self._ScriptName = None
        self._ProjectId = None
        self._ParentFolderPath = None
        self._ScriptConfig = None
        self._ScriptContent = None
        self._AccessScope = None

    @property
    def ScriptName(self):
        r"""脚本名称
        :rtype: str
        """
        return self._ScriptName

    @ScriptName.setter
    def ScriptName(self, ScriptName):
        self._ScriptName = ScriptName

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""父文件夹path，/aaa/bbb/ccc，根目录为空字符串或/
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def ScriptConfig(self):
        r"""数据探索脚本配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        """
        return self._ScriptConfig

    @ScriptConfig.setter
    def ScriptConfig(self, ScriptConfig):
        self._ScriptConfig = ScriptConfig

    @property
    def ScriptContent(self):
        r"""脚本内容，如有值，则要将内容进行base64编码
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def AccessScope(self):
        r"""权限范围：SHARED, PRIVATE
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope


    def _deserialize(self, params):
        self._ScriptName = params.get("ScriptName")
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        if params.get("ScriptConfig") is not None:
            self._ScriptConfig = SQLScriptConfig()
            self._ScriptConfig._deserialize(params.get("ScriptConfig"))
        self._ScriptContent = params.get("ScriptContent")
        self._AccessScope = params.get("AccessScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSQLScriptResponse(AbstractModel):
    r"""CreateSQLScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLScript()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateTaskBaseAttribute(AbstractModel):
    r"""创建任务基本属性信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskTypeId: 任务类型ID：

* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 32:DLC SQL
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :type TaskTypeId: str
        :param _WorkflowId: 工作流ID
        :type WorkflowId: str
        :param _OwnerUin: 任务负责人ID，默认为当前用户
        :type OwnerUin: str
        :param _TaskDescription: 任务描述
        :type TaskDescription: str
        """
        self._TaskName = None
        self._TaskTypeId = None
        self._WorkflowId = None
        self._OwnerUin = None
        self._TaskDescription = None

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskTypeId(self):
        r"""任务类型ID：

* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 32:DLC SQL
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :rtype: str
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def WorkflowId(self):
        r"""工作流ID
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def OwnerUin(self):
        r"""任务负责人ID，默认为当前用户
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskDescription(self):
        r"""任务描述
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskTypeId = params.get("TaskTypeId")
        self._WorkflowId = params.get("WorkflowId")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskDescription = params.get("TaskDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskConfiguration(AbstractModel):
    r"""创建任务配置信息

    """

    def __init__(self):
        r"""
        :param _ResourceGroup: 资源组ID： 需要通过 DescribeNormalSchedulerExecutorGroups 获取 ExecutorGroupId
        :type ResourceGroup: str
        :param _CodeContent: 代码内容的Base64编码
        :type CodeContent: str
        :param _TaskExtConfigurationList: 任务扩展属性配置列表
        :type TaskExtConfigurationList: list of TaskExtParameter
        :param _DataCluster: 集群ID
        :type DataCluster: str
        :param _BrokerIp: 指定的运行节点
        :type BrokerIp: str
        :param _YarnQueue: 资源池队列名称，需要通过 DescribeProjectClusterQueues 获取
        :type YarnQueue: str
        :param _SourceServiceId: 来源数据源ID, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
        :type SourceServiceId: str
        :param _TargetServiceId: 目标数据源ID, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
        :type TargetServiceId: str
        :param _TaskSchedulingParameterList: 调度参数
        :type TaskSchedulingParameterList: list of TaskSchedulingParameter
        :param _BundleId: Bundle使用的ID
        :type BundleId: str
        :param _BundleInfo: Bundle信息
        :type BundleInfo: str
        """
        self._ResourceGroup = None
        self._CodeContent = None
        self._TaskExtConfigurationList = None
        self._DataCluster = None
        self._BrokerIp = None
        self._YarnQueue = None
        self._SourceServiceId = None
        self._TargetServiceId = None
        self._TaskSchedulingParameterList = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ResourceGroup(self):
        r"""资源组ID： 需要通过 DescribeNormalSchedulerExecutorGroups 获取 ExecutorGroupId
        :rtype: str
        """
        return self._ResourceGroup

    @ResourceGroup.setter
    def ResourceGroup(self, ResourceGroup):
        self._ResourceGroup = ResourceGroup

    @property
    def CodeContent(self):
        r"""代码内容的Base64编码
        :rtype: str
        """
        return self._CodeContent

    @CodeContent.setter
    def CodeContent(self, CodeContent):
        self._CodeContent = CodeContent

    @property
    def TaskExtConfigurationList(self):
        r"""任务扩展属性配置列表
        :rtype: list of TaskExtParameter
        """
        return self._TaskExtConfigurationList

    @TaskExtConfigurationList.setter
    def TaskExtConfigurationList(self, TaskExtConfigurationList):
        self._TaskExtConfigurationList = TaskExtConfigurationList

    @property
    def DataCluster(self):
        r"""集群ID
        :rtype: str
        """
        return self._DataCluster

    @DataCluster.setter
    def DataCluster(self, DataCluster):
        self._DataCluster = DataCluster

    @property
    def BrokerIp(self):
        r"""指定的运行节点
        :rtype: str
        """
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp

    @property
    def YarnQueue(self):
        r"""资源池队列名称，需要通过 DescribeProjectClusterQueues 获取
        :rtype: str
        """
        return self._YarnQueue

    @YarnQueue.setter
    def YarnQueue(self, YarnQueue):
        self._YarnQueue = YarnQueue

    @property
    def SourceServiceId(self):
        r"""来源数据源ID, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
        :rtype: str
        """
        return self._SourceServiceId

    @SourceServiceId.setter
    def SourceServiceId(self, SourceServiceId):
        self._SourceServiceId = SourceServiceId

    @property
    def TargetServiceId(self):
        r"""目标数据源ID, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
        :rtype: str
        """
        return self._TargetServiceId

    @TargetServiceId.setter
    def TargetServiceId(self, TargetServiceId):
        self._TargetServiceId = TargetServiceId

    @property
    def TaskSchedulingParameterList(self):
        r"""调度参数
        :rtype: list of TaskSchedulingParameter
        """
        return self._TaskSchedulingParameterList

    @TaskSchedulingParameterList.setter
    def TaskSchedulingParameterList(self, TaskSchedulingParameterList):
        self._TaskSchedulingParameterList = TaskSchedulingParameterList

    @property
    def BundleId(self):
        r"""Bundle使用的ID
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle信息
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ResourceGroup = params.get("ResourceGroup")
        self._CodeContent = params.get("CodeContent")
        if params.get("TaskExtConfigurationList") is not None:
            self._TaskExtConfigurationList = []
            for item in params.get("TaskExtConfigurationList"):
                obj = TaskExtParameter()
                obj._deserialize(item)
                self._TaskExtConfigurationList.append(obj)
        self._DataCluster = params.get("DataCluster")
        self._BrokerIp = params.get("BrokerIp")
        self._YarnQueue = params.get("YarnQueue")
        self._SourceServiceId = params.get("SourceServiceId")
        self._TargetServiceId = params.get("TargetServiceId")
        if params.get("TaskSchedulingParameterList") is not None:
            self._TaskSchedulingParameterList = []
            for item in params.get("TaskSchedulingParameterList"):
                obj = TaskSchedulingParameter()
                obj._deserialize(item)
                self._TaskSchedulingParameterList.append(obj)
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskRequest(AbstractModel):
    r"""CreateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _TaskBaseAttribute: 任务基本属性
        :type TaskBaseAttribute: :class:`tencentcloud.wedata.v20250806.models.CreateTaskBaseAttribute`
        :param _TaskConfiguration: 任务配置
        :type TaskConfiguration: :class:`tencentcloud.wedata.v20250806.models.CreateTaskConfiguration`
        :param _TaskSchedulerConfiguration: 任务调度配置
        :type TaskSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.CreateTaskSchedulerConfiguration`
        """
        self._ProjectId = None
        self._TaskBaseAttribute = None
        self._TaskConfiguration = None
        self._TaskSchedulerConfiguration = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskBaseAttribute(self):
        r"""任务基本属性
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskBaseAttribute`
        """
        return self._TaskBaseAttribute

    @TaskBaseAttribute.setter
    def TaskBaseAttribute(self, TaskBaseAttribute):
        self._TaskBaseAttribute = TaskBaseAttribute

    @property
    def TaskConfiguration(self):
        r"""任务配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskConfiguration`
        """
        return self._TaskConfiguration

    @TaskConfiguration.setter
    def TaskConfiguration(self, TaskConfiguration):
        self._TaskConfiguration = TaskConfiguration

    @property
    def TaskSchedulerConfiguration(self):
        r"""任务调度配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskSchedulerConfiguration`
        """
        return self._TaskSchedulerConfiguration

    @TaskSchedulerConfiguration.setter
    def TaskSchedulerConfiguration(self, TaskSchedulerConfiguration):
        self._TaskSchedulerConfiguration = TaskSchedulerConfiguration


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        if params.get("TaskBaseAttribute") is not None:
            self._TaskBaseAttribute = CreateTaskBaseAttribute()
            self._TaskBaseAttribute._deserialize(params.get("TaskBaseAttribute"))
        if params.get("TaskConfiguration") is not None:
            self._TaskConfiguration = CreateTaskConfiguration()
            self._TaskConfiguration._deserialize(params.get("TaskConfiguration"))
        if params.get("TaskSchedulerConfiguration") is not None:
            self._TaskSchedulerConfiguration = CreateTaskSchedulerConfiguration()
            self._TaskSchedulerConfiguration._deserialize(params.get("TaskSchedulerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    r"""CreateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务ID
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateTaskResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务ID
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateTaskResult(AbstractModel):
    r"""创建任务返回体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
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
        


class CreateTaskSchedulerConfiguration(AbstractModel):
    r"""创建任务调度配置信息

    """

    def __init__(self):
        r"""
        :param _CycleType: 周期类型：默认为 DAY_CYCLE

支持的类型为 

* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
        :type CycleType: str
        :param _ScheduleTimeZone: 时区，默认为 UTC+8
        :type ScheduleTimeZone: str
        :param _CrontabExpression: Cron表达式，默认为 0 0 0 * * ? * 
        :type CrontabExpression: str
        :param _StartTime: 生效日期，默认为当前日期的 00:00:00
        :type StartTime: str
        :param _EndTime: 结束日期，默认为 2099-12-31 23:59:59
        :type EndTime: str
        :param _ExecutionStartTime: 执行时间 左闭区间，默认 00:00
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: 执行时间 右闭区间，默认 23:59
        :type ExecutionEndTime: str
        :param _ScheduleRunType: 调度类型: 0 正常调度 1 空跑调度，默认为 0
        :type ScheduleRunType: str
        :param _CalendarOpen: 日历调度 取值为 0 和 1， 1为打开，0为关闭，默认为0
        :type CalendarOpen: str
        :param _CalendarId: 日历调度 日历 ID
        :type CalendarId: str
        :param _SelfDepend: 自依赖, 默认值 serial, 取值为：parallel(并行), serial(串行), orderly(有序)
        :type SelfDepend: str
        :param _UpstreamDependencyConfigList: 上游依赖数组
        :type UpstreamDependencyConfigList: list of DependencyTaskBrief
        :param _EventListenerList: 事件数组
        :type EventListenerList: list of EventListener
        :param _RunPriority: 任务调度优先级 运行优先级 4高 5中 6低 , 默认:6
        :type RunPriority: str
        :param _RetryWait: 重试策略 重试等待时间,单位分钟: 默认: 5
        :type RetryWait: str
        :param _MaxRetryAttempts: 重试策略 最大尝试次数, 默认: 4
        :type MaxRetryAttempts: str
        :param _ExecutionTTL: 超时处理策略 运行耗时超时（单位：分钟）默认为 -1
        :type ExecutionTTL: str
        :param _WaitExecutionTotalTTL: 超时处理策略 等待总时长耗时超时（单位：分钟）默认为 -1
        :type WaitExecutionTotalTTL: str
        :param _AllowRedoType: 重跑&补录配置, 默认为 ALL; , ALL 运行成功或失败后皆可重跑或补录, FAILURE 运行成功后不可重跑或补录，运行失败后可重跑或补录, NONE 运行成功或失败后皆不可重跑或补录;
        :type AllowRedoType: str
        :param _ParamTaskOutList: 输出参数数组
        :type ParamTaskOutList: list of OutTaskParameter
        :param _ParamTaskInList: 输入参数数组
        :type ParamTaskInList: list of InTaskParameter
        :param _TaskOutputRegistryList: 产出登记
        :type TaskOutputRegistryList: list of TaskDataRegistry
        :param _InitStrategy: **实例生成策略**
* T_PLUS_0: T+0生成,默认策略
* T_PLUS_1: T+1生成
        :type InitStrategy: str
        """
        self._CycleType = None
        self._ScheduleTimeZone = None
        self._CrontabExpression = None
        self._StartTime = None
        self._EndTime = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None
        self._ScheduleRunType = None
        self._CalendarOpen = None
        self._CalendarId = None
        self._SelfDepend = None
        self._UpstreamDependencyConfigList = None
        self._EventListenerList = None
        self._RunPriority = None
        self._RetryWait = None
        self._MaxRetryAttempts = None
        self._ExecutionTTL = None
        self._WaitExecutionTotalTTL = None
        self._AllowRedoType = None
        self._ParamTaskOutList = None
        self._ParamTaskInList = None
        self._TaskOutputRegistryList = None
        self._InitStrategy = None

    @property
    def CycleType(self):
        r"""周期类型：默认为 DAY_CYCLE

支持的类型为 

* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def ScheduleTimeZone(self):
        r"""时区，默认为 UTC+8
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone

    @property
    def CrontabExpression(self):
        r"""Cron表达式，默认为 0 0 0 * * ? * 
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def StartTime(self):
        r"""生效日期，默认为当前日期的 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束日期，默认为 2099-12-31 23:59:59
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExecutionStartTime(self):
        r"""执行时间 左闭区间，默认 00:00
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""执行时间 右闭区间，默认 23:59
        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime

    @property
    def ScheduleRunType(self):
        r"""调度类型: 0 正常调度 1 空跑调度，默认为 0
        :rtype: str
        """
        return self._ScheduleRunType

    @ScheduleRunType.setter
    def ScheduleRunType(self, ScheduleRunType):
        self._ScheduleRunType = ScheduleRunType

    @property
    def CalendarOpen(self):
        r"""日历调度 取值为 0 和 1， 1为打开，0为关闭，默认为0
        :rtype: str
        """
        return self._CalendarOpen

    @CalendarOpen.setter
    def CalendarOpen(self, CalendarOpen):
        self._CalendarOpen = CalendarOpen

    @property
    def CalendarId(self):
        r"""日历调度 日历 ID
        :rtype: str
        """
        return self._CalendarId

    @CalendarId.setter
    def CalendarId(self, CalendarId):
        self._CalendarId = CalendarId

    @property
    def SelfDepend(self):
        r"""自依赖, 默认值 serial, 取值为：parallel(并行), serial(串行), orderly(有序)
        :rtype: str
        """
        return self._SelfDepend

    @SelfDepend.setter
    def SelfDepend(self, SelfDepend):
        self._SelfDepend = SelfDepend

    @property
    def UpstreamDependencyConfigList(self):
        r"""上游依赖数组
        :rtype: list of DependencyTaskBrief
        """
        return self._UpstreamDependencyConfigList

    @UpstreamDependencyConfigList.setter
    def UpstreamDependencyConfigList(self, UpstreamDependencyConfigList):
        self._UpstreamDependencyConfigList = UpstreamDependencyConfigList

    @property
    def EventListenerList(self):
        r"""事件数组
        :rtype: list of EventListener
        """
        return self._EventListenerList

    @EventListenerList.setter
    def EventListenerList(self, EventListenerList):
        self._EventListenerList = EventListenerList

    @property
    def RunPriority(self):
        r"""任务调度优先级 运行优先级 4高 5中 6低 , 默认:6
        :rtype: str
        """
        return self._RunPriority

    @RunPriority.setter
    def RunPriority(self, RunPriority):
        self._RunPriority = RunPriority

    @property
    def RetryWait(self):
        r"""重试策略 重试等待时间,单位分钟: 默认: 5
        :rtype: str
        """
        return self._RetryWait

    @RetryWait.setter
    def RetryWait(self, RetryWait):
        self._RetryWait = RetryWait

    @property
    def MaxRetryAttempts(self):
        r"""重试策略 最大尝试次数, 默认: 4
        :rtype: str
        """
        return self._MaxRetryAttempts

    @MaxRetryAttempts.setter
    def MaxRetryAttempts(self, MaxRetryAttempts):
        self._MaxRetryAttempts = MaxRetryAttempts

    @property
    def ExecutionTTL(self):
        r"""超时处理策略 运行耗时超时（单位：分钟）默认为 -1
        :rtype: str
        """
        return self._ExecutionTTL

    @ExecutionTTL.setter
    def ExecutionTTL(self, ExecutionTTL):
        self._ExecutionTTL = ExecutionTTL

    @property
    def WaitExecutionTotalTTL(self):
        r"""超时处理策略 等待总时长耗时超时（单位：分钟）默认为 -1
        :rtype: str
        """
        return self._WaitExecutionTotalTTL

    @WaitExecutionTotalTTL.setter
    def WaitExecutionTotalTTL(self, WaitExecutionTotalTTL):
        self._WaitExecutionTotalTTL = WaitExecutionTotalTTL

    @property
    def AllowRedoType(self):
        r"""重跑&补录配置, 默认为 ALL; , ALL 运行成功或失败后皆可重跑或补录, FAILURE 运行成功后不可重跑或补录，运行失败后可重跑或补录, NONE 运行成功或失败后皆不可重跑或补录;
        :rtype: str
        """
        return self._AllowRedoType

    @AllowRedoType.setter
    def AllowRedoType(self, AllowRedoType):
        self._AllowRedoType = AllowRedoType

    @property
    def ParamTaskOutList(self):
        r"""输出参数数组
        :rtype: list of OutTaskParameter
        """
        return self._ParamTaskOutList

    @ParamTaskOutList.setter
    def ParamTaskOutList(self, ParamTaskOutList):
        self._ParamTaskOutList = ParamTaskOutList

    @property
    def ParamTaskInList(self):
        r"""输入参数数组
        :rtype: list of InTaskParameter
        """
        return self._ParamTaskInList

    @ParamTaskInList.setter
    def ParamTaskInList(self, ParamTaskInList):
        self._ParamTaskInList = ParamTaskInList

    @property
    def TaskOutputRegistryList(self):
        r"""产出登记
        :rtype: list of TaskDataRegistry
        """
        return self._TaskOutputRegistryList

    @TaskOutputRegistryList.setter
    def TaskOutputRegistryList(self, TaskOutputRegistryList):
        self._TaskOutputRegistryList = TaskOutputRegistryList

    @property
    def InitStrategy(self):
        r"""**实例生成策略**
* T_PLUS_0: T+0生成,默认策略
* T_PLUS_1: T+1生成
        :rtype: str
        """
        return self._InitStrategy

    @InitStrategy.setter
    def InitStrategy(self, InitStrategy):
        self._InitStrategy = InitStrategy


    def _deserialize(self, params):
        self._CycleType = params.get("CycleType")
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        self._CrontabExpression = params.get("CrontabExpression")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        self._ScheduleRunType = params.get("ScheduleRunType")
        self._CalendarOpen = params.get("CalendarOpen")
        self._CalendarId = params.get("CalendarId")
        self._SelfDepend = params.get("SelfDepend")
        if params.get("UpstreamDependencyConfigList") is not None:
            self._UpstreamDependencyConfigList = []
            for item in params.get("UpstreamDependencyConfigList"):
                obj = DependencyTaskBrief()
                obj._deserialize(item)
                self._UpstreamDependencyConfigList.append(obj)
        if params.get("EventListenerList") is not None:
            self._EventListenerList = []
            for item in params.get("EventListenerList"):
                obj = EventListener()
                obj._deserialize(item)
                self._EventListenerList.append(obj)
        self._RunPriority = params.get("RunPriority")
        self._RetryWait = params.get("RetryWait")
        self._MaxRetryAttempts = params.get("MaxRetryAttempts")
        self._ExecutionTTL = params.get("ExecutionTTL")
        self._WaitExecutionTotalTTL = params.get("WaitExecutionTotalTTL")
        self._AllowRedoType = params.get("AllowRedoType")
        if params.get("ParamTaskOutList") is not None:
            self._ParamTaskOutList = []
            for item in params.get("ParamTaskOutList"):
                obj = OutTaskParameter()
                obj._deserialize(item)
                self._ParamTaskOutList.append(obj)
        if params.get("ParamTaskInList") is not None:
            self._ParamTaskInList = []
            for item in params.get("ParamTaskInList"):
                obj = InTaskParameter()
                obj._deserialize(item)
                self._ParamTaskInList.append(obj)
        if params.get("TaskOutputRegistryList") is not None:
            self._TaskOutputRegistryList = []
            for item in params.get("TaskOutputRegistryList"):
                obj = TaskDataRegistry()
                obj._deserialize(item)
                self._TaskOutputRegistryList.append(obj)
        self._InitStrategy = params.get("InitStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowFolderRequest(AbstractModel):
    r"""CreateWorkflowFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ParentFolderPath: 父文件夹绝对路径，如/abc/de，如果是根目录则传/
        :type ParentFolderPath: str
        :param _FolderName: 要创建的文件夹名字
        :type FolderName: str
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""父文件夹绝对路径，如/abc/de，如果是根目录则传/
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def FolderName(self):
        r"""要创建的文件夹名字
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowFolderResponse(AbstractModel):
    r"""CreateWorkflowFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建文件夹结果，如果创建失败则报错。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateFolderResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""创建文件夹结果，如果创建失败则报错。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkflowRequest(AbstractModel):
    r"""CreateWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _WorkflowName: 工作流名称
        :type WorkflowName: str
        :param _ParentFolderPath: 所属文件夹路径
        :type ParentFolderPath: str
        :param _WorkflowType: 工作流类型,取值示例：cycle 周期工作流；manual 手动工作流，默认传入cycle
        :type WorkflowType: str
        :param _WorkflowDesc: 工作流描述
        :type WorkflowDesc: str
        :param _OwnerUin: 工作流负责人ID
        :type OwnerUin: str
        :param _WorkflowParams: 工作流参数
        :type WorkflowParams: list of ParamInfo
        :param _WorkflowSchedulerConfiguration: 统一调度信息
        :type WorkflowSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfigurationInfo`
        :param _BundleId: BundleId项
        :type BundleId: str
        :param _BundleInfo: Bundle信息
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._WorkflowName = None
        self._ParentFolderPath = None
        self._WorkflowType = None
        self._WorkflowDesc = None
        self._OwnerUin = None
        self._WorkflowParams = None
        self._WorkflowSchedulerConfiguration = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowName(self):
        r"""工作流名称
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def ParentFolderPath(self):
        r"""所属文件夹路径
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def WorkflowType(self):
        r"""工作流类型,取值示例：cycle 周期工作流；manual 手动工作流，默认传入cycle
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def WorkflowDesc(self):
        r"""工作流描述
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def OwnerUin(self):
        r"""工作流负责人ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def WorkflowParams(self):
        r"""工作流参数
        :rtype: list of ParamInfo
        """
        return self._WorkflowParams

    @WorkflowParams.setter
    def WorkflowParams(self, WorkflowParams):
        self._WorkflowParams = WorkflowParams

    @property
    def WorkflowSchedulerConfiguration(self):
        r"""统一调度信息
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfigurationInfo`
        """
        return self._WorkflowSchedulerConfiguration

    @WorkflowSchedulerConfiguration.setter
    def WorkflowSchedulerConfiguration(self, WorkflowSchedulerConfiguration):
        self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfiguration

    @property
    def BundleId(self):
        r"""BundleId项
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle信息
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowName = params.get("WorkflowName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._WorkflowType = params.get("WorkflowType")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._OwnerUin = params.get("OwnerUin")
        if params.get("WorkflowParams") is not None:
            self._WorkflowParams = []
            for item in params.get("WorkflowParams"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._WorkflowParams.append(obj)
        if params.get("WorkflowSchedulerConfiguration") is not None:
            self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfigurationInfo()
            self._WorkflowSchedulerConfiguration._deserialize(params.get("WorkflowSchedulerConfiguration"))
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowResponse(AbstractModel):
    r"""CreateWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回工作流ID
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回工作流ID
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateWorkflowResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkflowResult(AbstractModel):
    r"""创建工作流结果

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 创建成功后的工作流id
        :type WorkflowId: str
        """
        self._WorkflowId = None

    @property
    def WorkflowId(self):
        r"""创建成功后的工作流id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataBackfillRange(AbstractModel):
    r"""补录计划日期范围

    """

    def __init__(self):
        r"""
        :param _StartDate: 开始日期，格式yyyy-MM-dd 表示从指定日期的00:00:00开始
注意：此字段可能返回 null，表示取不到有效值。
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd，表示从指定日期的 23:59:59结束
注意：此字段可能返回 null，表示取不到有效值。
        :type EndDate: str
        :param _ExecutionStartTime: 在[StartDate, EndDate]之间每天的开始时间点，格式HH:mm,只针对小时及周期小于小时的任务生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: 在[StartDate, EndDate]之间每天的结束时间点，格式HH:mm,只针对小时及周期小于小时的任务生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionEndTime: str
        """
        self._StartDate = None
        self._EndDate = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None

    @property
    def StartDate(self):
        r"""开始日期，格式yyyy-MM-dd 表示从指定日期的00:00:00开始
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""结束日期，格式yyyy-MM-dd，表示从指定日期的 23:59:59结束
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def ExecutionStartTime(self):
        r"""在[StartDate, EndDate]之间每天的开始时间点，格式HH:mm,只针对小时及周期小于小时的任务生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""在[StartDate, EndDate]之间每天的结束时间点，格式HH:mm,只针对小时及周期小于小时的任务生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmRuleResult(AbstractModel):
    r"""删除告警规则响应结果

    """

    def __init__(self):
        r"""
        :param _Status: 是否删除成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""是否删除成功
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
        


class DeleteCodeFileRequest(AbstractModel):
    r"""DeleteCodeFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _CodeFileId: 代码文件ID，参数值来自CreateCodeFile接口的返回
        :type CodeFileId: str
        """
        self._ProjectId = None
        self._CodeFileId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeFileId(self):
        r"""代码文件ID，参数值来自CreateCodeFile接口的返回
        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CodeFileId = params.get("CodeFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeFileResponse(AbstractModel):
    r"""DeleteCodeFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 执行结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFileActionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""执行结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFileActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeStudioFileActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteCodeFolderRequest(AbstractModel):
    r"""DeleteCodeFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _FolderId: 文件夹ID，参数值来自CreateCodeFolder接口的返回
        :type FolderId: str
        """
        self._ProjectId = None
        self._FolderId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""文件夹ID，参数值来自CreateCodeFolder接口的返回
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeFolderResponse(AbstractModel):
    r"""DeleteCodeFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 执行结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderActionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""执行结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeStudioFolderActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteFolderResult(AbstractModel):
    r"""删除资源文件夹结果

    """

    def __init__(self):
        r"""
        :param _Status: 删除状态,true表示成功，false表示失败
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""删除状态,true表示成功，false表示失败
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
        


class DeleteOpsAlarmRuleRequest(AbstractModel):
    r"""DeleteOpsAlarmRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _AlarmRuleId: 告警规则唯一id，接口CreateAlarmRule返回
与AlarmRuleName二选一
        :type AlarmRuleId: str
        """
        self._ProjectId = None
        self._AlarmRuleId = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmRuleId(self):
        r"""告警规则唯一id，接口CreateAlarmRule返回
与AlarmRuleName二选一
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmRuleId = params.get("AlarmRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOpsAlarmRuleResponse(AbstractModel):
    r"""DeleteOpsAlarmRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 是否删除成功
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteAlarmRuleResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""是否删除成功
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteAlarmRuleResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteAlarmRuleResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteResourceFileRequest(AbstractModel):
    r"""DeleteResourceFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ResourceId: 资源ID, 可通过ListResourceFiles接口获取
        :type ResourceId: str
        """
        self._ProjectId = None
        self._ResourceId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceId(self):
        r"""资源ID, 可通过ListResourceFiles接口获取
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceFileResponse(AbstractModel):
    r"""DeleteResourceFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 资源删除结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFileResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""资源删除结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFileResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteResourceFileResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteResourceFileResult(AbstractModel):
    r"""删除资源文件结果

    """

    def __init__(self):
        r"""
        :param _Status: true
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""true
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
        


class DeleteResourceFolderRequest(AbstractModel):
    r"""DeleteResourceFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _FolderId: 文件夹ID, 可通过ListResourceFolders接口获取
        :type FolderId: str
        """
        self._ProjectId = None
        self._FolderId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""文件夹ID, 可通过ListResourceFolders接口获取
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceFolderResponse(AbstractModel):
    r"""DeleteResourceFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: true代表删除成功，false代表删除失败
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteFolderResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""true代表删除成功，false代表删除失败
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteSQLFolderRequest(AbstractModel):
    r"""DeleteSQLFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FolderId: 文件夹Id
        :type FolderId: str
        :param _ProjectId: 项目id
        :type ProjectId: str
        """
        self._FolderId = None
        self._ProjectId = None

    @property
    def FolderId(self):
        r"""文件夹Id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSQLFolderResponse(AbstractModel):
    r"""DeleteSQLFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 操作结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""操作结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLContentActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteSQLScriptRequest(AbstractModel):
    r"""DeleteSQLScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScriptId: 探索脚本Id
        :type ScriptId: str
        :param _ProjectId: 项目Id
        :type ProjectId: str
        """
        self._ScriptId = None
        self._ProjectId = None

    @property
    def ScriptId(self):
        r"""探索脚本Id
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSQLScriptResponse(AbstractModel):
    r"""DeleteSQLScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 执行结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""执行结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLContentActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteTaskRequest(AbstractModel):
    r"""DeleteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _TaskId: 任务ID
和VirtualTaskId选填一个
        :type TaskId: str
        :param _OperateInform: 任务操作是否消息通知下游任务责任人true：通知
false：不通知
不传默认false
        :type OperateInform: bool
        :param _DeleteMode: 任务删除方式
true：不针对下游任务实例进行强制失败
false：针对下游任务实例进行强制失败
不传默认false

        :type DeleteMode: bool
        """
        self._ProjectId = None
        self._TaskId = None
        self._OperateInform = None
        self._DeleteMode = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务ID
和VirtualTaskId选填一个
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def OperateInform(self):
        r"""任务操作是否消息通知下游任务责任人true：通知
false：不通知
不传默认false
        :rtype: bool
        """
        return self._OperateInform

    @OperateInform.setter
    def OperateInform(self, OperateInform):
        self._OperateInform = OperateInform

    @property
    def DeleteMode(self):
        r"""任务删除方式
true：不针对下游任务实例进行强制失败
false：针对下游任务实例进行强制失败
不传默认false

        :rtype: bool
        """
        return self._DeleteMode

    @DeleteMode.setter
    def DeleteMode(self, DeleteMode):
        self._DeleteMode = DeleteMode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._OperateInform = params.get("OperateInform")
        self._DeleteMode = params.get("DeleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskResponse(AbstractModel):
    r"""DeleteTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 是否删除成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""是否删除成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteTaskResult(AbstractModel):
    r"""删除数据开发任务结果

    """

    def __init__(self):
        r"""
        :param _Status: 删除状态,true表示成功，false表示失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""删除状态,true表示成功，false表示失败
注意：此字段可能返回 null，表示取不到有效值。
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
        


class DeleteWorkflowFolderRequest(AbstractModel):
    r"""DeleteWorkflowFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _FolderId: 文件夹ID，可通过ListWorkflowFolders接口获取
        :type FolderId: str
        """
        self._ProjectId = None
        self._FolderId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""文件夹ID，可通过ListWorkflowFolders接口获取
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowFolderResponse(AbstractModel):
    r"""DeleteWorkflowFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 删除结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteFolderResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""删除结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteWorkflowRequest(AbstractModel):
    r"""DeleteWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _WorkflowId: 工作流id
        :type WorkflowId: str
        """
        self._ProjectId = None
        self._WorkflowId = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowId(self):
        r"""工作流id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowResponse(AbstractModel):
    r"""DeleteWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回删除成功的工作流任务个数、失败个数、任务总数
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回删除成功的工作流任务个数、失败个数、任务总数
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteWorkflowResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteWorkflowResult(AbstractModel):
    r"""删除工作流结果

    """

    def __init__(self):
        r"""
        :param _Status: 删除工作流是否成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""删除工作流是否成功
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
        


class DependencyConfigPage(AbstractModel):
    r"""查询任务上游依赖详情分页

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足查询条件的数据总条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 满足查询条件的数据总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _PageNumber: 当前请求的数据页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 当前请求的数据页条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _Items: 分页数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of TaskDependDto
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._Items = None

    @property
    def TotalCount(self):
        r"""满足查询条件的数据总条数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""满足查询条件的数据总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""当前请求的数据页数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""当前请求的数据页条数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Items(self):
        r"""分页数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskDependDto
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskDependDto()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DependencyStrategyTask(AbstractModel):
    r"""依赖配置策略

    """

    def __init__(self):
        r"""
        :param _PollingNullStrategy: 等待上游任务实例策略：EXECUTING（执行）；WAITING（等待）

注意：此字段可能返回 null，表示取不到有效值。
        :type PollingNullStrategy: str
        :param _TaskDependencyExecutingStrategies: 仅当PollingNullStrategy为EXECUTING时才需要填本字段，List类型：NOT_EXIST（默认，在分钟依赖分钟/小时依赖小时的情况下，父实例不在下游实例调度时间范围内）；PARENT_EXPIRED（父实例失败）；PARENT_TIMEOUT（父实例超时）。以上场景满足任一条件即可通过该父任务实例依赖判断，除以上场景外均需等待父实例。

注意：此字段可能返回 null，表示取不到有效值。
        :type TaskDependencyExecutingStrategies: list of str
        :param _TaskDependencyExecutingTimeoutValue: 仅当TaskDependencyExecutingStrategies中包含PARENT_TIMEOUT时才需要填本字段，下游任务依赖父实例执行超时时间，单位：分钟。

注意：此字段可能返回 null，表示取不到有效值。
        :type TaskDependencyExecutingTimeoutValue: int
        """
        self._PollingNullStrategy = None
        self._TaskDependencyExecutingStrategies = None
        self._TaskDependencyExecutingTimeoutValue = None

    @property
    def PollingNullStrategy(self):
        r"""等待上游任务实例策略：EXECUTING（执行）；WAITING（等待）

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PollingNullStrategy

    @PollingNullStrategy.setter
    def PollingNullStrategy(self, PollingNullStrategy):
        self._PollingNullStrategy = PollingNullStrategy

    @property
    def TaskDependencyExecutingStrategies(self):
        r"""仅当PollingNullStrategy为EXECUTING时才需要填本字段，List类型：NOT_EXIST（默认，在分钟依赖分钟/小时依赖小时的情况下，父实例不在下游实例调度时间范围内）；PARENT_EXPIRED（父实例失败）；PARENT_TIMEOUT（父实例超时）。以上场景满足任一条件即可通过该父任务实例依赖判断，除以上场景外均需等待父实例。

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TaskDependencyExecutingStrategies

    @TaskDependencyExecutingStrategies.setter
    def TaskDependencyExecutingStrategies(self, TaskDependencyExecutingStrategies):
        self._TaskDependencyExecutingStrategies = TaskDependencyExecutingStrategies

    @property
    def TaskDependencyExecutingTimeoutValue(self):
        r"""仅当TaskDependencyExecutingStrategies中包含PARENT_TIMEOUT时才需要填本字段，下游任务依赖父实例执行超时时间，单位：分钟。

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskDependencyExecutingTimeoutValue

    @TaskDependencyExecutingTimeoutValue.setter
    def TaskDependencyExecutingTimeoutValue(self, TaskDependencyExecutingTimeoutValue):
        self._TaskDependencyExecutingTimeoutValue = TaskDependencyExecutingTimeoutValue


    def _deserialize(self, params):
        self._PollingNullStrategy = params.get("PollingNullStrategy")
        self._TaskDependencyExecutingStrategies = params.get("TaskDependencyExecutingStrategies")
        self._TaskDependencyExecutingTimeoutValue = params.get("TaskDependencyExecutingTimeoutValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DependencyTaskBrief(AbstractModel):
    r"""依赖任务信息

    取值说明表：

    | 当前任务周期类型 | 上游任务周期类型 | 配置方式 | MainCyclicConfig取值 | 时间维度/实例范围           | SubordinateCyclicConfig取值       | offset取值             |
    | ---------------- | ---------------- | -------- | -------------------- | --------------------------- | --------------------------------- | ---------------------- |
    | HOUR_CYCLE       | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | MINUTE_CYCLE     | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | DAY_CYCLE        | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | DAY_CYCLE        | WEEK_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | HOUR_CYCLE       | HOUR_CYCLE       | 推荐策略 | HOUR                 | 按小时/最近实例             | CURRENT_HOUR                      | 无                     |
    | HOUR_CYCLE       | HOUR_CYCLE       | 推荐策略 | HOUR                 | 按小时/前一周期             | PREVIOUS_HOUR_CYCLE               | 无                     |
    | HOUR_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | WEEK                 | 按周/上周                   | PREVIOUS_WEEK                     | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | WEEK                 | 按周/上周五                 | PREVIOUS_FRIDAY                   | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | WEEK                 | 按周/上周日                 | PREVIOUS_WEEKEND                  | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天         、          | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/前一天                 | PREVIOUS_DAY                      | 无                     |
    | WEEK_CYCLE       | ONEOFF_CYCLE     | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 推荐策略 | HOUR                 | 按小时/前一个小时(-60,0]    | PREVIOUS_HOUR_LATER_OFFSET_MINUTE | 无                     |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 推荐策略 | HOUR                 | 按小时/前一个小时           | PREVIOUS_HOUR                     | 无                     |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 推荐策略 | HOUR                 | 按小时/当前小时             | CURRENT_HOUR                      | 无                     |
    | YEAR_CYCLE       | WEEK_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | WEEK_CYCLE       | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | MINUTE_CYCLE     | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | WEEK_CYCLE       | HOUR_CYCLE       | 推荐策略 | WEEK                 | 按周/上周                   | PREVIOUS_WEEK                     | 无                     |
    | WEEK_CYCLE       | HOUR_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | MINUTE_CYCLE     | HOUR_CYCLE       | 推荐策略 | HOUR                 | 按小时/当前小时             | CURRENT_HOUR                      | 无                     |
    | HOUR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | HOUR_CYCLE       | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | MONTH_CYCLE      | HOUR_CYCLE       | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | ONEOFF_CYCLE     | 推荐策略 | MONTH                | 按月/当月                   | CURRENT_MONTH                     | 无                     |
    | DAY_CYCLE        | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | DAY_CYCLE        | MONTH_CYCLE      | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | MONTH_CYCLE      | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | ONEOFF_CYCLE     | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | MINUTE_CYCLE     | MINUTE_CYCLE     | 推荐策略 | MINUTE               | 按分钟/当前分钟             | CURRENT_MINUTE                    | 无                     |
    | MINUTE_CYCLE     | MINUTE_CYCLE     | 推荐策略 | MINUTE               | 按分钟/前一周期             | PREVIOUS_MINUTE_CYCLE             | 无                     |
    | YEAR_CYCLE       | MINUTE_CYCLE     | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | ONEOFF_CYCLE     | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | DAY_CYCLE        | MINUTE_CYCLE     | 推荐策略 | DAY                  | 按天/前一天(-24 * 60,0]     | PREVIOUS_DAY_LATER_OFFSET_MINUTE  | 无                     |
    | DAY_CYCLE        | MINUTE_CYCLE     | 推荐策略 | DAY                  | 按天/前一天                 | PREVIOUS_DAY                      | 无                     |
    | DAY_CYCLE        | MINUTE_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | MINUTE_CYCLE     | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | WEEK_CYCLE       | WEEK_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | YEAR_CYCLE       | YEAR_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | YEAR_CYCLE       | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | YEAR_CYCLE       | HOUR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | MINUTE_CYCLE     | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | ONEOFF_CYCLE     | MINUTE_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | HOUR_CYCLE       | ONEOFF_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | MINUTE_CYCLE     | 推荐策略 | WEEK                 | 按周/上周                   | PREVIOUS_WEEK                     | 无                     |
    | WEEK_CYCLE       | MINUTE_CYCLE     | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | DAY_CYCLE        | HOUR_CYCLE       | 推荐策略 | DAY                  | 按天/前一天(-24,0]          | PREVIOUS_DAY_LATER_OFFSET_HOUR    | 无                     |
    | DAY_CYCLE        | HOUR_CYCLE       | 推荐策略 | DAY                  | 按天/前一天[-24,0)          | PREVIOUS_DAY                      | 无                     |
    | DAY_CYCLE        | HOUR_CYCLE       | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本年所有月             | ALL_MONTH_OF_YEAR                 | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/上月末                 | PREVIOUS_END_OF_MONTH             | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/上月初                 | PREVIOUS_BEGIN_OF_MONTH           | 无                     |
    | ONEOFF_CYCLE     | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | DAY_CYCLE        | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | ONEOFF_CYCLE     | HOUR_CYCLE       | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | DAY_CYCLE        | ONEOFF_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | MINUTE_CYCLE     | ONEOFF_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | WEEK_CYCLE       | MONTH_CYCLE      | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | YEAR_CYCLE       | ONEOFF_CYCLE     | 推荐策略 | YEAR                 | 按年/当年                   | CURRENT_YEAR                      | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | MONTH                | 按月/上月末                 | PREVIOUS_END_OF_MONTH             | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/前一天                 | PREVIOUS_DAY                      | 无                     |
    | YEAR_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/本年所有天             | ALL_DAY_OF_YEAR                   | 无                     |
    | YEAR_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | YEAR_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/前一天                 | PREVIOUS_DAY                      | 无                     |
    | HOUR_CYCLE       | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | MONTH_CYCLE      | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/当月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | MONTH_CYCLE      | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | MONTH_CYCLE      | MINUTE_CYCLE     | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | MONTH_CYCLE      | MINUTE_CYCLE     | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | WEEK_CYCLE       | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | MONTH_CYCLE      | WEEK_CYCLE       | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | WEEK_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | DAY_CYCLE        | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | DAY_CYCLE        | YEAR_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | ONEOFF_CYCLE     | ONEOFF_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | ONEOFF_CYCLE     | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | CRONTAB_CYCLE    | CRONTAB_CYCLE    | 推荐策略 | CRONTAB              | 无                          | CURRENT                           | 无                     |
    | HOUR_CYCLE       | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _MainCyclicConfig: 主依赖配置，取值为：

* CRONTAB
* DAY
* HOUR
* LIST_DAY
* LIST_HOUR
* LIST_MINUTE
* MINUTE
* MONTH
* RANGE_DAY
* RANGE_HOUR
* RANGE_MINUTE
* WEEK
* YEAR
注意：此字段可能返回 null，表示取不到有效值。
        :type MainCyclicConfig: str
        :param _SubordinateCyclicConfig: 次依赖配置，取值为：
* ALL_DAY_OF_YEAR
* ALL_MONTH_OF_YEAR
* CURRENT
* CURRENT_DAY
* CURRENT_HOUR
* CURRENT_MINUTE
* CURRENT_MONTH
* CURRENT_WEEK
* CURRENT_YEAR
* PREVIOUS_BEGIN_OF_MONTH
* PREVIOUS_DAY
* PREVIOUS_DAY_LATER_OFFSET_HOUR
* PREVIOUS_DAY_LATER_OFFSET_MINUTE
* PREVIOUS_END_OF_MONTH
* PREVIOUS_FRIDAY
* PREVIOUS_HOUR
* PREVIOUS_HOUR_CYCLE
* PREVIOUS_HOUR_LATER_OFFSET_MINUTE
* PREVIOUS_MINUTE_CYCLE
* PREVIOUS_MONTH
* PREVIOUS_WEEK
* PREVIOUS_WEEKEND
* RECENT_DATE
注意：此字段可能返回 null，表示取不到有效值。
        :type SubordinateCyclicConfig: str
        :param _Offset: 区间、列表模式下的偏移量
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: str
        :param _DependencyStrategy: 依赖执行策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DependencyStrategy: :class:`tencentcloud.wedata.v20250806.models.DependencyStrategyTask`
        """
        self._TaskId = None
        self._MainCyclicConfig = None
        self._SubordinateCyclicConfig = None
        self._Offset = None
        self._DependencyStrategy = None

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MainCyclicConfig(self):
        r"""主依赖配置，取值为：

* CRONTAB
* DAY
* HOUR
* LIST_DAY
* LIST_HOUR
* LIST_MINUTE
* MINUTE
* MONTH
* RANGE_DAY
* RANGE_HOUR
* RANGE_MINUTE
* WEEK
* YEAR
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MainCyclicConfig

    @MainCyclicConfig.setter
    def MainCyclicConfig(self, MainCyclicConfig):
        self._MainCyclicConfig = MainCyclicConfig

    @property
    def SubordinateCyclicConfig(self):
        r"""次依赖配置，取值为：
* ALL_DAY_OF_YEAR
* ALL_MONTH_OF_YEAR
* CURRENT
* CURRENT_DAY
* CURRENT_HOUR
* CURRENT_MINUTE
* CURRENT_MONTH
* CURRENT_WEEK
* CURRENT_YEAR
* PREVIOUS_BEGIN_OF_MONTH
* PREVIOUS_DAY
* PREVIOUS_DAY_LATER_OFFSET_HOUR
* PREVIOUS_DAY_LATER_OFFSET_MINUTE
* PREVIOUS_END_OF_MONTH
* PREVIOUS_FRIDAY
* PREVIOUS_HOUR
* PREVIOUS_HOUR_CYCLE
* PREVIOUS_HOUR_LATER_OFFSET_MINUTE
* PREVIOUS_MINUTE_CYCLE
* PREVIOUS_MONTH
* PREVIOUS_WEEK
* PREVIOUS_WEEKEND
* RECENT_DATE
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubordinateCyclicConfig

    @SubordinateCyclicConfig.setter
    def SubordinateCyclicConfig(self, SubordinateCyclicConfig):
        self._SubordinateCyclicConfig = SubordinateCyclicConfig

    @property
    def Offset(self):
        r"""区间、列表模式下的偏移量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DependencyStrategy(self):
        r"""依赖执行策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DependencyStrategyTask`
        """
        return self._DependencyStrategy

    @DependencyStrategy.setter
    def DependencyStrategy(self, DependencyStrategy):
        self._DependencyStrategy = DependencyStrategy


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._MainCyclicConfig = params.get("MainCyclicConfig")
        self._SubordinateCyclicConfig = params.get("SubordinateCyclicConfig")
        self._Offset = params.get("Offset")
        if params.get("DependencyStrategy") is not None:
            self._DependencyStrategy = DependencyStrategyTask()
            self._DependencyStrategy._deserialize(params.get("DependencyStrategy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventListener(AbstractModel):
    r"""监听事件器

    """

    def __init__(self):
        r"""
        :param _EventName: 事件名
注意：此字段可能返回 null，表示取不到有效值。
        :type EventName: str
        :param _EventSubType: 事件周期：SECOND, MIN, HOUR, DAY
注意：此字段可能返回 null，表示取不到有效值。
        :type EventSubType: str
        :param _EventBroadcastType: 事件广播类型：SINGLE, BROADCAST
注意：此字段可能返回 null，表示取不到有效值。
        :type EventBroadcastType: str
        :param _PropertiesList: 扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PropertiesList: list of ParamInfo
        """
        self._EventName = None
        self._EventSubType = None
        self._EventBroadcastType = None
        self._PropertiesList = None

    @property
    def EventName(self):
        r"""事件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def EventSubType(self):
        r"""事件周期：SECOND, MIN, HOUR, DAY
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventSubType

    @EventSubType.setter
    def EventSubType(self, EventSubType):
        self._EventSubType = EventSubType

    @property
    def EventBroadcastType(self):
        r"""事件广播类型：SINGLE, BROADCAST
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventBroadcastType

    @EventBroadcastType.setter
    def EventBroadcastType(self, EventBroadcastType):
        self._EventBroadcastType = EventBroadcastType

    @property
    def PropertiesList(self):
        r"""扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamInfo
        """
        return self._PropertiesList

    @PropertiesList.setter
    def PropertiesList(self, PropertiesList):
        self._PropertiesList = PropertiesList


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        self._EventSubType = params.get("EventSubType")
        self._EventBroadcastType = params.get("EventBroadcastType")
        if params.get("PropertiesList") is not None:
            self._PropertiesList = []
            for item in params.get("PropertiesList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._PropertiesList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmMessageRequest(AbstractModel):
    r"""GetAlarmMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目Id
        :type ProjectId: str
        :param _AlarmMessageId: 告警消息Id
        :type AlarmMessageId: str
        :param _TimeZone: 返回日期的时区, 默认UTC+8
        :type TimeZone: str
        """
        self._ProjectId = None
        self._AlarmMessageId = None
        self._TimeZone = None

    @property
    def ProjectId(self):
        r"""所属项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmMessageId(self):
        r"""告警消息Id
        :rtype: str
        """
        return self._AlarmMessageId

    @AlarmMessageId.setter
    def AlarmMessageId(self, AlarmMessageId):
        self._AlarmMessageId = AlarmMessageId

    @property
    def TimeZone(self):
        r"""返回日期的时区, 默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmMessageId = params.get("AlarmMessageId")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmMessageResponse(AbstractModel):
    r"""GetAlarmMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 告警信息
        :type Data: :class:`tencentcloud.wedata.v20250806.models.AlarmMessage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""告警信息
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmMessage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AlarmMessage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetCodeFileRequest(AbstractModel):
    r"""GetCodeFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _CodeFileId: 代码文件ID，参数值来自CreateCodeFile接口的返回
        :type CodeFileId: str
        :param _IncludeContent: true：返回文件内容+配置，false：不返回文件内容，只返回配置信息；默认为false
        :type IncludeContent: bool
        """
        self._ProjectId = None
        self._CodeFileId = None
        self._IncludeContent = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeFileId(self):
        r"""代码文件ID，参数值来自CreateCodeFile接口的返回
        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId

    @property
    def IncludeContent(self):
        r"""true：返回文件内容+配置，false：不返回文件内容，只返回配置信息；默认为false
        :rtype: bool
        """
        return self._IncludeContent

    @IncludeContent.setter
    def IncludeContent(self, IncludeContent):
        self._IncludeContent = IncludeContent


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CodeFileId = params.get("CodeFileId")
        self._IncludeContent = params.get("IncludeContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCodeFileResponse(AbstractModel):
    r"""GetCodeFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 代码文件详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""代码文件详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeFile()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsAlarmRuleRequest(AbstractModel):
    r"""GetOpsAlarmRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _AlarmRuleId: 告警规则唯一id
        :type AlarmRuleId: str
        """
        self._ProjectId = None
        self._AlarmRuleId = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmRuleId(self):
        r"""告警规则唯一id
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmRuleId = params.get("AlarmRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsAlarmRuleResponse(AbstractModel):
    r"""GetOpsAlarmRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 告警规则详细信息
        :type Data: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""告警规则详细信息
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AlarmRuleData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsAsyncJobRequest(AbstractModel):
    r"""GetOpsAsyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _AsyncId: 异步操作id
        :type AsyncId: str
        """
        self._ProjectId = None
        self._AsyncId = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AsyncId(self):
        r"""异步操作id
        :rtype: str
        """
        return self._AsyncId

    @AsyncId.setter
    def AsyncId(self, AsyncId):
        self._AsyncId = AsyncId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AsyncId = params.get("AsyncId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsAsyncJobResponse(AbstractModel):
    r"""GetOpsAsyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 异步操作详情结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncJobDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""异步操作详情结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncJobDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncJobDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsTaskCodeRequest(AbstractModel):
    r"""GetOpsTaskCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目id
        :type ProjectId: str
        :param _TaskId: 任务Id
        :type TaskId: str
        """
        self._ProjectId = None
        self._TaskId = None

    @property
    def ProjectId(self):
        r"""所属项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsTaskCodeResponse(AbstractModel):
    r"""GetOpsTaskCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 获取任务代码结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskCode`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""获取任务代码结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskCode`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskCode()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsTaskRequest(AbstractModel):
    r"""GetOpsTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id	
        :type TaskId: str
        :param _ProjectId: 项目Id
        :type ProjectId: str
        """
        self._TaskId = None
        self._ProjectId = None

    @property
    def TaskId(self):
        r"""任务Id	
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsTaskResponse(AbstractModel):
    r"""GetOpsTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.Task`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.Task`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsWorkflowRequest(AbstractModel):
    r"""GetOpsWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _WorkflowId: 工作流Id，可以从ListOpsWorkflows接口获取
        :type WorkflowId: str
        """
        self._ProjectId = None
        self._WorkflowId = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowId(self):
        r"""工作流Id，可以从ListOpsWorkflows接口获取
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsWorkflowResponse(AbstractModel):
    r"""GetOpsWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 工作流调度详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsWorkflowDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""工作流调度详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsWorkflowDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsWorkflowDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetResourceFileRequest(AbstractModel):
    r"""GetResourceFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ResourceId: 资源文件ID,可通过ListResourceFiles接口获取
        :type ResourceId: str
        """
        self._ProjectId = None
        self._ResourceId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceId(self):
        r"""资源文件ID,可通过ListResourceFiles接口获取
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourceFileResponse(AbstractModel):
    r"""GetResourceFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 资源文件详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ResourceFile`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""资源文件详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ResourceFile`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResourceFile()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetSQLScriptRequest(AbstractModel):
    r"""GetSQLScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScriptId: 探索脚本Id
        :type ScriptId: str
        :param _ProjectId: 项目Id
        :type ProjectId: str
        """
        self._ScriptId = None
        self._ProjectId = None

    @property
    def ScriptId(self):
        r"""探索脚本Id
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSQLScriptResponse(AbstractModel):
    r"""GetSQLScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 脚本详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""脚本详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLScript()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskCodeRequest(AbstractModel):
    r"""GetTaskCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目id
        :type ProjectId: str
        :param _TaskId: 任务Id
        :type TaskId: str
        """
        self._ProjectId = None
        self._TaskId = None

    @property
    def ProjectId(self):
        r"""所属项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskCodeResponse(AbstractModel):
    r"""GetTaskCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 获取任务代码结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskCodeResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""获取任务代码结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskCodeResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskCodeResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskInstanceLogRequest(AbstractModel):
    r"""GetTaskInstanceLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: **项目ID**
        :type ProjectId: str
        :param _InstanceKey: **实例唯一标识**
        :type InstanceKey: str
        :param _LifeRoundNum: **实例生命周期编号，标识实例的某一次执行**例如：周期实例第一次运行的编号为0，用户后期又重跑了该实例，第二次执行的编号为1; 默认最新一次
        :type LifeRoundNum: int
        :param _LogLevel: **日志级别** 默认All - Info - Debug - Warn - Error - All
        :type LogLevel: str
        :param _NextCursor: **分页查询日志时使用，无具体业务含义** 第一次查询时值为null 第二次及以后查询时使用上一次查询返回信息中的NextCursor字段值即可
        :type NextCursor: str
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._LifeRoundNum = None
        self._LogLevel = None
        self._NextCursor = None

    @property
    def ProjectId(self):
        r"""**项目ID**
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**实例唯一标识**
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def LifeRoundNum(self):
        r"""**实例生命周期编号，标识实例的某一次执行**例如：周期实例第一次运行的编号为0，用户后期又重跑了该实例，第二次执行的编号为1; 默认最新一次
        :rtype: int
        """
        return self._LifeRoundNum

    @LifeRoundNum.setter
    def LifeRoundNum(self, LifeRoundNum):
        self._LifeRoundNum = LifeRoundNum

    @property
    def LogLevel(self):
        r"""**日志级别** 默认All - Info - Debug - Warn - Error - All
        :rtype: str
        """
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def NextCursor(self):
        r"""**分页查询日志时使用，无具体业务含义** 第一次查询时值为null 第二次及以后查询时使用上一次查询返回信息中的NextCursor字段值即可
        :rtype: str
        """
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._LifeRoundNum = params.get("LifeRoundNum")
        self._LogLevel = params.get("LogLevel")
        self._NextCursor = params.get("NextCursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskInstanceLogResponse(AbstractModel):
    r"""GetTaskInstanceLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 调度实例详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.InstanceLog`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""调度实例详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.InstanceLog`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = InstanceLog()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskInstanceRequest(AbstractModel):
    r"""GetTaskInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目id
        :type ProjectId: str
        :param _InstanceKey: 实例唯一标识，可以通过ListInstances获取
        :type InstanceKey: str
        :param _TimeZone: **时区**timeZone, 传入的时间字符串的所在时区，默认UTC+8
        :type TimeZone: str
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._TimeZone = None

    @property
    def ProjectId(self):
        r"""所属项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""实例唯一标识，可以通过ListInstances获取
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def TimeZone(self):
        r"""**时区**timeZone, 传入的时间字符串的所在时区，默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskInstanceResponse(AbstractModel):
    r"""GetTaskInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 实例详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstanceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""实例详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstanceDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstanceDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskRequest(AbstractModel):
    r"""GetTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._ProjectId = None
        self._TaskId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskResponse(AbstractModel):
    r"""GetTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.Task`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.Task`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskVersionRequest(AbstractModel):
    r"""GetTaskVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _VersionId: 提交版本ID，不填默认拿最新提交版本
        :type VersionId: str
        """
        self._ProjectId = None
        self._TaskId = None
        self._VersionId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def VersionId(self):
        r"""提交版本ID，不填默认拿最新提交版本
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskVersionResponse(AbstractModel):
    r"""GetTaskVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 版本详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskVersionDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""版本详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskVersionDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskVersionDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetWorkflowRequest(AbstractModel):
    r"""GetWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _WorkflowId: 工作流ID 通过ListWorkflows接口获取
        :type WorkflowId: str
        """
        self._ProjectId = None
        self._WorkflowId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowId(self):
        r"""工作流ID 通过ListWorkflows接口获取
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkflowResponse(AbstractModel):
    r"""GetWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 工作流详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.WorkflowDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""工作流详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = WorkflowDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class InTaskParameter(AbstractModel):
    r"""参数传递-引用参数

    """

    def __init__(self):
        r"""
        :param _ParamKey: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamKey: str
        :param _ParamDesc: 参数描述：格式为 项目标识.任务名称.参数名；例：project_wedata_1.sh_250820_104107.pp_out
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamDesc: str
        :param _FromTaskId: 父任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FromTaskId: str
        :param _FromParamKey: 父任务参数key
注意：此字段可能返回 null，表示取不到有效值。
        :type FromParamKey: str
        """
        self._ParamKey = None
        self._ParamDesc = None
        self._FromTaskId = None
        self._FromParamKey = None

    @property
    def ParamKey(self):
        r"""参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamDesc(self):
        r"""参数描述：格式为 项目标识.任务名称.参数名；例：project_wedata_1.sh_250820_104107.pp_out
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamDesc

    @ParamDesc.setter
    def ParamDesc(self, ParamDesc):
        self._ParamDesc = ParamDesc

    @property
    def FromTaskId(self):
        r"""父任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FromTaskId

    @FromTaskId.setter
    def FromTaskId(self, FromTaskId):
        self._FromTaskId = FromTaskId

    @property
    def FromParamKey(self):
        r"""父任务参数key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FromParamKey

    @FromParamKey.setter
    def FromParamKey(self, FromParamKey):
        self._FromParamKey = FromParamKey


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamDesc = params.get("ParamDesc")
        self._FromTaskId = params.get("FromTaskId")
        self._FromParamKey = params.get("FromParamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExecution(AbstractModel):
    r"""调度实例详情

    """

    def __init__(self):
        r"""
        :param _InstanceKey: 实例唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceKey: str
        :param _LifeRoundNum: **实例生命周期编号，标识实例的某一次执行**

例如：周期实例第一次运行的编号为0，用户后期又重跑了该实例，第二次执行的编号为1
注意：此字段可能返回 null，表示取不到有效值。
        :type LifeRoundNum: int
        :param _InstanceState: **实例状态**
- WAIT_EVENT: 等待事件
- WAIT_UPSTREAM: 等待上游
- WAIT_RUN: 等待运行
- RUNNING: 运行中
- SKIP_RUNNING: 跳过运行
- FAILED_RETRY: 失败重试
- EXPIRED: 失败
- COMPLETED: 成功
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceState: str
        :param _RunType: **实例运行触发类型**

- RERUN 表示重跑
- ADDITION 表示补录
- PERIODIC 表示周期
- APERIODIC 表示非周期
- RERUN_SKIP_RUN 表示重跑 - 空跑
- ADDITION_SKIP_RUN 表示补录 - 空跑
- PERIODIC_SKIP_RUN 表示周期 - 空跑
- APERIODIC_SKIP_RUN 表示非周期 - 空跑
- MANUAL_TRIGGER 表示手动触发
- RERUN_MANUAL_TRIGGER 表示手动触发 - 重跑
注意：此字段可能返回 null，表示取不到有效值。
        :type RunType: str
        :param _Tries: 失败重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Tries: int
        :param _ExecutionPhaseList: **实例执行生命周期列表**
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionPhaseList: list of InstanceExecutionPhase
        :param _CostTime: 耗费时间, 单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: int
        """
        self._InstanceKey = None
        self._LifeRoundNum = None
        self._InstanceState = None
        self._RunType = None
        self._Tries = None
        self._ExecutionPhaseList = None
        self._CostTime = None

    @property
    def InstanceKey(self):
        r"""实例唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def LifeRoundNum(self):
        r"""**实例生命周期编号，标识实例的某一次执行**

例如：周期实例第一次运行的编号为0，用户后期又重跑了该实例，第二次执行的编号为1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LifeRoundNum

    @LifeRoundNum.setter
    def LifeRoundNum(self, LifeRoundNum):
        self._LifeRoundNum = LifeRoundNum

    @property
    def InstanceState(self):
        r"""**实例状态**
- WAIT_EVENT: 等待事件
- WAIT_UPSTREAM: 等待上游
- WAIT_RUN: 等待运行
- RUNNING: 运行中
- SKIP_RUNNING: 跳过运行
- FAILED_RETRY: 失败重试
- EXPIRED: 失败
- COMPLETED: 成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def RunType(self):
        r"""**实例运行触发类型**

- RERUN 表示重跑
- ADDITION 表示补录
- PERIODIC 表示周期
- APERIODIC 表示非周期
- RERUN_SKIP_RUN 表示重跑 - 空跑
- ADDITION_SKIP_RUN 表示补录 - 空跑
- PERIODIC_SKIP_RUN 表示周期 - 空跑
- APERIODIC_SKIP_RUN 表示非周期 - 空跑
- MANUAL_TRIGGER 表示手动触发
- RERUN_MANUAL_TRIGGER 表示手动触发 - 重跑
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunType

    @RunType.setter
    def RunType(self, RunType):
        self._RunType = RunType

    @property
    def Tries(self):
        r"""失败重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def ExecutionPhaseList(self):
        r"""**实例执行生命周期列表**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceExecutionPhase
        """
        return self._ExecutionPhaseList

    @ExecutionPhaseList.setter
    def ExecutionPhaseList(self, ExecutionPhaseList):
        self._ExecutionPhaseList = ExecutionPhaseList

    @property
    def CostTime(self):
        r"""耗费时间, 单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._LifeRoundNum = params.get("LifeRoundNum")
        self._InstanceState = params.get("InstanceState")
        self._RunType = params.get("RunType")
        self._Tries = params.get("Tries")
        if params.get("ExecutionPhaseList") is not None:
            self._ExecutionPhaseList = []
            for item in params.get("ExecutionPhaseList"):
                obj = InstanceExecutionPhase()
                obj._deserialize(item)
                self._ExecutionPhaseList.append(obj)
        self._CostTime = params.get("CostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExecutionPhase(AbstractModel):
    r"""实例执行的每个阶段详情

    """

    def __init__(self):
        r"""
        :param _StartTime: 该状态开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _DetailState: **实例生命周期阶段状态**

- WAIT_UPSTREAM 表示 等待事件/上游状态
- WAIT_RUN 表示 等待运行状态
- RUNNING 表示 运行中状态
- COMPLETE 表示 终态-完成
- FAILED 表示 终态-失败重试
- EXPIRED 表示 终态-失败
- SKIP_RUNNING 表示 终态-被上游分支节点跳过的分支
- HISTORY 表示 兼容2024-03-30之前的历史实例，之后实例无需关注次枚举类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailState: str
        :param _EndTime: 该状态结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._StartTime = None
        self._DetailState = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""该状态开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def DetailState(self):
        r"""**实例生命周期阶段状态**

- WAIT_UPSTREAM 表示 等待事件/上游状态
- WAIT_RUN 表示 等待运行状态
- RUNNING 表示 运行中状态
- COMPLETE 表示 终态-完成
- FAILED 表示 终态-失败重试
- EXPIRED 表示 终态-失败
- SKIP_RUNNING 表示 终态-被上游分支节点跳过的分支
- HISTORY 表示 兼容2024-03-30之前的历史实例，之后实例无需关注次枚举类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DetailState

    @DetailState.setter
    def DetailState(self, DetailState):
        self._DetailState = DetailState

    @property
    def EndTime(self):
        r"""该状态结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._DetailState = params.get("DetailState")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    r"""实例日志内容

    """

    def __init__(self):
        r"""
        :param _InstanceKey: 实例唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceKey: str
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _CodeContent: **运行代码内容**
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeContent: str
        :param _LogInfo: **日志内容**
注意：此字段可能返回 null，表示取不到有效值。
        :type LogInfo: str
        :param _NextCursor: **分页查询日志时使用，无具体业务含义**

第一次查询时值为null 
第二次及以后查询时使用上一次查询返回信息中的NextCursor字段值即可
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        """
        self._InstanceKey = None
        self._ProjectId = None
        self._CodeContent = None
        self._LogInfo = None
        self._NextCursor = None

    @property
    def InstanceKey(self):
        r"""实例唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ProjectId(self):
        r"""项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeContent(self):
        r"""**运行代码内容**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CodeContent

    @CodeContent.setter
    def CodeContent(self, CodeContent):
        self._CodeContent = CodeContent

    @property
    def LogInfo(self):
        r"""**日志内容**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogInfo

    @LogInfo.setter
    def LogInfo(self, LogInfo):
        self._LogInfo = LogInfo

    @property
    def NextCursor(self):
        r"""**分页查询日志时使用，无具体业务含义**

第一次查询时值为null 
第二次及以后查询时使用上一次查询返回信息中的NextCursor字段值即可
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._ProjectId = params.get("ProjectId")
        self._CodeContent = params.get("CodeContent")
        self._LogInfo = params.get("LogInfo")
        self._NextCursor = params.get("NextCursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobDto(AbstractModel):
    r"""数据探索任务JOB

    """

    def __init__(self):
        r"""
        :param _JobId: 数据探索任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _JobName: 数据探索任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param _JobType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type JobType: str
        :param _ScriptId: 脚本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptId: str
        :param _JobExecutionList: 子任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobExecutionList: list of JobExecutionDto
        :param _ScriptContent: 脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptContent: str
        :param _Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _OwnerUin: 云主账号UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _UserUin: 账号UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type UserUin: str
        :param _TimeCost: 耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeCost: int
        :param _ScriptContentTruncate: 是否脚本内容被截断
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptContentTruncate: bool
        """
        self._JobId = None
        self._JobName = None
        self._JobType = None
        self._ScriptId = None
        self._JobExecutionList = None
        self._ScriptContent = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._EndTime = None
        self._OwnerUin = None
        self._UserUin = None
        self._TimeCost = None
        self._ScriptContentTruncate = None

    @property
    def JobId(self):
        r"""数据探索任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        r"""数据探索任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobType(self):
        r"""任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def ScriptId(self):
        r"""脚本ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def JobExecutionList(self):
        r"""子任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of JobExecutionDto
        """
        return self._JobExecutionList

    @JobExecutionList.setter
    def JobExecutionList(self, JobExecutionList):
        self._JobExecutionList = JobExecutionList

    @property
    def ScriptContent(self):
        r"""脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def Status(self):
        r"""任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def EndTime(self):
        r"""结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def OwnerUin(self):
        r"""云主账号UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def UserUin(self):
        r"""账号UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def TimeCost(self):
        r"""耗时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeCost

    @TimeCost.setter
    def TimeCost(self, TimeCost):
        self._TimeCost = TimeCost

    @property
    def ScriptContentTruncate(self):
        r"""是否脚本内容被截断
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ScriptContentTruncate

    @ScriptContentTruncate.setter
    def ScriptContentTruncate(self, ScriptContentTruncate):
        self._ScriptContentTruncate = ScriptContentTruncate


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._JobType = params.get("JobType")
        self._ScriptId = params.get("ScriptId")
        if params.get("JobExecutionList") is not None:
            self._JobExecutionList = []
            for item in params.get("JobExecutionList"):
                obj = JobExecutionDto()
                obj._deserialize(item)
                self._JobExecutionList.append(obj)
        self._ScriptContent = params.get("ScriptContent")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._EndTime = params.get("EndTime")
        self._OwnerUin = params.get("OwnerUin")
        self._UserUin = params.get("UserUin")
        self._TimeCost = params.get("TimeCost")
        self._ScriptContentTruncate = params.get("ScriptContentTruncate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobExecutionDto(AbstractModel):
    r"""业务提交JOB的子任务

    """

    def __init__(self):
        r"""
        :param _JobId: 数据探索任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _JobExecutionId: 子查询任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobExecutionId: str
        :param _JobExecutionName: 子查询名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JobExecutionName: str
        :param _ScriptContent: 子查询sql内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptContent: str
        :param _Status: 子查询状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ExecuteStageInfo: 执行阶段
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecuteStageInfo: str
        :param _LogFilePath: 日志路径
注意：此字段可能返回 null，表示取不到有效值。
        :type LogFilePath: str
        :param _ResultFilePath: 下载结果路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultFilePath: str
        :param _ResultPreviewFilePath: 预览结果路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultPreviewFilePath: str
        :param _ResultTotalCount: 任务执行的结果总行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultTotalCount: int
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _TimeCost: 耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeCost: int
        :param _ContextScriptContent: 上下文SQL内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextScriptContent: list of str
        :param _ResultPreviewCount: 任务执行的结果预览行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultPreviewCount: int
        :param _ResultEffectCount: 任务执行的结果影响行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultEffectCount: int
        :param _CollectingTotalResult: 是否正在收集全量结果：默认false，true表示正在收集全量结果，用于前端判断是否需要继续轮询
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectingTotalResult: bool
        :param _ScriptContentTruncate: 是否需要截断脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptContentTruncate: bool
        """
        self._JobId = None
        self._JobExecutionId = None
        self._JobExecutionName = None
        self._ScriptContent = None
        self._Status = None
        self._CreateTime = None
        self._ExecuteStageInfo = None
        self._LogFilePath = None
        self._ResultFilePath = None
        self._ResultPreviewFilePath = None
        self._ResultTotalCount = None
        self._UpdateTime = None
        self._EndTime = None
        self._TimeCost = None
        self._ContextScriptContent = None
        self._ResultPreviewCount = None
        self._ResultEffectCount = None
        self._CollectingTotalResult = None
        self._ScriptContentTruncate = None

    @property
    def JobId(self):
        r"""数据探索任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobExecutionId(self):
        r"""子查询任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobExecutionId

    @JobExecutionId.setter
    def JobExecutionId(self, JobExecutionId):
        self._JobExecutionId = JobExecutionId

    @property
    def JobExecutionName(self):
        r"""子查询名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobExecutionName

    @JobExecutionName.setter
    def JobExecutionName(self, JobExecutionName):
        self._JobExecutionName = JobExecutionName

    @property
    def ScriptContent(self):
        r"""子查询sql内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def Status(self):
        r"""子查询状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExecuteStageInfo(self):
        r"""执行阶段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecuteStageInfo

    @ExecuteStageInfo.setter
    def ExecuteStageInfo(self, ExecuteStageInfo):
        self._ExecuteStageInfo = ExecuteStageInfo

    @property
    def LogFilePath(self):
        r"""日志路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogFilePath

    @LogFilePath.setter
    def LogFilePath(self, LogFilePath):
        self._LogFilePath = LogFilePath

    @property
    def ResultFilePath(self):
        r"""下载结果路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultFilePath

    @ResultFilePath.setter
    def ResultFilePath(self, ResultFilePath):
        self._ResultFilePath = ResultFilePath

    @property
    def ResultPreviewFilePath(self):
        r"""预览结果路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultPreviewFilePath

    @ResultPreviewFilePath.setter
    def ResultPreviewFilePath(self, ResultPreviewFilePath):
        self._ResultPreviewFilePath = ResultPreviewFilePath

    @property
    def ResultTotalCount(self):
        r"""任务执行的结果总行数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResultTotalCount

    @ResultTotalCount.setter
    def ResultTotalCount(self, ResultTotalCount):
        self._ResultTotalCount = ResultTotalCount

    @property
    def UpdateTime(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def EndTime(self):
        r"""结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TimeCost(self):
        r"""耗时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeCost

    @TimeCost.setter
    def TimeCost(self, TimeCost):
        self._TimeCost = TimeCost

    @property
    def ContextScriptContent(self):
        r"""上下文SQL内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ContextScriptContent

    @ContextScriptContent.setter
    def ContextScriptContent(self, ContextScriptContent):
        self._ContextScriptContent = ContextScriptContent

    @property
    def ResultPreviewCount(self):
        r"""任务执行的结果预览行数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResultPreviewCount

    @ResultPreviewCount.setter
    def ResultPreviewCount(self, ResultPreviewCount):
        self._ResultPreviewCount = ResultPreviewCount

    @property
    def ResultEffectCount(self):
        r"""任务执行的结果影响行数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResultEffectCount

    @ResultEffectCount.setter
    def ResultEffectCount(self, ResultEffectCount):
        self._ResultEffectCount = ResultEffectCount

    @property
    def CollectingTotalResult(self):
        r"""是否正在收集全量结果：默认false，true表示正在收集全量结果，用于前端判断是否需要继续轮询
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CollectingTotalResult

    @CollectingTotalResult.setter
    def CollectingTotalResult(self, CollectingTotalResult):
        self._CollectingTotalResult = CollectingTotalResult

    @property
    def ScriptContentTruncate(self):
        r"""是否需要截断脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ScriptContentTruncate

    @ScriptContentTruncate.setter
    def ScriptContentTruncate(self, ScriptContentTruncate):
        self._ScriptContentTruncate = ScriptContentTruncate


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobExecutionId = params.get("JobExecutionId")
        self._JobExecutionName = params.get("JobExecutionName")
        self._ScriptContent = params.get("ScriptContent")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ExecuteStageInfo = params.get("ExecuteStageInfo")
        self._LogFilePath = params.get("LogFilePath")
        self._ResultFilePath = params.get("ResultFilePath")
        self._ResultPreviewFilePath = params.get("ResultPreviewFilePath")
        self._ResultTotalCount = params.get("ResultTotalCount")
        self._UpdateTime = params.get("UpdateTime")
        self._EndTime = params.get("EndTime")
        self._TimeCost = params.get("TimeCost")
        self._ContextScriptContent = params.get("ContextScriptContent")
        self._ResultPreviewCount = params.get("ResultPreviewCount")
        self._ResultEffectCount = params.get("ResultEffectCount")
        self._CollectingTotalResult = params.get("CollectingTotalResult")
        self._ScriptContentTruncate = params.get("ScriptContentTruncate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVMap(AbstractModel):
    r"""map

    """

    def __init__(self):
        r"""
        :param _K: k
注意：此字段可能返回 null，表示取不到有效值。
        :type K: str
        :param _V: v
注意：此字段可能返回 null，表示取不到有效值。
        :type V: str
        """
        self._K = None
        self._V = None

    @property
    def K(self):
        r"""k
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._K

    @K.setter
    def K(self, K):
        self._K = K

    @property
    def V(self):
        r"""v
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._V

    @V.setter
    def V(self, V):
        self._V = V


    def _deserialize(self, params):
        self._K = params.get("K")
        self._V = params.get("V")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    r"""键值对

    """

    def __init__(self):
        r"""
        :param _K: 键名
注意：此字段可能返回 null，表示取不到有效值。
        :type K: str
        :param _V: 值，请勿传SQL(请求会被视为攻击接口)，如果有需要，请将SQL进行Base64转码并解码。
注意：此字段可能返回 null，表示取不到有效值。
        :type V: str
        """
        self._K = None
        self._V = None

    @property
    def K(self):
        r"""键名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._K

    @K.setter
    def K(self, K):
        self._K = K

    @property
    def V(self):
        r"""值，请勿传SQL(请求会被视为攻击接口)，如果有需要，请将SQL进行Base64转码并解码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._V

    @V.setter
    def V(self, V):
        self._V = V


    def _deserialize(self, params):
        self._K = params.get("K")
        self._V = params.get("V")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillTaskInstancesAsyncRequest(AbstractModel):
    r"""KillTaskInstancesAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _InstanceKeyList: 实例id列表,可以从ListInstances中获取
        :type InstanceKeyList: list of str
        """
        self._ProjectId = None
        self._InstanceKeyList = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKeyList(self):
        r"""实例id列表,可以从ListInstances中获取
        :rtype: list of str
        """
        return self._InstanceKeyList

    @InstanceKeyList.setter
    def InstanceKeyList(self, InstanceKeyList):
        self._InstanceKeyList = InstanceKeyList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKeyList = params.get("InstanceKeyList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillTaskInstancesAsyncResponse(AbstractModel):
    r"""KillTaskInstancesAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 批量中止操作的返回的异步id, 可以在接口GetAsyncJob获取具体执行详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""批量中止操作的返回的异步id, 可以在接口GetAsyncJob获取具体执行详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListAlarmMessages(AbstractModel):
    r"""告警信息列表

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        :param _Items: 告警信息列表
        :type Items: list of AlarmMessage
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""告警信息列表
        :rtype: list of AlarmMessage
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AlarmMessage()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAlarmMessagesRequest(AbstractModel):
    r"""ListAlarmMessages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目id
        :type ProjectId: str
        :param _PageNumber: 页码数，用于翻页，最小值为 1。
        :type PageNumber: int
        :param _PageSize: 每页显示的条数，最大 100 条
        :type PageSize: int
        :param _StartTime: 起始告警时间, 格式为yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param _EndTime: 截止告警时间, 格式yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        :param _AlarmLevel: 告警级别
        :type AlarmLevel: int
        :param _AlarmRecipientId: 告警接收人Id
        :type AlarmRecipientId: str
        :param _TimeZone: 对于传入和返回的过滤时区, 默认UTC+8
        :type TimeZone: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._StartTime = None
        self._EndTime = None
        self._AlarmLevel = None
        self._AlarmRecipientId = None
        self._TimeZone = None

    @property
    def ProjectId(self):
        r"""所属项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""页码数，用于翻页，最小值为 1。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的条数，最大 100 条
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StartTime(self):
        r"""起始告警时间, 格式为yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""截止告警时间, 格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AlarmLevel(self):
        r"""告警级别
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmRecipientId(self):
        r"""告警接收人Id
        :rtype: str
        """
        return self._AlarmRecipientId

    @AlarmRecipientId.setter
    def AlarmRecipientId(self, AlarmRecipientId):
        self._AlarmRecipientId = AlarmRecipientId

    @property
    def TimeZone(self):
        r"""对于传入和返回的过滤时区, 默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmRecipientId = params.get("AlarmRecipientId")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAlarmMessagesResponse(AbstractModel):
    r"""ListAlarmMessages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 告警信息列表
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListAlarmMessages`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""告警信息列表
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListAlarmMessages`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListAlarmMessages()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListAlarmRulesResult(AbstractModel):
    r"""查询告警规则列表

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页的页数，当前页数
        :type PageNumber: int
        :param _PageSize: 每页显示的条数
        :type PageSize: int
        :param _TotalPageNumber: 分页总页数
        :type TotalPageNumber: int
        :param _TotalCount: 所有的告警规则个数
        :type TotalCount: int
        :param _Items: 告警规则信息列表
        :type Items: list of AlarmRuleData
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPageNumber = None
        self._TotalCount = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""分页的页数，当前页数
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPageNumber(self):
        r"""分页总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def TotalCount(self):
        r"""所有的告警规则个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""告警规则信息列表
        :rtype: list of AlarmRuleData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AlarmRuleData()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCodeFolderContentsRequest(AbstractModel):
    r"""ListCodeFolderContents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ParentFolderPath: 父文件夹path，例如/aaa/bbb/ccc，路径头需带斜杠，根目录传/
        :type ParentFolderPath: str
        :param _Keyword: 文件夹名称/代码文件名称搜索
        :type Keyword: str
        :param _OnlyFolderNode: 只查询文件夹
        :type OnlyFolderNode: bool
        :param _OnlyUserSelfScript: 是否只查询用户自己创建的代码文件
        :type OnlyUserSelfScript: bool
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._Keyword = None
        self._OnlyFolderNode = None
        self._OnlyUserSelfScript = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""父文件夹path，例如/aaa/bbb/ccc，路径头需带斜杠，根目录传/
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def Keyword(self):
        r"""文件夹名称/代码文件名称搜索
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def OnlyFolderNode(self):
        r"""只查询文件夹
        :rtype: bool
        """
        return self._OnlyFolderNode

    @OnlyFolderNode.setter
    def OnlyFolderNode(self, OnlyFolderNode):
        self._OnlyFolderNode = OnlyFolderNode

    @property
    def OnlyUserSelfScript(self):
        r"""是否只查询用户自己创建的代码文件
        :rtype: bool
        """
        return self._OnlyUserSelfScript

    @OnlyUserSelfScript.setter
    def OnlyUserSelfScript(self, OnlyUserSelfScript):
        self._OnlyUserSelfScript = OnlyUserSelfScript


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._Keyword = params.get("Keyword")
        self._OnlyFolderNode = params.get("OnlyFolderNode")
        self._OnlyUserSelfScript = params.get("OnlyUserSelfScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCodeFolderContentsResponse(AbstractModel):
    r"""ListCodeFolderContents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CodeFolderNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CodeFolderNode
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CodeFolderNode()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListDataBackfillInstancesRequest(AbstractModel):
    r"""ListDataBackfillInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目Id
        :type ProjectId: str
        :param _DataBackfillPlanId: 补录计划Id
        :type DataBackfillPlanId: str
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        """
        self._ProjectId = None
        self._DataBackfillPlanId = None
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""所属项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DataBackfillPlanId(self):
        r"""补录计划Id
        :rtype: str
        """
        return self._DataBackfillPlanId

    @DataBackfillPlanId.setter
    def DataBackfillPlanId(self, DataBackfillPlanId):
        self._DataBackfillPlanId = DataBackfillPlanId

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DataBackfillPlanId = params.get("DataBackfillPlanId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDataBackfillInstancesResponse(AbstractModel):
    r"""ListDataBackfillInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 单个补录计划下的所有补录实例
        :type Data: :class:`tencentcloud.wedata.v20250806.models.BackfillInstanceCollection`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""单个补录计划下的所有补录实例
        :rtype: :class:`tencentcloud.wedata.v20250806.models.BackfillInstanceCollection`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = BackfillInstanceCollection()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListDownstreamOpsTasksRequest(AbstractModel):
    r"""ListDownstreamOpsTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id	
        :type TaskId: str
        :param _ProjectId: 项目Id	
        :type ProjectId: str
        :param _PageNumber: 分页页码
        :type PageNumber: str
        :param _PageSize: 分页大小
        :type PageSize: str
        """
        self._TaskId = None
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TaskId(self):
        r"""任务Id	
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProjectId(self):
        r"""项目Id	
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""分页页码
        :rtype: str
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDownstreamOpsTasksResponse(AbstractModel):
    r"""ListDownstreamOpsTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 下游依赖详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ChildDependencyConfigPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""下游依赖详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ChildDependencyConfigPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ChildDependencyConfigPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListDownstreamTaskInstancesRequest(AbstractModel):
    r"""ListDownstreamTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _InstanceKey: **实例唯一标识**
        :type InstanceKey: str
        :param _TimeZone: **时区** timeZone, 默认UTC+8
        :type TimeZone: str
        :param _PageNumber: **页码，整型**配合pageSize使用且不能小于1， 默认值1
        :type PageNumber: int
        :param _PageSize: **每页显示的条数，默认为10，最小值为1、最大值为100
        :type PageSize: int
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._TimeZone = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**实例唯一标识**
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def TimeZone(self):
        r"""**时区** timeZone, 默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def PageNumber(self):
        r"""**页码，整型**配合pageSize使用且不能小于1， 默认值1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""**每页显示的条数，默认为10，最小值为1、最大值为100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._TimeZone = params.get("TimeZone")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDownstreamTaskInstancesResponse(AbstractModel):
    r"""ListDownstreamTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 直接下游实例列表
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""直接下游实例列表
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstancePage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListDownstreamTasksRequest(AbstractModel):
    r"""ListDownstreamTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _PageNumber: 分页大小
        :type PageNumber: int
        :param _PageSize: 分页页码
        :type PageSize: int
        """
        self._ProjectId = None
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页页码
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDownstreamTasksResponse(AbstractModel):
    r"""ListDownstreamTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 下游依赖详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DependencyConfigPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""下游依赖详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DependencyConfigPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DependencyConfigPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListOpsAlarmRulesRequest(AbstractModel):
    r"""ListOpsAlarmRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _PageNumber: 分页的页数，默认为1
        :type PageNumber: int
        :param _PageSize: 每页显示的条数，默认为20，最小值为1、最大值为200
        :type PageSize: int
        :param _MonitorObjectType: 监控对象类型, 任务维度监控： 可按照任务/工作流/项目来配置：1.任务、2.工作流、3.项目（默认为1.任务） 项目维度监控： 项目整体任务波动告警， 7：项目波动监控告警
        :type MonitorObjectType: int
        :param _TaskId: 根据任务id查询告警规则
        :type TaskId: str
        :param _AlarmType: 查询配置对应告警类型的告警规则
告警规则监控类型 failure：失败告警 ；overtime：超时告警 success：成功告警; backTrackingOrRerunSuccess: 补录重跑成功告警 backTrackingOrRerunFailure：补录重跑失败告警；
项目波动告警
projectFailureInstanceUpwardFluctuationAlarm： 当天失败实例数向上波动率超过阀值告警； projectSuccessInstanceDownwardFluctuationAlarm：当天成功实例数向下波动率超过阀值告警；
离线集成任务对账告警： reconciliationFailure： 离线对账任务失败告警 reconciliationOvertime： 离线对账任务运行超时告警 reconciliationMismatch： 数据对账任务不一致条数超过阀值告警
        :type AlarmType: str
        :param _AlarmLevel: 查询配置了对应告警级别的告警规则
告警级别 1.普通、2.重要、3.紧急
        :type AlarmLevel: int
        :param _AlarmRecipientId: 查询配置对应告警接收人的告警规则
        :type AlarmRecipientId: str
        :param _Keyword: 根据告警规则id/规则名称查询对应的告警规则
        :type Keyword: str
        :param _CreateUserUin: 告警规则创建人过滤
        :type CreateUserUin: str
        :param _CreateTimeFrom: 告警规则创建时间范围起始时间, 格式如2025-08-17 00:00:00
        :type CreateTimeFrom: str
        :param _CreateTimeTo: 告警规则创建时间范围结束时间，格式如"2025-08-26 23:59:59"

        :type CreateTimeTo: str
        :param _UpdateTimeFrom: 最后更新时间过滤告警规则， 格式如"2025-08-26 00:00:00"

        :type UpdateTimeFrom: str
        :param _UpdateTimeTo: 最后更新时间过滤告警规则 格式如： "2025-08-26 23:59:59"

        :type UpdateTimeTo: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._MonitorObjectType = None
        self._TaskId = None
        self._AlarmType = None
        self._AlarmLevel = None
        self._AlarmRecipientId = None
        self._Keyword = None
        self._CreateUserUin = None
        self._CreateTimeFrom = None
        self._CreateTimeTo = None
        self._UpdateTimeFrom = None
        self._UpdateTimeTo = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""分页的页数，默认为1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的条数，默认为20，最小值为1、最大值为200
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def MonitorObjectType(self):
        r"""监控对象类型, 任务维度监控： 可按照任务/工作流/项目来配置：1.任务、2.工作流、3.项目（默认为1.任务） 项目维度监控： 项目整体任务波动告警， 7：项目波动监控告警
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def TaskId(self):
        r"""根据任务id查询告警规则
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def AlarmType(self):
        r"""查询配置对应告警类型的告警规则
告警规则监控类型 failure：失败告警 ；overtime：超时告警 success：成功告警; backTrackingOrRerunSuccess: 补录重跑成功告警 backTrackingOrRerunFailure：补录重跑失败告警；
项目波动告警
projectFailureInstanceUpwardFluctuationAlarm： 当天失败实例数向上波动率超过阀值告警； projectSuccessInstanceDownwardFluctuationAlarm：当天成功实例数向下波动率超过阀值告警；
离线集成任务对账告警： reconciliationFailure： 离线对账任务失败告警 reconciliationOvertime： 离线对账任务运行超时告警 reconciliationMismatch： 数据对账任务不一致条数超过阀值告警
        :rtype: str
        """
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmLevel(self):
        r"""查询配置了对应告警级别的告警规则
告警级别 1.普通、2.重要、3.紧急
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmRecipientId(self):
        r"""查询配置对应告警接收人的告警规则
        :rtype: str
        """
        return self._AlarmRecipientId

    @AlarmRecipientId.setter
    def AlarmRecipientId(self, AlarmRecipientId):
        self._AlarmRecipientId = AlarmRecipientId

    @property
    def Keyword(self):
        r"""根据告警规则id/规则名称查询对应的告警规则
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def CreateUserUin(self):
        r"""告警规则创建人过滤
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def CreateTimeFrom(self):
        r"""告警规则创建时间范围起始时间, 格式如2025-08-17 00:00:00
        :rtype: str
        """
        return self._CreateTimeFrom

    @CreateTimeFrom.setter
    def CreateTimeFrom(self, CreateTimeFrom):
        self._CreateTimeFrom = CreateTimeFrom

    @property
    def CreateTimeTo(self):
        r"""告警规则创建时间范围结束时间，格式如"2025-08-26 23:59:59"

        :rtype: str
        """
        return self._CreateTimeTo

    @CreateTimeTo.setter
    def CreateTimeTo(self, CreateTimeTo):
        self._CreateTimeTo = CreateTimeTo

    @property
    def UpdateTimeFrom(self):
        r"""最后更新时间过滤告警规则， 格式如"2025-08-26 00:00:00"

        :rtype: str
        """
        return self._UpdateTimeFrom

    @UpdateTimeFrom.setter
    def UpdateTimeFrom(self, UpdateTimeFrom):
        self._UpdateTimeFrom = UpdateTimeFrom

    @property
    def UpdateTimeTo(self):
        r"""最后更新时间过滤告警规则 格式如： "2025-08-26 23:59:59"

        :rtype: str
        """
        return self._UpdateTimeTo

    @UpdateTimeTo.setter
    def UpdateTimeTo(self, UpdateTimeTo):
        self._UpdateTimeTo = UpdateTimeTo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._MonitorObjectType = params.get("MonitorObjectType")
        self._TaskId = params.get("TaskId")
        self._AlarmType = params.get("AlarmType")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmRecipientId = params.get("AlarmRecipientId")
        self._Keyword = params.get("Keyword")
        self._CreateUserUin = params.get("CreateUserUin")
        self._CreateTimeFrom = params.get("CreateTimeFrom")
        self._CreateTimeTo = params.get("CreateTimeTo")
        self._UpdateTimeFrom = params.get("UpdateTimeFrom")
        self._UpdateTimeTo = params.get("UpdateTimeTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOpsAlarmRulesResponse(AbstractModel):
    r"""ListOpsAlarmRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 告警信息信息响应
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListAlarmRulesResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""告警信息信息响应
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListAlarmRulesResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListAlarmRulesResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListOpsTasksPage(AbstractModel):
    r"""任务列表分页

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _Items: 记录列表	
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of TaskOpsInfo
        :param _PageNumber: 页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TotalCount(self):
        r"""结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""记录列表	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskOpsInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskOpsInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOpsTasksRequest(AbstractModel):
    r"""ListOpsTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id	
        :type ProjectId: str
        :param _PageSize: 分页大小
        :type PageSize: str
        :param _PageNumber: 分页页码
        :type PageNumber: str
        :param _TaskTypeId: 任务类型Id 
 - 20：通用数据同步
 - 25：ETLTaskType
 - 26：ETLTaskType
 - 30：python
 - 31：pyspark
 - 34：HiveSQLTaskType
 - 35：shell
 - 36：SparkSQLTaskType
 - 21：JDBCSQLTaskType
 - 32：DLCTaskType
 - 33：ImpalaTaskType
 - 40：CDWTaskType
 - 41：kettle
 - 46：DLCSparkTaskType
 - 47：TiOne机器学习
 - 48：TrinoTaskType
 - 50：DLCPyspark39：spark
 - 92：mr
 - 38：shell脚本
 - 70：hivesql脚本
 - 1000：自定义业务通用
        :type TaskTypeId: str
        :param _WorkflowId: 工作流Id
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
        :type WorkflowName: str
        :param _OwnerUin: 责任人id
        :type OwnerUin: str
        :param _FolderId: 文件夹Id
        :type FolderId: str
        :param _SourceServiceId: 数据源id
        :type SourceServiceId: str
        :param _TargetServiceId: 目标数据源id
        :type TargetServiceId: str
        :param _ExecutorGroupId: 资源组id
        :type ExecutorGroupId: str
        :param _CycleType: 任务周期类型
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
        :type CycleType: str
        :param _Status: 任务状态:
- Y: 运行
- F: 停止
- O: 冻结
- T: 停止中
- INVALID: 已失效
        :type Status: str
        :param _TimeZone: 时区, 默认默认UTC+8
        :type TimeZone: str
        """
        self._ProjectId = None
        self._PageSize = None
        self._PageNumber = None
        self._TaskTypeId = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._OwnerUin = None
        self._FolderId = None
        self._SourceServiceId = None
        self._TargetServiceId = None
        self._ExecutorGroupId = None
        self._CycleType = None
        self._Status = None
        self._TimeZone = None

    @property
    def ProjectId(self):
        r"""项目Id	
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""分页页码
        :rtype: str
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def TaskTypeId(self):
        r"""任务类型Id 
 - 20：通用数据同步
 - 25：ETLTaskType
 - 26：ETLTaskType
 - 30：python
 - 31：pyspark
 - 34：HiveSQLTaskType
 - 35：shell
 - 36：SparkSQLTaskType
 - 21：JDBCSQLTaskType
 - 32：DLCTaskType
 - 33：ImpalaTaskType
 - 40：CDWTaskType
 - 41：kettle
 - 46：DLCSparkTaskType
 - 47：TiOne机器学习
 - 48：TrinoTaskType
 - 50：DLCPyspark39：spark
 - 92：mr
 - 38：shell脚本
 - 70：hivesql脚本
 - 1000：自定义业务通用
        :rtype: str
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def WorkflowId(self):
        r"""工作流Id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def OwnerUin(self):
        r"""责任人id
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def FolderId(self):
        r"""文件夹Id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def SourceServiceId(self):
        r"""数据源id
        :rtype: str
        """
        return self._SourceServiceId

    @SourceServiceId.setter
    def SourceServiceId(self, SourceServiceId):
        self._SourceServiceId = SourceServiceId

    @property
    def TargetServiceId(self):
        r"""目标数据源id
        :rtype: str
        """
        return self._TargetServiceId

    @TargetServiceId.setter
    def TargetServiceId(self, TargetServiceId):
        self._TargetServiceId = TargetServiceId

    @property
    def ExecutorGroupId(self):
        r"""资源组id
        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def CycleType(self):
        r"""任务周期类型
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def Status(self):
        r"""任务状态:
- Y: 运行
- F: 停止
- O: 冻结
- T: 停止中
- INVALID: 已失效
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TimeZone(self):
        r"""时区, 默认默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._TaskTypeId = params.get("TaskTypeId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._OwnerUin = params.get("OwnerUin")
        self._FolderId = params.get("FolderId")
        self._SourceServiceId = params.get("SourceServiceId")
        self._TargetServiceId = params.get("TargetServiceId")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._CycleType = params.get("CycleType")
        self._Status = params.get("Status")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOpsTasksResponse(AbstractModel):
    r"""ListOpsTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务列表
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListOpsTasksPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务列表
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsTasksPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListOpsTasksPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListOpsWorkflowsRequest(AbstractModel):
    r"""ListOpsWorkflows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _PageNumber: 分页页码
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _FolderId: 文件Id
        :type FolderId: str
        :param _Status: 工作流状态筛选
* ALL_RUNNING : 全部调度中
* ALL_FREEZED : 全部已暂停
* ALL_STOPPTED : 全部已下线
* PART_RUNNING : 部分调度中
* ALL_NO_RUNNING : 全部未调度
* ALL_INVALID : 全部已失效
        :type Status: str
        :param _OwnerUin: 负责人Id
        :type OwnerUin: str
        :param _WorkflowType: 工作流类型筛选, 支持值 Cycle或Manual. 默认只查询 Cycle
        :type WorkflowType: str
        :param _KeyWord: 工作流关键词过滤，支持工作流 Id/name 模糊匹配
        :type KeyWord: str
        :param _SortItem: 排序项，可选CreateTime、TaskCount
        :type SortItem: str
        :param _SortType: 排序方式，DESC或ASC, 大写
        :type SortType: str
        :param _CreateUserUin: 创建人Id
        :type CreateUserUin: str
        :param _ModifyTime: 更新时间，格式yyyy-MM-dd HH:mm:ss
        :type ModifyTime: str
        :param _CreateTime: 创建时间，格式yyyy-MM-dd HH:mm:ss
        :type CreateTime: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._FolderId = None
        self._Status = None
        self._OwnerUin = None
        self._WorkflowType = None
        self._KeyWord = None
        self._SortItem = None
        self._SortType = None
        self._CreateUserUin = None
        self._ModifyTime = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""分页页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def FolderId(self):
        r"""文件Id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def Status(self):
        r"""工作流状态筛选
* ALL_RUNNING : 全部调度中
* ALL_FREEZED : 全部已暂停
* ALL_STOPPTED : 全部已下线
* PART_RUNNING : 部分调度中
* ALL_NO_RUNNING : 全部未调度
* ALL_INVALID : 全部已失效
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUin(self):
        r"""负责人Id
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def WorkflowType(self):
        r"""工作流类型筛选, 支持值 Cycle或Manual. 默认只查询 Cycle
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def KeyWord(self):
        r"""工作流关键词过滤，支持工作流 Id/name 模糊匹配
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord

    @property
    def SortItem(self):
        r"""排序项，可选CreateTime、TaskCount
        :rtype: str
        """
        return self._SortItem

    @SortItem.setter
    def SortItem(self, SortItem):
        self._SortItem = SortItem

    @property
    def SortType(self):
        r"""排序方式，DESC或ASC, 大写
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def CreateUserUin(self):
        r"""创建人Id
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def ModifyTime(self):
        r"""更新时间，格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        r"""创建时间，格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._FolderId = params.get("FolderId")
        self._Status = params.get("Status")
        self._OwnerUin = params.get("OwnerUin")
        self._WorkflowType = params.get("WorkflowType")
        self._KeyWord = params.get("KeyWord")
        self._SortItem = params.get("SortItem")
        self._SortType = params.get("SortType")
        self._CreateUserUin = params.get("CreateUserUin")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOpsWorkflowsResponse(AbstractModel):
    r"""ListOpsWorkflows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 工作流列表
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsWorkflows`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""工作流列表
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsWorkflows`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsWorkflows()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListResourceFilesRequest(AbstractModel):
    r"""ListResourceFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _PageNumber: 数据页数，大于等于1。默认1
        :type PageNumber: int
        :param _PageSize: 每页显示的数据条数，最小为10条，最大为200 条。默认10
        :type PageSize: int
        :param _ResourceName: 资源文件名称(模糊搜索关键词)
        :type ResourceName: str
        :param _ParentFolderPath: 资源文件所属文件夹路径(如/a/b/c，查询c文件夹下的资源文件)
        :type ParentFolderPath: str
        :param _CreateUserUin: 创建人ID, 可通过DescribeCurrentUserInfo接口获取
        :type CreateUserUin: str
        :param _ModifyTimeStart: 更新时间范围,开始时间, 格式yyyy-MM-dd HH:mm:ss
        :type ModifyTimeStart: str
        :param _ModifyTimeEnd: 更新时间范围,结束时间, 格式yyyy-MM-dd HH:mm:ss
        :type ModifyTimeEnd: str
        :param _CreateTimeStart: 创建时间范围,开始时间, 格式yyyy-MM-dd HH:mm:ss
        :type CreateTimeStart: str
        :param _CreateTimeEnd: 创建时间范围,结束时间, 格式yyyy-MM-dd HH:mm:ss
        :type CreateTimeEnd: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._ResourceName = None
        self._ParentFolderPath = None
        self._CreateUserUin = None
        self._ModifyTimeStart = None
        self._ModifyTimeEnd = None
        self._CreateTimeStart = None
        self._CreateTimeEnd = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""数据页数，大于等于1。默认1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的数据条数，最小为10条，最大为200 条。默认10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ResourceName(self):
        r"""资源文件名称(模糊搜索关键词)
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ParentFolderPath(self):
        r"""资源文件所属文件夹路径(如/a/b/c，查询c文件夹下的资源文件)
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def CreateUserUin(self):
        r"""创建人ID, 可通过DescribeCurrentUserInfo接口获取
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def ModifyTimeStart(self):
        r"""更新时间范围,开始时间, 格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._ModifyTimeStart

    @ModifyTimeStart.setter
    def ModifyTimeStart(self, ModifyTimeStart):
        self._ModifyTimeStart = ModifyTimeStart

    @property
    def ModifyTimeEnd(self):
        r"""更新时间范围,结束时间, 格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._ModifyTimeEnd

    @ModifyTimeEnd.setter
    def ModifyTimeEnd(self, ModifyTimeEnd):
        self._ModifyTimeEnd = ModifyTimeEnd

    @property
    def CreateTimeStart(self):
        r"""创建时间范围,开始时间, 格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._CreateTimeStart

    @CreateTimeStart.setter
    def CreateTimeStart(self, CreateTimeStart):
        self._CreateTimeStart = CreateTimeStart

    @property
    def CreateTimeEnd(self):
        r"""创建时间范围,结束时间, 格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._CreateTimeEnd

    @CreateTimeEnd.setter
    def CreateTimeEnd(self, CreateTimeEnd):
        self._CreateTimeEnd = CreateTimeEnd


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ResourceName = params.get("ResourceName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._CreateUserUin = params.get("CreateUserUin")
        self._ModifyTimeStart = params.get("ModifyTimeStart")
        self._ModifyTimeEnd = params.get("ModifyTimeEnd")
        self._CreateTimeStart = params.get("CreateTimeStart")
        self._CreateTimeEnd = params.get("CreateTimeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListResourceFilesResponse(AbstractModel):
    r"""ListResourceFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 获取资源文件列表
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ResourceFilePage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""获取资源文件列表
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ResourceFilePage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResourceFilePage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListResourceFoldersRequest(AbstractModel):
    r"""ListResourceFolders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ParentFolderPath: 资源文件夹绝对路径，取值示例
/wedata/test
        :type ParentFolderPath: str
        :param _PageNumber: 数据页数，大于等于1。默认1
        :type PageNumber: int
        :param _PageSize: 每页显示的数据条数，最小为10条，最大为200 条。默认10
        :type PageSize: int
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""资源文件夹绝对路径，取值示例
/wedata/test
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def PageNumber(self):
        r"""数据页数，大于等于1。默认1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的数据条数，最小为10条，最大为200 条。默认10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListResourceFoldersResponse(AbstractModel):
    r"""ListResourceFolders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 分页的资源文件夹查询结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ResourceFolderPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""分页的资源文件夹查询结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ResourceFolderPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResourceFolderPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListSQLFolderContentsRequest(AbstractModel):
    r"""ListSQLFolderContents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _ParentFolderPath: 父文件夹path，/aaa/bbb/ccc，路径头需带斜杠，查询根目录传/
        :type ParentFolderPath: str
        :param _Keyword: 文件夹名称/脚本名称搜索
        :type Keyword: str
        :param _OnlyFolderNode: 只查询文件夹
        :type OnlyFolderNode: bool
        :param _OnlyUserSelfScript: 是否只查询用户自己创建的脚本
        :type OnlyUserSelfScript: bool
        :param _AccessScope: 权限范围：SHARED, PRIVATE
        :type AccessScope: str
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._Keyword = None
        self._OnlyFolderNode = None
        self._OnlyUserSelfScript = None
        self._AccessScope = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""父文件夹path，/aaa/bbb/ccc，路径头需带斜杠，查询根目录传/
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def Keyword(self):
        r"""文件夹名称/脚本名称搜索
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def OnlyFolderNode(self):
        r"""只查询文件夹
        :rtype: bool
        """
        return self._OnlyFolderNode

    @OnlyFolderNode.setter
    def OnlyFolderNode(self, OnlyFolderNode):
        self._OnlyFolderNode = OnlyFolderNode

    @property
    def OnlyUserSelfScript(self):
        r"""是否只查询用户自己创建的脚本
        :rtype: bool
        """
        return self._OnlyUserSelfScript

    @OnlyUserSelfScript.setter
    def OnlyUserSelfScript(self, OnlyUserSelfScript):
        self._OnlyUserSelfScript = OnlyUserSelfScript

    @property
    def AccessScope(self):
        r"""权限范围：SHARED, PRIVATE
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._Keyword = params.get("Keyword")
        self._OnlyFolderNode = params.get("OnlyFolderNode")
        self._OnlyUserSelfScript = params.get("OnlyUserSelfScript")
        self._AccessScope = params.get("AccessScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSQLFolderContentsResponse(AbstractModel):
    r"""ListSQLFolderContents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果列表
        :type Data: list of SQLFolderNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果列表
        :rtype: list of SQLFolderNode
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SQLFolderNode()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListSQLScriptRunsRequest(AbstractModel):
    r"""ListSQLScriptRuns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScriptId: 脚本id
        :type ScriptId: str
        :param _JobId: 任务id
        :type JobId: str
        :param _SearchWord: 搜索关键词
        :type SearchWord: str
        :param _ExecuteUserUin: 执行人
        :type ExecuteUserUin: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._ProjectId = None
        self._ScriptId = None
        self._JobId = None
        self._SearchWord = None
        self._ExecuteUserUin = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScriptId(self):
        r"""脚本id
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def JobId(self):
        r"""任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def SearchWord(self):
        r"""搜索关键词
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def ExecuteUserUin(self):
        r"""执行人
        :rtype: str
        """
        return self._ExecuteUserUin

    @ExecuteUserUin.setter
    def ExecuteUserUin(self, ExecuteUserUin):
        self._ExecuteUserUin = ExecuteUserUin

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ScriptId = params.get("ScriptId")
        self._JobId = params.get("JobId")
        self._SearchWord = params.get("SearchWord")
        self._ExecuteUserUin = params.get("ExecuteUserUin")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSQLScriptRunsResponse(AbstractModel):
    r"""ListSQLScriptRuns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据探索任务
        :type Data: list of JobDto
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""数据探索任务
        :rtype: list of JobDto
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = JobDto()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListTaskInfo(AbstractModel):
    r"""查询任务信息分页

    """

    def __init__(self):
        r"""
        :param _Items: 任务数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of TaskBaseAttribute
        :param _PageNumber: 当前请求的数据页数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 当前请求的数据页条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _TotalCount: 满足查询条件的数据总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 满足查询条件的数据总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        """
        self._Items = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None

    @property
    def Items(self):
        r"""任务数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskBaseAttribute
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""当前请求的数据页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""当前请求的数据页条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""满足查询条件的数据总条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""满足查询条件的数据总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskBaseAttribute()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskInstanceExecutionsRequest(AbstractModel):
    r"""ListTaskInstanceExecutions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目id
        :type ProjectId: str
        :param _InstanceKey: 实例唯一标识，可以通过ListInstances获取
        :type InstanceKey: str
        :param _TimeZone: **时区**timeZone, 传入的时间字符串的所在时区，默认UTC+8
        :type TimeZone: str
        :param _PageSize: 每页大小，默认10, 最大200
        :type PageSize: int
        :param _PageNumber: 分页页码，默认1
        :type PageNumber: int
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._TimeZone = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def ProjectId(self):
        r"""所属项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""实例唯一标识，可以通过ListInstances获取
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def TimeZone(self):
        r"""**时区**timeZone, 传入的时间字符串的所在时区，默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def PageSize(self):
        r"""每页大小，默认10, 最大200
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""分页页码，默认1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._TimeZone = params.get("TimeZone")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskInstanceExecutionsResponse(AbstractModel):
    r"""ListTaskInstanceExecutions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 实例详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstanceExecutions`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""实例详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstanceExecutions`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstanceExecutions()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListTaskInstancesRequest(AbstractModel):
    r"""ListTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: **项目ID**
        :type ProjectId: str
        :param _PageNumber: **页码，整型**
配合pageSize使用且不能小于1， 默认值1
        :type PageNumber: int
        :param _PageSize: **每页显示的条数，默认为10，最小值为1、最大值为100
        :type PageSize: int
        :param _Keyword: **任务名称 或 任务ID**
支持模糊搜索过滤, 多个用 英文逗号, 分割
        :type Keyword: str
        :param _TimeZone: **时区**timeZone, 传入的时间字符串的所在时区，默认UTC+8
        :type TimeZone: str
        :param _InstanceType: **实例类型** 
- 0 表示补录类型 
- 1 表示周期实例 
- 2 表示非周期实例
        :type InstanceType: int
        :param _InstanceState: **实例状态** - WAIT_EVENT: 等待事件 - WAIT_UPSTREAM: 等待上游 - WAIT_RUN: 等待运行 - RUNNING: 运行中 - SKIP_RUNNING: 跳过运行 - FAILED_RETRY: 失败重试 - EXPIRED: 失败 - COMPLETED: 成功
        :type InstanceState: str
        :param _TaskTypeId: **任务类型Id**
        :type TaskTypeId: int
        :param _CycleType: **任务周期类型** * ONEOFF_CYCLE: 一次性 * YEAR_CYCLE: 年 * MONTH_CYCLE: 月 * WEEK_CYCLE: 周 * DAY_CYCLE: 天 * HOUR_CYCLE: 小时 * MINUTE_CYCLE: 分钟 * CRONTAB_CYCLE: crontab表达式类型
        :type CycleType: str
        :param _OwnerUin: **任务负责人id**
        :type OwnerUin: str
        :param _FolderId: **任务所属文件id**
        :type FolderId: str
        :param _WorkflowId: **任务所属工作流id**
        :type WorkflowId: str
        :param _ExecutorGroupId: **执行资源组Id**
        :type ExecutorGroupId: str
        :param _ScheduleTimeFrom: **实例计划调度时间过滤条件**过滤起始时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :type ScheduleTimeFrom: str
        :param _ScheduleTimeTo: **实例计划调度时间过滤条件**过滤截止时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :type ScheduleTimeTo: str
        :param _StartTimeFrom: **实例执行开始时间过滤条件**过滤起始时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :type StartTimeFrom: str
        :param _StartTimeTo: **实例执行开始时间过滤条件**
过滤截止时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :type StartTimeTo: str
        :param _LastUpdateTimeFrom: **实例最近更新时间过滤条件**
过滤截止时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :type LastUpdateTimeFrom: str
        :param _LastUpdateTimeTo: **实例最近更新时间过滤条件**
过滤截止时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :type LastUpdateTimeTo: str
        :param _SortColumn: **查询结果排序字段**- SCHEDULE_DATE 表示 根据计划调度时间排序- START_TIME 表示 根据实例开始执行时间排序- END_TIME 表示 根据实例结束执行时间排序- COST_TIME 表示 根据实例执行时长排序
        :type SortColumn: str
        :param _SortType: **实例排序方式**

- ASC 
- DESC
        :type SortType: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None
        self._TimeZone = None
        self._InstanceType = None
        self._InstanceState = None
        self._TaskTypeId = None
        self._CycleType = None
        self._OwnerUin = None
        self._FolderId = None
        self._WorkflowId = None
        self._ExecutorGroupId = None
        self._ScheduleTimeFrom = None
        self._ScheduleTimeTo = None
        self._StartTimeFrom = None
        self._StartTimeTo = None
        self._LastUpdateTimeFrom = None
        self._LastUpdateTimeTo = None
        self._SortColumn = None
        self._SortType = None

    @property
    def ProjectId(self):
        r"""**项目ID**
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""**页码，整型**
配合pageSize使用且不能小于1， 默认值1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""**每页显示的条数，默认为10，最小值为1、最大值为100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        r"""**任务名称 或 任务ID**
支持模糊搜索过滤, 多个用 英文逗号, 分割
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def TimeZone(self):
        r"""**时区**timeZone, 传入的时间字符串的所在时区，默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def InstanceType(self):
        r"""**实例类型** 
- 0 表示补录类型 
- 1 表示周期实例 
- 2 表示非周期实例
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceState(self):
        r"""**实例状态** - WAIT_EVENT: 等待事件 - WAIT_UPSTREAM: 等待上游 - WAIT_RUN: 等待运行 - RUNNING: 运行中 - SKIP_RUNNING: 跳过运行 - FAILED_RETRY: 失败重试 - EXPIRED: 失败 - COMPLETED: 成功
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def TaskTypeId(self):
        r"""**任务类型Id**
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def CycleType(self):
        r"""**任务周期类型** * ONEOFF_CYCLE: 一次性 * YEAR_CYCLE: 年 * MONTH_CYCLE: 月 * WEEK_CYCLE: 周 * DAY_CYCLE: 天 * HOUR_CYCLE: 小时 * MINUTE_CYCLE: 分钟 * CRONTAB_CYCLE: crontab表达式类型
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def OwnerUin(self):
        r"""**任务负责人id**
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def FolderId(self):
        r"""**任务所属文件id**
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def WorkflowId(self):
        r"""**任务所属工作流id**
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def ExecutorGroupId(self):
        r"""**执行资源组Id**
        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def ScheduleTimeFrom(self):
        r"""**实例计划调度时间过滤条件**过滤起始时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._ScheduleTimeFrom

    @ScheduleTimeFrom.setter
    def ScheduleTimeFrom(self, ScheduleTimeFrom):
        self._ScheduleTimeFrom = ScheduleTimeFrom

    @property
    def ScheduleTimeTo(self):
        r"""**实例计划调度时间过滤条件**过滤截止时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._ScheduleTimeTo

    @ScheduleTimeTo.setter
    def ScheduleTimeTo(self, ScheduleTimeTo):
        self._ScheduleTimeTo = ScheduleTimeTo

    @property
    def StartTimeFrom(self):
        r"""**实例执行开始时间过滤条件**过滤起始时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._StartTimeFrom

    @StartTimeFrom.setter
    def StartTimeFrom(self, StartTimeFrom):
        self._StartTimeFrom = StartTimeFrom

    @property
    def StartTimeTo(self):
        r"""**实例执行开始时间过滤条件**
过滤截止时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._StartTimeTo

    @StartTimeTo.setter
    def StartTimeTo(self, StartTimeTo):
        self._StartTimeTo = StartTimeTo

    @property
    def LastUpdateTimeFrom(self):
        r"""**实例最近更新时间过滤条件**
过滤截止时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._LastUpdateTimeFrom

    @LastUpdateTimeFrom.setter
    def LastUpdateTimeFrom(self, LastUpdateTimeFrom):
        self._LastUpdateTimeFrom = LastUpdateTimeFrom

    @property
    def LastUpdateTimeTo(self):
        r"""**实例最近更新时间过滤条件**
过滤截止时间，时间格式为 yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._LastUpdateTimeTo

    @LastUpdateTimeTo.setter
    def LastUpdateTimeTo(self, LastUpdateTimeTo):
        self._LastUpdateTimeTo = LastUpdateTimeTo

    @property
    def SortColumn(self):
        r"""**查询结果排序字段**- SCHEDULE_DATE 表示 根据计划调度时间排序- START_TIME 表示 根据实例开始执行时间排序- END_TIME 表示 根据实例结束执行时间排序- COST_TIME 表示 根据实例执行时长排序
        :rtype: str
        """
        return self._SortColumn

    @SortColumn.setter
    def SortColumn(self, SortColumn):
        self._SortColumn = SortColumn

    @property
    def SortType(self):
        r"""**实例排序方式**

- ASC 
- DESC
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._TimeZone = params.get("TimeZone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceState = params.get("InstanceState")
        self._TaskTypeId = params.get("TaskTypeId")
        self._CycleType = params.get("CycleType")
        self._OwnerUin = params.get("OwnerUin")
        self._FolderId = params.get("FolderId")
        self._WorkflowId = params.get("WorkflowId")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._ScheduleTimeFrom = params.get("ScheduleTimeFrom")
        self._ScheduleTimeTo = params.get("ScheduleTimeTo")
        self._StartTimeFrom = params.get("StartTimeFrom")
        self._StartTimeTo = params.get("StartTimeTo")
        self._LastUpdateTimeFrom = params.get("LastUpdateTimeFrom")
        self._LastUpdateTimeTo = params.get("LastUpdateTimeTo")
        self._SortColumn = params.get("SortColumn")
        self._SortType = params.get("SortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskInstancesResponse(AbstractModel):
    r"""ListTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 实例结果集
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""实例结果集
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstancePage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListTaskVersions(AbstractModel):
    r"""查询任务版本分页列表

    """

    def __init__(self):
        r"""
        :param _Items: 记录列表	
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of TaskVersion
        :param _TotalCount: 满足查询条件的数据总条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 满足查询条件的数据总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _PageCount: 当前页记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageCount: int
        :param _PageSize: 当前请求的数据页条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _PageNumber: 当前请求的数据页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        """
        self._Items = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageCount = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Items(self):
        r"""记录列表	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskVersion
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""满足查询条件的数据总条数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""满足查询条件的数据总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageCount(self):
        r"""当前页记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def PageSize(self):
        r"""当前请求的数据页条数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""当前请求的数据页数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskVersion()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageCount = params.get("PageCount")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskVersionsRequest(AbstractModel):
    r"""ListTaskVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskVersionType: 保存版本：SAVE
提交版本：SUBMIT
默认为SAVE
        :type TaskVersionType: str
        :param _PageNumber: 请求的数据页数。默认值为1，取值大于等于1。
        :type PageNumber: int
        :param _PageSize: 每页显示的数据条数。默认值为10 ，最小值为10，最大值为200。
        :type PageSize: int
        """
        self._ProjectId = None
        self._TaskId = None
        self._TaskVersionType = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskVersionType(self):
        r"""保存版本：SAVE
提交版本：SUBMIT
默认为SAVE
        :rtype: str
        """
        return self._TaskVersionType

    @TaskVersionType.setter
    def TaskVersionType(self, TaskVersionType):
        self._TaskVersionType = TaskVersionType

    @property
    def PageNumber(self):
        r"""请求的数据页数。默认值为1，取值大于等于1。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的数据条数。默认值为10 ，最小值为10，最大值为200。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._TaskVersionType = params.get("TaskVersionType")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskVersionsResponse(AbstractModel):
    r"""ListTaskVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListTaskVersions`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskVersions`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListTaskVersions()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListTasksRequest(AbstractModel):
    r"""ListTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _PageNumber: 请求的数据页数。默认值为1，取值大于等于1
        :type PageNumber: int
        :param _PageSize: 每页显示的数据条数。默认值为10 ，最小值为10，最大值为200
        :type PageSize: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _WorkflowId: 所属工作流ID
        :type WorkflowId: str
        :param _OwnerUin: 责任人ID
        :type OwnerUin: str
        :param _TaskTypeId: 任务类型
        :type TaskTypeId: int
        :param _Status: 任务状态
* N: 新建 
* Y: 调度中 
* F: 已下线 
* O: 已暂停 
* T: 下线中 
* INVALID: 已失效
        :type Status: str
        :param _Submit: 提交状态
        :type Submit: bool
        :param _BundleId: BundleId信息
        :type BundleId: str
        :param _CreateUserUin: 创建人ID
        :type CreateUserUin: str
        :param _ModifyTime: 修改时间区间 yyyy-MM-dd HH:mm:ss，需要在数组填入两个时间
        :type ModifyTime: list of str
        :param _CreateTime: 创建时间区间 yyyy-MM-dd HH:mm:ss，需要在数组填入两个时间
        :type CreateTime: list of str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._TaskName = None
        self._WorkflowId = None
        self._OwnerUin = None
        self._TaskTypeId = None
        self._Status = None
        self._Submit = None
        self._BundleId = None
        self._CreateUserUin = None
        self._ModifyTime = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""请求的数据页数。默认值为1，取值大于等于1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的数据条数。默认值为10 ，最小值为10，最大值为200
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WorkflowId(self):
        r"""所属工作流ID
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def OwnerUin(self):
        r"""责任人ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskTypeId(self):
        r"""任务类型
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def Status(self):
        r"""任务状态
* N: 新建 
* Y: 调度中 
* F: 已下线 
* O: 已暂停 
* T: 下线中 
* INVALID: 已失效
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Submit(self):
        r"""提交状态
        :rtype: bool
        """
        return self._Submit

    @Submit.setter
    def Submit(self, Submit):
        self._Submit = Submit

    @property
    def BundleId(self):
        r"""BundleId信息
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def CreateUserUin(self):
        r"""创建人ID
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def ModifyTime(self):
        r"""修改时间区间 yyyy-MM-dd HH:mm:ss，需要在数组填入两个时间
        :rtype: list of str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        r"""创建时间区间 yyyy-MM-dd HH:mm:ss，需要在数组填入两个时间
        :rtype: list of str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TaskName = params.get("TaskName")
        self._WorkflowId = params.get("WorkflowId")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskTypeId = params.get("TaskTypeId")
        self._Status = params.get("Status")
        self._Submit = params.get("Submit")
        self._BundleId = params.get("BundleId")
        self._CreateUserUin = params.get("CreateUserUin")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTasksResponse(AbstractModel):
    r"""ListTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务分页信息
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListTaskInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务分页信息
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListTaskInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListUpstreamOpsTasksRequest(AbstractModel):
    r"""ListUpstreamOpsTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _PageNumber: 分页页码
        :type PageNumber: str
        :param _PageSize: 分页大小
        :type PageSize: str
        """
        self._ProjectId = None
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""分页页码
        :rtype: str
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUpstreamOpsTasksResponse(AbstractModel):
    r"""ListUpstreamOpsTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 上游任务详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ParentDependencyConfigPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""上游任务详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ParentDependencyConfigPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ParentDependencyConfigPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListUpstreamTaskInstancesRequest(AbstractModel):
    r"""ListUpstreamTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _InstanceKey: **实例唯一标识**
        :type InstanceKey: str
        :param _TimeZone: **时区** timeZone, 默认UTC+8
        :type TimeZone: str
        :param _PageNumber: **页码，整型**配合pageSize使用且不能小于1， 默认值1
        :type PageNumber: int
        :param _PageSize: **每页显示的条数，默认为10，最小值为1、最大值为100
        :type PageSize: int
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._TimeZone = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**实例唯一标识**
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def TimeZone(self):
        r"""**时区** timeZone, 默认UTC+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def PageNumber(self):
        r"""**页码，整型**配合pageSize使用且不能小于1， 默认值1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""**每页显示的条数，默认为10，最小值为1、最大值为100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._TimeZone = params.get("TimeZone")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUpstreamTaskInstancesResponse(AbstractModel):
    r"""ListUpstreamTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 上游实例列表
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""上游实例列表
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstancePage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListUpstreamTasksRequest(AbstractModel):
    r"""ListUpstreamTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _PageNumber: 请求的数据页数。默认值为1，取值大于等于1。
        :type PageNumber: int
        :param _PageSize: 请求的数据页数。默认值为1，取值大于等于1。
        :type PageSize: int
        """
        self._ProjectId = None
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""请求的数据页数。默认值为1，取值大于等于1。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""请求的数据页数。默认值为1，取值大于等于1。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUpstreamTasksResponse(AbstractModel):
    r"""ListUpstreamTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 上游任务详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DependencyConfigPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""上游任务详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DependencyConfigPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DependencyConfigPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListWorkflowFoldersRequest(AbstractModel):
    r"""ListWorkflowFolders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ParentFolderPath: 父文件夹绝对路径，如/abc/de，如果是根目录则传/
        :type ParentFolderPath: str
        :param _PageNumber: 数据页数，大于等于1。默认1
        :type PageNumber: int
        :param _PageSize: 每页显示的数据条数，最小为10条，最大为200 条。默认10
        :type PageSize: int
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""父文件夹绝对路径，如/abc/de，如果是根目录则传/
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def PageNumber(self):
        r"""数据页数，大于等于1。默认1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的数据条数，最小为10条，最大为200 条。默认10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowFoldersResponse(AbstractModel):
    r"""ListWorkflowFolders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 分页的文件夹查询结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.WorkflowFolderPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""分页的文件夹查询结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowFolderPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = WorkflowFolderPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListWorkflowInfo(AbstractModel):
    r"""查询工作流分页列表

    """

    def __init__(self):
        r"""
        :param _Items: 列表item
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of WorkflowInfo
        :param _TotalPageNumber: 满足查询条件的数据总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _PageNumber: 当前请求的数据页数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 当前请求的数据页条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _TotalCount: 满足查询条件的数据总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._Items = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None

    @property
    def Items(self):
        r"""列表item
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkflowInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalPageNumber(self):
        r"""满足查询条件的数据总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""当前请求的数据页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""当前请求的数据页条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""满足查询条件的数据总条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = WorkflowInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowsRequest(AbstractModel):
    r"""ListWorkflows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _PageNumber: 请求的数据页数。默认值为1，取值大于等于1
        :type PageNumber: int
        :param _PageSize: 每页显示的数据条数。默认值为10 ，最小值为10，最大值为200
        :type PageSize: int
        :param _Keyword: 搜索关键词
        :type Keyword: str
        :param _ParentFolderPath: 工作流所属文件夹
        :type ParentFolderPath: str
        :param _WorkflowType: 工作流类型，cycle和manual
        :type WorkflowType: str
        :param _BundleId: bundleId项
        :type BundleId: str
        :param _OwnerUin: 负责人ID
        :type OwnerUin: str
        :param _CreateUserUin: 创建人ID
        :type CreateUserUin: str
        :param _ModifyTime: 修改时间区间 yyyy-MM-dd HH:mm:ss，需要在数组填入两个时间
        :type ModifyTime: list of str
        :param _CreateTime: 创建时间区间 yyyy-MM-dd HH:mm:ss，需要在数组填入两个时间
        :type CreateTime: list of str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None
        self._ParentFolderPath = None
        self._WorkflowType = None
        self._BundleId = None
        self._OwnerUin = None
        self._CreateUserUin = None
        self._ModifyTime = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""请求的数据页数。默认值为1，取值大于等于1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的数据条数。默认值为10 ，最小值为10，最大值为200
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        r"""搜索关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ParentFolderPath(self):
        r"""工作流所属文件夹
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def WorkflowType(self):
        r"""工作流类型，cycle和manual
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def BundleId(self):
        r"""bundleId项
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def OwnerUin(self):
        r"""负责人ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateUserUin(self):
        r"""创建人ID
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def ModifyTime(self):
        r"""修改时间区间 yyyy-MM-dd HH:mm:ss，需要在数组填入两个时间
        :rtype: list of str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        r"""创建时间区间 yyyy-MM-dd HH:mm:ss，需要在数组填入两个时间
        :rtype: list of str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._WorkflowType = params.get("WorkflowType")
        self._BundleId = params.get("BundleId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateUserUin = params.get("CreateUserUin")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowsResponse(AbstractModel):
    r"""ListWorkflows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询工作流分页信息
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""查询工作流分页信息
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListWorkflowInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyAlarmRuleResult(AbstractModel):
    r"""更新告警规则响应

    """

    def __init__(self):
        r"""
        :param _Status: 是否更新成功
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""是否更新成功
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
        


class NotebookSessionInfo(AbstractModel):
    r"""notebook kernel session信息

    """

    def __init__(self):
        r"""
        :param _NotebookSessionId: 会话ID
        :type NotebookSessionId: str
        :param _NotebookSessionName: 会话名称
        :type NotebookSessionName: str
        """
        self._NotebookSessionId = None
        self._NotebookSessionName = None

    @property
    def NotebookSessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._NotebookSessionId

    @NotebookSessionId.setter
    def NotebookSessionId(self, NotebookSessionId):
        self._NotebookSessionId = NotebookSessionId

    @property
    def NotebookSessionName(self):
        r"""会话名称
        :rtype: str
        """
        return self._NotebookSessionName

    @NotebookSessionName.setter
    def NotebookSessionName(self, NotebookSessionName):
        self._NotebookSessionName = NotebookSessionName


    def _deserialize(self, params):
        self._NotebookSessionId = params.get("NotebookSessionId")
        self._NotebookSessionName = params.get("NotebookSessionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotificationFatigue(AbstractModel):
    r"""告警疲劳告警配置

    """

    def __init__(self):
        r"""
        :param _NotifyCount: 告警次数
        :type NotifyCount: int
        :param _NotifyInterval: 告警间隔，分钟
        :type NotifyInterval: int
        :param _QuietIntervals: 免打扰时间，例如示例值
[{DaysOfWeek: [1, 2], StartTime: "00:00:00", EndTime: "09:00:00"}]	
每周一、周二的00:00到09:00免打扰
注意：此字段可能返回 null，表示取不到有效值。
        :type QuietIntervals: list of AlarmQuietInterval
        """
        self._NotifyCount = None
        self._NotifyInterval = None
        self._QuietIntervals = None

    @property
    def NotifyCount(self):
        r"""告警次数
        :rtype: int
        """
        return self._NotifyCount

    @NotifyCount.setter
    def NotifyCount(self, NotifyCount):
        self._NotifyCount = NotifyCount

    @property
    def NotifyInterval(self):
        r"""告警间隔，分钟
        :rtype: int
        """
        return self._NotifyInterval

    @NotifyInterval.setter
    def NotifyInterval(self, NotifyInterval):
        self._NotifyInterval = NotifyInterval

    @property
    def QuietIntervals(self):
        r"""免打扰时间，例如示例值
[{DaysOfWeek: [1, 2], StartTime: "00:00:00", EndTime: "09:00:00"}]	
每周一、周二的00:00到09:00免打扰
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AlarmQuietInterval
        """
        return self._QuietIntervals

    @QuietIntervals.setter
    def QuietIntervals(self, QuietIntervals):
        self._QuietIntervals = QuietIntervals


    def _deserialize(self, params):
        self._NotifyCount = params.get("NotifyCount")
        self._NotifyInterval = params.get("NotifyInterval")
        if params.get("QuietIntervals") is not None:
            self._QuietIntervals = []
            for item in params.get("QuietIntervals"):
                obj = AlarmQuietInterval()
                obj._deserialize(item)
                self._QuietIntervals.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsAsyncJobDetail(AbstractModel):
    r"""异步操作详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _AsyncId: 操作id
        :type AsyncId: str
        :param _AsyncType: 异步操作类型
        :type AsyncType: str
        :param _Status: 异步操作状态：初始状态: INIT; 运行中: RUNNING; 成功: SUCCESS; 失败: FAIL; 部分成功: PART_SUCCESS
        :type Status: str
        :param _ErrorDesc: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDesc: str
        :param _TotalSubProcessCount: 子操作总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSubProcessCount: int
        :param _FinishedSubProcessCount: 已完成的子操作个数
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedSubProcessCount: int
        :param _SuccessSubProcessCount: 已成功的子操作个数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessSubProcessCount: int
        :param _CreateUserUin: 操作人id
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _CreateTime: 操作创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._ProjectId = None
        self._AsyncId = None
        self._AsyncType = None
        self._Status = None
        self._ErrorDesc = None
        self._TotalSubProcessCount = None
        self._FinishedSubProcessCount = None
        self._SuccessSubProcessCount = None
        self._CreateUserUin = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AsyncId(self):
        r"""操作id
        :rtype: str
        """
        return self._AsyncId

    @AsyncId.setter
    def AsyncId(self, AsyncId):
        self._AsyncId = AsyncId

    @property
    def AsyncType(self):
        r"""异步操作类型
        :rtype: str
        """
        return self._AsyncType

    @AsyncType.setter
    def AsyncType(self, AsyncType):
        self._AsyncType = AsyncType

    @property
    def Status(self):
        r"""异步操作状态：初始状态: INIT; 运行中: RUNNING; 成功: SUCCESS; 失败: FAIL; 部分成功: PART_SUCCESS
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorDesc(self):
        r"""错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorDesc

    @ErrorDesc.setter
    def ErrorDesc(self, ErrorDesc):
        self._ErrorDesc = ErrorDesc

    @property
    def TotalSubProcessCount(self):
        r"""子操作总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalSubProcessCount

    @TotalSubProcessCount.setter
    def TotalSubProcessCount(self, TotalSubProcessCount):
        self._TotalSubProcessCount = TotalSubProcessCount

    @property
    def FinishedSubProcessCount(self):
        r"""已完成的子操作个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FinishedSubProcessCount

    @FinishedSubProcessCount.setter
    def FinishedSubProcessCount(self, FinishedSubProcessCount):
        self._FinishedSubProcessCount = FinishedSubProcessCount

    @property
    def SuccessSubProcessCount(self):
        r"""已成功的子操作个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuccessSubProcessCount

    @SuccessSubProcessCount.setter
    def SuccessSubProcessCount(self, SuccessSubProcessCount):
        self._SuccessSubProcessCount = SuccessSubProcessCount

    @property
    def CreateUserUin(self):
        r"""操作人id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def CreateTime(self):
        r"""操作创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AsyncId = params.get("AsyncId")
        self._AsyncType = params.get("AsyncType")
        self._Status = params.get("Status")
        self._ErrorDesc = params.get("ErrorDesc")
        self._TotalSubProcessCount = params.get("TotalSubProcessCount")
        self._FinishedSubProcessCount = params.get("FinishedSubProcessCount")
        self._SuccessSubProcessCount = params.get("SuccessSubProcessCount")
        self._CreateUserUin = params.get("CreateUserUin")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsAsyncResponse(AbstractModel):
    r"""异步操作返回结构体

    """

    def __init__(self):
        r"""
        :param _AsyncId: 异步执行记录Id
        :type AsyncId: str
        """
        self._AsyncId = None

    @property
    def AsyncId(self):
        r"""异步执行记录Id
        :rtype: str
        """
        return self._AsyncId

    @AsyncId.setter
    def AsyncId(self, AsyncId):
        self._AsyncId = AsyncId


    def _deserialize(self, params):
        self._AsyncId = params.get("AsyncId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsTaskDepend(AbstractModel):
    r"""依赖任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _WorkflowId: 工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _Status: 任务状态:
- Y: 调度中
- F: 已下线
- O: 已暂停
- T: 下线中
- INVALID: 已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _TaskTypeId: 任务类型Id：
* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeId: int
        :param _TaskTypeDesc: 任务类型描述
 - 20 :  通用数据同步
 - 25 :  ETLTaskType
 - 26 :  ETLTaskType
 - 30 :  python
 - 31 :  pyspark
 - 34 :  hivesql
 - 35 :  shell
 - 36 :  sparksql
 - 21 :  jdbcsql
 - 32 :  dlc
 - 33 :  ImpalaTaskType
 - 40 :  CDWTaskType
 - 41 :  kettle
 - 42 :  TCHouse-X
 - 43 :  TCHouse-X SQL
 - 46 :  dlcsparkTaskType
 - 47 :  TiOneMachineLearningTaskType
 - 48 :  Trino
 - 50 :  DLCPyspark
 - 23 :  TencentDistributedSQL
 - 39 :  spark
 - 92 :  MRTaskType
 - 38 :  ShellScript
 - 70 :  HiveSQLScrip
 - 130 :  分支
 - 131 :  归并
 - 132 :  Notebook探索
 - 133 :  SSH节点
 - 134 :  StarRocks
 - 137 :  For-each
 - 10000 :  自定义业务通用
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeDesc: str
        :param _FolderName: 文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderName: str
        :param _FolderId: 文件夹id
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        :param _FirstSubmitTime: 最近提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstSubmitTime: str
        :param _FirstRunTime: 首次运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstRunTime: str
        :param _ScheduleDesc: 调度计划展示描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleDesc: str
        :param _CycleType: 任务周期类型
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _OwnerUin: 负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _ExecutionStartTime: 执行开始时间, 格式HH:mm, 如00:00
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: 执行结束时间, 格式HH:mm, 如23:59
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionEndTime: str
        """
        self._TaskId = None
        self._TaskName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._ProjectId = None
        self._ProjectName = None
        self._Status = None
        self._TaskTypeId = None
        self._TaskTypeDesc = None
        self._FolderName = None
        self._FolderId = None
        self._FirstSubmitTime = None
        self._FirstRunTime = None
        self._ScheduleDesc = None
        self._CycleType = None
        self._OwnerUin = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None

    @property
    def TaskId(self):
        r"""任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WorkflowId(self):
        r"""工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def ProjectId(self):
        r"""项目id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Status(self):
        r"""任务状态:
- Y: 调度中
- F: 已下线
- O: 已暂停
- T: 下线中
- INVALID: 已失效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskTypeId(self):
        r"""任务类型Id：
* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskTypeDesc(self):
        r"""任务类型描述
 - 20 :  通用数据同步
 - 25 :  ETLTaskType
 - 26 :  ETLTaskType
 - 30 :  python
 - 31 :  pyspark
 - 34 :  hivesql
 - 35 :  shell
 - 36 :  sparksql
 - 21 :  jdbcsql
 - 32 :  dlc
 - 33 :  ImpalaTaskType
 - 40 :  CDWTaskType
 - 41 :  kettle
 - 42 :  TCHouse-X
 - 43 :  TCHouse-X SQL
 - 46 :  dlcsparkTaskType
 - 47 :  TiOneMachineLearningTaskType
 - 48 :  Trino
 - 50 :  DLCPyspark
 - 23 :  TencentDistributedSQL
 - 39 :  spark
 - 92 :  MRTaskType
 - 38 :  ShellScript
 - 70 :  HiveSQLScrip
 - 130 :  分支
 - 131 :  归并
 - 132 :  Notebook探索
 - 133 :  SSH节点
 - 134 :  StarRocks
 - 137 :  For-each
 - 10000 :  自定义业务通用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeDesc

    @TaskTypeDesc.setter
    def TaskTypeDesc(self, TaskTypeDesc):
        self._TaskTypeDesc = TaskTypeDesc

    @property
    def FolderName(self):
        r"""文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def FolderId(self):
        r"""文件夹id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FirstSubmitTime(self):
        r"""最近提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FirstSubmitTime

    @FirstSubmitTime.setter
    def FirstSubmitTime(self, FirstSubmitTime):
        self._FirstSubmitTime = FirstSubmitTime

    @property
    def FirstRunTime(self):
        r"""首次运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FirstRunTime

    @FirstRunTime.setter
    def FirstRunTime(self, FirstRunTime):
        self._FirstRunTime = FirstRunTime

    @property
    def ScheduleDesc(self):
        r"""调度计划展示描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduleDesc

    @ScheduleDesc.setter
    def ScheduleDesc(self, ScheduleDesc):
        self._ScheduleDesc = ScheduleDesc

    @property
    def CycleType(self):
        r"""任务周期类型
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def OwnerUin(self):
        r"""负责人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ExecutionStartTime(self):
        r"""执行开始时间, 格式HH:mm, 如00:00
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""执行结束时间, 格式HH:mm, 如23:59
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Status = params.get("Status")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskTypeDesc = params.get("TaskTypeDesc")
        self._FolderName = params.get("FolderName")
        self._FolderId = params.get("FolderId")
        self._FirstSubmitTime = params.get("FirstSubmitTime")
        self._FirstRunTime = params.get("FirstRunTime")
        self._ScheduleDesc = params.get("ScheduleDesc")
        self._CycleType = params.get("CycleType")
        self._OwnerUin = params.get("OwnerUin")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsWorkflow(AbstractModel):
    r"""工作流列表分页详情

    """

    def __init__(self):
        r"""
        :param _TaskCount: 任务数量
        :type TaskCount: int
        :param _FolderName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderName: str
        :param _FolderId: 工作流文件id
        :type FolderId: str
        :param _WorkflowId: 工作流id
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _WorkflowType: 工作流类型
 - cycle周期
 - manual手动
        :type WorkflowType: str
        :param _WorkflowDesc: 工作流描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowDesc: str
        :param _OwnerUin: 负责人userId,多个‘；’隔开
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _Status: 工作流状态
* ALL_RUNNING : 全部调度中
* ALL_FREEZED : 全部已暂停
* ALL_STOPPTED : 全部已下线
* PART_RUNNING : 部分调度中
* ALL_NO_RUNNING : 全部未调度
* ALL_INVALID : 全部已失效
        :type Status: str
        :param _CreateTime: 工作流创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 最近更新时间, 包含开发、生产变更
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _UpdateUserUin: 最近更新人，包含开发、生产变更
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserUin: str
        """
        self._TaskCount = None
        self._FolderName = None
        self._FolderId = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowType = None
        self._WorkflowDesc = None
        self._OwnerUin = None
        self._ProjectId = None
        self._ProjectName = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._UpdateUserUin = None

    @property
    def TaskCount(self):
        r"""任务数量
        :rtype: int
        """
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def FolderName(self):
        r"""文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def FolderId(self):
        r"""工作流文件id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def WorkflowId(self):
        r"""工作流id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowType(self):
        r"""工作流类型
 - cycle周期
 - manual手动
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def WorkflowDesc(self):
        r"""工作流描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def OwnerUin(self):
        r"""负责人userId,多个‘；’隔开
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Status(self):
        r"""工作流状态
* ALL_RUNNING : 全部调度中
* ALL_FREEZED : 全部已暂停
* ALL_STOPPTED : 全部已下线
* PART_RUNNING : 部分调度中
* ALL_NO_RUNNING : 全部未调度
* ALL_INVALID : 全部已失效
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""工作流创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最近更新时间, 包含开发、生产变更
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def UpdateUserUin(self):
        r"""最近更新人，包含开发、生产变更
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin


    def _deserialize(self, params):
        self._TaskCount = params.get("TaskCount")
        self._FolderName = params.get("FolderName")
        self._FolderId = params.get("FolderId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowType = params.get("WorkflowType")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._UpdateUserUin = params.get("UpdateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsWorkflowDetail(AbstractModel):
    r"""工作流调度详情

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowDesc: 工作流描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowDesc: str
        :param _WorkflowType: 工作流类型：
 - cycle 周期；
 - manual手动
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowType: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _CreateUserUin: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _StartupTime: 延时执行时间,unit=minute
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupTime: int
        :param _StartTime: 配置生效日期 开始日期
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 配置结束日期 结束日期
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CycleType: 任务周期类型
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _FolderId: 文件夹Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        :param _InstanceInitStrategy: 任务实例初始化策略
 - T_PLUS_1（T+1）：延迟一天初始化
 - T_PLUS_0（T+0）：当天初始化
 - T_MINUS_1（T-1）：提前一天初始化
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceInitStrategy: str
        :param _SchedulerDesc: 调度计划释义
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerDesc: str
        :param _FirstSubmitTime: 工作流首次提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstSubmitTime: str
        :param _LatestSubmitTime: 工作流最近提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestSubmitTime: str
        :param _Status: 工作流状态
* ALL_RUNNING : 全部调度中
* ALL_FREEZED : 全部已暂停
* ALL_STOPPTED : 全部已下线
* PART_RUNNING : 部分调度中
* ALL_NO_RUNNING : 全部未调度
* ALL_INVALID : 全部已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _OwnerUin: 负责人, 多个以‘；’隔开
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        """
        self._WorkflowId = None
        self._WorkflowDesc = None
        self._WorkflowType = None
        self._CreateTime = None
        self._CreateUserUin = None
        self._UpdateTime = None
        self._StartupTime = None
        self._StartTime = None
        self._EndTime = None
        self._CycleType = None
        self._FolderId = None
        self._InstanceInitStrategy = None
        self._SchedulerDesc = None
        self._FirstSubmitTime = None
        self._LatestSubmitTime = None
        self._Status = None
        self._OwnerUin = None
        self._WorkflowName = None

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowDesc(self):
        r"""工作流描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def WorkflowType(self):
        r"""工作流类型：
 - cycle 周期；
 - manual手动
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateUserUin(self):
        r"""创建人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def UpdateTime(self):
        r"""修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartupTime(self):
        r"""延时执行时间,unit=minute
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StartupTime

    @StartupTime.setter
    def StartupTime(self, StartupTime):
        self._StartupTime = StartupTime

    @property
    def StartTime(self):
        r"""配置生效日期 开始日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""配置结束日期 结束日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CycleType(self):
        r"""任务周期类型
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def FolderId(self):
        r"""文件夹Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def InstanceInitStrategy(self):
        r"""任务实例初始化策略
 - T_PLUS_1（T+1）：延迟一天初始化
 - T_PLUS_0（T+0）：当天初始化
 - T_MINUS_1（T-1）：提前一天初始化
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceInitStrategy

    @InstanceInitStrategy.setter
    def InstanceInitStrategy(self, InstanceInitStrategy):
        self._InstanceInitStrategy = InstanceInitStrategy

    @property
    def SchedulerDesc(self):
        r"""调度计划释义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SchedulerDesc

    @SchedulerDesc.setter
    def SchedulerDesc(self, SchedulerDesc):
        self._SchedulerDesc = SchedulerDesc

    @property
    def FirstSubmitTime(self):
        r"""工作流首次提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FirstSubmitTime

    @FirstSubmitTime.setter
    def FirstSubmitTime(self, FirstSubmitTime):
        self._FirstSubmitTime = FirstSubmitTime

    @property
    def LatestSubmitTime(self):
        r"""工作流最近提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestSubmitTime

    @LatestSubmitTime.setter
    def LatestSubmitTime(self, LatestSubmitTime):
        self._LatestSubmitTime = LatestSubmitTime

    @property
    def Status(self):
        r"""工作流状态
* ALL_RUNNING : 全部调度中
* ALL_FREEZED : 全部已暂停
* ALL_STOPPTED : 全部已下线
* PART_RUNNING : 部分调度中
* ALL_NO_RUNNING : 全部未调度
* ALL_INVALID : 全部已失效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUin(self):
        r"""负责人, 多个以‘；’隔开
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._WorkflowType = params.get("WorkflowType")
        self._CreateTime = params.get("CreateTime")
        self._CreateUserUin = params.get("CreateUserUin")
        self._UpdateTime = params.get("UpdateTime")
        self._StartupTime = params.get("StartupTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CycleType = params.get("CycleType")
        self._FolderId = params.get("FolderId")
        self._InstanceInitStrategy = params.get("InstanceInitStrategy")
        self._SchedulerDesc = params.get("SchedulerDesc")
        self._FirstSubmitTime = params.get("FirstSubmitTime")
        self._LatestSubmitTime = params.get("LatestSubmitTime")
        self._Status = params.get("Status")
        self._OwnerUin = params.get("OwnerUin")
        self._WorkflowName = params.get("WorkflowName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsWorkflows(AbstractModel):
    r"""查询工作流分页列表

    """

    def __init__(self):
        r"""
        :param _Items: 记录列表	
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OpsWorkflow
        :param _TotalCount: 结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _PageSize: 分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _PageNumber: 分页页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        """
        self._Items = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Items(self):
        r"""记录列表	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OpsWorkflow
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageSize(self):
        r"""分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""分页页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OpsWorkflow()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutTaskParameter(AbstractModel):
    r"""参数传递-输出参数

    """

    def __init__(self):
        r"""
        :param _ParamKey: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamKey: str
        :param _ParamValue: 参数定义
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""参数定义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    r"""参数

    """

    def __init__(self):
        r"""
        :param _ParamKey: 参数名
        :type ParamKey: str
        :param _ParamValue: 参数值
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""参数名
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""参数值
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParentDependencyConfigPage(AbstractModel):
    r"""查询任务上游依赖详情分页

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _PageNumber: 页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _Items: 分页数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OpsTaskDepend
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._Items = None

    @property
    def TotalCount(self):
        r"""结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Items(self):
        r"""分页数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OpsTaskDepend
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OpsTaskDepend()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOpsTasksAsyncRequest(AbstractModel):
    r"""PauseOpsTasksAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目Id
        :type ProjectId: str
        :param _TaskIds: 任务Id列表
        :type TaskIds: list of str
        :param _KillInstance: 是否需要终止已生成实例
        :type KillInstance: bool
        """
        self._ProjectId = None
        self._TaskIds = None
        self._KillInstance = None

    @property
    def ProjectId(self):
        r"""所属项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskIds(self):
        r"""任务Id列表
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def KillInstance(self):
        r"""是否需要终止已生成实例
        :rtype: bool
        """
        return self._KillInstance

    @KillInstance.setter
    def KillInstance(self, KillInstance):
        self._KillInstance = KillInstance


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskIds = params.get("TaskIds")
        self._KillInstance = params.get("KillInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOpsTasksAsyncResponse(AbstractModel):
    r"""PauseOpsTasksAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 异步操作结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""异步操作结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ProjectInstanceStatisticsAlarmInfo(AbstractModel):
    r"""告警规则项目波动率告警配置信息

    """

    def __init__(self):
        r"""
        :param _AlarmType: 告警类型 

projectFailureInstanceUpwardFluctuationAlarm: 失败实例向上波动告警

projectSuccessInstanceDownwardFluctuationAlarm： 成功实例向下波动告警
        :type AlarmType: str
        :param _InstanceThresholdCountPercent: 实例成功数向下波动比例告警阀值；实例失败数向上波动比例告警阀值
        :type InstanceThresholdCountPercent: int
        :param _InstanceThresholdCount: 累计实例数波动阀值
        :type InstanceThresholdCount: int
        :param _StabilizeThreshold: 稳定性次数阈值(防抖动配置统计周期数)
        :type StabilizeThreshold: int
        :param _StabilizeStatisticsCycle: 稳定性统计周期(防抖动配置统计周期数)
        :type StabilizeStatisticsCycle: int
        :param _IsCumulant: 是否累计计算,false:连续,true:累计
        :type IsCumulant: bool
        :param _InstanceCount: 当日累计实例数;
当天失败实例数向下波动量
        :type InstanceCount: int
        """
        self._AlarmType = None
        self._InstanceThresholdCountPercent = None
        self._InstanceThresholdCount = None
        self._StabilizeThreshold = None
        self._StabilizeStatisticsCycle = None
        self._IsCumulant = None
        self._InstanceCount = None

    @property
    def AlarmType(self):
        r"""告警类型 

projectFailureInstanceUpwardFluctuationAlarm: 失败实例向上波动告警

projectSuccessInstanceDownwardFluctuationAlarm： 成功实例向下波动告警
        :rtype: str
        """
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def InstanceThresholdCountPercent(self):
        r"""实例成功数向下波动比例告警阀值；实例失败数向上波动比例告警阀值
        :rtype: int
        """
        return self._InstanceThresholdCountPercent

    @InstanceThresholdCountPercent.setter
    def InstanceThresholdCountPercent(self, InstanceThresholdCountPercent):
        self._InstanceThresholdCountPercent = InstanceThresholdCountPercent

    @property
    def InstanceThresholdCount(self):
        r"""累计实例数波动阀值
        :rtype: int
        """
        return self._InstanceThresholdCount

    @InstanceThresholdCount.setter
    def InstanceThresholdCount(self, InstanceThresholdCount):
        self._InstanceThresholdCount = InstanceThresholdCount

    @property
    def StabilizeThreshold(self):
        r"""稳定性次数阈值(防抖动配置统计周期数)
        :rtype: int
        """
        return self._StabilizeThreshold

    @StabilizeThreshold.setter
    def StabilizeThreshold(self, StabilizeThreshold):
        self._StabilizeThreshold = StabilizeThreshold

    @property
    def StabilizeStatisticsCycle(self):
        r"""稳定性统计周期(防抖动配置统计周期数)
        :rtype: int
        """
        return self._StabilizeStatisticsCycle

    @StabilizeStatisticsCycle.setter
    def StabilizeStatisticsCycle(self, StabilizeStatisticsCycle):
        self._StabilizeStatisticsCycle = StabilizeStatisticsCycle

    @property
    def IsCumulant(self):
        r"""是否累计计算,false:连续,true:累计
        :rtype: bool
        """
        return self._IsCumulant

    @IsCumulant.setter
    def IsCumulant(self, IsCumulant):
        self._IsCumulant = IsCumulant

    @property
    def InstanceCount(self):
        r"""当日累计实例数;
当天失败实例数向下波动量
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount


    def _deserialize(self, params):
        self._AlarmType = params.get("AlarmType")
        self._InstanceThresholdCountPercent = params.get("InstanceThresholdCountPercent")
        self._InstanceThresholdCount = params.get("InstanceThresholdCount")
        self._StabilizeThreshold = params.get("StabilizeThreshold")
        self._StabilizeStatisticsCycle = params.get("StabilizeStatisticsCycle")
        self._IsCumulant = params.get("IsCumulant")
        self._InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconciliationStrategyInfo(AbstractModel):
    r"""离线集成对账告警规则

    """

    def __init__(self):
        r"""
        :param _RuleType: 离线告警规则类型
reconciliationFailure： 离线对账失败告警
reconciliationOvertime： 离线对账任务运行超时告警(需配置超时时间)
reconciliationMismatch： 离线对账不一致条数告警(需配置不一致条数阀值)
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _MismatchCount: 对账不一致条数阀值， RuleType=reconciliationMismatch对账不一致条数类型，需要配置该字段，无默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type MismatchCount: int
        :param _Hour: 对账任务运行超时阀值： 小时， 默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :type Hour: int
        :param _Min: 对账任务运行超时阀值： 分钟， 默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: int
        """
        self._RuleType = None
        self._MismatchCount = None
        self._Hour = None
        self._Min = None

    @property
    def RuleType(self):
        r"""离线告警规则类型
reconciliationFailure： 离线对账失败告警
reconciliationOvertime： 离线对账任务运行超时告警(需配置超时时间)
reconciliationMismatch： 离线对账不一致条数告警(需配置不一致条数阀值)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def MismatchCount(self):
        r"""对账不一致条数阀值， RuleType=reconciliationMismatch对账不一致条数类型，需要配置该字段，无默认值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MismatchCount

    @MismatchCount.setter
    def MismatchCount(self, MismatchCount):
        self._MismatchCount = MismatchCount

    @property
    def Hour(self):
        r"""对账任务运行超时阀值： 小时， 默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def Min(self):
        r"""对账任务运行超时阀值： 分钟， 默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._MismatchCount = params.get("MismatchCount")
        self._Hour = params.get("Hour")
        self._Min = params.get("Min")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerunTaskInstancesAsyncRequest(AbstractModel):
    r"""RerunTaskInstancesAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _InstanceKeyList: 实例id列表,可以从ListInstances中获取
        :type InstanceKeyList: list of str
        :param _RerunType: 重跑类型, 1: 自身; 3: 孩子; 2: 自身以及孩子，默认1
        :type RerunType: str
        :param _CheckParentType: 是否检查上游任务： ALL（全部）、 MAKE_SCOPE（选中）、NONE （全部不检查），默认NONE
        :type CheckParentType: str
        :param _SonRangeType: 下游实例范围 WORKFLOW: 所在工作流 PROJECT: 所在项目 ALL: 所有跨工作流依赖的项目，默认WORKFLOW
        :type SonRangeType: str
        :param _SkipEventListening: 重跑是否忽略事件监听
        :type SkipEventListening: bool
        :param _RedefineParallelNum: 自定义实例运行并发度, 如果不配置，则使用任务原有自依赖
        :type RedefineParallelNum: int
        :param _RedefineSelfWorkflowDependency: 自定义的工作流自依赖: yes开启，no关闭，如果不配置，则使用工作流原有自依赖
        :type RedefineSelfWorkflowDependency: str
        :param _RedefineParamList: 重跑实例自定义参数
        :type RedefineParamList: :class:`tencentcloud.wedata.v20250806.models.KVMap`
        """
        self._ProjectId = None
        self._InstanceKeyList = None
        self._RerunType = None
        self._CheckParentType = None
        self._SonRangeType = None
        self._SkipEventListening = None
        self._RedefineParallelNum = None
        self._RedefineSelfWorkflowDependency = None
        self._RedefineParamList = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKeyList(self):
        r"""实例id列表,可以从ListInstances中获取
        :rtype: list of str
        """
        return self._InstanceKeyList

    @InstanceKeyList.setter
    def InstanceKeyList(self, InstanceKeyList):
        self._InstanceKeyList = InstanceKeyList

    @property
    def RerunType(self):
        r"""重跑类型, 1: 自身; 3: 孩子; 2: 自身以及孩子，默认1
        :rtype: str
        """
        return self._RerunType

    @RerunType.setter
    def RerunType(self, RerunType):
        self._RerunType = RerunType

    @property
    def CheckParentType(self):
        r"""是否检查上游任务： ALL（全部）、 MAKE_SCOPE（选中）、NONE （全部不检查），默认NONE
        :rtype: str
        """
        return self._CheckParentType

    @CheckParentType.setter
    def CheckParentType(self, CheckParentType):
        self._CheckParentType = CheckParentType

    @property
    def SonRangeType(self):
        r"""下游实例范围 WORKFLOW: 所在工作流 PROJECT: 所在项目 ALL: 所有跨工作流依赖的项目，默认WORKFLOW
        :rtype: str
        """
        return self._SonRangeType

    @SonRangeType.setter
    def SonRangeType(self, SonRangeType):
        self._SonRangeType = SonRangeType

    @property
    def SkipEventListening(self):
        r"""重跑是否忽略事件监听
        :rtype: bool
        """
        return self._SkipEventListening

    @SkipEventListening.setter
    def SkipEventListening(self, SkipEventListening):
        self._SkipEventListening = SkipEventListening

    @property
    def RedefineParallelNum(self):
        r"""自定义实例运行并发度, 如果不配置，则使用任务原有自依赖
        :rtype: int
        """
        return self._RedefineParallelNum

    @RedefineParallelNum.setter
    def RedefineParallelNum(self, RedefineParallelNum):
        self._RedefineParallelNum = RedefineParallelNum

    @property
    def RedefineSelfWorkflowDependency(self):
        r"""自定义的工作流自依赖: yes开启，no关闭，如果不配置，则使用工作流原有自依赖
        :rtype: str
        """
        return self._RedefineSelfWorkflowDependency

    @RedefineSelfWorkflowDependency.setter
    def RedefineSelfWorkflowDependency(self, RedefineSelfWorkflowDependency):
        self._RedefineSelfWorkflowDependency = RedefineSelfWorkflowDependency

    @property
    def RedefineParamList(self):
        r"""重跑实例自定义参数
        :rtype: :class:`tencentcloud.wedata.v20250806.models.KVMap`
        """
        return self._RedefineParamList

    @RedefineParamList.setter
    def RedefineParamList(self, RedefineParamList):
        self._RedefineParamList = RedefineParamList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKeyList = params.get("InstanceKeyList")
        self._RerunType = params.get("RerunType")
        self._CheckParentType = params.get("CheckParentType")
        self._SonRangeType = params.get("SonRangeType")
        self._SkipEventListening = params.get("SkipEventListening")
        self._RedefineParallelNum = params.get("RedefineParallelNum")
        self._RedefineSelfWorkflowDependency = params.get("RedefineSelfWorkflowDependency")
        if params.get("RedefineParamList") is not None:
            self._RedefineParamList = KVMap()
            self._RedefineParamList._deserialize(params.get("RedefineParamList"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerunTaskInstancesAsyncResponse(AbstractModel):
    r"""RerunTaskInstancesAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 批量重跑操作的返回的异步id, 可以在接口GetAsyncJob获取具体执行详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""批量重跑操作的返回的异步id, 可以在接口GetAsyncJob获取具体执行详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ResourceFile(AbstractModel):
    r"""资源文件详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ResourceId: 资源文件ID
        :type ResourceId: str
        :param _ResourceName: 资源文件名称
        :type ResourceName: str
        :param _LocalPath: 资源文件路径
        :type LocalPath: str
        :param _RemotePath: 资源对象COS存储路径
        :type RemotePath: str
        :param _FileExtensionType: 资源文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileExtensionType: str
        :param _Size: 资源大小
        :type Size: str
        :param _CreatorUserUin: 创建用户ID
        :type CreatorUserUin: str
        :param _CreatorUserName: 创建用户名称
        :type CreatorUserName: str
        :param _UpdateUserName: 最后更新用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserName: str
        :param _UpdateUserUin: 最后更新用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserUin: str
        :param _BucketName: COS 桶
        :type BucketName: str
        :param _CosRegion: COS 地域
        :type CosRegion: str
        :param _ResourceSourceMode: 资源来源模式
        :type ResourceSourceMode: str
        :param _BundleId: 本地工程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _BundleInfo: 本地工程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._ResourceId = None
        self._ResourceName = None
        self._LocalPath = None
        self._RemotePath = None
        self._FileExtensionType = None
        self._Size = None
        self._CreatorUserUin = None
        self._CreatorUserName = None
        self._UpdateUserName = None
        self._UpdateUserUin = None
        self._BucketName = None
        self._CosRegion = None
        self._ResourceSourceMode = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceId(self):
        r"""资源文件ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""资源文件名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def LocalPath(self):
        r"""资源文件路径
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def RemotePath(self):
        r"""资源对象COS存储路径
        :rtype: str
        """
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, RemotePath):
        self._RemotePath = RemotePath

    @property
    def FileExtensionType(self):
        r"""资源文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileExtensionType

    @FileExtensionType.setter
    def FileExtensionType(self, FileExtensionType):
        self._FileExtensionType = FileExtensionType

    @property
    def Size(self):
        r"""资源大小
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def CreatorUserUin(self):
        r"""创建用户ID
        :rtype: str
        """
        return self._CreatorUserUin

    @CreatorUserUin.setter
    def CreatorUserUin(self, CreatorUserUin):
        self._CreatorUserUin = CreatorUserUin

    @property
    def CreatorUserName(self):
        r"""创建用户名称
        :rtype: str
        """
        return self._CreatorUserName

    @CreatorUserName.setter
    def CreatorUserName(self, CreatorUserName):
        self._CreatorUserName = CreatorUserName

    @property
    def UpdateUserName(self):
        r"""最后更新用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateUserName

    @UpdateUserName.setter
    def UpdateUserName(self, UpdateUserName):
        self._UpdateUserName = UpdateUserName

    @property
    def UpdateUserUin(self):
        r"""最后更新用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def BucketName(self):
        r"""COS 桶
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def CosRegion(self):
        r"""COS 地域
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def ResourceSourceMode(self):
        r"""资源来源模式
        :rtype: str
        """
        return self._ResourceSourceMode

    @ResourceSourceMode.setter
    def ResourceSourceMode(self, ResourceSourceMode):
        self._ResourceSourceMode = ResourceSourceMode

    @property
    def BundleId(self):
        r"""本地工程ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""本地工程信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._LocalPath = params.get("LocalPath")
        self._RemotePath = params.get("RemotePath")
        self._FileExtensionType = params.get("FileExtensionType")
        self._Size = params.get("Size")
        self._CreatorUserUin = params.get("CreatorUserUin")
        self._CreatorUserName = params.get("CreatorUserName")
        self._UpdateUserName = params.get("UpdateUserName")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._BucketName = params.get("BucketName")
        self._CosRegion = params.get("CosRegion")
        self._ResourceSourceMode = params.get("ResourceSourceMode")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFileItem(AbstractModel):
    r"""获取资源文件列表item

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源文件ID
        :type ResourceId: str
        :param _ResourceName: 资源文件名称
        :type ResourceName: str
        :param _FileExtensionType: 资源文件类型
        :type FileExtensionType: str
        :param _LocalPath: 资源路径
        :type LocalPath: str
        """
        self._ResourceId = None
        self._ResourceName = None
        self._FileExtensionType = None
        self._LocalPath = None

    @property
    def ResourceId(self):
        r"""资源文件ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""资源文件名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def FileExtensionType(self):
        r"""资源文件类型
        :rtype: str
        """
        return self._FileExtensionType

    @FileExtensionType.setter
    def FileExtensionType(self, FileExtensionType):
        self._FileExtensionType = FileExtensionType

    @property
    def LocalPath(self):
        r"""资源路径
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._FileExtensionType = params.get("FileExtensionType")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFilePage(AbstractModel):
    r"""资源文件分页

    """

    def __init__(self):
        r"""
        :param _Items: 任务集合信息
        :type Items: list of ResourceFileItem
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _PageNumber: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 每页显示数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        """
        self._Items = None
        self._TotalPageNumber = None
        self._TotalCount = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Items(self):
        r"""任务集合信息
        :rtype: list of ResourceFileItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def TotalCount(self):
        r"""总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PageNumber(self):
        r"""当前页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ResourceFileItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._TotalCount = params.get("TotalCount")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFolder(AbstractModel):
    r"""资源文件夹详情

    """

    def __init__(self):
        r"""
        :param _FolderId: 资源文件夹ID
        :type FolderId: str
        :param _CreateUserUin: 创建人ID
        :type CreateUserUin: str
        :param _CreateUserName: 创建人名称
        :type CreateUserName: str
        :param _FolderPath: 文件夹路径
        :type FolderPath: str
        :param _FolderName: 文件夹名称
        :type FolderName: str
        """
        self._FolderId = None
        self._CreateUserUin = None
        self._CreateUserName = None
        self._FolderPath = None
        self._FolderName = None

    @property
    def FolderId(self):
        r"""资源文件夹ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def CreateUserUin(self):
        r"""创建人ID
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def CreateUserName(self):
        r"""创建人名称
        :rtype: str
        """
        return self._CreateUserName

    @CreateUserName.setter
    def CreateUserName(self, CreateUserName):
        self._CreateUserName = CreateUserName

    @property
    def FolderPath(self):
        r"""文件夹路径
        :rtype: str
        """
        return self._FolderPath

    @FolderPath.setter
    def FolderPath(self, FolderPath):
        self._FolderPath = FolderPath

    @property
    def FolderName(self):
        r"""文件夹名称
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._CreateUserUin = params.get("CreateUserUin")
        self._CreateUserName = params.get("CreateUserName")
        self._FolderPath = params.get("FolderPath")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFolderPage(AbstractModel):
    r"""资源文件分页

    """

    def __init__(self):
        r"""
        :param _Items: 资源文件夹集合信息
        :type Items: list of ResourceFolder
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _PageNumber: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 每页显示数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        """
        self._Items = None
        self._TotalPageNumber = None
        self._TotalCount = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Items(self):
        r"""资源文件夹集合信息
        :rtype: list of ResourceFolder
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def TotalCount(self):
        r"""总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PageNumber(self):
        r"""当前页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ResourceFolder()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._TotalCount = params.get("TotalCount")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSQLScriptRequest(AbstractModel):
    r"""RunSQLScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScriptId: 脚本id
        :type ScriptId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScriptContent: 脚本内容，不传则默认执行已保存的全量脚本内容；若传递则要用Base64编码
        :type ScriptContent: str
        :param _Params: 高级运行参数，JSON格式base64编码
        :type Params: str
        """
        self._ScriptId = None
        self._ProjectId = None
        self._ScriptContent = None
        self._Params = None

    @property
    def ScriptId(self):
        r"""脚本id
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScriptContent(self):
        r"""脚本内容，不传则默认执行已保存的全量脚本内容；若传递则要用Base64编码
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def Params(self):
        r"""高级运行参数，JSON格式base64编码
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ProjectId = params.get("ProjectId")
        self._ScriptContent = params.get("ScriptContent")
        self._Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSQLScriptResponse(AbstractModel):
    r"""RunSQLScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据探索任务
        :type Data: :class:`tencentcloud.wedata.v20250806.models.JobDto`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""数据探索任务
        :rtype: :class:`tencentcloud.wedata.v20250806.models.JobDto`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = JobDto()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SQLContentActionResult(AbstractModel):
    r"""SQL探索文件/文件夹操作结果

    """

    def __init__(self):
        r"""
        :param _Status: 操作是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        :param _FolderId: 文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        """
        self._Status = None
        self._FolderId = None

    @property
    def Status(self):
        r"""操作是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FolderId(self):
        r"""文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLFolderNode(AbstractModel):
    r"""SQL脚本文件树节点

    """

    def __init__(self):
        r"""
        :param _Id: 唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 类型 folder，script
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _ParentFolderPath: 父文件夹path，/aaa/bbb/ccc
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentFolderPath: str
        :param _IsLeaf: 是否叶子节点
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLeaf: bool
        :param _Params: 业务参数	
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: str
        :param _AccessScope: 权限范围: SHARED, PRIVATE
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessScope: str
        :param _Path: 节点路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _CreateUserUin: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _NodePermission: 当前用户对节点拥有的权限	
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePermission: str
        :param _Children: 子节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of SQLFolderNode
        :param _OwnerUin: 文件责任人
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._ParentFolderPath = None
        self._IsLeaf = None
        self._Params = None
        self._AccessScope = None
        self._Path = None
        self._CreateUserUin = None
        self._NodePermission = None
        self._Children = None
        self._OwnerUin = None

    @property
    def Id(self):
        r"""唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""类型 folder，script
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ParentFolderPath(self):
        r"""父文件夹path，/aaa/bbb/ccc
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def IsLeaf(self):
        r"""是否叶子节点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf

    @property
    def Params(self):
        r"""业务参数	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def AccessScope(self):
        r"""权限范围: SHARED, PRIVATE
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def Path(self):
        r"""节点路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def CreateUserUin(self):
        r"""创建人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def NodePermission(self):
        r"""当前用户对节点拥有的权限	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodePermission

    @NodePermission.setter
    def NodePermission(self, NodePermission):
        self._NodePermission = NodePermission

    @property
    def Children(self):
        r"""子节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SQLFolderNode
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def OwnerUin(self):
        r"""文件责任人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._IsLeaf = params.get("IsLeaf")
        self._Params = params.get("Params")
        self._AccessScope = params.get("AccessScope")
        self._Path = params.get("Path")
        self._CreateUserUin = params.get("CreateUserUin")
        self._NodePermission = params.get("NodePermission")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = SQLFolderNode()
                obj._deserialize(item)
                self._Children.append(obj)
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLScript(AbstractModel):
    r"""数据探索脚本业务处理实体

    """

    def __init__(self):
        r"""
        :param _ScriptId: 脚本id
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptId: str
        :param _ScriptName: 脚本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptName: str
        :param _OwnerUin: 脚本所有者 uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _ParentFolderPath: 父文件夹path，/aaa/bbb/ccc
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentFolderPath: str
        :param _ScriptConfig: 脚本配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptConfig: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        :param _ScriptContent: 脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptContent: str
        :param _UpdateUserUin: 最近一次操作人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserUin: str
        :param _ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _UpdateTime: 更新时间 yyyy-MM-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _CreateTime: 创建时间 yyyy-MM-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _AccessScope: 权限范围：SHARED, PRIVATE
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessScope: str
        :param _Path: 节点全路径，/aaa/bbb/ccc.ipynb，由各个节点的名称组成
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
        self._ScriptId = None
        self._ScriptName = None
        self._OwnerUin = None
        self._ParentFolderPath = None
        self._ScriptConfig = None
        self._ScriptContent = None
        self._UpdateUserUin = None
        self._ProjectId = None
        self._UpdateTime = None
        self._CreateTime = None
        self._AccessScope = None
        self._Path = None

    @property
    def ScriptId(self):
        r"""脚本id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ScriptName(self):
        r"""脚本名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScriptName

    @ScriptName.setter
    def ScriptName(self, ScriptName):
        self._ScriptName = ScriptName

    @property
    def OwnerUin(self):
        r"""脚本所有者 uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ParentFolderPath(self):
        r"""父文件夹path，/aaa/bbb/ccc
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def ScriptConfig(self):
        r"""脚本配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        """
        return self._ScriptConfig

    @ScriptConfig.setter
    def ScriptConfig(self, ScriptConfig):
        self._ScriptConfig = ScriptConfig

    @property
    def ScriptContent(self):
        r"""脚本内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def UpdateUserUin(self):
        r"""最近一次操作人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def ProjectId(self):
        r"""项目id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UpdateTime(self):
        r"""更新时间 yyyy-MM-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        r"""创建时间 yyyy-MM-dd hh:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AccessScope(self):
        r"""权限范围：SHARED, PRIVATE
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def Path(self):
        r"""节点全路径，/aaa/bbb/ccc.ipynb，由各个节点的名称组成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ScriptName = params.get("ScriptName")
        self._OwnerUin = params.get("OwnerUin")
        self._ParentFolderPath = params.get("ParentFolderPath")
        if params.get("ScriptConfig") is not None:
            self._ScriptConfig = SQLScriptConfig()
            self._ScriptConfig._deserialize(params.get("ScriptConfig"))
        self._ScriptContent = params.get("ScriptContent")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._ProjectId = params.get("ProjectId")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._AccessScope = params.get("AccessScope")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLScriptConfig(AbstractModel):
    r"""数据探索脚本配置

    """

    def __init__(self):
        r"""
        :param _DatasourceId: 数据源Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: str
        :param _DatasourceEnv: 数据源环境
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceEnv: str
        :param _ComputeResource: 计算资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputeResource: str
        :param _ExecutorGroupId: 执行资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupId: str
        :param _Params: 高级运行参数,变量替换，map-json String,String
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: str
        :param _AdvanceConfig: 高级设置，执行配置参数，map-json String,String. 采用Base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceConfig: str
        """
        self._DatasourceId = None
        self._DatasourceEnv = None
        self._ComputeResource = None
        self._ExecutorGroupId = None
        self._Params = None
        self._AdvanceConfig = None

    @property
    def DatasourceId(self):
        r"""数据源Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DatasourceId

    @DatasourceId.setter
    def DatasourceId(self, DatasourceId):
        self._DatasourceId = DatasourceId

    @property
    def DatasourceEnv(self):
        r"""数据源环境
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DatasourceEnv

    @DatasourceEnv.setter
    def DatasourceEnv(self, DatasourceEnv):
        self._DatasourceEnv = DatasourceEnv

    @property
    def ComputeResource(self):
        r"""计算资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComputeResource

    @ComputeResource.setter
    def ComputeResource(self, ComputeResource):
        self._ComputeResource = ComputeResource

    @property
    def ExecutorGroupId(self):
        r"""执行资源组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def Params(self):
        r"""高级运行参数,变量替换，map-json String,String
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def AdvanceConfig(self):
        r"""高级设置，执行配置参数，map-json String,String. 采用Base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AdvanceConfig

    @AdvanceConfig.setter
    def AdvanceConfig(self, AdvanceConfig):
        self._AdvanceConfig = AdvanceConfig


    def _deserialize(self, params):
        self._DatasourceId = params.get("DatasourceId")
        self._DatasourceEnv = params.get("DatasourceEnv")
        self._ComputeResource = params.get("ComputeResource")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._Params = params.get("Params")
        self._AdvanceConfig = params.get("AdvanceConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLStopResult(AbstractModel):
    r"""停止sql运行结果

    """

    def __init__(self):
        r"""
        :param _Status: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""是否成功
注意：此字段可能返回 null，表示取不到有效值。
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
        


class SetSuccessTaskInstancesAsyncRequest(AbstractModel):
    r"""SetSuccessTaskInstancesAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _InstanceKeyList: 实例id列表,可以从ListInstances中获取
        :type InstanceKeyList: list of str
        """
        self._ProjectId = None
        self._InstanceKeyList = None

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKeyList(self):
        r"""实例id列表,可以从ListInstances中获取
        :rtype: list of str
        """
        return self._InstanceKeyList

    @InstanceKeyList.setter
    def InstanceKeyList(self, InstanceKeyList):
        self._InstanceKeyList = InstanceKeyList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKeyList = params.get("InstanceKeyList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSuccessTaskInstancesAsyncResponse(AbstractModel):
    r"""SetSuccessTaskInstancesAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 批量置成功操作的返回的异步id, 可以在接口GetAsyncJob获取具体执行详情
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""批量置成功操作的返回的异步id, 可以在接口GetAsyncJob获取具体执行详情
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SqlCreateResult(AbstractModel):
    r"""创建数据探索脚本文件夹返回类

    """

    def __init__(self):
        r"""
        :param _FolderId: 文件夹id
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        """
        self._FolderId = None

    @property
    def FolderId(self):
        r"""文件夹id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOpsTasksAsyncRequest(AbstractModel):
    r"""StopOpsTasksAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目Id
        :type ProjectId: str
        :param _TaskIds: 任务Id列表
        :type TaskIds: list of str
        :param _KillInstance: 是否终止已生成实例，默认false
        :type KillInstance: bool
        """
        self._ProjectId = None
        self._TaskIds = None
        self._KillInstance = None

    @property
    def ProjectId(self):
        r"""所属项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskIds(self):
        r"""任务Id列表
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def KillInstance(self):
        r"""是否终止已生成实例，默认false
        :rtype: bool
        """
        return self._KillInstance

    @KillInstance.setter
    def KillInstance(self, KillInstance):
        self._KillInstance = KillInstance


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskIds = params.get("TaskIds")
        self._KillInstance = params.get("KillInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOpsTasksAsyncResponse(AbstractModel):
    r"""StopOpsTasksAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: AsyncId
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""AsyncId
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class StopSQLScriptRunRequest(AbstractModel):
    r"""StopSQLScriptRun请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 查询id
        :type JobId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._JobId = None
        self._ProjectId = None

    @property
    def JobId(self):
        r"""查询id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSQLScriptRunResponse(AbstractModel):
    r"""StopSQLScriptRun返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 执行结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLStopResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""执行结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLStopResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLStopResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SubmitTaskRequest(AbstractModel):
    r"""SubmitTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _VersionRemark: 版本备注
        :type VersionRemark: str
        """
        self._ProjectId = None
        self._TaskId = None
        self._VersionRemark = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def VersionRemark(self):
        r"""版本备注
        :rtype: str
        """
        return self._VersionRemark

    @VersionRemark.setter
    def VersionRemark(self, VersionRemark):
        self._VersionRemark = VersionRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._VersionRemark = params.get("VersionRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTaskResponse(AbstractModel):
    r"""SubmitTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 成功或者失败
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SubmitTaskResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""成功或者失败
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SubmitTaskResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SubmitTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SubmitTaskResult(AbstractModel):
    r"""提交数据开发任务结果

    """

    def __init__(self):
        r"""
        :param _VersionId: 生成的任务版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _Status: 提交状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._VersionId = None
        self._Status = None

    @property
    def VersionId(self):
        r"""生成的任务版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Status(self):
        r"""提交状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    r"""任务对象

    """

    def __init__(self):
        r"""
        :param _TaskBaseAttribute: 任务基本属性
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskBaseAttribute: :class:`tencentcloud.wedata.v20250806.models.TaskBaseAttribute`
        :param _TaskConfiguration: 任务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskConfiguration: :class:`tencentcloud.wedata.v20250806.models.TaskConfiguration`
        :param _TaskSchedulerConfiguration: 任务调度配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.TaskSchedulerConfiguration`
        """
        self._TaskBaseAttribute = None
        self._TaskConfiguration = None
        self._TaskSchedulerConfiguration = None

    @property
    def TaskBaseAttribute(self):
        r"""任务基本属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskBaseAttribute`
        """
        return self._TaskBaseAttribute

    @TaskBaseAttribute.setter
    def TaskBaseAttribute(self, TaskBaseAttribute):
        self._TaskBaseAttribute = TaskBaseAttribute

    @property
    def TaskConfiguration(self):
        r"""任务配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskConfiguration`
        """
        return self._TaskConfiguration

    @TaskConfiguration.setter
    def TaskConfiguration(self, TaskConfiguration):
        self._TaskConfiguration = TaskConfiguration

    @property
    def TaskSchedulerConfiguration(self):
        r"""任务调度配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskSchedulerConfiguration`
        """
        return self._TaskSchedulerConfiguration

    @TaskSchedulerConfiguration.setter
    def TaskSchedulerConfiguration(self, TaskSchedulerConfiguration):
        self._TaskSchedulerConfiguration = TaskSchedulerConfiguration


    def _deserialize(self, params):
        if params.get("TaskBaseAttribute") is not None:
            self._TaskBaseAttribute = TaskBaseAttribute()
            self._TaskBaseAttribute._deserialize(params.get("TaskBaseAttribute"))
        if params.get("TaskConfiguration") is not None:
            self._TaskConfiguration = TaskConfiguration()
            self._TaskConfiguration._deserialize(params.get("TaskConfiguration"))
        if params.get("TaskSchedulerConfiguration") is not None:
            self._TaskSchedulerConfiguration = TaskSchedulerConfiguration()
            self._TaskSchedulerConfiguration._deserialize(params.get("TaskSchedulerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskBaseAttribute(AbstractModel):
    r"""任务基本属性信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskTypeId: 任务类型ID：

* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeId: int
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _TaskLatestVersionNo: 最近一次保存版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskLatestVersionNo: str
        :param _TaskLatestSubmitVersionNo: 最近一次提交版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskLatestSubmitVersionNo: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _Status: 任务状态：
* N: 新建
* Y: 调度中
* F: 已下线
* O: 已暂停
* T: 下线中
* INVALID: 已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Submit: 任务最新提交状态，任务是否已经提交：true/false
注意：此字段可能返回 null，表示取不到有效值。
        :type Submit: bool
        :param _CreateTime: 任务创建时间，示例：2022-02-12 11:13:41
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _LastUpdateTime: 最后更新时间，示例：2025-08-13 16:34:06
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param _LastUpdateUserName: 最后更新人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateUserName: str
        :param _LastOpsTime: 最后运维时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOpsTime: str
        :param _LastOpsUserName: 最后运维人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOpsUserName: str
        :param _OwnerUin: 任务负责人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _TaskDescription: 任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskDescription: str
        :param _UpdateUserUin: 最近一次更新用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserUin: str
        :param _CreateUserUin: 创建用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        """
        self._TaskId = None
        self._TaskTypeId = None
        self._WorkflowId = None
        self._TaskName = None
        self._TaskLatestVersionNo = None
        self._TaskLatestSubmitVersionNo = None
        self._WorkflowName = None
        self._Status = None
        self._Submit = None
        self._CreateTime = None
        self._LastUpdateTime = None
        self._LastUpdateUserName = None
        self._LastOpsTime = None
        self._LastOpsUserName = None
        self._OwnerUin = None
        self._TaskDescription = None
        self._UpdateUserUin = None
        self._CreateUserUin = None

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskTypeId(self):
        r"""任务类型ID：

* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def TaskName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskLatestVersionNo(self):
        r"""最近一次保存版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskLatestVersionNo

    @TaskLatestVersionNo.setter
    def TaskLatestVersionNo(self, TaskLatestVersionNo):
        self._TaskLatestVersionNo = TaskLatestVersionNo

    @property
    def TaskLatestSubmitVersionNo(self):
        r"""最近一次提交版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskLatestSubmitVersionNo

    @TaskLatestSubmitVersionNo.setter
    def TaskLatestSubmitVersionNo(self, TaskLatestSubmitVersionNo):
        self._TaskLatestSubmitVersionNo = TaskLatestSubmitVersionNo

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def Status(self):
        r"""任务状态：
* N: 新建
* Y: 调度中
* F: 已下线
* O: 已暂停
* T: 下线中
* INVALID: 已失效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Submit(self):
        r"""任务最新提交状态，任务是否已经提交：true/false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Submit

    @Submit.setter
    def Submit(self, Submit):
        self._Submit = Submit

    @property
    def CreateTime(self):
        r"""任务创建时间，示例：2022-02-12 11:13:41
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""最后更新时间，示例：2025-08-13 16:34:06
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def LastUpdateUserName(self):
        r"""最后更新人名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUpdateUserName

    @LastUpdateUserName.setter
    def LastUpdateUserName(self, LastUpdateUserName):
        self._LastUpdateUserName = LastUpdateUserName

    @property
    def LastOpsTime(self):
        r"""最后运维时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastOpsTime

    @LastOpsTime.setter
    def LastOpsTime(self, LastOpsTime):
        self._LastOpsTime = LastOpsTime

    @property
    def LastOpsUserName(self):
        r"""最后运维人名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastOpsUserName

    @LastOpsUserName.setter
    def LastOpsUserName(self, LastOpsUserName):
        self._LastOpsUserName = LastOpsUserName

    @property
    def OwnerUin(self):
        r"""任务负责人ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskDescription(self):
        r"""任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def UpdateUserUin(self):
        r"""最近一次更新用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def CreateUserUin(self):
        r"""创建用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskTypeId = params.get("TaskTypeId")
        self._WorkflowId = params.get("WorkflowId")
        self._TaskName = params.get("TaskName")
        self._TaskLatestVersionNo = params.get("TaskLatestVersionNo")
        self._TaskLatestSubmitVersionNo = params.get("TaskLatestSubmitVersionNo")
        self._WorkflowName = params.get("WorkflowName")
        self._Status = params.get("Status")
        self._Submit = params.get("Submit")
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._LastUpdateUserName = params.get("LastUpdateUserName")
        self._LastOpsTime = params.get("LastOpsTime")
        self._LastOpsUserName = params.get("LastOpsUserName")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskDescription = params.get("TaskDescription")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._CreateUserUin = params.get("CreateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCode(AbstractModel):
    r"""任务代码

    """

    def __init__(self):
        r"""
        :param _CodeContent: 代码内容
        :type CodeContent: str
        :param _CodeFileSize: 代码文件大小，单位bytes
        :type CodeFileSize: int
        """
        self._CodeContent = None
        self._CodeFileSize = None

    @property
    def CodeContent(self):
        r"""代码内容
        :rtype: str
        """
        return self._CodeContent

    @CodeContent.setter
    def CodeContent(self, CodeContent):
        self._CodeContent = CodeContent

    @property
    def CodeFileSize(self):
        r"""代码文件大小，单位bytes
        :rtype: int
        """
        return self._CodeFileSize

    @CodeFileSize.setter
    def CodeFileSize(self, CodeFileSize):
        self._CodeFileSize = CodeFileSize


    def _deserialize(self, params):
        self._CodeContent = params.get("CodeContent")
        self._CodeFileSize = params.get("CodeFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCodeResult(AbstractModel):
    r"""任务代码

    """

    def __init__(self):
        r"""
        :param _CodeInfo: 代码内容
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeInfo: str
        :param _CodeFileSize: 代码文件大小，单位KB
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeFileSize: str
        """
        self._CodeInfo = None
        self._CodeFileSize = None

    @property
    def CodeInfo(self):
        r"""代码内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CodeInfo

    @CodeInfo.setter
    def CodeInfo(self, CodeInfo):
        self._CodeInfo = CodeInfo

    @property
    def CodeFileSize(self):
        r"""代码文件大小，单位KB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CodeFileSize

    @CodeFileSize.setter
    def CodeFileSize(self, CodeFileSize):
        self._CodeFileSize = CodeFileSize


    def _deserialize(self, params):
        self._CodeInfo = params.get("CodeInfo")
        self._CodeFileSize = params.get("CodeFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskConfiguration(AbstractModel):
    r"""任务配置信息

    """

    def __init__(self):
        r"""
        :param _CodeContent: 代码内容的Base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeContent: str
        :param _TaskExtConfigurationList: 任务扩展属性配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskExtConfigurationList: list of TaskExtParameter
        :param _DataCluster: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DataCluster: str
        :param _BrokerIp: 指定的运行节点
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerIp: str
        :param _YarnQueue: 资源池队列名称，需要通过 DescribeProjectClusterQueues 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type YarnQueue: str
        :param _SourceServiceId: 来源数据源ID, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceServiceId: str
        :param _SourceServiceType: 来源数据源类型, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceServiceType: str
        :param _SourceServiceName: 来源数据源名称, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceServiceName: str
        :param _TargetServiceId: 目标数据源ID, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetServiceId: str
        :param _TargetServiceType: 目标数据源类型, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetServiceType: str
        :param _TargetServiceName: 目标数据源名称, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetServiceName: str
        :param _ResourceGroup: 资源组ID： 需要通过 DescribeNormalSchedulerExecutorGroups 获取 ExecutorGroupId
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroup: str
        :param _ResourceGroupName: 资源组名称： 需要通过 DescribeNormalSchedulerExecutorGroups 获取 ExecutorGroupName
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _TaskSchedulingParameterList: 调度参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSchedulingParameterList: list of TaskSchedulingParameter
        :param _BundleId: Bundle使用的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _BundleInfo: Bundle信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleInfo: str
        """
        self._CodeContent = None
        self._TaskExtConfigurationList = None
        self._DataCluster = None
        self._BrokerIp = None
        self._YarnQueue = None
        self._SourceServiceId = None
        self._SourceServiceType = None
        self._SourceServiceName = None
        self._TargetServiceId = None
        self._TargetServiceType = None
        self._TargetServiceName = None
        self._ResourceGroup = None
        self._ResourceGroupName = None
        self._TaskSchedulingParameterList = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def CodeContent(self):
        r"""代码内容的Base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CodeContent

    @CodeContent.setter
    def CodeContent(self, CodeContent):
        self._CodeContent = CodeContent

    @property
    def TaskExtConfigurationList(self):
        r"""任务扩展属性配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskExtParameter
        """
        return self._TaskExtConfigurationList

    @TaskExtConfigurationList.setter
    def TaskExtConfigurationList(self, TaskExtConfigurationList):
        self._TaskExtConfigurationList = TaskExtConfigurationList

    @property
    def DataCluster(self):
        r"""集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataCluster

    @DataCluster.setter
    def DataCluster(self, DataCluster):
        self._DataCluster = DataCluster

    @property
    def BrokerIp(self):
        r"""指定的运行节点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp

    @property
    def YarnQueue(self):
        r"""资源池队列名称，需要通过 DescribeProjectClusterQueues 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._YarnQueue

    @YarnQueue.setter
    def YarnQueue(self, YarnQueue):
        self._YarnQueue = YarnQueue

    @property
    def SourceServiceId(self):
        r"""来源数据源ID, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceServiceId

    @SourceServiceId.setter
    def SourceServiceId(self, SourceServiceId):
        self._SourceServiceId = SourceServiceId

    @property
    def SourceServiceType(self):
        r"""来源数据源类型, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceServiceType

    @SourceServiceType.setter
    def SourceServiceType(self, SourceServiceType):
        self._SourceServiceType = SourceServiceType

    @property
    def SourceServiceName(self):
        r"""来源数据源名称, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceServiceName

    @SourceServiceName.setter
    def SourceServiceName(self, SourceServiceName):
        self._SourceServiceName = SourceServiceName

    @property
    def TargetServiceId(self):
        r"""目标数据源ID, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetServiceId

    @TargetServiceId.setter
    def TargetServiceId(self, TargetServiceId):
        self._TargetServiceId = TargetServiceId

    @property
    def TargetServiceType(self):
        r"""目标数据源类型, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetServiceType

    @TargetServiceType.setter
    def TargetServiceType(self, TargetServiceType):
        self._TargetServiceType = TargetServiceType

    @property
    def TargetServiceName(self):
        r"""目标数据源名称, 使用 ; 分隔, 需要通过 DescribeDataSourceWithoutInfo 获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetServiceName

    @TargetServiceName.setter
    def TargetServiceName(self, TargetServiceName):
        self._TargetServiceName = TargetServiceName

    @property
    def ResourceGroup(self):
        r"""资源组ID： 需要通过 DescribeNormalSchedulerExecutorGroups 获取 ExecutorGroupId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroup

    @ResourceGroup.setter
    def ResourceGroup(self, ResourceGroup):
        self._ResourceGroup = ResourceGroup

    @property
    def ResourceGroupName(self):
        r"""资源组名称： 需要通过 DescribeNormalSchedulerExecutorGroups 获取 ExecutorGroupName
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def TaskSchedulingParameterList(self):
        r"""调度参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskSchedulingParameter
        """
        return self._TaskSchedulingParameterList

    @TaskSchedulingParameterList.setter
    def TaskSchedulingParameterList(self, TaskSchedulingParameterList):
        self._TaskSchedulingParameterList = TaskSchedulingParameterList

    @property
    def BundleId(self):
        r"""Bundle使用的ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._CodeContent = params.get("CodeContent")
        if params.get("TaskExtConfigurationList") is not None:
            self._TaskExtConfigurationList = []
            for item in params.get("TaskExtConfigurationList"):
                obj = TaskExtParameter()
                obj._deserialize(item)
                self._TaskExtConfigurationList.append(obj)
        self._DataCluster = params.get("DataCluster")
        self._BrokerIp = params.get("BrokerIp")
        self._YarnQueue = params.get("YarnQueue")
        self._SourceServiceId = params.get("SourceServiceId")
        self._SourceServiceType = params.get("SourceServiceType")
        self._SourceServiceName = params.get("SourceServiceName")
        self._TargetServiceId = params.get("TargetServiceId")
        self._TargetServiceType = params.get("TargetServiceType")
        self._TargetServiceName = params.get("TargetServiceName")
        self._ResourceGroup = params.get("ResourceGroup")
        self._ResourceGroupName = params.get("ResourceGroupName")
        if params.get("TaskSchedulingParameterList") is not None:
            self._TaskSchedulingParameterList = []
            for item in params.get("TaskSchedulingParameterList"):
                obj = TaskSchedulingParameter()
                obj._deserialize(item)
                self._TaskSchedulingParameterList.append(obj)
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDataRegistry(AbstractModel):
    r"""任务数据库登记项

    """

    def __init__(self):
        r"""
        :param _DatasourceId: 数据源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasourceId: str
        :param _DatabaseName: 数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param _TableName: 表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param _PartitionName: 分区名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionName: str
        :param _DataFlowType: 输入输出表类型
      输入流
 UPSTREAM,
      输出流
  DOWNSTREAM;
注意：此字段可能返回 null，表示取不到有效值。
        :type DataFlowType: str
        :param _TablePhysicalId: 表物理唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TablePhysicalId: str
        :param _DbGuid: 库唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DbGuid: str
        :param _TableGuid: 表唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type TableGuid: str
        """
        self._DatasourceId = None
        self._DatabaseName = None
        self._TableName = None
        self._PartitionName = None
        self._DataFlowType = None
        self._TablePhysicalId = None
        self._DbGuid = None
        self._TableGuid = None

    @property
    def DatasourceId(self):
        r"""数据源ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DatasourceId

    @DatasourceId.setter
    def DatasourceId(self, DatasourceId):
        self._DatasourceId = DatasourceId

    @property
    def DatabaseName(self):
        r"""数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        r"""表名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def PartitionName(self):
        r"""分区名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PartitionName

    @PartitionName.setter
    def PartitionName(self, PartitionName):
        self._PartitionName = PartitionName

    @property
    def DataFlowType(self):
        r"""输入输出表类型
      输入流
 UPSTREAM,
      输出流
  DOWNSTREAM;
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataFlowType

    @DataFlowType.setter
    def DataFlowType(self, DataFlowType):
        self._DataFlowType = DataFlowType

    @property
    def TablePhysicalId(self):
        r"""表物理唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TablePhysicalId

    @TablePhysicalId.setter
    def TablePhysicalId(self, TablePhysicalId):
        self._TablePhysicalId = TablePhysicalId

    @property
    def DbGuid(self):
        r"""库唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DbGuid

    @DbGuid.setter
    def DbGuid(self, DbGuid):
        self._DbGuid = DbGuid

    @property
    def TableGuid(self):
        r"""表唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TableGuid

    @TableGuid.setter
    def TableGuid(self, TableGuid):
        self._TableGuid = TableGuid


    def _deserialize(self, params):
        self._DatasourceId = params.get("DatasourceId")
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._PartitionName = params.get("PartitionName")
        self._DataFlowType = params.get("DataFlowType")
        self._TablePhysicalId = params.get("TablePhysicalId")
        self._DbGuid = params.get("DbGuid")
        self._TableGuid = params.get("TableGuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDependDto(AbstractModel):
    r"""依赖任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _WorkflowId: 工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _Status: 任务状态:
- Y: 运行
- F: 停止
- O: 冻结
- T: 停止中
- INVALID: 已失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _TaskTypeId: 任务类型id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeId: int
        :param _TaskTypeDesc: 任务类型描述
 - 20 :  通用数据同步
 - 25 :  ETLTaskType
 - 26 :  ETLTaskType
 - 30 :  python
 - 31 :  pyspark
 - 34 :  hivesql
 - 35 :  shell
 - 36 :  sparksql
 - 21 :  jdbcsql
 - 32 :  dlc
 - 33 :  ImpalaTaskType
 - 40 :  CDWTaskType
 - 41 :  kettle
 - 42 :  TCHouse-X
 - 43 :  TCHouse-X SQL
 - 46 :  dlcsparkTaskType
 - 47 :  TiOneMachineLearningTaskType
 - 48 :  Trino
 - 50 :  DLCPyspark
 - 23 :  TencentDistributedSQL
 - 39 :  spark
 - 92 :  MRTaskType
 - 38 :  ShellScript
 - 70 :  HiveSQLScrip
 - 130 :  分支
 - 131 :  归并
 - 132 :  Notebook探索
 - 133 :  SSH节点
 - 134 :  StarRocks
 - 137 :  For-each
 - 10000 :  自定义业务通用
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeDesc: str
        :param _ScheduleDesc: 调度计划展示描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleDesc: str
        :param _StartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _DelayTime: 延迟时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayTime: int
        :param _CycleType: 周期类型：默认为 D

支持的类型为 

* O: 一次性
* Y: 年
* M: 月
* W: 周
* D: 天
* H: 小时
* I: 分钟
* C: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _OwnerUin: 负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _TaskAction: 弹性周期配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskAction: str
        :param _InitStrategy: 调度初始化策略
注意：此字段可能返回 null，表示取不到有效值。
        :type InitStrategy: str
        :param _CrontabExpression: crontab表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabExpression: str
        """
        self._TaskId = None
        self._TaskName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._ProjectId = None
        self._Status = None
        self._TaskTypeId = None
        self._TaskTypeDesc = None
        self._ScheduleDesc = None
        self._StartTime = None
        self._EndTime = None
        self._DelayTime = None
        self._CycleType = None
        self._OwnerUin = None
        self._TaskAction = None
        self._InitStrategy = None
        self._CrontabExpression = None

    @property
    def TaskId(self):
        r"""任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WorkflowId(self):
        r"""工作流id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def ProjectId(self):
        r"""项目id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""任务状态:
- Y: 运行
- F: 停止
- O: 冻结
- T: 停止中
- INVALID: 已失效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskTypeId(self):
        r"""任务类型id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskTypeDesc(self):
        r"""任务类型描述
 - 20 :  通用数据同步
 - 25 :  ETLTaskType
 - 26 :  ETLTaskType
 - 30 :  python
 - 31 :  pyspark
 - 34 :  hivesql
 - 35 :  shell
 - 36 :  sparksql
 - 21 :  jdbcsql
 - 32 :  dlc
 - 33 :  ImpalaTaskType
 - 40 :  CDWTaskType
 - 41 :  kettle
 - 42 :  TCHouse-X
 - 43 :  TCHouse-X SQL
 - 46 :  dlcsparkTaskType
 - 47 :  TiOneMachineLearningTaskType
 - 48 :  Trino
 - 50 :  DLCPyspark
 - 23 :  TencentDistributedSQL
 - 39 :  spark
 - 92 :  MRTaskType
 - 38 :  ShellScript
 - 70 :  HiveSQLScrip
 - 130 :  分支
 - 131 :  归并
 - 132 :  Notebook探索
 - 133 :  SSH节点
 - 134 :  StarRocks
 - 137 :  For-each
 - 10000 :  自定义业务通用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeDesc

    @TaskTypeDesc.setter
    def TaskTypeDesc(self, TaskTypeDesc):
        self._TaskTypeDesc = TaskTypeDesc

    @property
    def ScheduleDesc(self):
        r"""调度计划展示描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduleDesc

    @ScheduleDesc.setter
    def ScheduleDesc(self, ScheduleDesc):
        self._ScheduleDesc = ScheduleDesc

    @property
    def StartTime(self):
        r"""任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DelayTime(self):
        r"""延迟时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def CycleType(self):
        r"""周期类型：默认为 D

支持的类型为 

* O: 一次性
* Y: 年
* M: 月
* W: 周
* D: 天
* H: 小时
* I: 分钟
* C: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def OwnerUin(self):
        r"""负责人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskAction(self):
        r"""弹性周期配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskAction

    @TaskAction.setter
    def TaskAction(self, TaskAction):
        self._TaskAction = TaskAction

    @property
    def InitStrategy(self):
        r"""调度初始化策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InitStrategy

    @InitStrategy.setter
    def InitStrategy(self, InitStrategy):
        self._InitStrategy = InitStrategy

    @property
    def CrontabExpression(self):
        r"""crontab表达式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskTypeDesc = params.get("TaskTypeDesc")
        self._ScheduleDesc = params.get("ScheduleDesc")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DelayTime = params.get("DelayTime")
        self._CycleType = params.get("CycleType")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskAction = params.get("TaskAction")
        self._InitStrategy = params.get("InitStrategy")
        self._CrontabExpression = params.get("CrontabExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskExtParameter(AbstractModel):
    r"""任务扩展信息参数

    """

    def __init__(self):
        r"""
        :param _ParamKey: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamKey: str
        :param _ParamValue: 参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstance(AbstractModel):
    r"""调度任务实例实体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _InstanceKey: **实例唯一标识**
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceKey: str
        :param _FolderId: 文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        :param _FolderName: 文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderName: str
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _CurRunDate: 实例数据时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurRunDate: str
        :param _InstanceState: **实例状态**
- WAIT_EVENT: 等待事件
- WAIT_UPSTREAM: 等待上游
- WAIT_RUN: 等待运行
- RUNNING: 运行中
- SKIP_RUNNING: 跳过运行
- FAILED_RETRY: 失败重试
- EXPIRED: 失败
- COMPLETED: 成功
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceState: str
        :param _InstanceType: **实例类型**

- 0 表示补录类型
- 1 表示周期实例
- 2 表示非周期实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: int
        :param _OwnerUinList: 负责人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUinList: list of str
        :param _TotalRunNum: 累计运行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalRunNum: int
        :param _TaskType: 任务类型描述
        :type TaskType: str
        :param _TaskTypeId: 任务类型id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeId: int
        :param _CycleType: **任务周期类型**
支持过滤多个，条件间为 或 的过滤关系
* O: ONEOFF_CYCLE
* Y: YEAR_CYCLE
* M: MONTH_CYCLE
* W: WEEK_CYCLE
* D: DAY_CYCLE
* H: HOUR_CYCLE
* I: MINUTE_CYCLE
* C: CRONTAB_CYCLE
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _TryLimit: 每次运行失败，下发重试次数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type TryLimit: int
        :param _Tries: **失败重试次数**
再次使用 手动重跑 或 补录实例等方式触发运行时，会被重置为 0 后重新计数
注意：此字段可能返回 null，表示取不到有效值。
        :type Tries: int
        :param _StartTime: 运行开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 运行完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CostTime: 耗费时间, 单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: int
        :param _SchedulerTime: 计划调度时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerTime: str
        :param _LastUpdateTime: 实例最近更新时间, 时间格式为 yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param _ExecutorGroupId: 执行资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupId: str
        :param _ExecutorGroupName: 资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupName: str
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._FolderId = None
        self._FolderName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._TaskId = None
        self._TaskName = None
        self._CurRunDate = None
        self._InstanceState = None
        self._InstanceType = None
        self._OwnerUinList = None
        self._TotalRunNum = None
        self._TaskType = None
        self._TaskTypeId = None
        self._CycleType = None
        self._TryLimit = None
        self._Tries = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None
        self._SchedulerTime = None
        self._LastUpdateTime = None
        self._ExecutorGroupId = None
        self._ExecutorGroupName = None

    @property
    def ProjectId(self):
        r"""所属项目id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**实例唯一标识**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def FolderId(self):
        r"""文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def CurRunDate(self):
        r"""实例数据时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CurRunDate

    @CurRunDate.setter
    def CurRunDate(self, CurRunDate):
        self._CurRunDate = CurRunDate

    @property
    def InstanceState(self):
        r"""**实例状态**
- WAIT_EVENT: 等待事件
- WAIT_UPSTREAM: 等待上游
- WAIT_RUN: 等待运行
- RUNNING: 运行中
- SKIP_RUNNING: 跳过运行
- FAILED_RETRY: 失败重试
- EXPIRED: 失败
- COMPLETED: 成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def InstanceType(self):
        r"""**实例类型**

- 0 表示补录类型
- 1 表示周期实例
- 2 表示非周期实例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OwnerUinList(self):
        r"""负责人列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OwnerUinList

    @OwnerUinList.setter
    def OwnerUinList(self, OwnerUinList):
        self._OwnerUinList = OwnerUinList

    @property
    def TotalRunNum(self):
        r"""累计运行次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalRunNum

    @TotalRunNum.setter
    def TotalRunNum(self, TotalRunNum):
        self._TotalRunNum = TotalRunNum

    @property
    def TaskType(self):
        r"""任务类型描述
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskTypeId(self):
        r"""任务类型id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def CycleType(self):
        r"""**任务周期类型**
支持过滤多个，条件间为 或 的过滤关系
* O: ONEOFF_CYCLE
* Y: YEAR_CYCLE
* M: MONTH_CYCLE
* W: WEEK_CYCLE
* D: DAY_CYCLE
* H: HOUR_CYCLE
* I: MINUTE_CYCLE
* C: CRONTAB_CYCLE
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def TryLimit(self):
        r"""每次运行失败，下发重试次数限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TryLimit

    @TryLimit.setter
    def TryLimit(self, TryLimit):
        self._TryLimit = TryLimit

    @property
    def Tries(self):
        r"""**失败重试次数**
再次使用 手动重跑 或 补录实例等方式触发运行时，会被重置为 0 后重新计数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def StartTime(self):
        r"""运行开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""运行完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CostTime(self):
        r"""耗费时间, 单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def SchedulerTime(self):
        r"""计划调度时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SchedulerTime

    @SchedulerTime.setter
    def SchedulerTime(self, SchedulerTime):
        self._SchedulerTime = SchedulerTime

    @property
    def LastUpdateTime(self):
        r"""实例最近更新时间, 时间格式为 yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def ExecutorGroupId(self):
        r"""执行资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def ExecutorGroupName(self):
        r"""资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutorGroupName

    @ExecutorGroupName.setter
    def ExecutorGroupName(self, ExecutorGroupName):
        self._ExecutorGroupName = ExecutorGroupName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._CurRunDate = params.get("CurRunDate")
        self._InstanceState = params.get("InstanceState")
        self._InstanceType = params.get("InstanceType")
        self._OwnerUinList = params.get("OwnerUinList")
        self._TotalRunNum = params.get("TotalRunNum")
        self._TaskType = params.get("TaskType")
        self._TaskTypeId = params.get("TaskTypeId")
        self._CycleType = params.get("CycleType")
        self._TryLimit = params.get("TryLimit")
        self._Tries = params.get("Tries")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        self._SchedulerTime = params.get("SchedulerTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._ExecutorGroupName = params.get("ExecutorGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceDetail(AbstractModel):
    r"""调度任务实例详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _InstanceKey: **实例唯一标识**
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceKey: str
        :param _FolderId: 文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        :param _FolderName: 文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderName: str
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _TaskTypeId: taskType对应的id
        :type TaskTypeId: int
        :param _TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param _CycleType: **任务周期类型**
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _CurRunDate: 实例数据时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurRunDate: str
        :param _InstanceState: **实例状态**
- WAIT_EVENT: 等待事件
- WAIT_UPSTREAM: 等待上游
- WAIT_RUN: 等待运行
- RUNNING: 运行中
- SKIP_RUNNING: 跳过运行
- FAILED_RETRY: 失败重试
- EXPIRED: 失败
- COMPLETED: 成功
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceState: str
        :param _InstanceType: **实例类型**

- 0 表示补录类型
- 1 表示周期实例
- 2 表示非周期实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: int
        :param _OwnerUinList: 负责人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUinList: list of str
        :param _TotalRunNum: 累计运行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalRunNum: int
        :param _TryLimit: 每次运行失败，下发重试次数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type TryLimit: int
        :param _Tries: **失败重试次数**
再次使用 手动重跑 或 补录实例等方式触发运行时，会被重置为 0 后重新计数
注意：此字段可能返回 null，表示取不到有效值。
        :type Tries: int
        :param _CostTime: 耗费时间, 单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: int
        :param _StartTime: 运行开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 运行完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _SchedulerTime: 计划调度时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerTime: str
        :param _LastUpdateTime: 实例最近更新时间, 时间格式为 yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param _ExecutorGroupId: 执行资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupId: str
        :param _ExecutorGroupName: 资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupName: str
        :param _JobErrorMsg: 简要的任务失败信息
注意：此字段可能返回 null，表示取不到有效值。
        :type JobErrorMsg: str
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._FolderId = None
        self._FolderName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._TaskId = None
        self._TaskName = None
        self._TaskTypeId = None
        self._TaskType = None
        self._CycleType = None
        self._CurRunDate = None
        self._InstanceState = None
        self._InstanceType = None
        self._OwnerUinList = None
        self._TotalRunNum = None
        self._TryLimit = None
        self._Tries = None
        self._CostTime = None
        self._StartTime = None
        self._EndTime = None
        self._SchedulerTime = None
        self._LastUpdateTime = None
        self._ExecutorGroupId = None
        self._ExecutorGroupName = None
        self._JobErrorMsg = None

    @property
    def ProjectId(self):
        r"""所属项目id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**实例唯一标识**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def FolderId(self):
        r"""文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""文件夹名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskTypeId(self):
        r"""taskType对应的id
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskType(self):
        r"""任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def CycleType(self):
        r"""**任务周期类型**
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def CurRunDate(self):
        r"""实例数据时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CurRunDate

    @CurRunDate.setter
    def CurRunDate(self, CurRunDate):
        self._CurRunDate = CurRunDate

    @property
    def InstanceState(self):
        r"""**实例状态**
- WAIT_EVENT: 等待事件
- WAIT_UPSTREAM: 等待上游
- WAIT_RUN: 等待运行
- RUNNING: 运行中
- SKIP_RUNNING: 跳过运行
- FAILED_RETRY: 失败重试
- EXPIRED: 失败
- COMPLETED: 成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def InstanceType(self):
        r"""**实例类型**

- 0 表示补录类型
- 1 表示周期实例
- 2 表示非周期实例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OwnerUinList(self):
        r"""负责人列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OwnerUinList

    @OwnerUinList.setter
    def OwnerUinList(self, OwnerUinList):
        self._OwnerUinList = OwnerUinList

    @property
    def TotalRunNum(self):
        r"""累计运行次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalRunNum

    @TotalRunNum.setter
    def TotalRunNum(self, TotalRunNum):
        self._TotalRunNum = TotalRunNum

    @property
    def TryLimit(self):
        r"""每次运行失败，下发重试次数限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TryLimit

    @TryLimit.setter
    def TryLimit(self, TryLimit):
        self._TryLimit = TryLimit

    @property
    def Tries(self):
        r"""**失败重试次数**
再次使用 手动重跑 或 补录实例等方式触发运行时，会被重置为 0 后重新计数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def CostTime(self):
        r"""耗费时间, 单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def StartTime(self):
        r"""运行开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""运行完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SchedulerTime(self):
        r"""计划调度时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SchedulerTime

    @SchedulerTime.setter
    def SchedulerTime(self, SchedulerTime):
        self._SchedulerTime = SchedulerTime

    @property
    def LastUpdateTime(self):
        r"""实例最近更新时间, 时间格式为 yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def ExecutorGroupId(self):
        r"""执行资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def ExecutorGroupName(self):
        r"""资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutorGroupName

    @ExecutorGroupName.setter
    def ExecutorGroupName(self, ExecutorGroupName):
        self._ExecutorGroupName = ExecutorGroupName

    @property
    def JobErrorMsg(self):
        r"""简要的任务失败信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskType = params.get("TaskType")
        self._CycleType = params.get("CycleType")
        self._CurRunDate = params.get("CurRunDate")
        self._InstanceState = params.get("InstanceState")
        self._InstanceType = params.get("InstanceType")
        self._OwnerUinList = params.get("OwnerUinList")
        self._TotalRunNum = params.get("TotalRunNum")
        self._TryLimit = params.get("TryLimit")
        self._Tries = params.get("Tries")
        self._CostTime = params.get("CostTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SchedulerTime = params.get("SchedulerTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._ExecutorGroupName = params.get("ExecutorGroupName")
        self._JobErrorMsg = params.get("JobErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceExecutions(AbstractModel):
    r"""任务实例执行列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        :param _Items: 记录列表
        :type Items: list of InstanceExecution
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TotalCount(self):
        r"""结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""记录列表
        :rtype: list of InstanceExecution
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceExecution()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstancePage(AbstractModel):
    r"""实例列表分页实体

    """

    def __init__(self):
        r"""
        :param _TotalCount: **总条数**
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TotalPageNumber: **总分页数**
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPageNumber: int
        :param _PageNumber: 页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 每页条目数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _Items: 数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of TaskInstance
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._Items = None

    @property
    def TotalCount(self):
        r"""**总条数**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""**总分页数**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页条目数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Items(self):
        r"""数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskInstance
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskInstance()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOpsInfo(AbstractModel):
    r"""任务运维工作流列表详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskName: 任务名
        :type TaskName: str
        :param _OwnerUin: 负责人Id
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _Status: 任务状态:
- Y: 调度中
- F: 已下线
- O: 已暂停
- T: 下线中
- INVALID: 已失效
        :type Status: str
        :param _FolderId: 文件夹id
        :type FolderId: str
        :param _FolderName: 文件夹名字
        :type FolderName: str
        :param _WorkflowId: 工作流id
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
        :type WorkflowName: str
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _UpdateUserUin: 更新人名称
        :type UpdateUserUin: str
        :param _TaskTypeId: 任务类型Id：
* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :type TaskTypeId: int
        :param _TaskTypeDesc: 任务类型描述
 - 通用数据同步
 - ETLTaskType
 - ETLTaskType
 - python
 - pyspark
 - HiveSQLTaskType
 - shell
 - SparkSQLTaskType
 - JDBCSQLTaskType
 - DLCTaskType
 - ImpalaTaskType
 - CDWTaskType
 - kettle
 - DLCSparkTaskType
 - TiOne机器学习
 - TrinoTaskType
 - DLCPyspark
 - spark
 - mr
 - shell脚本
 - hivesql脚本
 - 自定义业务通用
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeDesc: str
        :param _CycleType: 任务周期类型
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _ExecutorGroupId: 资源组id
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutorGroupId: str
        :param _ScheduleDesc: 调度描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleDesc: str
        :param _ExecutorGroupName: 资源组名称
        :type ExecutorGroupName: str
        :param _LastSchedulerCommitTime: 最新调度提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastSchedulerCommitTime: str
        :param _FirstRunTime: 首次执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstRunTime: str
        :param _FirstSubmitTime: 最近一次提交时间
        :type FirstSubmitTime: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _LastUpdateTime: 最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        """
        self._TaskId = None
        self._TaskName = None
        self._OwnerUin = None
        self._Status = None
        self._FolderId = None
        self._FolderName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._ProjectId = None
        self._ProjectName = None
        self._UpdateUserUin = None
        self._TaskTypeId = None
        self._TaskTypeDesc = None
        self._CycleType = None
        self._ExecutorGroupId = None
        self._ScheduleDesc = None
        self._ExecutorGroupName = None
        self._LastSchedulerCommitTime = None
        self._FirstRunTime = None
        self._FirstSubmitTime = None
        self._CreateTime = None
        self._LastUpdateTime = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def OwnerUin(self):
        r"""负责人Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Status(self):
        r"""任务状态:
- Y: 调度中
- F: 已下线
- O: 已暂停
- T: 下线中
- INVALID: 已失效
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FolderId(self):
        r"""文件夹id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""文件夹名字
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def WorkflowId(self):
        r"""工作流id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def UpdateUserUin(self):
        r"""更新人名称
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def TaskTypeId(self):
        r"""任务类型Id：
* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskTypeDesc(self):
        r"""任务类型描述
 - 通用数据同步
 - ETLTaskType
 - ETLTaskType
 - python
 - pyspark
 - HiveSQLTaskType
 - shell
 - SparkSQLTaskType
 - JDBCSQLTaskType
 - DLCTaskType
 - ImpalaTaskType
 - CDWTaskType
 - kettle
 - DLCSparkTaskType
 - TiOne机器学习
 - TrinoTaskType
 - DLCPyspark
 - spark
 - mr
 - shell脚本
 - hivesql脚本
 - 自定义业务通用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskTypeDesc

    @TaskTypeDesc.setter
    def TaskTypeDesc(self, TaskTypeDesc):
        self._TaskTypeDesc = TaskTypeDesc

    @property
    def CycleType(self):
        r"""任务周期类型
* ONEOFF_CYCLE: 一次性
* YEAR_CYCLE: 年
* MONTH_CYCLE: 月
* WEEK_CYCLE: 周
* DAY_CYCLE: 天
* HOUR_CYCLE: 小时
* MINUTE_CYCLE: 分钟
* CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def ExecutorGroupId(self):
        r"""资源组id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def ScheduleDesc(self):
        r"""调度描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduleDesc

    @ScheduleDesc.setter
    def ScheduleDesc(self, ScheduleDesc):
        self._ScheduleDesc = ScheduleDesc

    @property
    def ExecutorGroupName(self):
        r"""资源组名称
        :rtype: str
        """
        return self._ExecutorGroupName

    @ExecutorGroupName.setter
    def ExecutorGroupName(self, ExecutorGroupName):
        self._ExecutorGroupName = ExecutorGroupName

    @property
    def LastSchedulerCommitTime(self):
        r"""最新调度提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastSchedulerCommitTime

    @LastSchedulerCommitTime.setter
    def LastSchedulerCommitTime(self, LastSchedulerCommitTime):
        self._LastSchedulerCommitTime = LastSchedulerCommitTime

    @property
    def FirstRunTime(self):
        r"""首次执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FirstRunTime

    @FirstRunTime.setter
    def FirstRunTime(self, FirstRunTime):
        self._FirstRunTime = FirstRunTime

    @property
    def FirstSubmitTime(self):
        r"""最近一次提交时间
        :rtype: str
        """
        return self._FirstSubmitTime

    @FirstSubmitTime.setter
    def FirstSubmitTime(self, FirstSubmitTime):
        self._FirstSubmitTime = FirstSubmitTime

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._OwnerUin = params.get("OwnerUin")
        self._Status = params.get("Status")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskTypeDesc = params.get("TaskTypeDesc")
        self._CycleType = params.get("CycleType")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._ScheduleDesc = params.get("ScheduleDesc")
        self._ExecutorGroupName = params.get("ExecutorGroupName")
        self._LastSchedulerCommitTime = params.get("LastSchedulerCommitTime")
        self._FirstRunTime = params.get("FirstRunTime")
        self._FirstSubmitTime = params.get("FirstSubmitTime")
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSchedulerConfiguration(AbstractModel):
    r"""任务调度配置信息

    """

    def __init__(self):
        r"""
        :param _CycleType: 周期类型：支持的类型为

ONEOFF_CYCLE: 一次性
YEAR_CYCLE: 年
MONTH_CYCLE: 月
WEEK_CYCLE: 周
DAY_CYCLE: 天
HOUR_CYCLE: 小时
MINUTE_CYCLE: 分钟
CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _ScheduleTimeZone: 时区
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleTimeZone: str
        :param _CrontabExpression: 0 2 3 1,L,2 * ?	
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabExpression: str
        :param _StartTime: 生效日期
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束日期
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _ExecutionStartTime: 执行时间 左闭区间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: 执行时间 右闭区间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionEndTime: str
        :param _ScheduleRunType: 调度类型: 0 正常调度 1 空跑调度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleRunType: int
        :param _CalendarOpen: 日历调度 取值为 0 和 1， 1为打开，0为关闭，默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :type CalendarOpen: str
        :param _CalendarId: 日历调度 日历 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CalendarId: str
        :param _CalendarName: 日历调度 日历名称, 需要从 DescribeScheduleCalendarPageList 中获取
注意：此字段可能返回 null，表示取不到有效值。
        :type CalendarName: str
        :param _SelfDepend: 自依赖, 默认值 serial, 取值为：parallel(并行), serial(串行), orderly(有序)
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfDepend: str
        :param _UpstreamDependencyConfigList: 上游依赖数组
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamDependencyConfigList: list of DependencyTaskBrief
        :param _DownStreamDependencyConfigList: 下游依赖数组
注意：此字段可能返回 null，表示取不到有效值。
        :type DownStreamDependencyConfigList: list of DependencyTaskBrief
        :param _EventListenerList: 事件数组
注意：此字段可能返回 null，表示取不到有效值。
        :type EventListenerList: list of EventListener
        :param _RunPriority: 任务调度优先级 运行优先级 4高 5中 6低 , 默认:6
注意：此字段可能返回 null，表示取不到有效值。
        :type RunPriority: int
        :param _RetryWait: 重试策略 重试等待时间,单位分钟: 默认: 5
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryWait: int
        :param _MaxRetryAttempts: 重试策略 最大尝试次数, 默认: 4
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetryAttempts: int
        :param _ExecutionTTL: 超时处理策略 运行耗时超时（单位：分钟）默认为 -1
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionTTL: int
        :param _WaitExecutionTotalTTL: 超时处理策略 等待总时长耗时超时（单位：分钟）默认为 -1
注意：此字段可能返回 null，表示取不到有效值。
        :type WaitExecutionTotalTTL: str
        :param _AllowRedoType: 重跑&补录配置, 默认为 ALL; , ALL 运行成功或失败后皆可重跑或补录, FAILURE 运行成功后不可重跑或补录，运行失败后可重跑或补录, NONE 运行成功或失败后皆不可重跑或补录;
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowRedoType: str
        :param _ParamTaskOutList: 输出参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTaskOutList: list of OutTaskParameter
        :param _ParamTaskInList: 输入参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTaskInList: list of InTaskParameter
        :param _TaskOutputRegistryList: 产出登记
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskOutputRegistryList: list of TaskDataRegistry
        :param _InitStrategy: **实例生成策略**
* T_PLUS_0: T+0生成,默认策略
* T_PLUS_1: T+1生成
注意：此字段可能返回 null，表示取不到有效值。
        :type InitStrategy: str
        """
        self._CycleType = None
        self._ScheduleTimeZone = None
        self._CrontabExpression = None
        self._StartTime = None
        self._EndTime = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None
        self._ScheduleRunType = None
        self._CalendarOpen = None
        self._CalendarId = None
        self._CalendarName = None
        self._SelfDepend = None
        self._UpstreamDependencyConfigList = None
        self._DownStreamDependencyConfigList = None
        self._EventListenerList = None
        self._RunPriority = None
        self._RetryWait = None
        self._MaxRetryAttempts = None
        self._ExecutionTTL = None
        self._WaitExecutionTotalTTL = None
        self._AllowRedoType = None
        self._ParamTaskOutList = None
        self._ParamTaskInList = None
        self._TaskOutputRegistryList = None
        self._InitStrategy = None

    @property
    def CycleType(self):
        r"""周期类型：支持的类型为

ONEOFF_CYCLE: 一次性
YEAR_CYCLE: 年
MONTH_CYCLE: 月
WEEK_CYCLE: 周
DAY_CYCLE: 天
HOUR_CYCLE: 小时
MINUTE_CYCLE: 分钟
CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def ScheduleTimeZone(self):
        r"""时区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone

    @property
    def CrontabExpression(self):
        r"""0 2 3 1,L,2 * ?	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def StartTime(self):
        r"""生效日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExecutionStartTime(self):
        r"""执行时间 左闭区间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""执行时间 右闭区间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime

    @property
    def ScheduleRunType(self):
        r"""调度类型: 0 正常调度 1 空跑调度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScheduleRunType

    @ScheduleRunType.setter
    def ScheduleRunType(self, ScheduleRunType):
        self._ScheduleRunType = ScheduleRunType

    @property
    def CalendarOpen(self):
        r"""日历调度 取值为 0 和 1， 1为打开，0为关闭，默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CalendarOpen

    @CalendarOpen.setter
    def CalendarOpen(self, CalendarOpen):
        self._CalendarOpen = CalendarOpen

    @property
    def CalendarId(self):
        r"""日历调度 日历 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CalendarId

    @CalendarId.setter
    def CalendarId(self, CalendarId):
        self._CalendarId = CalendarId

    @property
    def CalendarName(self):
        r"""日历调度 日历名称, 需要从 DescribeScheduleCalendarPageList 中获取
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CalendarName

    @CalendarName.setter
    def CalendarName(self, CalendarName):
        self._CalendarName = CalendarName

    @property
    def SelfDepend(self):
        r"""自依赖, 默认值 serial, 取值为：parallel(并行), serial(串行), orderly(有序)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SelfDepend

    @SelfDepend.setter
    def SelfDepend(self, SelfDepend):
        self._SelfDepend = SelfDepend

    @property
    def UpstreamDependencyConfigList(self):
        r"""上游依赖数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DependencyTaskBrief
        """
        return self._UpstreamDependencyConfigList

    @UpstreamDependencyConfigList.setter
    def UpstreamDependencyConfigList(self, UpstreamDependencyConfigList):
        self._UpstreamDependencyConfigList = UpstreamDependencyConfigList

    @property
    def DownStreamDependencyConfigList(self):
        r"""下游依赖数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DependencyTaskBrief
        """
        return self._DownStreamDependencyConfigList

    @DownStreamDependencyConfigList.setter
    def DownStreamDependencyConfigList(self, DownStreamDependencyConfigList):
        self._DownStreamDependencyConfigList = DownStreamDependencyConfigList

    @property
    def EventListenerList(self):
        r"""事件数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EventListener
        """
        return self._EventListenerList

    @EventListenerList.setter
    def EventListenerList(self, EventListenerList):
        self._EventListenerList = EventListenerList

    @property
    def RunPriority(self):
        r"""任务调度优先级 运行优先级 4高 5中 6低 , 默认:6
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RunPriority

    @RunPriority.setter
    def RunPriority(self, RunPriority):
        self._RunPriority = RunPriority

    @property
    def RetryWait(self):
        r"""重试策略 重试等待时间,单位分钟: 默认: 5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetryWait

    @RetryWait.setter
    def RetryWait(self, RetryWait):
        self._RetryWait = RetryWait

    @property
    def MaxRetryAttempts(self):
        r"""重试策略 最大尝试次数, 默认: 4
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxRetryAttempts

    @MaxRetryAttempts.setter
    def MaxRetryAttempts(self, MaxRetryAttempts):
        self._MaxRetryAttempts = MaxRetryAttempts

    @property
    def ExecutionTTL(self):
        r"""超时处理策略 运行耗时超时（单位：分钟）默认为 -1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExecutionTTL

    @ExecutionTTL.setter
    def ExecutionTTL(self, ExecutionTTL):
        self._ExecutionTTL = ExecutionTTL

    @property
    def WaitExecutionTotalTTL(self):
        r"""超时处理策略 等待总时长耗时超时（单位：分钟）默认为 -1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WaitExecutionTotalTTL

    @WaitExecutionTotalTTL.setter
    def WaitExecutionTotalTTL(self, WaitExecutionTotalTTL):
        self._WaitExecutionTotalTTL = WaitExecutionTotalTTL

    @property
    def AllowRedoType(self):
        r"""重跑&补录配置, 默认为 ALL; , ALL 运行成功或失败后皆可重跑或补录, FAILURE 运行成功后不可重跑或补录，运行失败后可重跑或补录, NONE 运行成功或失败后皆不可重跑或补录;
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AllowRedoType

    @AllowRedoType.setter
    def AllowRedoType(self, AllowRedoType):
        self._AllowRedoType = AllowRedoType

    @property
    def ParamTaskOutList(self):
        r"""输出参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OutTaskParameter
        """
        return self._ParamTaskOutList

    @ParamTaskOutList.setter
    def ParamTaskOutList(self, ParamTaskOutList):
        self._ParamTaskOutList = ParamTaskOutList

    @property
    def ParamTaskInList(self):
        r"""输入参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InTaskParameter
        """
        return self._ParamTaskInList

    @ParamTaskInList.setter
    def ParamTaskInList(self, ParamTaskInList):
        self._ParamTaskInList = ParamTaskInList

    @property
    def TaskOutputRegistryList(self):
        r"""产出登记
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskDataRegistry
        """
        return self._TaskOutputRegistryList

    @TaskOutputRegistryList.setter
    def TaskOutputRegistryList(self, TaskOutputRegistryList):
        self._TaskOutputRegistryList = TaskOutputRegistryList

    @property
    def InitStrategy(self):
        r"""**实例生成策略**
* T_PLUS_0: T+0生成,默认策略
* T_PLUS_1: T+1生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InitStrategy

    @InitStrategy.setter
    def InitStrategy(self, InitStrategy):
        self._InitStrategy = InitStrategy


    def _deserialize(self, params):
        self._CycleType = params.get("CycleType")
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        self._CrontabExpression = params.get("CrontabExpression")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        self._ScheduleRunType = params.get("ScheduleRunType")
        self._CalendarOpen = params.get("CalendarOpen")
        self._CalendarId = params.get("CalendarId")
        self._CalendarName = params.get("CalendarName")
        self._SelfDepend = params.get("SelfDepend")
        if params.get("UpstreamDependencyConfigList") is not None:
            self._UpstreamDependencyConfigList = []
            for item in params.get("UpstreamDependencyConfigList"):
                obj = DependencyTaskBrief()
                obj._deserialize(item)
                self._UpstreamDependencyConfigList.append(obj)
        if params.get("DownStreamDependencyConfigList") is not None:
            self._DownStreamDependencyConfigList = []
            for item in params.get("DownStreamDependencyConfigList"):
                obj = DependencyTaskBrief()
                obj._deserialize(item)
                self._DownStreamDependencyConfigList.append(obj)
        if params.get("EventListenerList") is not None:
            self._EventListenerList = []
            for item in params.get("EventListenerList"):
                obj = EventListener()
                obj._deserialize(item)
                self._EventListenerList.append(obj)
        self._RunPriority = params.get("RunPriority")
        self._RetryWait = params.get("RetryWait")
        self._MaxRetryAttempts = params.get("MaxRetryAttempts")
        self._ExecutionTTL = params.get("ExecutionTTL")
        self._WaitExecutionTotalTTL = params.get("WaitExecutionTotalTTL")
        self._AllowRedoType = params.get("AllowRedoType")
        if params.get("ParamTaskOutList") is not None:
            self._ParamTaskOutList = []
            for item in params.get("ParamTaskOutList"):
                obj = OutTaskParameter()
                obj._deserialize(item)
                self._ParamTaskOutList.append(obj)
        if params.get("ParamTaskInList") is not None:
            self._ParamTaskInList = []
            for item in params.get("ParamTaskInList"):
                obj = InTaskParameter()
                obj._deserialize(item)
                self._ParamTaskInList.append(obj)
        if params.get("TaskOutputRegistryList") is not None:
            self._TaskOutputRegistryList = []
            for item in params.get("TaskOutputRegistryList"):
                obj = TaskDataRegistry()
                obj._deserialize(item)
                self._TaskOutputRegistryList.append(obj)
        self._InitStrategy = params.get("InitStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSchedulingParameter(AbstractModel):
    r"""任务调度变量参数

    """

    def __init__(self):
        r"""
        :param _ParamKey: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamKey: str
        :param _ParamValue: 参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskVersion(AbstractModel):
    r"""任务版本列表信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 保存时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _VersionNum: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionNum: str
        :param _CreateUserUin: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _VersionId: 保存版本id
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _VersionRemark: 版本描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionRemark: str
        :param _ApproveStatus: 审批状态（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveStatus: str
        :param _Status: 生产状态（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ApproveUserUin: 审批人（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveUserUin: str
        """
        self._CreateTime = None
        self._VersionNum = None
        self._CreateUserUin = None
        self._VersionId = None
        self._VersionRemark = None
        self._ApproveStatus = None
        self._Status = None
        self._ApproveUserUin = None

    @property
    def CreateTime(self):
        r"""保存时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VersionNum(self):
        r"""版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def CreateUserUin(self):
        r"""创建人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def VersionId(self):
        r"""保存版本id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionRemark(self):
        r"""版本描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionRemark

    @VersionRemark.setter
    def VersionRemark(self, VersionRemark):
        self._VersionRemark = VersionRemark

    @property
    def ApproveStatus(self):
        r"""审批状态（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveStatus

    @ApproveStatus.setter
    def ApproveStatus(self, ApproveStatus):
        self._ApproveStatus = ApproveStatus

    @property
    def Status(self):
        r"""生产状态（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ApproveUserUin(self):
        r"""审批人（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveUserUin

    @ApproveUserUin.setter
    def ApproveUserUin(self, ApproveUserUin):
        self._ApproveUserUin = ApproveUserUin


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._VersionNum = params.get("VersionNum")
        self._CreateUserUin = params.get("CreateUserUin")
        self._VersionId = params.get("VersionId")
        self._VersionRemark = params.get("VersionRemark")
        self._ApproveStatus = params.get("ApproveStatus")
        self._Status = params.get("Status")
        self._ApproveUserUin = params.get("ApproveUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskVersionDetail(AbstractModel):
    r"""任务版本列表信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 保存时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _VersionNum: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionNum: str
        :param _CreateUserUin: 版本创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _VersionId: 保存版本Id
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _VersionRemark: 版本描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionRemark: str
        :param _ApproveStatus: 审批状态（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveStatus: str
        :param _ApproveTime: 生产状态（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveTime: str
        :param _Task: 版本的任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Task: :class:`tencentcloud.wedata.v20250806.models.Task`
        :param _ApproveUserUin: 审批人Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveUserUin: str
        """
        self._CreateTime = None
        self._VersionNum = None
        self._CreateUserUin = None
        self._VersionId = None
        self._VersionRemark = None
        self._ApproveStatus = None
        self._ApproveTime = None
        self._Task = None
        self._ApproveUserUin = None

    @property
    def CreateTime(self):
        r"""保存时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VersionNum(self):
        r"""版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def CreateUserUin(self):
        r"""版本创建人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def VersionId(self):
        r"""保存版本Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionRemark(self):
        r"""版本描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionRemark

    @VersionRemark.setter
    def VersionRemark(self, VersionRemark):
        self._VersionRemark = VersionRemark

    @property
    def ApproveStatus(self):
        r"""审批状态（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveStatus

    @ApproveStatus.setter
    def ApproveStatus(self, ApproveStatus):
        self._ApproveStatus = ApproveStatus

    @property
    def ApproveTime(self):
        r"""生产状态（只有提交版本有）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveTime

    @ApproveTime.setter
    def ApproveTime(self, ApproveTime):
        self._ApproveTime = ApproveTime

    @property
    def Task(self):
        r"""版本的任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.Task`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def ApproveUserUin(self):
        r"""审批人Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveUserUin

    @ApproveUserUin.setter
    def ApproveUserUin(self, ApproveUserUin):
        self._ApproveUserUin = ApproveUserUin


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._VersionNum = params.get("VersionNum")
        self._CreateUserUin = params.get("CreateUserUin")
        self._VersionId = params.get("VersionId")
        self._VersionRemark = params.get("VersionRemark")
        self._ApproveStatus = params.get("ApproveStatus")
        self._ApproveTime = params.get("ApproveTime")
        if params.get("Task") is not None:
            self._Task = Task()
            self._Task._deserialize(params.get("Task"))
        self._ApproveUserUin = params.get("ApproveUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeOutStrategyInfo(AbstractModel):
    r"""告警超时配置规则信息

    """

    def __init__(self):
        r"""
        :param _RuleType: 超时告警超时配置：

1.预计运行耗时超时，2.预计完成时间超时，3.预计等待调度耗时超时，4.预计周期内完成但实际未完成
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: int
        :param _Type: 超时值配置类型

1--指定值
2--平均值
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Hour: 超时指定值小时， 默认 为0
注意：此字段可能返回 null，表示取不到有效值。
        :type Hour: int
        :param _Min: 超时指定值分钟， 默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: int
        :param _ScheduleTimeZone: 超时时间对应的时区配置， 如 UTC+7, 默认为UTC+8
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleTimeZone: str
        """
        self._RuleType = None
        self._Type = None
        self._Hour = None
        self._Min = None
        self._ScheduleTimeZone = None

    @property
    def RuleType(self):
        r"""超时告警超时配置：

1.预计运行耗时超时，2.预计完成时间超时，3.预计等待调度耗时超时，4.预计周期内完成但实际未完成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def Type(self):
        r"""超时值配置类型

1--指定值
2--平均值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Hour(self):
        r"""超时指定值小时， 默认 为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def Min(self):
        r"""超时指定值分钟， 默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ScheduleTimeZone(self):
        r"""超时时间对应的时区配置， 如 UTC+7, 默认为UTC+8
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._Type = params.get("Type")
        self._Hour = params.get("Hour")
        self._Min = params.get("Min")
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeFileRequest(AbstractModel):
    r"""UpdateCodeFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _CodeFileId: 代码文件ID，参数值来自CreateCodeFile接口的返回
        :type CodeFileId: str
        :param _CodeFileConfig: 代码文件配置
        :type CodeFileConfig: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        :param _CodeFileContent: 代码文件内容
        :type CodeFileContent: str
        """
        self._ProjectId = None
        self._CodeFileId = None
        self._CodeFileConfig = None
        self._CodeFileContent = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeFileId(self):
        r"""代码文件ID，参数值来自CreateCodeFile接口的返回
        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId

    @property
    def CodeFileConfig(self):
        r"""代码文件配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        """
        return self._CodeFileConfig

    @CodeFileConfig.setter
    def CodeFileConfig(self, CodeFileConfig):
        self._CodeFileConfig = CodeFileConfig

    @property
    def CodeFileContent(self):
        r"""代码文件内容
        :rtype: str
        """
        return self._CodeFileContent

    @CodeFileContent.setter
    def CodeFileContent(self, CodeFileContent):
        self._CodeFileContent = CodeFileContent


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CodeFileId = params.get("CodeFileId")
        if params.get("CodeFileConfig") is not None:
            self._CodeFileConfig = CodeFileConfig()
            self._CodeFileConfig._deserialize(params.get("CodeFileConfig"))
        self._CodeFileContent = params.get("CodeFileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeFileResponse(AbstractModel):
    r"""UpdateCodeFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeFile()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateCodeFolderRequest(AbstractModel):
    r"""UpdateCodeFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _FolderId: 文件夹ID，参数值来自CreateCodeFolder接口的返回
        :type FolderId: str
        :param _FolderName: 文件夹名称
        :type FolderName: str
        """
        self._ProjectId = None
        self._FolderId = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""文件夹ID，参数值来自CreateCodeFolder接口的返回
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""文件夹名称
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeFolderResponse(AbstractModel):
    r"""UpdateCodeFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 执行结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderActionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""执行结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeStudioFolderActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateFolderResult(AbstractModel):
    r"""更新文件夹结果

    """

    def __init__(self):
        r"""
        :param _Status: 更新状态,true表示更新成功，false表示更新失败
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""更新状态,true表示更新成功，false表示更新失败
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
        


class UpdateOpsAlarmRuleRequest(AbstractModel):
    r"""UpdateOpsAlarmRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _AlarmRuleId: 告警规则唯一id，通过接口GetAlarmRule/ListAlarmRule获取
        :type AlarmRuleId: str
        :param _AlarmRuleName: 告警规则新的规则名称
        :type AlarmRuleName: str
        :param _MonitorObjectType: 监控对象类型, 
任务维度监控： 可按照任务/工作流/项目来配置：1.任务、2.工作流、3.项目（默认为1.任务） 
项目维度监控： 项目整体任务波动告警， 7：项目波动监控告警
        :type MonitorObjectType: int
        :param _MonitorObjectIds: 根据MonitorType 的设置传入不同的业务id，如下1（任务）： MonitorObjectIds为任务id列表2（工作流）： MonitorObjectIds 为工作流id列表(工作流id可从接口ListWorkflows获取)3（项目）： MonitorObjectIds为项目id列表
        :type MonitorObjectIds: list of str
        :param _AlarmTypes: 告警规则监控类型 failure：失败告警 ；overtime：超时告警 success：成功告警; backTrackingOrRerunSuccess: 补录重跑成功告警 backTrackingOrRerunFailure：补录重跑失败告警； 项目波动告警 projectFailureInstanceUpwardFluctuationAlarm： 当天失败实例数向上波动率超过阀值告警； projectFailureInstanceUpwardVolatilityAlarm：当天失败实例数向上波动量超过阀值告警 projectSuccessInstanceDownwardFluctuationAlarm：当天成功实例数向下波动率超过阀值告警； projectSuccessInstanceDownwardVolatilityAlarm： 当天成功实例数向下波动量超过阀值告警 projectFailureInstanceCountAlarm: 当天失败实例数超过阀值告警 projectFailureInstanceProportionAlarm： 当天失败实例数占比超过阀值告警 离线集成任务对账告警： reconciliationFailure： 离线对账任务失败告警 reconciliationOvertime： 离线对账任务运行超时告警 reconciliationMismatch： 数据对账任务不一致条数超过阀值告警
        :type AlarmTypes: list of str
        :param _AlarmRuleDetail: 告警规则配置信息 成功告警无需配置；失败告警可以配置首次失败告警或者所有重试失败告警；超时配置需要配置超时类型及超时阀值；项目波动告警需要配置波动率及防抖周期配置
        :type AlarmRuleDetail: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        :param _Status: 告警规则的启用状态0--禁用1--启用
        :type Status: int
        :param _AlarmLevel: 告警级别 1.普通、2.重要、3.紧急
        :type AlarmLevel: int
        :param _AlarmGroups: 告警接收人配置信息
        :type AlarmGroups: list of AlarmGroup
        :param _Description: 告警描述信息
        :type Description: str
        """
        self._ProjectId = None
        self._AlarmRuleId = None
        self._AlarmRuleName = None
        self._MonitorObjectType = None
        self._MonitorObjectIds = None
        self._AlarmTypes = None
        self._AlarmRuleDetail = None
        self._Status = None
        self._AlarmLevel = None
        self._AlarmGroups = None
        self._Description = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmRuleId(self):
        r"""告警规则唯一id，通过接口GetAlarmRule/ListAlarmRule获取
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId

    @property
    def AlarmRuleName(self):
        r"""告警规则新的规则名称
        :rtype: str
        """
        return self._AlarmRuleName

    @AlarmRuleName.setter
    def AlarmRuleName(self, AlarmRuleName):
        self._AlarmRuleName = AlarmRuleName

    @property
    def MonitorObjectType(self):
        r"""监控对象类型, 
任务维度监控： 可按照任务/工作流/项目来配置：1.任务、2.工作流、3.项目（默认为1.任务） 
项目维度监控： 项目整体任务波动告警， 7：项目波动监控告警
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def MonitorObjectIds(self):
        r"""根据MonitorType 的设置传入不同的业务id，如下1（任务）： MonitorObjectIds为任务id列表2（工作流）： MonitorObjectIds 为工作流id列表(工作流id可从接口ListWorkflows获取)3（项目）： MonitorObjectIds为项目id列表
        :rtype: list of str
        """
        return self._MonitorObjectIds

    @MonitorObjectIds.setter
    def MonitorObjectIds(self, MonitorObjectIds):
        self._MonitorObjectIds = MonitorObjectIds

    @property
    def AlarmTypes(self):
        r"""告警规则监控类型 failure：失败告警 ；overtime：超时告警 success：成功告警; backTrackingOrRerunSuccess: 补录重跑成功告警 backTrackingOrRerunFailure：补录重跑失败告警； 项目波动告警 projectFailureInstanceUpwardFluctuationAlarm： 当天失败实例数向上波动率超过阀值告警； projectFailureInstanceUpwardVolatilityAlarm：当天失败实例数向上波动量超过阀值告警 projectSuccessInstanceDownwardFluctuationAlarm：当天成功实例数向下波动率超过阀值告警； projectSuccessInstanceDownwardVolatilityAlarm： 当天成功实例数向下波动量超过阀值告警 projectFailureInstanceCountAlarm: 当天失败实例数超过阀值告警 projectFailureInstanceProportionAlarm： 当天失败实例数占比超过阀值告警 离线集成任务对账告警： reconciliationFailure： 离线对账任务失败告警 reconciliationOvertime： 离线对账任务运行超时告警 reconciliationMismatch： 数据对账任务不一致条数超过阀值告警
        :rtype: list of str
        """
        return self._AlarmTypes

    @AlarmTypes.setter
    def AlarmTypes(self, AlarmTypes):
        self._AlarmTypes = AlarmTypes

    @property
    def AlarmRuleDetail(self):
        r"""告警规则配置信息 成功告警无需配置；失败告警可以配置首次失败告警或者所有重试失败告警；超时配置需要配置超时类型及超时阀值；项目波动告警需要配置波动率及防抖周期配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        """
        return self._AlarmRuleDetail

    @AlarmRuleDetail.setter
    def AlarmRuleDetail(self, AlarmRuleDetail):
        self._AlarmRuleDetail = AlarmRuleDetail

    @property
    def Status(self):
        r"""告警规则的启用状态0--禁用1--启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmLevel(self):
        r"""告警级别 1.普通、2.重要、3.紧急
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmGroups(self):
        r"""告警接收人配置信息
        :rtype: list of AlarmGroup
        """
        return self._AlarmGroups

    @AlarmGroups.setter
    def AlarmGroups(self, AlarmGroups):
        self._AlarmGroups = AlarmGroups

    @property
    def Description(self):
        r"""告警描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmRuleId = params.get("AlarmRuleId")
        self._AlarmRuleName = params.get("AlarmRuleName")
        self._MonitorObjectType = params.get("MonitorObjectType")
        self._MonitorObjectIds = params.get("MonitorObjectIds")
        self._AlarmTypes = params.get("AlarmTypes")
        if params.get("AlarmRuleDetail") is not None:
            self._AlarmRuleDetail = AlarmRuleDetail()
            self._AlarmRuleDetail._deserialize(params.get("AlarmRuleDetail"))
        self._Status = params.get("Status")
        self._AlarmLevel = params.get("AlarmLevel")
        if params.get("AlarmGroups") is not None:
            self._AlarmGroups = []
            for item in params.get("AlarmGroups"):
                obj = AlarmGroup()
                obj._deserialize(item)
                self._AlarmGroups.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOpsAlarmRuleResponse(AbstractModel):
    r"""UpdateOpsAlarmRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 更新结果是否成功
true: 更新成功 false：更新失败/未更新
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ModifyAlarmRuleResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""更新结果是否成功
true: 更新成功 false：更新失败/未更新
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ModifyAlarmRuleResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ModifyAlarmRuleResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateOpsTasksOwnerRequest(AbstractModel):
    r"""UpdateOpsTasksOwner请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目Id
        :type ProjectId: str
        :param _TaskIds: 任务Id列表
        :type TaskIds: list of str
        :param _OwnerUin: 任务负责人Id
        :type OwnerUin: str
        """
        self._ProjectId = None
        self._TaskIds = None
        self._OwnerUin = None

    @property
    def ProjectId(self):
        r"""所属项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskIds(self):
        r"""任务Id列表
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def OwnerUin(self):
        r"""任务负责人Id
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskIds = params.get("TaskIds")
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOpsTasksOwnerResponse(AbstractModel):
    r"""UpdateOpsTasksOwner返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 操作结果
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateTasksOwner`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""操作结果
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTasksOwner`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateTasksOwner()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateResourceFileRequest(AbstractModel):
    r"""UpdateResourceFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ResourceId: 资源文件ID,可通过ListResourceFiles接口获取
        :type ResourceId: str
        :param _ResourceFile: - 上传文件及手填两种方式只能选择其一，如果两者均提供，取值顺序为文件>手填值
-  手填值必须是存在的cos路径, /datastudio/resource/ 为固定前缀, projectId 为项目ID,需传入具体值, parentFolderPath为父文件夹路径, name为文件名, 手填值取值示例:
     /datastudio/resource/projectId/parentFolderPath/name 

        :type ResourceFile: str
        :param _ResourceName: 资源名称, 尽可能和文件名保持一致
        :type ResourceName: str
        :param _BundleId: bundle客户端ID
        :type BundleId: str
        :param _BundleInfo: bundle客户端名称
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._ResourceId = None
        self._ResourceFile = None
        self._ResourceName = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceId(self):
        r"""资源文件ID,可通过ListResourceFiles接口获取
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceFile(self):
        r"""- 上传文件及手填两种方式只能选择其一，如果两者均提供，取值顺序为文件>手填值
-  手填值必须是存在的cos路径, /datastudio/resource/ 为固定前缀, projectId 为项目ID,需传入具体值, parentFolderPath为父文件夹路径, name为文件名, 手填值取值示例:
     /datastudio/resource/projectId/parentFolderPath/name 

        :rtype: str
        """
        return self._ResourceFile

    @ResourceFile.setter
    def ResourceFile(self, ResourceFile):
        self._ResourceFile = ResourceFile

    @property
    def ResourceName(self):
        r"""资源名称, 尽可能和文件名保持一致
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def BundleId(self):
        r"""bundle客户端ID
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""bundle客户端名称
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceId = params.get("ResourceId")
        self._ResourceFile = params.get("ResourceFile")
        self._ResourceName = params.get("ResourceName")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateResourceFileResponse(AbstractModel):
    r"""UpdateResourceFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 更新状态
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFileResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""更新状态
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFileResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateResourceFileResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateResourceFileResult(AbstractModel):
    r"""更新资源文件结果

    """

    def __init__(self):
        r"""
        :param _Status: true
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""true
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
        


class UpdateResourceFolderRequest(AbstractModel):
    r"""UpdateResourceFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _FolderId: 文件夹ID, 可通过ListResourceFolders接口获取
        :type FolderId: str
        :param _FolderName: 文件夹名称
        :type FolderName: str
        """
        self._ProjectId = None
        self._FolderId = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""文件夹ID, 可通过ListResourceFolders接口获取
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""文件夹名称
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateResourceFolderResponse(AbstractModel):
    r"""UpdateResourceFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 更新文件夹结果，如果更新失败则报错。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateFolderResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""更新文件夹结果，如果更新失败则报错。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateSQLFolderRequest(AbstractModel):
    r"""UpdateSQLFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FolderId: 文件夹Id
        :type FolderId: str
        :param _FolderName: 文件夹名称
        :type FolderName: str
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _AccessScope: 权限范围：SHARED, PRIVATE
        :type AccessScope: str
        """
        self._FolderId = None
        self._FolderName = None
        self._ProjectId = None
        self._AccessScope = None

    @property
    def FolderId(self):
        r"""文件夹Id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""文件夹名称
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AccessScope(self):
        r"""权限范围：SHARED, PRIVATE
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._ProjectId = params.get("ProjectId")
        self._AccessScope = params.get("AccessScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSQLFolderResponse(AbstractModel):
    r"""UpdateSQLFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 成功true，失败false
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""成功true，失败false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLContentActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateSQLScriptRequest(AbstractModel):
    r"""UpdateSQLScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScriptId: 探索脚本Id
        :type ScriptId: str
        :param _ProjectId: 项目Id
        :type ProjectId: str
        :param _ScriptConfig: 数据探索脚本配置
        :type ScriptConfig: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        :param _ScriptContent: 脚本内容, 需要用Base64编码
        :type ScriptContent: str
        """
        self._ScriptId = None
        self._ProjectId = None
        self._ScriptConfig = None
        self._ScriptContent = None

    @property
    def ScriptId(self):
        r"""探索脚本Id
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ProjectId(self):
        r"""项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScriptConfig(self):
        r"""数据探索脚本配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        """
        return self._ScriptConfig

    @ScriptConfig.setter
    def ScriptConfig(self, ScriptConfig):
        self._ScriptConfig = ScriptConfig

    @property
    def ScriptContent(self):
        r"""脚本内容, 需要用Base64编码
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ProjectId = params.get("ProjectId")
        if params.get("ScriptConfig") is not None:
            self._ScriptConfig = SQLScriptConfig()
            self._ScriptConfig._deserialize(params.get("ScriptConfig"))
        self._ScriptContent = params.get("ScriptContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSQLScriptResponse(AbstractModel):
    r"""UpdateSQLScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLScript()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateTaskBaseAttribute(AbstractModel):
    r"""更新任务基本属性信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _OwnerUin: 任务负责人ID
        :type OwnerUin: str
        :param _TaskDescription: 任务描述
        :type TaskDescription: str
        """
        self._TaskName = None
        self._OwnerUin = None
        self._TaskDescription = None

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def OwnerUin(self):
        r"""任务负责人ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskDescription(self):
        r"""任务描述
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskDescription = params.get("TaskDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTaskBrief(AbstractModel):
    r"""更新任务对象入参

    """

    def __init__(self):
        r"""
        :param _TaskBaseAttribute: 任务基本属性
        :type TaskBaseAttribute: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskBaseAttribute`
        :param _TaskConfiguration: 任务配置
        :type TaskConfiguration: :class:`tencentcloud.wedata.v20250806.models.TaskConfiguration`
        :param _TaskSchedulerConfiguration: 任务调度配置
        :type TaskSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.TaskSchedulerConfiguration`
        """
        self._TaskBaseAttribute = None
        self._TaskConfiguration = None
        self._TaskSchedulerConfiguration = None

    @property
    def TaskBaseAttribute(self):
        r"""任务基本属性
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskBaseAttribute`
        """
        return self._TaskBaseAttribute

    @TaskBaseAttribute.setter
    def TaskBaseAttribute(self, TaskBaseAttribute):
        self._TaskBaseAttribute = TaskBaseAttribute

    @property
    def TaskConfiguration(self):
        r"""任务配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskConfiguration`
        """
        return self._TaskConfiguration

    @TaskConfiguration.setter
    def TaskConfiguration(self, TaskConfiguration):
        self._TaskConfiguration = TaskConfiguration

    @property
    def TaskSchedulerConfiguration(self):
        r"""任务调度配置
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskSchedulerConfiguration`
        """
        return self._TaskSchedulerConfiguration

    @TaskSchedulerConfiguration.setter
    def TaskSchedulerConfiguration(self, TaskSchedulerConfiguration):
        self._TaskSchedulerConfiguration = TaskSchedulerConfiguration


    def _deserialize(self, params):
        if params.get("TaskBaseAttribute") is not None:
            self._TaskBaseAttribute = UpdateTaskBaseAttribute()
            self._TaskBaseAttribute._deserialize(params.get("TaskBaseAttribute"))
        if params.get("TaskConfiguration") is not None:
            self._TaskConfiguration = TaskConfiguration()
            self._TaskConfiguration._deserialize(params.get("TaskConfiguration"))
        if params.get("TaskSchedulerConfiguration") is not None:
            self._TaskSchedulerConfiguration = TaskSchedulerConfiguration()
            self._TaskSchedulerConfiguration._deserialize(params.get("TaskSchedulerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTaskRequest(AbstractModel):
    r"""UpdateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Task: 任务基本属性
        :type Task: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskBrief`
        """
        self._ProjectId = None
        self._TaskId = None
        self._Task = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Task(self):
        r"""任务基本属性
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskBrief`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        if params.get("Task") is not None:
            self._Task = UpdateTaskBrief()
            self._Task._deserialize(params.get("Task"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTaskResponse(AbstractModel):
    r"""UpdateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务ID
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务ID
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateTaskResult(AbstractModel):
    r"""更新任务返回体

    """

    def __init__(self):
        r"""
        :param _Status: 处理结果，成功返回 true，不成功返回 false
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""处理结果，成功返回 true，不成功返回 false
注意：此字段可能返回 null，表示取不到有效值。
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
        


class UpdateTasksOwner(AbstractModel):
    r"""批量修改任务负责人结果

    """

    def __init__(self):
        r"""
        :param _Status: 修改任务责任人结果
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""修改任务责任人结果
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
        


class UpdateWorkflowFolderRequest(AbstractModel):
    r"""UpdateWorkflowFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _FolderId: 文件夹ID，可通过ListWorkflowFolders接口获取
        :type FolderId: str
        :param _FolderName: 更新后的文件夹名称
        :type FolderName: str
        """
        self._ProjectId = None
        self._FolderId = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""文件夹ID，可通过ListWorkflowFolders接口获取
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""更新后的文件夹名称
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkflowFolderResponse(AbstractModel):
    r"""UpdateWorkflowFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 更新文件夹结果，如果更新失败则报错。
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateFolderResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""更新文件夹结果，如果更新失败则报错。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateWorkflowRequest(AbstractModel):
    r"""UpdateWorkflow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _WorkflowId: 工作流ID
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
        :type WorkflowName: str
        :param _OwnerUin: 责任人ID
        :type OwnerUin: str
        :param _WorkflowDesc: 备注
        :type WorkflowDesc: str
        :param _WorkflowParams: 工作流参数列表
        :type WorkflowParams: list of ParamInfo
        :param _WorkflowSchedulerConfiguration: 统一调度参数
        :type WorkflowSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfigurationInfo`
        :param _BundleId: BundleId项
        :type BundleId: str
        :param _BundleInfo: Bundle信息
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._OwnerUin = None
        self._WorkflowDesc = None
        self._WorkflowParams = None
        self._WorkflowSchedulerConfiguration = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowId(self):
        r"""工作流ID
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def OwnerUin(self):
        r"""责任人ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def WorkflowDesc(self):
        r"""备注
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def WorkflowParams(self):
        r"""工作流参数列表
        :rtype: list of ParamInfo
        """
        return self._WorkflowParams

    @WorkflowParams.setter
    def WorkflowParams(self, WorkflowParams):
        self._WorkflowParams = WorkflowParams

    @property
    def WorkflowSchedulerConfiguration(self):
        r"""统一调度参数
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfigurationInfo`
        """
        return self._WorkflowSchedulerConfiguration

    @WorkflowSchedulerConfiguration.setter
    def WorkflowSchedulerConfiguration(self, WorkflowSchedulerConfiguration):
        self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfiguration

    @property
    def BundleId(self):
        r"""BundleId项
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle信息
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._OwnerUin = params.get("OwnerUin")
        self._WorkflowDesc = params.get("WorkflowDesc")
        if params.get("WorkflowParams") is not None:
            self._WorkflowParams = []
            for item in params.get("WorkflowParams"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._WorkflowParams.append(obj)
        if params.get("WorkflowSchedulerConfiguration") is not None:
            self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfigurationInfo()
            self._WorkflowSchedulerConfiguration._deserialize(params.get("WorkflowSchedulerConfiguration"))
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkflowResponse(AbstractModel):
    r"""UpdateWorkflow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: true代表成功，false代表失败
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""true代表成功，false代表失败
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateWorkflowResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateWorkflowResult(AbstractModel):
    r"""更新工作流结果

    """

    def __init__(self):
        r"""
        :param _Status: 更新工作流结果
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""更新工作流结果
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
        


class WorkflowDetail(AbstractModel):
    r"""查询工作流详细信息

    """

    def __init__(self):
        r"""
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _OwnerUin: 责任人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _CreateUserUin: 创建人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        :param _WorkflowType: 工作流类型，cycle和manual
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowType: str
        :param _WorkflowParams: 工作流参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowParams: list of ParamInfo
        :param _WorkflowSchedulerConfiguration: 统一调度参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfiguration`
        :param _WorkflowDesc: 工作流描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowDesc: str
        :param _Path: 工作流所属路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _BundleId: BundleId项
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleId: str
        :param _BundleInfo: BundleInfo项
注意：此字段可能返回 null，表示取不到有效值。
        :type BundleInfo: str
        """
        self._WorkflowName = None
        self._OwnerUin = None
        self._CreateUserUin = None
        self._WorkflowType = None
        self._WorkflowParams = None
        self._WorkflowSchedulerConfiguration = None
        self._WorkflowDesc = None
        self._Path = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def OwnerUin(self):
        r"""责任人ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateUserUin(self):
        r"""创建人ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def WorkflowType(self):
        r"""工作流类型，cycle和manual
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def WorkflowParams(self):
        r"""工作流参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamInfo
        """
        return self._WorkflowParams

    @WorkflowParams.setter
    def WorkflowParams(self, WorkflowParams):
        self._WorkflowParams = WorkflowParams

    @property
    def WorkflowSchedulerConfiguration(self):
        r"""统一调度参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfiguration`
        """
        return self._WorkflowSchedulerConfiguration

    @WorkflowSchedulerConfiguration.setter
    def WorkflowSchedulerConfiguration(self, WorkflowSchedulerConfiguration):
        self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfiguration

    @property
    def WorkflowDesc(self):
        r"""工作流描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def Path(self):
        r"""工作流所属路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def BundleId(self):
        r"""BundleId项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""BundleInfo项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._WorkflowName = params.get("WorkflowName")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateUserUin = params.get("CreateUserUin")
        self._WorkflowType = params.get("WorkflowType")
        if params.get("WorkflowParams") is not None:
            self._WorkflowParams = []
            for item in params.get("WorkflowParams"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._WorkflowParams.append(obj)
        if params.get("WorkflowSchedulerConfiguration") is not None:
            self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfiguration()
            self._WorkflowSchedulerConfiguration._deserialize(params.get("WorkflowSchedulerConfiguration"))
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._Path = params.get("Path")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowFolder(AbstractModel):
    r"""文件夹信息

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _FolderId: 文件夹ID
        :type FolderId: str
        :param _FolderPath: 文件夹绝对路径
        :type FolderPath: str
        :param _CreateUserUin: 创建人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        """
        self._ProjectId = None
        self._FolderId = None
        self._FolderPath = None
        self._CreateUserUin = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""文件夹ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderPath(self):
        r"""文件夹绝对路径
        :rtype: str
        """
        return self._FolderPath

    @FolderPath.setter
    def FolderPath(self, FolderPath):
        self._FolderPath = FolderPath

    @property
    def CreateUserUin(self):
        r"""创建人ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        self._FolderPath = params.get("FolderPath")
        self._CreateUserUin = params.get("CreateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowFolderPage(AbstractModel):
    r"""资源文件分页

    """

    def __init__(self):
        r"""
        :param _PageNumber: 数据页数，大于等于1
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 每页显示的数据条数，最小为10条，最大为200 条
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _TotalCount: 文件夹总数
        :type TotalCount: int
        :param _TotalPageNumber: 总页数
        :type TotalPageNumber: int
        :param _Items: 文件夹列表
        :type Items: list of WorkflowFolder
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""数据页数，大于等于1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页显示的数据条数，最小为10条，最大为200 条
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""文件夹总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""总页数
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""文件夹列表
        :rtype: list of WorkflowFolder
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = WorkflowFolder()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowInfo(AbstractModel):
    r"""获取工作流的列表信息item

    """

    def __init__(self):
        r"""
        :param _WorkflowId: 工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowName: str
        :param _WorkflowType: 工作流类型，cycle及manual
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowType: str
        :param _OwnerUin: 负责人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 最新修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _UpdateUserUin: 最后更新人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateUserUin: str
        :param _WorkflowDesc: 工作流描述
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowDesc: str
        :param _CreateUserUin: 创建人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUserUin: str
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowType = None
        self._OwnerUin = None
        self._CreateTime = None
        self._ModifyTime = None
        self._UpdateUserUin = None
        self._WorkflowDesc = None
        self._CreateUserUin = None

    @property
    def WorkflowId(self):
        r"""工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowType(self):
        r"""工作流类型，cycle及manual
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def OwnerUin(self):
        r"""负责人ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""最新修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def UpdateUserUin(self):
        r"""最后更新人ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def WorkflowDesc(self):
        r"""工作流描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def CreateUserUin(self):
        r"""创建人ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowType = params.get("WorkflowType")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._CreateUserUin = params.get("CreateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowSchedulerConfiguration(AbstractModel):
    r"""工作流统一调度出参

    """

    def __init__(self):
        r"""
        :param _ScheduleTimeZone: 时区
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleTimeZone: str
        :param _CycleType: 周期类型：支持的类型为
ONEOFF_CYCLE: 一次性
YEAR_CYCLE: 年
MONTH_CYCLE: 月
WEEK_CYCLE: 周
DAY_CYCLE: 天
HOUR_CYCLE: 小时
MINUTE_CYCLE: 分钟
CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleType: str
        :param _SelfDepend: 自依赖, 默认值 serial, 取值为：parallel(并行), serial(串行), orderly(有序)
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfDepend: str
        :param _StartTime: 生效开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 生效结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _DependencyWorkflow: 工作流依赖，yes or no
注意：此字段可能返回 null，表示取不到有效值。
        :type DependencyWorkflow: str
        :param _ExecutionStartTime: 执行时间左闭区间，示例：00:00
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: 执行时间右闭区间，示例：23:59
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionEndTime: str
        :param _CrontabExpression: cron表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type CrontabExpression: str
        :param _CalendarOpen: 是否开启日历调度 1 开启 0关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type CalendarOpen: str
        :param _CalendarName: 日历名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CalendarName: str
        :param _CalendarId: 日历id
注意：此字段可能返回 null，表示取不到有效值。
        :type CalendarId: str
        """
        self._ScheduleTimeZone = None
        self._CycleType = None
        self._SelfDepend = None
        self._StartTime = None
        self._EndTime = None
        self._DependencyWorkflow = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None
        self._CrontabExpression = None
        self._CalendarOpen = None
        self._CalendarName = None
        self._CalendarId = None

    @property
    def ScheduleTimeZone(self):
        r"""时区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone

    @property
    def CycleType(self):
        r"""周期类型：支持的类型为
ONEOFF_CYCLE: 一次性
YEAR_CYCLE: 年
MONTH_CYCLE: 月
WEEK_CYCLE: 周
DAY_CYCLE: 天
HOUR_CYCLE: 小时
MINUTE_CYCLE: 分钟
CRONTAB_CYCLE: crontab表达式类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def SelfDepend(self):
        r"""自依赖, 默认值 serial, 取值为：parallel(并行), serial(串行), orderly(有序)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SelfDepend

    @SelfDepend.setter
    def SelfDepend(self, SelfDepend):
        self._SelfDepend = SelfDepend

    @property
    def StartTime(self):
        r"""生效开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""生效结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DependencyWorkflow(self):
        r"""工作流依赖，yes or no
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DependencyWorkflow

    @DependencyWorkflow.setter
    def DependencyWorkflow(self, DependencyWorkflow):
        self._DependencyWorkflow = DependencyWorkflow

    @property
    def ExecutionStartTime(self):
        r"""执行时间左闭区间，示例：00:00
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""执行时间右闭区间，示例：23:59
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime

    @property
    def CrontabExpression(self):
        r"""cron表达式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def CalendarOpen(self):
        r"""是否开启日历调度 1 开启 0关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CalendarOpen

    @CalendarOpen.setter
    def CalendarOpen(self, CalendarOpen):
        self._CalendarOpen = CalendarOpen

    @property
    def CalendarName(self):
        r"""日历名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CalendarName

    @CalendarName.setter
    def CalendarName(self, CalendarName):
        self._CalendarName = CalendarName

    @property
    def CalendarId(self):
        r"""日历id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CalendarId

    @CalendarId.setter
    def CalendarId(self, CalendarId):
        self._CalendarId = CalendarId


    def _deserialize(self, params):
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        self._CycleType = params.get("CycleType")
        self._SelfDepend = params.get("SelfDepend")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DependencyWorkflow = params.get("DependencyWorkflow")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        self._CrontabExpression = params.get("CrontabExpression")
        self._CalendarOpen = params.get("CalendarOpen")
        self._CalendarName = params.get("CalendarName")
        self._CalendarId = params.get("CalendarId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowSchedulerConfigurationInfo(AbstractModel):
    r"""工作流统一调度参数入参
    依赖任务信息

    取值说明表：

    | 当前任务周期类型 | 上游任务周期类型 | 配置方式 | MainCyclicConfig取值 | 时间维度/实例范围           | SubordinateCyclicConfig取值       | offset取值             |
    | ---------------- | ---------------- | -------- | -------------------- | --------------------------- | --------------------------------- | ---------------------- |
    | HOUR_CYCLE       | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | MINUTE_CYCLE     | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | DAY_CYCLE        | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | DAY_CYCLE        | WEEK_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | HOUR_CYCLE       | HOUR_CYCLE       | 推荐策略 | HOUR                 | 按小时/最近实例             | CURRENT_HOUR                      | 无                     |
    | HOUR_CYCLE       | HOUR_CYCLE       | 推荐策略 | HOUR                 | 按小时/前一周期             | PREVIOUS_HOUR_CYCLE               | 无                     |
    | HOUR_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | WEEK                 | 按周/上周                   | PREVIOUS_WEEK                     | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | WEEK                 | 按周/上周五                 | PREVIOUS_FRIDAY                   | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | WEEK                 | 按周/上周日                 | PREVIOUS_WEEKEND                  | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天         、          | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/前一天                 | PREVIOUS_DAY                      | 无                     |
    | WEEK_CYCLE       | ONEOFF_CYCLE     | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 推荐策略 | HOUR                 | 按小时/前一个小时(-60,0]    | PREVIOUS_HOUR_LATER_OFFSET_MINUTE | 无                     |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 推荐策略 | HOUR                 | 按小时/前一个小时           | PREVIOUS_HOUR                     | 无                     |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 推荐策略 | HOUR                 | 按小时/当前小时             | CURRENT_HOUR                      | 无                     |
    | YEAR_CYCLE       | WEEK_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | WEEK_CYCLE       | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | MINUTE_CYCLE     | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | WEEK_CYCLE       | HOUR_CYCLE       | 推荐策略 | WEEK                 | 按周/上周                   | PREVIOUS_WEEK                     | 无                     |
    | WEEK_CYCLE       | HOUR_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | MINUTE_CYCLE     | HOUR_CYCLE       | 推荐策略 | HOUR                 | 按小时/当前小时             | CURRENT_HOUR                      | 无                     |
    | HOUR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | HOUR_CYCLE       | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | MONTH_CYCLE      | HOUR_CYCLE       | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | ONEOFF_CYCLE     | 推荐策略 | MONTH                | 按月/当月                   | CURRENT_MONTH                     | 无                     |
    | DAY_CYCLE        | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | DAY_CYCLE        | MONTH_CYCLE      | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | MONTH_CYCLE      | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | ONEOFF_CYCLE     | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | MINUTE_CYCLE     | MINUTE_CYCLE     | 推荐策略 | MINUTE               | 按分钟/当前分钟             | CURRENT_MINUTE                    | 无                     |
    | MINUTE_CYCLE     | MINUTE_CYCLE     | 推荐策略 | MINUTE               | 按分钟/前一周期             | PREVIOUS_MINUTE_CYCLE             | 无                     |
    | YEAR_CYCLE       | MINUTE_CYCLE     | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | ONEOFF_CYCLE     | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | DAY_CYCLE        | MINUTE_CYCLE     | 推荐策略 | DAY                  | 按天/前一天(-24 * 60,0]     | PREVIOUS_DAY_LATER_OFFSET_MINUTE  | 无                     |
    | DAY_CYCLE        | MINUTE_CYCLE     | 推荐策略 | DAY                  | 按天/前一天                 | PREVIOUS_DAY                      | 无                     |
    | DAY_CYCLE        | MINUTE_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | MINUTE_CYCLE     | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | WEEK_CYCLE       | WEEK_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | YEAR_CYCLE       | YEAR_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | YEAR_CYCLE       | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | YEAR_CYCLE       | HOUR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | MINUTE_CYCLE     | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | ONEOFF_CYCLE     | MINUTE_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | HOUR_CYCLE       | ONEOFF_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | MINUTE_CYCLE     | 推荐策略 | WEEK                 | 按周/上周                   | PREVIOUS_WEEK                     | 无                     |
    | WEEK_CYCLE       | MINUTE_CYCLE     | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | DAY_CYCLE        | HOUR_CYCLE       | 推荐策略 | DAY                  | 按天/前一天(-24,0]          | PREVIOUS_DAY_LATER_OFFSET_HOUR    | 无                     |
    | DAY_CYCLE        | HOUR_CYCLE       | 推荐策略 | DAY                  | 按天/前一天[-24,0)          | PREVIOUS_DAY                      | 无                     |
    | DAY_CYCLE        | HOUR_CYCLE       | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本年所有月             | ALL_MONTH_OF_YEAR                 | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/上月末                 | PREVIOUS_END_OF_MONTH             | 无                     |
    | YEAR_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/上月初                 | PREVIOUS_BEGIN_OF_MONTH           | 无                     |
    | ONEOFF_CYCLE     | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | DAY_CYCLE        | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | ONEOFF_CYCLE     | HOUR_CYCLE       | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | DAY_CYCLE        | ONEOFF_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | MINUTE_CYCLE     | ONEOFF_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | WEEK_CYCLE       | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | WEEK_CYCLE       | MONTH_CYCLE      | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | YEAR_CYCLE       | ONEOFF_CYCLE     | 推荐策略 | YEAR                 | 按年/当年                   | CURRENT_YEAR                      | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | MONTH                | 按月/上月末                 | PREVIOUS_END_OF_MONTH             | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | MONTH_CYCLE      | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/前一天                 | PREVIOUS_DAY                      | 无                     |
    | YEAR_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/本年所有天             | ALL_DAY_OF_YEAR                   | 无                     |
    | YEAR_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | YEAR_CYCLE       | DAY_CYCLE        | 推荐策略 | DAY                  | 按天/前一天                 | PREVIOUS_DAY                      | 无                     |
    | HOUR_CYCLE       | WEEK_CYCLE       | 推荐策略 | WEEK                 | 按周/本周                   | CURRENT_WEEK                      | 无                     |
    | MONTH_CYCLE      | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/当月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | MONTH_CYCLE      | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | MONTH_CYCLE      | MINUTE_CYCLE     | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | MONTH_CYCLE      | MINUTE_CYCLE     | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | WEEK_CYCLE       | 推荐策略 | MONTH                | 按月/上月                   | PREVIOUS_MONTH                    | 无                     |
    | MONTH_CYCLE      | WEEK_CYCLE       | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | MONTH_CYCLE      | WEEK_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | DAY_CYCLE        | YEAR_CYCLE       | 推荐策略 | YEAR                 | 按年/本年                   | CURRENT_YEAR                      | 无                     |
    | DAY_CYCLE        | YEAR_CYCLE       | 推荐策略 | DAY                  | 按天/最近一次数据时间的实例 | RECENT_DATE                       | 无                     |
    | ONEOFF_CYCLE     | ONEOFF_CYCLE     | 推荐策略 | DAY                  | 按天/当天                   | CURRENT_DAY                       | 无                     |
    | ONEOFF_CYCLE     | MONTH_CYCLE      | 推荐策略 | MONTH                | 按月/本月                   | CURRENT_MONTH                     | 无                     |
    | CRONTAB_CYCLE    | CRONTAB_CYCLE    | 推荐策略 | CRONTAB              | 无                          | CURRENT                           | 无                     |
    | HOUR_CYCLE       | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | HOUR_CYCLE       | 自定义   | RANGE_HOUR           | 区间(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | DAY_CYCLE        | 自定义   | RANGE_DAY            | 区间(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | MINUTE_CYCLE     | 自定义   | RANGE_MINUTE         | 区间(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | HOUR_CYCLE       | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | MINUTE_CYCLE     | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | WEEK_CYCLE       | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | HOUR_CYCLE       | 自定义   | LIST_HOUR            | 列表(小时)                  | 无                                | 逗号分隔的整数，如-1,0 |
    | DAY_CYCLE        | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | YEAR_CYCLE       | DAY_CYCLE        | 自定义   | LIST_DAY             | 列表(天)                    | 无                                | 逗号分隔的整数，如-1,0 |
    | MONTH_CYCLE      | MINUTE_CYCLE     | 自定义   | LIST_MINUTE          | 列表(分钟)                  | 无                                | 逗号分隔的整数，如-1,0 |

    """

    def __init__(self):
        r"""
        :param _ScheduleTimeZone: 时区
        :type ScheduleTimeZone: str
        :param _CycleType: 周期类型：支持的类型为
ONEOFF_CYCLE: 一次性
YEAR_CYCLE: 年
MONTH_CYCLE: 月
WEEK_CYCLE: 周
DAY_CYCLE: 天
HOUR_CYCLE: 小时
MINUTE_CYCLE: 分钟
CRONTAB_CYCLE: crontab表达式类型
        :type CycleType: str
        :param _SelfDepend: 自依赖, 默认值 serial, 取值为：parallel(并行), serial(串行), orderly(有序)
        :type SelfDepend: str
        :param _StartTime: 生效开始时间
        :type StartTime: str
        :param _EndTime: 生效结束时间
        :type EndTime: str
        :param _CrontabExpression: cron表达式
        :type CrontabExpression: str
        :param _DependencyWorkflow: 工作流依赖，yes or no
        :type DependencyWorkflow: str
        :param _ModifyCycleValue: 0：不修改 1：将任务的上游依赖配置改为默认值
        :type ModifyCycleValue: str
        :param _ClearLink: 工作流存在跨工作流依赖且使用cron表达式调度。如果保存统一调度，会断开不支持的依赖关系
        :type ClearLink: bool
        :param _MainCyclicConfig: ModifyCycleValue为1的时候生效，表示默认修改的上游依赖-时间维度，取值为：
* CRONTAB
* DAY
* HOUR
* LIST_DAY
* LIST_HOUR
* LIST_MINUTE
* MINUTE
* MONTH
* RANGE_DAY
* RANGE_HOUR
* RANGE_MINUTE
* WEEK
* YEAR

https://capi.woa.com/object/detail?product=wedata&env=api_dev&version=2025-08-06&name=WorkflowSchedulerConfigurationInfo
        :type MainCyclicConfig: str
        :param _SubordinateCyclicConfig: ModifyCycleValue为1的时候生效，表示默认修改的上游依赖-实例范围
取值为：
* ALL_DAY_OF_YEAR
* ALL_MONTH_OF_YEAR
* CURRENT
* CURRENT_DAY
* CURRENT_HOUR
* CURRENT_MINUTE
* CURRENT_MONTH
* CURRENT_WEEK
* CURRENT_YEAR
* PREVIOUS_BEGIN_OF_MONTH
* PREVIOUS_DAY
* PREVIOUS_DAY_LATER_OFFSET_HOUR
* PREVIOUS_DAY_LATER_OFFSET_MINUTE
* PREVIOUS_END_OF_MONTH
* PREVIOUS_FRIDAY
* PREVIOUS_HOUR
* PREVIOUS_HOUR_CYCLE
* PREVIOUS_HOUR_LATER_OFFSET_MINUTE
* PREVIOUS_MINUTE_CYCLE
* PREVIOUS_MONTH
* PREVIOUS_WEEK
* PREVIOUS_WEEKEND
* RECENT_DATE

https://capi.woa.com/object/detail?product=wedata&env=api_dev&version=2025-08-06&name=WorkflowSchedulerConfigurationInfo
        :type SubordinateCyclicConfig: str
        :param _ExecutionStartTime: 执行时间左闭区间，示例：00:00，只有周期类型为MINUTE_CYCLE才需要填入
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: 执行时间右闭区间，示例：23:59，只有周期类型为MINUTE_CYCLE才需要填入
        :type ExecutionEndTime: str
        :param _CalendarOpen: 是否开启日历调度 1 开启 0关闭
        :type CalendarOpen: str
        :param _CalendarId: 日历id
        :type CalendarId: str
        """
        self._ScheduleTimeZone = None
        self._CycleType = None
        self._SelfDepend = None
        self._StartTime = None
        self._EndTime = None
        self._CrontabExpression = None
        self._DependencyWorkflow = None
        self._ModifyCycleValue = None
        self._ClearLink = None
        self._MainCyclicConfig = None
        self._SubordinateCyclicConfig = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None
        self._CalendarOpen = None
        self._CalendarId = None

    @property
    def ScheduleTimeZone(self):
        r"""时区
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone

    @property
    def CycleType(self):
        r"""周期类型：支持的类型为
ONEOFF_CYCLE: 一次性
YEAR_CYCLE: 年
MONTH_CYCLE: 月
WEEK_CYCLE: 周
DAY_CYCLE: 天
HOUR_CYCLE: 小时
MINUTE_CYCLE: 分钟
CRONTAB_CYCLE: crontab表达式类型
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def SelfDepend(self):
        r"""自依赖, 默认值 serial, 取值为：parallel(并行), serial(串行), orderly(有序)
        :rtype: str
        """
        return self._SelfDepend

    @SelfDepend.setter
    def SelfDepend(self, SelfDepend):
        self._SelfDepend = SelfDepend

    @property
    def StartTime(self):
        r"""生效开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""生效结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CrontabExpression(self):
        r"""cron表达式
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def DependencyWorkflow(self):
        r"""工作流依赖，yes or no
        :rtype: str
        """
        return self._DependencyWorkflow

    @DependencyWorkflow.setter
    def DependencyWorkflow(self, DependencyWorkflow):
        self._DependencyWorkflow = DependencyWorkflow

    @property
    def ModifyCycleValue(self):
        r"""0：不修改 1：将任务的上游依赖配置改为默认值
        :rtype: str
        """
        return self._ModifyCycleValue

    @ModifyCycleValue.setter
    def ModifyCycleValue(self, ModifyCycleValue):
        self._ModifyCycleValue = ModifyCycleValue

    @property
    def ClearLink(self):
        r"""工作流存在跨工作流依赖且使用cron表达式调度。如果保存统一调度，会断开不支持的依赖关系
        :rtype: bool
        """
        return self._ClearLink

    @ClearLink.setter
    def ClearLink(self, ClearLink):
        self._ClearLink = ClearLink

    @property
    def MainCyclicConfig(self):
        r"""ModifyCycleValue为1的时候生效，表示默认修改的上游依赖-时间维度，取值为：
* CRONTAB
* DAY
* HOUR
* LIST_DAY
* LIST_HOUR
* LIST_MINUTE
* MINUTE
* MONTH
* RANGE_DAY
* RANGE_HOUR
* RANGE_MINUTE
* WEEK
* YEAR

https://capi.woa.com/object/detail?product=wedata&env=api_dev&version=2025-08-06&name=WorkflowSchedulerConfigurationInfo
        :rtype: str
        """
        return self._MainCyclicConfig

    @MainCyclicConfig.setter
    def MainCyclicConfig(self, MainCyclicConfig):
        self._MainCyclicConfig = MainCyclicConfig

    @property
    def SubordinateCyclicConfig(self):
        r"""ModifyCycleValue为1的时候生效，表示默认修改的上游依赖-实例范围
取值为：
* ALL_DAY_OF_YEAR
* ALL_MONTH_OF_YEAR
* CURRENT
* CURRENT_DAY
* CURRENT_HOUR
* CURRENT_MINUTE
* CURRENT_MONTH
* CURRENT_WEEK
* CURRENT_YEAR
* PREVIOUS_BEGIN_OF_MONTH
* PREVIOUS_DAY
* PREVIOUS_DAY_LATER_OFFSET_HOUR
* PREVIOUS_DAY_LATER_OFFSET_MINUTE
* PREVIOUS_END_OF_MONTH
* PREVIOUS_FRIDAY
* PREVIOUS_HOUR
* PREVIOUS_HOUR_CYCLE
* PREVIOUS_HOUR_LATER_OFFSET_MINUTE
* PREVIOUS_MINUTE_CYCLE
* PREVIOUS_MONTH
* PREVIOUS_WEEK
* PREVIOUS_WEEKEND
* RECENT_DATE

https://capi.woa.com/object/detail?product=wedata&env=api_dev&version=2025-08-06&name=WorkflowSchedulerConfigurationInfo
        :rtype: str
        """
        return self._SubordinateCyclicConfig

    @SubordinateCyclicConfig.setter
    def SubordinateCyclicConfig(self, SubordinateCyclicConfig):
        self._SubordinateCyclicConfig = SubordinateCyclicConfig

    @property
    def ExecutionStartTime(self):
        r"""执行时间左闭区间，示例：00:00，只有周期类型为MINUTE_CYCLE才需要填入
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""执行时间右闭区间，示例：23:59，只有周期类型为MINUTE_CYCLE才需要填入
        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime

    @property
    def CalendarOpen(self):
        r"""是否开启日历调度 1 开启 0关闭
        :rtype: str
        """
        return self._CalendarOpen

    @CalendarOpen.setter
    def CalendarOpen(self, CalendarOpen):
        self._CalendarOpen = CalendarOpen

    @property
    def CalendarId(self):
        r"""日历id
        :rtype: str
        """
        return self._CalendarId

    @CalendarId.setter
    def CalendarId(self, CalendarId):
        self._CalendarId = CalendarId


    def _deserialize(self, params):
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        self._CycleType = params.get("CycleType")
        self._SelfDepend = params.get("SelfDepend")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CrontabExpression = params.get("CrontabExpression")
        self._DependencyWorkflow = params.get("DependencyWorkflow")
        self._ModifyCycleValue = params.get("ModifyCycleValue")
        self._ClearLink = params.get("ClearLink")
        self._MainCyclicConfig = params.get("MainCyclicConfig")
        self._SubordinateCyclicConfig = params.get("SubordinateCyclicConfig")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        self._CalendarOpen = params.get("CalendarOpen")
        self._CalendarId = params.get("CalendarId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        