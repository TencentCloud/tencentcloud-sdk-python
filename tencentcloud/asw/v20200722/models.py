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


class CreateFlowServiceRequest(AbstractModel):
    """CreateFlowService请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 定义文本（JSON格式）
        :type Definition: str
        :param FlowServiceName: 状态机所属服务名
        :type FlowServiceName: str
        :param IsNewRole: 是不是新的角色
        :type IsNewRole: bool
        :param Type: 状态机类型（EXPRESS，STANDARD）
        :type Type: str
        :param FlowServiceChineseName: 状态机所属服务中文名
        :type FlowServiceChineseName: str
        :param RoleResource: 角色资源名, 比如: qcs::cam::uin/20103392:roleName/SomeRoleForYourStateMachine
        :type RoleResource: str
        :param Description: 备注
        :type Description: str
        """
        self.Definition = None
        self.FlowServiceName = None
        self.IsNewRole = None
        self.Type = None
        self.FlowServiceChineseName = None
        self.RoleResource = None
        self.Description = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.FlowServiceName = params.get("FlowServiceName")
        self.IsNewRole = params.get("IsNewRole")
        self.Type = params.get("Type")
        self.FlowServiceChineseName = params.get("FlowServiceChineseName")
        self.RoleResource = params.get("RoleResource")
        self.Description = params.get("Description")


class CreateFlowServiceResponse(AbstractModel):
    """CreateFlowService返回参数结构体

    """

    def __init__(self):
        """
        :param FlowServiceResource: 状态机所属服务资源
        :type FlowServiceResource: str
        :param CreateDate: 生成日期
        :type CreateDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowServiceResource = None
        self.CreateDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowServiceResource = params.get("FlowServiceResource")
        self.CreateDate = params.get("CreateDate")
        self.RequestId = params.get("RequestId")


class DescribeExecutionRequest(AbstractModel):
    """DescribeExecution请求参数结构体

    """

    def __init__(self):
        """
        :param ExecutionResourceName: 执行资源名
        :type ExecutionResourceName: str
        """
        self.ExecutionResourceName = None


    def _deserialize(self, params):
        self.ExecutionResourceName = params.get("ExecutionResourceName")


class DescribeExecutionResponse(AbstractModel):
    """DescribeExecution返回参数结构体

    """

    def __init__(self):
        """
        :param ExecutionResourceName: 执行资源名
        :type ExecutionResourceName: str
        :param Name: 资源名称
        :type Name: str
        :param StartDate: 执行开始时间，毫秒
        :type StartDate: str
        :param StopDate: 执行结束时间，毫秒
        :type StopDate: str
        :param StateMachineResourceName: 状态机资源名
        :type StateMachineResourceName: str
        :param Status: 执行状态。INIT，RUNNING，SUCCEED，FAILED，TERMINATED
        :type Status: str
        :param Input: 执行的输入
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: str
        :param Output: 执行的输出
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        :param ExecutionDefinition: 启动执行时，状态机的定义
        :type ExecutionDefinition: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExecutionResourceName = None
        self.Name = None
        self.StartDate = None
        self.StopDate = None
        self.StateMachineResourceName = None
        self.Status = None
        self.Input = None
        self.Output = None
        self.ExecutionDefinition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExecutionResourceName = params.get("ExecutionResourceName")
        self.Name = params.get("Name")
        self.StartDate = params.get("StartDate")
        self.StopDate = params.get("StopDate")
        self.StateMachineResourceName = params.get("StateMachineResourceName")
        self.Status = params.get("Status")
        self.Input = params.get("Input")
        self.Output = params.get("Output")
        self.ExecutionDefinition = params.get("ExecutionDefinition")
        self.RequestId = params.get("RequestId")


