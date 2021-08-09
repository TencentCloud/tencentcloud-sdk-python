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


class AutomationAgentInfo(AbstractModel):
    """自动化助手客户端信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param Version: Agent 版本号。\n        :type Version: str\n        :param LastHeartbeatTime: 上次心跳时间\n        :type LastHeartbeatTime: str\n        :param AgentStatus: Agent状态，取值范围：
<li> Online：在线
<li> Offline：离线\n        :type AgentStatus: str\n        :param Environment: Agent运行环境\n        :type Environment: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Command(AbstractModel):
    """命令详情。

    """

    def __init__(self):
        """
        :param CommandId: 命令ID。\n        :type CommandId: str\n        :param CommandName: 命令名称。\n        :type CommandName: str\n        :param Description: 命令描述。\n        :type Description: str\n        :param Content: Base64编码后的命令内容。\n        :type Content: str\n        :param CommandType: 命令类型。\n        :type CommandType: str\n        :param WorkingDirectory: 命令执行路径。\n        :type WorkingDirectory: str\n        :param Timeout: 命令超时时间。\n        :type Timeout: int\n        :param CreatedTime: 命令创建时间。\n        :type CreatedTime: str\n        :param UpdatedTime: 命令更新时间。\n        :type UpdatedTime: str\n        :param EnableParameter: 是否启用自定义参数功能。\n        :type EnableParameter: bool\n        :param DefaultParameters: 自定义参数的默认取值。\n        :type DefaultParameters: str\n        :param FormattedDescription: 命令的结构化描述。公共命令有值，用户命令为空字符串。\n        :type FormattedDescription: str\n        :param CreatedBy: 命令创建者。TAT 代表公共命令，USER 代表个人命令。\n        :type CreatedBy: str\n        :param Tags: 命令关联的标签列表。\n        :type Tags: list of Tag\n        :param Username: 在实例上执行命令的用户名。\n        :type Username: str\n        """
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
        self.Tags = None
        self.Username = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommandDocument(AbstractModel):
    """命令执行详情。

    """

    def __init__(self):
        """
        :param Content: Base64 编码后的执行命令。\n        :type Content: str\n        :param CommandType: 命令类型。\n        :type CommandType: str\n        :param Timeout: 超时时间。\n        :type Timeout: int\n        :param WorkingDirectory: 执行路径。\n        :type WorkingDirectory: str\n        :param Username: 执行用户。\n        :type Username: str\n        """
        self.Content = None
        self.CommandType = None
        self.Timeout = None
        self.WorkingDirectory = None
        self.Username = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.CommandType = params.get("CommandType")
        self.Timeout = params.get("Timeout")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandRequest(AbstractModel):
    """CreateCommand请求参数结构体

    """

    def __init__(self):
        """
        :param CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。\n        :type CommandName: str\n        :param Content: Base64编码后的命令内容，长度不可超过64KB。\n        :type Content: str\n        :param Description: 命令描述。不超过120字符。\n        :type Description: str\n        :param CommandType: 命令类型，目前仅支持取值：SHELL。默认：SHELL。\n        :type CommandType: str\n        :param WorkingDirectory: 命令执行路径，默认：/root。\n        :type WorkingDirectory: str\n        :param Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。\n        :type Timeout: int\n        :param EnableParameter: 是否启用自定义参数功能。
