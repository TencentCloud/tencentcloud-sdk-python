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
        r"""
        :param _StackId: 资源栈ID
        :type StackId: str
        :param _VersionId: 待执行apply事件的版本ID
        :type VersionId: str
        """
        self._StackId = None
        self._VersionId = None

    @property
    def StackId(self):
        """资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def VersionId(self):
        """待执行apply事件的版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._StackId = params.get("StackId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyStackResponse(AbstractModel):
    """ApplyStack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventId: 执行的事件ID
        :type EventId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventId = None
        self._RequestId = None

    @property
    def EventId(self):
        """执行的事件ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._RequestId = params.get("RequestId")


class CreateStackRequest(AbstractModel):
    """CreateStack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StackName: 资源栈名称，不得超过60个字符
        :type StackName: str
        :param _StackRegion: 资源栈所在地域
        :type StackRegion: str
        :param _TemplateUrl: HCL模板URL，⽬前仅限 COS URL, ⽂件为zip压缩格式
        :type TemplateUrl: str
        :param _Description: 资源栈描述，不得超过200个字符
        :type Description: str
        """
        self._StackName = None
        self._StackRegion = None
        self._TemplateUrl = None
        self._Description = None

    @property
    def StackName(self):
        """资源栈名称，不得超过60个字符
        :rtype: str
        """
        return self._StackName

    @StackName.setter
    def StackName(self, StackName):
        self._StackName = StackName

    @property
    def StackRegion(self):
        """资源栈所在地域
        :rtype: str
        """
        return self._StackRegion

    @StackRegion.setter
    def StackRegion(self, StackRegion):
        self._StackRegion = StackRegion

    @property
    def TemplateUrl(self):
        """HCL模板URL，⽬前仅限 COS URL, ⽂件为zip压缩格式
        :rtype: str
        """
        return self._TemplateUrl

    @TemplateUrl.setter
    def TemplateUrl(self, TemplateUrl):
        self._TemplateUrl = TemplateUrl

    @property
    def Description(self):
        """资源栈描述，不得超过200个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._StackName = params.get("StackName")
        self._StackRegion = params.get("StackRegion")
        self._TemplateUrl = params.get("TemplateUrl")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStackResponse(AbstractModel):
    """CreateStack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StackId: 创建得到的资源栈ID
        :type StackId: str
        :param _VersionId: 资源栈版本ID
        :type VersionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StackId = None
        self._VersionId = None
        self._RequestId = None

    @property
    def StackId(self):
        """创建得到的资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def VersionId(self):
        """资源栈版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StackId = params.get("StackId")
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class CreateStackVersionRequest(AbstractModel):
    """CreateStackVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StackId: 待增加版本的资源栈ID
        :type StackId: str
        :param _TemplateUrl: 模板 URL，⽬前仅限 COS URL, ⽂件为zip压缩格式
        :type TemplateUrl: str
        :param _VersionName: 版本名称，不得超过60个字符
        :type VersionName: str
        :param _Description: 版本描述，不得超过200个字符
        :type Description: str
        """
        self._StackId = None
        self._TemplateUrl = None
        self._VersionName = None
        self._Description = None

    @property
    def StackId(self):
        """待增加版本的资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def TemplateUrl(self):
        """模板 URL，⽬前仅限 COS URL, ⽂件为zip压缩格式
        :rtype: str
        """
        return self._TemplateUrl

    @TemplateUrl.setter
    def TemplateUrl(self, TemplateUrl):
        self._TemplateUrl = TemplateUrl

    @property
    def VersionName(self):
        """版本名称，不得超过60个字符
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Description(self):
        """版本描述，不得超过200个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._StackId = params.get("StackId")
        self._TemplateUrl = params.get("TemplateUrl")
        self._VersionName = params.get("VersionName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStackVersionResponse(AbstractModel):
    """CreateStackVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionId: 新创建的版本ID
        :type VersionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionId = None
        self._RequestId = None

    @property
    def VersionId(self):
        """新创建的版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class DeleteStackRequest(AbstractModel):
    """DeleteStack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StackId: 待删除的资源栈ID
        :type StackId: str
        """
        self._StackId = None

    @property
    def StackId(self):
        """待删除的资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId


    def _deserialize(self, params):
        self._StackId = params.get("StackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStackResponse(AbstractModel):
    """DeleteStack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteStackVersionRequest(AbstractModel):
    """DeleteStackVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionId: 待删除的版本ID
        :type VersionId: str
        """
        self._VersionId = None

    @property
    def VersionId(self):
        """待删除的版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStackVersionResponse(AbstractModel):
    """DeleteStackVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeStackEventRequest(AbstractModel):
    """DescribeStackEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventId: 事件ID
        :type EventId: str
        """
        self._EventId = None

    @property
    def EventId(self):
        """事件ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStackEventResponse(AbstractModel):
    """DescribeStackEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventId: 事件ID
        :type EventId: str
        :param _VersionId: 版本ID
        :type VersionId: str
        :param _StackId: 资源栈ID
        :type StackId: str
        :param _Type: 事件类型
        :type Type: str
        :param _Status: 事件状态
        :type Status: str
        :param _EventMessage: 状态信息
        :type EventMessage: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ConsoleLog: 控制台输出文本
        :type ConsoleLog: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventId = None
        self._VersionId = None
        self._StackId = None
        self._Type = None
        self._Status = None
        self._EventMessage = None
        self._CreateTime = None
        self._ConsoleLog = None
        self._RequestId = None

    @property
    def EventId(self):
        """事件ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def VersionId(self):
        """版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def StackId(self):
        """资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def Type(self):
        """事件类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """事件状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventMessage(self):
        """状态信息
        :rtype: str
        """
        return self._EventMessage

    @EventMessage.setter
    def EventMessage(self, EventMessage):
        self._EventMessage = EventMessage

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
    def ConsoleLog(self):
        """控制台输出文本
        :rtype: str
        """
        return self._ConsoleLog

    @ConsoleLog.setter
    def ConsoleLog(self, ConsoleLog):
        self._ConsoleLog = ConsoleLog

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._VersionId = params.get("VersionId")
        self._StackId = params.get("StackId")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._EventMessage = params.get("EventMessage")
        self._CreateTime = params.get("CreateTime")
        self._ConsoleLog = params.get("ConsoleLog")
        self._RequestId = params.get("RequestId")


class DescribeStackEventsRequest(AbstractModel):
    """DescribeStackEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventIds: 按照⼀个或者多个事件ID查询
        :type EventIds: list of str
        :param _Filters: <li>**VersionId**</li>
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
类型：string
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节
        :type Limit: int
        """
        self._EventIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def EventIds(self):
        """按照⼀个或者多个事件ID查询
        :rtype: list of str
        """
        return self._EventIds

    @EventIds.setter
    def EventIds(self, EventIds):
        self._EventIds = EventIds

    @property
    def Filters(self):
        """<li>**VersionId**</li>
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
类型：string
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._EventIds = params.get("EventIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStackEventsResponse(AbstractModel):
    """DescribeStackEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的事件数量
        :type TotalCount: int
        :param _Events: 事件详细信息列表
        :type Events: list of EventInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Events = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的事件数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Events(self):
        """事件详细信息列表
        :rtype: list of EventInfo
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = EventInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStackVersionsRequest(AbstractModel):
    """DescribeStackVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionIds: 按照⼀个或者多个版本ID查询
        :type VersionIds: list of str
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节
        :type Limit: int
        :param _Filters: <li>**Name**</li>
按照【**版本名称**】进行过滤
类型：string

<li>**Status**</li>
按照【**版本状态**】过滤，形如`VERSION_EDITING`，`PLAN_IN_PROGRESS`等
类型：string

<li>**StackId**</li>
按照版本所属的【**资源栈ID**】进行过滤，形如`stk-xxxxxx`
类型：string
        :type Filters: list of Filter
        """
        self._VersionIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def VersionIds(self):
        """按照⼀个或者多个版本ID查询
        :rtype: list of str
        """
        return self._VersionIds

    @VersionIds.setter
    def VersionIds(self, VersionIds):
        self._VersionIds = VersionIds

    @property
    def Offset(self):
        """偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """<li>**Name**</li>
按照【**版本名称**】进行过滤
类型：string

<li>**Status**</li>
按照【**版本状态**】过滤，形如`VERSION_EDITING`，`PLAN_IN_PROGRESS`等
类型：string

<li>**StackId**</li>
按照版本所属的【**资源栈ID**】进行过滤，形如`stk-xxxxxx`
类型：string
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._VersionIds = params.get("VersionIds")
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
        


class DescribeStackVersionsResponse(AbstractModel):
    """DescribeStackVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的版本数量
        :type TotalCount: int
        :param _Versions: 版本详细信息列表
        :type Versions: list of VersionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Versions = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的版本数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Versions(self):
        """版本详细信息列表
        :rtype: list of VersionInfo
        """
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = VersionInfo()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStacksRequest(AbstractModel):
    """DescribeStacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StackIds: 按照⼀个或者多个资源栈ID查询
        :type StackIds: list of str
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._StackIds = None
        self._Offset = None
        self._Limit = None

    @property
    def StackIds(self):
        """按照⼀个或者多个资源栈ID查询
        :rtype: list of str
        """
        return self._StackIds

    @StackIds.setter
    def StackIds(self, StackIds):
        self._StackIds = StackIds

    @property
    def Offset(self):
        """偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StackIds = params.get("StackIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStacksResponse(AbstractModel):
    """DescribeStacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的资源栈数量
        :type TotalCount: int
        :param _Stacks: 资源栈详细信息列表
        :type Stacks: list of StackInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Stacks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的资源栈数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Stacks(self):
        """资源栈详细信息列表
        :rtype: list of StackInfo
        """
        return self._Stacks

    @Stacks.setter
    def Stacks(self, Stacks):
        self._Stacks = Stacks

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Stacks") is not None:
            self._Stacks = []
            for item in params.get("Stacks"):
                obj = StackInfo()
                obj._deserialize(item)
                self._Stacks.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyStackRequest(AbstractModel):
    """DestroyStack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StackId: 资源栈ID
        :type StackId: str
        :param _VersionId: 待执行destroy事件的版本ID
        :type VersionId: str
        """
        self._StackId = None
        self._VersionId = None

    @property
    def StackId(self):
        """资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def VersionId(self):
        """待执行destroy事件的版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._StackId = params.get("StackId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyStackResponse(AbstractModel):
    """DestroyStack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventId: 事件ID
        :type EventId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventId = None
        self._RequestId = None

    @property
    def EventId(self):
        """事件ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._RequestId = params.get("RequestId")


class EventInfo(AbstractModel):
    """事件详情

    """

    def __init__(self):
        r"""
        :param _EventId: 事件ID
        :type EventId: str
        :param _VersionId: 版本ID
        :type VersionId: str
        :param _StackId: 资源栈ID
        :type StackId: str
        :param _Type: 事件类型
        :type Type: str
        :param _Status: 版本状态
        :type Status: str
        :param _Message: 状态信息
        :type Message: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._EventId = None
        self._VersionId = None
        self._StackId = None
        self._Type = None
        self._Status = None
        self._Message = None
        self._CreateTime = None

    @property
    def EventId(self):
        """事件ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def VersionId(self):
        """版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def StackId(self):
        """资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def Type(self):
        """事件类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """版本状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        """状态信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._VersionId = params.get("VersionId")
        self._StackId = params.get("StackId")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 条件名字
        :type Name: str
        :param _Values: 匹配的值，可以有多个
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """条件名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """匹配的值，可以有多个
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
        


class PlanStackRequest(AbstractModel):
    """PlanStack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StackId: 资源栈ID
        :type StackId: str
        :param _VersionId: 待执行plan事件的版本ID
        :type VersionId: str
        """
        self._StackId = None
        self._VersionId = None

    @property
    def StackId(self):
        """资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def VersionId(self):
        """待执行plan事件的版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._StackId = params.get("StackId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanStackResponse(AbstractModel):
    """PlanStack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventId: 执行的事件ID
        :type EventId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventId = None
        self._RequestId = None

    @property
    def EventId(self):
        """执行的事件ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._RequestId = params.get("RequestId")


class StackInfo(AbstractModel):
    """资源栈信息

    """

    def __init__(self):
        r"""
        :param _StackId: 资源栈ID
        :type StackId: str
        :param _StackName: 资源栈名称
        :type StackName: str
        :param _Description: 资源栈描述
        :type Description: str
        :param _Region: 所处地域
        :type Region: str
        :param _Status: 资源栈状态
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._StackId = None
        self._StackName = None
        self._Description = None
        self._Region = None
        self._Status = None
        self._CreateTime = None

    @property
    def StackId(self):
        """资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def StackName(self):
        """资源栈名称
        :rtype: str
        """
        return self._StackName

    @StackName.setter
    def StackName(self, StackName):
        self._StackName = StackName

    @property
    def Description(self):
        """资源栈描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Region(self):
        """所处地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        """资源栈状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._StackId = params.get("StackId")
        self._StackName = params.get("StackName")
        self._Description = params.get("Description")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStackRequest(AbstractModel):
    """UpdateStack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StackId: 待更新的资源栈ID
        :type StackId: str
        :param _StackName: 资源栈名称，不得超过60个字符
        :type StackName: str
        :param _Description: 资源栈描述，不得超过200个字符
        :type Description: str
        """
        self._StackId = None
        self._StackName = None
        self._Description = None

    @property
    def StackId(self):
        """待更新的资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def StackName(self):
        """资源栈名称，不得超过60个字符
        :rtype: str
        """
        return self._StackName

    @StackName.setter
    def StackName(self, StackName):
        self._StackName = StackName

    @property
    def Description(self):
        """资源栈描述，不得超过200个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._StackId = params.get("StackId")
        self._StackName = params.get("StackName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStackResponse(AbstractModel):
    """UpdateStack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateStackVersionRequest(AbstractModel):
    """UpdateStackVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionId: 待更新的版本ID
        :type VersionId: str
        :param _TemplateUrl: 模板 URL，⽬前仅限 COS URL, ⽂件为zip压缩格式
        :type TemplateUrl: str
        :param _VersionName: 版本名称，不得超过60个字符
        :type VersionName: str
        :param _Description: 版本描述，不得超过200个字符
        :type Description: str
        """
        self._VersionId = None
        self._TemplateUrl = None
        self._VersionName = None
        self._Description = None

    @property
    def VersionId(self):
        """待更新的版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def TemplateUrl(self):
        """模板 URL，⽬前仅限 COS URL, ⽂件为zip压缩格式
        :rtype: str
        """
        return self._TemplateUrl

    @TemplateUrl.setter
    def TemplateUrl(self, TemplateUrl):
        self._TemplateUrl = TemplateUrl

    @property
    def VersionName(self):
        """版本名称，不得超过60个字符
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Description(self):
        """版本描述，不得超过200个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._TemplateUrl = params.get("TemplateUrl")
        self._VersionName = params.get("VersionName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStackVersionResponse(AbstractModel):
    """UpdateStackVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class VersionInfo(AbstractModel):
    """版本信息

    """

    def __init__(self):
        r"""
        :param _VersionId: 版本ID
        :type VersionId: str
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _Description: 版本描述
        :type Description: str
        :param _StackId: 资源栈ID
        :type StackId: str
        :param _Status: 版本状态
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._VersionId = None
        self._VersionName = None
        self._Description = None
        self._StackId = None
        self._Status = None
        self._CreateTime = None

    @property
    def VersionId(self):
        """版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionName(self):
        """版本名称
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Description(self):
        """版本描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StackId(self):
        """资源栈ID
        :rtype: str
        """
        return self._StackId

    @StackId.setter
    def StackId(self, StackId):
        self._StackId = StackId

    @property
    def Status(self):
        """版本状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._VersionName = params.get("VersionName")
        self._Description = params.get("Description")
        self._StackId = params.get("StackId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        