class DescribeExecutionsRequest(AbstractModel):
    """DescribeExecutions请求参数结构体

    """

    def __init__(self):
        """
        :param StateMachineResourceName: 状态机资源名
        :type StateMachineResourceName: str
        :param PageSize: 页大小，最大100
        :type PageSize: int
        :param PageIndex: 页序号，从1开始
        :type PageIndex: int
        :param FilterExecutionStatus: 按状态过滤条件，INIT，RUNNING，SUCCEED，FAILED，TERMINATED
        :type FilterExecutionStatus: str
        :param FilterExecutionResourceName: 按执行名过滤条件
        :type FilterExecutionResourceName: str
        """
        self.StateMachineResourceName = None
        self.PageSize = None
        self.PageIndex = None
        self.FilterExecutionStatus = None
        self.FilterExecutionResourceName = None


    def _deserialize(self, params):
        self.StateMachineResourceName = params.get("StateMachineResourceName")
        self.PageSize = params.get("PageSize")
        self.PageIndex = params.get("PageIndex")
        self.FilterExecutionStatus = params.get("FilterExecutionStatus")
        self.FilterExecutionResourceName = params.get("FilterExecutionResourceName")


class DescribeExecutionsResponse(AbstractModel):
    """DescribeExecutions返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeFlowServiceDetailRequest(AbstractModel):
    """DescribeFlowServiceDetail请求参数结构体

    """

    def __init__(self):
        """
        :param FlowServiceResource: 状态机所属服务资源名
        :type FlowServiceResource: str
        """
        self.FlowServiceResource = None


    def _deserialize(self, params):
        self.FlowServiceResource = params.get("FlowServiceResource")


class DescribeFlowServiceDetailResponse(AbstractModel):
    """DescribeFlowServiceDetail返回参数结构体

    """

    def __init__(self):
        """
        :param FlowServiceName: 状态机所属服务名
        :type FlowServiceName: str
        :param Status: 状态机状态
        :type Status: str
        :param Definition: 定义文本（JSON格式）
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: str
        :param RoleResource: 角色资源名
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleResource: str
        :param Type: 状态机的类型，可以为 （EXPRESS/STANDARD）
        :type Type: str
        :param CreateDate: 生成时间
        :type CreateDate: str
        :param Description: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param FlowServiceChineseName: 状态机所属服务中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowServiceChineseName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowServiceName = None
        self.Status = None
        self.Definition = None
        self.RoleResource = None
        self.Type = None
        self.CreateDate = None
        self.Description = None
        self.FlowServiceChineseName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowServiceName = params.get("FlowServiceName")
        self.Status = params.get("Status")
        self.Definition = params.get("Definition")
        self.RoleResource = params.get("RoleResource")
        self.Type = params.get("Type")
        self.CreateDate = params.get("CreateDate")
        self.Description = params.get("Description")
        self.FlowServiceChineseName = params.get("FlowServiceChineseName")
        self.RequestId = params.get("RequestId")


class DescribeFlowServicesRequest(AbstractModel):
    """DescribeFlowServices请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filter.Values的上限为5。参数名字仅支持FlowServiceName， Status, Type三种情况
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeFlowServicesResponse(AbstractModel):
    """DescribeFlowServices返回参数结构体

    """

    def __init__(self):
        """
        :param FlowServiceSet: 用户的状态机列表
        :type FlowServiceSet: list of StateMachine
        :param TotalCount: 用户的状态机总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowServiceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowServiceSet") is not None:
            self.FlowServiceSet = []
            for item in params.get("FlowServiceSet"):
                obj = StateMachine()
                obj._deserialize(item)
                self.FlowServiceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """模版过滤类型

    """

    def __init__(self):
        """
        :param Name: 过滤器名字
        :type Name: str
        :param Values: 过滤器值的数组
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ModifyFlowServiceRequest(AbstractModel):
    """ModifyFlowService请求参数结构体

    """

    def __init__(self):
        """
        :param FlowServiceResource: 状态机资源名
        :type FlowServiceResource: str
        :param Definition: 定义JSON
        :type Definition: str
        :param FlowServiceName: 状态机所属服务名
        :type FlowServiceName: str
        :param FlowServiceChineseName: 状态机所属服务中文名
        :type FlowServiceChineseName: str
        :param IsNewRole: 是否是新角色
        :type IsNewRole: bool
        :param Type: 状态机类型
        :type Type: str
        :param RoleResource: 角色资源名
        :type RoleResource: str
        :param Description: 状态机备注
        :type Description: str
        """
        self.FlowServiceResource = None
        self.Definition = None
        self.FlowServiceName = None
        self.FlowServiceChineseName = None
        self.IsNewRole = None
        self.Type = None
        self.RoleResource = None
        self.Description = None


    def _deserialize(self, params):
        self.FlowServiceResource = params.get("FlowServiceResource")
        self.Definition = params.get("Definition")
        self.FlowServiceName = params.get("FlowServiceName")
        self.FlowServiceChineseName = params.get("FlowServiceChineseName")
        self.IsNewRole = params.get("IsNewRole")
        self.Type = params.get("Type")
        self.RoleResource = params.get("RoleResource")
        self.Description = params.get("Description")


class ModifyFlowServiceResponse(AbstractModel):
    """ModifyFlowService返回参数结构体

    """

    def __init__(self):
        """
        :param FlowServiceResource: 状态机资源名
        :type FlowServiceResource: str
        :param UpdateDate: 更新时间
        :type UpdateDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowServiceResource = None
        self.UpdateDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowServiceResource = params.get("FlowServiceResource")
        self.UpdateDate = params.get("UpdateDate")
        self.RequestId = params.get("RequestId")


