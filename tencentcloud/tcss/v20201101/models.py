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


class AbnormalProcessChildRuleInfo(AbstractModel):
    """容器运行时安全，子策略信息

    """

    def __init__(self):
        r"""
        :param RuleMode: 策略模式，   RULE_MODE_RELEASE: 放行
   RULE_MODE_ALERT: 告警
   RULE_MODE_HOLDUP:拦截
        :type RuleMode: str
        :param ProcessPath: 进程路径
        :type ProcessPath: str
        :param RuleId: 子策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        """
        self.RuleMode = None
        self.ProcessPath = None
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleMode = params.get("RuleMode")
        self.ProcessPath = params.get("ProcessPath")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalProcessEventDescription(AbstractModel):
    """运行时容器访问控制事件描述信息

    """

    def __init__(self):
        r"""
        :param Description: 事件规则
        :type Description: str
        :param Solution: 解决方案
        :type Solution: str
        :param Remark: 事件备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param MatchRule: 命中规则详细信息
        :type MatchRule: :class:`tencentcloud.tcss.v20201101.models.AbnormalProcessChildRuleInfo`
        :param RuleName: 命中规则名字
        :type RuleName: str
        :param RuleId: 命中规则的id
        :type RuleId: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.MatchRule = None
        self.RuleName = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        if params.get("MatchRule") is not None:
            self.MatchRule = AbnormalProcessChildRuleInfo()
            self.MatchRule._deserialize(params.get("MatchRule"))
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalProcessEventInfo(AbstractModel):
    """容器运行时安全异常进程信息

    """

    def __init__(self):
        r"""
        :param ProcessPath: 进程目录
        :type ProcessPath: str
        :param EventType: 事件类型，MALICE_PROCESS_START:恶意进程启动
        :type EventType: str
        :param MatchRuleName: 命中规则
        :type MatchRuleName: str
        :param FoundTime: 生成时间
        :type FoundTime: str
        :param ContainerName: 容器名
        :type ContainerName: str
        :param ImageName: 镜像名
        :type ImageName: str
        :param Behavior: 动作执行结果，    BEHAVIOR_NONE: 无
    BEHAVIOR_ALERT: 告警
    BEHAVIOR_RELEASE：放行
    BEHAVIOR_HOLDUP_FAILED:拦截失败
    BEHAVIOR_HOLDUP_SUCCESSED：拦截失败
        :type Behavior: str
        :param Status: 状态，EVENT_UNDEAL:事件未处理
    EVENT_DEALED:事件已经处理
    EVENT_INGNORE：事件已经忽略
        :type Status: str
        :param Id: 事件记录的唯一id
        :type Id: str
        :param ImageId: 镜像id，用于跳转
        :type ImageId: str
        :param ContainerId: 容器id，用于跳转
        :type ContainerId: str
        :param Solution: 事件解决方案
        :type Solution: str
        :param Description: 事件详细描述
        :type Description: str
        :param MatchRuleId: 命中策略id
        :type MatchRuleId: str
        :param MatchAction: 命中规则行为：
RULE_MODE_RELEASE 放行
RULE_MODE_ALERT  告警
RULE_MODE_HOLDUP 拦截
        :type MatchAction: str
        :param MatchProcessPath: 命中规则进程信息
        :type MatchProcessPath: str
        :param RuleExist: 规则是否存在
        :type RuleExist: bool
        :param EventCount: 事件数量
        :type EventCount: int
        :param LatestFoundTime: 最近生成时间
        :type LatestFoundTime: str
        :param RuleId: 规则组Id
        :type RuleId: str
        """
        self.ProcessPath = None
        self.EventType = None
        self.MatchRuleName = None
        self.FoundTime = None
        self.ContainerName = None
        self.ImageName = None
        self.Behavior = None
        self.Status = None
        self.Id = None
        self.ImageId = None
        self.ContainerId = None
        self.Solution = None
        self.Description = None
        self.MatchRuleId = None
        self.MatchAction = None
        self.MatchProcessPath = None
        self.RuleExist = None
        self.EventCount = None
        self.LatestFoundTime = None
        self.RuleId = None


    def _deserialize(self, params):
        self.ProcessPath = params.get("ProcessPath")
        self.EventType = params.get("EventType")
        self.MatchRuleName = params.get("MatchRuleName")
        self.FoundTime = params.get("FoundTime")
        self.ContainerName = params.get("ContainerName")
        self.ImageName = params.get("ImageName")
        self.Behavior = params.get("Behavior")
        self.Status = params.get("Status")
        self.Id = params.get("Id")
        self.ImageId = params.get("ImageId")
        self.ContainerId = params.get("ContainerId")
        self.Solution = params.get("Solution")
        self.Description = params.get("Description")
        self.MatchRuleId = params.get("MatchRuleId")
        self.MatchAction = params.get("MatchAction")
        self.MatchProcessPath = params.get("MatchProcessPath")
        self.RuleExist = params.get("RuleExist")
        self.EventCount = params.get("EventCount")
        self.LatestFoundTime = params.get("LatestFoundTime")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalProcessRuleInfo(AbstractModel):
    """运行时安全，异常进程检测策略

    """

    def __init__(self):
        r"""
        :param IsEnable: true:策略启用，false:策略禁用
        :type IsEnable: bool
        :param ImageIds: 生效镜像id，空数组代表全部镜像
        :type ImageIds: list of str
        :param ChildRules: 用户策略的子策略数组
        :type ChildRules: list of AbnormalProcessChildRuleInfo
        :param RuleName: 策略名字
        :type RuleName: str
        :param RuleId: 策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param SystemChildRules: 系统策略的子策略数组
        :type SystemChildRules: list of AbnormalProcessSystemChildRuleInfo
        """
        self.IsEnable = None
        self.ImageIds = None
        self.ChildRules = None
        self.RuleName = None
        self.RuleId = None
        self.SystemChildRules = None


    def _deserialize(self, params):
        self.IsEnable = params.get("IsEnable")
        self.ImageIds = params.get("ImageIds")
        if params.get("ChildRules") is not None:
            self.ChildRules = []
            for item in params.get("ChildRules"):
                obj = AbnormalProcessChildRuleInfo()
                obj._deserialize(item)
                self.ChildRules.append(obj)
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        if params.get("SystemChildRules") is not None:
            self.SystemChildRules = []
            for item in params.get("SystemChildRules"):
                obj = AbnormalProcessSystemChildRuleInfo()
                obj._deserialize(item)
                self.SystemChildRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalProcessSystemChildRuleInfo(AbstractModel):
    """异常进程系统策略的子策略信息

    """

    def __init__(self):
        r"""
        :param RuleId: 子策略Id
        :type RuleId: str
        :param IsEnable: 子策略状态，true为开启，false为关闭
        :type IsEnable: bool
        :param RuleMode: 策略模式,  RULE_MODE_RELEASE: 放行
   RULE_MODE_ALERT: 告警
   RULE_MODE_HOLDUP:拦截
        :type RuleMode: str
        :param RuleType: 子策略检测的行为类型
