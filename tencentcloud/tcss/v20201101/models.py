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


class ABTestConfig(AbstractModel):
    """灰度项目配置

    """

    def __init__(self):
        r"""
        :param ProjectName: 灰度项目名称
        :type ProjectName: str
        :param Status: true：正在灰度，false：不在灰度
        :type Status: bool
        """
        self.ProjectName = None
        self.Status = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param RuleLevel: 威胁等级，HIGH:高，MIDDLE:中，LOW:低
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleLevel: str
        """
        self.RuleMode = None
        self.ProcessPath = None
        self.RuleId = None
        self.RuleLevel = None


    def _deserialize(self, params):
        self.RuleMode = params.get("RuleMode")
        self.ProcessPath = params.get("ProcessPath")
        self.RuleId = params.get("RuleId")
        self.RuleLevel = params.get("RuleLevel")
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
        :param RuleName: 命中规则名称，PROXY_TOOL：代理软件，TRANSFER_CONTROL：横向渗透，ATTACK_CMD：恶意命令，REVERSE_SHELL：反弹shell，FILELESS：无文件程序执行，RISK_CMD：高危命令，ABNORMAL_CHILD_PROC：敏感服务异常子进程启动，USER_DEFINED_RULE：用户自定义规则
        :type RuleName: str
        :param RuleId: 命中规则的id
        :type RuleId: str
        :param OperationTime: 事件最后一次处理的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationTime: str
        :param GroupName: 命中策略名称：SYSTEM_DEFINED_RULE （系统策略）或  用户自定义的策略名字
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.MatchRule = None
        self.RuleName = None
        self.RuleId = None
        self.OperationTime = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        if params.get("MatchRule") is not None:
            self.MatchRule = AbnormalProcessChildRuleInfo()
            self.MatchRule._deserialize(params.get("MatchRule"))
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        self.OperationTime = params.get("OperationTime")
        self.GroupName = params.get("GroupName")
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
        :param MatchRuleName: 命中规则名称，PROXY_TOOL：代理软件，TRANSFER_CONTROL：横向渗透，ATTACK_CMD：恶意命令，REVERSE_SHELL：反弹shell，FILELESS：无文件程序执行，RISK_CMD：高危命令，ABNORMAL_CHILD_PROC：敏感服务异常子进程启动，USER_DEFINED_RULE：用户自定义规则
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
        :param MatchGroupName: 命中策略名称：SYSTEM_DEFINED_RULE （系统策略）或  用户自定义的策略名字
        :type MatchGroupName: str
        :param MatchRuleLevel: 命中规则等级，HIGH：高危，MIDDLE：中危，LOW：低危。
        :type MatchRuleLevel: str
        :param ContainerNetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
"NODE_DESTROYED"      //节点已销毁
"CONTAINER_EXITED"    //容器已退出
"CONTAINER_DESTROYED" //容器已销毁
"SHARED_HOST"         // 容器与主机共享网络
"RESOURCE_LIMIT"      //隔离操作资源超限
"UNKNOW"              // 原因未知
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerIsolateOperationSrc: str
        :param ContainerStatus: 容器状态
正在运行: RUNNING
暂停: PAUSED
停止: STOPPED
已经创建: CREATED
已经销毁: DESTROYED
正在重启中: RESTARTING
迁移中: REMOVING
        :type ContainerStatus: str
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
        self.MatchGroupName = None
        self.MatchRuleLevel = None
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.ContainerStatus = None


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
        self.MatchGroupName = params.get("MatchGroupName")
        self.MatchRuleLevel = params.get("MatchRuleLevel")
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.ContainerStatus = params.get("ContainerStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalProcessEventTendencyInfo(AbstractModel):
    """待处理异常进程事件趋势

    """

    def __init__(self):
        r"""
        :param Date: 日期
        :type Date: str
        :param ProxyToolEventCount: 待处理代理软件事件数
        :type ProxyToolEventCount: int
        :param TransferControlEventCount: 待处理横向参透事件数
        :type TransferControlEventCount: int
        :param AttackCmdEventCount: 待处理恶意命令事件数
        :type AttackCmdEventCount: int
        :param ReverseShellEventCount: 待处理反弹shell事件数
        :type ReverseShellEventCount: int
        :param FilelessEventCount: 待处理无文件程序执行事件数
        :type FilelessEventCount: int
        :param RiskCmdEventCount: 待处理高危命令事件数
        :type RiskCmdEventCount: int
        :param AbnormalChildProcessEventCount: 待处理敏感服务异常子进程启动事件数
        :type AbnormalChildProcessEventCount: int
        :param UserDefinedRuleEventCount: 待处理自定义规则事件数
        :type UserDefinedRuleEventCount: int
        """
        self.Date = None
        self.ProxyToolEventCount = None
        self.TransferControlEventCount = None
        self.AttackCmdEventCount = None
        self.ReverseShellEventCount = None
        self.FilelessEventCount = None
        self.RiskCmdEventCount = None
        self.AbnormalChildProcessEventCount = None
        self.UserDefinedRuleEventCount = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.ProxyToolEventCount = params.get("ProxyToolEventCount")
        self.TransferControlEventCount = params.get("TransferControlEventCount")
        self.AttackCmdEventCount = params.get("AttackCmdEventCount")
        self.ReverseShellEventCount = params.get("ReverseShellEventCount")
        self.FilelessEventCount = params.get("FilelessEventCount")
        self.RiskCmdEventCount = params.get("RiskCmdEventCount")
        self.AbnormalChildProcessEventCount = params.get("AbnormalChildProcessEventCount")
        self.UserDefinedRuleEventCount = params.get("UserDefinedRuleEventCount")
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
        :param IsDefault: 是否是系统默认策略
        :type IsDefault: bool
        """
        self.IsEnable = None
        self.ImageIds = None
        self.ChildRules = None
        self.RuleName = None
        self.RuleId = None
        self.SystemChildRules = None
        self.IsDefault = None


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
        self.IsDefault = params.get("IsDefault")
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
        :param RuleLevel: 威胁等级，HIGH:高，MIDDLE:中，LOW:低
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleLevel: str
        """
        self.RuleId = None
        self.IsEnable = None
        self.RuleMode = None
        self.RuleType = None
        self.RuleLevel = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.IsEnable = params.get("IsEnable")
        self.RuleMode = params.get("RuleMode")
        self.RuleType = params.get("RuleType")
        self.RuleLevel = params.get("RuleLevel")
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
        :param OperationTime: 事件最后一次处理的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationTime: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.MatchRule = None
        self.RuleName = None
        self.RuleId = None
        self.OperationTime = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        if params.get("MatchRule") is not None:
            self.MatchRule = AccessControlChildRuleInfo()
            self.MatchRule._deserialize(params.get("MatchRule"))
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        self.OperationTime = params.get("OperationTime")
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
        :param ContainerNetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
"NODE_DESTROYED"      //节点已销毁
"CONTAINER_EXITED"    //容器已退出
"CONTAINER_DESTROYED" //容器已销毁
"SHARED_HOST"         // 容器与主机共享网络
"RESOURCE_LIMIT"      //隔离操作资源超限
"UNKNOW"              // 原因未知
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
        :type ContainerIsolateOperationSrc: str
        :param ContainerStatus: 容器状态
正在运行: RUNNING
暂停: PAUSED
停止: STOPPED
已经创建: CREATED
已经销毁: DESTROYED
正在重启中: RESTARTING
迁移中: REMOVING
        :type ContainerStatus: str
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
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.ContainerStatus = None


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
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.ContainerStatus = params.get("ContainerStatus")
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
        :param IsDefault: 是否是系统默认策略
        :type IsDefault: bool
        """
        self.IsEnable = None
        self.ImageIds = None
        self.ChildRules = None
        self.RuleName = None
        self.RuleId = None
        self.SystemChildRules = None
        self.IsDefault = None


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
        self.IsDefault = params.get("IsDefault")
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
        


class AddAndPublishNetworkFirewallPolicyDetailRequest(AbstractModel):
    """AddAndPublishNetworkFirewallPolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param FromPolicyRule: 入站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type FromPolicyRule: int
        :param ToPolicyRule: 出站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type ToPolicyRule: int
        :param PodSelector: pod选择器
        :type PodSelector: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 策略描述
        :type Description: str
        :param CustomPolicy: 自定义规则
        :type CustomPolicy: list of NetworkCustomPolicy
        """
        self.ClusterId = None
        self.PolicyName = None
        self.FromPolicyRule = None
        self.ToPolicyRule = None
        self.PodSelector = None
        self.Namespace = None
        self.Description = None
        self.CustomPolicy = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PolicyName = params.get("PolicyName")
        self.FromPolicyRule = params.get("FromPolicyRule")
        self.ToPolicyRule = params.get("ToPolicyRule")
        self.PodSelector = params.get("PodSelector")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        if params.get("CustomPolicy") is not None:
            self.CustomPolicy = []
            for item in params.get("CustomPolicy"):
                obj = NetworkCustomPolicy()
                obj._deserialize(item)
                self.CustomPolicy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAndPublishNetworkFirewallPolicyDetailResponse(AbstractModel):
    """AddAndPublishNetworkFirewallPolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class AddAndPublishNetworkFirewallPolicyYamlDetailRequest(AbstractModel):
    """AddAndPublishNetworkFirewallPolicyYamlDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Yaml: base64编码的networkpolicy yaml字符串
        :type Yaml: str
        :param Description: 策略描述
        :type Description: str
        """
        self.ClusterId = None
        self.PolicyName = None
        self.Yaml = None
        self.Description = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PolicyName = params.get("PolicyName")
        self.Yaml = params.get("Yaml")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAndPublishNetworkFirewallPolicyYamlDetailResponse(AbstractModel):
    """AddAndPublishNetworkFirewallPolicyYamlDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


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
        :param Insecure: 安全模式（证书校验）：0（默认） 非安全模式（跳过证书校验）：1
        :type Insecure: int
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
        self.Insecure = None


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
        self.Insecure = params.get("Insecure")
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


class AddComplianceAssetPolicySetToWhitelistRequest(AbstractModel):
    """AddComplianceAssetPolicySetToWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetPolicySetList: 资产ID+检查项IDs. 列表
        :type AssetPolicySetList: list of ComplianceAssetPolicySetItem
        """
        self.AssetPolicySetList = None


    def _deserialize(self, params):
        if params.get("AssetPolicySetList") is not None:
            self.AssetPolicySetList = []
            for item in params.get("AssetPolicySetList"):
                obj = ComplianceAssetPolicySetItem()
                obj._deserialize(item)
                self.AssetPolicySetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddComplianceAssetPolicySetToWhitelistResponse(AbstractModel):
    """AddComplianceAssetPolicySetToWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddCompliancePolicyAssetSetToWhitelistRequest(AbstractModel):
    """AddCompliancePolicyAssetSetToWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemId: 检查项ID
        :type CustomerPolicyItemId: int
        :param CustomerAssetItemIdSet: 需要忽略指定检查项内的资产ID列表
        :type CustomerAssetItemIdSet: list of int non-negative
        """
        self.CustomerPolicyItemId = None
        self.CustomerAssetItemIdSet = None


    def _deserialize(self, params):
        self.CustomerPolicyItemId = params.get("CustomerPolicyItemId")
        self.CustomerAssetItemIdSet = params.get("CustomerAssetItemIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCompliancePolicyAssetSetToWhitelistResponse(AbstractModel):
    """AddCompliancePolicyAssetSetToWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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