class StartExecutionRequest(AbstractModel):
    """StartExecution请求参数结构体

    """

    def __init__(self):
        """
        :param StateMachineResourceName: 状态机资源名
        :type StateMachineResourceName: str
        :param Input: 输入参数
        :type Input: str
        :param Name: 本次执行名。如果不填，系统会自动生成。如果填，应保证状态机下唯一
        :type Name: str
        """
        self.StateMachineResourceName = None
        self.Input = None
        self.Name = None


    def _deserialize(self, params):
        self.StateMachineResourceName = params.get("StateMachineResourceName")
        self.Input = params.get("Input")
        self.Name = params.get("Name")


class StartExecutionResponse(AbstractModel):
    """StartExecution返回参数结构体

    """

    def __init__(self):
        """
        :param ExecutionResourceName: 执行资源名
        :type ExecutionResourceName: str
        :param StartDate: 执行开始时间
        :type StartDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExecutionResourceName = None
        self.StartDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExecutionResourceName = params.get("ExecutionResourceName")
        self.StartDate = params.get("StartDate")
        self.RequestId = params.get("RequestId")


class StateMachine(AbstractModel):
    """状态机

    """

    def __init__(self):
        """
        :param FlowServiceResource: 状态机资源
        :type FlowServiceResource: str
        :param Type: 状态机类型。EXPRESS，STANDARD
        :type Type: str
        :param FlowServiceName: 状态机名称
        :type FlowServiceName: str
        :param FlowServiceChineseName: 状态机中文名
        :type FlowServiceChineseName: str
        :param CreateDate: 创建时间。timestamp
        :type CreateDate: str
        :param ModifyDate: 修改时间。timestamp
        :type ModifyDate: str
        :param Status: 状态机状态
        :type Status: str
        :param Creator: 创建者的subAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param Modifier: 修改者的subAccountUin
注意：此字段可能返回 null，表示取不到有效值。
        :type Modifier: str
        :param FlowServiceId: 状态机id
        :type FlowServiceId: str
        :param TemplateId: 模板id
        :type TemplateId: str
        :param Description: 备注
        :type Description: str
        """
        self.FlowServiceResource = None
        self.Type = None
        self.FlowServiceName = None
        self.FlowServiceChineseName = None
        self.CreateDate = None
        self.ModifyDate = None
        self.Status = None
        self.Creator = None
        self.Modifier = None
        self.FlowServiceId = None
        self.TemplateId = None
        self.Description = None


    def _deserialize(self, params):
        self.FlowServiceResource = params.get("FlowServiceResource")
        self.Type = params.get("Type")
        self.FlowServiceName = params.get("FlowServiceName")
        self.FlowServiceChineseName = params.get("FlowServiceChineseName")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.Status = params.get("Status")
        self.Creator = params.get("Creator")
        self.Modifier = params.get("Modifier")
        self.FlowServiceId = params.get("FlowServiceId")
        self.TemplateId = params.get("TemplateId")
        self.Description = params.get("Description")