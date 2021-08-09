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
        """
        :param GroupId: 拨测分组ID\n        :type GroupId: int\n        :param GroupName: 拨测分组名称\n        :type GroupName: str\n        :param IsDefault: 是否默认拨测分组。1表示是，0表示否\n        :type IsDefault: int\n        :param TaskNum: 使用本拨测分组的任务数\n        :type TaskNum: int\n        :param GroupDetail: 拨测结点列表\n        :type GroupDetail: list of CatAgent\n        :param MaxGroupNum: 最大拨测分组数\n        :type MaxGroupNum: int\n        """
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
        """
        :param ObjName: 告警对象的名称\n        :type ObjName: str\n        :param FirstOccurTime: 告警发生的时间\n        :type FirstOccurTime: str\n        :param LastOccurTime: 告警结束的时间\n        :type LastOccurTime: str\n        :param Status: 告警状态。1 表示已恢复，0 表示未恢复，2表示数据不足\n        :type Status: int\n        :param Content: 告警的内容\n        :type Content: str\n        :param TaskId: 拨测任务ID\n        :type TaskId: int\n        :param MetricName: 特征项名字\n        :type MetricName: str\n        :param MetricValue: 特征项数值\n        :type MetricValue: str\n        :param ObjId: 告警对象的ID\n        :type ObjId: str\n        """
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
        """
        :param TopicId: 主题的ID\n        :type TopicId: str\n        :param TopicName: 主题的名称\n        :type TopicName: str\n        """
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
        """
        :param TaskId: 拨测任务Id\n        :type TaskId: int\n        :param PolicyGroupId: 告警策略组Id\n        :type PolicyGroupId: int\n        :param IfBind: 是否绑定操作。非0 为绑定， 0 为 解绑。缺省表示 绑定。\n        :type IfBind: int\n        :param TopicId: 告警主题Id\n        :type TopicId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CatAgent(AbstractModel):
    """拨测Agent 所在省份、运营商

    """

    def __init__(self):
        """
        :param Province: 拨测结点所在的省份（拼音缩写）\n        :type Province: str\n        :param Isp: 拨测结点所在的运营商（英文缩写）\n        :type Isp: str\n        :param ProvinceName: 拨测结点所在的省份（中文名称）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProvinceName: str\n        :param IspName: 拨测结点所在的运营商（中文名称）
