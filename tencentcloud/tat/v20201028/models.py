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


class AutomationAgentInfo(AbstractModel):
    """自动化助手客户端信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Version: Agent 版本号。
        :type Version: str
        :param LastHeartbeatTime: 上次心跳时间
        :type LastHeartbeatTime: str
        :param AgentStatus: Agent状态，取值范围：
<li> Online：在线
<li> Offline：离线
        :type AgentStatus: str
        :param Environment: Agent运行环境
        :type Environment: str
        """
        self.InstanceId = None
        self.Version = None
        self.LastHeartbeatTime = None
        self.AgentStatus = None
        self.Environment = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Version = params.get("Version")
        self.LastHeartbeatTime = params.get("LastHeartbeatTime")
        self.AgentStatus = params.get("AgentStatus")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Command(AbstractModel):
    """命令详情。

    """

    def __init__(self):
        """
        :param CommandId: 命令ID。
        :type CommandId: str
        :param CommandName: 命令名称。
        :type CommandName: str
        :param Description: 命令描述。
        :type Description: str
        :param Content: Base64编码后的命令内容。
        :type Content: str
        :param CommandType: 命令类型。
        :type CommandType: str
        :param WorkingDirectory: 命令执行路径。
        :type WorkingDirectory: str
        :param Timeout: 命令超时时间。
        :type Timeout: int
        :param CreatedTime: 命令创建时间。
        :type CreatedTime: str
        :param UpdatedTime: 命令更新时间。
        :type UpdatedTime: str
        :param EnableParameter: 是否启用自定义参数功能。
        :type EnableParameter: bool
        :param DefaultParameters: 自定义参数的默认取值。
        :type DefaultParameters: str
        :param FormattedDescription: 命令的结构化描述。公共命令有值，用户命令为空字符串。
        :type FormattedDescription: str
        :param CreatedBy: 命令创建者。TAT 代表公共命令，USER 代表个人命令。
        :type CreatedBy: str
        """
        self.CommandId = None
        self.CommandName = None
        self.Description = None
        self.Content = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.EnableParameter = None
        self.DefaultParameters = None
        self.FormattedDescription = None
        self.CreatedBy = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.CommandName = params.get("CommandName")
        self.Description = params.get("Description")
        self.Content = params.get("Content")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.EnableParameter = params.get("EnableParameter")
        self.DefaultParameters = params.get("DefaultParameters")
        self.FormattedDescription = params.get("FormattedDescription")
        self.CreatedBy = params.get("CreatedBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CommandDocument(AbstractModel):
    """命令执行详情。

    """

    def __init__(self):
        """
        :param Content: Base64 编码后的执行命令。
        :type Content: str
        :param CommandType: 命令类型。
        :type CommandType: str
        :param Timeout: 超时时间。
        :type Timeout: int
        :param WorkingDirectory: 执行路径。
        :type WorkingDirectory: str
        """
        self.Content = None
        self.CommandType = None
        self.Timeout = None
        self.WorkingDirectory = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.CommandType = params.get("CommandType")
        self.Timeout = params.get("Timeout")
        self.WorkingDirectory = params.get("WorkingDirectory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCommandRequest(AbstractModel):
    """CreateCommand请求参数结构体

    """

    def __init__(self):
        """
        :param CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type CommandName: str
        :param Content: Base64编码后的命令内容，长度不可超过64KB。
        :type Content: str
        :param Description: 命令描述。不超过120字符。
        :type Description: str
        :param CommandType: 命令类型，目前仅支持取值：SHELL。默认：SHELL。
        :type CommandType: str
        :param WorkingDirectory: 命令执行路径，默认：/root。
        :type WorkingDirectory: str
        :param Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。
        :type Timeout: int
        :param EnableParameter: 是否启用自定义参数功能。
一旦创建，此值不提供修改。
默认值：false。
        :type EnableParameter: bool
        :param DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{\"varA\": \"222\"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果InvokeCommand时未提供参数取值，将使用这里的默认值进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type DefaultParameters: str
        """
        self.CommandName = None
        self.Content = None
        self.Description = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.EnableParameter = None
        self.DefaultParameters = None


    def _deserialize(self, params):
        self.CommandName = params.get("CommandName")
        self.Content = params.get("Content")
        self.Description = params.get("Description")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.EnableParameter = params.get("EnableParameter")
        self.DefaultParameters = params.get("DefaultParameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCommandResponse(AbstractModel):
    """CreateCommand返回参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 命令ID。
        :type CommandId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CommandId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteCommandRequest(AbstractModel):
    """DeleteCommand请求参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 待删除的命令ID。
        :type CommandId: str
        """
        self.CommandId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteCommandResponse(AbstractModel):
    """DeleteCommand返回参数结构体

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
        


class DescribeAutomationAgentStatusRequest(AbstractModel):
    """DescribeAutomationAgentStatus请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 待查询的实例ID列表。
        :type InstanceIds: list of str
        :param Filters: 过滤条件。<br> <li> agent-status - String - 是否必填：否 -（过滤条件）按照agent状态过滤，取值：Online 在线，Offline 离线。<br> <li> environment - String - 是否必填：否 -（过滤条件）按照agent运行环境查询，取值：Linux。<br> <li> instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。 <br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InstanceIds` 和 `Filters` 。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAutomationAgentStatusResponse(AbstractModel):
    """DescribeAutomationAgentStatus返回参数结构体

    """

    def __init__(self):
        """
        :param AutomationAgentSet: Agent 信息列表。
        :type AutomationAgentSet: list of AutomationAgentInfo
        :param TotalCount: 符合条件的 Agent 总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutomationAgentSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AutomationAgentSet") is not None:
            self.AutomationAgentSet = []
            for item in params.get("AutomationAgentSet"):
                obj = AutomationAgentInfo()
                obj._deserialize(item)
                self.AutomationAgentSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCommandsRequest(AbstractModel):
    """DescribeCommands请求参数结构体

    """

    def __init__(self):
        """
        :param CommandIds: 命令ID列表，每次请求的上限为100。参数不支持同时指定 `CommandIds` 和 `Filters` 。
        :type CommandIds: list of str
        :param Filters: 过滤条件。<br> <li> command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。<br> <li> command-name - String - 是否必填：否 -（过滤条件）按照命令名称过滤。<br> <li> created-by - String - 是否必填：否 -（过滤条件）按照命令创建者过滤，取值为 TAT 或 USER，TAT 代表公共命令，USER 代表由用户创建的命令。 <br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `CommandIds` 和 `Filters` 。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self.CommandIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.CommandIds = params.get("CommandIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCommandsResponse(AbstractModel):
    """DescribeCommands返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的命令总数。
        :type TotalCount: int
        :param CommandSet: 命令详情列表。
        :type CommandSet: list of Command
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CommandSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CommandSet") is not None:
            self.CommandSet = []
            for item in params.get("CommandSet"):
                obj = Command()
                obj._deserialize(item)
                self.CommandSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInvocationTasksRequest(AbstractModel):
    """DescribeInvocationTasks请求参数结构体

    """

    def __init__(self):
        """
        :param InvocationTaskIds: 执行任务ID列表，每次请求的上限为100。参数不支持同时指定 `InvocationTaskIds` 和 `Filters`。
        :type InvocationTaskIds: list of str
        :param Filters: 过滤条件。<br> <li> invocation-id - String - 是否必填：否 -（过滤条件）按照执行活动ID过滤。<br> <li> invocation-task-id - String - 是否必填：否 -（过滤条件）按照执行任务ID过滤。<br> <li> instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。 <br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InvocationTaskIds` 和 `Filters` 。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param HideOutput: 是否隐藏输出，取值范围：<br><li>True：隐藏输出 <br><li>False：不隐藏 <br>默认为 True。
        :type HideOutput: bool
        """
        self.InvocationTaskIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.HideOutput = None


    def _deserialize(self, params):
        self.InvocationTaskIds = params.get("InvocationTaskIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.HideOutput = params.get("HideOutput")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInvocationTasksResponse(AbstractModel):
    """DescribeInvocationTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的执行任务总数。
        :type TotalCount: int
        :param InvocationTaskSet: 执行任务列表。
        :type InvocationTaskSet: list of InvocationTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InvocationTaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InvocationTaskSet") is not None:
            self.InvocationTaskSet = []
            for item in params.get("InvocationTaskSet"):
                obj = InvocationTask()
                obj._deserialize(item)
                self.InvocationTaskSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInvocationsRequest(AbstractModel):
    """DescribeInvocations请求参数结构体

    """

    def __init__(self):
        """
        :param InvocationIds: 执行活动ID列表，每次请求的上限为100。参数不支持同时指定 `InvocationIds` 和 `Filters`。
        :type InvocationIds: list of str
        :param Filters: 过滤条件。<br> <li> invocation-id - String - 是否必填：否 -（过滤条件）按照执行活动ID过滤。<br> <li> command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。 <br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InvocationIds` 和 `Filters` 。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self.InvocationIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InvocationIds = params.get("InvocationIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInvocationsResponse(AbstractModel):
    """DescribeInvocations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的执行活动总数。
        :type TotalCount: int
        :param InvocationSet: 执行活动列表。
        :type InvocationSet: list of Invocation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InvocationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InvocationSet") is not None:
            self.InvocationSet = []
            for item in params.get("InvocationSet"):
                obj = Invocation()
                obj._deserialize(item)
                self.InvocationSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 地域数量
        :type TotalCount: int
        :param RegionSet: 地域信息列表
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口的`Filter`为例。若我们需要查询可用区（`zone`）为广州一区 ***并且*** 实例计费模式（`instance-charge-type`）为包年包月 ***或者*** 按量计费的实例时，可如下实现：
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Invocation(AbstractModel):
    """执行活动详情。

    """

    def __init__(self):
        """
        :param InvocationId: 执行活动ID。
        :type InvocationId: str
        :param CommandId: 命令ID。
        :type CommandId: str
        :param InvocationStatus: 执行任务状态。取值范围：
<li> PENDING：等待下发 
<li> RUNNING：命令运行中
<li> SUCCESS：命令成功
<li> FAILED：命令失败
<li> TIMEOUT：命令超时
<li> PARTIAL_FAILED：命令部分失败
        :type InvocationStatus: str
        :param InvocationTaskBasicInfoSet: 执行任务信息列表。
        :type InvocationTaskBasicInfoSet: list of InvocationTaskBasicInfo
        :param Description: 执行活动描述。
        :type Description: str
        :param StartTime: 执行活动开始时间。
        :type StartTime: str
        :param EndTime: 执行活动结束时间。
        :type EndTime: str
        :param CreatedTime: 执行活动创建时间。
        :type CreatedTime: str
        :param UpdatedTime: 执行活动更新时间。
        :type UpdatedTime: str
        :param Parameters: 自定义参数取值。
        :type Parameters: str
        :param DefaultParameters: 自定义参数的默认取值。
        :type DefaultParameters: str
        """
        self.InvocationId = None
        self.CommandId = None
        self.InvocationStatus = None
        self.InvocationTaskBasicInfoSet = None
        self.Description = None
        self.StartTime = None
        self.EndTime = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.Parameters = None
        self.DefaultParameters = None


    def _deserialize(self, params):
        self.InvocationId = params.get("InvocationId")
        self.CommandId = params.get("CommandId")
        self.InvocationStatus = params.get("InvocationStatus")
        if params.get("InvocationTaskBasicInfoSet") is not None:
            self.InvocationTaskBasicInfoSet = []
            for item in params.get("InvocationTaskBasicInfoSet"):
                obj = InvocationTaskBasicInfo()
                obj._deserialize(item)
                self.InvocationTaskBasicInfoSet.append(obj)
        self.Description = params.get("Description")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Parameters = params.get("Parameters")
        self.DefaultParameters = params.get("DefaultParameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InvocationTask(AbstractModel):
    """执行任务。

    """

    def __init__(self):
        """
        :param InvocationId: 执行活动ID。
        :type InvocationId: str
        :param InvocationTaskId: 执行任务ID。
        :type InvocationTaskId: str
        :param CommandId: 命令ID。
        :type CommandId: str
        :param TaskStatus: 执行任务状态。取值范围：
<li> PENDING：等待下发 
<li> DELIVERING：下发中
<li> DELIVER_DELAYED：延时下发 
<li> DELIVER_FAILED：下发失败
<li> RUNNING：命令运行中
<li> SUCCESS：命令成功
<li> FAILED：命令失败
<li> TIMEOUT：命令超时
<li> TASK_TIMEOUT：执行任务超时
        :type TaskStatus: str
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param TaskResult: 执行结果。
        :type TaskResult: :class:`tencentcloud.tat.v20201028.models.TaskResult`
        :param StartTime: 执行任务开始时间。
        :type StartTime: str
        :param EndTime: 执行任务结束时间。
        :type EndTime: str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        :param UpdatedTime: 更新时间。
        :type UpdatedTime: str
        :param CommandDocument: 执行任务所执行的命令详情。
        :type CommandDocument: :class:`tencentcloud.tat.v20201028.models.CommandDocument`
        """
        self.InvocationId = None
        self.InvocationTaskId = None
        self.CommandId = None
        self.TaskStatus = None
        self.InstanceId = None
        self.TaskResult = None
        self.StartTime = None
        self.EndTime = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.CommandDocument = None


    def _deserialize(self, params):
        self.InvocationId = params.get("InvocationId")
        self.InvocationTaskId = params.get("InvocationTaskId")
        self.CommandId = params.get("CommandId")
        self.TaskStatus = params.get("TaskStatus")
        self.InstanceId = params.get("InstanceId")
        if params.get("TaskResult") is not None:
            self.TaskResult = TaskResult()
            self.TaskResult._deserialize(params.get("TaskResult"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        if params.get("CommandDocument") is not None:
            self.CommandDocument = CommandDocument()
            self.CommandDocument._deserialize(params.get("CommandDocument"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InvocationTaskBasicInfo(AbstractModel):
    """执行活动任务简介。

    """

    def __init__(self):
        """
        :param InvocationTaskId: 执行任务ID。
        :type InvocationTaskId: str
        :param TaskStatus: 执行任务状态。取值范围：
<li> PENDING：等待下发 
<li> DELIVERING：下发中
<li> DELIVER_DELAYED：延时下发 
<li> DELIVER_FAILED：下发失败
<li> RUNNING：命令运行中
<li> SUCCESS：命令成功
<li> FAILED：命令失败
<li> TIMEOUT：命令超时
<li> TASK_TIMEOUT：执行任务超时
        :type TaskStatus: str
        :param InstanceId: 实例ID。
        :type InstanceId: str
        """
        self.InvocationTaskId = None
        self.TaskStatus = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.InvocationTaskId = params.get("InvocationTaskId")
        self.TaskStatus = params.get("TaskStatus")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InvokeCommandRequest(AbstractModel):
    """InvokeCommand请求参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 待触发的命令ID。
        :type CommandId: str
        :param InstanceIds: 待执行命令的实例ID列表。
        :type InstanceIds: list of str
        :param Parameters: Command 的自定义参数。字段类型为json encoded string。如：{\"varA\": \"222\"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果未提供该参数取值，将使用 Command 的 DefaultParameters 进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type Parameters: str
        """
        self.CommandId = None
        self.InstanceIds = None
        self.Parameters = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.InstanceIds = params.get("InstanceIds")
        self.Parameters = params.get("Parameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InvokeCommandResponse(AbstractModel):
    """InvokeCommand返回参数结构体

    """

    def __init__(self):
        """
        :param InvocationId: 执行活动ID。
        :type InvocationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvocationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvocationId = params.get("InvocationId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyCommandRequest(AbstractModel):
    """ModifyCommand请求参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 命令ID。
        :type CommandId: str
        :param CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type CommandName: str
        :param Description: 命令描述。不超过120字符。
        :type Description: str
        :param Content: Base64编码后的命令内容，长度不可超过64KB。
        :type Content: str
        :param CommandType: 命令类型，目前仅支持取值：SHELL。
        :type CommandType: str
        :param WorkingDirectory: 命令执行路径，默认：`/root`。
        :type WorkingDirectory: str
        :param Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。
        :type Timeout: int
        :param DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{\"varA\": \"222\"}。
采取整体全覆盖式修改，即修改时必须提供所有新默认值。
必须 Command 的 EnableParameter 为 true 时，才允许修改这个值。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type DefaultParameters: str
        """
        self.CommandId = None
        self.CommandName = None
        self.Description = None
        self.Content = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.DefaultParameters = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.CommandName = params.get("CommandName")
        self.Description = params.get("Description")
        self.Content = params.get("Content")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.DefaultParameters = params.get("DefaultParameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyCommandResponse(AbstractModel):
    """ModifyCommand返回参数结构体

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
        


class PreviewReplacedCommandContentRequest(AbstractModel):
    """PreviewReplacedCommandContent请求参数结构体

    """

    def __init__(self):
        """
        :param Parameters: 本次预览采用的自定义参数。字段类型为 json encoded string，如：{\"varA\": \"222\"}。
key 为自定义参数名称，value 为该参数的取值。kv 均为字符串型。
自定义参数最多 20 个。
自定义参数名称需符合以下规范：字符数目上限 64，可选范围【a-zA-Z0-9-_】。
如果将预览的 CommandId 设置过 DefaultParameters，本参数可以为空。
        :type Parameters: str
        :param CommandId: 要进行替换预览的命令，如果有设置过 DefaultParameters，会与 Parameters 进行叠加，后者覆盖前者。
CommandId 与 Content，必须且只能提供一个。
        :type CommandId: str
        :param Content: 要预览的命令内容，经 Base64 编码，长度不可超过 64KB。
CommandId 与 Content，必须且只能提供一个。
        :type Content: str
        """
        self.Parameters = None
        self.CommandId = None
        self.Content = None


    def _deserialize(self, params):
        self.Parameters = params.get("Parameters")
        self.CommandId = params.get("CommandId")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PreviewReplacedCommandContentResponse(AbstractModel):
    """PreviewReplacedCommandContent返回参数结构体

    """

    def __init__(self):
        """
        :param ReplacedContent: 自定义参数替换后的，经Base64编码的命令内容。
        :type ReplacedContent: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReplacedContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplacedContent = params.get("ReplacedContent")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegionInfo(AbstractModel):
    """描述单个地域信息

    """

    def __init__(self):
        """
        :param Region: 地域名称，例如，ap-guangzhou
        :type Region: str
        :param RegionName: 地域描述，例如: 广州
        :type RegionName: str
        :param RegionState: 地域是否可用状态
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunCommandRequest(AbstractModel):
    """RunCommand请求参数结构体

    """

    def __init__(self):
        """
        :param Content: Base64编码后的命令内容，长度不可超过64KB。
        :type Content: str
        :param InstanceIds: 待执行命令的实例ID列表。 支持实例类型：
<li> CVM
<li> LIGHTHOUSE
        :type InstanceIds: list of str
        :param CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type CommandName: str
        :param Description: 命令描述。不超过120字符。
        :type Description: str
        :param CommandType: 命令类型，目前仅支持取值：SHELL。默认：SHELL。
        :type CommandType: str
        :param WorkingDirectory: 命令执行路径，默认：/root。
        :type WorkingDirectory: str
        :param Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。
        :type Timeout: int
        :param SaveCommand: 是否保存命令，取值范围：
<li> True：保存
<li> False：不保存
默认为 False。
        :type SaveCommand: bool
        :param EnableParameter: 是否启用自定义参数功能。
一旦创建，此值不提供修改。
默认值：false。
        :type EnableParameter: bool
        :param DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{\"varA\": \"222\"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果 Parameters 未提供，将使用这里的默认值进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type DefaultParameters: str
        :param Parameters: Command 的自定义参数。字段类型为json encoded string。如：{\"varA\": \"222\"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果未提供该参数取值，将使用 DefaultParameters 进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type Parameters: str
        """
        self.Content = None
        self.InstanceIds = None
        self.CommandName = None
        self.Description = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.SaveCommand = None
        self.EnableParameter = None
        self.DefaultParameters = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.InstanceIds = params.get("InstanceIds")
        self.CommandName = params.get("CommandName")
        self.Description = params.get("Description")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.SaveCommand = params.get("SaveCommand")
        self.EnableParameter = params.get("EnableParameter")
        self.DefaultParameters = params.get("DefaultParameters")
        self.Parameters = params.get("Parameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunCommandResponse(AbstractModel):
    """RunCommand返回参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 命令ID。
        :type CommandId: str
        :param InvocationId: 执行活动ID。
        :type InvocationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CommandId = None
        self.InvocationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.InvocationId = params.get("InvocationId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TaskResult(AbstractModel):
    """任务结果。

    """

    def __init__(self):
        """
        :param ExitCode: 命令执行ExitCode。
        :type ExitCode: int
        :param Output: Base64编码后的命令输出。最大长度24KB。
        :type Output: str
        :param ExecStartTime: 命令执行开始时间。
        :type ExecStartTime: str
        :param ExecEndTime: 命令执行结束时间。
        :type ExecEndTime: str
        :param Dropped: 命令最终输出被截断的字节数。
        :type Dropped: int
        """
        self.ExitCode = None
        self.Output = None
        self.ExecStartTime = None
        self.ExecEndTime = None
        self.Dropped = None


    def _deserialize(self, params):
        self.ExitCode = params.get("ExitCode")
        self.Output = params.get("Output")
        self.ExecStartTime = params.get("ExecStartTime")
        self.ExecEndTime = params.get("ExecEndTime")
        self.Dropped = params.get("Dropped")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        