class AddEditImageAutoAuthorizedRuleRequest(AbstractModel):
    """AddEditImageAutoAuthorizedRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RangeType: 授权范围类别，MANUAL:自选主机节点，ALL:全部镜像
        :type RangeType: str
        :param MaxDailyCount: 每天最大的镜像授权数限制, 0表示无限制
        :type MaxDailyCount: int
        :param IsEnabled: 规则是否生效，0:不生效，1:已生效
        :type IsEnabled: int
        :param HostIdSet: 自选主机id，当授权范围为MANUAL:自选主机时且HostIdFilters为空时，必填
        :type HostIdSet: list of str
        :param RuleId: 规则id，在编辑时，必填
        :type RuleId: int
        :param HostIdFilters: 根据条件过滤，当授权范围为MANUAL:自选主机时且HostIdSet为空时，必填
        :type HostIdFilters: list of AssetFilters
        :param ExcludeHostIdSet: 根据条件过滤而且排除指定主机id
        :type ExcludeHostIdSet: list of str
        """
        self.RangeType = None
        self.MaxDailyCount = None
        self.IsEnabled = None
        self.HostIdSet = None
        self.RuleId = None
        self.HostIdFilters = None
        self.ExcludeHostIdSet = None


    def _deserialize(self, params):
        self.RangeType = params.get("RangeType")
        self.MaxDailyCount = params.get("MaxDailyCount")
        self.IsEnabled = params.get("IsEnabled")
        self.HostIdSet = params.get("HostIdSet")
        self.RuleId = params.get("RuleId")
        if params.get("HostIdFilters") is not None:
            self.HostIdFilters = []
            for item in params.get("HostIdFilters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.HostIdFilters.append(obj)
        self.ExcludeHostIdSet = params.get("ExcludeHostIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEditImageAutoAuthorizedRuleResponse(AbstractModel):
    """AddEditImageAutoAuthorizedRule返回参数结构体

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
        :param EventId: 仅在添加事件白名单时候使用
        :type EventId: str
        :param WhiteListInfo: 增加或编辑白名单信。新增白名单时WhiteListInfo.id为空，编辑白名单WhiteListInfo.id不能为空.
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


class AddEscapeWhiteListRequest(AbstractModel):
    """AddEscapeWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventType: 加白名单事件类型
   ESCAPE_CGROUPS：利用cgroup机制逃逸
   ESCAPE_TAMPER_SENSITIVE_FILE：篡改敏感文件逃逸
   ESCAPE_DOCKER_API：访问Docker API接口逃逸
   ESCAPE_VUL_OCCURRED：逃逸漏洞利用
   MOUNT_SENSITIVE_PTAH：敏感路径挂载
   PRIVILEGE_CONTAINER_START：特权容器
   PRIVILEGE：程序提权逃逸
        :type EventType: list of str
        :param ImageIDs: 加白名单镜像ID数组
        :type ImageIDs: list of str
        """
        self.EventType = None
        self.ImageIDs = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        self.ImageIDs = params.get("ImageIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEscapeWhiteListResponse(AbstractModel):
    """AddEscapeWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddIgnoreVulRequest(AbstractModel):
    """AddIgnoreVul请求参数结构体

    """

    def __init__(self):
        r"""
        :param List: 漏洞PocID信息列表
        :type List: list of ModifyIgnoreVul
        """
        self.List = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ModifyIgnoreVul()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddIgnoreVulResponse(AbstractModel):
    """AddIgnoreVul返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddNetworkFirewallPolicyDetailRequest(AbstractModel):
    """AddNetworkFirewallPolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param FromPolicyRule: 入站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type FromPolicyRule: int
        :param ToPolicyRule: 出站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type ToPolicyRule: int
        :param PodSelector: pod选择器
        :type PodSelector: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 策略描述
        :type Description: str
        :param CustomPolicy: 自定义规则
        :type CustomPolicy: list of NetworkCustomPolicy
        """
        self.ClusterId = None
        self.PolicyName = None
        self.FromPolicyRule = None
        self.ToPolicyRule = None
        self.PodSelector = None
        self.Namespace = None
        self.Description = None
        self.CustomPolicy = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PolicyName = params.get("PolicyName")
        self.FromPolicyRule = params.get("FromPolicyRule")
        self.ToPolicyRule = params.get("ToPolicyRule")
        self.PodSelector = params.get("PodSelector")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        if params.get("CustomPolicy") is not None:
            self.CustomPolicy = []
            for item in params.get("CustomPolicy"):
                obj = NetworkCustomPolicy()
                obj._deserialize(item)
                self.CustomPolicy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNetworkFirewallPolicyDetailResponse(AbstractModel):
    """AddNetworkFirewallPolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class AddNetworkFirewallPolicyYamlDetailRequest(AbstractModel):
    """AddNetworkFirewallPolicyYamlDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Yaml: base64编码的networkpolicy yaml字符串
        :type Yaml: str
        :param Description: 策略描述
        :type Description: str
        """
        self.ClusterId = None
        self.PolicyName = None
        self.Yaml = None
        self.Description = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PolicyName = params.get("PolicyName")
        self.Yaml = params.get("Yaml")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNetworkFirewallPolicyYamlDetailResponse(AbstractModel):
    """AddNetworkFirewallPolicyYamlDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
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
        


class AssetClusterListItem(AbstractModel):
    """集群列表Item

    """

    def __init__(self):
        r"""
        :param ClusterID: 集群ID
        :type ClusterID: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param Status: 集群状态
CSR_RUNNING: 运行中
CSR_EXCEPTION:异常
CSR_DEL:已经删除
        :type Status: str
        :param BindRuleName: 绑定规则名称
        :type BindRuleName: str
        :param ClusterType: 集群类型:
CT_TKE: TKE集群
CT_USER_CREATE: 用户自建集群
        :type ClusterType: str
        """
        self.ClusterID = None
        self.ClusterName = None
        self.Status = None
        self.BindRuleName = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        self.ClusterName = params.get("ClusterName")
        self.Status = params.get("Status")
        self.BindRuleName = params.get("BindRuleName")
        self.ClusterType = params.get("ClusterType")
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
        


class AutoAuthorizedImageInfo(AbstractModel):
    """镜像自动授权结果信息

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像id
        :type ImageId: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param AuthorizedTime: 授权时间
        :type AuthorizedTime: str
        :param Status: 授权结果，SUCCESS:成功，REACH_LIMIT:达到授权上限，LICENSE_INSUFFICIENT:授权数不足'
        :type Status: str
        :param IsAuthorized: 是否授权，1：是，0：否
        :type IsAuthorized: int
        """
        self.ImageId = None
        self.ImageName = None
        self.AuthorizedTime = None
        self.Status = None
        self.IsAuthorized = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.AuthorizedTime = params.get("AuthorizedTime")
        self.Status = params.get("Status")
        self.IsAuthorized = params.get("IsAuthorized")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoAuthorizedRuleHostInfo(AbstractModel):
    """自动授权镜像规则授权范围主机列表

    """

    def __init__(self):
        r"""
        :param HostID: 主机id
        :type HostID: str
        :param HostIP: 主机ip即内网ip
        :type HostIP: str
        :param HostName: 主机名称
        :type HostName: str
        :param ImageCnt: 镜像个数
        :type ImageCnt: int
        :param ContainerCnt: 容器个数
        :type ContainerCnt: int
        :param PublicIp: 外网ip
        :type PublicIp: str
        :param InstanceID: 主机实例ID
        :type InstanceID: str
        :param MachineType: 主机来源：["CVM", "ECM", "LH", "BM"]  中的之一为腾讯云服务器；["Other"]之一非腾讯云服务器；
        :type MachineType: str
        :param DockerVersion: docker 版本
        :type DockerVersion: str
        :param Status: agent运行状态
        :type Status: str
        """
        self.HostID = None
        self.HostIP = None
        self.HostName = None
        self.ImageCnt = None
        self.ContainerCnt = None
        self.PublicIp = None
        self.InstanceID = None
        self.MachineType = None
        self.DockerVersion = None
        self.Status = None


    def _deserialize(self, params):
        self.HostID = params.get("HostID")
        self.HostIP = params.get("HostIP")
        self.HostName = params.get("HostName")
        self.ImageCnt = params.get("ImageCnt")
        self.ContainerCnt = params.get("ContainerCnt")
        self.PublicIp = params.get("PublicIp")
        self.InstanceID = params.get("InstanceID")
        self.MachineType = params.get("MachineType")
        self.DockerVersion = params.get("DockerVersion")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CKafkaInstanceInfo(AbstractModel):
    """安全日志kafka可选信息

    """

    def __init__(self):
        r"""
        :param InstanceID: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param TopicList: 主题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of CKafkaTopicInfo
        :param RouteList: 路由列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteList: list of CkafkaRouteInfo
        :param KafkaVersion: kafka版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type KafkaVersion: str
        """
        self.InstanceID = None
        self.InstanceName = None
        self.TopicList = None
        self.RouteList = None
        self.KafkaVersion = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.InstanceName = params.get("InstanceName")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = CKafkaTopicInfo()
                obj._deserialize(item)
                self.TopicList.append(obj)
        if params.get("RouteList") is not None:
            self.RouteList = []
            for item in params.get("RouteList"):
                obj = CkafkaRouteInfo()
                obj._deserialize(item)
                self.RouteList.append(obj)
        self.KafkaVersion = params.get("KafkaVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CKafkaTopicInfo(AbstractModel):
    """Ckafka topic信息

    """

    def __init__(self):
        r"""
        :param TopicID: 主题ID
        :type TopicID: str
        :param TopicName: 主题名称
        :type TopicName: str
        """
        self.TopicID = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicID = params.get("TopicID")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckNetworkFirewallPolicyYamlRequest(AbstractModel):
    """CheckNetworkFirewallPolicyYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Yaml: base64编码的networkpolicy yaml字符串
        :type Yaml: str
        :param Description: 策略描述
        :type Description: str
        """
        self.ClusterId = None
        self.PolicyName = None
        self.Yaml = None
        self.Description = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PolicyName = params.get("PolicyName")
        self.Yaml = params.get("Yaml")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckNetworkFirewallPolicyYamlResponse(AbstractModel):
    """CheckNetworkFirewallPolicyYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


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


class CkafkaRouteInfo(AbstractModel):
    """ckafkal路由详情

    """

    def __init__(self):
        r"""
        :param RouteID: 路由ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteID: int
        :param Domain: 域名名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param DomainPort: 域名端口
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainPort: int
        :param Vip: 虚拟ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param VipType: 虚拟ip类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VipType: int
        :param AccessType: 接入类型
// 0：PLAINTEXT (明文方式，没有带用户信息老版本及社区版本都支持)
	// 1：SASL_PLAINTEXT（明文方式，不过在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
	// 2：SSL（SSL加密通信，没有带用户信息，老版本及社区版本都支持）
	// 3：SASL_SSL（SSL加密通信，在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: int
        """
        self.RouteID = None
        self.Domain = None
        self.DomainPort = None
        self.Vip = None
        self.VipType = None
        self.AccessType = None


    def _deserialize(self, params):
        self.RouteID = params.get("RouteID")
        self.Domain = params.get("Domain")
        self.DomainPort = params.get("DomainPort")
        self.Vip = params.get("Vip")
        self.VipType = params.get("VipType")
        self.AccessType = params.get("AccessType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogsetInfo(AbstractModel):
    """cls日志集信息

    """

    def __init__(self):
        r"""
        :param LogsetID: 日志集ID
        :type LogsetID: str
        :param LogsetName: 日志集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetName: str
        :param TopicList: cls主题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of ClsTopicInfo
        """
        self.LogsetID = None
        self.LogsetName = None
        self.TopicList = None


    def _deserialize(self, params):
        self.LogsetID = params.get("LogsetID")
        self.LogsetName = params.get("LogsetName")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = ClsTopicInfo()
                obj._deserialize(item)
                self.TopicList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsTopicInfo(AbstractModel):
    """cls主题信息

    """

    def __init__(self):
        r"""
        :param TopicID: 主题ID
        :type TopicID: str
        :param TopicName: 主题名称
        :type TopicName: str
        """
        self.TopicID = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicID = params.get("TopicID")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param IgnoredAssetNum: 忽略的资产数量
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoredAssetNum: int
        :param IsIgnored: 是否忽略该检测项
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnored: bool
        :param RiskAssessment: 受影响评估
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskAssessment: str
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
        self.IgnoredAssetNum = None
        self.IsIgnored = None
        self.RiskAssessment = None


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
        self.IgnoredAssetNum = params.get("IgnoredAssetNum")
        self.IsIgnored = params.get("IsIgnored")
        self.RiskAssessment = params.get("RiskAssessment")
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
        :param VerifyInfo: 检查项验证信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyInfo: str
        :param InstanceId: 主机实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
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
        self.VerifyInfo = None
        self.InstanceId = None


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
        self.VerifyInfo = params.get("VerifyInfo")
        self.InstanceId = params.get("InstanceId")
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
        :param InstanceId: 主机节点的实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
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
        self.InstanceId = None


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
        self.InstanceId = params.get("InstanceId")
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
        :param VerifyInfo: 验证信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyInfo: str
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
        self.VerifyInfo = None


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
        self.VerifyInfo = params.get("VerifyInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceAssetPolicySetItem(AbstractModel):
    """资产+检查项ids 集合单元

    """

    def __init__(self):
        r"""
        :param CustomerAssetItemId: 资产ID
        :type CustomerAssetItemId: int
        :param CustomerPolicyItemIdSet: 需要忽略指定资产内的检查项ID列表，为空表示所有
        :type CustomerPolicyItemIdSet: list of int non-negative
        """
        self.CustomerAssetItemId = None
        self.CustomerPolicyItemIdSet = None


    def _deserialize(self, params):
        self.CustomerAssetItemId = params.get("CustomerAssetItemId")
        self.CustomerPolicyItemIdSet = params.get("CustomerPolicyItemIdSet")
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
        :param OpenPolicyItemCount: 已开启的检查项总数
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenPolicyItemCount: int
        :param IgnoredPolicyItemCount: 已忽略的检查项总数
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoredPolicyItemCount: int
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
        self.OpenPolicyItemCount = None
        self.IgnoredPolicyItemCount = None


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
        self.OpenPolicyItemCount = params.get("OpenPolicyItemCount")
        self.IgnoredPolicyItemCount = params.get("IgnoredPolicyItemCount")
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
        :param ClusterVersion: K8S集群的版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterVersion: str
        """
        self.ClusterName = None
        self.ClusterVersion = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.ClusterVersion = params.get("ClusterVersion")
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
        :param Enable: 是否开启
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        """
        self.Frequency = None
        self.ExecutionTime = None
        self.Enable = None


    def _deserialize(self, params):
        self.Frequency = params.get("Frequency")
        self.ExecutionTime = params.get("ExecutionTime")
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompliancePolicyAssetSetItem(AbstractModel):
    """检查项+资产ids 的集合单元

    """

    def __init__(self):
        r"""
        :param CustomerPolicyItemId: 检查项ID
        :type CustomerPolicyItemId: int
        :param CustomerAssetItemIdSet: 需要忽略指定检查项内的资产ID列表，为空表示所有
        :type CustomerAssetItemIdSet: list of int non-negative
        """
        self.CustomerPolicyItemId = None
        self.CustomerAssetItemIdSet = None


    def _deserialize(self, params):
        self.CustomerPolicyItemId = params.get("CustomerPolicyItemId")
        self.CustomerAssetItemIdSet = params.get("CustomerAssetItemIdSet")
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
        :param ApplicableVersion: 检测项适用的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicableVersion: str
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
        self.ApplicableVersion = None


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
        self.ApplicableVersion = params.get("ApplicableVersion")
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
        


class ConfirmNetworkFirewallPolicyRequest(AbstractModel):
    """ConfirmNetworkFirewallPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Id: 策略Id数组
        :type Id: list of int non-negative
        """
        self.ClusterId = None
        self.Id = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmNetworkFirewallPolicyResponse(AbstractModel):
    """ConfirmNetworkFirewallPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建确认任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


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
        :param NetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
        :type NetStatus: str
        :param NetSubStatus: 网络子状态
        :type NetSubStatus: str
        :param IsolateSource: 隔离来源
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateSource: str
        :param IsolateTime: 隔离时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
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
        self.NetStatus = None
        self.NetSubStatus = None
        self.IsolateSource = None
        self.IsolateTime = None


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
        self.NetStatus = params.get("NetStatus")
        self.NetSubStatus = params.get("NetSubStatus")
        self.IsolateSource = params.get("IsolateSource")
        self.IsolateTime = params.get("IsolateTime")
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
        


class CreateAbnormalProcessRulesExportJobRequest(AbstractModel):
    """CreateAbnormalProcessRulesExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>RuleType - string  - 是否必填: 否 -规则类型</li>
<li>Status - string  - 是否必填: 否 -状态</li>
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
        


class CreateAbnormalProcessRulesExportJobResponse(AbstractModel):
    """CreateAbnormalProcessRulesExportJob返回参数结构体

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


class CreateAccessControlsRuleExportJobRequest(AbstractModel):
    """CreateAccessControlsRuleExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>RuleType - string  - 是否必填: 否 -规则类型</li>
<li>Status - string  - 是否必填: 否 -状态</li>
        :type Filters: list of RunTimeFilters
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
        :type By: list of str
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
        


class CreateAccessControlsRuleExportJobResponse(AbstractModel):
    """CreateAccessControlsRuleExportJob返回参数结构体

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
        :param All: 是否扫描全部镜像；全部镜像，镜像列表和根据过滤条件筛选三选一。
        :type All: bool
        :param Images: 需要扫描的镜像列表；全部镜像，镜像列表和根据过滤条件筛选三选一。
        :type Images: list of str
        :param ScanVul: 扫描漏洞；漏洞，木马和风险需选其一
        :type ScanVul: bool
        :param ScanVirus: 扫描木马；漏洞，木马和风险需选其一
        :type ScanVirus: bool
        :param ScanRisk: 扫描风险；漏洞，木马和风险需选其一
        :type ScanRisk: bool
        :param Filters: 根据过滤条件筛选出镜像；全部镜像，镜像列表和根据过滤条件筛选三选一。
        :type Filters: list of AssetFilters
        :param ExcludeImageIds: 根据过滤条件筛选出镜像，再排除个别镜像
        :type ExcludeImageIds: list of str
        """
        self.All = None
        self.Images = None
        self.ScanVul = None
        self.ScanVirus = None
        self.ScanRisk = None
        self.Filters = None
        self.ExcludeImageIds = None


    def _deserialize(self, params):
        self.All = params.get("All")
        self.Images = params.get("Images")
        self.ScanVul = params.get("ScanVul")
        self.ScanVirus = params.get("ScanVirus")
        self.ScanRisk = params.get("ScanRisk")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ExcludeImageIds = params.get("ExcludeImageIds")
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


class CreateAssetImageVirusExportJobRequest(AbstractModel):
    """CreateAssetImageVirusExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param ImageID: 镜像id
        :type ImageID: str
        :param Filters: 需要返回的数量，默认为10，最大值为10000
        :type Filters: list of AssetFilters
        :param Limit: 偏移量，默认为0。
        :type Limit: int
        :param Offset: 过滤参数,"Filters":[{"Name":"Status","Values":["2"]}]
        :type Offset: int
        :param By: 排序字段
        :type By: str
        :param Order: 升序降序,asc desc
        :type Order: str
        """
        self.ExportField = None
        self.ImageID = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.ExportField = params.get("ExportField")
        self.ImageID = params.get("ImageID")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetImageVirusExportJobResponse(AbstractModel):
    """CreateAssetImageVirusExportJob返回参数结构体

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


class CreateComponentExportJobRequest(AbstractModel):
    """CreateComponentExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10000，最大值为10000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ComponentName- String - 是否必填：否 - 镜像组件名称</li><li>ComponentVersion- String - 是否必填：否 - 镜像组件版本</li><li>ComponentType- String - 是否必填：否 - 镜像组件类型</li><li>VulLevel- String - 是否必填：否 - 漏洞威胁等级</li><li>HasVul- String - 是否必填：否 -是否有漏洞；true：是，false，否；不传或ALL ：全部</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式desc ，asc
        :type Order: str
        """
        self.ImageID = None
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
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
        


class CreateComponentExportJobResponse(AbstractModel):
    """CreateComponentExportJob返回参数结构体

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


class CreateDefenceVulExportJobRequest(AbstractModel):
    """CreateDefenceVulExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10000，最大值为10000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 威胁等级，CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低</li>
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>Name- string -是否必填: 否 - 漏洞名称</li>
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
        


class CreateDefenceVulExportJobResponse(AbstractModel):
    """CreateDefenceVulExportJob返回参数结构体

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


class CreateEmergencyVulExportJobRequest(AbstractModel):
    """CreateEmergencyVulExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为50000，最大值为50000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 威胁等级，CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低</li>
<li>Tags- string - 是否必填：否 - 漏洞标签，POC，EXP。</li>
<li>CanBeFixed- string - 是否必填：否 - 是否可修复true,false。</li>
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>ContainerID- string -是否必填: 否 - 容器ID</li>
<li>ContainerName- string -是否必填: 否 - 容器名称</li>
<li>ComponentName- string -是否必填: 否 - 组件名称</li>
<li>ComponentVersion- string -是否必填: 否 - 组件版本</li>
<li>Name- string -是否必填: 否 - 漏洞名称</li>
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
        


class CreateEmergencyVulExportJobResponse(AbstractModel):
    """CreateEmergencyVulExportJob返回参数结构体

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


class CreateEscapeEventsExportJobRequest(AbstractModel):
    """CreateEscapeEventsExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，最大值为10000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,Status：EVENT_UNDEAL:未处理，EVENT_DEALED:已处理，EVENT_INGNORE:忽略
        :type Filters: list of RunTimeFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段：latest_found_time
        :type By: str
        :param ExportField: 导出字段
        :type ExportField: list of str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None
        self.ExportField = None


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
        self.ExportField = params.get("ExportField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEscapeEventsExportJobResponse(AbstractModel):
    """CreateEscapeEventsExportJob返回参数结构体

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


class CreateEscapeWhiteListExportJobRequest(AbstractModel):
    """CreateEscapeWhiteListExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>EventType- String - 是否必填：否 - 加白事件类型，ESCAPE_CGROUPS：利用cgroup机制逃逸，ESCAPE_TAMPER_SENSITIVE_FILE：篡改敏感文件逃逸， ESCAPE_DOCKER_API：访问Docker API接口逃逸，ESCAPE_VUL_OCCURRED：逃逸漏洞利用，MOUNT_SENSITIVE_PTAH：敏感路径挂载，PRIVILEGE_CONTAINER_START：特权容器， PRIVILEGE：程序提权逃逸</li>
<li>ImageName- string - 是否必填：否 - 镜像名称。</li>
<li>ImageID- string - 是否必填：否 - 镜像ID。</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10000，最大值为10000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式：asc/desc
        :type Order: str
        :param By: 排序字段：主机数量：HostCount，容器数量：ContainerCount，更新时间：UpdateTime
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
        


class CreateEscapeWhiteListExportJobResponse(AbstractModel):
    """CreateEscapeWhiteListExportJob返回参数结构体

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


class CreateHostExportJobRequest(AbstractModel):
    """CreateHostExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - agent状态筛选，"ALL":"全部"(或不传该字段),"UNINSTALL"："未安装","OFFLINE"："离线", "ONLINE"："防护中"</li>
<li>HostName - String - 是否必填：否 - 主机名筛选</li>
<li>Group- String - 是否必填：否 - 主机群组搜索</li>
<li>HostIP- string - 是否必填：否 - 主机ip搜索</li>
<li>HostID- string - 是否必填：否 - 主机id搜索</li>
<li>DockerVersion- string - 是否必填：否 - docker版本搜索</li>
<li>MachineType- string - 是否必填：否 - 主机来源MachineType搜索，"ALL":"全部"(或不传该字段),主机来源：["CVM", "ECM", "LH", "BM"]  中的之一为腾讯云服务器；["Other"]之一非腾讯云服务器；</li>
<li>DockerStatus- string - 是否必填：否 - docker安装状态，"ALL":"全部"(或不传该字段),"INSTALL":"已安装","UNINSTALL":"未安装"</li>
<li>ProjectID- string - 是否必填：否 - 所属项目id搜索</li>
<li>Tag:xxx(tag:key)- string- 是否必填：否 - 标签键值搜索 示例Filters":[{"Name":"tag:tke-kind","Values":["service"]}]</li>
        :type Filters: list of AssetFilters
        :param Limit: 偏移量，默认为0。
        :type Limit: int
        :param Offset: 需要返回的数量，默认为10，最大值为10000
        :type Offset: int
        :param By: 排序字段
        :type By: str
        :param Order: 升序降序,asc desc
        :type Order: str
        :param ExportField: 导出字段
        :type ExportField: list of str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.By = None
        self.Order = None
        self.ExportField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.By = params.get("By")
        self.Order = params.get("Order")
        self.ExportField = params.get("ExportField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHostExportJobResponse(AbstractModel):
    """CreateHostExportJob返回参数结构体

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


class CreateImageExportJobRequest(AbstractModel):
    """CreateImageExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>ImageName- String - 是否必填：否 - 镜像名称筛选，</li>
<li>ScanStatus - String - 是否必填：否 - 镜像扫描状态notScan，scanning，scanned，scanErr</li>
<li>ImageID- String - 是否必填：否 - 镜像ID筛选，</li>
<li>SecurityRisk- String - 是否必填：否 - 安全风险，VulCnt 、VirusCnt、RiskCnt、IsTrustImage</li>
        :type Filters: list of RunTimeFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 asc,desc
        :type Order: str
        :param ExportField: 导出字段
        :type ExportField: list of str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.By = None
        self.Order = None
        self.ExportField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.By = params.get("By")
        self.Order = params.get("Order")
        self.ExportField = params.get("ExportField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageExportJobResponse(AbstractModel):
    """CreateImageExportJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 导出任务ID，前端拿着任务ID查询任务进度
        :type JobId: str
        :param DownloadUrl: excel文件下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class CreateK8sApiAbnormalEventExportJobRequest(AbstractModel):
    """CreateK8sApiAbnormalEventExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>TimeRange - string -是否必填: 否 - 时间范围筛选 ["2022-03-31 16:55:00", "2022-03-31 17:00:00"]</li>
<li>MatchRules - string  - 是否必填: 否 -命中规则筛选</li>
<li>RiskLevel - string  - 是否必填: 否 -威胁等级筛选</li>
<li>Status - string  - 是否必填: 否 -事件状态筛选</li>
<li>MatchRuleType - string  - 是否必填: 否 -命中规则类型筛选</li>
<li>ClusterRunningStatus - string  - 是否必填: 否 -集群运行状态</li>
<li>ClusterName - string  - 是否必填: 否 -集群名称</li>
<li>ClusterID - string  - 是否必填: 否 -集群ID</li>
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
        


class CreateK8sApiAbnormalEventExportJobResponse(AbstractModel):
    """CreateK8sApiAbnormalEventExportJob返回参数结构体

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


class CreateK8sApiAbnormalRuleExportJobRequest(AbstractModel):
    """CreateK8sApiAbnormalRuleExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>RuleType - string  - 是否必填: 否 -规则类型</li>
<li>Status - string  - 是否必填: 否 -状态</li>
        :type Filters: list of RunTimeFilters
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
        :type By: list of str
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
        


class CreateK8sApiAbnormalRuleExportJobResponse(AbstractModel):
    """CreateK8sApiAbnormalRuleExportJob返回参数结构体

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


class CreateK8sApiAbnormalRuleInfoRequest(AbstractModel):
    """CreateK8sApiAbnormalRuleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleInfo: 规则详情
        :type RuleInfo: :class:`tencentcloud.tcss.v20201101.models.K8sApiAbnormalRuleInfo`
        :param CopySrcRuleID: 拷贝规则ID(适用于复制规则场景)
        :type CopySrcRuleID: str
        :param EventID: 事件ID(适用于事件加白场景)
        :type EventID: int
        """
        self.RuleInfo = None
        self.CopySrcRuleID = None
        self.EventID = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = K8sApiAbnormalRuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.CopySrcRuleID = params.get("CopySrcRuleID")
        self.EventID = params.get("EventID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateK8sApiAbnormalRuleInfoResponse(AbstractModel):
    """CreateK8sApiAbnormalRuleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleID: 规则ID
        :type RuleID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.RequestId = params.get("RequestId")


class CreateNetworkFirewallClusterRefreshRequest(AbstractModel):
    """CreateNetworkFirewallClusterRefresh请求参数结构体

    """


class CreateNetworkFirewallClusterRefreshResponse(AbstractModel):
    """CreateNetworkFirewallClusterRefresh返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的集群检查任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建检查任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateNetworkFirewallPolicyDiscoverRequest(AbstractModel):
    """CreateNetworkFirewallPolicyDiscover请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
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
        


class CreateNetworkFirewallPolicyDiscoverResponse(AbstractModel):
    """CreateNetworkFirewallPolicyDiscover返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的集群检查任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建检查任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateNetworkFirewallPublishRequest(AbstractModel):
    """CreateNetworkFirewallPublish请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Id: 策略Id数组
        :type Id: list of int non-negative
        """
        self.ClusterId = None
        self.Id = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetworkFirewallPublishResponse(AbstractModel):
    """CreateNetworkFirewallPublish返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateNetworkFirewallUndoPublishRequest(AbstractModel):
    """CreateNetworkFirewallUndoPublish请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Id: 策略Id数组
        :type Id: list of int non-negative
        """
        self.ClusterId = None
        self.Id = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetworkFirewallUndoPublishResponse(AbstractModel):
    """CreateNetworkFirewallUndoPublish返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
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


class CreateProcessEventsExportJobRequest(AbstractModel):
    """CreateProcessEventsExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，最大值为10000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤参数,Status：EVENT_UNDEAL:未处理，EVENT_DEALED:已处理，EVENT_INGNORE:忽略
        :type Filters: list of AssetFilters
        :param Order: 升序降序,asc desc
        :type Order: str
        :param By: 排序字段：latest_found_time
        :type By: str
        :param ExportField: 导出字段
        :type ExportField: list of str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None
        self.ExportField = None


    def _deserialize(self, params):
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
        self.ExportField = params.get("ExportField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProcessEventsExportJobResponse(AbstractModel):
    """CreateProcessEventsExportJob返回参数结构体

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


class CreateRiskDnsEventExportJobRequest(AbstractModel):
    """CreateRiskDnsEventExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>EventStatus- String - 是否必填：否 - 事件状态，待处理：EVENT_UNDEAL，EVENT_DEALED：已处理，已忽略：EVENT_IGNORE， EVENT_ADD_WHITE：已加白</li>
<li>ContainerStatus- String - 是否必填：否 - 容器运行状态筛选，已创建：CREATED,正常运行：RUNNING, 暂定运行：PAUSED, 停止运行：	STOPPED，重启中：RESTARTING, 迁移中：REMOVING, 销毁：DESTROYED </li>
<li>ContainerNetStatus- String -是否必填: 否 -  容器网络状态筛选 未隔离：NORMAL，已隔离：ISOLATED，隔离失败：ISOLATE_FAILED，解除隔离失败：RESTORE_FAILED，解除隔离中：RESTORING，隔离中：ISOLATING</li>
<li>EventType - String -是否必填: 否 -  事件类型，恶意域名请求：DOMAIN，恶意IP请求：IP</li>
<li>TimeRange- String -是否必填: 否 -  时间范围，第一个值表示开始时间，第二个值表示结束时间 </li>
<li>RiskDns- string - 是否必填：否 - 恶意域名。</li>
<li>RiskIP- string - 是否必填：否 - 恶意IP。</li>
<li>ContainerName- string - 是否必填：否 - 容器名称。</li>
<li>ContainerID- string - 是否必填：否 - 容器ID。</li>
<li>ImageName- string - 是否必填：否 - 镜像名称。</li>
<li>ImageID- string - 是否必填：否 - 镜像ID。</li>
<li>HostName- string - 是否必填：否 - 主机名称。</li>
<li>HostIP- string - 是否必填：否 - 内网IP。</li>
<li>PublicIP- string - 是否必填：否 - 外网IP。</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，最大值为100000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式：asc/desc
        :type Order: str
        :param By: 排序字段：事件数量：EventCount
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
        


class CreateRiskDnsEventExportJobResponse(AbstractModel):
    """CreateRiskDnsEventExportJob返回参数结构体

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


class CreateSearchTemplateRequest(AbstractModel):
    """CreateSearchTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchTemplate: 搜索模板
        :type SearchTemplate: :class:`tencentcloud.tcss.v20201101.models.SearchTemplate`
        """
        self.SearchTemplate = None


    def _deserialize(self, params):
        if params.get("SearchTemplate") is not None:
            self.SearchTemplate = SearchTemplate()
            self.SearchTemplate._deserialize(params.get("SearchTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSearchTemplateResponse(AbstractModel):
    """CreateSearchTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSystemVulExportJobRequest(AbstractModel):
    """CreateSystemVulExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为50000，最大值为50000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>OnlyAffectedContainer- string - 是否必填：否 - 仅展示影响容器的漏洞true,false</li>
<li>OnlyAffectedNewestImage-string - 是否必填：否 - 仅展示影响最新版本镜像的漏洞true,false</li>
<li>Level- String - 是否必填：否 - 威胁等级，CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低</li>
<li>Tags- string - 是否必填：否 - 漏洞标签，POC，EXP。</li>
<li>CanBeFixed- string - 是否必填：否 - 是否可修复true,false。</li>
<li>CategoryType- string - 是否必填：否 - 漏洞子类型</li>
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>ContainerID- string -是否必填: 否 - 容器ID</li>
<li>ContainerName- string -是否必填: 否 - 容器名称</li>
<li>ComponentName- string -是否必填: 否 - 组件名称</li>
<li>ComponentVersion- string -是否必填: 否 - 组件版本</li>
<li>Name- string -是否必填: 否 - 漏洞名称</li>
<li>FocusOnType - string - 是否必填：否 -关注紧急度类型 。ALL :全部，SERIOUS_LEVEL： 严重和高危 ，IS_SUGGEST： 重点关注，POC_EXP 有Poc或Exp ，NETWORK_EXP: 远程Exp</li>
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
        


class CreateSystemVulExportJobResponse(AbstractModel):
    """CreateSystemVulExportJob返回参数结构体

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
        :param ScanPathMode: 扫描路径模式：
SCAN_PATH_ALL：全部路径
SCAN_PATH_DEFAULT：默认路径
SCAN_PATH_USER_DEFINE：用户自定义路径

        :type ScanPathMode: str
        """
        self.ScanPathAll = None
        self.ScanRangeType = None
        self.ScanRangeAll = None
        self.Timeout = None
        self.ScanPathType = None
        self.ScanIds = None
        self.ScanPath = None
        self.ScanPathMode = None


    def _deserialize(self, params):
        self.ScanPathAll = params.get("ScanPathAll")
        self.ScanRangeType = params.get("ScanRangeType")
        self.ScanRangeAll = params.get("ScanRangeAll")
        self.Timeout = params.get("Timeout")
        self.ScanPathType = params.get("ScanPathType")
        self.ScanIds = params.get("ScanIds")
        self.ScanPath = params.get("ScanPath")
        self.ScanPathMode = params.get("ScanPathMode")
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


class CreateVulContainerExportJobRequest(AbstractModel):
    """CreateVulContainerExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param Limit: 需要返回的数量，默认为50000，最大值为50000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>OnlyAffectedNewestImage- Bool- 是否必填：否 - 仅展示影响最新版本镜像的漏洞</li>
<li>ContainerID- string - 是否必填：否 - 容器ID</li>
<li>ContainerName- String -是否必填: 否 - 容器名称</li>
        :type Filters: list of RunTimeFilters
        """
        self.PocID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVulContainerExportJobResponse(AbstractModel):
    """CreateVulContainerExportJob返回参数结构体

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


class CreateVulDefenceEventExportJobRequest(AbstractModel):
    """CreateVulDefenceEventExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Status- String - 是否必填：否 - 插件状态，待处理：EVENT_UNDEAL，EVENT_DEALED：已处理，已忽略：EVENT_IGNORE， EVENT_DEFENDED：已防御</li>
<li>ContainerStatus- String - 是否必填：否 - 容器运行状态筛选，已创建：CREATED,正常运行：RUNNING, 暂定运行：PAUSED, 停止运行：	STOPPED，重启中：RESTARTING, 迁移中：REMOVING, 销毁：DESTROYED </li>
<li>ContainerNetStatus- String -是否必填: 否 -  容器网络状态筛选 未隔离：NORMAL，已隔离：ISOLATED，隔离失败：ISOLATE_FAILED，解除隔离失败：RESTORE_FAILED，解除隔离中：RESTORING，隔离中：ISOLATING</li>
<li>EventType - String -是否必填: 否 -  入侵状态，防御成功：EVENT_DEFENDED，尝试攻击：EVENT_ATTACK </li>
<li>TimeRange- String -是否必填: 否 -  时间范围，第一个值表示开始时间，第二个值表示结束时间 </li>
<li>VulName- string - 是否必填：否 - 漏洞名称。</li>
<li>CVEID- string - 是否必填：否 - CVE编号。</li>
<li>SourceIP- string - 是否必填：否 - 攻击源IP。</li>
<li>ContainerName- string - 是否必填：否 - 容器名称。</li>
<li>ContainerID- string - 是否必填：否 - 容器ID。</li>
<li>ImageName- string - 是否必填：否 - 镜像名称。</li>
<li>ImageID- string - 是否必填：否 - 镜像ID。</li>
<li>HostName- string - 是否必填：否 - 主机名称。</li>
<li>HostIP- string - 是否必填：否 - 内网IP。</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，最大值为100000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式：asc/desc
        :type Order: str
        :param By: 排序字段：事件数量：EventCount
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
        


class CreateVulDefenceEventExportJobResponse(AbstractModel):
    """CreateVulDefenceEventExportJob返回参数结构体

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


class CreateVulDefenceHostExportJobRequest(AbstractModel):
    """CreateVulDefenceHostExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Status- String - 是否必填：否 - 插件状态，正常：SUCCESS，异常：FAIL， NO_DEFENCE:未防御</li>
<li>KeyWords- string - 是否必填：否 - 主机名称/IP。</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，最大值为100000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式：asc/desc
        :type Order: str
        :param By: 排序字段：更新时间：ModifyTime/首次开启时间：CreateTime
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
        


class CreateVulDefenceHostExportJobResponse(AbstractModel):
    """CreateVulDefenceHostExportJob返回参数结构体

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


class CreateVulExportJobRequest(AbstractModel):
    """CreateVulExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ExportField: 导出字段
        :type ExportField: list of str
        :param Limit: 需要返回的数量，默认为10000，最大值为10000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ComponentName- String - 是否必填：否 - 镜像组件名称</li><li>ComponentVersion- String - 是否必填：否 - 镜像组件版本</li><li>ComponentType- String - 是否必填：否 - 镜像组件类型</li><li>VulLevel- String - 是否必填：否 - 漏洞威胁等级</li><li>HasVul- String - 是否必填：否 -是否有漏洞；true：是，false，否；不传或ALL ：全部</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式desc ，asc
        :type Order: str
        """
        self.ImageID = None
        self.ExportField = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
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
        


class CreateVulExportJobResponse(AbstractModel):
    """CreateVulExportJob返回参数结构体

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


class CreateVulImageExportJobRequest(AbstractModel):
    """CreateVulImageExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param Limit: 需要返回的数量，默认为50000，最大值为50000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>OnlyAffectedNewestImage- Bool- 是否必填：否 - 仅展示影响最新版本镜像的漏洞</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>ClientIP- string -是否必填: 否 - 内网IP</li>
<li>PublicIP- string -是否必填: 否 - 外网IP</li>
<li>ComponentName- string -是否必填: 否 - 组件名称</li>
<li>ComponentVersion- string -是否必填: 否 - 组件版本</li>
<li>HostName- string -是否必填: 否 - 主机名称</li>
        :type Filters: list of RunTimeFilters
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.PocID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
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
        


class CreateVulImageExportJobResponse(AbstractModel):
    """CreateVulImageExportJob返回参数结构体

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


class CreateVulScanTaskRequest(AbstractModel):
    """CreateVulScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param LocalImageScanType: 本地镜像扫描范围类型。ALL:全部本地镜像，NOT_SCAN：全部已授权未扫描本地镜像，IMAGEIDS:自选本地镜像ID
        :type LocalImageScanType: str
        :param LocalImageIDs: 根据已授权的本地镜像IDs扫描，优先权高于根据满足条件的已授权的本地镜像。
        :type LocalImageIDs: list of str
        :param RegistryImageScanType: 仓库镜像扫描范围类型。ALL:全部仓库镜像，NOT_SCAN：全部已授权未扫描仓库镜像，IMAGEIDS:自选仓库镜像ID
        :type RegistryImageScanType: str
        :param RegistryImageIDs: 根据已授权的仓库镜像IDs扫描，优先权高于根据满足条件的已授权的仓库镜像。
        :type RegistryImageIDs: list of int non-negative
        :param LocalTaskID: 本地镜像重新漏洞扫描时的任务ID
        :type LocalTaskID: int
        :param RegistryTaskID: 仓库镜像重新漏洞扫描时的任务ID
        :type RegistryTaskID: int
        """
        self.LocalImageScanType = None
        self.LocalImageIDs = None
        self.RegistryImageScanType = None
        self.RegistryImageIDs = None
        self.LocalTaskID = None
        self.RegistryTaskID = None


    def _deserialize(self, params):
        self.LocalImageScanType = params.get("LocalImageScanType")
        self.LocalImageIDs = params.get("LocalImageIDs")
        self.RegistryImageScanType = params.get("RegistryImageScanType")
        self.RegistryImageIDs = params.get("RegistryImageIDs")
        self.LocalTaskID = params.get("LocalTaskID")
        self.RegistryTaskID = params.get("RegistryTaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVulScanTaskResponse(AbstractModel):
    """CreateVulScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param LocalTaskID: 本地镜像重新漏洞扫描时的任务ID
        :type LocalTaskID: int
        :param RegistryTaskID: 仓库镜像重新漏洞扫描时的任务ID
        :type RegistryTaskID: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LocalTaskID = None
        self.RegistryTaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LocalTaskID = params.get("LocalTaskID")
        self.RegistryTaskID = params.get("RegistryTaskID")
        self.RequestId = params.get("RequestId")


class CreateWebVulExportJobRequest(AbstractModel):
    """CreateWebVulExportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为50000，最大值为50000
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>OnlyAffectedContainer- string - 是否必填：否 - 仅展示影响容器的漏洞true,false</li>
<li>OnlyAffectedNewestImage-string - 是否必填：否 - 仅展示影响最新版本镜像的漏洞true,false</li>
<li>Level- String - 是否必填：否 - 威胁等级，CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低</li>
<li>Tags- string - 是否必填：否 - 漏洞标签，POC，EXP。</li>
<li>CanBeFixed- string - 是否必填：否 - 是否可修复true,false。</li>
<li>CategoryType- string - 是否必填：否 - 漏洞子类型</li>
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>ContainerID- string -是否必填: 否 - 容器ID</li>
<li>ContainerName- string -是否必填: 否 - 容器名称</li>
<li>ComponentName- string -是否必填: 否 - 组件名称</li>
<li>ComponentVersion- string -是否必填: 否 - 组件版本</li>
<li>Name- string -是否必填: 否 - 漏洞名称</li>
<li>FocusOnType - string - 是否必填：否 -关注紧急度类型 。ALL :全部，SERIOUS_LEVEL： 严重和高危 ，IS_SUGGEST： 重点关注，POC_EXP 有Poc或Exp ，NETWORK_EXP: 远程Exp</li>
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
        


class CreateWebVulExportJobResponse(AbstractModel):
    """CreateWebVulExportJob返回参数结构体

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


class DeleteComplianceAssetPolicySetFromWhitelistRequest(AbstractModel):
    """DeleteComplianceAssetPolicySetFromWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetItemId: 资产ID
        :type AssetItemId: int
        :param CustomerPolicyItemIdSet: 需要忽略指定资产内的检查项ID列表
        :type CustomerPolicyItemIdSet: list of int non-negative
        """
        self.AssetItemId = None
        self.CustomerPolicyItemIdSet = None


    def _deserialize(self, params):
        self.AssetItemId = params.get("AssetItemId")
        self.CustomerPolicyItemIdSet = params.get("CustomerPolicyItemIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteComplianceAssetPolicySetFromWhitelistResponse(AbstractModel):
    """DeleteComplianceAssetPolicySetFromWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCompliancePolicyAssetSetFromWhitelistRequest(AbstractModel):
    """DeleteCompliancePolicyAssetSetFromWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyAssetSetList: （检查项ID+资产ID列表）的列表
        :type PolicyAssetSetList: list of CompliancePolicyAssetSetItem
        """
        self.PolicyAssetSetList = None


    def _deserialize(self, params):
        if params.get("PolicyAssetSetList") is not None:
            self.PolicyAssetSetList = []
            for item in params.get("PolicyAssetSetList"):
                obj = CompliancePolicyAssetSetItem()
                obj._deserialize(item)
                self.PolicyAssetSetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompliancePolicyAssetSetFromWhitelistResponse(AbstractModel):
    """DeleteCompliancePolicyAssetSetFromWhitelist返回参数结构体

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


class DeleteEscapeWhiteListRequest(AbstractModel):
    """DeleteEscapeWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param IDSet: 白名单记录ID数组
        :type IDSet: list of int
        """
        self.IDSet = None


    def _deserialize(self, params):
        self.IDSet = params.get("IDSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEscapeWhiteListResponse(AbstractModel):
    """DeleteEscapeWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIgnoreVulRequest(AbstractModel):
    """DeleteIgnoreVul请求参数结构体

    """

    def __init__(self):
        r"""
        :param List: 漏洞PocID 信息列表
        :type List: list of ModifyIgnoreVul
        """
        self.List = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ModifyIgnoreVul()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIgnoreVulResponse(AbstractModel):
    """DeleteIgnoreVul返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteK8sApiAbnormalRuleRequest(AbstractModel):
    """DeleteK8sApiAbnormalRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleIDSet: 规则ID集合
        :type RuleIDSet: list of str
        """
        self.RuleIDSet = None


    def _deserialize(self, params):
        self.RuleIDSet = params.get("RuleIDSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteK8sApiAbnormalRuleResponse(AbstractModel):
    """DeleteK8sApiAbnormalRule返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param Uuid: 客户端Uuid
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkFirewallPolicyDetailRequest(AbstractModel):
    """DeleteNetworkFirewallPolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Id: 策略Id数组
        :type Id: list of int non-negative
        """
        self.ClusterId = None
        self.Id = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetworkFirewallPolicyDetailResponse(AbstractModel):
    """DeleteNetworkFirewallPolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建删除任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteReverseShellEventsRequest(AbstractModel):
    """DeleteReverseShellEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIdSet: 事件ids
        :type EventIdSet: list of str
        """
        self.EventIdSet = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReverseShellEventsResponse(AbstractModel):
    """DeleteReverseShellEvents返回参数结构体

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


class DeleteRiskSyscallEventsRequest(AbstractModel):
    """DeleteRiskSyscallEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIdSet: 事件ids
        :type EventIdSet: list of str
        """
        self.EventIdSet = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRiskSyscallEventsResponse(AbstractModel):
    """DeleteRiskSyscallEvents返回参数结构体

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


class DeleteSearchTemplateRequest(AbstractModel):
    """DeleteSearchTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 模板ID
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
        


class DeleteSearchTemplateResponse(AbstractModel):
    """DeleteSearchTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeABTestConfigRequest(AbstractModel):
    """DescribeABTestConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectName: 灰度项目名称
        :type ProjectName: str
        """
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeABTestConfigResponse(AbstractModel):
    """DescribeABTestConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Config: 灰度项目配置
        :type Config: list of ABTestConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = ABTestConfig()
                obj._deserialize(item)
                self.Config.append(obj)
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
        :param AncestorProcessInfo: 祖先进程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessBaseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.ParentProcessInfo = None
        self.EventDetail = None
        self.AncestorProcessInfo = None
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
        if params.get("AncestorProcessInfo") is not None:
            self.AncestorProcessInfo = ProcessBaseInfo()
            self.AncestorProcessInfo._deserialize(params.get("AncestorProcessInfo"))
        self.RequestId = params.get("RequestId")


class DescribeAbnormalProcessEventTendencyRequest(AbstractModel):
    """DescribeAbnormalProcessEventTendency请求参数结构体

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
        


class DescribeAbnormalProcessEventTendencyResponse(AbstractModel):
    """DescribeAbnormalProcessEventTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 待处理异常进程事件趋势
        :type List: list of AbnormalProcessEventTendencyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AbnormalProcessEventTendencyInfo()
                obj._deserialize(item)
                self.List.append(obj)
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


class DescribeAbnormalProcessLevelSummaryRequest(AbstractModel):
    """DescribeAbnormalProcessLevelSummary请求参数结构体

    """


class DescribeAbnormalProcessLevelSummaryResponse(AbstractModel):
    """DescribeAbnormalProcessLevelSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param HighLevelEventCount: 异常进程高危待处理事件数
        :type HighLevelEventCount: int
        :param MediumLevelEventCount: 异常进程中危待处理事件数
        :type MediumLevelEventCount: int
        :param LowLevelEventCount: 异常进程低危待处理事件数
        :type LowLevelEventCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HighLevelEventCount = None
        self.MediumLevelEventCount = None
        self.LowLevelEventCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HighLevelEventCount = params.get("HighLevelEventCount")
        self.MediumLevelEventCount = params.get("MediumLevelEventCount")
        self.LowLevelEventCount = params.get("LowLevelEventCount")
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
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.RuleId = None
        self.ImageId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ImageId = params.get("ImageId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        :param ParentProcessInfo: 父进程信息
        :type ParentProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessBaseInfo`
        :param AncestorProcessInfo: 祖先进程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessBaseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.TamperedFileInfo = None
        self.EventDetail = None
        self.ParentProcessInfo = None
        self.AncestorProcessInfo = None
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
        if params.get("ParentProcessInfo") is not None:
            self.ParentProcessInfo = ProcessBaseInfo()
            self.ParentProcessInfo._deserialize(params.get("ParentProcessInfo"))
        if params.get("AncestorProcessInfo") is not None:
            self.AncestorProcessInfo = ProcessBaseInfo()
            self.AncestorProcessInfo._deserialize(params.get("AncestorProcessInfo"))
        self.RequestId = params.get("RequestId")


class DescribeAccessControlEventsExportRequest(AbstractModel):
    """DescribeAccessControlEventsExport请求参数结构体

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
        :param ExportField: 导出字段
        :type ExportField: list of str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None
        self.ExportField = None


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
        self.ExportField = params.get("ExportField")
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
        :param JobId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.JobId = params.get("JobId")
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
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.RuleId = None
        self.ImageId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ImageId = params.get("ImageId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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


class DescribeAgentDaemonSetCmdRequest(AbstractModel):
    """DescribeAgentDaemonSetCmd请求参数结构体

    """

    def __init__(self):
        r"""
        :param IsCloud: 是否是腾讯云
        :type IsCloud: bool
        :param NetType: 网络类型：basic-基础网络，private-VPC, public-公网，direct-专线
        :type NetType: str
        :param RegionCode: 地域标示, NetType=direct时必填
        :type RegionCode: str
        :param VpcId: VpcId, NetType=direct时必填
        :type VpcId: str
        :param ExpireDate: 命令有效期，非腾讯云时必填
        :type ExpireDate: str
        """
        self.IsCloud = None
        self.NetType = None
        self.RegionCode = None
        self.VpcId = None
        self.ExpireDate = None


    def _deserialize(self, params):
        self.IsCloud = params.get("IsCloud")
        self.NetType = params.get("NetType")
        self.RegionCode = params.get("RegionCode")
        self.VpcId = params.get("VpcId")
        self.ExpireDate = params.get("ExpireDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentDaemonSetCmdResponse(AbstractModel):
    """DescribeAgentDaemonSetCmd返回参数结构体

    """

    def __init__(self):
        r"""
        :param Command: 安装命令
        :type Command: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Command = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Command = params.get("Command")
        self.RequestId = params.get("RequestId")


class DescribeAgentInstallCommandRequest(AbstractModel):
    """DescribeAgentInstallCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param IsCloud: 是否是腾讯云
        :type IsCloud: bool
        :param NetType: 网络类型：basic-基础网络，private-VPC, public-公网，direct-专线
        :type NetType: str
        :param RegionCode: 地域标示, NetType=direct时必填
        :type RegionCode: str
        :param VpcId: VpcId, NetType=direct时必填
        :type VpcId: str
        :param ExpireDate: 命令有效期，非腾讯云时必填
        :type ExpireDate: str
        :param TagIds: 标签ID列表，IsCloud=false时才会生效
        :type TagIds: list of int non-negative
        """
        self.IsCloud = None
        self.NetType = None
        self.RegionCode = None
        self.VpcId = None
        self.ExpireDate = None
        self.TagIds = None


    def _deserialize(self, params):
        self.IsCloud = params.get("IsCloud")
        self.NetType = params.get("NetType")
        self.RegionCode = params.get("RegionCode")
        self.VpcId = params.get("VpcId")
        self.ExpireDate = params.get("ExpireDate")
        self.TagIds = params.get("TagIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentInstallCommandResponse(AbstractModel):
    """DescribeAgentInstallCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param LinuxCommand: linux系统安装命令
        :type LinuxCommand: str
        :param WindowsCommand: windows系统安装命令（windows2008及以上）
        :type WindowsCommand: str
        :param WindowsStepOne: windows系统安装命令第一步（windows2003）
        :type WindowsStepOne: str
        :param WindowsStepTwo: windows系统安装命令第二步（windows2003）
        :type WindowsStepTwo: str
        :param WindowsDownloadUrl: windows版agent下载链接
        :type WindowsDownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LinuxCommand = None
        self.WindowsCommand = None
        self.WindowsStepOne = None
        self.WindowsStepTwo = None
        self.WindowsDownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LinuxCommand = params.get("LinuxCommand")
        self.WindowsCommand = params.get("WindowsCommand")
        self.WindowsStepOne = params.get("WindowsStepOne")
        self.WindowsStepTwo = params.get("WindowsStepTwo")
        self.WindowsDownloadUrl = params.get("WindowsDownloadUrl")
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


class DescribeAssetClusterListRequest(AbstractModel):
    """DescribeAssetClusterList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>ClusterID - string  - 是否必填: 否 -集群ID</li>
<li>ClusterName - string  - 是否必填: 否 -集群名称</li>
<li>Status - string  - 是否必填: 否 -集群状态</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段。
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
        


class DescribeAssetClusterListResponse(AbstractModel):
    """DescribeAssetClusterList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 集群列表
        :type List: list of AssetClusterListItem
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
                obj = AssetClusterListItem()
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
        :param NetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
        :type NetStatus: str
        :param NetSubStatus: 网络子状态
        :type NetSubStatus: str
        :param IsolateSource: 隔离来源
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateSource: str
        :param IsolateTime: 隔离时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
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
        self.NetStatus = None
        self.NetSubStatus = None
        self.IsolateSource = None
        self.IsolateTime = None
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
        self.NetStatus = params.get("NetStatus")
        self.NetSubStatus = params.get("NetSubStatus")
        self.IsolateSource = params.get("IsolateSource")
        self.IsolateTime = params.get("IsolateTime")
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
<li>NetStatus - String -是否必填: 否 -  容器网络状态筛选 normal isolated isolating isolate_failed restoring restore_failed</li>
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
        :param Project: 所属项目
        :type Project: :class:`tencentcloud.tcss.v20201101.models.ProjectInfo`
        :param Tags: 标签
        :type Tags: list of TagInfo
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
        self.Project = None
        self.Tags = None
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
        if params.get("Project") is not None:
            self.Project = ProjectInfo()
            self.Project._deserialize(params.get("Project"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
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
<li>MachineType- string - 是否必填：否 - 主机来源MachineType搜索，"ALL":"全部"(或不传该字段),主机来源：["CVM", "ECM", "LH", "BM"]  中的之一为腾讯云服务器；["Other"]之一非腾讯云服务器；</li>
<li>DockerStatus- string - 是否必填：否 - docker安装状态，"ALL":"全部"(或不传该字段),"INSTALL":"已安装","UNINSTALL":"未安装"</li>
<li>ProjectID- string - 是否必填：否 - 所属项目id搜索</li>
<li>Tag:xxx(tag:key)- string- 是否必填：否 - 标签键值搜索 示例Filters":[{"Name":"tag:tke-kind","Values":["service"]}]</li>
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
        :param ImageId: 镜像ID
        :type ImageId: str
        """
        self.Id = None
        self.ImageId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ImageId = params.get("ImageId")
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
        :param Insecure: 安全模式（证书校验）：0（默认） 非安全模式（跳过证书校验）：1
注意：此字段可能返回 null，表示取不到有效值。
        :type Insecure: int
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
        self.Insecure = None
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
        self.Insecure = params.get("Insecure")
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
        :param JobId: 任务ID
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.JobId = params.get("JobId")
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
        :param HostUnInstallCnt: 主机未安装agent数量
        :type HostUnInstallCnt: int
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
        self.HostUnInstallCnt = None
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
        self.HostUnInstallCnt = params.get("HostUnInstallCnt")
        self.RequestId = params.get("RequestId")


class DescribeAssetSyncLastTimeRequest(AbstractModel):
    """DescribeAssetSyncLastTime请求参数结构体

    """


class DescribeAssetSyncLastTimeResponse(AbstractModel):
    """DescribeAssetSyncLastTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param AssetSyncLastTime: 资产最近同步时间
        :type AssetSyncLastTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AssetSyncLastTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AssetSyncLastTime = params.get("AssetSyncLastTime")
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


class DescribeAutoAuthorizedRuleHostRequest(AbstractModel):
    """DescribeAutoAuthorizedRuleHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则id
        :type RuleId: int
        :param Limit: 需要返回的数量，默认为全部；
        :type Limit: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Order: 排序字段
        :type Order: str
        :param By: 排序方式，asc，desc
        :type By: str
        """
        self.RuleId = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
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
        


class DescribeAutoAuthorizedRuleHostResponse(AbstractModel):
    """DescribeAutoAuthorizedRuleHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 镜像自动授权规则授权范围主机列表
        :type List: list of AutoAuthorizedRuleHostInfo
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
                obj = AutoAuthorizedRuleHostInfo()
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
        :param NetworkType: 网络类型.PublicNetwork为公网类型,VPCNetwork为VPC网络
        :type NetworkType: str
        :param ApiServerAddress: API Server地址
        :type ApiServerAddress: str
        :param NodeCount: 节点数
        :type NodeCount: int
        :param NamespaceCount: 命名空间数
        :type NamespaceCount: int
        :param WorkloadCount: 工作负载数
        :type WorkloadCount: int
        :param PodCount: Pod数量
        :type PodCount: int
        :param ServiceCount: Service数量
        :type ServiceCount: int
        :param IngressCount: Ingress数量
        :type IngressCount: int
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
        self.NetworkType = None
        self.ApiServerAddress = None
        self.NodeCount = None
        self.NamespaceCount = None
        self.WorkloadCount = None
        self.PodCount = None
        self.ServiceCount = None
        self.IngressCount = None
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
        self.NetworkType = params.get("NetworkType")
        self.ApiServerAddress = params.get("ApiServerAddress")
        self.NodeCount = params.get("NodeCount")
        self.NamespaceCount = params.get("NamespaceCount")
        self.WorkloadCount = params.get("WorkloadCount")
        self.PodCount = params.get("PodCount")
        self.ServiceCount = params.get("ServiceCount")
        self.IngressCount = params.get("IngressCount")
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
        :param CheckedClusterCount: 已经检查集群数
        :type CheckedClusterCount: int
        :param AutoCheckClusterCount: 自动检查集群数
        :type AutoCheckClusterCount: int
        :param ManualCheckClusterCount: 手动检查集群数
        :type ManualCheckClusterCount: int
        :param FailedClusterCount: 检查失败集群数
        :type FailedClusterCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RiskClusterCount = None
        self.UncheckClusterCount = None
        self.ManagedClusterCount = None
        self.IndependentClusterCount = None
        self.NoRiskClusterCount = None
        self.CheckedClusterCount = None
        self.AutoCheckClusterCount = None
        self.ManualCheckClusterCount = None
        self.FailedClusterCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.RiskClusterCount = params.get("RiskClusterCount")
        self.UncheckClusterCount = params.get("UncheckClusterCount")
        self.ManagedClusterCount = params.get("ManagedClusterCount")
        self.IndependentClusterCount = params.get("IndependentClusterCount")
        self.NoRiskClusterCount = params.get("NoRiskClusterCount")
        self.CheckedClusterCount = params.get("CheckedClusterCount")
        self.AutoCheckClusterCount = params.get("AutoCheckClusterCount")
        self.ManualCheckClusterCount = params.get("ManualCheckClusterCount")
        self.FailedClusterCount = params.get("FailedClusterCount")
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
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式 desc asc
        :type Order: str
        """
        self.Offset = None
        self.Limit = None
        self.AssetTypeSet = None
        self.Filters = None
        self.By = None
        self.Order = None


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
        self.By = params.get("By")
        self.Order = params.get("Order")
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
        :param HostUnInstallCnt: 主机未安装agent数量
        :type HostUnInstallCnt: int
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
        self.HostUnInstallCnt = None
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
        self.HostUnInstallCnt = params.get("HostUnInstallCnt")
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
        :param UnhandledMaliciousConnectionEventCnt: 未处理恶意外连事件
        :type UnhandledMaliciousConnectionEventCnt: int
        :param UnhandledK8sApiEventCnt: 未处理k8sApi事件
注意：此字段可能返回 null，表示取不到有效值。
        :type UnhandledK8sApiEventCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UnhandledEscapeCnt = None
        self.UnhandledReverseShellCnt = None
        self.UnhandledRiskSyscallCnt = None
        self.UnhandledAbnormalProcessCnt = None
        self.UnhandledFileCnt = None
        self.UnhandledVirusEventCnt = None
        self.UnhandledMaliciousConnectionEventCnt = None
        self.UnhandledK8sApiEventCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UnhandledEscapeCnt = params.get("UnhandledEscapeCnt")
        self.UnhandledReverseShellCnt = params.get("UnhandledReverseShellCnt")
        self.UnhandledRiskSyscallCnt = params.get("UnhandledRiskSyscallCnt")
        self.UnhandledAbnormalProcessCnt = params.get("UnhandledAbnormalProcessCnt")
        self.UnhandledFileCnt = params.get("UnhandledFileCnt")
        self.UnhandledVirusEventCnt = params.get("UnhandledVirusEventCnt")
        self.UnhandledMaliciousConnectionEventCnt = params.get("UnhandledMaliciousConnectionEventCnt")
        self.UnhandledK8sApiEventCnt = params.get("UnhandledK8sApiEventCnt")
        self.RequestId = params.get("RequestId")


class DescribeESAggregationsRequest(AbstractModel):
    """DescribeESAggregations请求参数结构体

    """

    def __init__(self):
        r"""
        :param Query: ES聚合条件JSON
        :type Query: str
        """
        self.Query = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeESAggregationsResponse(AbstractModel):
    """DescribeESAggregations返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: ES聚合结果JSON
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeESHitsRequest(AbstractModel):
    """DescribeESHits请求参数结构体

    """

    def __init__(self):
        r"""
        :param Query: ES查询条件JSON
        :type Query: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        """
        self.Query = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeESHitsResponse(AbstractModel):
    """DescribeESHits返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: ES查询结果JSON
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeEmergencyVulListRequest(AbstractModel):
    """DescribeEmergencyVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 威胁等级，CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低</li>
<li>Tags- string - 是否必填：否 - 漏洞标签，POC，EXP。</li>
<li>CanBeFixed- string - 是否必填：否 - 是否可修复true,false。</li>
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>ContainerID- string -是否必填: 否 - 容器ID</li>
<li>ContainerName- string -是否必填: 否 - 容器名称</li>
<li>ComponentName- string -是否必填: 否 - 组件名称</li>
<li>ComponentVersion- string -是否必填: 否 - 组件版本</li>
<li>Name- string -是否必填: 否 - 漏洞名称</li>
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
        


class DescribeEmergencyVulListResponse(AbstractModel):
    """DescribeEmergencyVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 漏洞总数
        :type TotalCount: int
        :param List: 漏洞列表
        :type List: list of EmergencyVulInfo
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
                obj = EmergencyVulInfo()
                obj._deserialize(item)
                self.List.append(obj)
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
        :param ParentProcessInfo: 父进程信息
        :type ParentProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessBaseInfo`
        :param AncestorProcessInfo: 祖先进程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessBaseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.EventDetail = None
        self.ParentProcessInfo = None
        self.AncestorProcessInfo = None
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
        if params.get("ParentProcessInfo") is not None:
            self.ParentProcessInfo = ProcessBaseInfo()
            self.ParentProcessInfo._deserialize(params.get("ParentProcessInfo"))
        if params.get("AncestorProcessInfo") is not None:
            self.AncestorProcessInfo = ProcessBaseInfo()
            self.AncestorProcessInfo._deserialize(params.get("AncestorProcessInfo"))
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
        :param Filters: 过滤参数,Status：EVENT_UNDEAL:未处理，EVENT_DEALED:已处理，EVENT_INGNORE:忽略
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


class DescribeEscapeEventTendencyRequest(AbstractModel):
    """DescribeEscapeEventTendency请求参数结构体

    """

    def __init__(self):
        r"""
        :param EndTime: 结束时间
        :type EndTime: str
        :param StartTime: 开始时间
        :type StartTime: str
        """
        self.EndTime = None
        self.StartTime = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEscapeEventTendencyResponse(AbstractModel):
    """DescribeEscapeEventTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 待处理逃逸事件趋势
        :type List: list of EscapeEventTendencyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = EscapeEventTendencyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEscapeEventTypeSummaryRequest(AbstractModel):
    """DescribeEscapeEventTypeSummary请求参数结构体

    """


class DescribeEscapeEventTypeSummaryResponse(AbstractModel):
    """DescribeEscapeEventTypeSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerEscapeEventCount: 容器逃逸事件数
        :type ContainerEscapeEventCount: int
        :param ProcessPrivilegeEventCount: 程序提权事件数
        :type ProcessPrivilegeEventCount: int
        :param RiskContainerEventCount: 风险容器事件数
        :type RiskContainerEventCount: int
        :param PendingEscapeEventCount: 逃逸事件待处理数
        :type PendingEscapeEventCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContainerEscapeEventCount = None
        self.ProcessPrivilegeEventCount = None
        self.RiskContainerEventCount = None
        self.PendingEscapeEventCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ContainerEscapeEventCount = params.get("ContainerEscapeEventCount")
        self.ProcessPrivilegeEventCount = params.get("ProcessPrivilegeEventCount")
        self.RiskContainerEventCount = params.get("RiskContainerEventCount")
        self.PendingEscapeEventCount = params.get("PendingEscapeEventCount")
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


class DescribeEscapeWhiteListRequest(AbstractModel):
    """DescribeEscapeWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>EventType- String - 是否必填：否 - 加白事件类型，ESCAPE_CGROUPS：利用cgroup机制逃逸，ESCAPE_TAMPER_SENSITIVE_FILE：篡改敏感文件逃逸， ESCAPE_DOCKER_API：访问Docker API接口逃逸，ESCAPE_VUL_OCCURRED：逃逸漏洞利用，MOUNT_SENSITIVE_PTAH：敏感路径挂载，PRIVILEGE_CONTAINER_START：特权容器， PRIVILEGE：程序提权逃逸</li>
<li>ImageName- string - 是否必填：否 - 镜像名称。</li>
<li>ImageID- string - 是否必填：否 - 镜像ID。</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式：asc/desc
        :type Order: str
        :param By: 排序字段：主机数量：HostCount，容器数量：ContainerCount，更新时间：UpdateTime
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
        


class DescribeEscapeWhiteListResponse(AbstractModel):
    """DescribeEscapeWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param List: 逃逸白名单列表
        :type List: list of EscapeWhiteListInfo
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
                obj = EscapeWhiteListInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExportJobDownloadURLRequest(AbstractModel):
    """DescribeExportJobDownloadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobID: 任务ID
        :type JobID: str
        """
        self.JobID = None


    def _deserialize(self, params):
        self.JobID = params.get("JobID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportJobDownloadURLResponse(AbstractModel):
    """DescribeExportJobDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadURL: 下载链接
        :type DownloadURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadURL = params.get("DownloadURL")
        self.RequestId = params.get("RequestId")


class DescribeExportJobManageListRequest(AbstractModel):
    """DescribeExportJobManageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>ExportStatus- string -是否必填: 否 - 导出状态 RUNNING: 导出中 SUCCESS:导出完成 FAILURE:失败
<li>ExportSource- string -是否必填: 否 - 导出来源 LocalImage: 本地镜像
</li>
        :type Filters: list of RunTimeFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
InsertTime: 创建时间
        :type By: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportJobManageListResponse(AbstractModel):
    """DescribeExportJobManageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 任务列表
        :type List: list of ExportJobInfo
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
                obj = ExportJobInfo()
                obj._deserialize(item)
                self.List.append(obj)
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
        :param NotScannedLocalImageCnt: 本地未开启扫描镜像数
        :type NotScannedLocalImageCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalAuthorizedCnt = None
        self.UsedAuthorizedCnt = None
        self.ScannedImageCnt = None
        self.NotScannedImageCnt = None
        self.NotScannedLocalImageCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalAuthorizedCnt = params.get("TotalAuthorizedCnt")
        self.UsedAuthorizedCnt = params.get("UsedAuthorizedCnt")
        self.ScannedImageCnt = params.get("ScannedImageCnt")
        self.NotScannedImageCnt = params.get("NotScannedImageCnt")
        self.NotScannedLocalImageCnt = params.get("NotScannedLocalImageCnt")
        self.RequestId = params.get("RequestId")


class DescribeImageAutoAuthorizedLogListRequest(AbstractModel):
    """DescribeImageAutoAuthorizedLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 自动授权任务Id
        :type TaskId: int
        :param Filters: Status授权结果，SUCCESS:成功，REACH_LIMIT:达到授权上限，LICENSE_INSUFFICIENT:授权数不足
        :type Filters: list of AssetFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param By: 排序字段：AuthorizedTime
        :type By: str
        :param Order: 排序方式，asc，desc
        :type Order: str
        """
        self.TaskId = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageAutoAuthorizedLogListResponse(AbstractModel):
    """DescribeImageAutoAuthorizedLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param List: 自动授权结果镜像列表
        :type List: list of AutoAuthorizedImageInfo
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
                obj = AutoAuthorizedImageInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageAutoAuthorizedRuleRequest(AbstractModel):
    """DescribeImageAutoAuthorizedRule请求参数结构体

    """


class DescribeImageAutoAuthorizedRuleResponse(AbstractModel):
    """DescribeImageAutoAuthorizedRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsEnabled: 规则是否生效，0:不生效，1:已生效
        :type IsEnabled: int
        :param RangeType: 授权范围类别，MANUAL:自选主机节点，ALL:全部镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeType: str
        :param HostCount: 授权范围是自选主机时的主机数量
注意：此字段可能返回 null，表示取不到有效值。
        :type HostCount: int
        :param MaxDailyCount: 每天最大的镜像授权数限制, 0表示无限制
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDailyCount: int
        :param RuleId: 规则id，用未设置时为0
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsEnabled = None
        self.RangeType = None
        self.HostCount = None
        self.MaxDailyCount = None
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsEnabled = params.get("IsEnabled")
        self.RangeType = params.get("RangeType")
        self.HostCount = params.get("HostCount")
        self.MaxDailyCount = params.get("MaxDailyCount")
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class DescribeImageAutoAuthorizedTaskListRequest(AbstractModel):
    """DescribeImageAutoAuthorizedTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Filters: 过滤字段
Status授权结果，全部授权成功：ALLSUCCSESS，部分授权失败：PARTIALFAIL,全部授权失败：ALLFAIL
Type授权方式，AUTO:自动授权，MANUAL:手动授权
Source 镜像来源，LOCAL:本地镜像，REGISTRY:仓库镜像
        :type Filters: list of AssetFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
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
        


class DescribeImageAutoAuthorizedTaskListResponse(AbstractModel):
    """DescribeImageAutoAuthorizedTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 自动授权任务列表
        :type List: list of ImageAutoAuthorizedTask
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
                obj = ImageAutoAuthorizedTask()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImageComponentListRequest(AbstractModel):
    """DescribeImageComponentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像ID
        :type ImageID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ComponentName- String - 是否必填：否 - 镜像组件名称</li><li>ComponentVersion- String - 是否必填：否 - 镜像组件版本</li><li>ComponentType- String - 是否必填：否 - 镜像组件类型</li><li>VulLevel- String - 是否必填：否 - 漏洞威胁等级</li><li>HasVul- String - 是否必填：否 -是否有漏洞；true：是，false，否；不传或ALL ：全部</li>
        :type Filters: list of AssetFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式desc ，asc
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
        


class DescribeImageComponentListResponse(AbstractModel):
    """DescribeImageComponentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param List: 镜像组件列表
        :type List: list of ImageComponent
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
                obj = ImageComponent()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageRegistryNamespaceListRequest(AbstractModel):
    """DescribeImageRegistryNamespaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 本次查询的起始偏移量，默认为0。
        :type Offset: int
        :param Limit: 本次查询的数据量，默认为10，最大值为100。
        :type Limit: int
        :param Filters: 查询的过滤条件。Name字段可取值"Namespace"。
        :type Filters: list of AssetFilters
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
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageRegistryNamespaceListResponse(AbstractModel):
    """DescribeImageRegistryNamespaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 可返回的项目空间的总量。
        :type TotalCount: int
        :param NamespaceList: 返回的项目空间列表
        :type NamespaceList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NamespaceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.NamespaceList = params.get("NamespaceList")
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


class DescribeIndexListRequest(AbstractModel):
    """DescribeIndexList请求参数结构体

    """


class DescribeIndexListResponse(AbstractModel):
    """DescribeIndexList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: ES 索引信息
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeInspectionReportRequest(AbstractModel):
    """DescribeInspectionReport请求参数结构体

    """


class DescribeInspectionReportResponse(AbstractModel):
    """DescribeInspectionReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReportName: 报告名称
        :type ReportName: str
        :param ReportUrl: 下载链接
        :type ReportUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReportName = None
        self.ReportUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportName = params.get("ReportName")
        self.ReportUrl = params.get("ReportUrl")
        self.RequestId = params.get("RequestId")


class DescribeK8sApiAbnormalEventInfoRequest(AbstractModel):
    """DescribeK8sApiAbnormalEventInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 事件ID
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeK8sApiAbnormalEventInfoResponse(AbstractModel):
    """DescribeK8sApiAbnormalEventInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 事件详情
        :type Info: :class:`tencentcloud.tcss.v20201101.models.K8sApiAbnormalEventInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = K8sApiAbnormalEventInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeK8sApiAbnormalEventListRequest(AbstractModel):
    """DescribeK8sApiAbnormalEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>TimeRange - string -是否必填: 否 - 时间范围筛选 ["2022-03-31 16:55:00", "2022-03-31 17:00:00"]</li>
<li>MatchRules - string  - 是否必填: 否 -命中规则筛选</li>
<li>RiskLevel - string  - 是否必填: 否 -威胁等级筛选</li>
<li>Status - string  - 是否必填: 否 -事件状态筛选</li>
<li>MatchRuleType - string  - 是否必填: 否 -命中规则类型筛选</li>
<li>ClusterRunningStatus - string  - 是否必填: 否 -集群运行状态</li>
<li>ClusterName - string  - 是否必填: 否 -集群名称</li>
<li>ClusterID - string  - 是否必填: 否 -集群ID</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
LatestFoundTime: 最近生成时间
AlarmCount: 告警数量
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
        


class DescribeK8sApiAbnormalEventListResponse(AbstractModel):
    """DescribeK8sApiAbnormalEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 事件列表
        :type List: list of K8sApiAbnormalEventListItem
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
                obj = K8sApiAbnormalEventListItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeK8sApiAbnormalRuleInfoRequest(AbstractModel):
    """DescribeK8sApiAbnormalRuleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleID: 规则ID
        :type RuleID: str
        """
        self.RuleID = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeK8sApiAbnormalRuleInfoResponse(AbstractModel):
    """DescribeK8sApiAbnormalRuleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 规则详情
        :type Info: :class:`tencentcloud.tcss.v20201101.models.K8sApiAbnormalRuleInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = K8sApiAbnormalRuleInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeK8sApiAbnormalRuleListRequest(AbstractModel):
    """DescribeK8sApiAbnormalRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>RuleType - string  - 是否必填: 否 -规则类型</li>
<li>Status - string  - 是否必填: 否 -状态</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段。
<li>UpdateTime - string  - 是否必填: 否 -最后更新时间</li>
<li>EffectClusterCount - string  - 是否必填: 否 -影响集群数</li>
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
        


class DescribeK8sApiAbnormalRuleListResponse(AbstractModel):
    """DescribeK8sApiAbnormalRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 规则列表
        :type List: list of K8sApiAbnormalRuleListItem
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
                obj = K8sApiAbnormalRuleListItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeK8sApiAbnormalRuleScopeListRequest(AbstractModel):
    """DescribeK8sApiAbnormalRuleScopeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleID: 规则ID
        :type RuleID: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Filters: 过滤条件。
<li>Action - string -是否必填: 否 - 执行动作</li>
<li>RiskLevel - string  - 是否必填: 否 -威胁等级筛选</li>
        :type Filters: list of RunTimeFilters
        """
        self.RuleID = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeK8sApiAbnormalRuleScopeListResponse(AbstractModel):
    """DescribeK8sApiAbnormalRuleScopeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 列表
        :type List: list of K8sApiAbnormalRuleScopeInfo
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
                obj = K8sApiAbnormalRuleScopeInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeK8sApiAbnormalSummaryRequest(AbstractModel):
    """DescribeK8sApiAbnormalSummary请求参数结构体

    """


class DescribeK8sApiAbnormalSummaryResponse(AbstractModel):
    """DescribeK8sApiAbnormalSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param UnhandleEventCount: 待处理事件个数
        :type UnhandleEventCount: int
        :param UnhandleHighLevelEventCount: 待处理高危事件个数
        :type UnhandleHighLevelEventCount: int
        :param UnhandleMediumLevelEventCount: 待处理中危事件个数
        :type UnhandleMediumLevelEventCount: int
        :param UnhandleLowLevelEventCount: 待处理低危事件个数
        :type UnhandleLowLevelEventCount: int
        :param UnhandleNoticeLevelEventCount: 待处理提示级别事件个数
        :type UnhandleNoticeLevelEventCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UnhandleEventCount = None
        self.UnhandleHighLevelEventCount = None
        self.UnhandleMediumLevelEventCount = None
        self.UnhandleLowLevelEventCount = None
        self.UnhandleNoticeLevelEventCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UnhandleEventCount = params.get("UnhandleEventCount")
        self.UnhandleHighLevelEventCount = params.get("UnhandleHighLevelEventCount")
        self.UnhandleMediumLevelEventCount = params.get("UnhandleMediumLevelEventCount")
        self.UnhandleLowLevelEventCount = params.get("UnhandleLowLevelEventCount")
        self.UnhandleNoticeLevelEventCount = params.get("UnhandleNoticeLevelEventCount")
        self.RequestId = params.get("RequestId")


class DescribeK8sApiAbnormalTendencyRequest(AbstractModel):
    """DescribeK8sApiAbnormalTendency请求参数结构体

    """

    def __init__(self):
        r"""
        :param TendencyPeriod: 趋势周期(默认为7天)
        :type TendencyPeriod: int
        """
        self.TendencyPeriod = None


    def _deserialize(self, params):
        self.TendencyPeriod = params.get("TendencyPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeK8sApiAbnormalTendencyResponse(AbstractModel):
    """DescribeK8sApiAbnormalTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 趋势列表
        :type List: list of K8sApiAbnormalTendencyItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = K8sApiAbnormalTendencyItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogStorageStatisticRequest(AbstractModel):
    """DescribeLogStorageStatistic请求参数结构体

    """


class DescribeLogStorageStatisticResponse(AbstractModel):
    """DescribeLogStorageStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalSize: 总容量（单位：B）
        :type TotalSize: int
        :param UsedSize: 已使用容量（单位：B）
        :type UsedSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalSize = None
        self.UsedSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalSize = params.get("TotalSize")
        self.UsedSize = params.get("UsedSize")
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallAuditRecordRequest(AbstractModel):
    """DescribeNetworkFirewallAuditRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每次查询的最大记录数量
        :type Limit: int
        :param Filters: Name - Action
Name 可取值：publish，unpublish，confirm，add，update，delete
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
        


class DescribeNetworkFirewallAuditRecordResponse(AbstractModel):
    """DescribeNetworkFirewallAuditRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群审计总数
        :type TotalCount: int
        :param AuditList: 集群的审计详细信息
        :type AuditList: list of NetworkAuditRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AuditList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AuditList") is not None:
            self.AuditList = []
            for item in params.get("AuditList"):
                obj = NetworkAuditRecord()
                obj._deserialize(item)
                self.AuditList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallClusterListRequest(AbstractModel):
    """DescribeNetworkFirewallClusterList请求参数结构体

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
        


class DescribeNetworkFirewallClusterListResponse(AbstractModel):
    """DescribeNetworkFirewallClusterList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群总数
        :type TotalCount: int
        :param ClusterInfoList: 集群的详细信息
        :type ClusterInfoList: list of NetworkClusterInfoItem
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
                obj = NetworkClusterInfoItem()
                obj._deserialize(item)
                self.ClusterInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallClusterRefreshStatusRequest(AbstractModel):
    """DescribeNetworkFirewallClusterRefreshStatus请求参数结构体

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
        


class DescribeNetworkFirewallClusterRefreshStatusResponse(AbstractModel):
    """DescribeNetworkFirewallClusterRefreshStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskStatus: 任务状态，可能为：Task_Running,Task_Succ,Task_Error,Task_NoExist
        :type TaskStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallNamespaceLabelListRequest(AbstractModel):
    """DescribeNetworkFirewallNamespaceLabelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
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
        


class DescribeNetworkFirewallNamespaceLabelListResponse(AbstractModel):
    """DescribeNetworkFirewallNamespaceLabelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群总数
        :type TotalCount: int
        :param ClusterNamespaceLabelList: 集群空间标签详细信息
        :type ClusterNamespaceLabelList: list of NetworkClusterNamespaceLabelInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterNamespaceLabelList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterNamespaceLabelList") is not None:
            self.ClusterNamespaceLabelList = []
            for item in params.get("ClusterNamespaceLabelList"):
                obj = NetworkClusterNamespaceLabelInfo()
                obj._deserialize(item)
                self.ClusterNamespaceLabelList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallNamespaceListRequest(AbstractModel):
    """DescribeNetworkFirewallNamespaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
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
        


class DescribeNetworkFirewallNamespaceListResponse(AbstractModel):
    """DescribeNetworkFirewallNamespaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群总数
        :type TotalCount: int
        :param ClusterNamespaceList: 集群的详细信息
        :type ClusterNamespaceList: list of NetworkClusterNamespaceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterNamespaceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterNamespaceList") is not None:
            self.ClusterNamespaceList = []
            for item in params.get("ClusterNamespaceList"):
                obj = NetworkClusterNamespaceInfo()
                obj._deserialize(item)
                self.ClusterNamespaceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallPodLabelsListRequest(AbstractModel):
    """DescribeNetworkFirewallPodLabelsList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
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
        


class DescribeNetworkFirewallPodLabelsListResponse(AbstractModel):
    """DescribeNetworkFirewallPodLabelsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群pod总数
        :type TotalCount: int
        :param PodList: 集群pod详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: list of NetworkClusterPodInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PodList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PodList") is not None:
            self.PodList = []
            for item in params.get("PodList"):
                obj = NetworkClusterPodInfo()
                obj._deserialize(item)
                self.PodList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallPolicyDetailRequest(AbstractModel):
    """DescribeNetworkFirewallPolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 策略Id
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
        


class DescribeNetworkFirewallPolicyDetailResponse(AbstractModel):
    """DescribeNetworkFirewallPolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param FromPolicyRule: 入站类型
        :type FromPolicyRule: int
        :param ToPolicyRule: 出站类型
        :type ToPolicyRule: int
        :param CustomPolicy: 自定义规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomPolicy: list of NetworkCustomPolicy
        :param PodSelector: pod选择器
        :type PodSelector: str
        :param Description: 策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param PolicyCreateTime: 策略创建时间
        :type PolicyCreateTime: str
        :param PolicySourceType: 策略源类型，分为System和Manual，分别代表手动和系统添加
        :type PolicySourceType: str
        :param NetworkPolicyPlugin: 网络策略对应的网络插件
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkPolicyPlugin: str
        :param PublishStatus: 网络策略状态
        :type PublishStatus: str
        :param PublishResult: 网络发布结果
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishResult: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.PolicyName = None
        self.Namespace = None
        self.FromPolicyRule = None
        self.ToPolicyRule = None
        self.CustomPolicy = None
        self.PodSelector = None
        self.Description = None
        self.PolicyCreateTime = None
        self.PolicySourceType = None
        self.NetworkPolicyPlugin = None
        self.PublishStatus = None
        self.PublishResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PolicyName = params.get("PolicyName")
        self.Namespace = params.get("Namespace")
        self.FromPolicyRule = params.get("FromPolicyRule")
        self.ToPolicyRule = params.get("ToPolicyRule")
        if params.get("CustomPolicy") is not None:
            self.CustomPolicy = []
            for item in params.get("CustomPolicy"):
                obj = NetworkCustomPolicy()
                obj._deserialize(item)
                self.CustomPolicy.append(obj)
        self.PodSelector = params.get("PodSelector")
        self.Description = params.get("Description")
        self.PolicyCreateTime = params.get("PolicyCreateTime")
        self.PolicySourceType = params.get("PolicySourceType")
        self.NetworkPolicyPlugin = params.get("NetworkPolicyPlugin")
        self.PublishStatus = params.get("PublishStatus")
        self.PublishResult = params.get("PublishResult")
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallPolicyDiscoverRequest(AbstractModel):
    """DescribeNetworkFirewallPolicyDiscover请求参数结构体

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
        


class DescribeNetworkFirewallPolicyDiscoverResponse(AbstractModel):
    """DescribeNetworkFirewallPolicyDiscover返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskStatus: 任务状态，可能为：Task_Running,Task_Succ,Task_Error,Task_NoExist
        :type TaskStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallPolicyListRequest(AbstractModel):
    """DescribeNetworkFirewallPolicyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
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
        


class DescribeNetworkFirewallPolicyListResponse(AbstractModel):
    """DescribeNetworkFirewallPolicyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群总数
        :type TotalCount: int
        :param NetPolicy: 集群的详细信息
        :type NetPolicy: list of NetworkPolicyInfoItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NetPolicy = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NetPolicy") is not None:
            self.NetPolicy = []
            for item in params.get("NetPolicy"):
                obj = NetworkPolicyInfoItem()
                obj._deserialize(item)
                self.NetPolicy.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallPolicyStatusRequest(AbstractModel):
    """DescribeNetworkFirewallPolicyStatus请求参数结构体

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
        


class DescribeNetworkFirewallPolicyStatusResponse(AbstractModel):
    """DescribeNetworkFirewallPolicyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskStatus: 任务状态，可能为：Task_Running,Task_Succ,Task_Error,Task_NoExist
        :type TaskStatus: str
        :param TaskResult: NameRepeat,K8sRuleIngressPortError等
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResult: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.TaskResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        self.TaskResult = params.get("TaskResult")
        self.RequestId = params.get("RequestId")


class DescribeNetworkFirewallPolicyYamlDetailRequest(AbstractModel):
    """DescribeNetworkFirewallPolicyYamlDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 策略Id
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
        


class DescribeNetworkFirewallPolicyYamlDetailResponse(AbstractModel):
    """DescribeNetworkFirewallPolicyYamlDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Yaml: base64编码的yaml字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param Description: 策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param PolicyCreateTime: 策略创建时间
        :type PolicyCreateTime: str
        :param PolicySourceType: 策略源类型，分为System和Manual，分别代表手动和系统添加
        :type PolicySourceType: str
        :param NetworkPolicyPlugin: 网络策略对应的网络插件
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkPolicyPlugin: str
        :param PublishStatus: 网络策略状态
        :type PublishStatus: str
        :param PublishResult: 网络发布结果
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishResult: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.PolicyName = None
        self.Yaml = None
        self.Description = None
        self.PolicyCreateTime = None
        self.PolicySourceType = None
        self.NetworkPolicyPlugin = None
        self.PublishStatus = None
        self.PublishResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PolicyName = params.get("PolicyName")
        self.Yaml = params.get("Yaml")
        self.Description = params.get("Description")
        self.PolicyCreateTime = params.get("PolicyCreateTime")
        self.PolicySourceType = params.get("PolicySourceType")
        self.NetworkPolicyPlugin = params.get("NetworkPolicyPlugin")
        self.PublishStatus = params.get("PublishStatus")
        self.PublishResult = params.get("PublishResult")
        self.RequestId = params.get("RequestId")


class DescribeNewestVulRequest(AbstractModel):
    """DescribeNewestVul请求参数结构体

    """


class DescribeNewestVulResponse(AbstractModel):
    """DescribeNewestVul返回参数结构体

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param VulName: 漏洞名称
        :type VulName: str
        :param SubmitTime: 披露时间
        :type SubmitTime: str
        :param Status: 应急漏洞风险情况：NOT_SCAN：未扫描，SCANNING：扫描中，SCANNED：已扫描
        :type Status: str
        :param CVEID: 漏洞CVEID
        :type CVEID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PocID = None
        self.VulName = None
        self.SubmitTime = None
        self.Status = None
        self.CVEID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
        self.VulName = params.get("VulName")
        self.SubmitTime = params.get("SubmitTime")
        self.Status = params.get("Status")
        self.CVEID = params.get("CVEID")
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
        :param BuyStatus: 购买状态
待购: Pending
已购: Normal
隔离: Isolate
        :type BuyStatus: str
        :param IsPurchased: 是否曾经购买过(false:未曾 true:曾经购买过)
        :type IsPurchased: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.CoresCnt = None
        self.MaxPostPayCoresCnt = None
        self.ResourceId = None
        self.BuyStatus = None
        self.IsPurchased = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CoresCnt = params.get("CoresCnt")
        self.MaxPostPayCoresCnt = params.get("MaxPostPayCoresCnt")
        self.ResourceId = params.get("ResourceId")
        self.BuyStatus = params.get("BuyStatus")
        self.IsPurchased = params.get("IsPurchased")
        self.RequestId = params.get("RequestId")


class DescribePromotionActivityRequest(AbstractModel):
    """DescribePromotionActivity请求参数结构体

    """

    def __init__(self):
        r"""
        :param ActiveID: 活动ID
        :type ActiveID: int
        """
        self.ActiveID = None


    def _deserialize(self, params):
        self.ActiveID = params.get("ActiveID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePromotionActivityResponse(AbstractModel):
    """DescribePromotionActivity返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 促销活动内容
        :type List: list of PromotionActivityContent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PromotionActivityContent()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePublicKeyRequest(AbstractModel):
    """DescribePublicKey请求参数结构体

    """


class DescribePublicKeyResponse(AbstractModel):
    """DescribePublicKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param PublicKey: 公钥
        :type PublicKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PublicKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PublicKey = params.get("PublicKey")
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
        :param BeginTime: 起始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param SubState: 子状态(具体意义依据State字段而定)
State为4时，有效值为: ISOLATE(隔离) DESTROED(已销毁)
注意：此字段可能返回 null，表示取不到有效值。
        :type SubState: str
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
        self.BeginTime = None
        self.SubState = None
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
        self.BeginTime = params.get("BeginTime")
        self.SubState = params.get("SubState")
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
        :param AncestorProcessInfo: 祖先进程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessBaseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.ParentProcessInfo = None
        self.EventDetail = None
        self.AncestorProcessInfo = None
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
        if params.get("AncestorProcessInfo") is not None:
            self.AncestorProcessInfo = ProcessBaseInfo()
            self.AncestorProcessInfo._deserialize(params.get("AncestorProcessInfo"))
        self.RequestId = params.get("RequestId")


class DescribeReverseShellEventsExportRequest(AbstractModel):
    """DescribeReverseShellEventsExport请求参数结构体

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
        :param ExportField: 导出字段
        :type ExportField: list of str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None
        self.ExportField = None


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
        self.ExportField = params.get("ExportField")
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
        :param JobId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.JobId = params.get("JobId")
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
        :param AncestorProcessInfo: 祖先进程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessInfo: :class:`tencentcloud.tcss.v20201101.models.ProcessBaseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBaseInfo = None
        self.ProcessInfo = None
        self.ParentProcessInfo = None
        self.EventDetail = None
        self.AncestorProcessInfo = None
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
        if params.get("AncestorProcessInfo") is not None:
            self.AncestorProcessInfo = ProcessBaseInfo()
            self.AncestorProcessInfo._deserialize(params.get("AncestorProcessInfo"))
        self.RequestId = params.get("RequestId")


class DescribeRiskSyscallEventsExportRequest(AbstractModel):
    """DescribeRiskSyscallEventsExport请求参数结构体

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
        :param ExportField: 导出字段
        :type ExportField: list of str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None
        self.ExportField = None


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
        self.ExportField = params.get("ExportField")
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
        :param JobId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.JobId = params.get("JobId")
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


class DescribeScanIgnoreVulListRequest(AbstractModel):
    """DescribeScanIgnoreVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>VulName- string - 是否必填：否 - 漏洞名称</li>
        :type Filters: list of RunTimeFilters
        :param Order: 排序方式:DESC,ACS
        :type Order: str
        :param By: 排序字段 UpdateTime
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
        


class DescribeScanIgnoreVulListResponse(AbstractModel):
    """DescribeScanIgnoreVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总是
        :type TotalCount: int
        :param List: 漏洞列表
        :type List: list of ScanIgnoreVul
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
                obj = ScanIgnoreVul()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSearchExportListRequest(AbstractModel):
    """DescribeSearchExportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Query: ES查询条件JSON
        :type Query: str
        """
        self.Query = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchExportListResponse(AbstractModel):
    """DescribeSearchExportList返回参数结构体

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


class DescribeSearchLogsRequest(AbstractModel):
    """DescribeSearchLogs请求参数结构体

    """


class DescribeSearchLogsResponse(AbstractModel):
    """DescribeSearchLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 历史搜索记录 保留最新的10条
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeSearchTemplatesRequest(AbstractModel):
    """DescribeSearchTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchTemplatesResponse(AbstractModel):
    """DescribeSearchTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 模板列表
        :type List: list of SearchTemplate
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
                obj = SearchTemplate()
                obj._deserialize(item)
                self.List.append(obj)
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


class DescribeSecLogAlertMsgRequest(AbstractModel):
    """DescribeSecLogAlertMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 告警类型
日志储量告警: log_reserve_full
日志存储时间告警: log_save_day_limit
kafka实例/公网域名不可用: kafka_instance_domain_unavailable
kafka 用户名密码错误: kafka_user_passwd_wrong
kafka后台报错字段: kafka_field_wrong
        :type Type: list of str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecLogAlertMsgResponse(AbstractModel):
    """DescribeSecLogAlertMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 告警消息队列
        :type List: list of SecLogAlertMsgInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SecLogAlertMsgInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecLogCleanSettingInfoRequest(AbstractModel):
    """DescribeSecLogCleanSettingInfo请求参数结构体

    """


class DescribeSecLogCleanSettingInfoResponse(AbstractModel):
    """DescribeSecLogCleanSettingInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReservesLimit: 触发清理的储量底线
        :type ReservesLimit: int
        :param ReservesDeadline: 清理停止时的储量截至线
        :type ReservesDeadline: int
        :param DayLimit: 触发清理的存储天数
        :type DayLimit: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReservesLimit = None
        self.ReservesDeadline = None
        self.DayLimit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservesLimit = params.get("ReservesLimit")
        self.ReservesDeadline = params.get("ReservesDeadline")
        self.DayLimit = params.get("DayLimit")
        self.RequestId = params.get("RequestId")


class DescribeSecLogDeliveryClsOptionsRequest(AbstractModel):
    """DescribeSecLogDeliveryClsOptions请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClsRegion: 地域
        :type ClsRegion: str
        """
        self.ClsRegion = None


    def _deserialize(self, params):
        self.ClsRegion = params.get("ClsRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecLogDeliveryClsOptionsResponse(AbstractModel):
    """DescribeSecLogDeliveryClsOptions返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogSetList: cls可选日志集合列表(仅当入参ClsRegion不为空时返回)
        :type LogSetList: list of ClsLogsetInfo
        :param RegionList: 可选地域列表(仅当入参ClsRegion为空时返回)
        :type RegionList: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogSetList = None
        self.RegionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogSetList") is not None:
            self.LogSetList = []
            for item in params.get("LogSetList"):
                obj = ClsLogsetInfo()
                obj._deserialize(item)
                self.LogSetList.append(obj)
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecLogDeliveryClsSettingRequest(AbstractModel):
    """DescribeSecLogDeliveryClsSetting请求参数结构体

    """


class DescribeSecLogDeliveryClsSettingResponse(AbstractModel):
    """DescribeSecLogDeliveryClsSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogTypeList: 日志类型列表
        :type LogTypeList: list of SecLogDeliveryClsSettingInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogTypeList") is not None:
            self.LogTypeList = []
            for item in params.get("LogTypeList"):
                obj = SecLogDeliveryClsSettingInfo()
                obj._deserialize(item)
                self.LogTypeList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecLogDeliveryKafkaOptionsRequest(AbstractModel):
    """DescribeSecLogDeliveryKafkaOptions请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegionID: 地域，若为空则返回所有可选地域
        :type RegionID: str
        """
        self.RegionID = None


    def _deserialize(self, params):
        self.RegionID = params.get("RegionID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecLogDeliveryKafkaOptionsResponse(AbstractModel):
    """DescribeSecLogDeliveryKafkaOptions返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: 实例列表
        :type InstanceList: list of CKafkaInstanceInfo
        :param RegionList: 地域列表
        :type RegionList: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.RegionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = CKafkaInstanceInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecLogDeliveryKafkaSettingRequest(AbstractModel):
    """DescribeSecLogDeliveryKafkaSetting请求参数结构体

    """


class DescribeSecLogDeliveryKafkaSettingResponse(AbstractModel):
    """DescribeSecLogDeliveryKafkaSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceID: 消息队列实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        :param InstanceName: 消息队列实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param LogTypeList: 日志类型队列
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTypeList: list of SecLogDeliveryKafkaSettingInfo
        :param User: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param RegionID: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceID = None
        self.InstanceName = None
        self.Domain = None
        self.LogTypeList = None
        self.User = None
        self.RegionID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.InstanceName = params.get("InstanceName")
        self.Domain = params.get("Domain")
        if params.get("LogTypeList") is not None:
            self.LogTypeList = []
            for item in params.get("LogTypeList"):
                obj = SecLogDeliveryKafkaSettingInfo()
                obj._deserialize(item)
                self.LogTypeList.append(obj)
        self.User = params.get("User")
        self.RegionID = params.get("RegionID")
        self.RequestId = params.get("RequestId")


class DescribeSecLogJoinObjectListRequest(AbstractModel):
    """DescribeSecLogJoinObjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogType: 日志类型
bash: "container_bash",
启动: "container_launch",
"k8s": "k8s_api"
        :type LogType: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status- String - 是否必填：否 - 主机状态 </li>
<li>HostIP- String - 是否必填：否 - 主机内网IP </li>
<li>PublicIP- String - 是否必填：否 - 主机外网IP </li>
<li>HostName- String - 是否必填：否 - 主机名称 </li>
        :type Filters: list of RunTimeFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式
        :type Order: str
        """
        self.LogType = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.LogType = params.get("LogType")
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
        


class DescribeSecLogJoinObjectListResponse(AbstractModel):
    """DescribeSecLogJoinObjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 接入对象列表
        :type List: list of SecLogJoinObjectInfo
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
                obj = SecLogJoinObjectInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecLogJoinTypeListRequest(AbstractModel):
    """DescribeSecLogJoinTypeList请求参数结构体

    """


class DescribeSecLogJoinTypeListResponse(AbstractModel):
    """DescribeSecLogJoinTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 接入日志列表
        :type List: list of SecLogJoinInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SecLogJoinInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecLogKafkaUINRequest(AbstractModel):
    """DescribeSecLogKafkaUIN请求参数结构体

    """


class DescribeSecLogKafkaUINResponse(AbstractModel):
    """DescribeSecLogKafkaUIN返回参数结构体

    """

    def __init__(self):
        r"""
        :param DstUIN: 目标UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type DstUIN: str
        :param Status: 授权状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DstUIN = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DstUIN = params.get("DstUIN")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeSecLogVasInfoRequest(AbstractModel):
    """DescribeSecLogVasInfo请求参数结构体

    """


class DescribeSecLogVasInfoResponse(AbstractModel):
    """DescribeSecLogVasInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param BuyStatus: 购买状态
待购: Pending
已购: Normal
隔离: Isolate
        :type BuyStatus: str
        :param LogSaveMonth: 存储时长(月)
        :type LogSaveMonth: int
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 截止时间
        :type EndTime: str
        :param LogCapacity: 存储容量(GB)
        :type LogCapacity: int
        :param ResourceID: 资源ID
        :type ResourceID: str
        :param IsPurchased: 是否曾经购买过(false:未曾 true:曾经购买过)
        :type IsPurchased: bool
        :param TrialCapacity: 试用存储容量(GB)
        :type TrialCapacity: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BuyStatus = None
        self.LogSaveMonth = None
        self.StartTime = None
        self.EndTime = None
        self.LogCapacity = None
        self.ResourceID = None
        self.IsPurchased = None
        self.TrialCapacity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BuyStatus = params.get("BuyStatus")
        self.LogSaveMonth = params.get("LogSaveMonth")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.LogCapacity = params.get("LogCapacity")
        self.ResourceID = params.get("ResourceID")
        self.IsPurchased = params.get("IsPurchased")
        self.TrialCapacity = params.get("TrialCapacity")
        self.RequestId = params.get("RequestId")


class DescribeSupportDefenceVulRequest(AbstractModel):
    """DescribeSupportDefenceVul请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Level- String - 是否必填：否 - 威胁等级，CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低</li>
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>Name- string -是否必填: 否 - 漏洞名称</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式：asc/desc
        :type Order: str
        :param By: 排序字段：披露时间：SubmitTime
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
        


class DescribeSupportDefenceVulResponse(AbstractModel):
    """DescribeSupportDefenceVul返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 支持防御的漏洞列表
        :type List: list of SupportDefenceVul
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
                obj = SupportDefenceVul()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSystemVulListRequest(AbstractModel):
    """DescribeSystemVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>OnlyAffectedContainer- string - 是否必填：否 - 仅展示影响容器的漏洞true,false</li>
<li>OnlyAffectedNewestImage-string - 是否必填：否 - 仅展示影响最新版本镜像的漏洞true,false</li>
<li>Level- String - 是否必填：否 - 威胁等级，CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低</li>
<li>Tags- string - 是否必填：否 - 漏洞标签，POC，EXP。</li>
<li>CanBeFixed- string - 是否必填：否 - 是否可修复true,false。</li>
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>ContainerID- string -是否必填: 否 - 容器ID</li>
<li>ContainerName- string -是否必填: 否 - 容器名称</li>
<li>ComponentName- string -是否必填: 否 - 组件名称</li>
<li>ComponentVersion- string -是否必填: 否 - 组件版本</li>
<li>Name- string -是否必填: 否 - 漏洞名称</li>
<li>FocusOnType - string - 是否必填：否 -关注紧急度类型 。ALL :全部，SERIOUS_LEVEL： 严重和高危 ，IS_SUGGEST： 重点关注，POC_EXP 有Poc或Exp ，NETWORK_EXP: 远程Exp</li>
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
        


class DescribeSystemVulListResponse(AbstractModel):
    """DescribeSystemVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 漏洞总数
        :type TotalCount: int
        :param List: 漏洞列表
        :type List: list of VulInfo
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
                obj = VulInfo()
                obj._deserialize(item)
                self.List.append(obj)
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


class DescribeTcssSummaryRequest(AbstractModel):
    """DescribeTcssSummary请求参数结构体

    """


class DescribeTcssSummaryResponse(AbstractModel):
    """DescribeTcssSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageCnt: 镜像总数
        :type ImageCnt: int
        :param ScannedImageCnt: 已扫描镜像数
        :type ScannedImageCnt: int
        :param UnScannedImageCnt: 待扫描镜像个数
        :type UnScannedImageCnt: int
        :param LocalImageCnt: 本地镜像个数
        :type LocalImageCnt: int
        :param RepositoryImageCnt: 仓库镜像个数
        :type RepositoryImageCnt: int
        :param RiskLocalImageCnt: 风险本地镜像个数
        :type RiskLocalImageCnt: int
        :param RiskRepositoryImageCnt: 风险仓库镜像个数
        :type RiskRepositoryImageCnt: int
        :param ContainerCnt: 容器个数
        :type ContainerCnt: int
        :param RiskContainerCnt: 风险容器个数
        :type RiskContainerCnt: int
        :param ClusterCnt: 集群个数
        :type ClusterCnt: int
        :param RiskClusterCnt: 风险集群个数
        :type RiskClusterCnt: int
        :param UnScannedVulCnt: 待扫描漏洞个数
        :type UnScannedVulCnt: int
        :param RiskVulCnt: 风险漏洞个数
        :type RiskVulCnt: int
        :param UnScannedBaseLineCnt: 安全基线待扫描项个数
        :type UnScannedBaseLineCnt: int
        :param RiskBaseLineCnt: 安全基线风险个数
        :type RiskBaseLineCnt: int
        :param RuntimeUnhandleEventCnt: 运行时(高危)待处理事件个数
        :type RuntimeUnhandleEventCnt: int
        :param UnScannedClusterCnt: 待扫描集群个数
        :type UnScannedClusterCnt: int
        :param ScanImageStatus: 是否已扫描镜像
        :type ScanImageStatus: bool
        :param ScanClusterStatus: 是否已扫描集群
        :type ScanClusterStatus: bool
        :param ScanBaseLineStatus: 是否已扫描基线
        :type ScanBaseLineStatus: bool
        :param ScanVulStatus: 是否已扫描漏洞
        :type ScanVulStatus: bool
        :param VulRiskImageCnt: 漏洞影响镜像数
        :type VulRiskImageCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageCnt = None
        self.ScannedImageCnt = None
        self.UnScannedImageCnt = None
        self.LocalImageCnt = None
        self.RepositoryImageCnt = None
        self.RiskLocalImageCnt = None
        self.RiskRepositoryImageCnt = None
        self.ContainerCnt = None
        self.RiskContainerCnt = None
        self.ClusterCnt = None
        self.RiskClusterCnt = None
        self.UnScannedVulCnt = None
        self.RiskVulCnt = None
        self.UnScannedBaseLineCnt = None
        self.RiskBaseLineCnt = None
        self.RuntimeUnhandleEventCnt = None
        self.UnScannedClusterCnt = None
        self.ScanImageStatus = None
        self.ScanClusterStatus = None
        self.ScanBaseLineStatus = None
        self.ScanVulStatus = None
        self.VulRiskImageCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageCnt = params.get("ImageCnt")
        self.ScannedImageCnt = params.get("ScannedImageCnt")
        self.UnScannedImageCnt = params.get("UnScannedImageCnt")
        self.LocalImageCnt = params.get("LocalImageCnt")
        self.RepositoryImageCnt = params.get("RepositoryImageCnt")
        self.RiskLocalImageCnt = params.get("RiskLocalImageCnt")
        self.RiskRepositoryImageCnt = params.get("RiskRepositoryImageCnt")
        self.ContainerCnt = params.get("ContainerCnt")
        self.RiskContainerCnt = params.get("RiskContainerCnt")
        self.ClusterCnt = params.get("ClusterCnt")
        self.RiskClusterCnt = params.get("RiskClusterCnt")
        self.UnScannedVulCnt = params.get("UnScannedVulCnt")
        self.RiskVulCnt = params.get("RiskVulCnt")
        self.UnScannedBaseLineCnt = params.get("UnScannedBaseLineCnt")
        self.RiskBaseLineCnt = params.get("RiskBaseLineCnt")
        self.RuntimeUnhandleEventCnt = params.get("RuntimeUnhandleEventCnt")
        self.UnScannedClusterCnt = params.get("UnScannedClusterCnt")
        self.ScanImageStatus = params.get("ScanImageStatus")
        self.ScanClusterStatus = params.get("ScanClusterStatus")
        self.ScanBaseLineStatus = params.get("ScanBaseLineStatus")
        self.ScanVulStatus = params.get("ScanVulStatus")
        self.VulRiskImageCnt = params.get("VulRiskImageCnt")
        self.RequestId = params.get("RequestId")


class DescribeUnauthorizedCoresTendencyRequest(AbstractModel):
    """DescribeUnauthorizedCoresTendency请求参数结构体

    """


class DescribeUnauthorizedCoresTendencyResponse(AbstractModel):
    """DescribeUnauthorizedCoresTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 未授权核数趋势
        :type List: list of UnauthorizedCoresTendency
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = UnauthorizedCoresTendency()
                obj._deserialize(item)
                self.List.append(obj)
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


class DescribeVirusAutoIsolateSampleDetailRequest(AbstractModel):
    """DescribeVirusAutoIsolateSampleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param MD5: 文件MD5值
        :type MD5: str
        """
        self.MD5 = None


    def _deserialize(self, params):
        self.MD5 = params.get("MD5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusAutoIsolateSampleDetailResponse(AbstractModel):
    """DescribeVirusAutoIsolateSampleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param MD5: 文件Md5值
        :type MD5: str
        :param Size: 文件大小(B)
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param VirusName: 病毒名
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusName: str
        :param RiskLevel: 风险等级 RISK_CRITICAL, RISK_HIGH, RISK_MEDIUM, RISK_LOW, RISK_NOTICE。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param KillEngine: 查杀引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type KillEngine: list of str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param HarmDescribe: 事件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HarmDescribe: str
        :param SuggestScheme: 建议方案
注意：此字段可能返回 null，表示取不到有效值。
        :type SuggestScheme: str
        :param ReferenceLink: 参考链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ReferenceLink: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MD5 = None
        self.Size = None
        self.VirusName = None
        self.RiskLevel = None
        self.KillEngine = None
        self.Tags = None
        self.HarmDescribe = None
        self.SuggestScheme = None
        self.ReferenceLink = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MD5 = params.get("MD5")
        self.Size = params.get("Size")
        self.VirusName = params.get("VirusName")
        self.RiskLevel = params.get("RiskLevel")
        self.KillEngine = params.get("KillEngine")
        self.Tags = params.get("Tags")
        self.HarmDescribe = params.get("HarmDescribe")
        self.SuggestScheme = params.get("SuggestScheme")
        self.ReferenceLink = params.get("ReferenceLink")
        self.RequestId = params.get("RequestId")


class DescribeVirusAutoIsolateSampleDownloadURLRequest(AbstractModel):
    """DescribeVirusAutoIsolateSampleDownloadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param MD5: 样本Md5值
        :type MD5: str
        """
        self.MD5 = None


    def _deserialize(self, params):
        self.MD5 = params.get("MD5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusAutoIsolateSampleDownloadURLResponse(AbstractModel):
    """DescribeVirusAutoIsolateSampleDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileUrl: 样本下载链接
        :type FileUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
        self.RequestId = params.get("RequestId")


class DescribeVirusAutoIsolateSampleListRequest(AbstractModel):
    """DescribeVirusAutoIsolateSampleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>MD5- String - 是否必填：否 - md5 </li>
<li>AutoIsolateSwitch- String - 是否必填：否 - 自动隔离开关 </li>
<li>VirusName- String - 是否必填：否 - 病毒名 </li>
        :type Filters: list of RunTimeFilters
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式
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
        


class DescribeVirusAutoIsolateSampleListResponse(AbstractModel):
    """DescribeVirusAutoIsolateSampleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 木马自动隔离样本列表
        :type List: list of VirusAutoIsolateSampleInfo
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
                obj = VirusAutoIsolateSampleInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVirusAutoIsolateSettingRequest(AbstractModel):
    """DescribeVirusAutoIsolateSetting请求参数结构体

    """


class DescribeVirusAutoIsolateSettingResponse(AbstractModel):
    """DescribeVirusAutoIsolateSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param AutoIsolateSwitch: 自动隔离开关(true:开 false:关)
        :type AutoIsolateSwitch: bool
        :param IsKillProgress: 是否中断隔离文件关联的进程(true:是 false:否)
        :type IsKillProgress: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AutoIsolateSwitch = None
        self.IsKillProgress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoIsolateSwitch = params.get("AutoIsolateSwitch")
        self.IsKillProgress = params.get("IsKillProgress")
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
        :param PProcessStartUser: 父进程启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :type PProcessStartUser: str
        :param PProcessUserGroup: 父进程用户组
注意：此字段可能返回 null，表示取不到有效值。
        :type PProcessUserGroup: str
        :param PProcessPath: 父进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type PProcessPath: str
        :param PProcessParam: 父进程命令行参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PProcessParam: str
        :param AncestorProcessStartUser: 祖先进程启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessStartUser: str
        :param AncestorProcessUserGroup: 祖先进程用户组
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessUserGroup: str
        :param AncestorProcessPath: 祖先进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessPath: str
        :param AncestorProcessParam: 祖先进程命令行参数
注意：此字段可能返回 null，表示取不到有效值。
        :type AncestorProcessParam: str
        :param OperationTime: 事件最后一次处理的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationTime: str
        :param ContainerNetStatus: 容器隔离状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器隔离子状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerIsolateOperationSrc: str
        :param CheckPlatform: 检测平台
1: 云查杀引擎
2: tav
3: binaryAi
4: 异常行为
5: 威胁情报
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPlatform: list of str
        :param FileAccessTime: 文件访问时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FileAccessTime: str
        :param FileModifyTime: 文件修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FileModifyTime: str
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
        self.PProcessStartUser = None
        self.PProcessUserGroup = None
        self.PProcessPath = None
        self.PProcessParam = None
        self.AncestorProcessStartUser = None
        self.AncestorProcessUserGroup = None
        self.AncestorProcessPath = None
        self.AncestorProcessParam = None
        self.OperationTime = None
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.CheckPlatform = None
        self.FileAccessTime = None
        self.FileModifyTime = None
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
        self.PProcessStartUser = params.get("PProcessStartUser")
        self.PProcessUserGroup = params.get("PProcessUserGroup")
        self.PProcessPath = params.get("PProcessPath")
        self.PProcessParam = params.get("PProcessParam")
        self.AncestorProcessStartUser = params.get("AncestorProcessStartUser")
        self.AncestorProcessUserGroup = params.get("AncestorProcessUserGroup")
        self.AncestorProcessPath = params.get("AncestorProcessPath")
        self.AncestorProcessParam = params.get("AncestorProcessParam")
        self.OperationTime = params.get("OperationTime")
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.CheckPlatform = params.get("CheckPlatform")
        self.FileAccessTime = params.get("FileAccessTime")
        self.FileModifyTime = params.get("FileModifyTime")
        self.RequestId = params.get("RequestId")


class DescribeVirusEventTendencyRequest(AbstractModel):
    """DescribeVirusEventTendency请求参数结构体

    """

    def __init__(self):
        r"""
        :param TendencyPeriod: 趋势周期(默认为7天)
        :type TendencyPeriod: int
        """
        self.TendencyPeriod = None


    def _deserialize(self, params):
        self.TendencyPeriod = params.get("TendencyPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusEventTendencyResponse(AbstractModel):
    """DescribeVirusEventTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 趋势列表
        :type List: list of VirusTendencyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = VirusTendencyInfo()
                obj._deserialize(item)
                self.List.append(obj)
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
<li>ContainerNetStatus - String -是否必填: 否 -  容器网络状态筛选 NORMAL ISOLATED ISOLATING RESTORING RESTORE_FAILED</li>
<li>TimeRange - string -是否必填: 否 - 时间范围筛选 ["2022-03-31 16:55:00", "2022-03-31 17:00:00"]</li>
<li>ContainerStatus - string -是否必填: 否 - 容器状态 RUNNING PAUSED STOPPED CREATED DESTROYED RESTARTING REMOVING</li>
<li>AutoIsolateMode - string -是否必填: 否 - 隔离方式 MANUAL AUTO</li>
<li>MD5 - string -是否必填: 否 - md5 </li>
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


class DescribeVirusManualScanEstimateTimeoutRequest(AbstractModel):
    """DescribeVirusManualScanEstimateTimeout请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScanRangeType: 扫描范围0容器1主机节点
        :type ScanRangeType: int
        :param ScanRangeAll: true 全选，false 自选
        :type ScanRangeAll: bool
        :param ScanIds: 自选扫描范围的容器id或者主机id 根据ScanRangeType决定
        :type ScanIds: list of str
        """
        self.ScanRangeType = None
        self.ScanRangeAll = None
        self.ScanIds = None


    def _deserialize(self, params):
        self.ScanRangeType = params.get("ScanRangeType")
        self.ScanRangeAll = params.get("ScanRangeAll")
        self.ScanIds = params.get("ScanIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusManualScanEstimateTimeoutResponse(AbstractModel):
    """DescribeVirusManualScanEstimateTimeout返回参数结构体

    """

    def __init__(self):
        r"""
        :param Timeout: 预估超时时间(h)
        :type Timeout: float
        :param ContainerScanConcurrencyCount: 单台主机并行扫描容器数
        :type ContainerScanConcurrencyCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Timeout = None
        self.ContainerScanConcurrencyCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Timeout = params.get("Timeout")
        self.ContainerScanConcurrencyCount = params.get("ContainerScanConcurrencyCount")
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
        :param ScanPathMode: 扫描路径模式：
SCAN_PATH_ALL：全部路径
SCAN_PATH_DEFAULT：默认路径
SCAN_PATH_USER_DEFINE：用户自定义路径

        :type ScanPathMode: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnableScan = None
        self.ScanPathAll = None
        self.ScanPathType = None
        self.ScanPath = None
        self.ScanPathMode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnableScan = params.get("EnableScan")
        self.ScanPathAll = params.get("ScanPathAll")
        self.ScanPathType = params.get("ScanPathType")
        self.ScanPath = params.get("ScanPath")
        self.ScanPathMode = params.get("ScanPathMode")
        self.RequestId = params.get("RequestId")


class DescribeVirusSampleDownloadUrlRequest(AbstractModel):
    """DescribeVirusSampleDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 木马id
        :type ID: str
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVirusSampleDownloadUrlResponse(AbstractModel):
    """DescribeVirusSampleDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileUrl: 样本下载地址
        :type FileUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
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
        :param ScanPathMode: 扫描路径模式：
SCAN_PATH_ALL：全部路径
SCAN_PATH_DEFAULT：默认路径
SCAN_PATH_USER_DEFINE：用户自定义路径

        :type ScanPathMode: str
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
        self.ScanPathMode = None
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
        self.ScanPathMode = params.get("ScanPathMode")
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
        :param IsolateIncrease: 隔离事件个数较昨日新增
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateIncrease: int
        :param IsolateCnt: 隔离事件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RiskContainerCnt = None
        self.RiskCnt = None
        self.VirusDataBaseModifyTime = None
        self.RiskContainerIncrease = None
        self.RiskIncrease = None
        self.IsolateIncrease = None
        self.IsolateCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RiskContainerCnt = params.get("RiskContainerCnt")
        self.RiskCnt = params.get("RiskCnt")
        self.VirusDataBaseModifyTime = params.get("VirusDataBaseModifyTime")
        self.RiskContainerIncrease = params.get("RiskContainerIncrease")
        self.RiskIncrease = params.get("RiskIncrease")
        self.IsolateIncrease = params.get("IsolateIncrease")
        self.IsolateCnt = params.get("IsolateCnt")
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
<li>HostIp- String - 是否必填：否 - 主机IP</li>
<li>ImageId- String - 是否必填：否 - 镜像ID</li>
<li>ImageName- String - 是否必填：否 - 镜像名称</li>
<li>Status- String - 是否必填：否 - 状态</li>
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
        :param TotalCount: 总数量(容器任务数量)
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


class DescribeVulContainerListRequest(AbstractModel):
    """DescribeVulContainerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>OnlyAffectedNewestImage- Bool- 是否必填：否 - 仅展示影响最新版本镜像的漏洞</li>
<li>ContainerID- string - 是否必填：否 - 容器ID</li>
<li>ContainerName- String -是否必填: 否 - 容器名称</li>
        :type Filters: list of RunTimeFilters
        """
        self.PocID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulContainerListResponse(AbstractModel):
    """DescribeVulContainerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 容器列表
        :type List: list of VulAffectedContainerInfo
        :param TotalCount: 容器总数
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
                obj = VulAffectedContainerInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVulDefenceEventDetailRequest(AbstractModel):
    """DescribeVulDefenceEventDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventID: 事件ID
        :type EventID: int
        """
        self.EventID = None


    def _deserialize(self, params):
        self.EventID = params.get("EventID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulDefenceEventDetailResponse(AbstractModel):
    """DescribeVulDefenceEventDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventDetail: 漏洞防御事件详细
        :type EventDetail: :class:`tencentcloud.tcss.v20201101.models.VulDefenceEventDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventDetail") is not None:
            self.EventDetail = VulDefenceEventDetail()
            self.EventDetail._deserialize(params.get("EventDetail"))
        self.RequestId = params.get("RequestId")


class DescribeVulDefenceEventRequest(AbstractModel):
    """DescribeVulDefenceEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Status- String - 是否必填：否 - 插件状态，待处理：EVENT_UNDEAL，EVENT_DEALED：已处理，已忽略：EVENT_IGNORE， EVENT_DEFENDED：已防御</li>
<li>ContainerStatus- String - 是否必填：否 - 容器运行状态筛选，已创建：CREATED,正常运行：RUNNING, 暂定运行：PAUSED, 停止运行：	STOPPED，重启中：RESTARTING, 迁移中：REMOVING, 销毁：DESTROYED </li>
<li>ContainerNetStatus- String -是否必填: 否 -  容器网络状态筛选 未隔离：NORMAL，已隔离：ISOLATED，隔离失败：ISOLATE_FAILED，解除隔离失败：RESTORE_FAILED，解除隔离中：RESTORING，隔离中：ISOLATING</li>
<li>EventType - String -是否必填: 否 -  入侵状态，防御成功：EVENT_DEFENDED，尝试攻击：EVENT_ATTACK </li>
<li>TimeRange- String -是否必填: 否 -  时间范围，第一个值表示开始时间，第二个值表示结束时间 </li>
<li>VulName- string - 是否必填：否 - 漏洞名称。</li>
<li>CVEID- string - 是否必填：否 - CVE编号。</li>
<li>SourceIP- string - 是否必填：否 - 攻击源IP。</li>
<li>ContainerName- string - 是否必填：否 - 容器名称。</li>
<li>ContainerID- string - 是否必填：否 - 容器ID。</li>
<li>ImageName- string - 是否必填：否 - 镜像名称。</li>
<li>ImageID- string - 是否必填：否 - 镜像ID。</li>
<li>HostName- string - 是否必填：否 - 主机名称。</li>
<li>HostIP- string - 是否必填：否 - 内网IP。</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式：asc/desc
        :type Order: str
        :param By: 排序字段：事件数量：EventCount
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
        


class DescribeVulDefenceEventResponse(AbstractModel):
    """DescribeVulDefenceEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 漏洞防御事件列表
        :type List: list of VulDefenceEvent
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
                obj = VulDefenceEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVulDefenceEventTendencyRequest(AbstractModel):
    """DescribeVulDefenceEventTendency请求参数结构体

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
        


class DescribeVulDefenceEventTendencyResponse(AbstractModel):
    """DescribeVulDefenceEventTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param DefendedList: 漏洞防御事件趋势
        :type DefendedList: list of VulDefenceEventTendency
        :param AttackList: 漏洞攻击事件趋势
        :type AttackList: list of VulDefenceEventTendency
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DefendedList = None
        self.AttackList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DefendedList") is not None:
            self.DefendedList = []
            for item in params.get("DefendedList"):
                obj = VulDefenceEventTendency()
                obj._deserialize(item)
                self.DefendedList.append(obj)
        if params.get("AttackList") is not None:
            self.AttackList = []
            for item in params.get("AttackList"):
                obj = VulDefenceEventTendency()
                obj._deserialize(item)
                self.AttackList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulDefenceHostRequest(AbstractModel):
    """DescribeVulDefenceHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Status- String - 是否必填：否 - 插件状态，正常：SUCCESS，异常：FAIL， NO_DEFENCE:未防御</li>
<li>KeyWords- string - 是否必填：否 - 主机名称/IP。</li>
        :type Filters: list of RunTimeFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式：asc/desc
        :type Order: str
        :param By: 排序字段：更新时间：ModifyTime/首次开启时间：CreateTime
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
        


class DescribeVulDefenceHostResponse(AbstractModel):
    """DescribeVulDefenceHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param List: 漏洞防御的主机列表
        :type List: list of VulDefenceHost
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
                obj = VulDefenceHost()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulDefencePluginRequest(AbstractModel):
    """DescribeVulDefencePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param HostID: 主机HostID即quuid
        :type HostID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status- String - 是否必填：否 -插件运行状态：注入中:INJECTING，注入成功：SUCCESS，注入失败：FAIL，插件超时：TIMEOUT，插件退出：QUIT</li>
        :type Filters: list of RunTimeFilters
        """
        self.HostID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.HostID = params.get("HostID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulDefencePluginResponse(AbstractModel):
    """DescribeVulDefencePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param List: 漏洞防御插件列表
        :type List: list of VulDefencePlugin
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
                obj = VulDefencePlugin()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulDefenceSettingRequest(AbstractModel):
    """DescribeVulDefenceSetting请求参数结构体

    """


class DescribeVulDefenceSettingResponse(AbstractModel):
    """DescribeVulDefenceSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsEnabled: 是否开启:0: 关闭 1:开启
        :type IsEnabled: int
        :param Scope: 漏洞防御主机范围: 0:自选主机节点，1:全部
        :type Scope: int
        :param HostCount: 漏洞防御主机数量
        :type HostCount: int
        :param ExceptionHostCount: 开启漏洞防御异常主机数量
        :type ExceptionHostCount: int
        :param HostIDs: 自选漏洞防御主机
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIDs: list of str
        :param HostTotalCount: 开通容器安全的主机总数
注意：此字段可能返回 null，表示取不到有效值。
        :type HostTotalCount: int
        :param SupportDefenseVulCount: 支持防御的漏洞数
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportDefenseVulCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsEnabled = None
        self.Scope = None
        self.HostCount = None
        self.ExceptionHostCount = None
        self.HostIDs = None
        self.HostTotalCount = None
        self.SupportDefenseVulCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsEnabled = params.get("IsEnabled")
        self.Scope = params.get("Scope")
        self.HostCount = params.get("HostCount")
        self.ExceptionHostCount = params.get("ExceptionHostCount")
        self.HostIDs = params.get("HostIDs")
        self.HostTotalCount = params.get("HostTotalCount")
        self.SupportDefenseVulCount = params.get("SupportDefenseVulCount")
        self.RequestId = params.get("RequestId")


class DescribeVulDetailRequest(AbstractModel):
    """DescribeVulDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        """
        self.PocID = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulDetailResponse(AbstractModel):
    """DescribeVulDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulInfo: 漏洞详情信息
        :type VulInfo: :class:`tencentcloud.tcss.v20201101.models.VulDetailInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulInfo") is not None:
            self.VulInfo = VulDetailInfo()
            self.VulInfo._deserialize(params.get("VulInfo"))
        self.RequestId = params.get("RequestId")


class DescribeVulIgnoreLocalImageListRequest(AbstractModel):
    """DescribeVulIgnoreLocalImageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式:DESC,ACS
        :type Order: str
        :param By: 排序字段 ImageSize
        :type By: str
        """
        self.PocID = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
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
        


class DescribeVulIgnoreLocalImageListResponse(AbstractModel):
    """DescribeVulIgnoreLocalImageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param List: 镜像列表
        :type List: list of VulIgnoreLocalImage
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
                obj = VulIgnoreLocalImage()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulIgnoreRegistryImageListRequest(AbstractModel):
    """DescribeVulIgnoreRegistryImageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.PocID = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulIgnoreRegistryImageListResponse(AbstractModel):
    """DescribeVulIgnoreRegistryImageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param List: 镜像列表
        :type List: list of VulIgnoreRegistryImage
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
                obj = VulIgnoreRegistryImage()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulImageListRequest(AbstractModel):
    """DescribeVulImageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>OnlyAffectedNewestImage- Bool- 是否必填：否 - 仅展示影响最新版本镜像的漏洞</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>HostIP- string -是否必填: 否 - 内网IP</li>
<li>PublicIP- string -是否必填: 否 - 外网IP</li>
<li>ComponentName- string -是否必填: 否 - 组件名称</li>
<li>ComponentVersion- string -是否必填: 否 - 组件版本</li>
<li>HostName- string -是否必填: 否 - 主机名称</li>
        :type Filters: list of RunTimeFilters
        :param Order: 排序方式
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.PocID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
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
        


class DescribeVulImageListResponse(AbstractModel):
    """DescribeVulImageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 受影响的镜像列表
        :type List: list of VulAffectedImageInfo
        :param TotalCount: 镜像总数
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
                obj = VulAffectedImageInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVulImageSummaryRequest(AbstractModel):
    """DescribeVulImageSummary请求参数结构体

    """


class DescribeVulImageSummaryResponse(AbstractModel):
    """DescribeVulImageSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param SeriousVulImageCount: 受严重或高危漏洞影响的镜像数
        :type SeriousVulImageCount: int
        :param ScannedImageCount: 已扫描的镜像数
        :type ScannedImageCount: int
        :param VulTotalCount: 漏洞总数量
        :type VulTotalCount: int
        :param SysTemVulCount: 系统漏洞数
        :type SysTemVulCount: int
        :param WebVulCount: web应用漏洞数
        :type WebVulCount: int
        :param AllAuthorizedImageCount: 已授权镜像数
        :type AllAuthorizedImageCount: int
        :param EmergencyVulCount: 应急漏洞数
        :type EmergencyVulCount: int
        :param SupportVulTotalCount: 支持扫描的漏洞总数量
        :type SupportVulTotalCount: int
        :param VulLibraryUpdateTime: 漏洞库更新时间
        :type VulLibraryUpdateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SeriousVulImageCount = None
        self.ScannedImageCount = None
        self.VulTotalCount = None
        self.SysTemVulCount = None
        self.WebVulCount = None
        self.AllAuthorizedImageCount = None
        self.EmergencyVulCount = None
        self.SupportVulTotalCount = None
        self.VulLibraryUpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SeriousVulImageCount = params.get("SeriousVulImageCount")
        self.ScannedImageCount = params.get("ScannedImageCount")
        self.VulTotalCount = params.get("VulTotalCount")
        self.SysTemVulCount = params.get("SysTemVulCount")
        self.WebVulCount = params.get("WebVulCount")
        self.AllAuthorizedImageCount = params.get("AllAuthorizedImageCount")
        self.EmergencyVulCount = params.get("EmergencyVulCount")
        self.SupportVulTotalCount = params.get("SupportVulTotalCount")
        self.VulLibraryUpdateTime = params.get("VulLibraryUpdateTime")
        self.RequestId = params.get("RequestId")


class DescribeVulLevelImageSummaryRequest(AbstractModel):
    """DescribeVulLevelImageSummary请求参数结构体

    """


class DescribeVulLevelImageSummaryResponse(AbstractModel):
    """DescribeVulLevelImageSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param HighLevelVulLocalImagePercent: 高危漏洞最新本地镜像占比
        :type HighLevelVulLocalImagePercent: float
        :param MediumLevelVulLocalImagePercent: 中危漏洞最新本地镜像占比
        :type MediumLevelVulLocalImagePercent: float
        :param LowLevelVulLocalImagePercent: 低危漏洞最新本地镜像占比
        :type LowLevelVulLocalImagePercent: float
        :param CriticalLevelVulLocalImagePercent: 严重漏洞最新本地镜像占比
        :type CriticalLevelVulLocalImagePercent: float
        :param LocalNewestImageCount: 影响的最新版本本地镜像数
        :type LocalNewestImageCount: int
        :param RegistryNewestImageCount: 影响的最新版本仓库镜像数
        :type RegistryNewestImageCount: int
        :param HighLevelVulRegistryImagePercent: 高危漏洞最新仓库镜像占比
        :type HighLevelVulRegistryImagePercent: float
        :param MediumLevelVulRegistryImagePercent: 中危漏洞最新仓库镜像占比
        :type MediumLevelVulRegistryImagePercent: float
        :param LowLevelVulRegistryImagePercent: 低危漏洞最新仓库镜像占比
        :type LowLevelVulRegistryImagePercent: float
        :param CriticalLevelVulRegistryImagePercent: 严重漏洞最新仓库镜像占比
        :type CriticalLevelVulRegistryImagePercent: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HighLevelVulLocalImagePercent = None
        self.MediumLevelVulLocalImagePercent = None
        self.LowLevelVulLocalImagePercent = None
        self.CriticalLevelVulLocalImagePercent = None
        self.LocalNewestImageCount = None
        self.RegistryNewestImageCount = None
        self.HighLevelVulRegistryImagePercent = None
        self.MediumLevelVulRegistryImagePercent = None
        self.LowLevelVulRegistryImagePercent = None
        self.CriticalLevelVulRegistryImagePercent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HighLevelVulLocalImagePercent = params.get("HighLevelVulLocalImagePercent")
        self.MediumLevelVulLocalImagePercent = params.get("MediumLevelVulLocalImagePercent")
        self.LowLevelVulLocalImagePercent = params.get("LowLevelVulLocalImagePercent")
        self.CriticalLevelVulLocalImagePercent = params.get("CriticalLevelVulLocalImagePercent")
        self.LocalNewestImageCount = params.get("LocalNewestImageCount")
        self.RegistryNewestImageCount = params.get("RegistryNewestImageCount")
        self.HighLevelVulRegistryImagePercent = params.get("HighLevelVulRegistryImagePercent")
        self.MediumLevelVulRegistryImagePercent = params.get("MediumLevelVulRegistryImagePercent")
        self.LowLevelVulRegistryImagePercent = params.get("LowLevelVulRegistryImagePercent")
        self.CriticalLevelVulRegistryImagePercent = params.get("CriticalLevelVulRegistryImagePercent")
        self.RequestId = params.get("RequestId")


class DescribeVulLevelSummaryRequest(AbstractModel):
    """DescribeVulLevelSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param CategoryType: 漏洞分类: SYSTEM:系统漏洞 WEB:web应用漏洞 EMERGENCY:应急漏洞
        :type CategoryType: str
        """
        self.CategoryType = None


    def _deserialize(self, params):
        self.CategoryType = params.get("CategoryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulLevelSummaryResponse(AbstractModel):
    """DescribeVulLevelSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param HighLevelVulCount: 高危漏洞数
        :type HighLevelVulCount: int
        :param MediumLevelVulCount: 中危漏洞数
        :type MediumLevelVulCount: int
        :param LowLevelVulCount: 低危漏洞数
        :type LowLevelVulCount: int
        :param CriticalLevelVulCount: 严重漏洞数
        :type CriticalLevelVulCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HighLevelVulCount = None
        self.MediumLevelVulCount = None
        self.LowLevelVulCount = None
        self.CriticalLevelVulCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HighLevelVulCount = params.get("HighLevelVulCount")
        self.MediumLevelVulCount = params.get("MediumLevelVulCount")
        self.LowLevelVulCount = params.get("LowLevelVulCount")
        self.CriticalLevelVulCount = params.get("CriticalLevelVulCount")
        self.RequestId = params.get("RequestId")


class DescribeVulScanAuthorizedImageSummaryRequest(AbstractModel):
    """DescribeVulScanAuthorizedImageSummary请求参数结构体

    """


class DescribeVulScanAuthorizedImageSummaryResponse(AbstractModel):
    """DescribeVulScanAuthorizedImageSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param AllAuthorizedImageCount: 全部已授权的本地镜像数
        :type AllAuthorizedImageCount: int
        :param UnScanAuthorizedImageCount: 已授权未扫描的本地镜像数
        :type UnScanAuthorizedImageCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllAuthorizedImageCount = None
        self.UnScanAuthorizedImageCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllAuthorizedImageCount = params.get("AllAuthorizedImageCount")
        self.UnScanAuthorizedImageCount = params.get("UnScanAuthorizedImageCount")
        self.RequestId = params.get("RequestId")


class DescribeVulScanInfoRequest(AbstractModel):
    """DescribeVulScanInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param LocalTaskID: 本地镜像漏洞扫描任务ID，无则返回最近一次的漏洞任务扫描
        :type LocalTaskID: int
        :param RegistryTaskID: 仓库镜像漏洞扫描任务ID，无则返回最近一次的漏洞任务扫描
        :type RegistryTaskID: int
        """
        self.LocalTaskID = None
        self.RegistryTaskID = None


    def _deserialize(self, params):
        self.LocalTaskID = params.get("LocalTaskID")
        self.RegistryTaskID = params.get("RegistryTaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulScanInfoResponse(AbstractModel):
    """DescribeVulScanInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param LocalImageScanCount: 本次扫描的本地镜像总数
        :type LocalImageScanCount: int
        :param IgnoreVulCount: 忽略的漏洞数量
        :type IgnoreVulCount: int
        :param ScanStartTime: 漏洞扫描的开始时间
        :type ScanStartTime: str
        :param ScanEndTime: 漏洞扫描的结束时间
        :type ScanEndTime: str
        :param FoundRiskImageCount: 发现风险镜像数量
        :type FoundRiskImageCount: int
        :param FoundVulCount: 本地发现漏洞数量
        :type FoundVulCount: int
        :param ScanProgress: 扫描进度
        :type ScanProgress: float
        :param RegistryImageScanCount: 本次扫描的仓库镜像总数
        :type RegistryImageScanCount: int
        :param LocalTaskID: 本地镜像最近一次的漏洞任务扫描ID
        :type LocalTaskID: int
        :param Status: 扫描状态:NOT_SCAN:未扫描，SCANNING:扫描中,SCANNED:完成，CANCELED：扫描停止
        :type Status: str
        :param RemainingTime: 剩余时间，秒
        :type RemainingTime: float
        :param RegistryTaskID: 仓库镜像最近一次的漏洞任务扫描ID
        :type RegistryTaskID: int
        :param RegistryFoundVulCount: 仓库发现漏洞数量
        :type RegistryFoundVulCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LocalImageScanCount = None
        self.IgnoreVulCount = None
        self.ScanStartTime = None
        self.ScanEndTime = None
        self.FoundRiskImageCount = None
        self.FoundVulCount = None
        self.ScanProgress = None
        self.RegistryImageScanCount = None
        self.LocalTaskID = None
        self.Status = None
        self.RemainingTime = None
        self.RegistryTaskID = None
        self.RegistryFoundVulCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LocalImageScanCount = params.get("LocalImageScanCount")
        self.IgnoreVulCount = params.get("IgnoreVulCount")
        self.ScanStartTime = params.get("ScanStartTime")
        self.ScanEndTime = params.get("ScanEndTime")
        self.FoundRiskImageCount = params.get("FoundRiskImageCount")
        self.FoundVulCount = params.get("FoundVulCount")
        self.ScanProgress = params.get("ScanProgress")
        self.RegistryImageScanCount = params.get("RegistryImageScanCount")
        self.LocalTaskID = params.get("LocalTaskID")
        self.Status = params.get("Status")
        self.RemainingTime = params.get("RemainingTime")
        self.RegistryTaskID = params.get("RegistryTaskID")
        self.RegistryFoundVulCount = params.get("RegistryFoundVulCount")
        self.RequestId = params.get("RequestId")


class DescribeVulScanLocalImageListRequest(AbstractModel):
    """DescribeVulScanLocalImageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 漏洞扫描任务ID
        :type TaskID: int
        :param Filters: 过滤条件。
<li>OnlyAffectedNewestImage- Bool- 是否必填：否 - 仅展示影响最新版本镜像的漏洞</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>ScanStatus- string -是否必填: 否 - 检测状态。WAIT_SCAN：待检测，SCANNING：检查中，SCANNED：检查完成，SCAN_ERR：检查失败，CANCELED：检测停止</li>
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
        self.TaskID = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
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
        


class DescribeVulScanLocalImageListResponse(AbstractModel):
    """DescribeVulScanLocalImageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 镜像总数
        :type TotalCount: int
        :param List: 镜像列表
        :type List: list of VulScanImageInfo
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
                obj = VulScanImageInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulSummaryRequest(AbstractModel):
    """DescribeVulSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>OnlyAffectedNewestImage- string- 是否必填：否 - 仅展示影响最新版本镜像的漏洞true,false</li>
<li>OnlyAffectedContainer-string- 是否必填：否 - 仅展示影响容器的漏洞,true,false</li>
<li>CategoryType- string - 是否必填：否 - 漏洞分类: SYSTEM:系统漏洞 WEB:web应用漏洞 ALL:全部漏洞</li>
        :type Filters: list of RunTimeFilters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RunTimeFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulSummaryResponse(AbstractModel):
    """DescribeVulSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulTotalCount: 漏洞总数量
        :type VulTotalCount: int
        :param SeriousVulCount: 严重及高危漏洞数量
        :type SeriousVulCount: int
        :param SuggestVulCount: 重点关注漏洞数量
        :type SuggestVulCount: int
        :param PocExpLevelVulCount: 有Poc或者Exp的漏洞数量
        :type PocExpLevelVulCount: int
        :param RemoteExpLevelVulCount: 有远程Exp的漏洞数量
        :type RemoteExpLevelVulCount: int
        :param SeriousVulNewestImageCount: 受严重或高危漏洞影响的最新版本镜像数
        :type SeriousVulNewestImageCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulTotalCount = None
        self.SeriousVulCount = None
        self.SuggestVulCount = None
        self.PocExpLevelVulCount = None
        self.RemoteExpLevelVulCount = None
        self.SeriousVulNewestImageCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulTotalCount = params.get("VulTotalCount")
        self.SeriousVulCount = params.get("SeriousVulCount")
        self.SuggestVulCount = params.get("SuggestVulCount")
        self.PocExpLevelVulCount = params.get("PocExpLevelVulCount")
        self.RemoteExpLevelVulCount = params.get("RemoteExpLevelVulCount")
        self.SeriousVulNewestImageCount = params.get("SeriousVulNewestImageCount")
        self.RequestId = params.get("RequestId")


class DescribeVulTendencyRequest(AbstractModel):
    """DescribeVulTendency请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param SphereOfInfluence: 枚举类型：
LATEST：最新版本
CONTAINER: 运行容器
        :type SphereOfInfluence: str
        """
        self.StartTime = None
        self.EndTime = None
        self.SphereOfInfluence = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SphereOfInfluence = params.get("SphereOfInfluence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulTendencyResponse(AbstractModel):
    """DescribeVulTendency返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulTendencySet: 漏洞趋势列表
        :type VulTendencySet: list of VulTendencyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulTendencySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulTendencySet") is not None:
            self.VulTendencySet = []
            for item in params.get("VulTendencySet"):
                obj = VulTendencyInfo()
                obj._deserialize(item)
                self.VulTendencySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulTopRankingRequest(AbstractModel):
    """DescribeVulTopRanking请求参数结构体

    """

    def __init__(self):
        r"""
        :param CategoryType: 漏洞分类: SYSTEM:系统漏洞 WEB:web应用漏洞 EMERGENCY:应急漏洞
        :type CategoryType: str
        """
        self.CategoryType = None


    def _deserialize(self, params):
        self.CategoryType = params.get("CategoryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulTopRankingResponse(AbstractModel):
    """DescribeVulTopRanking返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 漏洞Top排名信息列表
        :type List: list of VulTopRankingInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = VulTopRankingInfo()
                obj._deserialize(item)
                self.List.append(obj)
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


class DescribeWebVulListRequest(AbstractModel):
    """DescribeWebVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>OnlyAffectedContainer- string - 是否必填：否 - 仅展示影响容器的漏洞true,false</li>
<li>OnlyAffectedNewestImage-string - 是否必填：否 - 仅展示影响最新版本镜像的漏洞true,false</li>
<li>Level- String - 是否必填：否 - 威胁等级，CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低</li>
<li>Tags- string - 是否必填：否 - 漏洞标签，POC，EXP。</li>
<li>CanBeFixed- string - 是否必填：否 - 是否可修复true,false。</li>
<li>CVEID- string - 是否必填：否 - CVE编号</li>
<li>ImageID- string - 是否必填：否 - 镜像ID</li>
<li>ImageName- String -是否必填: 否 - 镜像名称</li>
<li>ContainerID- string -是否必填: 否 - 容器ID</li>
<li>ContainerName- string -是否必填: 否 - 容器名称</li>
<li>ComponentName- string -是否必填: 否 - 组件名称</li>
<li>ComponentVersion- string -是否必填: 否 - 组件版本</li>
<li>Name- string -是否必填: 否 - 漏洞名称</li>
<li>FocusOnType - string - 是否必填：否 -关注紧急度类型 。ALL :全部，SERIOUS_LEVEL： 严重和高危 ，IS_SUGGEST： 重点关注，POC_EXP 有Poc或Exp ，NETWORK_EXP: 远程Exp</li>
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
        


class DescribeWebVulListResponse(AbstractModel):
    """DescribeWebVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 漏洞总数
        :type TotalCount: int
        :param List: 漏洞列表
        :type List: list of VulInfo
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
                obj = VulInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class EmergencyVulInfo(AbstractModel):
    """应急漏洞列表信息

    """

    def __init__(self):
        r"""
        :param Name: 漏洞名称
        :type Name: str
        :param Tags: 漏洞标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param CVSSV3Score: CVSS V3分数
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSV3Score: float
        :param Level: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param CVEID: CVE编号
        :type CVEID: str
        :param Category: 漏洞类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param SubmitTime: 漏洞披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitTime: str
        :param LatestFoundTime: 最近发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestFoundTime: str
        :param Status: 应急漏洞风险情况：NOT_SCAN：未扫描，SCANNING：扫描中，SCANNED_NOT_RISK：已扫描，暂未风险 ，SCANNED_RISK：已扫描存在风险
        :type Status: str
        :param ID: 漏洞ID
        :type ID: int
        :param PocID: 漏洞PocID
        :type PocID: str
        :param DefenceStatus: 防御状态，NO_DEFENDED:未防御，DEFENDED:已防御
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceStatus: str
        :param DefenceScope: 漏洞防御主机范围: MANUAL:自选主机节点，ALL:全部
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceScope: str
        :param DefenceHostCount: 漏洞防御主机数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceHostCount: int
        :param DefendedCount: 已防御攻击次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DefendedCount: int
        """
        self.Name = None
        self.Tags = None
        self.CVSSV3Score = None
        self.Level = None
        self.CVEID = None
        self.Category = None
        self.SubmitTime = None
        self.LatestFoundTime = None
        self.Status = None
        self.ID = None
        self.PocID = None
        self.DefenceStatus = None
        self.DefenceScope = None
        self.DefenceHostCount = None
        self.DefendedCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Tags = params.get("Tags")
        self.CVSSV3Score = params.get("CVSSV3Score")
        self.Level = params.get("Level")
        self.CVEID = params.get("CVEID")
        self.Category = params.get("Category")
        self.SubmitTime = params.get("SubmitTime")
        self.LatestFoundTime = params.get("LatestFoundTime")
        self.Status = params.get("Status")
        self.ID = params.get("ID")
        self.PocID = params.get("PocID")
        self.DefenceStatus = params.get("DefenceStatus")
        self.DefenceScope = params.get("DefenceScope")
        self.DefenceHostCount = params.get("DefenceHostCount")
        self.DefendedCount = params.get("DefendedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param OperationTime: 事件最后一次处理的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationTime: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.OperationTime = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        self.OperationTime = params.get("OperationTime")
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
        :param Status: 状态，EVENT_UNDEAL:未处理，EVENT_DEALED:已处理，EVENT_INGNORE:忽略
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
        :param NodeIP: 节点IP
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeIP: str
        :param HostID: 主机IP
注意：此字段可能返回 null，表示取不到有效值。
        :type HostID: str
        :param ContainerNetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
"NODE_DESTROYED"      //节点已销毁
"CONTAINER_EXITED"    //容器已退出
"CONTAINER_DESTROYED" //容器已销毁
"SHARED_HOST"         // 容器与主机共享网络
"RESOURCE_LIMIT"      //隔离操作资源超限
"UNKNOW"              // 原因未知
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerIsolateOperationSrc: str
        :param ContainerStatus: 容器状态
正在运行: RUNNING
暂停: PAUSED
停止: STOPPED
已经创建: CREATED
已经销毁: DESTROYED
正在重启中: RESTARTING
迁移中: REMOVING
        :type ContainerStatus: str
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
        self.NodeIP = None
        self.HostID = None
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.ContainerStatus = None


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
        self.NodeIP = params.get("NodeIP")
        self.HostID = params.get("HostID")
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.ContainerStatus = params.get("ContainerStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EscapeEventTendencyInfo(AbstractModel):
    """待处理逃逸事件趋势

    """

    def __init__(self):
        r"""
        :param RiskContainerEventCount: 待处理风险容器事件总数
        :type RiskContainerEventCount: int
        :param ProcessPrivilegeEventCount: 待处理程序特权事件总数
        :type ProcessPrivilegeEventCount: int
        :param ContainerEscapeEventCount: 待处理容器逃逸事件总数
        :type ContainerEscapeEventCount: int
        :param Date: 日期
        :type Date: str
        """
        self.RiskContainerEventCount = None
        self.ProcessPrivilegeEventCount = None
        self.ContainerEscapeEventCount = None
        self.Date = None


    def _deserialize(self, params):
        self.RiskContainerEventCount = params.get("RiskContainerEventCount")
        self.ProcessPrivilegeEventCount = params.get("ProcessPrivilegeEventCount")
        self.ContainerEscapeEventCount = params.get("ContainerEscapeEventCount")
        self.Date = params.get("Date")
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
        :param Group: 规则组别。RISK_CONTAINER：风险容器，PROCESS_PRIVILEGE：程序特权，CONTAINER_ESCAPE：容器逃逸
        :type Group: str
        """
        self.Type = None
        self.Name = None
        self.IsEnable = None
        self.Group = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.IsEnable = params.get("IsEnable")
        self.Group = params.get("Group")
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
        


class EscapeWhiteListInfo(AbstractModel):
    """逃逸白名单

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ID: 白名单记录ID
        :type ID: int
        :param HostCount: 关联主机数量
        :type HostCount: int
        :param ContainerCount: 关联容器数量
        :type ContainerCount: int
        :param EventType: 加白事件类型
        :type EventType: list of str
        :param InsertTime: 创建时间
        :type InsertTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ImageSize: 镜像大小
        :type ImageSize: int
        """
        self.ImageID = None
        self.ImageName = None
        self.ID = None
        self.HostCount = None
        self.ContainerCount = None
        self.EventType = None
        self.InsertTime = None
        self.UpdateTime = None
        self.ImageSize = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.ID = params.get("ID")
        self.HostCount = params.get("HostCount")
        self.ContainerCount = params.get("ContainerCount")
        self.EventType = params.get("EventType")
        self.InsertTime = params.get("InsertTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ImageSize = params.get("ImageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportJobInfo(AbstractModel):
    """导出任务详情

    """

    def __init__(self):
        r"""
        :param JobID: 任务ID
        :type JobID: str
        :param JobName: 任务名称
        :type JobName: str
        :param Source: 来源
        :type Source: str
        :param ExportStatus: 导出状态
        :type ExportStatus: str
        :param ExportProgress: 导出进度
        :type ExportProgress: int
        :param FailureMsg: 失败原因
        :type FailureMsg: str
        :param Timeout: 超时时间
        :type Timeout: str
        :param InsertTime: 插入时间
        :type InsertTime: str
        """
        self.JobID = None
        self.JobName = None
        self.Source = None
        self.ExportStatus = None
        self.ExportProgress = None
        self.FailureMsg = None
        self.Timeout = None
        self.InsertTime = None


    def _deserialize(self, params):
        self.JobID = params.get("JobID")
        self.JobName = params.get("JobName")
        self.Source = params.get("Source")
        self.ExportStatus = params.get("ExportStatus")
        self.ExportProgress = params.get("ExportProgress")
        self.FailureMsg = params.get("FailureMsg")
        self.Timeout = params.get("Timeout")
        self.InsertTime = params.get("InsertTime")
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
<li>IsRealTime- int - 是否必填：否 - 过滤是否实时监控数据</li>
<li>TaskId- string - 是否必填：否 - 任务ID</li>
<li>TimeRange - string -是否必填: 否 - 时间范围筛选 ["2022-03-31 16:55:00", "2022-03-31 17:00:00"]</li>
<li>ContainerNetStatus - String -是否必填: 否 -  容器网络状态筛选 NORMAL ISOLATED ISOLATING RESTORING RESTORE_FAILED</li>
<li>ContainerStatus - string -是否必填: 否 - 容器状态 RUNNING PAUSED STOPPED CREATED DESTROYED RESTARTING REMOVING</li>
<li>AutoIsolateMode - string -是否必填: 否 - 隔离方式 MANUAL AUTO</li>
<li>MD5 - string -是否必填: 否 - md5 </li>
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
        :param NewFile: 新文件内容
        :type NewFile: str
        :param FileDiff: 新旧文件的差异
        :type FileDiff: str
        """
        self.FileName = None
        self.FileType = None
        self.FileSize = None
        self.FilePath = None
        self.FileCreateTime = None
        self.LatestTamperedFileMTime = None
        self.NewFile = None
        self.FileDiff = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileSize = params.get("FileSize")
        self.FilePath = params.get("FilePath")
        self.FileCreateTime = params.get("FileCreateTime")
        self.LatestTamperedFileMTime = params.get("LatestTamperedFileMTime")
        self.NewFile = params.get("NewFile")
        self.FileDiff = params.get("FileDiff")
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
        :param Project: 所属项目
注意：此字段可能返回 null，表示取不到有效值。
        :type Project: :class:`tencentcloud.tcss.v20201101.models.ProjectInfo`
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
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
        self.Project = None
        self.Tags = None


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
        if params.get("Project") is not None:
            self.Project = ProjectInfo()
            self.Project._deserialize(params.get("Project"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageAutoAuthorizedTask(AbstractModel):
    """镜像自动授权任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: int
        :param Type: 授权方式，AUTO:自动授权，MANUAL:手动授权
        :type Type: str
        :param AuthorizedDate: 任务日期
        :type AuthorizedDate: str
        :param Source: 镜像来源，LOCAL:本地镜像，REGISTRY:仓库镜像
        :type Source: str
        :param LastAuthorizedTime: 最近授权时间
        :type LastAuthorizedTime: str
        :param SuccessCount: 自动授权成功数
        :type SuccessCount: int
        :param FailCount: 自动授权失败数
        :type FailCount: int
        :param LatestFailCode: 最近任务失败码，REACH_LIMIT:达到授权上限，LICENSE_INSUFFICIENT:授权数不足
        :type LatestFailCode: str
        """
        self.TaskId = None
        self.Type = None
        self.AuthorizedDate = None
        self.Source = None
        self.LastAuthorizedTime = None
        self.SuccessCount = None
        self.FailCount = None
        self.LatestFailCode = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Type = params.get("Type")
        self.AuthorizedDate = params.get("AuthorizedDate")
        self.Source = params.get("Source")
        self.LastAuthorizedTime = params.get("LastAuthorizedTime")
        self.SuccessCount = params.get("SuccessCount")
        self.FailCount = params.get("FailCount")
        self.LatestFailCode = params.get("LatestFailCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageComponent(AbstractModel):
    """容器安全镜像组件信息

    """

    def __init__(self):
        r"""
        :param Name: 组件名称
        :type Name: str
        :param Version: 组件版本
        :type Version: str
        :param Path: 组件路径
        :type Path: str
        :param Type: 组件类型
        :type Type: str
        :param VulCount: 组件漏洞数量
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCount: int
        :param ImageID: 镜像ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageID: str
        """
        self.Name = None
        self.Version = None
        self.Path = None
        self.Type = None
        self.VulCount = None
        self.ImageID = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Path = params.get("Path")
        self.Type = params.get("Type")
        self.VulCount = params.get("VulCount")
        self.ImageID = params.get("ImageID")
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
        :param CheckPlatform: 检测平台
1: 云查杀引擎
2: tav
3: binaryAi
4: 异常行为
5: 威胁情报
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPlatform: list of str
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
        self.CheckPlatform = None


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
        self.CheckPlatform = params.get("CheckPlatform")
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
        :param ComponentCnt: 组件个数
        :type ComponentCnt: int
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
        self.ComponentCnt = None


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
        self.ComponentCnt = params.get("ComponentCnt")
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


class K8sApiAbnormalEventInfo(AbstractModel):
    """k8sApi异常事件详情

    """

    def __init__(self):
        r"""
        :param MatchRuleName: 命中规则名称
        :type MatchRuleName: str
        :param MatchRuleType: 命中规则类型
        :type MatchRuleType: str
        :param RiskLevel: 告警等级
        :type RiskLevel: str
        :param ClusterID: 集群ID
        :type ClusterID: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterRunningStatus: 集群运行状态
        :type ClusterRunningStatus: str
        :param FirstCreateTime: 初次生成时间
        :type FirstCreateTime: str
        :param LastCreateTime: 最近一次生成时间
        :type LastCreateTime: str
        :param AlarmCount: 告警数量
        :type AlarmCount: int
        :param Status: 状态
"EVENT_UNDEAL":未处理
"EVENT_DEALED": 已处理
"EVENT_IGNORE": 忽略
"EVENT_DEL": 删除
"EVENT_ADD_WHITE": 加白
        :type Status: str
        :param ClusterMasterIP: 集群masterIP
        :type ClusterMasterIP: str
        :param K8sVersion: k8s版本
        :type K8sVersion: str
        :param RunningComponent: 运行时组件
        :type RunningComponent: list of str
        :param Desc: 描述
        :type Desc: str
        :param Suggestion: 建议
        :type Suggestion: str
        :param Info: 请求信息
        :type Info: str
        :param MatchRuleID: 规则ID
        :type MatchRuleID: str
        :param HighLightFields: 高亮字段数组
        :type HighLightFields: list of str
        :param MatchRule: 命中规则
        :type MatchRule: :class:`tencentcloud.tcss.v20201101.models.K8sApiAbnormalRuleScopeInfo`
        """
        self.MatchRuleName = None
        self.MatchRuleType = None
        self.RiskLevel = None
        self.ClusterID = None
        self.ClusterName = None
        self.ClusterRunningStatus = None
        self.FirstCreateTime = None
        self.LastCreateTime = None
        self.AlarmCount = None
        self.Status = None
        self.ClusterMasterIP = None
        self.K8sVersion = None
        self.RunningComponent = None
        self.Desc = None
        self.Suggestion = None
        self.Info = None
        self.MatchRuleID = None
        self.HighLightFields = None
        self.MatchRule = None


    def _deserialize(self, params):
        self.MatchRuleName = params.get("MatchRuleName")
        self.MatchRuleType = params.get("MatchRuleType")
        self.RiskLevel = params.get("RiskLevel")
        self.ClusterID = params.get("ClusterID")
        self.ClusterName = params.get("ClusterName")
        self.ClusterRunningStatus = params.get("ClusterRunningStatus")
        self.FirstCreateTime = params.get("FirstCreateTime")
        self.LastCreateTime = params.get("LastCreateTime")
        self.AlarmCount = params.get("AlarmCount")
        self.Status = params.get("Status")
        self.ClusterMasterIP = params.get("ClusterMasterIP")
        self.K8sVersion = params.get("K8sVersion")
        self.RunningComponent = params.get("RunningComponent")
        self.Desc = params.get("Desc")
        self.Suggestion = params.get("Suggestion")
        self.Info = params.get("Info")
        self.MatchRuleID = params.get("MatchRuleID")
        self.HighLightFields = params.get("HighLightFields")
        if params.get("MatchRule") is not None:
            self.MatchRule = K8sApiAbnormalRuleScopeInfo()
            self.MatchRule._deserialize(params.get("MatchRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sApiAbnormalEventListItem(AbstractModel):
    """k8sapi异常事件列表Item

    """

    def __init__(self):
        r"""
        :param ID: 事件ID
        :type ID: int
        :param MatchRuleType: 命中规则类型
        :type MatchRuleType: str
        :param RiskLevel: 威胁等级
        :type RiskLevel: str
        :param ClusterID: 集群ID
        :type ClusterID: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterRunningStatus: 集群运行状态
        :type ClusterRunningStatus: str
        :param FirstCreateTime: 初次生成时间
        :type FirstCreateTime: str
        :param LastCreateTime: 最近一次生成时间
        :type LastCreateTime: str
        :param AlarmCount: 告警数量
        :type AlarmCount: int
        :param Status: 状态
        :type Status: str
        :param RuleType: 规则类型
        :type RuleType: str
        :param Desc: 描述信息
        :type Desc: str
        :param Suggestion: 解决方案
        :type Suggestion: str
        :param RuleName: 规则名称
        :type RuleName: str
        :param MatchRule: 命中规则
        :type MatchRule: :class:`tencentcloud.tcss.v20201101.models.K8sApiAbnormalRuleScopeInfo`
        """
        self.ID = None
        self.MatchRuleType = None
        self.RiskLevel = None
        self.ClusterID = None
        self.ClusterName = None
        self.ClusterRunningStatus = None
        self.FirstCreateTime = None
        self.LastCreateTime = None
        self.AlarmCount = None
        self.Status = None
        self.RuleType = None
        self.Desc = None
        self.Suggestion = None
        self.RuleName = None
        self.MatchRule = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.MatchRuleType = params.get("MatchRuleType")
        self.RiskLevel = params.get("RiskLevel")
        self.ClusterID = params.get("ClusterID")
        self.ClusterName = params.get("ClusterName")
        self.ClusterRunningStatus = params.get("ClusterRunningStatus")
        self.FirstCreateTime = params.get("FirstCreateTime")
        self.LastCreateTime = params.get("LastCreateTime")
        self.AlarmCount = params.get("AlarmCount")
        self.Status = params.get("Status")
        self.RuleType = params.get("RuleType")
        self.Desc = params.get("Desc")
        self.Suggestion = params.get("Suggestion")
        self.RuleName = params.get("RuleName")
        if params.get("MatchRule") is not None:
            self.MatchRule = K8sApiAbnormalRuleScopeInfo()
            self.MatchRule._deserialize(params.get("MatchRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sApiAbnormalRuleInfo(AbstractModel):
    """k8a api 异常请求规则详情

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称
        :type RuleName: str
        :param Status: 状态
        :type Status: bool
        :param RuleInfoList: 规则信息列表
        :type RuleInfoList: list of K8sApiAbnormalRuleScopeInfo
        :param EffectClusterIDSet: 生效集群IDSet
        :type EffectClusterIDSet: list of str
        :param RuleType: 规则类型
RT_SYSTEM 系统规则
RT_USER 用户自定义
        :type RuleType: str
        :param EffectAllCluster: 是否所有集群生效
        :type EffectAllCluster: bool
        :param RuleID: 规则ID
        :type RuleID: str
        """
        self.RuleName = None
        self.Status = None
        self.RuleInfoList = None
        self.EffectClusterIDSet = None
        self.RuleType = None
        self.EffectAllCluster = None
        self.RuleID = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("RuleInfoList") is not None:
            self.RuleInfoList = []
            for item in params.get("RuleInfoList"):
                obj = K8sApiAbnormalRuleScopeInfo()
                obj._deserialize(item)
                self.RuleInfoList.append(obj)
        self.EffectClusterIDSet = params.get("EffectClusterIDSet")
        self.RuleType = params.get("RuleType")
        self.EffectAllCluster = params.get("EffectAllCluster")
        self.RuleID = params.get("RuleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sApiAbnormalRuleListItem(AbstractModel):
    """k8s api 异常请求规则列表Item

    """

    def __init__(self):
        r"""
        :param RuleID: 规则ID
        :type RuleID: str
        :param RuleName: 规则名称
        :type RuleName: str
        :param RuleType: 规则类型
RT_SYSTEM 系统规则
RT_USER 用户自定义
        :type RuleType: str
        :param EffectClusterCount: 受影响集群总数
        :type EffectClusterCount: int
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param OprUin: 编辑账号
        :type OprUin: str
        :param Status: 状态
        :type Status: bool
        """
        self.RuleID = None
        self.RuleName = None
        self.RuleType = None
        self.EffectClusterCount = None
        self.UpdateTime = None
        self.OprUin = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.RuleName = params.get("RuleName")
        self.RuleType = params.get("RuleType")
        self.EffectClusterCount = params.get("EffectClusterCount")
        self.UpdateTime = params.get("UpdateTime")
        self.OprUin = params.get("OprUin")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sApiAbnormalRuleScopeInfo(AbstractModel):
    """k8s api 异常事件规则配置范围

    """

    def __init__(self):
        r"""
        :param Scope: 范围
系统事件:
ANONYMOUS_ACCESS: 匿名访问
ABNORMAL_UA_REQ: 异常UA请求
ANONYMOUS_ABNORMAL_PERMISSION: 匿名用户权限异动
GET_CREDENTIALS: 凭据信息获取
MOUNT_SENSITIVE_PATH: 敏感路径挂载
COMMAND_RUN: 命令执行
PRIVILEGE_CONTAINER: 特权容器
EXCEPTION_CRONTAB_TASK: 异常定时任务
STATICS_POD: 静态pod创建
ABNORMAL_CREATE_POD: 异常pod创建
USER_DEFINED: 用户自定义
        :type Scope: str
        :param Action: 动作(RULE_MODE_ALERT: 告警 RULE_MODE_RELEASE:放行)
        :type Action: str
        :param RiskLevel: 威胁等级 HIGH:高级 MIDDLE: 中级 LOW:低级 NOTICE:提示
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param Status: 开关状态(true:开 false:关) 适用于系统规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        :param IsDelete: 是否被删除 适用于自定义规则入参
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDelete: bool
        """
        self.Scope = None
        self.Action = None
        self.RiskLevel = None
        self.Status = None
        self.IsDelete = None


    def _deserialize(self, params):
        self.Scope = params.get("Scope")
        self.Action = params.get("Action")
        self.RiskLevel = params.get("RiskLevel")
        self.Status = params.get("Status")
        self.IsDelete = params.get("IsDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sApiAbnormalTendencyItem(AbstractModel):
    """k8sapi异常请求趋势Item

    """

    def __init__(self):
        r"""
        :param Date: 日期
        :type Date: str
        :param ExceptionUARequestCount: 异常UA请求事件数
        :type ExceptionUARequestCount: int
        :param AnonymousUserRightCount: 匿名用户权限事件数
        :type AnonymousUserRightCount: int
        :param CredentialInformationObtainCount: 凭据信息获取事件数
        :type CredentialInformationObtainCount: int
        :param SensitiveDataMountCount: 敏感数据挂载事件数
        :type SensitiveDataMountCount: int
        :param CmdExecCount: 命令执行事件数
        :type CmdExecCount: int
        :param AbnormalScheduledTaskCount: 异常定时任务事件数
        :type AbnormalScheduledTaskCount: int
        :param StaticsPodCreateCount: 静态Pod创建数
        :type StaticsPodCreateCount: int
        :param DoubtfulContainerCreateCount: 可疑容器创建数
        :type DoubtfulContainerCreateCount: int
        :param UserDefinedRuleCount: 自定义规则事件数
        :type UserDefinedRuleCount: int
        :param AnonymousAccessCount: 匿名访问事件数
        :type AnonymousAccessCount: int
        :param PrivilegeContainerCount: 特权容器事件数
        :type PrivilegeContainerCount: int
        """
        self.Date = None
        self.ExceptionUARequestCount = None
        self.AnonymousUserRightCount = None
        self.CredentialInformationObtainCount = None
        self.SensitiveDataMountCount = None
        self.CmdExecCount = None
        self.AbnormalScheduledTaskCount = None
        self.StaticsPodCreateCount = None
        self.DoubtfulContainerCreateCount = None
        self.UserDefinedRuleCount = None
        self.AnonymousAccessCount = None
        self.PrivilegeContainerCount = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.ExceptionUARequestCount = params.get("ExceptionUARequestCount")
        self.AnonymousUserRightCount = params.get("AnonymousUserRightCount")
        self.CredentialInformationObtainCount = params.get("CredentialInformationObtainCount")
        self.SensitiveDataMountCount = params.get("SensitiveDataMountCount")
        self.CmdExecCount = params.get("CmdExecCount")
        self.AbnormalScheduledTaskCount = params.get("AbnormalScheduledTaskCount")
        self.StaticsPodCreateCount = params.get("StaticsPodCreateCount")
        self.DoubtfulContainerCreateCount = params.get("DoubtfulContainerCreateCount")
        self.UserDefinedRuleCount = params.get("UserDefinedRuleCount")
        self.AnonymousAccessCount = params.get("AnonymousAccessCount")
        self.PrivilegeContainerCount = params.get("PrivilegeContainerCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param TaskID: 任务id；任务id，镜像id和根据过滤条件筛选三选一。
        :type TaskID: str
        :param Images: 镜像id；任务id，镜像id和根据过滤条件筛选三选一。
        :type Images: list of str
        :param Filters: 根据过滤条件筛选出镜像；任务id，镜像id和根据过滤条件筛选三选一。
        :type Filters: list of AssetFilters
        :param ExcludeImageIds: 根据过滤条件筛选出镜像，再排除个别镜像
        :type ExcludeImageIds: str
        """
        self.TaskID = None
        self.Images = None
        self.Filters = None
        self.ExcludeImageIds = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.Images = params.get("Images")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ExcludeImageIds = params.get("ExcludeImageIds")
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


class ModifyContainerNetStatusRequest(AbstractModel):
    """ModifyContainerNetStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerID: 容器ID
        :type ContainerID: str
        :param Status: 状态(
隔离容器: EVENT_ISOLATE_CONTAINER
恢复容器: EVENT_RESOTRE_CONTAINER
)
        :type Status: str
        """
        self.ContainerID = None
        self.Status = None


    def _deserialize(self, params):
        self.ContainerID = params.get("ContainerID")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyContainerNetStatusResponse(AbstractModel):
    """ModifyContainerNetStatus返回参数结构体

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
        :param Status: 标记事件的状态：
EVENT_UNDEAL:未处理（取消忽略），
EVENT_DEALED:已处理，
EVENT_IGNORE:忽略，
EVENT_DELETE：已删除
EVENT_ADD_WHITE：加白
        :type Status: str
        :param Remark: 备注
        :type Remark: str
        :param ImageIDs: 加白镜像ID数组
        :type ImageIDs: list of str
        :param EventType: 加白事件类型
   ESCAPE_CGROUPS：利用cgroup机制逃逸
   ESCAPE_TAMPER_SENSITIVE_FILE：篡改敏感文件逃逸
   ESCAPE_DOCKER_API：访问Docker API接口逃逸
   ESCAPE_VUL_OCCURRED：逃逸漏洞利用
   MOUNT_SENSITIVE_PTAH：敏感路径挂载
   PRIVILEGE_CONTAINER_START：特权容器
   PRIVILEGE：程序提权逃逸
        :type EventType: list of str
        """
        self.EventIdSet = None
        self.Status = None
        self.Remark = None
        self.ImageIDs = None
        self.EventType = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.ImageIDs = params.get("ImageIDs")
        self.EventType = params.get("EventType")
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


class ModifyEscapeWhiteListRequest(AbstractModel):
    """ModifyEscapeWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventType: 加白名单事件类型
   ESCAPE_CGROUPS：利用cgroup机制逃逸
   ESCAPE_TAMPER_SENSITIVE_FILE：篡改敏感文件逃逸
   ESCAPE_DOCKER_API：访问Docker API接口逃逸
   ESCAPE_VUL_OCCURRED：逃逸漏洞利用
   MOUNT_SENSITIVE_PTAH：敏感路径挂载
   PRIVILEGE_CONTAINER_START：特权容器
   PRIVILEGE：程序提权逃逸
        :type EventType: list of str
        :param IDSet: 白名单记录ID
        :type IDSet: list of int
        """
        self.EventType = None
        self.IDSet = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        self.IDSet = params.get("IDSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEscapeWhiteListResponse(AbstractModel):
    """ModifyEscapeWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIgnoreVul(AbstractModel):
    """漏洞扫描新增和取消忽略漏洞入参

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param ImageIDs: 忽略的镜像ID，空表示全部
        :type ImageIDs: list of str
        :param ImageType: 当有镜像时
镜像类型: LOCAL 本地镜像 REGISTRY 仓库镜像
        :type ImageType: str
        """
        self.PocID = None
        self.ImageIDs = None
        self.ImageType = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
        self.ImageIDs = params.get("ImageIDs")
        self.ImageType = params.get("ImageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAuthorizedRequest(AbstractModel):
    """ModifyImageAuthorized请求参数结构体

    """

    def __init__(self):
        r"""
        :param AllLocalImages: 本地镜像是否全部授权的标识，优先权高于根据本地镜像ids授权。等于true时需UpdatedLocalImageCnt大于0。
        :type AllLocalImages: bool
        :param AllRegistryImages: 仓库镜像是否全部授权的标识，优先权高于根据镜像ids授权。等于true时需UpdatedRegistryImageCnt大于0。
        :type AllRegistryImages: bool
        :param UpdatedLocalImageCnt: 指定操作授权的本地镜像数量，判断优先权最高，实际多出的镜像随机忽略，实际不足的部分也忽略。
        :type UpdatedLocalImageCnt: int
        :param UpdatedRegistryImageCnt: 指定操作授权的仓库镜像数量，判断优先权最高，实际多出的镜像随机忽略，实际不足的部分也忽略；
        :type UpdatedRegistryImageCnt: int
        :param ImageSourceType: 根据满足条件的本地镜像授权,本地镜像来源；ASSETIMAGE:本地镜像列表；IMAGEALL:同步本地镜像；AllLocalImages为false且LocalImageIds为空和UpdatedLocalImageCnt大于0时，需要
        :type ImageSourceType: str
        :param LocalImageFilter: 根据满足条件的本地镜像授权，AllLocalImages为false且LocalImageIds为空和UpdatedLocalImageCnt大于0时，需要。
        :type LocalImageFilter: list of AssetFilters
        :param RegistryImageFilter: 根据满足条件的仓库镜像授权，AllRegistryImages为false且RegistryImageIds为空和UpdatedRegistryImageCnt大于0时，需要。
        :type RegistryImageFilter: list of AssetFilters
        :param ExcludeLocalImageIds: 根据满足条件的镜像授权,同时排除的本地镜像。
        :type ExcludeLocalImageIds: list of str
        :param ExcludeRegistryImageIds: 根据满足条件的镜像授权,同时排除的仓库镜像。
        :type ExcludeRegistryImageIds: list of str
        :param LocalImageIds: 根据本地镜像ids授权，优先权高于根据满足条件的镜像授权。AllLocalImages为false且LocalImageFilter为空和UpdatedLocalImageCnt大于0时，需要。
        :type LocalImageIds: list of str
        :param RegistryImageIds: 根据仓库镜像Ids授权，优先权高于根据满足条件的镜像授。AllRegistryImages为false且RegistryImageFilter为空和UpdatedRegistryImageCnt大于0时，需要。
        :type RegistryImageIds: list of str
        :param OnlyShowLatest: 是否仅最新的镜像；RegistryImageFilter不为空且UpdatedRegistryImageCnt大于0时仓库镜像需要。
        :type OnlyShowLatest: bool
        """
        self.AllLocalImages = None
        self.AllRegistryImages = None
        self.UpdatedLocalImageCnt = None
        self.UpdatedRegistryImageCnt = None
        self.ImageSourceType = None
        self.LocalImageFilter = None
        self.RegistryImageFilter = None
        self.ExcludeLocalImageIds = None
        self.ExcludeRegistryImageIds = None
        self.LocalImageIds = None
        self.RegistryImageIds = None
        self.OnlyShowLatest = None


    def _deserialize(self, params):
        self.AllLocalImages = params.get("AllLocalImages")
        self.AllRegistryImages = params.get("AllRegistryImages")
        self.UpdatedLocalImageCnt = params.get("UpdatedLocalImageCnt")
        self.UpdatedRegistryImageCnt = params.get("UpdatedRegistryImageCnt")
        self.ImageSourceType = params.get("ImageSourceType")
        if params.get("LocalImageFilter") is not None:
            self.LocalImageFilter = []
            for item in params.get("LocalImageFilter"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.LocalImageFilter.append(obj)
        if params.get("RegistryImageFilter") is not None:
            self.RegistryImageFilter = []
            for item in params.get("RegistryImageFilter"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.RegistryImageFilter.append(obj)
        self.ExcludeLocalImageIds = params.get("ExcludeLocalImageIds")
        self.ExcludeRegistryImageIds = params.get("ExcludeRegistryImageIds")
        self.LocalImageIds = params.get("LocalImageIds")
        self.RegistryImageIds = params.get("RegistryImageIds")
        self.OnlyShowLatest = params.get("OnlyShowLatest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAuthorizedResponse(AbstractModel):
    """ModifyImageAuthorized返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyK8sApiAbnormalEventStatusRequest(AbstractModel):
    """ModifyK8sApiAbnormalEventStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIDSet: 事件ID集合
        :type EventIDSet: list of int non-negative
        :param Status: 状态
        :type Status: str
        :param Remark: 备注
        :type Remark: str
        """
        self.EventIDSet = None
        self.Status = None
        self.Remark = None


    def _deserialize(self, params):
        self.EventIDSet = params.get("EventIDSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyK8sApiAbnormalEventStatusResponse(AbstractModel):
    """ModifyK8sApiAbnormalEventStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyK8sApiAbnormalRuleInfoRequest(AbstractModel):
    """ModifyK8sApiAbnormalRuleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleInfo: 规则详情
        :type RuleInfo: :class:`tencentcloud.tcss.v20201101.models.K8sApiAbnormalRuleInfo`
        """
        self.RuleInfo = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = K8sApiAbnormalRuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyK8sApiAbnormalRuleInfoResponse(AbstractModel):
    """ModifyK8sApiAbnormalRuleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyK8sApiAbnormalRuleStatusRequest(AbstractModel):
    """ModifyK8sApiAbnormalRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleID: 规则ID
        :type RuleID: str
        :param Status: 状态(true:开 false:关)
        :type Status: bool
        """
        self.RuleID = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyK8sApiAbnormalRuleStatusResponse(AbstractModel):
    """ModifyK8sApiAbnormalRuleStatus返回参数结构体

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


class ModifySecLogCleanSettingInfoRequest(AbstractModel):
    """ModifySecLogCleanSettingInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReservesLimit: 触发清理的储量底线(50-99)
        :type ReservesLimit: int
        :param ReservesDeadline: 清理停止时的储量截至线(>0,小于ReservesLimit)
        :type ReservesDeadline: int
        :param DayLimit: 触发清理的存储天数(>=1)
        :type DayLimit: int
        """
        self.ReservesLimit = None
        self.ReservesDeadline = None
        self.DayLimit = None


    def _deserialize(self, params):
        self.ReservesLimit = params.get("ReservesLimit")
        self.ReservesDeadline = params.get("ReservesDeadline")
        self.DayLimit = params.get("DayLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecLogCleanSettingInfoResponse(AbstractModel):
    """ModifySecLogCleanSettingInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecLogDeliveryClsSettingRequest(AbstractModel):
    """ModifySecLogDeliveryClsSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param List: 日志信息
        :type List: list of SecLogDeliveryClsSettingInfo
        """
        self.List = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SecLogDeliveryClsSettingInfo()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecLogDeliveryClsSettingResponse(AbstractModel):
    """ModifySecLogDeliveryClsSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecLogDeliveryKafkaSettingRequest(AbstractModel):
    """ModifySecLogDeliveryKafkaSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceID: 实例ID
        :type InstanceID: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Domain: 域名
        :type Domain: str
        :param User: 用户名
        :type User: str
        :param Password: 密码
        :type Password: str
        :param LogTypeList: 日志类型队列
        :type LogTypeList: list of SecLogDeliveryKafkaSettingInfo
        :param AccessType: 接入类型
        :type AccessType: int
        :param KafkaVersion: kafka版本号
        :type KafkaVersion: str
        :param RegionID: 地域ID
        :type RegionID: str
        """
        self.InstanceID = None
        self.InstanceName = None
        self.Domain = None
        self.User = None
        self.Password = None
        self.LogTypeList = None
        self.AccessType = None
        self.KafkaVersion = None
        self.RegionID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.InstanceName = params.get("InstanceName")
        self.Domain = params.get("Domain")
        self.User = params.get("User")
        self.Password = params.get("Password")
        if params.get("LogTypeList") is not None:
            self.LogTypeList = []
            for item in params.get("LogTypeList"):
                obj = SecLogDeliveryKafkaSettingInfo()
                obj._deserialize(item)
                self.LogTypeList.append(obj)
        self.AccessType = params.get("AccessType")
        self.KafkaVersion = params.get("KafkaVersion")
        self.RegionID = params.get("RegionID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecLogDeliveryKafkaSettingResponse(AbstractModel):
    """ModifySecLogDeliveryKafkaSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecLogJoinObjectsRequest(AbstractModel):
    """ModifySecLogJoinObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogType: 日志类型
bash日志: container_bash
容器启动: container_launch
k8sApi: k8s_api
        :type LogType: str
        :param BindList: 绑定主机quuid列表
        :type BindList: list of str
        :param UnBindList: 待解绑主机quuid列表
        :type UnBindList: list of str
        """
        self.LogType = None
        self.BindList = None
        self.UnBindList = None


    def _deserialize(self, params):
        self.LogType = params.get("LogType")
        self.BindList = params.get("BindList")
        self.UnBindList = params.get("UnBindList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecLogJoinObjectsResponse(AbstractModel):
    """ModifySecLogJoinObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecLogJoinStateRequest(AbstractModel):
    """ModifySecLogJoinState请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogType: 日志类型
bash日志: container_bash
容器启动: container_launch
k8sApi: k8s_api
        :type LogType: str
        :param State: 状态(true:开 false:关)
        :type State: bool
        """
        self.LogType = None
        self.State = None


    def _deserialize(self, params):
        self.LogType = params.get("LogType")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecLogJoinStateResponse(AbstractModel):
    """ModifySecLogJoinState返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecLogKafkaUINRequest(AbstractModel):
    """ModifySecLogKafkaUIN请求参数结构体

    """

    def __init__(self):
        r"""
        :param DstUIN: 目标UIN
        :type DstUIN: str
        """
        self.DstUIN = None


    def _deserialize(self, params):
        self.DstUIN = params.get("DstUIN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecLogKafkaUINResponse(AbstractModel):
    """ModifySecLogKafkaUIN返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVirusAutoIsolateExampleSwitchRequest(AbstractModel):
    """ModifyVirusAutoIsolateExampleSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param MD5: 文件Md5值
        :type MD5: str
        :param Status: 开关(开:true 关: false)
        :type Status: bool
        """
        self.MD5 = None
        self.Status = None


    def _deserialize(self, params):
        self.MD5 = params.get("MD5")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirusAutoIsolateExampleSwitchResponse(AbstractModel):
    """ModifyVirusAutoIsolateExampleSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVirusAutoIsolateSettingRequest(AbstractModel):
    """ModifyVirusAutoIsolateSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param AutoIsolateSwitch: 自动隔离开关(true:开 false:关)
        :type AutoIsolateSwitch: bool
        :param IsKillProgress: 是否中断隔离文件关联的进程(true:是 false:否)
        :type IsKillProgress: bool
        """
        self.AutoIsolateSwitch = None
        self.IsKillProgress = None


    def _deserialize(self, params):
        self.AutoIsolateSwitch = params.get("AutoIsolateSwitch")
        self.IsKillProgress = params.get("IsKillProgress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVirusAutoIsolateSettingResponse(AbstractModel):
    """ModifyVirusAutoIsolateSetting返回参数结构体

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
	EVENT_ISOLATE_CONTAINER: 隔离容器
	EVENT_RESOTRE_CONTAINER: 恢复容器
        :type Status: str
        :param Remark: 事件备注
        :type Remark: str
        :param AutoIsolate: 是否后续自动隔离相同MD5文件
        :type AutoIsolate: bool
        """
        self.EventIdSet = None
        self.Status = None
        self.Remark = None
        self.AutoIsolate = None


    def _deserialize(self, params):
        self.EventIdSet = params.get("EventIdSet")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.AutoIsolate = params.get("AutoIsolate")
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
        :param ScanPathType: 当ScanPathAll为true 生效 0扫描以下路径 1、扫描除以下路径(扫描范围只能小于等于1)
        :type ScanPathType: int
        :param ScanPath: 自选排除或扫描的地址
        :type ScanPath: list of str
        :param ScanPathMode: 扫描路径模式：
SCAN_PATH_ALL：全部路径
SCAN_PATH_DEFAULT：默认路径
SCAN_PATH_USER_DEFINE：用户自定义路径

        :type ScanPathMode: str
        """
        self.EnableScan = None
        self.ScanPathAll = None
        self.ScanPathType = None
        self.ScanPath = None
        self.ScanPathMode = None


    def _deserialize(self, params):
        self.EnableScan = params.get("EnableScan")
        self.ScanPathAll = params.get("ScanPathAll")
        self.ScanPathType = params.get("ScanPathType")
        self.ScanPath = params.get("ScanPath")
        self.ScanPathMode = params.get("ScanPathMode")
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
        :param ScanPathMode: 扫描路径模式：
SCAN_PATH_ALL：全部路径
SCAN_PATH_DEFAULT：默认路径
SCAN_PATH_USER_DEFINE：用户自定义路径

        :type ScanPathMode: str
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
        self.ScanPathMode = None


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
        self.ScanPathMode = params.get("ScanPathMode")
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


class ModifyVulDefenceEventStatusRequest(AbstractModel):
    """ModifyVulDefenceEventStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIDs: 事件IDs数组
        :type EventIDs: list of int
        :param Status: 操作状态：
EVENT_DEALED：已处理，EVENT_IGNORE：忽略，EVENT_ISOLATE_CONTAINER：隔离容器，EVENT_DEL：删除
        :type Status: str
        :param Remark: 备注
        :type Remark: str
        """
        self.EventIDs = None
        self.Status = None
        self.Remark = None


    def _deserialize(self, params):
        self.EventIDs = params.get("EventIDs")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVulDefenceEventStatusResponse(AbstractModel):
    """ModifyVulDefenceEventStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVulDefenceSettingRequest(AbstractModel):
    """ModifyVulDefenceSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param IsEnabled: 是否开启:0: 关闭 1:开启
        :type IsEnabled: int
        :param Scope: 漏洞防御主机范围:0：自选 1: 全部主机。IsEnabled为1时必填
        :type Scope: int
        :param HostIDs: 自选漏洞防御主机,Scope为0时必填
        :type HostIDs: list of str
        """
        self.IsEnabled = None
        self.Scope = None
        self.HostIDs = None


    def _deserialize(self, params):
        self.IsEnabled = params.get("IsEnabled")
        self.Scope = params.get("Scope")
        self.HostIDs = params.get("HostIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVulDefenceSettingResponse(AbstractModel):
    """ModifyVulDefenceSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NetworkAuditRecord(AbstractModel):
    """网络集群资产审计返回结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param ClusterName: 集群名字
        :type ClusterName: str
        :param Region: 集群区域
        :type Region: str
        :param Action: 动作
        :type Action: str
        :param Operation: 操作人
        :type Operation: str
        :param NetworkPolicyName: 策略名
        :type NetworkPolicyName: str
        :param OperationTime: 操作时间
        :type OperationTime: str
        :param AppId: 操作人appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param Uin: 操作人uin
        :type Uin: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Region = None
        self.Action = None
        self.Operation = None
        self.NetworkPolicyName = None
        self.OperationTime = None
        self.AppId = None
        self.Uin = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.Action = params.get("Action")
        self.Operation = params.get("Operation")
        self.NetworkPolicyName = params.get("NetworkPolicyName")
        self.OperationTime = params.get("OperationTime")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkClusterInfoItem(AbstractModel):
    """网络集群资产返回的结构体

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
        :param Region: 集群区域
        :type Region: str
        :param NetworkPolicyPlugin: 集群网络插件
        :type NetworkPolicyPlugin: str
        :param ClusterStatus: 集群状态
        :type ClusterStatus: str
        :param TotalRuleCount: 总策略数量
        :type TotalRuleCount: int
        :param EnableRuleCount: 已开启策略数量
        :type EnableRuleCount: int
        :param NetworkPolicyPluginStatus: 集群网络插件状态，正常：Running 不正常：Error
        :type NetworkPolicyPluginStatus: str
        :param NetworkPolicyPluginError: 集群网络插件错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkPolicyPluginError: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterVersion = None
        self.ClusterOs = None
        self.ClusterType = None
        self.Region = None
        self.NetworkPolicyPlugin = None
        self.ClusterStatus = None
        self.TotalRuleCount = None
        self.EnableRuleCount = None
        self.NetworkPolicyPluginStatus = None
        self.NetworkPolicyPluginError = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterType = params.get("ClusterType")
        self.Region = params.get("Region")
        self.NetworkPolicyPlugin = params.get("NetworkPolicyPlugin")
        self.ClusterStatus = params.get("ClusterStatus")
        self.TotalRuleCount = params.get("TotalRuleCount")
        self.EnableRuleCount = params.get("EnableRuleCount")
        self.NetworkPolicyPluginStatus = params.get("NetworkPolicyPluginStatus")
        self.NetworkPolicyPluginError = params.get("NetworkPolicyPluginError")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkClusterNamespaceInfo(AbstractModel):
    """网络集群网络空间返回的结构体

    """

    def __init__(self):
        r"""
        :param Labels: 网络空间标签
        :type Labels: str
        :param Name: 网络空间名字
        :type Name: str
        """
        self.Labels = None
        self.Name = None


    def _deserialize(self, params):
        self.Labels = params.get("Labels")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkClusterNamespaceLabelInfo(AbstractModel):
    """网络集群网络空间标签返回的结构体

    """

    def __init__(self):
        r"""
        :param Labels: 网络空间标签
        :type Labels: str
        :param Name: 网络空间名字
        :type Name: str
        """
        self.Labels = None
        self.Name = None


    def _deserialize(self, params):
        self.Labels = params.get("Labels")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkClusterPodInfo(AbstractModel):
    """网络集群pod返回的结构体

    """

    def __init__(self):
        r"""
        :param PodName: pod名字
        :type PodName: str
        :param Namespace: pod空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param Labels: pod标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: str
        :param WorkloadKind: pod类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadKind: str
        """
        self.PodName = None
        self.Namespace = None
        self.Labels = None
        self.WorkloadKind = None


    def _deserialize(self, params):
        self.PodName = params.get("PodName")
        self.Namespace = params.get("Namespace")
        self.Labels = params.get("Labels")
        self.WorkloadKind = params.get("WorkloadKind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkCustomPolicy(AbstractModel):
    """网络集群策略自定义规则

    """

    def __init__(self):
        r"""
        :param Direction: 网络策略方向，分为FROM和TO
        :type Direction: str
        :param Ports: 网络策略策略端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Ports: list of NetworkPorts
        :param Peer: 网络策略策略对象

开启待确认：PublishedNoConfirm

开启已确认：PublishedConfirmed

关闭中：unPublishing

开启中：Publishing

待开启：unPublishEdit
注意：此字段可能返回 null，表示取不到有效值。
        :type Peer: list of NetworkPeer
        """
        self.Direction = None
        self.Ports = None
        self.Peer = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        if params.get("Ports") is not None:
            self.Ports = []
            for item in params.get("Ports"):
                obj = NetworkPorts()
                obj._deserialize(item)
                self.Ports.append(obj)
        if params.get("Peer") is not None:
            self.Peer = []
            for item in params.get("Peer"):
                obj = NetworkPeer()
                obj._deserialize(item)
                self.Peer.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkPeer(AbstractModel):
    """网络集群策略自定义规则

    """

    def __init__(self):
        r"""
        :param PeerType: 对象类型：

命名空间：NamespaceSelector，代表NamespaceSelector有值

pod类型：PodSelector，代表NamespaceSelector和PodSelector都有值

ip类型：IPBlock，代表只有IPBlock有值
        :type PeerType: str
        :param NamespaceSelector: 空间选择器
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceSelector: str
        :param PodSelector: pod选择器
注意：此字段可能返回 null，表示取不到有效值。
        :type PodSelector: str
        :param IPBlock: Ip选择器
注意：此字段可能返回 null，表示取不到有效值。
        :type IPBlock: str
        """
        self.PeerType = None
        self.NamespaceSelector = None
        self.PodSelector = None
        self.IPBlock = None


    def _deserialize(self, params):
        self.PeerType = params.get("PeerType")
        self.NamespaceSelector = params.get("NamespaceSelector")
        self.PodSelector = params.get("PodSelector")
        self.IPBlock = params.get("IPBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkPolicyInfoItem(AbstractModel):
    """网络集群策略返回的结构体

    """

    def __init__(self):
        r"""
        :param Name: 网络策略名
        :type Name: str
        :param Description: 网络策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param PublishStatus: 发布状态：

开启待确认：PublishedNoConfirm

开启已确认：PublishedConfirmed

关闭中：unPublishing

开启中：Publishing

待开启：unPublishEdit
        :type PublishStatus: str
        :param PolicySourceType: 策略类型：

自动发现：System

手动添加：Manual
        :type PolicySourceType: str
        :param Namespace: 策略空间
        :type Namespace: str
        :param PolicyCreateTime: 策略创建日期
        :type PolicyCreateTime: str
        :param NetworkPolicyPlugin: 策略类型

kube-router：KubeRouter

cilium：Cilium
        :type NetworkPolicyPlugin: str
        :param PublishResult: 策略发布结果
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishResult: str
        :param FromPolicyRule: 入站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type FromPolicyRule: int
        :param ToPolicyRule: 入站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type ToPolicyRule: int
        :param PodSelector: 作用对象
注意：此字段可能返回 null，表示取不到有效值。
        :type PodSelector: str
        :param Id: 网络策略Id
        :type Id: int
        """
        self.Name = None
        self.Description = None
        self.PublishStatus = None
        self.PolicySourceType = None
        self.Namespace = None
        self.PolicyCreateTime = None
        self.NetworkPolicyPlugin = None
        self.PublishResult = None
        self.FromPolicyRule = None
        self.ToPolicyRule = None
        self.PodSelector = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.PublishStatus = params.get("PublishStatus")
        self.PolicySourceType = params.get("PolicySourceType")
        self.Namespace = params.get("Namespace")
        self.PolicyCreateTime = params.get("PolicyCreateTime")
        self.NetworkPolicyPlugin = params.get("NetworkPolicyPlugin")
        self.PublishResult = params.get("PublishResult")
        self.FromPolicyRule = params.get("FromPolicyRule")
        self.ToPolicyRule = params.get("ToPolicyRule")
        self.PodSelector = params.get("PodSelector")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkPorts(AbstractModel):
    """网络集群策略自定义规则端口

    """

    def __init__(self):
        r"""
        :param Protocol: 网络策略协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param Port: 网络策略策略端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        """
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenTcssTrialRequest(AbstractModel):
    """OpenTcssTrial请求参数结构体

    """


class OpenTcssTrialResponse(AbstractModel):
    """OpenTcssTrial返回参数结构体

    """

    def __init__(self):
        r"""
        :param EndTime: 试用开通结束时间
        :type EndTime: str
        :param StartTime: 试用开通开始时间
        :type StartTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EndTime = None
        self.StartTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
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
        


class ProcessBaseInfo(AbstractModel):
    """运行时安全，进程基础信息

    """

    def __init__(self):
        r"""
        :param ProcessStartUser: 进程启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessStartUser: str
        :param ProcessUserGroup: 进程用户组
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessUserGroup: str
        :param ProcessPath: 进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessPath: str
        :param ProcessParam: 进程命令行参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessParam: str
        """
        self.ProcessStartUser = None
        self.ProcessUserGroup = None
        self.ProcessPath = None
        self.ProcessParam = None


    def _deserialize(self, params):
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
        


class ProjectInfo(AbstractModel):
    """主机所属项目

    """

    def __init__(self):
        r"""
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectID: 项目ID
        :type ProjectID: int
        """
        self.ProjectName = None
        self.ProjectID = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PromotionActivityContent(AbstractModel):
    """促销活动内容

    """

    def __init__(self):
        r"""
        :param MonthNum: 月数
        :type MonthNum: int
        :param CoresCountLimit: 核数最低限量
        :type CoresCountLimit: int
        :param ProfessionalDiscount: 专业版折扣
        :type ProfessionalDiscount: int
        :param ImageAuthorizationNum: 附赠镜像数
        :type ImageAuthorizationNum: int
        """
        self.MonthNum = None
        self.CoresCountLimit = None
        self.ProfessionalDiscount = None
        self.ImageAuthorizationNum = None


    def _deserialize(self, params):
        self.MonthNum = params.get("MonthNum")
        self.CoresCountLimit = params.get("CoresCountLimit")
        self.ProfessionalDiscount = params.get("ProfessionalDiscount")
        self.ImageAuthorizationNum = params.get("ImageAuthorizationNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RaspInfo(AbstractModel):
    """漏洞防御插件 rasp信息

    """

    def __init__(self):
        r"""
        :param Name: rasp名称
        :type Name: str
        :param Value: rasp  描述
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
        


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param Region: 地域标识
        :type Region: str
        :param RegionName: 地域名称
        :type RegionName: str
        """
        self.Region = None
        self.RegionName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
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


class ResetSecLogTopicConfigRequest(AbstractModel):
    """ResetSecLogTopicConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConfigType: 配置类型(ckafka/cls)
        :type ConfigType: str
        :param LogType: 日志类型
        :type LogType: str
        """
        self.ConfigType = None
        self.LogType = None


    def _deserialize(self, params):
        self.ConfigType = params.get("ConfigType")
        self.LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetSecLogTopicConfigResponse(AbstractModel):
    """ResetSecLogTopicConfig返回参数结构体

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
        :param OperationTime: 事件最后一次处理的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationTime: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.DstAddress = None
        self.OperationTime = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        self.DstAddress = params.get("DstAddress")
        self.OperationTime = params.get("OperationTime")
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
        :param ContainerNetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
	"NODE_DESTROYED"      //节点已销毁
	"CONTAINER_EXITED"    //容器已退出
	"CONTAINER_DESTROYED" //容器已销毁
	"SHARED_HOST"         // 容器与主机共享网络
	"RESOURCE_LIMIT"      //隔离操作资源超限
	"UNKNOW"              // 原因未知
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
        :type ContainerIsolateOperationSrc: str
        :param ContainerStatus: 容器状态
正在运行: RUNNING
暂停: PAUSED
停止: STOPPED
已经创建: CREATED
已经销毁: DESTROYED
正在重启中: RESTARTING
迁移中: REMOVING
        :type ContainerStatus: str
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
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.ContainerStatus = None


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
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.ContainerStatus = params.get("ContainerStatus")
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
        :param OperationTime: 事件最后一次处理的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationTime: str
        """
        self.Description = None
        self.Solution = None
        self.Remark = None
        self.SyscallName = None
        self.OperationTime = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Solution = params.get("Solution")
        self.Remark = params.get("Remark")
        self.SyscallName = params.get("SyscallName")
        self.OperationTime = params.get("OperationTime")
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
        :param ContainerNetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
"NODE_DESTROYED"      //节点已销毁
"CONTAINER_EXITED"    //容器已退出
"CONTAINER_DESTROYED" //容器已销毁
"SHARED_HOST"         // 容器与主机共享网络
"RESOURCE_LIMIT"      //隔离操作资源超限
"UNKNOW"              // 原因未知
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
        :type ContainerIsolateOperationSrc: str
        :param ContainerStatus: 容器状态
正在运行: RUNNING
暂停: PAUSED
停止: STOPPED
已经创建: CREATED
已经销毁: DESTROYED
正在重启中: RESTARTING
迁移中: REMOVING
        :type ContainerStatus: str
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
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.ContainerStatus = None


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
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.ContainerStatus = params.get("ContainerStatus")
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
        :param ContainerNetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
"NODE_DESTROYED"      //节点已销毁
"CONTAINER_EXITED"    //容器已退出
"CONTAINER_DESTROYED" //容器已销毁
"SHARED_HOST"         // 容器与主机共享网络
"RESOURCE_LIMIT"      //隔离操作资源超限
"UNKNOW"              // 原因未知
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerIsolateOperationSrc: str
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
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None


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
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
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


class ScanIgnoreVul(AbstractModel):
    """扫描忽略的漏洞

    """

    def __init__(self):
        r"""
        :param VulName: 漏洞名称
        :type VulName: str
        :param CVEID: 漏洞CVEID
        :type CVEID: str
        :param PocID: 漏洞PocID
        :type PocID: str
        :param RegistryImageCount: 忽略的仓库镜像数
        :type RegistryImageCount: int
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param IsIgnoreAll: 是否忽略所有镜像：0：否/1：是
        :type IsIgnoreAll: int
        :param LocalImageCount: 忽略的本地镜像数
        :type LocalImageCount: int
        """
        self.VulName = None
        self.CVEID = None
        self.PocID = None
        self.RegistryImageCount = None
        self.UpdateTime = None
        self.IsIgnoreAll = None
        self.LocalImageCount = None


    def _deserialize(self, params):
        self.VulName = params.get("VulName")
        self.CVEID = params.get("CVEID")
        self.PocID = params.get("PocID")
        self.RegistryImageCount = params.get("RegistryImageCount")
        self.UpdateTime = params.get("UpdateTime")
        self.IsIgnoreAll = params.get("IsIgnoreAll")
        self.LocalImageCount = params.get("LocalImageCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTemplate(AbstractModel):
    """快速搜索模板

    """

    def __init__(self):
        r"""
        :param Name: 检索名称
        :type Name: str
        :param LogType: 检索索引类型
        :type LogType: str
        :param Condition: 检索语句
        :type Condition: str
        :param TimeRange: 时间范围
        :type TimeRange: str
        :param Query: 转换的检索语句内容
        :type Query: str
        :param Flag: 检索方式。输入框检索：standard,过滤，检索：simple
        :type Flag: str
        :param DisplayData: 展示数据
        :type DisplayData: str
        :param Id: 规则ID
        :type Id: int
        """
        self.Name = None
        self.LogType = None
        self.Condition = None
        self.TimeRange = None
        self.Query = None
        self.Flag = None
        self.DisplayData = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.LogType = params.get("LogType")
        self.Condition = params.get("Condition")
        self.TimeRange = params.get("TimeRange")
        self.Query = params.get("Query")
        self.Flag = params.get("Flag")
        self.DisplayData = params.get("DisplayData")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogAlertMsgInfo(AbstractModel):
    """安全日志告警信息

    """

    def __init__(self):
        r"""
        :param MsgType: 告警类型
        :type MsgType: str
        :param MsgValue: 告警值
        :type MsgValue: str
        :param State: 状态(0:关闭 1:开启)
        :type State: bool
        """
        self.MsgType = None
        self.MsgValue = None
        self.State = None


    def _deserialize(self, params):
        self.MsgType = params.get("MsgType")
        self.MsgValue = params.get("MsgValue")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogDeliveryClsSettingInfo(AbstractModel):
    """安全日志-日志投递cls设置信息

    """

    def __init__(self):
        r"""
        :param LogType: 日志类型
        :type LogType: str
        :param State: 投递状态(true:开启 false:关闭)
        :type State: bool
        :param Region: 区域
        :type Region: str
        :param LogSet: 日志集
        :type LogSet: str
        :param TopicID: 主题ID
        :type TopicID: str
        :param LogSetName: 日志集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSetName: str
        :param TopicName: 主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        """
        self.LogType = None
        self.State = None
        self.Region = None
        self.LogSet = None
        self.TopicID = None
        self.LogSetName = None
        self.TopicName = None


    def _deserialize(self, params):
        self.LogType = params.get("LogType")
        self.State = params.get("State")
        self.Region = params.get("Region")
        self.LogSet = params.get("LogSet")
        self.TopicID = params.get("TopicID")
        self.LogSetName = params.get("LogSetName")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogDeliveryKafkaSettingInfo(AbstractModel):
    """安全日志日志投递kafka设置详情

    """

    def __init__(self):
        r"""
        :param LogType: 日志类型
        :type LogType: str
        :param TopicID: 主题ID
        :type TopicID: str
        :param TopicName: 主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param State: 投递状态(false:关 true:开)
        :type State: bool
        """
        self.LogType = None
        self.TopicID = None
        self.TopicName = None
        self.State = None


    def _deserialize(self, params):
        self.LogType = params.get("LogType")
        self.TopicID = params.get("TopicID")
        self.TopicName = params.get("TopicName")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogJoinInfo(AbstractModel):
    """安全日志接入详情

    """

    def __init__(self):
        r"""
        :param Count: 已接入数量
        :type Count: int
        :param IsJoined: 是否已接入(true:已接入 false:未接入)
        :type IsJoined: bool
        :param LogType: 日志类型(
容器bash:  "container_bash"
容器启动: "container_launch"
k8sApi: "k8s_api"
)
        :type LogType: str
        """
        self.Count = None
        self.IsJoined = None
        self.LogType = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.IsJoined = params.get("IsJoined")
        self.LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogJoinObjectInfo(AbstractModel):
    """安全日志接入对象详情

    """

    def __init__(self):
        r"""
        :param HostID: 主机ID
        :type HostID: str
        :param HostName: 主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param HostIP: 主机IP
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIP: str
        :param HostStatus: 主机状态
        :type HostStatus: str
        :param ClusterID: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterID: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param PublicIP: 外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIP: str
        :param JoinState: 接入状态(true:已接入  false:未接入)
        :type JoinState: bool
        :param ClusterVersion: 集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterVersion: str
        :param ClusterMainAddress: 集群主节点地址
        :type ClusterMainAddress: str
        """
        self.HostID = None
        self.HostName = None
        self.HostIP = None
        self.HostStatus = None
        self.ClusterID = None
        self.ClusterName = None
        self.PublicIP = None
        self.JoinState = None
        self.ClusterVersion = None
        self.ClusterMainAddress = None


    def _deserialize(self, params):
        self.HostID = params.get("HostID")
        self.HostName = params.get("HostName")
        self.HostIP = params.get("HostIP")
        self.HostStatus = params.get("HostStatus")
        self.ClusterID = params.get("ClusterID")
        self.ClusterName = params.get("ClusterName")
        self.PublicIP = params.get("PublicIP")
        self.JoinState = params.get("JoinState")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterMainAddress = params.get("ClusterMainAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
ET_VIRUS 木马事件
ET_MALICIOUS_CONNECTION 恶意外连事件
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


class StopVulScanTaskRequest(AbstractModel):
    """StopVulScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param LocalTaskID: 本地镜像漏洞扫描任务ID
        :type LocalTaskID: int
        :param LocalImageIDs: 本地镜像ID，无则全部
        :type LocalImageIDs: list of str
        :param RegistryImageIDs: 仓库镜像ID，无则全部
        :type RegistryImageIDs: list of int non-negative
        :param RegistryTaskID: 仓库镜像漏洞扫描任务ID
        :type RegistryTaskID: int
        """
        self.LocalTaskID = None
        self.LocalImageIDs = None
        self.RegistryImageIDs = None
        self.RegistryTaskID = None


    def _deserialize(self, params):
        self.LocalTaskID = params.get("LocalTaskID")
        self.LocalImageIDs = params.get("LocalImageIDs")
        self.RegistryImageIDs = params.get("RegistryImageIDs")
        self.RegistryTaskID = params.get("RegistryTaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopVulScanTaskResponse(AbstractModel):
    """StopVulScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SupportDefenceVul(AbstractModel):
    """支持防御的漏洞

    """

    def __init__(self):
        r"""
        :param PocID: 漏洞PocID
        :type PocID: str
        :param Name: 漏洞名称
        :type Name: str
        :param Tags: 漏洞标签
        :type Tags: list of str
        :param CVSSV3Score: 漏洞CVSS
        :type CVSSV3Score: float
        :param Level: 漏洞威胁等级
        :type Level: str
        :param CVEID: 漏洞CVEID
        :type CVEID: str
        :param SubmitTime: 漏洞披露时间
        :type SubmitTime: str
        """
        self.PocID = None
        self.Name = None
        self.Tags = None
        self.CVSSV3Score = None
        self.Level = None
        self.CVEID = None
        self.SubmitTime = None


    def _deserialize(self, params):
        self.PocID = params.get("PocID")
        self.Name = params.get("Name")
        self.Tags = params.get("Tags")
        self.CVSSV3Score = params.get("CVSSV3Score")
        self.Level = params.get("Level")
        self.CVEID = params.get("CVEID")
        self.SubmitTime = params.get("SubmitTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchImageAutoAuthorizedRuleRequest(AbstractModel):
    """SwitchImageAutoAuthorizedRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param IsEnabled: 规则是否生效，0:不生效，1:已生效
        :type IsEnabled: int
        :param RuleId: 规则id
        :type RuleId: int
        """
        self.IsEnabled = None
        self.RuleId = None


    def _deserialize(self, params):
        self.IsEnabled = params.get("IsEnabled")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchImageAutoAuthorizedRuleResponse(AbstractModel):
    """SwitchImageAutoAuthorizedRule返回参数结构体

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


class TagInfo(AbstractModel):
    """主机标签信息

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
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
        


class UnauthorizedCoresTendency(AbstractModel):
    """未授权核数趋势

    """

    def __init__(self):
        r"""
        :param DateTime: 日期
        :type DateTime: str
        :param CoresCount: 未授权的核数
        :type CoresCount: int
        """
        self.DateTime = None
        self.CoresCount = None


    def _deserialize(self, params):
        self.DateTime = params.get("DateTime")
        self.CoresCount = params.get("CoresCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAndPublishNetworkFirewallPolicyDetailRequest(AbstractModel):
    """UpdateAndPublishNetworkFirewallPolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Id: 策略Id
        :type Id: int
        :param FromPolicyRule: 入站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type FromPolicyRule: int
        :param ToPolicyRule: 出站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type ToPolicyRule: int
        :param PodSelector: pod选择器
        :type PodSelector: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 策略描述
        :type Description: str
        :param CustomPolicy: 自定义规则
        :type CustomPolicy: list of NetworkCustomPolicy
        """
        self.ClusterId = None
        self.Id = None
        self.FromPolicyRule = None
        self.ToPolicyRule = None
        self.PodSelector = None
        self.Namespace = None
        self.Description = None
        self.CustomPolicy = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Id = params.get("Id")
        self.FromPolicyRule = params.get("FromPolicyRule")
        self.ToPolicyRule = params.get("ToPolicyRule")
        self.PodSelector = params.get("PodSelector")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        if params.get("CustomPolicy") is not None:
            self.CustomPolicy = []
            for item in params.get("CustomPolicy"):
                obj = NetworkCustomPolicy()
                obj._deserialize(item)
                self.CustomPolicy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAndPublishNetworkFirewallPolicyDetailResponse(AbstractModel):
    """UpdateAndPublishNetworkFirewallPolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateAndPublishNetworkFirewallPolicyYamlDetailRequest(AbstractModel):
    """UpdateAndPublishNetworkFirewallPolicyYamlDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Id: 策略id
        :type Id: int
        :param Yaml: base64编码的networkpolicy yaml字符串
        :type Yaml: str
        :param Description: 策略描述
        :type Description: str
        """
        self.ClusterId = None
        self.Id = None
        self.Yaml = None
        self.Description = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Id = params.get("Id")
        self.Yaml = params.get("Yaml")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse(AbstractModel):
    """UpdateAndPublishNetworkFirewallPolicyYamlDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
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
        :param Insecure: 安全模式（证书校验）：0（默认） 非安全模式（跳过证书校验）：1
        :type Insecure: int
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
        self.Insecure = None


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
        self.Insecure = params.get("Insecure")
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


class UpdateNetworkFirewallPolicyDetailRequest(AbstractModel):
    """UpdateNetworkFirewallPolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Id: 策略Id
        :type Id: int
        :param FromPolicyRule: 入站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type FromPolicyRule: int
        :param ToPolicyRule: 出站规则

全部允许：1

全部拒绝 ：2

自定义：3
        :type ToPolicyRule: int
        :param PodSelector: pod选择器
        :type PodSelector: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 策略描述
        :type Description: str
        :param CustomPolicy: 自定义规则
        :type CustomPolicy: list of NetworkCustomPolicy
        """
        self.ClusterId = None
        self.Id = None
        self.FromPolicyRule = None
        self.ToPolicyRule = None
        self.PodSelector = None
        self.Namespace = None
        self.Description = None
        self.CustomPolicy = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Id = params.get("Id")
        self.FromPolicyRule = params.get("FromPolicyRule")
        self.ToPolicyRule = params.get("ToPolicyRule")
        self.PodSelector = params.get("PodSelector")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        if params.get("CustomPolicy") is not None:
            self.CustomPolicy = []
            for item in params.get("CustomPolicy"):
                obj = NetworkCustomPolicy()
                obj._deserialize(item)
                self.CustomPolicy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNetworkFirewallPolicyDetailResponse(AbstractModel):
    """UpdateNetworkFirewallPolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateNetworkFirewallPolicyYamlDetailRequest(AbstractModel):
    """UpdateNetworkFirewallPolicyYamlDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Id: 策略id
        :type Id: int
        :param Yaml: base64编码的networkpolicy yaml字符串
        :type Yaml: str
        :param Description: 策略描述
        :type Description: str
        """
        self.ClusterId = None
        self.Id = None
        self.Yaml = None
        self.Description = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Id = params.get("Id")
        self.Yaml = params.get("Yaml")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNetworkFirewallPolicyYamlDetailResponse(AbstractModel):
    """UpdateNetworkFirewallPolicyYamlDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 返回创建的任务的ID，为0表示创建失败。
        :type TaskId: int
        :param Result: 创建任务的结果，"Succ"为成功，"Failed"为失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class VirusAutoIsolateSampleInfo(AbstractModel):
    """木马自动隔离样本信息

    """

    def __init__(self):
        r"""
        :param MD5: 文件MD5值
        :type MD5: str
        :param VirusName: 病毒名
        :type VirusName: str
        :param ModifyTime: 最近编辑时间
        :type ModifyTime: str
        :param AutoIsolateSwitch: 自动隔离开关(true:开 false:关)
        :type AutoIsolateSwitch: bool
        """
        self.MD5 = None
        self.VirusName = None
        self.ModifyTime = None
        self.AutoIsolateSwitch = None


    def _deserialize(self, params):
        self.MD5 = params.get("MD5")
        self.VirusName = params.get("VirusName")
        self.ModifyTime = params.get("ModifyTime")
        self.AutoIsolateSwitch = params.get("AutoIsolateSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param ContainerStatus: 容器状态
正在运行: RUNNING
暂停: PAUSED
停止: STOPPED
已经创建: CREATED
已经销毁: DESTROYED
正在重启中: RESTARTING
迁移中: REMOVING
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
        :param ContainerNetStatus: 网络状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
	"NODE_DESTROYED"      //节点已销毁
	"CONTAINER_EXITED"    //容器已退出
	"CONTAINER_DESTROYED" //容器已销毁
	"SHARED_HOST"         // 容器与主机共享网络
	"RESOURCE_LIMIT"      //隔离操作资源超限
	"UNKNOW"              // 原因未知
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
        :type ContainerIsolateOperationSrc: str
        :param MD5: md5值
注意：此字段可能返回 null，表示取不到有效值。
        :type MD5: str
        :param RiskLevel: 风险等级 RISK_CRITICAL, RISK_HIGH, RISK_MEDIUM, RISK_LOW, RISK_NOTICE。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param CheckPlatform: 检测平台
1: 云查杀引擎
2: tav
3: binaryAi
4: 异常行为
5: 威胁情报
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPlatform: list of str
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
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.MD5 = None
        self.RiskLevel = None
        self.CheckPlatform = None


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
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.MD5 = params.get("MD5")
        self.RiskLevel = params.get("RiskLevel")
        self.CheckPlatform = params.get("CheckPlatform")
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
        


class VirusTendencyInfo(AbstractModel):
    """木马趋势详情

    """

    def __init__(self):
        r"""
        :param Date: 日期
        :type Date: str
        :param PendingEventCount: 待处理事件总数
        :type PendingEventCount: int
        :param RiskContainerCount: 风险容器总数
        :type RiskContainerCount: int
        :param EventCount: 事件总数
        :type EventCount: int
        :param IsolateEventCount: 隔离事件总数
        :type IsolateEventCount: int
        """
        self.Date = None
        self.PendingEventCount = None
        self.RiskContainerCount = None
        self.EventCount = None
        self.IsolateEventCount = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.PendingEventCount = params.get("PendingEventCount")
        self.RiskContainerCount = params.get("RiskContainerCount")
        self.EventCount = params.get("EventCount")
        self.IsolateEventCount = params.get("IsolateEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulAffectedComponentInfo(AbstractModel):
    """受漏洞影响的组件信息

    """

    def __init__(self):
        r"""
        :param Name: 组件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Version: 组件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: list of str
        :param FixedVersion: 组件修复版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FixedVersion: list of str
        """
        self.Name = None
        self.Version = None
        self.FixedVersion = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.FixedVersion = params.get("FixedVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulAffectedContainerInfo(AbstractModel):
    """受漏洞影响的容器信息

    """

    def __init__(self):
        r"""
        :param HostIP: 内网IP
        :type HostIP: str
        :param ContainerID: 容器ID
        :type ContainerID: str
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param PodName: Pod名称
        :type PodName: str
        :param PodIP: PodIP值
        :type PodIP: str
        :param HostName: 主机名称
        :type HostName: str
        :param HostID: 主机ID
        :type HostID: str
        :param PublicIP: 外网IP
        :type PublicIP: str
        """
        self.HostIP = None
        self.ContainerID = None
        self.ContainerName = None
        self.PodName = None
        self.PodIP = None
        self.HostName = None
        self.HostID = None
        self.PublicIP = None


    def _deserialize(self, params):
        self.HostIP = params.get("HostIP")
        self.ContainerID = params.get("ContainerID")
        self.ContainerName = params.get("ContainerName")
        self.PodName = params.get("PodName")
        self.PodIP = params.get("PodIP")
        self.HostName = params.get("HostName")
        self.HostID = params.get("HostID")
        self.PublicIP = params.get("PublicIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulAffectedImageComponentInfo(AbstractModel):
    """受漏洞影响的组件信息

    """

    def __init__(self):
        r"""
        :param Name: 组件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Version: 组件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param FixedVersion: 组件修复版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FixedVersion: str
        :param Path: 组件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
        self.Name = None
        self.Version = None
        self.FixedVersion = None
        self.Path = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.FixedVersion = params.get("FixedVersion")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulAffectedImageInfo(AbstractModel):
    """受漏洞影响的镜像信息

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param HostCount: 关联的主机数
        :type HostCount: int
        :param ContainerCount: 关联的容器数
        :type ContainerCount: int
        :param ComponentList: 组件列表
        :type ComponentList: list of VulAffectedImageComponentInfo
        """
        self.ImageID = None
        self.ImageName = None
        self.HostCount = None
        self.ContainerCount = None
        self.ComponentList = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.HostCount = params.get("HostCount")
        self.ContainerCount = params.get("ContainerCount")
        if params.get("ComponentList") is not None:
            self.ComponentList = []
            for item in params.get("ComponentList"):
                obj = VulAffectedImageComponentInfo()
                obj._deserialize(item)
                self.ComponentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulDefenceEvent(AbstractModel):
    """漏洞防御事件详情

    """

    def __init__(self):
        r"""
        :param CVEID: 漏洞CVEID
        :type CVEID: str
        :param VulName: 漏洞名称
        :type VulName: str
        :param PocID: 漏洞PocID
        :type PocID: str
        :param EventType: 入侵状态
        :type EventType: str
        :param SourceIP: 攻击源IP
        :type SourceIP: str
        :param City: 攻击源ip地址所在城市
        :type City: str
        :param EventCount: 事件数量
        :type EventCount: int
        :param ContainerID: 容器ID
        :type ContainerID: str
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param Status: 处理状态
        :type Status: str
        :param EventID: 事件ID
        :type EventID: int
        :param CreateTime: 首次发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ContainerNetStatus: 隔离状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
        :type ContainerNetStatus: str
        :param MergeTime: 最近发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MergeTime: str
        :param ContainerStatus: 容器状态
正在运行: RUNNING
暂停: PAUSED
停止: STOPPED
已经创建: CREATED
已经销毁: DESTROYED
正在重启中: RESTARTING
迁移中: REMOVING
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
	"NODE_DESTROYED"      //节点已销毁
	"CONTAINER_EXITED"    //容器已退出
	"CONTAINER_DESTROYED" //容器已销毁
	"SHARED_HOST"         // 容器与主机共享网络
	"RESOURCE_LIMIT"      //隔离操作资源超限
	"UNKNOW"              // 原因未知
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerIsolateOperationSrc: str
        :param QUUID: 主机QUUID
注意：此字段可能返回 null，表示取不到有效值。
        :type QUUID: str
        :param HostIP: 主机内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIP: str
        :param HostName: 主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        """
        self.CVEID = None
        self.VulName = None
        self.PocID = None
        self.EventType = None
        self.SourceIP = None
        self.City = None
        self.EventCount = None
        self.ContainerID = None
        self.ContainerName = None
        self.ImageID = None
        self.ImageName = None
        self.Status = None
        self.EventID = None
        self.CreateTime = None
        self.ContainerNetStatus = None
        self.MergeTime = None
        self.ContainerStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.QUUID = None
        self.HostIP = None
        self.HostName = None


    def _deserialize(self, params):
        self.CVEID = params.get("CVEID")
        self.VulName = params.get("VulName")
        self.PocID = params.get("PocID")
        self.EventType = params.get("EventType")
        self.SourceIP = params.get("SourceIP")
        self.City = params.get("City")
        self.EventCount = params.get("EventCount")
        self.ContainerID = params.get("ContainerID")
        self.ContainerName = params.get("ContainerName")
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.Status = params.get("Status")
        self.EventID = params.get("EventID")
        self.CreateTime = params.get("CreateTime")
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.MergeTime = params.get("MergeTime")
        self.ContainerStatus = params.get("ContainerStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.QUUID = params.get("QUUID")
        self.HostIP = params.get("HostIP")
        self.HostName = params.get("HostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulDefenceEventDetail(AbstractModel):
    """漏洞防御事件详情

    """

    def __init__(self):
        r"""
        :param CVEID: 漏洞CVEID
        :type CVEID: str
        :param VulName: 漏洞名称
        :type VulName: str
        :param PocID: 漏洞PocID
        :type PocID: str
        :param EventType: 入侵状态
        :type EventType: str
        :param SourceIP: 攻击源IP
        :type SourceIP: str
        :param City: 攻击源ip地址所在城市
        :type City: str
        :param EventCount: 事件数量
        :type EventCount: int
        :param ContainerID: 容器ID
        :type ContainerID: str
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param Status: 处理状态
        :type Status: str
        :param SourcePort: 攻击源端口
        :type SourcePort: list of str
        :param EventID: 事件ID
        :type EventID: int
        :param HostName: 主机名称
        :type HostName: str
        :param HostIP: 主机内网IP
        :type HostIP: str
        :param PublicIP: 主机外网IP
        :type PublicIP: str
        :param PodName: Pod名称
        :type PodName: str
        :param Description: 危害描述
        :type Description: str
        :param OfficialSolution: 修复建议
        :type OfficialSolution: str
        :param NetworkPayload: 攻击包
        :type NetworkPayload: str
        :param PID: 进程PID
注意：此字段可能返回 null，表示取不到有效值。
        :type PID: int
        :param MainClass: 进程主类名
注意：此字段可能返回 null，表示取不到有效值。
        :type MainClass: str
        :param StackTrace: 堆栈信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StackTrace: str
        :param ServerAccount: 监听账号
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerAccount: str
        :param ServerPort: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerPort: str
        :param ServerExe: 进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerExe: str
        :param ServerArg: 进程命令行参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerArg: str
        :param QUUID: 主机QUUID
注意：此字段可能返回 null，表示取不到有效值。
        :type QUUID: str
        :param ContainerNetStatus: 隔离状态
未隔离  	NORMAL
已隔离		ISOLATED
隔离中		ISOLATING
隔离失败	ISOLATE_FAILED
解除隔离中  RESTORING
解除隔离失败 RESTORE_FAILED
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetStatus: str
        :param ContainerNetSubStatus: 容器子状态
"AGENT_OFFLINE"       //Agent离线
	"NODE_DESTROYED"      //节点已销毁
	"CONTAINER_EXITED"    //容器已退出
	"CONTAINER_DESTROYED" //容器已销毁
	"SHARED_HOST"         // 容器与主机共享网络
	"RESOURCE_LIMIT"      //隔离操作资源超限
	"UNKNOW"              // 原因未知
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetSubStatus: str
        :param ContainerIsolateOperationSrc: 容器隔离操作来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerIsolateOperationSrc: str
        :param ContainerStatus: 容器状态
正在运行: RUNNING
暂停: PAUSED
停止: STOPPED
已经创建: CREATED
已经销毁: DESTROYED
正在重启中: RESTARTING
迁移中: REMOVING
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerStatus: str
        :param JNDIUrl: 接口Url
注意：此字段可能返回 null，表示取不到有效值。
        :type JNDIUrl: str
        :param RaspDetail: rasp detail
注意：此字段可能返回 null，表示取不到有效值。
        :type RaspDetail: list of RaspInfo
        """
        self.CVEID = None
        self.VulName = None
        self.PocID = None
        self.EventType = None
        self.SourceIP = None
        self.City = None
        self.EventCount = None
        self.ContainerID = None
        self.ContainerName = None
        self.ImageID = None
        self.ImageName = None
        self.Status = None
        self.SourcePort = None
        self.EventID = None
        self.HostName = None
        self.HostIP = None
        self.PublicIP = None
        self.PodName = None
        self.Description = None
        self.OfficialSolution = None
        self.NetworkPayload = None
        self.PID = None
        self.MainClass = None
        self.StackTrace = None
        self.ServerAccount = None
        self.ServerPort = None
        self.ServerExe = None
        self.ServerArg = None
        self.QUUID = None
        self.ContainerNetStatus = None
        self.ContainerNetSubStatus = None
        self.ContainerIsolateOperationSrc = None
        self.ContainerStatus = None
        self.JNDIUrl = None
        self.RaspDetail = None


    def _deserialize(self, params):
        self.CVEID = params.get("CVEID")
        self.VulName = params.get("VulName")
        self.PocID = params.get("PocID")
        self.EventType = params.get("EventType")
        self.SourceIP = params.get("SourceIP")
        self.City = params.get("City")
        self.EventCount = params.get("EventCount")
        self.ContainerID = params.get("ContainerID")
        self.ContainerName = params.get("ContainerName")
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.Status = params.get("Status")
        self.SourcePort = params.get("SourcePort")
        self.EventID = params.get("EventID")
        self.HostName = params.get("HostName")
        self.HostIP = params.get("HostIP")
        self.PublicIP = params.get("PublicIP")
        self.PodName = params.get("PodName")
        self.Description = params.get("Description")
        self.OfficialSolution = params.get("OfficialSolution")
        self.NetworkPayload = params.get("NetworkPayload")
        self.PID = params.get("PID")
        self.MainClass = params.get("MainClass")
        self.StackTrace = params.get("StackTrace")
        self.ServerAccount = params.get("ServerAccount")
        self.ServerPort = params.get("ServerPort")
        self.ServerExe = params.get("ServerExe")
        self.ServerArg = params.get("ServerArg")
        self.QUUID = params.get("QUUID")
        self.ContainerNetStatus = params.get("ContainerNetStatus")
        self.ContainerNetSubStatus = params.get("ContainerNetSubStatus")
        self.ContainerIsolateOperationSrc = params.get("ContainerIsolateOperationSrc")
        self.ContainerStatus = params.get("ContainerStatus")
        self.JNDIUrl = params.get("JNDIUrl")
        if params.get("RaspDetail") is not None:
            self.RaspDetail = []
            for item in params.get("RaspDetail"):
                obj = RaspInfo()
                obj._deserialize(item)
                self.RaspDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulDefenceEventTendency(AbstractModel):
    """漏洞防御攻击事件趋势

    """

    def __init__(self):
        r"""
        :param Date: 日期
        :type Date: str
        :param EventCount: 事件数量
        :type EventCount: int
        """
        self.Date = None
        self.EventCount = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.EventCount = params.get("EventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulDefenceHost(AbstractModel):
    """漏洞防御的主机信息

    """

    def __init__(self):
        r"""
        :param HostName: 主机名称
        :type HostName: str
        :param HostIP: 主机ip即内网ip
        :type HostIP: str
        :param HostID: 主机QUUID
        :type HostID: str
        :param Status: 插件状态，正常：SUCCESS，异常：FAIL， NO_DEFENDED:未防御
        :type Status: str
        :param PublicIP: 外网ip
        :type PublicIP: str
        :param CreateTime: 首次开启时间
        :type CreateTime: str
        :param ModifyTime: 更新时间
        :type ModifyTime: str
        """
        self.HostName = None
        self.HostIP = None
        self.HostID = None
        self.Status = None
        self.PublicIP = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        self.HostIP = params.get("HostIP")
        self.HostID = params.get("HostID")
        self.Status = params.get("Status")
        self.PublicIP = params.get("PublicIP")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulDefencePlugin(AbstractModel):
    """漏洞防护的插件信息

    """

    def __init__(self):
        r"""
        :param PID: java进程pid
        :type PID: int
        :param MainClass: 进程主类名
        :type MainClass: str
        :param Status: 插件运行状态：注入中:INJECTING，注入成功：SUCCESS，注入失败：FAIL，插件超时：TIMEOUT，插件退出：QUIT
        :type Status: str
        :param ErrorLog: 错误日志
        :type ErrorLog: str
        """
        self.PID = None
        self.MainClass = None
        self.Status = None
        self.ErrorLog = None


    def _deserialize(self, params):
        self.PID = params.get("PID")
        self.MainClass = params.get("MainClass")
        self.Status = params.get("Status")
        self.ErrorLog = params.get("ErrorLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulDetailInfo(AbstractModel):
    """漏洞详情信息

    """

    def __init__(self):
        r"""
        :param CVEID: CVE编号
        :type CVEID: str
        :param Name: 漏洞名称
        :type Name: str
        :param Tags: 漏洞标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param CategoryType: 漏洞类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryType: str
        :param Level: 漏洞威胁等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param SubmitTime: 漏洞披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitTime: str
        :param Description: 漏洞描述
        :type Description: str
        :param CVSSV3Desc: CVSS V3描述
        :type CVSSV3Desc: str
        :param OfficialSolution: 漏洞修复建议
        :type OfficialSolution: str
        :param DefenseSolution: 缓解措施
        :type DefenseSolution: str
        :param Reference: 参考链接
        :type Reference: list of str
        :param CVSSV3Score: CVSS V3分数
        :type CVSSV3Score: float
        :param ComponentList: 受漏洞影响的组件列表
        :type ComponentList: list of VulAffectedComponentInfo
        :param LocalImageCount: 影响本地镜像数
        :type LocalImageCount: int
        :param ContainerCount: 影响容器数
        :type ContainerCount: int
        :param RegistryImageCount: 影响仓库镜像数
        :type RegistryImageCount: int
        :param Category: 漏洞子类型
        :type Category: str
        :param LocalNewestImageCount: 影响最新本地镜像数
        :type LocalNewestImageCount: int
        :param RegistryNewestImageCount: 影响最新仓库镜像数
        :type RegistryNewestImageCount: int
        :param PocID: 漏洞PocID
        :type PocID: str
        :param DefenceStatus: 防御状态，NO_DEFENDED:未防御，DEFENDED:已防御
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceStatus: str
        :param DefenceScope: 漏洞防御主机范围: MANUAL:自选主机节点，ALL:全部
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceScope: str
        :param DefenceHostCount: 漏洞防御主机数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceHostCount: int
        :param DefendedCount: 已防御攻击次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DefendedCount: int
        :param ScanStatus: 是否已扫描，NOT_SCAN:未扫描,SCANNED:已扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanStatus: str
        """
        self.CVEID = None
        self.Name = None
        self.Tags = None
        self.CategoryType = None
        self.Level = None
        self.SubmitTime = None
        self.Description = None
        self.CVSSV3Desc = None
        self.OfficialSolution = None
        self.DefenseSolution = None
        self.Reference = None
        self.CVSSV3Score = None
        self.ComponentList = None
        self.LocalImageCount = None
        self.ContainerCount = None
        self.RegistryImageCount = None
        self.Category = None
        self.LocalNewestImageCount = None
        self.RegistryNewestImageCount = None
        self.PocID = None
        self.DefenceStatus = None
        self.DefenceScope = None
        self.DefenceHostCount = None
        self.DefendedCount = None
        self.ScanStatus = None


    def _deserialize(self, params):
        self.CVEID = params.get("CVEID")
        self.Name = params.get("Name")
        self.Tags = params.get("Tags")
        self.CategoryType = params.get("CategoryType")
        self.Level = params.get("Level")
        self.SubmitTime = params.get("SubmitTime")
        self.Description = params.get("Description")
        self.CVSSV3Desc = params.get("CVSSV3Desc")
        self.OfficialSolution = params.get("OfficialSolution")
        self.DefenseSolution = params.get("DefenseSolution")
        self.Reference = params.get("Reference")
        self.CVSSV3Score = params.get("CVSSV3Score")
        if params.get("ComponentList") is not None:
            self.ComponentList = []
            for item in params.get("ComponentList"):
                obj = VulAffectedComponentInfo()
                obj._deserialize(item)
                self.ComponentList.append(obj)
        self.LocalImageCount = params.get("LocalImageCount")
        self.ContainerCount = params.get("ContainerCount")
        self.RegistryImageCount = params.get("RegistryImageCount")
        self.Category = params.get("Category")
        self.LocalNewestImageCount = params.get("LocalNewestImageCount")
        self.RegistryNewestImageCount = params.get("RegistryNewestImageCount")
        self.PocID = params.get("PocID")
        self.DefenceStatus = params.get("DefenceStatus")
        self.DefenceScope = params.get("DefenceScope")
        self.DefenceHostCount = params.get("DefenceHostCount")
        self.DefendedCount = params.get("DefendedCount")
        self.ScanStatus = params.get("ScanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulIgnoreLocalImage(AbstractModel):
    """漏洞扫描忽略的本地镜像

    """

    def __init__(self):
        r"""
        :param ID: 记录ID
        :type ID: int
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageSize: 镜像大小
        :type ImageSize: int
        :param PocID: 漏洞PocID
        :type PocID: str
        """
        self.ID = None
        self.ImageID = None
        self.ImageName = None
        self.ImageSize = None
        self.PocID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.ImageSize = params.get("ImageSize")
        self.PocID = params.get("PocID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulIgnoreRegistryImage(AbstractModel):
    """漏洞扫描忽略的仓库镜像

    """

    def __init__(self):
        r"""
        :param ID: 记录ID
        :type ID: int
        :param RegistryName: 仓库名称
        :type RegistryName: str
        :param ImageVersion: 镜像版本
        :type ImageVersion: str
        :param RegistryPath: 仓库地址
        :type RegistryPath: str
        :param ImageID: 镜像ID
        :type ImageID: str
        :param PocID: 漏洞PocID
        :type PocID: str
        """
        self.ID = None
        self.RegistryName = None
        self.ImageVersion = None
        self.RegistryPath = None
        self.ImageID = None
        self.PocID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.RegistryName = params.get("RegistryName")
        self.ImageVersion = params.get("ImageVersion")
        self.RegistryPath = params.get("RegistryPath")
        self.ImageID = params.get("ImageID")
        self.PocID = params.get("PocID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulInfo(AbstractModel):
    """漏洞列表信息

    """

    def __init__(self):
        r"""
        :param Name: 漏洞名称
        :type Name: str
        :param Tags: 漏洞标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param CVSSV3Score: CVSS V3分数
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSV3Score: float
        :param Level: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param CVEID: CVE编号
        :type CVEID: str
        :param Category: 漏洞子类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param FoundTime: 首次发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FoundTime: str
        :param LatestFoundTime: 最近发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestFoundTime: str
        :param ID: 漏洞ID
        :type ID: int
        :param LocalImageCount: 影响本地镜像数
        :type LocalImageCount: int
        :param ContainerCount: 影响容器数
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerCount: int
        :param RegistryImageCount: 影响仓库镜像数
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryImageCount: int
        :param PocID: 漏洞PocID
注意：此字段可能返回 null，表示取不到有效值。
        :type PocID: str
        :param DefenceStatus: 防御状态，NO_DEFENDED:未防御，DEFENDED:已防御
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceStatus: str
        :param DefenceScope: 漏洞防御主机范围: MANUAL:自选主机节点，ALL:全部
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceScope: str
        :param DefenceHostCount: 漏洞防御主机数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenceHostCount: int
        :param DefendedCount: 已防御攻击次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DefendedCount: int
        """
        self.Name = None
        self.Tags = None
        self.CVSSV3Score = None
        self.Level = None
        self.CVEID = None
        self.Category = None
        self.FoundTime = None
        self.LatestFoundTime = None
        self.ID = None
        self.LocalImageCount = None
        self.ContainerCount = None
        self.RegistryImageCount = None
        self.PocID = None
        self.DefenceStatus = None
        self.DefenceScope = None
        self.DefenceHostCount = None
        self.DefendedCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Tags = params.get("Tags")
        self.CVSSV3Score = params.get("CVSSV3Score")
        self.Level = params.get("Level")
        self.CVEID = params.get("CVEID")
        self.Category = params.get("Category")
        self.FoundTime = params.get("FoundTime")
        self.LatestFoundTime = params.get("LatestFoundTime")
        self.ID = params.get("ID")
        self.LocalImageCount = params.get("LocalImageCount")
        self.ContainerCount = params.get("ContainerCount")
        self.RegistryImageCount = params.get("RegistryImageCount")
        self.PocID = params.get("PocID")
        self.DefenceStatus = params.get("DefenceStatus")
        self.DefenceScope = params.get("DefenceScope")
        self.DefenceHostCount = params.get("DefenceHostCount")
        self.DefendedCount = params.get("DefendedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulScanImageInfo(AbstractModel):
    """漏洞扫描的镜像信息

    """

    def __init__(self):
        r"""
        :param ImageID: 镜像ID
        :type ImageID: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param Size: 镜像大小
        :type Size: float
        :param ScanStatus: 任务状态:SCANNING:扫描中 FAILED:失败 FINISHED:完成 CANCELED:取消
        :type ScanStatus: str
        :param ScanDuration: 扫描时长
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanDuration: float
        :param HighLevelVulCount: 高危漏洞数
        :type HighLevelVulCount: int
        :param MediumLevelVulCount: 中危漏洞数
        :type MediumLevelVulCount: int
        :param LowLevelVulCount: 低危漏洞数
        :type LowLevelVulCount: int
        :param CriticalLevelVulCount: 严重漏洞数
        :type CriticalLevelVulCount: int
        :param TaskID: 本地镜像漏洞扫描任务ID
        :type TaskID: int
        :param ScanStartTime: 漏洞扫描的开始时间
        :type ScanStartTime: str
        :param ScanEndTime: 漏洞扫描的结束时间
        :type ScanEndTime: str
        :param ErrorStatus: 失败原因:TIMEOUT:超时 TOO_MANY:任务过多 OFFLINE:离线
        :type ErrorStatus: str
        """
        self.ImageID = None
        self.ImageName = None
        self.Size = None
        self.ScanStatus = None
        self.ScanDuration = None
        self.HighLevelVulCount = None
        self.MediumLevelVulCount = None
        self.LowLevelVulCount = None
        self.CriticalLevelVulCount = None
        self.TaskID = None
        self.ScanStartTime = None
        self.ScanEndTime = None
        self.ErrorStatus = None


    def _deserialize(self, params):
        self.ImageID = params.get("ImageID")
        self.ImageName = params.get("ImageName")
        self.Size = params.get("Size")
        self.ScanStatus = params.get("ScanStatus")
        self.ScanDuration = params.get("ScanDuration")
        self.HighLevelVulCount = params.get("HighLevelVulCount")
        self.MediumLevelVulCount = params.get("MediumLevelVulCount")
        self.LowLevelVulCount = params.get("LowLevelVulCount")
        self.CriticalLevelVulCount = params.get("CriticalLevelVulCount")
        self.TaskID = params.get("TaskID")
        self.ScanStartTime = params.get("ScanStartTime")
        self.ScanEndTime = params.get("ScanEndTime")
        self.ErrorStatus = params.get("ErrorStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulTendencyInfo(AbstractModel):
    """漏洞趋势信息

    """

    def __init__(self):
        r"""
        :param VulSet: 漏洞趋势列表
        :type VulSet: list of RunTimeTendencyInfo
        :param ImageType: 漏洞影响的镜像类型：
LOCAL：本地镜像
REGISTRY: 仓库镜像
        :type ImageType: str
        """
        self.VulSet = None
        self.ImageType = None


    def _deserialize(self, params):
        if params.get("VulSet") is not None:
            self.VulSet = []
            for item in params.get("VulSet"):
                obj = RunTimeTendencyInfo()
                obj._deserialize(item)
                self.VulSet.append(obj)
        self.ImageType = params.get("ImageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulTopRankingInfo(AbstractModel):
    """漏洞Top排名信息

    """

    def __init__(self):
        r"""
        :param VulName: 漏洞名称
        :type VulName: str
        :param Level: 威胁等级,CRITICAL:严重 HIGH:高/MIDDLE:中/LOW:低
        :type Level: str
        :param AffectedImageCount: 影响的镜像数
        :type AffectedImageCount: int
        :param AffectedContainerCount: 影响的容器数
        :type AffectedContainerCount: int
        :param ID: 漏洞ID
        :type ID: int
        :param PocID: 漏洞PocID
        :type PocID: str
        """
        self.VulName = None
        self.Level = None
        self.AffectedImageCount = None
        self.AffectedContainerCount = None
        self.ID = None
        self.PocID = None


    def _deserialize(self, params):
        self.VulName = params.get("VulName")
        self.Level = params.get("Level")
        self.AffectedImageCount = params.get("AffectedImageCount")
        self.AffectedContainerCount = params.get("AffectedContainerCount")
        self.ID = params.get("ID")
        self.PocID = params.get("PocID")
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
        