PROXY_TOOL： 代理软件
TRANSFER_CONTROL：横向渗透
ATTACK_CMD： 恶意命令
REVERSE_SHELL：反弹shell
FILELESS：无文件程序执行
RISK_CMD：高危命令
ABNORMAL_CHILD_PROC: 敏感服务异常子进程启动
        :type RuleType: str
        """
        self.RuleId = None
        self.IsEnable = None
        self.RuleMode = None
        self.RuleType = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.IsEnable = params.get("IsEnable")
        self.RuleMode = params.get("RuleMode")
        self.RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlChildRuleInfo(AbstractModel):
    """容器运行时安全，访问控制子策略信息

    """

    def __init__(self):
        r"""
        :param RuleMode: 策略模式,  RULE_MODE_RELEASE: 放行
   RULE_MODE_ALERT: 告警
   RULE_MODE_HOLDUP:拦截
        :type RuleMode: str
        :param ProcessPath: 进程路径
        :type ProcessPath: str
        :param TargetFilePath: 被访问文件路径，仅仅在访问控制生效
        :type TargetFilePath: str
        :param RuleId: 子策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        """
        self.RuleMode = None
        self.ProcessPath = None
        self.TargetFilePath = None
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleMode = params.get("RuleMode")
        self.ProcessPath = params.get("ProcessPath")
        self.TargetFilePath = params.get("TargetFilePath")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlEventDescription(AbstractModel):
    """运行时容器访问控制事件描述信息

    """

    def __init__(self):
        r"""
        :param Description: 事件规则
        :type Description: str
        :param Solution: 解决方案
        :type Solution: str
        :param Remark: 事件备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param MatchRule: 命中规则详细信息
        :type MatchRule: :class:`tencentcloud.tcss.v20201101.models.AccessControlChildRuleInfo`
        :param RuleName: 命中规则名字
        :type RuleName: str
        :param RuleId: 命中规则id
        :type RuleId: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.MatchRule = None
        self.RuleName = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        if params.get("MatchRule") is not None:
            self.MatchRule = AccessControlChildRuleInfo()
            self.MatchRule._deserialize(params.get("MatchRule"))
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlEventInfo(AbstractModel):
    """容器运行时安全访问控制事件信息

    """

    def __init__(self):
        r"""
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param MatchRuleName: 命中规则名称
        :type MatchRuleName: str
        :param FoundTime: 生成时间
        :type FoundTime: str
        :param ContainerName: 容器名
        :type ContainerName: str
        :param ImageName: 镜像名
        :type ImageName: str
        :param Behavior: 动作执行结果，   BEHAVIOR_NONE: 无
    BEHAVIOR_ALERT: 告警
    BEHAVIOR_RELEASE：放行
    BEHAVIOR_HOLDUP_FAILED:拦截失败
    BEHAVIOR_HOLDUP_SUCCESSED：拦截失败
        :type Behavior: str
        :param Status: 状态0:未处理  “EVENT_UNDEAL”:事件未处理
    "EVENT_DEALED":事件已经处理
    "EVENT_INGNORE"：事件已经忽略
        :type Status: str
        :param Id: 事件记录的唯一id
        :type Id: str
        :param FileName: 文件名称
        :type FileName: str
        :param EventType: 事件类型， FILE_ABNORMAL_READ:文件异常读取
        :type EventType: str
        :param ImageId: 镜像id, 用于跳转
        :type ImageId: str
        :param ContainerId: 容器id, 用于跳转
        :type ContainerId: str
        :param Solution: 事件解决方案
        :type Solution: str
        :param Description: 事件详细描述
        :type Description: str
        :param MatchRuleId: 命中策略id
        :type MatchRuleId: str
        :param MatchAction: 命中规则行为：
RULE_MODE_RELEASE 放行
RULE_MODE_ALERT  告警
RULE_MODE_HOLDUP 拦截
        :type MatchAction: str
        :param MatchProcessPath: 命中规则进程信息
        :type MatchProcessPath: str
        :param MatchFilePath: 命中规则文件信息
        :type MatchFilePath: str
        :param FilePath: 文件路径，包含名字
        :type FilePath: str
        :param RuleExist: 规则是否存在
        :type RuleExist: bool
        :param EventCount: 事件数量
        :type EventCount: int
        :param LatestFoundTime: 最近生成时间
        :type LatestFoundTime: str
        :param RuleId: 规则组id
        :type RuleId: str
        """
        self.ProcessName = None
        self.MatchRuleName = None
        self.FoundTime = None
        self.ContainerName = None
        self.ImageName = None
        self.Behavior = None
        self.Status = None
        self.Id = None
        self.FileName = None
        self.EventType = None
        self.ImageId = None
        self.ContainerId = None
        self.Solution = None
        self.Description = None
        self.MatchRuleId = None
        self.MatchAction = None
        self.MatchProcessPath = None
        self.MatchFilePath = None
        self.FilePath = None
        self.RuleExist = None
        self.EventCount = None
        self.LatestFoundTime = None
        self.RuleId = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.MatchRuleName = params.get("MatchRuleName")
        self.FoundTime = params.get("FoundTime")
        self.ContainerName = params.get("ContainerName")
        self.ImageName = params.get("ImageName")
        self.Behavior = params.get("Behavior")
        self.Status = params.get("Status")
        self.Id = params.get("Id")
        self.FileName = params.get("FileName")
        self.EventType = params.get("EventType")
        self.ImageId = params.get("ImageId")
        self.ContainerId = params.get("ContainerId")
        self.Solution = params.get("Solution")
        self.Description = params.get("Description")
        self.MatchRuleId = params.get("MatchRuleId")
        self.MatchAction = params.get("MatchAction")
        self.MatchProcessPath = params.get("MatchProcessPath")
        self.MatchFilePath = params.get("MatchFilePath")
        self.FilePath = params.get("FilePath")
        self.RuleExist = params.get("RuleExist")
        self.EventCount = params.get("EventCount")
        self.LatestFoundTime = params.get("LatestFoundTime")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlRuleInfo(AbstractModel):
    """容器运行时，访问控制策略信息

    """

    def __init__(self):
        r"""
        :param IsEnable: 开关,true:开启，false:禁用
        :type IsEnable: bool
        :param ImageIds: 生效惊现id，空数组代表全部镜像
        :type ImageIds: list of str
        :param ChildRules: 用户策略的子策略数组
        :type ChildRules: list of AccessControlChildRuleInfo
        :param RuleName: 策略名字
        :type RuleName: str
        :param RuleId: 策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param SystemChildRules: 系统策略的子策略数组
        :type SystemChildRules: list of AccessControlSystemChildRuleInfo
        """
        self.IsEnable = None
        self.ImageIds = None
        self.ChildRules = None
        self.RuleName = None
        self.RuleId = None
        self.SystemChildRules = None


    def _deserialize(self, params):
        self.IsEnable = params.get("IsEnable")
        self.ImageIds = params.get("ImageIds")
        if params.get("ChildRules") is not None:
            self.ChildRules = []
            for item in params.get("ChildRules"):
                obj = AccessControlChildRuleInfo()
                obj._deserialize(item)
                self.ChildRules.append(obj)
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        if params.get("SystemChildRules") is not None:
            self.SystemChildRules = []
            for item in params.get("SystemChildRules"):
                obj = AccessControlSystemChildRuleInfo()
                obj._deserialize(item)
                self.SystemChildRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlSystemChildRuleInfo(AbstractModel):
    """容器运行时安全，访问控制系统策略的子策略信息

    """

    def __init__(self):
        r"""
        :param RuleId: 子策略Id
        :type RuleId: str
        :param RuleMode: 策略模式,  RULE_MODE_RELEASE: 放行
   RULE_MODE_ALERT: 告警
   RULE_MODE_HOLDUP:拦截
        :type RuleMode: str
        :param IsEnable: 子策略状态，true为开启，false为关闭
        :type IsEnable: bool
        :param RuleType: 子策略检测的入侵行为类型
CHANGE_CRONTAB：篡改计划任务
CHANGE_SYS_BIN：篡改系统程序
CHANGE_USRCFG：篡改用户配置
        :type RuleType: str
        """
        self.RuleId = None
        self.RuleMode = None
        self.IsEnable = None
        self.RuleType = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleMode = params.get("RuleMode")
        self.IsEnable = params.get("IsEnable")
        self.RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAssetImageRegistryRegistryDetailRequest(AbstractModel):
    """AddAssetImageRegistryRegistryDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 仓库名
        :type Name: str
        :param Username: 用户名
        :type Username: str
        :param Password: 密码
        :type Password: str
        :param Url: 仓库url
        :type Url: str
        :param RegistryType: 仓库类型，列表：harbor
        :type RegistryType: str
        :param NetType: 网络类型，列表：public（公网）
        :type NetType: str
        :param RegistryVersion: 仓库版本
        :type RegistryVersion: str
        :param RegistryRegion: 区域，列表：default（默认）
        :type RegistryRegion: str
        :param SpeedLimit: 限速
        :type SpeedLimit: int
        """
        self.Name = None
        self.Username = None
        self.Password = None
        self.Url = None
        self.RegistryType = None
        self.NetType = None
        self.RegistryVersion = None
        self.RegistryRegion = None
        self.SpeedLimit = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.Url = params.get("Url")
        self.RegistryType = params.get("RegistryType")
        self.NetType = params.get("NetType")
        self.RegistryVersion = params.get("RegistryVersion")
        self.RegistryRegion = params.get("RegistryRegion")
        self.SpeedLimit = params.get("SpeedLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAssetImageRegistryRegistryDetailResponse(AbstractModel):
    """AddAssetImageRegistryRegistryDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param HealthCheckErr: 连接错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckErr: str
        :param NameRepeatErr: 名称错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NameRepeatErr: str
        :param RegistryId: 仓库唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HealthCheckErr = None
        self.NameRepeatErr = None
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HealthCheckErr = params.get("HealthCheckErr")
        self.NameRepeatErr = params.get("NameRepeatErr")
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class AddCompliancePolicyItemToWhitelistRequest(AbstractModel):
    """AddCompliancePolicyItemToWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemIdSet: 要忽略的检测项的ID的列表
        :type CustomerPolicyItemIdSet: list of int non-negative
        """
        self.CustomerPolicyItemIdSet = None


    def _deserialize(self, params):
        self.CustomerPolicyItemIdSet = params.get("CustomerPolicyItemIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCompliancePolicyItemToWhitelistResponse(AbstractModel):
    """AddCompliancePolicyItemToWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddEditAbnormalProcessRuleRequest(AbstractModel):
    """AddEditAbnormalProcessRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleInfo: 增加策略信息，策略id为空，编辑策略是id不能为空
        :type RuleInfo: :class:`tencentcloud.tcss.v20201101.models.AbnormalProcessRuleInfo`
        :param EventId: 仅在加白的时候带上
        :type EventId: str
        """
        self.RuleInfo = None
        self.EventId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = AbnormalProcessRuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEditAbnormalProcessRuleResponse(AbstractModel):
    """AddEditAbnormalProcessRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddEditAccessControlRuleRequest(AbstractModel):
    """AddEditAccessControlRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleInfo: 增加策略信息，策略id为空，编辑策略是id不能为空
        :type RuleInfo: :class:`tencentcloud.tcss.v20201101.models.AccessControlRuleInfo`
        :param EventId: 仅在白名单时候使用
        :type EventId: str
        """
        self.RuleInfo = None
        self.EventId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = AccessControlRuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEditAccessControlRuleResponse(AbstractModel):
    """AddEditAccessControlRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddEditReverseShellWhiteListRequest(AbstractModel):
    """AddEditReverseShellWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListInfo: 增加或编辑白名单信息。新增白名单时WhiteListInfo.id为空，编辑白名单WhiteListInfo.id不能为空。
        :type WhiteListInfo: :class:`tencentcloud.tcss.v20201101.models.ReverseShellWhiteListInfo`
        :param EventId: 仅在添加事件白名单时候使用
        :type EventId: str
        """
        self.WhiteListInfo = None
        self.EventId = None


    def _deserialize(self, params):
        if params.get("WhiteListInfo") is not None:
            self.WhiteListInfo = ReverseShellWhiteListInfo()
            self.WhiteListInfo._deserialize(params.get("WhiteListInfo"))
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEditReverseShellWhiteListResponse(AbstractModel):
    """AddEditReverseShellWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddEditRiskSyscallWhiteListRequest(AbstractModel):
    """AddEditRiskSyscallWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventId: 仅在添加白名单时候使用
        :type EventId: str
        :param WhiteListInfo: 增加白名单信息，白名单id为空，编辑白名单id不能为空
        :type WhiteListInfo: :class:`tencentcloud.tcss.v20201101.models.RiskSyscallWhiteListInfo`
        """
        self.EventId = None
        self.WhiteListInfo = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        if params.get("WhiteListInfo") is not None:
            self.WhiteListInfo = RiskSyscallWhiteListInfo()
            self.WhiteListInfo._deserialize(params.get("WhiteListInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEditRiskSyscallWhiteListResponse(AbstractModel):
    """AddEditRiskSyscallWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddEditWarningRulesRequest(AbstractModel):
    """AddEditWarningRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param WarningRules: 告警开关策略
        :type WarningRules: list of WarningRule
        """
        self.WarningRules = None


    def _deserialize(self, params):
        if params.get("WarningRules") is not None:
            self.WarningRules = []
            for item in params.get("WarningRules"):
                obj = WarningRule()
                obj._deserialize(item)
                self.WarningRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEditWarningRulesResponse(AbstractModel):
    """AddEditWarningRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AffectedNodeItem(AbstractModel):
    """受影响的节点类型结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名字
        :type ClusterName: str
        :param InstanceId: 实例id
        :type InstanceId: str
        :param PrivateIpAddresses: 内网ip地址
        :type PrivateIpAddresses: str
        :param InstanceRole: 节点的角色，Master、Work等
        :type InstanceRole: str
        :param ClusterVersion: k8s版本
        :type ClusterVersion: str
        :param ContainerRuntime: 运行时组件,docker或者containerd
        :type ContainerRuntime: str
        :param Region: 区域
        :type Region: str
        :param VerifyInfo: 检查结果的验证信息
        :type VerifyInfo: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceId = None
        self.PrivateIpAddresses = None
        self.InstanceRole = None
        self.ClusterVersion = None
        self.ContainerRuntime = None
        self.Region = None
        self.VerifyInfo = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceId = params.get("InstanceId")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceRole = params.get("InstanceRole")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.Region = params.get("Region")
        self.VerifyInfo = params.get("VerifyInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AffectedWorkloadItem(AbstractModel):
    """集群安全检查受影响的工作负载Item

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param ClusterName: 集群名字
        :type ClusterName: str
        :param WorkloadName: 工作负载名称
        :type WorkloadName: str
        :param WorkloadType: 工作负载类型
        :type WorkloadType: str
        :param Region: 区域
        :type Region: str
        :param VerifyInfo: 检测结果的验证信息
        :type VerifyInfo: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.WorkloadName = None
        self.WorkloadType = None
        self.Region = None
        self.VerifyInfo = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.WorkloadName = params.get("WorkloadName")
        self.WorkloadType = params.get("WorkloadType")
        self.Region = params.get("Region")
        self.VerifyInfo = params.get("VerifyInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetFilters(AbstractModel):
    """容器安全
    描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 过滤键的名称
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 是否模糊查询
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetSimpleImageInfo(AbstractModel):
    """容器安全资产镜像简略信息

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ContainerCnt: 关联容器个数
        :type ContainerCnt: int
        :param ScanTime: 最后扫描时间
        :type ScanTime: str
        :param Size: 镜像大小
        :type Size: int
        """
        self.ImageID = None
        self.ImageName = None
        self.ContainerCnt = None
        self.ScanTime = None
        self.Size = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.ContainerCnt = params.get("ContainerCnt")
        self.ScanTime = params.get("ScanTime")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRepeatAssetImageRegistryRequest(AbstractModel):
    """CheckRepeatAssetImageRegistry请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 仓库名
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRepeatAssetImageRegistryResponse(AbstractModel):
    """CheckRepeatAssetImageRegistry返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsRepeat: 是否重复
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRepeat: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsRepeat = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsRepeat = params.get("IsRepeat")
        self.RequestId = params.get("RequestId")


class ClusterCheckItem(AbstractModel):
    """表示一条集群安全检测项的详细信息

    """

    def __init__(self):
        r"""
        :param CheckItemId: 唯一的检测项的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckItemId: int
        :param Name: 风险项的名称
        :type Name: str
        :param ItemDetail: 检测项详细描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemDetail: str
        :param RiskLevel: 威胁等级。严重Serious,高危High,中危Middle,提示Hint
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param RiskTarget: 检查对象、风险对象.Runc,Kubelet,Containerd,Pods
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskTarget: str
        :param RiskType: 风险类别,漏洞风险CVERisk,配置风险ConfigRisk
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskType: str
        :param RiskAttribute: 检测项所属的风险类型,权限提升:PrivilegePromotion,拒绝服务:RefuseService,目录穿越:DirectoryEscape,未授权访问:UnauthorizedAccess,权限许可和访问控制问题:PrivilegeAndAccessControl,敏感信息泄露:SensitiveInfoLeak
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskAttribute: str
        :param RiskProperty: 风险特征,Tag.存在EXP:ExistEXP,存在POD:ExistPOC,无需重启:NoNeedReboot, 服务重启:ServerRestart,远程信息泄露:RemoteInfoLeak,远程拒绝服务:RemoteRefuseService,远程利用:RemoteExploit,远程执行:RemoteExecute
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskProperty: str
        :param CVENumber: CVE编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CVENumber: str
        :param DiscoverTime: 披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscoverTime: str
        :param Solution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param CVSS: CVSS信息,用于画图
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSS: str
        :param CVSSScore: CVSS分数
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSScore: str
        :param RelateLink: 参考连接
注意：此字段可能返回 null，表示取不到有效值。
        :type RelateLink: str
        :param AffectedType: 影响类型，为Node或者Workload
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedType: str
        :param AffectedVersion: 受影响的版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedVersion: str
        """
        self.CheckItemId = None
        self.Name = None
        self.ItemDetail = None
        self.RiskLevel = None
        self.RiskTarget = None
        self.RiskType = None
        self.RiskAttribute = None
        self.RiskProperty = None
        self.CVENumber = None
        self.DiscoverTime = None
        self.Solution = None
        self.CVSS = None
        self.CVSSScore = None
        self.RelateLink = None
        self.AffectedType = None
        self.AffectedVersion = None


    def _deserialize(self, params):
        self.CheckItemId = params.get("CheckItemId")
        self.Name = params.get("Name")
        self.ItemDetail = params.get("ItemDetail")
        self.RiskLevel = params.get("RiskLevel")
        self.RiskTarget = params.get("RiskTarget")
        self.RiskType = params.get("RiskType")
        self.RiskAttribute = params.get("RiskAttribute")
        self.RiskProperty = params.get("RiskProperty")
        self.CVENumber = params.get("CVENumber")
        self.DiscoverTime = params.get("DiscoverTime")
        self.Solution = params.get("Solution")
        self.CVSS = params.get("CVSS")
        self.CVSSScore = params.get("CVSSScore")
        self.RelateLink = params.get("RelateLink")
        self.AffectedType = params.get("AffectedType")
        self.AffectedVersion = params.get("AffectedVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCheckTaskItem(AbstractModel):
    """集群检查任务入参

    """

    def __init__(self):
        r"""
        :param ClusterId: 指定要扫描的集群ID
        :type ClusterId: str
        :param ClusterRegion: 集群所属地域
        :type ClusterRegion: str
        :param NodeIp: 指定要扫描的节点IP
        :type NodeIp: str
        :param WorkloadName: 按照要扫描的workload名字
        :type WorkloadName: str
        """
        self.ClusterId = None
        self.ClusterRegion = None
        self.NodeIp = None
        self.WorkloadName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterRegion = params.get("ClusterRegion")
        self.NodeIp = params.get("NodeIp")
        self.WorkloadName = params.get("WorkloadName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCreateComponentItem(AbstractModel):
    """CreateCheckComponent的入口参数,用于批量安装防御容器

    """

    def __init__(self):
        r"""
        :param ClusterId: 要安装组件的集群ID。
        :type ClusterId: str
        :param ClusterRegion: 该集群对应的地域
        :type ClusterRegion: str
        """
        self.ClusterId = None
        self.ClusterRegion = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterRegion = params.get("ClusterRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInfoItem(AbstractModel):
    """集群资产返回的结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param ClusterName: 集群名字
        :type ClusterName: str
        :param ClusterVersion: 集群版本
        :type ClusterVersion: str
        :param ClusterOs: 集群操作系统
        :type ClusterOs: str
        :param ClusterType: 集群类型
        :type ClusterType: str
        :param ClusterNodeNum: 集群节点数
        :type ClusterNodeNum: int
        :param Region: 集群区域
        :type Region: str
        :param DefenderStatus: 监控组件的状态，为Defender_Uninstall、Defender_Normal、Defender_Error、Defender_Installing
        :type DefenderStatus: str
        :param ClusterStatus: 集群状态
        :type ClusterStatus: str
        :param ClusterCheckMode: 集群的检测模式，为Cluster_Normal或者Cluster_Actived.
        :type ClusterCheckMode: str
        :param ClusterAutoCheck: 是否自动定期检测
        :type ClusterAutoCheck: bool
        :param DefenderErrorReason: 防护容器部署失败原因，为UserDaemonSetNotReady时,和UnreadyNodeNum转成"N个节点防御容器为就绪"，其他错误直接展示
        :type DefenderErrorReason: str
        :param UnreadyNodeNum: 防御容器没有ready状态的节点数量
        :type UnreadyNodeNum: int
        :param SeriousRiskCount: 严重风险检查项的数量
        :type SeriousRiskCount: int
        :param HighRiskCount: 高风险检查项的数量
        :type HighRiskCount: int
        :param MiddleRiskCount: 中风险检查项的数量
        :type MiddleRiskCount: int
        :param HintRiskCount: 提示风险检查项的数量
        :type HintRiskCount: int
        :param CheckFailReason: 检查失败原因
        :type CheckFailReason: str
        :param CheckStatus: 检查状态,为Task_Running, NoRisk, HasRisk, Uncheck, Task_Error
        :type CheckStatus: str
        :param TaskCreateTime: 任务创建时间,检查时间
        :type TaskCreateTime: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterVersion = None
        self.ClusterOs = None
        self.ClusterType = None
        self.ClusterNodeNum = None
        self.Region = None
        self.DefenderStatus = None
        self.ClusterStatus = None
        self.ClusterCheckMode = None
        self.ClusterAutoCheck = None
        self.DefenderErrorReason = None
        self.UnreadyNodeNum = None
        self.SeriousRiskCount = None
        self.HighRiskCount = None
        self.MiddleRiskCount = None
        self.HintRiskCount = None
        self.CheckFailReason = None
        self.CheckStatus = None
        self.TaskCreateTime = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterType = params.get("ClusterType")
        self.ClusterNodeNum = params.get("ClusterNodeNum")
        self.Region = params.get("Region")
        self.DefenderStatus = params.get("DefenderStatus")
        self.ClusterStatus = params.get("ClusterStatus")
        self.ClusterCheckMode = params.get("ClusterCheckMode")
        self.ClusterAutoCheck = params.get("ClusterAutoCheck")
        self.DefenderErrorReason = params.get("DefenderErrorReason")
        self.UnreadyNodeNum = params.get("UnreadyNodeNum")
        self.SeriousRiskCount = params.get("SeriousRiskCount")
        self.HighRiskCount = params.get("HighRiskCount")
        self.MiddleRiskCount = params.get("MiddleRiskCount")
        self.HintRiskCount = params.get("HintRiskCount")
        self.CheckFailReason = params.get("CheckFailReason")
        self.CheckStatus = params.get("CheckStatus")
        self.TaskCreateTime = params.get("TaskCreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterRiskItem(AbstractModel):
    """风险项是检查完之后，有问题的检测项，并且加了一些检查结果信息。

    """

    def __init__(self):
        r"""
        :param CheckItem: 检测项相关信息
        :type CheckItem: :class:`tencentcloud.tcss.v20201101.models.ClusterCheckItem`
        :param VerifyInfo: 验证信息
        :type VerifyInfo: str
        :param ErrorMessage: 事件描述,检查的错误信息
        :type ErrorMessage: str
        :param AffectedClusterCount: 受影响的集群数量
        :type AffectedClusterCount: int
        :param AffectedNodeCount: 受影响的节点数量
        :type AffectedNodeCount: int
        """
        self.CheckItem = None
        self.VerifyInfo = None
        self.ErrorMessage = None
        self.AffectedClusterCount = None
        self.AffectedNodeCount = None


    def _deserialize(self, params):
        if params.get("CheckItem") is not None:
            self.CheckItem = ClusterCheckItem()
            self.CheckItem._deserialize(params.get("CheckItem"))
        self.VerifyInfo = params.get("VerifyInfo")
        self.ErrorMessage = params.get("ErrorMessage")
        self.AffectedClusterCount = params.get("AffectedClusterCount")
        self.AffectedNodeCount = params.get("AffectedNodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceAffectedAsset(AbstractModel):
    """表示检测项所影响的资产的信息。

    """

    def __init__(self):
        r"""
        :param CustomerAssetId: 为客户分配的唯一的资产项的ID。
        :type CustomerAssetId: int
        :param AssetName: 资产项的名称。
        :type AssetName: str
        :param AssetType: 资产项的类型
        :type AssetType: str
        :param CheckStatus: 检测状态

CHECK_INIT, 待检测

CHECK_RUNNING, 检测中

CHECK_FINISHED, 检测完成

CHECK_FAILED, 检测失败
        :type CheckStatus: str
        :param NodeName: 节点名称。
        :type NodeName: str
        :param LastCheckTime: 上次检测的时间，格式为”YYYY-MM-DD HH:m::SS“。

如果没有检测过，此处为”0000-00-00 00:00:00“。
        :type LastCheckTime: str
        :param CheckResult: 检测结果。取值为：

RESULT_FAILED: 未通过

RESULT_PASSED: 通过
        :type CheckResult: str
        :param HostIP: 主机IP
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIP: str
        :param ImageTag: 镜像的tag
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTag: str
        """
        self.CustomerAssetId = None
        self.AssetName = None
        self.AssetType = None
        self.CheckStatus = None
        self.NodeName = None
        self.LastCheckTime = None
        self.CheckResult = None
        self.HostIP = None
        self.ImageTag = None


    def _deserialize(self, params):
        self.CustomerAssetId = params.get("CustomerAssetId")
        self.AssetName = params.get("AssetName")
        self.AssetType = params.get("AssetType")
        self.CheckStatus = params.get("CheckStatus")
        self.NodeName = params.get("NodeName")
        self.LastCheckTime = params.get("LastCheckTime")
        self.CheckResult = params.get("CheckResult")
        self.HostIP = params.get("HostIP")
        self.ImageTag = params.get("ImageTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceAssetDetailInfo(AbstractModel):
    """表示一项资产的详情。

    """

    def __init__(self):
        r"""
        :param CustomerAssetId: 客户资产的ID。
        :type CustomerAssetId: int
        :param AssetType: 资产类别。
        :type AssetType: str
        :param AssetName: 资产的名称。
        :type AssetName: str
        :param NodeName: 资产所属的节点的名称。
        :type NodeName: str
        :param HostName: 资产所在的主机的名称。
        :type HostName: str
        :param HostIP: 资产所在的主机的IP。
        :type HostIP: str
        :param CheckStatus: 检测状态
CHECK_INIT, 待检测
CHECK_RUNNING, 检测中
CHECK_FINISHED, 检测完成
CHECK_FAILED, 检测失败
        :type CheckStatus: str
        :param PassedPolicyItemCount: 此类资产通过的检测项的数目。
        :type PassedPolicyItemCount: int
        :param FailedPolicyItemCount: 此类资产未通过的检测的数目。
        :type FailedPolicyItemCount: int
        :param LastCheckTime: 上次检测的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param CheckResult: 检测结果：
RESULT_FAILED: 未通过。
RESULT_PASSED: 通过。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckResult: str
        :param AssetStatus: 资产的运行状态。
        :type AssetStatus: str
        :param AssetCreateTime: 创建资产的时间。
ASSET_NORMAL: 正常运行，
ASSET_PAUSED: 暂停运行，
ASSET_STOPPED: 停止运行，
ASSET_ABNORMAL: 异常
        :type AssetCreateTime: str
        """
        self.CustomerAssetId = None
        self.AssetType = None
        self.AssetName = None
        self.NodeName = None
        self.HostName = None
        self.HostIP = None
        self.CheckStatus = None
        self.PassedPolicyItemCount = None
        self.FailedPolicyItemCount = None
        self.LastCheckTime = None
        self.CheckResult = None
        self.AssetStatus = None
        self.AssetCreateTime = None


    def _deserialize(self, params):
        self.CustomerAssetId = params.get("CustomerAssetId")
        self.AssetType = params.get("AssetType")
        self.AssetName = params.get("AssetName")
        self.NodeName = params.get("NodeName")
        self.HostName = params.get("HostName")
        self.HostIP = params.get("HostIP")
        self.CheckStatus = params.get("CheckStatus")
        self.PassedPolicyItemCount = params.get("PassedPolicyItemCount")
        self.FailedPolicyItemCount = params.get("FailedPolicyItemCount")
        self.LastCheckTime = params.get("LastCheckTime")
        self.CheckResult = params.get("CheckResult")
        self.AssetStatus = params.get("AssetStatus")
        self.AssetCreateTime = params.get("AssetCreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceAssetInfo(AbstractModel):
    """表示一项资产的信息。

    """

    def __init__(self):
        r"""
        :param CustomerAssetId: 客户资产的ID。
        :type CustomerAssetId: int
        :param AssetType: 资产类别。
        :type AssetType: str
        :param AssetName: 资产的名称。
        :type AssetName: str
        :param ImageTag: 当资产为镜像时，这个字段为镜像Tag。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTag: str
        :param HostIP: 资产所在的主机IP。
        :type HostIP: str
        :param NodeName: 资产所属的节点的名称
        :type NodeName: str
        :param CheckStatus: 检测状态

CHECK_INIT, 待检测

CHECK_RUNNING, 检测中

CHECK_FINISHED, 检测完成

CHECK_FAILED, 检测失败
        :type CheckStatus: str
        :param PassedPolicyItemCount: 此类资产通过的检测项的数目。
注意：此字段可能返回 null，表示取不到有效值。
        :type PassedPolicyItemCount: int
        :param FailedPolicyItemCount: 此类资产未通过的检测的数目。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedPolicyItemCount: int
        :param LastCheckTime: 上次检测的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param CheckResult: 检测结果：
RESULT_FAILED: 未通过。
RESULT_PASSED: 通过。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckResult: str
        """
        self.CustomerAssetId = None
        self.AssetType = None
        self.AssetName = None
        self.ImageTag = None
        self.HostIP = None
        self.NodeName = None
        self.CheckStatus = None
        self.PassedPolicyItemCount = None
        self.FailedPolicyItemCount = None
        self.LastCheckTime = None
        self.CheckResult = None


    def _deserialize(self, params):
        self.CustomerAssetId = params.get("CustomerAssetId")
        self.AssetType = params.get("AssetType")
        self.AssetName = params.get("AssetName")
        self.ImageTag = params.get("ImageTag")
        self.HostIP = params.get("HostIP")
        self.NodeName = params.get("NodeName")
        self.CheckStatus = params.get("CheckStatus")
        self.PassedPolicyItemCount = params.get("PassedPolicyItemCount")
        self.FailedPolicyItemCount = params.get("FailedPolicyItemCount")
        self.LastCheckTime = params.get("LastCheckTime")
        self.CheckResult = params.get("CheckResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceAssetPolicyItem(AbstractModel):
    """表示一条检测项的信息。

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemId: 为客户分配的唯一的检测项的ID。
        :type CustomerPolicyItemId: int
        :param BasePolicyItemId: 检测项的原始ID
        :type BasePolicyItemId: int
        :param Name: 检测项的名称。
        :type Name: str
        :param Category: 检测项所属的类型的名称
        :type Category: str
        :param BenchmarkStandardId: 所属的合规标准的ID
        :type BenchmarkStandardId: int
        :param BenchmarkStandardName: 所属的合规标准的名称
        :type BenchmarkStandardName: str
        :param RiskLevel: 威胁等级
        :type RiskLevel: str
        :param CheckStatus: 检测状态
CHECK_INIT, 待检测
CHECK_RUNNING, 检测中
CHECK_FINISHED, 检测完成
CHECK_FAILED, 检测失败
        :type CheckStatus: str
        :param CheckResult: 检测结果
RESULT_PASSED: 通过
RESULT_FAILED: 未通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckResult: str
        :param WhitelistId: 检测项对应的白名单项的ID。如果存在且非0，表示检测项被用户忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type WhitelistId: int
        :param FixSuggestion: 处理建议。
        :type FixSuggestion: str
        :param LastCheckTime: 最近检测的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        """
        self.CustomerPolicyItemId = None
        self.BasePolicyItemId = None
        self.Name = None
        self.Category = None
        self.BenchmarkStandardId = None
        self.BenchmarkStandardName = None
        self.RiskLevel = None
        self.CheckStatus = None
        self.CheckResult = None
        self.WhitelistId = None
        self.FixSuggestion = None
        self.LastCheckTime = None


    def _deserialize(self, params):
        self.CustomerPolicyItemId = params.get("CustomerPolicyItemId")
        self.BasePolicyItemId = params.get("BasePolicyItemId")
        self.Name = params.get("Name")
        self.Category = params.get("Category")
        self.BenchmarkStandardId = params.get("BenchmarkStandardId")
        self.BenchmarkStandardName = params.get("BenchmarkStandardName")
        self.RiskLevel = params.get("RiskLevel")
        self.CheckStatus = params.get("CheckStatus")
        self.CheckResult = params.get("CheckResult")
        self.WhitelistId = params.get("WhitelistId")
        self.FixSuggestion = params.get("FixSuggestion")
        self.LastCheckTime = params.get("LastCheckTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceAssetSummary(AbstractModel):
    """表示一类资产的总览信息。

    """

    def __init__(self):
        r"""
        :param AssetType: 资产类别。
        :type AssetType: str
        :param IsCustomerFirstCheck: 是否为客户的首次检测。与CheckStatus配合使用。
        :type IsCustomerFirstCheck: bool
        :param CheckStatus: 检测状态

CHECK_UNINIT, 用户未启用此功能

CHECK_INIT, 待检测

CHECK_RUNNING, 检测中

CHECK_FINISHED, 检测完成

CHECK_FAILED, 检测失败
        :type CheckStatus: str
        :param CheckProgress: 此类别的检测进度，为 0~100 的数。若未在检测中，无此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckProgress: float
        :param PassedPolicyItemCount: 此类资产通过的检测项的数目。
        :type PassedPolicyItemCount: int
        :param FailedPolicyItemCount: 此类资产未通过的检测的数目。
        :type FailedPolicyItemCount: int
        :param FailedCriticalPolicyItemCount: 此类资产下未通过的严重级别的检测项的数目。
        :type FailedCriticalPolicyItemCount: int
        :param FailedHighRiskPolicyItemCount: 此类资产下未通过的高危检测项的数目。
        :type FailedHighRiskPolicyItemCount: int
        :param FailedMediumRiskPolicyItemCount: 此类资产下未通过的中危检测项的数目。
        :type FailedMediumRiskPolicyItemCount: int
        :param FailedLowRiskPolicyItemCount: 此类资产下未通过的低危检测项的数目。
        :type FailedLowRiskPolicyItemCount: int
        :param NoticePolicyItemCount: 此类资产下提示级别的检测项的数目。
        :type NoticePolicyItemCount: int
        :param PassedAssetCount: 通过检测的资产的数目。
        :type PassedAssetCount: int
        :param FailedAssetCount: 未通过检测的资产的数目。
        :type FailedAssetCount: int
        :param AssetPassedRate: 此类资产的合规率，0~100的数。
        :type AssetPassedRate: float
        :param ScanFailedAssetCount: 检测失败的资产的数目。
        :type ScanFailedAssetCount: int
        :param CheckCostTime: 上次检测的耗时，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckCostTime: float
        :param LastCheckTime: 上次检测的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param PeriodRule: 定时检测规则。
        :type PeriodRule: :class:`tencentcloud.tcss.v20201101.models.CompliancePeriodTaskRule`
        """
        self.AssetType = None
        self.IsCustomerFirstCheck = None
        self.CheckStatus = None
        self.CheckProgress = None
        self.PassedPolicyItemCount = None
        self.FailedPolicyItemCount = None
        self.FailedCriticalPolicyItemCount = None
        self.FailedHighRiskPolicyItemCount = None
        self.FailedMediumRiskPolicyItemCount = None
        self.FailedLowRiskPolicyItemCount = None
        self.NoticePolicyItemCount = None
        self.PassedAssetCount = None
        self.FailedAssetCount = None
        self.AssetPassedRate = None
        self.ScanFailedAssetCount = None
        self.CheckCostTime = None
        self.LastCheckTime = None
        self.PeriodRule = None


    def _deserialize(self, params):
        self.AssetType = params.get("AssetType")
        self.IsCustomerFirstCheck = params.get("IsCustomerFirstCheck")
        self.CheckStatus = params.get("CheckStatus")
        self.CheckProgress = params.get("CheckProgress")
        self.PassedPolicyItemCount = params.get("PassedPolicyItemCount")
        self.FailedPolicyItemCount = params.get("FailedPolicyItemCount")
        self.FailedCriticalPolicyItemCount = params.get("FailedCriticalPolicyItemCount")
        self.FailedHighRiskPolicyItemCount = params.get("FailedHighRiskPolicyItemCount")
        self.FailedMediumRiskPolicyItemCount = params.get("FailedMediumRiskPolicyItemCount")
        self.FailedLowRiskPolicyItemCount = params.get("FailedLowRiskPolicyItemCount")
        self.NoticePolicyItemCount = params.get("NoticePolicyItemCount")
        self.PassedAssetCount = params.get("PassedAssetCount")
        self.FailedAssetCount = params.get("FailedAssetCount")
        self.AssetPassedRate = params.get("AssetPassedRate")
        self.ScanFailedAssetCount = params.get("ScanFailedAssetCount")
        self.CheckCostTime = params.get("CheckCostTime")
        self.LastCheckTime = params.get("LastCheckTime")
        if params.get("PeriodRule") is not None:
            self.PeriodRule = CompliancePeriodTaskRule()
            self.PeriodRule._deserialize(params.get("PeriodRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceBenchmarkStandard(AbstractModel):
    """表示一个合规标准的信息。

    """

    def __init__(self):
        r"""
        :param StandardId: 合规标准的ID
        :type StandardId: int
        :param Name: 合规标准的名称
        :type Name: str
        :param PolicyItemCount: 合规标准包含的数目
        :type PolicyItemCount: int
        :param Enabled: 是否启用此标准
        :type Enabled: bool
        :param Description: 标准的描述
        :type Description: str
        """
        self.StandardId = None
        self.Name = None
        self.PolicyItemCount = None
        self.Enabled = None
        self.Description = None


    def _deserialize(self, params):
        self.StandardId = params.get("StandardId")
        self.Name = params.get("Name")
        self.PolicyItemCount = params.get("PolicyItemCount")
        self.Enabled = params.get("Enabled")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceBenchmarkStandardEnable(AbstractModel):
    """表示是否启用合规标准。

    """

    def __init__(self):
        r"""
        :param StandardId: 合规标准的ID。
        :type StandardId: int
        :param Enable: 是否启用合规标准
        :type Enable: bool
        """
        self.StandardId = None
        self.Enable = None


    def _deserialize(self, params):
        self.StandardId = params.get("StandardId")
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceContainerDetailInfo(AbstractModel):
    """表示容器资产专属的详情。

    """

    def __init__(self):
        r"""
        :param ContainerId: 容器在主机上的ID。
        :type ContainerId: str
        :param PodName: 容器所属的Pod的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        """
        self.ContainerId = None
        self.PodName = None


    def _deserialize(self, params):
        self.ContainerId = params.get("ContainerId")
        self.PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceFilters(AbstractModel):
    """键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 过滤键的名称
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 是否模糊查询。默认为是。
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceHostDetailInfo(AbstractModel):
    """表示主机资产专属的详情。

    """

    def __init__(self):
        r"""
        :param DockerVersion: 主机上的Docker版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerVersion: str
        :param K8SVersion: 主机上的K8S的版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type K8SVersion: str
        """
        self.DockerVersion = None
        self.K8SVersion = None


    def _deserialize(self, params):
        self.DockerVersion = params.get("DockerVersion")
        self.K8SVersion = params.get("K8SVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceImageDetailInfo(AbstractModel):
    """表示镜像资产专属的详情。

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像在主机上的ID。
        :type ImageId: str
        :param ImageName: 镜像的名称。
        :type ImageName: str
        :param ImageTag: 镜像的Tag。
        :type ImageTag: str
        :param Repository: 镜像所在远程仓库的路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Repository: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageTag = None
        self.Repository = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageTag = params.get("ImageTag")
        self.Repository = params.get("Repository")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceK8SDetailInfo(AbstractModel):
    """表示K8S资产专属的详情。

    """

    def __init__(self):
        r"""
        :param ClusterName: K8S集群的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        """
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompliancePeriodTask(AbstractModel):
    """表示一个合规基线检测定时任务的信息。

    """

    def __init__(self):
        r"""
        :param PeriodTaskId: 周期任务的ID
        :type PeriodTaskId: int
        :param AssetType: 资产类型。
ASSET_CONTAINER, 容器
ASSET_IMAGE, 镜像
ASSET_HOST, 主机
ASSET_K8S, K8S资产
        :type AssetType: str
        :param LastTriggerTime: 最近一次触发的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTriggerTime: str
        :param TotalPolicyItemCount: 总的检查项数目
        :type TotalPolicyItemCount: int
        :param PeriodRule: 周期设置
        :type PeriodRule: :class:`tencentcloud.tcss.v20201101.models.CompliancePeriodTaskRule`
        :param BenchmarkStandardSet: 合规标准列表
        :type BenchmarkStandardSet: list of ComplianceBenchmarkStandard
        """
        self.PeriodTaskId = None
        self.AssetType = None
        self.LastTriggerTime = None
        self.TotalPolicyItemCount = None
        self.PeriodRule = None
        self.BenchmarkStandardSet = None


    def _deserialize(self, params):
        self.PeriodTaskId = params.get("PeriodTaskId")
        self.AssetType = params.get("AssetType")
        self.LastTriggerTime = params.get("LastTriggerTime")
        self.TotalPolicyItemCount = params.get("TotalPolicyItemCount")
        if params.get("PeriodRule") is not None:
            self.PeriodRule = CompliancePeriodTaskRule()
            self.PeriodRule._deserialize(params.get("PeriodRule"))
        if params.get("BenchmarkStandardSet") is not None:
            self.BenchmarkStandardSet = []
            for item in params.get("BenchmarkStandardSet"):
                obj = ComplianceBenchmarkStandard()
                obj._deserialize(item)
                self.BenchmarkStandardSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompliancePeriodTaskRule(AbstractModel):
    """表示一个定时任务的周期设置

    """

    def __init__(self):
        r"""
        :param Frequency: 执行的频率（几天一次），取值为：1,3,7。
        :type Frequency: int
        :param ExecutionTime: 在这天的什么时间执行，格式为：HH:mm:SS。
        :type ExecutionTime: str
        """
        self.Frequency = None
        self.ExecutionTime = None


    def _deserialize(self, params):
        self.Frequency = params.get("Frequency")
        self.ExecutionTime = params.get("ExecutionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompliancePolicyItemSummary(AbstractModel):
    """表示一条检测项对应的汇总信息。

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemId: 为客户分配的唯一的检测项的ID。
        :type CustomerPolicyItemId: int
        :param BasePolicyItemId: 检测项的原始ID。
        :type BasePolicyItemId: int
        :param Name: 检测项的名称。
        :type Name: str
        :param Category: 检测项所属的类型，枚举字符串。
        :type Category: str
        :param BenchmarkStandardName: 所属的合规标准
        :type BenchmarkStandardName: str
        :param RiskLevel: 威胁等级。RISK_CRITICAL, RISK_HIGH, RISK_MEDIUM, RISK_LOW, RISK_NOTICE。
        :type RiskLevel: str
        :param AssetType: 检测项所属的资产类型
        :type AssetType: str
        :param LastCheckTime: 最近检测的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param CheckStatus: 检测状态

CHECK_INIT, 待检测

CHECK_RUNNING, 检测中

CHECK_FINISHED, 检测完成

CHECK_FAILED, 检测失败
        :type CheckStatus: str
        :param CheckResult: 检测结果。RESULT_PASSED: 通过

RESULT_FAILED: 未通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckResult: str
        :param PassedAssetCount: 通过检测的资产的数目
注意：此字段可能返回 null，表示取不到有效值。
        :type PassedAssetCount: int
        :param FailedAssetCount: 未通过检测的资产的数目
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedAssetCount: int
        :param WhitelistId: 检测项对应的白名单项的ID。如果存在且非0，表示检测项被用户忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type WhitelistId: int
        :param FixSuggestion: 处理建议。
        :type FixSuggestion: str
        :param BenchmarkStandardId: 所属的合规标准的ID
        :type BenchmarkStandardId: int
        """
        self.CustomerPolicyItemId = None
        self.BasePolicyItemId = None
        self.Name = None
        self.Category = None
        self.BenchmarkStandardName = None
        self.RiskLevel = None
        self.AssetType = None
        self.LastCheckTime = None
        self.CheckStatus = None
        self.CheckResult = None
        self.PassedAssetCount = None
        self.FailedAssetCount = None
        self.WhitelistId = None
        self.FixSuggestion = None
        self.BenchmarkStandardId = None


    def _deserialize(self, params):
        self.CustomerPolicyItemId = params.get("CustomerPolicyItemId")
        self.BasePolicyItemId = params.get("BasePolicyItemId")
        self.Name = params.get("Name")
        self.Category = params.get("Category")
        self.BenchmarkStandardName = params.get("BenchmarkStandardName")
        self.RiskLevel = params.get("RiskLevel")
        self.AssetType = params.get("AssetType")
        self.LastCheckTime = params.get("LastCheckTime")
        self.CheckStatus = params.get("CheckStatus")
        self.CheckResult = params.get("CheckResult")
        self.PassedAssetCount = params.get("PassedAssetCount")
        self.FailedAssetCount = params.get("FailedAssetCount")
        self.WhitelistId = params.get("WhitelistId")
        self.FixSuggestion = params.get("FixSuggestion")
        self.BenchmarkStandardId = params.get("BenchmarkStandardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceScanFailedAsset(AbstractModel):
    """表示检测失败的资产的信息。

    """

    def __init__(self):
        r"""
        :param CustomerAssetId: 客户资产的ID。
        :type CustomerAssetId: int
        :param AssetType: 资产类别。
        :type AssetType: str
        :param CheckStatus: 检测状态
CHECK_INIT, 待检测
CHECK_RUNNING, 检测中
CHECK_FINISHED, 检测完成
CHECK_FAILED, 检测失败
        :type CheckStatus: str
        :param AssetName: 资产的名称。
        :type AssetName: str
        :param FailureReason: 资产检测失败的原因。
        :type FailureReason: str
        :param Suggestion: 检测失败的处理建议。
        :type Suggestion: str
        :param CheckTime: 检测的时间。
        :type CheckTime: str
        """
        self.CustomerAssetId = None
        self.AssetType = None
        self.CheckStatus = None
        self.AssetName = None
        self.FailureReason = None
        self.Suggestion = None
        self.CheckTime = None


    def _deserialize(self, params):
        self.CustomerAssetId = params.get("CustomerAssetId")
        self.AssetType = params.get("AssetType")
        self.CheckStatus = params.get("CheckStatus")
        self.AssetName = params.get("AssetName")
        self.FailureReason = params.get("FailureReason")
        self.Suggestion = params.get("Suggestion")
        self.CheckTime = params.get("CheckTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceWhitelistItem(AbstractModel):
    """表示一条白名单记录。

    """

    def __init__(self):
        r"""
        :param WhitelistItemId: 白名单项的ID。
        :type WhitelistItemId: int
        :param CustomerPolicyItemId: 客户检测项的ID。
        :type CustomerPolicyItemId: int
        :param Name: 检测项的名称。
        :type Name: str
        :param StandardName: 合规标准的名称。
        :type StandardName: str
        :param StandardId: 合规标准的ID。
        :type StandardId: int
        :param AffectedAssetCount: 检测项影响的资产的数目。
        :type AffectedAssetCount: int
        :param LastUpdateTime: 最后更新的时间
        :type LastUpdateTime: str
        :param InsertTime: 加入到白名单的时间
        :type InsertTime: str
        """
        self.WhitelistItemId = None
        self.CustomerPolicyItemId = None
        self.Name = None
        self.StandardName = None
        self.StandardId = None
        self.AffectedAssetCount = None
        self.LastUpdateTime = None
        self.InsertTime = None


    def _deserialize(self, params):
        self.WhitelistItemId = params.get("WhitelistItemId")
        self.CustomerPolicyItemId = params.get("CustomerPolicyItemId")
        self.Name = params.get("Name")
        self.StandardName = params.get("StandardName")
        self.StandardId = params.get("StandardId")
        self.AffectedAssetCount = params.get("AffectedAssetCount")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.InsertTime = params.get("InsertTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentInfo(AbstractModel):
    """容器组件信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Version: 版本
        :type Version: str
        """
        self.Name = None
        self.Version = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentsInfo(AbstractModel):
    """组件信息

    """

    def __init__(self):
        r"""
        :param Component: 组件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Component: str
        :param Version: 组件版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self.Component = None
        self.Version = None


    def _deserialize(self, params):
        self.Component = params.get("Component")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerInfo(AbstractModel):
    """容器列表集合

    """

    def __init__(self):
        r"""
        :param ContainerID: 容器id
        :type ContainerID: str
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param Status: 容器运行状态
        :type Status: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param RunAs: 运行用户
        :type RunAs: str
        :param Cmd: 命令行
        :type Cmd: str
        :param CPUUsage: CPU使用率 *1000
        :type CPUUsage: int
        :param RamUsage: 内存使用 kb
        :type RamUsage: int
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageID: 镜像id
        :type ImageID: str
        :param POD: 镜像id
        :type POD: str
        :param HostID: 主机id
        :type HostID: str
        :param HostIP: 主机ip
        :type HostIP: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param HostName: 主机名称
        :type HostName: str
        :param PublicIp: 外网ip
        :type PublicIp: str
        """
        self.ContainerID = None
        self.ContainerName = None
        self.Status = None
        self.CreateTime = None
        self.RunAs = None
        self.Cmd = None
        self.CPUUsage = None
        self.RamUsage = None
        self.ImageName = None
        self.ImageID = None
        self.POD = None
        self.HostID = None
        self.HostIP = None
        self.UpdateTime = None
        self.HostName = None
        self.PublicIp = None


    def _deserialize(self, params):
        self.ContainerID = params.get("ContainerID")
        self.ContainerName = params.get("ContainerName")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.RunAs = params.get("RunAs")
        self.Cmd = params.get("Cmd")
        self.CPUUsage = params.get("CPUUsage")
        self.RamUsage = params.get("RamUsage")
        self.ImageName = params.get("ImageName")
        self.ImageID = params.get("ImageID")
        self.POD = params.get("POD")
        self.HostID = params.get("HostID")
        self.HostIP = params.get("HostIP")
        self.UpdateTime = params.get("UpdateTime")
        self.HostName = params.get("HostName")
        self.PublicIp = params.get("PublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerMount(AbstractModel):
    """容器挂载信息

    """

    def __init__(self):
        r"""
        :param Type: 挂载类型 bind
        :type Type: str
        :param Source: 宿主机路径
        :type Source: str
        :param Destination: 容器内路径
        :type Destination: str
        :param Mode: 模式
        :type Mode: str
        :param RW: 读写权限
        :type RW: bool
        :param Propagation: 传播类型
        :type Propagation: str
        :param Name: 名称
        :type Name: str
        :param Driver: 驱动
        :type Driver: str
        """
        self.Type = None
        self.Source = None
        self.Destination = None
        self.Mode = None
        self.RW = None
        self.Propagation = None
        self.Name = None
        self.Driver = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Source = params.get("Source")
        self.Destination = params.get("Destination")
        self.Mode = params.get("Mode")
        self.RW = params.get("RW")
        self.Propagation = params.get("Propagation")
        self.Name = params.get("Name")
        self.Driver = params.get("Driver")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerNetwork(AbstractModel):
    """容器网络信息

    """

    def __init__(self):
        r"""
        :param EndpointID: endpoint id
        :type EndpointID: str
        :param Mode: 模式:bridge
        :type Mode: str
        :param Name: 网络名称
        :type Name: str
        :param NetworkID: 网络ID
        :type NetworkID: str
        :param Gateway: 网关
        :type Gateway: str
        :param Ipv4: IPV4地址
        :type Ipv4: str
        :param Ipv6: IPV6地址
        :type Ipv6: str
        :param MAC: MAC 地址
        :type MAC: str
        """
        self.EndpointID = None
        self.Mode = None
        self.Name = None
        self.NetworkID = None
        self.Gateway = None
        self.Ipv4 = None
        self.Ipv6 = None
        self.MAC = None


    def _deserialize(self, params):
        self.EndpointID = params.get("EndpointID")
        self.Mode = params.get("Mode")
        self.Name = params.get("Name")
        self.NetworkID = params.get("NetworkID")
        self.Gateway = params.get("Gateway")
        self.Ipv4 = params.get("Ipv4")
        self.Ipv6 = params.get("Ipv6")
        self.MAC = params.get("MAC")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetImageRegistryScanTaskOneKeyRequest(AbstractModel):
    """CreateAssetImageRegistryScanTaskOneKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param All: 是否扫描全部镜像
        :type All: bool
        :param Images: 扫描的镜像列表
        :type Images: list of ImageInfo
        :param ScanType: 扫描类型数组
        :type ScanType: list of str
        :param Id: 扫描的镜像列表Id
        :type Id: list of int non-negative
        """
        self.All = None
        self.Images = None
        self.ScanType = None
        self.Id = None


    def _deserialize(self, params):
        self.All = params.get("All")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.Images.append(obj)
        self.ScanType = params.get("ScanType")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetImageRegistryScanTaskOneKeyResponse(AbstractModel):
    """CreateAssetImageRegistryScanTaskOneKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAssetImageRegistryScanTaskRequest(AbstractModel):
    """CreateAssetImageRegistryScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param All: 是否扫描全部镜像
        :type All: bool
        :param Images: 扫描的镜像列表
        :type Images: list of ImageInfo
        :param ScanType: 扫描类型数组
        :type ScanType: list of str
        :param Id: 扫描的镜像列表
        :type Id: list of int non-negative
        :param Filters: 过滤条件
        :type Filters: list of AssetFilters
        :param ExcludeImageList: 不需要扫描的镜像列表, 与Filters配合使用
        :type ExcludeImageList: list of int non-negative
        :param OnlyScanLatest: 是否仅扫描各repository最新版的镜像, 与Filters配合使用
        :type OnlyScanLatest: bool
        """
        self.All = None
        self.Images = None
        self.ScanType = None
        self.Id = None
        self.Filters = None
        self.ExcludeImageList = None
        self.OnlyScanLatest = None


    def _deserialize(self, params):
        self.All = params.get("All")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.Images.append(obj)
        self.ScanType = params.get("ScanType")
        self.Id = params.get("Id")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ExcludeImageList = params.get("ExcludeImageList")
        self.OnlyScanLatest = params.get("OnlyScanLatest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetImageRegistryScanTaskResponse(AbstractModel):
    """CreateAssetImageRegistryScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAssetImageScanSettingRequest(AbstractModel):
    """CreateAssetImageScanSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param Enable: 开关
        :type Enable: bool
        :param ScanTime: 扫描时间
        :type ScanTime: str
        :param ScanPeriod: 扫描周期
        :type ScanPeriod: int
        :param ScanVirus: 扫描木马
        :type ScanVirus: bool
        :param ScanRisk: 扫描敏感信息
        :type ScanRisk: bool
        :param ScanVul: 扫描漏洞
        :type ScanVul: bool
        :param All: 全部镜像
        :type All: bool
        :param Images: 自定义镜像
        :type Images: list of str
        """
        self.Enable = None
        self.ScanTime = None
        self.ScanPeriod = None
        self.ScanVirus = None
        self.ScanRisk = None
        self.ScanVul = None
        self.All = None
        self.Images = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.ScanTime = params.get("ScanTime")
        self.ScanPeriod = params.get("ScanPeriod")
        self.ScanVirus = params.get("ScanVirus")
        self.ScanRisk = params.get("ScanRisk")
        self.ScanVul = params.get("ScanVul")
        self.All = params.get("All")
        self.Images = params.get("Images")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetImageScanSettingResponse(AbstractModel):
    """CreateAssetImageScanSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAssetImageScanTaskRequest(AbstractModel):
    """CreateAssetImageScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param All: 是否扫描全部镜像
        :type All: bool
        :param Images: 需要扫描的镜像列表
        :type Images: list of str
        :param ScanVul: 扫描漏洞
        :type ScanVul: bool
        :param ScanVirus: 扫描木马
        :type ScanVirus: bool
        :param ScanRisk: 扫描风险
        :type ScanRisk: bool
        """
        self.All = None
        self.Images = None
        self.ScanVul = None
        self.ScanVirus = None
        self.ScanRisk = None


    def _deserialize(self, params):
        self.All = params.get("All")
        self.Images = params.get("Images")
        self.ScanVul = params.get("ScanVul")
        self.ScanVirus = params.get("ScanVirus")
        self.ScanRisk = params.get("ScanRisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetImageScanTaskResponse(AbstractModel):
    """CreateAssetImageScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class CreateCheckComponentRequest(AbstractModel):
    """CreateCheckComponent请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterInfoList: 要安装的集群列表信息
        :type ClusterInfoList: list of ClusterCreateComponentItem
        """
        self.ClusterInfoList = None


    def _deserialize(self, params):
        if params.get("ClusterInfoList") is not None:
            self.ClusterInfoList = []
            for item in params.get("ClusterInfoList"):
                obj = ClusterCreateComponentItem()
                obj._deserialize(item)
                self.ClusterInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCheckComponentResponse(AbstractModel):
    """CreateCheckComponent返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstallResult: "InstallSucc"表示安装成功，"InstallFailed"表示安装失败
        :type InstallResult: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstallResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstallResult = params.get("InstallResult")
        self.RequestId = params.get("RequestId")


class CreateClusterCheckTaskRequest(AbstractModel):
    """CreateClusterCheckTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterCheckTaskList: 指定要扫描的集群信息
        :type ClusterCheckTaskList: list of ClusterCheckTaskItem
        """
        self.ClusterCheckTaskList = None


    def _deserialize(self, params):
        if params.get("ClusterCheckTaskList") is not None:
            self.ClusterCheckTaskList = []
            for item in params.get("ClusterCheckTaskList"):
                obj = ClusterCheckTaskItem()
                obj._deserialize(item)
                self.ClusterCheckTaskList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterCheckTaskResponse(AbstractModel):
    """CreateClusterCheckTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的集群检查任务的ID，为0表示创建失败。
        :type TaskId: int
        :param CreateResult: 创建检查任务的结果，"Succ"为成功，其他的为失败原因
        :type CreateResult: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.CreateResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.CreateResult = params.get("CreateResult")
        self.RequestId = params.get("RequestId")


class CreateComplianceTaskRequest(AbstractModel):
    """CreateComplianceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetTypeSet: 指定要扫描的资产类型列表。
ASSET_CONTAINER, 容器
ASSET_IMAGE, 镜像
ASSET_HOST, 主机
ASSET_K8S, K8S资产
AssetTypeSet, PolicySetId, PeriodTaskId三个参数，必须要给其中一个参数填写有效的值。
        :type AssetTypeSet: list of str
        :param PolicySetId: 按照策略集ID指定的策略执行合规检查。
        :type PolicySetId: int
        :param PeriodTaskId: 按照定时任务ID指定的策略执行合规检查。
        :type PeriodTaskId: int
        """
        self.AssetTypeSet = None
        self.PolicySetId = None
        self.PeriodTaskId = None


    def _deserialize(self, params):
        self.AssetTypeSet = params.get("AssetTypeSet")
        self.PolicySetId = params.get("PolicySetId")
        self.PeriodTaskId = params.get("PeriodTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateComplianceTaskResponse(AbstractModel):
    """CreateComplianceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的合规检查任务的ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateExportComplianceStatusListJobRequest(AbstractModel):
    """CreateExportComplianceStatusListJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetType: 要导出信息的资产类型
        :type AssetType: str
        :param ExportByAsset: 按照检测项导出，还是按照资产导出。true: 按照资产导出；false: 按照检测项导出。
        :type ExportByAsset: bool
        :param ExportAll: true, 全部导出；false, 根据IdList来导出数据。
        :type ExportAll: bool
        :param IdList: 要导出的资产ID列表或检测项ID列表，由ExportByAsset的取值决定。
        :type IdList: list of int non-negative
        """
        self.AssetType = None
        self.ExportByAsset = None
        self.ExportAll = None
        self.IdList = None


    def _deserialize(self, params):
        self.AssetType = params.get("AssetType")
        self.ExportByAsset = params.get("ExportByAsset")
        self.ExportAll = params.get("ExportAll")
        self.IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExportComplianceStatusListJobResponse(AbstractModel):
    """CreateExportComplianceStatusListJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 返回创建的导出任务的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateOrModifyPostPayCoresRequest(AbstractModel):
    """CreateOrModifyPostPayCores请求参数结构体

    """

    def __init__(self):
        r"""
        :param CoresCnt: 弹性计费上限，最小值500
        :type CoresCnt: int
        """
        self.CoresCnt = None


    def _deserialize(self, params):
        self.CoresCnt = params.get("CoresCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrModifyPostPayCoresResponse(AbstractModel):
    """CreateOrModifyPostPayCores返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRefreshTaskRequest(AbstractModel):
    """CreateRefreshTask请求参数结构体

    """


class CreateRefreshTaskResponse(AbstractModel):
    """CreateRefreshTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的集群检查任务的ID，为0表示创建失败。
        :type TaskId: int
        :param CreateResult: 创建检查任务的结果，"Succ"为成功，"Failed"为失败
        :type CreateResult: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.CreateResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.CreateResult = params.get("CreateResult")
        self.RequestId = params.get("RequestId")


class CreateVirusScanAgainRequest(AbstractModel):
    """CreateVirusScanAgain请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ContainerIds: 需要扫描的容器id集合
        :type ContainerIds: list of str
        :param TimeoutAll: 是否是扫描全部超时的
        :type TimeoutAll: bool
        :param Timeout: 重新设置的超时时长
        :type Timeout: int
        """
        self.TaskId = None
        self.ContainerIds = None
        self.TimeoutAll = None
        self.Timeout = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ContainerIds = params.get("ContainerIds")
        self.TimeoutAll = params.get("TimeoutAll")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVirusScanAgainResponse(AbstractModel):
    """CreateVirusScanAgain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVirusScanTaskRequest(AbstractModel):
    """CreateVirusScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScanPathAll: 是否扫描所有路径
        :type ScanPathAll: bool
        :param ScanRangeType: 扫描范围0容器1主机节点
        :type ScanRangeType: int
        :param ScanRangeAll: true 全选，false 自选
        :type ScanRangeAll: bool
        :param Timeout: 超时时长，单位小时
        :type Timeout: int
        :param ScanPathType: 当ScanPathAll为false生效 0扫描以下路径 1、扫描除以下路径
        :type ScanPathType: int
        :param ScanIds: 自选扫描范围的容器id或者主机id 根据ScanRangeType决定
        :type ScanIds: list of str
        :param ScanPath: 自选排除或扫描的地址
        :type ScanPath: list of str
        """
        self.ScanPathAll = None
        self.ScanRangeType = None
        self.ScanRangeAll = None
        self.Timeout = None
        self.ScanPathType = None
        self.ScanIds = None
        self.ScanPath = None


    def _deserialize(self, params):
        self.ScanPathAll = params.get("ScanPathAll")
        self.ScanRangeType = params.get("ScanRangeType")
        self.ScanRangeAll = params.get("ScanRangeAll")
        self.Timeout = params.get("Timeout")
        self.ScanPathType = params.get("ScanPathType")
        self.ScanIds = params.get("ScanIds")
        self.ScanPath = params.get("ScanPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVirusScanTaskResponse(AbstractModel):
    """CreateVirusScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class DeleteAbnormalProcessRulesRequest(AbstractModel):
    """DeleteAbnormalProcessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleIdSet: 策略的ids
        :type RuleIdSet: list of str
        """
        self.RuleIdSet = None


    def _deserialize(self, params):
        self.RuleIdSet = params.get("RuleIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAbnormalProcessRulesResponse(AbstractModel):
    """DeleteAbnormalProcessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAccessControlRulesRequest(AbstractModel):
    """DeleteAccessControlRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleIdSet: 策略的ids
        :type RuleIdSet: list of str
        """
        self.RuleIdSet = None


    def _deserialize(self, params):
        self.RuleIdSet = params.get("RuleIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessControlRulesResponse(AbstractModel):
    """DeleteAccessControlRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCompliancePolicyItemFromWhitelistRequest(AbstractModel):
    """DeleteCompliancePolicyItemFromWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param WhitelistIdSet: 指定的白名单项的ID的列表
        :type WhitelistIdSet: list of int non-negative
        """
        self.WhitelistIdSet = None


    def _deserialize(self, params):
        self.WhitelistIdSet = params.get("WhitelistIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompliancePolicyItemFromWhitelistResponse(AbstractModel):
    """DeleteCompliancePolicyItemFromWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReverseShellWhiteListsRequest(AbstractModel):
    """DeleteReverseShellWhiteLists请求参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListIdSet: 白名单ids
        :type WhiteListIdSet: list of str
        """
        self.WhiteListIdSet = None


    def _deserialize(self, params):
        self.WhiteListIdSet = params.get("WhiteListIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReverseShellWhiteListsResponse(AbstractModel):
    """DeleteReverseShellWhiteLists返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRiskSyscallWhiteListsRequest(AbstractModel):
    """DeleteRiskSyscallWhiteLists请求参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListIdSet: 白名单ids
        :type WhiteListIdSet: list of str
        """
        self.WhiteListIdSet = None


    def _deserialize(self, params):
        self.WhiteListIdSet = params.get("WhiteListIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRiskSyscallWhiteListsResponse(AbstractModel):
    """DeleteRiskSyscallWhiteLists返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAbnormalProcessDetailRequest(AbstractModel):
    """DescribeAbnormalProcessDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventId: 事件唯一id
        :type EventId: str
        """
        self.EventId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalProcessDetailResponse(AbstractModel):
    """DescribeAbnormalProcessDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventBaseInfo: 事件基本信息
        :type EventBaseInfo: :class:`tencentcloud.tcss.v20201101.models.RunTimeEventBaseInfo`
        :param ProcessInfo: 进程信息
        :type ProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessDetailInfo`
        :param ParentProcessInfo: 父进程信息
        :type ParentProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessDetailBaseInfo`
        :param EventDetail: 事件描述
        :type EventDetail: :class:`tencentcloud.tcss.v20201101.models.AbnormalProcessEventDescription`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.ParentProcessInfo = None
        self.EventDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventBaseInfo") is not None:
            self.EventBaseInfo = RunTimeEventBaseInfo()
            self.EventBaseInfo._deserialize(params.get("EventBaseInfo"))
        if params.get("ProcessInfo") is not None:
            self.ProcessInfo = ProcessDetailInfo()
            self.ProcessInfo._deserialize(params.get("ProcessInfo"))
        if params.get("ParentProcessInfo") is not None:
            self.ParentProcessInfo = ProcessDetailBaseInfo()
            self.ParentProcessInfo._deserialize(params.get("ParentProcessInfo"))
        if params.get("EventDetail") is not None:
            self.EventDetail = AbnormalProcessEventDescription()
            self.EventDetail._deserialize(params.get("EventDetail"))
        self.RequestId = params.get("RequestId")


class DescribeAbnormalProcessEventsExportRequest(AbstractModel):
    """DescribeAbnormalProcessEventsExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalProcessEventsExportResponse(AbstractModel):
    """DescribeAbnormalProcessEventsExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: execle下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAbnormalProcessEventsRequest(AbstractModel):
    """DescribeAbnormalProcessEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalProcessEventsResponse(AbstractModel):
    """DescribeAbnormalProcessEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param EventSet: 异常进程数组
        :type EventSet: list of AbnormalProcessEventInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = AbnormalProcessEventInfo()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAbnormalProcessRuleDetailRequest(AbstractModel):
    """DescribeAbnormalProcessRuleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 策略唯一id
        :type RuleId: str
        :param ImageId: 镜像id, 在添加白名单的时候使用
        :type ImageId: str
        """
        self.RuleId = None
        self.ImageId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalProcessRuleDetailResponse(AbstractModel):
    """DescribeAbnormalProcessRuleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleDetail: 异常进程策略详细信息
        :type RuleDetail: :class:`tencentcloud.tcss.v20201101.models.AbnormalProcessRuleInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleDetail") is not None:
            self.RuleDetail = AbnormalProcessRuleInfo()
            self.RuleDetail._deserialize(params.get("RuleDetail"))
        self.RequestId = params.get("RequestId")


class DescribeAbnormalProcessRulesExportRequest(AbstractModel):
    """DescribeAbnormalProcessRulesExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalProcessRulesExportResponse(AbstractModel):
    """DescribeAbnormalProcessRulesExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: execle下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAbnormalProcessRulesRequest(AbstractModel):
    """DescribeAbnormalProcessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalProcessRulesResponse(AbstractModel):
    """DescribeAbnormalProcessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param RuleSet: 异常进程策略信息列表
        :type RuleSet: list of RuleBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleBaseInfo()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccessControlDetailRequest(AbstractModel):
    """DescribeAccessControlDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventId: 事件唯一id
        :type EventId: str
        """
        self.EventId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessControlDetailResponse(AbstractModel):
    """DescribeAccessControlDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventBaseInfo: 事件基本信息
        :type EventBaseInfo: :class:`tencentcloud.tcss.v20201101.models.RunTimeEventBaseInfo`
        :param ProcessInfo: 进程信息
        :type ProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessDetailInfo`
        :param TamperedFileInfo: 被篡改信息
        :type TamperedFileInfo: :class:`tencentcloud.tcss.v20201101.models.FileAttributeInfo`
        :param EventDetail: 事件描述
        :type EventDetail: :class:`tencentcloud.tcss.v20201101.models.AccessControlEventDescription`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.TamperedFileInfo = None
        self.EventDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventBaseInfo") is not None:
            self.EventBaseInfo = RunTimeEventBaseInfo()
            self.EventBaseInfo._deserialize(params.get("EventBaseInfo"))
        if params.get("ProcessInfo") is not None:
            self.ProcessInfo = ProcessDetailInfo()
            self.ProcessInfo._deserialize(params.get("ProcessInfo"))
        if params.get("TamperedFileInfo") is not None:
            self.TamperedFileInfo = FileAttributeInfo()
            self.TamperedFileInfo._deserialize(params.get("TamperedFileInfo"))
        if params.get("EventDetail") is not None:
            self.EventDetail = AccessControlEventDescription()
            self.EventDetail._deserialize(params.get("EventDetail"))
        self.RequestId = params.get("RequestId")


class DescribeAccessControlEventsExportRequest(AbstractModel):
    """DescribeAccessControlEventsExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessControlEventsExportResponse(AbstractModel):
    """DescribeAccessControlEventsExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: execle下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAccessControlEventsRequest(AbstractModel):
    """DescribeAccessControlEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessControlEventsResponse(AbstractModel):
    """DescribeAccessControlEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param EventSet: 访问控制事件数组
        :type EventSet: list of AccessControlEventInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = AccessControlEventInfo()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccessControlRuleDetailRequest(AbstractModel):
    """DescribeAccessControlRuleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 策略唯一id
        :type RuleId: str
        :param ImageId: 镜像id, 仅仅在事件加白的时候使用
        :type ImageId: str
        """
        self.RuleId = None
        self.ImageId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessControlRuleDetailResponse(AbstractModel):
    """DescribeAccessControlRuleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleDetail: 运行时策略详细信息
        :type RuleDetail: :class:`tencentcloud.tcss.v20201101.models.AccessControlRuleInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleDetail") is not None:
            self.RuleDetail = AccessControlRuleInfo()
            self.RuleDetail._deserialize(params.get("RuleDetail"))
        self.RequestId = params.get("RequestId")


class DescribeAccessControlRulesExportRequest(AbstractModel):
    """DescribeAccessControlRulesExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessControlRulesExportResponse(AbstractModel):
    """DescribeAccessControlRulesExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: execle下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAccessControlRulesRequest(AbstractModel):
    """DescribeAccessControlRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessControlRulesResponse(AbstractModel):
    """DescribeAccessControlRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param RuleSet: 访问控制策略信息列表
        :type RuleSet: list of RuleBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleBaseInfo()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAffectedClusterCountRequest(AbstractModel):
    """DescribeAffectedClusterCount请求参数结构体

    """


class DescribeAffectedClusterCountResponse(AbstractModel):
    """DescribeAffectedClusterCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param SeriousRiskClusterCount: 严重风险的集群数量
        :type SeriousRiskClusterCount: int
        :param HighRiskClusterCount: 高危风险的集群数量
        :type HighRiskClusterCount: int
        :param MiddleRiskClusterCount: 中危风险的集群数量
        :type MiddleRiskClusterCount: int
        :param HintRiskClusterCount: 低危风险的集群数量
        :type HintRiskClusterCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SeriousRiskClusterCount = None
        self.HighRiskClusterCount = None
        self.MiddleRiskClusterCount = None
        self.HintRiskClusterCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SeriousRiskClusterCount = params.get("SeriousRiskClusterCount")
        self.HighRiskClusterCount = params.get("HighRiskClusterCount")
        self.MiddleRiskClusterCount = params.get("MiddleRiskClusterCount")
        self.HintRiskClusterCount = params.get("HintRiskClusterCount")
        self.RequestId = params.get("RequestId")


class DescribeAffectedNodeListRequest(AbstractModel):
    """DescribeAffectedNodeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CheckItemId: 唯一的检测项的ID
        :type CheckItemId: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每次查询的最大记录数量
        :type Limit: int
        :param Filters: Name - String
Name 可取值：ClusterName, ClusterId,InstanceId,PrivateIpAddresses
        :type Filters: list of ComplianceFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.CheckItemId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.CheckItemId = params.get("CheckItemId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAffectedNodeListResponse(AbstractModel):
    """DescribeAffectedNodeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 受影响的节点总数
        :type TotalCount: int
        :param AffectedNodeList: 受影响的节点列表
        :type AffectedNodeList: list of AffectedNodeItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AffectedNodeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AffectedNodeList") is not None:
            self.AffectedNodeList = []
            for item in params.get("AffectedNodeList"):
                obj = AffectedNodeItem()
                obj._deserialize(item)
                self.AffectedNodeList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAffectedWorkloadListRequest(AbstractModel):
    """DescribeAffectedWorkloadList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CheckItemId: 唯一的检测项的ID
        :type CheckItemId: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每次查询的最大记录数量
        :type Limit: int
        :param Filters: Name - String
Name 可取值：WorkloadType,ClusterId
        :type Filters: list of ComplianceFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.CheckItemId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.CheckItemId = params.get("CheckItemId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAffectedWorkloadListResponse(AbstractModel):
    """DescribeAffectedWorkloadList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 受影响的workload列表数量
        :type TotalCount: int
        :param AffectedWorkloadList: 受影响的workload列表
        :type AffectedWorkloadList: list of AffectedWorkloadItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AffectedWorkloadList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AffectedWorkloadList") is not None:
            self.AffectedWorkloadList = []
            for item in params.get("AffectedWorkloadList"):
                obj = AffectedWorkloadItem()
                obj._deserialize(item)
                self.AffectedWorkloadList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetAppServiceListRequest(AbstractModel):
    """DescribeAssetAppServiceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords- String - 是否必填：否 - 模糊查询可选字段</li>
        :type Filters: list of AssetFilters
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
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetAppServiceListResponse(AbstractModel):
    """DescribeAssetAppServiceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: db服务列表
        :type List: list of ServiceInfo
        :param TotalCount: 总数量
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
                obj = ServiceInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetComponentListRequest(AbstractModel):
    """DescribeAssetComponentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerID: 容器id
        :type ContainerID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件
        :type Filters: list of AssetFilters
        """
        self.ContainerID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ContainerID = params.get("ContainerID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetComponentListResponse(AbstractModel):
    """DescribeAssetComponentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 组件列表
        :type List: list of ComponentInfo
        :param TotalCount: 总数量
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
                obj = ComponentInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetContainerDetailRequest(AbstractModel):
    """DescribeAssetContainerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerId: 容器id
        :type ContainerId: str
        """
        self.ContainerId = None


    def _deserialize(self, params):
        self.ContainerId = params.get("ContainerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetContainerDetailResponse(AbstractModel):
    """DescribeAssetContainerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param HostID: 主机id
        :type HostID: str
        :param HostIP: 主机ip
        :type HostIP: str
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param Status: 运行状态
        :type Status: str
        :param RunAs: 运行账户
        :type RunAs: str
        :param Cmd: 命令行
        :type Cmd: str
        :param CPUUsage: CPU使用率 * 1000
        :type CPUUsage: int
        :param RamUsage: 内存使用 KB
        :type RamUsage: int
        :param ImageName: 镜像名
        :type ImageName: str
        :param ImageID: 镜像ID
        :type ImageID: str
        :param POD: 归属POD
        :type POD: str
        :param K8sMaster: k8s 主节点
        :type K8sMaster: str
        :param ProcessCnt: 容器内进程数
        :type ProcessCnt: int
        :param PortCnt: 容器内端口数
        :type PortCnt: int
        :param ComponentCnt: 组件数
        :type ComponentCnt: int
        :param AppCnt: app数
        :type AppCnt: int
        :param WebServiceCnt: websvc数
        :type WebServiceCnt: int
        :param Mounts: 挂载
        :type Mounts: list of ContainerMount
        :param Network: 容器网络信息
        :type Network: :class:`tencentcloud.tcss.v20201101.models.ContainerNetwork`
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ImageCreateTime: 镜像创建时间
        :type ImageCreateTime: str
        :param ImageSize: 镜像大小
        :type ImageSize: int
        :param HostStatus: 主机状态 offline,online,pause
        :type HostStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HostID = None
        self.HostIP = None
        self.ContainerName = None
        self.Status = None
        self.RunAs = None
        self.Cmd = None
        self.CPUUsage = None
        self.RamUsage = None
        self.ImageName = None
        self.ImageID = None
        self.POD = None
        self.K8sMaster = None
        self.ProcessCnt = None
        self.PortCnt = None
        self.ComponentCnt = None
        self.AppCnt = None
        self.WebServiceCnt = None
        self.Mounts = None
        self.Network = None
        self.CreateTime = None
        self.ImageCreateTime = None
        self.ImageSize = None
        self.HostStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HostID = params.get("HostID")
        self.HostIP = params.get("HostIP")
        self.ContainerName = params.get("ContainerName")
        self.Status = params.get("Status")
        self.RunAs = params.get("RunAs")
        self.Cmd = params.get("Cmd")
        self.CPUUsage = params.get("CPUUsage")
        self.RamUsage = params.get("RamUsage")
        self.ImageName = params.get("ImageName")
        self.ImageID = params.get("ImageID")
        self.POD = params.get("POD")
        self.K8sMaster = params.get("K8sMaster")
        self.ProcessCnt = params.get("ProcessCnt")
        self.PortCnt = params.get("PortCnt")
        self.ComponentCnt = params.get("ComponentCnt")
        self.AppCnt = params.get("AppCnt")
        self.WebServiceCnt = params.get("WebServiceCnt")
        if params.get("Mounts") is not None:
            self.Mounts = []
            for item in params.get("Mounts"):
                obj = ContainerMount()
                obj._deserialize(item)
                self.Mounts.append(obj)
        if params.get("Network") is not None:
            self.Network = ContainerNetwork()
            self.Network._deserialize(params.get("Network"))
        self.CreateTime = params.get("CreateTime")
        self.ImageCreateTime = params.get("ImageCreateTime")
        self.ImageSize = params.get("ImageSize")
        self.HostStatus = params.get("HostStatus")
        self.RequestId = params.get("RequestId")


class DescribeAssetContainerListRequest(AbstractModel):
    """DescribeAssetContainerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ContainerName - String - 是否必填：否 - 容器名称模糊搜索</li>
<li>Status - String - 是否必填：否 - 容器运行状态筛选，0："created",1："running", 2："paused", 3："restarting", 4："removing", 5："exited", 6："dead" </li>
<li>Runas - String - 是否必填：否 - 运行用户筛选</li>
<li>ImageName- String - 是否必填：否 - 镜像名称搜索</li>
<li>HostIP- string - 是否必填：否 - 主机ip搜索</li>
<li>OrderBy - String 是否必填：否 -排序字段，支持：cpu_usage, mem_usage的动态排序 ["cpu_usage","+"]  '+'升序、'-'降序</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetContainerListResponse(AbstractModel):
    """DescribeAssetContainerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 容器列表
        :type List: list of ContainerInfo
        :param TotalCount: 总数量
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
                obj = ContainerInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetDBServiceListRequest(AbstractModel):
    """DescribeAssetDBServiceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords- String - 是否必填：否 - 模糊查询可选字段</li>
        :type Filters: list of AssetFilters
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
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDBServiceListResponse(AbstractModel):
    """DescribeAssetDBServiceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: db服务列表
        :type List: list of ServiceInfo
        :param TotalCount: 总数量
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
                obj = ServiceInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetHostDetailRequest(AbstractModel):
    """DescribeAssetHostDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param HostId: 主机id
        :type HostId: str
        """
        self.HostId = None


    def _deserialize(self, params):
        self.HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetHostDetailResponse(AbstractModel):
    """DescribeAssetHostDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param UUID: 云镜uuid
        :type UUID: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param HostName: 主机名
        :type HostName: str
        :param Group: 主机分组
        :type Group: str
        :param HostIP: 主机IP
        :type HostIP: str
        :param OsName: 操作系统
        :type OsName: str
        :param AgentVersion: agent版本
        :type AgentVersion: str
        :param KernelVersion: 内核版本
        :type KernelVersion: str
        :param DockerVersion: docker版本
        :type DockerVersion: str
        :param DockerAPIVersion: docker api版本
        :type DockerAPIVersion: str
        :param DockerGoVersion: docker go 版本
        :type DockerGoVersion: str
        :param DockerFileSystemDriver: docker 文件系统类型
        :type DockerFileSystemDriver: str
        :param DockerRootDir: docker root 目录
        :type DockerRootDir: str
        :param ImageCnt: 镜像数
        :type ImageCnt: int
        :param ContainerCnt: 容器数
        :type ContainerCnt: int
        :param K8sMasterIP: k8s IP
        :type K8sMasterIP: str
        :param K8sVersion: k8s version
        :type K8sVersion: str
        :param KubeProxyVersion: kube proxy
        :type KubeProxyVersion: str
        :param Status: "UNINSTALL"："未安装","OFFLINE"："离线", "ONLINE"："防护中
        :type Status: str
        :param IsContainerd: 是否Containerd
        :type IsContainerd: bool
        :param MachineType: 主机来源;"TENCENTCLOUD":"腾讯云服务器","OTHERCLOUD":"非腾讯云服务器"
        :type MachineType: str
        :param PublicIp: 外网ip
        :type PublicIp: str
        :param InstanceID: 主机实例ID
        :type InstanceID: str
        :param RegionID: 地域ID
        :type RegionID: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UUID = None
        self.UpdateTime = None
        self.HostName = None
        self.Group = None
        self.HostIP = None
        self.OsName = None
        self.AgentVersion = None
        self.KernelVersion = None
        self.DockerVersion = None
        self.DockerAPIVersion = None
        self.DockerGoVersion = None
        self.DockerFileSystemDriver = None
        self.DockerRootDir = None
        self.ImageCnt = None
        self.ContainerCnt = None
        self.K8sMasterIP = None
        self.K8sVersion = None
        self.KubeProxyVersion = None
        self.Status = None
        self.IsContainerd = None
        self.MachineType = None
        self.PublicIp = None
        self.InstanceID = None
        self.RegionID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UUID = params.get("UUID")
        self.UpdateTime = params.get("UpdateTime")
        self.HostName = params.get("HostName")
        self.Group = params.get("Group")
        self.HostIP = params.get("HostIP")
        self.OsName = params.get("OsName")
        self.AgentVersion = params.get("AgentVersion")
        self.KernelVersion = params.get("KernelVersion")
        self.DockerVersion = params.get("DockerVersion")
        self.DockerAPIVersion = params.get("DockerAPIVersion")
        self.DockerGoVersion = params.get("DockerGoVersion")
        self.DockerFileSystemDriver = params.get("DockerFileSystemDriver")
        self.DockerRootDir = params.get("DockerRootDir")
        self.ImageCnt = params.get("ImageCnt")
        self.ContainerCnt = params.get("ContainerCnt")
        self.K8sMasterIP = params.get("K8sMasterIP")
        self.K8sVersion = params.get("K8sVersion")
        self.KubeProxyVersion = params.get("KubeProxyVersion")
        self.Status = params.get("Status")
        self.IsContainerd = params.get("IsContainerd")
        self.MachineType = params.get("MachineType")
        self.PublicIp = params.get("PublicIp")
        self.InstanceID = params.get("InstanceID")
        self.RegionID = params.get("RegionID")
        self.RequestId = params.get("RequestId")


class DescribeAssetHostListRequest(AbstractModel):
    """DescribeAssetHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - agent状态筛选，"ALL":"全部"(或不传该字段),"UNINSTALL"："未安装","OFFLINE"："离线", "ONLINE"："防护中"</li>
<li>HostName - String - 是否必填：否 - 主机名筛选</li>
<li>Group- String - 是否必填：否 - 主机群组搜索</li>
<li>HostIP- string - 是否必填：否 - 主机ip搜索</li>
<li>HostID- string - 是否必填：否 - 主机id搜索</li>
<li>DockerVersion- string - 是否必填：否 - docker版本搜索</li>
<li>MachineType- string - 是否必填：否 - 主机来源MachineType搜索，"ALL":"全部"(或不传该字段),"TENCENTCLOUD":"腾讯云服务器","OTHERCLOUD":"非腾讯云服务器"</li>
<li>DockerStatus- string - 是否必填：否 - docker安装状态，"ALL":"全部"(或不传该字段),"INSTALL":"已安装","UNINSTALL":"未安装"</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetHostListResponse(AbstractModel):
    """DescribeAssetHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 主机列表
        :type List: list of HostInfo
        :param TotalCount: 总数量
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
                obj = HostInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageBindRuleInfoRequest(AbstractModel):
    """DescribeAssetImageBindRuleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"EventType","Values":[""]}]
EventType取值：
"FILE_ABNORMAL_READ" 访问控制
"MALICE_PROCESS_START" 恶意进程启动
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageBindRuleInfoResponse(AbstractModel):
    """DescribeAssetImageBindRuleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param ImageBindRuleSet: 镜像绑定规则列表
        :type ImageBindRuleSet: list of ImagesBindRuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageBindRuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageBindRuleSet") is not None:
            self.ImageBindRuleSet = []
            for item in params.get("ImageBindRuleSet"):
                obj = ImagesBindRuleInfo()
                obj._deserialize(item)
                self.ImageBindRuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetImageDetailRequest(AbstractModel):
    """DescribeAssetImageDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像id
        :type ImageID: str
        """
        self.ImageID = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageDetailResponse(AbstractModel):
    """DescribeAssetImageDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Size: 镜像大小
        :type Size: int
        :param HostCnt: 关联主机个数
注意：此字段可能返回 null，表示取不到有效值。
        :type HostCnt: int
        :param ContainerCnt: 关联容器个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerCnt: int
        :param ScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTime: str
        :param VulCnt: 漏洞个数
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCnt: int
        :param RiskCnt: 风险行为数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCnt: int
        :param SensitiveInfoCnt: 敏感信息数
注意：此字段可能返回 null，表示取不到有效值。
        :type SensitiveInfoCnt: int
        :param IsTrustImage: 是否信任镜像
        :type IsTrustImage: bool
        :param OsName: 镜像系统
        :type OsName: str
        :param AgentError: agent镜像扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentError: str
        :param ScanError: 后端镜像扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanError: str
        :param Architecture: 系统架构
注意：此字段可能返回 null，表示取不到有效值。
        :type Architecture: str
        :param Author: 作者
注意：此字段可能返回 null，表示取不到有效值。
        :type Author: str
        :param BuildHistory: 构建历史
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildHistory: str
        :param ScanVirusProgress: 木马扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVirusProgress: int
        :param ScanVulProgress: 漏洞扫进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVulProgress: int
        :param ScanRiskProgress: 敏感信息扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRiskProgress: int
        :param ScanVirusError: 木马扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVirusError: str
        :param ScanVulError: 漏洞扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVulError: str
        :param ScanRiskError: 敏感信息错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRiskError: str
        :param ScanStatus: 镜像扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanStatus: str
        :param VirusCnt: 木马病毒数
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusCnt: int
        :param Status: 镜像扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param RemainScanTime: 剩余扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainScanTime: int
        :param IsAuthorized: 授权为：1，未授权为：0
        :type IsAuthorized: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageID = None
        self.ImageName = None
        self.CreateTime = None
        self.Size = None
        self.HostCnt = None
        self.ContainerCnt = None
        self.ScanTime = None
        self.VulCnt = None
        self.RiskCnt = None
        self.SensitiveInfoCnt = None
        self.IsTrustImage = None
        self.OsName = None
        self.AgentError = None
        self.ScanError = None
        self.Architecture = None
        self.Author = None
        self.BuildHistory = None
        self.ScanVirusProgress = None
        self.ScanVulProgress = None
        self.ScanRiskProgress = None
        self.ScanVirusError = None
        self.ScanVulError = None
        self.ScanRiskError = None
        self.ScanStatus = None
        self.VirusCnt = None
        self.Status = None
        self.RemainScanTime = None
        self.IsAuthorized = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.CreateTime = params.get("CreateTime")
        self.Size = params.get("Size")
        self.HostCnt = params.get("HostCnt")
        self.ContainerCnt = params.get("ContainerCnt")
        self.ScanTime = params.get("ScanTime")
        self.VulCnt = params.get("VulCnt")
        self.RiskCnt = params.get("RiskCnt")
        self.SensitiveInfoCnt = params.get("SensitiveInfoCnt")
        self.IsTrustImage = params.get("IsTrustImage")
        self.OsName = params.get("OsName")
        self.AgentError = params.get("AgentError")
        self.ScanError = params.get("ScanError")
        self.Architecture = params.get("Architecture")
        self.Author = params.get("Author")
        self.BuildHistory = params.get("BuildHistory")
        self.ScanVirusProgress = params.get("ScanVirusProgress")
        self.ScanVulProgress = params.get("ScanVulProgress")
        self.ScanRiskProgress = params.get("ScanRiskProgress")
        self.ScanVirusError = params.get("ScanVirusError")
        self.ScanVulError = params.get("ScanVulError")
        self.ScanRiskError = params.get("ScanRiskError")
        self.ScanStatus = params.get("ScanStatus")
        self.VirusCnt = params.get("VirusCnt")
        self.Status = params.get("Status")
        self.RemainScanTime = params.get("RemainScanTime")
        self.IsAuthorized = params.get("IsAuthorized")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageHostListRequest(AbstractModel):
    """DescribeAssetImageHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件 支持ImageID,HostID
        :type Filters: list of AssetFilters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageHostListResponse(AbstractModel):
    """DescribeAssetImageHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像列表
        :type List: list of ImageHost
        :param TotalCount: 总数量
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
                obj = ImageHost()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageListExportRequest(AbstractModel):
    """DescribeAssetImageListExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ImageName- String - 是否必填：否 - 镜像名称筛选，</li>
<li>ScanStatus - String - 是否必填：否 - 镜像扫描状态notScan，scanning，scanned，scanErr</li>
<li>ImageID- String - 是否必填：否 - 镜像ID筛选，</li>
<li>SecurityRisk- String - 是否必填：否 - 安全风险，VulCnt 、VirusCnt、RiskCnt、IsTrustImage</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageListExportResponse(AbstractModel):
    """DescribeAssetImageListExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: excel文件下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageListRequest(AbstractModel):
    """DescribeAssetImageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ImageName- String - 是否必填：否 - 镜像名称筛选，</li>
<li>ScanStatus - String - 是否必填：否 - 镜像扫描状态notScan，scanning，scanned，scanErr</li>
<li>ImageID- String - 是否必填：否 - 镜像ID筛选，</li>
<li>SecurityRisk- String - 是否必填：否 - 安全风险，VulCnt 、VirusCnt、RiskCnt、IsTrustImage</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageListResponse(AbstractModel):
    """DescribeAssetImageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像列表
        :type List: list of ImagesInfo
        :param TotalCount: 总数量
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
                obj = ImagesInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryAssetStatusRequest(AbstractModel):
    """DescribeAssetImageRegistryAssetStatus请求参数结构体

    """


class DescribeAssetImageRegistryAssetStatusResponse(AbstractModel):
    """DescribeAssetImageRegistryAssetStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 更新进度状态,doing更新中，success更新成功，failed失败
        :type Status: str
        :param Err: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Err: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Err = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Err = params.get("Err")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryDetailRequest(AbstractModel):
    """DescribeAssetImageRegistryDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 仓库列表id
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryDetailResponse(AbstractModel):
    """DescribeAssetImageRegistryDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageDigest: 镜像Digest
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageDigest: str
        :param ImageRepoAddress: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageRepoAddress: str
        :param RegistryType: 镜像类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryType: str
        :param ImageName: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageName: str
        :param ImageTag: 镜像版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTag: str
        :param ScanTime: 扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTime: str
        :param ScanStatus: 扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanStatus: str
        :param VulCnt: 安全漏洞数
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCnt: int
        :param VirusCnt: 木马病毒数
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusCnt: int
        :param RiskCnt: 风险行为数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCnt: int
        :param SentiveInfoCnt: 敏感信息数
注意：此字段可能返回 null，表示取不到有效值。
        :type SentiveInfoCnt: int
        :param OsName: 镜像系统
注意：此字段可能返回 null，表示取不到有效值。
        :type OsName: str
        :param ScanVirusError: 木马扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVirusError: str
        :param ScanVulError: 漏洞扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVulError: str
        :param LayerInfo: 层文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LayerInfo: str
        :param InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param ScanRiskError: 高危扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRiskError: str
        :param ScanVirusProgress: 木马信息扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVirusProgress: int
        :param ScanVulProgress: 漏洞扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVulProgress: int
        :param ScanRiskProgress: 敏感扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRiskProgress: int
        :param ScanRemainTime: 剩余扫描时间秒
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRemainTime: int
        :param CveStatus: cve扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CveStatus: str
        :param RiskStatus: 高危扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskStatus: str
        :param VirusStatus: 木马扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusStatus: str
        :param Progress: 总进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param IsAuthorized: 授权状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAuthorized: int
        :param ImageSize: 镜像大小
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSize: int
        :param ImageId: 镜像Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param RegistryRegion: 镜像区域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryRegion: str
        :param ImageCreateTime: 镜像创建的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageDigest = None
        self.ImageRepoAddress = None
        self.RegistryType = None
        self.ImageName = None
        self.ImageTag = None
        self.ScanTime = None
        self.ScanStatus = None
        self.VulCnt = None
        self.VirusCnt = None
        self.RiskCnt = None
        self.SentiveInfoCnt = None
        self.OsName = None
        self.ScanVirusError = None
        self.ScanVulError = None
        self.LayerInfo = None
        self.InstanceId = None
        self.InstanceName = None
        self.Namespace = None
        self.ScanRiskError = None
        self.ScanVirusProgress = None
        self.ScanVulProgress = None
        self.ScanRiskProgress = None
        self.ScanRemainTime = None
        self.CveStatus = None
        self.RiskStatus = None
        self.VirusStatus = None
        self.Progress = None
        self.IsAuthorized = None
        self.ImageSize = None
        self.ImageId = None
        self.RegistryRegion = None
        self.ImageCreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageDigest = params.get("ImageDigest")
        self.ImageRepoAddress = params.get("ImageRepoAddress")
        self.RegistryType = params.get("RegistryType")
        self.ImageName = params.get("ImageName")
        self.ImageTag = params.get("ImageTag")
        self.ScanTime = params.get("ScanTime")
        self.ScanStatus = params.get("ScanStatus")
        self.VulCnt = params.get("VulCnt")
        self.VirusCnt = params.get("VirusCnt")
        self.RiskCnt = params.get("RiskCnt")
        self.SentiveInfoCnt = params.get("SentiveInfoCnt")
        self.OsName = params.get("OsName")
        self.ScanVirusError = params.get("ScanVirusError")
        self.ScanVulError = params.get("ScanVulError")
        self.LayerInfo = params.get("LayerInfo")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Namespace = params.get("Namespace")
        self.ScanRiskError = params.get("ScanRiskError")
        self.ScanVirusProgress = params.get("ScanVirusProgress")
        self.ScanVulProgress = params.get("ScanVulProgress")
        self.ScanRiskProgress = params.get("ScanRiskProgress")
        self.ScanRemainTime = params.get("ScanRemainTime")
        self.CveStatus = params.get("CveStatus")
        self.RiskStatus = params.get("RiskStatus")
        self.VirusStatus = params.get("VirusStatus")
        self.Progress = params.get("Progress")
        self.IsAuthorized = params.get("IsAuthorized")
        self.ImageSize = params.get("ImageSize")
        self.ImageId = params.get("ImageId")
        self.RegistryRegion = params.get("RegistryRegion")
        self.ImageCreateTime = params.get("ImageCreateTime")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryListExportRequest(AbstractModel):
    """DescribeAssetImageRegistryListExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Filters: 排序字段
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式，asc，desc
        :type Order: str
        :param OnlyShowLatest: 是否仅展示repository版本最新的镜像，默认为false
        :type OnlyShowLatest: bool
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None
        self.OnlyShowLatest = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        self.OnlyShowLatest = params.get("OnlyShowLatest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryListExportResponse(AbstractModel):
    """DescribeAssetImageRegistryListExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: excel文件下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryListRequest(AbstractModel):
    """DescribeAssetImageRegistryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Filters: 过滤字段
IsAuthorized是否授权，取值全部all，未授权0，已授权1
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式，asc，desc
        :type Order: str
        :param OnlyShowLatest: 是否仅展示各repository最新的镜像, 默认为false
        :type OnlyShowLatest: bool
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None
        self.OnlyShowLatest = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        self.OnlyShowLatest = params.get("OnlyShowLatest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryListResponse(AbstractModel):
    """DescribeAssetImageRegistryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像仓库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of ImageRepoInfo
        :param TotalCount: 总数量
注意：此字段可能返回 null，表示取不到有效值。
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
                obj = ImageRepoInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryRegistryDetailRequest(AbstractModel):
    """DescribeAssetImageRegistryRegistryDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 仓库唯一id
        :type RegistryId: int
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryRegistryDetailResponse(AbstractModel):
    """DescribeAssetImageRegistryRegistryDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 仓库名
        :type Name: str
        :param Username: 用户名
        :type Username: str
        :param Password: 密码
        :type Password: str
        :param Url: 仓库url
        :type Url: str
        :param RegistryType: 仓库类型，列表：harbor
        :type RegistryType: str
        :param RegistryVersion: 仓库版本
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryVersion: str
        :param NetType: 网络类型，列表：public（公网）
        :type NetType: str
        :param RegistryRegion: 区域，列表:default（默认）
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryRegion: str
        :param SpeedLimit: 限速
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeedLimit: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Username = None
        self.Password = None
        self.Url = None
        self.RegistryType = None
        self.RegistryVersion = None
        self.NetType = None
        self.RegistryRegion = None
        self.SpeedLimit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.Url = params.get("Url")
        self.RegistryType = params.get("RegistryType")
        self.RegistryVersion = params.get("RegistryVersion")
        self.NetType = params.get("NetType")
        self.RegistryRegion = params.get("RegistryRegion")
        self.SpeedLimit = params.get("SpeedLimit")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryRegistryListRequest(AbstractModel):
    """DescribeAssetImageRegistryRegistryList请求参数结构体

    """


class DescribeAssetImageRegistryRegistryListResponse(AbstractModel):
    """DescribeAssetImageRegistryRegistryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryRiskInfoListRequest(AbstractModel):
    """DescribeAssetImageRegistryRiskInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 漏洞级别筛选，</li>
<li>Name - String - 是否必填：否 - 漏洞名称</li>
        :type Filters: list of AssetFilters
        :param ImageInfo: 镜像id
        :type ImageInfo: :class:`tencentcloud.tcss.v20201101.models.ImageInfo`
        :param By: 排序字段（Level）
        :type By: str
        :param Order: 排序方式 + -
        :type Order: str
        :param Id: 镜像标识Id
        :type Id: int
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ImageInfo = None
        self.By = None
        self.Order = None
        self.Id = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.By = params.get("By")
        self.Order = params.get("Order")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryRiskInfoListResponse(AbstractModel):
    """DescribeAssetImageRegistryRiskInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像漏洞列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of ImageRisk
        :param TotalCount: 总数量
注意：此字段可能返回 null，表示取不到有效值。
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
                obj = ImageRisk()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryRiskListExportRequest(AbstractModel):
    """DescribeAssetImageRegistryRiskListExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 漏洞级别筛选，</li>
<li>Name - String - 是否必填：否 - 漏洞名称</li>
        :type Filters: list of AssetFilters
        :param ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tcss.v20201101.models.ImageInfo`
        :param Id: 镜像标识Id
        :type Id: int
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ImageInfo = None
        self.Id = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryRiskListExportResponse(AbstractModel):
    """DescribeAssetImageRegistryRiskListExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: excel文件下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryScanStatusOneKeyRequest(AbstractModel):
    """DescribeAssetImageRegistryScanStatusOneKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param Images: 需要获取进度的镜像列表
        :type Images: list of ImageInfo
        :param All: 是否获取全部镜像
        :type All: bool
        :param Id: 需要获取进度的镜像列表Id
        :type Id: list of int non-negative
        """
        self.Images = None
        self.All = None
        self.Id = None


    def _deserialize(self, params):
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.Images.append(obj)
        self.All = params.get("All")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryScanStatusOneKeyResponse(AbstractModel):
    """DescribeAssetImageRegistryScanStatusOneKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageTotal: 镜像个数
        :type ImageTotal: int
        :param ImageScanCnt: 扫描镜像个数
        :type ImageScanCnt: int
        :param ImageStatus: 扫描进度列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageStatus: list of ImageProgress
        :param SuccessCount: 安全个数
        :type SuccessCount: int
        :param RiskCount: 风险个数
        :type RiskCount: int
        :param Schedule: 总的扫描进度
        :type Schedule: int
        :param Status: 总的扫描状态
        :type Status: str
        :param ScanRemainTime: 扫描剩余时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRemainTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageTotal = None
        self.ImageScanCnt = None
        self.ImageStatus = None
        self.SuccessCount = None
        self.RiskCount = None
        self.Schedule = None
        self.Status = None
        self.ScanRemainTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageTotal = params.get("ImageTotal")
        self.ImageScanCnt = params.get("ImageScanCnt")
        if params.get("ImageStatus") is not None:
            self.ImageStatus = []
            for item in params.get("ImageStatus"):
                obj = ImageProgress()
                obj._deserialize(item)
                self.ImageStatus.append(obj)
        self.SuccessCount = params.get("SuccessCount")
        self.RiskCount = params.get("RiskCount")
        self.Schedule = params.get("Schedule")
        self.Status = params.get("Status")
        self.ScanRemainTime = params.get("ScanRemainTime")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistrySummaryRequest(AbstractModel):
    """DescribeAssetImageRegistrySummary请求参数结构体

    """


class DescribeAssetImageRegistrySummaryResponse(AbstractModel):
    """DescribeAssetImageRegistrySummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryVirusListExportRequest(AbstractModel):
    """DescribeAssetImageRegistryVirusListExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 漏洞级别筛选，</li>
<li>Name - String - 是否必填：否 - 漏洞名称</li>
        :type Filters: list of AssetFilters
        :param ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tcss.v20201101.models.ImageInfo`
        :param Id: 镜像标识Id
        :type Id: int
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ImageInfo = None
        self.Id = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryVirusListExportResponse(AbstractModel):
    """DescribeAssetImageRegistryVirusListExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: excel文件下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryVirusListRequest(AbstractModel):
    """DescribeAssetImageRegistryVirusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 漏洞级别筛选，</li>
<li>Name - String - 是否必填：否 - 漏洞名称</li>
        :type Filters: list of AssetFilters
        :param ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tcss.v20201101.models.ImageInfo`
        :param Id: 镜像标识Id
        :type Id: int
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ImageInfo = None
        self.Id = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryVirusListResponse(AbstractModel):
    """DescribeAssetImageRegistryVirusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像漏洞列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of ImageVirus
        :param TotalCount: 总数量
注意：此字段可能返回 null，表示取不到有效值。
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
                obj = ImageVirus()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryVulListExportRequest(AbstractModel):
    """DescribeAssetImageRegistryVulListExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 漏洞级别筛选，</li>
<li>Name - String - 是否必填：否 - 漏洞名称</li>
        :type Filters: list of AssetFilters
        :param ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tcss.v20201101.models.ImageInfo`
        :param Id: 镜像标识Id
        :type Id: int
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ImageInfo = None
        self.Id = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryVulListExportResponse(AbstractModel):
    """DescribeAssetImageRegistryVulListExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: excel文件下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRegistryVulListRequest(AbstractModel):
    """DescribeAssetImageRegistryVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 漏洞级别筛选，</li>
<li>Name - String - 是否必填：否 - 漏洞名称</li>
        :type Filters: list of AssetFilters
        :param ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tcss.v20201101.models.ImageInfo`
        :param Id: 镜像标识Id
        :type Id: int
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ImageInfo = None
        self.Id = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRegistryVulListResponse(AbstractModel):
    """DescribeAssetImageRegistryVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像漏洞列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of ImageVul
        :param TotalCount: 总数量
注意：此字段可能返回 null，表示取不到有效值。
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
                obj = ImageVul()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRiskListExportRequest(AbstractModel):
    """DescribeAssetImageRiskListExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param ImageID: 镜像id
        :type ImageID: str
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 风险级别 1,2,3,4，</li>
<li>Behavior - String - 是否必填：否 - 风险行为 1,2,3,4</li>
<li>Type - String - 是否必填：否 - 风险类型  1,2,</li>
        :type Filters: list of AssetFilters
        """
        self.ExportField = None
        self.ImageID = None
        self.Filters = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.ImageID = params.get("ImageID")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRiskListExportResponse(AbstractModel):
    """DescribeAssetImageRiskListExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: excel文件下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageRiskListRequest(AbstractModel):
    """DescribeAssetImageRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像id
        :type ImageID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 风险级别 1,2,3,4，</li>
<li>Behavior - String - 是否必填：否 - 风险行为 1,2,3,4</li>
<li>Type - String - 是否必填：否 - 风险类型  1,2,</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式
        :type Order: str
        """
        self.ImageID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageRiskListResponse(AbstractModel):
    """DescribeAssetImageRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像病毒列表
        :type List: list of ImageRiskInfo
        :param TotalCount: 总数量
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
                obj = ImageRiskInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageScanSettingRequest(AbstractModel):
    """DescribeAssetImageScanSetting请求参数结构体

    """


class DescribeAssetImageScanSettingResponse(AbstractModel):
    """DescribeAssetImageScanSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param Enable: 开关
        :type Enable: bool
        :param ScanTime: 扫描时刻(完整时间;后端按0时区解析时分秒)
        :type ScanTime: str
        :param ScanPeriod: 扫描间隔
        :type ScanPeriod: int
        :param ScanVirus: 扫描木马
        :type ScanVirus: bool
        :param ScanRisk: 扫描敏感信息
        :type ScanRisk: bool
        :param ScanVul: 扫描漏洞
        :type ScanVul: bool
        :param All: 扫描全部镜像
        :type All: bool
        :param Images: 自定义扫描镜像
        :type Images: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Enable = None
        self.ScanTime = None
        self.ScanPeriod = None
        self.ScanVirus = None
        self.ScanRisk = None
        self.ScanVul = None
        self.All = None
        self.Images = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.ScanTime = params.get("ScanTime")
        self.ScanPeriod = params.get("ScanPeriod")
        self.ScanVirus = params.get("ScanVirus")
        self.ScanRisk = params.get("ScanRisk")
        self.ScanVul = params.get("ScanVul")
        self.All = params.get("All")
        self.Images = params.get("Images")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageScanStatusRequest(AbstractModel):
    """DescribeAssetImageScanStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        """
        self.TaskID = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageScanStatusResponse(AbstractModel):
    """DescribeAssetImageScanStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageTotal: 镜像个数
        :type ImageTotal: int
        :param ImageScanCnt: 扫描镜像个数
        :type ImageScanCnt: int
        :param Status: 扫描状态
        :type Status: str
        :param Schedule: 扫描进度 ImageScanCnt/ImageTotal *100
        :type Schedule: int
        :param SuccessCount: 安全个数
        :type SuccessCount: int
        :param RiskCount: 风险个数
        :type RiskCount: int
        :param LeftSeconds: 剩余扫描时间
        :type LeftSeconds: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageTotal = None
        self.ImageScanCnt = None
        self.Status = None
        self.Schedule = None
        self.SuccessCount = None
        self.RiskCount = None
        self.LeftSeconds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageTotal = params.get("ImageTotal")
        self.ImageScanCnt = params.get("ImageScanCnt")
        self.Status = params.get("Status")
        self.Schedule = params.get("Schedule")
        self.SuccessCount = params.get("SuccessCount")
        self.RiskCount = params.get("RiskCount")
        self.LeftSeconds = params.get("LeftSeconds")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageScanTaskRequest(AbstractModel):
    """DescribeAssetImageScanTask请求参数结构体

    """


class DescribeAssetImageScanTaskResponse(AbstractModel):
    """DescribeAssetImageScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageSimpleListRequest(AbstractModel):
    """DescribeAssetImageSimpleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords- String - 是否必填：否 - 镜像名、镜像id 称筛选，</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageSimpleListResponse(AbstractModel):
    """DescribeAssetImageSimpleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像列表
        :type List: list of AssetSimpleImageInfo
        :param TotalCount: 总数量
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
                obj = AssetSimpleImageInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageVirusListExportRequest(AbstractModel):
    """DescribeAssetImageVirusListExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 列表支持字段
        :type ExportField: list of str
        :param ImageID: 镜像id
        :type ImageID: str
        :param Filters: 过滤条件。
<li>Name- String - 是否必填：否 - 镜像名称筛选，</li>
<li>RiskLevel - String - 是否必填：否 - 风险等级  1,2,3,4</li>
        :type Filters: list of AssetFilters
        """
        self.ExportField = None
        self.ImageID = None
        self.Filters = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.ImageID = params.get("ImageID")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageVirusListExportResponse(AbstractModel):
    """DescribeAssetImageVirusListExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: excel文件下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageVirusListRequest(AbstractModel):
    """DescribeAssetImageVirusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像id
        :type ImageID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Name- String - 是否必填：否 - 镜像名称筛选，</li>
<li>RiskLevel - String - 是否必填：否 - 风险等级  1,2,3,4</li>
        :type Filters: list of AssetFilters
        :param Order: 排序 asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.ImageID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageVirusListResponse(AbstractModel):
    """DescribeAssetImageVirusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像病毒列表
        :type List: list of ImageVirusInfo
        :param TotalCount: 总数量
        :type TotalCount: int
        :param VirusScanStatus: 病毒扫描状态
0:未扫描
1:扫描中
2:扫描完成
3:扫描出错
4:扫描取消
        :type VirusScanStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.VirusScanStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ImageVirusInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.VirusScanStatus = params.get("VirusScanStatus")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageVulListExportRequest(AbstractModel):
    """DescribeAssetImageVulListExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param ImageID: 镜像id
        :type ImageID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Name- String - 是否必填：否 - 漏洞名称名称筛选，</li>
<li>Level - String - 是否必填：否 - 风险等级  1,2,3,4</li>
        :type Filters: list of AssetFilters
        """
        self.ExportField = None
        self.ImageID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.ImageID = params.get("ImageID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageVulListExportResponse(AbstractModel):
    """DescribeAssetImageVulListExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: excel文件下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeAssetImageVulListRequest(AbstractModel):
    """DescribeAssetImageVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像id
        :type ImageID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Name- String - 是否必填：否 - 漏洞名称名称筛选，</li>
<li>Level - String - 是否必填：否 - 风险等级  1,2,3,4</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段（Level）
        :type By: str
        :param Order: 排序方式 + -
        :type Order: str
        """
        self.ImageID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetImageVulListResponse(AbstractModel):
    """DescribeAssetImageVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像漏洞列表
        :type List: list of ImagesVul
        :param TotalCount: 总数量
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
                obj = ImagesVul()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetPortListRequest(AbstractModel):
    """DescribeAssetPortList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>All - String - 是否必填：否 - 模糊查询可选字段</li>
<li>RunAs - String - 是否必填：否 - 运行用户筛选，</li>
<li>ContainerID - String - 是否必填：否 - 容器id</li>
<li>HostID- String - 是否必填：是 - 主机id</li>
<li>HostIP- string - 是否必填：否 - 主机ip搜索</li>
<li>ProcessName- string - 是否必填：否 - 进程名搜索</li>
        :type Filters: list of AssetFilters
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
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetPortListResponse(AbstractModel):
    """DescribeAssetPortList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 端口列表
        :type List: list of PortInfo
        :param TotalCount: 总数量
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
                obj = PortInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetProcessListRequest(AbstractModel):
    """DescribeAssetProcessList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>RunAs - String - 是否必填：否 - 运行用户筛选，</li>
<li>ContainerID - String - 是否必填：否 - 容器id</li>
<li>HostID- String - 是否必填：是 - 主机id</li>
<li>HostIP- string - 是否必填：否 - 主机ip搜索</li>
<li>ProcessName- string - 是否必填：否 - 进程名搜索</li>
<li>Pid- string - 是否必填：否 - 进程id搜索(关联进程)</li>
        :type Filters: list of AssetFilters
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
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetProcessListResponse(AbstractModel):
    """DescribeAssetProcessList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 端口列表
        :type List: list of ProcessInfo
        :param TotalCount: 总数量
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
                obj = ProcessInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetSummaryRequest(AbstractModel):
    """DescribeAssetSummary请求参数结构体

    """


class DescribeAssetSummaryResponse(AbstractModel):
    """DescribeAssetSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppCnt: 应用个数
        :type AppCnt: int
        :param ContainerCnt: 容器个数
        :type ContainerCnt: int
        :param ContainerPause: 暂停的容器个数
        :type ContainerPause: int
        :param ContainerRunning: 运行的容器个数
        :type ContainerRunning: int
        :param ContainerStop: 停止运行的容器个数
        :type ContainerStop: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param DbCnt: 数据库个数
        :type DbCnt: int
        :param ImageCnt: 镜像个数
        :type ImageCnt: int
        :param HostOnline: 主机在线个数
        :type HostOnline: int
        :param HostCnt: 主机个数
        :type HostCnt: int
        :param ImageHasRiskInfoCnt: 有风险的镜像个数
        :type ImageHasRiskInfoCnt: int
        :param ImageHasVirusCnt: 有病毒的镜像个数
        :type ImageHasVirusCnt: int
        :param ImageHasVulsCnt: 有漏洞的镜像个数
        :type ImageHasVulsCnt: int
        :param ImageUntrustCnt: 不受信任的镜像个数
        :type ImageUntrustCnt: int
        :param ListenPortCnt: 监听的端口个数
        :type ListenPortCnt: int
        :param ProcessCnt: 进程个数
        :type ProcessCnt: int
        :param WebServiceCnt: web服务个数
        :type WebServiceCnt: int
        :param LatestImageScanTime: 最近镜像扫描时间
        :type LatestImageScanTime: str
        :param ImageUnsafeCnt: 风险镜像个数
        :type ImageUnsafeCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppCnt = None
        self.ContainerCnt = None
        self.ContainerPause = None
        self.ContainerRunning = None
        self.ContainerStop = None
        self.CreateTime = None
        self.DbCnt = None
        self.ImageCnt = None
        self.HostOnline = None
        self.HostCnt = None
        self.ImageHasRiskInfoCnt = None
        self.ImageHasVirusCnt = None
        self.ImageHasVulsCnt = None
        self.ImageUntrustCnt = None
        self.ListenPortCnt = None
        self.ProcessCnt = None
        self.WebServiceCnt = None
        self.LatestImageScanTime = None
        self.ImageUnsafeCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppCnt = params.get("AppCnt")
        self.ContainerCnt = params.get("ContainerCnt")
        self.ContainerPause = params.get("ContainerPause")
        self.ContainerRunning = params.get("ContainerRunning")
        self.ContainerStop = params.get("ContainerStop")
        self.CreateTime = params.get("CreateTime")
        self.DbCnt = params.get("DbCnt")
        self.ImageCnt = params.get("ImageCnt")
        self.HostOnline = params.get("HostOnline")
        self.HostCnt = params.get("HostCnt")
        self.ImageHasRiskInfoCnt = params.get("ImageHasRiskInfoCnt")
        self.ImageHasVirusCnt = params.get("ImageHasVirusCnt")
        self.ImageHasVulsCnt = params.get("ImageHasVulsCnt")
        self.ImageUntrustCnt = params.get("ImageUntrustCnt")
        self.ListenPortCnt = params.get("ListenPortCnt")
        self.ProcessCnt = params.get("ProcessCnt")
        self.WebServiceCnt = params.get("WebServiceCnt")
        self.LatestImageScanTime = params.get("LatestImageScanTime")
        self.ImageUnsafeCnt = params.get("ImageUnsafeCnt")
        self.RequestId = params.get("RequestId")


class DescribeAssetWebServiceListRequest(AbstractModel):
    """DescribeAssetWebServiceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords- String - 是否必填：否 - 模糊查询可选字段</li>
<li>Type- String - 是否必填：否 - 主机运行状态筛选，"Apache"
"Jboss"
"lighttpd"
"Nginx"
"Tomcat"</li>
        :type Filters: list of AssetFilters
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
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetWebServiceListResponse(AbstractModel):
    """DescribeAssetWebServiceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 主机列表
        :type List: list of ServiceInfo
        :param TotalCount: 总数量
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
                obj = ServiceInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCheckItemListRequest(AbstractModel):
    """DescribeCheckItemList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每次查询的最大记录数量
        :type Limit: int
        :param Filters: Name 可取值：risk_level风险等级, risk_target检查对象，风险对象,risk_type风险类别,risk_attri检测项所属的风险类型
        :type Filters: list of ComplianceFilters
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
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckItemListResponse(AbstractModel):
    """DescribeCheckItemList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterCheckItems: 检查项详情数组
        :type ClusterCheckItems: list of ClusterCheckItem
        :param TotalCount: 检查项总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterCheckItems = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterCheckItems") is not None:
            self.ClusterCheckItems = []
            for item in params.get("ClusterCheckItems"):
                obj = ClusterCheckItem()
                obj._deserialize(item)
                self.ClusterCheckItems.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param ClusterName: 集群名字
        :type ClusterName: str
        :param ScanTaskProgress: 当前集群扫描任务的进度，100表示扫描完成.
        :type ScanTaskProgress: int
        :param ClusterVersion: 集群版本
        :type ClusterVersion: str
        :param ContainerRuntime: 运行时组件
        :type ContainerRuntime: str
        :param ClusterNodeNum: 集群节点数
        :type ClusterNodeNum: int
        :param ClusterStatus: 集群状态 (Running 运行中 Creating 创建中 Abnormal 异常 )
        :type ClusterStatus: str
        :param ClusterType: 集群类型：为托管集群MANAGED_CLUSTER、独立集群INDEPENDENT_CLUSTER
        :type ClusterType: str
        :param Region: 集群区域
        :type Region: str
        :param SeriousRiskCount: 严重风险检查项的数量
        :type SeriousRiskCount: int
        :param HighRiskCount: 高风险检查项的数量
        :type HighRiskCount: int
        :param MiddleRiskCount: 中风险检查项的数量
        :type MiddleRiskCount: int
        :param HintRiskCount: 提示风险检查项的数量
        :type HintRiskCount: int
        :param CheckStatus: 检查任务的状态
        :type CheckStatus: str
        :param DefenderStatus: 防御容器状态
        :type DefenderStatus: str
        :param TaskCreateTime: 扫描任务创建时间
        :type TaskCreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ScanTaskProgress = None
        self.ClusterVersion = None
        self.ContainerRuntime = None
        self.ClusterNodeNum = None
        self.ClusterStatus = None
        self.ClusterType = None
        self.Region = None
        self.SeriousRiskCount = None
        self.HighRiskCount = None
        self.MiddleRiskCount = None
        self.HintRiskCount = None
        self.CheckStatus = None
        self.DefenderStatus = None
        self.TaskCreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ScanTaskProgress = params.get("ScanTaskProgress")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.ClusterNodeNum = params.get("ClusterNodeNum")
        self.ClusterStatus = params.get("ClusterStatus")
        self.ClusterType = params.get("ClusterType")
        self.Region = params.get("Region")
        self.SeriousRiskCount = params.get("SeriousRiskCount")
        self.HighRiskCount = params.get("HighRiskCount")
        self.MiddleRiskCount = params.get("MiddleRiskCount")
        self.HintRiskCount = params.get("HintRiskCount")
        self.CheckStatus = params.get("CheckStatus")
        self.DefenderStatus = params.get("DefenderStatus")
        self.TaskCreateTime = params.get("TaskCreateTime")
        self.RequestId = params.get("RequestId")


class DescribeClusterSummaryRequest(AbstractModel):
    """DescribeClusterSummary请求参数结构体

    """


class DescribeClusterSummaryResponse(AbstractModel):
    """DescribeClusterSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群总数
        :type TotalCount: int
        :param RiskClusterCount: 有风险的集群数量
        :type RiskClusterCount: int
        :param UncheckClusterCount: 未检查的集群数量
        :type UncheckClusterCount: int
        :param ManagedClusterCount: 托管集群数量
        :type ManagedClusterCount: int
        :param IndependentClusterCount: 独立集群数量
        :type IndependentClusterCount: int
        :param NoRiskClusterCount: 无风险的集群数量
        :type NoRiskClusterCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RiskClusterCount = None
        self.UncheckClusterCount = None
        self.ManagedClusterCount = None
        self.IndependentClusterCount = None
        self.NoRiskClusterCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.RiskClusterCount = params.get("RiskClusterCount")
        self.UncheckClusterCount = params.get("UncheckClusterCount")
        self.ManagedClusterCount = params.get("ManagedClusterCount")
        self.IndependentClusterCount = params.get("IndependentClusterCount")
        self.NoRiskClusterCount = params.get("NoRiskClusterCount")
        self.RequestId = params.get("RequestId")


class DescribeComplianceAssetDetailInfoRequest(AbstractModel):
    """DescribeComplianceAssetDetailInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerAssetId: 客户资产ID。
        :type CustomerAssetId: int
        """
        self.CustomerAssetId = None


    def _deserialize(self, params):
        self.CustomerAssetId = params.get("CustomerAssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceAssetDetailInfoResponse(AbstractModel):
    """DescribeComplianceAssetDetailInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param AssetDetailInfo: 某资产的详情。
        :type AssetDetailInfo: :class:`tencentcloud.tcss.v20201101.models.ComplianceAssetDetailInfo`
        :param ContainerDetailInfo: 当资产为容器时，返回此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerDetailInfo: :class:`tencentcloud.tcss.v20201101.models.ComplianceContainerDetailInfo`
        :param ImageDetailInfo: 当资产为镜像时，返回此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageDetailInfo: :class:`tencentcloud.tcss.v20201101.models.ComplianceImageDetailInfo`
        :param HostDetailInfo: 当资产为主机时，返回此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostDetailInfo: :class:`tencentcloud.tcss.v20201101.models.ComplianceHostDetailInfo`
        :param K8SDetailInfo: 当资产为K8S时，返回此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type K8SDetailInfo: :class:`tencentcloud.tcss.v20201101.models.ComplianceK8SDetailInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AssetDetailInfo = None
        self.ContainerDetailInfo = None
        self.ImageDetailInfo = None
        self.HostDetailInfo = None
        self.K8SDetailInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssetDetailInfo") is not None:
            self.AssetDetailInfo = ComplianceAssetDetailInfo()
            self.AssetDetailInfo._deserialize(params.get("AssetDetailInfo"))
        if params.get("ContainerDetailInfo") is not None:
            self.ContainerDetailInfo = ComplianceContainerDetailInfo()
            self.ContainerDetailInfo._deserialize(params.get("ContainerDetailInfo"))
        if params.get("ImageDetailInfo") is not None:
            self.ImageDetailInfo = ComplianceImageDetailInfo()
            self.ImageDetailInfo._deserialize(params.get("ImageDetailInfo"))
        if params.get("HostDetailInfo") is not None:
            self.HostDetailInfo = ComplianceHostDetailInfo()
            self.HostDetailInfo._deserialize(params.get("HostDetailInfo"))
        if params.get("K8SDetailInfo") is not None:
            self.K8SDetailInfo = ComplianceK8SDetailInfo()
            self.K8SDetailInfo._deserialize(params.get("K8SDetailInfo"))
        self.RequestId = params.get("RequestId")


class DescribeComplianceAssetListRequest(AbstractModel):
    """DescribeComplianceAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetTypeSet: 资产类型列表。
        :type AssetTypeSet: list of str
        :param Offset: 起始偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回的数据量，默认为10，最大为100。
        :type Limit: int
        :param Filters: 查询过滤器
        :type Filters: list of ComplianceFilters
        """
        self.AssetTypeSet = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.AssetTypeSet = params.get("AssetTypeSet")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceAssetListResponse(AbstractModel):
    """DescribeComplianceAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回资产的总数。
        :type TotalCount: int
        :param AssetInfoList: 返回各类资产的列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetInfoList: list of ComplianceAssetInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AssetInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AssetInfoList") is not None:
            self.AssetInfoList = []
            for item in params.get("AssetInfoList"):
                obj = ComplianceAssetInfo()
                obj._deserialize(item)
                self.AssetInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComplianceAssetPolicyItemListRequest(AbstractModel):
    """DescribeComplianceAssetPolicyItemList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerAssetId: 客户资产的ID。
        :type CustomerAssetId: int
        :param Offset: 起始偏移量，默认为0。
        :type Offset: int
        :param Limit: 要获取的数据量，默认为10，最大为100。
        :type Limit: int
        :param Filters: 过滤器列表。Name字段支持
RiskLevel
        :type Filters: list of ComplianceFilters
        """
        self.CustomerAssetId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.CustomerAssetId = params.get("CustomerAssetId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceAssetPolicyItemListResponse(AbstractModel):
    """DescribeComplianceAssetPolicyItemList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回检测项的总数。如果用户未启用基线检查，此处返回0。
        :type TotalCount: int
        :param AssetPolicyItemList: 返回某个资产下的检测项的列表。
        :type AssetPolicyItemList: list of ComplianceAssetPolicyItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AssetPolicyItemList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AssetPolicyItemList") is not None:
            self.AssetPolicyItemList = []
            for item in params.get("AssetPolicyItemList"):
                obj = ComplianceAssetPolicyItem()
                obj._deserialize(item)
                self.AssetPolicyItemList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCompliancePeriodTaskListRequest(AbstractModel):
    """DescribeCompliancePeriodTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetType: 资产的类型，取值为：
ASSET_CONTAINER, 容器
ASSET_IMAGE, 镜像
ASSET_HOST, 主机
ASSET_K8S, K8S资产
        :type AssetType: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100。
        :type Limit: int
        """
        self.AssetType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AssetType = params.get("AssetType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompliancePeriodTaskListResponse(AbstractModel):
    """DescribeCompliancePeriodTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 定时任务的总量。
        :type TotalCount: int
        :param PeriodTaskSet: 定时任务信息的列表
        :type PeriodTaskSet: list of CompliancePeriodTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PeriodTaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PeriodTaskSet") is not None:
            self.PeriodTaskSet = []
            for item in params.get("PeriodTaskSet"):
                obj = CompliancePeriodTask()
                obj._deserialize(item)
                self.PeriodTaskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCompliancePolicyItemAffectedAssetListRequest(AbstractModel):
    """DescribeCompliancePolicyItemAffectedAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemId: DescribeComplianceTaskPolicyItemSummaryList返回的CustomerPolicyItemId，表示检测项的ID。
        :type CustomerPolicyItemId: int
        :param Offset: 起始偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100。
        :type Limit: int
        :param Filters: 过滤条件。
Name - String
Name 可取值：NodeName, CheckResult
        :type Filters: list of ComplianceFilters
        """
        self.CustomerPolicyItemId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.CustomerPolicyItemId = params.get("CustomerPolicyItemId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompliancePolicyItemAffectedAssetListResponse(AbstractModel):
    """DescribeCompliancePolicyItemAffectedAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param AffectedAssetList: 返回各检测项所影响的资产的列表。
        :type AffectedAssetList: list of ComplianceAffectedAsset
        :param TotalCount: 检测项影响的资产的总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AffectedAssetList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AffectedAssetList") is not None:
            self.AffectedAssetList = []
            for item in params.get("AffectedAssetList"):
                obj = ComplianceAffectedAsset()
                obj._deserialize(item)
                self.AffectedAssetList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCompliancePolicyItemAffectedSummaryRequest(AbstractModel):
    """DescribeCompliancePolicyItemAffectedSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemId: DescribeComplianceTaskPolicyItemSummaryList返回的CustomerPolicyItemId，表示检测项的ID。
        :type CustomerPolicyItemId: int
        """
        self.CustomerPolicyItemId = None


    def _deserialize(self, params):
        self.CustomerPolicyItemId = params.get("CustomerPolicyItemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompliancePolicyItemAffectedSummaryResponse(AbstractModel):
    """DescribeCompliancePolicyItemAffectedSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyItemSummary: 返回各检测项影响的资产的汇总信息。
        :type PolicyItemSummary: :class:`tencentcloud.tcss.v20201101.models.CompliancePolicyItemSummary`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyItemSummary = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyItemSummary") is not None:
            self.PolicyItemSummary = CompliancePolicyItemSummary()
            self.PolicyItemSummary._deserialize(params.get("PolicyItemSummary"))
        self.RequestId = params.get("RequestId")


class DescribeComplianceScanFailedAssetListRequest(AbstractModel):
    """DescribeComplianceScanFailedAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetTypeSet: 资产类型列表。
ASSET_CONTAINER, 容器
ASSET_IMAGE, 镜像
ASSET_HOST, 主机
ASSET_K8S, K8S资产
        :type AssetTypeSet: list of str
        :param Offset: 起始偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回的数据量，默认为10，最大为100。
        :type Limit: int
        :param Filters: 查询过滤器
        :type Filters: list of ComplianceFilters
        """
        self.AssetTypeSet = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.AssetTypeSet = params.get("AssetTypeSet")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceScanFailedAssetListResponse(AbstractModel):
    """DescribeComplianceScanFailedAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回检测失败的资产的总数。
        :type TotalCount: int
        :param ScanFailedAssetList: 返回各类检测失败的资产的汇总信息的列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanFailedAssetList: list of ComplianceScanFailedAsset
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ScanFailedAssetList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ScanFailedAssetList") is not None:
            self.ScanFailedAssetList = []
            for item in params.get("ScanFailedAssetList"):
                obj = ComplianceScanFailedAsset()
                obj._deserialize(item)
                self.ScanFailedAssetList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComplianceTaskAssetSummaryRequest(AbstractModel):
    """DescribeComplianceTaskAssetSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetTypeSet: 资产类型列表。
ASSET_CONTAINER, 容器
ASSET_IMAGE, 镜像
ASSET_HOST, 主机
ASSET_K8S, K8S资产
        :type AssetTypeSet: list of str
        """
        self.AssetTypeSet = None


    def _deserialize(self, params):
        self.AssetTypeSet = params.get("AssetTypeSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceTaskAssetSummaryResponse(AbstractModel):
    """DescribeComplianceTaskAssetSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 返回用户的状态，

USER_UNINIT: 用户未初始化。
USER_INITIALIZING，表示用户正在初始化环境。
USER_NORMAL: 正常状态。
        :type Status: str
        :param AssetSummaryList: 返回各类资产的汇总信息的列表。
        :type AssetSummaryList: list of ComplianceAssetSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.AssetSummaryList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        if params.get("AssetSummaryList") is not None:
            self.AssetSummaryList = []
            for item in params.get("AssetSummaryList"):
                obj = ComplianceAssetSummary()
                obj._deserialize(item)
                self.AssetSummaryList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComplianceTaskPolicyItemSummaryListRequest(AbstractModel):
    """DescribeComplianceTaskPolicyItemSummaryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetType: 资产类型。仅查询与指定资产类型相关的检测项。

ASSET_CONTAINER, 容器

ASSET_IMAGE, 镜像

ASSET_HOST, 主机

ASSET_K8S, K8S资产
        :type AssetType: str
        :param Offset: 起始偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100。
        :type Limit: int
        :param Filters: 过滤条件。
Name - String
Name 可取值：ItemType, StandardId,  RiskLevel。
当为K8S资产时，还可取ClusterName。
        :type Filters: list of ComplianceFilters
        """
        self.AssetType = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.AssetType = params.get("AssetType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceTaskPolicyItemSummaryListResponse(AbstractModel):
    """DescribeComplianceTaskPolicyItemSummaryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回最近一次合规检查任务的ID。这个任务为本次所展示数据的来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param TotalCount: 返回检测项的总数。
        :type TotalCount: int
        :param PolicyItemSummaryList: 返回各检测项对应的汇总信息的列表。
        :type PolicyItemSummaryList: list of CompliancePolicyItemSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.TotalCount = None
        self.PolicyItemSummaryList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TotalCount = params.get("TotalCount")
        if params.get("PolicyItemSummaryList") is not None:
            self.PolicyItemSummaryList = []
            for item in params.get("PolicyItemSummaryList"):
                obj = CompliancePolicyItemSummary()
                obj._deserialize(item)
                self.PolicyItemSummaryList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComplianceWhitelistItemListRequest(AbstractModel):
    """DescribeComplianceWhitelistItemList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 起始偏移量，默认为0。
        :type Offset: int
        :param Limit: 要获取的数量，默认为10，最大为100。
        :type Limit: int
        :param AssetTypeSet: 资产类型列表。
        :type AssetTypeSet: list of str
        :param Filters: 查询过滤器
        :type Filters: list of ComplianceFilters
        """
        self.Offset = None
        self.Limit = None
        self.AssetTypeSet = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AssetTypeSet = params.get("AssetTypeSet")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceWhitelistItemListResponse(AbstractModel):
    """DescribeComplianceWhitelistItemList返回参数结构体

    """

    def __init__(self):
        r"""
        :param WhitelistItemSet: 白名单项的列表。
        :type WhitelistItemSet: list of ComplianceWhitelistItem
        :param TotalCount: 白名单项的总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WhitelistItemSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WhitelistItemSet") is not None:
            self.WhitelistItemSet = []
            for item in params.get("WhitelistItemSet"):
                obj = ComplianceWhitelistItem()
                obj._deserialize(item)
                self.WhitelistItemSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeContainerAssetSummaryRequest(AbstractModel):
    """DescribeContainerAssetSummary请求参数结构体

    """


class DescribeContainerAssetSummaryResponse(AbstractModel):
    """DescribeContainerAssetSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerTotalCnt: 容器总数
        :type ContainerTotalCnt: int
        :param ContainerRunningCnt: 正在运行容器数量
        :type ContainerRunningCnt: int
        :param ContainerPauseCnt: 暂停运行容器数量
        :type ContainerPauseCnt: int
        :param ContainerStopped: 停止运行容器数量
        :type ContainerStopped: int
        :param ImageCnt: 本地镜像数量
        :type ImageCnt: int
        :param HostCnt: 主机节点数量
        :type HostCnt: int
        :param HostRunningCnt: 主机正在运行节点数量
        :type HostRunningCnt: int
        :param HostOfflineCnt: 主机离线节点数量
        :type HostOfflineCnt: int
        :param ImageRegistryCnt: 镜像仓库数量
        :type ImageRegistryCnt: int
        :param ImageTotalCnt: 镜像总数
        :type ImageTotalCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContainerTotalCnt = None
        self.ContainerRunningCnt = None
        self.ContainerPauseCnt = None
        self.ContainerStopped = None
        self.ImageCnt = None
        self.HostCnt = None
        self.HostRunningCnt = None
        self.HostOfflineCnt = None
        self.ImageRegistryCnt = None
        self.ImageTotalCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ContainerTotalCnt = params.get("ContainerTotalCnt")
        self.ContainerRunningCnt = params.get("ContainerRunningCnt")
        self.ContainerPauseCnt = params.get("ContainerPauseCnt")
        self.ContainerStopped = params.get("ContainerStopped")
        self.ImageCnt = params.get("ImageCnt")
        self.HostCnt = params.get("HostCnt")
        self.HostRunningCnt = params.get("HostRunningCnt")
        self.HostOfflineCnt = params.get("HostOfflineCnt")
        self.ImageRegistryCnt = params.get("ImageRegistryCnt")
        self.ImageTotalCnt = params.get("ImageTotalCnt")
        self.RequestId = params.get("RequestId")


class DescribeContainerSecEventSummaryRequest(AbstractModel):
    """DescribeContainerSecEventSummary请求参数结构体

    """


class DescribeContainerSecEventSummaryResponse(AbstractModel):
    """DescribeContainerSecEventSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param UnhandledEscapeCnt: 未处理逃逸事件
        :type UnhandledEscapeCnt: int
        :param UnhandledReverseShellCnt: 未处理反弹shell事件
        :type UnhandledReverseShellCnt: int
        :param UnhandledRiskSyscallCnt: 未处理高危系统调用
        :type UnhandledRiskSyscallCnt: int
        :param UnhandledAbnormalProcessCnt: 未处理异常进程
        :type UnhandledAbnormalProcessCnt: int
        :param UnhandledFileCnt: 未处理文件篡改
        :type UnhandledFileCnt: int
        :param UnhandledVirusEventCnt: 未处理木马事件
        :type UnhandledVirusEventCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UnhandledEscapeCnt = None
        self.UnhandledReverseShellCnt = None
        self.UnhandledRiskSyscallCnt = None
        self.UnhandledAbnormalProcessCnt = None
        self.UnhandledFileCnt = None
        self.UnhandledVirusEventCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UnhandledEscapeCnt = params.get("UnhandledEscapeCnt")
        self.UnhandledReverseShellCnt = params.get("UnhandledReverseShellCnt")
        self.UnhandledRiskSyscallCnt = params.get("UnhandledRiskSyscallCnt")
        self.UnhandledAbnormalProcessCnt = params.get("UnhandledAbnormalProcessCnt")
        self.UnhandledFileCnt = params.get("UnhandledFileCnt")
        self.UnhandledVirusEventCnt = params.get("UnhandledVirusEventCnt")
        self.RequestId = params.get("RequestId")


class DescribeEscapeEventDetailRequest(AbstractModel):
    """DescribeEscapeEventDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventId: 事件唯一id
        :type EventId: str
        """
        self.EventId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEscapeEventDetailResponse(AbstractModel):
    """DescribeEscapeEventDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventBaseInfo: 事件基本信息
        :type EventBaseInfo: :class:`tencentcloud.tcss.v20201101.models.RunTimeEventBaseInfo`
        :param ProcessInfo: 进程信息
        :type ProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessDetailInfo`
        :param EventDetail: 事件描述
        :type EventDetail: :class:`tencentcloud.tcss.v20201101.models.EscapeEventDescription`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.EventDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventBaseInfo") is not None:
            self.EventBaseInfo = RunTimeEventBaseInfo()
            self.EventBaseInfo._deserialize(params.get("EventBaseInfo"))
        if params.get("ProcessInfo") is not None:
            self.ProcessInfo = ProcessDetailInfo()
            self.ProcessInfo._deserialize(params.get("ProcessInfo"))
        if params.get("EventDetail") is not None:
            self.EventDetail = EscapeEventDescription()
            self.EventDetail._deserialize(params.get("EventDetail"))
        self.RequestId = params.get("RequestId")


class DescribeEscapeEventInfoRequest(AbstractModel):
    """DescribeEscapeEventInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEscapeEventInfoResponse(AbstractModel):
    """DescribeEscapeEventInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventSet: 逃逸事件数组
        :type EventSet: list of EscapeEventInfo
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = EscapeEventInfo()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEscapeEventsExportRequest(AbstractModel):
    """DescribeEscapeEventsExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEscapeEventsExportResponse(AbstractModel):
    """DescribeEscapeEventsExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: execle下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeEscapeRuleInfoRequest(AbstractModel):
    """DescribeEscapeRuleInfo请求参数结构体

    """


class DescribeEscapeRuleInfoResponse(AbstractModel):
    """DescribeEscapeRuleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleSet: 规则信息
        :type RuleSet: list of EscapeRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = EscapeRule()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEscapeSafeStateRequest(AbstractModel):
    """DescribeEscapeSafeState请求参数结构体

    """


class DescribeEscapeSafeStateResponse(AbstractModel):
    """DescribeEscapeSafeState返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsSafe: Unsafe：存在风险，Safe：暂无风险,UnKnown:未知风险
        :type IsSafe: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSafe = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSafe = params.get("IsSafe")
        self.RequestId = params.get("RequestId")


class DescribeExportJobResultRequest(AbstractModel):
    """DescribeExportJobResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: CreateExportComplianceStatusListJob返回的JobId字段的值
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportJobResultResponse(AbstractModel):
    """DescribeExportJobResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param ExportStatus: 导出的状态。取值为, SUCCESS:成功、FAILURE:失败，RUNNING: 进行中。
        :type ExportStatus: str
        :param DownloadURL: 返回下载URL
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadURL: str
        :param ExportProgress: 当ExportStatus为RUNNING时，返回导出进度。0~100范围的浮点数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportProgress: float
        :param FailureMsg: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExportStatus = None
        self.DownloadURL = None
        self.ExportProgress = None
        self.FailureMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExportStatus = params.get("ExportStatus")
        self.DownloadURL = params.get("DownloadURL")
        self.ExportProgress = params.get("ExportProgress")
        self.FailureMsg = params.get("FailureMsg")
        self.RequestId = params.get("RequestId")


class DescribeImageAuthorizedInfoRequest(AbstractModel):
    """DescribeImageAuthorizedInfo请求参数结构体

    """


class DescribeImageAuthorizedInfoResponse(AbstractModel):
    """DescribeImageAuthorizedInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalAuthorizedCnt: 总共有效的镜像授权数
        :type TotalAuthorizedCnt: int
        :param UsedAuthorizedCnt: 已使用镜像授权数
        :type UsedAuthorizedCnt: int
        :param ScannedImageCnt: 已开启扫描镜像数
        :type ScannedImageCnt: int
        :param NotScannedImageCnt: 未开启扫描镜像数
        :type NotScannedImageCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalAuthorizedCnt = None
        self.UsedAuthorizedCnt = None
        self.ScannedImageCnt = None
        self.NotScannedImageCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalAuthorizedCnt = params.get("TotalAuthorizedCnt")
        self.UsedAuthorizedCnt = params.get("UsedAuthorizedCnt")
        self.ScannedImageCnt = params.get("ScannedImageCnt")
        self.NotScannedImageCnt = params.get("NotScannedImageCnt")
        self.RequestId = params.get("RequestId")


class DescribeImageRegistryTimingScanTaskRequest(AbstractModel):
    """DescribeImageRegistryTimingScanTask请求参数结构体

    """


class DescribeImageRegistryTimingScanTaskResponse(AbstractModel):
    """DescribeImageRegistryTimingScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Enable: 定时扫描开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        :param ScanTime: 定时任务扫描时间
        :type ScanTime: str
        :param ScanPeriod: 定时扫描间隔
        :type ScanPeriod: int
        :param ScanType: 扫描类型数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanType: list of str
        :param All: 扫描全部镜像
        :type All: bool
        :param Images: 自定义扫描镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type Images: list of ImageInfo
        :param Id: 自动以扫描镜像Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Enable = None
        self.ScanTime = None
        self.ScanPeriod = None
        self.ScanType = None
        self.All = None
        self.Images = None
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.ScanTime = params.get("ScanTime")
        self.ScanPeriod = params.get("ScanPeriod")
        self.ScanType = params.get("ScanType")
        self.All = params.get("All")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.Images.append(obj)
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class DescribeImageRiskSummaryRequest(AbstractModel):
    """DescribeImageRiskSummary请求参数结构体

    """


class DescribeImageRiskSummaryResponse(AbstractModel):
    """DescribeImageRiskSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulnerabilityCnt: 安全漏洞
        :type VulnerabilityCnt: list of RunTimeRiskInfo
        :param MalwareVirusCnt: 木马病毒
        :type MalwareVirusCnt: list of RunTimeRiskInfo
        :param RiskCnt: 敏感信息
        :type RiskCnt: list of RunTimeRiskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulnerabilityCnt = None
        self.MalwareVirusCnt = None
        self.RiskCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulnerabilityCnt") is not None:
            self.VulnerabilityCnt = []
            for item in params.get("VulnerabilityCnt"):
                obj = RunTimeRiskInfo()
                obj._deserialize(item)
                self.VulnerabilityCnt.append(obj)
        if params.get("MalwareVirusCnt") is not None:
            self.MalwareVirusCnt = []
            for item in params.get("MalwareVirusCnt"):
                obj = RunTimeRiskInfo()
                obj._deserialize(item)
                self.MalwareVirusCnt.append(obj)
        if params.get("RiskCnt") is not None:
            self.RiskCnt = []
            for item in params.get("RiskCnt"):
                obj = RunTimeRiskInfo()
                obj._deserialize(item)
                self.RiskCnt.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageRiskTendencyRequest(AbstractModel):
    """DescribeImageRiskTendency请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageRiskTendencyResponse(AbstractModel):
    """DescribeImageRiskTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageRiskTendencySet: 本地镜像新增风险趋势信息列表
        :type ImageRiskTendencySet: list of ImageRiskTendencyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageRiskTendencySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageRiskTendencySet") is not None:
            self.ImageRiskTendencySet = []
            for item in params.get("ImageRiskTendencySet"):
                obj = ImageRiskTendencyInfo()
                obj._deserialize(item)
                self.ImageRiskTendencySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageSimpleListRequest(AbstractModel):
    """DescribeImageSimpleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: IsAuthorized 是否已经授权, 0:否 1:是 无:全部
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSimpleListResponse(AbstractModel):
    """DescribeImageSimpleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageList: 镜像列表
        :type ImageList: list of ImageSimpleInfo
        :param ImageCnt: 镜像数
        :type ImageCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageList = None
        self.ImageCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageList") is not None:
            self.ImageList = []
            for item in params.get("ImageList"):
                obj = ImageSimpleInfo()
                obj._deserialize(item)
                self.ImageList.append(obj)
        self.ImageCnt = params.get("ImageCnt")
        self.RequestId = params.get("RequestId")


class DescribePostPayDetailRequest(AbstractModel):
    """DescribePostPayDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostPayDetailResponse(AbstractModel):
    """DescribePostPayDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param SoftQuotaDayDetail: 弹性计费扣费详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftQuotaDayDetail: list of SoftQuotaDayInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SoftQuotaDayDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SoftQuotaDayDetail") is not None:
            self.SoftQuotaDayDetail = []
            for item in params.get("SoftQuotaDayDetail"):
                obj = SoftQuotaDayInfo()
                obj._deserialize(item)
                self.SoftQuotaDayDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo请求参数结构体

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 专业版开始时间，补充购买时才不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 专业版结束时间，补充购买时才不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param CoresCnt: 需购买的机器核数
        :type CoresCnt: int
        :param MaxPostPayCoresCnt: 弹性计费上限
        :type MaxPostPayCoresCnt: int
        :param ResourceId: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.CoresCnt = None
        self.MaxPostPayCoresCnt = None
        self.ResourceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CoresCnt = params.get("CoresCnt")
        self.MaxPostPayCoresCnt = params.get("MaxPostPayCoresCnt")
        self.ResourceId = params.get("ResourceId")
        self.RequestId = params.get("RequestId")


class DescribePurchaseStateInfoRequest(AbstractModel):
    """DescribePurchaseStateInfo请求参数结构体

    """


class DescribePurchaseStateInfoResponse(AbstractModel):
    """DescribePurchaseStateInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param State: 0：可申请试用可购买；1：只可购买(含试用审核不通过和试用过期)；2：试用生效中；3：专业版生效中；4：专业版过期
        :type State: int
        :param CoresCnt: 总核数
注意：此字段可能返回 null，表示取不到有效值。
        :type CoresCnt: int
        :param AuthorizedCoresCnt: 已购买核数
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizedCoresCnt: int
        :param ImageCnt: 镜像数
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCnt: int
        :param AuthorizedImageCnt: 已授权镜像数
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizedImageCnt: int
        :param PurchasedAuthorizedCnt: 已购买镜像授权数
注意：此字段可能返回 null，表示取不到有效值。
        :type PurchasedAuthorizedCnt: int
        :param ExpirationTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpirationTime: str
        :param AutomaticRenewal: 0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
注意：此字段可能返回 null，表示取不到有效值。
        :type AutomaticRenewal: int
        :param GivenAuthorizedCnt: 试用期间赠送镜像授权数，可能会过期
注意：此字段可能返回 null，表示取不到有效值。
        :type GivenAuthorizedCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.State = None
        self.CoresCnt = None
        self.AuthorizedCoresCnt = None
        self.ImageCnt = None
        self.AuthorizedImageCnt = None
        self.PurchasedAuthorizedCnt = None
        self.ExpirationTime = None
        self.AutomaticRenewal = None
        self.GivenAuthorizedCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.CoresCnt = params.get("CoresCnt")
        self.AuthorizedCoresCnt = params.get("AuthorizedCoresCnt")
        self.ImageCnt = params.get("ImageCnt")
        self.AuthorizedImageCnt = params.get("AuthorizedImageCnt")
        self.PurchasedAuthorizedCnt = params.get("PurchasedAuthorizedCnt")
        self.ExpirationTime = params.get("ExpirationTime")
        self.AutomaticRenewal = params.get("AutomaticRenewal")
        self.GivenAuthorizedCnt = params.get("GivenAuthorizedCnt")
        self.RequestId = params.get("RequestId")


class DescribeRefreshTaskRequest(AbstractModel):
    """DescribeRefreshTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
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
        


class DescribeRefreshTaskResponse(AbstractModel):
    """DescribeRefreshTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskStatus: 刷新任务状态，可能为：Task_New,Task_Running,Task_Finish,Task_Error,Task_NoExist
        :type TaskStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        self.RequestId = params.get("RequestId")


class DescribeReverseShellDetailRequest(AbstractModel):
    """DescribeReverseShellDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventId: 事件唯一id
        :type EventId: str
        """
        self.EventId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReverseShellDetailResponse(AbstractModel):
    """DescribeReverseShellDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventBaseInfo: 事件基本信息
        :type EventBaseInfo: :class:`tencentcloud.tcss.v20201101.models.RunTimeEventBaseInfo`
        :param ProcessInfo: 进程信息
        :type ProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessDetailInfo`
        :param ParentProcessInfo: 父进程信息
        :type ParentProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessDetailBaseInfo`
        :param EventDetail: 事件描述
        :type EventDetail: :class:`tencentcloud.tcss.v20201101.models.ReverseShellEventDescription`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.ParentProcessInfo = None
        self.EventDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventBaseInfo") is not None:
            self.EventBaseInfo = RunTimeEventBaseInfo()
            self.EventBaseInfo._deserialize(params.get("EventBaseInfo"))
        if params.get("ProcessInfo") is not None:
            self.ProcessInfo = ProcessDetailInfo()
            self.ProcessInfo._deserialize(params.get("ProcessInfo"))
        if params.get("ParentProcessInfo") is not None:
            self.ParentProcessInfo = ProcessDetailBaseInfo()
            self.ParentProcessInfo._deserialize(params.get("ParentProcessInfo"))
        if params.get("EventDetail") is not None:
            self.EventDetail = ReverseShellEventDescription()
            self.EventDetail._deserialize(params.get("EventDetail"))
        self.RequestId = params.get("RequestId")


class DescribeReverseShellEventsExportRequest(AbstractModel):
    """DescribeReverseShellEventsExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReverseShellEventsExportResponse(AbstractModel):
    """DescribeReverseShellEventsExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: execle下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeReverseShellEventsRequest(AbstractModel):
    """DescribeReverseShellEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReverseShellEventsResponse(AbstractModel):
    """DescribeReverseShellEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param EventSet: 反弹shell数组
        :type EventSet: list of ReverseShellEventInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = ReverseShellEventInfo()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReverseShellWhiteListDetailRequest(AbstractModel):
    """DescribeReverseShellWhiteListDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListId: 白名单id
        :type WhiteListId: str
        """
        self.WhiteListId = None


    def _deserialize(self, params):
        self.WhiteListId = params.get("WhiteListId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReverseShellWhiteListDetailResponse(AbstractModel):
    """DescribeReverseShellWhiteListDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListDetailInfo: 事件基本信息
        :type WhiteListDetailInfo: :class:`tencentcloud.tcss.v20201101.models.ReverseShellWhiteListInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WhiteListDetailInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WhiteListDetailInfo") is not None:
            self.WhiteListDetailInfo = ReverseShellWhiteListInfo()
            self.WhiteListDetailInfo._deserialize(params.get("WhiteListDetailInfo"))
        self.RequestId = params.get("RequestId")


class DescribeReverseShellWhiteListsRequest(AbstractModel):
    """DescribeReverseShellWhiteLists请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReverseShellWhiteListsResponse(AbstractModel):
    """DescribeReverseShellWhiteLists返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param WhiteListSet: 白名单信息列表
        :type WhiteListSet: list of ReverseShellWhiteListBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WhiteListSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WhiteListSet") is not None:
            self.WhiteListSet = []
            for item in params.get("WhiteListSet"):
                obj = ReverseShellWhiteListBaseInfo()
                obj._deserialize(item)
                self.WhiteListSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRiskListRequest(AbstractModel):
    """DescribeRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 要查询的集群ID，如果不指定，则查询用户所有的风险项
        :type ClusterId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每次查询的最大记录数量
        :type Limit: int
        :param Filters: Name - String
Name 可取值：RiskLevel风险等级, RiskTarget检查对象，风险对象,RiskType风险类别,RiskAttribute检测项所属的风险类型,Name
        :type Filters: list of ComplianceFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskListResponse(AbstractModel):
    """DescribeRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterRiskItems: 风险详情数组
        :type ClusterRiskItems: list of ClusterRiskItem
        :param TotalCount: 风险项的总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterRiskItems = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterRiskItems") is not None:
            self.ClusterRiskItems = []
            for item in params.get("ClusterRiskItems"):
                obj = ClusterRiskItem()
                obj._deserialize(item)
                self.ClusterRiskItems.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRiskSyscallDetailRequest(AbstractModel):
    """DescribeRiskSyscallDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventId: 事件唯一id
        :type EventId: str
        """
        self.EventId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskSyscallDetailResponse(AbstractModel):
    """DescribeRiskSyscallDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventBaseInfo: 事件基本信息
        :type EventBaseInfo: :class:`tencentcloud.tcss.v20201101.models.RunTimeEventBaseInfo`
        :param ProcessInfo: 进程信息
        :type ProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessDetailInfo`
        :param ParentProcessInfo: 父进程信息
        :type ParentProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessDetailBaseInfo`
        :param EventDetail: 事件描述
        :type EventDetail: :class:`tencentcloud.tcss.v20201101.models.RiskSyscallEventDescription`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.ParentProcessInfo = None
        self.EventDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventBaseInfo") is not None:
            self.EventBaseInfo = RunTimeEventBaseInfo()
            self.EventBaseInfo._deserialize(params.get("EventBaseInfo"))
        if params.get("ProcessInfo") is not None:
            self.ProcessInfo = ProcessDetailInfo()
            self.ProcessInfo._deserialize(params.get("ProcessInfo"))
        if params.get("ParentProcessInfo") is not None:
            self.ParentProcessInfo = ProcessDetailBaseInfo()
            self.ParentProcessInfo._deserialize(params.get("ParentProcessInfo"))
        if params.get("EventDetail") is not None:
            self.EventDetail = RiskSyscallEventDescription()
            self.EventDetail._deserialize(params.get("EventDetail"))
        self.RequestId = params.get("RequestId")


class DescribeRiskSyscallEventsExportRequest(AbstractModel):
    """DescribeRiskSyscallEventsExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskSyscallEventsExportResponse(AbstractModel):
    """DescribeRiskSyscallEventsExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: Excel下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeRiskSyscallEventsRequest(AbstractModel):
    """DescribeRiskSyscallEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskSyscallEventsResponse(AbstractModel):
    """DescribeRiskSyscallEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param EventSet: 高危系统调用数组
        :type EventSet: list of RiskSyscallEventInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = RiskSyscallEventInfo()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRiskSyscallNamesRequest(AbstractModel):
    """DescribeRiskSyscallNames请求参数结构体

    """


class DescribeRiskSyscallNamesResponse(AbstractModel):
    """DescribeRiskSyscallNames返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param SyscallNames: 系统调用名称列表
        :type SyscallNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SyscallNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.SyscallNames = params.get("SyscallNames")
        self.RequestId = params.get("RequestId")


class DescribeRiskSyscallWhiteListDetailRequest(AbstractModel):
    """DescribeRiskSyscallWhiteListDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListId: 白名单id
        :type WhiteListId: str
        """
        self.WhiteListId = None


    def _deserialize(self, params):
        self.WhiteListId = params.get("WhiteListId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskSyscallWhiteListDetailResponse(AbstractModel):
    """DescribeRiskSyscallWhiteListDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListDetailInfo: 白名单基本信息
        :type WhiteListDetailInfo: :class:`tencentcloud.tcss.v20201101.models.RiskSyscallWhiteListInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WhiteListDetailInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WhiteListDetailInfo") is not None:
            self.WhiteListDetailInfo = RiskSyscallWhiteListInfo()
            self.WhiteListDetailInfo._deserialize(params.get("WhiteListDetailInfo"))
        self.RequestId = params.get("RequestId")


class DescribeRiskSyscallWhiteListsRequest(AbstractModel):
    """DescribeRiskSyscallWhiteLists请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskSyscallWhiteListsResponse(AbstractModel):
    """DescribeRiskSyscallWhiteLists返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 事件总数量
        :type TotalCount: int
        :param WhiteListSet: 白名单信息列表
        :type WhiteListSet: list of RiskSyscallWhiteListBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WhiteListSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WhiteListSet") is not None:
            self.WhiteListSet = []
            for item in params.get("WhiteListSet"):
                obj = RiskSyscallWhiteListBaseInfo()
                obj._deserialize(item)
                self.WhiteListSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecEventsTendencyRequest(AbstractModel):
    """DescribeSecEventsTendency请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecEventsTendencyResponse(AbstractModel):
    """DescribeSecEventsTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventTendencySet: 运行时安全事件趋势信息列表
        :type EventTendencySet: list of SecTendencyEventInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventTendencySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventTendencySet") is not None:
            self.EventTendencySet = []
            for item in params.get("EventTendencySet"):
                obj = SecTendencyEventInfo()
                obj._deserialize(item)
                self.EventTendencySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskResultSummaryRequest(AbstractModel):
    """DescribeTaskResultSummary请求参数结构体

    """


class DescribeTaskResultSummaryResponse(AbstractModel):
    """DescribeTaskResultSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param SeriousRiskNodeCount: 严重风险影响的节点数量,返回7天数据
        :type SeriousRiskNodeCount: list of int non-negative
        :param HighRiskNodeCount: 高风险影响的节点的数量,返回7天数据
        :type HighRiskNodeCount: list of int non-negative
        :param MiddleRiskNodeCount: 中风险检查项的节点数量,返回7天数据
        :type MiddleRiskNodeCount: list of int non-negative
        :param HintRiskNodeCount: 提示风险检查项的节点数量,返回7天数据
        :type HintRiskNodeCount: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SeriousRiskNodeCount = None
        self.HighRiskNodeCount = None
        self.MiddleRiskNodeCount = None
        self.HintRiskNodeCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SeriousRiskNodeCount = params.get("SeriousRiskNodeCount")
        self.HighRiskNodeCount = params.get("HighRiskNodeCount")
        self.MiddleRiskNodeCount = params.get("MiddleRiskNodeCount")
        self.HintRiskNodeCount = params.get("HintRiskNodeCount")
        self.RequestId = params.get("RequestId")


class DescribeUnfinishRefreshTaskRequest(AbstractModel):
    """DescribeUnfinishRefreshTask请求参数结构体

    """


class DescribeUnfinishRefreshTaskResponse(AbstractModel):
    """DescribeUnfinishRefreshTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回最近的一次任务ID
        :type TaskId: int
        :param TaskStatus: 任务状态，为Task_New,Task_Running,Task_Finish,Task_Error,Task_NoExist.Task_New,Task_Running表示有任务存在，不允许新下发
        :type TaskStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskStatus = params.get("TaskStatus")
        self.RequestId = params.get("RequestId")


class DescribeUserClusterRequest(AbstractModel):
    """DescribeUserCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每次查询的最大记录数量
        :type Limit: int
        :param Filters: Name - String
Name 可取值：ClusterName,ClusterId,ClusterType,Region,ClusterCheckMode,ClusterAutoCheck
        :type Filters: list of ComplianceFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ComplianceFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserClusterResponse(AbstractModel):
    """DescribeUserCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群总数
        :type TotalCount: int
        :param ClusterInfoList: 集群的详细信息
        :type ClusterInfoList: list of ClusterInfoItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterInfoList") is not None:
            self.ClusterInfoList = []
            for item in params.get("ClusterInfoList"):
                obj = ClusterInfoItem()
                obj._deserialize(item)
                self.ClusterInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeValueAddedSrvInfoRequest(AbstractModel):
    """DescribeValueAddedSrvInfo请求参数结构体

    """


class DescribeValueAddedSrvInfoResponse(AbstractModel):
    """DescribeValueAddedSrvInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryImageCnt: 仓库镜像未授权数量
        :type RegistryImageCnt: int
        :param LocalImageCnt: 本地镜像未授权数量
        :type LocalImageCnt: int
        :param UnusedAuthorizedCnt: 未使用的镜像安全扫描授权数
        :type UnusedAuthorizedCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryImageCnt = None
        self.LocalImageCnt = None
        self.UnusedAuthorizedCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryImageCnt = params.get("RegistryImageCnt")
        self.LocalImageCnt = params.get("LocalImageCnt")
        self.UnusedAuthorizedCnt = params.get("UnusedAuthorizedCnt")
        self.RequestId = params.get("RequestId")


class DescribeVirusDetailRequest(AbstractModel):
    """DescribeVirusDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 木马文件id
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusDetailResponse(AbstractModel):
    """DescribeVirusDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param ImageName: 镜像名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageName: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Size: 木马文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param FilePath: 木马文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param ModifyTime: 最近生成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param VirusName: 病毒名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusName: str
        :param RiskLevel: 风险等级 RISK_CRITICAL, RISK_HIGH, RISK_MEDIUM, RISK_LOW, RISK_NOTICE。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param ContainerName: 容器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param ContainerId: 容器id
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerId: str
        :param HostName: 主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param HostId: 主机id
注意：此字段可能返回 null，表示取不到有效值。
        :type HostId: str
        :param ProcessName: 进程名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessName: str
        :param ProcessPath: 进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessPath: str
        :param ProcessMd5: 进程md5
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessMd5: str
        :param ProcessId: 进程id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessId: int
        :param ProcessArgv: 进程参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessArgv: str
        :param ProcessChan: 进程链
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessChan: str
        :param ProcessAccountGroup: 进程组
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessAccountGroup: str
        :param ProcessStartAccount: 进程启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessStartAccount: str
        :param ProcessFileAuthority: 进程文件权限
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessFileAuthority: str
        :param SourceType: 来源：0：一键扫描， 1：定时扫描 2：实时监控
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: int
        :param PodName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param HarmDescribe: 事件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HarmDescribe: str
        :param SuggestScheme: 建议方案
注意：此字段可能返回 null，表示取不到有效值。
        :type SuggestScheme: str
        :param Mark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Mark: str
        :param FileName: 风险文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileMd5: 文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMd5: str
        :param EventType: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EventType: str
        :param Status: DEAL_NONE:文件待处理
DEAL_IGNORE:已经忽略
DEAL_ADD_WHITELIST:加白
DEAL_DEL:文件已经删除
DEAL_ISOLATE:已经隔离
DEAL_ISOLATING:隔离中
DEAL_ISOLATE_FAILED:隔离失败
DEAL_RECOVERING:恢复中
DEAL_RECOVER_FAILED: 恢复失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param SubStatus: 失败子状态:
FILE_NOT_FOUND:文件不存在
FILE_ABNORMAL:文件异常
FILE_ABNORMAL_DEAL_RECOVER:恢复文件时，文件异常
BACKUP_FILE_NOT_FOUND:备份文件不存在
CONTAINER_NOT_FOUND_DEAL_ISOLATE:隔离时，容器不存在
CONTAINER_NOT_FOUND_DEAL_RECOVER:恢复时，容器不存在
注意：此字段可能返回 null，表示取不到有效值。
        :type SubStatus: str
        :param HostIP: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIP: str
        :param ClientIP: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageId = None
        self.ImageName = None
        self.CreateTime = None
        self.Size = None
        self.FilePath = None
        self.ModifyTime = None
        self.VirusName = None
        self.RiskLevel = None
        self.ContainerName = None
        self.ContainerId = None
        self.HostName = None
        self.HostId = None
        self.ProcessName = None
        self.ProcessPath = None
        self.ProcessMd5 = None
        self.ProcessId = None
        self.ProcessArgv = None
        self.ProcessChan = None
        self.ProcessAccountGroup = None
        self.ProcessStartAccount = None
        self.ProcessFileAuthority = None
        self.SourceType = None
        self.PodName = None
        self.Tags = None
        self.HarmDescribe = None
        self.SuggestScheme = None
        self.Mark = None
        self.FileName = None
        self.FileMd5 = None
        self.EventType = None
        self.Status = None
        self.SubStatus = None
        self.HostIP = None
        self.ClientIP = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.CreateTime = params.get("CreateTime")
        self.Size = params.get("Size")
        self.FilePath = params.get("FilePath")
        self.ModifyTime = params.get("ModifyTime")
        self.VirusName = params.get("VirusName")
        self.RiskLevel = params.get("RiskLevel")
        self.ContainerName = params.get("ContainerName")
        self.ContainerId = params.get("ContainerId")
        self.HostName = params.get("HostName")
        self.HostId = params.get("HostId")
        self.ProcessName = params.get("ProcessName")
        self.ProcessPath = params.get("ProcessPath")
        self.ProcessMd5 = params.get("ProcessMd5")
        self.ProcessId = params.get("ProcessId")
        self.ProcessArgv = params.get("ProcessArgv")
        self.ProcessChan = params.get("ProcessChan")
        self.ProcessAccountGroup = params.get("ProcessAccountGroup")
        self.ProcessStartAccount = params.get("ProcessStartAccount")
        self.ProcessFileAuthority = params.get("ProcessFileAuthority")
        self.SourceType = params.get("SourceType")
        self.PodName = params.get("PodName")
        self.Tags = params.get("Tags")
        self.HarmDescribe = params.get("HarmDescribe")
        self.SuggestScheme = params.get("SuggestScheme")
        self.Mark = params.get("Mark")
        self.FileName = params.get("FileName")
        self.FileMd5 = params.get("FileMd5")
        self.EventType = params.get("EventType")
        self.Status = params.get("Status")
        self.SubStatus = params.get("SubStatus")
        self.HostIP = params.get("HostIP")
        self.ClientIP = params.get("ClientIP")
        self.RequestId = params.get("RequestId")


class DescribeVirusListRequest(AbstractModel):
    """DescribeVirusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>FileName - String - 是否必填：否 - 文件名称</li>
<li>FilePath - String - 是否必填：否 - 文件路径</li>
<li>VirusName - String - 是否必填：否 - 病毒名称</li>
<li>ContainerName- String - 是否必填：是 - 容器名称</li>
<li>ContainerId- string - 是否必填：否 - 容器id</li>
<li>ImageName- string - 是否必填：否 - 镜像名称</li>
<li>ImageId- string - 是否必填：否 - 镜像id</li>
<li>IsRealTime- int - 是否必填：否 - 过滤是否实时监控数据</li>
<li>TaskId- string - 是否必填：否 - 任务ID</li>
        :type Filters: list of RunTimeFilters
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusListResponse(AbstractModel):
    """DescribeVirusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 木马列表
        :type List: list of VirusInfo
        :param TotalCount: 总数量
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
                obj = VirusInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVirusMonitorSettingRequest(AbstractModel):
    """DescribeVirusMonitorSetting请求参数结构体

    """


class DescribeVirusMonitorSettingResponse(AbstractModel):
    """DescribeVirusMonitorSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param EnableScan: 是否开启实时监控
        :type EnableScan: bool
        :param ScanPathAll: 扫描全部路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPathAll: bool
        :param ScanPathType: 当ScanPathAll为true 生效 0扫描以下路径 1、扫描除以下路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPathType: int
        :param ScanPath: 自选排除或扫描的地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPath: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnableScan = None
        self.ScanPathAll = None
        self.ScanPathType = None
        self.ScanPath = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnableScan = params.get("EnableScan")
        self.ScanPathAll = params.get("ScanPathAll")
        self.ScanPathType = params.get("ScanPathType")
        self.ScanPath = params.get("ScanPath")
        self.RequestId = params.get("RequestId")


class DescribeVirusScanSettingRequest(AbstractModel):
    """DescribeVirusScanSetting请求参数结构体

    """


class DescribeVirusScanSettingResponse(AbstractModel):
    """DescribeVirusScanSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param EnableScan: 是否开启定期扫描
        :type EnableScan: bool
        :param Cycle: 检测周期每隔多少天
        :type Cycle: int
        :param BeginScanAt: 扫描开始时间
        :type BeginScanAt: str
        :param ScanPathAll: 扫描全部路径
        :type ScanPathAll: bool
        :param ScanPathType: 当ScanPathAll为true 生效 0扫描以下路径 1、扫描除以下路径
        :type ScanPathType: int
        :param Timeout: 超时时长，单位小时
        :type Timeout: int
        :param ScanRangeType: 扫描范围0容器1主机节点
        :type ScanRangeType: int
        :param ScanRangeAll: true 全选，false 自选
        :type ScanRangeAll: bool
        :param ScanIds: 自选扫描范围的容器id或者主机id 根据ScanRangeType决定
        :type ScanIds: list of str
        :param ScanPath: 自选排除或扫描的地址
        :type ScanPath: list of str
        :param ClickTimeout: 一键检测的超时设置
注意：此字段可能返回 null，表示取不到有效值。
        :type ClickTimeout: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnableScan = None
        self.Cycle = None
        self.BeginScanAt = None
        self.ScanPathAll = None
        self.ScanPathType = None
        self.Timeout = None
        self.ScanRangeType = None
        self.ScanRangeAll = None
        self.ScanIds = None
        self.ScanPath = None
        self.ClickTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnableScan = params.get("EnableScan")
        self.Cycle = params.get("Cycle")
        self.BeginScanAt = params.get("BeginScanAt")
        self.ScanPathAll = params.get("ScanPathAll")
        self.ScanPathType = params.get("ScanPathType")
        self.Timeout = params.get("Timeout")
        self.ScanRangeType = params.get("ScanRangeType")
        self.ScanRangeAll = params.get("ScanRangeAll")
        self.ScanIds = params.get("ScanIds")
        self.ScanPath = params.get("ScanPath")
        self.ClickTimeout = params.get("ClickTimeout")
        self.RequestId = params.get("RequestId")


class DescribeVirusScanTaskStatusRequest(AbstractModel):
    """DescribeVirusScanTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        """
        self.TaskID = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusScanTaskStatusResponse(AbstractModel):
    """DescribeVirusScanTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerTotal: 查杀容器个数
        :type ContainerTotal: int
        :param RiskContainerCnt: 风险容器个数
        :type RiskContainerCnt: int
        :param Status: 扫描状态 任务状态:
SCAN_NONE:无， 
SCAN_SCANNING:正在扫描中，
SCAN_FINISH：扫描完成， 
SCAN_TIMEOUT：扫描超时
SCAN_CANCELING: 取消中
SCAN_CANCELED:已取消
        :type Status: str
        :param Schedule: 扫描进度 I
        :type Schedule: int
        :param ContainerScanCnt: 已经扫描了的容器个数
        :type ContainerScanCnt: int
        :param RiskCnt: 风险个数
        :type RiskCnt: int
        :param LeftSeconds: 剩余扫描时间
        :type LeftSeconds: int
        :param StartTime: 扫描开始时间
        :type StartTime: str
        :param EndTime: 扫描结束时间
        :type EndTime: str
        :param ScanType: 扫描类型，"CYCLE"：周期扫描， "MANUAL"：手动扫描
        :type ScanType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContainerTotal = None
        self.RiskContainerCnt = None
        self.Status = None
        self.Schedule = None
        self.ContainerScanCnt = None
        self.RiskCnt = None
        self.LeftSeconds = None
        self.StartTime = None
        self.EndTime = None
        self.ScanType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ContainerTotal = params.get("ContainerTotal")
        self.RiskContainerCnt = params.get("RiskContainerCnt")
        self.Status = params.get("Status")
        self.Schedule = params.get("Schedule")
        self.ContainerScanCnt = params.get("ContainerScanCnt")
        self.RiskCnt = params.get("RiskCnt")
        self.LeftSeconds = params.get("LeftSeconds")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ScanType = params.get("ScanType")
        self.RequestId = params.get("RequestId")


class DescribeVirusScanTimeoutSettingRequest(AbstractModel):
    """DescribeVirusScanTimeoutSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScanType: 设置类型0一键检测，1定时检测
        :type ScanType: int
        """
        self.ScanType = None


    def _deserialize(self, params):
        self.ScanType = params.get("ScanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusScanTimeoutSettingResponse(AbstractModel):
    """DescribeVirusScanTimeoutSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param Timeout: 超时时长单位小时
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Timeout = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Timeout = params.get("Timeout")
        self.RequestId = params.get("RequestId")


class DescribeVirusSummaryRequest(AbstractModel):
    """DescribeVirusSummary请求参数结构体

    """


class DescribeVirusSummaryResponse(AbstractModel):
    """DescribeVirusSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 最近的一次扫描任务id
        :type TaskId: str
        :param RiskContainerCnt: 木马影响容器个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskContainerCnt: int
        :param RiskCnt: 待处理风险个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCnt: int
        :param VirusDataBaseModifyTime: 病毒库更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusDataBaseModifyTime: str
        :param RiskContainerIncrease: 木马影响容器个数较昨日增长
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskContainerIncrease: int
        :param RiskIncrease: 待处理风险个数较昨日增长
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskIncrease: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RiskContainerCnt = None
        self.RiskCnt = None
        self.VirusDataBaseModifyTime = None
        self.RiskContainerIncrease = None
        self.RiskIncrease = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RiskContainerCnt = params.get("RiskContainerCnt")
        self.RiskCnt = params.get("RiskCnt")
        self.VirusDataBaseModifyTime = params.get("VirusDataBaseModifyTime")
        self.RiskContainerIncrease = params.get("RiskContainerIncrease")
        self.RiskIncrease = params.get("RiskIncrease")
        self.RequestId = params.get("RequestId")


class DescribeVirusTaskListRequest(AbstractModel):
    """DescribeVirusTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ContainerName - String - 是否必填：否 - 容器名称</li>
<li>ContainerId - String - 是否必填：否 - 容器id</li>
<li>Hostname - String - 是否必填：否 - 主机名称</li>
<li>HostIp- String - 是否必填：是 - 容器名称</li>
        :type Filters: list of RunTimeFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式
        :type Order: str
        """
        self.TaskId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusTaskListResponse(AbstractModel):
    """DescribeVirusTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 文件查杀列表
        :type List: list of VirusTaskInfo
        :param TotalCount: 总数量
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
                obj = VirusTaskInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWarningRulesRequest(AbstractModel):
    """DescribeWarningRules请求参数结构体

    """


class DescribeWarningRulesResponse(AbstractModel):
    """DescribeWarningRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param WarningRules: 告警策略列表
        :type WarningRules: list of WarningRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WarningRules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WarningRules") is not None:
            self.WarningRules = []
            for item in params.get("WarningRules"):
                obj = WarningRule()
                obj._deserialize(item)
                self.WarningRules.append(obj)
        self.RequestId = params.get("RequestId")


class EscapeEventDescription(AbstractModel):
    """运行时容器逃逸事件描述信息

    """

    def __init__(self):
        r"""
        :param Description: 事件规则
        :type Description: str
        :param Solution: 解决方案
        :type Solution: str
        :param Remark: 事件备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EscapeEventInfo(AbstractModel):
    """容器逃逸事件列表

    """

    def __init__(self):
        r"""
        :param EventType: 事件类型
   ESCAPE_HOST_ACESS_FILE:宿主机文件访问逃逸
   ESCAPE_MOUNT_NAMESPACE:MountNamespace逃逸
   ESCAPE_PRIVILEDGE:程序提权逃逸
   ESCAPE_PRIVILEDGE_CONTAINER_START:特权容器启动逃逸
   ESCAPE_MOUNT_SENSITIVE_PTAH:敏感路径挂载
   ESCAPE_SYSCALL:Syscall逃逸
        :type EventType: str
        :param ContainerName: 容器名
        :type ContainerName: str
        :param ImageName: 镜像名
        :type ImageName: str
        :param Status: 状态
     EVENT_UNDEAL:事件未处理
     EVENT_DEALED:事件已经处理
     EVENT_INGNORE：事件忽略
        :type Status: str
        :param EventId: 事件记录的唯一id
        :type EventId: str
        :param NodeName: 节点名称
        :type NodeName: str
        :param PodName: pod(实例)的名字
        :type PodName: str
        :param FoundTime: 生成时间
        :type FoundTime: str
        :param EventName: 事件名字，
宿主机文件访问逃逸、
Syscall逃逸、
MountNamespace逃逸、
程序提权逃逸、
特权容器启动逃逸、
敏感路径挂载
        :type EventName: str
        :param ImageId: 镜像id，用于跳转
        :type ImageId: str
        :param ContainerId: 容器id，用于跳转
        :type ContainerId: str
        :param Solution: 事件解决方案
        :type Solution: str
        :param Description: 事件描述
        :type Description: str
        :param EventCount: 事件数量
        :type EventCount: int
        :param LatestFoundTime: 最近生成时间
        :type LatestFoundTime: str
        """
        self.EventType = None
        self.ContainerName = None
        self.ImageName = None
        self.Status = None
        self.EventId = None
        self.NodeName = None
        self.PodName = None
        self.FoundTime = None
        self.EventName = None
        self.ImageId = None
        self.ContainerId = None
        self.Solution = None
        self.Description = None
        self.EventCount = None
        self.LatestFoundTime = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        self.ContainerName = params.get("ContainerName")
        self.ImageName = params.get("ImageName")
        self.Status = params.get("Status")
        self.EventId = params.get("EventId")
        self.NodeName = params.get("NodeName")
        self.PodName = params.get("PodName")
        self.FoundTime = params.get("FoundTime")
        self.EventName = params.get("EventName")
        self.ImageId = params.get("ImageId")
        self.ContainerId = params.get("ContainerId")
        self.Solution = params.get("Solution")
        self.Description = params.get("Description")
        self.EventCount = params.get("EventCount")
        self.LatestFoundTime = params.get("LatestFoundTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EscapeRule(AbstractModel):
    """容器逃逸扫描策略开关信息

    """

    def __init__(self):
        r"""
        :param Type: 规则类型   
ESCAPE_HOST_ACESS_FILE:宿主机文件访问逃逸
   ESCAPE_MOUNT_NAMESPACE:MountNamespace逃逸
   ESCAPE_PRIVILEDGE:程序提权逃逸
   ESCAPE_PRIVILEDGE_CONTAINER_START:特权容器启动逃逸
   ESCAPE_MOUNT_SENSITIVE_PTAH:敏感路径挂载
ESCAPE_SYSCALL:Syscall逃逸
        :type Type: str
        :param Name: 规则名称
宿主机文件访问逃逸、
Syscall逃逸、
MountNamespace逃逸、
程序提权逃逸、
特权容器启动逃逸、
敏感路径挂载
        :type Name: str
        :param IsEnable: 是否打开：false否 ，true是
        :type IsEnable: bool
        """
        self.Type = None
        self.Name = None
        self.IsEnable = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.IsEnable = params.get("IsEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EscapeRuleEnabled(AbstractModel):
    """修改容器逃逸扫描策略开关信息

    """

    def __init__(self):
        r"""
        :param Type: 规则类型
   ESCAPE_HOST_ACESS_FILE:宿主机文件访问逃逸
   ESCAPE_MOUNT_NAMESPACE:MountNamespace逃逸
   ESCAPE_PRIVILEDGE:程序提权逃逸
   ESCAPE_PRIVILEDGE_CONTAINER_START:特权容器启动逃逸
   ESCAPE_MOUNT_SENSITIVE_PTAH:敏感路径挂载
   ESCAPE_SYSCALL:Syscall逃逸
        :type Type: str
        :param IsEnable: 是否打开：false否 ，true是
        :type IsEnable: bool
        """
        self.Type = None
        self.IsEnable = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.IsEnable = params.get("IsEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVirusListRequest(AbstractModel):
    """ExportVirusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>FileName - String - 是否必填：否 - 文件名称</li>
<li>FilePath - String - 是否必填：否 - 文件路径</li>
<li>VirusName - String - 是否必填：否 - 病毒名称</li>
<li>ContainerName- String - 是否必填：是 - 容器名称</li>
<li>ContainerId- string - 是否必填：否 - 容器id</li>
<li>ImageName- string - 是否必填：否 - 镜像名称</li>
<li>ImageId- string - 是否必填：否 - 镜像id</li>
        :type Filters: list of RunTimeFilters
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
        :type By: str
        :param ExportField: 导出字段
        :type ExportField: list of str
        """
        self.Filters = None
        self.Order = None
        self.By = None
        self.ExportField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        self.ExportField = params.get("ExportField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVirusListResponse(AbstractModel):
    """ExportVirusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 导出任务ID，前端拿着任务ID查询任务进度
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class FileAttributeInfo(AbstractModel):
    """容器安全运行时，文件属性信息

    """

    def __init__(self):
        r"""
        :param FileName: 文件名
        :type FileName: str
        :param FileType: 文件类型
        :type FileType: str
        :param FileSize: 文件大小(字节)
        :type FileSize: int
        :param FilePath: 文件路径
        :type FilePath: str
        :param FileCreateTime: 文件创建时间
        :type FileCreateTime: str
        :param LatestTamperedFileMTime: 最近被篡改文件创建时间
        :type LatestTamperedFileMTime: str
        """
        self.FileName = None
        self.FileType = None
        self.FileSize = None
        self.FilePath = None
        self.FileCreateTime = None
        self.LatestTamperedFileMTime = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileSize = params.get("FileSize")
        self.FilePath = params.get("FilePath")
        self.FileCreateTime = params.get("FileCreateTime")
        self.LatestTamperedFileMTime = params.get("LatestTamperedFileMTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostInfo(AbstractModel):
    """容器安全主机列表

    """

    def __init__(self):
        r"""
        :param HostID: 主机id
        :type HostID: str
        :param HostIP: 主机ip即内网ip
        :type HostIP: str
        :param HostName: 主机名称
        :type HostName: str
        :param Group: 业务组
        :type Group: str
        :param DockerVersion: docker 版本
        :type DockerVersion: str
        :param DockerFileSystemDriver: docker 文件系统类型
        :type DockerFileSystemDriver: str
        :param ImageCnt: 镜像个数
        :type ImageCnt: int
        :param ContainerCnt: 容器个数
        :type ContainerCnt: int
        :param Status: agent运行状态
        :type Status: str
        :param IsContainerd: 是否是Containerd
        :type IsContainerd: bool
        :param MachineType: 主机来源：["CVM", "ECM", "LH", "BM"]  中的之一为腾讯云服务器；["Other"]之一非腾讯云服务器；
        :type MachineType: str
        :param PublicIp: 外网ip
        :type PublicIp: str
        :param Uuid: 主机uuid
        :type Uuid: str
        :param InstanceID: 主机实例ID
        :type InstanceID: str
        :param RegionID: 地域ID
        :type RegionID: int
        """
        self.HostID = None
        self.HostIP = None
        self.HostName = None
        self.Group = None
        self.DockerVersion = None
        self.DockerFileSystemDriver = None
        self.ImageCnt = None
        self.ContainerCnt = None
        self.Status = None
        self.IsContainerd = None
        self.MachineType = None
        self.PublicIp = None
        self.Uuid = None
        self.InstanceID = None
        self.RegionID = None


    def _deserialize(self, params):
        self.HostID = params.get("HostID")
        self.HostIP = params.get("HostIP")
        self.HostName = params.get("HostName")
        self.Group = params.get("Group")
        self.DockerVersion = params.get("DockerVersion")
        self.DockerFileSystemDriver = params.get("DockerFileSystemDriver")
        self.ImageCnt = params.get("ImageCnt")
        self.ContainerCnt = params.get("ContainerCnt")
        self.Status = params.get("Status")
        self.IsContainerd = params.get("IsContainerd")
        self.MachineType = params.get("MachineType")
        self.PublicIp = params.get("PublicIp")
        self.Uuid = params.get("Uuid")
        self.InstanceID = params.get("InstanceID")
        self.RegionID = params.get("RegionID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageHost(AbstractModel):
    """容器安全 主机镜像关联列表

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像id
        :type ImageID: str
        :param HostID: 主机id
        :type HostID: str
        """
        self.ImageID = None
        self.HostID = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.HostID = params.get("HostID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """基本镜像信息

    """

    def __init__(self):
        r"""
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageTag: 镜像tag
        :type ImageTag: str
        :param Force: 强制扫描
        :type Force: str
        :param ImageDigest: 镜像id
        :type ImageDigest: str
        :param RegistryType: 仓库类型
        :type RegistryType: str
        :param ImageRepoAddress: 镜像仓库地址
        :type ImageRepoAddress: str
        :param InstanceId: 实例id
        :type InstanceId: str
        """
        self.InstanceName = None
        self.Namespace = None
        self.ImageName = None
        self.ImageTag = None
        self.Force = None
        self.ImageDigest = None
        self.RegistryType = None
        self.ImageRepoAddress = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.Namespace = params.get("Namespace")
        self.ImageName = params.get("ImageName")
        self.ImageTag = params.get("ImageTag")
        self.Force = params.get("Force")
        self.ImageDigest = params.get("ImageDigest")
        self.RegistryType = params.get("RegistryType")
        self.ImageRepoAddress = params.get("ImageRepoAddress")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageProgress(AbstractModel):
    """基本镜像信息

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像id
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param RegistryType: 仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryType: str
        :param ImageRepoAddress: 镜像仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageRepoAddress: str
        :param InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param ImageName: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageName: str
        :param ImageTag: 镜像tag
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTag: str
        :param ScanStatus: 镜像扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanStatus: str
        :param CveProgress: 镜像cve扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CveProgress: int
        :param RiskProgress: 镜像敏感扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskProgress: int
        :param VirusProgress: 镜像木马扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusProgress: int
        """
        self.ImageId = None
        self.RegistryType = None
        self.ImageRepoAddress = None
        self.InstanceId = None
        self.InstanceName = None
        self.Namespace = None
        self.ImageName = None
        self.ImageTag = None
        self.ScanStatus = None
        self.CveProgress = None
        self.RiskProgress = None
        self.VirusProgress = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.RegistryType = params.get("RegistryType")
        self.ImageRepoAddress = params.get("ImageRepoAddress")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Namespace = params.get("Namespace")
        self.ImageName = params.get("ImageName")
        self.ImageTag = params.get("ImageTag")
        self.ScanStatus = params.get("ScanStatus")
        self.CveProgress = params.get("CveProgress")
        self.RiskProgress = params.get("RiskProgress")
        self.VirusProgress = params.get("VirusProgress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRepoInfo(AbstractModel):
    """容器安全镜像仓库列表

    """

    def __init__(self):
        r"""
        :param ImageDigest: 镜像Digest
        :type ImageDigest: str
        :param ImageRepoAddress: 镜像仓库地址
        :type ImageRepoAddress: str
        :param RegistryType: 仓库类型
        :type RegistryType: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageTag: 镜像版本
        :type ImageTag: str
        :param ImageSize: 镜像大小
        :type ImageSize: int
        :param ScanTime: 最近扫描时间
        :type ScanTime: str
        :param ScanStatus: 扫描状态
        :type ScanStatus: str
        :param VulCnt: 安全漏洞数
        :type VulCnt: int
        :param VirusCnt: 木马病毒数
        :type VirusCnt: int
        :param RiskCnt: 风险行为数
        :type RiskCnt: int
        :param SentiveInfoCnt: 敏感信息数
        :type SentiveInfoCnt: int
        :param IsTrustImage: 是否可信镜像
        :type IsTrustImage: bool
        :param OsName: 镜像系统
        :type OsName: str
        :param ScanVirusError: 木马扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVirusError: str
        :param ScanVulError: 漏洞扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVulError: str
        :param InstanceId: 实例id
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param ScanRiskError: 高危扫描错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRiskError: str
        :param ScanVirusProgress: 敏感信息扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVirusProgress: int
        :param ScanVulProgress: 木马扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVulProgress: int
        :param ScanRiskProgress: 漏洞扫描进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRiskProgress: int
        :param ScanRemainTime: 剩余扫描时间秒
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRemainTime: int
        :param CveStatus: cve扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CveStatus: str
        :param RiskStatus: 高危扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskStatus: str
        :param VirusStatus: 木马扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusStatus: str
        :param Progress: 总进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param IsAuthorized: 授权状态
        :type IsAuthorized: int
        :param RegistryRegion: 仓库区域
        :type RegistryRegion: str
        :param Id: 列表id
        :type Id: int
        :param ImageId: 镜像Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param ImageCreateTime: 镜像创建的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCreateTime: str
        :param IsLatestImage: 是否为镜像的最新版本
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLatestImage: bool
        """
        self.ImageDigest = None
        self.ImageRepoAddress = None
        self.RegistryType = None
        self.ImageName = None
        self.ImageTag = None
        self.ImageSize = None
        self.ScanTime = None
        self.ScanStatus = None
        self.VulCnt = None
        self.VirusCnt = None
        self.RiskCnt = None
        self.SentiveInfoCnt = None
        self.IsTrustImage = None
        self.OsName = None
        self.ScanVirusError = None
        self.ScanVulError = None
        self.InstanceId = None
        self.InstanceName = None
        self.Namespace = None
        self.ScanRiskError = None
        self.ScanVirusProgress = None
        self.ScanVulProgress = None
        self.ScanRiskProgress = None
        self.ScanRemainTime = None
        self.CveStatus = None
        self.RiskStatus = None
        self.VirusStatus = None
        self.Progress = None
        self.IsAuthorized = None
        self.RegistryRegion = None
        self.Id = None
        self.ImageId = None
        self.ImageCreateTime = None
        self.IsLatestImage = None


    def _deserialize(self, params):
        self.ImageDigest = params.get("ImageDigest")
        self.ImageRepoAddress = params.get("ImageRepoAddress")
        self.RegistryType = params.get("RegistryType")
        self.ImageName = params.get("ImageName")
        self.ImageTag = params.get("ImageTag")
        self.ImageSize = params.get("ImageSize")
        self.ScanTime = params.get("ScanTime")
        self.ScanStatus = params.get("ScanStatus")
        self.VulCnt = params.get("VulCnt")
        self.VirusCnt = params.get("VirusCnt")
        self.RiskCnt = params.get("RiskCnt")
        self.SentiveInfoCnt = params.get("SentiveInfoCnt")
        self.IsTrustImage = params.get("IsTrustImage")
        self.OsName = params.get("OsName")
        self.ScanVirusError = params.get("ScanVirusError")
        self.ScanVulError = params.get("ScanVulError")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Namespace = params.get("Namespace")
        self.ScanRiskError = params.get("ScanRiskError")
        self.ScanVirusProgress = params.get("ScanVirusProgress")
        self.ScanVulProgress = params.get("ScanVulProgress")
        self.ScanRiskProgress = params.get("ScanRiskProgress")
        self.ScanRemainTime = params.get("ScanRemainTime")
        self.CveStatus = params.get("CveStatus")
        self.RiskStatus = params.get("RiskStatus")
        self.VirusStatus = params.get("VirusStatus")
        self.Progress = params.get("Progress")
        self.IsAuthorized = params.get("IsAuthorized")
        self.RegistryRegion = params.get("RegistryRegion")
        self.Id = params.get("Id")
        self.ImageId = params.get("ImageId")
        self.ImageCreateTime = params.get("ImageCreateTime")
        self.IsLatestImage = params.get("IsLatestImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRisk(AbstractModel):
    """容器安全镜像高危行为信息

    """

    def __init__(self):
        r"""
        :param Behavior: 高危行为
注意：此字段可能返回 null，表示取不到有效值。
        :type Behavior: int
        :param Type: 种类
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param Level: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param InstructionContent: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type InstructionContent: str
        """
        self.Behavior = None
        self.Type = None
        self.Level = None
        self.Desc = None
        self.InstructionContent = None


    def _deserialize(self, params):
        self.Behavior = params.get("Behavior")
        self.Type = params.get("Type")
        self.Level = params.get("Level")
        self.Desc = params.get("Desc")
        self.InstructionContent = params.get("InstructionContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRiskInfo(AbstractModel):
    """镜像风险详情

    """

    def __init__(self):
        r"""
        :param Behavior: 行为
        :type Behavior: int
        :param Type: 类型
        :type Type: int
        :param Level: 级别
        :type Level: int
        :param Desc: 详情
        :type Desc: str
        :param InstructionContent: 解决方案
        :type InstructionContent: str
        """
        self.Behavior = None
        self.Type = None
        self.Level = None
        self.Desc = None
        self.InstructionContent = None


    def _deserialize(self, params):
        self.Behavior = params.get("Behavior")
        self.Type = params.get("Type")
        self.Level = params.get("Level")
        self.Desc = params.get("Desc")
        self.InstructionContent = params.get("InstructionContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRiskTendencyInfo(AbstractModel):
    """运行时安全事件趋势信息

    """

    def __init__(self):
        r"""
        :param ImageRiskSet: 趋势列表
        :type ImageRiskSet: list of RunTimeTendencyInfo
        :param ImageRiskType: 风险类型：
IRT_VULNERABILITY : 安全漏洞
IRT_MALWARE_VIRUS: 木马病毒
IRT_RISK:敏感信息
        :type ImageRiskType: str
        """
        self.ImageRiskSet = None
        self.ImageRiskType = None


    def _deserialize(self, params):
        if params.get("ImageRiskSet") is not None:
            self.ImageRiskSet = []
            for item in params.get("ImageRiskSet"):
                obj = RunTimeTendencyInfo()
                obj._deserialize(item)
                self.ImageRiskSet.append(obj)
        self.ImageRiskType = params.get("ImageRiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSimpleInfo(AbstractModel):
    """镜像列表

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像id
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param Size: 镜像大小
        :type Size: int
        :param ImageType: 类型
        :type ImageType: str
        :param ContainerCnt: 关联容器数
        :type ContainerCnt: int
        """
        self.ImageID = None
        self.ImageName = None
        self.Size = None
        self.ImageType = None
        self.ContainerCnt = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.Size = params.get("Size")
        self.ImageType = params.get("ImageType")
        self.ContainerCnt = params.get("ContainerCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageVirus(AbstractModel):
    """容器安全镜像病毒信息

    """

    def __init__(self):
        r"""
        :param Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param RiskLevel: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param Category: 分类
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param VirusName: 病毒名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusName: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Solution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param FileName: 文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileMd5: 文件md5
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMd5: str
        :param FileSize: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param FirstScanTime: 首次发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstScanTime: str
        :param LatestScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestScanTime: str
        """
        self.Path = None
        self.RiskLevel = None
        self.Category = None
        self.VirusName = None
        self.Tags = None
        self.Desc = None
        self.Solution = None
        self.FileType = None
        self.FileName = None
        self.FileMd5 = None
        self.FileSize = None
        self.FirstScanTime = None
        self.LatestScanTime = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.RiskLevel = params.get("RiskLevel")
        self.Category = params.get("Category")
        self.VirusName = params.get("VirusName")
        self.Tags = params.get("Tags")
        self.Desc = params.get("Desc")
        self.Solution = params.get("Solution")
        self.FileType = params.get("FileType")
        self.FileName = params.get("FileName")
        self.FileMd5 = params.get("FileMd5")
        self.FileSize = params.get("FileSize")
        self.FirstScanTime = params.get("FirstScanTime")
        self.LatestScanTime = params.get("LatestScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageVirusInfo(AbstractModel):
    """容器安全镜像病毒信息

    """

    def __init__(self):
        r"""
        :param Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param RiskLevel: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: int
        :param VirusName: 病毒名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusName: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Solution: 修护建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Solution: str
        :param Size: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param FirstScanTime: 首次发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstScanTime: str
        :param LatestScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestScanTime: str
        :param Md5: 文件md5
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param FileName: 文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        """
        self.Path = None
        self.RiskLevel = None
        self.VirusName = None
        self.Tags = None
        self.Desc = None
        self.Solution = None
        self.Size = None
        self.FirstScanTime = None
        self.LatestScanTime = None
        self.Md5 = None
        self.FileName = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.RiskLevel = params.get("RiskLevel")
        self.VirusName = params.get("VirusName")
        self.Tags = params.get("Tags")
        self.Desc = params.get("Desc")
        self.Solution = params.get("Solution")
        self.Size = params.get("Size")
        self.FirstScanTime = params.get("FirstScanTime")
        self.LatestScanTime = params.get("LatestScanTime")
        self.Md5 = params.get("Md5")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageVul(AbstractModel):
    """容器安全镜像漏洞信息

    """

    def __init__(self):
        r"""
        :param CVEID: 漏洞id
注意：此字段可能返回 null，表示取不到有效值。
        :type CVEID: str
        :param POCID: 观点验证程序id
注意：此字段可能返回 null，表示取不到有效值。
        :type POCID: str
        :param Name: 漏洞名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Components: 涉及组件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Components: list of ComponentsInfo
        :param Category: 分类
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param CategoryType: 分类2
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryType: str
        :param Level: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param Des: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Des: str
        :param OfficialSolution: 解决方案
注意：此字段可能返回 null，表示取不到有效值。
        :type OfficialSolution: str
        :param Reference: 引用
注意：此字段可能返回 null，表示取不到有效值。
        :type Reference: str
        :param DefenseSolution: 防御方案
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseSolution: str
        :param SubmitTime: 提交时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitTime: str
        :param CvssScore: Cvss分数
注意：此字段可能返回 null，表示取不到有效值。
        :type CvssScore: str
        :param CvssVector: Cvss信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CvssVector: str
        :param IsSuggest: 是否建议修复
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSuggest: str
        :param FixedVersions: 修复版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type FixedVersions: str
        :param Tag: 漏洞标签:"CanBeFixed","DynamicLevelPoc","DynamicLevelExp"
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of str
        :param Component: 组件名
注意：此字段可能返回 null，表示取不到有效值。
        :type Component: str
        :param Version: 组件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self.CVEID = None
        self.POCID = None
        self.Name = None
        self.Components = None
        self.Category = None
        self.CategoryType = None
        self.Level = None
        self.Des = None
        self.OfficialSolution = None
        self.Reference = None
        self.DefenseSolution = None
        self.SubmitTime = None
        self.CvssScore = None
        self.CvssVector = None
        self.IsSuggest = None
        self.FixedVersions = None
        self.Tag = None
        self.Component = None
        self.Version = None


    def _deserialize(self, params):
        self.CVEID = params.get("CVEID")
        self.POCID = params.get("POCID")
        self.Name = params.get("Name")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = ComponentsInfo()
                obj._deserialize(item)
                self.Components.append(obj)
        self.Category = params.get("Category")
        self.CategoryType = params.get("CategoryType")
        self.Level = params.get("Level")
        self.Des = params.get("Des")
        self.OfficialSolution = params.get("OfficialSolution")
        self.Reference = params.get("Reference")
        self.DefenseSolution = params.get("DefenseSolution")
        self.SubmitTime = params.get("SubmitTime")
        self.CvssScore = params.get("CvssScore")
        self.CvssVector = params.get("CvssVector")
        self.IsSuggest = params.get("IsSuggest")
        self.FixedVersions = params.get("FixedVersions")
        self.Tag = params.get("Tag")
        self.Component = params.get("Component")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImagesBindRuleInfo(AbstractModel):
    """查询镜像绑定的运行时规则信息

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像id
        :type ImageId: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ContainerCnt: 关联容器数量
        :type ContainerCnt: int
        :param RuleId: 绑定规则id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param RuleName: 规则名字
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param ImageSize: 镜像大小
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSize: int
        :param ScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTime: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ContainerCnt = None
        self.RuleId = None
        self.RuleName = None
        self.ImageSize = None
        self.ScanTime = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ContainerCnt = params.get("ContainerCnt")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.ImageSize = params.get("ImageSize")
        self.ScanTime = params.get("ScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImagesInfo(AbstractModel):
    """容器安全镜像列表

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像id
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Size: 镜像大小
        :type Size: int
        :param HostCnt: 主机个数
        :type HostCnt: int
        :param ContainerCnt: 容器个数
        :type ContainerCnt: int
        :param ScanTime: 扫描时间
        :type ScanTime: str
        :param VulCnt: 漏洞个数
        :type VulCnt: int
        :param VirusCnt: 病毒个数
        :type VirusCnt: int
        :param RiskCnt: 敏感信息个数
        :type RiskCnt: int
        :param IsTrustImage: 是否信任镜像
        :type IsTrustImage: bool
        :param OsName: 镜像系统
        :type OsName: str
        :param AgentError: agent镜像扫描错误
        :type AgentError: str
        :param ScanError: 后端镜像扫描错误
        :type ScanError: str
        :param ScanStatus: 扫描状态
        :type ScanStatus: str
        :param ScanVirusError: 木马扫描错误信息
        :type ScanVirusError: str
        :param ScanVulError: 漏洞扫描错误信息
        :type ScanVulError: str
        :param ScanRiskError: 风险扫描错误信息
        :type ScanRiskError: str
        :param IsSuggest: 是否是重点关注镜像，为0不是，非0是
        :type IsSuggest: int
        :param IsAuthorized: 是否授权，1是0否
        :type IsAuthorized: int
        """
        self.ImageID = None
        self.ImageName = None
        self.CreateTime = None
        self.Size = None
        self.HostCnt = None
        self.ContainerCnt = None
        self.ScanTime = None
        self.VulCnt = None
        self.VirusCnt = None
        self.RiskCnt = None
        self.IsTrustImage = None
        self.OsName = None
        self.AgentError = None
        self.ScanError = None
        self.ScanStatus = None
        self.ScanVirusError = None
        self.ScanVulError = None
        self.ScanRiskError = None
        self.IsSuggest = None
        self.IsAuthorized = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.CreateTime = params.get("CreateTime")
        self.Size = params.get("Size")
        self.HostCnt = params.get("HostCnt")
        self.ContainerCnt = params.get("ContainerCnt")
        self.ScanTime = params.get("ScanTime")
        self.VulCnt = params.get("VulCnt")
        self.VirusCnt = params.get("VirusCnt")
        self.RiskCnt = params.get("RiskCnt")
        self.IsTrustImage = params.get("IsTrustImage")
        self.OsName = params.get("OsName")
        self.AgentError = params.get("AgentError")
        self.ScanError = params.get("ScanError")
        self.ScanStatus = params.get("ScanStatus")
        self.ScanVirusError = params.get("ScanVirusError")
        self.ScanVulError = params.get("ScanVulError")
        self.ScanRiskError = params.get("ScanRiskError")
        self.IsSuggest = params.get("IsSuggest")
        self.IsAuthorized = params.get("IsAuthorized")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImagesVul(AbstractModel):
    """容器安全镜像漏洞

    """

    def __init__(self):
        r"""
        :param CVEID: 漏洞id
        :type CVEID: str
        :param Name: 漏洞名称
        :type Name: str
        :param Component: 组件
        :type Component: str
        :param Version: 版本
        :type Version: str
        :param Category: 分类
        :type Category: str
        :param CategoryType: 分类2
        :type CategoryType: str
        :param Level: 风险等级
        :type Level: int
        :param Des: 描述
        :type Des: str
        :param OfficialSolution: 解决方案
        :type OfficialSolution: str
        :param Reference: 引用
        :type Reference: str
        :param DefenseSolution: 防御方案
        :type DefenseSolution: str
        :param SubmitTime: 提交时间
        :type SubmitTime: str
        :param CVSSV3Score: CVSS V3分数
        :type CVSSV3Score: float
        :param CVSSV3Desc: CVSS V3描述
        :type CVSSV3Desc: str
        :param IsSuggest: 是否是重点关注：true：是，false：不是
        :type IsSuggest: bool
        :param FixedVersions: 修复版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type FixedVersions: str
        :param Tag: 漏洞标签:"CanBeFixed","DynamicLevelPoc","DynamicLevelExp"
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of str
        """
        self.CVEID = None
        self.Name = None
        self.Component = None
        self.Version = None
        self.Category = None
        self.CategoryType = None
        self.Level = None
        self.Des = None
        self.OfficialSolution = None
        self.Reference = None
        self.DefenseSolution = None
        self.SubmitTime = None
        self.CVSSV3Score = None
        self.CVSSV3Desc = None
        self.IsSuggest = None
        self.FixedVersions = None
        self.Tag = None


    def _deserialize(self, params):
        self.CVEID = params.get("CVEID")
        self.Name = params.get("Name")
        self.Component = params.get("Component")
        self.Version = params.get("Version")
        self.Category = params.get("Category")
        self.CategoryType = params.get("CategoryType")
        self.Level = params.get("Level")
        self.Des = params.get("Des")
        self.OfficialSolution = params.get("OfficialSolution")
        self.Reference = params.get("Reference")
        self.DefenseSolution = params.get("DefenseSolution")
        self.SubmitTime = params.get("SubmitTime")
        self.CVSSV3Score = params.get("CVSSV3Score")
        self.CVSSV3Desc = params.get("CVSSV3Desc")
        self.IsSuggest = params.get("IsSuggest")
        self.FixedVersions = params.get("FixedVersions")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeUserComplianceEnvironmentRequest(AbstractModel):
    """InitializeUserComplianceEnvironment请求参数结构体

    """


class InitializeUserComplianceEnvironmentResponse(AbstractModel):
    """InitializeUserComplianceEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAbnormalProcessRuleStatusRequest(AbstractModel):
    """ModifyAbnormalProcessRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleIdSet: 策略的ids
        :type RuleIdSet: list of str
        :param IsEnable: 策略开关，true开启，false关闭
        :type IsEnable: bool
        """
        self.RuleIdSet = None
        self.IsEnable = None


    def _deserialize(self, params):
        self.RuleIdSet = params.get("RuleIdSet")
        self.IsEnable = params.get("IsEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAbnormalProcessRuleStatusResponse(AbstractModel):
    """ModifyAbnormalProcessRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAbnormalProcessStatusRequest(AbstractModel):
    """ModifyAbnormalProcessStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIdSet: 处理事件ids
        :type EventIdSet: list of str
        :param Status: 标记事件的状态，   
    EVENT_DEALED:事件处理
    EVENT_INGNORE"：事件忽略
     EVENT_DEL:事件删除
     EVENT_ADD_WHITE:事件加白
        :type Status: str
        :param Remark: 事件备注
        :type Remark: str
        """
        self.EventIdSet = None
        self.Status = None
        self.Remark = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAbnormalProcessStatusResponse(AbstractModel):
    """ModifyAbnormalProcessStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccessControlRuleStatusRequest(AbstractModel):
    """ModifyAccessControlRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleIdSet: 策略的ids
        :type RuleIdSet: list of str
        :param IsEnable: 策略开关，true:代表开启， false代表关闭
        :type IsEnable: bool
        """
        self.RuleIdSet = None
        self.IsEnable = None


    def _deserialize(self, params):
        self.RuleIdSet = params.get("RuleIdSet")
        self.IsEnable = params.get("IsEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessControlRuleStatusResponse(AbstractModel):
    """ModifyAccessControlRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccessControlStatusRequest(AbstractModel):
    """ModifyAccessControlStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIdSet: 处理事件ids
        :type EventIdSet: list of str
        :param Status: 标记事件的状态，     
EVENT_DEALED:事件已经处理
     EVENT_INGNORE：事件忽略
     EVENT_DEL:事件删除
     EVENT_ADD_WHITE:事件加白
        :type Status: str
        :param Remark: 备注事件信息
        :type Remark: str
        """
        self.EventIdSet = None
        self.Status = None
        self.Remark = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessControlStatusResponse(AbstractModel):
    """ModifyAccessControlStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAssetImageRegistryScanStopOneKeyRequest(AbstractModel):
    """ModifyAssetImageRegistryScanStopOneKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param All: 是否扫描全部镜像
        :type All: bool
        :param Images: 扫描的镜像列表
        :type Images: list of ImageInfo
        :param Id: 扫描的镜像列表Id
        :type Id: list of int non-negative
        """
        self.All = None
        self.Images = None
        self.Id = None


    def _deserialize(self, params):
        self.All = params.get("All")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.Images.append(obj)
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssetImageRegistryScanStopOneKeyResponse(AbstractModel):
    """ModifyAssetImageRegistryScanStopOneKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAssetImageRegistryScanStopRequest(AbstractModel):
    """ModifyAssetImageRegistryScanStop请求参数结构体

    """

    def __init__(self):
        r"""
        :param All: 是否扫描全部镜像
        :type All: bool
        :param Images: 扫描的镜像列表
        :type Images: list of ImageInfo
        :param Id: 扫描的镜像列表
        :type Id: list of int non-negative
        :param Filters: 过滤条件
        :type Filters: list of AssetFilters
        :param ExcludeImageList: 不要扫描的镜像列表，与Filters配合使用
        :type ExcludeImageList: list of int non-negative
        :param OnlyScanLatest: 是否仅扫描各repository最新版本的镜像
        :type OnlyScanLatest: bool
        """
        self.All = None
        self.Images = None
        self.Id = None
        self.Filters = None
        self.ExcludeImageList = None
        self.OnlyScanLatest = None


    def _deserialize(self, params):
        self.All = params.get("All")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.Images.append(obj)
        self.Id = params.get("Id")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ExcludeImageList = params.get("ExcludeImageList")
        self.OnlyScanLatest = params.get("OnlyScanLatest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssetImageRegistryScanStopResponse(AbstractModel):
    """ModifyAssetImageRegistryScanStop返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAssetImageScanStopRequest(AbstractModel):
    """ModifyAssetImageScanStop请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        :param Images: 镜像id
        :type Images: list of str
        """
        self.TaskID = None
        self.Images = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.Images = params.get("Images")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssetImageScanStopResponse(AbstractModel):
    """ModifyAssetImageScanStop返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 停止状态
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyAssetRequest(AbstractModel):
    """ModifyAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param All: 全部同步
        :type All: bool
        :param Hosts: 要同步的主机列表 两个参数必选一个 All优先
        :type Hosts: list of str
        """
        self.All = None
        self.Hosts = None


    def _deserialize(self, params):
        self.All = params.get("All")
        self.Hosts = params.get("Hosts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssetResponse(AbstractModel):
    """ModifyAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 同步任务发送结果
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyCompliancePeriodTaskRequest(AbstractModel):
    """ModifyCompliancePeriodTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param PeriodTaskId: 要修改的定时任务的ID，由DescribeCompliancePeriodTaskList接口返回。
        :type PeriodTaskId: int
        :param PeriodRule: 定时任务的周期规则。不填时，不修改。
        :type PeriodRule: :class:`tencentcloud.tcss.v20201101.models.CompliancePeriodTaskRule`
        :param StandardSettings: 设置合规标准。不填时，不修改。
        :type StandardSettings: list of ComplianceBenchmarkStandardEnable
        """
        self.PeriodTaskId = None
        self.PeriodRule = None
        self.StandardSettings = None


    def _deserialize(self, params):
        self.PeriodTaskId = params.get("PeriodTaskId")
        if params.get("PeriodRule") is not None:
            self.PeriodRule = CompliancePeriodTaskRule()
            self.PeriodRule._deserialize(params.get("PeriodRule"))
        if params.get("StandardSettings") is not None:
            self.StandardSettings = []
            for item in params.get("StandardSettings"):
                obj = ComplianceBenchmarkStandardEnable()
                obj._deserialize(item)
                self.StandardSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompliancePeriodTaskResponse(AbstractModel):
    """ModifyCompliancePeriodTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEscapeEventStatusRequest(AbstractModel):
    """ModifyEscapeEventStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIdSet: 处理事件ids
        :type EventIdSet: list of str
        :param Status: 标记事件的状态
   EVENT_DEALED:事件已经处理
     EVENT_INGNORE：事件忽略
     EVENT_DEL:事件删除
        :type Status: str
        :param Remark: 备注
        :type Remark: str
        """
        self.EventIdSet = None
        self.Status = None
        self.Remark = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEscapeEventStatusResponse(AbstractModel):
    """ModifyEscapeEventStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEscapeRuleRequest(AbstractModel):
    """ModifyEscapeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleSet: 需要修改的数组
        :type RuleSet: list of EscapeRuleEnabled
        """
        self.RuleSet = None


    def _deserialize(self, params):
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = EscapeRuleEnabled()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEscapeRuleResponse(AbstractModel):
    """ModifyEscapeRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyReverseShellStatusRequest(AbstractModel):
    """ModifyReverseShellStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIdSet: 处理事件ids
        :type EventIdSet: list of str
        :param Status: 标记事件的状态，   
    EVENT_DEALED:事件处理
    EVENT_INGNORE"：事件忽略
     EVENT_DEL:事件删除
     EVENT_ADD_WHITE:事件加白
        :type Status: str
        :param Remark: 事件备注
        :type Remark: str
        """
        self.EventIdSet = None
        self.Status = None
        self.Remark = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReverseShellStatusResponse(AbstractModel):
    """ModifyReverseShellStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRiskSyscallStatusRequest(AbstractModel):
    """ModifyRiskSyscallStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIdSet: 处理事件ids
        :type EventIdSet: list of str
        :param Status: 标记事件的状态，   
    EVENT_DEALED:事件处理
    EVENT_INGNORE"：事件忽略
     EVENT_DEL:事件删除
     EVENT_ADD_WHITE:事件加白
        :type Status: str
        :param Remark: 事件备注
        :type Remark: str
        """
        self.EventIdSet = None
        self.Status = None
        self.Remark = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRiskSyscallStatusResponse(AbstractModel):
    """ModifyRiskSyscallStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVirusFileStatusRequest(AbstractModel):
    """ModifyVirusFileStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIdSet: 处理事件id
        :type EventIdSet: list of str
        :param Status: 标记事件的状态，   
    EVENT_DEALED:事件处理
    EVENT_INGNORE"：事件忽略
     EVENT_DEL:事件删除
     EVENT_ADD_WHITE:事件加白
     EVENT_PENDING: 事件待处理
        :type Status: str
        :param Remark: 事件备注
        :type Remark: str
        """
        self.EventIdSet = None
        self.Status = None
        self.Remark = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirusFileStatusResponse(AbstractModel):
    """ModifyVirusFileStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVirusMonitorSettingRequest(AbstractModel):
    """ModifyVirusMonitorSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnableScan: 是否开启定期扫描
        :type EnableScan: bool
        :param ScanPathAll: 扫描全部路径
        :type ScanPathAll: bool
        :param ScanPathType: 当ScanPathAll为true 生效 0扫描以下路径 1、扫描除以下路径
        :type ScanPathType: int
        :param ScanPath: 自选排除或扫描的地址
        :type ScanPath: list of str
        """
        self.EnableScan = None
        self.ScanPathAll = None
        self.ScanPathType = None
        self.ScanPath = None


    def _deserialize(self, params):
        self.EnableScan = params.get("EnableScan")
        self.ScanPathAll = params.get("ScanPathAll")
        self.ScanPathType = params.get("ScanPathType")
        self.ScanPath = params.get("ScanPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirusMonitorSettingResponse(AbstractModel):
    """ModifyVirusMonitorSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVirusScanSettingRequest(AbstractModel):
    """ModifyVirusScanSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnableScan: 是否开启定期扫描
        :type EnableScan: bool
        :param Cycle: 检测周期每隔多少天(1|3|7)
        :type Cycle: int
        :param BeginScanAt: 扫描开始时间
        :type BeginScanAt: str
        :param ScanPathAll: 扫描全部路径(true:全选,false:自选)
        :type ScanPathAll: bool
        :param ScanPathType: 当ScanPathAll为true 生效 0扫描以下路径 1、扫描除以下路径
        :type ScanPathType: int
        :param Timeout: 超时时长(5~24h)
        :type Timeout: int
        :param ScanRangeType: 扫描范围0容器1主机节点
        :type ScanRangeType: int
        :param ScanRangeAll: true 全选，false 自选
        :type ScanRangeAll: bool
        :param ScanIds: 自选扫描范围的容器id或者主机id 根据ScanRangeType决定
        :type ScanIds: list of str
        :param ScanPath: 扫描路径
        :type ScanPath: list of str
        """
        self.EnableScan = None
        self.Cycle = None
        self.BeginScanAt = None
        self.ScanPathAll = None
        self.ScanPathType = None
        self.Timeout = None
        self.ScanRangeType = None
        self.ScanRangeAll = None
        self.ScanIds = None
        self.ScanPath = None


    def _deserialize(self, params):
        self.EnableScan = params.get("EnableScan")
        self.Cycle = params.get("Cycle")
        self.BeginScanAt = params.get("BeginScanAt")
        self.ScanPathAll = params.get("ScanPathAll")
        self.ScanPathType = params.get("ScanPathType")
        self.Timeout = params.get("Timeout")
        self.ScanRangeType = params.get("ScanRangeType")
        self.ScanRangeAll = params.get("ScanRangeAll")
        self.ScanIds = params.get("ScanIds")
        self.ScanPath = params.get("ScanPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirusScanSettingResponse(AbstractModel):
    """ModifyVirusScanSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVirusScanTimeoutSettingRequest(AbstractModel):
    """ModifyVirusScanTimeoutSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param Timeout: 超时时长单位小时(5~24h)
        :type Timeout: int
        :param ScanType: 设置类型0一键检测，1定时检测
        :type ScanType: int
        """
        self.Timeout = None
        self.ScanType = None


    def _deserialize(self, params):
        self.Timeout = params.get("Timeout")
        self.ScanType = params.get("ScanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirusScanTimeoutSettingResponse(AbstractModel):
    """ModifyVirusScanTimeoutSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PortInfo(AbstractModel):
    """容器安全端口信息列表

    """

    def __init__(self):
        r"""
        :param Type: 类型
        :type Type: str
        :param PublicIP: 对外ip
        :type PublicIP: str
        :param PublicPort: 主机端口
        :type PublicPort: int
        :param ContainerPort: 容器端口
        :type ContainerPort: int
        :param ContainerPID: 容器Pid
        :type ContainerPID: int
        :param ContainerName: 容器名
        :type ContainerName: str
        :param HostID: 主机id
        :type HostID: str
        :param HostIP: 主机ip
        :type HostIP: str
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param ListenContainer: 容器内监听地址
        :type ListenContainer: str
        :param ListenHost: 容器外监听地址
        :type ListenHost: str
        :param RunAs: 运行账号
        :type RunAs: str
        :param HostName: 主机名称
        :type HostName: str
        :param PublicIp: 外网ip
        :type PublicIp: str
        """
        self.Type = None
        self.PublicIP = None
        self.PublicPort = None
        self.ContainerPort = None
        self.ContainerPID = None
        self.ContainerName = None
        self.HostID = None
        self.HostIP = None
        self.ProcessName = None
        self.ListenContainer = None
        self.ListenHost = None
        self.RunAs = None
        self.HostName = None
        self.PublicIp = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PublicIP = params.get("PublicIP")
        self.PublicPort = params.get("PublicPort")
        self.ContainerPort = params.get("ContainerPort")
        self.ContainerPID = params.get("ContainerPID")
        self.ContainerName = params.get("ContainerName")
        self.HostID = params.get("HostID")
        self.HostIP = params.get("HostIP")
        self.ProcessName = params.get("ProcessName")
        self.ListenContainer = params.get("ListenContainer")
        self.ListenHost = params.get("ListenHost")
        self.RunAs = params.get("RunAs")
        self.HostName = params.get("HostName")
        self.PublicIp = params.get("PublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessDetailBaseInfo(AbstractModel):
    """运行是安全详情，进程基础信息

    """

    def __init__(self):
        r"""
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param ProcessId: 进程pid
        :type ProcessId: int
        :param ProcessStartUser: 进程启动用户
        :type ProcessStartUser: str
        :param ProcessUserGroup: 进程用户组
        :type ProcessUserGroup: str
        :param ProcessPath: 进程路径
        :type ProcessPath: str
        :param ProcessParam: 进程命令行参数
        :type ProcessParam: str
        """
        self.ProcessName = None
        self.ProcessId = None
        self.ProcessStartUser = None
        self.ProcessUserGroup = None
        self.ProcessPath = None
        self.ProcessParam = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.ProcessId = params.get("ProcessId")
        self.ProcessStartUser = params.get("ProcessStartUser")
        self.ProcessUserGroup = params.get("ProcessUserGroup")
        self.ProcessPath = params.get("ProcessPath")
        self.ProcessParam = params.get("ProcessParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessDetailInfo(AbstractModel):
    """运行是安全详情，进程信息

    """

    def __init__(self):
        r"""
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param ProcessAuthority: 进程权限
        :type ProcessAuthority: str
        :param ProcessId: 进程pid
        :type ProcessId: int
        :param ProcessStartUser: 进程启动用户
        :type ProcessStartUser: str
        :param ProcessUserGroup: 进程用户组
        :type ProcessUserGroup: str
        :param ProcessPath: 进程路径
        :type ProcessPath: str
        :param ProcessTree: 进程树
        :type ProcessTree: str
        :param ProcessMd5: 进程md5
        :type ProcessMd5: str
        :param ProcessParam: 进程命令行参数
        :type ProcessParam: str
        """
        self.ProcessName = None
        self.ProcessAuthority = None
        self.ProcessId = None
        self.ProcessStartUser = None
        self.ProcessUserGroup = None
        self.ProcessPath = None
        self.ProcessTree = None
        self.ProcessMd5 = None
        self.ProcessParam = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.ProcessAuthority = params.get("ProcessAuthority")
        self.ProcessId = params.get("ProcessId")
        self.ProcessStartUser = params.get("ProcessStartUser")
        self.ProcessUserGroup = params.get("ProcessUserGroup")
        self.ProcessPath = params.get("ProcessPath")
        self.ProcessTree = params.get("ProcessTree")
        self.ProcessMd5 = params.get("ProcessMd5")
        self.ProcessParam = params.get("ProcessParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessInfo(AbstractModel):
    """容器安全进程列表

    """

    def __init__(self):
        r"""
        :param StartTime: 进程启动时间
        :type StartTime: str
        :param RunAs: 运行用户
        :type RunAs: str
        :param CmdLine: 命令行参数
        :type CmdLine: str
        :param Exe: Exe路径
        :type Exe: str
        :param PID: 主机PID
        :type PID: int
        :param ContainerPID: 容器内pid
        :type ContainerPID: int
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param HostID: 主机id
        :type HostID: str
        :param HostIP: 主机ip
        :type HostIP: str
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param HostName: 主机名称
        :type HostName: str
        :param PublicIp: 外网ip
        :type PublicIp: str
        """
        self.StartTime = None
        self.RunAs = None
        self.CmdLine = None
        self.Exe = None
        self.PID = None
        self.ContainerPID = None
        self.ContainerName = None
        self.HostID = None
        self.HostIP = None
        self.ProcessName = None
        self.HostName = None
        self.PublicIp = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.RunAs = params.get("RunAs")
        self.CmdLine = params.get("CmdLine")
        self.Exe = params.get("Exe")
        self.PID = params.get("PID")
        self.ContainerPID = params.get("ContainerPID")
        self.ContainerName = params.get("ContainerName")
        self.HostID = params.get("HostID")
        self.HostIP = params.get("HostIP")
        self.ProcessName = params.get("ProcessName")
        self.HostName = params.get("HostName")
        self.PublicIp = params.get("PublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAssetImageRegistryRegistryDetailRequest(AbstractModel):
    """RemoveAssetImageRegistryRegistryDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 仓库唯一id
        :type RegistryId: int
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAssetImageRegistryRegistryDetailResponse(AbstractModel):
    """RemoveAssetImageRegistryRegistryDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewImageAuthorizeStateRequest(AbstractModel):
    """RenewImageAuthorizeState请求参数结构体

    """

    def __init__(self):
        r"""
        :param AllImages: 是否全部未授权镜像
        :type AllImages: bool
        :param ImageIds: 镜像ids
        :type ImageIds: list of str
        """
        self.AllImages = None
        self.ImageIds = None


    def _deserialize(self, params):
        self.AllImages = params.get("AllImages")
        self.ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewImageAuthorizeStateResponse(AbstractModel):
    """RenewImageAuthorizeState返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReverseShellEventDescription(AbstractModel):
    """运行时容器反弹shell事件描述信息

    """

    def __init__(self):
        r"""
        :param Description: 描述信息
        :type Description: str
        :param Solution: 解决方案
        :type Solution: str
        :param Remark: 事件备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param DstAddress: 目标地址
        :type DstAddress: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.DstAddress = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        self.DstAddress = params.get("DstAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReverseShellEventInfo(AbstractModel):
    """容器安全运行时高危系统调用信息

    """

    def __init__(self):
        r"""
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param ProcessPath: 进程路径
        :type ProcessPath: str
        :param ImageId: 镜像id
        :type ImageId: str
        :param ContainerId: 容器id
        :type ContainerId: str
        :param ImageName: 镜像名
        :type ImageName: str
        :param ContainerName: 容器名
        :type ContainerName: str
        :param FoundTime: 生成时间
        :type FoundTime: str
        :param Solution: 事件解决方案
        :type Solution: str
        :param Description: 事件详细描述
        :type Description: str
        :param Status: 状态，EVENT_UNDEAL:事件未处理
    EVENT_DEALED:事件已经处理
    EVENT_INGNORE：事件已经忽略
    EVENT_ADD_WHITE：时间已经加白
        :type Status: str
        :param EventId: 事件id
        :type EventId: str
        :param Remark: 备注
        :type Remark: str
        :param PProcessName: 父进程名
        :type PProcessName: str
        :param EventCount: 事件数量
        :type EventCount: int
        :param LatestFoundTime: 最近生成时间
        :type LatestFoundTime: str
        :param DstAddress: 目标地址
        :type DstAddress: str
        """
        self.ProcessName = None
        self.ProcessPath = None
        self.ImageId = None
        self.ContainerId = None
        self.ImageName = None
        self.ContainerName = None
        self.FoundTime = None
        self.Solution = None
        self.Description = None
        self.Status = None
        self.EventId = None
        self.Remark = None
        self.PProcessName = None
        self.EventCount = None
        self.LatestFoundTime = None
        self.DstAddress = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.ProcessPath = params.get("ProcessPath")
        self.ImageId = params.get("ImageId")
        self.ContainerId = params.get("ContainerId")
        self.ImageName = params.get("ImageName")
        self.ContainerName = params.get("ContainerName")
        self.FoundTime = params.get("FoundTime")
        self.Solution = params.get("Solution")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.EventId = params.get("EventId")
        self.Remark = params.get("Remark")
        self.PProcessName = params.get("PProcessName")
        self.EventCount = params.get("EventCount")
        self.LatestFoundTime = params.get("LatestFoundTime")
        self.DstAddress = params.get("DstAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReverseShellWhiteListBaseInfo(AbstractModel):
    """反弹shell白名单信息

    """

    def __init__(self):
        r"""
        :param Id: 白名单id
        :type Id: str
        :param ImageCount: 镜像数量
        :type ImageCount: int
        :param ProcessName: 连接进程名字
        :type ProcessName: str
        :param DstIp: 目标地址ip
        :type DstIp: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param DstPort: 目标端口
        :type DstPort: str
        :param IsGlobal: 是否是全局白名单，true全局
        :type IsGlobal: bool
        :param ImageIds: 镜像id数组，为空代表全部
        :type ImageIds: list of str
        """
        self.Id = None
        self.ImageCount = None
        self.ProcessName = None
        self.DstIp = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DstPort = None
        self.IsGlobal = None
        self.ImageIds = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ImageCount = params.get("ImageCount")
        self.ProcessName = params.get("ProcessName")
        self.DstIp = params.get("DstIp")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.DstPort = params.get("DstPort")
        self.IsGlobal = params.get("IsGlobal")
        self.ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReverseShellWhiteListInfo(AbstractModel):
    """反弹shell白名单信息

    """

    def __init__(self):
        r"""
        :param DstIp: 目标IP
        :type DstIp: str
        :param DstPort: 目标端口
        :type DstPort: str
        :param ProcessName: 目标进程
        :type ProcessName: str
        :param ImageIds: 镜像id数组，为空代表全部
        :type ImageIds: list of str
        :param Id: 白名单id，如果新建则id为空
        :type Id: str
        """
        self.DstIp = None
        self.DstPort = None
        self.ProcessName = None
        self.ImageIds = None
        self.Id = None


    def _deserialize(self, params):
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.ProcessName = params.get("ProcessName")
        self.ImageIds = params.get("ImageIds")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskSyscallEventDescription(AbstractModel):
    """运行时容器高危系统调用事件描述信息

    """

    def __init__(self):
        r"""
        :param Description: 描述信息
        :type Description: str
        :param Solution: 解决方案
        :type Solution: str
        :param Remark: 事件备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param SyscallName: 系统调用名称
        :type SyscallName: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.SyscallName = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        self.SyscallName = params.get("SyscallName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskSyscallEventInfo(AbstractModel):
    """容器安全运行时高危系统调用信息

    """

    def __init__(self):
        r"""
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param ProcessPath: 进程路径
        :type ProcessPath: str
        :param ImageId: 镜像id
        :type ImageId: str
        :param ContainerId: 容器id
        :type ContainerId: str
        :param ImageName: 镜像名
        :type ImageName: str
        :param ContainerName: 容器名
        :type ContainerName: str
        :param FoundTime: 生成时间
        :type FoundTime: str
        :param Solution: 事件解决方案
        :type Solution: str
        :param Description: 事件详细描述
        :type Description: str
        :param SyscallName: 系统调用名称
        :type SyscallName: str
        :param Status: 状态，EVENT_UNDEAL:事件未处理
    EVENT_DEALED:事件已经处理
    EVENT_INGNORE：事件已经忽略
    EVENT_ADD_WHITE：时间已经加白
        :type Status: str
        :param EventId: 事件id
        :type EventId: str
        :param NodeName: 节点名称
        :type NodeName: str
        :param PodName: pod(实例)的名字
        :type PodName: str
        :param Remark: 备注
        :type Remark: str
        :param RuleExist: 系统监控名称是否存在
        :type RuleExist: bool
        :param EventCount: 事件数量
        :type EventCount: int
        :param LatestFoundTime: 最近生成时间
        :type LatestFoundTime: str
        """
        self.ProcessName = None
        self.ProcessPath = None
        self.ImageId = None
        self.ContainerId = None
        self.ImageName = None
        self.ContainerName = None
        self.FoundTime = None
        self.Solution = None
        self.Description = None
        self.SyscallName = None
        self.Status = None
        self.EventId = None
        self.NodeName = None
        self.PodName = None
        self.Remark = None
        self.RuleExist = None
        self.EventCount = None
        self.LatestFoundTime = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.ProcessPath = params.get("ProcessPath")
        self.ImageId = params.get("ImageId")
        self.ContainerId = params.get("ContainerId")
        self.ImageName = params.get("ImageName")
        self.ContainerName = params.get("ContainerName")
        self.FoundTime = params.get("FoundTime")
        self.Solution = params.get("Solution")
        self.Description = params.get("Description")
        self.SyscallName = params.get("SyscallName")
        self.Status = params.get("Status")
        self.EventId = params.get("EventId")
        self.NodeName = params.get("NodeName")
        self.PodName = params.get("PodName")
        self.Remark = params.get("Remark")
        self.RuleExist = params.get("RuleExist")
        self.EventCount = params.get("EventCount")
        self.LatestFoundTime = params.get("LatestFoundTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskSyscallWhiteListBaseInfo(AbstractModel):
    """高危系统调用白名单信息

    """

    def __init__(self):
        r"""
        :param Id: 白名单id
        :type Id: str
        :param ImageCount: 镜像数量
        :type ImageCount: int
        :param ProcessPath: 连接进程路径
        :type ProcessPath: str
        :param SyscallNames: 系统调用名称列表
        :type SyscallNames: list of str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param IsGlobal: 是否是全局白名单，true全局
        :type IsGlobal: bool
        :param ImageIds: 镜像id数组
        :type ImageIds: list of str
        """
        self.Id = None
        self.ImageCount = None
        self.ProcessPath = None
        self.SyscallNames = None
        self.CreateTime = None
        self.UpdateTime = None
        self.IsGlobal = None
        self.ImageIds = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ImageCount = params.get("ImageCount")
        self.ProcessPath = params.get("ProcessPath")
        self.SyscallNames = params.get("SyscallNames")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.IsGlobal = params.get("IsGlobal")
        self.ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskSyscallWhiteListInfo(AbstractModel):
    """高危系统调用白名单信息

    """

    def __init__(self):
        r"""
        :param ImageIds: 镜像id数组，为空代表全部
        :type ImageIds: list of str
        :param SyscallNames: 系统调用名称，通过DescribeRiskSyscallNames接口获取枚举列表
        :type SyscallNames: list of str
        :param ProcessPath: 目标进程
        :type ProcessPath: str
        :param Id: 白名单id，如果新建则id为空
        :type Id: str
        """
        self.ImageIds = None
        self.SyscallNames = None
        self.ProcessPath = None
        self.Id = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        self.SyscallNames = params.get("SyscallNames")
        self.ProcessPath = params.get("ProcessPath")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleBaseInfo(AbstractModel):
    """运行时安全，策略基本信息

    """

    def __init__(self):
        r"""
        :param IsDefault: true: 默认策略，false:自定义策略
        :type IsDefault: bool
        :param EffectImageCount: 策略生效镜像数量
        :type EffectImageCount: int
        :param RuleId: 策略Id
        :type RuleId: str
        :param UpdateTime: 策略更新时间, 存在为空的情况
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param RuleName: 策略名字
        :type RuleName: str
        :param EditUserName: 编辑用户名称
        :type EditUserName: str
        :param IsEnable: true: 策略启用，false：策略禁用
        :type IsEnable: bool
        """
        self.IsDefault = None
        self.EffectImageCount = None
        self.RuleId = None
        self.UpdateTime = None
        self.RuleName = None
        self.EditUserName = None
        self.IsEnable = None


    def _deserialize(self, params):
        self.IsDefault = params.get("IsDefault")
        self.EffectImageCount = params.get("EffectImageCount")
        self.RuleId = params.get("RuleId")
        self.UpdateTime = params.get("UpdateTime")
        self.RuleName = params.get("RuleName")
        self.EditUserName = params.get("EditUserName")
        self.IsEnable = params.get("IsEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunTimeEventBaseInfo(AbstractModel):
    """运行时安全事件基本信息

    """

    def __init__(self):
        r"""
        :param EventId: 事件唯一ID
        :type EventId: str
        :param FoundTime: 事件发现时间
        :type FoundTime: str
        :param ContainerId: 容器id
        :type ContainerId: str
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param ImageId: 镜像id
        :type ImageId: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param NodeName: 节点名称
        :type NodeName: str
        :param PodName: Pod名称
        :type PodName: str
        :param Status: 状态， “EVENT_UNDEAL”:事件未处理
    "EVENT_DEALED":事件已经处理
    "EVENT_INGNORE"：事件已经忽略
        :type Status: str
        :param EventName: 事件名称：
宿主机文件访问逃逸、
Syscall逃逸、
MountNamespace逃逸、
程序提权逃逸、
特权容器启动逃逸、
敏感路径挂载
恶意进程启动
文件篡改
        :type EventName: str
        :param EventType: 事件类型
   ESCAPE_HOST_ACESS_FILE:宿主机文件访问逃逸
   ESCAPE_MOUNT_NAMESPACE:MountNamespace逃逸
   ESCAPE_PRIVILEDGE:程序提权逃逸
   ESCAPE_PRIVILEDGE_CONTAINER_START:特权容器启动逃逸
   ESCAPE_MOUNT_SENSITIVE_PTAH:敏感路径挂载
   ESCAPE_SYSCALL:Syscall逃逸
        :type EventType: str
        :param EventCount: 事件数量
        :type EventCount: int
        :param LatestFoundTime: 最近生成时间
        :type LatestFoundTime: str
        :param HostIP: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIP: str
        :param ClientIP: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        """
        self.EventId = None
        self.FoundTime = None
        self.ContainerId = None
        self.ContainerName = None
        self.ImageId = None
        self.ImageName = None
        self.NodeName = None
        self.PodName = None
        self.Status = None
        self.EventName = None
        self.EventType = None
        self.EventCount = None
        self.LatestFoundTime = None
        self.HostIP = None
        self.ClientIP = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.FoundTime = params.get("FoundTime")
        self.ContainerId = params.get("ContainerId")
        self.ContainerName = params.get("ContainerName")
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.NodeName = params.get("NodeName")
        self.PodName = params.get("PodName")
        self.Status = params.get("Status")
        self.EventName = params.get("EventName")
        self.EventType = params.get("EventType")
        self.EventCount = params.get("EventCount")
        self.LatestFoundTime = params.get("LatestFoundTime")
        self.HostIP = params.get("HostIP")
        self.ClientIP = params.get("ClientIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunTimeFilters(AbstractModel):
    """容器安全
    描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 过滤键的名称
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 是否模糊查询
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunTimeRiskInfo(AbstractModel):
    """运行时风险信息

    """

    def __init__(self):
        r"""
        :param Cnt: 数量
        :type Cnt: int
        :param Level: 风险等级：
CRITICAL: 严重
HIGH: 高
MEDIUM：中
LOW: 低
        :type Level: str
        """
        self.Cnt = None
        self.Level = None


    def _deserialize(self, params):
        self.Cnt = params.get("Cnt")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunTimeTendencyInfo(AbstractModel):
    """运行时趋势信息

    """

    def __init__(self):
        r"""
        :param CurTime: 当天时间
        :type CurTime: str
        :param Cnt: 当前数量
        :type Cnt: int
        """
        self.CurTime = None
        self.Cnt = None


    def _deserialize(self, params):
        self.CurTime = params.get("CurTime")
        self.Cnt = params.get("Cnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanComplianceAssetsByPolicyItemRequest(AbstractModel):
    """ScanComplianceAssetsByPolicyItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemId: 指定的检测项的ID
        :type CustomerPolicyItemId: int
        :param CustomerAssetIdSet: 要重新扫描的客户资产项ID的列表。
        :type CustomerAssetIdSet: list of int non-negative
        """
        self.CustomerPolicyItemId = None
        self.CustomerAssetIdSet = None


    def _deserialize(self, params):
        self.CustomerPolicyItemId = params.get("CustomerPolicyItemId")
        self.CustomerAssetIdSet = params.get("CustomerAssetIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanComplianceAssetsByPolicyItemResponse(AbstractModel):
    """ScanComplianceAssetsByPolicyItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回重新检测任务的ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ScanComplianceAssetsRequest(AbstractModel):
    """ScanComplianceAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerAssetIdSet: 要重新扫描的客户资产项ID的列表。
        :type CustomerAssetIdSet: list of int non-negative
        """
        self.CustomerAssetIdSet = None


    def _deserialize(self, params):
        self.CustomerAssetIdSet = params.get("CustomerAssetIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanComplianceAssetsResponse(AbstractModel):
    """ScanComplianceAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回重新检测任务的ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ScanCompliancePolicyItemsRequest(AbstractModel):
    """ScanCompliancePolicyItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemIdSet: 要重新扫描的客户检测项的列表。
        :type CustomerPolicyItemIdSet: list of int non-negative
        """
        self.CustomerPolicyItemIdSet = None


    def _deserialize(self, params):
        self.CustomerPolicyItemIdSet = params.get("CustomerPolicyItemIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanCompliancePolicyItemsResponse(AbstractModel):
    """ScanCompliancePolicyItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回重新检测任务的ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ScanComplianceScanFailedAssetsRequest(AbstractModel):
    """ScanComplianceScanFailedAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerAssetIdSet: 要重新扫描的客户资产项ID的列表。
        :type CustomerAssetIdSet: list of int non-negative
        """
        self.CustomerAssetIdSet = None


    def _deserialize(self, params):
        self.CustomerAssetIdSet = params.get("CustomerAssetIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanComplianceScanFailedAssetsResponse(AbstractModel):
    """ScanComplianceScanFailedAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回重新检测任务的ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SecTendencyEventInfo(AbstractModel):
    """运行时安全事件趋势信息

    """

    def __init__(self):
        r"""
        :param EventSet: 趋势列表
        :type EventSet: list of RunTimeTendencyInfo
        :param EventType: 事件类型：
ET_ESCAPE : 容器逃逸
ET_REVERSE_SHELL: 反弹shell
ET_RISK_SYSCALL:高危系统调用
ET_ABNORMAL_PROCESS: 异常进程
ET_ACCESS_CONTROL 文件篡改
        :type EventType: str
        """
        self.EventSet = None
        self.EventType = None


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = RunTimeTendencyInfo()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.EventType = params.get("EventType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceInfo(AbstractModel):
    """容器安全服务信息列表

    """

    def __init__(self):
        r"""
        :param ServiceID: 服务id
        :type ServiceID: str
        :param HostID: 主机id
        :type HostID: str
        :param HostIP: 主机ip
        :type HostIP: str
        :param ContainerName: 容器名
        :type ContainerName: str
        :param Type: 服务名 例如nginx/redis
        :type Type: str
        :param Version: 版本
        :type Version: str
        :param RunAs: 账号
        :type RunAs: str
        :param Listen: 监听端口
        :type Listen: list of str
        :param Config: 配置
        :type Config: str
        :param ProcessCnt: 关联进程数
        :type ProcessCnt: int
        :param AccessLog: 访问日志
        :type AccessLog: str
        :param ErrorLog: 错误日志
        :type ErrorLog: str
        :param DataPath: 数据目录
        :type DataPath: str
        :param WebRoot: web目录
        :type WebRoot: str
        :param Pids: 关联的进程id
        :type Pids: list of int non-negative
        :param MainType: 服务类型 app,web,db
        :type MainType: str
        :param Exe: 执行文件
        :type Exe: str
        :param Parameter: 服务命令行参数
        :type Parameter: str
        :param ContainerId: 容器id
        :type ContainerId: str
        :param HostName: 主机名称
        :type HostName: str
        :param PublicIp: 外网ip
        :type PublicIp: str
        """
        self.ServiceID = None
        self.HostID = None
        self.HostIP = None
        self.ContainerName = None
        self.Type = None
        self.Version = None
        self.RunAs = None
        self.Listen = None
        self.Config = None
        self.ProcessCnt = None
        self.AccessLog = None
        self.ErrorLog = None
        self.DataPath = None
        self.WebRoot = None
        self.Pids = None
        self.MainType = None
        self.Exe = None
        self.Parameter = None
        self.ContainerId = None
        self.HostName = None
        self.PublicIp = None


    def _deserialize(self, params):
        self.ServiceID = params.get("ServiceID")
        self.HostID = params.get("HostID")
        self.HostIP = params.get("HostIP")
        self.ContainerName = params.get("ContainerName")
        self.Type = params.get("Type")
        self.Version = params.get("Version")
        self.RunAs = params.get("RunAs")
        self.Listen = params.get("Listen")
        self.Config = params.get("Config")
        self.ProcessCnt = params.get("ProcessCnt")
        self.AccessLog = params.get("AccessLog")
        self.ErrorLog = params.get("ErrorLog")
        self.DataPath = params.get("DataPath")
        self.WebRoot = params.get("WebRoot")
        self.Pids = params.get("Pids")
        self.MainType = params.get("MainType")
        self.Exe = params.get("Exe")
        self.Parameter = params.get("Parameter")
        self.ContainerId = params.get("ContainerId")
        self.HostName = params.get("HostName")
        self.PublicIp = params.get("PublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCheckModeRequest(AbstractModel):
    """SetCheckMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterIds: 要设置的集群ID列表
        :type ClusterIds: list of str
        :param ClusterCheckMode: 集群检查模式(正常模式"Cluster_Normal"、主动模式"Cluster_Actived"、不设置"Cluster_Unset")
        :type ClusterCheckMode: str
        :param ClusterAutoCheck: 0不设置 1打开 2关闭
        :type ClusterAutoCheck: int
        """
        self.ClusterIds = None
        self.ClusterCheckMode = None
        self.ClusterAutoCheck = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        self.ClusterCheckMode = params.get("ClusterCheckMode")
        self.ClusterAutoCheck = params.get("ClusterAutoCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCheckModeResponse(AbstractModel):
    """SetCheckMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param SetCheckResult: "Succ"表示设置成功，"Failed"表示设置失败
        :type SetCheckResult: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetCheckResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SetCheckResult = params.get("SetCheckResult")
        self.RequestId = params.get("RequestId")


class SoftQuotaDayInfo(AbstractModel):
    """后付费详情

    """

    def __init__(self):
        r"""
        :param PayTime: 扣费时间
        :type PayTime: str
        :param CoresCnt: 计费核数
        :type CoresCnt: int
        """
        self.PayTime = None
        self.CoresCnt = None


    def _deserialize(self, params):
        self.PayTime = params.get("PayTime")
        self.CoresCnt = params.get("CoresCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopVirusScanTaskRequest(AbstractModel):
    """StopVirusScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param ContainerIds: 需要停止的容器id 为空默认停止整个任务
        :type ContainerIds: list of str
        """
        self.TaskId = None
        self.ContainerIds = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ContainerIds = params.get("ContainerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopVirusScanTaskResponse(AbstractModel):
    """StopVirusScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SyncAssetImageRegistryAssetRequest(AbstractModel):
    """SyncAssetImageRegistryAsset请求参数结构体

    """


class SyncAssetImageRegistryAssetResponse(AbstractModel):
    """SyncAssetImageRegistryAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateAssetImageRegistryRegistryDetailRequest(AbstractModel):
    """UpdateAssetImageRegistryRegistryDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 仓库名
        :type Name: str
        :param Username: 用户名
        :type Username: str
        :param Password: 密码
        :type Password: str
        :param Url: 仓库url
        :type Url: str
        :param RegistryType: 仓库类型，列表：harbor
        :type RegistryType: str
        :param NetType: 网络类型，列表：public（公网）
        :type NetType: str
        :param RegistryVersion: 仓库版本
        :type RegistryVersion: str
        :param RegistryRegion: 区域，列表：default（默认）
        :type RegistryRegion: str
        :param SpeedLimit: 限速
        :type SpeedLimit: int
        """
        self.Name = None
        self.Username = None
        self.Password = None
        self.Url = None
        self.RegistryType = None
        self.NetType = None
        self.RegistryVersion = None
        self.RegistryRegion = None
        self.SpeedLimit = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.Url = params.get("Url")
        self.RegistryType = params.get("RegistryType")
        self.NetType = params.get("NetType")
        self.RegistryVersion = params.get("RegistryVersion")
        self.RegistryRegion = params.get("RegistryRegion")
        self.SpeedLimit = params.get("SpeedLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssetImageRegistryRegistryDetailResponse(AbstractModel):
    """UpdateAssetImageRegistryRegistryDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param HealthCheckErr: 连接错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckErr: str
        :param NameRepeatErr: 名称错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NameRepeatErr: str
        :param RegistryId: 仓库唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HealthCheckErr = None
        self.NameRepeatErr = None
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HealthCheckErr = params.get("HealthCheckErr")
        self.NameRepeatErr = params.get("NameRepeatErr")
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class UpdateImageRegistryTimingScanTaskRequest(AbstractModel):
    """UpdateImageRegistryTimingScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScanPeriod: 定时扫描周期
        :type ScanPeriod: int
        :param Enable: 定时扫描开关
        :type Enable: bool
        :param ScanTime: 定时扫描的时间
        :type ScanTime: str
        :param ScanType: 扫描木马类型数组
        :type ScanType: list of str
        :param Images: 扫描镜像
        :type Images: list of ImageInfo
        :param All: 是否扫描所有
        :type All: bool
        :param Id: 扫描镜像Id
        :type Id: list of int non-negative
        """
        self.ScanPeriod = None
        self.Enable = None
        self.ScanTime = None
        self.ScanType = None
        self.Images = None
        self.All = None
        self.Id = None


    def _deserialize(self, params):
        self.ScanPeriod = params.get("ScanPeriod")
        self.Enable = params.get("Enable")
        self.ScanTime = params.get("ScanTime")
        self.ScanType = params.get("ScanType")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.Images.append(obj)
        self.All = params.get("All")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateImageRegistryTimingScanTaskResponse(AbstractModel):
    """UpdateImageRegistryTimingScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirusInfo(AbstractModel):
    """运行时木马列表信息

    """

    def __init__(self):
        r"""
        :param FileName: 文件名称
        :type FileName: str
        :param FilePath: 文件路径
        :type FilePath: str
        :param VirusName: 病毒名称
        :type VirusName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 更新时间
        :type ModifyTime: str
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param ContainerId: 容器id
        :type ContainerId: str
        :param ContainerStatus: 容器状态，CS_RUNING:运行， CS_PAUSE:暂停，CS_STOP:停止，
												       CS_CREATE:已经创建， CS_DESTORY:销毁
        :type ContainerStatus: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageId: 镜像id
        :type ImageId: str
        :param Status: DEAL_NONE:文件待处理
DEAL_IGNORE:已经忽略
DEAL_ADD_WHITELIST:加白
DEAL_DEL:文件已经删除
DEAL_ISOLATE:已经隔离
DEAL_ISOLATING:隔离中
DEAL_ISOLATE_FAILED:隔离失败
DEAL_RECOVERING:恢复中
DEAL_RECOVER_FAILED: 恢复失败
        :type Status: str
        :param Id: 事件id
        :type Id: str
        :param HarmDescribe: 事件描述
        :type HarmDescribe: str
        :param SuggestScheme: 建议方案
        :type SuggestScheme: str
        :param SubStatus: 失败子状态:
FILE_NOT_FOUND:文件不存在
FILE_ABNORMAL:文件异常
FILE_ABNORMAL_DEAL_RECOVER:恢复文件时，文件异常
BACKUP_FILE_NOT_FOUND:备份文件不存在
CONTAINER_NOT_FOUND_DEAL_ISOLATE:隔离时，容器不存在
CONTAINER_NOT_FOUND_DEAL_RECOVER:恢复时，容器不存在
TIMEOUT: 超时
TOO_MANY: 任务过多
OFFLINE: 离线
INTERNAL: 服务内部错误
VALIDATION: 参数非法
        :type SubStatus: str
        """
        self.FileName = None
        self.FilePath = None
        self.VirusName = None
        self.CreateTime = None
        self.ModifyTime = None
        self.ContainerName = None
        self.ContainerId = None
        self.ContainerStatus = None
        self.ImageName = None
        self.ImageId = None
        self.Status = None
        self.Id = None
        self.HarmDescribe = None
        self.SuggestScheme = None
        self.SubStatus = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FilePath = params.get("FilePath")
        self.VirusName = params.get("VirusName")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.ContainerName = params.get("ContainerName")
        self.ContainerId = params.get("ContainerId")
        self.ContainerStatus = params.get("ContainerStatus")
        self.ImageName = params.get("ImageName")
        self.ImageId = params.get("ImageId")
        self.Status = params.get("Status")
        self.Id = params.get("Id")
        self.HarmDescribe = params.get("HarmDescribe")
        self.SuggestScheme = params.get("SuggestScheme")
        self.SubStatus = params.get("SubStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirusTaskInfo(AbstractModel):
    """运行时文件查杀任务容器列表信息

    """

    def __init__(self):
        r"""
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param ContainerId: 容器id
        :type ContainerId: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageId: 镜像Id
        :type ImageId: str
        :param HostName: 主机名称
        :type HostName: str
        :param HostIp: 主机ip
        :type HostIp: str
        :param Status: 扫描状态：
WAIT: 等待扫描
FAILED: 失败
SCANNING: 扫描中
FINISHED: 结束
CANCELING: 取消中
CANCELED: 已取消
CANCEL_FAILED： 取消失败
        :type Status: str
        :param StartTime: 检测开始时间
        :type StartTime: str
        :param EndTime: 检测结束时间
        :type EndTime: str
        :param RiskCnt: 风险个数
        :type RiskCnt: int
        :param Id: 事件id
        :type Id: str
        :param ErrorMsg: 错误原因:
SEND_SUCCESSED: 下发成功
SCAN_WAIT: agent排队扫描等待中
OFFLINE: 离线
SEND_FAILED:下发失败
TIMEOUT: 超时
LOW_AGENT_VERSION: 客户端版本过低
AGENT_NOT_FOUND: 镜像所属客户端版不存在
TOO_MANY: 任务过多
VALIDATION: 参数非法
INTERNAL: 服务内部错误
MISC: 其他错误
UNAUTH: 所在镜像未授权
SEND_CANCEL_SUCCESSED:下发成功
        :type ErrorMsg: str
        """
        self.ContainerName = None
        self.ContainerId = None
        self.ImageName = None
        self.ImageId = None
        self.HostName = None
        self.HostIp = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.RiskCnt = None
        self.Id = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.ContainerName = params.get("ContainerName")
        self.ContainerId = params.get("ContainerId")
        self.ImageName = params.get("ImageName")
        self.ImageId = params.get("ImageId")
        self.HostName = params.get("HostName")
        self.HostIp = params.get("HostIp")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RiskCnt = params.get("RiskCnt")
        self.Id = params.get("Id")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WarningRule(AbstractModel):
    """告警配置策略

    """

    def __init__(self):
        r"""
        :param Type: 告警事件类型：
镜像仓库安全-木马：IMG_REG_VIRUS
镜像仓库安全-漏洞：IMG_REG_VUL
镜像仓库安全-敏感信息：IMG_REG_RISK
镜像安全-木马：IMG_VIRUS
镜像安全-漏洞：IMG_VUL
镜像安全-敏感信息：IMG_RISK
镜像安全-镜像拦截：IMG_INTERCEPT
运行时安全-容器逃逸：RUNTIME_ESCAPE
运行时安全-异常进程：RUNTIME_FILE
运行时安全-异常文件访问：RUNTIME_PROCESS
运行时安全-高危系统调用：RUNTIME_SYSCALL
运行时安全-反弹Shell：RUNTIME_REVERSE_SHELL
运行时安全-木马：RUNTIME_VIRUS
        :type Type: str
        :param Switch: 开关状态：
打开：ON
关闭：OFF
        :type Switch: str
        :param BeginTime: 告警开始时间，格式: HH:mm
        :type BeginTime: str
        :param EndTime: 告警结束时间，格式: HH:mm
        :type EndTime: str
        :param ControlBits: 告警等级策略控制，二进制位每位代表一个含义，值以字符串类型传递
控制开关分为高、中、低，则二进制位分别为：第1位:低，第2位:中，第3位:高，0表示关闭、1表示打开。
如：高危和中危打开告警，低危关闭告警，则二进制值为：110
告警类型不区分等级控制，则传1。
        :type ControlBits: str
        """
        self.Type = None
        self.Switch = None
        self.BeginTime = None
        self.EndTime = None
        self.ControlBits = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Switch = params.get("Switch")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.ControlBits = params.get("ControlBits")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        