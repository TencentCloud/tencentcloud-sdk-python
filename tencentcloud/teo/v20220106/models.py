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


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Targets: 要预热的资源列表，每个元素格式类似如下:
http://www.example.com/example.txt
        :type Targets: list of str
        :param EncodeUrl: 是否对url进行encode
若内容含有非 ASCII 字符集的字符，请开启此开关，编码转换（编码规则遵循 RFC3986）
        :type EncodeUrl: bool
        :param Headers: 附带的http头部信息
        :type Headers: list of Header
        """
        self.ZoneId = None
        self.Targets = None
        self.EncodeUrl = None
        self.Headers = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param FailedList: 失败的任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of FailReason
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Type: 类型，当前支持的类型：
- purge_url：URL
- purge_prefix：前缀
- purge_host：Hostname
- purge_all：全部缓存
        :type Type: str
        :param Targets: 要刷新的资源列表，每个元素格式依据Type而定
1) Type = purge_host 时
形如：www.example.com 或 foo.bar.example.com
2) Type = purge_prefix 时
形如：http://www.example.com/example
3) Type = purge_url 时
形如：https://www.example.com/example.jpg
4）Type = purge_all 时
Targets可为空，不需要填写
        :type Targets: list of str
        :param EncodeUrl: 若有编码转换，仅清除编码转换后匹配的资源
若内容含有非 ASCII 字符集的字符，请开启此开关，编码转换（编码规则遵循 RFC3986）
        :type EncodeUrl: bool
        """
        self.ZoneId = None
        self.Type = None
        self.Targets = None
        self.EncodeUrl = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param FailedList: 失败的任务列表及原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of FailReason
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param StartTime: 查询起始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Offset: 查询起始偏移量
        :type Offset: int
        :param Limit: 查询最大返回的结果条数
        :type Limit: int
        :param Statuses: 查询的状态
允许的值为：processing、success、failed、timeout、invalid
        :type Statuses: list of str
        :param ZoneId: zone id
        :type ZoneId: str
        :param Domains: 查询的域名列表
        :type Domains: list of str
        :param Target: 查询的资源
        :type Target: str
        """
        self.JobId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 该查询条件总共条目数
        :type TotalCount: int
        :param Tasks: 任务结果列表
        :type Tasks: list of Task
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param Type: 类型
        :type Type: str
        :param StartTime: 查询起始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Offset: 查询起始偏移量
        :type Offset: int
        :param Limit: 查询最大返回的结果条数
        :type Limit: int
        :param Statuses: 查询的状态
允许的值为：processing、success、failed、timeout、invalid
        :type Statuses: list of str
        :param ZoneId: zone id
        :type ZoneId: str
        :param Domains: 查询的域名列表
        :type Domains: list of str
        :param Target: 查询内容
        :type Target: str
        """
        self.JobId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 该查询条件总共条目数
        :type TotalCount: int
        :param Tasks: 任务结果列表
        :type Tasks: list of Task
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页查询偏移量。默认值：0，最小值：0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值：1000，最大值：1000。
        :type Limit: int
        :param Filters: 查询条件过滤器，复杂类型。
        :type Filters: list of ZoneFilter
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
                obj = ZoneFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的站点个数。
        :type TotalCount: int
        :param Zones: 站点详细信息列表。
        :type Zones: list of Zone
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Zones = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RequestId = params.get("RequestId")


class FailReason(AbstractModel):
    """失败原因

    """

    def __init__(self):
        r"""
        :param Reason: 失败原因
        :type Reason: str
        :param Targets: 处理失败的资源列表。
该列表元素来源于输入参数中的Targets，因此格式和入参中的Targets保持一致
        :type Targets: list of str
        """
        self.Reason = None
        self.Targets = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """刷新预热附带的头部信息

    """

    def __init__(self):
        r"""
        :param Name: HTTP头部
        :type Name: str
        :param Value: HTTP头部值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """计费资源

    """

    def __init__(self):
        r"""
        :param Id: 资源 ID。
        :type Id: str
        :param PayMode: 付费模式，取值有：
