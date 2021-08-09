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


class ApplyStackRequest(AbstractModel):
    """ApplyStack请求参数结构体

    """

    def __init__(self):
        """
        :param StackId: 资源栈ID\n        :type StackId: str\n        :param VersionId: 待执行apply事件的版本ID\n        :type VersionId: str\n        """
        self.StackId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.StackId = params.get("StackId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyStackResponse(AbstractModel):
    """ApplyStack返回参数结构体

    """

    def __init__(self):
        """
        :param EventId: 执行的事件ID\n        :type EventId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EventId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.RequestId = params.get("RequestId")


class CreateStackRequest(AbstractModel):
    """CreateStack请求参数结构体

    """

    def __init__(self):
        """
        :param StackName: 资源栈名称，不得超过60个字符\n        :type StackName: str\n        :param StackRegion: 资源栈所在地域\n        :type StackRegion: str\n        :param TemplateUrl: HCL模板URL，⽬前仅限 COS URL, ⽂件为zip压缩格式\n        :type TemplateUrl: str\n        :param Description: 资源栈描述，不得超过200个字符\n        :type Description: str\n        """
        self.StackName = None
        self.StackRegion = None
        self.TemplateUrl = None
        self.Description = None


    def _deserialize(self, params):
        self.StackName = params.get("StackName")
        self.StackRegion = params.get("StackRegion")
        self.TemplateUrl = params.get("TemplateUrl")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStackResponse(AbstractModel):
    """CreateStack返回参数结构体

    """

    def __init__(self):
        """
        :param StackId: 创建得到的资源栈ID\n        :type StackId: str\n        :param VersionId: 资源栈版本ID\n        :type VersionId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.StackId = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StackId = params.get("StackId")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class CreateStackVersionRequest(AbstractModel):
    """CreateStackVersion请求参数结构体

    """

    def __init__(self):
        """
        :param StackId: 待增加版本的资源栈ID\n        :type StackId: str\n        :param TemplateUrl: 模板 URL，⽬前仅限 COS URL, ⽂件为zip压缩格式\n        :type TemplateUrl: str\n        :param VersionName: 版本名称，不得超过60个字符\n        :type VersionName: str\n        :param Description: 版本描述，不得超过200个字符\n        :type Description: str\n        """
        self.StackId = None
        self.TemplateUrl = None
        self.VersionName = None
        self.Description = None


    def _deserialize(self, params):
        self.StackId = params.get("StackId")
        self.TemplateUrl = params.get("TemplateUrl")
        self.VersionName = params.get("VersionName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStackVersionResponse(AbstractModel):
    """CreateStackVersion返回参数结构体

    """

    def __init__(self):
        """
        :param VersionId: 新创建的版本ID\n        :type VersionId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class DeleteStackRequest(AbstractModel):
    """DeleteStack请求参数结构体

    """

    def __init__(self):
        """
        :param StackId: 待删除的资源栈ID\n        :type StackId: str\n        """
        self.StackId = None


    def _deserialize(self, params):
        self.StackId = params.get("StackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStackResponse(AbstractModel):
    """DeleteStack返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStackVersionRequest(AbstractModel):
    """DeleteStackVersion请求参数结构体

    """

    def __init__(self):
        """
        :param VersionId: 待删除的版本ID\n        :type VersionId: str\n        """
        self.VersionId = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStackVersionResponse(AbstractModel):
    """DeleteStackVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeStackEventRequest(AbstractModel):
    """DescribeStackEvent请求参数结构体

    """

    def __init__(self):
        """
        :param EventId: 事件ID\n        :type EventId: str\n        """
        self.EventId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStackEventResponse(AbstractModel):
    """DescribeStackEvent返回参数结构体

    """

    def __init__(self):
        """
        :param EventId: 事件ID\n        :type EventId: str\n        :param VersionId: 版本ID\n        :type VersionId: str\n        :param StackId: 资源栈ID\n        :type StackId: str\n        :param Type: 事件类型\n        :type Type: str\n        :param Status: 事件状态\n        :type Status: str\n        :param EventMessage: 状态信息\n        :type EventMessage: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param ConsoleLog: 控制台输出文本\n        :type ConsoleLog: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EventId = None
        self.VersionId = None
        self.StackId = None
        self.Type = None
        self.Status = None
        self.EventMessage = None
        self.CreateTime = None
        self.ConsoleLog = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.VersionId = params.get("VersionId")
        self.StackId = params.get("StackId")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.EventMessage = params.get("EventMessage")
        self.CreateTime = params.get("CreateTime")
        self.ConsoleLog = params.get("ConsoleLog")
        self.RequestId = params.get("RequestId")


class DescribeStackEventsRequest(AbstractModel):
    """DescribeStackEvents请求参数结构体

    """

    def __init__(self):
        """
        :param EventIds: 按照⼀个或者多个事件ID查询\n        :type EventIds: list of str\n        :param Filters: <li>**VersionId**</li>
按照【**版本ID**】过滤，VersionId形如 `ver-kg8hn58h`
类型：string

<li>**StackId**</li>
按照【**资源栈ID**】过滤，StackId形如 `stk-hz5vn3te`
类型：string

<li>**Type**</li>
按照【**事件类型**】过滤，Type 形如 plan, apply, destroy
类型：string

<li>**Status**</li>
按照【**事件状态**】过滤，Status形如 queueing, running, success, failed
类型：string\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节\n        :type Limit: int\n        """
        self.EventIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EventIds = params.get("EventIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStackEventsResponse(AbstractModel):
    """DescribeStackEvents返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的事件数量\n        :type TotalCount: int\n        :param Events: 事件详细信息列表\n        :type Events: list of EventInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStackVersionsRequest(AbstractModel):
    """DescribeStackVersions请求参数结构体

    """

    def __init__(self):
        """
        :param VersionIds: 按照⼀个或者多个版本ID查询\n        :type VersionIds: list of str\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节\n        :type Limit: int\n        :param Filters: <li>**Name**</li>
按照【**版本名称**】进行过滤
类型：string

<li>**Status**</li>
按照【**版本状态**】过滤，形如`VERSION_EDITING`，`PLAN_IN_PROGRESS`等
类型：string

<li>**StackId**</li>
按照版本所属的【**资源栈ID**】进行过滤，形如`stk-xxxxxx`
类型：string\n        :type Filters: list of Filter\n        """
        self.VersionIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.VersionIds = params.get("VersionIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStackVersionsResponse(AbstractModel):
    """DescribeStackVersions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的版本数量\n        :type TotalCount: int\n        :param Versions: 版本详细信息列表\n        :type Versions: list of VersionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = VersionInfo()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStacksRequest(AbstractModel):
    """DescribeStacks请求参数结构体

    """

    def __init__(self):
        """
        :param StackIds: 按照⼀个或者多个资源栈ID查询\n        :type StackIds: list of str\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Limit: int\n        """
        self.StackIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StackIds = params.get("StackIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStacksResponse(AbstractModel):
    """DescribeStacks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的资源栈数量\n        :type TotalCount: int\n        :param Stacks: 资源栈详细信息列表\n        :type Stacks: list of StackInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Stacks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Stacks") is not None:
            self.Stacks = []
            for item in params.get("Stacks"):
                obj = StackInfo()
                obj._deserialize(item)
                self.Stacks.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyStackRequest(AbstractModel):
    """DestroyStack请求参数结构体

    """

    def __init__(self):
        """
        :param StackId: 资源栈ID\n        :type StackId: str\n        :param VersionId: 待执行destroy事件的版本ID\n        :type VersionId: str\n        """
        self.StackId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.StackId = params.get("StackId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyStackResponse(AbstractModel):
    """DestroyStack返回参数结构体

    """

    def __init__(self):
        """
        :param EventId: 事件ID\n        :type EventId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EventId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.RequestId = params.get("RequestId")


class EventInfo(AbstractModel):
    """事件详情

    """

    def __init__(self):
        """
        :param EventId: 事件ID\n        :type EventId: str\n        :param VersionId: 版本ID\n        :type VersionId: str\n        :param StackId: 资源栈ID\n        :type StackId: str\n        :param Type: 事件类型\n        :type Type: str\n        :param Status: 版本状态\n        :type Status: str\n        :param Message: 状态信息\n        :type Message: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        """
        self.EventId = None
        self.VersionId = None
        self.StackId = None
        self.Type = None
        self.Status = None
        self.Message = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.VersionId = params.get("VersionId")
        self.StackId = params.get("StackId")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤条件

    """

    def __init__(self):
        """
        :param Name: 条件名字\n        :type Name: str\n        :param Values: 匹配的值，可以有多个\n        :type Values: list of str\n        """
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
        


class PlanStackRequest(AbstractModel):
    """PlanStack请求参数结构体

    """

    def __init__(self):
        """
        :param StackId: 资源栈ID\n        :type StackId: str\n        :param VersionId: 待执行plan事件的版本ID\n        :type VersionId: str\n        """
        self.StackId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.StackId = params.get("StackId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanStackResponse(AbstractModel):
    """PlanStack返回参数结构体

    """

    def __init__(self):
        """
        :param EventId: 执行的事件ID\n        :type EventId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EventId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.RequestId = params.get("RequestId")


class StackInfo(AbstractModel):
    """资源栈信息

    """

    def __init__(self):
        """
        :param StackId: 资源栈ID\n        :type StackId: str\n        :param StackName: 资源栈名称\n        :type StackName: str\n        :param Description: 资源栈描述\n        :type Description: str\n        :param Region: 所处地域\n        :type Region: str\n        :param Status: 资源栈状态\n        :type Status: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        """
        self.StackId = None
        self.StackName = None
        self.Description = None
        self.Region = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.StackId = params.get("StackId")
        self.StackName = params.get("StackName")
        self.Description = params.get("Description")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStackRequest(AbstractModel):
    """UpdateStack请求参数结构体

    """

    def __init__(self):
        """
        :param StackId: 待更新的资源栈ID\n        :type StackId: str\n        :param StackName: 资源栈名称，不得超过60个字符\n        :type StackName: str\n        :param Description: 资源栈描述，不得超过200个字符\n        :type Description: str\n        """
        self.StackId = None
        self.StackName = None
        self.Description = None


    def _deserialize(self, params):
        self.StackId = params.get("StackId")
        self.StackName = params.get("StackName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStackResponse(AbstractModel):
    """UpdateStack返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateStackVersionRequest(AbstractModel):
    """UpdateStackVersion请求参数结构体

    """

    def __init__(self):
        """
        :param VersionId: 待更新的版本ID\n        :type VersionId: str\n        :param TemplateUrl: 模板 URL，⽬前仅限 COS URL, ⽂件为zip压缩格式\n        :type TemplateUrl: str\n        :param VersionName: 版本名称，不得超过60个字符\n        :type VersionName: str\n        :param Description: 版本描述，不得超过200个字符\n        :type Description: str\n        """
        self.VersionId = None
        self.TemplateUrl = None
        self.VersionName = None
        self.Description = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.TemplateUrl = params.get("TemplateUrl")
        self.VersionName = params.get("VersionName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStackVersionResponse(AbstractModel):
    """UpdateStackVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VersionInfo(AbstractModel):
    """版本信息

    """

    def __init__(self):
        """
        :param VersionId: 版本ID\n        :type VersionId: str\n        :param VersionName: 版本名称\n        :type VersionName: str\n        :param Description: 版本描述\n        :type Description: str\n        :param StackId: 资源栈ID\n        :type StackId: str\n        :param Status: 版本状态\n        :type Status: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        """
        self.VersionId = None
        self.VersionName = None
        self.Description = None
        self.StackId = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.VersionName = params.get("VersionName")
        self.Description = params.get("Description")
        self.StackId = params.get("StackId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        