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

from tencentcloud.common.abstract_model import AbstractModel


class BindingPolicyObjectDimension(AbstractModel):
    """策略绑定实例维度信息

    """

    def __init__(self):
        """
        :param Region: 地域名
        :type Region: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param Dimensions: 维度信息
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


class BindingPolicyObjectRequest(AbstractModel):
    """BindingPolicyObject请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 策略分组Id
        :type GroupId: int
        :param Module: 必填。固定值"monitor"
        :type Module: str
        :param InstanceGroupId: 实例分组ID
        :type InstanceGroupId: int
        :param Dimensions: 需要绑定的对象维度信息
        :type Dimensions: list of BindingPolicyObjectDimension
        """
        self.GroupId = None
        self.Module = None
        self.InstanceGroupId = None
        self.Dimensions = None


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
        :param EventConditions: 策略组中的时间告警规则
        :type EventConditions: list of CreatePolicyGroupEventCondition
        :param BackEndCall: 是否为后端调用。当且仅当值为1时，后台拉取策略模版中的规则填充入Conditions以及EventConditions字段
        :type BackEndCall: int
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
        :param Limit: 每页返回的数量，默认20
        :type Limit: int
        :param Offset: 页偏移量，默认0
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


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 业务命名空间
        :type Namespace: str
        :param MetricName: 指标名
        :type MetricName: str
        """
        self.Namespace = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")


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


class DescribeBindingPolicyObjectListRequest(AbstractModel):
    """DescribeBindingPolicyObjectList请求参数结构体

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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.NoShieldedSum = None
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
        self.RequestId = params.get("RequestId")


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
        :type CalcType: int
        :param CalcValue: 检测阈值
        :type CalcValue: str
        :param ContinueTime: 持续多长时间触发规则会告警(单位秒)
        :type ContinueTime: int
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
        """
        self.GroupId = None
        self.GroupName = None
        self.ViewName = None
        self.Remark = None
        self.LastEditUin = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ViewName = params.get("ViewName")
        self.Remark = params.get("Remark")
        self.LastEditUin = params.get("LastEditUin")


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
        self.RequestId = params.get("RequestId")


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
        :param InstanceId: 影响对象，比如ins-19708ino
        :type InstanceId: list of str
        :param Dimensions: 维度过滤，比如外网IP:10.0.0.1
        :type Dimensions: list of DescribeProductEventListDimensions
        :param RegionList: 地域过滤，比如gz
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


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间，每个云产品会有一个命名空间
        :type Namespace: str
        :param MetricName: 指标名称，各个云产品的详细指标说明请参阅各个产品[监控接口](https://cloud.tencent.com/document/product/248/30384)文档
        :type MetricName: str
        :param Instances: 实例对象的维度组合
        :type Instances: list of Instance
        :param Period: 监控统计周期。默认为取值为300，单位为s
        :type Period: int
        :param StartTime: 起始时间，如2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param EndTime: 结束时间，默认为当前时间。 EndTime不能小于StartTime
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
        :type ReceiverType: list of str
        :param Id: Id
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


class UnBindingAllPolicyObjectRequest(AbstractModel):
    """UnBindingAllPolicyObject请求参数结构体

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


class UnBindingPolicyObjectRequest(AbstractModel):
    """UnBindingPolicyObject请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 固定值，为"monitor"
        :type Module: str
        :param GroupId: 策略组id
        :type GroupId: int
        :param UniqueId: 待删除对象实例的唯一id列表
        :type UniqueId: list of str
        """
        self.Module = None
        self.GroupId = None
        self.UniqueId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.UniqueId = params.get("UniqueId")


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