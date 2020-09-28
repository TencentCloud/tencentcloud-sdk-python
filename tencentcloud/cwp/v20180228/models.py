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


class Account(AbstractModel):
    """帐号列表信息数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param Username: 帐号名。
        :type Username: str
        :param Groups: 帐号所属组。
        :type Groups: str
        :param Privilege: 帐号类型。
<li>ORDINARY：普通帐号</li>
<li>SUPPER：超级管理员帐号</li>
        :type Privilege: str
        :param AccountCreateTime: 帐号创建时间。
        :type AccountCreateTime: str
        :param LastLoginTime: 帐号最后登录时间。
        :type LastLoginTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.Groups = None
        self.Privilege = None
        self.AccountCreateTime = None
        self.LastLoginTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.Groups = params.get("Groups")
        self.Privilege = params.get("Privilege")
        self.AccountCreateTime = params.get("AccountCreateTime")
        self.LastLoginTime = params.get("LastLoginTime")


class AccountStatistics(AbstractModel):
    """帐号统计数据。

    """

    def __init__(self):
        """
        :param Username: 用户名。
        :type Username: str
        :param MachineNum: 主机数量。
        :type MachineNum: int
        """
        self.Username = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.MachineNum = params.get("MachineNum")


class AddLoginWhiteListRequest(AbstractModel):
    """AddLoginWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param Rules: 白名单规则
        :type Rules: :class:`tencentcloud.cwp.v20180228.models.LoginWhiteListsRule`
        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = LoginWhiteListsRule()
            self.Rules._deserialize(params.get("Rules"))


class AddLoginWhiteListResponse(AbstractModel):
    """AddLoginWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddMachineTagRequest(AbstractModel):
    """AddMachineTag请求参数结构体

    """

    def __init__(self):
        """
        :param Quuid: 云服务器ID
        :type Quuid: str
        :param TagId: 标签ID
        :type TagId: int
        :param MRegion: 云服务器地区
        :type MRegion: str
        :param MArea: 云服务器类型(CVM|BM)
        :type MArea: str
        """
        self.Quuid = None
        self.TagId = None
        self.MRegion = None
        self.MArea = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.TagId = params.get("TagId")
        self.MRegion = params.get("MRegion")
        self.MArea = params.get("MArea")


class AddMachineTagResponse(AbstractModel):
    """AddMachineTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AgentVul(AbstractModel):
    """主机漏洞信息

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param VulName: 漏洞名称。
        :type VulName: str
        :param VulLevel: 漏洞危害等级。
<li>HIGH：高危</li>
<li>MIDDLE：中危</li>
<li>LOW：低危</li>
<li>NOTICE：提示</li>
        :type VulLevel: str
        :param LastScanTime: 最后扫描时间。
        :type LastScanTime: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulId: 漏洞种类ID。
        :type VulId: int
        :param VulStatus: 漏洞状态。
<li>UN_OPERATED : 待处理</li>
<li>FIXED : 已修复</li>
        :type VulStatus: str
        """
        self.Id = None
        self.MachineIp = None
        self.VulName = None
        self.VulLevel = None
        self.LastScanTime = None
        self.Description = None
        self.VulId = None
        self.VulStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.LastScanTime = params.get("LastScanTime")
        self.Description = params.get("Description")
        self.VulId = params.get("VulId")
        self.VulStatus = params.get("VulStatus")