一旦创建，此值不提供修改。
默认值：false。\n        :type EnableParameter: bool\n        :param DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{\"varA\": \"222\"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果InvokeCommand时未提供参数取值，将使用这里的默认值进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。\n        :type DefaultParameters: str\n        :param Tags: 为命令关联的标签，列表长度不超过10。\n        :type Tags: list of Tag\n        :param Username: 在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。默认情况下，在Linux实例中以root用户执行命令。\n        :type Username: str\n        """
        self.CommandName = None
        self.Content = None
        self.Description = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.EnableParameter = None
        self.DefaultParameters = None
        self.Tags = None
        self.Username = None


    def _deserialize(self, params):
        self.CommandName = params.get("CommandName")
        self.Content = params.get("Content")
        self.Description = params.get("Description")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.EnableParameter = params.get("EnableParameter")
        self.DefaultParameters = params.get("DefaultParameters")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandResponse(AbstractModel):
    """CreateCommand返回参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 命令ID。\n        :type CommandId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CommandId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.RequestId = params.get("RequestId")


class DeleteCommandRequest(AbstractModel):
    """DeleteCommand请求参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 待删除的命令ID。\n        :type CommandId: str\n        """
        self.CommandId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandResponse(AbstractModel):
    """DeleteCommand返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAutomationAgentStatusRequest(AbstractModel):
    """DescribeAutomationAgentStatus请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 待查询的实例ID列表。\n        :type InstanceIds: list of str\n        :param Filters: 过滤条件。<br> <li> agent-status - String - 是否必填：否 -（过滤条件）按照agent状态过滤，取值：Online 在线，Offline 离线。<br> <li> environment - String - 是否必填：否 -（过滤条件）按照agent运行环境查询，取值：Linux。<br> <li> instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。 <br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InstanceIds` 和 `Filters` 。\n        :type Filters: list of Filter\n        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Limit: int\n        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Offset: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutomationAgentStatusResponse(AbstractModel):
    """DescribeAutomationAgentStatus返回参数结构体

    """

    def __init__(self):
        """
        :param AutomationAgentSet: Agent 信息列表。\n        :type AutomationAgentSet: list of AutomationAgentInfo\n        :param TotalCount: 符合条件的 Agent 总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCommandsRequest(AbstractModel):
    """DescribeCommands请求参数结构体

    """

    def __init__(self):
        """
        :param CommandIds: 命令ID列表，每次请求的上限为100。参数不支持同时指定 `CommandIds` 和 `Filters` 。\n        :type CommandIds: list of str\n        :param Filters: 过滤条件。
<li> command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。
<li> command-name - String - 是否必填：否 -（过滤条件）按照命令名称过滤。
<li> created-by - String - 是否必填：否 -（过滤条件）按照命令创建者过滤，取值为 TAT 或 USER，TAT 代表公共命令，USER 代表由用户创建的命令。 
<li> tag-key - String - 是否必填：否 -（过滤条件）按照标签键进行过滤。</li>
<li> tag-value - String - 是否必填：否 -（过滤条件）按照标签值进行过滤。</li>
<li> tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例4</li>

每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `CommandIds` 和 `Filters` 。\n        :type Filters: list of Filter\n        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Limit: int\n        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Offset: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCommandsResponse(AbstractModel):
    """DescribeCommands返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的命令总数。\n        :type TotalCount: int\n        :param CommandSet: 命令详情列表。\n        :type CommandSet: list of Command\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeInvocationTasksRequest(AbstractModel):
    """DescribeInvocationTasks请求参数结构体

    """

    def __init__(self):
        """
        :param InvocationTaskIds: 执行任务ID列表，每次请求的上限为100。参数不支持同时指定 `InvocationTaskIds` 和 `Filters`。\n        :type InvocationTaskIds: list of str\n        :param Filters: 过滤条件。<br> <li> invocation-id - String - 是否必填：否 -（过滤条件）按照执行活动ID过滤。<br> <li> invocation-task-id - String - 是否必填：否 -（过滤条件）按照执行任务ID过滤。<br> <li> instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。 <br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InvocationTaskIds` 和 `Filters` 。\n        :type Filters: list of Filter\n        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Limit: int\n        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Offset: int\n        :param HideOutput: 是否隐藏输出，取值范围：<br><li>True：隐藏输出 <br><li>False：不隐藏 <br>默认为 True。\n        :type HideOutput: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationTasksResponse(AbstractModel):
    """DescribeInvocationTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的执行任务总数。\n        :type TotalCount: int\n        :param InvocationTaskSet: 执行任务列表。\n        :type InvocationTaskSet: list of InvocationTask\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeInvocationsRequest(AbstractModel):
    """DescribeInvocations请求参数结构体

    """

    def __init__(self):
        """
        :param InvocationIds: 执行活动ID列表，每次请求的上限为100。参数不支持同时指定 `InvocationIds` 和 `Filters`。\n        :type InvocationIds: list of str\n        :param Filters: 过滤条件。<br> <li> invocation-id - String - 是否必填：否 -（过滤条件）按照执行活动ID过滤。<br> 
<li> command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。 
<li> command-created-by - String - 是否必填：否 -（过滤条件）按照执行的命令类型过滤，取值为 TAT 或 USER，TAT 代表公共命令，USER 代表由用户创建的命令。
<li> instance-kind - String - 是否必填：否 -（过滤条件）按照运行实例类型过滤，取值为 CVM 或 LIGHTHOUSE，CVM 代表实例为云服务器， LIGHTHOUSE 代表实例为轻量应用服务器。
<br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InvocationIds` 和 `Filters` 。\n        :type Filters: list of Filter\n        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Limit: int\n        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Offset: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationsResponse(AbstractModel):
    """DescribeInvocations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的执行活动总数。\n        :type TotalCount: int\n        :param InvocationSet: 执行活动列表。\n        :type InvocationSet: list of Invocation\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 地域数量\n        :type TotalCount: int\n        :param RegionSet: 地域信息列表\n        :type RegionSet: list of RegionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Name: 需要过滤的字段。\n        :type Name: str\n        :param Values: 字段的过滤值。\n        :type Values: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Invocation(AbstractModel):
    """执行活动详情。

    """

    def __init__(self):
        """
        :param InvocationId: 执行活动ID。\n        :type InvocationId: str\n        :param CommandId: 命令ID。\n        :type CommandId: str\n        :param InvocationStatus: 执行任务状态。取值范围：
<li> PENDING：等待下发 
<li> RUNNING：命令运行中
<li> SUCCESS：命令成功
<li> FAILED：命令失败
<li> TIMEOUT：命令超时
<li> PARTIAL_FAILED：命令部分失败\n        :type InvocationStatus: str\n        :param InvocationTaskBasicInfoSet: 执行任务信息列表。\n        :type InvocationTaskBasicInfoSet: list of InvocationTaskBasicInfo\n        :param Description: 执行活动描述。\n        :type Description: str\n        :param StartTime: 执行活动开始时间。\n        :type StartTime: str\n        :param EndTime: 执行活动结束时间。\n        :type EndTime: str\n        :param CreatedTime: 执行活动创建时间。\n        :type CreatedTime: str\n        :param UpdatedTime: 执行活动更新时间。\n        :type UpdatedTime: str\n        :param Parameters: 自定义参数取值。\n        :type Parameters: str\n        :param DefaultParameters: 自定义参数的默认取值。\n        :type DefaultParameters: str\n        :param InstanceKind: 执行命令的实例类型，取值范围：CVM、LIGHTHOUSE。\n        :type InstanceKind: str\n        :param Username: 在实例上执行命令时使用的用户名。\n        :type Username: str\n        :param InvocationSource: 调用来源。\n        :type InvocationSource: str\n        """
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
        self.InstanceKind = None
        self.Username = None
        self.InvocationSource = None


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
        self.InstanceKind = params.get("InstanceKind")
        self.Username = params.get("Username")
        self.InvocationSource = params.get("InvocationSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTask(AbstractModel):
    """执行任务。

    """

    def __init__(self):
        """
        :param InvocationId: 执行活动ID。\n        :type InvocationId: str\n        :param InvocationTaskId: 执行任务ID。\n        :type InvocationTaskId: str\n        :param CommandId: 命令ID。\n        :type CommandId: str\n        :param TaskStatus: 执行任务状态。取值范围：
<li> PENDING：等待下发 
<li> DELIVERING：下发中
<li> DELIVER_DELAYED：延时下发 
<li> DELIVER_FAILED：下发失败
<li> RUNNING：命令运行中
<li> SUCCESS：命令成功
<li> FAILED：命令失败
<li> TIMEOUT：命令超时
<li> TASK_TIMEOUT：执行任务超时\n        :type TaskStatus: str\n        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param TaskResult: 执行结果。\n        :type TaskResult: :class:`tencentcloud.tat.v20201028.models.TaskResult`\n        :param StartTime: 执行任务开始时间。\n        :type StartTime: str\n        :param EndTime: 执行任务结束时间。\n        :type EndTime: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param UpdatedTime: 更新时间。\n        :type UpdatedTime: str\n        :param CommandDocument: 执行任务所执行的命令详情。\n        :type CommandDocument: :class:`tencentcloud.tat.v20201028.models.CommandDocument`\n        :param ErrorInfo: 执行任务失败时的错误信息。\n        :type ErrorInfo: str\n        :param InvocationSource: 调用来源。\n        :type InvocationSource: str\n        """
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
        self.ErrorInfo = None
        self.InvocationSource = None


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
        self.ErrorInfo = params.get("ErrorInfo")
        self.InvocationSource = params.get("InvocationSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTaskBasicInfo(AbstractModel):
    """执行活动任务简介。

    """

    def __init__(self):
        """
        :param InvocationTaskId: 执行任务ID。\n        :type InvocationTaskId: str\n        :param TaskStatus: 执行任务状态。取值范围：
<li> PENDING：等待下发 
<li> DELIVERING：下发中
<li> DELIVER_DELAYED：延时下发 
<li> DELIVER_FAILED：下发失败
<li> RUNNING：命令运行中
<li> SUCCESS：命令成功
<li> FAILED：命令失败
<li> TIMEOUT：命令超时
<li> TASK_TIMEOUT：执行任务超时\n        :type TaskStatus: str\n        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCommandRequest(AbstractModel):
    """InvokeCommand请求参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 待触发的命令ID。\n        :type CommandId: str\n        :param InstanceIds: 待执行命令的实例ID列表，上限100。\n        :type InstanceIds: list of str\n        :param Parameters: Command 的自定义参数。字段类型为json encoded string。如：{\"varA\": \"222\"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果未提供该参数取值，将使用 Command 的 DefaultParameters 进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。\n        :type Parameters: str\n        :param Username: 在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。若不填，默认以 Command 配置的 Username 执行。\n        :type Username: str\n        :param WorkingDirectory: 命令执行路径, 默认以Command配置的WorkingDirectory执行。\n        :type WorkingDirectory: str\n        :param Timeout: 命令超时时间，取值范围[1, 86400]。默认以Command配置的Timeout执行。\n        :type Timeout: int\n        """
        self.CommandId = None
        self.InstanceIds = None
        self.Parameters = None
        self.Username = None
        self.WorkingDirectory = None
        self.Timeout = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.InstanceIds = params.get("InstanceIds")
        self.Parameters = params.get("Parameters")
        self.Username = params.get("Username")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCommandResponse(AbstractModel):
    """InvokeCommand返回参数结构体

    """

    def __init__(self):
        """
        :param InvocationId: 执行活动ID。\n        :type InvocationId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InvocationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvocationId = params.get("InvocationId")
        self.RequestId = params.get("RequestId")


class ModifyCommandRequest(AbstractModel):
    """ModifyCommand请求参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 命令ID。\n        :type CommandId: str\n        :param CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。\n        :type CommandName: str\n        :param Description: 命令描述。不超过120字符。\n        :type Description: str\n        :param Content: Base64编码后的命令内容，长度不可超过64KB。\n        :type Content: str\n        :param CommandType: 命令类型，目前仅支持取值：SHELL。\n        :type CommandType: str\n        :param WorkingDirectory: 命令执行路径，默认：`/root`。\n        :type WorkingDirectory: str\n        :param Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。\n        :type Timeout: int\n        :param DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{\"varA\": \"222\"}。
采取整体全覆盖式修改，即修改时必须提供所有新默认值。
必须 Command 的 EnableParameter 为 true 时，才允许修改这个值。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。\n        :type DefaultParameters: str\n        :param Username: 在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。默认情况下，在Linux实例中以root用户执行命令。\n        :type Username: str\n        """
        self.CommandId = None
        self.CommandName = None
        self.Description = None
        self.Content = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.DefaultParameters = None
        self.Username = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.CommandName = params.get("CommandName")
        self.Description = params.get("Description")
        self.Content = params.get("Content")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.DefaultParameters = params.get("DefaultParameters")
        self.Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCommandResponse(AbstractModel):
    """ModifyCommand返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PreviewReplacedCommandContentRequest(AbstractModel):
    """PreviewReplacedCommandContent请求参数结构体

    """

    def __init__(self):
        """
        :param Parameters: 本次预览采用的自定义参数。字段类型为 json encoded string，如：{\"varA\": \"222\"}。
key 为自定义参数名称，value 为该参数的取值。kv 均为字符串型。
自定义参数最多 20 个。
自定义参数名称需符合以下规范：字符数目上限 64，可选范围【a-zA-Z0-9-_】。
如果将预览的 CommandId 设置过 DefaultParameters，本参数可以为空。\n        :type Parameters: str\n        :param CommandId: 要进行替换预览的命令，如果有设置过 DefaultParameters，会与 Parameters 进行叠加，后者覆盖前者。
CommandId 与 Content，必须且只能提供一个。\n        :type CommandId: str\n        :param Content: 要预览的命令内容，经 Base64 编码，长度不可超过 64KB。
CommandId 与 Content，必须且只能提供一个。\n        :type Content: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewReplacedCommandContentResponse(AbstractModel):
    """PreviewReplacedCommandContent返回参数结构体

    """

    def __init__(self):
        """
        :param ReplacedContent: 自定义参数替换后的，经Base64编码的命令内容。\n        :type ReplacedContent: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReplacedContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplacedContent = params.get("ReplacedContent")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """描述单个地域信息

    """

    def __init__(self):
        """
        :param Region: 地域名称，例如，ap-guangzhou\n        :type Region: str\n        :param RegionName: 地域描述，例如: 广州\n        :type RegionName: str\n        :param RegionState: 地域是否可用状态，AVAILABLE 代表可用\n        :type RegionState: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCommandRequest(AbstractModel):
    """RunCommand请求参数结构体

    """

    def __init__(self):
        """
        :param Content: Base64编码后的命令内容，长度不可超过64KB。\n        :type Content: str\n        :param InstanceIds: 待执行命令的实例ID列表，上限100。支持实例类型：
<li> CVM
<li> LIGHTHOUSE\n        :type InstanceIds: list of str\n        :param CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。\n        :type CommandName: str\n        :param Description: 命令描述。不超过120字符。\n        :type Description: str\n        :param CommandType: 命令类型，目前仅支持取值：SHELL。默认：SHELL。\n        :type CommandType: str\n        :param WorkingDirectory: 命令执行路径，默认：/root。\n        :type WorkingDirectory: str\n        :param Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。\n        :type Timeout: int\n        :param SaveCommand: 是否保存命令，取值范围：
<li> True：保存
<li> False：不保存
默认为 False。\n        :type SaveCommand: bool\n        :param EnableParameter: 是否启用自定义参数功能。
一旦创建，此值不提供修改。
默认值：false。\n        :type EnableParameter: bool\n        :param DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{\"varA\": \"222\"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果 Parameters 未提供，将使用这里的默认值进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。\n        :type DefaultParameters: str\n        :param Parameters: Command 的自定义参数。字段类型为json encoded string。如：{\"varA\": \"222\"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果未提供该参数取值，将使用 DefaultParameters 进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。\n        :type Parameters: str\n        :param Tags: 如果保存命令，可为命令设置标签。列表长度不超过10。\n        :type Tags: list of Tag\n        :param Username: 在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。默认情况下，在Linux实例中以root用户执行命令。\n        :type Username: str\n        """
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
        self.Tags = None
        self.Username = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCommandResponse(AbstractModel):
    """RunCommand返回参数结构体

    """

    def __init__(self):
        """
        :param CommandId: 命令ID。\n        :type CommandId: str\n        :param InvocationId: 执行活动ID。\n        :type InvocationId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CommandId = None
        self.InvocationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.InvocationId = params.get("InvocationId")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        """
        :param Key: 标签键。\n        :type Key: str\n        :param Value: 标签值。\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """任务结果。

    """

    def __init__(self):
        """
        :param ExitCode: 命令执行ExitCode。\n        :type ExitCode: int\n        :param Output: Base64编码后的命令输出。最大长度24KB。\n        :type Output: str\n        :param ExecStartTime: 命令执行开始时间。\n        :type ExecStartTime: str\n        :param ExecEndTime: 命令执行结束时间。\n        :type ExecEndTime: str\n        :param Dropped: 命令最终输出被截断的字节数。\n        :type Dropped: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        