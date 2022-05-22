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


class AgentGroup(AbstractModel):
    """拨测分组

    """

    def __init__(self):
        r"""
        :param GroupId: 拨测分组ID
        :type GroupId: int
        :param GroupName: 拨测分组名称
        :type GroupName: str
        :param IsDefault: 是否默认拨测分组。1表示是，0表示否
        :type IsDefault: int
        :param TaskNum: 使用本拨测分组的任务数
        :type TaskNum: int
        :param GroupDetail: 拨测结点列表
        :type GroupDetail: list of CatAgent
        :param MaxGroupNum: 最大拨测分组数
        :type MaxGroupNum: int
        """
        self.GroupId = None
        self.GroupName = None
        self.IsDefault = None
        self.TaskNum = None
        self.GroupDetail = None
        self.MaxGroupNum = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.IsDefault = params.get("IsDefault")
        self.TaskNum = params.get("TaskNum")
        if params.get("GroupDetail") is not None:
            self.GroupDetail = []
            for item in params.get("GroupDetail"):
                obj = CatAgent()
                obj._deserialize(item)
                self.GroupDetail.append(obj)
        self.MaxGroupNum = params.get("MaxGroupNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmInfo(AbstractModel):
    """拨测告警信息

    """

    def __init__(self):
        r"""
        :param ObjName: 告警对象的名称
        :type ObjName: str
        :param FirstOccurTime: 告警发生的时间
        :type FirstOccurTime: str
        :param LastOccurTime: 告警结束的时间
        :type LastOccurTime: str
        :param Status: 告警状态。1 表示已恢复，0 表示未恢复，2表示数据不足
        :type Status: int
        :param Content: 告警的内容
        :type Content: str
        :param TaskId: 拨测任务ID
        :type TaskId: int
        :param MetricName: 特征项名字
        :type MetricName: str
        :param MetricValue: 特征项数值
        :type MetricValue: str
        :param ObjId: 告警对象的ID
        :type ObjId: str
        """
        self.ObjName = None
        self.FirstOccurTime = None
        self.LastOccurTime = None
        self.Status = None
        self.Content = None
        self.TaskId = None
        self.MetricName = None
        self.MetricValue = None
        self.ObjId = None


    def _deserialize(self, params):
        self.ObjName = params.get("ObjName")
        self.FirstOccurTime = params.get("FirstOccurTime")
        self.LastOccurTime = params.get("LastOccurTime")
        self.Status = params.get("Status")
        self.Content = params.get("Content")
        self.TaskId = params.get("TaskId")
        self.MetricName = params.get("MetricName")
        self.MetricValue = params.get("MetricValue")
        self.ObjId = params.get("ObjId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTopic(AbstractModel):
    """告警主题

    """

    def __init__(self):
        r"""
        :param TopicId: 主题的ID
        :type TopicId: str
        :param TopicName: 主题的名称
        :type TopicName: str
        """
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAlarmPolicyRequest(AbstractModel):
    """BindAlarmPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 拨测任务Id
        :type TaskId: int
        :param PolicyGroupId: 告警策略组Id
        :type PolicyGroupId: int
        :param IfBind: 是否绑定操作。非0 为绑定， 0 为 解绑。缺省表示 绑定。
        :type IfBind: int
        :param TopicId: 告警主题Id
        :type TopicId: str
        """
        self.TaskId = None
        self.PolicyGroupId = None
        self.IfBind = None
        self.TopicId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.PolicyGroupId = params.get("PolicyGroupId")
        self.IfBind = params.get("IfBind")
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAlarmPolicyResponse(AbstractModel):
    """BindAlarmPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CatAgent(AbstractModel):
    """拨测Agent 所在省份、运营商

    """

    def __init__(self):
        r"""
        :param Province: 拨测结点所在的省份（拼音缩写）
        :type Province: str
        :param Isp: 拨测结点所在的运营商（英文缩写）
        :type Isp: str
        :param ProvinceName: 拨测结点所在的省份（中文名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProvinceName: str
        :param IspName: 拨测结点所在的运营商（中文名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type IspName: str
        """
        self.Province = None
        self.Isp = None
        self.ProvinceName = None
        self.IspName = None


    def _deserialize(self, params):
        self.Province = params.get("Province")
        self.Isp = params.get("Isp")
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CatLog(AbstractModel):
    """拨测记录

    """

    def __init__(self):
        r"""
        :param Time: 拨测时间点
        :type Time: str
        :param CatTypeName: 拨测类型
        :type CatTypeName: str
        :param TaskId: 任务ID
        :type TaskId: int
        :param City: 拨测点所在城市
        :type City: str
        :param Isp: 拨测点所在运营商
        :type Isp: str
        :param ServerIp: 被拨测Server的IP
        :type ServerIp: str
        :param DomainName: 被拨测Server的域名
        :type DomainName: str
        :param TotalTime: 执行耗时，单位毫秒
        :type TotalTime: int
        :param ResultType: 成功失败(1 失败，0 成功）
        :type ResultType: int
        :param ResultCode: 失败错误码
        :type ResultCode: int
        :param ReqPkgSize: 请求包大小
        :type ReqPkgSize: int
        :param RspPkgSize: 回应包大小
        :type RspPkgSize: int
        :param ReqMsg: 拨测请求
        :type ReqMsg: str
        :param RespMsg: 拨测回应
        :type RespMsg: str
        :param ClientIp: 客户端IP
        :type ClientIp: str
        :param CityName: 拨测点所在城市名称
        :type CityName: str
        :param IspName: 拨测点所在运营商名称
        :type IspName: str
        :param ParseTime: 解析耗时，单位毫秒
        :type ParseTime: int
        :param ConnectTime: 连接耗时，单位毫秒
        :type ConnectTime: int
        :param SendTime: 数据发送耗时，单位毫秒
        :type SendTime: int
        :param WaitTime: 等待耗时，单位毫秒
        :type WaitTime: int
        :param ReceiveTime: 接收耗时，单位毫秒
        :type ReceiveTime: int
        """
        self.Time = None
        self.CatTypeName = None
        self.TaskId = None
        self.City = None
        self.Isp = None
        self.ServerIp = None
        self.DomainName = None
        self.TotalTime = None
        self.ResultType = None
        self.ResultCode = None
        self.ReqPkgSize = None
        self.RspPkgSize = None
        self.ReqMsg = None
        self.RespMsg = None
        self.ClientIp = None
        self.CityName = None
        self.IspName = None
        self.ParseTime = None
        self.ConnectTime = None
        self.SendTime = None
        self.WaitTime = None
        self.ReceiveTime = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.CatTypeName = params.get("CatTypeName")
        self.TaskId = params.get("TaskId")
        self.City = params.get("City")
        self.Isp = params.get("Isp")
        self.ServerIp = params.get("ServerIp")
        self.DomainName = params.get("DomainName")
        self.TotalTime = params.get("TotalTime")
        self.ResultType = params.get("ResultType")
        self.ResultCode = params.get("ResultCode")
        self.ReqPkgSize = params.get("ReqPkgSize")
        self.RspPkgSize = params.get("RspPkgSize")
        self.ReqMsg = params.get("ReqMsg")
        self.RespMsg = params.get("RespMsg")
        self.ClientIp = params.get("ClientIp")
        self.CityName = params.get("CityName")
        self.IspName = params.get("IspName")
        self.ParseTime = params.get("ParseTime")
        self.ConnectTime = params.get("ConnectTime")
        self.SendTime = params.get("SendTime")
        self.WaitTime = params.get("WaitTime")
        self.ReceiveTime = params.get("ReceiveTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CatReturnDetail(AbstractModel):
    """拨测失败详情

    """

    def __init__(self):
        r"""
        :param IspName: 运营商名称
        :type IspName: str
        :param Province: 省份全拼
        :type Province: str
        :param ProvinceName: 省份中文名称
        :type ProvinceName: str
        :param MapKey: Map键值
        :type MapKey: str
        :param ServerIp: 拨测目标的IP
        :type ServerIp: str
        :param ResultCount: 拨测失败个数
        :type ResultCount: int
        :param ResultCode: 拨测失败返回码
        :type ResultCode: int
        :param ErrorReason: 拨测失败原因描述
        :type ErrorReason: str
        """
        self.IspName = None
        self.Province = None
        self.ProvinceName = None
        self.MapKey = None
        self.ServerIp = None
        self.ResultCount = None
        self.ResultCode = None
        self.ErrorReason = None


    def _deserialize(self, params):
        self.IspName = params.get("IspName")
        self.Province = params.get("Province")
        self.ProvinceName = params.get("ProvinceName")
        self.MapKey = params.get("MapKey")
        self.ServerIp = params.get("ServerIp")
        self.ResultCount = params.get("ResultCount")
        self.ResultCode = params.get("ResultCode")
        self.ErrorReason = params.get("ErrorReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CatReturnSummary(AbstractModel):
    """拨测失败返回情况汇总

    """

    def __init__(self):
        r"""
        :param ResultCount: 拨测失败个数
        :type ResultCount: int
        :param ResultCode: 拨测失败返回码
        :type ResultCode: int
        :param ErrorReason: 拨测失败原因描述
        :type ErrorReason: str
        """
        self.ResultCount = None
        self.ResultCode = None
        self.ErrorReason = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.ResultCode = params.get("ResultCode")
        self.ErrorReason = params.get("ErrorReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CatTaskDetail(AbstractModel):
    """任务信息和告警策略组

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param TaskName: 任务名称
        :type TaskName: str
        :param Period: 任务周期，单位为分钟。目前支持1，5，15，30几种取值
        :type Period: int
        :param CatTypeName: 拨测类型。http, https, ping, tcp 之一
        :type CatTypeName: str
        :param CgiUrl: 拨测任务的URL
        :type CgiUrl: str
        :param AgentGroupId: 拨测分组ID
        :type AgentGroupId: int
        :param PolicyGroupId: 告警策略组ID
        :type PolicyGroupId: int
        :param Status: 任务状态。1表示暂停，2表示运行中，0为初始态
        :type Status: int
        :param AddTime: 任务创建时间
        :type AddTime: str
        :param Type: 任务类型。0 站点监控，2 可用性监控
        :type Type: int
        :param TopicId: 绑定的统一告警主题ID
        :type TopicId: str
        :param AlarmStatus: 告警状态。0 未启用，1, 启用
        :type AlarmStatus: int
        :param Host: 指定的域名
        :type Host: str
        :param Port: 拨测目标的端口号
        :type Port: int
        :param CheckStr: 要在结果中进行匹配的字符串
        :type CheckStr: str
        :param CheckType: 1 表示通过检查结果是否包含CheckStr 进行校验
        :type CheckType: int
        :param UserAgent: 用户Agent信息
        :type UserAgent: str
        :param Cookie: 设置的Cookie信息
        :type Cookie: str
        :param PostData: POST 请求数据。空字符串表示非POST请求
        :type PostData: str
        :param SslVer: SSL协议版本
        :type SslVer: str
        :param IsHeader: 是否为Header请求。非0 Header 请求
        :type IsHeader: int
        :param DnsSvr: 目的DNS服务器
        :type DnsSvr: str
        :param DnsCheckIp: 需要检验是否在DNS IP列表的IP
        :type DnsCheckIp: str
        :param DnsQueryType: DNS查询类型
        :type DnsQueryType: str
        :param UserName: 登录服务器的账号
        :type UserName: str
        :param PassWord: 登录服务器的密码
        :type PassWord: str
        :param UseSecConn: 是否使用安全链接SSL， 0 不使用，1 使用
        :type UseSecConn: int
        :param NeedAuth: FTP登录验证方式  0 不验证  1 匿名登录  2 需要身份验证
        :type NeedAuth: int
        :param ReqDataType: 请求数据类型。0 表示请求为字符串类型。1表示为二进制类型
        :type ReqDataType: int
        :param ReqData: 发起TCP, UDP请求的协议请求数据
        :type ReqData: str
        :param RespDataType: 响应数据类型。0 表示响应为字符串类型。1表示为二进制类型
        :type RespDataType: int
        :param RespData: 预期的UDP请求的回应数据
        :type RespData: str
        :param RedirectFollowNum: 跟随跳转次数
        :type RedirectFollowNum: int
        """
        self.TaskId = None
        self.TaskName = None
        self.Period = None
        self.CatTypeName = None
        self.CgiUrl = None
        self.AgentGroupId = None
        self.PolicyGroupId = None
        self.Status = None
        self.AddTime = None
        self.Type = None
        self.TopicId = None
        self.AlarmStatus = None
        self.Host = None
        self.Port = None
        self.CheckStr = None
        self.CheckType = None
        self.UserAgent = None
        self.Cookie = None
        self.PostData = None
        self.SslVer = None
        self.IsHeader = None
        self.DnsSvr = None
        self.DnsCheckIp = None
        self.DnsQueryType = None
        self.UserName = None
        self.PassWord = None
        self.UseSecConn = None
        self.NeedAuth = None
        self.ReqDataType = None
        self.ReqData = None
        self.RespDataType = None
        self.RespData = None
        self.RedirectFollowNum = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.Period = params.get("Period")
        self.CatTypeName = params.get("CatTypeName")
        self.CgiUrl = params.get("CgiUrl")
        self.AgentGroupId = params.get("AgentGroupId")
        self.PolicyGroupId = params.get("PolicyGroupId")
        self.Status = params.get("Status")
        self.AddTime = params.get("AddTime")
        self.Type = params.get("Type")
        self.TopicId = params.get("TopicId")
        self.AlarmStatus = params.get("AlarmStatus")
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.CheckStr = params.get("CheckStr")
        self.CheckType = params.get("CheckType")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")
        self.PostData = params.get("PostData")
        self.SslVer = params.get("SslVer")
        self.IsHeader = params.get("IsHeader")
        self.DnsSvr = params.get("DnsSvr")
        self.DnsCheckIp = params.get("DnsCheckIp")
        self.DnsQueryType = params.get("DnsQueryType")
        self.UserName = params.get("UserName")
        self.PassWord = params.get("PassWord")
        self.UseSecConn = params.get("UseSecConn")
        self.NeedAuth = params.get("NeedAuth")
        self.ReqDataType = params.get("ReqDataType")
        self.ReqData = params.get("ReqData")
        self.RespDataType = params.get("RespDataType")
        self.RespData = params.get("RespData")
        self.RedirectFollowNum = params.get("RedirectFollowNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentGroupRequest(AbstractModel):
    """CreateAgentGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupName: 拨测分组名称，不超过32个字符
        :type GroupName: str
        :param IsDefault: 是否为默认分组，取值可为 0 或 1。取 1 时表示设置为默认分组
        :type IsDefault: int
        :param Agents: Province, Isp 需要成对地进行选择。参数对的取值范围。参见：DescribeAgents 的返回结果。
        :type Agents: list of CatAgent
        """
        self.GroupName = None
        self.IsDefault = None
        self.Agents = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.IsDefault = params.get("IsDefault")
        if params.get("Agents") is not None:
            self.Agents = []
            for item in params.get("Agents"):
                obj = CatAgent()
                obj._deserialize(item)
                self.Agents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentGroupResponse(AbstractModel):
    """CreateAgentGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 拨测分组Id
        :type GroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateProbeTasksRequest(AbstractModel):
    """CreateProbeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTasks: 批量任务名-地址
        :type BatchTasks: list of ProbeTaskBasicConfiguration
        :param TaskType: 任务类型
        :type TaskType: int
        :param Nodes: 拨测节点
        :type Nodes: list of str
        :param Interval: 拨测间隔
        :type Interval: int
        :param Parameters: 拨测参数
        :type Parameters: str
        :param TaskCategory: 任务分类
<li>1 = PC</li>
<li> 2 = Mobile </li>
        :type TaskCategory: int
        :param Cron: 定时任务cron表达式
        :type Cron: str
        :param Tag: 资源标签值
        :type Tag: list of Tag
        :param ProbeType: 测试类型，包含定时测试与即时测试
        :type ProbeType: int
        :param PluginSource: 插件类型
        :type PluginSource: str
        :param ClientNum: 客户度ID
        :type ClientNum: str
        """
        self.BatchTasks = None
        self.TaskType = None
        self.Nodes = None
        self.Interval = None
        self.Parameters = None
        self.TaskCategory = None
        self.Cron = None
        self.Tag = None
        self.ProbeType = None
        self.PluginSource = None
        self.ClientNum = None


    def _deserialize(self, params):
        if params.get("BatchTasks") is not None:
            self.BatchTasks = []
            for item in params.get("BatchTasks"):
                obj = ProbeTaskBasicConfiguration()
                obj._deserialize(item)
                self.BatchTasks.append(obj)
        self.TaskType = params.get("TaskType")
        self.Nodes = params.get("Nodes")
        self.Interval = params.get("Interval")
        self.Parameters = params.get("Parameters")
        self.TaskCategory = params.get("TaskCategory")
        self.Cron = params.get("Cron")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.ProbeType = params.get("ProbeType")
        self.PluginSource = params.get("PluginSource")
        self.ClientNum = params.get("ClientNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProbeTasksResponse(AbstractModel):
    """CreateProbeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIDs: 任务ID列表
        :type TaskIDs: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskIDs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskIDs = params.get("TaskIDs")
        self.RequestId = params.get("RequestId")


class CreateTaskExRequest(AbstractModel):
    """CreateTaskEx请求参数结构体

    """

    def __init__(self):
        r"""
        :param CatTypeName: http, https, ping, tcp, ftp, smtp, udp, dns 之一
        :type CatTypeName: str
        :param Url: 拨测的URL， 例如：www.qq.com (URL域名解析需要能解析出具体的IP)
        :type Url: str
        :param Period: 拨测周期。取值可为1,5,15,30之一, 单位：分钟。精度不能低于用户等级规定的最小精度
        :type Period: int
        :param TaskName: 拨测任务名称不能超过32个字符。同一个用户创建的任务名不可重复
        :type TaskName: str
        :param AgentGroupId: 拨测分组ID，体现本拨测任务要采用哪些运营商作为拨测源。一般可直接填写本用户的默认拨测分组。参见：DescribeAgentGroups 接口，本参数使用返回结果里的GroupId的值。注意： Type为0时，AgentGroupId为必填
        :type AgentGroupId: int
        :param Host: 指定域名(如需要)
        :type Host: str
        :param IsHeader: 是否为Header请求（非0 发起Header 请求。为0，且PostData 非空，发起POST请求。为0，PostData 为空，发起GET请求）
        :type IsHeader: int
        :param SslVer: URL中含有"https"时有用。缺省为SSLv23。需要为 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一
        :type SslVer: str
        :param PostData: POST请求数据。空字符串表示非POST请求
        :type PostData: str
        :param UserAgent: 用户Agent信息
        :type UserAgent: str
        :param CheckStr: 要在结果中进行匹配的字符串
        :type CheckStr: str
        :param CheckType: 1 表示通过检查结果是否包含CheckStr 进行校验
        :type CheckType: int
        :param Cookie: 需要设置的Cookie信息
        :type Cookie: str
        :param TaskId: 任务ID，用于验证且修改任务时传入原任务ID
        :type TaskId: int
        :param UserName: 登录服务器的账号。如果为空字符串，表示不用校验用户密码。只做简单连接服务器的拨测
        :type UserName: str
        :param PassWord: 登录服务器的密码
        :type PassWord: str
        :param ReqDataType: 缺省为0。0 表示请求为字符串类型。1表示为二进制类型
        :type ReqDataType: int
        :param ReqData: 发起TCP, UDP请求的协议请求数据
        :type ReqData: str
        :param RespDataType: 缺省为0。0 表示响应为字符串类型。1表示为二进制类型
        :type RespDataType: int
        :param RespData: 预期的UDP请求的回应数据。字符串型，只需要返回的结果里包含本字符串算校验通过。二进制型，则需要严格等于才算通过
        :type RespData: str
        :param DnsSvr: 目的DNS服务器  可以为空字符串
        :type DnsSvr: str
        :param DnsCheckIp: 需要检验是否在DNS IP列表的IP。可以为空字符串，表示不校验
        :type DnsCheckIp: str
        :param DnsQueryType: 需要为下列值之一。缺省为A。A, MX, NS, CNAME, TXT, ANY
        :type DnsQueryType: str
        :param UseSecConn: 是否使用安全链接SSL， 0 不使用，1 使用
        :type UseSecConn: int
        :param NeedAuth: FTP登录验证方式， 0 不验证 ， 1 匿名登录， 2 需要身份验证
        :type NeedAuth: int
        :param Port: 拨测目标的端口号
        :type Port: int
        :param Type: Type=0 默认 （站点监控）Type=2 可用率监控
        :type Type: int
        :param IsVerify: IsVerify=0 非验证任务 IsVerify=1 验证任务，不传则默认为0
        :type IsVerify: int
        :param RedirectFollowNum: 跟随跳转次数，取值范围0-5，不传则表示不跟随
        :type RedirectFollowNum: int
        """
        self.CatTypeName = None
        self.Url = None
        self.Period = None
        self.TaskName = None
        self.AgentGroupId = None
        self.Host = None
        self.IsHeader = None
        self.SslVer = None
        self.PostData = None
        self.UserAgent = None
        self.CheckStr = None
        self.CheckType = None
        self.Cookie = None
        self.TaskId = None
        self.UserName = None
        self.PassWord = None
        self.ReqDataType = None
        self.ReqData = None
        self.RespDataType = None
        self.RespData = None
        self.DnsSvr = None
        self.DnsCheckIp = None
        self.DnsQueryType = None
        self.UseSecConn = None
        self.NeedAuth = None
        self.Port = None
        self.Type = None
        self.IsVerify = None
        self.RedirectFollowNum = None


    def _deserialize(self, params):
        self.CatTypeName = params.get("CatTypeName")
        self.Url = params.get("Url")
        self.Period = params.get("Period")
        self.TaskName = params.get("TaskName")
        self.AgentGroupId = params.get("AgentGroupId")
        self.Host = params.get("Host")
        self.IsHeader = params.get("IsHeader")
        self.SslVer = params.get("SslVer")
        self.PostData = params.get("PostData")
        self.UserAgent = params.get("UserAgent")
        self.CheckStr = params.get("CheckStr")
        self.CheckType = params.get("CheckType")
        self.Cookie = params.get("Cookie")
        self.TaskId = params.get("TaskId")
        self.UserName = params.get("UserName")
        self.PassWord = params.get("PassWord")
        self.ReqDataType = params.get("ReqDataType")
        self.ReqData = params.get("ReqData")
        self.RespDataType = params.get("RespDataType")
        self.RespData = params.get("RespData")
        self.DnsSvr = params.get("DnsSvr")
        self.DnsCheckIp = params.get("DnsCheckIp")
        self.DnsQueryType = params.get("DnsQueryType")
        self.UseSecConn = params.get("UseSecConn")
        self.NeedAuth = params.get("NeedAuth")
        self.Port = params.get("Port")
        self.Type = params.get("Type")
        self.IsVerify = params.get("IsVerify")
        self.RedirectFollowNum = params.get("RedirectFollowNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskExResponse(AbstractModel):
    """CreateTaskEx返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultId: 拨测结果查询ID。接下来可以使用查询拨测是否能够成功，验证能否通过。
        :type ResultId: int
        :param TaskId: 拨测任务ID。验证通过后，创建任务时使用，传递给CreateTask 接口。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultId = params.get("ResultId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DataPoint(AbstractModel):
    """时延等数据，数据点

    """

    def __init__(self):
        r"""
        :param LogTime: 数据点的时间
        :type LogTime: str
        :param MetricValue: 数据值
        :type MetricValue: float
        """
        self.LogTime = None
        self.MetricValue = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.MetricValue = params.get("MetricValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataPointMetric(AbstractModel):
    """包含MetricName的DataPoint数据

    """

    def __init__(self):
        r"""
        :param MetricName: 数据项
        :type MetricName: str
        :param Points: 数据点的时间和值
        :type Points: list of DataPoint
        """
        self.MetricName = None
        self.Points = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = DataPoint()
                obj._deserialize(item)
                self.Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentGroupRequest(AbstractModel):
    """DeleteAgentGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 拨测分组id
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentGroupResponse(AbstractModel):
    """DeleteAgentGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProbeTaskRequest(AbstractModel):
    """DeleteProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProbeTaskResponse(AbstractModel):
    """DeleteProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 任务总量
        :type Total: int
        :param SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param Results: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.SuccessCount = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteTasksRequest(AbstractModel):
    """DeleteTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 拨测任务id
        :type TaskIds: list of int non-negative
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTasksResponse(AbstractModel):
    """DeleteTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAgentGroupsRequest(AbstractModel):
    """DescribeAgentGroups请求参数结构体

    """


class DescribeAgentGroupsResponse(AbstractModel):
    """DescribeAgentGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param SysDefaultGroup: 用户所属的系统默认拨测分组
        :type SysDefaultGroup: :class:`tencentcloud.cat.v20180409.models.AgentGroup`
        :param CustomGroups: 用户创建的拨测分组列表
        :type CustomGroups: list of AgentGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SysDefaultGroup = None
        self.CustomGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SysDefaultGroup") is not None:
            self.SysDefaultGroup = AgentGroup()
            self.SysDefaultGroup._deserialize(params.get("SysDefaultGroup"))
        if params.get("CustomGroups") is not None:
            self.CustomGroups = []
            for item in params.get("CustomGroups"):
                obj = AgentGroup()
                obj._deserialize(item)
                self.CustomGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentsRequest(AbstractModel):
    """DescribeAgents请求参数结构体

    """


class DescribeAgentsResponse(AbstractModel):
    """DescribeAgents返回参数结构体

    """

    def __init__(self):
        r"""
        :param Agents: 本用户可选的拨测点列表
        :type Agents: list of CatAgent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Agents = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Agents") is not None:
            self.Agents = []
            for item in params.get("Agents"):
                obj = CatAgent()
                obj._deserialize(item)
                self.Agents.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmTopicRequest(AbstractModel):
    """DescribeAlarmTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param NeedAdd: 如果不存在拨测相关的主题，是否自动创建一个。取值可为0, 1，默认为0
        :type NeedAdd: int
        """
        self.NeedAdd = None


    def _deserialize(self, params):
        self.NeedAdd = params.get("NeedAdd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmTopicResponse(AbstractModel):
    """DescribeAlarmTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 主题个数
        :type TotalCount: int
        :param Topics: 主题列表
        :type Topics: list of AlarmTopic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Topics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = AlarmTopic()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmsByTaskRequest(AbstractModel):
    """DescribeAlarmsByTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 拨测任务Id
        :type TaskId: int
        :param Offset: 从第Offset 条开始查询。缺省值为0
        :type Offset: int
        :param Limit: 本批次查询Limit 条记录。缺省值为20
        :type Limit: int
        :param Status: 0 全部, 1 已恢复, 2 未恢复  默认为0。其他值，视为0 查全部状态
        :type Status: int
        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省为7天前0点
        :type BeginTime: str
        :param EndTime: 格式如：2017-05-10 00:00:00  缺省为明天0点
        :type EndTime: str
        :param SortBy: 排序字段，可为Time, ObjName, Duration, Status, Content 之一。缺省为Time
        :type SortBy: str
        :param SortType: 升序或降序。可为Desc, Asc之一。缺省为Desc
        :type SortType: str
        :param ObjName: 告警对象的名称
        :type ObjName: str
        """
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.BeginTime = None
        self.EndTime = None
        self.SortBy = None
        self.SortType = None
        self.ObjName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SortBy = params.get("SortBy")
        self.SortType = params.get("SortType")
        self.ObjName = params.get("ObjName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmsByTaskResponse(AbstractModel):
    """DescribeAlarmsByTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param AlarmInfos: 告警信息列表
        :type AlarmInfos: list of AlarmInfo
        :param FaultRatio: 故障率
        :type FaultRatio: float
        :param FaultTimeSpec: 故障总时长
        :type FaultTimeSpec: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlarmInfos = None
        self.FaultRatio = None
        self.FaultTimeSpec = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlarmInfos") is not None:
            self.AlarmInfos = []
            for item in params.get("AlarmInfos"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self.AlarmInfos.append(obj)
        self.FaultRatio = params.get("FaultRatio")
        self.FaultTimeSpec = params.get("FaultTimeSpec")
        self.RequestId = params.get("RequestId")


class DescribeAlarmsRequest(AbstractModel):
    """DescribeAlarms请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 从第Offset 条开始查询。缺省值为0
        :type Offset: int
        :param Limit: 本批次查询Limit 条记录。缺省值为20
        :type Limit: int
        :param Status: 0 全部, 1 已恢复, 2 未恢复  默认为0。其他值，视为0 查全部状态。
        :type Status: int
        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省为7天前0点
        :type BeginTime: str
        :param EndTime: 格式如：2017-05-10 00:00:00  缺省为明天0点
        :type EndTime: str
        :param ObjName: 告警任务名
        :type ObjName: str
        :param SortBy: 排序字段，可为Time, ObjName, Duration, Status, Content 之一。缺省为Time。
        :type SortBy: str
        :param SortType: 升序或降序。可为Desc, Asc之一。缺省为Desc。
        :type SortType: str
        """
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.BeginTime = None
        self.EndTime = None
        self.ObjName = None
        self.SortBy = None
        self.SortType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.ObjName = params.get("ObjName")
        self.SortBy = params.get("SortBy")
        self.SortType = params.get("SortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmsResponse(AbstractModel):
    """DescribeAlarms返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 告警总条数
        :type TotalCount: int
        :param AlarmInfos: 本批告警信息列表
        :type AlarmInfos: list of AlarmInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AlarmInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AlarmInfos") is not None:
            self.AlarmInfos = []
            for item in params.get("AlarmInfos"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self.AlarmInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCatLogsRequest(AbstractModel):
    """DescribeCatLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 拨测任务Id
        :type TaskId: int
        :param Offset: 从第Offset 条开始查询。缺省值为0
        :type Offset: int
        :param Limit: 本批次查询Limit 条记录。缺省值为20
        :type Limit: int
        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省为当天0点，最多拉取1天的数据
        :type BeginTime: str
        :param EndTime: 格式如：2017-05-10 00:00:00  缺省为当前时间
        :type EndTime: str
        :param SortType: 按时间升序或降序。默认降序。可选值： Desc, Asc
        :type SortType: str
        """
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.BeginTime = None
        self.EndTime = None
        self.SortType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SortType = params.get("SortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCatLogsResponse(AbstractModel):
    """DescribeCatLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的总记录数
        :type TotalCount: int
        :param CatLogs: 拨测记录列表
        :type CatLogs: list of CatLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CatLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CatLogs") is not None:
            self.CatLogs = []
            for item in params.get("CatLogs"):
                obj = CatLog()
                obj._deserialize(item)
                self.CatLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDetailedSingleProbeDataRequest(AbstractModel):
    """DescribeDetailedSingleProbeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginTime: 开始时间戳（毫秒级）
        :type BeginTime: int
        :param EndTime: 结束时间戳（毫秒级）
        :type EndTime: int
        :param TaskType: 任务类型
        :type TaskType: str
        :param SortField: 待排序字段
        :type SortField: str
        :param Ascending: true表示升序
        :type Ascending: bool
        :param SelectedFields: 选中字段
        :type SelectedFields: list of str
        :param Offset: 起始取数位置
        :type Offset: int
        :param Limit: 取数数量
        :type Limit: int
        :param TaskID: 任务ID
        :type TaskID: list of str
        :param Operators: 拨测点运营商
        :type Operators: list of str
        :param Districts: 拨测点地区
        :type Districts: list of str
        :param ErrorTypes: 错误类型
        :type ErrorTypes: list of str
        :param City: 城市
        :type City: list of str
        """
        self.BeginTime = None
        self.EndTime = None
        self.TaskType = None
        self.SortField = None
        self.Ascending = None
        self.SelectedFields = None
        self.Offset = None
        self.Limit = None
        self.TaskID = None
        self.Operators = None
        self.Districts = None
        self.ErrorTypes = None
        self.City = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TaskType = params.get("TaskType")
        self.SortField = params.get("SortField")
        self.Ascending = params.get("Ascending")
        self.SelectedFields = params.get("SelectedFields")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TaskID = params.get("TaskID")
        self.Operators = params.get("Operators")
        self.Districts = params.get("Districts")
        self.ErrorTypes = params.get("ErrorTypes")
        self.City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDetailedSingleProbeDataResponse(AbstractModel):
    """DescribeDetailedSingleProbeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataSet: 单次详情数据
        :type DataSet: list of DetailedSingleDataDefine
        :param TotalNumber: 符合条件的数据总数
        :type TotalNumber: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataSet = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataSet") is not None:
            self.DataSet = []
            for item in params.get("DataSet"):
                obj = DetailedSingleDataDefine()
                obj._deserialize(item)
                self.DataSet.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeProbeMetricDataRequest(AbstractModel):
    """DescribeProbeMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param AnalyzeTaskType: 分析任务类型
        :type AnalyzeTaskType: str
        :param MetricType: 指标类型，counter 或者 gauge
        :type MetricType: str
        :param Field: 指标详细字段
        :type Field: str
        :param Filter: 过滤条件
        :type Filter: str
        :param GroupBy: 聚合时间, 1m、1d、100d 等等
        :type GroupBy: str
        :param Filters: 过滤条件数组
        :type Filters: list of str
        """
        self.AnalyzeTaskType = None
        self.MetricType = None
        self.Field = None
        self.Filter = None
        self.GroupBy = None
        self.Filters = None


    def _deserialize(self, params):
        self.AnalyzeTaskType = params.get("AnalyzeTaskType")
        self.MetricType = params.get("MetricType")
        self.Field = params.get("Field")
        self.Filter = params.get("Filter")
        self.GroupBy = params.get("GroupBy")
        self.Filters = params.get("Filters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeMetricDataResponse(AbstractModel):
    """DescribeProbeMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricSet: 指标 JSON 序列化后的字符串
        :type MetricSet: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MetricSet = params.get("MetricSet")
        self.RequestId = params.get("RequestId")


class DescribeProbeNodesRequest(AbstractModel):
    """DescribeProbeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeType: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type NodeType: int
        :param Location: 节点区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 海外 </li>
        :type Location: int
        :param IsIPv6: 是否IPv6
        :type IsIPv6: bool
        :param NodeName: 名字模糊搜索
        :type NodeName: str
        :param PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        """
        self.NodeType = None
        self.Location = None
        self.IsIPv6 = None
        self.NodeName = None
        self.PayMode = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.Location = params.get("Location")
        self.IsIPv6 = params.get("IsIPv6")
        self.NodeName = params.get("NodeName")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeNodesResponse(AbstractModel):
    """DescribeProbeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param NodeSet: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of NodeDefine
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeDefine()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProbeTasksRequest(AbstractModel):
    """DescribeProbeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIDs: 任务 ID  列表
        :type TaskIDs: list of str
        :param TaskName: 任务名
        :type TaskName: str
        :param TargetAddress: 拨测目标
        :type TargetAddress: str
        :param TaskStatus: 任务状态列表
        :type TaskStatus: list of int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        :param OrderState: 订单状态
<li>1 = 正常</li>
<li> 2 = 欠费 </li>
        :type OrderState: int
        :param TaskType: 拨测类型
        :type TaskType: list of int
        :param TaskCategory: 节点类型
        :type TaskCategory: list of int
        :param OrderBy: 排序的列
        :type OrderBy: str
        :param Ascend: 是否正序
        :type Ascend: bool
        :param TagFilters: 资源标签值
        :type TagFilters: list of KeyValuePair
        """
        self.TaskIDs = None
        self.TaskName = None
        self.TargetAddress = None
        self.TaskStatus = None
        self.Offset = None
        self.Limit = None
        self.PayMode = None
        self.OrderState = None
        self.TaskType = None
        self.TaskCategory = None
        self.OrderBy = None
        self.Ascend = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.TaskIDs = params.get("TaskIDs")
        self.TaskName = params.get("TaskName")
        self.TargetAddress = params.get("TargetAddress")
        self.TaskStatus = params.get("TaskStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PayMode = params.get("PayMode")
        self.OrderState = params.get("OrderState")
        self.TaskType = params.get("TaskType")
        self.TaskCategory = params.get("TaskCategory")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = KeyValuePair()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeTasksResponse(AbstractModel):
    """DescribeProbeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskSet: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSet: list of ProbeTask
        :param Total: 任务总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = ProbeTask()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 拨测任务id 数组
        :type TaskIds: list of int non-negative
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tasks: 拨测任务列表
        :type Tasks: list of CatTaskDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = CatTaskDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksByTypeRequest(AbstractModel):
    """DescribeTasksByType请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 从第Offset 条开始查询。缺省值为0
        :type Offset: int
        :param Limit: 本批次查询Limit 条记录。缺省值为20
        :type Limit: int
        :param Type: 拨测任务类型。0 站点监控，2 可用性监控。缺省值为2
        :type Type: int
        """
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksByTypeResponse(AbstractModel):
    """DescribeTasksByType返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的总任务数
        :type TotalCount: int
        :param Tasks: 任务列表
        :type Tasks: list of TaskAlarm
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
                obj = TaskAlarm()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserLimitRequest(AbstractModel):
    """DescribeUserLimit请求参数结构体

    """


class DescribeUserLimitResponse(AbstractModel):
    """DescribeUserLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param MaxTaskNum: 用户可建立的最大任务数
        :type MaxTaskNum: int
        :param MaxAgentNum: 用户可用的最大拨测结点数
        :type MaxAgentNum: int
        :param MaxGroupNum: 用户可建立的最大拨测分组数
        :type MaxGroupNum: int
        :param MinPeriod: 用户可用的最小拨测间隔
        :type MinPeriod: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaxTaskNum = None
        self.MaxAgentNum = None
        self.MaxGroupNum = None
        self.MinPeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxTaskNum = params.get("MaxTaskNum")
        self.MaxAgentNum = params.get("MaxAgentNum")
        self.MaxGroupNum = params.get("MaxGroupNum")
        self.MinPeriod = params.get("MinPeriod")
        self.RequestId = params.get("RequestId")


class DetailedSingleDataDefine(AbstractModel):
    """单条详细拨测数据

    """

    def __init__(self):
        r"""
        :param ProbeTime: 拨测时间戳
        :type ProbeTime: int
        :param Labels: 储存所有string类型字段
        :type Labels: list of Label
        :param Fields: 储存所有float类型字段
        :type Fields: list of Field
        """
        self.ProbeTime = None
        self.Labels = None
        self.Fields = None


    def _deserialize(self, params):
        self.ProbeTime = params.get("ProbeTime")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Fields") is not None:
            self.Fields = []
            for item in params.get("Fields"):
                obj = Field()
                obj._deserialize(item)
                self.Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DimensionsDetail(AbstractModel):
    """拨测点维度信息

    """

    def __init__(self):
        r"""
        :param Isp: 运营商列表
        :type Isp: list of str
        :param Province: 省份列表
        :type Province: list of str
        """
        self.Isp = None
        self.Province = None


    def _deserialize(self, params):
        self.Isp = params.get("Isp")
        self.Province = params.get("Province")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Field(AbstractModel):
    """储存float类型字段

    """

    def __init__(self):
        r"""
        :param ID: 自定义字段编号
        :type ID: int
        :param Name: 自定义字段名称/说明
        :type Name: str
        :param Value: 字段值
        :type Value: float
        """
        self.ID = None
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAvailRatioHistoryRequest(AbstractModel):
    """GetAvailRatioHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 拨测任务Id
        :type TaskId: int
        :param TimeStamp: 具体时间点
        :type TimeStamp: str
        """
        self.TaskId = None
        self.TimeStamp = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TimeStamp = params.get("TimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAvailRatioHistoryResponse(AbstractModel):
    """GetAvailRatioHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param AvgAvailRatio: 整体平均可用率
        :type AvgAvailRatio: float
        :param LowestAvailRatio: 各省份最低可用率
        :type LowestAvailRatio: float
        :param LowestProvince: 可用率最低的省份
        :type LowestProvince: str
        :param LowestIsp: 可用率最低的运营商
        :type LowestIsp: str
        :param ProvinceData: 分省份的可用率数据
        :type ProvinceData: list of ProvinceDetail
        :param AvgTime: 国内平均耗时，单位毫秒
        :type AvgTime: float
        :param AvgAvailRatio2: 国外平均可用率
        :type AvgAvailRatio2: float
        :param AvgTime2: 国外平均耗时，单位毫秒
        :type AvgTime2: float
        :param LowestAvailRatio2: 国外最低可用率
        :type LowestAvailRatio2: float
        :param LowestProvince2: 国外可用率最低的区域
        :type LowestProvince2: str
        :param LowestIsp2: 国外可用率最低的运营商
        :type LowestIsp2: str
        :param ProvinceData2: 国外分区域的可用率数据
        :type ProvinceData2: list of ProvinceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AvgAvailRatio = None
        self.LowestAvailRatio = None
        self.LowestProvince = None
        self.LowestIsp = None
        self.ProvinceData = None
        self.AvgTime = None
        self.AvgAvailRatio2 = None
        self.AvgTime2 = None
        self.LowestAvailRatio2 = None
        self.LowestProvince2 = None
        self.LowestIsp2 = None
        self.ProvinceData2 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AvgAvailRatio = params.get("AvgAvailRatio")
        self.LowestAvailRatio = params.get("LowestAvailRatio")
        self.LowestProvince = params.get("LowestProvince")
        self.LowestIsp = params.get("LowestIsp")
        if params.get("ProvinceData") is not None:
            self.ProvinceData = []
            for item in params.get("ProvinceData"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData.append(obj)
        self.AvgTime = params.get("AvgTime")
        self.AvgAvailRatio2 = params.get("AvgAvailRatio2")
        self.AvgTime2 = params.get("AvgTime2")
        self.LowestAvailRatio2 = params.get("LowestAvailRatio2")
        self.LowestProvince2 = params.get("LowestProvince2")
        self.LowestIsp2 = params.get("LowestIsp2")
        if params.get("ProvinceData2") is not None:
            self.ProvinceData2 = []
            for item in params.get("ProvinceData2"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData2.append(obj)
        self.RequestId = params.get("RequestId")


class GetDailyAvailRatioRequest(AbstractModel):
    """GetDailyAvailRatio请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 拨测任务Id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDailyAvailRatioResponse(AbstractModel):
    """GetDailyAvailRatio返回参数结构体

    """

    def __init__(self):
        r"""
        :param AvgAvailRatio: 整体平均可用率
        :type AvgAvailRatio: float
        :param LowestAvailRatio: 各省份最低可用率
        :type LowestAvailRatio: float
        :param LowestProvince: 可用率最低的省份
        :type LowestProvince: str
        :param ProvinceData: 分省份的可用率数据
        :type ProvinceData: list of ProvinceDetail
        :param AvgTime: 国内平均耗时，单位毫秒
        :type AvgTime: float
        :param AvgAvailRatio2: 国外平均可用率
        :type AvgAvailRatio2: float
        :param AvgTime2: 国外平均耗时，单位毫秒
        :type AvgTime2: float
        :param LowestAvailRatio2: 国外最低可用率
        :type LowestAvailRatio2: float
        :param LowestProvince2: 国外可用率最低的区域
        :type LowestProvince2: str
        :param ProvinceData2: 国外分区域的可用率数据
        :type ProvinceData2: list of ProvinceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AvgAvailRatio = None
        self.LowestAvailRatio = None
        self.LowestProvince = None
        self.ProvinceData = None
        self.AvgTime = None
        self.AvgAvailRatio2 = None
        self.AvgTime2 = None
        self.LowestAvailRatio2 = None
        self.LowestProvince2 = None
        self.ProvinceData2 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AvgAvailRatio = params.get("AvgAvailRatio")
        self.LowestAvailRatio = params.get("LowestAvailRatio")
        self.LowestProvince = params.get("LowestProvince")
        if params.get("ProvinceData") is not None:
            self.ProvinceData = []
            for item in params.get("ProvinceData"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData.append(obj)
        self.AvgTime = params.get("AvgTime")
        self.AvgAvailRatio2 = params.get("AvgAvailRatio2")
        self.AvgTime2 = params.get("AvgTime2")
        self.LowestAvailRatio2 = params.get("LowestAvailRatio2")
        self.LowestProvince2 = params.get("LowestProvince2")
        if params.get("ProvinceData2") is not None:
            self.ProvinceData2 = []
            for item in params.get("ProvinceData2"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData2.append(obj)
        self.RequestId = params.get("RequestId")


class GetRealAvailRatioRequest(AbstractModel):
    """GetRealAvailRatio请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 拨测任务Id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRealAvailRatioResponse(AbstractModel):
    """GetRealAvailRatio返回参数结构体

    """

    def __init__(self):
        r"""
        :param AvgAvailRatio: 国内平均可用率
        :type AvgAvailRatio: float
        :param LowestAvailRatio: 各省份最低可用率
        :type LowestAvailRatio: float
        :param LowestProvince: 可用率最低的省份
        :type LowestProvince: str
        :param LowestIsp: 可用率最低的运营商
        :type LowestIsp: str
        :param ProvinceData: 分省份的可用率数据
        :type ProvinceData: list of ProvinceDetail
        :param AvgTime: 国内平均耗时，单位毫秒
        :type AvgTime: float
        :param AvgAvailRatio2: 国外平均可用率
        :type AvgAvailRatio2: float
        :param AvgTime2: 国外平均耗时，单位毫秒
        :type AvgTime2: float
        :param LowestAvailRatio2: 国外最低可用率
        :type LowestAvailRatio2: float
        :param LowestProvince2: 国外可用率最低的区域
        :type LowestProvince2: str
        :param LowestIsp2: 国外可用率最低的运营商
        :type LowestIsp2: str
        :param ProvinceData2: 国外分区域的可用率数据
        :type ProvinceData2: list of ProvinceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AvgAvailRatio = None
        self.LowestAvailRatio = None
        self.LowestProvince = None
        self.LowestIsp = None
        self.ProvinceData = None
        self.AvgTime = None
        self.AvgAvailRatio2 = None
        self.AvgTime2 = None
        self.LowestAvailRatio2 = None
        self.LowestProvince2 = None
        self.LowestIsp2 = None
        self.ProvinceData2 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AvgAvailRatio = params.get("AvgAvailRatio")
        self.LowestAvailRatio = params.get("LowestAvailRatio")
        self.LowestProvince = params.get("LowestProvince")
        self.LowestIsp = params.get("LowestIsp")
        if params.get("ProvinceData") is not None:
            self.ProvinceData = []
            for item in params.get("ProvinceData"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData.append(obj)
        self.AvgTime = params.get("AvgTime")
        self.AvgAvailRatio2 = params.get("AvgAvailRatio2")
        self.AvgTime2 = params.get("AvgTime2")
        self.LowestAvailRatio2 = params.get("LowestAvailRatio2")
        self.LowestProvince2 = params.get("LowestProvince2")
        self.LowestIsp2 = params.get("LowestIsp2")
        if params.get("ProvinceData2") is not None:
            self.ProvinceData2 = []
            for item in params.get("ProvinceData2"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData2.append(obj)
        self.RequestId = params.get("RequestId")


class GetRespTimeTrendExRequest(AbstractModel):
    """GetRespTimeTrendEx请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 验证成功的拨测任务id
        :type TaskId: int
        :param Date: 统计数据的发生日期。格式如：2017-05-09
        :type Date: str
        :param Period: 数据的采集周期，单位分钟。取值可为 1, 5, 15, 30
        :type Period: int
        :param Dimensions: 可为 Isp, Province
        :type Dimensions: :class:`tencentcloud.cat.v20180409.models.DimensionsDetail`
        :param MetricName: 可为  totalTime, parseTime, connectTime, sendTime, waitTime, receiveTime, availRatio。缺省值为 totalTime
        :type MetricName: str
        """
        self.TaskId = None
        self.Date = None
        self.Period = None
        self.Dimensions = None
        self.MetricName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Date = params.get("Date")
        self.Period = params.get("Period")
        if params.get("Dimensions") is not None:
            self.Dimensions = DimensionsDetail()
            self.Dimensions._deserialize(params.get("Dimensions"))
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRespTimeTrendExResponse(AbstractModel):
    """GetRespTimeTrendEx返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataPoints: 数据点集合，时延等走势数据
        :type DataPoints: list of DataPointMetric
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataPoints = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataPoints") is not None:
            self.DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPointMetric()
                obj._deserialize(item)
                self.DataPoints.append(obj)
        self.RequestId = params.get("RequestId")


class GetResultSummaryRequest(AbstractModel):
    """GetResultSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务Id列表
        :type TaskIds: list of int non-negative
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResultSummaryResponse(AbstractModel):
    """GetResultSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RealData: 实时统计数据
        :type RealData: list of ResultSummary
        :param DayData: 按天的统计数据
        :type DayData: list of ResultSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RealData = None
        self.DayData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RealData") is not None:
            self.RealData = []
            for item in params.get("RealData"):
                obj = ResultSummary()
                obj._deserialize(item)
                self.RealData.append(obj)
        if params.get("DayData") is not None:
            self.DayData = []
            for item in params.get("DayData"):
                obj = ResultSummary()
                obj._deserialize(item)
                self.DayData.append(obj)
        self.RequestId = params.get("RequestId")


class GetReturnCodeHistoryRequest(AbstractModel):
    """GetReturnCodeHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 正整数。验证成功的拨测任务id
        :type TaskId: int
        :param BeginTime: 开始时间点。格式如：2017-05-09 10:20:00。注意，BeginTime 和 EndTime 需要在同一天
        :type BeginTime: str
        :param EndTime: 结束时间点。格式如：2017-05-09 10:25:00。注意，BeginTime 和 EndTime 需要在同一天
        :type EndTime: str
        :param Province: 省份名称的全拼
        :type Province: str
        """
        self.TaskId = None
        self.BeginTime = None
        self.EndTime = None
        self.Province = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Province = params.get("Province")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReturnCodeHistoryResponse(AbstractModel):
    """GetReturnCodeHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param Details: 拨测失败详情列表
        :type Details: list of CatReturnDetail
        :param Summary: 拨测失败汇总列表
        :type Summary: list of CatReturnSummary
        :param BeginTime: 开始时间
        :type BeginTime: str
        :param EndTime: 截至时间
        :type EndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Details = None
        self.Summary = None
        self.BeginTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = CatReturnDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        if params.get("Summary") is not None:
            self.Summary = []
            for item in params.get("Summary"):
                obj = CatReturnSummary()
                obj._deserialize(item)
                self.Summary.append(obj)
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class GetReturnCodeInfoRequest(AbstractModel):
    """GetReturnCodeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 正整数。验证成功的拨测任务id
        :type TaskId: int
        :param BeginTime: 开始时间点。格式如：2017-05-09 10:20:00，最多拉群两天的数据
        :type BeginTime: str
        :param EndTime: 结束时间点。格式如：2017-05-09 10:25:00，最多拉群两天的数据
        :type EndTime: str
        :param Province: 省份名称的全拼
        :type Province: str
        """
        self.TaskId = None
        self.BeginTime = None
        self.EndTime = None
        self.Province = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Province = params.get("Province")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReturnCodeInfoResponse(AbstractModel):
    """GetReturnCodeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Details: 拨测失败详情列表
        :type Details: list of CatReturnDetail
        :param Summary: 拨测失败汇总列表
        :type Summary: list of CatReturnSummary
        :param BeginTime: 开始时间
        :type BeginTime: str
        :param EndTime: 截至时间
        :type EndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Details = None
        self.Summary = None
        self.BeginTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = CatReturnDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        if params.get("Summary") is not None:
            self.Summary = []
            for item in params.get("Summary"):
                obj = CatReturnSummary()
                obj._deserialize(item)
                self.Summary.append(obj)
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class GetTaskTotalNumberRequest(AbstractModel):
    """GetTaskTotalNumber请求参数结构体

    """


class GetTaskTotalNumberResponse(AbstractModel):
    """GetTaskTotalNumber返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 拨测任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class IspDetail(AbstractModel):
    """运营商可用率

    """

    def __init__(self):
        r"""
        :param IspName: 运营商名称
        :type IspName: str
        :param AvailRatio: 可用率
        :type AvailRatio: float
        :param AvgTime: 平均耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgTime: float
        """
        self.IspName = None
        self.AvailRatio = None
        self.AvgTime = None


    def _deserialize(self, params):
        self.IspName = params.get("IspName")
        self.AvailRatio = params.get("AvailRatio")
        self.AvgTime = params.get("AvgTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValuePair(AbstractModel):
    """健值对

    """

    def __init__(self):
        r"""
        :param Key: 健
        :type Key: str
        :param Value: 值
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
        


class Label(AbstractModel):
    """保存string类型字段

    """

    def __init__(self):
        r"""
        :param ID: 自定义字段编号
        :type ID: int
        :param Name: 自定义字段名称/说明
        :type Name: str
        :param Value: 字段值
        :type Value: str
        """
        self.ID = None
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentGroupRequest(AbstractModel):
    """ModifyAgentGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 拨测分组ID
        :type GroupId: int
        :param GroupName: 拨测分组名称
        :type GroupName: str
        :param IsDefault: 是否为默认分组。取值可为0，1。取 1 时表示设置为默认分组
        :type IsDefault: int
        :param Agents: Province, Isp 需要成对地进行选择。参数对的取值范围。参见：DescribeAgents 的返回结果。
        :type Agents: list of CatAgent
        """
        self.GroupId = None
        self.GroupName = None
        self.IsDefault = None
        self.Agents = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.IsDefault = params.get("IsDefault")
        if params.get("Agents") is not None:
            self.Agents = []
            for item in params.get("Agents"):
                obj = CatAgent()
                obj._deserialize(item)
                self.Agents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentGroupResponse(AbstractModel):
    """ModifyAgentGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTaskExRequest(AbstractModel):
    """ModifyTaskEx请求参数结构体

    """

    def __init__(self):
        r"""
        :param CatTypeName: http, https, ping, tcp, ftp, smtp, udp, dns 之一
        :type CatTypeName: str
        :param Url: 拨测的URL，例如：www.qq.com (URL域名解析需要能解析出具体的IP)
        :type Url: str
        :param Period: 拨测周期。取值可为1,5,15,30之一, 单位：分钟。精度不能低于用户等级规定的最小精度
        :type Period: int
        :param TaskName: 拨测任务名称不能超过32个字符。同一个用户创建的任务名不可重复
        :type TaskName: str
        :param TaskId: 验证成功的拨测任务ID
        :type TaskId: int
        :param AgentGroupId: 拨测分组ID，体现本拨测任务要采用哪些运营商作为拨测源。一般可直接填写本用户的默认拨测分组。参见：DescribeAgentGroupList 接口，本参数使用返回结果里的GroupId的值。注意，Type为0时，AgentGroupId为必填
        :type AgentGroupId: int
        :param Host: 指定域名(如需要)
        :type Host: str
        :param Port: 拨测目标的端口号
        :type Port: int
        :param IsHeader: 是否为Header请求（非0 发起Header 请求。为0，且PostData非空，发起POST请求。为0，PostData为空，发起GET请求）
        :type IsHeader: int
        :param SslVer: URL中含有"https"时有用。缺省为SSLv23。需要为 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一
        :type SslVer: str
        :param PostData: POST 请求数据，空字符串表示非POST请求
        :type PostData: str
        :param UserAgent: 用户Agent信息
        :type UserAgent: str
        :param CheckStr: 要在结果中进行匹配的字符串
        :type CheckStr: str
        :param CheckType: 1 表示通过检查结果是否包含CheckStr 进行校验
        :type CheckType: int
        :param Cookie: 需要设置的Cookie信息
        :type Cookie: str
        :param UserName: 登录服务器的账号。如果为空字符串，表示不用校验用户密码。只做简单连接服务器的拨测
        :type UserName: str
        :param PassWord: 登录服务器的密码
        :type PassWord: str
        :param ReqDataType: 缺省为0，0 表示请求为字符串类型, 1表示为二进制类型
        :type ReqDataType: int
        :param ReqData: 发起TCP, UDP请求的协议请求数据
        :type ReqData: str
        :param RespDataType: 缺省为0。0 表示请求为字符串类型。1表示为二进制类型
        :type RespDataType: str
        :param RespData: 预期的UDP请求的回应数据。字符串型，只需要返回的结果里包含本字符串算校验通过。二进制型，则需要严格等于才算通过
        :type RespData: str
        :param DnsSvr: 目的DNS服务器，可以为空字符串
        :type DnsSvr: str
        :param DnsCheckIp: 需要检验是否在DNS IP列表的IP。可以为空字符串，表示不校验
        :type DnsCheckIp: str
        :param DnsQueryType: 需要为下列值之一。缺省为A。A, MX, NS, CNAME, TXT, ANY
        :type DnsQueryType: str
        :param UseSecConn: 是否使用安全链接SSL， 0 不使用，1 使用
        :type UseSecConn: int
        :param NeedAuth: FTP登录验证方式，  0 不验证  1 匿名登录  2 需要身份验证
        :type NeedAuth: int
        :param Type: Type=0 默认 （站点监控） Type=2 可用率监控
        :type Type: int
        :param RedirectFollowNum: 跟随跳转次数，取值范围0-5，不传则表示不跟随
        :type RedirectFollowNum: int
        """
        self.CatTypeName = None
        self.Url = None
        self.Period = None
        self.TaskName = None
        self.TaskId = None
        self.AgentGroupId = None
        self.Host = None
        self.Port = None
        self.IsHeader = None
        self.SslVer = None
        self.PostData = None
        self.UserAgent = None
        self.CheckStr = None
        self.CheckType = None
        self.Cookie = None
        self.UserName = None
        self.PassWord = None
        self.ReqDataType = None
        self.ReqData = None
        self.RespDataType = None
        self.RespData = None
        self.DnsSvr = None
        self.DnsCheckIp = None
        self.DnsQueryType = None
        self.UseSecConn = None
        self.NeedAuth = None
        self.Type = None
        self.RedirectFollowNum = None


    def _deserialize(self, params):
        self.CatTypeName = params.get("CatTypeName")
        self.Url = params.get("Url")
        self.Period = params.get("Period")
        self.TaskName = params.get("TaskName")
        self.TaskId = params.get("TaskId")
        self.AgentGroupId = params.get("AgentGroupId")
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.IsHeader = params.get("IsHeader")
        self.SslVer = params.get("SslVer")
        self.PostData = params.get("PostData")
        self.UserAgent = params.get("UserAgent")
        self.CheckStr = params.get("CheckStr")
        self.CheckType = params.get("CheckType")
        self.Cookie = params.get("Cookie")
        self.UserName = params.get("UserName")
        self.PassWord = params.get("PassWord")
        self.ReqDataType = params.get("ReqDataType")
        self.ReqData = params.get("ReqData")
        self.RespDataType = params.get("RespDataType")
        self.RespData = params.get("RespData")
        self.DnsSvr = params.get("DnsSvr")
        self.DnsCheckIp = params.get("DnsCheckIp")
        self.DnsQueryType = params.get("DnsQueryType")
        self.UseSecConn = params.get("UseSecConn")
        self.NeedAuth = params.get("NeedAuth")
        self.Type = params.get("Type")
        self.RedirectFollowNum = params.get("RedirectFollowNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskExResponse(AbstractModel):
    """ModifyTaskEx返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 拨测任务ID。验证通过后，创建任务时使用，传递给CreateTask 接口。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class NodeDefine(AbstractModel):
    """探测节点

    """

    def __init__(self):
        r"""
        :param Name: 节点名称
        :type Name: str
        :param Code: 节点代码
        :type Code: str
        :param Type: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type Type: int
        :param NetService: 网络服务商
        :type NetService: str
        :param District: 区域
        :type District: str
        :param City: 城市
        :type City: str
        :param IPType: IP 类型
<li> 1 = IPv4 </li>
<li> 2 = IPv6 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IPType: int
        :param Location: 区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 国外 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: int
        :param CodeType: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: str
        :param NodeDefineStatus: 节点状态：1-运行,2-下线
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeDefineStatus: int
        """
        self.Name = None
        self.Code = None
        self.Type = None
        self.NetService = None
        self.District = None
        self.City = None
        self.IPType = None
        self.Location = None
        self.CodeType = None
        self.NodeDefineStatus = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        self.NetService = params.get("NetService")
        self.District = params.get("District")
        self.City = params.get("City")
        self.IPType = params.get("IPType")
        self.Location = params.get("Location")
        self.CodeType = params.get("CodeType")
        self.NodeDefineStatus = params.get("NodeDefineStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseTaskRequest(AbstractModel):
    """PauseTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 拨测任务id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseTaskResponse(AbstractModel):
    """PauseTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProbeTask(AbstractModel):
    """拨测任务

    """

    def __init__(self):
        r"""
        :param Name: 任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param TaskId: 任务 ID
        :type TaskId: str
        :param TaskType: 任务类型
        :type TaskType: int
        :param Nodes: 拨测节点列表
        :type Nodes: list of str
        :param Interval: 拨测间隔
        :type Interval: int
        :param Parameters: 拨测参数
        :type Parameters: str
        :param Status: 任务状态
        :type Status: int
        :param TargetAddress: 目标地址
        :type TargetAddress: str
        :param PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        :param OrderState: 订单状态
<li>1 = 正常</li>
<li> 2 = 欠费 </li>
        :type OrderState: int
        :param TaskCategory: 任务分类
<li>1 = PC</li>
<li> 2 = Mobile </li>
        :type TaskCategory: int
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param Cron: 定时任务cron表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type Cron: str
        :param CronState: 定时任务启动状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CronState: int
        :param TagInfoList: 任务当前绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfoList: list of KeyValuePair
        """
        self.Name = None
        self.TaskId = None
        self.TaskType = None
        self.Nodes = None
        self.Interval = None
        self.Parameters = None
        self.Status = None
        self.TargetAddress = None
        self.PayMode = None
        self.OrderState = None
        self.TaskCategory = None
        self.CreatedAt = None
        self.Cron = None
        self.CronState = None
        self.TagInfoList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.Nodes = params.get("Nodes")
        self.Interval = params.get("Interval")
        self.Parameters = params.get("Parameters")
        self.Status = params.get("Status")
        self.TargetAddress = params.get("TargetAddress")
        self.PayMode = params.get("PayMode")
        self.OrderState = params.get("OrderState")
        self.TaskCategory = params.get("TaskCategory")
        self.CreatedAt = params.get("CreatedAt")
        self.Cron = params.get("Cron")
        self.CronState = params.get("CronState")
        if params.get("TagInfoList") is not None:
            self.TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = KeyValuePair()
                obj._deserialize(item)
                self.TagInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProbeTaskBasicConfiguration(AbstractModel):
    """type ProbeTaskBasicConfiguration struct {
    	TaskID        TaskID `json:"TaskId" gorm:"column:task_id"`
    	Name          string `json:"Name" binding:"required" gorm:"column:name"`
    	TargetAddress string `json:"TargetAddress" binding:"required" gorm:"column:target_address"`
    }

    """

    def __init__(self):
        r"""
        :param Name: 拨测任务名称
        :type Name: str
        :param TargetAddress: 拨测目标地址
        :type TargetAddress: str
        """
        self.Name = None
        self.TargetAddress = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TargetAddress = params.get("TargetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProvinceDetail(AbstractModel):
    """省份可用率

    """

    def __init__(self):
        r"""
        :param AvgAvailRatio: 可用率
        :type AvgAvailRatio: float
        :param ProvinceName: 省份名称
        :type ProvinceName: str
        :param Mapkey: 省份英文名称
        :type Mapkey: str
        :param TimeStamp: 统计时间点
        :type TimeStamp: str
        :param IspDetail: 分运营商可用率
        :type IspDetail: list of IspDetail
        :param AvgTime: 平均耗时，单位毫秒
        :type AvgTime: float
        :param Province: 省份
        :type Province: str
        """
        self.AvgAvailRatio = None
        self.ProvinceName = None
        self.Mapkey = None
        self.TimeStamp = None
        self.IspDetail = None
        self.AvgTime = None
        self.Province = None


    def _deserialize(self, params):
        self.AvgAvailRatio = params.get("AvgAvailRatio")
        self.ProvinceName = params.get("ProvinceName")
        self.Mapkey = params.get("Mapkey")
        self.TimeStamp = params.get("TimeStamp")
        if params.get("IspDetail") is not None:
            self.IspDetail = []
            for item in params.get("IspDetail"):
                obj = IspDetail()
                obj._deserialize(item)
                self.IspDetail.append(obj)
        self.AvgTime = params.get("AvgTime")
        self.Province = params.get("Province")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultSummary(AbstractModel):
    """实时统计数据

    """

    def __init__(self):
        r"""
        :param LogTime: 统计时间
        :type LogTime: str
        :param TaskId: 任务ID
        :type TaskId: int
        :param AvailRatio: 实时可用率
        :type AvailRatio: float
        :param ReponseTime: 实时响应时间
        :type ReponseTime: float
        """
        self.LogTime = None
        self.TaskId = None
        self.AvailRatio = None
        self.ReponseTime = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.TaskId = params.get("TaskId")
        self.AvailRatio = params.get("AvailRatio")
        self.ReponseTime = params.get("ReponseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProbeTaskRequest(AbstractModel):
    """ResumeProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProbeTaskResponse(AbstractModel):
    """ResumeProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 任务总量
        :type Total: int
        :param SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param Results: 任务执行详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.SuccessCount = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class RunTaskRequest(AbstractModel):
    """RunTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunTaskResponse(AbstractModel):
    """RunTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SuspendProbeTaskRequest(AbstractModel):
    """SuspendProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendProbeTaskResponse(AbstractModel):
    """SuspendProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 任务总量
        :type Total: int
        :param SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param Results: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.SuccessCount = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """资源的标签，通过标签对资源进行划分用于支持细粒度的鉴权、分账等场景

    """

    def __init__(self):
        r"""
        :param TagKey: key
        :type TagKey: str
        :param TagValue: value
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
        


class TaskAlarm(AbstractModel):
    """可用性监控任务状态及告警信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param TaskName: 任务名称
        :type TaskName: str
        :param Period: 任务周期，单位为分钟。目前支持1，5，15，30几种取值
        :type Period: int
        :param CatTypeName: 拨测类型。http, https, ping, tcp, udp, smtp, pop3, dns 之一
        :type CatTypeName: str
        :param Status: 任务状态。1表示暂停，2表示运行中，0为初始态
        :type Status: int
        :param CgiUrl: 拨测任务的URL
        :type CgiUrl: str
        :param AddTime: 任务创建时间
        :type AddTime: str
        :param AlarmStatus: 告警状态。1 故障，0 正常
        :type AlarmStatus: int
        :param StatusInfo: 告警状态描述，统计信息
        :type StatusInfo: str
        :param UpdateTime: 任务更新时间
        :type UpdateTime: str
        """
        self.TaskId = None
        self.TaskName = None
        self.Period = None
        self.CatTypeName = None
        self.Status = None
        self.CgiUrl = None
        self.AddTime = None
        self.AlarmStatus = None
        self.StatusInfo = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.Period = params.get("Period")
        self.CatTypeName = params.get("CatTypeName")
        self.Status = params.get("Status")
        self.CgiUrl = params.get("CgiUrl")
        self.AddTime = params.get("AddTime")
        self.AlarmStatus = params.get("AlarmStatus")
        self.StatusInfo = params.get("StatusInfo")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """任务执行结果

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID
        :type TaskId: str
        :param Success: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: bool
        :param ErrorMessage: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        """
        self.TaskId = None
        self.Success = None
        self.ErrorMessage = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Success = params.get("Success")
        self.ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProbeTaskConfigurationListRequest(AbstractModel):
    """UpdateProbeTaskConfigurationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务 ID
        :type TaskIds: list of str
        :param Nodes: 拨测节点
        :type Nodes: list of str
        :param Interval: 拨测间隔
        :type Interval: int
        :param Parameters: 拨测参数
        :type Parameters: str
        :param Cron: 定时任务cron表达式
        :type Cron: str
        """
        self.TaskIds = None
        self.Nodes = None
        self.Interval = None
        self.Parameters = None
        self.Cron = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.Nodes = params.get("Nodes")
        self.Interval = params.get("Interval")
        self.Parameters = params.get("Parameters")
        self.Cron = params.get("Cron")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProbeTaskConfigurationListResponse(AbstractModel):
    """UpdateProbeTaskConfigurationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VerifyResultRequest(AbstractModel):
    """VerifyResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResultId: 要查询的拨测任务的结果id
        :type ResultId: int
        """
        self.ResultId = None


    def _deserialize(self, params):
        self.ResultId = params.get("ResultId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyResultResponse(AbstractModel):
    """VerifyResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorReason: 错误的原因
        :type ErrorReason: str
        :param ResultCode: 错误号
        :type ResultCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorReason = None
        self.ResultCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorReason = params.get("ErrorReason")
        self.ResultCode = params.get("ResultCode")
        self.RequestId = params.get("RequestId")