注意：此字段可能返回 null，表示取不到有效值。\n        :type IspName: str\n        """
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
        """
        :param Time: 拨测时间点\n        :type Time: str\n        :param CatTypeName: 拨测类型\n        :type CatTypeName: str\n        :param TaskId: 任务ID\n        :type TaskId: int\n        :param City: 拨测点所在城市\n        :type City: str\n        :param Isp: 拨测点所在运营商\n        :type Isp: str\n        :param ServerIp: 被拨测Server的IP\n        :type ServerIp: str\n        :param DomainName: 被拨测Server的域名\n        :type DomainName: str\n        :param TotalTime: 执行耗时，单位毫秒\n        :type TotalTime: int\n        :param ResultType: 成功失败(1 失败，0 成功）\n        :type ResultType: int\n        :param ResultCode: 失败错误码\n        :type ResultCode: int\n        :param ReqPkgSize: 请求包大小\n        :type ReqPkgSize: int\n        :param RspPkgSize: 回应包大小\n        :type RspPkgSize: int\n        :param ReqMsg: 拨测请求\n        :type ReqMsg: str\n        :param RespMsg: 拨测回应\n        :type RespMsg: str\n        :param ClientIp: 客户端IP\n        :type ClientIp: str\n        :param CityName: 拨测点所在城市名称\n        :type CityName: str\n        :param IspName: 拨测点所在运营商名称\n        :type IspName: str\n        :param ParseTime: 解析耗时，单位毫秒\n        :type ParseTime: int\n        :param ConnectTime: 连接耗时，单位毫秒\n        :type ConnectTime: int\n        :param SendTime: 数据发送耗时，单位毫秒\n        :type SendTime: int\n        :param WaitTime: 等待耗时，单位毫秒\n        :type WaitTime: int\n        :param ReceiveTime: 接收耗时，单位毫秒\n        :type ReceiveTime: int\n        """
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
        """
        :param IspName: 运营商名称\n        :type IspName: str\n        :param Province: 省份全拼\n        :type Province: str\n        :param ProvinceName: 省份中文名称\n        :type ProvinceName: str\n        :param MapKey: Map键值\n        :type MapKey: str\n        :param ServerIp: 拨测目标的IP\n        :type ServerIp: str\n        :param ResultCount: 拨测失败个数\n        :type ResultCount: int\n        :param ResultCode: 拨测失败返回码\n        :type ResultCode: int\n        :param ErrorReason: 拨测失败原因描述\n        :type ErrorReason: str\n        """
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
        """
        :param ResultCount: 拨测失败个数\n        :type ResultCount: int\n        :param ResultCode: 拨测失败返回码\n        :type ResultCode: int\n        :param ErrorReason: 拨测失败原因描述\n        :type ErrorReason: str\n        """
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
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param TaskName: 任务名称\n        :type TaskName: str\n        :param Period: 任务周期，单位为分钟。目前支持1，5，15，30几种取值\n        :type Period: int\n        :param CatTypeName: 拨测类型。http, https, ping, tcp 之一\n        :type CatTypeName: str\n        :param CgiUrl: 拨测任务的URL\n        :type CgiUrl: str\n        :param AgentGroupId: 拨测分组ID\n        :type AgentGroupId: int\n        :param PolicyGroupId: 告警策略组ID\n        :type PolicyGroupId: int\n        :param Status: 任务状态。1表示暂停，2表示运行中，0为初始态\n        :type Status: int\n        :param AddTime: 任务创建时间\n        :type AddTime: str\n        :param Type: 任务类型。0 站点监控，2 可用性监控\n        :type Type: int\n        :param TopicId: 绑定的统一告警主题ID\n        :type TopicId: str\n        :param AlarmStatus: 告警状态。0 未启用，1, 启用\n        :type AlarmStatus: int\n        :param Host: 指定的域名\n        :type Host: str\n        :param Port: 拨测目标的端口号\n        :type Port: int\n        :param CheckStr: 要在结果中进行匹配的字符串\n        :type CheckStr: str\n        :param CheckType: 1 表示通过检查结果是否包含CheckStr 进行校验\n        :type CheckType: int\n        :param UserAgent: 用户Agent信息\n        :type UserAgent: str\n        :param Cookie: 设置的Cookie信息\n        :type Cookie: str\n        :param PostData: POST 请求数据。空字符串表示非POST请求\n        :type PostData: str\n        :param SslVer: SSL协议版本\n        :type SslVer: str\n        :param IsHeader: 是否为Header请求。非0 Header 请求\n        :type IsHeader: int\n        :param DnsSvr: 目的DNS服务器\n        :type DnsSvr: str\n        :param DnsCheckIp: 需要检验是否在DNS IP列表的IP\n        :type DnsCheckIp: str\n        :param DnsQueryType: DNS查询类型\n        :type DnsQueryType: str\n        :param UserName: 登录服务器的账号\n        :type UserName: str\n        :param PassWord: 登录服务器的密码\n        :type PassWord: str\n        :param UseSecConn: 是否使用安全链接SSL， 0 不使用，1 使用\n        :type UseSecConn: int\n        :param NeedAuth: FTP登录验证方式  0 不验证  1 匿名登录  2 需要身份验证\n        :type NeedAuth: int\n        :param ReqDataType: 请求数据类型。0 表示请求为字符串类型。1表示为二进制类型\n        :type ReqDataType: int\n        :param ReqData: 发起TCP, UDP请求的协议请求数据\n        :type ReqData: str\n        :param RespDataType: 响应数据类型。0 表示响应为字符串类型。1表示为二进制类型\n        :type RespDataType: int\n        :param RespData: 预期的UDP请求的回应数据\n        :type RespData: str\n        :param RedirectFollowNum: 跟随跳转次数\n        :type RedirectFollowNum: int\n        """
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
        """
        :param GroupName: 拨测分组名称，不超过32个字符\n        :type GroupName: str\n        :param IsDefault: 是否为默认分组，取值可为 0 或 1。取 1 时表示设置为默认分组\n        :type IsDefault: int\n        :param Agents: Province, Isp 需要成对地进行选择。参数对的取值范围。参见：DescribeAgents 的返回结果。\n        :type Agents: list of CatAgent\n        """
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
        """
        :param GroupId: 拨测分组Id\n        :type GroupId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateTaskExRequest(AbstractModel):
    """CreateTaskEx请求参数结构体

    """

    def __init__(self):
        """
        :param CatTypeName: http, https, ping, tcp, ftp, smtp, udp, dns 之一\n        :type CatTypeName: str\n        :param Url: 拨测的URL， 例如：www.qq.com (URL域名解析需要能解析出具体的IP)\n        :type Url: str\n        :param Period: 拨测周期。取值可为1,5,15,30之一, 单位：分钟。精度不能低于用户等级规定的最小精度\n        :type Period: int\n        :param TaskName: 拨测任务名称不能超过32个字符。同一个用户创建的任务名不可重复\n        :type TaskName: str\n        :param AgentGroupId: 拨测分组ID，体现本拨测任务要采用哪些运营商作为拨测源。一般可直接填写本用户的默认拨测分组。参见：DescribeAgentGroups 接口，本参数使用返回结果里的GroupId的值。注意： Type为0时，AgentGroupId为必填\n        :type AgentGroupId: int\n        :param Host: 指定域名(如需要)\n        :type Host: str\n        :param IsHeader: 是否为Header请求（非0 发起Header 请求。为0，且PostData 非空，发起POST请求。为0，PostData 为空，发起GET请求）\n        :type IsHeader: int\n        :param SslVer: URL中含有"https"时有用。缺省为SSLv23。需要为 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一\n        :type SslVer: str\n        :param PostData: POST请求数据。空字符串表示非POST请求\n        :type PostData: str\n        :param UserAgent: 用户Agent信息\n        :type UserAgent: str\n        :param CheckStr: 要在结果中进行匹配的字符串\n        :type CheckStr: str\n        :param CheckType: 1 表示通过检查结果是否包含CheckStr 进行校验\n        :type CheckType: int\n        :param Cookie: 需要设置的Cookie信息\n        :type Cookie: str\n        :param TaskId: 任务ID，用于验证且修改任务时传入原任务ID\n        :type TaskId: int\n        :param UserName: 登录服务器的账号。如果为空字符串，表示不用校验用户密码。只做简单连接服务器的拨测\n        :type UserName: str\n        :param PassWord: 登录服务器的密码\n        :type PassWord: str\n        :param ReqDataType: 缺省为0。0 表示请求为字符串类型。1表示为二进制类型\n        :type ReqDataType: int\n        :param ReqData: 发起TCP, UDP请求的协议请求数据\n        :type ReqData: str\n        :param RespDataType: 缺省为0。0 表示响应为字符串类型。1表示为二进制类型\n        :type RespDataType: int\n        :param RespData: 预期的UDP请求的回应数据。字符串型，只需要返回的结果里包含本字符串算校验通过。二进制型，则需要严格等于才算通过\n        :type RespData: str\n        :param DnsSvr: 目的DNS服务器  可以为空字符串\n        :type DnsSvr: str\n        :param DnsCheckIp: 需要检验是否在DNS IP列表的IP。可以为空字符串，表示不校验\n        :type DnsCheckIp: str\n        :param DnsQueryType: 需要为下列值之一。缺省为A。A, MX, NS, CNAME, TXT, ANY\n        :type DnsQueryType: str\n        :param UseSecConn: 是否使用安全链接SSL， 0 不使用，1 使用\n        :type UseSecConn: int\n        :param NeedAuth: FTP登录验证方式， 0 不验证 ， 1 匿名登录， 2 需要身份验证\n        :type NeedAuth: int\n        :param Port: 拨测目标的端口号\n        :type Port: int\n        :param Type: Type=0 默认 （站点监控）Type=2 可用率监控\n        :type Type: int\n        :param IsVerify: IsVerify=0 非验证任务 IsVerify=1 验证任务，不传则默认为0\n        :type IsVerify: int\n        :param RedirectFollowNum: 跟随跳转次数，取值范围0-5，不传则表示不跟随\n        :type RedirectFollowNum: int\n        """
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
        """
        :param ResultId: 拨测结果查询ID。接下来可以使用查询拨测是否能够成功，验证能否通过。\n        :type ResultId: int\n        :param TaskId: 拨测任务ID。验证通过后，创建任务时使用，传递给CreateTask 接口。\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param LogTime: 数据点的时间\n        :type LogTime: str\n        :param MetricValue: 数据值\n        :type MetricValue: float\n        """
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
        """
        :param MetricName: 数据项\n        :type MetricName: str\n        :param Points: 数据点的时间和值\n        :type Points: list of DataPoint\n        """
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
        """
        :param GroupId: 拨测分组id\n        :type GroupId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTasksRequest(AbstractModel):
    """DeleteTasks请求参数结构体

    """

    def __init__(self):
        """
        :param TaskIds: 拨测任务id\n        :type TaskIds: list of int non-negative\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param SysDefaultGroup: 用户所属的系统默认拨测分组\n        :type SysDefaultGroup: :class:`tencentcloud.cat.v20180409.models.AgentGroup`\n        :param CustomGroups: 用户创建的拨测分组列表\n        :type CustomGroups: list of AgentGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Agents: 本用户可选的拨测点列表\n        :type Agents: list of CatAgent\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param NeedAdd: 如果不存在拨测相关的主题，是否自动创建一个。取值可为0, 1，默认为0\n        :type NeedAdd: int\n        """
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
        """
        :param TotalCount: 主题个数\n        :type TotalCount: int\n        :param Topics: 主题列表\n        :type Topics: list of AlarmTopic\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaskId: 拨测任务Id\n        :type TaskId: int\n        :param Offset: 从第Offset 条开始查询。缺省值为0\n        :type Offset: int\n        :param Limit: 本批次查询Limit 条记录。缺省值为20\n        :type Limit: int\n        :param Status: 0 全部, 1 已恢复, 2 未恢复  默认为0。其他值，视为0 查全部状态\n        :type Status: int\n        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省为7天前0点\n        :type BeginTime: str\n        :param EndTime: 格式如：2017-05-10 00:00:00  缺省为明天0点\n        :type EndTime: str\n        :param SortBy: 排序字段，可为Time, ObjName, Duration, Status, Content 之一。缺省为Time\n        :type SortBy: str\n        :param SortType: 升序或降序。可为Desc, Asc之一。缺省为Desc\n        :type SortType: str\n        :param ObjName: 告警对象的名称\n        :type ObjName: str\n        """
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
        """
        :param AlarmInfos: 告警信息列表\n        :type AlarmInfos: list of AlarmInfo\n        :param FaultRatio: 故障率\n        :type FaultRatio: float\n        :param FaultTimeSpec: 故障总时长\n        :type FaultTimeSpec: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Offset: 从第Offset 条开始查询。缺省值为0\n        :type Offset: int\n        :param Limit: 本批次查询Limit 条记录。缺省值为20\n        :type Limit: int\n        :param Status: 0 全部, 1 已恢复, 2 未恢复  默认为0。其他值，视为0 查全部状态。\n        :type Status: int\n        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省为7天前0点\n        :type BeginTime: str\n        :param EndTime: 格式如：2017-05-10 00:00:00  缺省为明天0点\n        :type EndTime: str\n        :param ObjName: 告警任务名\n        :type ObjName: str\n        :param SortBy: 排序字段，可为Time, ObjName, Duration, Status, Content 之一。缺省为Time。\n        :type SortBy: str\n        :param SortType: 升序或降序。可为Desc, Asc之一。缺省为Desc。\n        :type SortType: str\n        """
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
        """
        :param TotalCount: 告警总条数\n        :type TotalCount: int\n        :param AlarmInfos: 本批告警信息列表\n        :type AlarmInfos: list of AlarmInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaskId: 拨测任务Id\n        :type TaskId: int\n        :param Offset: 从第Offset 条开始查询。缺省值为0\n        :type Offset: int\n        :param Limit: 本批次查询Limit 条记录。缺省值为20\n        :type Limit: int\n        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省为当天0点，最多拉取1天的数据\n        :type BeginTime: str\n        :param EndTime: 格式如：2017-05-10 00:00:00  缺省为当前时间\n        :type EndTime: str\n        :param SortType: 按时间升序或降序。默认降序。可选值： Desc, Asc\n        :type SortType: str\n        """
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
        """
        :param TotalCount: 符合条件的总记录数\n        :type TotalCount: int\n        :param CatLogs: 拨测记录列表\n        :type CatLogs: list of CatLog\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TaskIds: 拨测任务id 数组\n        :type TaskIds: list of int non-negative\n        """
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
        """
        :param Tasks: 拨测任务列表\n        :type Tasks: list of CatTaskDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Offset: 从第Offset 条开始查询。缺省值为0\n        :type Offset: int\n        :param Limit: 本批次查询Limit 条记录。缺省值为20\n        :type Limit: int\n        :param Type: 拨测任务类型。0 站点监控，2 可用性监控。缺省值为2\n        :type Type: int\n        """
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
        """
        :param TotalCount: 符合条件的总任务数\n        :type TotalCount: int\n        :param Tasks: 任务列表\n        :type Tasks: list of TaskAlarm\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param MaxTaskNum: 用户可建立的最大任务数\n        :type MaxTaskNum: int\n        :param MaxAgentNum: 用户可用的最大拨测结点数\n        :type MaxAgentNum: int\n        :param MaxGroupNum: 用户可建立的最大拨测分组数\n        :type MaxGroupNum: int\n        :param MinPeriod: 用户可用的最小拨测间隔\n        :type MinPeriod: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DimensionsDetail(AbstractModel):
    """拨测点维度信息

    """

    def __init__(self):
        """
        :param Isp: 运营商列表\n        :type Isp: list of str\n        :param Province: 省份列表\n        :type Province: list of str\n        """
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
        


class GetAvailRatioHistoryRequest(AbstractModel):
    """GetAvailRatioHistory请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 拨测任务Id\n        :type TaskId: int\n        :param TimeStamp: 具体时间点\n        :type TimeStamp: str\n        """
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
        """
        :param AvgAvailRatio: 整体平均可用率\n        :type AvgAvailRatio: float\n        :param LowestAvailRatio: 各省份最低可用率\n        :type LowestAvailRatio: float\n        :param LowestProvince: 可用率最低的省份\n        :type LowestProvince: str\n        :param LowestIsp: 可用率最低的运营商\n        :type LowestIsp: str\n        :param ProvinceData: 分省份的可用率数据\n        :type ProvinceData: list of ProvinceDetail\n        :param AvgTime: 国内平均耗时，单位毫秒\n        :type AvgTime: float\n        :param AvgAvailRatio2: 国外平均可用率\n        :type AvgAvailRatio2: float\n        :param AvgTime2: 国外平均耗时，单位毫秒\n        :type AvgTime2: float\n        :param LowestAvailRatio2: 国外最低可用率\n        :type LowestAvailRatio2: float\n        :param LowestProvince2: 国外可用率最低的区域\n        :type LowestProvince2: str\n        :param LowestIsp2: 国外可用率最低的运营商\n        :type LowestIsp2: str\n        :param ProvinceData2: 国外分区域的可用率数据\n        :type ProvinceData2: list of ProvinceDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaskId: 拨测任务Id\n        :type TaskId: int\n        """
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
        """
        :param AvgAvailRatio: 整体平均可用率\n        :type AvgAvailRatio: float\n        :param LowestAvailRatio: 各省份最低可用率\n        :type LowestAvailRatio: float\n        :param LowestProvince: 可用率最低的省份\n        :type LowestProvince: str\n        :param ProvinceData: 分省份的可用率数据\n        :type ProvinceData: list of ProvinceDetail\n        :param AvgTime: 国内平均耗时，单位毫秒\n        :type AvgTime: float\n        :param AvgAvailRatio2: 国外平均可用率\n        :type AvgAvailRatio2: float\n        :param AvgTime2: 国外平均耗时，单位毫秒\n        :type AvgTime2: float\n        :param LowestAvailRatio2: 国外最低可用率\n        :type LowestAvailRatio2: float\n        :param LowestProvince2: 国外可用率最低的区域\n        :type LowestProvince2: str\n        :param ProvinceData2: 国外分区域的可用率数据\n        :type ProvinceData2: list of ProvinceDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaskId: 拨测任务Id\n        :type TaskId: int\n        """
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
        """
        :param AvgAvailRatio: 国内平均可用率\n        :type AvgAvailRatio: float\n        :param LowestAvailRatio: 各省份最低可用率\n        :type LowestAvailRatio: float\n        :param LowestProvince: 可用率最低的省份\n        :type LowestProvince: str\n        :param LowestIsp: 可用率最低的运营商\n        :type LowestIsp: str\n        :param ProvinceData: 分省份的可用率数据\n        :type ProvinceData: list of ProvinceDetail\n        :param AvgTime: 国内平均耗时，单位毫秒\n        :type AvgTime: float\n        :param AvgAvailRatio2: 国外平均可用率\n        :type AvgAvailRatio2: float\n        :param AvgTime2: 国外平均耗时，单位毫秒\n        :type AvgTime2: float\n        :param LowestAvailRatio2: 国外最低可用率\n        :type LowestAvailRatio2: float\n        :param LowestProvince2: 国外可用率最低的区域\n        :type LowestProvince2: str\n        :param LowestIsp2: 国外可用率最低的运营商\n        :type LowestIsp2: str\n        :param ProvinceData2: 国外分区域的可用率数据\n        :type ProvinceData2: list of ProvinceDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaskId: 验证成功的拨测任务id\n        :type TaskId: int\n        :param Date: 统计数据的发生日期。格式如：2017-05-09\n        :type Date: str\n        :param Period: 数据的采集周期，单位分钟。取值可为 1, 5, 15, 30\n        :type Period: int\n        :param Dimensions: 可为 Isp, Province\n        :type Dimensions: :class:`tencentcloud.cat.v20180409.models.DimensionsDetail`\n        :param MetricName: 可为  totalTime, parseTime, connectTime, sendTime, waitTime, receiveTime, availRatio。缺省值为 totalTime\n        :type MetricName: str\n        """
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
        """
        :param DataPoints: 数据点集合，时延等走势数据\n        :type DataPoints: list of DataPointMetric\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaskIds: 任务Id列表\n        :type TaskIds: list of int non-negative\n        """
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
        """
        :param RealData: 实时统计数据\n        :type RealData: list of ResultSummary\n        :param DayData: 按天的统计数据\n        :type DayData: list of ResultSummary\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaskId: 正整数。验证成功的拨测任务id\n        :type TaskId: int\n        :param BeginTime: 开始时间点。格式如：2017-05-09 10:20:00。注意，BeginTime 和 EndTime 需要在同一天\n        :type BeginTime: str\n        :param EndTime: 结束时间点。格式如：2017-05-09 10:25:00。注意，BeginTime 和 EndTime 需要在同一天\n        :type EndTime: str\n        :param Province: 省份名称的全拼\n        :type Province: str\n        """
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
        """
        :param Details: 拨测失败详情列表\n        :type Details: list of CatReturnDetail\n        :param Summary: 拨测失败汇总列表\n        :type Summary: list of CatReturnSummary\n        :param BeginTime: 开始时间\n        :type BeginTime: str\n        :param EndTime: 截至时间\n        :type EndTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaskId: 正整数。验证成功的拨测任务id\n        :type TaskId: int\n        :param BeginTime: 开始时间点。格式如：2017-05-09 10:20:00，最多拉群两天的数据\n        :type BeginTime: str\n        :param EndTime: 结束时间点。格式如：2017-05-09 10:25:00，最多拉群两天的数据\n        :type EndTime: str\n        :param Province: 省份名称的全拼\n        :type Province: str\n        """
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
        """
        :param Details: 拨测失败详情列表\n        :type Details: list of CatReturnDetail\n        :param Summary: 拨测失败汇总列表\n        :type Summary: list of CatReturnSummary\n        :param BeginTime: 开始时间\n        :type BeginTime: str\n        :param EndTime: 截至时间\n        :type EndTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TotalCount: 拨测任务总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class IspDetail(AbstractModel):
    """运营商可用率

    """

    def __init__(self):
        """
        :param IspName: 运营商名称\n        :type IspName: str\n        :param AvailRatio: 可用率\n        :type AvailRatio: float\n        :param AvgTime: 平均耗时
注意：此字段可能返回 null，表示取不到有效值。\n        :type AvgTime: float\n        """
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
        


class ModifyAgentGroupRequest(AbstractModel):
    """ModifyAgentGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 拨测分组ID\n        :type GroupId: int\n        :param GroupName: 拨测分组名称\n        :type GroupName: str\n        :param IsDefault: 是否为默认分组。取值可为0，1。取 1 时表示设置为默认分组\n        :type IsDefault: int\n        :param Agents: Province, Isp 需要成对地进行选择。参数对的取值范围。参见：DescribeAgents 的返回结果。\n        :type Agents: list of CatAgent\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTaskExRequest(AbstractModel):
    """ModifyTaskEx请求参数结构体

    """

    def __init__(self):
        """
        :param CatTypeName: http, https, ping, tcp, ftp, smtp, udp, dns 之一\n        :type CatTypeName: str\n        :param Url: 拨测的URL，例如：www.qq.com (URL域名解析需要能解析出具体的IP)\n        :type Url: str\n        :param Period: 拨测周期。取值可为1,5,15,30之一, 单位：分钟。精度不能低于用户等级规定的最小精度\n        :type Period: int\n        :param TaskName: 拨测任务名称不能超过32个字符。同一个用户创建的任务名不可重复\n        :type TaskName: str\n        :param TaskId: 验证成功的拨测任务ID\n        :type TaskId: int\n        :param AgentGroupId: 拨测分组ID，体现本拨测任务要采用哪些运营商作为拨测源。一般可直接填写本用户的默认拨测分组。参见：DescribeAgentGroupList 接口，本参数使用返回结果里的GroupId的值。注意，Type为0时，AgentGroupId为必填\n        :type AgentGroupId: int\n        :param Host: 指定域名(如需要)\n        :type Host: str\n        :param Port: 拨测目标的端口号\n        :type Port: int\n        :param IsHeader: 是否为Header请求（非0 发起Header 请求。为0，且PostData非空，发起POST请求。为0，PostData为空，发起GET请求）\n        :type IsHeader: int\n        :param SslVer: URL中含有"https"时有用。缺省为SSLv23。需要为 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一\n        :type SslVer: str\n        :param PostData: POST 请求数据，空字符串表示非POST请求\n        :type PostData: str\n        :param UserAgent: 用户Agent信息\n        :type UserAgent: str\n        :param CheckStr: 要在结果中进行匹配的字符串\n        :type CheckStr: str\n        :param CheckType: 1 表示通过检查结果是否包含CheckStr 进行校验\n        :type CheckType: int\n        :param Cookie: 需要设置的Cookie信息\n        :type Cookie: str\n        :param UserName: 登录服务器的账号。如果为空字符串，表示不用校验用户密码。只做简单连接服务器的拨测\n        :type UserName: str\n        :param PassWord: 登录服务器的密码\n        :type PassWord: str\n        :param ReqDataType: 缺省为0，0 表示请求为字符串类型, 1表示为二进制类型\n        :type ReqDataType: int\n        :param ReqData: 发起TCP, UDP请求的协议请求数据\n        :type ReqData: str\n        :param RespDataType: 缺省为0。0 表示请求为字符串类型。1表示为二进制类型\n        :type RespDataType: str\n        :param RespData: 预期的UDP请求的回应数据。字符串型，只需要返回的结果里包含本字符串算校验通过。二进制型，则需要严格等于才算通过\n        :type RespData: str\n        :param DnsSvr: 目的DNS服务器，可以为空字符串\n        :type DnsSvr: str\n        :param DnsCheckIp: 需要检验是否在DNS IP列表的IP。可以为空字符串，表示不校验\n        :type DnsCheckIp: str\n        :param DnsQueryType: 需要为下列值之一。缺省为A。A, MX, NS, CNAME, TXT, ANY\n        :type DnsQueryType: str\n        :param UseSecConn: 是否使用安全链接SSL， 0 不使用，1 使用\n        :type UseSecConn: int\n        :param NeedAuth: FTP登录验证方式，  0 不验证  1 匿名登录  2 需要身份验证\n        :type NeedAuth: int\n        :param Type: Type=0 默认 （站点监控） Type=2 可用率监控\n        :type Type: int\n        :param RedirectFollowNum: 跟随跳转次数，取值范围0-5，不传则表示不跟随\n        :type RedirectFollowNum: int\n        """
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
        """
        :param TaskId: 拨测任务ID。验证通过后，创建任务时使用，传递给CreateTask 接口。\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PauseTaskRequest(AbstractModel):
    """PauseTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 拨测任务id\n        :type TaskId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProvinceDetail(AbstractModel):
    """省份可用率

    """

    def __init__(self):
        """
        :param AvgAvailRatio: 可用率\n        :type AvgAvailRatio: float\n        :param ProvinceName: 省份名称\n        :type ProvinceName: str\n        :param Mapkey: 省份英文名称\n        :type Mapkey: str\n        :param TimeStamp: 统计时间点\n        :type TimeStamp: str\n        :param IspDetail: 分运营商可用率\n        :type IspDetail: list of IspDetail\n        :param AvgTime: 平均耗时，单位毫秒\n        :type AvgTime: float\n        :param Province: 省份\n        :type Province: str\n        """
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
        """
        :param LogTime: 统计时间\n        :type LogTime: str\n        :param TaskId: 任务ID\n        :type TaskId: int\n        :param AvailRatio: 实时可用率\n        :type AvailRatio: float\n        :param ReponseTime: 实时响应时间\n        :type ReponseTime: float\n        """
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
        


class RunTaskRequest(AbstractModel):
    """RunTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务Id\n        :type TaskId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TaskAlarm(AbstractModel):
    """可用性监控任务状态及告警信息

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param TaskName: 任务名称\n        :type TaskName: str\n        :param Period: 任务周期，单位为分钟。目前支持1，5，15，30几种取值\n        :type Period: int\n        :param CatTypeName: 拨测类型。http, https, ping, tcp, udp, smtp, pop3, dns 之一\n        :type CatTypeName: str\n        :param Status: 任务状态。1表示暂停，2表示运行中，0为初始态\n        :type Status: int\n        :param CgiUrl: 拨测任务的URL\n        :type CgiUrl: str\n        :param AddTime: 任务创建时间\n        :type AddTime: str\n        :param AlarmStatus: 告警状态。1 故障，0 正常\n        :type AlarmStatus: int\n        :param StatusInfo: 告警状态描述，统计信息\n        :type StatusInfo: str\n        :param UpdateTime: 任务更新时间\n        :type UpdateTime: str\n        """
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
        


class VerifyResultRequest(AbstractModel):
    """VerifyResult请求参数结构体

    """

    def __init__(self):
        """
        :param ResultId: 要查询的拨测任务的结果id\n        :type ResultId: int\n        """
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
        """
        :param ErrorReason: 错误的原因\n        :type ErrorReason: str\n        :param ResultCode: 错误号\n        :type ResultCode: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ErrorReason = None
        self.ResultCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorReason = params.get("ErrorReason")
        self.ResultCode = params.get("ResultCode")
        self.RequestId = params.get("RequestId")