class BashEvent(AbstractModel):
    """高危命令数据

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: int
        :param Uuid: 云镜ID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param User: 执行用户名
        :type User: str
        :param Platform: 平台类型
        :type Platform: int
        :param BashCmd: 执行命令
        :type BashCmd: str
        :param RuleId: 规则ID
        :type RuleId: int
        :param RuleName: 规则名称
        :type RuleName: str
        :param RuleLevel: 规则等级
        :type RuleLevel: int
        :param Status: 处理状态
        :type Status: int
        :param CreateTime: 发生时间
        :type CreateTime: str
        :param MachineName: 主机名
        :type MachineName: str
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.User = None
        self.Platform = None
        self.BashCmd = None
        self.RuleId = None
        self.RuleName = None
        self.RuleLevel = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.User = params.get("User")
        self.Platform = params.get("Platform")
        self.BashCmd = params.get("BashCmd")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RuleLevel = params.get("RuleLevel")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")


class BashRule(AbstractModel):
    """高危命令规则

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param Name: 规则名称
        :type Name: str
        :param Level: 危险等级(1: 高危 2:中危 3: 低危)
        :type Level: int
        :param Rule: 正则表达式
        :type Rule: str
        :param Decription: 规则描述
        :type Decription: str
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态 (0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        """
        self.Id = None
        self.Uuid = None
        self.Name = None
        self.Level = None
        self.Rule = None
        self.Decription = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Rule = params.get("Rule")
        self.Decription = params.get("Decription")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")


class BruteAttack(AbstractModel):
    """暴力破解列表

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Status: 破解事件状态
<li>BRUTEATTACK_FAIL_ACCOUNT： 暴力破解事件-失败(存在帐号)  </li>
<li>BRUTEATTACK_FAIL_NOACCOUNT：暴力破解事件-失败(帐号不存在)</li>
<li>BRUTEATTACK_SUCCESS：暴力破解事件-成功</li>
        :type Status: str
        :param UserName: 用户名称。
        :type UserName: str
        :param City: 城市ID。
        :type City: int
        :param Country: 国家ID。
        :type Country: int
        :param Province: 省份ID。
        :type Province: int
        :param SrcIp: 来源IP。
        :type SrcIp: str
        :param Count: 尝试破解次数。
        :type Count: int
        :param CreateTime: 发生时间。
        :type CreateTime: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param IsProVersion: 是否专业版。
        :type IsProVersion: bool
        :param BanStatus: 阻断状态。
        :type BanStatus: str
        :param Quuid: 机器UUID
        :type Quuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.UserName = None
        self.City = None
        self.Country = None
        self.Province = None
        self.SrcIp = None
        self.Count = None
        self.CreateTime = None
        self.MachineName = None
        self.Uuid = None
        self.IsProVersion = None
        self.BanStatus = None
        self.Quuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.UserName = params.get("UserName")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.SrcIp = params.get("SrcIp")
        self.Count = params.get("Count")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.Uuid = params.get("Uuid")
        self.IsProVersion = params.get("IsProVersion")
        self.BanStatus = params.get("BanStatus")
        self.Quuid = params.get("Quuid")


class ChargePrepaid(AbstractModel):
    """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。

    """

    def __init__(self):
        """
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自动续费标识。取值范围：
<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li>

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class CloseProVersionRequest(AbstractModel):
    """CloseProVersion请求参数结构体

    """

    def __init__(self):
        """
        :param Quuid: 主机唯一标识Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self.Quuid = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")


class CloseProVersionResponse(AbstractModel):
    """CloseProVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Component(AbstractModel):
    """组件列表数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param ComponentVersion: 组件版本号。
        :type ComponentVersion: str
        :param ComponentType: 组件类型。
<li>SYSTEM：系统组件</li>
<li>WEB：Web组件</li>
        :type ComponentType: str
        :param ComponentName: 组件名称。
        :type ComponentName: str
        :param ModifyTime: 组件检测更新时间。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.ComponentVersion = None
        self.ComponentType = None
        self.ComponentName = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.ComponentVersion = params.get("ComponentVersion")
        self.ComponentType = params.get("ComponentType")
        self.ComponentName = params.get("ComponentName")
        self.ModifyTime = params.get("ModifyTime")


class ComponentStatistics(AbstractModel):
    """组件统计数据。

    """

    def __init__(self):
        """
        :param Id: 组件ID。
        :type Id: int
        :param MachineNum: 主机数量。
        :type MachineNum: int
        :param ComponentName: 组件名称。
        :type ComponentName: str
        :param ComponentType: 组件类型。
<li>WEB：Web组件</li>
<li>SYSTEM：系统组件</li>
        :type ComponentType: str
        :param Description: 组件描述。
        :type Description: str
        """
        self.Id = None
        self.MachineNum = None
        self.ComponentName = None
        self.ComponentType = None
        self.Description = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineNum = params.get("MachineNum")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Description = params.get("Description")


class CreateBaselineStrategyRequest(AbstractModel):
    """CreateBaselineStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param StrategyName: 策略名称
        :type StrategyName: str
        :param ScanCycle: 检测周期, 表示每隔多少天进行检测.示例: 2, 表示每2天进行检测一次.
        :type ScanCycle: int
        :param ScanAt: 定期检测时间，该时间下发扫描. 示例:“22:00”, 表示在22:00下发检测
        :type ScanAt: str
        :param CategoryIds: 该策略下选择的基线id数组. 示例: [1,3,5,7]
        :type CategoryIds: list of int non-negative
        :param IsGlobal: 扫描范围是否全部服务器, 1:是  0:否, 为1则为全部专业版主机
        :type IsGlobal: int
        :param MachineType: 云主机类型：“CVM”：虚拟主机，"BMS"：裸金属，"ECM"：边缘计算主机
        :type MachineType: str
        :param RegionCode: 主机地域. 示例: "ap-bj"
        :type RegionCode: str
        :param Quuids: 主机id数组. 示例: ["quuid1","quuid2"]
        :type Quuids: list of str
        """
        self.StrategyName = None
        self.ScanCycle = None
        self.ScanAt = None
        self.CategoryIds = None
        self.IsGlobal = None
        self.MachineType = None
        self.RegionCode = None
        self.Quuids = None


    def _deserialize(self, params):
        self.StrategyName = params.get("StrategyName")
        self.ScanCycle = params.get("ScanCycle")
        self.ScanAt = params.get("ScanAt")
        self.CategoryIds = params.get("CategoryIds")
        self.IsGlobal = params.get("IsGlobal")
        self.MachineType = params.get("MachineType")
        self.RegionCode = params.get("RegionCode")
        self.Quuids = params.get("Quuids")


class CreateBaselineStrategyResponse(AbstractModel):
    """CreateBaselineStrategy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateOpenPortTaskRequest(AbstractModel):
    """CreateOpenPortTask请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class CreateOpenPortTaskResponse(AbstractModel):
    """CreateOpenPortTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProcessTaskRequest(AbstractModel):
    """CreateProcessTask请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class CreateProcessTaskResponse(AbstractModel):
    """CreateProcessTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUsualLoginPlacesRequest(AbstractModel):
    """CreateUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuids: 云镜客户端UUID数组。
        :type Uuids: list of str
        :param Places: 登录地域信息数组。
        :type Places: list of Place
        """
        self.Uuids = None
        self.Places = None


    def _deserialize(self, params):
        self.Uuids = params.get("Uuids")
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)


class CreateUsualLoginPlacesResponse(AbstractModel):
    """CreateUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DefendAttackLog(AbstractModel):
    """网络攻击日志

    """

    def __init__(self):
        """
        :param Id: 日志ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param SrcIp: 来源IP
        :type SrcIp: str
        :param SrcPort: 来源端口
        :type SrcPort: int
        :param HttpMethod: 攻击方式
        :type HttpMethod: str
        :param HttpCgi: 攻击描述
        :type HttpCgi: str
        :param HttpParam: 攻击参数
        :type HttpParam: str
        :param VulType: 威胁类型
        :type VulType: str
        :param CreatedAt: 攻击时间
        :type CreatedAt: str
        :param MachineIp: 目标服务器IP
        :type MachineIp: str
        :param MachineName: 目标服务器名称
        :type MachineName: str
        :param DstIp: 目标IP
        :type DstIp: str
        :param DstPort: 目标端口
        :type DstPort: int
        :param HttpContent: 攻击内容
        :type HttpContent: str
        """
        self.Id = None
        self.Uuid = None
        self.SrcIp = None
        self.SrcPort = None
        self.HttpMethod = None
        self.HttpCgi = None
        self.HttpParam = None
        self.VulType = None
        self.CreatedAt = None
        self.MachineIp = None
        self.MachineName = None
        self.DstIp = None
        self.DstPort = None
        self.HttpContent = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.SrcIp = params.get("SrcIp")
        self.SrcPort = params.get("SrcPort")
        self.HttpMethod = params.get("HttpMethod")
        self.HttpCgi = params.get("HttpCgi")
        self.HttpParam = params.get("HttpParam")
        self.VulType = params.get("VulType")
        self.CreatedAt = params.get("CreatedAt")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.HttpContent = params.get("HttpContent")


class DeleteAttackLogsRequest(AbstractModel):
    """DeleteAttackLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 日志ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteAttackLogsResponse(AbstractModel):
    """DeleteAttackLogs返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBashEventsRequest(AbstractModel):
    """DeleteBashEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteBashEventsResponse(AbstractModel):
    """DeleteBashEvents返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBashRulesRequest(AbstractModel):
    """DeleteBashRules请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteBashRulesResponse(AbstractModel):
    """DeleteBashRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 暴力破解事件Id数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoginWhiteListRequest(AbstractModel):
    """DeleteLoginWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 白名单ID
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteLoginWhiteListResponse(AbstractModel):
    """DeleteLoginWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineTagRequest(AbstractModel):
    """DeleteMachineTag请求参数结构体

    """

    def __init__(self):
        """
        :param Rid: 关联的标签ID
        :type Rid: int
        """
        self.Rid = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")


class DeleteMachineTagResponse(AbstractModel):
    """DeleteMachineTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMaliciousRequestsRequest(AbstractModel):
    """DeleteMaliciousRequests请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 恶意请求记录ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteMaliciousRequestsResponse(AbstractModel):
    """DeleteMaliciousRequests返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马记录ID数组
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 异地登录事件ID数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivilegeEventsRequest(AbstractModel):
    """DeletePrivilegeEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeletePrivilegeEventsResponse(AbstractModel):
    """DeletePrivilegeEvents返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivilegeRulesRequest(AbstractModel):
    """DeletePrivilegeRules请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeletePrivilegeRulesResponse(AbstractModel):
    """DeletePrivilegeRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReverseShellEventsRequest(AbstractModel):
    """DeleteReverseShellEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteReverseShellEventsResponse(AbstractModel):
    """DeleteReverseShellEvents返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReverseShellRulesRequest(AbstractModel):
    """DeleteReverseShellRules请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteReverseShellRulesResponse(AbstractModel):
    """DeleteReverseShellRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagsRequest(AbstractModel):
    """DeleteTags请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 标签ID
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteTagsResponse(AbstractModel):
    """DeleteTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsualLoginPlacesRequest(AbstractModel):
    """DeleteUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端Uuid
        :type Uuid: str
        :param CityIds: 已添加常用登录地城市ID数组
        :type CityIds: list of int non-negative
        """
        self.Uuid = None
        self.CityIds = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.CityIds = params.get("CityIds")


class DeleteUsualLoginPlacesResponse(AbstractModel):
    """DeleteUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号用户名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号统计列表记录总数。
        :type TotalCount: int
        :param AccountStatistics: 帐号统计列表。
        :type AccountStatistics: list of AccountStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountStatistics") is not None:
            self.AccountStatistics = []
            for item in params.get("AccountStatistics"):
                obj = AccountStatistics()
                obj._deserialize(item)
                self.AccountStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Username和Uuid必填其一，使用Uuid表示，查询该主机下列表信息。
        :type Uuid: str
        :param Username: 云镜客户端唯一Uuid。Username和Uuid必填其一，使用Username表示，查询该用户名下列表信息。
        :type Username: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
<li>Privilege - String - 是否必填：否 - 帐号类型（ORDINARY: 普通帐号 | SUPPER: 超级管理员帐号）</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Username = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Username = params.get("Username")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号列表记录总数。
        :type TotalCount: int
        :param Accounts: 帐号数据列表。
        :type Accounts: list of Account
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Accounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentVulsRequest(AbstractModel):
    """DescribeAgentVuls请求参数结构体

    """

    def __init__(self):
        """
        :param VulType: 漏洞类型。
<li>WEB: Web应用漏洞</li>
<li>SYSTEM：系统组件漏洞</li>
<li>BASELINE：安全基线</li>
        :type VulType: str
        :param Uuid: 客户端UUID。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | FIXED：已修复）
        :type Filters: list of Filter
        """
        self.VulType = None
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAgentVulsResponse(AbstractModel):
    """DescribeAgentVuls返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param AgentVuls: 主机漏洞信息
        :type AgentVuls: list of AgentVul
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AgentVuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AgentVuls") is not None:
            self.AgentVuls = []
            for item in params.get("AgentVuls"):
                obj = AgentVul()
                obj._deserialize(item)
                self.AgentVuls.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmAttributeRequest(AbstractModel):
    """DescribeAlarmAttribute请求参数结构体

    """


class DescribeAlarmAttributeResponse(AbstractModel):
    """DescribeAlarmAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param Offline: 防护软件离线告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type Offline: str
        :param Malware: 发现木马告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type Malware: str
        :param NonlocalLogin: 发现异地登录告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type NonlocalLogin: str
        :param CrackSuccess: 被暴力破解成功告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type CrackSuccess: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Offline = None
        self.Malware = None
        self.NonlocalLogin = None
        self.CrackSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offline = params.get("Offline")
        self.Malware = params.get("Malware")
        self.NonlocalLogin = params.get("NonlocalLogin")
        self.CrackSuccess = params.get("CrackSuccess")
        self.RequestId = params.get("RequestId")


class DescribeAttackLogInfoRequest(AbstractModel):
    """DescribeAttackLogInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 日志ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DescribeAttackLogInfoResponse(AbstractModel):
    """DescribeAttackLogInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 日志ID
        :type Id: int
        :param Quuid: 主机ID
        :type Quuid: str
        :param SrcPort: 攻击来源端口
        :type SrcPort: int
        :param SrcIp: 攻击来源IP
        :type SrcIp: str
        :param DstPort: 攻击目标端口
        :type DstPort: int
        :param DstIp: 攻击目标IP
        :type DstIp: str
        :param HttpMethod: 攻击方法
        :type HttpMethod: str
        :param HttpHost: 攻击目标主机
        :type HttpHost: str
        :param HttpHead: 攻击头信息
        :type HttpHead: str
        :param HttpUserAgent: 攻击者浏览器标识
        :type HttpUserAgent: str
        :param HttpReferer: 请求源
        :type HttpReferer: str
        :param VulType: 威胁类型
        :type VulType: str
        :param HttpCgi: 攻击路径
        :type HttpCgi: str
        :param HttpParam: 攻击参数
        :type HttpParam: str
        :param CreatedAt: 攻击时间
        :type CreatedAt: str
        :param HttpContent: 攻击内容
        :type HttpContent: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Quuid = None
        self.SrcPort = None
        self.SrcIp = None
        self.DstPort = None
        self.DstIp = None
        self.HttpMethod = None
        self.HttpHost = None
        self.HttpHead = None
        self.HttpUserAgent = None
        self.HttpReferer = None
        self.VulType = None
        self.HttpCgi = None
        self.HttpParam = None
        self.CreatedAt = None
        self.HttpContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Quuid = params.get("Quuid")
        self.SrcPort = params.get("SrcPort")
        self.SrcIp = params.get("SrcIp")
        self.DstPort = params.get("DstPort")
        self.DstIp = params.get("DstIp")
        self.HttpMethod = params.get("HttpMethod")
        self.HttpHost = params.get("HttpHost")
        self.HttpHead = params.get("HttpHead")
        self.HttpUserAgent = params.get("HttpUserAgent")
        self.HttpReferer = params.get("HttpReferer")
        self.VulType = params.get("VulType")
        self.HttpCgi = params.get("HttpCgi")
        self.HttpParam = params.get("HttpParam")
        self.CreatedAt = params.get("CreatedAt")
        self.HttpContent = params.get("HttpContent")
        self.RequestId = params.get("RequestId")


class DescribeAttackLogsRequest(AbstractModel):
    """DescribeAttackLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>HttpMethod - String - 是否必填：否 - 攻击方法(POST|GET)</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
<li>DateRange - String - 是否必填：否 - 时间范围(存储最近3个月的数据)，如最近一个月["2019-11-17", "2019-12-17"]</li>
        :type Filters: list of Filter
        :param Uuid: 主机安全客户端ID
        :type Uuid: str
        :param Quuid: 云主机机器ID
        :type Quuid: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Uuid = None
        self.Quuid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")


class DescribeAttackLogsResponse(AbstractModel):
    """DescribeAttackLogs返回参数结构体

    """

    def __init__(self):
        """
        :param AttackLogs: 日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackLogs: list of DefendAttackLog
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AttackLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttackLogs") is not None:
            self.AttackLogs = []
            for item in params.get("AttackLogs"):
                obj = DefendAttackLog()
                obj._deserialize(item)
                self.AttackLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBashEventsRequest(AbstractModel):
    """DescribeBashEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键词(主机内网IP)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeBashEventsResponse(AbstractModel):
    """DescribeBashEvents返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 高危命令事件列表
        :type List: list of BashEvent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BashEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBashRulesRequest(AbstractModel):
    """DescribeBashRules请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 0-系统规则; 1-用户规则
        :type Type: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(规则名称)</li>
        :type Filters: list of Filter
        """
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeBashRulesResponse(AbstractModel):
    """DescribeBashRules返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表内容
        :type List: list of BashRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BashRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBruteAttacksRequest(AbstractModel):
    """DescribeBruteAttacks请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 -  查询关键字</li>
<li>Status - String - 是否必填：否 -  查询状态（FAILED：破解失败 |SUCCESS：破解成功）</li>
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        """
        self.Uuid = None
        self.Offset = None
        self.Filters = None
        self.Limit = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")


class DescribeBruteAttacksResponse(AbstractModel):
    """DescribeBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 事件数量
        :type TotalCount: int
        :param BruteAttacks: 暴力破解事件列表
        :type BruteAttacks: list of BruteAttack
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BruteAttacks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = BruteAttack()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentInfoRequest(AbstractModel):
    """DescribeComponentInfo请求参数结构体

    """

    def __init__(self):
        """
        :param ComponentId: 组件ID。
        :type ComponentId: int
        """
        self.ComponentId = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")


class DescribeComponentInfoResponse(AbstractModel):
    """DescribeComponentInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 组件ID。
        :type Id: int
        :param ComponentName: 组件名称。
        :type ComponentName: str
        :param ComponentType: 组件类型。
<li>WEB：web组件</li>
<li>SYSTEM：系统组件</li>
        :type ComponentType: str
        :param Homepage: 组件官网。
        :type Homepage: str
        :param Description: 组件描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.ComponentName = None
        self.ComponentType = None
        self.Homepage = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Homepage = params.get("Homepage")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeComponentStatisticsRequest(AbstractModel):
    """DescribeComponentStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
ComponentName - String - 是否必填：否 - 组件名称
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 组件统计列表记录总数。
        :type TotalCount: int
        :param ComponentStatistics: 组件统计列表数据数组。
        :type ComponentStatistics: list of ComponentStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ComponentStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComponentStatistics") is not None:
            self.ComponentStatistics = []
            for item in params.get("ComponentStatistics"):
                obj = ComponentStatistics()
                obj._deserialize(item)
                self.ComponentStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentsRequest(AbstractModel):
    """DescribeComponents请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Uuid和ComponentId必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param ComponentId: 组件ID。Uuid和ComponentId必填其一，使用ComponentId表示，查询该组件列表信息。
        :type ComponentId: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ComponentVersion - String - 是否必填：否 - 组件版本号</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.ComponentId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.ComponentId = params.get("ComponentId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeComponentsResponse(AbstractModel):
    """DescribeComponents返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 组件列表记录总数。
        :type TotalCount: int
        :param Components: 组件列表数据。
        :type Components: list of Component
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Components = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHistoryAccountsRequest(AbstractModel):
    """DescribeHistoryAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号变更历史列表记录总数。
        :type TotalCount: int
        :param HistoryAccounts: 帐号变更历史数据数组。
        :type HistoryAccounts: list of HistoryAccount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HistoryAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HistoryAccounts") is not None:
            self.HistoryAccounts = []
            for item in params.get("HistoryAccounts"):
                obj = HistoryAccount()
                obj._deserialize(item)
                self.HistoryAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImpactedHostsRequest(AbstractModel):
    """DescribeImpactedHosts请求参数结构体

    """

    def __init__(self):
        """
        :param VulId: 漏洞种类ID。
        :type VulId: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED：待处理 | FIXED：已修复）</li>
        :type Filters: list of Filter
        """
        self.VulId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeImpactedHostsResponse(AbstractModel):
    """DescribeImpactedHosts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param ImpactedHosts: 漏洞影响机器列表数组
        :type ImpactedHosts: list of ImpactedHost
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImpactedHosts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImpactedHosts") is not None:
            self.ImpactedHosts = []
            for item in params.get("ImpactedHosts"):
                obj = ImpactedHost()
                obj._deserialize(item)
                self.ImpactedHosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoginWhiteListRequest(AbstractModel):
    """DescribeLoginWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeLoginWhiteListResponse(AbstractModel):
    """DescribeLoginWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param LoginWhiteLists: 异地登录白名单数组
        :type LoginWhiteLists: list of LoginWhiteLists
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoginWhiteLists = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoginWhiteLists") is not None:
            self.LoginWhiteLists = []
            for item in params.get("LoginWhiteLists"):
                obj = LoginWhiteLists()
                obj._deserialize(item)
                self.LoginWhiteLists.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineInfoRequest(AbstractModel):
    """DescribeMachineInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo返回参数结构体

    """

    def __init__(self):
        """
        :param MachineIp: 机器ip。
        :type MachineIp: str
        :param ProtectDays: 受云镜保护天数。
        :type ProtectDays: int
        :param MachineOs: 操作系统。
        :type MachineOs: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param MachineStatus: 在线状态。
<li>ONLINE： 在线</li>
<li>OFFLINE：离线</li>
        :type MachineStatus: str
        :param InstanceId: CVM或BM主机唯一标识。
        :type InstanceId: str
        :param MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param Quuid: CVM或BM主机唯一Uuid。
        :type Quuid: str
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param IsProVersion: 是否开通专业版。
<li>true：是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param ProVersionOpenDate: 专业版开通时间。
        :type ProVersionOpenDate: str
        :param MachineType: 云主机类型。
<li>CVM: 虚拟主机</li>
<li>BM: 黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param FreeMalwaresLeft: 免费木马剩余检测数量。
        :type FreeMalwaresLeft: int
        :param FreeVulsLeft: 免费漏洞剩余检测数量。
        :type FreeVulsLeft: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineIp = None
        self.ProtectDays = None
        self.MachineOs = None
        self.MachineName = None
        self.MachineStatus = None
        self.InstanceId = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.IsProVersion = None
        self.ProVersionOpenDate = None
        self.MachineType = None
        self.MachineRegion = None
        self.PayMode = None
        self.FreeMalwaresLeft = None
        self.FreeVulsLeft = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.ProtectDays = params.get("ProtectDays")
        self.MachineOs = params.get("MachineOs")
        self.MachineName = params.get("MachineName")
        self.MachineStatus = params.get("MachineStatus")
        self.InstanceId = params.get("InstanceId")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.IsProVersion = params.get("IsProVersion")
        self.ProVersionOpenDate = params.get("ProVersionOpenDate")
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.PayMode = params.get("PayMode")
        self.FreeMalwaresLeft = params.get("FreeMalwaresLeft")
        self.FreeVulsLeft = params.get("FreeVulsLeft")
        self.RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线 | UNINSTALLED：未安装）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of Filter
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回参数结构体

    """

    def __init__(self):
        """
        :param Machines: 主机列表
        :type Machines: list of Machine
        :param TotalCount: 主机数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Machines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMaliciousRequestsRequest(AbstractModel):
    """DescribeMaliciousRequests请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | TRUSTED：已信任 | UN_TRUSTED：已取消信任）</li>
<li>Domain - String - 是否必填：否 - 恶意请求的域名</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        :param Uuid: 云镜客户端唯一UUID。
        :type Uuid: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Uuid = params.get("Uuid")


class DescribeMaliciousRequestsResponse(AbstractModel):
    """DescribeMaliciousRequests返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param MaliciousRequests: 恶意请求记录数组。
        :type MaliciousRequests: list of MaliciousRequest
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MaliciousRequests = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MaliciousRequests") is not None:
            self.MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = MaliciousRequest()
                obj._deserialize(item)
                self.MaliciousRequests.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMalwaresRequest(AbstractModel):
    """DescribeMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 木马状态（UN_OPERATED: 未处理 | SEGREGATED: 已隔离|TRUSTED：信任）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询。
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeMalwaresResponse(AbstractModel):
    """DescribeMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 木马总数。
        :type TotalCount: int
        :param Malwares: Malware数组。
        :type Malwares: list of Malware
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Malwares = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = Malware()
                obj._deserialize(item)
                self.Malwares.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 -  查询关键字</li>
<li>Status - String - 是否必填：否 -  登录状态（NON_LOCAL_LOGIN: 异地登录 | NORMAL_LOGIN : 正常登录）</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param NonLocalLoginPlaces: 异地登录信息数组。
        :type NonLocalLoginPlaces: list of NonLocalLoginPlace
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NonLocalLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = NonLocalLoginPlace()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortStatisticsRequest(AbstractModel):
    """DescribeOpenPortStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 端口统计列表总数
        :type TotalCount: int
        :param OpenPortStatistics: 端口统计数据列表
        :type OpenPortStatistics: list of OpenPortStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OpenPortStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPortStatistics") is not None:
            self.OpenPortStatistics = []
            for item in params.get("OpenPortStatistics"):
                obj = OpenPortStatistics()
                obj._deserialize(item)
                self.OpenPortStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortTaskStatusRequest(AbstractModel):
    """DescribeOpenPortTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeOpenPortTaskStatusResponse(AbstractModel):
    """DescribeOpenPortTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态。
<li>COMPLETE：完成（此时可以调用DescribeOpenPorts接口获取实时进程列表）</li>
<li>AGENT_OFFLINE：云镜客户端离线</li>
<li>COLLECTING：端口获取中</li>
<li>FAILED：进程获取失败</li>
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeOpenPortsRequest(AbstractModel):
    """DescribeOpenPorts请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Port和Uuid必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param Port: 开放端口号。Port和Uuid必填其一，使用Port表示查询该端口的列表信息。
        :type Port: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
<li>ProcessName - String - 是否必填：否 - 进程名</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Port = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Port = params.get("Port")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeOpenPortsResponse(AbstractModel):
    """DescribeOpenPorts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 端口列表记录总数。
        :type TotalCount: int
        :param OpenPorts: 端口列表。
        :type OpenPorts: list of OpenPort
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OpenPorts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPorts") is not None:
            self.OpenPorts = []
            for item in params.get("OpenPorts"):
                obj = OpenPort()
                obj._deserialize(item)
                self.OpenPorts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewStatisticsRequest(AbstractModel):
    """DescribeOverviewStatistics请求参数结构体

    """


class DescribeOverviewStatisticsResponse(AbstractModel):
    """DescribeOverviewStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param OnlineMachineNum: 服务器在线数。
        :type OnlineMachineNum: int
        :param ProVersionMachineNum: 专业服务器数。
        :type ProVersionMachineNum: int
        :param MalwareNum: 木马文件数。
        :type MalwareNum: int
        :param NonlocalLoginNum: 异地登录数。
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: 暴力破解成功数。
        :type BruteAttackSuccessNum: int
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param BaseLineNum: 安全基线数。
        :type BaseLineNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OnlineMachineNum = None
        self.ProVersionMachineNum = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.BaseLineNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.BaseLineNum = params.get("BaseLineNum")
        self.RequestId = params.get("RequestId")


class DescribePrivilegeEventsRequest(AbstractModel):
    """DescribePrivilegeEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键词(主机IP)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribePrivilegeEventsResponse(AbstractModel):
    """DescribePrivilegeEvents返回参数结构体

    """

    def __init__(self):
        """
        :param List: 数据列表
        :type List: list of PrivilegeEscalationProcess
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PrivilegeEscalationProcess()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePrivilegeRulesRequest(AbstractModel):
    """DescribePrivilegeRules请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(进程名称)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribePrivilegeRulesResponse(AbstractModel):
    """DescribePrivilegeRules返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表内容
        :type List: list of PrivilegeRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PrivilegeRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo请求参数结构体

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo返回参数结构体

    """

    def __init__(self):
        """
        :param PostPayCost: 后付费昨日扣费
        :type PostPayCost: int
        :param IsAutoOpenProVersion: 新增主机是否自动开通专业版
        :type IsAutoOpenProVersion: bool
        :param ProVersionNum: 开通专业版主机数
        :type ProVersionNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PostPayCost = None
        self.IsAutoOpenProVersion = None
        self.ProVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PostPayCost = params.get("PostPayCost")
        self.IsAutoOpenProVersion = params.get("IsAutoOpenProVersion")
        self.ProVersionNum = params.get("ProVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeProcessStatisticsRequest(AbstractModel):
    """DescribeProcessStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ProcessName - String - 是否必填：否 - 进程名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 进程统计列表记录总数。
        :type TotalCount: int
        :param ProcessStatistics: 进程统计列表数据数组。
        :type ProcessStatistics: list of ProcessStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProcessStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcessStatistics") is not None:
            self.ProcessStatistics = []
            for item in params.get("ProcessStatistics"):
                obj = ProcessStatistics()
                obj._deserialize(item)
                self.ProcessStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProcessTaskStatusRequest(AbstractModel):
    """DescribeProcessTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeProcessTaskStatusResponse(AbstractModel):
    """DescribeProcessTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态。
<li>COMPLETE：完成（此时可以调用DescribeProcesses接口获取实时进程列表）</li>
<li>AGENT_OFFLINE：云镜客户端离线</li>
<li>COLLECTING：进程获取中</li>
<li>FAILED：进程获取失败</li>
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeProcessesRequest(AbstractModel):
    """DescribeProcesses请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Uuid和ProcessName必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param ProcessName: 进程名。Uuid和ProcessName必填其一，使用ProcessName表示，查询该进程列表信息。
        :type ProcessName: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ProcessName - String - 是否必填：否 - 进程名</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.ProcessName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeProcessesResponse(AbstractModel):
    """DescribeProcesses返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 进程列表记录总数。
        :type TotalCount: int
        :param Processes: 进程列表数据数组。
        :type Processes: list of Process
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Processes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Processes") is not None:
            self.Processes = []
            for item in params.get("Processes"):
                obj = Process()
                obj._deserialize(item)
                self.Processes.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReverseShellEventsRequest(AbstractModel):
    """DescribeReverseShellEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(主机内网IP|进程名)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeReverseShellEventsResponse(AbstractModel):
    """DescribeReverseShellEvents返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表内容
        :type List: list of ReverseShell
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ReverseShell()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeReverseShellRulesRequest(AbstractModel):
    """DescribeReverseShellRules请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(进程名称)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeReverseShellRulesResponse(AbstractModel):
    """DescribeReverseShellRules返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表内容
        :type List: list of ReverseShellRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ReverseShellRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityDynamicsRequest(AbstractModel):
    """DescribeSecurityDynamics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityDynamics: 安全事件消息数组。
        :type SecurityDynamics: list of SecurityDynamic
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityDynamics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityDynamics") is not None:
            self.SecurityDynamics = []
            for item in params.get("SecurityDynamics"):
                obj = SecurityDynamic()
                obj._deserialize(item)
                self.SecurityDynamics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityTrendsRequest(AbstractModel):
    """DescribeSecurityTrends请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 开始时间。
        :type BeginDate: str
        :param EndDate: 结束时间。
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends返回参数结构体

    """

    def __init__(self):
        """
        :param Malwares: 木马事件统计数据数组。
        :type Malwares: list of SecurityTrend
        :param NonLocalLoginPlaces: 异地登录事件统计数据数组。
        :type NonLocalLoginPlaces: list of SecurityTrend
        :param BruteAttacks: 密码破解事件统计数据数组。
        :type BruteAttacks: list of SecurityTrend
        :param Vuls: 漏洞统计数据数组。
        :type Vuls: list of SecurityTrend
        :param BaseLines: 基线统计数据数组。
        :type BaseLines: list of SecurityTrend
        :param MaliciousRequests: 恶意请求统计数据数组。
        :type MaliciousRequests: list of SecurityTrend
        :param HighRiskBashs: 高危命令统计数据数组。
        :type HighRiskBashs: list of SecurityTrend
        :param ReverseShells: 反弹shell统计数据数组。
        :type ReverseShells: list of SecurityTrend
        :param PrivilegeEscalations: 本地提权统计数据数组。
        :type PrivilegeEscalations: list of SecurityTrend
        :param CyberAttacks: 网络攻击统计数据数组。
        :type CyberAttacks: list of SecurityTrend
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Malwares = None
        self.NonLocalLoginPlaces = None
        self.BruteAttacks = None
        self.Vuls = None
        self.BaseLines = None
        self.MaliciousRequests = None
        self.HighRiskBashs = None
        self.ReverseShells = None
        self.PrivilegeEscalations = None
        self.CyberAttacks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Malwares.append(obj)
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Vuls.append(obj)
        if params.get("BaseLines") is not None:
            self.BaseLines = []
            for item in params.get("BaseLines"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BaseLines.append(obj)
        if params.get("MaliciousRequests") is not None:
            self.MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.MaliciousRequests.append(obj)
        if params.get("HighRiskBashs") is not None:
            self.HighRiskBashs = []
            for item in params.get("HighRiskBashs"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.HighRiskBashs.append(obj)
        if params.get("ReverseShells") is not None:
            self.ReverseShells = []
            for item in params.get("ReverseShells"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.ReverseShells.append(obj)
        if params.get("PrivilegeEscalations") is not None:
            self.PrivilegeEscalations = []
            for item in params.get("PrivilegeEscalations"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.PrivilegeEscalations.append(obj)
        if params.get("CyberAttacks") is not None:
            self.CyberAttacks = []
            for item in params.get("CyberAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.CyberAttacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagMachinesRequest(AbstractModel):
    """DescribeTagMachines请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 标签ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DescribeTagMachinesResponse(AbstractModel):
    """DescribeTagMachines返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表数据
        :type List: list of TagMachine
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = TagMachine()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        """
        self.MachineType = None
        self.MachineRegion = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表信息
        :type List: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Tag()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsualLoginPlacesRequest(AbstractModel):
    """DescribeUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端UUID
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param UsualLoginPlaces: 常用登录地数组
        :type UsualLoginPlaces: list of UsualPlace
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UsualLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UsualLoginPlaces") is not None:
            self.UsualLoginPlaces = []
            for item in params.get("UsualLoginPlaces"):
                obj = UsualPlace()
                obj._deserialize(item)
                self.UsualLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulInfoRequest(AbstractModel):
    """DescribeVulInfo请求参数结构体

    """

    def __init__(self):
        """
        :param VulId: 漏洞种类ID。
        :type VulId: int
        """
        self.VulId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")


class DescribeVulInfoResponse(AbstractModel):
    """DescribeVulInfo返回参数结构体

    """

    def __init__(self):
        """
        :param VulId: 漏洞种类ID。
        :type VulId: int
        :param VulName: 漏洞名称。
        :type VulName: str
        :param VulLevel: 漏洞等级。
        :type VulLevel: str
        :param VulType: 漏洞类型。
        :type VulType: str
        :param Description: 漏洞描述。
        :type Description: str
        :param RepairPlan: 修复方案。
        :type RepairPlan: str
        :param CveId: 漏洞CVE。
        :type CveId: str
        :param Reference: 参考链接。
        :type Reference: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.VulType = None
        self.Description = None
        self.RepairPlan = None
        self.CveId = None
        self.Reference = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.RepairPlan = params.get("RepairPlan")
        self.CveId = params.get("CveId")
        self.Reference = params.get("Reference")
        self.RequestId = params.get("RequestId")


class DescribeVulScanResultRequest(AbstractModel):
    """DescribeVulScanResult请求参数结构体

    """


class DescribeVulScanResultResponse(AbstractModel):
    """DescribeVulScanResult返回参数结构体

    """

    def __init__(self):
        """
        :param VulNum: 漏洞数量。
        :type VulNum: int
        :param ProVersionNum: 专业版机器数。
        :type ProVersionNum: int
        :param ImpactedHostNum: 受影响的专业版主机数。
        :type ImpactedHostNum: int
        :param HostNum: 主机总数。
        :type HostNum: int
        :param BasicVersionNum: 基础版机器数。
        :type BasicVersionNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulNum = None
        self.ProVersionNum = None
        self.ImpactedHostNum = None
        self.HostNum = None
        self.BasicVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulNum = params.get("VulNum")
        self.ProVersionNum = params.get("ProVersionNum")
        self.ImpactedHostNum = params.get("ImpactedHostNum")
        self.HostNum = params.get("HostNum")
        self.BasicVersionNum = params.get("BasicVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls请求参数结构体

    """

    def __init__(self):
        """
        :param VulType: 漏洞类型。
<li>WEB：Web应用漏洞</li>
<li>SYSTEM：系统组件漏洞</li>
<li>BASELINE：安全基线</li>
        :type VulType: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | FIXED：已修复）

Status过滤条件值只能取其一，不能是“或”逻辑。
        :type Filters: list of Filter
        """
        self.VulType = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 漏洞数量。
        :type TotalCount: int
        :param Vuls: 漏洞列表数组。
        :type Vuls: list of Vul
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Vuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self.Vuls.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportBruteAttacksRequest(AbstractModel):
    """DescribeWeeklyReportBruteAttacks请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportBruteAttacksResponse(AbstractModel):
    """DescribeWeeklyReportBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReportBruteAttacks: 专业周报密码破解数组。
        :type WeeklyReportBruteAttacks: list of WeeklyReportBruteAttack
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportBruteAttacks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportBruteAttacks") is not None:
            self.WeeklyReportBruteAttacks = []
            for item in params.get("WeeklyReportBruteAttacks"):
                obj = WeeklyReportBruteAttack()
                obj._deserialize(item)
                self.WeeklyReportBruteAttacks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportInfoRequest(AbstractModel):
    """DescribeWeeklyReportInfo请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业周报开始时间。
        :type BeginDate: str
        """
        self.BeginDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")


class DescribeWeeklyReportInfoResponse(AbstractModel):
    """DescribeWeeklyReportInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyName: 账号所属公司或个人名称。
        :type CompanyName: str
        :param MachineNum: 机器总数。
        :type MachineNum: int
        :param OnlineMachineNum: 云镜客户端在线数。
        :type OnlineMachineNum: int
        :param OfflineMachineNum: 云镜客户端离线数。
        :type OfflineMachineNum: int
        :param ProVersionMachineNum: 开通云镜专业版数量。
        :type ProVersionMachineNum: int
        :param BeginDate: 周报开始时间。
        :type BeginDate: str
        :param EndDate: 周报结束时间。
        :type EndDate: str
        :param Level: 安全等级。
<li>HIGH：高</li>
<li>MIDDLE：中</li>
<li>LOW：低</li>
        :type Level: str
        :param MalwareNum: 木马记录数。
        :type MalwareNum: int
        :param NonlocalLoginNum: 异地登录数。
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: 密码破解成功数。
        :type BruteAttackSuccessNum: int
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param DownloadUrl: 导出文件下载地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyName = None
        self.MachineNum = None
        self.OnlineMachineNum = None
        self.OfflineMachineNum = None
        self.ProVersionMachineNum = None
        self.BeginDate = None
        self.EndDate = None
        self.Level = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.MachineNum = params.get("MachineNum")
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.OfflineMachineNum = params.get("OfflineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.Level = params.get("Level")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportMalwaresRequest(AbstractModel):
    """DescribeWeeklyReportMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportMalwaresResponse(AbstractModel):
    """DescribeWeeklyReportMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReportMalwares: 专业周报木马数据。
        :type WeeklyReportMalwares: list of WeeklyReportMalware
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportMalwares = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportMalwares") is not None:
            self.WeeklyReportMalwares = []
            for item in params.get("WeeklyReportMalwares"):
                obj = WeeklyReportMalware()
                obj._deserialize(item)
                self.WeeklyReportMalwares.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReportNonlocalLoginPlaces: 专业周报异地登录数据。
        :type WeeklyReportNonlocalLoginPlaces: list of WeeklyReportNonlocalLoginPlace
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportNonlocalLoginPlaces = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportNonlocalLoginPlaces") is not None:
            self.WeeklyReportNonlocalLoginPlaces = []
            for item in params.get("WeeklyReportNonlocalLoginPlaces"):
                obj = WeeklyReportNonlocalLoginPlace()
                obj._deserialize(item)
                self.WeeklyReportNonlocalLoginPlaces.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportVulsRequest(AbstractModel):
    """DescribeWeeklyReportVuls请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 专业版周报开始时间。
        :type BeginDate: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportVulsResponse(AbstractModel):
    """DescribeWeeklyReportVuls返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReportVuls: 专业周报漏洞数据数组。
        :type WeeklyReportVuls: list of WeeklyReportVul
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportVuls = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportVuls") is not None:
            self.WeeklyReportVuls = []
            for item in params.get("WeeklyReportVuls"):
                obj = WeeklyReportVul()
                obj._deserialize(item)
                self.WeeklyReportVuls.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportsRequest(AbstractModel):
    """DescribeWeeklyReports请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportsResponse(AbstractModel):
    """DescribeWeeklyReports返回参数结构体

    """

    def __init__(self):
        """
        :param WeeklyReports: 专业周报列表数组。
        :type WeeklyReports: list of WeeklyReport
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReports = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReports") is not None:
            self.WeeklyReports = []
            for item in params.get("WeeklyReports"):
                obj = WeeklyReport()
                obj._deserialize(item)
                self.WeeklyReports.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class EditBashRuleRequest(AbstractModel):
    """EditBashRule请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 规则名称
        :type Name: str
        :param Level: 危险等级(1: 高危 2:中危 3: 低危)
        :type Level: int
        :param Rule: 正则表达式
        :type Rule: str
        :param Id: 规则ID(新增时不填)
        :type Id: int
        :param Uuid: 客户端ID(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Uuid: str
        :param Hostip: 主机IP(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Hostip: str
        :param IsGlobal: 是否全局规则(默认否)
        :type IsGlobal: int
        """
        self.Name = None
        self.Level = None
        self.Rule = None
        self.Id = None
        self.Uuid = None
        self.Hostip = None
        self.IsGlobal = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Rule = params.get("Rule")
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Hostip = params.get("Hostip")
        self.IsGlobal = params.get("IsGlobal")


class EditBashRuleResponse(AbstractModel):
    """EditBashRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditPrivilegeRuleRequest(AbstractModel):
    """EditPrivilegeRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 规则ID(新增时请留空)
        :type Id: int
        :param Uuid: 客户端ID(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Uuid: str
        :param Hostip: 主机IP(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Hostip: str
        :param ProcessName: 进程名
        :type ProcessName: str
        :param SMode: 是否S权限进程
        :type SMode: int
        :param IsGlobal: 是否全局规则(默认否)
        :type IsGlobal: int
        """
        self.Id = None
        self.Uuid = None
        self.Hostip = None
        self.ProcessName = None
        self.SMode = None
        self.IsGlobal = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Hostip = params.get("Hostip")
        self.ProcessName = params.get("ProcessName")
        self.SMode = params.get("SMode")
        self.IsGlobal = params.get("IsGlobal")


class EditPrivilegeRuleResponse(AbstractModel):
    """EditPrivilegeRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditReverseShellRuleRequest(AbstractModel):
    """EditReverseShellRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 规则ID(新增时请留空)
        :type Id: int
        :param Uuid: 客户端ID(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Uuid: str
        :param Hostip: 主机IP(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Hostip: str
        :param DestIp: 目标IP
        :type DestIp: str
        :param DestPort: 目标端口
        :type DestPort: str
        :param ProcessName: 进程名
        :type ProcessName: str
        :param IsGlobal: 是否全局规则(默认否)
        :type IsGlobal: int
        """
        self.Id = None
        self.Uuid = None
        self.Hostip = None
        self.DestIp = None
        self.DestPort = None
        self.ProcessName = None
        self.IsGlobal = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Hostip = params.get("Hostip")
        self.DestIp = params.get("DestIp")
        self.DestPort = params.get("DestPort")
        self.ProcessName = params.get("ProcessName")
        self.IsGlobal = params.get("IsGlobal")


class EditReverseShellRuleResponse(AbstractModel):
    """EditReverseShellRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditTagsRequest(AbstractModel):
    """EditTags请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 标签名
        :type Name: str
        :param Id: 标签ID
        :type Id: int
        :param Quuids: CVM主机ID
        :type Quuids: list of str
        """
        self.Name = None
        self.Id = None
        self.Quuids = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.Quuids = params.get("Quuids")


class EditTagsResponse(AbstractModel):
    """EditTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExportAttackLogsRequest(AbstractModel):
    """ExportAttackLogs请求参数结构体

    """


class ExportAttackLogsResponse(AbstractModel):
    """ExportAttackLogs返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportBashEventsRequest(AbstractModel):
    """ExportBashEvents请求参数结构体

    """


class ExportBashEventsResponse(AbstractModel):
    """ExportBashEvents返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportBruteAttacksRequest(AbstractModel):
    """ExportBruteAttacks请求参数结构体

    """


class ExportBruteAttacksResponse(AbstractModel):
    """ExportBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportMaliciousRequestsRequest(AbstractModel):
    """ExportMaliciousRequests请求参数结构体

    """


class ExportMaliciousRequestsResponse(AbstractModel):
    """ExportMaliciousRequests返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportMalwaresRequest(AbstractModel):
    """ExportMalwares请求参数结构体

    """


class ExportMalwaresResponse(AbstractModel):
    """ExportMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportNonlocalLoginPlacesRequest(AbstractModel):
    """ExportNonlocalLoginPlaces请求参数结构体

    """


class ExportNonlocalLoginPlacesResponse(AbstractModel):
    """ExportNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportPrivilegeEventsRequest(AbstractModel):
    """ExportPrivilegeEvents请求参数结构体

    """


class ExportPrivilegeEventsResponse(AbstractModel):
    """ExportPrivilegeEvents返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportReverseShellEventsRequest(AbstractModel):
    """ExportReverseShellEvents请求参数结构体

    """


class ExportReverseShellEventsResponse(AbstractModel):
    """ExportReverseShellEvents返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    * 最多只能有5个Filter
    * 同一个Filter存在多个Values，Values值数量最多不能超过5个。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class HistoryAccount(AbstractModel):
    """账号变更历史数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param Username: 帐号名。
        :type Username: str
        :param ModifyType: 帐号变更类型。
<li>CREATE：表示新增帐号</li>
<li>MODIFY：表示修改帐号</li>
<li>DELETE：表示删除帐号</li>
        :type ModifyType: str
        :param ModifyTime: 变更时间。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.ModifyType = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.ModifyType = params.get("ModifyType")
        self.ModifyTime = params.get("ModifyTime")


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 漏洞ID数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImpactedHost(AbstractModel):
    """受影响主机信息

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param LastScanTime: 最后检测时间。
        :type LastScanTime: str
        :param VulStatus: 漏洞状态。
<li>UN_OPERATED ：待处理</li>
<li>SCANING : 扫描中</li>
<li>FIXED : 已修复</li>
        :type VulStatus: str
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulId: 漏洞种类ID。
        :type VulId: int
        :param IsProVersion: 是否为专业版。
        :type IsProVersion: bool
        """
        self.Id = None
        self.MachineIp = None
        self.MachineName = None
        self.LastScanTime = None
        self.VulStatus = None
        self.Uuid = None
        self.Description = None
        self.VulId = None
        self.IsProVersion = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.LastScanTime = params.get("LastScanTime")
        self.VulStatus = params.get("VulStatus")
        self.Uuid = params.get("Uuid")
        self.Description = params.get("Description")
        self.VulId = params.get("VulId")
        self.IsProVersion = params.get("IsProVersion")


class InquiryPriceOpenProVersionPrepaidRequest(AbstractModel):
    """InquiryPriceOpenProVersionPrepaid请求参数结构体

    """

    def __init__(self):
        """
        :param ChargePrepaid: 预付费模式(包年包月)参数设置。
        :type ChargePrepaid: :class:`tencentcloud.cwp.v20180228.models.ChargePrepaid`
        :param Machines: 需要开通专业版机器列表数组。
        :type Machines: list of ProVersionMachine
        """
        self.ChargePrepaid = None
        self.Machines = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = ProVersionMachine()
                obj._deserialize(item)
                self.Machines.append(obj)


class InquiryPriceOpenProVersionPrepaidResponse(AbstractModel):
    """InquiryPriceOpenProVersionPrepaid返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 预支费用的原价，单位：元。
        :type OriginalPrice: float
        :param DiscountPrice: 预支费用的折扣价，单位：元。
        :type DiscountPrice: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.RequestId = params.get("RequestId")


class LoginWhiteLists(AbstractModel):
    """异地登录白名单

    """

    def __init__(self):
        """
        :param Id: 记录ID
        :type Id: int
        :param Uuid: 云镜客户端ID
        :type Uuid: str
        :param Places: 白名单地域
        :type Places: list of Place
        :param UserName: 白名单用户（多个用户逗号隔开）
        :type UserName: str
        :param SrcIp: 白名单IP（多个IP逗号隔开）
        :type SrcIp: str
        :param IsGlobal: 是否为全局规则
        :type IsGlobal: bool
        :param CreateTime: 创建白名单时间
        :type CreateTime: str
        :param ModifyTime: 修改白名单时间
        :type ModifyTime: str
        :param MachineName: 机器名
        :type MachineName: str
        :param HostIp: 机器IP
        :type HostIp: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.Id = None
        self.Uuid = None
        self.Places = None
        self.UserName = None
        self.SrcIp = None
        self.IsGlobal = None
        self.CreateTime = None
        self.ModifyTime = None
        self.MachineName = None
        self.HostIp = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)
        self.UserName = params.get("UserName")
        self.SrcIp = params.get("SrcIp")
        self.IsGlobal = params.get("IsGlobal")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.MachineName = params.get("MachineName")
        self.HostIp = params.get("HostIp")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class LoginWhiteListsRule(AbstractModel):
    """白名单规则

    """

    def __init__(self):
        """
        :param Places: 加白地域
        :type Places: list of Place
        :param SrcIp: 加白源IP，支持网段，多个IP以逗号隔开
        :type SrcIp: str
        :param UserName: 加白用户名，多个用户名以逗号隔开
        :type UserName: str
        :param IsGlobal: 是否对全局生效
        :type IsGlobal: bool
        :param HostIp: 白名单生效的机器
        :type HostIp: str
        :param Id: 规则ID，用于更新规则
        :type Id: int
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.Places = None
        self.SrcIp = None
        self.UserName = None
        self.IsGlobal = None
        self.HostIp = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)
        self.SrcIp = params.get("SrcIp")
        self.UserName = params.get("UserName")
        self.IsGlobal = params.get("IsGlobal")
        self.HostIp = params.get("HostIp")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class Machine(AbstractModel):
    """主机列表

    """

    def __init__(self):
        """
        :param MachineName: 主机名称。
        :type MachineName: str
        :param MachineOs: 主机系统。
        :type MachineOs: str
        :param MachineStatus: 主机状态。
<li>OFFLINE: 离线  </li>
<li>ONLINE: 在线</li>
<li>MACHINE_STOPPED: 已关机</li>
        :type MachineStatus: str
        :param Uuid: 云镜客户端唯一Uuid，若客户端长时间不在线将返回空字符。
        :type Uuid: str
        :param Quuid: CVM或BM机器唯一Uuid。
        :type Quuid: str
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param IsProVersion: 是否是专业版。
<li>true： 是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param MalwareNum: 木马数。
        :type MalwareNum: int
        :param Tag: 标签信息
        :type Tag: list of MachineTag
        :param BaselineNum: 基线风险数。
        :type BaselineNum: int
        :param CyberAttackNum: 网络风险数。
        :type CyberAttackNum: int
        :param SecurityStatus: 风险状态。
<li>SAFE：安全</li>
<li>RISK：风险</li>
<li>UNKNOWN：未知</li>
        :type SecurityStatus: str
        :param InvasionNum: 入侵事件数
        :type InvasionNum: int
        :param RegionInfo: 地域信息
        :type RegionInfo: :class:`tencentcloud.cwp.v20180228.models.RegionInfo`
        """
        self.MachineName = None
        self.MachineOs = None
        self.MachineStatus = None
        self.Uuid = None
        self.Quuid = None
        self.VulNum = None
        self.MachineIp = None
        self.IsProVersion = None
        self.MachineWanIp = None
        self.PayMode = None
        self.MalwareNum = None
        self.Tag = None
        self.BaselineNum = None
        self.CyberAttackNum = None
        self.SecurityStatus = None
        self.InvasionNum = None
        self.RegionInfo = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachineOs = params.get("MachineOs")
        self.MachineStatus = params.get("MachineStatus")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.VulNum = params.get("VulNum")
        self.MachineIp = params.get("MachineIp")
        self.IsProVersion = params.get("IsProVersion")
        self.MachineWanIp = params.get("MachineWanIp")
        self.PayMode = params.get("PayMode")
        self.MalwareNum = params.get("MalwareNum")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.BaselineNum = params.get("BaselineNum")
        self.CyberAttackNum = params.get("CyberAttackNum")
        self.SecurityStatus = params.get("SecurityStatus")
        self.InvasionNum = params.get("InvasionNum")
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))


class MachineTag(AbstractModel):
    """服务器标签信息

    """

    def __init__(self):
        """
        :param Rid: 关联标签ID
        :type Rid: int
        :param Name: 标签名
        :type Name: str
        :param TagId: 标签ID
        :type TagId: int
        """
        self.Rid = None
        self.Name = None
        self.TagId = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")
        self.Name = params.get("Name")
        self.TagId = params.get("TagId")


class MaliciousRequest(AbstractModel):
    """恶意请求数据。

    """

    def __init__(self):
        """
        :param Id: 记录ID。
        :type Id: int
        :param Uuid: 云镜客户端UUID。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param Domain: 恶意请求域名。
        :type Domain: str
        :param Count: 恶意请求数。
        :type Count: int
        :param ProcessName: 进程名。
        :type ProcessName: str
        :param Status: 记录状态。
<li>UN_OPERATED：待处理</li>
<li>TRUSTED：已信任</li>
<li>UN_TRUSTED：已取消信任</li>
        :type Status: str
        :param Description: 恶意请求域名描述。
        :type Description: str
        :param Reference: 参考地址。
        :type Reference: str
        :param CreateTime: 发现时间。
        :type CreateTime: str
        :param MergeTime: 记录合并时间。
        :type MergeTime: str
        :param ProcessMd5: 进程MD5
值。
        :type ProcessMd5: str
        :param CmdLine: 执行命令行。
        :type CmdLine: str
        :param Pid: 进程PID。
        :type Pid: int
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Domain = None
        self.Count = None
        self.ProcessName = None
        self.Status = None
        self.Description = None
        self.Reference = None
        self.CreateTime = None
        self.MergeTime = None
        self.ProcessMd5 = None
        self.CmdLine = None
        self.Pid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Domain = params.get("Domain")
        self.Count = params.get("Count")
        self.ProcessName = params.get("ProcessName")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Reference = params.get("Reference")
        self.CreateTime = params.get("CreateTime")
        self.MergeTime = params.get("MergeTime")
        self.ProcessMd5 = params.get("ProcessMd5")
        self.CmdLine = params.get("CmdLine")
        self.Pid = params.get("Pid")


class Malware(AbstractModel):
    """木马相关信息

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Status: 当前木马状态。
<li>UN_OPERATED：未处理</li><li>SEGREGATED：已隔离</li><li>TRUSTED：已信任</li>
<li>SEPARATING：隔离中</li><li>RECOVERING：恢复中</li>
        :type Status: str
        :param FilePath: 木马所在的路径。
        :type FilePath: str
        :param Description: 木马描述。
        :type Description: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param FileCreateTime: 木马文件创建时间。
        :type FileCreateTime: str
        :param ModifyTime: 木马文件修改时间。
        :type ModifyTime: str
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.FilePath = None
        self.Description = None
        self.MachineName = None
        self.FileCreateTime = None
        self.ModifyTime = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.FilePath = params.get("FilePath")
        self.Description = params.get("Description")
        self.MachineName = params.get("MachineName")
        self.FileCreateTime = params.get("FileCreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Uuid = params.get("Uuid")


class MisAlarmNonlocalLoginPlacesRequest(AbstractModel):
    """MisAlarmNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 异地登录事件Id数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class MisAlarmNonlocalLoginPlacesResponse(AbstractModel):
    """MisAlarmNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmAttributeRequest(AbstractModel):
    """ModifyAlarmAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param Attribute: 告警项目。
<li>Offline：防护软件离线</li>
<li>Malware：发现木马文件</li>
<li>NonlocalLogin：发现异地登录行为</li>
<li>CrackSuccess：被暴力破解成功</li>
        :type Attribute: str
        :param Value: 告警项目属性。
<li>CLOSE：关闭</li>
<li>OPEN：打开</li>
        :type Value: str
        """
        self.Attribute = None
        self.Value = None


    def _deserialize(self, params):
        self.Attribute = params.get("Attribute")
        self.Value = params.get("Value")


class ModifyAlarmAttributeResponse(AbstractModel):
    """ModifyAlarmAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAutoOpenProVersionConfigRequest(AbstractModel):
    """ModifyAutoOpenProVersionConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 设置自动开通状态。
<li>CLOSE：关闭</li>
<li>OPEN：打开</li>
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoginWhiteListRequest(AbstractModel):
    """ModifyLoginWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param Rules: 白名单规则
        :type Rules: :class:`tencentcloud.cwp.v20180228.models.LoginWhiteListsRule`
        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = LoginWhiteListsRule()
            self.Rules._deserialize(params.get("Rules"))


class ModifyLoginWhiteListResponse(AbstractModel):
    """ModifyLoginWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProVersionRenewFlagRequest(AbstractModel):
    """ModifyProVersionRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param RenewFlag: 自动续费标识。取值范围：
<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li>
        :type RenewFlag: str
        :param Quuid: 主机唯一ID，对应CVM的uuid、BM的instanceId。
        :type Quuid: str
        """
        self.RenewFlag = None
        self.Quuid = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Quuid = params.get("Quuid")


class ModifyProVersionRenewFlagResponse(AbstractModel):
    """ModifyProVersionRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NonLocalLoginPlace(AbstractModel):
    """异地登录

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Status: 登录状态
<li>NON_LOCAL_LOGIN：异地登录</li>
<li>NORMAL_LOGIN：正常登录</li>
        :type Status: str
        :param UserName: 用户名。
        :type UserName: str
        :param City: 城市ID。
        :type City: int
        :param Country: 国家ID。
        :type Country: int
        :param Province: 省份ID。
        :type Province: int
        :param SrcIp: 登录IP。
        :type SrcIp: str
        :param MachineName: 机器名称。
        :type MachineName: str
        :param LoginTime: 登录时间。
        :type LoginTime: str
        :param Uuid: 云镜客户端唯一标识Uuid。
        :type Uuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.UserName = None
        self.City = None
        self.Country = None
        self.Province = None
        self.SrcIp = None
        self.MachineName = None
        self.LoginTime = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.UserName = params.get("UserName")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.SrcIp = params.get("SrcIp")
        self.MachineName = params.get("MachineName")
        self.LoginTime = params.get("LoginTime")
        self.Uuid = params.get("Uuid")


class OpenPort(AbstractModel):
    """端口列表

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一UUID。
        :type Uuid: str
        :param Port: 开放端口号。
        :type Port: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param ProcessName: 端口对应进程名。
        :type ProcessName: str
        :param Pid: 端口对应进程Pid。
        :type Pid: int
        :param CreateTime: 记录创建时间。
        :type CreateTime: str
        :param ModifyTime: 记录更新时间。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.Port = None
        self.MachineIp = None
        self.MachineName = None
        self.ProcessName = None
        self.Pid = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Port = params.get("Port")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.ProcessName = params.get("ProcessName")
        self.Pid = params.get("Pid")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")


class OpenPortStatistics(AbstractModel):
    """端口统计列表

    """

    def __init__(self):
        """
        :param Port: 端口号
        :type Port: int
        :param MachineNum: 主机数量
        :type MachineNum: int
        """
        self.Port = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.MachineNum = params.get("MachineNum")


class OpenProVersionPrepaidRequest(AbstractModel):
    """OpenProVersionPrepaid请求参数结构体

    """

    def __init__(self):
        """
        :param ChargePrepaid: 购买相关参数。
        :type ChargePrepaid: :class:`tencentcloud.cwp.v20180228.models.ChargePrepaid`
        :param Machines: 需要开通专业版主机信息数组。
        :type Machines: list of ProVersionMachine
        """
        self.ChargePrepaid = None
        self.Machines = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = ProVersionMachine()
                obj._deserialize(item)
                self.Machines.append(obj)


class OpenProVersionPrepaidResponse(AbstractModel):
    """OpenProVersionPrepaid返回参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 订单ID列表。
        :type DealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.RequestId = params.get("RequestId")


class OpenProVersionRequest(AbstractModel):
    """OpenProVersion请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。
如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Quuids: 主机唯一标识Uuid数组。
黑石的InstanceId，CVM的Uuid
        :type Quuids: list of str
        :param ActivityId: 活动ID。
        :type ActivityId: int
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Quuids = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Quuids = params.get("Quuids")
        self.ActivityId = params.get("ActivityId")


class OpenProVersionResponse(AbstractModel):
    """OpenProVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Place(AbstractModel):
    """登录地信息

    """

    def __init__(self):
        """
        :param CityId: 城市 ID。
        :type CityId: int
        :param ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param CountryId: 国家ID，暂只支持国内：1。
        :type CountryId: int
        """
        self.CityId = None
        self.ProvinceId = None
        self.CountryId = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.ProvinceId = params.get("ProvinceId")
        self.CountryId = params.get("CountryId")


class PrivilegeEscalationProcess(AbstractModel):
    """本地提权数据

    """

    def __init__(self):
        """
        :param Id: 数据ID
        :type Id: int
        :param Uuid: 云镜ID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param ProcessName: 进程名
        :type ProcessName: str
        :param FullPath: 进程路径
        :type FullPath: str
        :param CmdLine: 执行命令
        :type CmdLine: str
        :param UserName: 用户名
        :type UserName: str
        :param UserGroup: 用户组
        :type UserGroup: str
        :param ProcFilePrivilege: 进程文件权限
        :type ProcFilePrivilege: str
        :param ParentProcName: 父进程名
        :type ParentProcName: str
        :param ParentProcUser: 父进程用户名
        :type ParentProcUser: str
        :param ParentProcGroup: 父进程用户组
        :type ParentProcGroup: str
        :param ParentProcPath: 父进程路径
        :type ParentProcPath: str
        :param ProcTree: 进程树
        :type ProcTree: str
        :param Status: 处理状态
        :type Status: int
        :param CreateTime: 发生时间
        :type CreateTime: str
        :param MachineName: 机器名
        :type MachineName: str
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.ProcessName = None
        self.FullPath = None
        self.CmdLine = None
        self.UserName = None
        self.UserGroup = None
        self.ProcFilePrivilege = None
        self.ParentProcName = None
        self.ParentProcUser = None
        self.ParentProcGroup = None
        self.ParentProcPath = None
        self.ProcTree = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.ProcessName = params.get("ProcessName")
        self.FullPath = params.get("FullPath")
        self.CmdLine = params.get("CmdLine")
        self.UserName = params.get("UserName")
        self.UserGroup = params.get("UserGroup")
        self.ProcFilePrivilege = params.get("ProcFilePrivilege")
        self.ParentProcName = params.get("ParentProcName")
        self.ParentProcUser = params.get("ParentProcUser")
        self.ParentProcGroup = params.get("ParentProcGroup")
        self.ParentProcPath = params.get("ParentProcPath")
        self.ProcTree = params.get("ProcTree")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")


class PrivilegeRule(AbstractModel):
    """本地提权规则

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param ProcessName: 进程名
        :type ProcessName: str
        :param SMode: 是否S权限
        :type SMode: int
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态(0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        """
        self.Id = None
        self.Uuid = None
        self.ProcessName = None
        self.SMode = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.SMode = params.get("SMode")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")


class ProVersionMachine(AbstractModel):
    """需要开通专业版机器信息。

    """

    def __init__(self):
        """
        :param MachineType: 主机类型。
<li>CVM: 虚拟主机</li>
<li>BM: 黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 主机所在地域。
如：ap-guangzhou、ap-beijing
        :type MachineRegion: str
        :param Quuid: 主机唯一标识Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Quuid = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Quuid = params.get("Quuid")


class Process(AbstractModel):
    """进程信息数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一UUID。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param Pid: 进程Pid。
        :type Pid: int
        :param Ppid: 进程Ppid。
        :type Ppid: int
        :param ProcessName: 进程名。
        :type ProcessName: str
        :param Username: 进程用户名。
        :type Username: str
        :param Platform: 所属平台。
<li>WIN32：windows32位</li>
<li>WIN64：windows64位</li>
<li>LINUX32：Linux32位</li>
<li>LINUX64：Linux64位</li>
        :type Platform: str
        :param FullPath: 进程路径。
        :type FullPath: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Pid = None
        self.Ppid = None
        self.ProcessName = None
        self.Username = None
        self.Platform = None
        self.FullPath = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Pid = params.get("Pid")
        self.Ppid = params.get("Ppid")
        self.ProcessName = params.get("ProcessName")
        self.Username = params.get("Username")
        self.Platform = params.get("Platform")
        self.FullPath = params.get("FullPath")
        self.CreateTime = params.get("CreateTime")


class ProcessStatistics(AbstractModel):
    """进程数据统计数据。

    """

    def __init__(self):
        """
        :param ProcessName: 进程名。
        :type ProcessName: str
        :param MachineNum: 主机数量。
        :type MachineNum: int
        """
        self.ProcessName = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.MachineNum = params.get("MachineNum")


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马Id数组,单次最大删除不能超过200条
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessIds: 恢复成功id数组
        :type SuccessIds: list of int non-negative
        :param FailedIds: 恢复失败id数组
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        """
        :param Region: 地域标志，如 ap-guangzhou，ap-shanghai，ap-beijing
        :type Region: str
        :param RegionName: 地域中文名，如华南地区（广州），华东地区（上海金融），华北地区（北京）
        :type RegionName: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param RegionCode: 地域代码，如 gz，sh，bj
        :type RegionCode: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionCode = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionCode = params.get("RegionCode")


class RenewProVersionRequest(AbstractModel):
    """RenewProVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ChargePrepaid: 购买相关参数。
        :type ChargePrepaid: :class:`tencentcloud.cwp.v20180228.models.ChargePrepaid`
        :param Quuid: 主机唯一ID，对应CVM的uuid、BM的InstanceId。
        :type Quuid: str
        """
        self.ChargePrepaid = None
        self.Quuid = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        self.Quuid = params.get("Quuid")


class RenewProVersionResponse(AbstractModel):
    """RenewProVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RescanImpactedHostRequest(AbstractModel):
    """RescanImpactedHost请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class RescanImpactedHostResponse(AbstractModel):
    """RescanImpactedHost返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReverseShell(AbstractModel):
    """反弹Shell数据

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: int
        :param Uuid: 云镜UUID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param DstIp: 目标IP
        :type DstIp: str
        :param DstPort: 目标端口
        :type DstPort: int
        :param ProcessName: 进程名
        :type ProcessName: str
        :param FullPath: 进程路径
        :type FullPath: str
        :param CmdLine: 命令详情
        :type CmdLine: str
        :param UserName: 执行用户
        :type UserName: str
        :param UserGroup: 执行用户组
        :type UserGroup: str
        :param ParentProcName: 父进程名
        :type ParentProcName: str
        :param ParentProcUser: 父进程用户
        :type ParentProcUser: str
        :param ParentProcGroup: 父进程用户组
        :type ParentProcGroup: str
        :param ParentProcPath: 父进程路径
        :type ParentProcPath: str
        :param Status: 处理状态
        :type Status: int
        :param CreateTime: 产生时间
        :type CreateTime: str
        :param MachineName: 主机名
        :type MachineName: str
        :param ProcTree: 进程树
        :type ProcTree: str
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.DstIp = None
        self.DstPort = None
        self.ProcessName = None
        self.FullPath = None
        self.CmdLine = None
        self.UserName = None
        self.UserGroup = None
        self.ParentProcName = None
        self.ParentProcUser = None
        self.ParentProcGroup = None
        self.ParentProcPath = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None
        self.ProcTree = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.ProcessName = params.get("ProcessName")
        self.FullPath = params.get("FullPath")
        self.CmdLine = params.get("CmdLine")
        self.UserName = params.get("UserName")
        self.UserGroup = params.get("UserGroup")
        self.ParentProcName = params.get("ParentProcName")
        self.ParentProcUser = params.get("ParentProcUser")
        self.ParentProcGroup = params.get("ParentProcGroup")
        self.ParentProcPath = params.get("ParentProcPath")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.ProcTree = params.get("ProcTree")


class ReverseShellRule(AbstractModel):
    """反弹Shell规则

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param DestIp: 目标IP
        :type DestIp: str
        :param DestPort: 目标端口
        :type DestPort: str
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态 (0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        """
        self.Id = None
        self.Uuid = None
        self.ProcessName = None
        self.DestIp = None
        self.DestPort = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.DestIp = params.get("DestIp")
        self.DestPort = params.get("DestPort")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")


class SecurityDynamic(AbstractModel):
    """安全事件消息数据。

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端UUID。
        :type Uuid: str
        :param EventTime: 安全事件发生事件。
        :type EventTime: str
        :param EventType: 安全事件类型。
<li>MALWARE：木马事件</li>
<li>NON_LOCAL_LOGIN：异地登录</li>
<li>BRUTEATTACK_SUCCESS：密码破解成功</li>
<li>VUL：漏洞</li>
<li>BASELINE：安全基线</li>
        :type EventType: str
        :param Message: 安全事件消息。
        :type Message: str
        :param SecurityLevel: 安全事件等级。
<li>RISK: 严重</li>
<li>HIGH: 高危</li>
<li>NORMAL: 中危</li>
<li>LOW: 低危</li>
        :type SecurityLevel: str
        """
        self.Uuid = None
        self.EventTime = None
        self.EventType = None
        self.Message = None
        self.SecurityLevel = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.Message = params.get("Message")
        self.SecurityLevel = params.get("SecurityLevel")


class SecurityTrend(AbstractModel):
    """安全趋势统计数据。

    """

    def __init__(self):
        """
        :param Date: 事件时间。
        :type Date: str
        :param EventNum: 事件数量。
        :type EventNum: int
        """
        self.Date = None
        self.EventNum = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.EventNum = params.get("EventNum")


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马事件ID数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessIds: 隔离成功的id数组。
        :type SuccessIds: list of int non-negative
        :param FailedIds: 隔离失败的id数组。
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class SetBashEventsStatusRequest(AbstractModel):
    """SetBashEventsStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        :param Status: 新状态(0-待处理 1-高危 2-正常)
        :type Status: int
        """
        self.Ids = None
        self.Status = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.Status = params.get("Status")


class SetBashEventsStatusResponse(AbstractModel):
    """SetBashEventsStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SwitchBashRulesRequest(AbstractModel):
    """SwitchBashRules请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param Disabled: 是否禁用
        :type Disabled: int
        """
        self.Id = None
        self.Disabled = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Disabled = params.get("Disabled")


class SwitchBashRulesResponse(AbstractModel):
    """SwitchBashRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签信息

    """

    def __init__(self):
        """
        :param Id: 标签ID
        :type Id: int
        :param Name: 标签名
        :type Name: str
        :param Count: 服务器数
        :type Count: int
        """
        self.Id = None
        self.Name = None
        self.Count = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Count = params.get("Count")


class TagMachine(AbstractModel):
    """标签相关服务器信息

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param MachineRegion: 主机区域
        :type MachineRegion: str
        :param MachineType: 主机区域类型
        :type MachineType: str
        """
        self.Id = None
        self.Quuid = None
        self.MachineName = None
        self.MachineIp = None
        self.MachineWanIp = None
        self.MachineRegion = None
        self.MachineType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Quuid = params.get("Quuid")
        self.MachineName = params.get("MachineName")
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.MachineRegion = params.get("MachineRegion")
        self.MachineType = params.get("MachineType")


class TrustMaliciousRequestRequest(AbstractModel):
    """TrustMaliciousRequest请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 恶意请求记录ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class TrustMaliciousRequestResponse(AbstractModel):
    """TrustMaliciousRequest返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马ID数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMaliciousRequestRequest(AbstractModel):
    """UntrustMaliciousRequest请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 受信任记录ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class UntrustMaliciousRequestResponse(AbstractModel):
    """UntrustMaliciousRequest返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马ID数组，单次最大处理不能超过200条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsualPlace(AbstractModel):
    """常用登录地

    """

    def __init__(self):
        """
        :param Id: ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param CountryId: 国家 ID。
        :type CountryId: int
        :param ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param CityId: 城市 ID。
        :type CityId: int
        """
        self.Id = None
        self.Uuid = None
        self.CountryId = None
        self.ProvinceId = None
        self.CityId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.CountryId = params.get("CountryId")
        self.ProvinceId = params.get("ProvinceId")
        self.CityId = params.get("CityId")


class Vul(AbstractModel):
    """漏洞列表数据

    """

    def __init__(self):
        """
        :param VulId: 漏洞种类ID
        :type VulId: int
        :param VulName: 漏洞名称
        :type VulName: str
        :param VulLevel: 漏洞危害等级:
HIGH：高危
MIDDLE：中危
LOW：低危
NOTICE：提示
        :type VulLevel: str
        :param LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param ImpactedHostNum: 受影响机器数量
        :type ImpactedHostNum: int
        :param VulStatus: 漏洞状态
* UN_OPERATED : 待处理
* FIXED : 已修复
        :type VulStatus: str
        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.LastScanTime = None
        self.ImpactedHostNum = None
        self.VulStatus = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.LastScanTime = params.get("LastScanTime")
        self.ImpactedHostNum = params.get("ImpactedHostNum")
        self.VulStatus = params.get("VulStatus")


class WeeklyReport(AbstractModel):
    """周报列表。

    """

    def __init__(self):
        """
        :param BeginDate: 周报开始时间。
        :type BeginDate: str
        :param EndDate: 周报结束时间。
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")


class WeeklyReportBruteAttack(AbstractModel):
    """专业周报密码破解数据。

    """

    def __init__(self):
        """
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Username: 被破解用户名。
        :type Username: str
        :param SrcIp: 源IP。
        :type SrcIp: str
        :param Count: 尝试次数。
        :type Count: int
        :param AttackTime: 攻击时间。
        :type AttackTime: str
        """
        self.MachineIp = None
        self.Username = None
        self.SrcIp = None
        self.Count = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.Username = params.get("Username")
        self.SrcIp = params.get("SrcIp")
        self.Count = params.get("Count")
        self.AttackTime = params.get("AttackTime")


class WeeklyReportMalware(AbstractModel):
    """专业周报木马数据。

    """

    def __init__(self):
        """
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param FilePath: 木马文件路径。
        :type FilePath: str
        :param Md5: 木马文件MD5值。
        :type Md5: str
        :param FindTime: 木马发现时间。
        :type FindTime: str
        :param Status: 当前木马状态。
<li>UN_OPERATED：未处理</li>
<li>SEGREGATED：已隔离</li>
<li>TRUSTED：已信任</li>
<li>SEPARATING：隔离中</li>
<li>RECOVERING：恢复中</li>
        :type Status: str
        """
        self.MachineIp = None
        self.FilePath = None
        self.Md5 = None
        self.FindTime = None
        self.Status = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.FilePath = params.get("FilePath")
        self.Md5 = params.get("Md5")
        self.FindTime = params.get("FindTime")
        self.Status = params.get("Status")


class WeeklyReportNonlocalLoginPlace(AbstractModel):
    """专业周报异地登录数据。

    """

    def __init__(self):
        """
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param Username: 用户名。
        :type Username: str
        :param SrcIp: 源IP。
        :type SrcIp: str
        :param Country: 国家ID。
        :type Country: int
        :param Province: 省份ID。
        :type Province: int
        :param City: 城市ID。
        :type City: int
        :param LoginTime: 登录时间。
        :type LoginTime: str
        """
        self.MachineIp = None
        self.Username = None
        self.SrcIp = None
        self.Country = None
        self.Province = None
        self.City = None
        self.LoginTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.Username = params.get("Username")
        self.SrcIp = params.get("SrcIp")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.LoginTime = params.get("LoginTime")


class WeeklyReportVul(AbstractModel):
    """专业版周报漏洞数据。

    """

    def __init__(self):
        """
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param VulName: 漏洞名称。
        :type VulName: str
        :param VulType: 漏洞类型。
<li> WEB : Web漏洞</li>
<li> SYSTEM :系统组件漏洞</li>
<li> BASELINE : 安全基线</li>
        :type VulType: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulStatus: 漏洞状态。
<li> UN_OPERATED : 待处理</li>
<li> SCANING : 扫描中</li>
<li> FIXED : 已修复</li>
        :type VulStatus: str
        :param LastScanTime: 最后扫描时间。
        :type LastScanTime: str
        """
        self.MachineIp = None
        self.VulName = None
        self.VulType = None
        self.Description = None
        self.VulStatus = None
        self.LastScanTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.VulName = params.get("VulName")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.VulStatus = params.get("VulStatus")
        self.LastScanTime = params.get("LastScanTime")