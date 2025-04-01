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


class AddUserContactRequest(AbstractModel):
    """AddUserContact请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 联系人姓名，由中英文、数字、空格、!@#$%^&*()_+-=（）组成，不能以下划线开头，长度在20以内。
        :type Name: str
        :param _ContactInfo: 邮箱地址，支持大小写字母、数字、下划线、连字符及@字符， 只能以数字或字母开头，邮箱地址不可重复。
        :type ContactInfo: str
        :param _Product: 服务产品类型，固定值："mysql"。
        :type Product: str
        """
        self._Name = None
        self._ContactInfo = None
        self._Product = None

    @property
    def Name(self):
        """联系人姓名，由中英文、数字、空格、!@#$%^&*()_+-=（）组成，不能以下划线开头，长度在20以内。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContactInfo(self):
        """邮箱地址，支持大小写字母、数字、下划线、连字符及@字符， 只能以数字或字母开头，邮箱地址不可重复。
        :rtype: str
        """
        return self._ContactInfo

    @ContactInfo.setter
    def ContactInfo(self, ContactInfo):
        self._ContactInfo = ContactInfo

    @property
    def Product(self):
        """服务产品类型，固定值："mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ContactInfo = params.get("ContactInfo")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserContactResponse(AbstractModel):
    """AddUserContact返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 添加成功的联系人id。
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """添加成功的联系人id。
        :rtype: int
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


