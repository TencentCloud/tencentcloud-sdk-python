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


class CreateFlowServiceRequest(AbstractModel):
    """CreateFlowService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Definition: 定义文本（JSON格式）
        :type Definition: str
        :param _FlowServiceName: 状态机所属服务名
        :type FlowServiceName: str
        :param _IsNewRole: 是不是新的角色
        :type IsNewRole: bool
        :param _Type: 状态机类型（EXPRESS，STANDARD）
        :type Type: str
        :param _FlowServiceChineseName: 状态机所属服务中文名
        :type FlowServiceChineseName: str
        :param _RoleResource: 角色资源名, 比如: qcs::cam::uin/20103392:roleName/SomeRoleForYourStateMachine
        :type RoleResource: str
        :param _Description: 备注
        :type Description: str
        :param _EnableCLS: 是否开启CLS日志投递功能
        :type EnableCLS: bool
        :param _Input: 该状态机的默认输入
        :type Input: str
        """
        self._Definition = None
        self._FlowServiceName = None
        self._IsNewRole = None
        self._Type = None
        self._FlowServiceChineseName = None
        self._RoleResource = None
        self._Description = None
        self._EnableCLS = None
        self._Input = None

    @property
    def Definition(self):
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def FlowServiceName(self):
        return self._FlowServiceName

    @FlowServiceName.setter
    def FlowServiceName(self, FlowServiceName):
        self._FlowServiceName = FlowServiceName

    @property
    def IsNewRole(self):
        return self._IsNewRole

    @IsNewRole.setter
    def IsNewRole(self, IsNewRole):
        self._IsNewRole = IsNewRole

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FlowServiceChineseName(self):
        return self._FlowServiceChineseName

    @FlowServiceChineseName.setter
    def FlowServiceChineseName(self, FlowServiceChineseName):
        self._FlowServiceChineseName = FlowServiceChineseName

    @property
    def RoleResource(self):
        return self._RoleResource

    @RoleResource.setter
    def RoleResource(self, RoleResource):
        self._RoleResource = RoleResource

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnableCLS(self):
        return self._EnableCLS

    @EnableCLS.setter
    def EnableCLS(self, EnableCLS):
        self._EnableCLS = EnableCLS

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._Definition = params.get("Definition")
        self._FlowServiceName = params.get("FlowServiceName")
        self._IsNewRole = params.get("IsNewRole")
        self._Type = params.get("Type")
        self._FlowServiceChineseName = params.get("FlowServiceChineseName")
        self._RoleResource = params.get("RoleResource")
        self._Description = params.get("Description")
        self._EnableCLS = params.get("EnableCLS")
        self._Input = params.get("Input")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowServiceResponse(AbstractModel):
    """CreateFlowService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowServiceResource: 状态机所属服务资源
        :type FlowServiceResource: str
        :param _CreateDate: 生成日期
        :type CreateDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowServiceResource = None
        self._CreateDate = None
        self._RequestId = None

    @property
    def FlowServiceResource(self):
        return self._FlowServiceResource

    @FlowServiceResource.setter
    def FlowServiceResource(self, FlowServiceResource):
        self._FlowServiceResource = FlowServiceResource

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowServiceResource = params.get("FlowServiceResource")
        self._CreateDate = params.get("CreateDate")
        self._RequestId = params.get("RequestId")


class DescribeExecutionHistoryRequest(AbstractModel):
    """DescribeExecutionHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionResourceName: 执行资源名
        :type ExecutionResourceName: str
        """
        self._ExecutionResourceName = None

    @property
    def ExecutionResourceName(self):
        return self._ExecutionResourceName

    @ExecutionResourceName.setter
    def ExecutionResourceName(self, ExecutionResourceName):
        self._ExecutionResourceName = ExecutionResourceName


    def _deserialize(self, params):
        self._ExecutionResourceName = params.get("ExecutionResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExecutionHistoryResponse(AbstractModel):
    """DescribeExecutionHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 执行的事件列表
        :type Events: list of ExecutionEvent
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = ExecutionEvent()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExecutionRequest(AbstractModel):
    """DescribeExecution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionResourceName: 执行资源名
        :type ExecutionResourceName: str
        """
        self._ExecutionResourceName = None

    @property
    def ExecutionResourceName(self):
        return self._ExecutionResourceName

    @ExecutionResourceName.setter
    def ExecutionResourceName(self, ExecutionResourceName):
        self._ExecutionResourceName = ExecutionResourceName


    def _deserialize(self, params):
        self._ExecutionResourceName = params.get("ExecutionResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExecutionResponse(AbstractModel):
    """DescribeExecution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionResourceName: 执行资源名
        :type ExecutionResourceName: str
        :param _Name: 资源名称
        :type Name: str
        :param _StartDate: 执行开始时间，毫秒
        :type StartDate: str
        :param _StopDate: 执行结束时间，毫秒
        :type StopDate: str
        :param _StateMachineResourceName: 状态机资源名
        :type StateMachineResourceName: str
        :param _Status: 执行状态。INIT，RUNNING，SUCCEED，FAILED，TERMINATED
        :type Status: str
        :param _Input: 执行的输入
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: str
        :param _Output: 执行的输出
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        :param _ExecutionDefinition: 启动执行时，状态机的定义
        :type ExecutionDefinition: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExecutionResourceName = None
        self._Name = None
        self._StartDate = None
        self._StopDate = None
        self._StateMachineResourceName = None
        self._Status = None
        self._Input = None
        self._Output = None
        self._ExecutionDefinition = None
        self._RequestId = None

    @property
    def ExecutionResourceName(self):
        return self._ExecutionResourceName

    @ExecutionResourceName.setter
    def ExecutionResourceName(self, ExecutionResourceName):
        self._ExecutionResourceName = ExecutionResourceName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def StopDate(self):
        return self._StopDate

    @StopDate.setter
    def StopDate(self, StopDate):
        self._StopDate = StopDate

    @property
    def StateMachineResourceName(self):
        return self._StateMachineResourceName

    @StateMachineResourceName.setter
    def StateMachineResourceName(self, StateMachineResourceName):
        self._StateMachineResourceName = StateMachineResourceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def ExecutionDefinition(self):
        return self._ExecutionDefinition

    @ExecutionDefinition.setter
    def ExecutionDefinition(self, ExecutionDefinition):
        self._ExecutionDefinition = ExecutionDefinition

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExecutionResourceName = params.get("ExecutionResourceName")
        self._Name = params.get("Name")
        self._StartDate = params.get("StartDate")
        self._StopDate = params.get("StopDate")
        self._StateMachineResourceName = params.get("StateMachineResourceName")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._ExecutionDefinition = params.get("ExecutionDefinition")
        self._RequestId = params.get("RequestId")


class DescribeExecutionsRequest(AbstractModel):
    """DescribeExecutions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StateMachineResourceName: 状态机资源名
        :type StateMachineResourceName: str
        :param _PageSize: 页大小，最大100
        :type PageSize: int
        :param _PageIndex: 页序号，从1开始
        :type PageIndex: int
        :param _FilterExecutionStatus: 按状态过滤条件，INIT，RUNNING，SUCCEED，FAILED，TERMINATED
        :type FilterExecutionStatus: str
        :param _FilterExecutionResourceName: 按执行名过滤条件
        :type FilterExecutionResourceName: str
        """
        self._StateMachineResourceName = None
        self._PageSize = None
        self._PageIndex = None
        self._FilterExecutionStatus = None
        self._FilterExecutionResourceName = None

    @property
    def StateMachineResourceName(self):
        return self._StateMachineResourceName

    @StateMachineResourceName.setter
    def StateMachineResourceName(self, StateMachineResourceName):
        self._StateMachineResourceName = StateMachineResourceName

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageIndex(self):
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def FilterExecutionStatus(self):
        return self._FilterExecutionStatus

    @FilterExecutionStatus.setter
    def FilterExecutionStatus(self, FilterExecutionStatus):
        self._FilterExecutionStatus = FilterExecutionStatus

    @property
    def FilterExecutionResourceName(self):
        return self._FilterExecutionResourceName

    @FilterExecutionResourceName.setter
    def FilterExecutionResourceName(self, FilterExecutionResourceName):
        self._FilterExecutionResourceName = FilterExecutionResourceName


    def _deserialize(self, params):
        self._StateMachineResourceName = params.get("StateMachineResourceName")
        self._PageSize = params.get("PageSize")
        self._PageIndex = params.get("PageIndex")
        self._FilterExecutionStatus = params.get("FilterExecutionStatus")
        self._FilterExecutionResourceName = params.get("FilterExecutionResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExecutionsResponse(AbstractModel):
    """DescribeExecutions返回参数结构体

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


class DescribeFlowServiceDetailRequest(AbstractModel):
    """DescribeFlowServiceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowServiceResource: 状态机所属服务资源名
        :type FlowServiceResource: str
        """
        self._FlowServiceResource = None

    @property
    def FlowServiceResource(self):
        return self._FlowServiceResource

    @FlowServiceResource.setter
    def FlowServiceResource(self, FlowServiceResource):
        self._FlowServiceResource = FlowServiceResource


    def _deserialize(self, params):
        self._FlowServiceResource = params.get("FlowServiceResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowServiceDetailResponse(AbstractModel):
    """DescribeFlowServiceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowServiceName: 状态机所属服务名
        :type FlowServiceName: str
        :param _Status: 状态机状态
        :type Status: str
        :param _Definition: 定义文本（JSON格式）
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: str
        :param _RoleResource: 角色资源名
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleResource: str
        :param _Type: 状态机的类型，可以为 （EXPRESS/STANDARD）
        :type Type: str
        :param _CreateDate: 生成时间
        :type CreateDate: str
        :param _Description: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _FlowServiceChineseName: 状态机所属服务中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowServiceChineseName: str
        :param _EnableCLS: 是否开启日志CLS服务
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableCLS: bool
        :param _CLSUrl: CLS日志查看地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CLSUrl: str
        :param _FlowInput: 工作流提示输入
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowInput: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowServiceName = None
        self._Status = None
        self._Definition = None
        self._RoleResource = None
        self._Type = None
        self._CreateDate = None
        self._Description = None
        self._FlowServiceChineseName = None
        self._EnableCLS = None
        self._CLSUrl = None
        self._FlowInput = None
        self._RequestId = None

    @property
    def FlowServiceName(self):
        return self._FlowServiceName

    @FlowServiceName.setter
    def FlowServiceName(self, FlowServiceName):
        self._FlowServiceName = FlowServiceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Definition(self):
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def RoleResource(self):
        return self._RoleResource

    @RoleResource.setter
    def RoleResource(self, RoleResource):
        self._RoleResource = RoleResource

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def FlowServiceChineseName(self):
        return self._FlowServiceChineseName

    @FlowServiceChineseName.setter
    def FlowServiceChineseName(self, FlowServiceChineseName):
        self._FlowServiceChineseName = FlowServiceChineseName

    @property
    def EnableCLS(self):
        return self._EnableCLS

    @EnableCLS.setter
    def EnableCLS(self, EnableCLS):
        self._EnableCLS = EnableCLS

    @property
    def CLSUrl(self):
        return self._CLSUrl

    @CLSUrl.setter
    def CLSUrl(self, CLSUrl):
        self._CLSUrl = CLSUrl

    @property
    def FlowInput(self):
        return self._FlowInput

    @FlowInput.setter
    def FlowInput(self, FlowInput):
        self._FlowInput = FlowInput

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowServiceName = params.get("FlowServiceName")
        self._Status = params.get("Status")
        self._Definition = params.get("Definition")
        self._RoleResource = params.get("RoleResource")
        self._Type = params.get("Type")
        self._CreateDate = params.get("CreateDate")
        self._Description = params.get("Description")
        self._FlowServiceChineseName = params.get("FlowServiceChineseName")
        self._EnableCLS = params.get("EnableCLS")
        self._CLSUrl = params.get("CLSUrl")
        self._FlowInput = params.get("FlowInput")
        self._RequestId = params.get("RequestId")


class DescribeFlowServicesRequest(AbstractModel):
    """DescribeFlowServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filter.Values的上限为5。参数名字仅支持FlowServiceName， Status, Type三种情况
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
        


class DescribeFlowServicesResponse(AbstractModel):
    """DescribeFlowServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowServiceSet: 用户的状态机列表
        :type FlowServiceSet: list of StateMachine
        :param _TotalCount: 用户的状态机总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowServiceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FlowServiceSet(self):
        return self._FlowServiceSet

    @FlowServiceSet.setter
    def FlowServiceSet(self, FlowServiceSet):
        self._FlowServiceSet = FlowServiceSet

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
        if params.get("FlowServiceSet") is not None:
            self._FlowServiceSet = []
            for item in params.get("FlowServiceSet"):
                obj = StateMachine()
                obj._deserialize(item)
                self._FlowServiceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ExecutionEvent(AbstractModel):
    """执行的事件历史

    """

    def __init__(self):
        r"""
        :param _ExecutionResourceName: 执行资源名
        :type ExecutionResourceName: str
        :param _EventId: 自增序号
        :type EventId: int
        :param _EventCategory: 事件类型
        :type EventCategory: str
        :param _StepName: 步骤节点名称
        :type StepName: str
        :param _ResourceName: 该步骤引用的资源名
        :type ResourceName: str
        :param _Timestamp: 该事件发生时间，毫秒
        :type Timestamp: str
        :param _Content: 事件内容
        :type Content: str
        :param _Exception: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Exception: str
        """
        self._ExecutionResourceName = None
        self._EventId = None
        self._EventCategory = None
        self._StepName = None
        self._ResourceName = None
        self._Timestamp = None
        self._Content = None
        self._Exception = None

    @property
    def ExecutionResourceName(self):
        return self._ExecutionResourceName

    @ExecutionResourceName.setter
    def ExecutionResourceName(self, ExecutionResourceName):
        self._ExecutionResourceName = ExecutionResourceName

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def EventCategory(self):
        return self._EventCategory

    @EventCategory.setter
    def EventCategory(self, EventCategory):
        self._EventCategory = EventCategory

    @property
    def StepName(self):
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

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

    @property
    def Exception(self):
        return self._Exception

    @Exception.setter
    def Exception(self, Exception):
        self._Exception = Exception


    def _deserialize(self, params):
        self._ExecutionResourceName = params.get("ExecutionResourceName")
        self._EventId = params.get("EventId")
        self._EventCategory = params.get("EventCategory")
        self._StepName = params.get("StepName")
        self._ResourceName = params.get("ResourceName")
        self._Timestamp = params.get("Timestamp")
        self._Content = params.get("Content")
        self._Exception = params.get("Exception")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """模版过滤类型

    """

    def __init__(self):
        r"""
        :param _Name: 过滤器名字
        :type Name: str
        :param _Values: 过滤器值的数组
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

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
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFlowServiceRequest(AbstractModel):
    """ModifyFlowService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowServiceResource: 状态机资源名
        :type FlowServiceResource: str
        :param _Definition: 定义JSON
        :type Definition: str
        :param _FlowServiceName: 状态机所属服务名
        :type FlowServiceName: str
        :param _FlowServiceChineseName: 状态机所属服务中文名
        :type FlowServiceChineseName: str
        :param _IsNewRole: 是否是新角色
        :type IsNewRole: bool
        :param _Type: 状态机类型
        :type Type: str
        :param _RoleResource: 角色资源名
        :type RoleResource: str
        :param _Description: 状态机备注
        :type Description: str
        :param _EnableCLS: 是否允许日志投递
        :type EnableCLS: bool
        """
        self._FlowServiceResource = None
        self._Definition = None
        self._FlowServiceName = None
        self._FlowServiceChineseName = None
        self._IsNewRole = None
        self._Type = None
        self._RoleResource = None
        self._Description = None
        self._EnableCLS = None

    @property
    def FlowServiceResource(self):
        return self._FlowServiceResource

    @FlowServiceResource.setter
    def FlowServiceResource(self, FlowServiceResource):
        self._FlowServiceResource = FlowServiceResource

    @property
    def Definition(self):
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def FlowServiceName(self):
        return self._FlowServiceName

    @FlowServiceName.setter
    def FlowServiceName(self, FlowServiceName):
        self._FlowServiceName = FlowServiceName

    @property
    def FlowServiceChineseName(self):
        return self._FlowServiceChineseName

    @FlowServiceChineseName.setter
    def FlowServiceChineseName(self, FlowServiceChineseName):
        self._FlowServiceChineseName = FlowServiceChineseName

    @property
    def IsNewRole(self):
        return self._IsNewRole

    @IsNewRole.setter
    def IsNewRole(self, IsNewRole):
        self._IsNewRole = IsNewRole

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RoleResource(self):
        return self._RoleResource

    @RoleResource.setter
    def RoleResource(self, RoleResource):
        self._RoleResource = RoleResource

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnableCLS(self):
        return self._EnableCLS

    @EnableCLS.setter
    def EnableCLS(self, EnableCLS):
        self._EnableCLS = EnableCLS


    def _deserialize(self, params):
        self._FlowServiceResource = params.get("FlowServiceResource")
        self._Definition = params.get("Definition")
        self._FlowServiceName = params.get("FlowServiceName")
        self._FlowServiceChineseName = params.get("FlowServiceChineseName")
        self._IsNewRole = params.get("IsNewRole")
        self._Type = params.get("Type")
        self._RoleResource = params.get("RoleResource")
        self._Description = params.get("Description")
        self._EnableCLS = params.get("EnableCLS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFlowServiceResponse(AbstractModel):
    """ModifyFlowService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowServiceResource: 状态机资源名
        :type FlowServiceResource: str
        :param _UpdateDate: 更新时间
        :type UpdateDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowServiceResource = None
        self._UpdateDate = None
        self._RequestId = None

    @property
    def FlowServiceResource(self):
        return self._FlowServiceResource

    @FlowServiceResource.setter
    def FlowServiceResource(self, FlowServiceResource):
        self._FlowServiceResource = FlowServiceResource

    @property
    def UpdateDate(self):
        return self._UpdateDate

    @UpdateDate.setter
    def UpdateDate(self, UpdateDate):
        self._UpdateDate = UpdateDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowServiceResource = params.get("FlowServiceResource")
        self._UpdateDate = params.get("UpdateDate")
        self._RequestId = params.get("RequestId")


class StartExecutionRequest(AbstractModel):
    """StartExecution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StateMachineResourceName: 状态机资源名
        :type StateMachineResourceName: str
        :param _Input: 输入参数，内容为JsonObject，长度不大于524288字符。
        :type Input: str
        :param _Name: 本次执行名。如果不填，系统会自动生成。如果填，应保证状态机下唯一
        :type Name: str
        """
        self._StateMachineResourceName = None
        self._Input = None
        self._Name = None

    @property
    def StateMachineResourceName(self):
        return self._StateMachineResourceName

    @StateMachineResourceName.setter
    def StateMachineResourceName(self, StateMachineResourceName):
        self._StateMachineResourceName = StateMachineResourceName

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._StateMachineResourceName = params.get("StateMachineResourceName")
        self._Input = params.get("Input")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartExecutionResponse(AbstractModel):
    """StartExecution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionResourceName: 执行资源名
        :type ExecutionResourceName: str
        :param _StartDate: 执行开始时间
        :type StartDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExecutionResourceName = None
        self._StartDate = None
        self._RequestId = None

    @property
    def ExecutionResourceName(self):
        return self._ExecutionResourceName

    @ExecutionResourceName.setter
    def ExecutionResourceName(self, ExecutionResourceName):
        self._ExecutionResourceName = ExecutionResourceName

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExecutionResourceName = params.get("ExecutionResourceName")
        self._StartDate = params.get("StartDate")
        self._RequestId = params.get("RequestId")


class StateMachine(AbstractModel):
    """状态机

    """

    def __init__(self):
        r"""
        :param _FlowServiceResource: 状态机资源
        :type FlowServiceResource: str
        :param _Type: 状态机类型。EXPRESS，STANDARD
        :type Type: str
        :param _FlowServiceName: 状态机名称
        :type FlowServiceName: str
        :param _FlowServiceChineseName: 状态机中文名
        :type FlowServiceChineseName: str
        :param _CreateDate: 创建时间。timestamp
        :type CreateDate: str
        :param _ModifyDate: 修改时间。timestamp
        :type ModifyDate: str
        :param _Status: 状态机状态
        :type Status: str
        :param _Creator: 创建者的subAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _Modifier: 修改者的subAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type Modifier: str
        :param _FlowServiceId: 状态机id
        :type FlowServiceId: str
        :param _TemplateId: 模板id
        :type TemplateId: str
        :param _Description: 备注
        :type Description: str
        """
        self._FlowServiceResource = None
        self._Type = None
        self._FlowServiceName = None
        self._FlowServiceChineseName = None
        self._CreateDate = None
        self._ModifyDate = None
        self._Status = None
        self._Creator = None
        self._Modifier = None
        self._FlowServiceId = None
        self._TemplateId = None
        self._Description = None

    @property
    def FlowServiceResource(self):
        return self._FlowServiceResource

    @FlowServiceResource.setter
    def FlowServiceResource(self, FlowServiceResource):
        self._FlowServiceResource = FlowServiceResource

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FlowServiceName(self):
        return self._FlowServiceName

    @FlowServiceName.setter
    def FlowServiceName(self, FlowServiceName):
        self._FlowServiceName = FlowServiceName

    @property
    def FlowServiceChineseName(self):
        return self._FlowServiceChineseName

    @FlowServiceChineseName.setter
    def FlowServiceChineseName(self, FlowServiceChineseName):
        self._FlowServiceChineseName = FlowServiceChineseName

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def Modifier(self):
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def FlowServiceId(self):
        return self._FlowServiceId

    @FlowServiceId.setter
    def FlowServiceId(self, FlowServiceId):
        self._FlowServiceId = FlowServiceId

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._FlowServiceResource = params.get("FlowServiceResource")
        self._Type = params.get("Type")
        self._FlowServiceName = params.get("FlowServiceName")
        self._FlowServiceChineseName = params.get("FlowServiceChineseName")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._Status = params.get("Status")
        self._Creator = params.get("Creator")
        self._Modifier = params.get("Modifier")
        self._FlowServiceId = params.get("FlowServiceId")
        self._TemplateId = params.get("TemplateId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopExecutionRequest(AbstractModel):
    """StopExecution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionQrn: 执行名称
        :type ExecutionQrn: str
        """
        self._ExecutionQrn = None

    @property
    def ExecutionQrn(self):
        return self._ExecutionQrn

    @ExecutionQrn.setter
    def ExecutionQrn(self, ExecutionQrn):
        self._ExecutionQrn = ExecutionQrn


    def _deserialize(self, params):
        self._ExecutionQrn = params.get("ExecutionQrn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopExecutionResponse(AbstractModel):
    """StopExecution返回参数结构体

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