<li>0：后付费。</li>
        :type PayMode: int
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param EnableTime: 生效时间。
        :type EnableTime: str
        :param ExpireTime: 失效时间。
        :type ExpireTime: str
        :param Status: 套餐状态，取值有：
<li>normal：正常；</li>
<li>isolated：隔离；</li>
<li>destroyed：销毁。</li>
        :type Status: str
        :param Sv: 询价参数。
        :type Sv: list of Sv
        :param AutoRenewFlag: 是否自动续费，取值有：
<li>0：默认状态；</li>
<li>1：自动续费；</li>
<li>2：不自动续费。</li>
        :type AutoRenewFlag: int
        :param PlanId: 套餐关联资源 ID。
        :type PlanId: str
        :param Area: 地域，取值有：
<li>mainland：国内；</li>
<li>overseas：海外。</li>
        :type Area: str
        """
        self.Id = None
        self.PayMode = None
        self.CreateTime = None
        self.EnableTime = None
        self.ExpireTime = None
        self.Status = None
        self.Sv = None
        self.AutoRenewFlag = None
        self.PlanId = None
        self.Area = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.EnableTime = params.get("EnableTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")
        if params.get("Sv") is not None:
            self.Sv = []
            for item in params.get("Sv"):
                obj = Sv()
                obj._deserialize(item)
                self.Sv.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PlanId = params.get("PlanId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sv(AbstractModel):
    """询价参数

    """

    def __init__(self):
        r"""
        :param Key: 询价参数键。
        :type Key: str
        :param Value: 询价参数值。
        :type Value: str
        """
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
        


class Tag(AbstractModel):
    """标签配置

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """内容管理任务结果

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param Status: 状态
        :type Status: str
        :param Target: 资源
        :type Target: str
        :param Type: 任务类型
        :type Type: str
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param UpdateTime: 任务完成时间
        :type UpdateTime: str
        """
        self.JobId = None
        self.Status = None
        self.Target = None
        self.Type = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Status = params.get("Status")
        self.Target = params.get("Target")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """站点信息

    """

    def __init__(self):
        r"""
        :param Id: 站点ID。
        :type Id: str
        :param Name: 站点名称。
        :type Name: str
        :param OriginalNameServers: 站点当前使用的 NS 列表。
        :type OriginalNameServers: list of str
        :param NameServers: 腾讯云分配的 NS 列表。
        :type NameServers: list of str
        :param Status: 站点状态，取值有：
<li> active：NS 已切换； </li>
<li> pending：NS 未切换；</li>
<li> moved：NS 已切走；</li>
<li> deactivated：被封禁。 </li>
        :type Status: str
        :param Type: 站点接入方式，取值有
<li> full：NS 接入； </li>
<li> partial：CNAME 接入。</li>
        :type Type: str
        :param Paused: 站点是否关闭。
        :type Paused: bool
        :param CnameSpeedUp: 是否开启cname加速，取值有：
<li> enabled：开启；</li>
<li> disabled：关闭。</li>
        :type CnameSpeedUp: str
        :param CnameStatus: cname 接入状态，取值有：
<li> finished：站点已验证；</li>
<li> pending：站点验证中。</li>
        :type CnameStatus: str
        :param Tags: 资源标签列表。
        :type Tags: list of Tag
        :param Resources: 计费资源列表。
        :type Resources: list of Resource
        :param CreatedOn: 站点创建时间。
        :type CreatedOn: str
        :param ModifiedOn: 站点修改时间。
        :type ModifiedOn: str
        :param Area: 站点接入地域，取值为：
<li> global：全球；</li>
<li> mainland：中国大陆；</li>
<li> overseas：境外区域。</li>
        :type Area: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.Tags = None
        self.Resources = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.Area = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CnameSpeedUp = params.get("CnameSpeedUp")
        self.CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneFilter(AbstractModel):
    """站点查询过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名，支持的列表如下：
<li> name：站点名；</li>
<li> status：站点状态；</li>
<li> tagKey：标签键；</li>
<li> tagValue: 标签值。</li>
        :type Name: str
        :param Values: 过滤字段值。
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为name。模糊查询时，Values长度最大为1。默认为false。
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        