class Aggregation(AbstractModel):
    """mongodb慢查模板概览明细

    """

    def __init__(self):
        r"""
        :param _AvgExecTime: 平均执行时间（ms）。
        :type AvgExecTime: int
        :param _AvgDocsExamined: 平均扫描行数。
        :type AvgDocsExamined: int
        :param _SlowLogCount: 产生慢查次数（/天）。
        :type SlowLogCount: int
        :param _SortCount: 内存排序次数。
        :type SortCount: int
        :param _SlowLogs: 慢查模板概览。
        :type SlowLogs: list of str
        """
        self._AvgExecTime = None
        self._AvgDocsExamined = None
        self._SlowLogCount = None
        self._SortCount = None
        self._SlowLogs = None

    @property
    def AvgExecTime(self):
        """平均执行时间（ms）。
        :rtype: int
        """
        return self._AvgExecTime

    @AvgExecTime.setter
    def AvgExecTime(self, AvgExecTime):
        self._AvgExecTime = AvgExecTime

    @property
    def AvgDocsExamined(self):
        """平均扫描行数。
        :rtype: int
        """
        return self._AvgDocsExamined

    @AvgDocsExamined.setter
    def AvgDocsExamined(self, AvgDocsExamined):
        self._AvgDocsExamined = AvgDocsExamined

    @property
    def SlowLogCount(self):
        """产生慢查次数（/天）。
        :rtype: int
        """
        return self._SlowLogCount

    @SlowLogCount.setter
    def SlowLogCount(self, SlowLogCount):
        self._SlowLogCount = SlowLogCount

    @property
    def SortCount(self):
        """内存排序次数。
        :rtype: int
        """
        return self._SortCount

    @SortCount.setter
    def SortCount(self, SortCount):
        self._SortCount = SortCount

    @property
    def SlowLogs(self):
        """慢查模板概览。
        :rtype: list of str
        """
        return self._SlowLogs

    @SlowLogs.setter
    def SlowLogs(self, SlowLogs):
        self._SlowLogs = SlowLogs


    def _deserialize(self, params):
        self._AvgExecTime = params.get("AvgExecTime")
        self._AvgDocsExamined = params.get("AvgDocsExamined")
        self._SlowLogCount = params.get("SlowLogCount")
        self._SortCount = params.get("SortCount")
        self._SlowLogs = params.get("SlowLogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmProfileList(AbstractModel):
    """通知模板

    """

    def __init__(self):
        r"""
        :param _IsWebHook: 0-不是 1-是
        :type IsWebHook: int
        :param _ReceiveUinCount: 接收告警用户数量
        :type ReceiveUinCount: int
        :param _Lang: 语言
        :type Lang: str
        :param _TemplateType: 模板类型
        :type TemplateType: str
        :param _Remark: 备注
        :type Remark: str
        :param _ReceiveGroupCount: 接收组数量
        :type ReceiveGroupCount: int
        :param _UpdateUin: 更新用户的uin
        :type UpdateUin: int
        :param _ReceiveType: 接收类型
        :type ReceiveType: list of int
        :param _ReceiveInfo: 接收用户信息
        :type ReceiveInfo: list of ReceiveInfo
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _TemplateName: 模板名
        :type TemplateName: str
        :param _SendChannel: 发送渠道
        :type SendChannel: list of int
        :param _TemplateId: 模板id
        :type TemplateId: int
        :param _WebHookCount: webhook数量
        :type WebHookCount: int
        """
        self._IsWebHook = None
        self._ReceiveUinCount = None
        self._Lang = None
        self._TemplateType = None
        self._Remark = None
        self._ReceiveGroupCount = None
        self._UpdateUin = None
        self._ReceiveType = None
        self._ReceiveInfo = None
        self._UpdateTime = None
        self._TemplateName = None
        self._SendChannel = None
        self._TemplateId = None
        self._WebHookCount = None

    @property
    def IsWebHook(self):
        """0-不是 1-是
        :rtype: int
        """
        return self._IsWebHook

    @IsWebHook.setter
    def IsWebHook(self, IsWebHook):
        self._IsWebHook = IsWebHook

    @property
    def ReceiveUinCount(self):
        """接收告警用户数量
        :rtype: int
        """
        return self._ReceiveUinCount

    @ReceiveUinCount.setter
    def ReceiveUinCount(self, ReceiveUinCount):
        self._ReceiveUinCount = ReceiveUinCount

    @property
    def Lang(self):
        """语言
        :rtype: str
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def TemplateType(self):
        """模板类型
        :rtype: str
        """
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ReceiveGroupCount(self):
        """接收组数量
        :rtype: int
        """
        return self._ReceiveGroupCount

    @ReceiveGroupCount.setter
    def ReceiveGroupCount(self, ReceiveGroupCount):
        self._ReceiveGroupCount = ReceiveGroupCount

    @property
    def UpdateUin(self):
        """更新用户的uin
        :rtype: int
        """
        return self._UpdateUin

    @UpdateUin.setter
    def UpdateUin(self, UpdateUin):
        self._UpdateUin = UpdateUin

    @property
    def ReceiveType(self):
        """接收类型
        :rtype: list of int
        """
        return self._ReceiveType

    @ReceiveType.setter
    def ReceiveType(self, ReceiveType):
        self._ReceiveType = ReceiveType

    @property
    def ReceiveInfo(self):
        """接收用户信息
        :rtype: list of ReceiveInfo
        """
        return self._ReceiveInfo

    @ReceiveInfo.setter
    def ReceiveInfo(self, ReceiveInfo):
        self._ReceiveInfo = ReceiveInfo

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
    def TemplateName(self):
        """模板名
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def SendChannel(self):
        """发送渠道
        :rtype: list of int
        """
        return self._SendChannel

    @SendChannel.setter
    def SendChannel(self, SendChannel):
        self._SendChannel = SendChannel

    @property
    def TemplateId(self):
        """模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def WebHookCount(self):
        """webhook数量
        :rtype: int
        """
        return self._WebHookCount

    @WebHookCount.setter
    def WebHookCount(self, WebHookCount):
        self._WebHookCount = WebHookCount


    def _deserialize(self, params):
        self._IsWebHook = params.get("IsWebHook")
        self._ReceiveUinCount = params.get("ReceiveUinCount")
        self._Lang = params.get("Lang")
        self._TemplateType = params.get("TemplateType")
        self._Remark = params.get("Remark")
        self._ReceiveGroupCount = params.get("ReceiveGroupCount")
        self._UpdateUin = params.get("UpdateUin")
        self._ReceiveType = params.get("ReceiveType")
        if params.get("ReceiveInfo") is not None:
            self._ReceiveInfo = []
            for item in params.get("ReceiveInfo"):
                obj = ReceiveInfo()
                obj._deserialize(item)
                self._ReceiveInfo.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._TemplateName = params.get("TemplateName")
        self._SendChannel = params.get("SendChannel")
        self._TemplateId = params.get("TemplateId")
        self._WebHookCount = params.get("WebHookCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmsRules(AbstractModel):
    """告警规则

    """

    def __init__(self):
        r"""
        :param _Interval: 间隔
        :type Interval: int
        :param _Name: 告警名
        :type Name: str
        :param _Metric: 指标
        :type Metric: str
        :param _Operator: 操作符
        :type Operator: str
        :param _Severity: 等级 
fatal-致命
critical-严重
warning-告警
information-通知

        :type Severity: str
        :param _Value: 指标值
        :type Value: float
        """
        self._Interval = None
        self._Name = None
        self._Metric = None
        self._Operator = None
        self._Severity = None
        self._Value = None

    @property
    def Interval(self):
        """间隔
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Name(self):
        """告警名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Metric(self):
        """指标
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Operator(self):
        """操作符
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Severity(self):
        """等级 
fatal-致命
critical-严重
warning-告警
information-通知

        :rtype: str
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def Value(self):
        """指标值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        self._Name = params.get("Name")
        self._Metric = params.get("Metric")
        self._Operator = params.get("Operator")
        self._Severity = params.get("Severity")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditInstance(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        r"""
        :param _AuditStatus: 审计状态，已开通审计为：YES，未开通审计为：ON。
        :type AuditStatus: str
        :param _BillingAmount: 审计日志大小，为兼容老版本用。
        :type BillingAmount: int
        :param _BillingConfirmed: 计费确认状态，0-未确认；1-已确认。
        :type BillingConfirmed: int
        :param _ColdLogExpireDay: 低频存储时长。
        :type ColdLogExpireDay: int
        :param _ColdLogSize: 低频日志存储量单位MB。
        :type ColdLogSize: int
        :param _HotLogExpireDay: 高频日志存储天数。
        :type HotLogExpireDay: int
        :param _HotLogSize: 高频日志存储量，单位MB。
        :type HotLogSize: int
        :param _InstanceId: 实例Id。
        :type InstanceId: str
        :param _LogExpireDay: 日志保存总天数，为高频存储时长+低频存储时长。
        :type LogExpireDay: int
        :param _CreateTime: 实例创建时间。
        :type CreateTime: str
        :param _InstanceInfo: 实例详细信息。
        :type InstanceInfo: :class:`tencentcloud.dbbrain.v20210527.models.AuditInstanceInfo`
        """
        self._AuditStatus = None
        self._BillingAmount = None
        self._BillingConfirmed = None
        self._ColdLogExpireDay = None
        self._ColdLogSize = None
        self._HotLogExpireDay = None
        self._HotLogSize = None
        self._InstanceId = None
        self._LogExpireDay = None
        self._CreateTime = None
        self._InstanceInfo = None

    @property
    def AuditStatus(self):
        """审计状态，已开通审计为：YES，未开通审计为：ON。
        :rtype: str
        """
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def BillingAmount(self):
        """审计日志大小，为兼容老版本用。
        :rtype: int
        """
        return self._BillingAmount

    @BillingAmount.setter
    def BillingAmount(self, BillingAmount):
        self._BillingAmount = BillingAmount

    @property
    def BillingConfirmed(self):
        """计费确认状态，0-未确认；1-已确认。
        :rtype: int
        """
        return self._BillingConfirmed

    @BillingConfirmed.setter
    def BillingConfirmed(self, BillingConfirmed):
        self._BillingConfirmed = BillingConfirmed

    @property
    def ColdLogExpireDay(self):
        """低频存储时长。
        :rtype: int
        """
        return self._ColdLogExpireDay

    @ColdLogExpireDay.setter
    def ColdLogExpireDay(self, ColdLogExpireDay):
        self._ColdLogExpireDay = ColdLogExpireDay

    @property
    def ColdLogSize(self):
        """低频日志存储量单位MB。
        :rtype: int
        """
        return self._ColdLogSize

    @ColdLogSize.setter
    def ColdLogSize(self, ColdLogSize):
        self._ColdLogSize = ColdLogSize

    @property
    def HotLogExpireDay(self):
        """高频日志存储天数。
        :rtype: int
        """
        return self._HotLogExpireDay

    @HotLogExpireDay.setter
    def HotLogExpireDay(self, HotLogExpireDay):
        self._HotLogExpireDay = HotLogExpireDay

    @property
    def HotLogSize(self):
        """高频日志存储量，单位MB。
        :rtype: int
        """
        return self._HotLogSize

    @HotLogSize.setter
    def HotLogSize(self, HotLogSize):
        self._HotLogSize = HotLogSize

    @property
    def InstanceId(self):
        """实例Id。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        """日志保存总天数，为高频存储时长+低频存储时长。
        :rtype: int
        """
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def CreateTime(self):
        """实例创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InstanceInfo(self):
        """实例详细信息。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.AuditInstanceInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo


    def _deserialize(self, params):
        self._AuditStatus = params.get("AuditStatus")
        self._BillingAmount = params.get("BillingAmount")
        self._BillingConfirmed = params.get("BillingConfirmed")
        self._ColdLogExpireDay = params.get("ColdLogExpireDay")
        self._ColdLogSize = params.get("ColdLogSize")
        self._HotLogExpireDay = params.get("HotLogExpireDay")
        self._HotLogSize = params.get("HotLogSize")
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._CreateTime = params.get("CreateTime")
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = AuditInstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditInstanceFilter(AbstractModel):
    """实例列表查询条件

    """

    def __init__(self):
        r"""
        :param _Name: 搜索条件名称
        :type Name: str
        :param _Values: 要搜索的条件的值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """搜索条件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """要搜索的条件的值
        :rtype: list of str
        """
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
        


class AuditInstanceInfo(AbstractModel):
    """实例详情

    """

    def __init__(self):
        r"""
        :param _AppId: appId。
        :type AppId: int
        :param _AuditStatus: 审计状态，0-未开通审计；1-已开通审计。
        :type AuditStatus: int
        :param _InstanceId: 实例Id。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _ProjectId: 项目Id。
        :type ProjectId: int
        :param _Region: 实例所在地域。
        :type Region: str
        :param _ResourceTags: 资源Tags。
        :type ResourceTags: list of str
        """
        self._AppId = None
        self._AuditStatus = None
        self._InstanceId = None
        self._InstanceName = None
        self._ProjectId = None
        self._Region = None
        self._ResourceTags = None

    @property
    def AppId(self):
        """appId。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AuditStatus(self):
        """审计状态，0-未开通审计；1-已开通审计。
        :rtype: int
        """
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def InstanceId(self):
        """实例Id。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ProjectId(self):
        """项目Id。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        """实例所在地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ResourceTags(self):
        """资源Tags。
        :rtype: list of str
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AuditStatus = params.get("AuditStatus")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._ResourceTags = params.get("ResourceTags")
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
        :param _AsyncRequestId: 审计日志文件生成异步任务ID。
        :type AsyncRequestId: int
        :param _FileName: 审计日志文件名称。
        :type FileName: str
        :param _CreateTime: 审计日志文件创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param _Status: 文件状态值。可能返回的值为：
"creating" - 生成中;
"failed" - 创建失败;
"success" - 已生成;
        :type Status: str
        :param _FileSize: 文件大小，单位为 KB。
        :type FileSize: float
        :param _DownloadUrl: 审计日志下载地址。
        :type DownloadUrl: str
        :param _ErrMsg: 错误信息。
        :type ErrMsg: str
        :param _Progress: 文件生成进度。
        :type Progress: float
        :param _FinishTime: 文件生成成功时间。
        :type FinishTime: str
        """
        self._AsyncRequestId = None
        self._FileName = None
        self._CreateTime = None
        self._Status = None
        self._FileSize = None
        self._DownloadUrl = None
        self._ErrMsg = None
        self._Progress = None
        self._FinishTime = None

    @property
    def AsyncRequestId(self):
        """审计日志文件生成异步任务ID。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def FileName(self):
        """审计日志文件名称。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CreateTime(self):
        """审计日志文件创建时间。格式为 : "2019-03-20 17:09:13"。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        """文件状态值。可能返回的值为：
"creating" - 生成中;
"failed" - 创建失败;
"success" - 已生成;
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FileSize(self):
        """文件大小，单位为 KB。
        :rtype: float
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DownloadUrl(self):
        """审计日志下载地址。
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def ErrMsg(self):
        """错误信息。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Progress(self):
        """文件生成进度。
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def FinishTime(self):
        """文件生成成功时间。
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._FileName = params.get("FileName")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._FileSize = params.get("FileSize")
        self._DownloadUrl = params.get("DownloadUrl")
        self._ErrMsg = params.get("ErrMsg")
        self._Progress = params.get("Progress")
        self._FinishTime = params.get("FinishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFilter(AbstractModel):
    """过滤条件。可按设置的过滤条件过滤日志。

    """

    def __init__(self):
        r"""
        :param _Host: 客户端地址。
        :type Host: list of str
        :param _DBName: 数据库名称。
        :type DBName: list of str
        :param _User: 用户名。
        :type User: list of str
        :param _SentRows: 返回行数。表示筛选返回行数大于该值的审计日志。
        :type SentRows: int
        :param _AffectRows: 影响行数。表示筛选影响行数大于该值的审计日志。
        :type AffectRows: int
        :param _ExecTime: 执行时间。单位为：µs。表示筛选执行时间大于该值的审计日志。
        :type ExecTime: int
        """
        self._Host = None
        self._DBName = None
        self._User = None
        self._SentRows = None
        self._AffectRows = None
        self._ExecTime = None

    @property
    def Host(self):
        """客户端地址。
        :rtype: list of str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DBName(self):
        """数据库名称。
        :rtype: list of str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def User(self):
        """用户名。
        :rtype: list of str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def SentRows(self):
        """返回行数。表示筛选返回行数大于该值的审计日志。
        :rtype: int
        """
        return self._SentRows

    @SentRows.setter
    def SentRows(self, SentRows):
        self._SentRows = SentRows

    @property
    def AffectRows(self):
        """影响行数。表示筛选影响行数大于该值的审计日志。
        :rtype: int
        """
        return self._AffectRows

    @AffectRows.setter
    def AffectRows(self, AffectRows):
        self._AffectRows = AffectRows

    @property
    def ExecTime(self):
        """执行时间。单位为：µs。表示筛选执行时间大于该值的审计日志。
        :rtype: int
        """
        return self._ExecTime

    @ExecTime.setter
    def ExecTime(self, ExecTime):
        self._ExecTime = ExecTime


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._DBName = params.get("DBName")
        self._User = params.get("User")
        self._SentRows = params.get("SentRows")
        self._AffectRows = params.get("AffectRows")
        self._ExecTime = params.get("ExecTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutonomyActionVo(AbstractModel):
    """redis自治事件任务详情

    """

    def __init__(self):
        r"""
        :param _ActionId: 自治任务ID。
        :type ActionId: int
        :param _EventId: 自治事件ID。
        :type EventId: int
        :param _Type: 类型：支持RedisAutoScaleUp
        :type Type: str
        :param _TriggerTime: 自治任务触发时间。
        :type TriggerTime: str
        :param _CreateTime: 自治任务创建时间。
        :type CreateTime: str
        :param _UpdateTime: 自治任务更新时间
        :type UpdateTime: str
        :param _FinishTime: 自治任务完成时间。
        :type FinishTime: str
        :param _ExpireTime: 剩余时间，单位：秒。
        :type ExpireTime: int
        :param _Reason: 触发原因。
        :type Reason: str
        :param _Status: 自治任务状态：支持 RUNNING，FINISHED，TERMINATED，CANCELLED
        :type Status: str
        """
        self._ActionId = None
        self._EventId = None
        self._Type = None
        self._TriggerTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._FinishTime = None
        self._ExpireTime = None
        self._Reason = None
        self._Status = None

    @property
    def ActionId(self):
        """自治任务ID。
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def EventId(self):
        """自治事件ID。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Type(self):
        """类型：支持RedisAutoScaleUp
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TriggerTime(self):
        """自治任务触发时间。
        :rtype: str
        """
        return self._TriggerTime

    @TriggerTime.setter
    def TriggerTime(self, TriggerTime):
        self._TriggerTime = TriggerTime

    @property
    def CreateTime(self):
        """自治任务创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """自治任务更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def FinishTime(self):
        """自治任务完成时间。
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def ExpireTime(self):
        """剩余时间，单位：秒。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Reason(self):
        """触发原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Status(self):
        """自治任务状态：支持 RUNNING，FINISHED，TERMINATED，CANCELLED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ActionId = params.get("ActionId")
        self._EventId = params.get("EventId")
        self._Type = params.get("Type")
        self._TriggerTime = params.get("TriggerTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._FinishTime = params.get("FinishTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Reason = params.get("Reason")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutonomyEventVo(AbstractModel):
    """自治事件详情

    """

    def __init__(self):
        r"""
        :param _EventId: 自治事件ID。
        :type EventId: int
        :param _Type: 自治事件类型：支持RunningAutoRecovery，RedisAutoScale
        :type Type: str
        :param _Status: 自治事件状态：支持 RUNNING，FINISHED，TERMINATED
        :type Status: str
        :param _Reason: 触发原因。	
        :type Reason: str
        :param _TriggerTime: 自治任务触发时间。
        :type TriggerTime: int
        :param _LastTriggerTime: 自治任务最后触发时间。
        :type LastTriggerTime: int
        :param _CreateTime: 自治任务创建时间。
        :type CreateTime: int
        :param _UpdateTime: 自治任务更新时间。
        :type UpdateTime: int
        :param _FinishTime: 自治任务完成时间；非结束状态的时候，该值无意义。
        :type FinishTime: int
        """
        self._EventId = None
        self._Type = None
        self._Status = None
        self._Reason = None
        self._TriggerTime = None
        self._LastTriggerTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._FinishTime = None

    @property
    def EventId(self):
        """自治事件ID。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Type(self):
        """自治事件类型：支持RunningAutoRecovery，RedisAutoScale
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """自治事件状态：支持 RUNNING，FINISHED，TERMINATED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        """触发原因。	
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def TriggerTime(self):
        """自治任务触发时间。
        :rtype: int
        """
        return self._TriggerTime

    @TriggerTime.setter
    def TriggerTime(self, TriggerTime):
        self._TriggerTime = TriggerTime

    @property
    def LastTriggerTime(self):
        """自治任务最后触发时间。
        :rtype: int
        """
        return self._LastTriggerTime

    @LastTriggerTime.setter
    def LastTriggerTime(self, LastTriggerTime):
        self._LastTriggerTime = LastTriggerTime

    @property
    def CreateTime(self):
        """自治任务创建时间。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """自治任务更新时间。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def FinishTime(self):
        """自治任务完成时间；非结束状态的时候，该值无意义。
        :rtype: int
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._TriggerTime = params.get("TriggerTime")
        self._LastTriggerTime = params.get("LastTriggerTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._FinishTime = params.get("FinishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutonomyUserProfileInfo(AbstractModel):
    """自治用户配置详情

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启自治。
        :type Enabled: bool
        :param _Uin: 用户Uin。
        :type Uin: str
        :param _MemoryUpperLimit: 内存上限。
        :type MemoryUpperLimit: int
        :param _ThresholdRule: 指标阈值规则。
        :type ThresholdRule: :class:`tencentcloud.dbbrain.v20210527.models.MetricThreshold`
        :param _EnabledItems: 自治功能类型。
        :type EnabledItems: list of str
        """
        self._Enabled = None
        self._Uin = None
        self._MemoryUpperLimit = None
        self._ThresholdRule = None
        self._EnabledItems = None

    @property
    def Enabled(self):
        """是否开启自治。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Uin(self):
        """用户Uin。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def MemoryUpperLimit(self):
        """内存上限。
        :rtype: int
        """
        return self._MemoryUpperLimit

    @MemoryUpperLimit.setter
    def MemoryUpperLimit(self, MemoryUpperLimit):
        self._MemoryUpperLimit = MemoryUpperLimit

    @property
    def ThresholdRule(self):
        """指标阈值规则。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.MetricThreshold`
        """
        return self._ThresholdRule

    @ThresholdRule.setter
    def ThresholdRule(self, ThresholdRule):
        self._ThresholdRule = ThresholdRule

    @property
    def EnabledItems(self):
        """自治功能类型。
        :rtype: list of str
        """
        return self._EnabledItems

    @EnabledItems.setter
    def EnabledItems(self, EnabledItems):
        self._EnabledItems = EnabledItems


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Uin = params.get("Uin")
        self._MemoryUpperLimit = params.get("MemoryUpperLimit")
        if params.get("ThresholdRule") is not None:
            self._ThresholdRule = MetricThreshold()
            self._ThresholdRule._deserialize(params.get("ThresholdRule"))
        self._EnabledItems = params.get("EnabledItems")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDBAutonomyActionRequest(AbstractModel):
    """CancelDBAutonomyAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActionId: 自治任务ID。
        :type ActionId: int
        :param _InstanceId: 实列ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        """
        self._ActionId = None
        self._InstanceId = None
        self._Product = None

    @property
    def ActionId(self):
        """自治任务ID。
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def InstanceId(self):
        """实列ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._ActionId = params.get("ActionId")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDBAutonomyActionResponse(AbstractModel):
    """CancelDBAutonomyAction返回参数结构体

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


class CancelKillTaskRequest(AbstractModel):
    """CancelKillTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKillTaskResponse(AbstractModel):
    """CancelKillTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: kill会话任务终止成功返回1。
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """kill会话任务终止成功返回1。
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


class CancelRedisBigKeyAnalysisTasksRequest(AbstractModel):
    """CancelRedisBigKeyAnalysisTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestIds: 自治任务ID。
        :type AsyncRequestIds: list of int
        :param _InstanceId: 实列ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        """
        self._AsyncRequestIds = None
        self._InstanceId = None
        self._Product = None

    @property
    def AsyncRequestIds(self):
        """自治任务ID。
        :rtype: list of int
        """
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def InstanceId(self):
        """实列ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelRedisBigKeyAnalysisTasksResponse(AbstractModel):
    """CancelRedisBigKeyAnalysisTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 终止大Key任务结果；0-成功。
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """终止大Key任务结果；0-成功。
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


class CloseAuditServiceRequest(AbstractModel):
    """CloseAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB。
        :type Product: str
        :param _NodeRequestType: 与Product保持一致。如："dcdb" ,"mariadb"。
        :type NodeRequestType: str
        :param _InstanceId: 实例Id。
        :type InstanceId: str
        """
        self._Product = None
        self._NodeRequestType = None
        self._InstanceId = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def NodeRequestType(self):
        """与Product保持一致。如："dcdb" ,"mariadb"。
        :rtype: str
        """
        return self._NodeRequestType

    @NodeRequestType.setter
    def NodeRequestType(self, NodeRequestType):
        self._NodeRequestType = NodeRequestType

    @property
    def InstanceId(self):
        """实例Id。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._NodeRequestType = params.get("NodeRequestType")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseAuditServiceResponse(AbstractModel):
    """CloseAuditService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 0-关闭审计成功，非0关闭审计失败。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """0-关闭审计成功，非0关闭审计失败。
        :rtype: int
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


class CmdCostGroup(AbstractModel):
    """redis延迟分布区间详情

    """

    def __init__(self):
        r"""
        :param _Percent: 该延迟区间内命令数占总命令数百分比
        :type Percent: float
        :param _CostUpperLimit: 延迟区间上界，单位ms
        :type CostUpperLimit: str
        :param _CostLowerLimit: 延迟区间下界，单位ms
        :type CostLowerLimit: str
        :param _Count: 该延迟区间内命令次数
        :type Count: int
        """
        self._Percent = None
        self._CostUpperLimit = None
        self._CostLowerLimit = None
        self._Count = None

    @property
    def Percent(self):
        """该延迟区间内命令数占总命令数百分比
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CostUpperLimit(self):
        """延迟区间上界，单位ms
        :rtype: str
        """
        return self._CostUpperLimit

    @CostUpperLimit.setter
    def CostUpperLimit(self, CostUpperLimit):
        self._CostUpperLimit = CostUpperLimit

    @property
    def CostLowerLimit(self):
        """延迟区间下界，单位ms
        :rtype: str
        """
        return self._CostLowerLimit

    @CostLowerLimit.setter
    def CostLowerLimit(self, CostLowerLimit):
        self._CostLowerLimit = CostLowerLimit

    @property
    def Count(self):
        """该延迟区间内命令次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Percent = params.get("Percent")
        self._CostUpperLimit = params.get("CostUpperLimit")
        self._CostLowerLimit = params.get("CostLowerLimit")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmdPerfInfo(AbstractModel):
    """redis命令延迟趋势

    """

    def __init__(self):
        r"""
        :param _Command: redis命令
        :type Command: str
        :param _SeriesData: 监控数据
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        """
        self._Command = None
        self._SeriesData = None

    @property
    def Command(self):
        """redis命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def SeriesData(self):
        """监控数据
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        """
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._Command = params.get("Command")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContactItem(AbstractModel):
    """联系人contact描述。

    """

    def __init__(self):
        r"""
        :param _Id: 联系人id。
        :type Id: int
        :param _Name: 联系人姓名。
        :type Name: str
        :param _Mail: 联系人绑定的邮箱。
        :type Mail: str
        """
        self._Id = None
        self._Name = None
        self._Mail = None

    @property
    def Id(self):
        """联系人id。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """联系人姓名。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        """联系人绑定的邮箱。
        :rtype: str
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditLogFileRequest(AbstractModel):
    """CreateAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB for MariaDB。
        :type Product: str
        :param _NodeRequestType: 与Product保持一致。如："dcdb" ,"mariadb"
        :type NodeRequestType: str
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。	
        :type StartTime: str
        :param _EndTime: 截止时间，如“2019-09-11 10:13:14”。
        :type EndTime: str
        :param _Filter: 过滤条件。可按设置的过滤条件过滤日志。
        :type Filter: :class:`tencentcloud.dbbrain.v20210527.models.AuditLogFilter`
        """
        self._Product = None
        self._NodeRequestType = None
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Filter = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB for MariaDB。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def NodeRequestType(self):
        """与Product保持一致。如："dcdb" ,"mariadb"
        :rtype: str
        """
        return self._NodeRequestType

    @NodeRequestType.setter
    def NodeRequestType(self, NodeRequestType):
        self._NodeRequestType = NodeRequestType

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2019-09-10 12:13:14”。	
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """截止时间，如“2019-09-11 10:13:14”。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filter(self):
        """过滤条件。可按设置的过滤条件过滤日志。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.AuditLogFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._NodeRequestType = params.get("NodeRequestType")
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filter") is not None:
            self._Filter = AuditLogFilter()
            self._Filter._deserialize(params.get("Filter"))
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
        :param _AsyncRequestId: 审计日志文件下载的任务ID
        :type AsyncRequestId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """审计日志文件下载的任务ID
        :rtype: int
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


class CreateDBDiagReportTaskRequest(AbstractModel):
    """CreateDBDiagReportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2020-11-08T14:00:00+08:00”。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2020-11-09T14:00:00+08:00”。
        :type EndTime: str
        :param _SendMailFlag: 是否发送邮件: 0 - 否，1 - 是。
        :type SendMailFlag: int
        :param _ContactPerson: 接收邮件的联系人ID数组。
        :type ContactPerson: list of int
        :param _ContactGroup: 接收邮件的联系组ID数组。
        :type ContactGroup: list of int
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"redis" - 云数据库 Redis，默认值为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SendMailFlag = None
        self._ContactPerson = None
        self._ContactGroup = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2020-11-08T14:00:00+08:00”。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如“2020-11-09T14:00:00+08:00”。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SendMailFlag(self):
        """是否发送邮件: 0 - 否，1 - 是。
        :rtype: int
        """
        return self._SendMailFlag

    @SendMailFlag.setter
    def SendMailFlag(self, SendMailFlag):
        self._SendMailFlag = SendMailFlag

    @property
    def ContactPerson(self):
        """接收邮件的联系人ID数组。
        :rtype: list of int
        """
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactGroup(self):
        """接收邮件的联系组ID数组。
        :rtype: list of int
        """
        return self._ContactGroup

    @ContactGroup.setter
    def ContactGroup(self, ContactGroup):
        self._ContactGroup = ContactGroup

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"redis" - 云数据库 Redis，默认值为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SendMailFlag = params.get("SendMailFlag")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactGroup = params.get("ContactGroup")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskResponse(AbstractModel):
    """CreateDBDiagReportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :rtype: int
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


class CreateDBDiagReportUrlRequest(AbstractModel):
    """CreateDBDiagReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AsyncRequestId: 健康报告相应的任务ID，可通过DescribeDBDiagReportTasks查询。
        :type AsyncRequestId: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._AsyncRequestId = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        """健康报告相应的任务ID，可通过DescribeDBDiagReportTasks查询。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportUrlResponse(AbstractModel):
    """CreateDBDiagReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportUrl: 健康报告浏览地址。
        :type ReportUrl: str
        :param _ExpireTime: 健康报告浏览地址到期时间戳（秒）。
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportUrl = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def ReportUrl(self):
        """健康报告浏览地址。
        :rtype: str
        """
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def ExpireTime(self):
        """健康报告浏览地址到期时间戳（秒）。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

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
        self._ReportUrl = params.get("ReportUrl")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class CreateKillTaskRequest(AbstractModel):
    """CreateKillTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: kill会话任务的关联实例ID。
        :type InstanceId: str
        :param _Duration: 任务持续时间，单位秒，手动关闭任务传-1。
        :type Duration: int
        :param _Host: 任务过滤条件，客户端IP。
        :type Host: str
        :param _DB: 任务过滤条件，数据库库名,多个","隔开。
        :type DB: str
        :param _Command: 任务过滤条件，相关命令，多个","隔开。
        :type Command: str
        :param _Info: 任务过滤条件，支持单条件前缀匹配。
        :type Info: str
        :param _Infos: 任务过滤条件，支持多个关键字匹配，与Info参数互斥。
        :type Infos: list of str
        :param _User: 任务过滤条件，用户类型。
        :type User: str
        :param _Time: 任务过滤条件，会话持续时长，单位秒。
        :type Time: int
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Duration = None
        self._Host = None
        self._DB = None
        self._Command = None
        self._Info = None
        self._Infos = None
        self._User = None
        self._Time = None
        self._Product = None

    @property
    def InstanceId(self):
        """kill会话任务的关联实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Duration(self):
        """任务持续时间，单位秒，手动关闭任务传-1。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Host(self):
        """任务过滤条件，客户端IP。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DB(self):
        """任务过滤条件，数据库库名,多个","隔开。
        :rtype: str
        """
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def Command(self):
        """任务过滤条件，相关命令，多个","隔开。
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Info(self):
        """任务过滤条件，支持单条件前缀匹配。
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Infos(self):
        """任务过滤条件，支持多个关键字匹配，与Info参数互斥。
        :rtype: list of str
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def User(self):
        """任务过滤条件，用户类型。
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Time(self):
        """任务过滤条件，会话持续时长，单位秒。
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Duration = params.get("Duration")
        self._Host = params.get("Host")
        self._DB = params.get("DB")
        self._Command = params.get("Command")
        self._Info = params.get("Info")
        self._Infos = params.get("Infos")
        self._User = params.get("User")
        self._Time = params.get("Time")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKillTaskResponse(AbstractModel):
    """CreateKillTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: kill会话任务创建成功返回1
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """kill会话任务创建成功返回1
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


class CreateMailProfileRequest(AbstractModel):
    """CreateMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileInfo: 邮件配置内容。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        :param _ProfileLevel: 配置级别，支持值包括："User" - 用户级别，"Instance" - 实例级别，其中数据库巡检邮件配置为用户级别，定期生成邮件配置为实例级别。
        :type ProfileLevel: str
        :param _ProfileName: 配置名称，需要保持唯一性，数据库巡检邮件配置名称自拟；定期生成邮件配置命名格式："scheduler_" + {instanceId}，如"schduler_cdb-test"。
        :type ProfileName: str
        :param _ProfileType: 配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :type ProfileType: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL。
        :type Product: str
        :param _BindInstanceIds: 配置绑定的实例ID，当配置级别为"Instance"时需要传入且只能为一个实例；当配置级别为“User”时，此参数不填。
        :type BindInstanceIds: list of str
        """
        self._ProfileInfo = None
        self._ProfileLevel = None
        self._ProfileName = None
        self._ProfileType = None
        self._Product = None
        self._BindInstanceIds = None

    @property
    def ProfileInfo(self):
        """邮件配置内容。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        """
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

    @property
    def ProfileLevel(self):
        """配置级别，支持值包括："User" - 用户级别，"Instance" - 实例级别，其中数据库巡检邮件配置为用户级别，定期生成邮件配置为实例级别。
        :rtype: str
        """
        return self._ProfileLevel

    @ProfileLevel.setter
    def ProfileLevel(self, ProfileLevel):
        self._ProfileLevel = ProfileLevel

    @property
    def ProfileName(self):
        """配置名称，需要保持唯一性，数据库巡检邮件配置名称自拟；定期生成邮件配置命名格式："scheduler_" + {instanceId}，如"schduler_cdb-test"。
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileType(self):
        """配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def BindInstanceIds(self):
        """配置绑定的实例ID，当配置级别为"Instance"时需要传入且只能为一个实例；当配置级别为“User”时，此参数不填。
        :rtype: list of str
        """
        return self._BindInstanceIds

    @BindInstanceIds.setter
    def BindInstanceIds(self, BindInstanceIds):
        self._BindInstanceIds = BindInstanceIds


    def _deserialize(self, params):
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._ProfileLevel = params.get("ProfileLevel")
        self._ProfileName = params.get("ProfileName")
        self._ProfileType = params.get("ProfileType")
        self._Product = params.get("Product")
        self._BindInstanceIds = params.get("BindInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMailProfileResponse(AbstractModel):
    """CreateMailProfile返回参数结构体

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


class CreateProxySessionKillTaskRequest(AbstractModel):
    """CreateProxySessionKillTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        :param _InstanceProxyId: 实列代理ID。
        :type InstanceProxyId: str
        """
        self._InstanceId = None
        self._Product = None
        self._InstanceProxyId = None

    @property
    def InstanceId(self):
        """实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceProxyId(self):
        """实列代理ID。
        :rtype: str
        """
        return self._InstanceProxyId

    @InstanceProxyId.setter
    def InstanceProxyId(self, InstanceProxyId):
        self._InstanceProxyId = InstanceProxyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        self._InstanceProxyId = params.get("InstanceProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxySessionKillTaskResponse(AbstractModel):
    """CreateProxySessionKillTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 创建 kill 会话任务返回的异步任务 id
        :type AsyncRequestId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """创建 kill 会话任务返回的异步任务 id
        :rtype: int
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


class CreateRedisBigKeyAnalysisTaskRequest(AbstractModel):
    """CreateRedisBigKeyAnalysisTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :type Product: str
        :param _ShardIds: 分片节点序号列表。当列表为空时，选择所有分片节点。
        :type ShardIds: list of int
        :param _KeyDelimiterList: Top Key前缀的分隔符列表。
目前仅支持以下分割符：[",", ";", ":", "_", "-", "+", "@", "=", "|", "#", "."]，当列表为空时，默认选择所有分隔符。
        :type KeyDelimiterList: list of str
        """
        self._InstanceId = None
        self._Product = None
        self._ShardIds = None
        self._KeyDelimiterList = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ShardIds(self):
        """分片节点序号列表。当列表为空时，选择所有分片节点。
        :rtype: list of int
        """
        return self._ShardIds

    @ShardIds.setter
    def ShardIds(self, ShardIds):
        self._ShardIds = ShardIds

    @property
    def KeyDelimiterList(self):
        """Top Key前缀的分隔符列表。
目前仅支持以下分割符：[",", ";", ":", "_", "-", "+", "@", "=", "|", "#", "."]，当列表为空时，默认选择所有分隔符。
        :rtype: list of str
        """
        return self._KeyDelimiterList

    @KeyDelimiterList.setter
    def KeyDelimiterList(self, KeyDelimiterList):
        self._KeyDelimiterList = KeyDelimiterList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        self._ShardIds = params.get("ShardIds")
        self._KeyDelimiterList = params.get("KeyDelimiterList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedisBigKeyAnalysisTaskResponse(AbstractModel):
    """CreateRedisBigKeyAnalysisTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务ID。
        :type AsyncRequestId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """异步任务ID。
        :rtype: int
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


class CreateSchedulerMailProfileRequest(AbstractModel):
    """CreateSchedulerMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WeekConfiguration: 取值范围1-7，分别代表周一至周日。
        :type WeekConfiguration: list of int
        :param _ProfileInfo: 邮件配置内容。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        :param _ProfileName: 配置名称，需要保持唯一性，定期生成邮件配置命名格式："scheduler_" + {instanceId}，如"schduler_cdb-test"。
        :type ProfileName: str
        :param _BindInstanceId: 配置订阅的实例ID。
        :type BindInstanceId: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._WeekConfiguration = None
        self._ProfileInfo = None
        self._ProfileName = None
        self._BindInstanceId = None
        self._Product = None

    @property
    def WeekConfiguration(self):
        """取值范围1-7，分别代表周一至周日。
        :rtype: list of int
        """
        return self._WeekConfiguration

    @WeekConfiguration.setter
    def WeekConfiguration(self, WeekConfiguration):
        self._WeekConfiguration = WeekConfiguration

    @property
    def ProfileInfo(self):
        """邮件配置内容。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        """
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

    @property
    def ProfileName(self):
        """配置名称，需要保持唯一性，定期生成邮件配置命名格式："scheduler_" + {instanceId}，如"schduler_cdb-test"。
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def BindInstanceId(self):
        """配置订阅的实例ID。
        :rtype: str
        """
        return self._BindInstanceId

    @BindInstanceId.setter
    def BindInstanceId(self, BindInstanceId):
        self._BindInstanceId = BindInstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._WeekConfiguration = params.get("WeekConfiguration")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._ProfileName = params.get("ProfileName")
        self._BindInstanceId = params.get("BindInstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulerMailProfileResponse(AbstractModel):
    """CreateSchedulerMailProfile返回参数结构体

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


class CreateSecurityAuditLogExportTaskRequest(AbstractModel):
    """CreateSecurityAuditLogExportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param _StartTime: 导出日志开始时间，例如2020-12-28 00:00:00。
        :type StartTime: str
        :param _EndTime: 导出日志结束时间，例如2020-12-28 01:00:00。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        :param _DangerLevels: 日志风险等级列表，支持值包括：0 无风险；1 低风险；2 中风险；3 高风险。
        :type DangerLevels: list of int
        """
        self._SecAuditGroupId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._DangerLevels = None

    @property
    def SecAuditGroupId(self):
        """安全审计组Id。
        :rtype: str
        """
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def StartTime(self):
        """导出日志开始时间，例如2020-12-28 00:00:00。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """导出日志结束时间，例如2020-12-28 01:00:00。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def DangerLevels(self):
        """日志风险等级列表，支持值包括：0 无风险；1 低风险；2 中风险；3 高风险。
        :rtype: list of int
        """
        return self._DangerLevels

    @DangerLevels.setter
    def DangerLevels(self, DangerLevels):
        self._DangerLevels = DangerLevels


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityAuditLogExportTaskResponse(AbstractModel):
    """CreateSecurityAuditLogExportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 日志导出任务Id。
        :type AsyncRequestId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        """日志导出任务Id。
        :rtype: int
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


class CreateSqlFilterRequest(AbstractModel):
    """CreateSqlFilter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _SqlType: SQL类型，取值包括SELECT, UPDATE, DELETE, INSERT, REPLACE。
        :type SqlType: str
        :param _FilterKey: 关键字，用于筛选SQL语句，多个关键字用英文逗号分隔，逗号不能作为关键词，多个关键词之间的关系为“逻辑与”。
        :type FilterKey: str
        :param _MaxConcurrency: 最大并发度，取值不能小于0，如果该值设为 0，则表示限制所有匹配的SQL执行。
        :type MaxConcurrency: int
        :param _Duration: 限流时长，单位秒，支持-1和小于2147483647的正整数，-1表示永不过期。
        :type Duration: int
        :param _SessionToken: 通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :type SessionToken: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._SqlType = None
        self._FilterKey = None
        self._MaxConcurrency = None
        self._Duration = None
        self._SessionToken = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SqlType(self):
        """SQL类型，取值包括SELECT, UPDATE, DELETE, INSERT, REPLACE。
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def FilterKey(self):
        """关键字，用于筛选SQL语句，多个关键字用英文逗号分隔，逗号不能作为关键词，多个关键词之间的关系为“逻辑与”。
        :rtype: str
        """
        return self._FilterKey

    @FilterKey.setter
    def FilterKey(self, FilterKey):
        self._FilterKey = FilterKey

    @property
    def MaxConcurrency(self):
        """最大并发度，取值不能小于0，如果该值设为 0，则表示限制所有匹配的SQL执行。
        :rtype: int
        """
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def Duration(self):
        """限流时长，单位秒，支持-1和小于2147483647的正整数，-1表示永不过期。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def SessionToken(self):
        """通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SqlType = params.get("SqlType")
        self._FilterKey = params.get("FilterKey")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._Duration = params.get("Duration")
        self._SessionToken = params.get("SessionToken")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSqlFilterResponse(AbstractModel):
    """CreateSqlFilter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FilterId: 限流任务ID。
        :type FilterId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FilterId = None
        self._RequestId = None

    @property
    def FilterId(self):
        """限流任务ID。
        :rtype: int
        """
        return self._FilterId

    @FilterId.setter
    def FilterId(self, FilterId):
        self._FilterId = FilterId

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
        self._FilterId = params.get("FilterId")
        self._RequestId = params.get("RequestId")


class CreateUserAutonomyProfileRequest(AbstractModel):
    """CreateUserAutonomyProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileType: 配置类型，为需要配置的功能枚举值，目前包含一下枚举值：AutonomyGlobal（自治功能全局配置）、RedisAutoScaleUp（Redis自治扩容配置）
        :type ProfileType: str
        :param _InstanceId: 实列ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        :param _ProfileInfo: 自治功能相关配置，标准JSON字符串格式。
        :type ProfileInfo: str
        """
        self._ProfileType = None
        self._InstanceId = None
        self._Product = None
        self._ProfileInfo = None

    @property
    def ProfileType(self):
        """配置类型，为需要配置的功能枚举值，目前包含一下枚举值：AutonomyGlobal（自治功能全局配置）、RedisAutoScaleUp（Redis自治扩容配置）
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def InstanceId(self):
        """实列ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProfileInfo(self):
        """自治功能相关配置，标准JSON字符串格式。
        :rtype: str
        """
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo


    def _deserialize(self, params):
        self._ProfileType = params.get("ProfileType")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        self._ProfileInfo = params.get("ProfileInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserAutonomyProfileResponse(AbstractModel):
    """CreateUserAutonomyProfile返回参数结构体

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


class DeleteAuditLogFileRequest(AbstractModel):
    """DeleteAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB for MariaDB。
        :type Product: str
        :param _NodeRequestType: 与Product保持一致。如："dcdb" ,"mariadb"	
        :type NodeRequestType: str
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _AsyncRequestId: 审计日志文件生成异步任务ID。
        :type AsyncRequestId: int
        """
        self._Product = None
        self._NodeRequestType = None
        self._InstanceId = None
        self._AsyncRequestId = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB for MariaDB。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def NodeRequestType(self):
        """与Product保持一致。如："dcdb" ,"mariadb"	
        :rtype: str
        """
        return self._NodeRequestType

    @NodeRequestType.setter
    def NodeRequestType(self, NodeRequestType):
        self._NodeRequestType = NodeRequestType

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        """审计日志文件生成异步任务ID。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._NodeRequestType = params.get("NodeRequestType")
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
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


class DeleteDBDiagReportTasksRequest(AbstractModel):
    """DeleteDBDiagReportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestIds: 需要删除的任务id列表
        :type AsyncRequestIds: list of int
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._AsyncRequestIds = None
        self._InstanceId = None
        self._Product = None

    @property
    def AsyncRequestIds(self):
        """需要删除的任务id列表
        :rtype: list of int
        """
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBDiagReportTasksResponse(AbstractModel):
    """DeleteDBDiagReportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务删除状态, 0-删除成功
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """任务删除状态, 0-删除成功
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


class DeleteRedisBigKeyAnalysisTasksRequest(AbstractModel):
    """DeleteRedisBigKeyAnalysisTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AsyncRequestIds: 待删除的异步任务ID列表。
        :type AsyncRequestIds: list of int
        :param _Product: 服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :type Product: str
        """
        self._InstanceId = None
        self._AsyncRequestIds = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestIds(self):
        """待删除的异步任务ID列表。
        :rtype: list of int
        """
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Product(self):
        """服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRedisBigKeyAnalysisTasksResponse(AbstractModel):
    """DeleteRedisBigKeyAnalysisTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，为0时代表正常处理。
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，为0时代表正常处理。
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


class DeleteSecurityAuditLogExportTasksRequest(AbstractModel):
    """DeleteSecurityAuditLogExportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param _AsyncRequestIds: 日志导出任务Id列表，接口会忽略不存在或已删除的任务Id。
        :type AsyncRequestIds: list of int non-negative
        :param _Product: 服务产品类型，支持值： "mysql" - 云数据库 MySQL。
        :type Product: str
        """
        self._SecAuditGroupId = None
        self._AsyncRequestIds = None
        self._Product = None

    @property
    def SecAuditGroupId(self):
        """安全审计组Id。
        :rtype: str
        """
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def AsyncRequestIds(self):
        """日志导出任务Id列表，接口会忽略不存在或已删除的任务Id。
        :rtype: list of int non-negative
        """
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Product(self):
        """服务产品类型，支持值： "mysql" - 云数据库 MySQL。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityAuditLogExportTasksResponse(AbstractModel):
    """DeleteSecurityAuditLogExportTasks返回参数结构体

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


class DeleteSqlFiltersRequest(AbstractModel):
    """DeleteSqlFilters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _FilterIds: 限流任务ID列表。
        :type FilterIds: list of int
        :param _SessionToken: 通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :type SessionToken: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._FilterIds = None
        self._SessionToken = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FilterIds(self):
        """限流任务ID列表。
        :rtype: list of int
        """
        return self._FilterIds

    @FilterIds.setter
    def FilterIds(self, FilterIds):
        self._FilterIds = FilterIds

    @property
    def SessionToken(self):
        """通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FilterIds = params.get("FilterIds")
        self._SessionToken = params.get("SessionToken")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSqlFiltersResponse(AbstractModel):
    """DeleteSqlFilters返回参数结构体

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


class DescribeAlarmTemplateRequest(AbstractModel):
    """DescribeAlarmTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateNameRegexp: 搜索字段
        :type TemplateNameRegexp: str
        :param _Limit: 返回限制长度
        :type Limit: int
        :param _Offset: 偏置
        :type Offset: int
        :param _Product: mysql -  mysql
cynosdb -  tdsql-c
        :type Product: str
        """
        self._TemplateNameRegexp = None
        self._Limit = None
        self._Offset = None
        self._Product = None

    @property
    def TemplateNameRegexp(self):
        """搜索字段
        :rtype: str
        """
        return self._TemplateNameRegexp

    @TemplateNameRegexp.setter
    def TemplateNameRegexp(self, TemplateNameRegexp):
        self._TemplateNameRegexp = TemplateNameRegexp

    @property
    def Limit(self):
        """返回限制长度
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Product(self):
        """mysql -  mysql
cynosdb -  tdsql-c
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._TemplateNameRegexp = params.get("TemplateNameRegexp")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmTemplateResponse(AbstractModel):
    """DescribeAlarmTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileList: 模板列表
        :type ProfileList: list of AlarmProfileList
        :param _TotalCount: 模板总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProfileList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProfileList(self):
        """模板列表
        :rtype: list of AlarmProfileList
        """
        return self._ProfileList

    @ProfileList.setter
    def ProfileList(self, ProfileList):
        self._ProfileList = ProfileList

    @property
    def TotalCount(self):
        """模板总数
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
        if params.get("ProfileList") is not None:
            self._ProfileList = []
            for item in params.get("ProfileList"):
                obj = AlarmProfileList()
                obj._deserialize(item)
                self._ProfileList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAllUserContactRequest(AbstractModel):
    """DescribeAllUserContact请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，固定值：mysql。
        :type Product: str
        :param _Names: 联系人名数组，支持模糊搜索。
        :type Names: list of str
        """
        self._Product = None
        self._Names = None

    @property
    def Product(self):
        """服务产品类型，固定值：mysql。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Names(self):
        """联系人名数组，支持模糊搜索。
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserContactResponse(AbstractModel):
    """DescribeAllUserContact返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 联系人的总数量。
        :type TotalCount: int
        :param _Contacts: 联系人的信息。
        :type Contacts: list of ContactItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Contacts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """联系人的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Contacts(self):
        """联系人的信息。
        :rtype: list of ContactItem
        """
        return self._Contacts

    @Contacts.setter
    def Contacts(self, Contacts):
        self._Contacts = Contacts

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
        if params.get("Contacts") is not None:
            self._Contacts = []
            for item in params.get("Contacts"):
                obj = ContactItem()
                obj._deserialize(item)
                self._Contacts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllUserGroupRequest(AbstractModel):
    """DescribeAllUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，固定值：mysql。
        :type Product: str
        :param _Names: 联系组名称数组，支持模糊搜索。
        :type Names: list of str
        """
        self._Product = None
        self._Names = None

    @property
    def Product(self):
        """服务产品类型，固定值：mysql。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Names(self):
        """联系组名称数组，支持模糊搜索。
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserGroupResponse(AbstractModel):
    """DescribeAllUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 组总数。
        :type TotalCount: int
        :param _Groups: 组信息。
        :type Groups: list of GroupItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """组总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        """组信息。
        :rtype: list of GroupItem
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = GroupItem()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditInstanceListRequest(AbstractModel):
    """DescribeAuditInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB。
        :type Product: str
        :param _NodeRequestType: 与Product保持一致。如："dcdb" ,"mariadb"。
        :type NodeRequestType: str
        :param _AuditSwitch: 审计状态标识，0-未开通审计；1-已开通审计，默认为0。
        :type AuditSwitch: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 查询数目，默认为20，最大为100。
        :type Limit: int
        :param _Filters: 查询实例的搜索条件。
        :type Filters: list of AuditInstanceFilter
        """
        self._Product = None
        self._NodeRequestType = None
        self._AuditSwitch = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def NodeRequestType(self):
        """与Product保持一致。如："dcdb" ,"mariadb"。
        :rtype: str
        """
        return self._NodeRequestType

    @NodeRequestType.setter
    def NodeRequestType(self, NodeRequestType):
        self._NodeRequestType = NodeRequestType

    @property
    def AuditSwitch(self):
        """审计状态标识，0-未开通审计；1-已开通审计，默认为0。
        :rtype: int
        """
        return self._AuditSwitch

    @AuditSwitch.setter
    def AuditSwitch(self, AuditSwitch):
        self._AuditSwitch = AuditSwitch

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询数目，默认为20，最大为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """查询实例的搜索条件。
        :rtype: list of AuditInstanceFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._NodeRequestType = params.get("NodeRequestType")
        self._AuditSwitch = params.get("AuditSwitch")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AuditInstanceFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditInstanceListResponse(AbstractModel):
    """DescribeAuditInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例个数。
        :type TotalCount: int
        :param _Items: 实例详情。
        :type Items: list of AuditInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的实例个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """实例详情。
        :rtype: list of AuditInstance
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
                obj = AuditInstance()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditLogFilesRequest(AbstractModel):
    """DescribeAuditLogFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB for MariaDB， "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB for MySQL， "postgres" - 云数据库 PostgreSQL
        :type Product: str
        :param _NodeRequestType: 该字段规则如下： 当product为"dcdb"则输入"dcdb"， 当product为"mariadb"则输入"mariadb"， 当product为"mysql"则输入"mysql"， 当product为"cynosdb"则输入"mysql"， 当product为"postgres"则输入"postgres"。
        :type NodeRequestType: str
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 查询数目，默认为20，最大为100。
        :type Limit: int
        """
        self._Product = None
        self._NodeRequestType = None
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB for MariaDB， "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB for MySQL， "postgres" - 云数据库 PostgreSQL
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def NodeRequestType(self):
        """该字段规则如下： 当product为"dcdb"则输入"dcdb"， 当product为"mariadb"则输入"mariadb"， 当product为"mysql"则输入"mysql"， 当product为"cynosdb"则输入"mysql"， 当product为"postgres"则输入"postgres"。
        :rtype: str
        """
        return self._NodeRequestType

    @NodeRequestType.setter
    def NodeRequestType(self, NodeRequestType):
        self._NodeRequestType = NodeRequestType

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询数目，默认为20，最大为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._NodeRequestType = params.get("NodeRequestType")
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
        


class DescribeAuditLogFilesResponse(AbstractModel):
    """DescribeAuditLogFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的审计日志文件个数。
        :type TotalCount: int
        :param _Items: 审计日志文件详情。
        :type Items: list of AuditLogFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的审计日志文件个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """审计日志文件详情。
        :rtype: list of AuditLogFile
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
                obj = AuditLogFile()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBAutonomyActionsRequest(AbstractModel):
    """DescribeDBAutonomyActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventId: 事件ID。
        :type EventId: int
        :param _InstanceId: 实列ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        """
        self._EventId = None
        self._InstanceId = None
        self._Product = None

    @property
    def EventId(self):
        """事件ID。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def InstanceId(self):
        """实列ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBAutonomyActionsResponse(AbstractModel):
    """DescribeDBAutonomyActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 自治事件总数。
        :type TotalCount: int
        :param _Actions: 自治事件列表。
        :type Actions: list of AutonomyActionVo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Actions = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """自治事件总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Actions(self):
        """自治事件列表。
        :rtype: list of AutonomyActionVo
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

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
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = AutonomyActionVo()
                obj._deserialize(item)
                self._Actions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBAutonomyEventsRequest(AbstractModel):
    """DescribeDBAutonomyEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        :param _InstanceId: 实列ID。
        :type InstanceId: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _Offset: 分页参数，默认值为0。
        :type Offset: int
        :param _Limit: 分页参数，默认值为20。
        :type Limit: int
        """
        self._Product = None
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """实列ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """分页参数，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数，默认值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Product = params.get("Product")
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
        


class DescribeDBAutonomyEventsResponse(AbstractModel):
    """DescribeDBAutonomyEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 自治事件列表总数。
        :type TotalCount: int
        :param _Events: 自治事件列表。
        :type Events: list of AutonomyEventVo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Events = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """自治事件列表总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Events(self):
        """自治事件列表。
        :rtype: list of AutonomyEventVo
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

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
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = AutonomyEventVo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagEventRequest(AbstractModel):
    """DescribeDBDiagEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _EventId: 事件 ID 。通过“获取实例诊断历史DescribeDBDiagHistory”获取。
        :type EventId: int
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._EventId = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventId(self):
        """事件 ID 。通过“获取实例诊断历史DescribeDBDiagHistory”获取。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EventId = params.get("EventId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiagItem: 诊断项。
        :type DiagItem: str
        :param _DiagType: 诊断类型。
        :type DiagType: str
        :param _EventId: 事件 ID 。
        :type EventId: int
        :param _Explanation: 诊断事件详情，若无附加解释信息则输出为空。
        :type Explanation: str
        :param _Outline: 诊断概要。
        :type Outline: str
        :param _Problem: 诊断出的问题。
        :type Problem: str
        :param _Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Suggestions: 诊断建议，若无建议则输出为空。
        :type Suggestions: str
        :param _Metric: 保留字段。
        :type Metric: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiagItem = None
        self._DiagType = None
        self._EventId = None
        self._Explanation = None
        self._Outline = None
        self._Problem = None
        self._Severity = None
        self._StartTime = None
        self._Suggestions = None
        self._Metric = None
        self._EndTime = None
        self._RequestId = None

    @property
    def DiagItem(self):
        """诊断项。
        :rtype: str
        """
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def DiagType(self):
        """诊断类型。
        :rtype: str
        """
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def EventId(self):
        """事件 ID 。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Explanation(self):
        """诊断事件详情，若无附加解释信息则输出为空。
        :rtype: str
        """
        return self._Explanation

    @Explanation.setter
    def Explanation(self, Explanation):
        self._Explanation = Explanation

    @property
    def Outline(self):
        """诊断概要。
        :rtype: str
        """
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Problem(self):
        """诊断出的问题。
        :rtype: str
        """
        return self._Problem

    @Problem.setter
    def Problem(self, Problem):
        self._Problem = Problem

    @property
    def Severity(self):
        """严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :rtype: int
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Suggestions(self):
        """诊断建议，若无建议则输出为空。
        :rtype: str
        """
        return self._Suggestions

    @Suggestions.setter
    def Suggestions(self, Suggestions):
        self._Suggestions = Suggestions

    @property
    def Metric(self):
        """保留字段。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def EndTime(self):
        """结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
        self._DiagItem = params.get("DiagItem")
        self._DiagType = params.get("DiagType")
        self._EventId = params.get("EventId")
        self._Explanation = params.get("Explanation")
        self._Outline = params.get("Outline")
        self._Problem = params.get("Problem")
        self._Severity = params.get("Severity")
        self._StartTime = params.get("StartTime")
        self._Suggestions = params.get("Suggestions")
        self._Metric = params.get("Metric")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeDBDiagEventsRequest(AbstractModel):
    """DescribeDBDiagEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，如“2021-05-27 00:00:00”，支持的最早查询时间为当前时间的前30天。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2021-05-27 01:00:00”，结束时间与开始时间的间隔最大可为7天。
        :type EndTime: str
        :param _Severities: 风险等级列表，取值按影响程度从高至低分别为：1 - 致命、2 -严重、3 - 告警、4 - 提示、5 -健康。
        :type Severities: list of int
        :param _InstanceIds: 实例ID列表。
        :type InstanceIds: list of str
        :param _Product: 服务产品类型，支持值包括："mysql" - 云数据库 MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :type Product: str
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大值为50。
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Severities = None
        self._InstanceIds = None
        self._Product = None
        self._Offset = None
        self._Limit = None

    @property
    def StartTime(self):
        """开始时间，如“2021-05-27 00:00:00”，支持的最早查询时间为当前时间的前30天。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如“2021-05-27 01:00:00”，结束时间与开始时间的间隔最大可为7天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Severities(self):
        """风险等级列表，取值按影响程度从高至低分别为：1 - 致命、2 -严重、3 - 告警、4 - 提示、5 -健康。
        :rtype: list of int
        """
        return self._Severities

    @Severities.setter
    def Severities(self, Severities):
        self._Severities = Severities

    @property
    def InstanceIds(self):
        """实例ID列表。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Product(self):
        """服务产品类型，支持值包括："mysql" - 云数据库 MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        """偏移量，默认0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认20，最大值为50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Severities = params.get("Severities")
        self._InstanceIds = params.get("InstanceIds")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventsResponse(AbstractModel):
    """DescribeDBDiagEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 诊断事件的总数目。
        :type TotalCount: int
        :param _Items: 诊断事件的列表。
        :type Items: list of DiagHistoryEventItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """诊断事件的总数目。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """诊断事件的列表。
        :rtype: list of DiagHistoryEventItem
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
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagHistoryRequest(AbstractModel):
    """DescribeDBDiagHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2019-09-11 12:13:14”，结束时间与开始时间的间隔最大可为2天。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2019-09-10 12:13:14”。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如“2019-09-11 12:13:14”，结束时间与开始时间的间隔最大可为2天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 事件描述。
        :type Events: list of DiagHistoryEventItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._RequestId = None

    @property
    def Events(self):
        """事件描述。
        :rtype: list of DiagHistoryEventItem
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

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
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagReportTasksRequest(AbstractModel):
    """DescribeDBDiagReportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 第一个任务的开始时间，用于范围查询，时间格式如：2019-09-10 12:13:14。
        :type StartTime: str
        :param _EndTime: 最后一个任务的开始时间，用于范围查询，时间格式如：2019-09-10 12:13:14。
        :type EndTime: str
        :param _InstanceIds: 实例ID数组，用于筛选指定实例的任务列表。
        :type InstanceIds: list of str
        :param _Sources: 任务的触发来源，支持的取值包括："DAILY_INSPECTION" - 实例巡检；"SCHEDULED" - 计划任务；"MANUAL" - 手动触发。
        :type Sources: list of str
        :param _HealthLevels: 报告的健康等级，支持的取值包括："HEALTH" - 健康；"SUB_HEALTH" - 亚健康；"RISK" - 危险；"HIGH_RISK" - 高危。
        :type HealthLevels: str
        :param _TaskStatuses: 任务的状态，支持的取值包括："created" - 新建；"chosen" - 待执行； "running" - 执行中；"failed" - 失败；"finished" - 已完成。
        :type TaskStatuses: str
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大值为100。
        :type Limit: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :type Product: str
        """
        self._StartTime = None
        self._EndTime = None
        self._InstanceIds = None
        self._Sources = None
        self._HealthLevels = None
        self._TaskStatuses = None
        self._Offset = None
        self._Limit = None
        self._Product = None

    @property
    def StartTime(self):
        """第一个任务的开始时间，用于范围查询，时间格式如：2019-09-10 12:13:14。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """最后一个任务的开始时间，用于范围查询，时间格式如：2019-09-10 12:13:14。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceIds(self):
        """实例ID数组，用于筛选指定实例的任务列表。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Sources(self):
        """任务的触发来源，支持的取值包括："DAILY_INSPECTION" - 实例巡检；"SCHEDULED" - 计划任务；"MANUAL" - 手动触发。
        :rtype: list of str
        """
        return self._Sources

    @Sources.setter
    def Sources(self, Sources):
        self._Sources = Sources

    @property
    def HealthLevels(self):
        """报告的健康等级，支持的取值包括："HEALTH" - 健康；"SUB_HEALTH" - 亚健康；"RISK" - 危险；"HIGH_RISK" - 高危。
        :rtype: str
        """
        return self._HealthLevels

    @HealthLevels.setter
    def HealthLevels(self, HealthLevels):
        self._HealthLevels = HealthLevels

    @property
    def TaskStatuses(self):
        """任务的状态，支持的取值包括："created" - 新建；"chosen" - 待执行； "running" - 执行中；"failed" - 失败；"finished" - 已完成。
        :rtype: str
        """
        return self._TaskStatuses

    @TaskStatuses.setter
    def TaskStatuses(self, TaskStatuses):
        self._TaskStatuses = TaskStatuses

    @property
    def Offset(self):
        """偏移量，默认0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceIds = params.get("InstanceIds")
        self._Sources = params.get("Sources")
        self._HealthLevels = params.get("HealthLevels")
        self._TaskStatuses = params.get("TaskStatuses")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagReportTasksResponse(AbstractModel):
    """DescribeDBDiagReportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数目。
        :type TotalCount: int
        :param _Tasks: 任务列表。
        :type Tasks: list of HealthReportTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """任务总数目。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        """任务列表。
        :rtype: list of HealthReportTask
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
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = HealthReportTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBPerfTimeSeriesRequest(AbstractModel):
    """DescribeDBPerfTimeSeries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要获取性能趋势的实例ID。
        :type InstanceId: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _Metric: 指标名称，多个指标之间用逗号分隔。
        :type Metric: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，"mongodb" - 云数据库 MongoDB
        :type Product: str
        :param _ClusterId: 需要获取性能趋势的集群ID。
        :type ClusterId: str
        :param _Period: 性能数据统计粒度。
        :type Period: int
        :param _InstanceNodeId: 实列节点ID。
        :type InstanceNodeId: str
        :param _InstanceProxyId: 实列代理ID。
        :type InstanceProxyId: str
        :param _ProxyId: 代理节点ID。
        :type ProxyId: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Product = None
        self._ClusterId = None
        self._Period = None
        self._InstanceNodeId = None
        self._InstanceProxyId = None
        self._ProxyId = None

    @property
    def InstanceId(self):
        """需要获取性能趋势的实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        """指标名称，多个指标之间用逗号分隔。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，"mongodb" - 云数据库 MongoDB
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ClusterId(self):
        """需要获取性能趋势的集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Period(self):
        """性能数据统计粒度。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceNodeId(self):
        """实列节点ID。
        :rtype: str
        """
        return self._InstanceNodeId

    @InstanceNodeId.setter
    def InstanceNodeId(self, InstanceNodeId):
        self._InstanceNodeId = InstanceNodeId

    @property
    def InstanceProxyId(self):
        """实列代理ID。
        :rtype: str
        """
        return self._InstanceProxyId

    @InstanceProxyId.setter
    def InstanceProxyId(self, InstanceProxyId):
        self._InstanceProxyId = InstanceProxyId

    @property
    def ProxyId(self):
        """代理节点ID。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Product = params.get("Product")
        self._ClusterId = params.get("ClusterId")
        self._Period = params.get("Period")
        self._InstanceNodeId = params.get("InstanceNodeId")
        self._InstanceProxyId = params.get("InstanceProxyId")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPerfTimeSeriesResponse(AbstractModel):
    """DescribeDBPerfTimeSeries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 实列性能数据。
        :type Data: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """实列性能数据。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
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
            self._Data = MonitorMetricSeriesData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDBSpaceStatusRequest(AbstractModel):
    """DescribeDBSpaceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _RangeDays: 时间段天数，截止日期为当日，默认为7天。
        :type RangeDays: int
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"mongodb" - 云数据库 MongoDB，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._RangeDays = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RangeDays(self):
        """时间段天数，截止日期为当日，默认为7天。
        :rtype: int
        """
        return self._RangeDays

    @RangeDays.setter
    def RangeDays(self, RangeDays):
        self._RangeDays = RangeDays

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"mongodb" - 云数据库 MongoDB，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RangeDays = params.get("RangeDays")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSpaceStatusResponse(AbstractModel):
    """DescribeDBSpaceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Growth: 磁盘增长量(MB)。
        :type Growth: int
        :param _Remain: 磁盘剩余(MB)。
        :type Remain: int
        :param _Total: 磁盘总量(MB)。
        :type Total: int
        :param _AvailableDays: 预计可用天数。
        :type AvailableDays: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Growth = None
        self._Remain = None
        self._Total = None
        self._AvailableDays = None
        self._RequestId = None

    @property
    def Growth(self):
        """磁盘增长量(MB)。
        :rtype: int
        """
        return self._Growth

    @Growth.setter
    def Growth(self, Growth):
        self._Growth = Growth

    @property
    def Remain(self):
        """磁盘剩余(MB)。
        :rtype: int
        """
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def Total(self):
        """磁盘总量(MB)。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AvailableDays(self):
        """预计可用天数。
        :rtype: int
        """
        return self._AvailableDays

    @AvailableDays.setter
    def AvailableDays(self, AvailableDays):
        self._AvailableDays = AvailableDays

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
        self._Growth = params.get("Growth")
        self._Remain = params.get("Remain")
        self._Total = params.get("Total")
        self._AvailableDays = params.get("AvailableDays")
        self._RequestId = params.get("RequestId")


class DescribeDiagDBInstancesRequest(AbstractModel):
    """DescribeDiagDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSupported: 是否是DBbrain支持的实例，固定传 true。
        :type IsSupported: bool
        :param _Product: 服务产品类型，支持值包括："mysql" - 云数据库 MySQL，"cynosdb" - 云数据库 TDSQL-C for MySQL，"dbbrain-mysql" - 自建 MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :type Product: str
        :param _Offset: 分页参数，偏移量。
        :type Offset: int
        :param _Limit: 分页参数，分页值，最大值为100。
        :type Limit: int
        :param _InstanceNames: 根据实例名称条件查询。
        :type InstanceNames: list of str
        :param _InstanceIds: 根据实例ID条件查询。
        :type InstanceIds: list of str
        :param _Regions: 根据地域条件查询。
        :type Regions: list of str
        """
        self._IsSupported = None
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._InstanceNames = None
        self._InstanceIds = None
        self._Regions = None

    @property
    def IsSupported(self):
        """是否是DBbrain支持的实例，固定传 true。
        :rtype: bool
        """
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def Product(self):
        """服务产品类型，支持值包括："mysql" - 云数据库 MySQL，"cynosdb" - 云数据库 TDSQL-C for MySQL，"dbbrain-mysql" - 自建 MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        """分页参数，偏移量。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数，分页值，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceNames(self):
        """根据实例名称条件查询。
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def InstanceIds(self):
        """根据实例ID条件查询。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Regions(self):
        """根据地域条件查询。
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._IsSupported = params.get("IsSupported")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceNames = params.get("InstanceNames")
        self._InstanceIds = params.get("InstanceIds")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagDBInstancesResponse(AbstractModel):
    """DescribeDiagDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _DbScanStatus: 全实例巡检状态：0：开启全实例巡检；1：未开启全实例巡检。
        :type DbScanStatus: int
        :param _Items: 实例相关信息。
        :type Items: list of InstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DbScanStatus = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """实例总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DbScanStatus(self):
        """全实例巡检状态：0：开启全实例巡检；1：未开启全实例巡检。
        :rtype: int
        """
        return self._DbScanStatus

    @DbScanStatus.setter
    def DbScanStatus(self, DbScanStatus):
        self._DbScanStatus = DbScanStatus

    @property
    def Items(self):
        """实例相关信息。
        :rtype: list of InstanceInfo
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
        self._DbScanStatus = params.get("DbScanStatus")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHealthScoreRequest(AbstractModel):
    """DescribeHealthScore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要获取健康得分的实例ID。
        :type InstanceId: str
        :param _Time: 获取健康得分的时间，时间格式如：2019-09-10 12:13:14。
        :type Time: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Time = None
        self._Product = None

    @property
    def InstanceId(self):
        """需要获取健康得分的实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Time(self):
        """获取健康得分的时间，时间格式如：2019-09-10 12:13:14。
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Time = params.get("Time")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthScoreResponse(AbstractModel):
    """DescribeHealthScore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 健康得分以及异常扣分项。
        :type Data: :class:`tencentcloud.dbbrain.v20210527.models.HealthScoreInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """健康得分以及异常扣分项。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.HealthScoreInfo`
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
            self._Data = HealthScoreInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeIndexRecommendAggregationSlowLogsRequest(AbstractModel):
    """DescribeIndexRecommendAggregationSlowLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括："mongodb" - 云数据库 。
        :type Product: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Db: 数据库名称。
        :type Db: str
        :param _Collection: 表明。
        :type Collection: str
        :param _Signs: 签名。
        :type Signs: list of str
        """
        self._Product = None
        self._InstanceId = None
        self._Db = None
        self._Collection = None
        self._Signs = None

    @property
    def Product(self):
        """服务产品类型，支持值包括："mongodb" - 云数据库 。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Db(self):
        """数据库名称。
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Collection(self):
        """表明。
        :rtype: str
        """
        return self._Collection

    @Collection.setter
    def Collection(self, Collection):
        self._Collection = Collection

    @property
    def Signs(self):
        """签名。
        :rtype: list of str
        """
        return self._Signs

    @Signs.setter
    def Signs(self, Signs):
        self._Signs = Signs


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._Db = params.get("Db")
        self._Collection = params.get("Collection")
        self._Signs = params.get("Signs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexRecommendAggregationSlowLogsResponse(AbstractModel):
    """DescribeIndexRecommendAggregationSlowLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Aggregation: 查询实例慢查询聚合结果。
        :type Aggregation: :class:`tencentcloud.dbbrain.v20210527.models.Aggregation`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Aggregation = None
        self._RequestId = None

    @property
    def Aggregation(self):
        """查询实例慢查询聚合结果。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.Aggregation`
        """
        return self._Aggregation

    @Aggregation.setter
    def Aggregation(self, Aggregation):
        self._Aggregation = Aggregation

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
        if params.get("Aggregation") is not None:
            self._Aggregation = Aggregation()
            self._Aggregation._deserialize(params.get("Aggregation"))
        self._RequestId = params.get("RequestId")


class DescribeIndexRecommendInfoRequest(AbstractModel):
    """DescribeIndexRecommendInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括："mongodb" - 云数据库 。
        :type Product: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        """
        self._Product = None
        self._InstanceId = None

    @property
    def Product(self):
        """服务产品类型，支持值包括："mongodb" - 云数据库 。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexRecommendInfoResponse(AbstractModel):
    """DescribeIndexRecommendInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CollectionNum: 索引推荐的集合数量。
        :type CollectionNum: int
        :param _IndexNum: 索引推荐的索引数量。
        :type IndexNum: int
        :param _Items: 索引项。
        :type Items: list of MongoDBIndex
        :param _Level: 优化级别，1-4，优先级从高到低。
        :type Level: int
        :param _Optimized: 历史优化数。
        :type Optimized: int
        :param _OptimizedCount: 累计优化条数。
        :type OptimizedCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CollectionNum = None
        self._IndexNum = None
        self._Items = None
        self._Level = None
        self._Optimized = None
        self._OptimizedCount = None
        self._RequestId = None

    @property
    def CollectionNum(self):
        """索引推荐的集合数量。
        :rtype: int
        """
        return self._CollectionNum

    @CollectionNum.setter
    def CollectionNum(self, CollectionNum):
        self._CollectionNum = CollectionNum

    @property
    def IndexNum(self):
        """索引推荐的索引数量。
        :rtype: int
        """
        return self._IndexNum

    @IndexNum.setter
    def IndexNum(self, IndexNum):
        self._IndexNum = IndexNum

    @property
    def Items(self):
        """索引项。
        :rtype: list of MongoDBIndex
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Level(self):
        """优化级别，1-4，优先级从高到低。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Optimized(self):
        """历史优化数。
        :rtype: int
        """
        return self._Optimized

    @Optimized.setter
    def Optimized(self, Optimized):
        self._Optimized = Optimized

    @property
    def OptimizedCount(self):
        """累计优化条数。
        :rtype: int
        """
        return self._OptimizedCount

    @OptimizedCount.setter
    def OptimizedCount(self, OptimizedCount):
        self._OptimizedCount = OptimizedCount

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
        self._CollectionNum = params.get("CollectionNum")
        self._IndexNum = params.get("IndexNum")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = MongoDBIndex()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Level = params.get("Level")
        self._Optimized = params.get("Optimized")
        self._OptimizedCount = params.get("OptimizedCount")
        self._RequestId = params.get("RequestId")


class DescribeMailProfileRequest(AbstractModel):
    """DescribeMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileType: 配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :type ProfileType: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _Limit: 分页单位，最大支持50。
        :type Limit: int
        :param _ProfileName: 根据邮件配置名称查询，定期发送的邮件配置名称遵循："scheduler_"+{instanceId}的规则。
        :type ProfileName: str
        """
        self._ProfileType = None
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._ProfileName = None

    @property
    def ProfileType(self):
        """配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        """分页偏移量。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页单位，最大支持50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProfileName(self):
        """根据邮件配置名称查询，定期发送的邮件配置名称遵循："scheduler_"+{instanceId}的规则。
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName


    def _deserialize(self, params):
        self._ProfileType = params.get("ProfileType")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProfileName = params.get("ProfileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMailProfileResponse(AbstractModel):
    """DescribeMailProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileList: 邮件配置详情。
        :type ProfileList: list of UserProfile
        :param _TotalCount: 邮件配置总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProfileList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProfileList(self):
        """邮件配置详情。
        :rtype: list of UserProfile
        """
        return self._ProfileList

    @ProfileList.setter
    def ProfileList(self, ProfileList):
        self._ProfileList = ProfileList

    @property
    def TotalCount(self):
        """邮件配置总数。
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
        if params.get("ProfileList") is not None:
            self._ProfileList = []
            for item in params.get("ProfileList"):
                obj = UserProfile()
                obj._deserialize(item)
                self._ProfileList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMySqlProcessListRequest(AbstractModel):
    """DescribeMySqlProcessList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _ID: 线程的ID，用于筛选线程列表。
        :type ID: int
        :param _User: 线程的操作账号名，用于筛选线程列表。
        :type User: str
        :param _Host: 线程的操作主机地址，用于筛选线程列表。
        :type Host: str
        :param _DB: 线程的操作数据库，用于筛选线程列表。
        :type DB: str
        :param _State: 线程的操作状态，用于筛选线程列表。
        :type State: str
        :param _Command: 线程的执行类型，用于筛选线程列表。
        :type Command: str
        :param _Time: 线程的操作时长最小值，单位秒，用于筛选操作时长大于该值的线程列表。
        :type Time: int
        :param _Info: 线程的操作语句，用于筛选线程列表。
        :type Info: str
        :param _Limit: 返回数量，默认20。
        :type Limit: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        :param _StatDimensions: 会话统计的维度信息,可以多个维度。
        :type StatDimensions: list of StatDimension
        """
        self._InstanceId = None
        self._ID = None
        self._User = None
        self._Host = None
        self._DB = None
        self._State = None
        self._Command = None
        self._Time = None
        self._Info = None
        self._Limit = None
        self._Product = None
        self._StatDimensions = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ID(self):
        """线程的ID，用于筛选线程列表。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def User(self):
        """线程的操作账号名，用于筛选线程列表。
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        """线程的操作主机地址，用于筛选线程列表。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DB(self):
        """线程的操作数据库，用于筛选线程列表。
        :rtype: str
        """
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def State(self):
        """线程的操作状态，用于筛选线程列表。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Command(self):
        """线程的执行类型，用于筛选线程列表。
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Time(self):
        """线程的操作时长最小值，单位秒，用于筛选操作时长大于该值的线程列表。
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Info(self):
        """线程的操作语句，用于筛选线程列表。
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Limit(self):
        """返回数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def StatDimensions(self):
        """会话统计的维度信息,可以多个维度。
        :rtype: list of StatDimension
        """
        return self._StatDimensions

    @StatDimensions.setter
    def StatDimensions(self, StatDimensions):
        self._StatDimensions = StatDimensions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ID = params.get("ID")
        self._User = params.get("User")
        self._Host = params.get("Host")
        self._DB = params.get("DB")
        self._State = params.get("State")
        self._Command = params.get("Command")
        self._Time = params.get("Time")
        self._Info = params.get("Info")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        if params.get("StatDimensions") is not None:
            self._StatDimensions = []
            for item in params.get("StatDimensions"):
                obj = StatDimension()
                obj._deserialize(item)
                self._StatDimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMySqlProcessListResponse(AbstractModel):
    """DescribeMySqlProcessList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProcessList: 实时线程列表。
        :type ProcessList: list of MySqlProcess
        :param _Statistics: sql会话统计信息。
        :type Statistics: list of StatisticInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProcessList = None
        self._Statistics = None
        self._RequestId = None

    @property
    def ProcessList(self):
        """实时线程列表。
        :rtype: list of MySqlProcess
        """
        return self._ProcessList

    @ProcessList.setter
    def ProcessList(self, ProcessList):
        self._ProcessList = ProcessList

    @property
    def Statistics(self):
        """sql会话统计信息。
        :rtype: list of StatisticInfo
        """
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

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
        if params.get("ProcessList") is not None:
            self._ProcessList = []
            for item in params.get("ProcessList"):
                obj = MySqlProcess()
                obj._deserialize(item)
                self._ProcessList.append(obj)
        if params.get("Statistics") is not None:
            self._Statistics = []
            for item in params.get("Statistics"):
                obj = StatisticInfo()
                obj._deserialize(item)
                self._Statistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNoPrimaryKeyTablesRequest(AbstractModel):
    """DescribeNoPrimaryKeyTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Date: 查询日期，如2021-05-27，最早为30天前的日期。
        :type Date: str
        :param _Limit: 查询数目，默认为20，最大为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Date = None
        self._Limit = None
        self._Offset = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        """查询日期，如2021-05-27，最早为30天前的日期。
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Limit(self):
        """查询数目，默认为20，最大为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNoPrimaryKeyTablesResponse(AbstractModel):
    """DescribeNoPrimaryKeyTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NoPrimaryKeyTableCount: 无主键表总数。
        :type NoPrimaryKeyTableCount: int
        :param _NoPrimaryKeyTableCountDiff: 与昨日扫描无主键表的差值，正数为增加，负数为减少，0为无变化。
        :type NoPrimaryKeyTableCountDiff: int
        :param _NoPrimaryKeyTableRecordCount: 记录的无主键表总数（不超过无主键表总数），可用于分页查询。
        :type NoPrimaryKeyTableRecordCount: int
        :param _NoPrimaryKeyTables: 无主键表列表。
        :type NoPrimaryKeyTables: list of Table
        :param _Timestamp: 采集时间戳（秒）。
        :type Timestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NoPrimaryKeyTableCount = None
        self._NoPrimaryKeyTableCountDiff = None
        self._NoPrimaryKeyTableRecordCount = None
        self._NoPrimaryKeyTables = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def NoPrimaryKeyTableCount(self):
        """无主键表总数。
        :rtype: int
        """
        return self._NoPrimaryKeyTableCount

    @NoPrimaryKeyTableCount.setter
    def NoPrimaryKeyTableCount(self, NoPrimaryKeyTableCount):
        self._NoPrimaryKeyTableCount = NoPrimaryKeyTableCount

    @property
    def NoPrimaryKeyTableCountDiff(self):
        """与昨日扫描无主键表的差值，正数为增加，负数为减少，0为无变化。
        :rtype: int
        """
        return self._NoPrimaryKeyTableCountDiff

    @NoPrimaryKeyTableCountDiff.setter
    def NoPrimaryKeyTableCountDiff(self, NoPrimaryKeyTableCountDiff):
        self._NoPrimaryKeyTableCountDiff = NoPrimaryKeyTableCountDiff

    @property
    def NoPrimaryKeyTableRecordCount(self):
        """记录的无主键表总数（不超过无主键表总数），可用于分页查询。
        :rtype: int
        """
        return self._NoPrimaryKeyTableRecordCount

    @NoPrimaryKeyTableRecordCount.setter
    def NoPrimaryKeyTableRecordCount(self, NoPrimaryKeyTableRecordCount):
        self._NoPrimaryKeyTableRecordCount = NoPrimaryKeyTableRecordCount

    @property
    def NoPrimaryKeyTables(self):
        """无主键表列表。
        :rtype: list of Table
        """
        return self._NoPrimaryKeyTables

    @NoPrimaryKeyTables.setter
    def NoPrimaryKeyTables(self, NoPrimaryKeyTables):
        self._NoPrimaryKeyTables = NoPrimaryKeyTables

    @property
    def Timestamp(self):
        """采集时间戳（秒）。
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

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
        self._NoPrimaryKeyTableCount = params.get("NoPrimaryKeyTableCount")
        self._NoPrimaryKeyTableCountDiff = params.get("NoPrimaryKeyTableCountDiff")
        self._NoPrimaryKeyTableRecordCount = params.get("NoPrimaryKeyTableRecordCount")
        if params.get("NoPrimaryKeyTables") is not None:
            self._NoPrimaryKeyTables = []
            for item in params.get("NoPrimaryKeyTables"):
                obj = Table()
                obj._deserialize(item)
                self._NoPrimaryKeyTables.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeProxyProcessStatisticsRequest(AbstractModel):
    """DescribeProxyProcessStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _InstanceProxyId: 该实例下需要查询的某一个 ProxyID 。
        :type InstanceProxyId: str
        :param _Limit: 返回数量。
        :type Limit: int
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _SortBy: 按照某字段排序。支持值包括："AllConn"，"ActiveConn"，"Ip"。
        :type SortBy: str
        :param _OrderDirection: 排序方向。支持值包括："DESC"，"ASC"。
        :type OrderDirection: str
        """
        self._InstanceId = None
        self._InstanceProxyId = None
        self._Limit = None
        self._Product = None
        self._Offset = None
        self._SortBy = None
        self._OrderDirection = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceProxyId(self):
        """该实例下需要查询的某一个 ProxyID 。
        :rtype: str
        """
        return self._InstanceProxyId

    @InstanceProxyId.setter
    def InstanceProxyId(self, InstanceProxyId):
        self._InstanceProxyId = InstanceProxyId

    @property
    def Limit(self):
        """返回数量。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        """偏移量，默认0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SortBy(self):
        """按照某字段排序。支持值包括："AllConn"，"ActiveConn"，"Ip"。
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderDirection(self):
        """排序方向。支持值包括："DESC"，"ASC"。
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceProxyId = params.get("InstanceProxyId")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._SortBy = params.get("SortBy")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyProcessStatisticsResponse(AbstractModel):
    """DescribeProxyProcessStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProcessStatistics: 实时会话统计详情。
        :type ProcessStatistics: :class:`tencentcloud.dbbrain.v20210527.models.ProcessStatistic`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProcessStatistics = None
        self._RequestId = None

    @property
    def ProcessStatistics(self):
        """实时会话统计详情。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ProcessStatistic`
        """
        return self._ProcessStatistics

    @ProcessStatistics.setter
    def ProcessStatistics(self, ProcessStatistics):
        self._ProcessStatistics = ProcessStatistics

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
        if params.get("ProcessStatistics") is not None:
            self._ProcessStatistics = ProcessStatistic()
            self._ProcessStatistics._deserialize(params.get("ProcessStatistics"))
        self._RequestId = params.get("RequestId")


class DescribeProxySessionKillTasksRequest(AbstractModel):
    """DescribeProxySessionKillTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AsyncRequestIds: kill 会话异步任务 ID,  接口 CreateProxySessionKillTask 调用成功后获取。
        :type AsyncRequestIds: list of int
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        """
        self._InstanceId = None
        self._AsyncRequestIds = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestIds(self):
        """kill 会话异步任务 ID,  接口 CreateProxySessionKillTask 调用成功后获取。
        :rtype: list of int
        """
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySessionKillTasksResponse(AbstractModel):
    """DescribeProxySessionKillTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: kill 任务的详情。
        :type Tasks: list of TaskInfo
        :param _TotalCount: 任务总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tasks(self):
        """kill 任务的详情。
        :rtype: list of TaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        """任务总数。
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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRedisBigKeyAnalysisTasksRequest(AbstractModel):
    """DescribeRedisBigKeyAnalysisTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :type Product: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Limit: 查询数目，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._Product = None
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def Product(self):
        """服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """查询数目，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisBigKeyAnalysisTasksResponse(AbstractModel):
    """DescribeRedisBigKeyAnalysisTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数。
        :type TotalCount: int
        :param _Tasks: 任务列表。
        :type Tasks: list of RedisBigKeyTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """任务总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        """任务列表。
        :rtype: list of RedisBigKeyTask
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
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = RedisBigKeyTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRedisCmdPerfTimeSeriesRequest(AbstractModel):
    """DescribeRedisCmdPerfTimeSeries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Product: 服务产品类型，仅仅支持值 "redis" - 云数据库 Redis。
        :type Product: str
        :param _StartTime: 开始时间，如“2025-03-17T00:00:00+00:00”。0天 < 当前服务器时间 - 开始时间 <= 10天。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2025-03-17T01:00:00+00:00”，0天 < 结束时间 - 开始时间 <= 10天。
        :type EndTime: str
        :param _CommandList: 需要分析的redis命令
        :type CommandList: list of str
        :param _Metric: 监控指标，以逗号分隔
        :type Metric: str
        :param _Period: 监控指标时间粒度，单位秒，若不提供则根据开始时间和结束时间取默认值
        :type Period: int
        """
        self._InstanceId = None
        self._Product = None
        self._StartTime = None
        self._EndTime = None
        self._CommandList = None
        self._Metric = None
        self._Period = None

    @property
    def InstanceId(self):
        """实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，仅仅支持值 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def StartTime(self):
        """开始时间，如“2025-03-17T00:00:00+00:00”。0天 < 当前服务器时间 - 开始时间 <= 10天。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如“2025-03-17T01:00:00+00:00”，0天 < 结束时间 - 开始时间 <= 10天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CommandList(self):
        """需要分析的redis命令
        :rtype: list of str
        """
        return self._CommandList

    @CommandList.setter
    def CommandList(self, CommandList):
        self._CommandList = CommandList

    @property
    def Metric(self):
        """监控指标，以逗号分隔
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Period(self):
        """监控指标时间粒度，单位秒，若不提供则根据开始时间和结束时间取默认值
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CommandList = params.get("CommandList")
        self._Metric = params.get("Metric")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisCmdPerfTimeSeriesResponse(AbstractModel):
    """DescribeRedisCmdPerfTimeSeries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CmdPerfList: redis命令延迟趋势
        :type CmdPerfList: list of CmdPerfInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CmdPerfList = None
        self._RequestId = None

    @property
    def CmdPerfList(self):
        """redis命令延迟趋势
        :rtype: list of CmdPerfInfo
        """
        return self._CmdPerfList

    @CmdPerfList.setter
    def CmdPerfList(self, CmdPerfList):
        self._CmdPerfList = CmdPerfList

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
        if params.get("CmdPerfList") is not None:
            self._CmdPerfList = []
            for item in params.get("CmdPerfList"):
                obj = CmdPerfInfo()
                obj._deserialize(item)
                self._CmdPerfList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRedisCommandCostStatisticsRequest(AbstractModel):
    """DescribeRedisCommandCostStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2025-03-17T00:00:00+00:00”。0天 < 当前服务器时间 - 开始时间 <= 10天。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2025-03-17T01:00:00+00:00”，0天 < 结束时间 - 开始时间 <= 10天。
        :type EndTime: str
        :param _Product: 服务产品类型，仅仅支持值 "redis" - 云数据库 Redis。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2025-03-17T00:00:00+00:00”。0天 < 当前服务器时间 - 开始时间 <= 10天。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如“2025-03-17T01:00:00+00:00”，0天 < 结束时间 - 开始时间 <= 10天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """服务产品类型，仅仅支持值 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisCommandCostStatisticsResponse(AbstractModel):
    """DescribeRedisCommandCostStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CmdCostGroups: redis延迟分布区间
        :type CmdCostGroups: list of CmdCostGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CmdCostGroups = None
        self._RequestId = None

    @property
    def CmdCostGroups(self):
        """redis延迟分布区间
        :rtype: list of CmdCostGroup
        """
        return self._CmdCostGroups

    @CmdCostGroups.setter
    def CmdCostGroups(self, CmdCostGroups):
        self._CmdCostGroups = CmdCostGroups

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
        if params.get("CmdCostGroups") is not None:
            self._CmdCostGroups = []
            for item in params.get("CmdCostGroups"):
                obj = CmdCostGroup()
                obj._deserialize(item)
                self._CmdCostGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRedisCommandOverviewRequest(AbstractModel):
    """DescribeRedisCommandOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2025-03-17T00:00:00+00:00”。0天 < 当前服务器时间 - 开始时间 <= 10天。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2025-03-17T01:00:00+00:00”，0天 < 结束时间 - 开始时间 <= 10天。
        :type EndTime: str
        :param _Product: 服务产品类型，仅仅支持值 "redis" - 云数据库 Redis。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2025-03-17T00:00:00+00:00”。0天 < 当前服务器时间 - 开始时间 <= 10天。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如“2025-03-17T01:00:00+00:00”，0天 < 结束时间 - 开始时间 <= 10天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """服务产品类型，仅仅支持值 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisCommandOverviewResponse(AbstractModel):
    """DescribeRedisCommandOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CmdList: redis访问命令统计
        :type CmdList: list of RedisCmdInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CmdList = None
        self._RequestId = None

    @property
    def CmdList(self):
        """redis访问命令统计
        :rtype: list of RedisCmdInfo
        """
        return self._CmdList

    @CmdList.setter
    def CmdList(self, CmdList):
        self._CmdList = CmdList

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
        if params.get("CmdList") is not None:
            self._CmdList = []
            for item in params.get("CmdList"):
                obj = RedisCmdInfo()
                obj._deserialize(item)
                self._CmdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRedisProcessListRequest(AbstractModel):
    """DescribeRedisProcessList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Redis 实例ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :type Product: str
        :param _Limit: 查询的Proxy节点数量上限，默认值为20，最大值为50。
        :type Limit: int
        :param _Offset: Proxy节点的偏移量，默认值为0。
        :type Offset: int
        """
        self._InstanceId = None
        self._Product = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """Redis 实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Limit(self):
        """查询的Proxy节点数量上限，默认值为20，最大值为50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Proxy节点的偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisProcessListResponse(AbstractModel):
    """DescribeRedisProcessList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyCount: 该实例的Proxy节点数量，可用于分页查询。
        :type ProxyCount: int
        :param _Processes: 实时会话详情列表。
        :type Processes: list of Process
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyCount = None
        self._Processes = None
        self._RequestId = None

    @property
    def ProxyCount(self):
        """该实例的Proxy节点数量，可用于分页查询。
        :rtype: int
        """
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def Processes(self):
        """实时会话详情列表。
        :rtype: list of Process
        """
        return self._Processes

    @Processes.setter
    def Processes(self, Processes):
        self._Processes = Processes

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
        self._ProxyCount = params.get("ProxyCount")
        if params.get("Processes") is not None:
            self._Processes = []
            for item in params.get("Processes"):
                obj = Process()
                obj._deserialize(item)
                self._Processes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRedisSlowLogTopSqlsRequest(AbstractModel):
    """DescribeRedisSlowLogTopSqls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值： "redis" - 云数据库 Redis。
        :type Product: str
        :param _InstanceProxyId: Redis Proxy节点ID。
        :type InstanceProxyId: str
        :param _SortBy: 排序键，支持ExecTimes,QueryTime,QueryTimeMax,QueryTimeAvg等排序键，默认为QueryTime。
        :type SortBy: str
        :param _OrderBy: 排序方式，支持ASC（升序）以及DESC（降序），默认为DESC。
        :type OrderBy: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._InstanceProxyId = None
        self._SortBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2019-09-10 12:13:14”。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """服务产品类型，支持值： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceProxyId(self):
        """Redis Proxy节点ID。
        :rtype: str
        """
        return self._InstanceProxyId

    @InstanceProxyId.setter
    def InstanceProxyId(self, InstanceProxyId):
        self._InstanceProxyId = InstanceProxyId

    @property
    def SortBy(self):
        """排序键，支持ExecTimes,QueryTime,QueryTimeMax,QueryTimeAvg等排序键，默认为QueryTime。
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderBy(self):
        """排序方式，支持ASC（升序）以及DESC（降序），默认为DESC。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._InstanceProxyId = params.get("InstanceProxyId")
        self._SortBy = params.get("SortBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisSlowLogTopSqlsResponse(AbstractModel):
    """DescribeRedisSlowLogTopSqls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _Rows: 慢日志 top sql 列表。
        :type Rows: list of SlowLogAgg
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        """慢日志 top sql 列表。
        :rtype: list of SlowLogAgg
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

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
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = SlowLogAgg()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRedisTopBigKeysRequest(AbstractModel):
    """DescribeRedisTopBigKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Date: 查询日期，如2021-05-27，最早可为前30天的日期。
        :type Date: str
        :param _Product: 服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :type Product: str
        :param _SortBy: 排序字段，取值包括Capacity - 内存，ItemCount - 元素数量，默认为Capacity。
        :type SortBy: str
        :param _KeyType: key类型筛选条件，默认为不进行筛选，取值包括string, list, set, hash, sortedset, stream。
        :type KeyType: str
        :param _Limit: 查询数目，默认为20，最大值为100。
        :type Limit: int
        :param _AsyncRequestId: 异步任务ID。当为空时，选择最近任务的ID。
        :type AsyncRequestId: int
        :param _ShardIds: 分片节点序号列表。当列表为空时，选择所有分片节点。
        :type ShardIds: list of int
        """
        self._InstanceId = None
        self._Date = None
        self._Product = None
        self._SortBy = None
        self._KeyType = None
        self._Limit = None
        self._AsyncRequestId = None
        self._ShardIds = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        """查询日期，如2021-05-27，最早可为前30天的日期。
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Product(self):
        """服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SortBy(self):
        """排序字段，取值包括Capacity - 内存，ItemCount - 元素数量，默认为Capacity。
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def KeyType(self):
        """key类型筛选条件，默认为不进行筛选，取值包括string, list, set, hash, sortedset, stream。
        :rtype: str
        """
        return self._KeyType

    @KeyType.setter
    def KeyType(self, KeyType):
        self._KeyType = KeyType

    @property
    def Limit(self):
        """查询数目，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AsyncRequestId(self):
        """异步任务ID。当为空时，选择最近任务的ID。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def ShardIds(self):
        """分片节点序号列表。当列表为空时，选择所有分片节点。
        :rtype: list of int
        """
        return self._ShardIds

    @ShardIds.setter
    def ShardIds(self, ShardIds):
        self._ShardIds = ShardIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        self._Product = params.get("Product")
        self._SortBy = params.get("SortBy")
        self._KeyType = params.get("KeyType")
        self._Limit = params.get("Limit")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._ShardIds = params.get("ShardIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisTopBigKeysResponse(AbstractModel):
    """DescribeRedisTopBigKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopKeys: top key列表。
        :type TopKeys: list of RedisKeySpaceData
        :param _Timestamp: 采集时间戳（秒）。
        :type Timestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopKeys = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopKeys(self):
        """top key列表。
        :rtype: list of RedisKeySpaceData
        """
        return self._TopKeys

    @TopKeys.setter
    def TopKeys(self, TopKeys):
        self._TopKeys = TopKeys

    @property
    def Timestamp(self):
        """采集时间戳（秒）。
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

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
        if params.get("TopKeys") is not None:
            self._TopKeys = []
            for item in params.get("TopKeys"):
                obj = RedisKeySpaceData()
                obj._deserialize(item)
                self._TopKeys.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeRedisTopHotKeysRequest(AbstractModel):
    """DescribeRedisTopHotKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2024-09-22T00:00:00+00:00”。0天 < 当前服务器时间 - 开始时间 <= 10天。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2024-09-22T01:00:00+00:00”，0天 < 结束时间 - 开始时间 <= 10天。
        :type EndTime: str
        :param _Product: 服务产品类型，仅仅支持值 "redis" - 云数据库 Redis。
        :type Product: str
        :param _InstanceNodeIds: Redis 节点数组。
        :type InstanceNodeIds: list of str
        :param _Limit: top 数目，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._InstanceNodeIds = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2024-09-22T00:00:00+00:00”。0天 < 当前服务器时间 - 开始时间 <= 10天。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如“2024-09-22T01:00:00+00:00”，0天 < 结束时间 - 开始时间 <= 10天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """服务产品类型，仅仅支持值 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceNodeIds(self):
        """Redis 节点数组。
        :rtype: list of str
        """
        return self._InstanceNodeIds

    @InstanceNodeIds.setter
    def InstanceNodeIds(self, InstanceNodeIds):
        self._InstanceNodeIds = InstanceNodeIds

    @property
    def Limit(self):
        """top 数目，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._InstanceNodeIds = params.get("InstanceNodeIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisTopHotKeysResponse(AbstractModel):
    """DescribeRedisTopHotKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopHotKeys: 热Key分析结果
        :type TopHotKeys: list of TopHotKeys
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopHotKeys = None
        self._RequestId = None

    @property
    def TopHotKeys(self):
        """热Key分析结果
        :rtype: list of TopHotKeys
        """
        return self._TopHotKeys

    @TopHotKeys.setter
    def TopHotKeys(self, TopHotKeys):
        self._TopHotKeys = TopHotKeys

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
        if params.get("TopHotKeys") is not None:
            self._TopHotKeys = []
            for item in params.get("TopHotKeys"):
                obj = TopHotKeys()
                obj._deserialize(item)
                self._TopHotKeys.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRedisTopKeyPrefixListRequest(AbstractModel):
    """DescribeRedisTopKeyPrefixList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Date: 查询日期，如2021-05-27，最早可为前30天的日期。
        :type Date: str
        :param _Product: 服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :type Product: str
        :param _Limit: 查询数目，默认为20，最大值为500。
        :type Limit: int
        :param _ShardIds: 分片ID数组。
        :type ShardIds: list of int
        """
        self._InstanceId = None
        self._Date = None
        self._Product = None
        self._Limit = None
        self._ShardIds = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        """查询日期，如2021-05-27，最早可为前30天的日期。
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Product(self):
        """服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Limit(self):
        """查询数目，默认为20，最大值为500。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ShardIds(self):
        """分片ID数组。
        :rtype: list of int
        """
        return self._ShardIds

    @ShardIds.setter
    def ShardIds(self, ShardIds):
        self._ShardIds = ShardIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        self._Product = params.get("Product")
        self._Limit = params.get("Limit")
        self._ShardIds = params.get("ShardIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisTopKeyPrefixListResponse(AbstractModel):
    """DescribeRedisTopKeyPrefixList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: top key前缀列表。
        :type Items: list of RedisPreKeySpaceData
        :param _Timestamp: 采集时间戳（秒）。
        :type Timestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def Items(self):
        """top key前缀列表。
        :rtype: list of RedisPreKeySpaceData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Timestamp(self):
        """采集时间戳（秒）。
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RedisPreKeySpaceData()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeSecurityAuditLogDownloadUrlsRequest(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param _AsyncRequestId: 异步任务Id。
        :type AsyncRequestId: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        """
        self._SecAuditGroupId = None
        self._AsyncRequestId = None
        self._Product = None

    @property
    def SecAuditGroupId(self):
        """安全审计组Id。
        :rtype: str
        """
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def AsyncRequestId(self):
        """异步任务Id。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogDownloadUrlsResponse(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: 导出结果的COS链接列表。当结果集很大时，可能会切分为多个url下载。
        :type Urls: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Urls = None
        self._RequestId = None

    @property
    def Urls(self):
        """导出结果的COS链接列表。当结果集很大时，可能会切分为多个url下载。
        :rtype: list of str
        """
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

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
        self._Urls = params.get("Urls")
        self._RequestId = params.get("RequestId")


class DescribeSecurityAuditLogExportTasksRequest(AbstractModel):
    """DescribeSecurityAuditLogExportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        :param _AsyncRequestIds: 日志导出任务Id列表。
        :type AsyncRequestIds: list of int non-negative
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _Limit: 返回数量，默认20，最大值为100。
        :type Limit: int
        """
        self._SecAuditGroupId = None
        self._Product = None
        self._AsyncRequestIds = None
        self._Offset = None
        self._Limit = None

    @property
    def SecAuditGroupId(self):
        """安全审计组Id。
        :rtype: str
        """
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def AsyncRequestIds(self):
        """日志导出任务Id列表。
        :rtype: list of int non-negative
        """
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Offset(self):
        """偏移量，默认0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._Product = params.get("Product")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogExportTasksResponse(AbstractModel):
    """DescribeSecurityAuditLogExportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 安全审计日志导出任务列表。
        :type Tasks: list of SecLogExportTaskInfo
        :param _TotalCount: 安全审计日志导出任务总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tasks(self):
        """安全审计日志导出任务列表。
        :rtype: list of SecLogExportTaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        """安全审计日志导出任务总数。
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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = SecLogExportTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogQueryTimeStatsRequest(AbstractModel):
    """DescribeSlowLogQueryTimeStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :type EndTime: str
        :param _Product: "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，"mongodb" - 云数据库 MongoDB，默认为"mysql"。
        :type Product: str
        :param _InstanceProxyId: Proxy节点ID。
        :type InstanceProxyId: str
        :param _InstanceNodeId: 实列节点ID。
        :type InstanceNodeId: str
        :param _Type: 查询类型，目前支持值：mongod，mongos。
        :type Type: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._InstanceProxyId = None
        self._InstanceNodeId = None
        self._Type = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2019-09-10 12:13:14”。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """"mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，"redis" - 云数据库 Redis，"mongodb" - 云数据库 MongoDB，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceProxyId(self):
        """Proxy节点ID。
        :rtype: str
        """
        return self._InstanceProxyId

    @InstanceProxyId.setter
    def InstanceProxyId(self, InstanceProxyId):
        self._InstanceProxyId = InstanceProxyId

    @property
    def InstanceNodeId(self):
        """实列节点ID。
        :rtype: str
        """
        return self._InstanceNodeId

    @InstanceNodeId.setter
    def InstanceNodeId(self, InstanceNodeId):
        self._InstanceNodeId = InstanceNodeId

    @property
    def Type(self):
        """查询类型，目前支持值：mongod，mongos。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._InstanceProxyId = params.get("InstanceProxyId")
        self._InstanceNodeId = params.get("InstanceNodeId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogQueryTimeStatsResponse(AbstractModel):
    """DescribeSlowLogQueryTimeStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _Items: 慢日志 top sql 列表。
        :type Items: list of SqlCostDistribution
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """慢日志 top sql 列表。
        :rtype: list of SqlCostDistribution
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
                obj = SqlCostDistribution()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2019-09-10 12:13:14”，结束时间与开始时间的间隔最大可为7天。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"redis" - 云数据库 Redis，"mongodb" - 云数据库 MongoDB，默认为"mysql"。
        :type Product: str
        :param _InstanceProxyId: Proxy节点ID。	
        :type InstanceProxyId: str
        :param _InstanceNodeId: 实列节点ID。	
        :type InstanceNodeId: str
        :param _Type: 查询类型，目前支持值：mongod，mongos。
        :type Type: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._InstanceProxyId = None
        self._InstanceNodeId = None
        self._Type = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2019-09-10 12:13:14”。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如“2019-09-10 12:13:14”，结束时间与开始时间的间隔最大可为7天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"redis" - 云数据库 Redis，"mongodb" - 云数据库 MongoDB，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceProxyId(self):
        """Proxy节点ID。	
        :rtype: str
        """
        return self._InstanceProxyId

    @InstanceProxyId.setter
    def InstanceProxyId(self, InstanceProxyId):
        self._InstanceProxyId = InstanceProxyId

    @property
    def InstanceNodeId(self):
        """实列节点ID。	
        :rtype: str
        """
        return self._InstanceNodeId

    @InstanceNodeId.setter
    def InstanceNodeId(self, InstanceNodeId):
        self._InstanceNodeId = InstanceNodeId

    @property
    def Type(self):
        """查询类型，目前支持值：mongod，mongos。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._InstanceProxyId = params.get("InstanceProxyId")
        self._InstanceNodeId = params.get("InstanceNodeId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 柱间单位时间间隔，单位为秒。
        :type Period: int
        :param _TimeSeries: 单位时间间隔内慢日志数量统计。
        :type TimeSeries: list of TimeSlice
        :param _SeriesData: 单位时间间隔内的实例 cpu 利用率监控数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Period = None
        self._TimeSeries = None
        self._SeriesData = None
        self._RequestId = None

    @property
    def Period(self):
        """柱间单位时间间隔，单位为秒。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TimeSeries(self):
        """单位时间间隔内慢日志数量统计。
        :rtype: list of TimeSlice
        """
        return self._TimeSeries

    @TimeSeries.setter
    def TimeSeries(self, TimeSeries):
        self._TimeSeries = TimeSeries

    @property
    def SeriesData(self):
        """单位时间间隔内的实例 cpu 利用率监控数据。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        """
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData

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
        self._Period = params.get("Period")
        if params.get("TimeSeries") is not None:
            self._TimeSeries = []
            for item in params.get("TimeSeries"):
                obj = TimeSlice()
                obj._deserialize(item)
                self._TimeSeries.append(obj)
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        self._RequestId = params.get("RequestId")


class DescribeSlowLogTopSqlsRequest(AbstractModel):
    """DescribeSlowLogTopSqls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :type EndTime: str
        :param _SortBy: 排序键，目前支持 QueryTime,ExecTimes,RowsSent,LockTime以及RowsExamined 等排序键，默认为QueryTime。
        :type SortBy: str
        :param _OrderBy: 排序方式，支持ASC（升序）以及DESC（降序），默认为DESC。
        :type OrderBy: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _SchemaList: 数据库名称数组。
        :type SchemaList: list of SchemaItem
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SortBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._SchemaList = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """开始时间，如“2019-09-10 12:13:14”。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SortBy(self):
        """排序键，目前支持 QueryTime,ExecTimes,RowsSent,LockTime以及RowsExamined 等排序键，默认为QueryTime。
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderBy(self):
        """排序方式，支持ASC（升序）以及DESC（降序），默认为DESC。
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SchemaList(self):
        """数据库名称数组。
        :rtype: list of SchemaItem
        """
        return self._SchemaList

    @SchemaList.setter
    def SchemaList(self, SchemaList):
        self._SchemaList = SchemaList

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SortBy = params.get("SortBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("SchemaList") is not None:
            self._SchemaList = []
            for item in params.get("SchemaList"):
                obj = SchemaItem()
                obj._deserialize(item)
                self._SchemaList.append(obj)
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _Rows: 慢日志 top sql 列表
        :type Rows: list of SlowLogTopSqlItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        """慢日志 top sql 列表
        :rtype: list of SlowLogTopSqlItem
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

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
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = SlowLogTopSqlItem()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogUserHostStatsRequest(AbstractModel):
    """DescribeSlowLogUserHostStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _StartTime: 查询范围的开始时间，时间格式如：2019-09-10 12:13:14。
        :type StartTime: str
        :param _EndTime: 查询范围的结束时间，时间格式如：2019-09-10 12:13:14。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        :param _Md5: SQL模板的MD5值
        :type Md5: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._Md5 = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """查询范围的开始时间，时间格式如：2019-09-10 12:13:14。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询范围的结束时间，时间格式如：2019-09-10 12:13:14。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Md5(self):
        """SQL模板的MD5值
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogUserHostStatsResponse(AbstractModel):
    """DescribeSlowLogUserHostStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 来源地址数目。
        :type TotalCount: int
        :param _Items: 各来源地址的慢日志占比详情列表。
        :type Items: list of SlowLogHost
        :param _UserNameItems: 各来源用户名的慢日志占比详情列表。
        :type UserNameItems: list of SlowLogUser
        :param _UserTotalCount: 来源用户数目。
        :type UserTotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._UserNameItems = None
        self._UserTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """来源地址数目。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """各来源地址的慢日志占比详情列表。
        :rtype: list of SlowLogHost
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def UserNameItems(self):
        """各来源用户名的慢日志占比详情列表。
        :rtype: list of SlowLogUser
        """
        return self._UserNameItems

    @UserNameItems.setter
    def UserNameItems(self, UserNameItems):
        self._UserNameItems = UserNameItems

    @property
    def UserTotalCount(self):
        """来源用户数目。
        :rtype: int
        """
        return self._UserTotalCount

    @UserTotalCount.setter
    def UserTotalCount(self, UserTotalCount):
        self._UserTotalCount = UserTotalCount

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
                obj = SlowLogHost()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("UserNameItems") is not None:
            self._UserNameItems = []
            for item in params.get("UserNameItems"):
                obj = SlowLogUser()
                obj._deserialize(item)
                self._UserNameItems.append(obj)
        self._UserTotalCount = params.get("UserTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB for MySQL，默认为"mysql"。
        :type Product: str
        :param _InstanceId: 实例id。
        :type InstanceId: str
        :param _Md5: sql模板的md5值
        :type Md5: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :type EndTime: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 查询数目，默认为20，最大为100。
        :type Limit: int
        :param _DB: 数据库列表
        :type DB: list of str
        :param _Key: 关键字
        :type Key: list of str
        :param _User: 用户
        :type User: list of str
        :param _Ip: IP
        :type Ip: list of str
        :param _Time: 耗时区间,耗时区间的左右边界分别对应数组的第0个元素和第一个元素
        :type Time: list of int
        """
        self._Product = None
        self._InstanceId = None
        self._Md5 = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._DB = None
        self._Key = None
        self._User = None
        self._Ip = None
        self._Time = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """实例id。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Md5(self):
        """sql模板的md5值
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def StartTime(self):
        """开始时间，如“2019-09-10 12:13:14”。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询数目，默认为20，最大为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DB(self):
        """数据库列表
        :rtype: list of str
        """
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def Key(self):
        """关键字
        :rtype: list of str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def User(self):
        """用户
        :rtype: list of str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Ip(self):
        """IP
        :rtype: list of str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Time(self):
        """耗时区间,耗时区间的左右边界分别对应数组的第0个元素和第一个元素
        :rtype: list of int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._Md5 = params.get("Md5")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DB = params.get("DB")
        self._Key = params.get("Key")
        self._User = params.get("User")
        self._Ip = params.get("Ip")
        self._Time = params.get("Time")
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
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _Rows: 慢日志明细
        :type Rows: list of SlowLogInfoItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        """慢日志明细
        :rtype: list of SlowLogInfoItem
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

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
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = SlowLogInfoItem()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSqlFiltersRequest(AbstractModel):
    """DescribeSqlFilters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _FilterIds: 任务ID列表，用于筛选任务列表。
        :type FilterIds: list of int
        :param _Statuses: 任务状态列表，用于筛选任务列表，取值包括RUNNING - 运行中, FINISHED - 已完成, TERMINATED - 已终止。
        :type Statuses: list of str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._FilterIds = None
        self._Statuses = None
        self._Offset = None
        self._Limit = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FilterIds(self):
        """任务ID列表，用于筛选任务列表。
        :rtype: list of int
        """
        return self._FilterIds

    @FilterIds.setter
    def FilterIds(self, FilterIds):
        self._FilterIds = FilterIds

    @property
    def Statuses(self):
        """任务状态列表，用于筛选任务列表，取值包括RUNNING - 运行中, FINISHED - 已完成, TERMINATED - 已终止。
        :rtype: list of str
        """
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FilterIds = params.get("FilterIds")
        self._Statuses = params.get("Statuses")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSqlFiltersResponse(AbstractModel):
    """DescribeSqlFilters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 限流任务总数目。
        :type TotalCount: int
        :param _Items: 限流任务列表。
        :type Items: list of SQLFilter
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """限流任务总数目。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """限流任务列表。
        :rtype: list of SQLFilter
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
                obj = SQLFilter()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSqlTemplateRequest(AbstractModel):
    """DescribeSqlTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Schema: 数据库名。
        :type Schema: str
        :param _SqlText: SQL语句。
        :type SqlText: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Schema = None
        self._SqlText = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Schema(self):
        """数据库名。
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def SqlText(self):
        """SQL语句。
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Schema = params.get("Schema")
        self._SqlText = params.get("SqlText")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSqlTemplateResponse(AbstractModel):
    """DescribeSqlTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Schema: 数据库名。
        :type Schema: str
        :param _SqlText: SQL语句。
        :type SqlText: str
        :param _SqlType: SQL类型。
        :type SqlType: str
        :param _SqlTemplate: SQL模版内容。
        :type SqlTemplate: str
        :param _SqlId: SQL模版ID。
        :type SqlId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Schema = None
        self._SqlText = None
        self._SqlType = None
        self._SqlTemplate = None
        self._SqlId = None
        self._RequestId = None

    @property
    def Schema(self):
        """数据库名。
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def SqlText(self):
        """SQL语句。
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def SqlType(self):
        """SQL类型。
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def SqlTemplate(self):
        """SQL模版内容。
        :rtype: str
        """
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def SqlId(self):
        """SQL模版ID。
        :rtype: int
        """
        return self._SqlId

    @SqlId.setter
    def SqlId(self, SqlId):
        self._SqlId = SqlId

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
        self._Schema = params.get("Schema")
        self._SqlText = params.get("SqlText")
        self._SqlType = params.get("SqlType")
        self._SqlTemplate = params.get("SqlTemplate")
        self._SqlId = params.get("SqlId")
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceSchemaTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Limit: 返回的Top库数量，最大值为100，默认为20。
        :type Limit: int
        :param _SortBy: 筛选Top库所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param _StartDate: 开始日期，如“2021-01-01”，最早为当日的前第29天，默认为截止日期的前第6天。
        :type StartDate: str
        :param _EndDate: 截止日期，如“2021-01-01”，最早为当日的前第29天，默认为当日。
        :type EndDate: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._StartDate = None
        self._EndDate = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """返回的Top库数量，最大值为100，默认为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """筛选Top库所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def StartDate(self):
        """开始日期，如“2021-01-01”，最早为当日的前第29天，默认为截止日期的前第6天。
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """截止日期，如“2021-01-01”，最早为当日的前第29天，默认为当日。
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemaTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopSpaceSchemaTimeSeries: 返回的Top库空间统计信息的时序数据列表。
        :type TopSpaceSchemaTimeSeries: list of SchemaSpaceTimeSeries
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopSpaceSchemaTimeSeries = None
        self._RequestId = None

    @property
    def TopSpaceSchemaTimeSeries(self):
        """返回的Top库空间统计信息的时序数据列表。
        :rtype: list of SchemaSpaceTimeSeries
        """
        return self._TopSpaceSchemaTimeSeries

    @TopSpaceSchemaTimeSeries.setter
    def TopSpaceSchemaTimeSeries(self, TopSpaceSchemaTimeSeries):
        self._TopSpaceSchemaTimeSeries = TopSpaceSchemaTimeSeries

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
        if params.get("TopSpaceSchemaTimeSeries") is not None:
            self._TopSpaceSchemaTimeSeries = []
            for item in params.get("TopSpaceSchemaTimeSeries"):
                obj = SchemaSpaceTimeSeries()
                obj._deserialize(item)
                self._TopSpaceSchemaTimeSeries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceSchemasRequest(AbstractModel):
    """DescribeTopSpaceSchemas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _Limit: 返回的Top库数量，最大值为100，默认为20。
        :type Limit: int
        :param _SortBy: 筛选Top库所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """返回的Top库数量，最大值为100，默认为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """筛选Top库所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemasResponse(AbstractModel):
    """DescribeTopSpaceSchemas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopSpaceSchemas: 返回的Top库空间统计信息列表。
        :type TopSpaceSchemas: list of SchemaSpaceData
        :param _Timestamp: 采集库空间数据的时间戳（秒）。
        :type Timestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopSpaceSchemas = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopSpaceSchemas(self):
        """返回的Top库空间统计信息列表。
        :rtype: list of SchemaSpaceData
        """
        return self._TopSpaceSchemas

    @TopSpaceSchemas.setter
    def TopSpaceSchemas(self, TopSpaceSchemas):
        self._TopSpaceSchemas = TopSpaceSchemas

    @property
    def Timestamp(self):
        """采集库空间数据的时间戳（秒）。
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

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
        if params.get("TopSpaceSchemas") is not None:
            self._TopSpaceSchemas = []
            for item in params.get("TopSpaceSchemas"):
                obj = SchemaSpaceData()
                obj._deserialize(item)
                self._TopSpaceSchemas.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceTableTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceTableTimeSeries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _Limit: 返回的Top表数量，最大值为100，默认为20。
        :type Limit: int
        :param _SortBy: 筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize，默认为 PhysicalFileSize。
        :type SortBy: str
        :param _StartDate: 开始日期，如“2021-01-01”，最早为当日的前第29天，默认为截止日期的前第6天。
        :type StartDate: str
        :param _EndDate: 截止日期，如“2021-01-01”，最早为当日的前第29天，默认为当日。
        :type EndDate: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._StartDate = None
        self._EndDate = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """返回的Top表数量，最大值为100，默认为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize，默认为 PhysicalFileSize。
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def StartDate(self):
        """开始日期，如“2021-01-01”，最早为当日的前第29天，默认为截止日期的前第6天。
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """截止日期，如“2021-01-01”，最早为当日的前第29天，默认为当日。
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopSpaceTableTimeSeries: 返回的Top表空间统计信息的时序数据列表。
        :type TopSpaceTableTimeSeries: list of TableSpaceTimeSeries
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopSpaceTableTimeSeries = None
        self._RequestId = None

    @property
    def TopSpaceTableTimeSeries(self):
        """返回的Top表空间统计信息的时序数据列表。
        :rtype: list of TableSpaceTimeSeries
        """
        return self._TopSpaceTableTimeSeries

    @TopSpaceTableTimeSeries.setter
    def TopSpaceTableTimeSeries(self, TopSpaceTableTimeSeries):
        self._TopSpaceTableTimeSeries = TopSpaceTableTimeSeries

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
        if params.get("TopSpaceTableTimeSeries") is not None:
            self._TopSpaceTableTimeSeries = []
            for item in params.get("TopSpaceTableTimeSeries"):
                obj = TableSpaceTimeSeries()
                obj._deserialize(item)
                self._TopSpaceTableTimeSeries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceTablesRequest(AbstractModel):
    """DescribeTopSpaceTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _Limit: 返回的Top表数量，最大值为100，默认为20。
        :type Limit: int
        :param _SortBy: 筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """返回的Top表数量，最大值为100，默认为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopSpaceTables: 返回的Top表空间统计信息列表。
        :type TopSpaceTables: list of TableSpaceData
        :param _Timestamp: 采集表空间数据的时间戳（秒）。
        :type Timestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopSpaceTables = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopSpaceTables(self):
        """返回的Top表空间统计信息列表。
        :rtype: list of TableSpaceData
        """
        return self._TopSpaceTables

    @TopSpaceTables.setter
    def TopSpaceTables(self, TopSpaceTables):
        self._TopSpaceTables = TopSpaceTables

    @property
    def Timestamp(self):
        """采集表空间数据的时间戳（秒）。
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

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
        if params.get("TopSpaceTables") is not None:
            self._TopSpaceTables = []
            for item in params.get("TopSpaceTables"):
                obj = TableSpaceData()
                obj._deserialize(item)
                self._TopSpaceTables.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeUserAutonomyProfileRequest(AbstractModel):
    """DescribeUserAutonomyProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileType: 配置类型，为需要配置的功能枚举值，目前包含一下枚举值：AutonomyGlobal（自治功能全局配置）、RedisAutoScaleUp（Redis自治扩容配置）。
        :type ProfileType: str
        :param _InstanceId: 实列ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        """
        self._ProfileType = None
        self._InstanceId = None
        self._Product = None

    @property
    def ProfileType(self):
        """配置类型，为需要配置的功能枚举值，目前包含一下枚举值：AutonomyGlobal（自治功能全局配置）、RedisAutoScaleUp（Redis自治扩容配置）。
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def InstanceId(self):
        """实列ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._ProfileType = params.get("ProfileType")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserAutonomyProfileResponse(AbstractModel):
    """DescribeUserAutonomyProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileType: 配置类型，为需要配置的功能枚举值，目前包含一下枚举值：AutonomyGlobal（自治功能全局配置）、RedisAutoScaleUp（Redis自治扩容配置）。
        :type ProfileType: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _ProfileInfo: 自治用户配置。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.AutonomyUserProfileInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProfileType = None
        self._UpdateTime = None
        self._ProfileInfo = None
        self._RequestId = None

    @property
    def ProfileType(self):
        """配置类型，为需要配置的功能枚举值，目前包含一下枚举值：AutonomyGlobal（自治功能全局配置）、RedisAutoScaleUp（Redis自治扩容配置）。
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def UpdateTime(self):
        """更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ProfileInfo(self):
        """自治用户配置。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.AutonomyUserProfileInfo`
        """
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

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
        self._ProfileType = params.get("ProfileType")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = AutonomyUserProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._RequestId = params.get("RequestId")


class DescribeUserSqlAdviceRequest(AbstractModel):
    """DescribeUserSqlAdvice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _SqlText: SQL语句。
        :type SqlText: str
        :param _Schema: 库名。
        :type Schema: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL；"dbbrain-mysql" - 自建 MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._SqlText = None
        self._Schema = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SqlText(self):
        """SQL语句。
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        """库名。
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL；"dbbrain-mysql" - 自建 MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSqlAdviceResponse(AbstractModel):
    """DescribeUserSqlAdvice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Advices: SQL优化建议，可解析为JSON数组，无需优化时输出为空。
        :type Advices: str
        :param _Comments: SQL优化建议备注，可解析为String数组，无需优化时输出为空。
        :type Comments: str
        :param _SqlText: SQL语句。
        :type SqlText: str
        :param _Schema: 库名。
        :type Schema: str
        :param _Tables: 相关表的DDL信息，可解析为JSON数组。
        :type Tables: str
        :param _SqlPlan: SQL执行计划，可解析为JSON，无需优化时输出为空。
        :type SqlPlan: str
        :param _Cost: SQL优化后的成本节约详情，可解析为JSON，无需优化时输出为空。
        :type Cost: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Advices = None
        self._Comments = None
        self._SqlText = None
        self._Schema = None
        self._Tables = None
        self._SqlPlan = None
        self._Cost = None
        self._RequestId = None

    @property
    def Advices(self):
        """SQL优化建议，可解析为JSON数组，无需优化时输出为空。
        :rtype: str
        """
        return self._Advices

    @Advices.setter
    def Advices(self, Advices):
        self._Advices = Advices

    @property
    def Comments(self):
        """SQL优化建议备注，可解析为String数组，无需优化时输出为空。
        :rtype: str
        """
        return self._Comments

    @Comments.setter
    def Comments(self, Comments):
        self._Comments = Comments

    @property
    def SqlText(self):
        """SQL语句。
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        """库名。
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def Tables(self):
        """相关表的DDL信息，可解析为JSON数组。
        :rtype: str
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def SqlPlan(self):
        """SQL执行计划，可解析为JSON，无需优化时输出为空。
        :rtype: str
        """
        return self._SqlPlan

    @SqlPlan.setter
    def SqlPlan(self, SqlPlan):
        self._SqlPlan = SqlPlan

    @property
    def Cost(self):
        """SQL优化后的成本节约详情，可解析为JSON，无需优化时输出为空。
        :rtype: str
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

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
        self._Advices = params.get("Advices")
        self._Comments = params.get("Comments")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._Tables = params.get("Tables")
        self._SqlPlan = params.get("SqlPlan")
        self._Cost = params.get("Cost")
        self._RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """实例诊断历史事件

    """

    def __init__(self):
        r"""
        :param _DiagType: 诊断类型。
        :type DiagType: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EventId: 事件唯一ID 。
        :type EventId: int
        :param _Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param _Outline: 诊断概要。
        :type Outline: str
        :param _DiagItem: 诊断项说明。
        :type DiagItem: str
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _Metric: 保留字段。
        :type Metric: str
        :param _Region: 地域。
        :type Region: str
        """
        self._DiagType = None
        self._EndTime = None
        self._StartTime = None
        self._EventId = None
        self._Severity = None
        self._Outline = None
        self._DiagItem = None
        self._InstanceId = None
        self._Metric = None
        self._Region = None

    @property
    def DiagType(self):
        """诊断类型。
        :rtype: str
        """
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def EndTime(self):
        """结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        """开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EventId(self):
        """事件唯一ID 。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Severity(self):
        """严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :rtype: int
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def Outline(self):
        """诊断概要。
        :rtype: str
        """
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def DiagItem(self):
        """诊断项说明。
        :rtype: str
        """
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def InstanceId(self):
        """实例 ID 。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Metric(self):
        """保留字段。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Region(self):
        """地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._DiagType = params.get("DiagType")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._EventId = params.get("EventId")
        self._Severity = params.get("Severity")
        self._Outline = params.get("Outline")
        self._DiagItem = params.get("DiagItem")
        self._InstanceId = params.get("InstanceId")
        self._Metric = params.get("Metric")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    """异常事件信息。

    """

    def __init__(self):
        r"""
        :param _EventId: 事件 ID 。
        :type EventId: int
        :param _DiagType: 诊断类型。
        :type DiagType: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _Outline: 概要。
        :type Outline: str
        :param _Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param _ScoreLost: 扣分。
        :type ScoreLost: int
        :param _Metric: 保留字段。
        :type Metric: str
        :param _Count: 告警数目。
        :type Count: int
        """
        self._EventId = None
        self._DiagType = None
        self._StartTime = None
        self._EndTime = None
        self._Outline = None
        self._Severity = None
        self._ScoreLost = None
        self._Metric = None
        self._Count = None

    @property
    def EventId(self):
        """事件 ID 。
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def DiagType(self):
        """诊断类型。
        :rtype: str
        """
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def StartTime(self):
        """开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Outline(self):
        """概要。
        :rtype: str
        """
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Severity(self):
        """严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :rtype: int
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def ScoreLost(self):
        """扣分。
        :rtype: int
        """
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def Metric(self):
        """保留字段。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Count(self):
        """告警数目。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._DiagType = params.get("DiagType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Outline = params.get("Outline")
        self._Severity = params.get("Severity")
        self._ScoreLost = params.get("ScoreLost")
        self._Metric = params.get("Metric")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupItem(AbstractModel):
    """描述组信息。

    """

    def __init__(self):
        r"""
        :param _Id: 组id。
        :type Id: int
        :param _Name: 组名称。
        :type Name: str
        :param _MemberCount: 组成员数量。
        :type MemberCount: int
        """
        self._Id = None
        self._Name = None
        self._MemberCount = None

    @property
    def Id(self):
        """组id。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """组名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberCount(self):
        """组成员数量。
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MemberCount = params.get("MemberCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthReportTask(AbstractModel):
    """健康报告任务详情。

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务请求 ID。
        :type AsyncRequestId: int
        :param _Source: 任务的触发来源，支持的取值包括："DAILY_INSPECTION" - 实例巡检；"SCHEDULED" - 定时生成；"MANUAL" - 手动触发。
        :type Source: str
        :param _Progress: 任务完成进度，单位%。
        :type Progress: int
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _StartTime: 任务开始执行时间。
        :type StartTime: str
        :param _EndTime: 任务完成执行时间。
        :type EndTime: str
        :param _InstanceInfo: 任务所属实例的基础信息。
        :type InstanceInfo: :class:`tencentcloud.dbbrain.v20210527.models.InstanceBasicInfo`
        :param _HealthStatus: 健康报告中的健康信息。
        :type HealthStatus: :class:`tencentcloud.dbbrain.v20210527.models.HealthStatus`
        """
        self._AsyncRequestId = None
        self._Source = None
        self._Progress = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._InstanceInfo = None
        self._HealthStatus = None

    @property
    def AsyncRequestId(self):
        """异步任务请求 ID。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Source(self):
        """任务的触发来源，支持的取值包括："DAILY_INSPECTION" - 实例巡检；"SCHEDULED" - 定时生成；"MANUAL" - 手动触发。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Progress(self):
        """任务完成进度，单位%。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CreateTime(self):
        """任务创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """任务开始执行时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务完成执行时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceInfo(self):
        """任务所属实例的基础信息。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.InstanceBasicInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def HealthStatus(self):
        """健康报告中的健康信息。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.HealthStatus`
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Source = params.get("Source")
        self._Progress = params.get("Progress")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceBasicInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        if params.get("HealthStatus") is not None:
            self._HealthStatus = HealthStatus()
            self._HealthStatus._deserialize(params.get("HealthStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthScoreInfo(AbstractModel):
    """获取健康得分返回的详情。

    """

    def __init__(self):
        r"""
        :param _IssueTypes: 异常详情。
        :type IssueTypes: list of IssueTypeInfo
        :param _EventsTotalCount: 异常事件总数。
        :type EventsTotalCount: int
        :param _HealthScore: 健康得分。
        :type HealthScore: int
        :param _HealthLevel: 健康等级, 如："HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK"。
        :type HealthLevel: str
        """
        self._IssueTypes = None
        self._EventsTotalCount = None
        self._HealthScore = None
        self._HealthLevel = None

    @property
    def IssueTypes(self):
        """异常详情。
        :rtype: list of IssueTypeInfo
        """
        return self._IssueTypes

    @IssueTypes.setter
    def IssueTypes(self, IssueTypes):
        self._IssueTypes = IssueTypes

    @property
    def EventsTotalCount(self):
        """异常事件总数。
        :rtype: int
        """
        return self._EventsTotalCount

    @EventsTotalCount.setter
    def EventsTotalCount(self, EventsTotalCount):
        self._EventsTotalCount = EventsTotalCount

    @property
    def HealthScore(self):
        """健康得分。
        :rtype: int
        """
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def HealthLevel(self):
        """健康等级, 如："HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK"。
        :rtype: str
        """
        return self._HealthLevel

    @HealthLevel.setter
    def HealthLevel(self, HealthLevel):
        self._HealthLevel = HealthLevel


    def _deserialize(self, params):
        if params.get("IssueTypes") is not None:
            self._IssueTypes = []
            for item in params.get("IssueTypes"):
                obj = IssueTypeInfo()
                obj._deserialize(item)
                self._IssueTypes.append(obj)
        self._EventsTotalCount = params.get("EventsTotalCount")
        self._HealthScore = params.get("HealthScore")
        self._HealthLevel = params.get("HealthLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthStatus(AbstractModel):
    """实例健康详情。

    """

    def __init__(self):
        r"""
        :param _HealthScore: 健康分数，满分100。
        :type HealthScore: int
        :param _HealthLevel: 健康等级，取值包括："HEALTH" - 健康；"SUB_HEALTH" - 亚健康；"RISK"- 危险；"HIGH_RISK" - 高危。
        :type HealthLevel: str
        :param _ScoreLost: 总扣分分数。
        :type ScoreLost: int
        :param _ScoreDetails: 扣分详情。
        :type ScoreDetails: list of ScoreDetail
        :param _HealthLevelVersion: 健康等级版本，默认为"V1"
        :type HealthLevelVersion: str
        """
        self._HealthScore = None
        self._HealthLevel = None
        self._ScoreLost = None
        self._ScoreDetails = None
        self._HealthLevelVersion = None

    @property
    def HealthScore(self):
        """健康分数，满分100。
        :rtype: int
        """
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def HealthLevel(self):
        """健康等级，取值包括："HEALTH" - 健康；"SUB_HEALTH" - 亚健康；"RISK"- 危险；"HIGH_RISK" - 高危。
        :rtype: str
        """
        return self._HealthLevel

    @HealthLevel.setter
    def HealthLevel(self, HealthLevel):
        self._HealthLevel = HealthLevel

    @property
    def ScoreLost(self):
        """总扣分分数。
        :rtype: int
        """
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def ScoreDetails(self):
        """扣分详情。
        :rtype: list of ScoreDetail
        """
        return self._ScoreDetails

    @ScoreDetails.setter
    def ScoreDetails(self, ScoreDetails):
        self._ScoreDetails = ScoreDetails

    @property
    def HealthLevelVersion(self):
        """健康等级版本，默认为"V1"
        :rtype: str
        """
        return self._HealthLevelVersion

    @HealthLevelVersion.setter
    def HealthLevelVersion(self, HealthLevelVersion):
        self._HealthLevelVersion = HealthLevelVersion


    def _deserialize(self, params):
        self._HealthScore = params.get("HealthScore")
        self._HealthLevel = params.get("HealthLevel")
        self._ScoreLost = params.get("ScoreLost")
        if params.get("ScoreDetails") is not None:
            self._ScoreDetails = []
            for item in params.get("ScoreDetails"):
                obj = ScoreDetail()
                obj._deserialize(item)
                self._ScoreDetails.append(obj)
        self._HealthLevelVersion = params.get("HealthLevelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexesToBuild(AbstractModel):
    """推荐的索引

    """

    def __init__(self):
        r"""
        :param _Id: 索引id，唯一标识一个索引。
        :type Id: int
        :param _IndexCommand: 创建索引命令。
        :type IndexCommand: str
        :param _IndexStr: 索引字符串。
        :type IndexStr: str
        :param _Level: 优化级别，1-4，优先级从高到低。
        :type Level: int
        :param _Score: 索引得分。
        :type Score: int
        :param _Signs: 签名。
        :type Signs: list of str
        :param _Status: 0-待创建；1-创建中。
        :type Status: int
        """
        self._Id = None
        self._IndexCommand = None
        self._IndexStr = None
        self._Level = None
        self._Score = None
        self._Signs = None
        self._Status = None

    @property
    def Id(self):
        """索引id，唯一标识一个索引。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IndexCommand(self):
        """创建索引命令。
        :rtype: str
        """
        return self._IndexCommand

    @IndexCommand.setter
    def IndexCommand(self, IndexCommand):
        self._IndexCommand = IndexCommand

    @property
    def IndexStr(self):
        """索引字符串。
        :rtype: str
        """
        return self._IndexStr

    @IndexStr.setter
    def IndexStr(self, IndexStr):
        self._IndexStr = IndexStr

    @property
    def Level(self):
        """优化级别，1-4，优先级从高到低。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Score(self):
        """索引得分。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Signs(self):
        """签名。
        :rtype: list of str
        """
        return self._Signs

    @Signs.setter
    def Signs(self, Signs):
        self._Signs = Signs

    @property
    def Status(self):
        """0-待创建；1-创建中。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._IndexCommand = params.get("IndexCommand")
        self._IndexStr = params.get("IndexStr")
        self._Level = params.get("Level")
        self._Score = params.get("Score")
        self._Signs = params.get("Signs")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexesToDrop(AbstractModel):
    """无效索引

    """

    def __init__(self):
        r"""
        :param _IndexStr: 索引字符串。
        :type IndexStr: str
        :param _Score: 索引得分。
        :type Score: int
        :param _Reason: 无效原因。
        :type Reason: str
        :param _IndexCommand: 删除索引命令。
        :type IndexCommand: str
        :param _IndexName: 索引名。
        :type IndexName: str
        """
        self._IndexStr = None
        self._Score = None
        self._Reason = None
        self._IndexCommand = None
        self._IndexName = None

    @property
    def IndexStr(self):
        """索引字符串。
        :rtype: str
        """
        return self._IndexStr

    @IndexStr.setter
    def IndexStr(self, IndexStr):
        self._IndexStr = IndexStr

    @property
    def Score(self):
        """索引得分。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Reason(self):
        """无效原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def IndexCommand(self):
        """删除索引命令。
        :rtype: str
        """
        return self._IndexCommand

    @IndexCommand.setter
    def IndexCommand(self, IndexCommand):
        self._IndexCommand = IndexCommand

    @property
    def IndexName(self):
        """索引名。
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName


    def _deserialize(self, params):
        self._IndexStr = params.get("IndexStr")
        self._Score = params.get("Score")
        self._Reason = params.get("Reason")
        self._IndexCommand = params.get("IndexCommand")
        self._IndexName = params.get("IndexName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceBasicInfo(AbstractModel):
    """实例基础信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Vip: 实例内网IP。
        :type Vip: str
        :param _Vport: 实例内网Port。
        :type Vport: int
        :param _Product: 实例产品。
        :type Product: str
        :param _EngineVersion: 实例引擎版本。
        :type EngineVersion: str
        :param _Cpu: CPU数量，对于Redis为0。
        :type Cpu: int
        :param _DeployMode: 实例部署模式。
        :type DeployMode: str
        :param _InstanceConf: 实例内存配置。
        :type InstanceConf: :class:`tencentcloud.dbbrain.v20210527.models.RedisInstanceConf`
        :param _IsSupported: DBbrain是否支持该实例。
        :type IsSupported: bool
        :param _Memory: 实例内存，单位MB。
        :type Memory: int
        :param _Region: 实例地域。
        :type Region: str
        :param _UniqSubnetId: 实例子网统一ID，对于redis为空字符串。
        :type UniqSubnetId: str
        :param _UniqVpcId: 实例私有网络统一ID，对于redis为空字符串。
        :type UniqVpcId: str
        :param _Volume: 实例磁盘容量，对于Redis为0。
        :type Volume: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Vip = None
        self._Vport = None
        self._Product = None
        self._EngineVersion = None
        self._Cpu = None
        self._DeployMode = None
        self._InstanceConf = None
        self._IsSupported = None
        self._Memory = None
        self._Region = None
        self._UniqSubnetId = None
        self._UniqVpcId = None
        self._Volume = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        """实例内网IP。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """实例内网Port。
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Product(self):
        """实例产品。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def EngineVersion(self):
        """实例引擎版本。
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Cpu(self):
        """CPU数量，对于Redis为0。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DeployMode(self):
        """实例部署模式。
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def InstanceConf(self):
        """实例内存配置。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.RedisInstanceConf`
        """
        return self._InstanceConf

    @InstanceConf.setter
    def InstanceConf(self, InstanceConf):
        self._InstanceConf = InstanceConf

    @property
    def IsSupported(self):
        """DBbrain是否支持该实例。
        :rtype: bool
        """
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def Memory(self):
        """实例内存，单位MB。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Region(self):
        """实例地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def UniqSubnetId(self):
        """实例子网统一ID，对于redis为空字符串。
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def UniqVpcId(self):
        """实例私有网络统一ID，对于redis为空字符串。
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Volume(self):
        """实例磁盘容量，对于Redis为0。
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Product = params.get("Product")
        self._EngineVersion = params.get("EngineVersion")
        self._Cpu = params.get("Cpu")
        self._DeployMode = params.get("DeployMode")
        if params.get("InstanceConf") is not None:
            self._InstanceConf = RedisInstanceConf()
            self._InstanceConf._deserialize(params.get("InstanceConf"))
        self._IsSupported = params.get("IsSupported")
        self._Memory = params.get("Memory")
        self._Region = params.get("Region")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfs(AbstractModel):
    """实例配置。

    """

    def __init__(self):
        r"""
        :param _DailyInspection: 数据库巡检开关, Yes/No。
        :type DailyInspection: str
        :param _OverviewDisplay: 实例概览开关，Yes/No。
        :type OverviewDisplay: str
        :param _KeyDelimiters: redis大key分析的自定义分割符，仅redis使用
        :type KeyDelimiters: list of str
        :param _ShardNum: 分片节点数量。
        :type ShardNum: str
        :param _AnalysisTopKey: 是否开启大key周期性分析，仅redis产品有效。
        :type AnalysisTopKey: str
        """
        self._DailyInspection = None
        self._OverviewDisplay = None
        self._KeyDelimiters = None
        self._ShardNum = None
        self._AnalysisTopKey = None

    @property
    def DailyInspection(self):
        """数据库巡检开关, Yes/No。
        :rtype: str
        """
        return self._DailyInspection

    @DailyInspection.setter
    def DailyInspection(self, DailyInspection):
        self._DailyInspection = DailyInspection

    @property
    def OverviewDisplay(self):
        """实例概览开关，Yes/No。
        :rtype: str
        """
        return self._OverviewDisplay

    @OverviewDisplay.setter
    def OverviewDisplay(self, OverviewDisplay):
        self._OverviewDisplay = OverviewDisplay

    @property
    def KeyDelimiters(self):
        """redis大key分析的自定义分割符，仅redis使用
        :rtype: list of str
        """
        return self._KeyDelimiters

    @KeyDelimiters.setter
    def KeyDelimiters(self, KeyDelimiters):
        self._KeyDelimiters = KeyDelimiters

    @property
    def ShardNum(self):
        """分片节点数量。
        :rtype: str
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def AnalysisTopKey(self):
        """是否开启大key周期性分析，仅redis产品有效。
        :rtype: str
        """
        return self._AnalysisTopKey

    @AnalysisTopKey.setter
    def AnalysisTopKey(self, AnalysisTopKey):
        self._AnalysisTopKey = AnalysisTopKey


    def _deserialize(self, params):
        self._DailyInspection = params.get("DailyInspection")
        self._OverviewDisplay = params.get("OverviewDisplay")
        self._KeyDelimiters = params.get("KeyDelimiters")
        self._ShardNum = params.get("ShardNum")
        self._AnalysisTopKey = params.get("AnalysisTopKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceID(AbstractModel):
    """实例id

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
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
        


class InstanceInfo(AbstractModel):
    """查询实例列表，返回实例的相关信息的对象。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Region: 实例所属地域。
        :type Region: str
        :param _HealthScore: 健康得分。
        :type HealthScore: int
        :param _Product: 所属产品。
        :type Product: str
        :param _EventCount: 异常事件数量。
        :type EventCount: int
        :param _InstanceType: 实例类型：1:MASTER；2:DR，3：RO，4:SDR。
        :type InstanceType: int
        :param _Cpu: 核心数。
        :type Cpu: int
        :param _Memory: 内存，单位MB。
        :type Memory: int
        :param _Volume: 硬盘存储，单位GB。
        :type Volume: int
        :param _EngineVersion: 数据库版本。
        :type EngineVersion: str
        :param _Vip: 内网地址。
        :type Vip: str
        :param _Vport: 内网端口。
        :type Vport: int
        :param _Source: 接入来源。
        :type Source: str
        :param _GroupId: 分组ID。
        :type GroupId: str
        :param _GroupName: 分组组名。
        :type GroupName: str
        :param _Status: 实例状态：0：发货中；1：运行正常；4：销毁中；5：隔离中。
        :type Status: int
        :param _UniqSubnetId: 子网统一ID。
        :type UniqSubnetId: str
        :param _DeployMode: cdb类型。
        :type DeployMode: str
        :param _InitFlag: cdb实例初始化标志：0：未初始化；1：已初始化。
        :type InitFlag: int
        :param _TaskStatus: 任务状态。
        :type TaskStatus: int
        :param _UniqVpcId: 私有网络统一ID。
        :type UniqVpcId: str
        :param _InstanceConf: 实例巡检/概览的状态。
        :type InstanceConf: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        :param _DeadlineTime: 资源到期时间。
        :type DeadlineTime: str
        :param _IsSupported: 是否是DBbrain支持的实例。
        :type IsSupported: bool
        :param _SecAuditStatus: 实例安全审计日志开启状态：ON： 安全审计开启；OFF： 未开启安全审计。
        :type SecAuditStatus: str
        :param _AuditPolicyStatus: 实例审计日志开启状态，ALL_AUDIT： 开启全审计；RULE_AUDIT： 开启规则审计；UNBOUND： 未开启审计。
        :type AuditPolicyStatus: str
        :param _AuditRunningStatus: 实例审计日志运行状态：normal： 运行中； paused： 欠费暂停。
        :type AuditRunningStatus: str
        :param _InternalVip: 内网vip。
        :type InternalVip: str
        :param _InternalVport: 内网port。
        :type InternalVport: int
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _ClusterId: 所属集群ID（仅对集群数据库产品该字段非空，如TDSQL-C）。
        :type ClusterId: str
        :param _ClusterName: 所属集群名称（仅对集群数据库产品该字段非空，如TDSQL-C）。
        :type ClusterName: str
        :param _AgentStatus: 自建MySQL的Agent状态，"not_deployed" - 未部署，"deploying" - 部署中，"connected" - 连接正常，"deploy_failed" - 连接失败，"monitoring" - 连接正常，"stopped" - 暂停连接，"connect_failed" - 连接失败，unknown - 未知。
        :type AgentStatus: str
        :param _InstanceStatus: 自建MySQL的实例状态，"not_attached" - 未连接，"attached" - 连接正常，"failed" - 连接失败，"stopped" - 停止监控，unknown- 未知。
        :type InstanceStatus: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._HealthScore = None
        self._Product = None
        self._EventCount = None
        self._InstanceType = None
        self._Cpu = None
        self._Memory = None
        self._Volume = None
        self._EngineVersion = None
        self._Vip = None
        self._Vport = None
        self._Source = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None
        self._UniqSubnetId = None
        self._DeployMode = None
        self._InitFlag = None
        self._TaskStatus = None
        self._UniqVpcId = None
        self._InstanceConf = None
        self._DeadlineTime = None
        self._IsSupported = None
        self._SecAuditStatus = None
        self._AuditPolicyStatus = None
        self._AuditRunningStatus = None
        self._InternalVip = None
        self._InternalVport = None
        self._CreateTime = None
        self._ClusterId = None
        self._ClusterName = None
        self._AgentStatus = None
        self._InstanceStatus = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        """实例所属地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def HealthScore(self):
        """健康得分。
        :rtype: int
        """
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def Product(self):
        """所属产品。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def EventCount(self):
        """异常事件数量。
        :rtype: int
        """
        return self._EventCount

    @EventCount.setter
    def EventCount(self, EventCount):
        self._EventCount = EventCount

    @property
    def InstanceType(self):
        """实例类型：1:MASTER；2:DR，3：RO，4:SDR。
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Cpu(self):
        """核心数。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存，单位MB。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        """硬盘存储，单位GB。
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def EngineVersion(self):
        """数据库版本。
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Vip(self):
        """内网地址。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """内网端口。
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Source(self):
        """接入来源。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def GroupId(self):
        """分组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """分组组名。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        """实例状态：0：发货中；1：运行正常；4：销毁中；5：隔离中。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UniqSubnetId(self):
        """子网统一ID。
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def DeployMode(self):
        """cdb类型。
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def InitFlag(self):
        """cdb实例初始化标志：0：未初始化；1：已初始化。
        :rtype: int
        """
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def TaskStatus(self):
        """任务状态。
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def UniqVpcId(self):
        """私有网络统一ID。
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def InstanceConf(self):
        """实例巡检/概览的状态。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        """
        return self._InstanceConf

    @InstanceConf.setter
    def InstanceConf(self, InstanceConf):
        self._InstanceConf = InstanceConf

    @property
    def DeadlineTime(self):
        """资源到期时间。
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def IsSupported(self):
        """是否是DBbrain支持的实例。
        :rtype: bool
        """
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def SecAuditStatus(self):
        """实例安全审计日志开启状态：ON： 安全审计开启；OFF： 未开启安全审计。
        :rtype: str
        """
        return self._SecAuditStatus

    @SecAuditStatus.setter
    def SecAuditStatus(self, SecAuditStatus):
        self._SecAuditStatus = SecAuditStatus

    @property
    def AuditPolicyStatus(self):
        """实例审计日志开启状态，ALL_AUDIT： 开启全审计；RULE_AUDIT： 开启规则审计；UNBOUND： 未开启审计。
        :rtype: str
        """
        return self._AuditPolicyStatus

    @AuditPolicyStatus.setter
    def AuditPolicyStatus(self, AuditPolicyStatus):
        self._AuditPolicyStatus = AuditPolicyStatus

    @property
    def AuditRunningStatus(self):
        """实例审计日志运行状态：normal： 运行中； paused： 欠费暂停。
        :rtype: str
        """
        return self._AuditRunningStatus

    @AuditRunningStatus.setter
    def AuditRunningStatus(self, AuditRunningStatus):
        self._AuditRunningStatus = AuditRunningStatus

    @property
    def InternalVip(self):
        """内网vip。
        :rtype: str
        """
        return self._InternalVip

    @InternalVip.setter
    def InternalVip(self, InternalVip):
        self._InternalVip = InternalVip

    @property
    def InternalVport(self):
        """内网port。
        :rtype: int
        """
        return self._InternalVport

    @InternalVport.setter
    def InternalVport(self, InternalVport):
        self._InternalVport = InternalVport

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
    def ClusterId(self):
        """所属集群ID（仅对集群数据库产品该字段非空，如TDSQL-C）。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """所属集群名称（仅对集群数据库产品该字段非空，如TDSQL-C）。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AgentStatus(self):
        """自建MySQL的Agent状态，"not_deployed" - 未部署，"deploying" - 部署中，"connected" - 连接正常，"deploy_failed" - 连接失败，"monitoring" - 连接正常，"stopped" - 暂停连接，"connect_failed" - 连接失败，unknown - 未知。
        :rtype: str
        """
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def InstanceStatus(self):
        """自建MySQL的实例状态，"not_attached" - 未连接，"attached" - 连接正常，"failed" - 连接失败，"stopped" - 停止监控，unknown- 未知。
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._HealthScore = params.get("HealthScore")
        self._Product = params.get("Product")
        self._EventCount = params.get("EventCount")
        self._InstanceType = params.get("InstanceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._EngineVersion = params.get("EngineVersion")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Source = params.get("Source")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._DeployMode = params.get("DeployMode")
        self._InitFlag = params.get("InitFlag")
        self._TaskStatus = params.get("TaskStatus")
        self._UniqVpcId = params.get("UniqVpcId")
        if params.get("InstanceConf") is not None:
            self._InstanceConf = InstanceConfs()
            self._InstanceConf._deserialize(params.get("InstanceConf"))
        self._DeadlineTime = params.get("DeadlineTime")
        self._IsSupported = params.get("IsSupported")
        self._SecAuditStatus = params.get("SecAuditStatus")
        self._AuditPolicyStatus = params.get("AuditPolicyStatus")
        self._AuditRunningStatus = params.get("AuditRunningStatus")
        self._InternalVip = params.get("InternalVip")
        self._InternalVport = params.get("InternalVport")
        self._CreateTime = params.get("CreateTime")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._AgentStatus = params.get("AgentStatus")
        self._InstanceStatus = params.get("InstanceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueTypeInfo(AbstractModel):
    """指标信息。

    """

    def __init__(self):
        r"""
        :param _IssueType: 指标分类：AVAILABILITY：可用性，MAINTAINABILITY：可维护性，PERFORMANCE，性能，RELIABILITY可靠性。
        :type IssueType: str
        :param _Events: 异常事件。
        :type Events: list of EventInfo
        :param _TotalCount: 异常事件总数。
        :type TotalCount: int
        """
        self._IssueType = None
        self._Events = None
        self._TotalCount = None

    @property
    def IssueType(self):
        """指标分类：AVAILABILITY：可用性，MAINTAINABILITY：可维护性，PERFORMANCE，性能，RELIABILITY可靠性。
        :rtype: str
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def Events(self):
        """异常事件。
        :rtype: list of EventInfo
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        """异常事件总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._IssueType = params.get("IssueType")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMySqlThreadsRequest(AbstractModel):
    """KillMySqlThreads请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Stage: kill会话任务的阶段，取值包括："Prepare"-准备阶段，"Commit"-提交阶段。
        :type Stage: str
        :param _Threads: 需要kill的sql会话ID列表，此参数用于Prepare阶段。
        :type Threads: list of int
        :param _SqlExecId: 执行ID，此参数用于Commit阶段。
        :type SqlExecId: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        :param _RecordHistory: 默认是true，会记录下kill的记录；该参数为true, 则在kill操作前校验目标会话是否存在，存在则继续kill，否则取消kill。为了加快kill速度，可设置为false。
        :type RecordHistory: bool
        """
        self._InstanceId = None
        self._Stage = None
        self._Threads = None
        self._SqlExecId = None
        self._Product = None
        self._RecordHistory = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Stage(self):
        """kill会话任务的阶段，取值包括："Prepare"-准备阶段，"Commit"-提交阶段。
        :rtype: str
        """
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def Threads(self):
        """需要kill的sql会话ID列表，此参数用于Prepare阶段。
        :rtype: list of int
        """
        return self._Threads

    @Threads.setter
    def Threads(self, Threads):
        self._Threads = Threads

    @property
    def SqlExecId(self):
        """执行ID，此参数用于Commit阶段。
        :rtype: str
        """
        return self._SqlExecId

    @SqlExecId.setter
    def SqlExecId(self, SqlExecId):
        self._SqlExecId = SqlExecId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RecordHistory(self):
        """默认是true，会记录下kill的记录；该参数为true, 则在kill操作前校验目标会话是否存在，存在则继续kill，否则取消kill。为了加快kill速度，可设置为false。
        :rtype: bool
        """
        return self._RecordHistory

    @RecordHistory.setter
    def RecordHistory(self, RecordHistory):
        self._RecordHistory = RecordHistory


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Stage = params.get("Stage")
        self._Threads = params.get("Threads")
        self._SqlExecId = params.get("SqlExecId")
        self._Product = params.get("Product")
        self._RecordHistory = params.get("RecordHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMySqlThreadsResponse(AbstractModel):
    """KillMySqlThreads返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Threads: kill完成的sql会话ID列表。
        :type Threads: list of int
        :param _SqlExecId: 执行ID， Prepare阶段的任务输出，用于Commit阶段中指定执行kill操作的会话ID。
        :type SqlExecId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Threads = None
        self._SqlExecId = None
        self._RequestId = None

    @property
    def Threads(self):
        """kill完成的sql会话ID列表。
        :rtype: list of int
        """
        return self._Threads

    @Threads.setter
    def Threads(self, Threads):
        self._Threads = Threads

    @property
    def SqlExecId(self):
        """执行ID， Prepare阶段的任务输出，用于Commit阶段中指定执行kill操作的会话ID。
        :rtype: str
        """
        return self._SqlExecId

    @SqlExecId.setter
    def SqlExecId(self, SqlExecId):
        self._SqlExecId = SqlExecId

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
        self._Threads = params.get("Threads")
        self._SqlExecId = params.get("SqlExecId")
        self._RequestId = params.get("RequestId")


class MailConfiguration(AbstractModel):
    """邮件发送配置

    """

    def __init__(self):
        r"""
        :param _SendMail: 是否开启邮件发送: 0, 否; 1, 是。
        :type SendMail: int
        :param _Region: 地域配置, 如["ap-guangzhou", "ap-shanghai"]。巡检的邮件发送模板，配置需要发送巡检邮件的地域；订阅的邮件发送模板，配置当前订阅实例的所属地域。
        :type Region: list of str
        :param _HealthStatus: 发送指定的健康等级的报告, 如["HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK"]。
        :type HealthStatus: list of str
        :param _ContactPerson: 联系人id, 联系人/联系组不能都为空。
        :type ContactPerson: list of int
        :param _ContactGroup: 联系组id, 联系人/联系组不能都为空。
        :type ContactGroup: list of int
        """
        self._SendMail = None
        self._Region = None
        self._HealthStatus = None
        self._ContactPerson = None
        self._ContactGroup = None

    @property
    def SendMail(self):
        """是否开启邮件发送: 0, 否; 1, 是。
        :rtype: int
        """
        return self._SendMail

    @SendMail.setter
    def SendMail(self, SendMail):
        self._SendMail = SendMail

    @property
    def Region(self):
        """地域配置, 如["ap-guangzhou", "ap-shanghai"]。巡检的邮件发送模板，配置需要发送巡检邮件的地域；订阅的邮件发送模板，配置当前订阅实例的所属地域。
        :rtype: list of str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def HealthStatus(self):
        """发送指定的健康等级的报告, 如["HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK"]。
        :rtype: list of str
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ContactPerson(self):
        """联系人id, 联系人/联系组不能都为空。
        :rtype: list of int
        """
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactGroup(self):
        """联系组id, 联系人/联系组不能都为空。
        :rtype: list of int
        """
        return self._ContactGroup

    @ContactGroup.setter
    def ContactGroup(self, ContactGroup):
        self._ContactGroup = ContactGroup


    def _deserialize(self, params):
        self._SendMail = params.get("SendMail")
        self._Region = params.get("Region")
        self._HealthStatus = params.get("HealthStatus")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactGroup = params.get("ContactGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricThreshold(AbstractModel):
    """自治指标阈值

    """

    def __init__(self):
        r"""
        :param _Metric: 指标。
        :type Metric: str
        :param _Threshold: 阈值。
        :type Threshold: int
        :param _Duration: 时间间隔。
        :type Duration: int
        """
        self._Metric = None
        self._Threshold = None
        self._Duration = None

    @property
    def Metric(self):
        """指标。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Threshold(self):
        """阈值。
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Duration(self):
        """时间间隔。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Threshold = params.get("Threshold")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyRequest(AbstractModel):
    """ModifyAlarmPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyType: 类型
        :type ApplyType: str
        :param _Enable: 开启策略
        :type Enable: int
        :param _InstanceIds: 列表
        :type InstanceIds: list of InstanceID
        :param _NewProfileLevel: User-动态关联该用户所有实例
Instance-关联实例列表的实例
        :type NewProfileLevel: str
        :param _NewProfileName: 新策略名
        :type NewProfileName: str
        :param _ProfileName: 旧策略名
        :type ProfileName: str
        :param _ProfileType: 策略类型
        :type ProfileType: str
        :param _Remark: 备注
        :type Remark: str
        :param _RuleType: 规则类型 0-快速，1-自定义 若值为0，则QuickRule不能为空，若值为1，则Rules 不能为空
        :type RuleType: int
        :param _TemplateInfo: 接受模板
        :type TemplateInfo: list of TemplateInfo
        :param _QuickRule: 快速规则  支持包括fatal-致命, critical-严重,
warning-告警,
information-通知
        :type QuickRule: str
        :param _Rules: 自定义规则
        :type Rules: list of AlarmsRules
        """
        self._ApplyType = None
        self._Enable = None
        self._InstanceIds = None
        self._NewProfileLevel = None
        self._NewProfileName = None
        self._ProfileName = None
        self._ProfileType = None
        self._Remark = None
        self._RuleType = None
        self._TemplateInfo = None
        self._QuickRule = None
        self._Rules = None

    @property
    def ApplyType(self):
        """类型
        :rtype: str
        """
        return self._ApplyType

    @ApplyType.setter
    def ApplyType(self, ApplyType):
        self._ApplyType = ApplyType

    @property
    def Enable(self):
        """开启策略
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def InstanceIds(self):
        """列表
        :rtype: list of InstanceID
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def NewProfileLevel(self):
        """User-动态关联该用户所有实例
Instance-关联实例列表的实例
        :rtype: str
        """
        return self._NewProfileLevel

    @NewProfileLevel.setter
    def NewProfileLevel(self, NewProfileLevel):
        self._NewProfileLevel = NewProfileLevel

    @property
    def NewProfileName(self):
        """新策略名
        :rtype: str
        """
        return self._NewProfileName

    @NewProfileName.setter
    def NewProfileName(self, NewProfileName):
        self._NewProfileName = NewProfileName

    @property
    def ProfileName(self):
        """旧策略名
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileType(self):
        """策略类型
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RuleType(self):
        """规则类型 0-快速，1-自定义 若值为0，则QuickRule不能为空，若值为1，则Rules 不能为空
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def TemplateInfo(self):
        """接受模板
        :rtype: list of TemplateInfo
        """
        return self._TemplateInfo

    @TemplateInfo.setter
    def TemplateInfo(self, TemplateInfo):
        self._TemplateInfo = TemplateInfo

    @property
    def QuickRule(self):
        """快速规则  支持包括fatal-致命, critical-严重,
warning-告警,
information-通知
        :rtype: str
        """
        return self._QuickRule

    @QuickRule.setter
    def QuickRule(self, QuickRule):
        self._QuickRule = QuickRule

    @property
    def Rules(self):
        """自定义规则
        :rtype: list of AlarmsRules
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._ApplyType = params.get("ApplyType")
        self._Enable = params.get("Enable")
        if params.get("InstanceIds") is not None:
            self._InstanceIds = []
            for item in params.get("InstanceIds"):
                obj = InstanceID()
                obj._deserialize(item)
                self._InstanceIds.append(obj)
        self._NewProfileLevel = params.get("NewProfileLevel")
        self._NewProfileName = params.get("NewProfileName")
        self._ProfileName = params.get("ProfileName")
        self._ProfileType = params.get("ProfileType")
        self._Remark = params.get("Remark")
        self._RuleType = params.get("RuleType")
        if params.get("TemplateInfo") is not None:
            self._TemplateInfo = []
            for item in params.get("TemplateInfo"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self._TemplateInfo.append(obj)
        self._QuickRule = params.get("QuickRule")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = AlarmsRules()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyResponse(AbstractModel):
    """ModifyAlarmPolicy返回参数结构体

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


class ModifyAuditServiceRequest(AbstractModel):
    """ModifyAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB。
        :type Product: str
        :param _NodeRequestType: 与Product保持一致。如："dcdb" ,"mariadb"。
        :type NodeRequestType: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _LogExpireDay: 日志保存总时长，只能是7,30,90,180,365,1095,1825。
        :type LogExpireDay: int
        :param _HotLogExpireDay: 高频日志保存时长，只能是7,30,90,180,365,1095,1825。
        :type HotLogExpireDay: int
        """
        self._Product = None
        self._NodeRequestType = None
        self._InstanceId = None
        self._LogExpireDay = None
        self._HotLogExpireDay = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def NodeRequestType(self):
        """与Product保持一致。如："dcdb" ,"mariadb"。
        :rtype: str
        """
        return self._NodeRequestType

    @NodeRequestType.setter
    def NodeRequestType(self, NodeRequestType):
        self._NodeRequestType = NodeRequestType

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        """日志保存总时长，只能是7,30,90,180,365,1095,1825。
        :rtype: int
        """
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HotLogExpireDay(self):
        """高频日志保存时长，只能是7,30,90,180,365,1095,1825。
        :rtype: int
        """
        return self._HotLogExpireDay

    @HotLogExpireDay.setter
    def HotLogExpireDay(self, HotLogExpireDay):
        self._HotLogExpireDay = HotLogExpireDay


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._NodeRequestType = params.get("NodeRequestType")
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HotLogExpireDay = params.get("HotLogExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditServiceResponse(AbstractModel):
    """ModifyAuditService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 审计配置修改结果，0-修改成功,非0-修改失败。
        :type Success: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        """审计配置修改结果，0-修改成功,非0-修改失败。
        :rtype: int
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

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
        self._Success = params.get("Success")
        self._RequestId = params.get("RequestId")


class ModifyDiagDBInstanceConfRequest(AbstractModel):
    """ModifyDiagDBInstanceConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceConfs: 实例配置，包括巡检、概览开关等。
        :type InstanceConfs: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        :param _Regions: 生效实例地域，取值为"All"，代表全地域。
        :type Regions: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"redis" - 云数据库 Redis。
        :type Product: str
        :param _InstanceIds: 指定更改巡检状态的实例ID。
        :type InstanceIds: list of str
        """
        self._InstanceConfs = None
        self._Regions = None
        self._Product = None
        self._InstanceIds = None

    @property
    def InstanceConfs(self):
        """实例配置，包括巡检、概览开关等。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        """
        return self._InstanceConfs

    @InstanceConfs.setter
    def InstanceConfs(self, InstanceConfs):
        self._InstanceConfs = InstanceConfs

    @property
    def Regions(self):
        """生效实例地域，取值为"All"，代表全地域。
        :rtype: str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Product(self):
        """服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，"redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceIds(self):
        """指定更改巡检状态的实例ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        if params.get("InstanceConfs") is not None:
            self._InstanceConfs = InstanceConfs()
            self._InstanceConfs._deserialize(params.get("InstanceConfs"))
        self._Regions = params.get("Regions")
        self._Product = params.get("Product")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfResponse(AbstractModel):
    """ModifyDiagDBInstanceConf返回参数结构体

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


class ModifySqlFiltersRequest(AbstractModel):
    """ModifySqlFilters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _FilterIds: SQL限流任务ID列表。
        :type FilterIds: list of int
        :param _Status: 限流任务状态，取值支持TERMINATED - 终止。
        :type Status: str
        :param _SessionToken: 通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :type SessionToken: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._FilterIds = None
        self._Status = None
        self._SessionToken = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FilterIds(self):
        """SQL限流任务ID列表。
        :rtype: list of int
        """
        return self._FilterIds

    @FilterIds.setter
    def FilterIds(self, FilterIds):
        self._FilterIds = FilterIds

    @property
    def Status(self):
        """限流任务状态，取值支持TERMINATED - 终止。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SessionToken(self):
        """通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FilterIds = params.get("FilterIds")
        self._Status = params.get("Status")
        self._SessionToken = params.get("SessionToken")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySqlFiltersResponse(AbstractModel):
    """ModifySqlFilters返回参数结构体

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


class ModifyUserAutonomyProfileRequest(AbstractModel):
    """ModifyUserAutonomyProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileType: 配置类型，为需要配置的功能枚举值，目前包含一下枚举值：AutonomyGlobal（自治功能全局配置）、RedisAutoScaleUp（Redis自治扩容配置）
        :type ProfileType: str
        :param _InstanceId: 实列ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        :param _NewProfileInfo: 自治功能相关配置，标准JSON字符串格式。
        :type NewProfileInfo: str
        """
        self._ProfileType = None
        self._InstanceId = None
        self._Product = None
        self._NewProfileInfo = None

    @property
    def ProfileType(self):
        """配置类型，为需要配置的功能枚举值，目前包含一下枚举值：AutonomyGlobal（自治功能全局配置）、RedisAutoScaleUp（Redis自治扩容配置）
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def InstanceId(self):
        """实列ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def NewProfileInfo(self):
        """自治功能相关配置，标准JSON字符串格式。
        :rtype: str
        """
        return self._NewProfileInfo

    @NewProfileInfo.setter
    def NewProfileInfo(self, NewProfileInfo):
        self._NewProfileInfo = NewProfileInfo


    def _deserialize(self, params):
        self._ProfileType = params.get("ProfileType")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        self._NewProfileInfo = params.get("NewProfileInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserAutonomyProfileResponse(AbstractModel):
    """ModifyUserAutonomyProfile返回参数结构体

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


class MongoDBIndex(AbstractModel):
    """Mongodb索引项

    """

    def __init__(self):
        r"""
        :param _ClusterId: 实例id。
        :type ClusterId: str
        :param _Collection: 表名。
        :type Collection: str
        :param _Db: 库名。
        :type Db: str
        :param _Level: 优化级别，1-4，优先级从高到低。
        :type Level: int
        :param _Score: 得分。
        :type Score: int
        :param _IndexesToBuild: 推荐索引列表。
        :type IndexesToBuild: list of IndexesToBuild
        :param _IndexesToDrop: 无效索引列表。
        :type IndexesToDrop: list of IndexesToDrop
        """
        self._ClusterId = None
        self._Collection = None
        self._Db = None
        self._Level = None
        self._Score = None
        self._IndexesToBuild = None
        self._IndexesToDrop = None

    @property
    def ClusterId(self):
        """实例id。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Collection(self):
        """表名。
        :rtype: str
        """
        return self._Collection

    @Collection.setter
    def Collection(self, Collection):
        self._Collection = Collection

    @property
    def Db(self):
        """库名。
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Level(self):
        """优化级别，1-4，优先级从高到低。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Score(self):
        """得分。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def IndexesToBuild(self):
        """推荐索引列表。
        :rtype: list of IndexesToBuild
        """
        return self._IndexesToBuild

    @IndexesToBuild.setter
    def IndexesToBuild(self, IndexesToBuild):
        self._IndexesToBuild = IndexesToBuild

    @property
    def IndexesToDrop(self):
        """无效索引列表。
        :rtype: list of IndexesToDrop
        """
        return self._IndexesToDrop

    @IndexesToDrop.setter
    def IndexesToDrop(self, IndexesToDrop):
        self._IndexesToDrop = IndexesToDrop


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Collection = params.get("Collection")
        self._Db = params.get("Db")
        self._Level = params.get("Level")
        self._Score = params.get("Score")
        if params.get("IndexesToBuild") is not None:
            self._IndexesToBuild = []
            for item in params.get("IndexesToBuild"):
                obj = IndexesToBuild()
                obj._deserialize(item)
                self._IndexesToBuild.append(obj)
        if params.get("IndexesToDrop") is not None:
            self._IndexesToDrop = []
            for item in params.get("IndexesToDrop"):
                obj = IndexesToDrop()
                obj._deserialize(item)
                self._IndexesToDrop.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorFloatMetric(AbstractModel):
    """监控数据（浮点型）

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名称。
        :type Metric: str
        :param _Unit: 指标单位。
        :type Unit: str
        :param _Values: 指标值。
        :type Values: list of float
        """
        self._Metric = None
        self._Unit = None
        self._Values = None

    @property
    def Metric(self):
        """指标名称。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Unit(self):
        """指标单位。
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Values(self):
        """指标值。
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Unit = params.get("Unit")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorFloatMetricSeriesData(AbstractModel):
    """单位时间间隔内的监控指标数据（浮点型）

    """

    def __init__(self):
        r"""
        :param _Series: 监控指标。
        :type Series: list of MonitorFloatMetric
        :param _Timestamp: 监控指标对应的时间戳。
        :type Timestamp: list of int
        """
        self._Series = None
        self._Timestamp = None

    @property
    def Series(self):
        """监控指标。
        :rtype: list of MonitorFloatMetric
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Timestamp(self):
        """监控指标对应的时间戳。
        :rtype: list of int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = MonitorFloatMetric()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetric(AbstractModel):
    """监控数据

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名称。
        :type Metric: str
        :param _Unit: 指标单位。
        :type Unit: str
        :param _Values: 指标值。
        :type Values: list of float
        """
        self._Metric = None
        self._Unit = None
        self._Values = None

    @property
    def Metric(self):
        """指标名称。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Unit(self):
        """指标单位。
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Values(self):
        """指标值。
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Unit = params.get("Unit")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetricSeriesData(AbstractModel):
    """单位时间间隔内的监控指标数据

    """

    def __init__(self):
        r"""
        :param _Series: 监控指标。
        :type Series: list of MonitorMetric
        :param _Timestamp: 监控指标对应的时间戳。
        :type Timestamp: list of int
        """
        self._Series = None
        self._Timestamp = None

    @property
    def Series(self):
        """监控指标。
        :rtype: list of MonitorMetric
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Timestamp(self):
        """监控指标对应的时间戳。
        :rtype: list of int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = MonitorMetric()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySqlProcess(AbstractModel):
    """关系型数据库线程

    """

    def __init__(self):
        r"""
        :param _ID: 线程ID。
        :type ID: str
        :param _User: 线程的操作账号名。
        :type User: str
        :param _Host: 线程的操作主机地址。
        :type Host: str
        :param _DB: 线程的操作数据库。
        :type DB: str
        :param _State: 线程的操作状态。
        :type State: str
        :param _Command: 线程的执行类型。
        :type Command: str
        :param _Time: 线程的操作时长，单位秒。
        :type Time: str
        :param _Info: 线程的操作语句。
        :type Info: str
        """
        self._ID = None
        self._User = None
        self._Host = None
        self._DB = None
        self._State = None
        self._Command = None
        self._Time = None
        self._Info = None

    @property
    def ID(self):
        """线程ID。
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def User(self):
        """线程的操作账号名。
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        """线程的操作主机地址。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DB(self):
        """线程的操作数据库。
        :rtype: str
        """
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def State(self):
        """线程的操作状态。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Command(self):
        """线程的执行类型。
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Time(self):
        """线程的操作时长，单位秒。
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Info(self):
        """线程的操作语句。
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._User = params.get("User")
        self._Host = params.get("Host")
        self._DB = params.get("DB")
        self._State = params.get("State")
        self._Command = params.get("Command")
        self._Time = params.get("Time")
        self._Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceRequest(AbstractModel):
    """OpenAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB。
        :type Product: str
        :param _NodeRequestType: 与Product保持一致。如："dcdb" ,"mariadb"。
        :type NodeRequestType: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _LogExpireDay: 日志保存总时长，只能是7,30,90,180,365,1095,1825。
        :type LogExpireDay: int
        :param _HotLogExpireDay: 高频日志保存时长，只能是7,30,90,180,365,1095,1825。
        :type HotLogExpireDay: int
        """
        self._Product = None
        self._NodeRequestType = None
        self._InstanceId = None
        self._LogExpireDay = None
        self._HotLogExpireDay = None

    @property
    def Product(self):
        """服务产品类型，支持值包括： "dcdb" - 云数据库 Tdsql， "mariadb" - 云数据库 MariaDB。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def NodeRequestType(self):
        """与Product保持一致。如："dcdb" ,"mariadb"。
        :rtype: str
        """
        return self._NodeRequestType

    @NodeRequestType.setter
    def NodeRequestType(self, NodeRequestType):
        self._NodeRequestType = NodeRequestType

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        """日志保存总时长，只能是7,30,90,180,365,1095,1825。
        :rtype: int
        """
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HotLogExpireDay(self):
        """高频日志保存时长，只能是7,30,90,180,365,1095,1825。
        :rtype: int
        """
        return self._HotLogExpireDay

    @HotLogExpireDay.setter
    def HotLogExpireDay(self, HotLogExpireDay):
        self._HotLogExpireDay = HotLogExpireDay


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._NodeRequestType = params.get("NodeRequestType")
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HotLogExpireDay = params.get("HotLogExpireDay")
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
        :param _TaskId: taskId 为0表示开通审计成功，否则开通失败
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """taskId 为0表示开通审计成功，否则开通失败
        :rtype: int
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


class Process(AbstractModel):
    """实时会话详情。

    """

    def __init__(self):
        r"""
        :param _Id: 会话 ID。
        :type Id: int
        :param _Address: 访问来源，IP 地址和端口号。
        :type Address: str
        :param _FileDescriptor: 文件描述符。
        :type FileDescriptor: int
        :param _Name: 会话名称，使用 CLIENT SETNAME 命令设置。
        :type Name: str
        :param _LastCommand: 最后一次执行的命令。
        :type LastCommand: str
        :param _Age: 会话存活时间，单位：秒。
        :type Age: int
        :param _Idle: 最后一次执行命令后空闲的时间，单位：秒。
        :type Idle: int
        :param _ProxyId: 会话所属的 Proxy节点 ID。
        :type ProxyId: str
        """
        self._Id = None
        self._Address = None
        self._FileDescriptor = None
        self._Name = None
        self._LastCommand = None
        self._Age = None
        self._Idle = None
        self._ProxyId = None

    @property
    def Id(self):
        """会话 ID。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Address(self):
        """访问来源，IP 地址和端口号。
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def FileDescriptor(self):
        """文件描述符。
        :rtype: int
        """
        return self._FileDescriptor

    @FileDescriptor.setter
    def FileDescriptor(self, FileDescriptor):
        self._FileDescriptor = FileDescriptor

    @property
    def Name(self):
        """会话名称，使用 CLIENT SETNAME 命令设置。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LastCommand(self):
        """最后一次执行的命令。
        :rtype: str
        """
        return self._LastCommand

    @LastCommand.setter
    def LastCommand(self, LastCommand):
        self._LastCommand = LastCommand

    @property
    def Age(self):
        """会话存活时间，单位：秒。
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Idle(self):
        """最后一次执行命令后空闲的时间，单位：秒。
        :rtype: int
        """
        return self._Idle

    @Idle.setter
    def Idle(self, Idle):
        self._Idle = Idle

    @property
    def ProxyId(self):
        """会话所属的 Proxy节点 ID。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Address = params.get("Address")
        self._FileDescriptor = params.get("FileDescriptor")
        self._Name = params.get("Name")
        self._LastCommand = params.get("LastCommand")
        self._Age = params.get("Age")
        self._Idle = params.get("Idle")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStatistic(AbstractModel):
    """实时会话统计详情。

    """

    def __init__(self):
        r"""
        :param _Items: 会话详情数组。
        :type Items: list of SessionItem
        :param _AllConnSum: 总连接数。
        :type AllConnSum: int
        :param _ActiveConnSum: 总活跃连接数。
        :type ActiveConnSum: int
        """
        self._Items = None
        self._AllConnSum = None
        self._ActiveConnSum = None

    @property
    def Items(self):
        """会话详情数组。
        :rtype: list of SessionItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def AllConnSum(self):
        """总连接数。
        :rtype: int
        """
        return self._AllConnSum

    @AllConnSum.setter
    def AllConnSum(self, AllConnSum):
        self._AllConnSum = AllConnSum

    @property
    def ActiveConnSum(self):
        """总活跃连接数。
        :rtype: int
        """
        return self._ActiveConnSum

    @ActiveConnSum.setter
    def ActiveConnSum(self, ActiveConnSum):
        self._ActiveConnSum = ActiveConnSum


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SessionItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._AllConnSum = params.get("AllConnSum")
        self._ActiveConnSum = params.get("ActiveConnSum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProfileInfo(AbstractModel):
    """用户配置的信息

    """

    def __init__(self):
        r"""
        :param _Language: 语言, 如"zh"。
        :type Language: str
        :param _MailConfiguration: 邮件模板的内容。
        :type MailConfiguration: :class:`tencentcloud.dbbrain.v20210527.models.MailConfiguration`
        """
        self._Language = None
        self._MailConfiguration = None

    @property
    def Language(self):
        """语言, 如"zh"。
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def MailConfiguration(self):
        """邮件模板的内容。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.MailConfiguration`
        """
        return self._MailConfiguration

    @MailConfiguration.setter
    def MailConfiguration(self, MailConfiguration):
        self._MailConfiguration = MailConfiguration


    def _deserialize(self, params):
        self._Language = params.get("Language")
        if params.get("MailConfiguration") is not None:
            self._MailConfiguration = MailConfiguration()
            self._MailConfiguration._deserialize(params.get("MailConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveInfo(AbstractModel):
    """接收组信息

    """

    def __init__(self):
        r"""
        :param _ReceiveGroup: 接收组
        :type ReceiveGroup: list of int
        :param _EndReceiveTime: 最后接收时间
        :type EndReceiveTime: str
        :param _ReceiveName: 接收名
        :type ReceiveName: str
        :param _SendChannel: 推送渠道
        :type SendChannel: list of int
        :param _StartReceiveTime: 开始时间
        :type StartReceiveTime: str
        :param _ReceiveUin: 接收用户列表
        :type ReceiveUin: list of ReceiveUin
        """
        self._ReceiveGroup = None
        self._EndReceiveTime = None
        self._ReceiveName = None
        self._SendChannel = None
        self._StartReceiveTime = None
        self._ReceiveUin = None

    @property
    def ReceiveGroup(self):
        """接收组
        :rtype: list of int
        """
        return self._ReceiveGroup

    @ReceiveGroup.setter
    def ReceiveGroup(self, ReceiveGroup):
        self._ReceiveGroup = ReceiveGroup

    @property
    def EndReceiveTime(self):
        """最后接收时间
        :rtype: str
        """
        return self._EndReceiveTime

    @EndReceiveTime.setter
    def EndReceiveTime(self, EndReceiveTime):
        self._EndReceiveTime = EndReceiveTime

    @property
    def ReceiveName(self):
        """接收名
        :rtype: str
        """
        return self._ReceiveName

    @ReceiveName.setter
    def ReceiveName(self, ReceiveName):
        self._ReceiveName = ReceiveName

    @property
    def SendChannel(self):
        """推送渠道
        :rtype: list of int
        """
        return self._SendChannel

    @SendChannel.setter
    def SendChannel(self, SendChannel):
        self._SendChannel = SendChannel

    @property
    def StartReceiveTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartReceiveTime

    @StartReceiveTime.setter
    def StartReceiveTime(self, StartReceiveTime):
        self._StartReceiveTime = StartReceiveTime

    @property
    def ReceiveUin(self):
        """接收用户列表
        :rtype: list of ReceiveUin
        """
        return self._ReceiveUin

    @ReceiveUin.setter
    def ReceiveUin(self, ReceiveUin):
        self._ReceiveUin = ReceiveUin


    def _deserialize(self, params):
        self._ReceiveGroup = params.get("ReceiveGroup")
        self._EndReceiveTime = params.get("EndReceiveTime")
        self._ReceiveName = params.get("ReceiveName")
        self._SendChannel = params.get("SendChannel")
        self._StartReceiveTime = params.get("StartReceiveTime")
        if params.get("ReceiveUin") is not None:
            self._ReceiveUin = []
            for item in params.get("ReceiveUin"):
                obj = ReceiveUin()
                obj._deserialize(item)
                self._ReceiveUin.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveUin(AbstractModel):
    """接收用户

    """

    def __init__(self):
        r"""
        :param _UinName: 用户名
        :type UinName: str
        :param _Uin: 用户id
        :type Uin: str
        """
        self._UinName = None
        self._Uin = None

    @property
    def UinName(self):
        """用户名
        :rtype: str
        """
        return self._UinName

    @UinName.setter
    def UinName(self, UinName):
        self._UinName = UinName

    @property
    def Uin(self):
        """用户id
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._UinName = params.get("UinName")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisBigKeyTask(AbstractModel):
    """Redis大Key分析任务详情。

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务请求 ID。
        :type AsyncRequestId: int
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _EndTime: 任务结束时间。
        :type EndTime: str
        :param _TaskStatus: 任务状态。
        :type TaskStatus: str
        :param _Progress: 任务执行进度。
        :type Progress: int
        :param _ShardIds: 任务包含的分片节点序号列表。
        :type ShardIds: list of int
        """
        self._AsyncRequestId = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._TaskStatus = None
        self._Progress = None
        self._ShardIds = None

    @property
    def AsyncRequestId(self):
        """异步任务请求 ID。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def CreateTime(self):
        """任务创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """任务开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskStatus(self):
        """任务状态。
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Progress(self):
        """任务执行进度。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def ShardIds(self):
        """任务包含的分片节点序号列表。
        :rtype: list of int
        """
        return self._ShardIds

    @ShardIds.setter
    def ShardIds(self, ShardIds):
        self._ShardIds = ShardIds


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskStatus = params.get("TaskStatus")
        self._Progress = params.get("Progress")
        self._ShardIds = params.get("ShardIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisCmdInfo(AbstractModel):
    """redis访问命令详情

    """

    def __init__(self):
        r"""
        :param _Cmd: redis命令
        :type Cmd: str
        :param _Count: 命令次数
        :type Count: int
        """
        self._Cmd = None
        self._Count = None

    @property
    def Cmd(self):
        """redis命令
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Count(self):
        """命令次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisInstanceConf(AbstractModel):
    """Redis实例内存配置参数

    """

    def __init__(self):
        r"""
        :param _ReplicasNum: 副本数量
        :type ReplicasNum: str
        :param _ShardNum: 分片数量
        :type ShardNum: str
        :param _ShardSize: 分片内存大小，单位MB
        :type ShardSize: str
        """
        self._ReplicasNum = None
        self._ShardNum = None
        self._ShardSize = None

    @property
    def ReplicasNum(self):
        """副本数量
        :rtype: str
        """
        return self._ReplicasNum

    @ReplicasNum.setter
    def ReplicasNum(self, ReplicasNum):
        self._ReplicasNum = ReplicasNum

    @property
    def ShardNum(self):
        """分片数量
        :rtype: str
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def ShardSize(self):
        """分片内存大小，单位MB
        :rtype: str
        """
        return self._ShardSize

    @ShardSize.setter
    def ShardSize(self, ShardSize):
        self._ShardSize = ShardSize


    def _deserialize(self, params):
        self._ReplicasNum = params.get("ReplicasNum")
        self._ShardNum = params.get("ShardNum")
        self._ShardSize = params.get("ShardSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisKeySpaceData(AbstractModel):
    """redis key空间信息。

    """

    def __init__(self):
        r"""
        :param _Key: key名。
        :type Key: str
        :param _Type: key类型。
        :type Type: str
        :param _Encoding: key编码方式。
        :type Encoding: str
        :param _ExpireTime: key过期时间戳（毫秒），0代表未设置过期时间。
        :type ExpireTime: int
        :param _Length: key内存大小，单位Byte。
        :type Length: int
        :param _ItemCount: 元素个数。
        :type ItemCount: int
        :param _MaxElementSize: 最大元素长度。
        :type MaxElementSize: int
        :param _AveElementSize: 平均元素长度。
        :type AveElementSize: int
        :param _ShardId: 所属分片序号。
        :type ShardId: str
        """
        self._Key = None
        self._Type = None
        self._Encoding = None
        self._ExpireTime = None
        self._Length = None
        self._ItemCount = None
        self._MaxElementSize = None
        self._AveElementSize = None
        self._ShardId = None

    @property
    def Key(self):
        """key名。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        """key类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Encoding(self):
        """key编码方式。
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def ExpireTime(self):
        """key过期时间戳（毫秒），0代表未设置过期时间。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Length(self):
        """key内存大小，单位Byte。
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def ItemCount(self):
        """元素个数。
        :rtype: int
        """
        return self._ItemCount

    @ItemCount.setter
    def ItemCount(self, ItemCount):
        self._ItemCount = ItemCount

    @property
    def MaxElementSize(self):
        """最大元素长度。
        :rtype: int
        """
        return self._MaxElementSize

    @MaxElementSize.setter
    def MaxElementSize(self, MaxElementSize):
        self._MaxElementSize = MaxElementSize

    @property
    def AveElementSize(self):
        """平均元素长度。
        :rtype: int
        """
        return self._AveElementSize

    @AveElementSize.setter
    def AveElementSize(self, AveElementSize):
        self._AveElementSize = AveElementSize

    @property
    def ShardId(self):
        """所属分片序号。
        :rtype: str
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Encoding = params.get("Encoding")
        self._ExpireTime = params.get("ExpireTime")
        self._Length = params.get("Length")
        self._ItemCount = params.get("ItemCount")
        self._MaxElementSize = params.get("MaxElementSize")
        self._AveElementSize = params.get("AveElementSize")
        self._ShardId = params.get("ShardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisPreKeySpaceData(AbstractModel):
    """redis key前缀空间信息

    """

    def __init__(self):
        r"""
        :param _AveElementSize: 平均元素长度。
        :type AveElementSize: int
        :param _Length: 总占用内存（Byte）。
        :type Length: int
        :param _KeyPreIndex: key前缀。
        :type KeyPreIndex: str
        :param _ItemCount: 元素数量。
        :type ItemCount: int
        :param _Count: key个数。
        :type Count: int
        :param _MaxElementSize: 最大元素长度。
        :type MaxElementSize: int
        """
        self._AveElementSize = None
        self._Length = None
        self._KeyPreIndex = None
        self._ItemCount = None
        self._Count = None
        self._MaxElementSize = None

    @property
    def AveElementSize(self):
        """平均元素长度。
        :rtype: int
        """
        return self._AveElementSize

    @AveElementSize.setter
    def AveElementSize(self, AveElementSize):
        self._AveElementSize = AveElementSize

    @property
    def Length(self):
        """总占用内存（Byte）。
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def KeyPreIndex(self):
        """key前缀。
        :rtype: str
        """
        return self._KeyPreIndex

    @KeyPreIndex.setter
    def KeyPreIndex(self, KeyPreIndex):
        self._KeyPreIndex = KeyPreIndex

    @property
    def ItemCount(self):
        """元素数量。
        :rtype: int
        """
        return self._ItemCount

    @ItemCount.setter
    def ItemCount(self, ItemCount):
        self._ItemCount = ItemCount

    @property
    def Count(self):
        """key个数。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def MaxElementSize(self):
        """最大元素长度。
        :rtype: int
        """
        return self._MaxElementSize

    @MaxElementSize.setter
    def MaxElementSize(self, MaxElementSize):
        self._MaxElementSize = MaxElementSize


    def _deserialize(self, params):
        self._AveElementSize = params.get("AveElementSize")
        self._Length = params.get("Length")
        self._KeyPreIndex = params.get("KeyPreIndex")
        self._ItemCount = params.get("ItemCount")
        self._Count = params.get("Count")
        self._MaxElementSize = params.get("MaxElementSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLFilter(AbstractModel):
    """实例SQL限流任务。

    """

    def __init__(self):
        r"""
        :param _Id: 任务ID。
        :type Id: int
        :param _Status: 任务状态，取值包括RUNNING - 运行中, FINISHED - 已完成, TERMINATED - 已终止。
        :type Status: str
        :param _SqlType: SQL类型，取值包括SELECT, UPDATE, DELETE, INSERT, REPLACE。
        :type SqlType: str
        :param _OriginKeys: 筛选SQL的关键词，多个关键词用英文逗号拼接。
        :type OriginKeys: str
        :param _OriginRule: 筛选SQL的规则。
        :type OriginRule: str
        :param _RejectedSqlCount: 已拒绝SQL数目。
        :type RejectedSqlCount: int
        :param _CurrentConcurrency: 当前并发数。
        :type CurrentConcurrency: int
        :param _MaxConcurrency: 最大并发数。
        :type MaxConcurrency: int
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _CurrentTime: 当前时间。
        :type CurrentTime: str
        :param _ExpireTime: 限流过期时间。
        :type ExpireTime: str
        """
        self._Id = None
        self._Status = None
        self._SqlType = None
        self._OriginKeys = None
        self._OriginRule = None
        self._RejectedSqlCount = None
        self._CurrentConcurrency = None
        self._MaxConcurrency = None
        self._CreateTime = None
        self._CurrentTime = None
        self._ExpireTime = None

    @property
    def Id(self):
        """任务ID。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """任务状态，取值包括RUNNING - 运行中, FINISHED - 已完成, TERMINATED - 已终止。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SqlType(self):
        """SQL类型，取值包括SELECT, UPDATE, DELETE, INSERT, REPLACE。
        :rtype: str
        """
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def OriginKeys(self):
        """筛选SQL的关键词，多个关键词用英文逗号拼接。
        :rtype: str
        """
        return self._OriginKeys

    @OriginKeys.setter
    def OriginKeys(self, OriginKeys):
        self._OriginKeys = OriginKeys

    @property
    def OriginRule(self):
        """筛选SQL的规则。
        :rtype: str
        """
        return self._OriginRule

    @OriginRule.setter
    def OriginRule(self, OriginRule):
        self._OriginRule = OriginRule

    @property
    def RejectedSqlCount(self):
        """已拒绝SQL数目。
        :rtype: int
        """
        return self._RejectedSqlCount

    @RejectedSqlCount.setter
    def RejectedSqlCount(self, RejectedSqlCount):
        self._RejectedSqlCount = RejectedSqlCount

    @property
    def CurrentConcurrency(self):
        """当前并发数。
        :rtype: int
        """
        return self._CurrentConcurrency

    @CurrentConcurrency.setter
    def CurrentConcurrency(self, CurrentConcurrency):
        self._CurrentConcurrency = CurrentConcurrency

    @property
    def MaxConcurrency(self):
        """最大并发数。
        :rtype: int
        """
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def CreateTime(self):
        """任务创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CurrentTime(self):
        """当前时间。
        :rtype: str
        """
        return self._CurrentTime

    @CurrentTime.setter
    def CurrentTime(self, CurrentTime):
        self._CurrentTime = CurrentTime

    @property
    def ExpireTime(self):
        """限流过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._SqlType = params.get("SqlType")
        self._OriginKeys = params.get("OriginKeys")
        self._OriginRule = params.get("OriginRule")
        self._RejectedSqlCount = params.get("RejectedSqlCount")
        self._CurrentConcurrency = params.get("CurrentConcurrency")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._CreateTime = params.get("CreateTime")
        self._CurrentTime = params.get("CurrentTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaItem(AbstractModel):
    """SchemaItem数组

    """

    def __init__(self):
        r"""
        :param _Schema: 数据库名称
        :type Schema: str
        """
        self._Schema = None

    @property
    def Schema(self):
        """数据库名称
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema


    def _deserialize(self, params):
        self._Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceData(AbstractModel):
    """库空间统计数据。

    """

    def __init__(self):
        r"""
        :param _TableSchema: 库名。
        :type TableSchema: str
        :param _DataLength: 数据空间（MB）。
        :type DataLength: float
        :param _IndexLength: 索引空间（MB）。
        :type IndexLength: float
        :param _DataFree: 碎片空间（MB）。
        :type DataFree: float
        :param _TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        :param _FragRatio: 碎片率（%）。
        :type FragRatio: float
        :param _TableRows: 行数。
        :type TableRows: int
        :param _PhysicalFileSize: 库中所有表对应的独立物理文件大小加和（MB）。
        :type PhysicalFileSize: float
        """
        self._TableSchema = None
        self._DataLength = None
        self._IndexLength = None
        self._DataFree = None
        self._TotalLength = None
        self._FragRatio = None
        self._TableRows = None
        self._PhysicalFileSize = None

    @property
    def TableSchema(self):
        """库名。
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def DataLength(self):
        """数据空间（MB）。
        :rtype: float
        """
        return self._DataLength

    @DataLength.setter
    def DataLength(self, DataLength):
        self._DataLength = DataLength

    @property
    def IndexLength(self):
        """索引空间（MB）。
        :rtype: float
        """
        return self._IndexLength

    @IndexLength.setter
    def IndexLength(self, IndexLength):
        self._IndexLength = IndexLength

    @property
    def DataFree(self):
        """碎片空间（MB）。
        :rtype: float
        """
        return self._DataFree

    @DataFree.setter
    def DataFree(self, DataFree):
        self._DataFree = DataFree

    @property
    def TotalLength(self):
        """总使用空间（MB）。
        :rtype: float
        """
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength

    @property
    def FragRatio(self):
        """碎片率（%）。
        :rtype: float
        """
        return self._FragRatio

    @FragRatio.setter
    def FragRatio(self, FragRatio):
        self._FragRatio = FragRatio

    @property
    def TableRows(self):
        """行数。
        :rtype: int
        """
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def PhysicalFileSize(self):
        """库中所有表对应的独立物理文件大小加和（MB）。
        :rtype: float
        """
        return self._PhysicalFileSize

    @PhysicalFileSize.setter
    def PhysicalFileSize(self, PhysicalFileSize):
        self._PhysicalFileSize = PhysicalFileSize


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        self._DataLength = params.get("DataLength")
        self._IndexLength = params.get("IndexLength")
        self._DataFree = params.get("DataFree")
        self._TotalLength = params.get("TotalLength")
        self._FragRatio = params.get("FragRatio")
        self._TableRows = params.get("TableRows")
        self._PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceTimeSeries(AbstractModel):
    """库空间时序数据

    """

    def __init__(self):
        r"""
        :param _TableSchema: 库名
        :type TableSchema: str
        :param _SeriesData: 单位时间间隔内的空间指标数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        """
        self._TableSchema = None
        self._SeriesData = None

    @property
    def TableSchema(self):
        """库名
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def SeriesData(self):
        """单位时间间隔内的空间指标数据。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        """
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreDetail(AbstractModel):
    """扣分详情。

    """

    def __init__(self):
        r"""
        :param _IssueType: 扣分项分类，取值包括：可用性、可维护性、性能及可靠性。
        :type IssueType: str
        :param _ScoreLost: 扣分总分。
        :type ScoreLost: int
        :param _ScoreLostMax: 扣分总分上限。
        :type ScoreLostMax: int
        :param _Items: 扣分项列表。
        :type Items: list of ScoreItem
        """
        self._IssueType = None
        self._ScoreLost = None
        self._ScoreLostMax = None
        self._Items = None

    @property
    def IssueType(self):
        """扣分项分类，取值包括：可用性、可维护性、性能及可靠性。
        :rtype: str
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def ScoreLost(self):
        """扣分总分。
        :rtype: int
        """
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def ScoreLostMax(self):
        """扣分总分上限。
        :rtype: int
        """
        return self._ScoreLostMax

    @ScoreLostMax.setter
    def ScoreLostMax(self, ScoreLostMax):
        self._ScoreLostMax = ScoreLostMax

    @property
    def Items(self):
        """扣分项列表。
        :rtype: list of ScoreItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._IssueType = params.get("IssueType")
        self._ScoreLost = params.get("ScoreLost")
        self._ScoreLostMax = params.get("ScoreLostMax")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ScoreItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreItem(AbstractModel):
    """诊断扣分项。

    """

    def __init__(self):
        r"""
        :param _DiagItem: 异常诊断项名称。
        :type DiagItem: str
        :param _IssueType: 诊断项分类，取值包括：可用性、可维护性、性能及可靠性。
        :type IssueType: str
        :param _TopSeverity: 健康等级，取值包括：信息、提示、告警、严重、致命。
        :type TopSeverity: str
        :param _Count: 该异常诊断项出现次数。
        :type Count: int
        :param _ScoreLost: 扣分分数。
        :type ScoreLost: int
        """
        self._DiagItem = None
        self._IssueType = None
        self._TopSeverity = None
        self._Count = None
        self._ScoreLost = None

    @property
    def DiagItem(self):
        """异常诊断项名称。
        :rtype: str
        """
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def IssueType(self):
        """诊断项分类，取值包括：可用性、可维护性、性能及可靠性。
        :rtype: str
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def TopSeverity(self):
        """健康等级，取值包括：信息、提示、告警、严重、致命。
        :rtype: str
        """
        return self._TopSeverity

    @TopSeverity.setter
    def TopSeverity(self, TopSeverity):
        self._TopSeverity = TopSeverity

    @property
    def Count(self):
        """该异常诊断项出现次数。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ScoreLost(self):
        """扣分分数。
        :rtype: int
        """
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost


    def _deserialize(self, params):
        self._DiagItem = params.get("DiagItem")
        self._IssueType = params.get("IssueType")
        self._TopSeverity = params.get("TopSeverity")
        self._Count = params.get("Count")
        self._ScoreLost = params.get("ScoreLost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogExportTaskInfo(AbstractModel):
    """安全审计日志导出任务信息

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务Id。
        :type AsyncRequestId: int
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _EndTime: 任务结束时间。
        :type EndTime: str
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _Status: 任务状态。
        :type Status: str
        :param _Progress: 任务执行进度。
        :type Progress: int
        :param _LogStartTime: 导出日志开始时间。
        :type LogStartTime: str
        :param _LogEndTime: 导出日志结束时间。
        :type LogEndTime: str
        :param _TotalSize: 日志文件总大小，单位KB。
        :type TotalSize: int
        :param _DangerLevels: 风险等级列表。0 无风险；1 低风险；2 中风险；3 高风险。
        :type DangerLevels: list of int non-negative
        """
        self._AsyncRequestId = None
        self._StartTime = None
        self._EndTime = None
        self._CreateTime = None
        self._Status = None
        self._Progress = None
        self._LogStartTime = None
        self._LogEndTime = None
        self._TotalSize = None
        self._DangerLevels = None

    @property
    def AsyncRequestId(self):
        """异步任务Id。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def StartTime(self):
        """任务开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreateTime(self):
        """任务创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        """任务状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        """任务执行进度。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def LogStartTime(self):
        """导出日志开始时间。
        :rtype: str
        """
        return self._LogStartTime

    @LogStartTime.setter
    def LogStartTime(self, LogStartTime):
        self._LogStartTime = LogStartTime

    @property
    def LogEndTime(self):
        """导出日志结束时间。
        :rtype: str
        """
        return self._LogEndTime

    @LogEndTime.setter
    def LogEndTime(self, LogEndTime):
        self._LogEndTime = LogEndTime

    @property
    def TotalSize(self):
        """日志文件总大小，单位KB。
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def DangerLevels(self):
        """风险等级列表。0 无风险；1 低风险；2 中风险；3 高风险。
        :rtype: list of int non-negative
        """
        return self._DangerLevels

    @DangerLevels.setter
    def DangerLevels(self, DangerLevels):
        self._DangerLevels = DangerLevels


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._LogStartTime = params.get("LogStartTime")
        self._LogEndTime = params.get("LogEndTime")
        self._TotalSize = params.get("TotalSize")
        self._DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionItem(AbstractModel):
    """实时会话访问来源详情。

    """

    def __init__(self):
        r"""
        :param _Ip: 访问来源。
        :type Ip: str
        :param _ActiveConn: 当前访问来源活跃连接数
        :type ActiveConn: str
        :param _AllConn: 当前访问来源总连接数
        :type AllConn: int
        """
        self._Ip = None
        self._ActiveConn = None
        self._AllConn = None

    @property
    def Ip(self):
        """访问来源。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ActiveConn(self):
        """当前访问来源活跃连接数
        :rtype: str
        """
        return self._ActiveConn

    @ActiveConn.setter
    def ActiveConn(self, ActiveConn):
        self._ActiveConn = ActiveConn

    @property
    def AllConn(self):
        """当前访问来源总连接数
        :rtype: int
        """
        return self._AllConn

    @AllConn.setter
    def AllConn(self, AllConn):
        self._AllConn = AllConn


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._ActiveConn = params.get("ActiveConn")
        self._AllConn = params.get("AllConn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogAgg(AbstractModel):
    """redis top慢日志聚合详情。

    """

    def __init__(self):
        r"""
        :param _Cmd: 命令模版。
        :type Cmd: str
        :param _Detail: 命令详情。
        :type Detail: str
        :param _ExecTimes: 执行次数。
        :type ExecTimes: int
        :param _QueryTime: 总耗时。
        :type QueryTime: float
        :param _QueryTimeAvg: 平均执行时间。
        :type QueryTimeAvg: float
        :param _QueryTimeMax: 最大执行时间。
        :type QueryTimeMax: float
        :param _QueryTimeMin: 最小执行时间。
        :type QueryTimeMin: float
        :param _QueryTimeRatio: 总耗时占比
        :type QueryTimeRatio: float
        """
        self._Cmd = None
        self._Detail = None
        self._ExecTimes = None
        self._QueryTime = None
        self._QueryTimeAvg = None
        self._QueryTimeMax = None
        self._QueryTimeMin = None
        self._QueryTimeRatio = None

    @property
    def Cmd(self):
        """命令模版。
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Detail(self):
        """命令详情。
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def ExecTimes(self):
        """执行次数。
        :rtype: int
        """
        return self._ExecTimes

    @ExecTimes.setter
    def ExecTimes(self, ExecTimes):
        self._ExecTimes = ExecTimes

    @property
    def QueryTime(self):
        """总耗时。
        :rtype: float
        """
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def QueryTimeAvg(self):
        """平均执行时间。
        :rtype: float
        """
        return self._QueryTimeAvg

    @QueryTimeAvg.setter
    def QueryTimeAvg(self, QueryTimeAvg):
        self._QueryTimeAvg = QueryTimeAvg

    @property
    def QueryTimeMax(self):
        """最大执行时间。
        :rtype: float
        """
        return self._QueryTimeMax

    @QueryTimeMax.setter
    def QueryTimeMax(self, QueryTimeMax):
        self._QueryTimeMax = QueryTimeMax

    @property
    def QueryTimeMin(self):
        """最小执行时间。
        :rtype: float
        """
        return self._QueryTimeMin

    @QueryTimeMin.setter
    def QueryTimeMin(self, QueryTimeMin):
        self._QueryTimeMin = QueryTimeMin

    @property
    def QueryTimeRatio(self):
        """总耗时占比
        :rtype: float
        """
        return self._QueryTimeRatio

    @QueryTimeRatio.setter
    def QueryTimeRatio(self, QueryTimeRatio):
        self._QueryTimeRatio = QueryTimeRatio


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        self._Detail = params.get("Detail")
        self._ExecTimes = params.get("ExecTimes")
        self._QueryTime = params.get("QueryTime")
        self._QueryTimeAvg = params.get("QueryTimeAvg")
        self._QueryTimeMax = params.get("QueryTimeMax")
        self._QueryTimeMin = params.get("QueryTimeMin")
        self._QueryTimeRatio = params.get("QueryTimeRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogHost(AbstractModel):
    """慢日志来源地址详情。

    """

    def __init__(self):
        r"""
        :param _UserHost: 来源地址。
        :type UserHost: str
        :param _Ratio: 该来源地址的慢日志数目占总数目的比例，单位%。
        :type Ratio: float
        :param _Count: 该来源地址的慢日志数目。
        :type Count: int
        """
        self._UserHost = None
        self._Ratio = None
        self._Count = None

    @property
    def UserHost(self):
        """来源地址。
        :rtype: str
        """
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def Ratio(self):
        """该来源地址的慢日志数目占总数目的比例，单位%。
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Count(self):
        """该来源地址的慢日志数目。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserHost = params.get("UserHost")
        self._Ratio = params.get("Ratio")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogInfoItem(AbstractModel):
    """慢日志详细信息

    """

    def __init__(self):
        r"""
        :param _Timestamp: 慢日志开始时间
        :type Timestamp: str
        :param _SqlText: sql语句
        :type SqlText: str
        :param _Database: 数据库
        :type Database: str
        :param _UserName: User来源
        :type UserName: str
        :param _UserHost: IP来源
        :type UserHost: str
        :param _QueryTime: 执行时间,单位秒
        :type QueryTime: float
        :param _LockTime: 锁时间,单位秒
        :type LockTime: float
        :param _RowsExamined: 扫描行数
        :type RowsExamined: int
        :param _RowsSent: 返回行数
        :type RowsSent: int
        """
        self._Timestamp = None
        self._SqlText = None
        self._Database = None
        self._UserName = None
        self._UserHost = None
        self._QueryTime = None
        self._LockTime = None
        self._RowsExamined = None
        self._RowsSent = None

    @property
    def Timestamp(self):
        """慢日志开始时间
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SqlText(self):
        """sql语句
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Database(self):
        """数据库
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def UserName(self):
        """User来源
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserHost(self):
        """IP来源
        :rtype: str
        """
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def QueryTime(self):
        """执行时间,单位秒
        :rtype: float
        """
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def LockTime(self):
        """锁时间,单位秒
        :rtype: float
        """
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def RowsExamined(self):
        """扫描行数
        :rtype: int
        """
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsSent(self):
        """返回行数
        :rtype: int
        """
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._SqlText = params.get("SqlText")
        self._Database = params.get("Database")
        self._UserName = params.get("UserName")
        self._UserHost = params.get("UserHost")
        self._QueryTime = params.get("QueryTime")
        self._LockTime = params.get("LockTime")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsSent = params.get("RowsSent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogTopSqlItem(AbstractModel):
    """慢日志TopSql

    """

    def __init__(self):
        r"""
        :param _LockTime: sql总锁等待时间，单位秒
        :type LockTime: float
        :param _LockTimeMax: 最大锁等待时间，单位秒
        :type LockTimeMax: float
        :param _LockTimeMin: 最小锁等待时间，单位秒
        :type LockTimeMin: float
        :param _RowsExamined: 总扫描行数
        :type RowsExamined: int
        :param _RowsExaminedMax: 最大扫描行数
        :type RowsExaminedMax: int
        :param _RowsExaminedMin: 最小扫描行数
        :type RowsExaminedMin: int
        :param _QueryTime: 总耗时，单位秒
        :type QueryTime: float
        :param _QueryTimeMax: 最大执行时间，单位秒
        :type QueryTimeMax: float
        :param _QueryTimeMin: 最小执行时间，单位秒
        :type QueryTimeMin: float
        :param _RowsSent: 总返回行数
        :type RowsSent: int
        :param _RowsSentMax: 最大返回行数
        :type RowsSentMax: int
        :param _RowsSentMin: 最小返回行数
        :type RowsSentMin: int
        :param _ExecTimes: 执行次数
        :type ExecTimes: int
        :param _SqlTemplate: sql模板
        :type SqlTemplate: str
        :param _SqlText: 带参数SQL（随机）
        :type SqlText: str
        :param _Schema: 数据库名
        :type Schema: str
        :param _QueryTimeRatio: 总耗时占比，单位%
        :type QueryTimeRatio: float
        :param _LockTimeRatio: sql总锁等待时间占比，单位%
        :type LockTimeRatio: float
        :param _RowsExaminedRatio: 总扫描行数占比，单位%
        :type RowsExaminedRatio: float
        :param _RowsSentRatio: 总返回行数占比，单位%
        :type RowsSentRatio: float
        :param _QueryTimeAvg: 平均执行时间，单位秒
        :type QueryTimeAvg: float
        :param _RowsSentAvg: 平均返回行数
        :type RowsSentAvg: float
        :param _LockTimeAvg: 平均锁等待时间，单位秒
        :type LockTimeAvg: float
        :param _RowsExaminedAvg: 平均扫描行数
        :type RowsExaminedAvg: float
        :param _Md5: SQL模板的MD5值
        :type Md5: str
        """
        self._LockTime = None
        self._LockTimeMax = None
        self._LockTimeMin = None
        self._RowsExamined = None
        self._RowsExaminedMax = None
        self._RowsExaminedMin = None
        self._QueryTime = None
        self._QueryTimeMax = None
        self._QueryTimeMin = None
        self._RowsSent = None
        self._RowsSentMax = None
        self._RowsSentMin = None
        self._ExecTimes = None
        self._SqlTemplate = None
        self._SqlText = None
        self._Schema = None
        self._QueryTimeRatio = None
        self._LockTimeRatio = None
        self._RowsExaminedRatio = None
        self._RowsSentRatio = None
        self._QueryTimeAvg = None
        self._RowsSentAvg = None
        self._LockTimeAvg = None
        self._RowsExaminedAvg = None
        self._Md5 = None

    @property
    def LockTime(self):
        """sql总锁等待时间，单位秒
        :rtype: float
        """
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def LockTimeMax(self):
        """最大锁等待时间，单位秒
        :rtype: float
        """
        return self._LockTimeMax

    @LockTimeMax.setter
    def LockTimeMax(self, LockTimeMax):
        self._LockTimeMax = LockTimeMax

    @property
    def LockTimeMin(self):
        """最小锁等待时间，单位秒
        :rtype: float
        """
        return self._LockTimeMin

    @LockTimeMin.setter
    def LockTimeMin(self, LockTimeMin):
        self._LockTimeMin = LockTimeMin

    @property
    def RowsExamined(self):
        """总扫描行数
        :rtype: int
        """
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsExaminedMax(self):
        """最大扫描行数
        :rtype: int
        """
        return self._RowsExaminedMax

    @RowsExaminedMax.setter
    def RowsExaminedMax(self, RowsExaminedMax):
        self._RowsExaminedMax = RowsExaminedMax

    @property
    def RowsExaminedMin(self):
        """最小扫描行数
        :rtype: int
        """
        return self._RowsExaminedMin

    @RowsExaminedMin.setter
    def RowsExaminedMin(self, RowsExaminedMin):
        self._RowsExaminedMin = RowsExaminedMin

    @property
    def QueryTime(self):
        """总耗时，单位秒
        :rtype: float
        """
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def QueryTimeMax(self):
        """最大执行时间，单位秒
        :rtype: float
        """
        return self._QueryTimeMax

    @QueryTimeMax.setter
    def QueryTimeMax(self, QueryTimeMax):
        self._QueryTimeMax = QueryTimeMax

    @property
    def QueryTimeMin(self):
        """最小执行时间，单位秒
        :rtype: float
        """
        return self._QueryTimeMin

    @QueryTimeMin.setter
    def QueryTimeMin(self, QueryTimeMin):
        self._QueryTimeMin = QueryTimeMin

    @property
    def RowsSent(self):
        """总返回行数
        :rtype: int
        """
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def RowsSentMax(self):
        """最大返回行数
        :rtype: int
        """
        return self._RowsSentMax

    @RowsSentMax.setter
    def RowsSentMax(self, RowsSentMax):
        self._RowsSentMax = RowsSentMax

    @property
    def RowsSentMin(self):
        """最小返回行数
        :rtype: int
        """
        return self._RowsSentMin

    @RowsSentMin.setter
    def RowsSentMin(self, RowsSentMin):
        self._RowsSentMin = RowsSentMin

    @property
    def ExecTimes(self):
        """执行次数
        :rtype: int
        """
        return self._ExecTimes

    @ExecTimes.setter
    def ExecTimes(self, ExecTimes):
        self._ExecTimes = ExecTimes

    @property
    def SqlTemplate(self):
        """sql模板
        :rtype: str
        """
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def SqlText(self):
        """带参数SQL（随机）
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        """数据库名
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def QueryTimeRatio(self):
        """总耗时占比，单位%
        :rtype: float
        """
        return self._QueryTimeRatio

    @QueryTimeRatio.setter
    def QueryTimeRatio(self, QueryTimeRatio):
        self._QueryTimeRatio = QueryTimeRatio

    @property
    def LockTimeRatio(self):
        """sql总锁等待时间占比，单位%
        :rtype: float
        """
        return self._LockTimeRatio

    @LockTimeRatio.setter
    def LockTimeRatio(self, LockTimeRatio):
        self._LockTimeRatio = LockTimeRatio

    @property
    def RowsExaminedRatio(self):
        """总扫描行数占比，单位%
        :rtype: float
        """
        return self._RowsExaminedRatio

    @RowsExaminedRatio.setter
    def RowsExaminedRatio(self, RowsExaminedRatio):
        self._RowsExaminedRatio = RowsExaminedRatio

    @property
    def RowsSentRatio(self):
        """总返回行数占比，单位%
        :rtype: float
        """
        return self._RowsSentRatio

    @RowsSentRatio.setter
    def RowsSentRatio(self, RowsSentRatio):
        self._RowsSentRatio = RowsSentRatio

    @property
    def QueryTimeAvg(self):
        """平均执行时间，单位秒
        :rtype: float
        """
        return self._QueryTimeAvg

    @QueryTimeAvg.setter
    def QueryTimeAvg(self, QueryTimeAvg):
        self._QueryTimeAvg = QueryTimeAvg

    @property
    def RowsSentAvg(self):
        """平均返回行数
        :rtype: float
        """
        return self._RowsSentAvg

    @RowsSentAvg.setter
    def RowsSentAvg(self, RowsSentAvg):
        self._RowsSentAvg = RowsSentAvg

    @property
    def LockTimeAvg(self):
        """平均锁等待时间，单位秒
        :rtype: float
        """
        return self._LockTimeAvg

    @LockTimeAvg.setter
    def LockTimeAvg(self, LockTimeAvg):
        self._LockTimeAvg = LockTimeAvg

    @property
    def RowsExaminedAvg(self):
        """平均扫描行数
        :rtype: float
        """
        return self._RowsExaminedAvg

    @RowsExaminedAvg.setter
    def RowsExaminedAvg(self, RowsExaminedAvg):
        self._RowsExaminedAvg = RowsExaminedAvg

    @property
    def Md5(self):
        """SQL模板的MD5值
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._LockTime = params.get("LockTime")
        self._LockTimeMax = params.get("LockTimeMax")
        self._LockTimeMin = params.get("LockTimeMin")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsExaminedMax = params.get("RowsExaminedMax")
        self._RowsExaminedMin = params.get("RowsExaminedMin")
        self._QueryTime = params.get("QueryTime")
        self._QueryTimeMax = params.get("QueryTimeMax")
        self._QueryTimeMin = params.get("QueryTimeMin")
        self._RowsSent = params.get("RowsSent")
        self._RowsSentMax = params.get("RowsSentMax")
        self._RowsSentMin = params.get("RowsSentMin")
        self._ExecTimes = params.get("ExecTimes")
        self._SqlTemplate = params.get("SqlTemplate")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._QueryTimeRatio = params.get("QueryTimeRatio")
        self._LockTimeRatio = params.get("LockTimeRatio")
        self._RowsExaminedRatio = params.get("RowsExaminedRatio")
        self._RowsSentRatio = params.get("RowsSentRatio")
        self._QueryTimeAvg = params.get("QueryTimeAvg")
        self._RowsSentAvg = params.get("RowsSentAvg")
        self._LockTimeAvg = params.get("LockTimeAvg")
        self._RowsExaminedAvg = params.get("RowsExaminedAvg")
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogUser(AbstractModel):
    """慢日志来源用户详情。

    """

    def __init__(self):
        r"""
        :param _UserName: 来源用户名。
        :type UserName: str
        :param _Ratio: 该来源用户名的慢日志数目占总数目的比例，单位%。
        :type Ratio: float
        :param _Count: 该来源用户名的慢日志数目。
        :type Count: int
        """
        self._UserName = None
        self._Ratio = None
        self._Count = None

    @property
    def UserName(self):
        """来源用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Ratio(self):
        """该来源用户名的慢日志数目占总数目的比例，单位%。
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Count(self):
        """该来源用户名的慢日志数目。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Ratio = params.get("Ratio")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SqlCostDistribution(AbstractModel):
    """分段耗时 SQL 分布

    """

    def __init__(self):
        r"""
        :param _Count: sql条数。
        :type Count: int
        :param _From: 分段耗时下边界，单位是秒。
        :type From: float
        :param _To: 分段耗时上边界，单位是秒。
        :type To: float
        :param _Ratio: 耗时占比。
        :type Ratio: float
        """
        self._Count = None
        self._From = None
        self._To = None
        self._Ratio = None

    @property
    def Count(self):
        """sql条数。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def From(self):
        """分段耗时下边界，单位是秒。
        :rtype: float
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """分段耗时上边界，单位是秒。
        :rtype: float
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Ratio(self):
        """耗时占比。
        :rtype: float
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatDimension(AbstractModel):
    """会话统计的维度信息,可以多个维度

    """

    def __init__(self):
        r"""
        :param _Dimension: 维度名称，目前仅支持：SqlTag。
        :type Dimension: str
        :param _Data: SQL 标签过滤与统计信息
示例：

示例 1：[p=position] 统计包含 p=position 标签的 SQL 会话。
示例 2：[p] 统计包含 p 标签的 SQL 会话。
示例 3：[p=position, c=idCard] 统计同时包含 p=position 标签和 c=idCard 标签的 SQL 会话。
        :type Data: list of str
        """
        self._Dimension = None
        self._Data = None

    @property
    def Dimension(self):
        """维度名称，目前仅支持：SqlTag。
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def Data(self):
        """SQL 标签过滤与统计信息
示例：

示例 1：[p=position] 统计包含 p=position 标签的 SQL 会话。
示例 2：[p] 统计包含 p 标签的 SQL 会话。
示例 3：[p=position, c=idCard] 统计同时包含 p=position 标签和 c=idCard 标签的 SQL 会话。
        :rtype: list of str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Dimension = params.get("Dimension")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticDataInfo(AbstractModel):
    """统计分析维度下的统计数据详情

    """

    def __init__(self):
        r"""
        :param _Name: 统计维度的值。
        :type Name: str
        :param _TimeAvg: 平均时间。
        :type TimeAvg: float
        :param _TimeSum: 总时间。
        :type TimeSum: float
        :param _Count: 数量。
        :type Count: int
        """
        self._Name = None
        self._TimeAvg = None
        self._TimeSum = None
        self._Count = None

    @property
    def Name(self):
        """统计维度的值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TimeAvg(self):
        """平均时间。
        :rtype: float
        """
        return self._TimeAvg

    @TimeAvg.setter
    def TimeAvg(self, TimeAvg):
        self._TimeAvg = TimeAvg

    @property
    def TimeSum(self):
        """总时间。
        :rtype: float
        """
        return self._TimeSum

    @TimeSum.setter
    def TimeSum(self, TimeSum):
        self._TimeSum = TimeSum

    @property
    def Count(self):
        """数量。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TimeAvg = params.get("TimeAvg")
        self._TimeSum = params.get("TimeSum")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticInfo(AbstractModel):
    """sql会话统计信息

    """

    def __init__(self):
        r"""
        :param _Dimension: 统计分析的维度。
        :type Dimension: str
        :param _Data: 统计分析的维度下的统计数据详情。
        :type Data: list of StatisticDataInfo
        """
        self._Dimension = None
        self._Data = None

    @property
    def Dimension(self):
        """统计分析的维度。
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def Data(self):
        """统计分析的维度下的统计数据详情。
        :rtype: list of StatisticDataInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Dimension = params.get("Dimension")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = StatisticDataInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """表结构。

    """

    def __init__(self):
        r"""
        :param _TableSchema: 库名。
        :type TableSchema: str
        :param _TableName: 表名。
        :type TableName: str
        :param _Engine: 库表的存储引擎。
        :type Engine: str
        :param _TableRows: 行数。
        :type TableRows: int
        :param _TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        """
        self._TableSchema = None
        self._TableName = None
        self._Engine = None
        self._TableRows = None
        self._TotalLength = None

    @property
    def TableSchema(self):
        """库名。
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def TableName(self):
        """表名。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Engine(self):
        """库表的存储引擎。
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def TableRows(self):
        """行数。
        :rtype: int
        """
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def TotalLength(self):
        """总使用空间（MB）。
        :rtype: float
        """
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        self._TableName = params.get("TableName")
        self._Engine = params.get("Engine")
        self._TableRows = params.get("TableRows")
        self._TotalLength = params.get("TotalLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceData(AbstractModel):
    """库表空间统计数据。

    """

    def __init__(self):
        r"""
        :param _TableName: 表名。
        :type TableName: str
        :param _TableSchema: 库名。
        :type TableSchema: str
        :param _Engine: 库表的存储引擎。
        :type Engine: str
        :param _DataLength: 数据空间（MB）。
        :type DataLength: float
        :param _IndexLength: 索引空间（MB）。
        :type IndexLength: float
        :param _DataFree: 碎片空间（MB）。
        :type DataFree: float
        :param _TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        :param _FragRatio: 碎片率（%）。
        :type FragRatio: float
        :param _TableRows: 行数。
        :type TableRows: int
        :param _PhysicalFileSize: 表对应的独立物理文件大小（MB）。
        :type PhysicalFileSize: float
        """
        self._TableName = None
        self._TableSchema = None
        self._Engine = None
        self._DataLength = None
        self._IndexLength = None
        self._DataFree = None
        self._TotalLength = None
        self._FragRatio = None
        self._TableRows = None
        self._PhysicalFileSize = None

    @property
    def TableName(self):
        """表名。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableSchema(self):
        """库名。
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def Engine(self):
        """库表的存储引擎。
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def DataLength(self):
        """数据空间（MB）。
        :rtype: float
        """
        return self._DataLength

    @DataLength.setter
    def DataLength(self, DataLength):
        self._DataLength = DataLength

    @property
    def IndexLength(self):
        """索引空间（MB）。
        :rtype: float
        """
        return self._IndexLength

    @IndexLength.setter
    def IndexLength(self, IndexLength):
        self._IndexLength = IndexLength

    @property
    def DataFree(self):
        """碎片空间（MB）。
        :rtype: float
        """
        return self._DataFree

    @DataFree.setter
    def DataFree(self, DataFree):
        self._DataFree = DataFree

    @property
    def TotalLength(self):
        """总使用空间（MB）。
        :rtype: float
        """
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength

    @property
    def FragRatio(self):
        """碎片率（%）。
        :rtype: float
        """
        return self._FragRatio

    @FragRatio.setter
    def FragRatio(self, FragRatio):
        self._FragRatio = FragRatio

    @property
    def TableRows(self):
        """行数。
        :rtype: int
        """
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def PhysicalFileSize(self):
        """表对应的独立物理文件大小（MB）。
        :rtype: float
        """
        return self._PhysicalFileSize

    @PhysicalFileSize.setter
    def PhysicalFileSize(self, PhysicalFileSize):
        self._PhysicalFileSize = PhysicalFileSize


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableSchema = params.get("TableSchema")
        self._Engine = params.get("Engine")
        self._DataLength = params.get("DataLength")
        self._IndexLength = params.get("IndexLength")
        self._DataFree = params.get("DataFree")
        self._TotalLength = params.get("TotalLength")
        self._FragRatio = params.get("FragRatio")
        self._TableRows = params.get("TableRows")
        self._PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceTimeSeries(AbstractModel):
    """库表空间时序数据

    """

    def __init__(self):
        r"""
        :param _TableName: 表名。
        :type TableName: str
        :param _TableSchema: 库名。
        :type TableSchema: str
        :param _Engine: 库表的存储引擎。
        :type Engine: str
        :param _SeriesData: 单位时间间隔内的空间指标数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorFloatMetricSeriesData`
        """
        self._TableName = None
        self._TableSchema = None
        self._Engine = None
        self._SeriesData = None

    @property
    def TableName(self):
        """表名。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableSchema(self):
        """库名。
        :rtype: str
        """
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def Engine(self):
        """库表的存储引擎。
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def SeriesData(self):
        """单位时间间隔内的空间指标数据。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.MonitorFloatMetricSeriesData`
        """
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableSchema = params.get("TableSchema")
        self._Engine = params.get("Engine")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorFloatMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """展示 redis kill 会话任务状态。

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务 ID。
        :type AsyncRequestId: int
        :param _InstProxyList: 当前实例所有 proxy 列表。
        :type InstProxyList: list of str
        :param _InstProxyCount: 当前实例所有 proxy 数量。
        :type InstProxyCount: int
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _StartTime: 任务启动时间。
        :type StartTime: str
        :param _TaskStatus: 任务的状态，支持的取值包括："created" - 新建；"chosen" - 待执行； "running" - 执行中；"failed" - 失败；"finished" - 已完成。
        :type TaskStatus: str
        :param _FinishedProxyList: 完成 kill 任务的 proxyId。
        :type FinishedProxyList: list of str
        :param _FailedProxyList: kill 任务实行失败的 proxyId。
        :type FailedProxyList: list of str
        :param _EndTime: 任务结束时间。
        :type EndTime: str
        :param _Progress: 任务执行进度。
        :type Progress: int
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._AsyncRequestId = None
        self._InstProxyList = None
        self._InstProxyCount = None
        self._CreateTime = None
        self._StartTime = None
        self._TaskStatus = None
        self._FinishedProxyList = None
        self._FailedProxyList = None
        self._EndTime = None
        self._Progress = None
        self._InstanceId = None

    @property
    def AsyncRequestId(self):
        """异步任务 ID。
        :rtype: int
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def InstProxyList(self):
        """当前实例所有 proxy 列表。
        :rtype: list of str
        """
        return self._InstProxyList

    @InstProxyList.setter
    def InstProxyList(self, InstProxyList):
        self._InstProxyList = InstProxyList

    @property
    def InstProxyCount(self):
        """当前实例所有 proxy 数量。
        :rtype: int
        """
        return self._InstProxyCount

    @InstProxyCount.setter
    def InstProxyCount(self, InstProxyCount):
        self._InstProxyCount = InstProxyCount

    @property
    def CreateTime(self):
        """任务创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """任务启动时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskStatus(self):
        """任务的状态，支持的取值包括："created" - 新建；"chosen" - 待执行； "running" - 执行中；"failed" - 失败；"finished" - 已完成。
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def FinishedProxyList(self):
        """完成 kill 任务的 proxyId。
        :rtype: list of str
        """
        return self._FinishedProxyList

    @FinishedProxyList.setter
    def FinishedProxyList(self, FinishedProxyList):
        self._FinishedProxyList = FinishedProxyList

    @property
    def FailedProxyList(self):
        """kill 任务实行失败的 proxyId。
        :rtype: list of str
        """
        return self._FailedProxyList

    @FailedProxyList.setter
    def FailedProxyList(self, FailedProxyList):
        self._FailedProxyList = FailedProxyList

    @property
    def EndTime(self):
        """任务结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Progress(self):
        """任务执行进度。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def InstanceId(self):
        """实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._InstProxyList = params.get("InstProxyList")
        self._InstProxyCount = params.get("InstProxyCount")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._TaskStatus = params.get("TaskStatus")
        self._FinishedProxyList = params.get("FinishedProxyList")
        self._FailedProxyList = params.get("FailedProxyList")
        self._EndTime = params.get("EndTime")
        self._Progress = params.get("Progress")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateInfo(AbstractModel):
    """通知模板

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
        :type TemplateId: str
        :param _TemplateName: 模板名
        :type TemplateName: str
        """
        self._TemplateId = None
        self._TemplateName = None

    @property
    def TemplateId(self):
        """模板id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """模板名
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeSlice(AbstractModel):
    """单位时间间隔内的慢日志统计

    """

    def __init__(self):
        r"""
        :param _Count: 总数
        :type Count: int
        :param _Timestamp: 统计开始时间
        :type Timestamp: int
        """
        self._Count = None
        self._Timestamp = None

    @property
    def Count(self):
        """总数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Timestamp(self):
        """统计开始时间
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopHotKeys(AbstractModel):
    """热key分析返回信息

    """

    def __init__(self):
        r"""
        :param _Count: 访问频次。
        :type Count: int
        :param _Db: 热Key所属数据库。
        :type Db: str
        :param _InstanceNodeId: Redis节点。
        :type InstanceNodeId: str
        :param _Key: 热Key。
        :type Key: str
        :param _Type: 数据类型。
        :type Type: str
        """
        self._Count = None
        self._Db = None
        self._InstanceNodeId = None
        self._Key = None
        self._Type = None

    @property
    def Count(self):
        """访问频次。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Db(self):
        """热Key所属数据库。
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def InstanceNodeId(self):
        """Redis节点。
        :rtype: str
        """
        return self._InstanceNodeId

    @InstanceNodeId.setter
    def InstanceNodeId(self, InstanceNodeId):
        self._InstanceNodeId = InstanceNodeId

    @property
    def Key(self):
        """热Key。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        """数据类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Db = params.get("Db")
        self._InstanceNodeId = params.get("InstanceNodeId")
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAgentSwitchRequest(AbstractModel):
    """UpdateAgentSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent标识。
        :type AgentId: str
        :param _Switch: 停止或重连Agent，支持值包括："on" - 重连Agent， "off" - 停止Agent。
        :type Switch: str
        :param _Product: 服务产品类型，仅支持 "dbbrain-mysql" - 自建MySQL。
        :type Product: str
        """
        self._AgentId = None
        self._Switch = None
        self._Product = None

    @property
    def AgentId(self):
        """Agent标识。
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Switch(self):
        """停止或重连Agent，支持值包括："on" - 重连Agent， "off" - 停止Agent。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Product(self):
        """服务产品类型，仅支持 "dbbrain-mysql" - 自建MySQL。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._Switch = params.get("Switch")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAgentSwitchResponse(AbstractModel):
    """UpdateAgentSwitch返回参数结构体

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


class UpdateMonitorSwitchRequest(AbstractModel):
    """UpdateMonitorSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Switch: 停止或重连Agent实例，支持值包括："on" - 重连实例， "off" - 停止实例。
        :type Switch: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Product: 服务产品类型，仅支持 "dbbrain-mysql" - 自建MySQL。
        :type Product: str
        """
        self._Switch = None
        self._InstanceId = None
        self._Product = None

    @property
    def Switch(self):
        """停止或重连Agent实例，支持值包括："on" - 重连实例， "off" - 停止实例。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Product(self):
        """服务产品类型，仅支持 "dbbrain-mysql" - 自建MySQL。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._InstanceId = params.get("InstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateMonitorSwitchResponse(AbstractModel):
    """UpdateMonitorSwitch返回参数结构体

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


class UserProfile(AbstractModel):
    """用户配置的相关信息，包括邮件配置。

    """

    def __init__(self):
        r"""
        :param _ProfileId: 配置的id。
        :type ProfileId: str
        :param _ProfileType: 配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :type ProfileType: str
        :param _ProfileLevel: 配置级别，支持值包括："User" - 用户级别，"Instance" - 实例级别，其中数据库巡检邮件配置为用户级别，定期生成邮件配置为实例级别。
        :type ProfileLevel: str
        :param _ProfileName: 配置名称。
        :type ProfileName: str
        :param _ProfileInfo: 配置详情。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        """
        self._ProfileId = None
        self._ProfileType = None
        self._ProfileLevel = None
        self._ProfileName = None
        self._ProfileInfo = None

    @property
    def ProfileId(self):
        """配置的id。
        :rtype: str
        """
        return self._ProfileId

    @ProfileId.setter
    def ProfileId(self, ProfileId):
        self._ProfileId = ProfileId

    @property
    def ProfileType(self):
        """配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :rtype: str
        """
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def ProfileLevel(self):
        """配置级别，支持值包括："User" - 用户级别，"Instance" - 实例级别，其中数据库巡检邮件配置为用户级别，定期生成邮件配置为实例级别。
        :rtype: str
        """
        return self._ProfileLevel

    @ProfileLevel.setter
    def ProfileLevel(self, ProfileLevel):
        self._ProfileLevel = ProfileLevel

    @property
    def ProfileName(self):
        """配置名称。
        :rtype: str
        """
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileInfo(self):
        """配置详情。
        :rtype: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        """
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo


    def _deserialize(self, params):
        self._ProfileId = params.get("ProfileId")
        self._ProfileType = params.get("ProfileType")
        self._ProfileLevel = params.get("ProfileLevel")
        self._ProfileName = params.get("ProfileName")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyUserAccountRequest(AbstractModel):
    """VerifyUserAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _User: 数据库账号名。
        :type User: str
        :param _Password: 数据库账号密码。
        :type Password: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._User = None
        self._Password = None
        self._Product = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """数据库账号名。
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """数据库账号密码。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Product(self):
        """服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyUserAccountResponse(AbstractModel):
    """VerifyUserAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionToken: 会话token，有效期为5分钟。
        :type SessionToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionToken = None
        self._RequestId = None

    @property
    def SessionToken(self):
        """会话token，有效期为5分钟。
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

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
        self._SessionToken = params.get("SessionToken")
        self._RequestId = params.get("RequestId")