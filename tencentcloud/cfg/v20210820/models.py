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


class ActionFieldConfigDetail(AbstractModel):
    """动作动态参数返回格式

    """

    def __init__(self):
        r"""
        :param _Type: 组件类型
可选项如下：
input  文本框
textarea  多行文本框
number  数值输入框
select   选择器
cascader  级联选择器
radio  单选
time   时间选择
        :type Type: str
        :param _Lable: 组件label
        :type Lable: str
        :param _Field: 组件唯一标识， 传回后端时的key
        :type Field: str
        :param _DefaultValue: 默认值
        :type DefaultValue: str
        :param _Config: 支持配置项如下,可根据需要选择配置项，不需要配置是设置空{}：

{

  placeholder: string (占位符)

  tooltip: string (提示信息)

  reg: RegExp (对输入内容格式进行正则校验的规则)

  max: number (对于输入框，限制最大输入字符数，对于数值输入框，设置上限)

  min: number (对于数值输入框，设置下限)

  step: number (设置数值输入框的步长，默认为1)

  format: string (时间选择的格式，如YYYY-MM-DD表示年月日, YYYY-MM-DD HH:mm:ss 表示时分秒)

  separator:  string[] (多行输入框的分隔符，不传或者为空时表示不分隔，直接返回用户输入的文本字符串)

  multiple: boolean (是否多选,对选择器和级联选择器有效)

  options:  选择器的选项【支持以下两种形式】

直接给定选项数组  { value: string; label: string }[]
通过调接口获取选项                                                                                                                                       { api: string(接口地址),                                                                                                                                       params: string[] (接口参数,对应于参数配置的field，前端根据field对应的所有组件的输入值作为参数查询数据， 为空时在组件加载时直接请求数据)                                                                                                    }
}
        :type Config: str
        :param _Required: 是否必填 (0 -- 否   1-- 是)
        :type Required: int
        :param _Validate: compute配置依赖的其他field满足的条件时通过校验（如：三个表单项中必须至少有一个填写了）

[fieldName,

{ config:  此项保留，等待后面具体场景细化  }

]
        :type Validate: str
        :param _Visible: 是否可见
        :type Visible: str
        """
        self._Type = None
        self._Lable = None
        self._Field = None
        self._DefaultValue = None
        self._Config = None
        self._Required = None
        self._Validate = None
        self._Visible = None

    @property
    def Type(self):
        """组件类型
可选项如下：
input  文本框
textarea  多行文本框
number  数值输入框
select   选择器
cascader  级联选择器
radio  单选
time   时间选择
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Lable(self):
        """组件label
        :rtype: str
        """
        return self._Lable

    @Lable.setter
    def Lable(self, Lable):
        self._Lable = Lable

    @property
    def Field(self):
        """组件唯一标识， 传回后端时的key
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def DefaultValue(self):
        """默认值
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Config(self):
        """支持配置项如下,可根据需要选择配置项，不需要配置是设置空{}：

{

  placeholder: string (占位符)

  tooltip: string (提示信息)

  reg: RegExp (对输入内容格式进行正则校验的规则)

  max: number (对于输入框，限制最大输入字符数，对于数值输入框，设置上限)

  min: number (对于数值输入框，设置下限)

  step: number (设置数值输入框的步长，默认为1)

  format: string (时间选择的格式，如YYYY-MM-DD表示年月日, YYYY-MM-DD HH:mm:ss 表示时分秒)

  separator:  string[] (多行输入框的分隔符，不传或者为空时表示不分隔，直接返回用户输入的文本字符串)

  multiple: boolean (是否多选,对选择器和级联选择器有效)

  options:  选择器的选项【支持以下两种形式】

直接给定选项数组  { value: string; label: string }[]
通过调接口获取选项                                                                                                                                       { api: string(接口地址),                                                                                                                                       params: string[] (接口参数,对应于参数配置的field，前端根据field对应的所有组件的输入值作为参数查询数据， 为空时在组件加载时直接请求数据)                                                                                                    }
}
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Required(self):
        """是否必填 (0 -- 否   1-- 是)
        :rtype: int
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def Validate(self):
        """compute配置依赖的其他field满足的条件时通过校验（如：三个表单项中必须至少有一个填写了）

[fieldName,

{ config:  此项保留，等待后面具体场景细化  }

]
        :rtype: str
        """
        return self._Validate

    @Validate.setter
    def Validate(self, Validate):
        self._Validate = Validate

    @property
    def Visible(self):
        """是否可见
        :rtype: str
        """
        return self._Visible

    @Visible.setter
    def Visible(self, Visible):
        self._Visible = Visible


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Lable = params.get("Lable")
        self._Field = params.get("Field")
        self._DefaultValue = params.get("DefaultValue")
        self._Config = params.get("Config")
        self._Required = params.get("Required")
        self._Validate = params.get("Validate")
        self._Visible = params.get("Visible")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionFieldConfigResult(AbstractModel):
    """动作栏位配置结果

    """

    def __init__(self):
        r"""
        :param _ActionId: 动作ID
        :type ActionId: int
        :param _ActionName: 动作名称
        :type ActionName: str
        :param _ConfigDetail: 动作对应的栏位配置详情
        :type ConfigDetail: list of ActionFieldConfigDetail
        """
        self._ActionId = None
        self._ActionName = None
        self._ConfigDetail = None

    @property
    def ActionId(self):
        """动作ID
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def ActionName(self):
        """动作名称
        :rtype: str
        """
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def ConfigDetail(self):
        """动作对应的栏位配置详情
        :rtype: list of ActionFieldConfigDetail
        """
        return self._ConfigDetail

    @ConfigDetail.setter
    def ConfigDetail(self, ConfigDetail):
        self._ConfigDetail = ConfigDetail


    def _deserialize(self, params):
        self._ActionId = params.get("ActionId")
        self._ActionName = params.get("ActionName")
        if params.get("ConfigDetail") is not None:
            self._ConfigDetail = []
            for item in params.get("ConfigDetail"):
                obj = ActionFieldConfigDetail()
                obj._deserialize(item)
                self._ConfigDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionFilter(AbstractModel):
    """动作库筛选栏位

    """

    def __init__(self):
        r"""
        :param _Keyword: 关键字
        :type Keyword: str
        :param _Values: 搜索内容值
        :type Values: list of str
        """
        self._Keyword = None
        self._Values = None

    @property
    def Keyword(self):
        """关键字
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Values(self):
        """搜索内容值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionLibraryListResult(AbstractModel):
    """动作库数据列表

    """

    def __init__(self):
        r"""
        :param _ActionName: 动作名称
        :type ActionName: str
        :param _Desc: 动作描述
        :type Desc: str
        :param _ActionType: 动作类型。范围：["平台","自定义"]
        :type ActionType: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Creator: 创建人
        :type Creator: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _RiskDesc: 动作风险描述
        :type RiskDesc: str
        :param _ActionId: 动作ID
        :type ActionId: int
        :param _AttributeId: 动作属性（ 1：故障  2：恢复）
        :type AttributeId: int
        :param _RelationActionId: 关联的动作ID
        :type RelationActionId: int
        :param _ActionCommand: 操作命令
        :type ActionCommand: str
        :param _ActionCommandType: 动作类型（0 -- tat   1 -- 云API）
        :type ActionCommandType: int
        :param _ActionContent: 自定义动作的参数，json string
        :type ActionContent: str
        :param _ResourceType: 二级分类
        :type ResourceType: str
        :param _ActionDetail: 动作描述
        :type ActionDetail: str
        :param _IsAllowed: 是否允许当前账号使用
        :type IsAllowed: bool
        :param _ActionBestCase: 最佳实践案例的链接地址
        :type ActionBestCase: str
        :param _ObjectType: 对象类型
        :type ObjectType: str
        :param _MetricIdList: 监控指标ID列表
        :type MetricIdList: list of int non-negative
        :param _IsNewAction: 是否是新动作
        :type IsNewAction: bool
        :param _ObjectTypeId: 对象类型ID
        :type ObjectTypeId: int
        """
        self._ActionName = None
        self._Desc = None
        self._ActionType = None
        self._CreateTime = None
        self._Creator = None
        self._UpdateTime = None
        self._RiskDesc = None
        self._ActionId = None
        self._AttributeId = None
        self._RelationActionId = None
        self._ActionCommand = None
        self._ActionCommandType = None
        self._ActionContent = None
        self._ResourceType = None
        self._ActionDetail = None
        self._IsAllowed = None
        self._ActionBestCase = None
        self._ObjectType = None
        self._MetricIdList = None
        self._IsNewAction = None
        self._ObjectTypeId = None

    @property
    def ActionName(self):
        """动作名称
        :rtype: str
        """
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def Desc(self):
        """动作描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ActionType(self):
        """动作类型。范围：["平台","自定义"]
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

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
    def Creator(self):
        """创建人
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

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
    def RiskDesc(self):
        """动作风险描述
        :rtype: str
        """
        return self._RiskDesc

    @RiskDesc.setter
    def RiskDesc(self, RiskDesc):
        self._RiskDesc = RiskDesc

    @property
    def ActionId(self):
        """动作ID
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def AttributeId(self):
        """动作属性（ 1：故障  2：恢复）
        :rtype: int
        """
        return self._AttributeId

    @AttributeId.setter
    def AttributeId(self, AttributeId):
        self._AttributeId = AttributeId

    @property
    def RelationActionId(self):
        """关联的动作ID
        :rtype: int
        """
        return self._RelationActionId

    @RelationActionId.setter
    def RelationActionId(self, RelationActionId):
        self._RelationActionId = RelationActionId

    @property
    def ActionCommand(self):
        """操作命令
        :rtype: str
        """
        return self._ActionCommand

    @ActionCommand.setter
    def ActionCommand(self, ActionCommand):
        self._ActionCommand = ActionCommand

    @property
    def ActionCommandType(self):
        """动作类型（0 -- tat   1 -- 云API）
        :rtype: int
        """
        return self._ActionCommandType

    @ActionCommandType.setter
    def ActionCommandType(self, ActionCommandType):
        self._ActionCommandType = ActionCommandType

    @property
    def ActionContent(self):
        """自定义动作的参数，json string
        :rtype: str
        """
        return self._ActionContent

    @ActionContent.setter
    def ActionContent(self, ActionContent):
        self._ActionContent = ActionContent

    @property
    def ResourceType(self):
        """二级分类
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ActionDetail(self):
        """动作描述
        :rtype: str
        """
        return self._ActionDetail

    @ActionDetail.setter
    def ActionDetail(self, ActionDetail):
        self._ActionDetail = ActionDetail

    @property
    def IsAllowed(self):
        """是否允许当前账号使用
        :rtype: bool
        """
        return self._IsAllowed

    @IsAllowed.setter
    def IsAllowed(self, IsAllowed):
        self._IsAllowed = IsAllowed

    @property
    def ActionBestCase(self):
        """最佳实践案例的链接地址
        :rtype: str
        """
        return self._ActionBestCase

    @ActionBestCase.setter
    def ActionBestCase(self, ActionBestCase):
        self._ActionBestCase = ActionBestCase

    @property
    def ObjectType(self):
        """对象类型
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def MetricIdList(self):
        """监控指标ID列表
        :rtype: list of int non-negative
        """
        return self._MetricIdList

    @MetricIdList.setter
    def MetricIdList(self, MetricIdList):
        self._MetricIdList = MetricIdList

    @property
    def IsNewAction(self):
        """是否是新动作
        :rtype: bool
        """
        return self._IsNewAction

    @IsNewAction.setter
    def IsNewAction(self, IsNewAction):
        self._IsNewAction = IsNewAction

    @property
    def ObjectTypeId(self):
        """对象类型ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId


    def _deserialize(self, params):
        self._ActionName = params.get("ActionName")
        self._Desc = params.get("Desc")
        self._ActionType = params.get("ActionType")
        self._CreateTime = params.get("CreateTime")
        self._Creator = params.get("Creator")
        self._UpdateTime = params.get("UpdateTime")
        self._RiskDesc = params.get("RiskDesc")
        self._ActionId = params.get("ActionId")
        self._AttributeId = params.get("AttributeId")
        self._RelationActionId = params.get("RelationActionId")
        self._ActionCommand = params.get("ActionCommand")
        self._ActionCommandType = params.get("ActionCommandType")
        self._ActionContent = params.get("ActionContent")
        self._ResourceType = params.get("ResourceType")
        self._ActionDetail = params.get("ActionDetail")
        self._IsAllowed = params.get("IsAllowed")
        self._ActionBestCase = params.get("ActionBestCase")
        self._ObjectType = params.get("ObjectType")
        self._MetricIdList = params.get("MetricIdList")
        self._IsNewAction = params.get("IsNewAction")
        self._ObjectTypeId = params.get("ObjectTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmServiceInfo(AbstractModel):
    """应用性能监控产品中应用信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务ID
        :type InstanceId: str
        :param _ServiceNameList: 应用名称
        :type ServiceNameList: list of str
        :param _RegionId: 地域ID
        :type RegionId: int
        """
        self._InstanceId = None
        self._ServiceNameList = None
        self._RegionId = None

    @property
    def InstanceId(self):
        """业务ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceNameList(self):
        """应用名称
        :rtype: list of str
        """
        return self._ServiceNameList

    @ServiceNameList.setter
    def ServiceNameList(self, ServiceNameList):
        self._ServiceNameList = ServiceNameList

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceNameList = params.get("ServiceNameList")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFromActionRequest(AbstractModel):
    """CreateTaskFromAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskActionId: 动作ID，可从动作列表接口DescribeActionLibraryList获取
        :type TaskActionId: int
        :param _TaskInstances: 参与演练的实例ID
        :type TaskInstances: list of str
        :param _TaskTitle: 演练名称，不填则默认取动作名称
        :type TaskTitle: str
        :param _TaskDescription: 演练描述，不填则默认取动作描述
        :type TaskDescription: str
        :param _TaskActionGeneralConfiguration: 动作通用参数，需要json序列化传入，可以从动作详情接口DescribeActionFieldConfigList获取，不填默认使用动作默认参数
        :type TaskActionGeneralConfiguration: str
        :param _TaskActionCustomConfiguration: 动作自定义参数，需要json序列化传入，可以从动作详情接口DescribeActionFieldConfigList获取，不填默认使用动作默认参数，注意：必填参数，是没有默认值的 ，务必保证传入有效值
        :type TaskActionCustomConfiguration: str
        :param _TaskPauseDuration: 演练自动暂停时间，单位分钟, 不填则默认为60
        :type TaskPauseDuration: int
        """
        self._TaskActionId = None
        self._TaskInstances = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskActionGeneralConfiguration = None
        self._TaskActionCustomConfiguration = None
        self._TaskPauseDuration = None

    @property
    def TaskActionId(self):
        """动作ID，可从动作列表接口DescribeActionLibraryList获取
        :rtype: int
        """
        return self._TaskActionId

    @TaskActionId.setter
    def TaskActionId(self, TaskActionId):
        self._TaskActionId = TaskActionId

    @property
    def TaskInstances(self):
        """参与演练的实例ID
        :rtype: list of str
        """
        return self._TaskInstances

    @TaskInstances.setter
    def TaskInstances(self, TaskInstances):
        self._TaskInstances = TaskInstances

    @property
    def TaskTitle(self):
        """演练名称，不填则默认取动作名称
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """演练描述，不填则默认取动作描述
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskActionGeneralConfiguration(self):
        """动作通用参数，需要json序列化传入，可以从动作详情接口DescribeActionFieldConfigList获取，不填默认使用动作默认参数
        :rtype: str
        """
        return self._TaskActionGeneralConfiguration

    @TaskActionGeneralConfiguration.setter
    def TaskActionGeneralConfiguration(self, TaskActionGeneralConfiguration):
        self._TaskActionGeneralConfiguration = TaskActionGeneralConfiguration

    @property
    def TaskActionCustomConfiguration(self):
        """动作自定义参数，需要json序列化传入，可以从动作详情接口DescribeActionFieldConfigList获取，不填默认使用动作默认参数，注意：必填参数，是没有默认值的 ，务必保证传入有效值
        :rtype: str
        """
        return self._TaskActionCustomConfiguration

    @TaskActionCustomConfiguration.setter
    def TaskActionCustomConfiguration(self, TaskActionCustomConfiguration):
        self._TaskActionCustomConfiguration = TaskActionCustomConfiguration

    @property
    def TaskPauseDuration(self):
        """演练自动暂停时间，单位分钟, 不填则默认为60
        :rtype: int
        """
        return self._TaskPauseDuration

    @TaskPauseDuration.setter
    def TaskPauseDuration(self, TaskPauseDuration):
        self._TaskPauseDuration = TaskPauseDuration


    def _deserialize(self, params):
        self._TaskActionId = params.get("TaskActionId")
        self._TaskInstances = params.get("TaskInstances")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskActionGeneralConfiguration = params.get("TaskActionGeneralConfiguration")
        self._TaskActionCustomConfiguration = params.get("TaskActionCustomConfiguration")
        self._TaskPauseDuration = params.get("TaskPauseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFromActionResponse(AbstractModel):
    """CreateTaskFromAction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 创建成功的演练ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """创建成功的演练ID
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


class CreateTaskFromMultiActionRequest(AbstractModel):
    """CreateTaskFromMultiAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInstances: 参与演练的实例ID
CVM ins-xxx
MySQL cdb-xxx
CLB lb-xxx
Redis crs-xxx
NAT网关 nat-xxx
Redis crs-xxx
专线-独享专用通道 dcx-xxx
标准集群普通节点 {"ClusterId":"cls-xxx","InstanceId":"ins-xxx","LanIP":"1.1.1.1"}
标准集群Pod {"ClusterId":"cls-xxx","PodName":"podname","NodeName":"1.1.1.1","NameSpace":"ns","Workload":"workload"}
TDSQL-MySQL(InnoDB) tdsqlshard-xxx
TDSQL-C cynosdbmysql-xxx
VPC子网 subnet-xxxx
CKafka ckafka-xxx
MariaDB tdsql-xxxx
PostgreSQL postgres-xxx
云原生网关 gateway-xxx
标准集群超级节点 {"ClusterId":"cls-xxx","InstanceId":"eklet-xxx","LanIP":"1.1.1.1,"NodePoolId":"np-xxx"}
Serverless集群超级节点 {"ClusterId":"cls-xxxx","InstanceId":"eklet-xxxx","LanIP":"1.1.1.1"}
Elasticsearch集群 es-xxxx
RabbitMQ amqp-xxxx
        :type TaskInstances: list of str
        :param _TaskTitle: 演练名称，不填则默认取动作名称
        :type TaskTitle: str
        :param _TaskDescription: 演练描述，不填则默认取动作描述
        :type TaskDescription: str
        :param _TaskPauseDuration: 演练自动暂停时间，单位分钟, 不填则默认为60
        :type TaskPauseDuration: int
        :param _TaskAction: 演练动作组配置
        :type TaskAction: list of TaskGroupForAction
        """
        self._TaskInstances = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskPauseDuration = None
        self._TaskAction = None

    @property
    def TaskInstances(self):
        """参与演练的实例ID
CVM ins-xxx
MySQL cdb-xxx
CLB lb-xxx
Redis crs-xxx
NAT网关 nat-xxx
Redis crs-xxx
专线-独享专用通道 dcx-xxx
标准集群普通节点 {"ClusterId":"cls-xxx","InstanceId":"ins-xxx","LanIP":"1.1.1.1"}
标准集群Pod {"ClusterId":"cls-xxx","PodName":"podname","NodeName":"1.1.1.1","NameSpace":"ns","Workload":"workload"}
TDSQL-MySQL(InnoDB) tdsqlshard-xxx
TDSQL-C cynosdbmysql-xxx
VPC子网 subnet-xxxx
CKafka ckafka-xxx
MariaDB tdsql-xxxx
PostgreSQL postgres-xxx
云原生网关 gateway-xxx
标准集群超级节点 {"ClusterId":"cls-xxx","InstanceId":"eklet-xxx","LanIP":"1.1.1.1,"NodePoolId":"np-xxx"}
Serverless集群超级节点 {"ClusterId":"cls-xxxx","InstanceId":"eklet-xxxx","LanIP":"1.1.1.1"}
Elasticsearch集群 es-xxxx
RabbitMQ amqp-xxxx
        :rtype: list of str
        """
        return self._TaskInstances

    @TaskInstances.setter
    def TaskInstances(self, TaskInstances):
        self._TaskInstances = TaskInstances

    @property
    def TaskTitle(self):
        """演练名称，不填则默认取动作名称
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """演练描述，不填则默认取动作描述
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskPauseDuration(self):
        """演练自动暂停时间，单位分钟, 不填则默认为60
        :rtype: int
        """
        return self._TaskPauseDuration

    @TaskPauseDuration.setter
    def TaskPauseDuration(self, TaskPauseDuration):
        self._TaskPauseDuration = TaskPauseDuration

    @property
    def TaskAction(self):
        """演练动作组配置
        :rtype: list of TaskGroupForAction
        """
        return self._TaskAction

    @TaskAction.setter
    def TaskAction(self, TaskAction):
        self._TaskAction = TaskAction


    def _deserialize(self, params):
        self._TaskInstances = params.get("TaskInstances")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskPauseDuration = params.get("TaskPauseDuration")
        if params.get("TaskAction") is not None:
            self._TaskAction = []
            for item in params.get("TaskAction"):
                obj = TaskGroupForAction()
                obj._deserialize(item)
                self._TaskAction.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFromMultiActionResponse(AbstractModel):
    """CreateTaskFromMultiAction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 创建成功的演练ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """创建成功的演练ID
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


class CreateTaskFromTemplateRequest(AbstractModel):
    """CreateTaskFromTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 从经验库中查询到的经验模板ID
        :type TemplateId: int
        :param _TaskConfig: 演练的配置参数
        :type TaskConfig: :class:`tencentcloud.cfg.v20210820.models.TaskConfig`
        """
        self._TemplateId = None
        self._TaskConfig = None

    @property
    def TemplateId(self):
        """从经验库中查询到的经验模板ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TaskConfig(self):
        """演练的配置参数
        :rtype: :class:`tencentcloud.cfg.v20210820.models.TaskConfig`
        """
        return self._TaskConfig

    @TaskConfig.setter
    def TaskConfig(self, TaskConfig):
        self._TaskConfig = TaskConfig


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("TaskConfig") is not None:
            self._TaskConfig = TaskConfig()
            self._TaskConfig._deserialize(params.get("TaskConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFromTemplateResponse(AbstractModel):
    """CreateTaskFromTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 创建成功的演练ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """创建成功的演练ID
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


class DeleteTaskRequest(AbstractModel):
    """DeleteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
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
        


class DeleteTaskResponse(AbstractModel):
    """DeleteTask返回参数结构体

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


class DescribeActionFieldConfigListRequest(AbstractModel):
    """DescribeActionFieldConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActionIds: 动作ID列表
        :type ActionIds: list of int non-negative
        :param _ObjectTypeId: 对象类型ID
        :type ObjectTypeId: int
        """
        self._ActionIds = None
        self._ObjectTypeId = None

    @property
    def ActionIds(self):
        """动作ID列表
        :rtype: list of int non-negative
        """
        return self._ActionIds

    @ActionIds.setter
    def ActionIds(self, ActionIds):
        self._ActionIds = ActionIds

    @property
    def ObjectTypeId(self):
        """对象类型ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId


    def _deserialize(self, params):
        self._ActionIds = params.get("ActionIds")
        self._ObjectTypeId = params.get("ObjectTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionFieldConfigListResponse(AbstractModel):
    """DescribeActionFieldConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Common: 通用栏位配置列表
        :type Common: list of ActionFieldConfigResult
        :param _Results: 动作栏位配置列表
        :type Results: list of ActionFieldConfigResult
        :param _ResourceOffline: 资源下线信息
        :type ResourceOffline: list of ResourceOffline
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Common = None
        self._Results = None
        self._ResourceOffline = None
        self._RequestId = None

    @property
    def Common(self):
        """通用栏位配置列表
        :rtype: list of ActionFieldConfigResult
        """
        return self._Common

    @Common.setter
    def Common(self, Common):
        self._Common = Common

    @property
    def Results(self):
        """动作栏位配置列表
        :rtype: list of ActionFieldConfigResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def ResourceOffline(self):
        """资源下线信息
        :rtype: list of ResourceOffline
        """
        return self._ResourceOffline

    @ResourceOffline.setter
    def ResourceOffline(self, ResourceOffline):
        self._ResourceOffline = ResourceOffline

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
        if params.get("Common") is not None:
            self._Common = []
            for item in params.get("Common"):
                obj = ActionFieldConfigResult()
                obj._deserialize(item)
                self._Common.append(obj)
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ActionFieldConfigResult()
                obj._deserialize(item)
                self._Results.append(obj)
        if params.get("ResourceOffline") is not None:
            self._ResourceOffline = []
            for item in params.get("ResourceOffline"):
                obj = ResourceOffline()
                obj._deserialize(item)
                self._ResourceOffline.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeActionLibraryListRequest(AbstractModel):
    """DescribeActionLibraryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 0-100
        :type Limit: int
        :param _Offset: 默认值0
        :type Offset: int
        :param _ObjectType: 对象类型ID
        :type ObjectType: int
        :param _Filters: Keyword取值{"动作名称": "a_title", "描述": "a_desc", "动作类型": "a_type", "创建时间": "a_create_time", "二级分类": "a_resource_type"}
        :type Filters: list of ActionFilter
        :param _Attribute: 动作分类，1表示故障动作，2表示恢复动作
        :type Attribute: list of int
        :param _ActionIds: 筛选项 -动作ID
        :type ActionIds: list of int non-negative
        """
        self._Limit = None
        self._Offset = None
        self._ObjectType = None
        self._Filters = None
        self._Attribute = None
        self._ActionIds = None

    @property
    def Limit(self):
        """0-100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """默认值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ObjectType(self):
        """对象类型ID
        :rtype: int
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def Filters(self):
        """Keyword取值{"动作名称": "a_title", "描述": "a_desc", "动作类型": "a_type", "创建时间": "a_create_time", "二级分类": "a_resource_type"}
        :rtype: list of ActionFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Attribute(self):
        """动作分类，1表示故障动作，2表示恢复动作
        :rtype: list of int
        """
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def ActionIds(self):
        """筛选项 -动作ID
        :rtype: list of int non-negative
        """
        return self._ActionIds

    @ActionIds.setter
    def ActionIds(self, ActionIds):
        self._ActionIds = ActionIds


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ObjectType = params.get("ObjectType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ActionFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Attribute = params.get("Attribute")
        self._ActionIds = params.get("ActionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionLibraryListResponse(AbstractModel):
    """DescribeActionLibraryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 查询结果列表
        :type Results: list of ActionLibraryListResult
        :param _Total: 符合记录条数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._Total = None
        self._RequestId = None

    @property
    def Results(self):
        """查询结果列表
        :rtype: list of ActionLibraryListResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def Total(self):
        """符合记录条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ActionLibraryListResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeObjectTypeListRequest(AbstractModel):
    """DescribeObjectTypeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SupportType: 所支持的对象
0：全平台产品
1：平台接入的对象
2：应用所支持的部分对象
        :type SupportType: int
        """
        self._SupportType = None

    @property
    def SupportType(self):
        """所支持的对象
0：全平台产品
1：平台接入的对象
2：应用所支持的部分对象
        :rtype: int
        """
        return self._SupportType

    @SupportType.setter
    def SupportType(self, SupportType):
        self._SupportType = SupportType


    def _deserialize(self, params):
        self._SupportType = params.get("SupportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeObjectTypeListResponse(AbstractModel):
    """DescribeObjectTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ObjectTypeList: 对象类型列表
        :type ObjectTypeList: list of ObjectType
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ObjectTypeList = None
        self._RequestId = None

    @property
    def ObjectTypeList(self):
        """对象类型列表
        :rtype: list of ObjectType
        """
        return self._ObjectTypeList

    @ObjectTypeList.setter
    def ObjectTypeList(self, ObjectTypeList):
        self._ObjectTypeList = ObjectTypeList

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
        if params.get("ObjectTypeList") is not None:
            self._ObjectTypeList = []
            for item in params.get("ObjectTypeList"):
                obj = ObjectType()
                obj._deserialize(item)
                self._ObjectTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePolicy(AbstractModel):
    """查询-保护策略

    """

    def __init__(self):
        r"""
        :param _TaskPolicyIdList: 保护策略ID列表
        :type TaskPolicyIdList: list of str
        :param _TaskPolicyStatus: 保护策略状态
        :type TaskPolicyStatus: str
        :param _TaskPolicyRule: 策略规则
        :type TaskPolicyRule: str
        :param _TaskPolicyDealType: 护栏策略生效处理策略 1:顺序执行，2:暂停
        :type TaskPolicyDealType: int
        """
        self._TaskPolicyIdList = None
        self._TaskPolicyStatus = None
        self._TaskPolicyRule = None
        self._TaskPolicyDealType = None

    @property
    def TaskPolicyIdList(self):
        """保护策略ID列表
        :rtype: list of str
        """
        return self._TaskPolicyIdList

    @TaskPolicyIdList.setter
    def TaskPolicyIdList(self, TaskPolicyIdList):
        self._TaskPolicyIdList = TaskPolicyIdList

    @property
    def TaskPolicyStatus(self):
        """保护策略状态
        :rtype: str
        """
        return self._TaskPolicyStatus

    @TaskPolicyStatus.setter
    def TaskPolicyStatus(self, TaskPolicyStatus):
        self._TaskPolicyStatus = TaskPolicyStatus

    @property
    def TaskPolicyRule(self):
        """策略规则
        :rtype: str
        """
        return self._TaskPolicyRule

    @TaskPolicyRule.setter
    def TaskPolicyRule(self, TaskPolicyRule):
        self._TaskPolicyRule = TaskPolicyRule

    @property
    def TaskPolicyDealType(self):
        """护栏策略生效处理策略 1:顺序执行，2:暂停
        :rtype: int
        """
        return self._TaskPolicyDealType

    @TaskPolicyDealType.setter
    def TaskPolicyDealType(self, TaskPolicyDealType):
        self._TaskPolicyDealType = TaskPolicyDealType


    def _deserialize(self, params):
        self._TaskPolicyIdList = params.get("TaskPolicyIdList")
        self._TaskPolicyStatus = params.get("TaskPolicyStatus")
        self._TaskPolicyRule = params.get("TaskPolicyRule")
        self._TaskPolicyDealType = params.get("TaskPolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskExecuteLogsRequest(AbstractModel):
    """DescribeTaskExecuteLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _Limit: 返回的内容行数
        :type Limit: int
        :param _Offset: 日志起始的行数。
        :type Offset: int
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Limit(self):
        """返回的内容行数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """日志起始的行数。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskExecuteLogsResponse(AbstractModel):
    """DescribeTaskExecuteLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogMessage: 日志数据
        :type LogMessage: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogMessage = None
        self._RequestId = None

    @property
    def LogMessage(self):
        """日志数据
        :rtype: list of str
        """
        return self._LogMessage

    @LogMessage.setter
    def LogMessage(self, LogMessage):
        self._LogMessage = LogMessage

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
        self._LogMessage = params.get("LogMessage")
        self._RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    """DescribeTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页Limit
        :type Limit: int
        :param _Offset: 分页Offset
        :type Offset: int
        :param _TaskTitle: 演练名称
        :type TaskTitle: str
        :param _TaskTag: 标签键
        :type TaskTag: list of str
        :param _TaskStatus: 任务状态(1001 -- 未开始 1002 -- 进行中 1003 -- 暂停中 1004 -- 任务结束)
        :type TaskStatus: int
        :param _TaskStartTime: 开始时间，固定格式%Y-%m-%d %H:%M:%S
        :type TaskStartTime: str
        :param _TaskEndTime: 结束时间，固定格式%Y-%m-%d %H:%M:%S
        :type TaskEndTime: str
        :param _TaskUpdateTime: 更新时间，固定格式%Y-%m-%d %H:%M:%S
        :type TaskUpdateTime: str
        :param _Tags: 标签对
        :type Tags: list of TagWithDescribe
        :param _Filters: 筛选条件
        :type Filters: list of ActionFilter
        :param _TaskId: 演练ID
        :type TaskId: list of int non-negative
        :param _ApplicationId: 关联应用ID筛选
        :type ApplicationId: list of str
        :param _ApplicationName: 关联应用筛选
        :type ApplicationName: list of str
        :param _TaskStatusList: 任务状态筛选--支持多选 任务状态(1001 -- 未开始 1002 -- 进行中 1003 -- 暂停中 1004 -- 任务结束)
        :type TaskStatusList: list of int non-negative
        :param _ArchId: 架构ID
        :type ArchId: str
        :param _ArchName: 架构名称
        :type ArchName: str
        """
        self._Limit = None
        self._Offset = None
        self._TaskTitle = None
        self._TaskTag = None
        self._TaskStatus = None
        self._TaskStartTime = None
        self._TaskEndTime = None
        self._TaskUpdateTime = None
        self._Tags = None
        self._Filters = None
        self._TaskId = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._TaskStatusList = None
        self._ArchId = None
        self._ArchName = None

    @property
    def Limit(self):
        """分页Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TaskTitle(self):
        """演练名称
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskTag(self):
        """标签键
        :rtype: list of str
        """
        return self._TaskTag

    @TaskTag.setter
    def TaskTag(self, TaskTag):
        self._TaskTag = TaskTag

    @property
    def TaskStatus(self):
        """任务状态(1001 -- 未开始 1002 -- 进行中 1003 -- 暂停中 1004 -- 任务结束)
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskStartTime(self):
        """开始时间，固定格式%Y-%m-%d %H:%M:%S
        :rtype: str
        """
        return self._TaskStartTime

    @TaskStartTime.setter
    def TaskStartTime(self, TaskStartTime):
        self._TaskStartTime = TaskStartTime

    @property
    def TaskEndTime(self):
        """结束时间，固定格式%Y-%m-%d %H:%M:%S
        :rtype: str
        """
        return self._TaskEndTime

    @TaskEndTime.setter
    def TaskEndTime(self, TaskEndTime):
        self._TaskEndTime = TaskEndTime

    @property
    def TaskUpdateTime(self):
        """更新时间，固定格式%Y-%m-%d %H:%M:%S
        :rtype: str
        """
        return self._TaskUpdateTime

    @TaskUpdateTime.setter
    def TaskUpdateTime(self, TaskUpdateTime):
        self._TaskUpdateTime = TaskUpdateTime

    @property
    def Tags(self):
        """标签对
        :rtype: list of TagWithDescribe
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Filters(self):
        """筛选条件
        :rtype: list of ActionFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TaskId(self):
        """演练ID
        :rtype: list of int non-negative
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ApplicationId(self):
        """关联应用ID筛选
        :rtype: list of str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """关联应用筛选
        :rtype: list of str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def TaskStatusList(self):
        """任务状态筛选--支持多选 任务状态(1001 -- 未开始 1002 -- 进行中 1003 -- 暂停中 1004 -- 任务结束)
        :rtype: list of int non-negative
        """
        return self._TaskStatusList

    @TaskStatusList.setter
    def TaskStatusList(self, TaskStatusList):
        self._TaskStatusList = TaskStatusList

    @property
    def ArchId(self):
        """架构ID
        :rtype: str
        """
        return self._ArchId

    @ArchId.setter
    def ArchId(self, ArchId):
        self._ArchId = ArchId

    @property
    def ArchName(self):
        """架构名称
        :rtype: str
        """
        return self._ArchName

    @ArchName.setter
    def ArchName(self, ArchName):
        self._ArchName = ArchName


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskTag = params.get("TaskTag")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskStartTime = params.get("TaskStartTime")
        self._TaskEndTime = params.get("TaskEndTime")
        self._TaskUpdateTime = params.get("TaskUpdateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ActionFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TaskId = params.get("TaskId")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._TaskStatusList = params.get("TaskStatusList")
        self._ArchId = params.get("ArchId")
        self._ArchName = params.get("ArchName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskListResponse(AbstractModel):
    """DescribeTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskList: 无
        :type TaskList: list of TaskListItem
        :param _Total: 列表数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskList = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskList(self):
        """无
        :rtype: list of TaskListItem
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def Total(self):
        """列表数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = TaskListItem()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeTaskPolicyTriggerLogRequest(AbstractModel):
    """DescribeTaskPolicyTriggerLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 演练ID
        :type TaskId: int
        :param _Page: 页码
        :type Page: int
        :param _PageSize: 页数量
        :type PageSize: int
        """
        self._TaskId = None
        self._Page = None
        self._PageSize = None

    @property
    def TaskId(self):
        """演练ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Page(self):
        """页码
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        """页数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskPolicyTriggerLogResponse(AbstractModel):
    """DescribeTaskPolicyTriggerLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TriggerLogs: 触发日志
        :type TriggerLogs: list of PolicyTriggerLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TriggerLogs = None
        self._RequestId = None

    @property
    def TriggerLogs(self):
        """触发日志
        :rtype: list of PolicyTriggerLog
        """
        return self._TriggerLogs

    @TriggerLogs.setter
    def TriggerLogs(self, TriggerLogs):
        self._TriggerLogs = TriggerLogs

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
        if params.get("TriggerLogs") is not None:
            self._TriggerLogs = []
            for item in params.get("TriggerLogs"):
                obj = PolicyTriggerLog()
                obj._deserialize(item)
                self._TriggerLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
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
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Task: 任务信息
        :type Task: :class:`tencentcloud.cfg.v20210820.models.Task`
        :param _ReportInfo: 任务对应的演练报告信息，null表示未导出报告
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportInfo: :class:`tencentcloud.cfg.v20210820.models.TaskReportInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Task = None
        self._ReportInfo = None
        self._RequestId = None

    @property
    def Task(self):
        """任务信息
        :rtype: :class:`tencentcloud.cfg.v20210820.models.Task`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def ReportInfo(self):
        """任务对应的演练报告信息，null表示未导出报告
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cfg.v20210820.models.TaskReportInfo`
        """
        return self._ReportInfo

    @ReportInfo.setter
    def ReportInfo(self, ReportInfo):
        self._ReportInfo = ReportInfo

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
        if params.get("Task") is not None:
            self._Task = Task()
            self._Task._deserialize(params.get("Task"))
        if params.get("ReportInfo") is not None:
            self._ReportInfo = TaskReportInfo()
            self._ReportInfo._deserialize(params.get("ReportInfo"))
        self._RequestId = params.get("RequestId")


class DescribeTemplateListRequest(AbstractModel):
    """DescribeTemplateList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页Limit, 最大值100
        :type Limit: int
        :param _Offset: 分页Offset
        :type Offset: int
        :param _Title: 演练名称
        :type Title: str
        :param _Tag: 标签键
        :type Tag: list of str
        :param _IsUsed: 状态，1---使用中， 2---停用
        :type IsUsed: int
        :param _Tags: 标签对
        :type Tags: list of TagWithDescribe
        :param _TemplateSource: 经验来源 0-自建 1-专家推荐
        :type TemplateSource: int
        :param _TemplateIdList: 经验ID
        :type TemplateIdList: list of int
        :param _Filters: 过滤参数
        :type Filters: list of ActionFilter
        """
        self._Limit = None
        self._Offset = None
        self._Title = None
        self._Tag = None
        self._IsUsed = None
        self._Tags = None
        self._TemplateSource = None
        self._TemplateIdList = None
        self._Filters = None

    @property
    def Limit(self):
        """分页Limit, 最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Title(self):
        """演练名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Tag(self):
        """标签键
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def IsUsed(self):
        """状态，1---使用中， 2---停用
        :rtype: int
        """
        return self._IsUsed

    @IsUsed.setter
    def IsUsed(self, IsUsed):
        self._IsUsed = IsUsed

    @property
    def Tags(self):
        """标签对
        :rtype: list of TagWithDescribe
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TemplateSource(self):
        """经验来源 0-自建 1-专家推荐
        :rtype: int
        """
        return self._TemplateSource

    @TemplateSource.setter
    def TemplateSource(self, TemplateSource):
        self._TemplateSource = TemplateSource

    @property
    def TemplateIdList(self):
        """经验ID
        :rtype: list of int
        """
        return self._TemplateIdList

    @TemplateIdList.setter
    def TemplateIdList(self, TemplateIdList):
        self._TemplateIdList = TemplateIdList

    @property
    def Filters(self):
        """过滤参数
        :rtype: list of ActionFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Title = params.get("Title")
        self._Tag = params.get("Tag")
        self._IsUsed = params.get("IsUsed")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TemplateSource = params.get("TemplateSource")
        self._TemplateIdList = params.get("TemplateIdList")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ActionFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateListResponse(AbstractModel):
    """DescribeTemplateList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateList: 经验库列表
        :type TemplateList: list of TemplateListItem
        :param _Total: 列表数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateList = None
        self._Total = None
        self._RequestId = None

    @property
    def TemplateList(self):
        """经验库列表
        :rtype: list of TemplateListItem
        """
        return self._TemplateList

    @TemplateList.setter
    def TemplateList(self, TemplateList):
        self._TemplateList = TemplateList

    @property
    def Total(self):
        """列表数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("TemplateList") is not None:
            self._TemplateList = []
            for item in params.get("TemplateList"):
                obj = TemplateListItem()
                obj._deserialize(item)
                self._TemplateList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeTemplateRequest(AbstractModel):
    """DescribeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 经验库ID
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """经验库ID
        :rtype: int
        """
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
        


class DescribeTemplateResponse(AbstractModel):
    """DescribeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 经验库详情
        :type Template: :class:`tencentcloud.cfg.v20210820.models.Template`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        """经验库详情
        :rtype: :class:`tencentcloud.cfg.v20210820.models.Template`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

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
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class ExecuteTaskInstanceRequest(AbstractModel):
    """ExecuteTaskInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _TaskActionId: 任务动作ID
        :type TaskActionId: int
        :param _TaskInstanceIds: 任务动作实例ID
        :type TaskInstanceIds: list of int non-negative
        :param _IsOperateAll: 是否操作整个任务
        :type IsOperateAll: bool
        :param _ActionType: 操作类型：（1--启动   2--执行  3--跳过   5--重试）
        :type ActionType: int
        :param _TaskGroupId: 动作组ID
        :type TaskGroupId: int
        """
        self._TaskId = None
        self._TaskActionId = None
        self._TaskInstanceIds = None
        self._IsOperateAll = None
        self._ActionType = None
        self._TaskGroupId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskActionId(self):
        """任务动作ID
        :rtype: int
        """
        return self._TaskActionId

    @TaskActionId.setter
    def TaskActionId(self, TaskActionId):
        self._TaskActionId = TaskActionId

    @property
    def TaskInstanceIds(self):
        """任务动作实例ID
        :rtype: list of int non-negative
        """
        return self._TaskInstanceIds

    @TaskInstanceIds.setter
    def TaskInstanceIds(self, TaskInstanceIds):
        self._TaskInstanceIds = TaskInstanceIds

    @property
    def IsOperateAll(self):
        """是否操作整个任务
        :rtype: bool
        """
        return self._IsOperateAll

    @IsOperateAll.setter
    def IsOperateAll(self, IsOperateAll):
        self._IsOperateAll = IsOperateAll

    @property
    def ActionType(self):
        """操作类型：（1--启动   2--执行  3--跳过   5--重试）
        :rtype: int
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def TaskGroupId(self):
        """动作组ID
        :rtype: int
        """
        return self._TaskGroupId

    @TaskGroupId.setter
    def TaskGroupId(self, TaskGroupId):
        self._TaskGroupId = TaskGroupId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskActionId = params.get("TaskActionId")
        self._TaskInstanceIds = params.get("TaskInstanceIds")
        self._IsOperateAll = params.get("IsOperateAll")
        self._ActionType = params.get("ActionType")
        self._TaskGroupId = params.get("TaskGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteTaskInstanceResponse(AbstractModel):
    """ExecuteTaskInstance返回参数结构体

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


class ExecuteTaskRequest(AbstractModel):
    """ExecuteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 需要执行的任务ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """需要执行的任务ID
        :rtype: int
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
        


class ExecuteTaskResponse(AbstractModel):
    """ExecuteTask返回参数结构体

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


class ModifyTaskRunStatusRequest(AbstractModel):
    """ModifyTaskRunStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _Status: 任务状态, 1001--未开始 1002--进行中（执行）1003--进行中（暂停）1004--执行结束
        :type Status: int
        :param _IsExpect: 执行结果是否符合预期（当前扭转状态为执行结束时，需要必传此字段）
        :type IsExpect: bool
        :param _Summary: 演习结论（当演习状态转变为执行结束时，需要填写此字段）
        :type Summary: str
        :param _Issue: 问题以及改进
        :type Issue: str
        :param _Record: 演练记录
        :type Record: str
        """
        self._TaskId = None
        self._Status = None
        self._IsExpect = None
        self._Summary = None
        self._Issue = None
        self._Record = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """任务状态, 1001--未开始 1002--进行中（执行）1003--进行中（暂停）1004--执行结束
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsExpect(self):
        """执行结果是否符合预期（当前扭转状态为执行结束时，需要必传此字段）
        :rtype: bool
        """
        return self._IsExpect

    @IsExpect.setter
    def IsExpect(self, IsExpect):
        self._IsExpect = IsExpect

    @property
    def Summary(self):
        """演习结论（当演习状态转变为执行结束时，需要填写此字段）
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Issue(self):
        """问题以及改进
        :rtype: str
        """
        return self._Issue

    @Issue.setter
    def Issue(self, Issue):
        self._Issue = Issue

    @property
    def Record(self):
        """演练记录
        :rtype: str
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._IsExpect = params.get("IsExpect")
        self._Summary = params.get("Summary")
        self._Issue = params.get("Issue")
        self._Record = params.get("Record")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskRunStatusResponse(AbstractModel):
    """ModifyTaskRunStatus返回参数结构体

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


class ObjectType(AbstractModel):
    """对象类型

    """

    def __init__(self):
        r"""
        :param _ObjectTypeId: 对象类型ID
        :type ObjectTypeId: int
        :param _ObjectTypeTitle: 对象类型名称
        :type ObjectTypeTitle: str
        :param _ObjectTypeLevelOne: 对象类型第一级
        :type ObjectTypeLevelOne: str
        :param _ObjectTypeParams: 对象类型参数
        :type ObjectTypeParams: :class:`tencentcloud.cfg.v20210820.models.ObjectTypeConfig`
        :param _ObjectTypeJsonParse: tke接口json解析规则，null不需要解析
        :type ObjectTypeJsonParse: :class:`tencentcloud.cfg.v20210820.models.ObjectTypeJsonParse`
        :param _ObjectHasNewAction: 是否包含新动作
        :type ObjectHasNewAction: bool
        :param _ObjectPlatformName: 对应在平台架构图中的资源类型名称
        :type ObjectPlatformName: str
        :param _ObjectSupportType: 1：平台支持的对象 2：应用支持的部分对象
        :type ObjectSupportType: int
        :param _ArchLayer: 1.接入层 2.逻辑层 3. 数据层
        :type ArchLayer: int
        :param _IsArchSvg: 是否支持演练生图
        :type IsArchSvg: bool
        """
        self._ObjectTypeId = None
        self._ObjectTypeTitle = None
        self._ObjectTypeLevelOne = None
        self._ObjectTypeParams = None
        self._ObjectTypeJsonParse = None
        self._ObjectHasNewAction = None
        self._ObjectPlatformName = None
        self._ObjectSupportType = None
        self._ArchLayer = None
        self._IsArchSvg = None

    @property
    def ObjectTypeId(self):
        """对象类型ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId

    @property
    def ObjectTypeTitle(self):
        """对象类型名称
        :rtype: str
        """
        return self._ObjectTypeTitle

    @ObjectTypeTitle.setter
    def ObjectTypeTitle(self, ObjectTypeTitle):
        self._ObjectTypeTitle = ObjectTypeTitle

    @property
    def ObjectTypeLevelOne(self):
        """对象类型第一级
        :rtype: str
        """
        return self._ObjectTypeLevelOne

    @ObjectTypeLevelOne.setter
    def ObjectTypeLevelOne(self, ObjectTypeLevelOne):
        self._ObjectTypeLevelOne = ObjectTypeLevelOne

    @property
    def ObjectTypeParams(self):
        """对象类型参数
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ObjectTypeConfig`
        """
        return self._ObjectTypeParams

    @ObjectTypeParams.setter
    def ObjectTypeParams(self, ObjectTypeParams):
        self._ObjectTypeParams = ObjectTypeParams

    @property
    def ObjectTypeJsonParse(self):
        """tke接口json解析规则，null不需要解析
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ObjectTypeJsonParse`
        """
        return self._ObjectTypeJsonParse

    @ObjectTypeJsonParse.setter
    def ObjectTypeJsonParse(self, ObjectTypeJsonParse):
        self._ObjectTypeJsonParse = ObjectTypeJsonParse

    @property
    def ObjectHasNewAction(self):
        """是否包含新动作
        :rtype: bool
        """
        return self._ObjectHasNewAction

    @ObjectHasNewAction.setter
    def ObjectHasNewAction(self, ObjectHasNewAction):
        self._ObjectHasNewAction = ObjectHasNewAction

    @property
    def ObjectPlatformName(self):
        """对应在平台架构图中的资源类型名称
        :rtype: str
        """
        return self._ObjectPlatformName

    @ObjectPlatformName.setter
    def ObjectPlatformName(self, ObjectPlatformName):
        self._ObjectPlatformName = ObjectPlatformName

    @property
    def ObjectSupportType(self):
        """1：平台支持的对象 2：应用支持的部分对象
        :rtype: int
        """
        return self._ObjectSupportType

    @ObjectSupportType.setter
    def ObjectSupportType(self, ObjectSupportType):
        self._ObjectSupportType = ObjectSupportType

    @property
    def ArchLayer(self):
        """1.接入层 2.逻辑层 3. 数据层
        :rtype: int
        """
        return self._ArchLayer

    @ArchLayer.setter
    def ArchLayer(self, ArchLayer):
        self._ArchLayer = ArchLayer

    @property
    def IsArchSvg(self):
        """是否支持演练生图
        :rtype: bool
        """
        return self._IsArchSvg

    @IsArchSvg.setter
    def IsArchSvg(self, IsArchSvg):
        self._IsArchSvg = IsArchSvg


    def _deserialize(self, params):
        self._ObjectTypeId = params.get("ObjectTypeId")
        self._ObjectTypeTitle = params.get("ObjectTypeTitle")
        self._ObjectTypeLevelOne = params.get("ObjectTypeLevelOne")
        if params.get("ObjectTypeParams") is not None:
            self._ObjectTypeParams = ObjectTypeConfig()
            self._ObjectTypeParams._deserialize(params.get("ObjectTypeParams"))
        if params.get("ObjectTypeJsonParse") is not None:
            self._ObjectTypeJsonParse = ObjectTypeJsonParse()
            self._ObjectTypeJsonParse._deserialize(params.get("ObjectTypeJsonParse"))
        self._ObjectHasNewAction = params.get("ObjectHasNewAction")
        self._ObjectPlatformName = params.get("ObjectPlatformName")
        self._ObjectSupportType = params.get("ObjectSupportType")
        self._ArchLayer = params.get("ArchLayer")
        self._IsArchSvg = params.get("IsArchSvg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTypeConfig(AbstractModel):
    """对象类型配置

    """

    def __init__(self):
        r"""
        :param _Key: 主键
        :type Key: str
        :param _Fields: 对象类型配置字段列表
        :type Fields: list of ObjectTypeConfigFields
        """
        self._Key = None
        self._Fields = None

    @property
    def Key(self):
        """主键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Fields(self):
        """对象类型配置字段列表
        :rtype: list of ObjectTypeConfigFields
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = ObjectTypeConfigFields()
                obj._deserialize(item)
                self._Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTypeConfigFields(AbstractModel):
    """对象类型字段类型

    """

    def __init__(self):
        r"""
        :param _Key: instanceId
        :type Key: str
        :param _Header: 实例id
        :type Header: str
        :param _Transfer: 字段值是否需要转译，当不需要转译时，此字段返回null
        :type Transfer: str
        :param _JsonParse: tke的pod字段信息解析
        :type JsonParse: str
        :param _Type: 字段类型 0:str 1:list
        :type Type: int
        """
        self._Key = None
        self._Header = None
        self._Transfer = None
        self._JsonParse = None
        self._Type = None

    @property
    def Key(self):
        """instanceId
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Header(self):
        """实例id
        :rtype: str
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Transfer(self):
        """字段值是否需要转译，当不需要转译时，此字段返回null
        :rtype: str
        """
        return self._Transfer

    @Transfer.setter
    def Transfer(self, Transfer):
        self._Transfer = Transfer

    @property
    def JsonParse(self):
        """tke的pod字段信息解析
        :rtype: str
        """
        return self._JsonParse

    @JsonParse.setter
    def JsonParse(self, JsonParse):
        self._JsonParse = JsonParse

    @property
    def Type(self):
        """字段类型 0:str 1:list
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Header = params.get("Header")
        self._Transfer = params.get("Transfer")
        self._JsonParse = params.get("JsonParse")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTypeJsonParse(AbstractModel):
    """标准pod对象类型下拉数据的解析

    """

    def __init__(self):
        r"""
        :param _NameSpace: 命名空间
        :type NameSpace: str
        :param _WorkloadName: 工作负载名称
        :type WorkloadName: str
        :param _LanIP: 节点IP
        :type LanIP: str
        :param _InstanceId: 节点ID
        :type InstanceId: str
        """
        self._NameSpace = None
        self._WorkloadName = None
        self._LanIP = None
        self._InstanceId = None

    @property
    def NameSpace(self):
        """命名空间
        :rtype: str
        """
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def WorkloadName(self):
        """工作负载名称
        :rtype: str
        """
        return self._WorkloadName

    @WorkloadName.setter
    def WorkloadName(self, WorkloadName):
        self._WorkloadName = WorkloadName

    @property
    def LanIP(self):
        """节点IP
        :rtype: str
        """
        return self._LanIP

    @LanIP.setter
    def LanIP(self, LanIP):
        self._LanIP = LanIP

    @property
    def InstanceId(self):
        """节点ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._NameSpace = params.get("NameSpace")
        self._WorkloadName = params.get("WorkloadName")
        self._LanIP = params.get("LanIP")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyTriggerLog(AbstractModel):
    """护栏策略触发日志

    """

    def __init__(self):
        r"""
        :param _TaskId: 演练ID
        :type TaskId: int
        :param _Name: 名称
        :type Name: str
        :param _TriggerType: 类型，0--触发，1--恢复
        :type TriggerType: int
        :param _Content: 内容
        :type Content: str
        :param _CreatTime: 触发时间
        :type CreatTime: str
        """
        self._TaskId = None
        self._Name = None
        self._TriggerType = None
        self._Content = None
        self._CreatTime = None

    @property
    def TaskId(self):
        """演练ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TriggerType(self):
        """类型，0--触发，1--恢复
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Content(self):
        """内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CreatTime(self):
        """触发时间
        :rtype: str
        """
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._TriggerType = params.get("TriggerType")
        self._Content = params.get("Content")
        self._CreatTime = params.get("CreatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceOffline(AbstractModel):
    """资源下线

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: int
        :param _ResourceDeleteTime: 资源下线时间
        :type ResourceDeleteTime: str
        :param _ResourceDeleteMessage: 资源下线提示
        :type ResourceDeleteMessage: str
        """
        self._ResourceId = None
        self._ResourceDeleteTime = None
        self._ResourceDeleteMessage = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: int
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceDeleteTime(self):
        """资源下线时间
        :rtype: str
        """
        return self._ResourceDeleteTime

    @ResourceDeleteTime.setter
    def ResourceDeleteTime(self, ResourceDeleteTime):
        self._ResourceDeleteTime = ResourceDeleteTime

    @property
    def ResourceDeleteMessage(self):
        """资源下线提示
        :rtype: str
        """
        return self._ResourceDeleteMessage

    @ResourceDeleteMessage.setter
    def ResourceDeleteMessage(self, ResourceDeleteMessage):
        self._ResourceDeleteMessage = ResourceDeleteMessage


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceDeleteTime = params.get("ResourceDeleteTime")
        self._ResourceDeleteMessage = params.get("ResourceDeleteMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagWithCreate(AbstractModel):
    """用于传入创建、编辑标签

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
        """标签键
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
        


class TagWithDescribe(AbstractModel):
    """展示标签列表

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
        """标签键
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
        


class Task(AbstractModel):
    """任务

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _TaskTitle: 任务标题
        :type TaskTitle: str
        :param _TaskDescription: 任务描述
        :type TaskDescription: str
        :param _TaskTag: 自定义标签
        :type TaskTag: str
        :param _TaskStatus: 任务状态，1001--未开始  1002--进行中（执行）1003--进行中（暂停）1004--执行结束
        :type TaskStatus: int
        :param _TaskStatusType: 任务结束状态，表明任务以何种状态结束: 0 -- 尚未结束，1 -- 成功，2-- 失败，3--终止
        :type TaskStatusType: int
        :param _TaskProtectStrategy: 保护策略
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskProtectStrategy: str
        :param _TaskCreateTime: 任务创建时间
        :type TaskCreateTime: str
        :param _TaskUpdateTime: 任务更新时间
        :type TaskUpdateTime: str
        :param _TaskGroups: 任务动作组
        :type TaskGroups: list of TaskGroup
        :param _TaskStartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStartTime: str
        :param _TaskEndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskEndTime: str
        :param _TaskExpect: 是否符合预期。1：符合预期，2：不符合预期
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskExpect: int
        :param _TaskSummary: 演习记录
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSummary: str
        :param _TaskMode: 任务模式。1:手工执行，2:自动执行
        :type TaskMode: int
        :param _TaskPauseDuration: 自动暂停时长。单位分钟
        :type TaskPauseDuration: int
        :param _TaskOwnerUin: 演练创建者Uin
        :type TaskOwnerUin: str
        :param _TaskRegionId: 地域ID
        :type TaskRegionId: int
        :param _TaskMonitors: 监控指标列表
        :type TaskMonitors: list of TaskMonitor
        :param _TaskPolicy: 保护策略
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPolicy: :class:`tencentcloud.cfg.v20210820.models.DescribePolicy`
        :param _Tags: 标签列表
        :type Tags: list of TagWithDescribe
        :param _TaskPlanId: 关联的演练计划ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPlanId: int
        :param _TaskPlanTitle: 关联的演练计划名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPlanTitle: str
        :param _ApplicationId: 关联的应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _ApplicationName: 关联的应用名称
        :type ApplicationName: str
        :param _AlarmPolicy: 关联的告警指标
        :type AlarmPolicy: list of str
        :param _ApmServiceList: 关联的APM服务
        :type ApmServiceList: list of ApmServiceInfo
        :param _VerifyId: 关联的隐患验证项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyId: int
        :param _PolicyDealType: 护栏处理方式，1--顺序回滚，2--演练暂停
        :type PolicyDealType: int
        :param _TaskPlanStartTime: 计划开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPlanStartTime: str
        :param _TaskPlanEndTime: 计划结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPlanEndTime: str
        :param _TaskOrg: 人员组织
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskOrg: list of TaskOrg
        :param _TaskIssue: 问题和改进
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskIssue: str
        :param _TaskRegionName: region信息
        :type TaskRegionName: str
        :param _TaskArchId: 架构ID
        :type TaskArchId: str
        :param _TaskScenario: 演练场景
        :type TaskScenario: list of TaskTarget
        :param _TaskPurpose: 演练目的
        :type TaskPurpose: list of TaskTarget
        """
        self._TaskId = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskTag = None
        self._TaskStatus = None
        self._TaskStatusType = None
        self._TaskProtectStrategy = None
        self._TaskCreateTime = None
        self._TaskUpdateTime = None
        self._TaskGroups = None
        self._TaskStartTime = None
        self._TaskEndTime = None
        self._TaskExpect = None
        self._TaskSummary = None
        self._TaskMode = None
        self._TaskPauseDuration = None
        self._TaskOwnerUin = None
        self._TaskRegionId = None
        self._TaskMonitors = None
        self._TaskPolicy = None
        self._Tags = None
        self._TaskPlanId = None
        self._TaskPlanTitle = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._AlarmPolicy = None
        self._ApmServiceList = None
        self._VerifyId = None
        self._PolicyDealType = None
        self._TaskPlanStartTime = None
        self._TaskPlanEndTime = None
        self._TaskOrg = None
        self._TaskIssue = None
        self._TaskRegionName = None
        self._TaskArchId = None
        self._TaskScenario = None
        self._TaskPurpose = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskTitle(self):
        """任务标题
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """任务描述
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskTag(self):
        """自定义标签
        :rtype: str
        """
        return self._TaskTag

    @TaskTag.setter
    def TaskTag(self, TaskTag):
        self._TaskTag = TaskTag

    @property
    def TaskStatus(self):
        """任务状态，1001--未开始  1002--进行中（执行）1003--进行中（暂停）1004--执行结束
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskStatusType(self):
        """任务结束状态，表明任务以何种状态结束: 0 -- 尚未结束，1 -- 成功，2-- 失败，3--终止
        :rtype: int
        """
        return self._TaskStatusType

    @TaskStatusType.setter
    def TaskStatusType(self, TaskStatusType):
        self._TaskStatusType = TaskStatusType

    @property
    def TaskProtectStrategy(self):
        """保护策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskProtectStrategy

    @TaskProtectStrategy.setter
    def TaskProtectStrategy(self, TaskProtectStrategy):
        self._TaskProtectStrategy = TaskProtectStrategy

    @property
    def TaskCreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._TaskCreateTime

    @TaskCreateTime.setter
    def TaskCreateTime(self, TaskCreateTime):
        self._TaskCreateTime = TaskCreateTime

    @property
    def TaskUpdateTime(self):
        """任务更新时间
        :rtype: str
        """
        return self._TaskUpdateTime

    @TaskUpdateTime.setter
    def TaskUpdateTime(self, TaskUpdateTime):
        self._TaskUpdateTime = TaskUpdateTime

    @property
    def TaskGroups(self):
        """任务动作组
        :rtype: list of TaskGroup
        """
        return self._TaskGroups

    @TaskGroups.setter
    def TaskGroups(self, TaskGroups):
        self._TaskGroups = TaskGroups

    @property
    def TaskStartTime(self):
        """开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskStartTime

    @TaskStartTime.setter
    def TaskStartTime(self, TaskStartTime):
        self._TaskStartTime = TaskStartTime

    @property
    def TaskEndTime(self):
        """结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskEndTime

    @TaskEndTime.setter
    def TaskEndTime(self, TaskEndTime):
        self._TaskEndTime = TaskEndTime

    @property
    def TaskExpect(self):
        """是否符合预期。1：符合预期，2：不符合预期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskExpect

    @TaskExpect.setter
    def TaskExpect(self, TaskExpect):
        self._TaskExpect = TaskExpect

    @property
    def TaskSummary(self):
        """演习记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskSummary

    @TaskSummary.setter
    def TaskSummary(self, TaskSummary):
        self._TaskSummary = TaskSummary

    @property
    def TaskMode(self):
        """任务模式。1:手工执行，2:自动执行
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def TaskPauseDuration(self):
        """自动暂停时长。单位分钟
        :rtype: int
        """
        return self._TaskPauseDuration

    @TaskPauseDuration.setter
    def TaskPauseDuration(self, TaskPauseDuration):
        self._TaskPauseDuration = TaskPauseDuration

    @property
    def TaskOwnerUin(self):
        """演练创建者Uin
        :rtype: str
        """
        return self._TaskOwnerUin

    @TaskOwnerUin.setter
    def TaskOwnerUin(self, TaskOwnerUin):
        self._TaskOwnerUin = TaskOwnerUin

    @property
    def TaskRegionId(self):
        """地域ID
        :rtype: int
        """
        return self._TaskRegionId

    @TaskRegionId.setter
    def TaskRegionId(self, TaskRegionId):
        self._TaskRegionId = TaskRegionId

    @property
    def TaskMonitors(self):
        """监控指标列表
        :rtype: list of TaskMonitor
        """
        return self._TaskMonitors

    @TaskMonitors.setter
    def TaskMonitors(self, TaskMonitors):
        self._TaskMonitors = TaskMonitors

    @property
    def TaskPolicy(self):
        """保护策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribePolicy`
        """
        return self._TaskPolicy

    @TaskPolicy.setter
    def TaskPolicy(self, TaskPolicy):
        self._TaskPolicy = TaskPolicy

    @property
    def Tags(self):
        """标签列表
        :rtype: list of TagWithDescribe
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TaskPlanId(self):
        """关联的演练计划ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskPlanId

    @TaskPlanId.setter
    def TaskPlanId(self, TaskPlanId):
        self._TaskPlanId = TaskPlanId

    @property
    def TaskPlanTitle(self):
        """关联的演练计划名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskPlanTitle

    @TaskPlanTitle.setter
    def TaskPlanTitle(self, TaskPlanTitle):
        self._TaskPlanTitle = TaskPlanTitle

    @property
    def ApplicationId(self):
        """关联的应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """关联的应用名称
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def AlarmPolicy(self):
        """关联的告警指标
        :rtype: list of str
        """
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy

    @property
    def ApmServiceList(self):
        """关联的APM服务
        :rtype: list of ApmServiceInfo
        """
        return self._ApmServiceList

    @ApmServiceList.setter
    def ApmServiceList(self, ApmServiceList):
        self._ApmServiceList = ApmServiceList

    @property
    def VerifyId(self):
        """关联的隐患验证项ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VerifyId

    @VerifyId.setter
    def VerifyId(self, VerifyId):
        self._VerifyId = VerifyId

    @property
    def PolicyDealType(self):
        """护栏处理方式，1--顺序回滚，2--演练暂停
        :rtype: int
        """
        return self._PolicyDealType

    @PolicyDealType.setter
    def PolicyDealType(self, PolicyDealType):
        self._PolicyDealType = PolicyDealType

    @property
    def TaskPlanStartTime(self):
        """计划开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskPlanStartTime

    @TaskPlanStartTime.setter
    def TaskPlanStartTime(self, TaskPlanStartTime):
        self._TaskPlanStartTime = TaskPlanStartTime

    @property
    def TaskPlanEndTime(self):
        """计划结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskPlanEndTime

    @TaskPlanEndTime.setter
    def TaskPlanEndTime(self, TaskPlanEndTime):
        self._TaskPlanEndTime = TaskPlanEndTime

    @property
    def TaskOrg(self):
        """人员组织
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskOrg
        """
        return self._TaskOrg

    @TaskOrg.setter
    def TaskOrg(self, TaskOrg):
        self._TaskOrg = TaskOrg

    @property
    def TaskIssue(self):
        """问题和改进
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskIssue

    @TaskIssue.setter
    def TaskIssue(self, TaskIssue):
        self._TaskIssue = TaskIssue

    @property
    def TaskRegionName(self):
        """region信息
        :rtype: str
        """
        return self._TaskRegionName

    @TaskRegionName.setter
    def TaskRegionName(self, TaskRegionName):
        self._TaskRegionName = TaskRegionName

    @property
    def TaskArchId(self):
        """架构ID
        :rtype: str
        """
        return self._TaskArchId

    @TaskArchId.setter
    def TaskArchId(self, TaskArchId):
        self._TaskArchId = TaskArchId

    @property
    def TaskScenario(self):
        """演练场景
        :rtype: list of TaskTarget
        """
        return self._TaskScenario

    @TaskScenario.setter
    def TaskScenario(self, TaskScenario):
        self._TaskScenario = TaskScenario

    @property
    def TaskPurpose(self):
        """演练目的
        :rtype: list of TaskTarget
        """
        return self._TaskPurpose

    @TaskPurpose.setter
    def TaskPurpose(self, TaskPurpose):
        self._TaskPurpose = TaskPurpose


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskTag = params.get("TaskTag")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskStatusType = params.get("TaskStatusType")
        self._TaskProtectStrategy = params.get("TaskProtectStrategy")
        self._TaskCreateTime = params.get("TaskCreateTime")
        self._TaskUpdateTime = params.get("TaskUpdateTime")
        if params.get("TaskGroups") is not None:
            self._TaskGroups = []
            for item in params.get("TaskGroups"):
                obj = TaskGroup()
                obj._deserialize(item)
                self._TaskGroups.append(obj)
        self._TaskStartTime = params.get("TaskStartTime")
        self._TaskEndTime = params.get("TaskEndTime")
        self._TaskExpect = params.get("TaskExpect")
        self._TaskSummary = params.get("TaskSummary")
        self._TaskMode = params.get("TaskMode")
        self._TaskPauseDuration = params.get("TaskPauseDuration")
        self._TaskOwnerUin = params.get("TaskOwnerUin")
        self._TaskRegionId = params.get("TaskRegionId")
        if params.get("TaskMonitors") is not None:
            self._TaskMonitors = []
            for item in params.get("TaskMonitors"):
                obj = TaskMonitor()
                obj._deserialize(item)
                self._TaskMonitors.append(obj)
        if params.get("TaskPolicy") is not None:
            self._TaskPolicy = DescribePolicy()
            self._TaskPolicy._deserialize(params.get("TaskPolicy"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TaskPlanId = params.get("TaskPlanId")
        self._TaskPlanTitle = params.get("TaskPlanTitle")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._AlarmPolicy = params.get("AlarmPolicy")
        if params.get("ApmServiceList") is not None:
            self._ApmServiceList = []
            for item in params.get("ApmServiceList"):
                obj = ApmServiceInfo()
                obj._deserialize(item)
                self._ApmServiceList.append(obj)
        self._VerifyId = params.get("VerifyId")
        self._PolicyDealType = params.get("PolicyDealType")
        self._TaskPlanStartTime = params.get("TaskPlanStartTime")
        self._TaskPlanEndTime = params.get("TaskPlanEndTime")
        if params.get("TaskOrg") is not None:
            self._TaskOrg = []
            for item in params.get("TaskOrg"):
                obj = TaskOrg()
                obj._deserialize(item)
                self._TaskOrg.append(obj)
        self._TaskIssue = params.get("TaskIssue")
        self._TaskRegionName = params.get("TaskRegionName")
        self._TaskArchId = params.get("TaskArchId")
        if params.get("TaskScenario") is not None:
            self._TaskScenario = []
            for item in params.get("TaskScenario"):
                obj = TaskTarget()
                obj._deserialize(item)
                self._TaskScenario.append(obj)
        if params.get("TaskPurpose") is not None:
            self._TaskPurpose = []
            for item in params.get("TaskPurpose"):
                obj = TaskTarget()
                obj._deserialize(item)
                self._TaskPurpose.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskConfig(AbstractModel):
    """从经验模板创建演练时需要配置的任务参数

    """

    def __init__(self):
        r"""
        :param _TaskGroupsConfig: 动作组配置，需要保证配置个数和经验中的动作组个数一致
        :type TaskGroupsConfig: list of TaskGroupConfig
        :param _TaskTitle: 更改后的演练名称，不填则默认取经验名称
        :type TaskTitle: str
        :param _TaskDescription: 更改后的演练描述，不填则默认取经验描述
        :type TaskDescription: str
        :param _TaskMode: 演练执行模式：1----手工执行/ 2 ---自动执行，不填则默认取经验执行模式
        :type TaskMode: int
        :param _TaskPauseDuration: 演练自动暂停时间，单位分钟, 不填则默认取经验自动暂停时间
        :type TaskPauseDuration: int
        :param _Tags: 演练标签信息，不填则默认取经验标签
        :type Tags: list of TagWithCreate
        :param _PolicyDealType: 护栏处理方式，1--顺序回滚，2--演练暂停
        :type PolicyDealType: int
        """
        self._TaskGroupsConfig = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskMode = None
        self._TaskPauseDuration = None
        self._Tags = None
        self._PolicyDealType = None

    @property
    def TaskGroupsConfig(self):
        """动作组配置，需要保证配置个数和经验中的动作组个数一致
        :rtype: list of TaskGroupConfig
        """
        return self._TaskGroupsConfig

    @TaskGroupsConfig.setter
    def TaskGroupsConfig(self, TaskGroupsConfig):
        self._TaskGroupsConfig = TaskGroupsConfig

    @property
    def TaskTitle(self):
        """更改后的演练名称，不填则默认取经验名称
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """更改后的演练描述，不填则默认取经验描述
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskMode(self):
        """演练执行模式：1----手工执行/ 2 ---自动执行，不填则默认取经验执行模式
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def TaskPauseDuration(self):
        """演练自动暂停时间，单位分钟, 不填则默认取经验自动暂停时间
        :rtype: int
        """
        return self._TaskPauseDuration

    @TaskPauseDuration.setter
    def TaskPauseDuration(self, TaskPauseDuration):
        self._TaskPauseDuration = TaskPauseDuration

    @property
    def Tags(self):
        """演练标签信息，不填则默认取经验标签
        :rtype: list of TagWithCreate
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PolicyDealType(self):
        """护栏处理方式，1--顺序回滚，2--演练暂停
        :rtype: int
        """
        return self._PolicyDealType

    @PolicyDealType.setter
    def PolicyDealType(self, PolicyDealType):
        self._PolicyDealType = PolicyDealType


    def _deserialize(self, params):
        if params.get("TaskGroupsConfig") is not None:
            self._TaskGroupsConfig = []
            for item in params.get("TaskGroupsConfig"):
                obj = TaskGroupConfig()
                obj._deserialize(item)
                self._TaskGroupsConfig.append(obj)
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskMode = params.get("TaskMode")
        self._TaskPauseDuration = params.get("TaskPauseDuration")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithCreate()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PolicyDealType = params.get("PolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroup(AbstractModel):
    """任务分组

    """

    def __init__(self):
        r"""
        :param _TaskGroupId: 任务动作ID
        :type TaskGroupId: int
        :param _TaskGroupTitle: 分组标题
        :type TaskGroupTitle: str
        :param _TaskGroupDescription: 分组描述
        :type TaskGroupDescription: str
        :param _TaskGroupOrder: 任务分组顺序
        :type TaskGroupOrder: int
        :param _ObjectTypeId: 对象类型ID
        :type ObjectTypeId: int
        :param _TaskGroupCreateTime: 任务分组创建时间
        :type TaskGroupCreateTime: str
        :param _TaskGroupUpdateTime: 任务分组更新时间
        :type TaskGroupUpdateTime: str
        :param _TaskGroupActions: 动作分组动作列表
        :type TaskGroupActions: list of TaskGroupAction
        :param _TaskGroupInstanceList: 实例列表
        :type TaskGroupInstanceList: list of str
        :param _TaskGroupMode: 执行模式。1 --- 顺序执行，2 --- 阶段执行
        :type TaskGroupMode: int
        :param _TaskGroupDiscardInstanceList: 不参演的实例列表
        :type TaskGroupDiscardInstanceList: list of str
        :param _TaskGroupSelectedInstanceList: 参演实例列表
        :type TaskGroupSelectedInstanceList: list of str
        :param _TaskGroupInstancesExecuteRule: 机器选取规则
        :type TaskGroupInstancesExecuteRule: list of TaskGroupInstancesExecuteRules
        """
        self._TaskGroupId = None
        self._TaskGroupTitle = None
        self._TaskGroupDescription = None
        self._TaskGroupOrder = None
        self._ObjectTypeId = None
        self._TaskGroupCreateTime = None
        self._TaskGroupUpdateTime = None
        self._TaskGroupActions = None
        self._TaskGroupInstanceList = None
        self._TaskGroupMode = None
        self._TaskGroupDiscardInstanceList = None
        self._TaskGroupSelectedInstanceList = None
        self._TaskGroupInstancesExecuteRule = None

    @property
    def TaskGroupId(self):
        """任务动作ID
        :rtype: int
        """
        return self._TaskGroupId

    @TaskGroupId.setter
    def TaskGroupId(self, TaskGroupId):
        self._TaskGroupId = TaskGroupId

    @property
    def TaskGroupTitle(self):
        """分组标题
        :rtype: str
        """
        return self._TaskGroupTitle

    @TaskGroupTitle.setter
    def TaskGroupTitle(self, TaskGroupTitle):
        self._TaskGroupTitle = TaskGroupTitle

    @property
    def TaskGroupDescription(self):
        """分组描述
        :rtype: str
        """
        return self._TaskGroupDescription

    @TaskGroupDescription.setter
    def TaskGroupDescription(self, TaskGroupDescription):
        self._TaskGroupDescription = TaskGroupDescription

    @property
    def TaskGroupOrder(self):
        """任务分组顺序
        :rtype: int
        """
        return self._TaskGroupOrder

    @TaskGroupOrder.setter
    def TaskGroupOrder(self, TaskGroupOrder):
        self._TaskGroupOrder = TaskGroupOrder

    @property
    def ObjectTypeId(self):
        """对象类型ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId

    @property
    def TaskGroupCreateTime(self):
        """任务分组创建时间
        :rtype: str
        """
        return self._TaskGroupCreateTime

    @TaskGroupCreateTime.setter
    def TaskGroupCreateTime(self, TaskGroupCreateTime):
        self._TaskGroupCreateTime = TaskGroupCreateTime

    @property
    def TaskGroupUpdateTime(self):
        """任务分组更新时间
        :rtype: str
        """
        return self._TaskGroupUpdateTime

    @TaskGroupUpdateTime.setter
    def TaskGroupUpdateTime(self, TaskGroupUpdateTime):
        self._TaskGroupUpdateTime = TaskGroupUpdateTime

    @property
    def TaskGroupActions(self):
        """动作分组动作列表
        :rtype: list of TaskGroupAction
        """
        return self._TaskGroupActions

    @TaskGroupActions.setter
    def TaskGroupActions(self, TaskGroupActions):
        self._TaskGroupActions = TaskGroupActions

    @property
    def TaskGroupInstanceList(self):
        """实例列表
        :rtype: list of str
        """
        return self._TaskGroupInstanceList

    @TaskGroupInstanceList.setter
    def TaskGroupInstanceList(self, TaskGroupInstanceList):
        self._TaskGroupInstanceList = TaskGroupInstanceList

    @property
    def TaskGroupMode(self):
        """执行模式。1 --- 顺序执行，2 --- 阶段执行
        :rtype: int
        """
        return self._TaskGroupMode

    @TaskGroupMode.setter
    def TaskGroupMode(self, TaskGroupMode):
        self._TaskGroupMode = TaskGroupMode

    @property
    def TaskGroupDiscardInstanceList(self):
        """不参演的实例列表
        :rtype: list of str
        """
        return self._TaskGroupDiscardInstanceList

    @TaskGroupDiscardInstanceList.setter
    def TaskGroupDiscardInstanceList(self, TaskGroupDiscardInstanceList):
        self._TaskGroupDiscardInstanceList = TaskGroupDiscardInstanceList

    @property
    def TaskGroupSelectedInstanceList(self):
        """参演实例列表
        :rtype: list of str
        """
        return self._TaskGroupSelectedInstanceList

    @TaskGroupSelectedInstanceList.setter
    def TaskGroupSelectedInstanceList(self, TaskGroupSelectedInstanceList):
        self._TaskGroupSelectedInstanceList = TaskGroupSelectedInstanceList

    @property
    def TaskGroupInstancesExecuteRule(self):
        """机器选取规则
        :rtype: list of TaskGroupInstancesExecuteRules
        """
        return self._TaskGroupInstancesExecuteRule

    @TaskGroupInstancesExecuteRule.setter
    def TaskGroupInstancesExecuteRule(self, TaskGroupInstancesExecuteRule):
        self._TaskGroupInstancesExecuteRule = TaskGroupInstancesExecuteRule


    def _deserialize(self, params):
        self._TaskGroupId = params.get("TaskGroupId")
        self._TaskGroupTitle = params.get("TaskGroupTitle")
        self._TaskGroupDescription = params.get("TaskGroupDescription")
        self._TaskGroupOrder = params.get("TaskGroupOrder")
        self._ObjectTypeId = params.get("ObjectTypeId")
        self._TaskGroupCreateTime = params.get("TaskGroupCreateTime")
        self._TaskGroupUpdateTime = params.get("TaskGroupUpdateTime")
        if params.get("TaskGroupActions") is not None:
            self._TaskGroupActions = []
            for item in params.get("TaskGroupActions"):
                obj = TaskGroupAction()
                obj._deserialize(item)
                self._TaskGroupActions.append(obj)
        self._TaskGroupInstanceList = params.get("TaskGroupInstanceList")
        self._TaskGroupMode = params.get("TaskGroupMode")
        self._TaskGroupDiscardInstanceList = params.get("TaskGroupDiscardInstanceList")
        self._TaskGroupSelectedInstanceList = params.get("TaskGroupSelectedInstanceList")
        if params.get("TaskGroupInstancesExecuteRule") is not None:
            self._TaskGroupInstancesExecuteRule = []
            for item in params.get("TaskGroupInstancesExecuteRule"):
                obj = TaskGroupInstancesExecuteRules()
                obj._deserialize(item)
                self._TaskGroupInstancesExecuteRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupAction(AbstractModel):
    """任务分组动作

    """

    def __init__(self):
        r"""
        :param _TaskGroupActionId: 任务分组动作ID
        :type TaskGroupActionId: int
        :param _TaskGroupInstances: 任务分组动作实例列表
        :type TaskGroupInstances: list of TaskGroupInstance
        :param _ActionId: 动作ID
        :type ActionId: int
        :param _TaskGroupActionOrder: 分组动作顺序
        :type TaskGroupActionOrder: int
        :param _TaskGroupActionGeneralConfiguration: 分组动作通用配置
        :type TaskGroupActionGeneralConfiguration: str
        :param _TaskGroupActionCustomConfiguration: 分组动作自定义配置
        :type TaskGroupActionCustomConfiguration: str
        :param _TaskGroupActionStatus: 分组动作状态
        :type TaskGroupActionStatus: int
        :param _TaskGroupActionCreateTime: 动作分组创建时间
        :type TaskGroupActionCreateTime: str
        :param _TaskGroupActionUpdateTime: 动作分组更新时间
        :type TaskGroupActionUpdateTime: str
        :param _ActionTitle: 动作名称
        :type ActionTitle: str
        :param _TaskGroupActionStatusType: 状态类型: 0 -- 无状态，1 -- 成功，2-- 失败，3--终止，4--跳过
        :type TaskGroupActionStatusType: int
        :param _TaskGroupActionRandomId: RandomId
        :type TaskGroupActionRandomId: int
        :param _TaskGroupActionRecoverId: RecoverId
        :type TaskGroupActionRecoverId: int
        :param _TaskGroupActionExecuteId: ExecuteId
        :type TaskGroupActionExecuteId: int
        :param _ActionApiType: 调用api类型，0:tat, 1:云api
        :type ActionApiType: int
        :param _ActionAttribute: 1:故障，2:恢复
        :type ActionAttribute: int
        :param _ActionType: 动作类型：平台、自定义
        :type ActionType: str
        :param _IsExecuteRedo: 是否可重试
        :type IsExecuteRedo: bool
        :param _ActionRisk: 动作风险级别
        :type ActionRisk: str
        :param _TaskGroupActionExecuteTime: 动作运行时间
        :type TaskGroupActionExecuteTime: int
        :param _TaskGroupActionStartTime: 动作开始执行时间
        :type TaskGroupActionStartTime: str
        """
        self._TaskGroupActionId = None
        self._TaskGroupInstances = None
        self._ActionId = None
        self._TaskGroupActionOrder = None
        self._TaskGroupActionGeneralConfiguration = None
        self._TaskGroupActionCustomConfiguration = None
        self._TaskGroupActionStatus = None
        self._TaskGroupActionCreateTime = None
        self._TaskGroupActionUpdateTime = None
        self._ActionTitle = None
        self._TaskGroupActionStatusType = None
        self._TaskGroupActionRandomId = None
        self._TaskGroupActionRecoverId = None
        self._TaskGroupActionExecuteId = None
        self._ActionApiType = None
        self._ActionAttribute = None
        self._ActionType = None
        self._IsExecuteRedo = None
        self._ActionRisk = None
        self._TaskGroupActionExecuteTime = None
        self._TaskGroupActionStartTime = None

    @property
    def TaskGroupActionId(self):
        """任务分组动作ID
        :rtype: int
        """
        return self._TaskGroupActionId

    @TaskGroupActionId.setter
    def TaskGroupActionId(self, TaskGroupActionId):
        self._TaskGroupActionId = TaskGroupActionId

    @property
    def TaskGroupInstances(self):
        """任务分组动作实例列表
        :rtype: list of TaskGroupInstance
        """
        return self._TaskGroupInstances

    @TaskGroupInstances.setter
    def TaskGroupInstances(self, TaskGroupInstances):
        self._TaskGroupInstances = TaskGroupInstances

    @property
    def ActionId(self):
        """动作ID
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def TaskGroupActionOrder(self):
        """分组动作顺序
        :rtype: int
        """
        return self._TaskGroupActionOrder

    @TaskGroupActionOrder.setter
    def TaskGroupActionOrder(self, TaskGroupActionOrder):
        self._TaskGroupActionOrder = TaskGroupActionOrder

    @property
    def TaskGroupActionGeneralConfiguration(self):
        """分组动作通用配置
        :rtype: str
        """
        return self._TaskGroupActionGeneralConfiguration

    @TaskGroupActionGeneralConfiguration.setter
    def TaskGroupActionGeneralConfiguration(self, TaskGroupActionGeneralConfiguration):
        self._TaskGroupActionGeneralConfiguration = TaskGroupActionGeneralConfiguration

    @property
    def TaskGroupActionCustomConfiguration(self):
        """分组动作自定义配置
        :rtype: str
        """
        return self._TaskGroupActionCustomConfiguration

    @TaskGroupActionCustomConfiguration.setter
    def TaskGroupActionCustomConfiguration(self, TaskGroupActionCustomConfiguration):
        self._TaskGroupActionCustomConfiguration = TaskGroupActionCustomConfiguration

    @property
    def TaskGroupActionStatus(self):
        """分组动作状态
        :rtype: int
        """
        return self._TaskGroupActionStatus

    @TaskGroupActionStatus.setter
    def TaskGroupActionStatus(self, TaskGroupActionStatus):
        self._TaskGroupActionStatus = TaskGroupActionStatus

    @property
    def TaskGroupActionCreateTime(self):
        """动作分组创建时间
        :rtype: str
        """
        return self._TaskGroupActionCreateTime

    @TaskGroupActionCreateTime.setter
    def TaskGroupActionCreateTime(self, TaskGroupActionCreateTime):
        self._TaskGroupActionCreateTime = TaskGroupActionCreateTime

    @property
    def TaskGroupActionUpdateTime(self):
        """动作分组更新时间
        :rtype: str
        """
        return self._TaskGroupActionUpdateTime

    @TaskGroupActionUpdateTime.setter
    def TaskGroupActionUpdateTime(self, TaskGroupActionUpdateTime):
        self._TaskGroupActionUpdateTime = TaskGroupActionUpdateTime

    @property
    def ActionTitle(self):
        """动作名称
        :rtype: str
        """
        return self._ActionTitle

    @ActionTitle.setter
    def ActionTitle(self, ActionTitle):
        self._ActionTitle = ActionTitle

    @property
    def TaskGroupActionStatusType(self):
        """状态类型: 0 -- 无状态，1 -- 成功，2-- 失败，3--终止，4--跳过
        :rtype: int
        """
        return self._TaskGroupActionStatusType

    @TaskGroupActionStatusType.setter
    def TaskGroupActionStatusType(self, TaskGroupActionStatusType):
        self._TaskGroupActionStatusType = TaskGroupActionStatusType

    @property
    def TaskGroupActionRandomId(self):
        """RandomId
        :rtype: int
        """
        return self._TaskGroupActionRandomId

    @TaskGroupActionRandomId.setter
    def TaskGroupActionRandomId(self, TaskGroupActionRandomId):
        self._TaskGroupActionRandomId = TaskGroupActionRandomId

    @property
    def TaskGroupActionRecoverId(self):
        """RecoverId
        :rtype: int
        """
        return self._TaskGroupActionRecoverId

    @TaskGroupActionRecoverId.setter
    def TaskGroupActionRecoverId(self, TaskGroupActionRecoverId):
        self._TaskGroupActionRecoverId = TaskGroupActionRecoverId

    @property
    def TaskGroupActionExecuteId(self):
        """ExecuteId
        :rtype: int
        """
        return self._TaskGroupActionExecuteId

    @TaskGroupActionExecuteId.setter
    def TaskGroupActionExecuteId(self, TaskGroupActionExecuteId):
        self._TaskGroupActionExecuteId = TaskGroupActionExecuteId

    @property
    def ActionApiType(self):
        """调用api类型，0:tat, 1:云api
        :rtype: int
        """
        return self._ActionApiType

    @ActionApiType.setter
    def ActionApiType(self, ActionApiType):
        self._ActionApiType = ActionApiType

    @property
    def ActionAttribute(self):
        """1:故障，2:恢复
        :rtype: int
        """
        return self._ActionAttribute

    @ActionAttribute.setter
    def ActionAttribute(self, ActionAttribute):
        self._ActionAttribute = ActionAttribute

    @property
    def ActionType(self):
        """动作类型：平台、自定义
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def IsExecuteRedo(self):
        """是否可重试
        :rtype: bool
        """
        return self._IsExecuteRedo

    @IsExecuteRedo.setter
    def IsExecuteRedo(self, IsExecuteRedo):
        self._IsExecuteRedo = IsExecuteRedo

    @property
    def ActionRisk(self):
        """动作风险级别
        :rtype: str
        """
        return self._ActionRisk

    @ActionRisk.setter
    def ActionRisk(self, ActionRisk):
        self._ActionRisk = ActionRisk

    @property
    def TaskGroupActionExecuteTime(self):
        """动作运行时间
        :rtype: int
        """
        return self._TaskGroupActionExecuteTime

    @TaskGroupActionExecuteTime.setter
    def TaskGroupActionExecuteTime(self, TaskGroupActionExecuteTime):
        self._TaskGroupActionExecuteTime = TaskGroupActionExecuteTime

    @property
    def TaskGroupActionStartTime(self):
        """动作开始执行时间
        :rtype: str
        """
        return self._TaskGroupActionStartTime

    @TaskGroupActionStartTime.setter
    def TaskGroupActionStartTime(self, TaskGroupActionStartTime):
        self._TaskGroupActionStartTime = TaskGroupActionStartTime


    def _deserialize(self, params):
        self._TaskGroupActionId = params.get("TaskGroupActionId")
        if params.get("TaskGroupInstances") is not None:
            self._TaskGroupInstances = []
            for item in params.get("TaskGroupInstances"):
                obj = TaskGroupInstance()
                obj._deserialize(item)
                self._TaskGroupInstances.append(obj)
        self._ActionId = params.get("ActionId")
        self._TaskGroupActionOrder = params.get("TaskGroupActionOrder")
        self._TaskGroupActionGeneralConfiguration = params.get("TaskGroupActionGeneralConfiguration")
        self._TaskGroupActionCustomConfiguration = params.get("TaskGroupActionCustomConfiguration")
        self._TaskGroupActionStatus = params.get("TaskGroupActionStatus")
        self._TaskGroupActionCreateTime = params.get("TaskGroupActionCreateTime")
        self._TaskGroupActionUpdateTime = params.get("TaskGroupActionUpdateTime")
        self._ActionTitle = params.get("ActionTitle")
        self._TaskGroupActionStatusType = params.get("TaskGroupActionStatusType")
        self._TaskGroupActionRandomId = params.get("TaskGroupActionRandomId")
        self._TaskGroupActionRecoverId = params.get("TaskGroupActionRecoverId")
        self._TaskGroupActionExecuteId = params.get("TaskGroupActionExecuteId")
        self._ActionApiType = params.get("ActionApiType")
        self._ActionAttribute = params.get("ActionAttribute")
        self._ActionType = params.get("ActionType")
        self._IsExecuteRedo = params.get("IsExecuteRedo")
        self._ActionRisk = params.get("ActionRisk")
        self._TaskGroupActionExecuteTime = params.get("TaskGroupActionExecuteTime")
        self._TaskGroupActionStartTime = params.get("TaskGroupActionStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupActionConfig(AbstractModel):
    """动作组中的动作参数

    """

    def __init__(self):
        r"""
        :param _TaskGroupActionOrder: 该动作在动作组中的顺序，从1开始，不填或填错将匹配不到经验中要修改参数的动作
        :type TaskGroupActionOrder: int
        :param _TaskGroupActionGeneralConfiguration: 动作通用参数，需要json序列化传入，可以从查询经验详情接口获取，不填默认使用经验中动作参数
        :type TaskGroupActionGeneralConfiguration: str
        :param _TaskGroupActionCustomConfiguration: 动作自定义参数，需要json序列化传入，可以从查询经验详情接口获取，不填默认使用经验中动作参数
        :type TaskGroupActionCustomConfiguration: str
        """
        self._TaskGroupActionOrder = None
        self._TaskGroupActionGeneralConfiguration = None
        self._TaskGroupActionCustomConfiguration = None

    @property
    def TaskGroupActionOrder(self):
        """该动作在动作组中的顺序，从1开始，不填或填错将匹配不到经验中要修改参数的动作
        :rtype: int
        """
        return self._TaskGroupActionOrder

    @TaskGroupActionOrder.setter
    def TaskGroupActionOrder(self, TaskGroupActionOrder):
        self._TaskGroupActionOrder = TaskGroupActionOrder

    @property
    def TaskGroupActionGeneralConfiguration(self):
        """动作通用参数，需要json序列化传入，可以从查询经验详情接口获取，不填默认使用经验中动作参数
        :rtype: str
        """
        return self._TaskGroupActionGeneralConfiguration

    @TaskGroupActionGeneralConfiguration.setter
    def TaskGroupActionGeneralConfiguration(self, TaskGroupActionGeneralConfiguration):
        self._TaskGroupActionGeneralConfiguration = TaskGroupActionGeneralConfiguration

    @property
    def TaskGroupActionCustomConfiguration(self):
        """动作自定义参数，需要json序列化传入，可以从查询经验详情接口获取，不填默认使用经验中动作参数
        :rtype: str
        """
        return self._TaskGroupActionCustomConfiguration

    @TaskGroupActionCustomConfiguration.setter
    def TaskGroupActionCustomConfiguration(self, TaskGroupActionCustomConfiguration):
        self._TaskGroupActionCustomConfiguration = TaskGroupActionCustomConfiguration


    def _deserialize(self, params):
        self._TaskGroupActionOrder = params.get("TaskGroupActionOrder")
        self._TaskGroupActionGeneralConfiguration = params.get("TaskGroupActionGeneralConfiguration")
        self._TaskGroupActionCustomConfiguration = params.get("TaskGroupActionCustomConfiguration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupConfig(AbstractModel):
    """动作组的配置项

    """

    def __init__(self):
        r"""
        :param _TaskGroupInstances: 动作组所关联的实例对象
CVM ins-xxx
MySQL cdb-xxx
CLB lb-xxx
Redis crs-xxx
NAT网关 nat-xxx
专线-独享专用通道 dcx-xxx
标准集群普通节点 {"ClusterId":"cls-xxx","InstanceId":"ins-xxx","LanIP":"1.1.1.1"}
标准集群Pod {"ClusterId":"cls-xxx","PodName":"podname","NodeName":"1.1.1.1","NameSpace":"ns","Workload":"workload"}
TDSQL-MySQL(InnoDB) tdsqlshard-xxx
TDSQL-C cynosdbmysql-xxx
VPC子网 subnet-xxxx
CKafka ckafka-xxx
MariaDB tdsql-xxxx
PostgreSQL postgres-xxx
云原生网关 gateway-xxx
标准集群超级节点 {"ClusterId":"cls-xxx","InstanceId":"eklet-xxx","LanIP":"1.1.1.1,"NodePoolId":"np-xxx"}
Serverless集群超级节点 {"ClusterId":"cls-xxxx","InstanceId":"eklet-xxxx","LanIP":"1.1.1.1"}
Elasticsearch集群 es-xxxx
RabbitMQ amqp-xxxx
        :type TaskGroupInstances: list of str
        :param _TaskGroupTitle: 动作组标题，不填默认取经验中的动作组名称
        :type TaskGroupTitle: str
        :param _TaskGroupDescription: 动作组描述，不填默认取经验中的动作组描述
        :type TaskGroupDescription: str
        :param _TaskGroupMode: 动作执行模式。1 --- 顺序执行，2 --- 阶段执行, 不填默认取经验中的动作组执行模式
        :type TaskGroupMode: int
        :param _TaskGroupActionsConfig: 动作组中的动作参数，不填默认使用经验中的动作参数，配置时可以只指定想要修改参数的动作
        :type TaskGroupActionsConfig: list of TaskGroupActionConfig
        """
        self._TaskGroupInstances = None
        self._TaskGroupTitle = None
        self._TaskGroupDescription = None
        self._TaskGroupMode = None
        self._TaskGroupActionsConfig = None

    @property
    def TaskGroupInstances(self):
        """动作组所关联的实例对象
CVM ins-xxx
MySQL cdb-xxx
CLB lb-xxx
Redis crs-xxx
NAT网关 nat-xxx
专线-独享专用通道 dcx-xxx
标准集群普通节点 {"ClusterId":"cls-xxx","InstanceId":"ins-xxx","LanIP":"1.1.1.1"}
标准集群Pod {"ClusterId":"cls-xxx","PodName":"podname","NodeName":"1.1.1.1","NameSpace":"ns","Workload":"workload"}
TDSQL-MySQL(InnoDB) tdsqlshard-xxx
TDSQL-C cynosdbmysql-xxx
VPC子网 subnet-xxxx
CKafka ckafka-xxx
MariaDB tdsql-xxxx
PostgreSQL postgres-xxx
云原生网关 gateway-xxx
标准集群超级节点 {"ClusterId":"cls-xxx","InstanceId":"eklet-xxx","LanIP":"1.1.1.1,"NodePoolId":"np-xxx"}
Serverless集群超级节点 {"ClusterId":"cls-xxxx","InstanceId":"eklet-xxxx","LanIP":"1.1.1.1"}
Elasticsearch集群 es-xxxx
RabbitMQ amqp-xxxx
        :rtype: list of str
        """
        return self._TaskGroupInstances

    @TaskGroupInstances.setter
    def TaskGroupInstances(self, TaskGroupInstances):
        self._TaskGroupInstances = TaskGroupInstances

    @property
    def TaskGroupTitle(self):
        """动作组标题，不填默认取经验中的动作组名称
        :rtype: str
        """
        return self._TaskGroupTitle

    @TaskGroupTitle.setter
    def TaskGroupTitle(self, TaskGroupTitle):
        self._TaskGroupTitle = TaskGroupTitle

    @property
    def TaskGroupDescription(self):
        """动作组描述，不填默认取经验中的动作组描述
        :rtype: str
        """
        return self._TaskGroupDescription

    @TaskGroupDescription.setter
    def TaskGroupDescription(self, TaskGroupDescription):
        self._TaskGroupDescription = TaskGroupDescription

    @property
    def TaskGroupMode(self):
        """动作执行模式。1 --- 顺序执行，2 --- 阶段执行, 不填默认取经验中的动作组执行模式
        :rtype: int
        """
        return self._TaskGroupMode

    @TaskGroupMode.setter
    def TaskGroupMode(self, TaskGroupMode):
        self._TaskGroupMode = TaskGroupMode

    @property
    def TaskGroupActionsConfig(self):
        """动作组中的动作参数，不填默认使用经验中的动作参数，配置时可以只指定想要修改参数的动作
        :rtype: list of TaskGroupActionConfig
        """
        return self._TaskGroupActionsConfig

    @TaskGroupActionsConfig.setter
    def TaskGroupActionsConfig(self, TaskGroupActionsConfig):
        self._TaskGroupActionsConfig = TaskGroupActionsConfig


    def _deserialize(self, params):
        self._TaskGroupInstances = params.get("TaskGroupInstances")
        self._TaskGroupTitle = params.get("TaskGroupTitle")
        self._TaskGroupDescription = params.get("TaskGroupDescription")
        self._TaskGroupMode = params.get("TaskGroupMode")
        if params.get("TaskGroupActionsConfig") is not None:
            self._TaskGroupActionsConfig = []
            for item in params.get("TaskGroupActionsConfig"):
                obj = TaskGroupActionConfig()
                obj._deserialize(item)
                self._TaskGroupActionsConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupForAction(AbstractModel):
    """演练动作组简易配置

    """

    def __init__(self):
        r"""
        :param _TaskActionId: 动作ID
        :type TaskActionId: int
        :param _TaskActionGeneralConfiguration: {"ActionTimeout":1800}
        :type TaskActionGeneralConfiguration: str
        :param _TaskActionCustomConfiguration: {"ip": "0.0.0.0"}
        :type TaskActionCustomConfiguration: str
        """
        self._TaskActionId = None
        self._TaskActionGeneralConfiguration = None
        self._TaskActionCustomConfiguration = None

    @property
    def TaskActionId(self):
        """动作ID
        :rtype: int
        """
        return self._TaskActionId

    @TaskActionId.setter
    def TaskActionId(self, TaskActionId):
        self._TaskActionId = TaskActionId

    @property
    def TaskActionGeneralConfiguration(self):
        """{"ActionTimeout":1800}
        :rtype: str
        """
        return self._TaskActionGeneralConfiguration

    @TaskActionGeneralConfiguration.setter
    def TaskActionGeneralConfiguration(self, TaskActionGeneralConfiguration):
        self._TaskActionGeneralConfiguration = TaskActionGeneralConfiguration

    @property
    def TaskActionCustomConfiguration(self):
        """{"ip": "0.0.0.0"}
        :rtype: str
        """
        return self._TaskActionCustomConfiguration

    @TaskActionCustomConfiguration.setter
    def TaskActionCustomConfiguration(self, TaskActionCustomConfiguration):
        self._TaskActionCustomConfiguration = TaskActionCustomConfiguration


    def _deserialize(self, params):
        self._TaskActionId = params.get("TaskActionId")
        self._TaskActionGeneralConfiguration = params.get("TaskActionGeneralConfiguration")
        self._TaskActionCustomConfiguration = params.get("TaskActionCustomConfiguration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupInstance(AbstractModel):
    """任务分组动作实例

    """

    def __init__(self):
        r"""
        :param _TaskGroupInstanceId: 实例ID
        :type TaskGroupInstanceId: int
        :param _TaskGroupInstanceObjectId: 实例ID
        :type TaskGroupInstanceObjectId: str
        :param _TaskGroupInstanceStatus: 实例动作执行状态
        :type TaskGroupInstanceStatus: int
        :param _TaskGroupInstanceCreateTime: 实例创建时间
        :type TaskGroupInstanceCreateTime: str
        :param _TaskGroupInstanceUpdateTime: 实例更新时间
        :type TaskGroupInstanceUpdateTime: str
        :param _TaskGroupInstanceStatusType: 状态类型: 0 -- 无状态，1 -- 成功，2-- 失败，3--终止，4--跳过
        :type TaskGroupInstanceStatusType: int
        :param _TaskGroupInstanceStartTime: 执行开始时间
        :type TaskGroupInstanceStartTime: str
        :param _TaskGroupInstanceEndTime: 执行结束时间
        :type TaskGroupInstanceEndTime: str
        :param _TaskGroupInstanceExecuteLog: 实例动作执行日志
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskGroupInstanceExecuteLog: str
        :param _TaskGroupInstanceIsRedo: 实例是否可重试
        :type TaskGroupInstanceIsRedo: bool
        :param _TaskGroupInstanceExecuteTime: 动作实例执行时间
        :type TaskGroupInstanceExecuteTime: int
        """
        self._TaskGroupInstanceId = None
        self._TaskGroupInstanceObjectId = None
        self._TaskGroupInstanceStatus = None
        self._TaskGroupInstanceCreateTime = None
        self._TaskGroupInstanceUpdateTime = None
        self._TaskGroupInstanceStatusType = None
        self._TaskGroupInstanceStartTime = None
        self._TaskGroupInstanceEndTime = None
        self._TaskGroupInstanceExecuteLog = None
        self._TaskGroupInstanceIsRedo = None
        self._TaskGroupInstanceExecuteTime = None

    @property
    def TaskGroupInstanceId(self):
        """实例ID
        :rtype: int
        """
        return self._TaskGroupInstanceId

    @TaskGroupInstanceId.setter
    def TaskGroupInstanceId(self, TaskGroupInstanceId):
        self._TaskGroupInstanceId = TaskGroupInstanceId

    @property
    def TaskGroupInstanceObjectId(self):
        """实例ID
        :rtype: str
        """
        return self._TaskGroupInstanceObjectId

    @TaskGroupInstanceObjectId.setter
    def TaskGroupInstanceObjectId(self, TaskGroupInstanceObjectId):
        self._TaskGroupInstanceObjectId = TaskGroupInstanceObjectId

    @property
    def TaskGroupInstanceStatus(self):
        """实例动作执行状态
        :rtype: int
        """
        return self._TaskGroupInstanceStatus

    @TaskGroupInstanceStatus.setter
    def TaskGroupInstanceStatus(self, TaskGroupInstanceStatus):
        self._TaskGroupInstanceStatus = TaskGroupInstanceStatus

    @property
    def TaskGroupInstanceCreateTime(self):
        """实例创建时间
        :rtype: str
        """
        return self._TaskGroupInstanceCreateTime

    @TaskGroupInstanceCreateTime.setter
    def TaskGroupInstanceCreateTime(self, TaskGroupInstanceCreateTime):
        self._TaskGroupInstanceCreateTime = TaskGroupInstanceCreateTime

    @property
    def TaskGroupInstanceUpdateTime(self):
        """实例更新时间
        :rtype: str
        """
        return self._TaskGroupInstanceUpdateTime

    @TaskGroupInstanceUpdateTime.setter
    def TaskGroupInstanceUpdateTime(self, TaskGroupInstanceUpdateTime):
        self._TaskGroupInstanceUpdateTime = TaskGroupInstanceUpdateTime

    @property
    def TaskGroupInstanceStatusType(self):
        """状态类型: 0 -- 无状态，1 -- 成功，2-- 失败，3--终止，4--跳过
        :rtype: int
        """
        return self._TaskGroupInstanceStatusType

    @TaskGroupInstanceStatusType.setter
    def TaskGroupInstanceStatusType(self, TaskGroupInstanceStatusType):
        self._TaskGroupInstanceStatusType = TaskGroupInstanceStatusType

    @property
    def TaskGroupInstanceStartTime(self):
        """执行开始时间
        :rtype: str
        """
        return self._TaskGroupInstanceStartTime

    @TaskGroupInstanceStartTime.setter
    def TaskGroupInstanceStartTime(self, TaskGroupInstanceStartTime):
        self._TaskGroupInstanceStartTime = TaskGroupInstanceStartTime

    @property
    def TaskGroupInstanceEndTime(self):
        """执行结束时间
        :rtype: str
        """
        return self._TaskGroupInstanceEndTime

    @TaskGroupInstanceEndTime.setter
    def TaskGroupInstanceEndTime(self, TaskGroupInstanceEndTime):
        self._TaskGroupInstanceEndTime = TaskGroupInstanceEndTime

    @property
    def TaskGroupInstanceExecuteLog(self):
        warnings.warn("parameter `TaskGroupInstanceExecuteLog` is deprecated", DeprecationWarning) 

        """实例动作执行日志
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskGroupInstanceExecuteLog

    @TaskGroupInstanceExecuteLog.setter
    def TaskGroupInstanceExecuteLog(self, TaskGroupInstanceExecuteLog):
        warnings.warn("parameter `TaskGroupInstanceExecuteLog` is deprecated", DeprecationWarning) 

        self._TaskGroupInstanceExecuteLog = TaskGroupInstanceExecuteLog

    @property
    def TaskGroupInstanceIsRedo(self):
        """实例是否可重试
        :rtype: bool
        """
        return self._TaskGroupInstanceIsRedo

    @TaskGroupInstanceIsRedo.setter
    def TaskGroupInstanceIsRedo(self, TaskGroupInstanceIsRedo):
        self._TaskGroupInstanceIsRedo = TaskGroupInstanceIsRedo

    @property
    def TaskGroupInstanceExecuteTime(self):
        """动作实例执行时间
        :rtype: int
        """
        return self._TaskGroupInstanceExecuteTime

    @TaskGroupInstanceExecuteTime.setter
    def TaskGroupInstanceExecuteTime(self, TaskGroupInstanceExecuteTime):
        self._TaskGroupInstanceExecuteTime = TaskGroupInstanceExecuteTime


    def _deserialize(self, params):
        self._TaskGroupInstanceId = params.get("TaskGroupInstanceId")
        self._TaskGroupInstanceObjectId = params.get("TaskGroupInstanceObjectId")
        self._TaskGroupInstanceStatus = params.get("TaskGroupInstanceStatus")
        self._TaskGroupInstanceCreateTime = params.get("TaskGroupInstanceCreateTime")
        self._TaskGroupInstanceUpdateTime = params.get("TaskGroupInstanceUpdateTime")
        self._TaskGroupInstanceStatusType = params.get("TaskGroupInstanceStatusType")
        self._TaskGroupInstanceStartTime = params.get("TaskGroupInstanceStartTime")
        self._TaskGroupInstanceEndTime = params.get("TaskGroupInstanceEndTime")
        self._TaskGroupInstanceExecuteLog = params.get("TaskGroupInstanceExecuteLog")
        self._TaskGroupInstanceIsRedo = params.get("TaskGroupInstanceIsRedo")
        self._TaskGroupInstanceExecuteTime = params.get("TaskGroupInstanceExecuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskGroupInstancesExecuteRules(AbstractModel):
    """机器选取规则

    """

    def __init__(self):
        r"""
        :param _TaskGroupInstancesExecuteMode: 实例选取模式
        :type TaskGroupInstancesExecuteMode: int
        :param _TaskGroupInstancesExecutePercent: 按比例选取模式下选取比例
        :type TaskGroupInstancesExecutePercent: int
        :param _TaskGroupInstancesExecuteNum: 按数量选取模式下选取数量
        :type TaskGroupInstancesExecuteNum: int
        """
        self._TaskGroupInstancesExecuteMode = None
        self._TaskGroupInstancesExecutePercent = None
        self._TaskGroupInstancesExecuteNum = None

    @property
    def TaskGroupInstancesExecuteMode(self):
        """实例选取模式
        :rtype: int
        """
        return self._TaskGroupInstancesExecuteMode

    @TaskGroupInstancesExecuteMode.setter
    def TaskGroupInstancesExecuteMode(self, TaskGroupInstancesExecuteMode):
        self._TaskGroupInstancesExecuteMode = TaskGroupInstancesExecuteMode

    @property
    def TaskGroupInstancesExecutePercent(self):
        """按比例选取模式下选取比例
        :rtype: int
        """
        return self._TaskGroupInstancesExecutePercent

    @TaskGroupInstancesExecutePercent.setter
    def TaskGroupInstancesExecutePercent(self, TaskGroupInstancesExecutePercent):
        self._TaskGroupInstancesExecutePercent = TaskGroupInstancesExecutePercent

    @property
    def TaskGroupInstancesExecuteNum(self):
        """按数量选取模式下选取数量
        :rtype: int
        """
        return self._TaskGroupInstancesExecuteNum

    @TaskGroupInstancesExecuteNum.setter
    def TaskGroupInstancesExecuteNum(self, TaskGroupInstancesExecuteNum):
        self._TaskGroupInstancesExecuteNum = TaskGroupInstancesExecuteNum


    def _deserialize(self, params):
        self._TaskGroupInstancesExecuteMode = params.get("TaskGroupInstancesExecuteMode")
        self._TaskGroupInstancesExecutePercent = params.get("TaskGroupInstancesExecutePercent")
        self._TaskGroupInstancesExecuteNum = params.get("TaskGroupInstancesExecuteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskListItem(AbstractModel):
    """任务列表信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _TaskTitle: 任务标题
        :type TaskTitle: str
        :param _TaskDescription: 任务描述
        :type TaskDescription: str
        :param _TaskTag: 任务标签
        :type TaskTag: str
        :param _TaskStatus: 任务状态(1001 -- 未开始   1002 -- 进行中  1003 -- 暂停中   1004 -- 任务结束)
        :type TaskStatus: int
        :param _TaskCreateTime: 任务创建时间
        :type TaskCreateTime: str
        :param _TaskUpdateTime: 任务更新时间
        :type TaskUpdateTime: str
        :param _TaskPreCheckStatus: 0--未开始，1--进行中，2--已完成
        :type TaskPreCheckStatus: int
        :param _TaskPreCheckSuccess: 环境检查是否通过
        :type TaskPreCheckSuccess: bool
        :param _TaskExpect: 演练是否符合预期 1-符合预期 2-不符合预期
        :type TaskExpect: int
        :param _ApplicationId: 关联应用ID
        :type ApplicationId: str
        :param _ApplicationName: 关联应用名称
        :type ApplicationName: str
        :param _VerifyId: 验证项ID
        :type VerifyId: int
        :param _TaskStatusType: 状态类型: 0 -- 无状态，1 -- 成功，2-- 失败，3--终止
        :type TaskStatusType: int
        :param _ArchId: 架构ID
        :type ArchId: str
        :param _ArchName: 架构名称
        :type ArchName: str
        """
        self._TaskId = None
        self._TaskTitle = None
        self._TaskDescription = None
        self._TaskTag = None
        self._TaskStatus = None
        self._TaskCreateTime = None
        self._TaskUpdateTime = None
        self._TaskPreCheckStatus = None
        self._TaskPreCheckSuccess = None
        self._TaskExpect = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._VerifyId = None
        self._TaskStatusType = None
        self._ArchId = None
        self._ArchName = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskTitle(self):
        """任务标题
        :rtype: str
        """
        return self._TaskTitle

    @TaskTitle.setter
    def TaskTitle(self, TaskTitle):
        self._TaskTitle = TaskTitle

    @property
    def TaskDescription(self):
        """任务描述
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def TaskTag(self):
        """任务标签
        :rtype: str
        """
        return self._TaskTag

    @TaskTag.setter
    def TaskTag(self, TaskTag):
        self._TaskTag = TaskTag

    @property
    def TaskStatus(self):
        """任务状态(1001 -- 未开始   1002 -- 进行中  1003 -- 暂停中   1004 -- 任务结束)
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskCreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._TaskCreateTime

    @TaskCreateTime.setter
    def TaskCreateTime(self, TaskCreateTime):
        self._TaskCreateTime = TaskCreateTime

    @property
    def TaskUpdateTime(self):
        """任务更新时间
        :rtype: str
        """
        return self._TaskUpdateTime

    @TaskUpdateTime.setter
    def TaskUpdateTime(self, TaskUpdateTime):
        self._TaskUpdateTime = TaskUpdateTime

    @property
    def TaskPreCheckStatus(self):
        """0--未开始，1--进行中，2--已完成
        :rtype: int
        """
        return self._TaskPreCheckStatus

    @TaskPreCheckStatus.setter
    def TaskPreCheckStatus(self, TaskPreCheckStatus):
        self._TaskPreCheckStatus = TaskPreCheckStatus

    @property
    def TaskPreCheckSuccess(self):
        """环境检查是否通过
        :rtype: bool
        """
        return self._TaskPreCheckSuccess

    @TaskPreCheckSuccess.setter
    def TaskPreCheckSuccess(self, TaskPreCheckSuccess):
        self._TaskPreCheckSuccess = TaskPreCheckSuccess

    @property
    def TaskExpect(self):
        """演练是否符合预期 1-符合预期 2-不符合预期
        :rtype: int
        """
        return self._TaskExpect

    @TaskExpect.setter
    def TaskExpect(self, TaskExpect):
        self._TaskExpect = TaskExpect

    @property
    def ApplicationId(self):
        """关联应用ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """关联应用名称
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def VerifyId(self):
        """验证项ID
        :rtype: int
        """
        return self._VerifyId

    @VerifyId.setter
    def VerifyId(self, VerifyId):
        self._VerifyId = VerifyId

    @property
    def TaskStatusType(self):
        """状态类型: 0 -- 无状态，1 -- 成功，2-- 失败，3--终止
        :rtype: int
        """
        return self._TaskStatusType

    @TaskStatusType.setter
    def TaskStatusType(self, TaskStatusType):
        self._TaskStatusType = TaskStatusType

    @property
    def ArchId(self):
        """架构ID
        :rtype: str
        """
        return self._ArchId

    @ArchId.setter
    def ArchId(self, ArchId):
        self._ArchId = ArchId

    @property
    def ArchName(self):
        """架构名称
        :rtype: str
        """
        return self._ArchName

    @ArchName.setter
    def ArchName(self, ArchName):
        self._ArchName = ArchName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskTitle = params.get("TaskTitle")
        self._TaskDescription = params.get("TaskDescription")
        self._TaskTag = params.get("TaskTag")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskCreateTime = params.get("TaskCreateTime")
        self._TaskUpdateTime = params.get("TaskUpdateTime")
        self._TaskPreCheckStatus = params.get("TaskPreCheckStatus")
        self._TaskPreCheckSuccess = params.get("TaskPreCheckSuccess")
        self._TaskExpect = params.get("TaskExpect")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._VerifyId = params.get("VerifyId")
        self._TaskStatusType = params.get("TaskStatusType")
        self._ArchId = params.get("ArchId")
        self._ArchName = params.get("ArchName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskMonitor(AbstractModel):
    """监控指标

    """

    def __init__(self):
        r"""
        :param _TaskMonitorId: 演练监控指标ID
        :type TaskMonitorId: int
        :param _MetricId: 监控指标ID
        :type MetricId: int
        :param _TaskMonitorObjectTypeId: 监控指标对象类型ID
        :type TaskMonitorObjectTypeId: int
        :param _MetricName: 指标名称
        :type MetricName: str
        :param _InstancesIds: 实例ID列表
        :type InstancesIds: list of str
        :param _MetricChineseName: 中文指标
        :type MetricChineseName: str
        :param _Unit: 单位
        :type Unit: str
        """
        self._TaskMonitorId = None
        self._MetricId = None
        self._TaskMonitorObjectTypeId = None
        self._MetricName = None
        self._InstancesIds = None
        self._MetricChineseName = None
        self._Unit = None

    @property
    def TaskMonitorId(self):
        """演练监控指标ID
        :rtype: int
        """
        return self._TaskMonitorId

    @TaskMonitorId.setter
    def TaskMonitorId(self, TaskMonitorId):
        self._TaskMonitorId = TaskMonitorId

    @property
    def MetricId(self):
        """监控指标ID
        :rtype: int
        """
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def TaskMonitorObjectTypeId(self):
        """监控指标对象类型ID
        :rtype: int
        """
        return self._TaskMonitorObjectTypeId

    @TaskMonitorObjectTypeId.setter
    def TaskMonitorObjectTypeId(self, TaskMonitorObjectTypeId):
        self._TaskMonitorObjectTypeId = TaskMonitorObjectTypeId

    @property
    def MetricName(self):
        """指标名称
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def InstancesIds(self):
        """实例ID列表
        :rtype: list of str
        """
        return self._InstancesIds

    @InstancesIds.setter
    def InstancesIds(self, InstancesIds):
        self._InstancesIds = InstancesIds

    @property
    def MetricChineseName(self):
        """中文指标
        :rtype: str
        """
        return self._MetricChineseName

    @MetricChineseName.setter
    def MetricChineseName(self, MetricChineseName):
        self._MetricChineseName = MetricChineseName

    @property
    def Unit(self):
        """单位
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._TaskMonitorId = params.get("TaskMonitorId")
        self._MetricId = params.get("MetricId")
        self._TaskMonitorObjectTypeId = params.get("TaskMonitorObjectTypeId")
        self._MetricName = params.get("MetricName")
        self._InstancesIds = params.get("InstancesIds")
        self._MetricChineseName = params.get("MetricChineseName")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOrg(AbstractModel):
    """演练人员组织

    """

    def __init__(self):
        r"""
        :param _TaskRole: 演练角色
        :type TaskRole: str
        :param _TaskOperator: 负责人
        :type TaskOperator: str
        """
        self._TaskRole = None
        self._TaskOperator = None

    @property
    def TaskRole(self):
        """演练角色
        :rtype: str
        """
        return self._TaskRole

    @TaskRole.setter
    def TaskRole(self, TaskRole):
        self._TaskRole = TaskRole

    @property
    def TaskOperator(self):
        """负责人
        :rtype: str
        """
        return self._TaskOperator

    @TaskOperator.setter
    def TaskOperator(self, TaskOperator):
        self._TaskOperator = TaskOperator


    def _deserialize(self, params):
        self._TaskRole = params.get("TaskRole")
        self._TaskOperator = params.get("TaskOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskReportInfo(AbstractModel):
    """演练报告状态信息

    """

    def __init__(self):
        r"""
        :param _Stage: 0--未开始，1--正在导出，2--导出成功，3--导出失败
        :type Stage: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ExpirationTime: 有效期截止时间
        :type ExpirationTime: str
        :param _Expired: 是否有效
        :type Expired: bool
        :param _CosUrl: 演练报告cos文件地址
        :type CosUrl: str
        :param _Log: 演练报告导出日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: str
        :param _ArchiveStage: 0--未开始，1--正在归档，2--归档成功，3--归档失败
        :type ArchiveStage: int
        :param _ArchiveTime: 归档时间
        :type ArchiveTime: str
        :param _ArchiveUuid: 归档ID
        :type ArchiveUuid: str
        """
        self._Stage = None
        self._CreateTime = None
        self._ExpirationTime = None
        self._Expired = None
        self._CosUrl = None
        self._Log = None
        self._ArchiveStage = None
        self._ArchiveTime = None
        self._ArchiveUuid = None

    @property
    def Stage(self):
        """0--未开始，1--正在导出，2--导出成功，3--导出失败
        :rtype: int
        """
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

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
    def ExpirationTime(self):
        """有效期截止时间
        :rtype: str
        """
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime

    @property
    def Expired(self):
        """是否有效
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def CosUrl(self):
        """演练报告cos文件地址
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def Log(self):
        """演练报告导出日志
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def ArchiveStage(self):
        """0--未开始，1--正在归档，2--归档成功，3--归档失败
        :rtype: int
        """
        return self._ArchiveStage

    @ArchiveStage.setter
    def ArchiveStage(self, ArchiveStage):
        self._ArchiveStage = ArchiveStage

    @property
    def ArchiveTime(self):
        """归档时间
        :rtype: str
        """
        return self._ArchiveTime

    @ArchiveTime.setter
    def ArchiveTime(self, ArchiveTime):
        self._ArchiveTime = ArchiveTime

    @property
    def ArchiveUuid(self):
        """归档ID
        :rtype: str
        """
        return self._ArchiveUuid

    @ArchiveUuid.setter
    def ArchiveUuid(self, ArchiveUuid):
        self._ArchiveUuid = ArchiveUuid


    def _deserialize(self, params):
        self._Stage = params.get("Stage")
        self._CreateTime = params.get("CreateTime")
        self._ExpirationTime = params.get("ExpirationTime")
        self._Expired = params.get("Expired")
        self._CosUrl = params.get("CosUrl")
        self._Log = params.get("Log")
        self._ArchiveStage = params.get("ArchiveStage")
        self._ArchiveTime = params.get("ArchiveTime")
        self._ArchiveUuid = params.get("ArchiveUuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskTarget(AbstractModel):
    """演练目标

    """

    def __init__(self):
        r"""
        :param _TargetId: 目标标签ID
        :type TargetId: int
        :param _TargetDesc: 目标描述
        :type TargetDesc: str
        :param _Type: 1:演练场景
2:演练目标
        :type Type: int
        :param _Source: 1:平台 2:用户个人
        :type Source: int
        """
        self._TargetId = None
        self._TargetDesc = None
        self._Type = None
        self._Source = None

    @property
    def TargetId(self):
        """目标标签ID
        :rtype: int
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetDesc(self):
        """目标描述
        :rtype: str
        """
        return self._TargetDesc

    @TargetDesc.setter
    def TargetDesc(self, TargetDesc):
        self._TargetDesc = TargetDesc

    @property
    def Type(self):
        """1:演练场景
2:演练目标
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Source(self):
        """1:平台 2:用户个人
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._TargetDesc = params.get("TargetDesc")
        self._Type = params.get("Type")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """经验库

    """

    def __init__(self):
        r"""
        :param _TemplateId: 经验库ID
        :type TemplateId: int
        :param _TemplateTitle: 经验库标题
        :type TemplateTitle: str
        :param _TemplateDescription: 经验库描述
        :type TemplateDescription: str
        :param _TemplateTag: 自定义标签
        :type TemplateTag: str
        :param _TemplateIsUsed: 使用状态。1 ---- 使用中，2 --- 停用
        :type TemplateIsUsed: int
        :param _TemplateCreateTime: 经验库创建时间
        :type TemplateCreateTime: str
        :param _TemplateUpdateTime: 经验库更新时间
        :type TemplateUpdateTime: str
        :param _TemplateMode: 经验库模式。1:手工执行，2:自动执行
        :type TemplateMode: int
        :param _TemplatePauseDuration: 自动暂停时长。单位分钟
        :type TemplatePauseDuration: int
        :param _TemplateOwnerUin: 演练创建者Uin
        :type TemplateOwnerUin: str
        :param _TemplateRegionId: 地域ID
        :type TemplateRegionId: int
        :param _TemplateGroups: 动作组
        :type TemplateGroups: list of TemplateGroup
        :param _TemplateMonitors: 监控指标
        :type TemplateMonitors: list of TemplateMonitor
        :param _TemplatePolicy: 护栏监控
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplatePolicy: :class:`tencentcloud.cfg.v20210820.models.TemplatePolicy`
        :param _Tags: 标签列表
        :type Tags: list of TagWithDescribe
        :param _TemplateSource: 经验来源 0-自建 1-专家推荐
        :type TemplateSource: int
        :param _ApmServiceList: apm应用信息
        :type ApmServiceList: list of ApmServiceInfo
        :param _AlarmPolicy: 告警指标
        :type AlarmPolicy: list of str
        :param _PolicyDealType: 护栏处理方式，1--顺序回滚，2--演练暂停
        :type PolicyDealType: int
        """
        self._TemplateId = None
        self._TemplateTitle = None
        self._TemplateDescription = None
        self._TemplateTag = None
        self._TemplateIsUsed = None
        self._TemplateCreateTime = None
        self._TemplateUpdateTime = None
        self._TemplateMode = None
        self._TemplatePauseDuration = None
        self._TemplateOwnerUin = None
        self._TemplateRegionId = None
        self._TemplateGroups = None
        self._TemplateMonitors = None
        self._TemplatePolicy = None
        self._Tags = None
        self._TemplateSource = None
        self._ApmServiceList = None
        self._AlarmPolicy = None
        self._PolicyDealType = None

    @property
    def TemplateId(self):
        """经验库ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateTitle(self):
        """经验库标题
        :rtype: str
        """
        return self._TemplateTitle

    @TemplateTitle.setter
    def TemplateTitle(self, TemplateTitle):
        self._TemplateTitle = TemplateTitle

    @property
    def TemplateDescription(self):
        """经验库描述
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def TemplateTag(self):
        """自定义标签
        :rtype: str
        """
        return self._TemplateTag

    @TemplateTag.setter
    def TemplateTag(self, TemplateTag):
        self._TemplateTag = TemplateTag

    @property
    def TemplateIsUsed(self):
        """使用状态。1 ---- 使用中，2 --- 停用
        :rtype: int
        """
        return self._TemplateIsUsed

    @TemplateIsUsed.setter
    def TemplateIsUsed(self, TemplateIsUsed):
        self._TemplateIsUsed = TemplateIsUsed

    @property
    def TemplateCreateTime(self):
        """经验库创建时间
        :rtype: str
        """
        return self._TemplateCreateTime

    @TemplateCreateTime.setter
    def TemplateCreateTime(self, TemplateCreateTime):
        self._TemplateCreateTime = TemplateCreateTime

    @property
    def TemplateUpdateTime(self):
        """经验库更新时间
        :rtype: str
        """
        return self._TemplateUpdateTime

    @TemplateUpdateTime.setter
    def TemplateUpdateTime(self, TemplateUpdateTime):
        self._TemplateUpdateTime = TemplateUpdateTime

    @property
    def TemplateMode(self):
        """经验库模式。1:手工执行，2:自动执行
        :rtype: int
        """
        return self._TemplateMode

    @TemplateMode.setter
    def TemplateMode(self, TemplateMode):
        self._TemplateMode = TemplateMode

    @property
    def TemplatePauseDuration(self):
        """自动暂停时长。单位分钟
        :rtype: int
        """
        return self._TemplatePauseDuration

    @TemplatePauseDuration.setter
    def TemplatePauseDuration(self, TemplatePauseDuration):
        self._TemplatePauseDuration = TemplatePauseDuration

    @property
    def TemplateOwnerUin(self):
        """演练创建者Uin
        :rtype: str
        """
        return self._TemplateOwnerUin

    @TemplateOwnerUin.setter
    def TemplateOwnerUin(self, TemplateOwnerUin):
        self._TemplateOwnerUin = TemplateOwnerUin

    @property
    def TemplateRegionId(self):
        """地域ID
        :rtype: int
        """
        return self._TemplateRegionId

    @TemplateRegionId.setter
    def TemplateRegionId(self, TemplateRegionId):
        self._TemplateRegionId = TemplateRegionId

    @property
    def TemplateGroups(self):
        """动作组
        :rtype: list of TemplateGroup
        """
        return self._TemplateGroups

    @TemplateGroups.setter
    def TemplateGroups(self, TemplateGroups):
        self._TemplateGroups = TemplateGroups

    @property
    def TemplateMonitors(self):
        """监控指标
        :rtype: list of TemplateMonitor
        """
        return self._TemplateMonitors

    @TemplateMonitors.setter
    def TemplateMonitors(self, TemplateMonitors):
        self._TemplateMonitors = TemplateMonitors

    @property
    def TemplatePolicy(self):
        """护栏监控
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cfg.v20210820.models.TemplatePolicy`
        """
        return self._TemplatePolicy

    @TemplatePolicy.setter
    def TemplatePolicy(self, TemplatePolicy):
        self._TemplatePolicy = TemplatePolicy

    @property
    def Tags(self):
        """标签列表
        :rtype: list of TagWithDescribe
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TemplateSource(self):
        """经验来源 0-自建 1-专家推荐
        :rtype: int
        """
        return self._TemplateSource

    @TemplateSource.setter
    def TemplateSource(self, TemplateSource):
        self._TemplateSource = TemplateSource

    @property
    def ApmServiceList(self):
        """apm应用信息
        :rtype: list of ApmServiceInfo
        """
        return self._ApmServiceList

    @ApmServiceList.setter
    def ApmServiceList(self, ApmServiceList):
        self._ApmServiceList = ApmServiceList

    @property
    def AlarmPolicy(self):
        """告警指标
        :rtype: list of str
        """
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy

    @property
    def PolicyDealType(self):
        """护栏处理方式，1--顺序回滚，2--演练暂停
        :rtype: int
        """
        return self._PolicyDealType

    @PolicyDealType.setter
    def PolicyDealType(self, PolicyDealType):
        self._PolicyDealType = PolicyDealType


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateTitle = params.get("TemplateTitle")
        self._TemplateDescription = params.get("TemplateDescription")
        self._TemplateTag = params.get("TemplateTag")
        self._TemplateIsUsed = params.get("TemplateIsUsed")
        self._TemplateCreateTime = params.get("TemplateCreateTime")
        self._TemplateUpdateTime = params.get("TemplateUpdateTime")
        self._TemplateMode = params.get("TemplateMode")
        self._TemplatePauseDuration = params.get("TemplatePauseDuration")
        self._TemplateOwnerUin = params.get("TemplateOwnerUin")
        self._TemplateRegionId = params.get("TemplateRegionId")
        if params.get("TemplateGroups") is not None:
            self._TemplateGroups = []
            for item in params.get("TemplateGroups"):
                obj = TemplateGroup()
                obj._deserialize(item)
                self._TemplateGroups.append(obj)
        if params.get("TemplateMonitors") is not None:
            self._TemplateMonitors = []
            for item in params.get("TemplateMonitors"):
                obj = TemplateMonitor()
                obj._deserialize(item)
                self._TemplateMonitors.append(obj)
        if params.get("TemplatePolicy") is not None:
            self._TemplatePolicy = TemplatePolicy()
            self._TemplatePolicy._deserialize(params.get("TemplatePolicy"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDescribe()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TemplateSource = params.get("TemplateSource")
        if params.get("ApmServiceList") is not None:
            self._ApmServiceList = []
            for item in params.get("ApmServiceList"):
                obj = ApmServiceInfo()
                obj._deserialize(item)
                self._ApmServiceList.append(obj)
        self._AlarmPolicy = params.get("AlarmPolicy")
        self._PolicyDealType = params.get("PolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroup(AbstractModel):
    """任务分组

    """

    def __init__(self):
        r"""
        :param _TemplateGroupId: 经验库动作ID
        :type TemplateGroupId: int
        :param _TemplateGroupActions: 经验库动作分组动作列表
        :type TemplateGroupActions: list of TemplateGroupAction
        :param _Title: 分组标题
        :type Title: str
        :param _Description: 分组描述
        :type Description: str
        :param _Order: 分组顺序
        :type Order: int
        :param _Mode: 执行模式。1 --- 顺序执行，2 --- 阶段执行
        :type Mode: int
        :param _ObjectTypeId: 对象类型ID
        :type ObjectTypeId: int
        :param _CreateTime: 分组创建时间
        :type CreateTime: str
        :param _UpdateTime: 分组更新时间
        :type UpdateTime: str
        """
        self._TemplateGroupId = None
        self._TemplateGroupActions = None
        self._Title = None
        self._Description = None
        self._Order = None
        self._Mode = None
        self._ObjectTypeId = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def TemplateGroupId(self):
        """经验库动作ID
        :rtype: int
        """
        return self._TemplateGroupId

    @TemplateGroupId.setter
    def TemplateGroupId(self, TemplateGroupId):
        self._TemplateGroupId = TemplateGroupId

    @property
    def TemplateGroupActions(self):
        """经验库动作分组动作列表
        :rtype: list of TemplateGroupAction
        """
        return self._TemplateGroupActions

    @TemplateGroupActions.setter
    def TemplateGroupActions(self, TemplateGroupActions):
        self._TemplateGroupActions = TemplateGroupActions

    @property
    def Title(self):
        """分组标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Description(self):
        """分组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Order(self):
        """分组顺序
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Mode(self):
        """执行模式。1 --- 顺序执行，2 --- 阶段执行
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ObjectTypeId(self):
        """对象类型ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId

    @property
    def CreateTime(self):
        """分组创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """分组更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TemplateGroupId = params.get("TemplateGroupId")
        if params.get("TemplateGroupActions") is not None:
            self._TemplateGroupActions = []
            for item in params.get("TemplateGroupActions"):
                obj = TemplateGroupAction()
                obj._deserialize(item)
                self._TemplateGroupActions.append(obj)
        self._Title = params.get("Title")
        self._Description = params.get("Description")
        self._Order = params.get("Order")
        self._Mode = params.get("Mode")
        self._ObjectTypeId = params.get("ObjectTypeId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroupAction(AbstractModel):
    """任务分组动作

    """

    def __init__(self):
        r"""
        :param _TemplateGroupActionId: 经验库分组动作ID
        :type TemplateGroupActionId: int
        :param _ActionId: 动作ID
        :type ActionId: int
        :param _Order: 分组动作顺序
        :type Order: int
        :param _GeneralConfiguration: 分组动作通用配置
        :type GeneralConfiguration: str
        :param _CustomConfiguration: 分组动作自定义配置
        :type CustomConfiguration: str
        :param _CreateTime: 动作分组创建时间
        :type CreateTime: str
        :param _UpdateTime: 动作分组更新时间
        :type UpdateTime: str
        :param _ActionTitle: 动作名称
        :type ActionTitle: str
        :param _RandomId: 自身随机id
        :type RandomId: int
        :param _RecoverId: 恢复动作id
        :type RecoverId: int
        :param _ExecuteId: 执行动作id
        :type ExecuteId: int
        :param _ActionApiType: 调用api类型，0:tat, 1:云api
        :type ActionApiType: int
        :param _ActionAttribute: 1:故障，2:恢复
        :type ActionAttribute: int
        :param _ActionType: 动作类型：平台和自定义
        :type ActionType: str
        :param _ActionRisk: 动作风险等级，1:低风险 2:中风险 3:高风险
        :type ActionRisk: str
        :param _FailurePerformance: 故障表现
        :type FailurePerformance: str
        """
        self._TemplateGroupActionId = None
        self._ActionId = None
        self._Order = None
        self._GeneralConfiguration = None
        self._CustomConfiguration = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ActionTitle = None
        self._RandomId = None
        self._RecoverId = None
        self._ExecuteId = None
        self._ActionApiType = None
        self._ActionAttribute = None
        self._ActionType = None
        self._ActionRisk = None
        self._FailurePerformance = None

    @property
    def TemplateGroupActionId(self):
        """经验库分组动作ID
        :rtype: int
        """
        return self._TemplateGroupActionId

    @TemplateGroupActionId.setter
    def TemplateGroupActionId(self, TemplateGroupActionId):
        self._TemplateGroupActionId = TemplateGroupActionId

    @property
    def ActionId(self):
        """动作ID
        :rtype: int
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def Order(self):
        """分组动作顺序
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def GeneralConfiguration(self):
        """分组动作通用配置
        :rtype: str
        """
        return self._GeneralConfiguration

    @GeneralConfiguration.setter
    def GeneralConfiguration(self, GeneralConfiguration):
        self._GeneralConfiguration = GeneralConfiguration

    @property
    def CustomConfiguration(self):
        """分组动作自定义配置
        :rtype: str
        """
        return self._CustomConfiguration

    @CustomConfiguration.setter
    def CustomConfiguration(self, CustomConfiguration):
        self._CustomConfiguration = CustomConfiguration

    @property
    def CreateTime(self):
        """动作分组创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """动作分组更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ActionTitle(self):
        """动作名称
        :rtype: str
        """
        return self._ActionTitle

    @ActionTitle.setter
    def ActionTitle(self, ActionTitle):
        self._ActionTitle = ActionTitle

    @property
    def RandomId(self):
        """自身随机id
        :rtype: int
        """
        return self._RandomId

    @RandomId.setter
    def RandomId(self, RandomId):
        self._RandomId = RandomId

    @property
    def RecoverId(self):
        """恢复动作id
        :rtype: int
        """
        return self._RecoverId

    @RecoverId.setter
    def RecoverId(self, RecoverId):
        self._RecoverId = RecoverId

    @property
    def ExecuteId(self):
        """执行动作id
        :rtype: int
        """
        return self._ExecuteId

    @ExecuteId.setter
    def ExecuteId(self, ExecuteId):
        self._ExecuteId = ExecuteId

    @property
    def ActionApiType(self):
        """调用api类型，0:tat, 1:云api
        :rtype: int
        """
        return self._ActionApiType

    @ActionApiType.setter
    def ActionApiType(self, ActionApiType):
        self._ActionApiType = ActionApiType

    @property
    def ActionAttribute(self):
        """1:故障，2:恢复
        :rtype: int
        """
        return self._ActionAttribute

    @ActionAttribute.setter
    def ActionAttribute(self, ActionAttribute):
        self._ActionAttribute = ActionAttribute

    @property
    def ActionType(self):
        """动作类型：平台和自定义
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionRisk(self):
        """动作风险等级，1:低风险 2:中风险 3:高风险
        :rtype: str
        """
        return self._ActionRisk

    @ActionRisk.setter
    def ActionRisk(self, ActionRisk):
        self._ActionRisk = ActionRisk

    @property
    def FailurePerformance(self):
        """故障表现
        :rtype: str
        """
        return self._FailurePerformance

    @FailurePerformance.setter
    def FailurePerformance(self, FailurePerformance):
        self._FailurePerformance = FailurePerformance


    def _deserialize(self, params):
        self._TemplateGroupActionId = params.get("TemplateGroupActionId")
        self._ActionId = params.get("ActionId")
        self._Order = params.get("Order")
        self._GeneralConfiguration = params.get("GeneralConfiguration")
        self._CustomConfiguration = params.get("CustomConfiguration")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ActionTitle = params.get("ActionTitle")
        self._RandomId = params.get("RandomId")
        self._RecoverId = params.get("RecoverId")
        self._ExecuteId = params.get("ExecuteId")
        self._ActionApiType = params.get("ActionApiType")
        self._ActionAttribute = params.get("ActionAttribute")
        self._ActionType = params.get("ActionType")
        self._ActionRisk = params.get("ActionRisk")
        self._FailurePerformance = params.get("FailurePerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateListItem(AbstractModel):
    """经验库列表信息

    """

    def __init__(self):
        r"""
        :param _TemplateId: 经验库ID
        :type TemplateId: int
        :param _TemplateTitle: 经验库标题
        :type TemplateTitle: str
        :param _TemplateDescription: 经验库描述
        :type TemplateDescription: str
        :param _TemplateTag: 经验库标签
        :type TemplateTag: str
        :param _TemplateIsUsed: 经验库状态。1 -- 使用中，2 -- 停用
        :type TemplateIsUsed: int
        :param _TemplateCreateTime: 经验库创建时间
        :type TemplateCreateTime: str
        :param _TemplateUpdateTime: 经验库更新时间
        :type TemplateUpdateTime: str
        :param _TemplateUsedNum: 经验库关联的任务数量
        :type TemplateUsedNum: int
        :param _TemplateSource: 经验库来源 0-自建经验 1-专家推荐
        :type TemplateSource: int
        """
        self._TemplateId = None
        self._TemplateTitle = None
        self._TemplateDescription = None
        self._TemplateTag = None
        self._TemplateIsUsed = None
        self._TemplateCreateTime = None
        self._TemplateUpdateTime = None
        self._TemplateUsedNum = None
        self._TemplateSource = None

    @property
    def TemplateId(self):
        """经验库ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateTitle(self):
        """经验库标题
        :rtype: str
        """
        return self._TemplateTitle

    @TemplateTitle.setter
    def TemplateTitle(self, TemplateTitle):
        self._TemplateTitle = TemplateTitle

    @property
    def TemplateDescription(self):
        """经验库描述
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def TemplateTag(self):
        """经验库标签
        :rtype: str
        """
        return self._TemplateTag

    @TemplateTag.setter
    def TemplateTag(self, TemplateTag):
        self._TemplateTag = TemplateTag

    @property
    def TemplateIsUsed(self):
        """经验库状态。1 -- 使用中，2 -- 停用
        :rtype: int
        """
        return self._TemplateIsUsed

    @TemplateIsUsed.setter
    def TemplateIsUsed(self, TemplateIsUsed):
        self._TemplateIsUsed = TemplateIsUsed

    @property
    def TemplateCreateTime(self):
        """经验库创建时间
        :rtype: str
        """
        return self._TemplateCreateTime

    @TemplateCreateTime.setter
    def TemplateCreateTime(self, TemplateCreateTime):
        self._TemplateCreateTime = TemplateCreateTime

    @property
    def TemplateUpdateTime(self):
        """经验库更新时间
        :rtype: str
        """
        return self._TemplateUpdateTime

    @TemplateUpdateTime.setter
    def TemplateUpdateTime(self, TemplateUpdateTime):
        self._TemplateUpdateTime = TemplateUpdateTime

    @property
    def TemplateUsedNum(self):
        """经验库关联的任务数量
        :rtype: int
        """
        return self._TemplateUsedNum

    @TemplateUsedNum.setter
    def TemplateUsedNum(self, TemplateUsedNum):
        self._TemplateUsedNum = TemplateUsedNum

    @property
    def TemplateSource(self):
        """经验库来源 0-自建经验 1-专家推荐
        :rtype: int
        """
        return self._TemplateSource

    @TemplateSource.setter
    def TemplateSource(self, TemplateSource):
        self._TemplateSource = TemplateSource


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateTitle = params.get("TemplateTitle")
        self._TemplateDescription = params.get("TemplateDescription")
        self._TemplateTag = params.get("TemplateTag")
        self._TemplateIsUsed = params.get("TemplateIsUsed")
        self._TemplateCreateTime = params.get("TemplateCreateTime")
        self._TemplateUpdateTime = params.get("TemplateUpdateTime")
        self._TemplateUsedNum = params.get("TemplateUsedNum")
        self._TemplateSource = params.get("TemplateSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateMonitor(AbstractModel):
    """监控指标

    """

    def __init__(self):
        r"""
        :param _MonitorId: pk
        :type MonitorId: int
        :param _MetricId: 监控指标ID
        :type MetricId: int
        :param _ObjectTypeId: 监控指标对象类型ID
        :type ObjectTypeId: int
        :param _MetricName: 指标名称
        :type MetricName: str
        :param _MetricChineseName: 中文指标
        :type MetricChineseName: str
        """
        self._MonitorId = None
        self._MetricId = None
        self._ObjectTypeId = None
        self._MetricName = None
        self._MetricChineseName = None

    @property
    def MonitorId(self):
        """pk
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def MetricId(self):
        """监控指标ID
        :rtype: int
        """
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def ObjectTypeId(self):
        """监控指标对象类型ID
        :rtype: int
        """
        return self._ObjectTypeId

    @ObjectTypeId.setter
    def ObjectTypeId(self, ObjectTypeId):
        self._ObjectTypeId = ObjectTypeId

    @property
    def MetricName(self):
        """指标名称
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricChineseName(self):
        """中文指标
        :rtype: str
        """
        return self._MetricChineseName

    @MetricChineseName.setter
    def MetricChineseName(self, MetricChineseName):
        self._MetricChineseName = MetricChineseName


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._MetricId = params.get("MetricId")
        self._ObjectTypeId = params.get("ObjectTypeId")
        self._MetricName = params.get("MetricName")
        self._MetricChineseName = params.get("MetricChineseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplatePolicy(AbstractModel):
    """保护策略

    """

    def __init__(self):
        r"""
        :param _TemplatePolicyIdList: 保护策略ID列表
        :type TemplatePolicyIdList: list of str
        :param _TemplatePolicyRule: 策略规则
        :type TemplatePolicyRule: str
        :param _TemplatePolicyDealType: 护栏策略生效处理策略 1:顺序执行，2:暂停
        :type TemplatePolicyDealType: int
        """
        self._TemplatePolicyIdList = None
        self._TemplatePolicyRule = None
        self._TemplatePolicyDealType = None

    @property
    def TemplatePolicyIdList(self):
        """保护策略ID列表
        :rtype: list of str
        """
        return self._TemplatePolicyIdList

    @TemplatePolicyIdList.setter
    def TemplatePolicyIdList(self, TemplatePolicyIdList):
        self._TemplatePolicyIdList = TemplatePolicyIdList

    @property
    def TemplatePolicyRule(self):
        """策略规则
        :rtype: str
        """
        return self._TemplatePolicyRule

    @TemplatePolicyRule.setter
    def TemplatePolicyRule(self, TemplatePolicyRule):
        self._TemplatePolicyRule = TemplatePolicyRule

    @property
    def TemplatePolicyDealType(self):
        """护栏策略生效处理策略 1:顺序执行，2:暂停
        :rtype: int
        """
        return self._TemplatePolicyDealType

    @TemplatePolicyDealType.setter
    def TemplatePolicyDealType(self, TemplatePolicyDealType):
        self._TemplatePolicyDealType = TemplatePolicyDealType


    def _deserialize(self, params):
        self._TemplatePolicyIdList = params.get("TemplatePolicyIdList")
        self._TemplatePolicyRule = params.get("TemplatePolicyRule")
        self._TemplatePolicyDealType = params.get("TemplatePolicyDealType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerPolicyRequest(AbstractModel):
    """TriggerPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 混沌演练ID

        :type TaskId: int
        :param _Name: 名称
        :type Name: str
        :param _Content: 触发内容
        :type Content: str
        :param _TriggerType: 触发类型，0--触发；1--恢复
        :type TriggerType: int
        """
        self._TaskId = None
        self._Name = None
        self._Content = None
        self._TriggerType = None

    @property
    def TaskId(self):
        """混沌演练ID

        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """触发内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def TriggerType(self):
        """触发类型，0--触发；1--恢复
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._TriggerType = params.get("TriggerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerPolicyResponse(AbstractModel):
    """TriggerPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 演练ID
        :type TaskId: int
        :param _Success: 是否触发成功
        :type Success: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Success = None
        self._RequestId = None

    @property
    def TaskId(self):
        """演练ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Success(self):
        """是否触发成功
        :rtype: bool
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
        self._TaskId = params.get("TaskId")
        self._Success = params.get("Success")
        self._RequestId = params.get("RequestId")