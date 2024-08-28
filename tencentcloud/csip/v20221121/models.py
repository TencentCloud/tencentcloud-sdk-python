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


class AddNewBindRoleUserRequest(AbstractModel):
    """AddNewBindRoleUser请求参数结构体

    """


class AddNewBindRoleUserResponse(AbstractModel):
    """AddNewBindRoleUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0成功，其他失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class AlertExtraInfo(AbstractModel):
    """告警下拉字段

    """

    def __init__(self):
        r"""
        :param _RelateEvent: 相关攻击事件
注意：此字段可能返回 null，表示取不到有效值。
        :type RelateEvent: :class:`tencentcloud.csip.v20221121.models.RelatedEvent`
        :param _LeakContent: 泄漏内容
注意：此字段可能返回 null，表示取不到有效值。
        :type LeakContent: str
        :param _LeakAPI: 泄漏API
注意：此字段可能返回 null，表示取不到有效值。
        :type LeakAPI: str
        :param _SecretID: secretID
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretID: str
        :param _Rule: 命中规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: str
        :param _RuleDesc: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDesc: str
        :param _ProtocolPort: 协议端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolPort: str
        :param _AttackContent: 攻击内容
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackContent: str
        :param _AttackIPProfile: 攻击IP画像
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackIPProfile: str
        :param _AttackIPTags: 攻击IP标签
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackIPTags: str
        :param _RequestMethod: 请求方式
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestMethod: str
        :param _HttpLog: HTTP日志
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpLog: str
        :param _AttackDomain: 被攻击域名
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackDomain: str
        :param _FilePath: 文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param _UserAgent: user_agent
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAgent: str
        :param _RequestHeaders: 请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeaders: str
        :param _LoginUserName: 登录用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginUserName: str
        :param _VulnerabilityName: 漏洞名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityName: str
        :param _CVE: 公共漏洞和暴露
注意：此字段可能返回 null，表示取不到有效值。
        :type CVE: str
        :param _ServiceProcess: 服务进程
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceProcess: str
        :param _FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileSize: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: str
        :param _FileMD5: 文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMD5: str
        :param _FileLastAccessTime: 文件最近访问时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FileLastAccessTime: str
        :param _FileModifyTime: 文件修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FileModifyTime: str
        :param _RecentAccessTime: 最近访问时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RecentAccessTime: str
        :param _RecentModifyTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RecentModifyTime: str
        :param _VirusName: 病毒名
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusName: str
        :param _VirusFileTags: 病毒文件标签
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusFileTags: str
        :param _BehavioralCharacteristics: 行为特征
注意：此字段可能返回 null，表示取不到有效值。
        :type BehavioralCharacteristics: str
        :param _ProcessNamePID: 进程名（PID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessNamePID: str
        :param _ProcessPath: 进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessPath: str
        :param _ProcessCommandLine: 进程命令行
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessCommandLine: str
        :param _ProcessPermissions: 进程权限
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessPermissions: str
        :param _ExecutedCommand: 执行命令
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutedCommand: str
        :param _AffectedFileName: 受影响文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedFileName: str
        :param _DecoyPath: 诱饵路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DecoyPath: str
        :param _MaliciousProcessFileSize: 恶意进程文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MaliciousProcessFileSize: str
        :param _MaliciousProcessFileMD5: 恶意进程文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type MaliciousProcessFileMD5: str
        :param _MaliciousProcessNamePID: 恶意进程名（PID）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaliciousProcessNamePID: str
        :param _MaliciousProcessPath: 恶意进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type MaliciousProcessPath: str
        :param _MaliciousProcessStartTime: 恶意进程启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MaliciousProcessStartTime: str
        :param _CommandContent: 命令内容
注意：此字段可能返回 null，表示取不到有效值。
        :type CommandContent: str
        :param _StartupUser: 启动用户
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupUser: str
        :param _UserGroup: 用户所属组
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroup: str
        :param _NewPermissions: 新增权限
注意：此字段可能返回 null，表示取不到有效值。
        :type NewPermissions: str
        :param _ParentProcess: 父进程
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentProcess: str
        :param _ClassName: 类名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassName: str
        :param _ClassLoader: 所属类加载器
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassLoader: str
        :param _ClassFileSize: 类文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassFileSize: str
        :param _ClassFileMD5: 类文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassFileMD5: str
        :param _ParentClassName: 父类名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentClassName: str
        :param _InheritedInterface: 继承接口
注意：此字段可能返回 null，表示取不到有效值。
        :type InheritedInterface: str
        :param _Comment: 注释
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _PayloadContent: 载荷内容
注意：此字段可能返回 null，表示取不到有效值。
        :type PayloadContent: str
        :param _CallbackAddressPortrait: 回连地址画像
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackAddressPortrait: str
        :param _CallbackAddressTag: 回连地址标签
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackAddressTag: str
        :param _ProcessMD5: 进程MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessMD5: str
        :param _FilePermission: 文件权限
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePermission: str
        :param _FromLogAnalysisData: 来源于日志分析的信息字段
注意：此字段可能返回 null，表示取不到有效值。
        :type FromLogAnalysisData: list of KeyValue
        :param _HitProbe: 命中探针
注意：此字段可能返回 null，表示取不到有效值。
        :type HitProbe: str
        :param _HitHoneyPot: 命中蜜罐

注意：此字段可能返回 null，表示取不到有效值。
        :type HitHoneyPot: str
        :param _CommandList: 命令列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CommandList: str
        :param _AttackEventDesc: 攻击事件描述

注意：此字段可能返回 null，表示取不到有效值。
        :type AttackEventDesc: str
        :param _ProcessInfo: 进程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessInfo: str
        :param _UserNameAndPwd: 使用用户名&密码
注意：此字段可能返回 null，表示取不到有效值。
        :type UserNameAndPwd: str
        :param _StrategyID: 主机防护策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyID: str
        :param _StrategyName: 主机防护策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyName: str
        :param _HitStrategy: 主机防护命中策略，是策略ID和策略名称的组合
注意：此字段可能返回 null，表示取不到有效值。
        :type HitStrategy: str
        :param _ProcessName: 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessName: str
        :param _PID: PID
注意：此字段可能返回 null，表示取不到有效值。
        :type PID: str
        :param _PodName: 容器Pod名
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param _PodID: 容器PodID
注意：此字段可能返回 null，表示取不到有效值。
        :type PodID: str
        :param _Response: Http响应
注意：此字段可能返回 null，表示取不到有效值。
        :type Response: str
        :param _SystemCall: 系统调用
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemCall: str
        :param _Verb: 操作类型verb
注意：此字段可能返回 null，表示取不到有效值。
        :type Verb: str
        :param _LogID: 日志ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogID: str
        :param _Different: 变更内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Different: str
        :param _EventType: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EventType: str
        :param _Description: 事件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _TargetAddress: 目标地址(容器反弹shell)
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAddress: str
        :param _MaliciousRequestDomain: 恶意请求域名(容器恶意外联)
注意：此字段可能返回 null，表示取不到有效值。
        :type MaliciousRequestDomain: str
        :param _RuleType: 规则类型(容器K8sAPI异常请求)
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RequestURI: 请求资源(容器K8sAPI异常请求)
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestURI: str
        :param _RequestUser: 发起请求用户(容器K8sAPI异常请求)
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestUser: str
        :param _RequestObject: 请求对象(容器K8sAPI异常请求)
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestObject: str
        :param _ResponseObject: 响应对象(容器K8sAPI异常请求)
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseObject: str
        :param _FileType: 文件类型(容器文件篡改)
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _TIType: 标签特征(容器恶意外联)
注意：此字段可能返回 null，表示取不到有效值。
        :type TIType: str
        :param _SourceIP: 来源IP(容器K8sAPI异常请求)
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceIP: str
        """
        self._RelateEvent = None
        self._LeakContent = None
        self._LeakAPI = None
        self._SecretID = None
        self._Rule = None
        self._RuleDesc = None
        self._ProtocolPort = None
        self._AttackContent = None
        self._AttackIPProfile = None
        self._AttackIPTags = None
        self._RequestMethod = None
        self._HttpLog = None
        self._AttackDomain = None
        self._FilePath = None
        self._UserAgent = None
        self._RequestHeaders = None
        self._LoginUserName = None
        self._VulnerabilityName = None
        self._CVE = None
        self._ServiceProcess = None
        self._FileName = None
        self._FileSize = None
        self._FileMD5 = None
        self._FileLastAccessTime = None
        self._FileModifyTime = None
        self._RecentAccessTime = None
        self._RecentModifyTime = None
        self._VirusName = None
        self._VirusFileTags = None
        self._BehavioralCharacteristics = None
        self._ProcessNamePID = None
        self._ProcessPath = None
        self._ProcessCommandLine = None
        self._ProcessPermissions = None
        self._ExecutedCommand = None
        self._AffectedFileName = None
        self._DecoyPath = None
        self._MaliciousProcessFileSize = None
        self._MaliciousProcessFileMD5 = None
        self._MaliciousProcessNamePID = None
        self._MaliciousProcessPath = None
        self._MaliciousProcessStartTime = None
        self._CommandContent = None
        self._StartupUser = None
        self._UserGroup = None
        self._NewPermissions = None
        self._ParentProcess = None
        self._ClassName = None
        self._ClassLoader = None
        self._ClassFileSize = None
        self._ClassFileMD5 = None
        self._ParentClassName = None
        self._InheritedInterface = None
        self._Comment = None
        self._PayloadContent = None
        self._CallbackAddressPortrait = None
        self._CallbackAddressTag = None
        self._ProcessMD5 = None
        self._FilePermission = None
        self._FromLogAnalysisData = None
        self._HitProbe = None
        self._HitHoneyPot = None
        self._CommandList = None
        self._AttackEventDesc = None
        self._ProcessInfo = None
        self._UserNameAndPwd = None
        self._StrategyID = None
        self._StrategyName = None
        self._HitStrategy = None
        self._ProcessName = None
        self._PID = None
        self._PodName = None
        self._PodID = None
        self._Response = None
        self._SystemCall = None
        self._Verb = None
        self._LogID = None
        self._Different = None
        self._EventType = None
        self._Description = None
        self._TargetAddress = None
        self._MaliciousRequestDomain = None
        self._RuleType = None
        self._RequestURI = None
        self._RequestUser = None
        self._RequestObject = None
        self._ResponseObject = None
        self._FileType = None
        self._TIType = None
        self._SourceIP = None

    @property
    def RelateEvent(self):
        return self._RelateEvent

    @RelateEvent.setter
    def RelateEvent(self, RelateEvent):
        self._RelateEvent = RelateEvent

    @property
    def LeakContent(self):
        return self._LeakContent

    @LeakContent.setter
    def LeakContent(self, LeakContent):
        self._LeakContent = LeakContent

    @property
    def LeakAPI(self):
        return self._LeakAPI

    @LeakAPI.setter
    def LeakAPI(self, LeakAPI):
        self._LeakAPI = LeakAPI

    @property
    def SecretID(self):
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RuleDesc(self):
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def ProtocolPort(self):
        return self._ProtocolPort

    @ProtocolPort.setter
    def ProtocolPort(self, ProtocolPort):
        self._ProtocolPort = ProtocolPort

    @property
    def AttackContent(self):
        return self._AttackContent

    @AttackContent.setter
    def AttackContent(self, AttackContent):
        self._AttackContent = AttackContent

    @property
    def AttackIPProfile(self):
        return self._AttackIPProfile

    @AttackIPProfile.setter
    def AttackIPProfile(self, AttackIPProfile):
        self._AttackIPProfile = AttackIPProfile

    @property
    def AttackIPTags(self):
        return self._AttackIPTags

    @AttackIPTags.setter
    def AttackIPTags(self, AttackIPTags):
        self._AttackIPTags = AttackIPTags

    @property
    def RequestMethod(self):
        return self._RequestMethod

    @RequestMethod.setter
    def RequestMethod(self, RequestMethod):
        self._RequestMethod = RequestMethod

    @property
    def HttpLog(self):
        return self._HttpLog

    @HttpLog.setter
    def HttpLog(self, HttpLog):
        self._HttpLog = HttpLog

    @property
    def AttackDomain(self):
        return self._AttackDomain

    @AttackDomain.setter
    def AttackDomain(self, AttackDomain):
        self._AttackDomain = AttackDomain

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def RequestHeaders(self):
        return self._RequestHeaders

    @RequestHeaders.setter
    def RequestHeaders(self, RequestHeaders):
        self._RequestHeaders = RequestHeaders

    @property
    def LoginUserName(self):
        return self._LoginUserName

    @LoginUserName.setter
    def LoginUserName(self, LoginUserName):
        self._LoginUserName = LoginUserName

    @property
    def VulnerabilityName(self):
        return self._VulnerabilityName

    @VulnerabilityName.setter
    def VulnerabilityName(self, VulnerabilityName):
        self._VulnerabilityName = VulnerabilityName

    @property
    def CVE(self):
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def ServiceProcess(self):
        return self._ServiceProcess

    @ServiceProcess.setter
    def ServiceProcess(self, ServiceProcess):
        self._ServiceProcess = ServiceProcess

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileMD5(self):
        return self._FileMD5

    @FileMD5.setter
    def FileMD5(self, FileMD5):
        self._FileMD5 = FileMD5

    @property
    def FileLastAccessTime(self):
        return self._FileLastAccessTime

    @FileLastAccessTime.setter
    def FileLastAccessTime(self, FileLastAccessTime):
        self._FileLastAccessTime = FileLastAccessTime

    @property
    def FileModifyTime(self):
        return self._FileModifyTime

    @FileModifyTime.setter
    def FileModifyTime(self, FileModifyTime):
        self._FileModifyTime = FileModifyTime

    @property
    def RecentAccessTime(self):
        return self._RecentAccessTime

    @RecentAccessTime.setter
    def RecentAccessTime(self, RecentAccessTime):
        self._RecentAccessTime = RecentAccessTime

    @property
    def RecentModifyTime(self):
        return self._RecentModifyTime

    @RecentModifyTime.setter
    def RecentModifyTime(self, RecentModifyTime):
        self._RecentModifyTime = RecentModifyTime

    @property
    def VirusName(self):
        return self._VirusName

    @VirusName.setter
    def VirusName(self, VirusName):
        self._VirusName = VirusName

    @property
    def VirusFileTags(self):
        return self._VirusFileTags

    @VirusFileTags.setter
    def VirusFileTags(self, VirusFileTags):
        self._VirusFileTags = VirusFileTags

    @property
    def BehavioralCharacteristics(self):
        return self._BehavioralCharacteristics

    @BehavioralCharacteristics.setter
    def BehavioralCharacteristics(self, BehavioralCharacteristics):
        self._BehavioralCharacteristics = BehavioralCharacteristics

    @property
    def ProcessNamePID(self):
        return self._ProcessNamePID

    @ProcessNamePID.setter
    def ProcessNamePID(self, ProcessNamePID):
        self._ProcessNamePID = ProcessNamePID

    @property
    def ProcessPath(self):
        return self._ProcessPath

    @ProcessPath.setter
    def ProcessPath(self, ProcessPath):
        self._ProcessPath = ProcessPath

    @property
    def ProcessCommandLine(self):
        return self._ProcessCommandLine

    @ProcessCommandLine.setter
    def ProcessCommandLine(self, ProcessCommandLine):
        self._ProcessCommandLine = ProcessCommandLine

    @property
    def ProcessPermissions(self):
        return self._ProcessPermissions

    @ProcessPermissions.setter
    def ProcessPermissions(self, ProcessPermissions):
        self._ProcessPermissions = ProcessPermissions

    @property
    def ExecutedCommand(self):
        return self._ExecutedCommand

    @ExecutedCommand.setter
    def ExecutedCommand(self, ExecutedCommand):
        self._ExecutedCommand = ExecutedCommand

    @property
    def AffectedFileName(self):
        return self._AffectedFileName

    @AffectedFileName.setter
    def AffectedFileName(self, AffectedFileName):
        self._AffectedFileName = AffectedFileName

    @property
    def DecoyPath(self):
        return self._DecoyPath

    @DecoyPath.setter
    def DecoyPath(self, DecoyPath):
        self._DecoyPath = DecoyPath

    @property
    def MaliciousProcessFileSize(self):
        return self._MaliciousProcessFileSize

    @MaliciousProcessFileSize.setter
    def MaliciousProcessFileSize(self, MaliciousProcessFileSize):
        self._MaliciousProcessFileSize = MaliciousProcessFileSize

    @property
    def MaliciousProcessFileMD5(self):
        return self._MaliciousProcessFileMD5

    @MaliciousProcessFileMD5.setter
    def MaliciousProcessFileMD5(self, MaliciousProcessFileMD5):
        self._MaliciousProcessFileMD5 = MaliciousProcessFileMD5

    @property
    def MaliciousProcessNamePID(self):
        return self._MaliciousProcessNamePID

    @MaliciousProcessNamePID.setter
    def MaliciousProcessNamePID(self, MaliciousProcessNamePID):
        self._MaliciousProcessNamePID = MaliciousProcessNamePID

    @property
    def MaliciousProcessPath(self):
        return self._MaliciousProcessPath

    @MaliciousProcessPath.setter
    def MaliciousProcessPath(self, MaliciousProcessPath):
        self._MaliciousProcessPath = MaliciousProcessPath

    @property
    def MaliciousProcessStartTime(self):
        return self._MaliciousProcessStartTime

    @MaliciousProcessStartTime.setter
    def MaliciousProcessStartTime(self, MaliciousProcessStartTime):
        self._MaliciousProcessStartTime = MaliciousProcessStartTime

    @property
    def CommandContent(self):
        return self._CommandContent

    @CommandContent.setter
    def CommandContent(self, CommandContent):
        self._CommandContent = CommandContent

    @property
    def StartupUser(self):
        return self._StartupUser

    @StartupUser.setter
    def StartupUser(self, StartupUser):
        self._StartupUser = StartupUser

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def NewPermissions(self):
        return self._NewPermissions

    @NewPermissions.setter
    def NewPermissions(self, NewPermissions):
        self._NewPermissions = NewPermissions

    @property
    def ParentProcess(self):
        return self._ParentProcess

    @ParentProcess.setter
    def ParentProcess(self, ParentProcess):
        self._ParentProcess = ParentProcess

    @property
    def ClassName(self):
        return self._ClassName

    @ClassName.setter
    def ClassName(self, ClassName):
        self._ClassName = ClassName

    @property
    def ClassLoader(self):
        return self._ClassLoader

    @ClassLoader.setter
    def ClassLoader(self, ClassLoader):
        self._ClassLoader = ClassLoader

    @property
    def ClassFileSize(self):
        return self._ClassFileSize

    @ClassFileSize.setter
    def ClassFileSize(self, ClassFileSize):
        self._ClassFileSize = ClassFileSize

    @property
    def ClassFileMD5(self):
        return self._ClassFileMD5

    @ClassFileMD5.setter
    def ClassFileMD5(self, ClassFileMD5):
        self._ClassFileMD5 = ClassFileMD5

    @property
    def ParentClassName(self):
        return self._ParentClassName

    @ParentClassName.setter
    def ParentClassName(self, ParentClassName):
        self._ParentClassName = ParentClassName

    @property
    def InheritedInterface(self):
        return self._InheritedInterface

    @InheritedInterface.setter
    def InheritedInterface(self, InheritedInterface):
        self._InheritedInterface = InheritedInterface

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def PayloadContent(self):
        return self._PayloadContent

    @PayloadContent.setter
    def PayloadContent(self, PayloadContent):
        self._PayloadContent = PayloadContent

    @property
    def CallbackAddressPortrait(self):
        return self._CallbackAddressPortrait

    @CallbackAddressPortrait.setter
    def CallbackAddressPortrait(self, CallbackAddressPortrait):
        self._CallbackAddressPortrait = CallbackAddressPortrait

    @property
    def CallbackAddressTag(self):
        return self._CallbackAddressTag

    @CallbackAddressTag.setter
    def CallbackAddressTag(self, CallbackAddressTag):
        self._CallbackAddressTag = CallbackAddressTag

    @property
    def ProcessMD5(self):
        return self._ProcessMD5

    @ProcessMD5.setter
    def ProcessMD5(self, ProcessMD5):
        self._ProcessMD5 = ProcessMD5

    @property
    def FilePermission(self):
        return self._FilePermission

    @FilePermission.setter
    def FilePermission(self, FilePermission):
        self._FilePermission = FilePermission

    @property
    def FromLogAnalysisData(self):
        return self._FromLogAnalysisData

    @FromLogAnalysisData.setter
    def FromLogAnalysisData(self, FromLogAnalysisData):
        self._FromLogAnalysisData = FromLogAnalysisData

    @property
    def HitProbe(self):
        return self._HitProbe

    @HitProbe.setter
    def HitProbe(self, HitProbe):
        self._HitProbe = HitProbe

    @property
    def HitHoneyPot(self):
        return self._HitHoneyPot

    @HitHoneyPot.setter
    def HitHoneyPot(self, HitHoneyPot):
        self._HitHoneyPot = HitHoneyPot

    @property
    def CommandList(self):
        return self._CommandList

    @CommandList.setter
    def CommandList(self, CommandList):
        self._CommandList = CommandList

    @property
    def AttackEventDesc(self):
        return self._AttackEventDesc

    @AttackEventDesc.setter
    def AttackEventDesc(self, AttackEventDesc):
        self._AttackEventDesc = AttackEventDesc

    @property
    def ProcessInfo(self):
        return self._ProcessInfo

    @ProcessInfo.setter
    def ProcessInfo(self, ProcessInfo):
        self._ProcessInfo = ProcessInfo

    @property
    def UserNameAndPwd(self):
        return self._UserNameAndPwd

    @UserNameAndPwd.setter
    def UserNameAndPwd(self, UserNameAndPwd):
        self._UserNameAndPwd = UserNameAndPwd

    @property
    def StrategyID(self):
        return self._StrategyID

    @StrategyID.setter
    def StrategyID(self, StrategyID):
        self._StrategyID = StrategyID

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def HitStrategy(self):
        return self._HitStrategy

    @HitStrategy.setter
    def HitStrategy(self, HitStrategy):
        self._HitStrategy = HitStrategy

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def PID(self):
        return self._PID

    @PID.setter
    def PID(self, PID):
        self._PID = PID

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def PodID(self):
        return self._PodID

    @PodID.setter
    def PodID(self, PodID):
        self._PodID = PodID

    @property
    def Response(self):
        return self._Response

    @Response.setter
    def Response(self, Response):
        self._Response = Response

    @property
    def SystemCall(self):
        return self._SystemCall

    @SystemCall.setter
    def SystemCall(self, SystemCall):
        self._SystemCall = SystemCall

    @property
    def Verb(self):
        return self._Verb

    @Verb.setter
    def Verb(self, Verb):
        self._Verb = Verb

    @property
    def LogID(self):
        return self._LogID

    @LogID.setter
    def LogID(self, LogID):
        self._LogID = LogID

    @property
    def Different(self):
        return self._Different

    @Different.setter
    def Different(self, Different):
        self._Different = Different

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TargetAddress(self):
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress

    @property
    def MaliciousRequestDomain(self):
        return self._MaliciousRequestDomain

    @MaliciousRequestDomain.setter
    def MaliciousRequestDomain(self, MaliciousRequestDomain):
        self._MaliciousRequestDomain = MaliciousRequestDomain

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RequestURI(self):
        return self._RequestURI

    @RequestURI.setter
    def RequestURI(self, RequestURI):
        self._RequestURI = RequestURI

    @property
    def RequestUser(self):
        return self._RequestUser

    @RequestUser.setter
    def RequestUser(self, RequestUser):
        self._RequestUser = RequestUser

    @property
    def RequestObject(self):
        return self._RequestObject

    @RequestObject.setter
    def RequestObject(self, RequestObject):
        self._RequestObject = RequestObject

    @property
    def ResponseObject(self):
        return self._ResponseObject

    @ResponseObject.setter
    def ResponseObject(self, ResponseObject):
        self._ResponseObject = ResponseObject

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def TIType(self):
        return self._TIType

    @TIType.setter
    def TIType(self, TIType):
        self._TIType = TIType

    @property
    def SourceIP(self):
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP


    def _deserialize(self, params):
        if params.get("RelateEvent") is not None:
            self._RelateEvent = RelatedEvent()
            self._RelateEvent._deserialize(params.get("RelateEvent"))
        self._LeakContent = params.get("LeakContent")
        self._LeakAPI = params.get("LeakAPI")
        self._SecretID = params.get("SecretID")
        self._Rule = params.get("Rule")
        self._RuleDesc = params.get("RuleDesc")
        self._ProtocolPort = params.get("ProtocolPort")
        self._AttackContent = params.get("AttackContent")
        self._AttackIPProfile = params.get("AttackIPProfile")
        self._AttackIPTags = params.get("AttackIPTags")
        self._RequestMethod = params.get("RequestMethod")
        self._HttpLog = params.get("HttpLog")
        self._AttackDomain = params.get("AttackDomain")
        self._FilePath = params.get("FilePath")
        self._UserAgent = params.get("UserAgent")
        self._RequestHeaders = params.get("RequestHeaders")
        self._LoginUserName = params.get("LoginUserName")
        self._VulnerabilityName = params.get("VulnerabilityName")
        self._CVE = params.get("CVE")
        self._ServiceProcess = params.get("ServiceProcess")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._FileMD5 = params.get("FileMD5")
        self._FileLastAccessTime = params.get("FileLastAccessTime")
        self._FileModifyTime = params.get("FileModifyTime")
        self._RecentAccessTime = params.get("RecentAccessTime")
        self._RecentModifyTime = params.get("RecentModifyTime")
        self._VirusName = params.get("VirusName")
        self._VirusFileTags = params.get("VirusFileTags")
        self._BehavioralCharacteristics = params.get("BehavioralCharacteristics")
        self._ProcessNamePID = params.get("ProcessNamePID")
        self._ProcessPath = params.get("ProcessPath")
        self._ProcessCommandLine = params.get("ProcessCommandLine")
        self._ProcessPermissions = params.get("ProcessPermissions")
        self._ExecutedCommand = params.get("ExecutedCommand")
        self._AffectedFileName = params.get("AffectedFileName")
        self._DecoyPath = params.get("DecoyPath")
        self._MaliciousProcessFileSize = params.get("MaliciousProcessFileSize")
        self._MaliciousProcessFileMD5 = params.get("MaliciousProcessFileMD5")
        self._MaliciousProcessNamePID = params.get("MaliciousProcessNamePID")
        self._MaliciousProcessPath = params.get("MaliciousProcessPath")
        self._MaliciousProcessStartTime = params.get("MaliciousProcessStartTime")
        self._CommandContent = params.get("CommandContent")
        self._StartupUser = params.get("StartupUser")
        self._UserGroup = params.get("UserGroup")
        self._NewPermissions = params.get("NewPermissions")
        self._ParentProcess = params.get("ParentProcess")
        self._ClassName = params.get("ClassName")
        self._ClassLoader = params.get("ClassLoader")
        self._ClassFileSize = params.get("ClassFileSize")
        self._ClassFileMD5 = params.get("ClassFileMD5")
        self._ParentClassName = params.get("ParentClassName")
        self._InheritedInterface = params.get("InheritedInterface")
        self._Comment = params.get("Comment")
        self._PayloadContent = params.get("PayloadContent")
        self._CallbackAddressPortrait = params.get("CallbackAddressPortrait")
        self._CallbackAddressTag = params.get("CallbackAddressTag")
        self._ProcessMD5 = params.get("ProcessMD5")
        self._FilePermission = params.get("FilePermission")
        if params.get("FromLogAnalysisData") is not None:
            self._FromLogAnalysisData = []
            for item in params.get("FromLogAnalysisData"):
                obj = KeyValue()
                obj._deserialize(item)
                self._FromLogAnalysisData.append(obj)
        self._HitProbe = params.get("HitProbe")
        self._HitHoneyPot = params.get("HitHoneyPot")
        self._CommandList = params.get("CommandList")
        self._AttackEventDesc = params.get("AttackEventDesc")
        self._ProcessInfo = params.get("ProcessInfo")
        self._UserNameAndPwd = params.get("UserNameAndPwd")
        self._StrategyID = params.get("StrategyID")
        self._StrategyName = params.get("StrategyName")
        self._HitStrategy = params.get("HitStrategy")
        self._ProcessName = params.get("ProcessName")
        self._PID = params.get("PID")
        self._PodName = params.get("PodName")
        self._PodID = params.get("PodID")
        self._Response = params.get("Response")
        self._SystemCall = params.get("SystemCall")
        self._Verb = params.get("Verb")
        self._LogID = params.get("LogID")
        self._Different = params.get("Different")
        self._EventType = params.get("EventType")
        self._Description = params.get("Description")
        self._TargetAddress = params.get("TargetAddress")
        self._MaliciousRequestDomain = params.get("MaliciousRequestDomain")
        self._RuleType = params.get("RuleType")
        self._RequestURI = params.get("RequestURI")
        self._RequestUser = params.get("RequestUser")
        self._RequestObject = params.get("RequestObject")
        self._ResponseObject = params.get("ResponseObject")
        self._FileType = params.get("FileType")
        self._TIType = params.get("TIType")
        self._SourceIP = params.get("SourceIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertInfo(AbstractModel):
    """告警中心全量告警列表数据

    """

    def __init__(self):
        r"""
        :param _ID: 告警ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Name: 告警名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Source: 告警来源
CFW:云防火墙
WAF:Web应用防火墙
CWP:主机安全
CSIP:云安全中心
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _Level: 告警等级
1:提示
2:低危
3:中危
4:高危
5:严重
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _Attacker: 攻击者
注意：此字段可能返回 null，表示取不到有效值。
        :type Attacker: :class:`tencentcloud.csip.v20221121.models.RoleInfo`
        :param _Victim: 受害者
注意：此字段可能返回 null，表示取不到有效值。
        :type Victim: :class:`tencentcloud.csip.v20221121.models.RoleInfo`
        :param _EvidenceData: 证据数据(例如攻击内容等)
注意：此字段可能返回 null，表示取不到有效值。
        :type EvidenceData: str
        :param _EvidenceLocation: 证据位置(例如协议端口)
注意：此字段可能返回 null，表示取不到有效值。
        :type EvidenceLocation: str
        :param _EvidencePath: 证据路径
注意：此字段可能返回 null，表示取不到有效值。
        :type EvidencePath: str
        :param _CreateTime: 首次告警时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 最近告警时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Count: 告警次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _UrgentSuggestion: 紧急缓解建议
注意：此字段可能返回 null，表示取不到有效值。
        :type UrgentSuggestion: str
        :param _RemediationSuggestion: 根治建议
注意：此字段可能返回 null，表示取不到有效值。
        :type RemediationSuggestion: str
        :param _Status: 处理状态
0：未处置，1：已忽略，2：已处置
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ProcessType: 告警处理类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessType: str
        :param _Type: 告警大类
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _SubType: 告警小类
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param _ExtraInfo: 下拉字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: :class:`tencentcloud.csip.v20221121.models.AlertExtraInfo`
        :param _Key: 聚合字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Date: 告警日期
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param _AppID: appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppID: str
        :param _NickName: 账户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _Uin: 账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _Action: 行为
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: int
        :param _RiskInvestigation: 风险排查
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInvestigation: str
        :param _RiskTreatment: 风险处置
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskTreatment: str
        :param _LogType: 日志类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LogType: str
        :param _LogSearch: 语句检索
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSearch: str
        """
        self._ID = None
        self._Name = None
        self._Source = None
        self._Level = None
        self._Attacker = None
        self._Victim = None
        self._EvidenceData = None
        self._EvidenceLocation = None
        self._EvidencePath = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Count = None
        self._UrgentSuggestion = None
        self._RemediationSuggestion = None
        self._Status = None
        self._ProcessType = None
        self._Type = None
        self._SubType = None
        self._ExtraInfo = None
        self._Key = None
        self._Date = None
        self._AppID = None
        self._NickName = None
        self._Uin = None
        self._Action = None
        self._RiskInvestigation = None
        self._RiskTreatment = None
        self._LogType = None
        self._LogSearch = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Attacker(self):
        return self._Attacker

    @Attacker.setter
    def Attacker(self, Attacker):
        self._Attacker = Attacker

    @property
    def Victim(self):
        return self._Victim

    @Victim.setter
    def Victim(self, Victim):
        self._Victim = Victim

    @property
    def EvidenceData(self):
        return self._EvidenceData

    @EvidenceData.setter
    def EvidenceData(self, EvidenceData):
        self._EvidenceData = EvidenceData

    @property
    def EvidenceLocation(self):
        return self._EvidenceLocation

    @EvidenceLocation.setter
    def EvidenceLocation(self, EvidenceLocation):
        self._EvidenceLocation = EvidenceLocation

    @property
    def EvidencePath(self):
        return self._EvidencePath

    @EvidencePath.setter
    def EvidencePath(self, EvidencePath):
        self._EvidencePath = EvidencePath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def UrgentSuggestion(self):
        return self._UrgentSuggestion

    @UrgentSuggestion.setter
    def UrgentSuggestion(self, UrgentSuggestion):
        self._UrgentSuggestion = UrgentSuggestion

    @property
    def RemediationSuggestion(self):
        return self._RemediationSuggestion

    @RemediationSuggestion.setter
    def RemediationSuggestion(self, RemediationSuggestion):
        self._RemediationSuggestion = RemediationSuggestion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProcessType(self):
        return self._ProcessType

    @ProcessType.setter
    def ProcessType(self, ProcessType):
        self._ProcessType = ProcessType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def ExtraInfo(self):
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AppID(self):
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RiskInvestigation(self):
        return self._RiskInvestigation

    @RiskInvestigation.setter
    def RiskInvestigation(self, RiskInvestigation):
        self._RiskInvestigation = RiskInvestigation

    @property
    def RiskTreatment(self):
        return self._RiskTreatment

    @RiskTreatment.setter
    def RiskTreatment(self, RiskTreatment):
        self._RiskTreatment = RiskTreatment

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def LogSearch(self):
        return self._LogSearch

    @LogSearch.setter
    def LogSearch(self, LogSearch):
        self._LogSearch = LogSearch


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Source = params.get("Source")
        self._Level = params.get("Level")
        if params.get("Attacker") is not None:
            self._Attacker = RoleInfo()
            self._Attacker._deserialize(params.get("Attacker"))
        if params.get("Victim") is not None:
            self._Victim = RoleInfo()
            self._Victim._deserialize(params.get("Victim"))
        self._EvidenceData = params.get("EvidenceData")
        self._EvidenceLocation = params.get("EvidenceLocation")
        self._EvidencePath = params.get("EvidencePath")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Count = params.get("Count")
        self._UrgentSuggestion = params.get("UrgentSuggestion")
        self._RemediationSuggestion = params.get("RemediationSuggestion")
        self._Status = params.get("Status")
        self._ProcessType = params.get("ProcessType")
        self._Type = params.get("Type")
        self._SubType = params.get("SubType")
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = AlertExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._Key = params.get("Key")
        self._Date = params.get("Date")
        self._AppID = params.get("AppID")
        self._NickName = params.get("NickName")
        self._Uin = params.get("Uin")
        self._Action = params.get("Action")
        self._RiskInvestigation = params.get("RiskInvestigation")
        self._RiskTreatment = params.get("RiskTreatment")
        self._LogType = params.get("LogType")
        self._LogSearch = params.get("LogSearch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetBaseInfoResponse(AbstractModel):
    """主机资产详情

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc-id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc-name
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _Os: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AccountNum: 账号数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountNum: int
        :param _PortNum: 端口数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PortNum: int
        :param _ProcessNum: 进程数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessNum: int
        :param _SoftApplicationNum: 软件应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftApplicationNum: int
        :param _DatabaseNum: 数据库数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseNum: int
        :param _WebApplicationNum: Web应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebApplicationNum: int
        :param _ServiceNum: 服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceNum: int
        :param _WebFrameworkNum: web框架数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebFrameworkNum: int
        :param _WebSiteNum: Web站点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSiteNum: int
        :param _JarPackageNum: Jar包数量
注意：此字段可能返回 null，表示取不到有效值。
        :type JarPackageNum: int
        :param _StartServiceNum: 启动服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StartServiceNum: int
        :param _ScheduledTaskNum: 计划任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledTaskNum: int
        :param _EnvironmentVariableNum: 环境变量数量
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentVariableNum: int
        :param _KernelModuleNum: 内核模块数量
注意：此字段可能返回 null，表示取不到有效值。
        :type KernelModuleNum: int
        :param _SystemInstallationPackageNum: 系统安装包数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemInstallationPackageNum: int
        :param _SurplusProtectDay: 剩余防护时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SurplusProtectDay: int
        :param _CWPStatus: 客户端是否安装  1 已安装 0 未安装
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPStatus: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _ProtectLevel: 防护等级
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectLevel: str
        :param _ProtectedDay: 防护时长
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectedDay: int
        """
        self._VpcId = None
        self._VpcName = None
        self._AssetName = None
        self._Os = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Region = None
        self._AssetType = None
        self._AssetId = None
        self._AccountNum = None
        self._PortNum = None
        self._ProcessNum = None
        self._SoftApplicationNum = None
        self._DatabaseNum = None
        self._WebApplicationNum = None
        self._ServiceNum = None
        self._WebFrameworkNum = None
        self._WebSiteNum = None
        self._JarPackageNum = None
        self._StartServiceNum = None
        self._ScheduledTaskNum = None
        self._EnvironmentVariableNum = None
        self._KernelModuleNum = None
        self._SystemInstallationPackageNum = None
        self._SurplusProtectDay = None
        self._CWPStatus = None
        self._Tag = None
        self._ProtectLevel = None
        self._ProtectedDay = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AccountNum(self):
        return self._AccountNum

    @AccountNum.setter
    def AccountNum(self, AccountNum):
        self._AccountNum = AccountNum

    @property
    def PortNum(self):
        return self._PortNum

    @PortNum.setter
    def PortNum(self, PortNum):
        self._PortNum = PortNum

    @property
    def ProcessNum(self):
        return self._ProcessNum

    @ProcessNum.setter
    def ProcessNum(self, ProcessNum):
        self._ProcessNum = ProcessNum

    @property
    def SoftApplicationNum(self):
        return self._SoftApplicationNum

    @SoftApplicationNum.setter
    def SoftApplicationNum(self, SoftApplicationNum):
        self._SoftApplicationNum = SoftApplicationNum

    @property
    def DatabaseNum(self):
        return self._DatabaseNum

    @DatabaseNum.setter
    def DatabaseNum(self, DatabaseNum):
        self._DatabaseNum = DatabaseNum

    @property
    def WebApplicationNum(self):
        return self._WebApplicationNum

    @WebApplicationNum.setter
    def WebApplicationNum(self, WebApplicationNum):
        self._WebApplicationNum = WebApplicationNum

    @property
    def ServiceNum(self):
        return self._ServiceNum

    @ServiceNum.setter
    def ServiceNum(self, ServiceNum):
        self._ServiceNum = ServiceNum

    @property
    def WebFrameworkNum(self):
        return self._WebFrameworkNum

    @WebFrameworkNum.setter
    def WebFrameworkNum(self, WebFrameworkNum):
        self._WebFrameworkNum = WebFrameworkNum

    @property
    def WebSiteNum(self):
        return self._WebSiteNum

    @WebSiteNum.setter
    def WebSiteNum(self, WebSiteNum):
        self._WebSiteNum = WebSiteNum

    @property
    def JarPackageNum(self):
        return self._JarPackageNum

    @JarPackageNum.setter
    def JarPackageNum(self, JarPackageNum):
        self._JarPackageNum = JarPackageNum

    @property
    def StartServiceNum(self):
        return self._StartServiceNum

    @StartServiceNum.setter
    def StartServiceNum(self, StartServiceNum):
        self._StartServiceNum = StartServiceNum

    @property
    def ScheduledTaskNum(self):
        return self._ScheduledTaskNum

    @ScheduledTaskNum.setter
    def ScheduledTaskNum(self, ScheduledTaskNum):
        self._ScheduledTaskNum = ScheduledTaskNum

    @property
    def EnvironmentVariableNum(self):
        return self._EnvironmentVariableNum

    @EnvironmentVariableNum.setter
    def EnvironmentVariableNum(self, EnvironmentVariableNum):
        self._EnvironmentVariableNum = EnvironmentVariableNum

    @property
    def KernelModuleNum(self):
        return self._KernelModuleNum

    @KernelModuleNum.setter
    def KernelModuleNum(self, KernelModuleNum):
        self._KernelModuleNum = KernelModuleNum

    @property
    def SystemInstallationPackageNum(self):
        return self._SystemInstallationPackageNum

    @SystemInstallationPackageNum.setter
    def SystemInstallationPackageNum(self, SystemInstallationPackageNum):
        self._SystemInstallationPackageNum = SystemInstallationPackageNum

    @property
    def SurplusProtectDay(self):
        return self._SurplusProtectDay

    @SurplusProtectDay.setter
    def SurplusProtectDay(self, SurplusProtectDay):
        self._SurplusProtectDay = SurplusProtectDay

    @property
    def CWPStatus(self):
        return self._CWPStatus

    @CWPStatus.setter
    def CWPStatus(self, CWPStatus):
        self._CWPStatus = CWPStatus

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProtectLevel(self):
        return self._ProtectLevel

    @ProtectLevel.setter
    def ProtectLevel(self, ProtectLevel):
        self._ProtectLevel = ProtectLevel

    @property
    def ProtectedDay(self):
        return self._ProtectedDay

    @ProtectedDay.setter
    def ProtectedDay(self, ProtectedDay):
        self._ProtectedDay = ProtectedDay


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AssetName = params.get("AssetName")
        self._Os = params.get("Os")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Region = params.get("Region")
        self._AssetType = params.get("AssetType")
        self._AssetId = params.get("AssetId")
        self._AccountNum = params.get("AccountNum")
        self._PortNum = params.get("PortNum")
        self._ProcessNum = params.get("ProcessNum")
        self._SoftApplicationNum = params.get("SoftApplicationNum")
        self._DatabaseNum = params.get("DatabaseNum")
        self._WebApplicationNum = params.get("WebApplicationNum")
        self._ServiceNum = params.get("ServiceNum")
        self._WebFrameworkNum = params.get("WebFrameworkNum")
        self._WebSiteNum = params.get("WebSiteNum")
        self._JarPackageNum = params.get("JarPackageNum")
        self._StartServiceNum = params.get("StartServiceNum")
        self._ScheduledTaskNum = params.get("ScheduledTaskNum")
        self._EnvironmentVariableNum = params.get("EnvironmentVariableNum")
        self._KernelModuleNum = params.get("KernelModuleNum")
        self._SystemInstallationPackageNum = params.get("SystemInstallationPackageNum")
        self._SurplusProtectDay = params.get("SurplusProtectDay")
        self._CWPStatus = params.get("CWPStatus")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProtectLevel = params.get("ProtectLevel")
        self._ProtectedDay = params.get("ProtectedDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetClusterPod(AbstractModel):
    """集群pod列表

    """

    def __init__(self):
        r"""
        :param _AppId: 租户id
        :type AppId: int
        :param _Uin: 租户uin
        :type Uin: str
        :param _Nick: 租户昵称
        :type Nick: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _AssetId: pod id
        :type AssetId: str
        :param _AssetName: pod名称
        :type AssetName: str
        :param _InstanceCreateTime: pod创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCreateTime: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ClusterId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _MachineId: 主机id
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineId: str
        :param _MachineName: 主机名
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineName: str
        :param _PodIp: pod ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PodIp: str
        :param _ServiceCount: 关联service数
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param _ContainerCount: 关联容器数
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerCount: int
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _IsCore: 是否核心：1:核心，2:非核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._Region = None
        self._AssetId = None
        self._AssetName = None
        self._InstanceCreateTime = None
        self._Namespace = None
        self._Status = None
        self._ClusterId = None
        self._ClusterName = None
        self._MachineId = None
        self._MachineName = None
        self._PodIp = None
        self._ServiceCount = None
        self._ContainerCount = None
        self._PublicIp = None
        self._PrivateIp = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def InstanceCreateTime(self):
        return self._InstanceCreateTime

    @InstanceCreateTime.setter
    def InstanceCreateTime(self, InstanceCreateTime):
        self._InstanceCreateTime = InstanceCreateTime

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def MachineId(self):
        return self._MachineId

    @MachineId.setter
    def MachineId(self, MachineId):
        self._MachineId = MachineId

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def PodIp(self):
        return self._PodIp

    @PodIp.setter
    def PodIp(self, PodIp):
        self._PodIp = PodIp

    @property
    def ServiceCount(self):
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def ContainerCount(self):
        return self._ContainerCount

    @ContainerCount.setter
    def ContainerCount(self, ContainerCount):
        self._ContainerCount = ContainerCount

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._Region = params.get("Region")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._InstanceCreateTime = params.get("InstanceCreateTime")
        self._Namespace = params.get("Namespace")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._MachineId = params.get("MachineId")
        self._MachineName = params.get("MachineName")
        self._PodIp = params.get("PodIp")
        self._ServiceCount = params.get("ServiceCount")
        self._ContainerCount = params.get("ContainerCount")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetInfoDetail(AbstractModel):
    """资产扫描结构细节

    """

    def __init__(self):
        r"""
        :param _AppID: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppID: str
        :param _CVEId: CVE编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CVEId: str
        :param _IsScan: 是扫描，0默认未扫描，1正在扫描，2扫描完成，3扫描出错
注意：此字段可能返回 null，表示取不到有效值。
        :type IsScan: int
        :param _InfluenceAsset: 影响资产数目
注意：此字段可能返回 null，表示取不到有效值。
        :type InfluenceAsset: int
        :param _NotRepairAsset: 未修复资产数目
注意：此字段可能返回 null，表示取不到有效值。
        :type NotRepairAsset: int
        :param _NotProtectAsset: 未防护资产数目
注意：此字段可能返回 null，表示取不到有效值。
        :type NotProtectAsset: int
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskPercent: 任务百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskPercent: int
        :param _TaskTime: 任务时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTime: int
        :param _ScanTime: 扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTime: str
        """
        self._AppID = None
        self._CVEId = None
        self._IsScan = None
        self._InfluenceAsset = None
        self._NotRepairAsset = None
        self._NotProtectAsset = None
        self._TaskId = None
        self._TaskPercent = None
        self._TaskTime = None
        self._ScanTime = None

    @property
    def AppID(self):
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def CVEId(self):
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId

    @property
    def IsScan(self):
        return self._IsScan

    @IsScan.setter
    def IsScan(self, IsScan):
        self._IsScan = IsScan

    @property
    def InfluenceAsset(self):
        return self._InfluenceAsset

    @InfluenceAsset.setter
    def InfluenceAsset(self, InfluenceAsset):
        self._InfluenceAsset = InfluenceAsset

    @property
    def NotRepairAsset(self):
        return self._NotRepairAsset

    @NotRepairAsset.setter
    def NotRepairAsset(self, NotRepairAsset):
        self._NotRepairAsset = NotRepairAsset

    @property
    def NotProtectAsset(self):
        return self._NotProtectAsset

    @NotProtectAsset.setter
    def NotProtectAsset(self, NotProtectAsset):
        self._NotProtectAsset = NotProtectAsset

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskPercent(self):
        return self._TaskPercent

    @TaskPercent.setter
    def TaskPercent(self, TaskPercent):
        self._TaskPercent = TaskPercent

    @property
    def TaskTime(self):
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ScanTime(self):
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._CVEId = params.get("CVEId")
        self._IsScan = params.get("IsScan")
        self._InfluenceAsset = params.get("InfluenceAsset")
        self._NotRepairAsset = params.get("NotRepairAsset")
        self._NotProtectAsset = params.get("NotProtectAsset")
        self._TaskId = params.get("TaskId")
        self._TaskPercent = params.get("TaskPercent")
        self._TaskTime = params.get("TaskTime")
        self._ScanTime = params.get("ScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetInstanceTypeMap(AbstractModel):
    """资产类型和实例类型的映射

    """

    def __init__(self):
        r"""
        :param _Text: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Value: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _InstanceTypeList: 资产类型和实例类型映射关系
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTypeList: list of FilterDataObject
        """
        self._Text = None
        self._Value = None
        self._InstanceTypeList = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def InstanceTypeList(self):
        return self._InstanceTypeList

    @InstanceTypeList.setter
    def InstanceTypeList(self, InstanceTypeList):
        self._InstanceTypeList = InstanceTypeList


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Value = params.get("Value")
        if params.get("InstanceTypeList") is not None:
            self._InstanceTypeList = []
            for item in params.get("InstanceTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetTag(AbstractModel):
    """安全中心资产标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的key值,可以是字母、数字、下划线
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签的vale值,可以是字母、数字、下划线
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewCFGRisk(AbstractModel):
    """资产视角配置风险

    """

    def __init__(self):
        r"""
        :param _Id: 唯一id
        :type Id: str
        :param _CFGName: 配置名
        :type CFGName: str
        :param _CheckType: 检查类型
        :type CheckType: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _From: 来源
        :type From: str
        :param _Status: 状态
        :type Status: int
        :param _CFGSTD: 相关规范
        :type CFGSTD: str
        :param _CFGDescribe: 配置详情
        :type CFGDescribe: str
        :param _CFGFix: 修复建议
        :type CFGFix: str
        :param _CFGHelpURL: 帮助文档链接
        :type CFGHelpURL: str
        :param _Index: 前端使用索引
        :type Index: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        """
        self._Id = None
        self._CFGName = None
        self._CheckType = None
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._AffectAsset = None
        self._Level = None
        self._FirstTime = None
        self._RecentTime = None
        self._From = None
        self._Status = None
        self._CFGSTD = None
        self._CFGDescribe = None
        self._CFGFix = None
        self._CFGHelpURL = None
        self._Index = None
        self._AppId = None
        self._Nick = None
        self._Uin = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CFGName(self):
        return self._CFGName

    @CFGName.setter
    def CFGName(self, CFGName):
        self._CFGName = CFGName

    @property
    def CheckType(self):
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CFGSTD(self):
        return self._CFGSTD

    @CFGSTD.setter
    def CFGSTD(self, CFGSTD):
        self._CFGSTD = CFGSTD

    @property
    def CFGDescribe(self):
        return self._CFGDescribe

    @CFGDescribe.setter
    def CFGDescribe(self, CFGDescribe):
        self._CFGDescribe = CFGDescribe

    @property
    def CFGFix(self):
        return self._CFGFix

    @CFGFix.setter
    def CFGFix(self, CFGFix):
        self._CFGFix = CFGFix

    @property
    def CFGHelpURL(self):
        return self._CFGHelpURL

    @CFGHelpURL.setter
    def CFGHelpURL(self, CFGHelpURL):
        self._CFGHelpURL = CFGHelpURL

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CFGName = params.get("CFGName")
        self._CheckType = params.get("CheckType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._FirstTime = params.get("FirstTime")
        self._RecentTime = params.get("RecentTime")
        self._From = params.get("From")
        self._Status = params.get("Status")
        self._CFGSTD = params.get("CFGSTD")
        self._CFGDescribe = params.get("CFGDescribe")
        self._CFGFix = params.get("CFGFix")
        self._CFGHelpURL = params.get("CFGHelpURL")
        self._Index = params.get("Index")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewPortRisk(AbstractModel):
    """资产视角的端口风险对象

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: int
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Suggestion: 处置建议,0保持现状、1限制访问、2封禁端口
        :type Suggestion: int
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: 风险ID
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _From: 识别来源，详细看枚举返回。
        :type From: str
        """
        self._Port = None
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Protocol = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Suggestion = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._From = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Suggestion = params.get("Suggestion")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewVULRisk(AbstractModel):
    """资产视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。

        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: 风险ID
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _Port: 端口
        :type Port: str
        :param _Describe: 漏洞描述
        :type Describe: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _References: 技术参考
        :type References: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _VULName: 漏洞名称
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Fix: 修复方案
        :type Fix: str
        :param _POCId: pocid
        :type POCId: str
        :param _From: 扫描来源
        :type From: str
        :param _CWPVersion: 主机版本
        :type CWPVersion: int
        :param _IsSupportRepair: 是否支持修复
        :type IsSupportRepair: bool
        :param _IsSupportDetect: 是否支持扫描
        :type IsSupportDetect: bool
        :param _InstanceUUID: 实例uuid
        :type InstanceUUID: str
        :param _Payload: 攻击载荷
        :type Payload: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type EMGCVulType: int
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._VULType = None
        self._Port = None
        self._Describe = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._VULName = None
        self._CVE = None
        self._Fix = None
        self._POCId = None
        self._From = None
        self._CWPVersion = None
        self._IsSupportRepair = None
        self._IsSupportDetect = None
        self._InstanceUUID = None
        self._Payload = None
        self._EMGCVulType = None

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VULType(self):
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def VULName(self):
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Fix(self):
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def POCId(self):
        return self._POCId

    @POCId.setter
    def POCId(self, POCId):
        self._POCId = POCId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CWPVersion(self):
        return self._CWPVersion

    @CWPVersion.setter
    def CWPVersion(self, CWPVersion):
        self._CWPVersion = CWPVersion

    @property
    def IsSupportRepair(self):
        return self._IsSupportRepair

    @IsSupportRepair.setter
    def IsSupportRepair(self, IsSupportRepair):
        self._IsSupportRepair = IsSupportRepair

    @property
    def IsSupportDetect(self):
        return self._IsSupportDetect

    @IsSupportDetect.setter
    def IsSupportDetect(self, IsSupportDetect):
        self._IsSupportDetect = IsSupportDetect

    @property
    def InstanceUUID(self):
        return self._InstanceUUID

    @InstanceUUID.setter
    def InstanceUUID(self, InstanceUUID):
        self._InstanceUUID = InstanceUUID

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def EMGCVulType(self):
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._VULType = params.get("VULType")
        self._Port = params.get("Port")
        self._Describe = params.get("Describe")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Fix = params.get("Fix")
        self._POCId = params.get("POCId")
        self._From = params.get("From")
        self._CWPVersion = params.get("CWPVersion")
        self._IsSupportRepair = params.get("IsSupportRepair")
        self._IsSupportDetect = params.get("IsSupportDetect")
        self._InstanceUUID = params.get("InstanceUUID")
        self._Payload = params.get("Payload")
        self._EMGCVulType = params.get("EMGCVulType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewVULRiskData(AbstractModel):
    """资产视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Component: 组件
        :type Component: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1标记已处置、2已忽略，3已处置 ，4 处置中 ，5 检测中 ，6部分已处置
        :type Status: int
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _Port: 端口
        :type Port: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _VULName: 漏洞名称
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _POCId: pocid
        :type POCId: str
        :param _From: 扫描来源
        :type From: str
        :param _CWPVersion: 主机版本
        :type CWPVersion: int
        :param _InstanceUUID: 实例uuid
        :type InstanceUUID: str
        :param _Payload: 攻击载荷
        :type Payload: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type EMGCVulType: int
        :param _CVSS: CVSS评分
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSS: float
        :param _Index: 前端索引id
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        :param _PCMGRId: pcmgrId
注意：此字段可能返回 null，表示取不到有效值。
        :type PCMGRId: str
        :param _LogId: 报告id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogId: str
        :param _TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _VulTag: 漏洞标签
注意：此字段可能返回 null，表示取不到有效值。
        :type VulTag: list of str
        :param _DisclosureTime: 漏洞披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DisclosureTime: str
        :param _AttackHeat: 攻击热度
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackHeat: int
        :param _IsSuggest: 是否必修漏洞1是，0不是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSuggest: int
        :param _HandleTaskId: 处置任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type HandleTaskId: str
        :param _EngineSource: 引擎来源
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineSource: str
        :param _VulRiskId: 新的漏洞风险id(同全网漏洞表的riskid)
注意：此字段可能返回 null，表示取不到有效值。
        :type VulRiskId: str
        :param _TvdID: 新版漏洞id
注意：此字段可能返回 null，表示取不到有效值。
        :type TvdID: str
        :param _IsOneClick: 是否可以一键体检，1-可以，0-不可以
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOneClick: int
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._RiskId = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._VULType = None
        self._Port = None
        self._AppName = None
        self._AppVersion = None
        self._VULURL = None
        self._VULName = None
        self._CVE = None
        self._POCId = None
        self._From = None
        self._CWPVersion = None
        self._InstanceUUID = None
        self._Payload = None
        self._EMGCVulType = None
        self._CVSS = None
        self._Index = None
        self._PCMGRId = None
        self._LogId = None
        self._TaskId = None
        self._VulTag = None
        self._DisclosureTime = None
        self._AttackHeat = None
        self._IsSuggest = None
        self._HandleTaskId = None
        self._EngineSource = None
        self._VulRiskId = None
        self._TvdID = None
        self._IsOneClick = None

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RiskId(self):
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VULType(self):
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def VULName(self):
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def POCId(self):
        return self._POCId

    @POCId.setter
    def POCId(self, POCId):
        self._POCId = POCId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CWPVersion(self):
        return self._CWPVersion

    @CWPVersion.setter
    def CWPVersion(self, CWPVersion):
        self._CWPVersion = CWPVersion

    @property
    def InstanceUUID(self):
        return self._InstanceUUID

    @InstanceUUID.setter
    def InstanceUUID(self, InstanceUUID):
        self._InstanceUUID = InstanceUUID

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def EMGCVulType(self):
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def CVSS(self):
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def PCMGRId(self):
        return self._PCMGRId

    @PCMGRId.setter
    def PCMGRId(self, PCMGRId):
        self._PCMGRId = PCMGRId

    @property
    def LogId(self):
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def VulTag(self):
        return self._VulTag

    @VulTag.setter
    def VulTag(self, VulTag):
        self._VulTag = VulTag

    @property
    def DisclosureTime(self):
        return self._DisclosureTime

    @DisclosureTime.setter
    def DisclosureTime(self, DisclosureTime):
        self._DisclosureTime = DisclosureTime

    @property
    def AttackHeat(self):
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def IsSuggest(self):
        return self._IsSuggest

    @IsSuggest.setter
    def IsSuggest(self, IsSuggest):
        self._IsSuggest = IsSuggest

    @property
    def HandleTaskId(self):
        return self._HandleTaskId

    @HandleTaskId.setter
    def HandleTaskId(self, HandleTaskId):
        self._HandleTaskId = HandleTaskId

    @property
    def EngineSource(self):
        return self._EngineSource

    @EngineSource.setter
    def EngineSource(self, EngineSource):
        self._EngineSource = EngineSource

    @property
    def VulRiskId(self):
        return self._VulRiskId

    @VulRiskId.setter
    def VulRiskId(self, VulRiskId):
        self._VulRiskId = VulRiskId

    @property
    def TvdID(self):
        return self._TvdID

    @TvdID.setter
    def TvdID(self, TvdID):
        self._TvdID = TvdID

    @property
    def IsOneClick(self):
        return self._IsOneClick

    @IsOneClick.setter
    def IsOneClick(self, IsOneClick):
        self._IsOneClick = IsOneClick


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._RiskId = params.get("RiskId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._VULType = params.get("VULType")
        self._Port = params.get("Port")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._POCId = params.get("POCId")
        self._From = params.get("From")
        self._CWPVersion = params.get("CWPVersion")
        self._InstanceUUID = params.get("InstanceUUID")
        self._Payload = params.get("Payload")
        self._EMGCVulType = params.get("EMGCVulType")
        self._CVSS = params.get("CVSS")
        self._Index = params.get("Index")
        self._PCMGRId = params.get("PCMGRId")
        self._LogId = params.get("LogId")
        self._TaskId = params.get("TaskId")
        self._VulTag = params.get("VulTag")
        self._DisclosureTime = params.get("DisclosureTime")
        self._AttackHeat = params.get("AttackHeat")
        self._IsSuggest = params.get("IsSuggest")
        self._HandleTaskId = params.get("HandleTaskId")
        self._EngineSource = params.get("EngineSource")
        self._VulRiskId = params.get("VulRiskId")
        self._TvdID = params.get("TvdID")
        self._IsOneClick = params.get("IsOneClick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewWeakPassRisk(AbstractModel):
    """资产视角的弱口令风险

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: ID，处理风险使用
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _PasswordType: 弱口令类型
        :type PasswordType: str
        :param _From: 来源
        :type From: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _VULURL: 漏洞url
        :type VULURL: str
        :param _Fix: 修复建议
        :type Fix: str
        :param _Payload: 证明
        :type Payload: str
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._PasswordType = None
        self._From = None
        self._VULType = None
        self._VULURL = None
        self._Fix = None
        self._Payload = None

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def PasswordType(self):
        return self._PasswordType

    @PasswordType.setter
    def PasswordType(self, PasswordType):
        self._PasswordType = PasswordType

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def VULType(self):
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULURL(self):
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Fix(self):
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._PasswordType = params.get("PasswordType")
        self._From = params.get("From")
        self._VULType = params.get("VULType")
        self._VULURL = params.get("VULURL")
        self._Fix = params.get("Fix")
        self._Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BugInfoDetail(AbstractModel):
    """漏洞详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 漏洞编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _PatchId: 漏洞对应pocId
注意：此字段可能返回 null，表示取不到有效值。
        :type PatchId: str
        :param _VULName: 漏洞名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VULName: str
        :param _Level: 漏洞严重性：high,middle，low，info
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param _CVSSScore: cvss评分
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSScore: str
        :param _CVEId: cve编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CVEId: str
        :param _Tag: 漏洞标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param _VULCategory: 漏洞种类，1:web应用，2:系统组件漏洞，3:配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VULCategory: int
        :param _ImpactOs: 漏洞影响系统
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactOs: str
        :param _ImpactCOMPENT: 漏洞影响组件
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactCOMPENT: str
        :param _ImpactVersion: 漏洞影响版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactVersion: str
        :param _Reference: 链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Reference: str
        :param _VULDescribe: 漏洞描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VULDescribe: str
        :param _Fix: 修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Fix: str
        :param _ProSupport: 产品支持状态，实时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ProSupport: int
        :param _IsPublish: 是否公开，0为未发布，1为发布
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublish: int
        :param _ReleaseTime: 释放时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _SubCategory: 漏洞子类别
注意：此字段可能返回 null，表示取不到有效值。
        :type SubCategory: str
        """
        self._Id = None
        self._PatchId = None
        self._VULName = None
        self._Level = None
        self._CVSSScore = None
        self._CVEId = None
        self._Tag = None
        self._VULCategory = None
        self._ImpactOs = None
        self._ImpactCOMPENT = None
        self._ImpactVersion = None
        self._Reference = None
        self._VULDescribe = None
        self._Fix = None
        self._ProSupport = None
        self._IsPublish = None
        self._ReleaseTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._SubCategory = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PatchId(self):
        return self._PatchId

    @PatchId.setter
    def PatchId(self, PatchId):
        self._PatchId = PatchId

    @property
    def VULName(self):
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def CVSSScore(self):
        return self._CVSSScore

    @CVSSScore.setter
    def CVSSScore(self, CVSSScore):
        self._CVSSScore = CVSSScore

    @property
    def CVEId(self):
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def VULCategory(self):
        return self._VULCategory

    @VULCategory.setter
    def VULCategory(self, VULCategory):
        self._VULCategory = VULCategory

    @property
    def ImpactOs(self):
        return self._ImpactOs

    @ImpactOs.setter
    def ImpactOs(self, ImpactOs):
        self._ImpactOs = ImpactOs

    @property
    def ImpactCOMPENT(self):
        return self._ImpactCOMPENT

    @ImpactCOMPENT.setter
    def ImpactCOMPENT(self, ImpactCOMPENT):
        self._ImpactCOMPENT = ImpactCOMPENT

    @property
    def ImpactVersion(self):
        return self._ImpactVersion

    @ImpactVersion.setter
    def ImpactVersion(self, ImpactVersion):
        self._ImpactVersion = ImpactVersion

    @property
    def Reference(self):
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def VULDescribe(self):
        return self._VULDescribe

    @VULDescribe.setter
    def VULDescribe(self, VULDescribe):
        self._VULDescribe = VULDescribe

    @property
    def Fix(self):
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def ProSupport(self):
        return self._ProSupport

    @ProSupport.setter
    def ProSupport(self, ProSupport):
        self._ProSupport = ProSupport

    @property
    def IsPublish(self):
        return self._IsPublish

    @IsPublish.setter
    def IsPublish(self, IsPublish):
        self._IsPublish = IsPublish

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def SubCategory(self):
        return self._SubCategory

    @SubCategory.setter
    def SubCategory(self, SubCategory):
        self._SubCategory = SubCategory


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PatchId = params.get("PatchId")
        self._VULName = params.get("VULName")
        self._Level = params.get("Level")
        self._CVSSScore = params.get("CVSSScore")
        self._CVEId = params.get("CVEId")
        self._Tag = params.get("Tag")
        self._VULCategory = params.get("VULCategory")
        self._ImpactOs = params.get("ImpactOs")
        self._ImpactCOMPENT = params.get("ImpactCOMPENT")
        self._ImpactVersion = params.get("ImpactVersion")
        self._Reference = params.get("Reference")
        self._VULDescribe = params.get("VULDescribe")
        self._Fix = params.get("Fix")
        self._ProSupport = params.get("ProSupport")
        self._IsPublish = params.get("IsPublish")
        self._ReleaseTime = params.get("ReleaseTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._SubCategory = params.get("SubCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVMAssetVO(AbstractModel):
    """主机资产信息

    主机防护状态枚举，左边是常量，右边是显示
    0：未安装
    1：基础版防护中
    2：普惠版防护中
    3：专业版防护中
    4：旗舰版防护中
    5：已离线
    6：已关机

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _CWPStatus: 防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPStatus: int
        :param _AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 私网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc 名
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _AppId: appid信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _AvailableArea: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableArea: str
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _SubnetName: 子网名
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _InstanceUuid: uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceUuid: str
        :param _InstanceQUuid: qquid
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceQUuid: str
        :param _OsName: os名
注意：此字段可能返回 null，表示取不到有效值。
        :type OsName: str
        :param _PartitionCount: 分区
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionCount: int
        :param _CPUInfo: cpu信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUInfo: str
        :param _CPUSize: cpu大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUSize: int
        :param _CPULoad: cpu负载
注意：此字段可能返回 null，表示取不到有效值。
        :type CPULoad: str
        :param _MemorySize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemorySize: str
        :param _MemoryLoad: 内存负载
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryLoad: str
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: str
        :param _DiskLoad: 硬盘负载
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskLoad: str
        :param _AccountCount: 账号数
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountCount: str
        :param _ProcessCount: 进程数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessCount: str
        :param _AppCount: 软件应用
注意：此字段可能返回 null，表示取不到有效值。
        :type AppCount: str
        :param _PortCount: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type PortCount: int
        :param _Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param _Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param _Intercept: 网络拦截
注意：此字段可能返回 null，表示取不到有效值。
        :type Intercept: int
        :param _InBandwidth: 入向峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InBandwidth: str
        :param _OutBandwidth: 出向峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type OutBandwidth: str
        :param _InFlow: 入向累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type InFlow: str
        :param _OutFlow: 出向累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _NetWorkOut: 恶意主动外联
注意：此字段可能返回 null，表示取不到有效值。
        :type NetWorkOut: int
        :param _PortRisk: 端口风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _MemberId: memberId
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param _Os: os全称
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        :param _RiskExposure: 风险服务暴露
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskExposure: int
        :param _BASAgentStatus: 模拟攻击工具状态。0代表未安装，1代表已安装，2代表已离线
注意：此字段可能返回 null，表示取不到有效值。
        :type BASAgentStatus: int
        :param _IsNewAsset: 1新资产；0 非新资产
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        :param _CVMAgentStatus: 0 未安装  1安装 2:安装中
注意：此字段可能返回 null，表示取不到有效值。
        :type CVMAgentStatus: int
        :param _CVMStatus: 1:开启 0:未开启
注意：此字段可能返回 null，表示取不到有效值。
        :type CVMStatus: int
        :param _DefenseModel: 1:客户端已安装 0：未安装 2: Agentless
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseModel: int
        :param _TatStatus: 1:已安装 0:未安装
注意：此字段可能返回 null，表示取不到有效值。
        :type TatStatus: int
        :param _CpuTrend: cpu趋势图
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuTrend: list of Element
        :param _MemoryTrend: 内存趋势图
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryTrend: list of Element
        :param _AgentStatus: 1:agent在线 0:agent离线 2:主机离线
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentStatus: int
        :param _CloseDefenseCount: 本月防护关闭次数
注意：此字段可能返回 null，表示取不到有效值。
        :type CloseDefenseCount: int
        :param _InstanceState: 运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceState: str
        :param _SecurityGroupIds: 安全组数据
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param _AgentMemRss: 物理内存占用KB
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentMemRss: int
        :param _AgentCpuPer: CPU使用率百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentCpuPer: float
        :param _RealAppid: cvm真正所属的appid
注意：此字段可能返回 null，表示取不到有效值。
        :type RealAppid: int
        :param _CloudType: 云资产类型：0：腾讯云，1：aws，2：azure
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudType: int
        :param _ProtectStatus: 主机防护状态枚举
0：未安装
1：基础版防护中
2：普惠版防护中
3：专业版防护中
4：旗舰版防护中
5：已离线
6：已关机
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectStatus: int
        :param _OfflineTime: 最后离线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTime: str
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._CWPStatus = None
        self._AssetCreateTime = None
        self._PublicIp = None
        self._PrivateIp = None
        self._VpcId = None
        self._VpcName = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._AvailableArea = None
        self._IsCore = None
        self._SubnetId = None
        self._SubnetName = None
        self._InstanceUuid = None
        self._InstanceQUuid = None
        self._OsName = None
        self._PartitionCount = None
        self._CPUInfo = None
        self._CPUSize = None
        self._CPULoad = None
        self._MemorySize = None
        self._MemoryLoad = None
        self._DiskSize = None
        self._DiskLoad = None
        self._AccountCount = None
        self._ProcessCount = None
        self._AppCount = None
        self._PortCount = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._NetWorkOut = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._Tag = None
        self._MemberId = None
        self._Os = None
        self._RiskExposure = None
        self._BASAgentStatus = None
        self._IsNewAsset = None
        self._CVMAgentStatus = None
        self._CVMStatus = None
        self._DefenseModel = None
        self._TatStatus = None
        self._CpuTrend = None
        self._MemoryTrend = None
        self._AgentStatus = None
        self._CloseDefenseCount = None
        self._InstanceState = None
        self._SecurityGroupIds = None
        self._AgentMemRss = None
        self._AgentCpuPer = None
        self._RealAppid = None
        self._CloudType = None
        self._ProtectStatus = None
        self._OfflineTime = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CWPStatus(self):
        return self._CWPStatus

    @CWPStatus.setter
    def CWPStatus(self, CWPStatus):
        self._CWPStatus = CWPStatus

    @property
    def AssetCreateTime(self):
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def AvailableArea(self):
        return self._AvailableArea

    @AvailableArea.setter
    def AvailableArea(self, AvailableArea):
        self._AvailableArea = AvailableArea

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def InstanceUuid(self):
        return self._InstanceUuid

    @InstanceUuid.setter
    def InstanceUuid(self, InstanceUuid):
        self._InstanceUuid = InstanceUuid

    @property
    def InstanceQUuid(self):
        return self._InstanceQUuid

    @InstanceQUuid.setter
    def InstanceQUuid(self, InstanceQUuid):
        self._InstanceQUuid = InstanceQUuid

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def PartitionCount(self):
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def CPUInfo(self):
        return self._CPUInfo

    @CPUInfo.setter
    def CPUInfo(self, CPUInfo):
        self._CPUInfo = CPUInfo

    @property
    def CPUSize(self):
        return self._CPUSize

    @CPUSize.setter
    def CPUSize(self, CPUSize):
        self._CPUSize = CPUSize

    @property
    def CPULoad(self):
        return self._CPULoad

    @CPULoad.setter
    def CPULoad(self, CPULoad):
        self._CPULoad = CPULoad

    @property
    def MemorySize(self):
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def MemoryLoad(self):
        return self._MemoryLoad

    @MemoryLoad.setter
    def MemoryLoad(self, MemoryLoad):
        self._MemoryLoad = MemoryLoad

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskLoad(self):
        return self._DiskLoad

    @DiskLoad.setter
    def DiskLoad(self, DiskLoad):
        self._DiskLoad = DiskLoad

    @property
    def AccountCount(self):
        return self._AccountCount

    @AccountCount.setter
    def AccountCount(self, AccountCount):
        self._AccountCount = AccountCount

    @property
    def ProcessCount(self):
        return self._ProcessCount

    @ProcessCount.setter
    def ProcessCount(self, ProcessCount):
        self._ProcessCount = ProcessCount

    @property
    def AppCount(self):
        return self._AppCount

    @AppCount.setter
    def AppCount(self, AppCount):
        self._AppCount = AppCount

    @property
    def PortCount(self):
        return self._PortCount

    @PortCount.setter
    def PortCount(self, PortCount):
        self._PortCount = PortCount

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def NetWorkOut(self):
        return self._NetWorkOut

    @NetWorkOut.setter
    def NetWorkOut(self, NetWorkOut):
        self._NetWorkOut = NetWorkOut

    @property
    def PortRisk(self):
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def RiskExposure(self):
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def BASAgentStatus(self):
        return self._BASAgentStatus

    @BASAgentStatus.setter
    def BASAgentStatus(self, BASAgentStatus):
        self._BASAgentStatus = BASAgentStatus

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def CVMAgentStatus(self):
        return self._CVMAgentStatus

    @CVMAgentStatus.setter
    def CVMAgentStatus(self, CVMAgentStatus):
        self._CVMAgentStatus = CVMAgentStatus

    @property
    def CVMStatus(self):
        return self._CVMStatus

    @CVMStatus.setter
    def CVMStatus(self, CVMStatus):
        self._CVMStatus = CVMStatus

    @property
    def DefenseModel(self):
        return self._DefenseModel

    @DefenseModel.setter
    def DefenseModel(self, DefenseModel):
        self._DefenseModel = DefenseModel

    @property
    def TatStatus(self):
        return self._TatStatus

    @TatStatus.setter
    def TatStatus(self, TatStatus):
        self._TatStatus = TatStatus

    @property
    def CpuTrend(self):
        return self._CpuTrend

    @CpuTrend.setter
    def CpuTrend(self, CpuTrend):
        self._CpuTrend = CpuTrend

    @property
    def MemoryTrend(self):
        return self._MemoryTrend

    @MemoryTrend.setter
    def MemoryTrend(self, MemoryTrend):
        self._MemoryTrend = MemoryTrend

    @property
    def AgentStatus(self):
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def CloseDefenseCount(self):
        return self._CloseDefenseCount

    @CloseDefenseCount.setter
    def CloseDefenseCount(self, CloseDefenseCount):
        self._CloseDefenseCount = CloseDefenseCount

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AgentMemRss(self):
        return self._AgentMemRss

    @AgentMemRss.setter
    def AgentMemRss(self, AgentMemRss):
        self._AgentMemRss = AgentMemRss

    @property
    def AgentCpuPer(self):
        return self._AgentCpuPer

    @AgentCpuPer.setter
    def AgentCpuPer(self, AgentCpuPer):
        self._AgentCpuPer = AgentCpuPer

    @property
    def RealAppid(self):
        return self._RealAppid

    @RealAppid.setter
    def RealAppid(self, RealAppid):
        self._RealAppid = RealAppid

    @property
    def CloudType(self):
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def ProtectStatus(self):
        return self._ProtectStatus

    @ProtectStatus.setter
    def ProtectStatus(self, ProtectStatus):
        self._ProtectStatus = ProtectStatus

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._CWPStatus = params.get("CWPStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._AvailableArea = params.get("AvailableArea")
        self._IsCore = params.get("IsCore")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._InstanceUuid = params.get("InstanceUuid")
        self._InstanceQUuid = params.get("InstanceQUuid")
        self._OsName = params.get("OsName")
        self._PartitionCount = params.get("PartitionCount")
        self._CPUInfo = params.get("CPUInfo")
        self._CPUSize = params.get("CPUSize")
        self._CPULoad = params.get("CPULoad")
        self._MemorySize = params.get("MemorySize")
        self._MemoryLoad = params.get("MemoryLoad")
        self._DiskSize = params.get("DiskSize")
        self._DiskLoad = params.get("DiskLoad")
        self._AccountCount = params.get("AccountCount")
        self._ProcessCount = params.get("ProcessCount")
        self._AppCount = params.get("AppCount")
        self._PortCount = params.get("PortCount")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._NetWorkOut = params.get("NetWorkOut")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._MemberId = params.get("MemberId")
        self._Os = params.get("Os")
        self._RiskExposure = params.get("RiskExposure")
        self._BASAgentStatus = params.get("BASAgentStatus")
        self._IsNewAsset = params.get("IsNewAsset")
        self._CVMAgentStatus = params.get("CVMAgentStatus")
        self._CVMStatus = params.get("CVMStatus")
        self._DefenseModel = params.get("DefenseModel")
        self._TatStatus = params.get("TatStatus")
        if params.get("CpuTrend") is not None:
            self._CpuTrend = []
            for item in params.get("CpuTrend"):
                obj = Element()
                obj._deserialize(item)
                self._CpuTrend.append(obj)
        if params.get("MemoryTrend") is not None:
            self._MemoryTrend = []
            for item in params.get("MemoryTrend"):
                obj = Element()
                obj._deserialize(item)
                self._MemoryTrend.append(obj)
        self._AgentStatus = params.get("AgentStatus")
        self._CloseDefenseCount = params.get("CloseDefenseCount")
        self._InstanceState = params.get("InstanceState")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._AgentMemRss = params.get("AgentMemRss")
        self._AgentCpuPer = params.get("AgentCpuPer")
        self._RealAppid = params.get("RealAppid")
        self._CloudType = params.get("CloudType")
        self._ProtectStatus = params.get("ProtectStatus")
        self._OfflineTime = params.get("OfflineTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListenerListInfo(AbstractModel):
    """clb实例和监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器id
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _ListenerName: 监听器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _LoadBalancerId: 负载均衡Id
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Vip: 负载均衡ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _VPort: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type VPort: int
        :param _Zone: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _NumericalVpcId: 私有网络id
注意：此字段可能返回 null，表示取不到有效值。
        :type NumericalVpcId: int
        :param _LoadBalancerType: 负载均衡类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _Domain: 监听器域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _LoadBalancerDomain: 负载均衡域名
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerDomain: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Protocol = None
        self._Region = None
        self._Vip = None
        self._VPort = None
        self._Zone = None
        self._NumericalVpcId = None
        self._LoadBalancerType = None
        self._Domain = None
        self._LoadBalancerDomain = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NumericalVpcId(self):
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerDomain(self):
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Protocol = params.get("Protocol")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._Zone = params.get("Zone")
        self._NumericalVpcId = params.get("NumericalVpcId")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Domain = params.get("Domain")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAndIpRequest(AbstractModel):
    """CreateDomainAndIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 公网IP/域名
        :type Content: list of str
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._Content = None
        self._MemberId = None
        self._Tags = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._MemberId = params.get("MemberId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAndIpResponse(AbstractModel):
    """CreateDomainAndIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回创建成功的数量
        :type Data: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class CreateRiskCenterScanTaskRequest(AbstractModel):
    """CreateRiskCenterScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ScanAssetType: 0-全扫，1-指定资产扫，2-排除资产扫，3-手动填写扫；1和2则Assets字段必填，3则SelfDefiningAssets必填
        :type ScanAssetType: int
        :param _ScanItem: 扫描项目；port/poc/weakpass/webcontent/configrisk/exposedserver
        :type ScanItem: list of str
        :param _ScanPlanType: 0-周期任务,1-立即扫描,2-定时扫描,3-自定义；0,2,3则ScanPlanContent必填
        :type ScanPlanType: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Assets: 扫描资产信息列表
        :type Assets: list of TaskAssetObject
        :param _ScanPlanContent: 扫描计划详情
        :type ScanPlanContent: str
        :param _SelfDefiningAssets: ip/域名/url数组
        :type SelfDefiningAssets: list of str
        :param _ScanFrom: 请求发起源，默认为vss表示漏洞扫描服务，云安全中心的用户请填充csip
        :type ScanFrom: str
        :param _TaskAdvanceCFG: 高级配置
        :type TaskAdvanceCFG: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        :param _TaskMode: 体检模式，0-标准模式，1-快速模式，2-高级模式，默认标准模式
        :type TaskMode: int
        :param _Tags: 资产标签
        :type Tags: :class:`tencentcloud.csip.v20221121.models.AssetTag`
        :param _FinishWebHook: 任务完成回调webhook地址
        :type FinishWebHook: str
        """
        self._TaskName = None
        self._ScanAssetType = None
        self._ScanItem = None
        self._ScanPlanType = None
        self._MemberId = None
        self._Assets = None
        self._ScanPlanContent = None
        self._SelfDefiningAssets = None
        self._ScanFrom = None
        self._TaskAdvanceCFG = None
        self._TaskMode = None
        self._Tags = None
        self._FinishWebHook = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ScanAssetType(self):
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def ScanItem(self):
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanPlanType(self):
        return self._ScanPlanType

    @ScanPlanType.setter
    def ScanPlanType(self, ScanPlanType):
        self._ScanPlanType = ScanPlanType

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Assets(self):
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def ScanPlanContent(self):
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def SelfDefiningAssets(self):
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def ScanFrom(self):
        return self._ScanFrom

    @ScanFrom.setter
    def ScanFrom(self, ScanFrom):
        self._ScanFrom = ScanFrom

    @property
    def TaskAdvanceCFG(self):
        return self._TaskAdvanceCFG

    @TaskAdvanceCFG.setter
    def TaskAdvanceCFG(self, TaskAdvanceCFG):
        self._TaskAdvanceCFG = TaskAdvanceCFG

    @property
    def TaskMode(self):
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FinishWebHook(self):
        return self._FinishWebHook

    @FinishWebHook.setter
    def FinishWebHook(self, FinishWebHook):
        self._FinishWebHook = FinishWebHook


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._ScanAssetType = params.get("ScanAssetType")
        self._ScanItem = params.get("ScanItem")
        self._ScanPlanType = params.get("ScanPlanType")
        self._MemberId = params.get("MemberId")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        self._ScanFrom = params.get("ScanFrom")
        if params.get("TaskAdvanceCFG") is not None:
            self._TaskAdvanceCFG = TaskAdvanceCFG()
            self._TaskAdvanceCFG._deserialize(params.get("TaskAdvanceCFG"))
        self._TaskMode = params.get("TaskMode")
        if params.get("Tags") is not None:
            self._Tags = AssetTag()
            self._Tags._deserialize(params.get("Tags"))
        self._FinishWebHook = params.get("FinishWebHook")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRiskCenterScanTaskResponse(AbstractModel):
    """CreateRiskCenterScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _Status: 0,任务创建成功；小于0失败；-1为存在资产未认证
        :type Status: int
        :param _UnAuthAsset: 未认证资产列表
        :type UnAuthAsset: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._UnAuthAsset = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnAuthAsset(self):
        return self._UnAuthAsset

    @UnAuthAsset.setter
    def UnAuthAsset(self, UnAuthAsset):
        self._UnAuthAsset = UnAuthAsset

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._UnAuthAsset = params.get("UnAuthAsset")
        self._RequestId = params.get("RequestId")


class DBAssetVO(AbstractModel):
    """db资产输出字段

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _VpcId: vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc标签
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param _Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param _Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param _ScanTask: 扫描任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param _AppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 昵称别名
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _IsNewAsset: 是否新资产: 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._VpcId = None
        self._VpcName = None
        self._Region = None
        self._Domain = None
        self._AssetCreateTime = None
        self._LastScanTime = None
        self._ConfigurationRisk = None
        self._Attack = None
        self._Access = None
        self._ScanTask = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._Port = None
        self._Tag = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Status = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AssetCreateTime(self):
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def ConfigurationRisk(self):
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._Region = params.get("Region")
        self._Domain = params.get("Domain")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._LastScanTime = params.get("LastScanTime")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._ScanTask = params.get("ScanTask")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._Port = params.get("Port")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Status = params.get("Status")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSearchBug(AbstractModel):
    """漏洞和资产信息

    """

    def __init__(self):
        r"""
        :param _StateCode: 返回查询状态
        :type StateCode: str
        :param _DataBug: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type DataBug: list of BugInfoDetail
        :param _DataAsset: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type DataAsset: list of AssetInfoDetail
        :param _VSSScan: true支持扫描。false不支持扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type VSSScan: bool
        :param _CWPScan: 0不支持，1支持
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPScan: str
        :param _CFWPatch: 1支持虚拟补丁，0或空不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWPatch: str
        :param _WafPatch: 0不支持，1支持
注意：此字段可能返回 null，表示取不到有效值。
        :type WafPatch: int
        :param _CWPFix: 0不支持，1支持
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPFix: int
        """
        self._StateCode = None
        self._DataBug = None
        self._DataAsset = None
        self._VSSScan = None
        self._CWPScan = None
        self._CFWPatch = None
        self._WafPatch = None
        self._CWPFix = None

    @property
    def StateCode(self):
        return self._StateCode

    @StateCode.setter
    def StateCode(self, StateCode):
        self._StateCode = StateCode

    @property
    def DataBug(self):
        return self._DataBug

    @DataBug.setter
    def DataBug(self, DataBug):
        self._DataBug = DataBug

    @property
    def DataAsset(self):
        return self._DataAsset

    @DataAsset.setter
    def DataAsset(self, DataAsset):
        self._DataAsset = DataAsset

    @property
    def VSSScan(self):
        return self._VSSScan

    @VSSScan.setter
    def VSSScan(self, VSSScan):
        self._VSSScan = VSSScan

    @property
    def CWPScan(self):
        return self._CWPScan

    @CWPScan.setter
    def CWPScan(self, CWPScan):
        self._CWPScan = CWPScan

    @property
    def CFWPatch(self):
        return self._CFWPatch

    @CFWPatch.setter
    def CFWPatch(self, CFWPatch):
        self._CFWPatch = CFWPatch

    @property
    def WafPatch(self):
        return self._WafPatch

    @WafPatch.setter
    def WafPatch(self, WafPatch):
        self._WafPatch = WafPatch

    @property
    def CWPFix(self):
        return self._CWPFix

    @CWPFix.setter
    def CWPFix(self, CWPFix):
        self._CWPFix = CWPFix


    def _deserialize(self, params):
        self._StateCode = params.get("StateCode")
        if params.get("DataBug") is not None:
            self._DataBug = []
            for item in params.get("DataBug"):
                obj = BugInfoDetail()
                obj._deserialize(item)
                self._DataBug.append(obj)
        if params.get("DataAsset") is not None:
            self._DataAsset = []
            for item in params.get("DataAsset"):
                obj = AssetInfoDetail()
                obj._deserialize(item)
                self._DataAsset.append(obj)
        self._VSSScan = params.get("VSSScan")
        self._CWPScan = params.get("CWPScan")
        self._CFWPatch = params.get("CFWPatch")
        self._WafPatch = params.get("WafPatch")
        self._CWPFix = params.get("CWPFix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbAssetInfo(AbstractModel):
    """db资产详情

    """

    def __init__(self):
        r"""
        :param _CFWStatus: 云防状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWStatus: int
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _VpcName: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 私网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _VpcId: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _CFWProtectLevel: 云防保护版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWProtectLevel: int
        :param _Tag: tag信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        """
        self._CFWStatus = None
        self._AssetId = None
        self._VpcName = None
        self._AssetType = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Region = None
        self._VpcId = None
        self._AssetName = None
        self._CFWProtectLevel = None
        self._Tag = None

    @property
    def CFWStatus(self):
        return self._CFWStatus

    @CFWStatus.setter
    def CFWStatus(self, CFWStatus):
        self._CFWStatus = CFWStatus

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def CFWProtectLevel(self):
        return self._CFWProtectLevel

    @CFWProtectLevel.setter
    def CFWProtectLevel(self, CFWProtectLevel):
        self._CFWProtectLevel = CFWProtectLevel

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._CFWStatus = params.get("CFWStatus")
        self._AssetId = params.get("AssetId")
        self._VpcName = params.get("VpcName")
        self._AssetType = params.get("AssetType")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._AssetName = params.get("AssetName")
        self._CFWProtectLevel = params.get("CFWProtectLevel")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAndIpRequest(AbstractModel):
    """DeleteDomainAndIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Content: 资产
        :type Content: list of PublicIpDomainListKey
        :param _RetainPath: 是否保留路径配置，1：保留，其他：不保留，默认不传为不保留
        :type RetainPath: int
        :param _IgnoreAsset: 以后是否忽略该资产，，1：忽略，其他：不忽略，默认不传为忽略
        :type IgnoreAsset: int
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        :param _Type: 删除类型，取值： ALL， 删除全部，将直接忽略Content的内容；                                           其他值 ,非全部，则Centent必填，  默认为其他值。
        :type Type: str
        """
        self._MemberId = None
        self._Content = None
        self._RetainPath = None
        self._IgnoreAsset = None
        self._Tags = None
        self._Type = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RetainPath(self):
        return self._RetainPath

    @RetainPath.setter
    def RetainPath(self, RetainPath):
        self._RetainPath = RetainPath

    @property
    def IgnoreAsset(self):
        return self._IgnoreAsset

    @IgnoreAsset.setter
    def IgnoreAsset(self, IgnoreAsset):
        self._IgnoreAsset = IgnoreAsset

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = PublicIpDomainListKey()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RetainPath = params.get("RetainPath")
        self._IgnoreAsset = params.get("IgnoreAsset")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAndIpResponse(AbstractModel):
    """DeleteDomainAndIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 删除的资产数量
        :type Data: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DeleteRiskScanTaskRequest(AbstractModel):
    """DeleteRiskScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIdList: 任务id 列表
        :type TaskIdList: list of TaskIdListKey
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._TaskIdList = None
        self._MemberId = None

    @property
    def TaskIdList(self):
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        if params.get("TaskIdList") is not None:
            self._TaskIdList = []
            for item in params.get("TaskIdList"):
                obj = TaskIdListKey()
                obj._deserialize(item)
                self._TaskIdList.append(obj)
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRiskScanTaskResponse(AbstractModel):
    """DeleteRiskScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAlertListRequest(AbstractModel):
    """DescribeAlertList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 标签搜索筛选
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _OperatedMemberId: 被调用的集团账号的成员id
        :type OperatedMemberId: list of str
        :param _AssetType: 0:默认全部 1:资产ID 2:域名
        :type AssetType: int
        """
        self._Filter = None
        self._MemberId = None
        self._OperatedMemberId = None
        self._AssetType = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def OperatedMemberId(self):
        return self._OperatedMemberId

    @OperatedMemberId.setter
    def OperatedMemberId(self, OperatedMemberId):
        self._OperatedMemberId = OperatedMemberId

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._MemberId = params.get("MemberId")
        self._OperatedMemberId = params.get("OperatedMemberId")
        self._AssetType = params.get("AssetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertListResponse(AbstractModel):
    """DescribeAlertList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlertList: 全量告警列表
        :type AlertList: list of AlertInfo
        :param _AlertTypeCount: 告警大类数量
        :type AlertTypeCount: list of TagCount
        :param _TotalCount: 告警总数
        :type TotalCount: int
        :param _ReturnCode: 0：succeed 1：timeout
        :type ReturnCode: int
        :param _ReturnMsg: 返回状态信息
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlertList = None
        self._AlertTypeCount = None
        self._TotalCount = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def AlertList(self):
        return self._AlertList

    @AlertList.setter
    def AlertList(self, AlertList):
        self._AlertList = AlertList

    @property
    def AlertTypeCount(self):
        return self._AlertTypeCount

    @AlertTypeCount.setter
    def AlertTypeCount(self, AlertTypeCount):
        self._AlertTypeCount = AlertTypeCount

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AlertList") is not None:
            self._AlertList = []
            for item in params.get("AlertList"):
                obj = AlertInfo()
                obj._deserialize(item)
                self._AlertList.append(obj)
        if params.get("AlertTypeCount") is not None:
            self._AlertTypeCount = []
            for item in params.get("AlertTypeCount"):
                obj = TagCount()
                obj._deserialize(item)
                self._AlertTypeCount.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeAssetViewVulRiskListRequest(AbstractModel):
    """DescribeAssetViewVulRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetViewVulRiskListResponse(AbstractModel):
    """DescribeAssetViewVulRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的漏洞风险列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AssetViewVULRiskData
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _Tags: tag枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._InstanceTypeLists = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewVULRiskData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCFWAssetStatisticsRequest(AbstractModel):
    """DescribeCFWAssetStatistics请求参数结构体

    """


class DescribeCFWAssetStatisticsResponse(AbstractModel):
    """DescribeCFWAssetStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkTotal: 网络资产总数
        :type NetworkTotal: int
        :param _ClbTotal: 资产clb数量
        :type ClbTotal: int
        :param _NatTotal: nat数量
        :type NatTotal: int
        :param _PublicAssetTotal: 公网ip数量
        :type PublicAssetTotal: int
        :param _CVMAssetTotal: 主机数量
        :type CVMAssetTotal: int
        :param _CFGTotal: 配置风险
        :type CFGTotal: int
        :param _PortTotal: 端口风险
        :type PortTotal: int
        :param _WebsiteTotal: 内容风险
        :type WebsiteTotal: int
        :param _ServerTotal: 风险服务暴露
        :type ServerTotal: int
        :param _WeakPasswordTotal: 弱口令风险
        :type WeakPasswordTotal: int
        :param _VULTotal: 漏洞风险
        :type VULTotal: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NetworkTotal = None
        self._ClbTotal = None
        self._NatTotal = None
        self._PublicAssetTotal = None
        self._CVMAssetTotal = None
        self._CFGTotal = None
        self._PortTotal = None
        self._WebsiteTotal = None
        self._ServerTotal = None
        self._WeakPasswordTotal = None
        self._VULTotal = None
        self._RequestId = None

    @property
    def NetworkTotal(self):
        return self._NetworkTotal

    @NetworkTotal.setter
    def NetworkTotal(self, NetworkTotal):
        self._NetworkTotal = NetworkTotal

    @property
    def ClbTotal(self):
        return self._ClbTotal

    @ClbTotal.setter
    def ClbTotal(self, ClbTotal):
        self._ClbTotal = ClbTotal

    @property
    def NatTotal(self):
        return self._NatTotal

    @NatTotal.setter
    def NatTotal(self, NatTotal):
        self._NatTotal = NatTotal

    @property
    def PublicAssetTotal(self):
        return self._PublicAssetTotal

    @PublicAssetTotal.setter
    def PublicAssetTotal(self, PublicAssetTotal):
        self._PublicAssetTotal = PublicAssetTotal

    @property
    def CVMAssetTotal(self):
        return self._CVMAssetTotal

    @CVMAssetTotal.setter
    def CVMAssetTotal(self, CVMAssetTotal):
        self._CVMAssetTotal = CVMAssetTotal

    @property
    def CFGTotal(self):
        return self._CFGTotal

    @CFGTotal.setter
    def CFGTotal(self, CFGTotal):
        self._CFGTotal = CFGTotal

    @property
    def PortTotal(self):
        return self._PortTotal

    @PortTotal.setter
    def PortTotal(self, PortTotal):
        self._PortTotal = PortTotal

    @property
    def WebsiteTotal(self):
        return self._WebsiteTotal

    @WebsiteTotal.setter
    def WebsiteTotal(self, WebsiteTotal):
        self._WebsiteTotal = WebsiteTotal

    @property
    def ServerTotal(self):
        return self._ServerTotal

    @ServerTotal.setter
    def ServerTotal(self, ServerTotal):
        self._ServerTotal = ServerTotal

    @property
    def WeakPasswordTotal(self):
        return self._WeakPasswordTotal

    @WeakPasswordTotal.setter
    def WeakPasswordTotal(self, WeakPasswordTotal):
        self._WeakPasswordTotal = WeakPasswordTotal

    @property
    def VULTotal(self):
        return self._VULTotal

    @VULTotal.setter
    def VULTotal(self, VULTotal):
        self._VULTotal = VULTotal

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NetworkTotal = params.get("NetworkTotal")
        self._ClbTotal = params.get("ClbTotal")
        self._NatTotal = params.get("NatTotal")
        self._PublicAssetTotal = params.get("PublicAssetTotal")
        self._CVMAssetTotal = params.get("CVMAssetTotal")
        self._CFGTotal = params.get("CFGTotal")
        self._PortTotal = params.get("PortTotal")
        self._WebsiteTotal = params.get("WebsiteTotal")
        self._ServerTotal = params.get("ServerTotal")
        self._WeakPasswordTotal = params.get("WeakPasswordTotal")
        self._VULTotal = params.get("VULTotal")
        self._RequestId = params.get("RequestId")


class DescribeCVMAssetInfoRequest(AbstractModel):
    """DescribeCVMAssetInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: -
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetInfoResponse(AbstractModel):
    """DescribeCVMAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.csip.v20221121.models.AssetBaseInfoResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AssetBaseInfoResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCVMAssetsRequest(AbstractModel):
    """DescribeCVMAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetsResponse(AbstractModel):
    """DescribeCVMAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CVMAssetVO
        :param _RegionList: 地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param _DefenseStatusList: 防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseStatusList: list of FilterDataObject
        :param _VpcList: vpc枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeList: list of FilterDataObject
        :param _SystemTypeList: 操作系统枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemTypeList: list of FilterDataObject
        :param _IpTypeList: ip列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTypeList: list of FilterDataObject
        :param _AppIdList: appid列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of FilterDataObject
        :param _ZoneList: 可用区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneList: list of FilterDataObject
        :param _OsList: os列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OsList: list of FilterDataObject
        :param _AssetMapInstanceTypeList: 资产类型和实例类型的对应关系
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetMapInstanceTypeList: list of AssetInstanceTypeMap
        :param _PublicPrivateAttr: 公网内网枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicPrivateAttr: list of FilterDataObject
        :param _ProtectStatusList: 主机防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectStatusList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._DefenseStatusList = None
        self._VpcList = None
        self._AssetTypeList = None
        self._SystemTypeList = None
        self._IpTypeList = None
        self._AppIdList = None
        self._ZoneList = None
        self._OsList = None
        self._AssetMapInstanceTypeList = None
        self._PublicPrivateAttr = None
        self._ProtectStatusList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def DefenseStatusList(self):
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AssetTypeList(self):
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def SystemTypeList(self):
        return self._SystemTypeList

    @SystemTypeList.setter
    def SystemTypeList(self, SystemTypeList):
        self._SystemTypeList = SystemTypeList

    @property
    def IpTypeList(self):
        return self._IpTypeList

    @IpTypeList.setter
    def IpTypeList(self, IpTypeList):
        self._IpTypeList = IpTypeList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ZoneList(self):
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def OsList(self):
        return self._OsList

    @OsList.setter
    def OsList(self, OsList):
        self._OsList = OsList

    @property
    def AssetMapInstanceTypeList(self):
        return self._AssetMapInstanceTypeList

    @AssetMapInstanceTypeList.setter
    def AssetMapInstanceTypeList(self, AssetMapInstanceTypeList):
        self._AssetMapInstanceTypeList = AssetMapInstanceTypeList

    @property
    def PublicPrivateAttr(self):
        return self._PublicPrivateAttr

    @PublicPrivateAttr.setter
    def PublicPrivateAttr(self, PublicPrivateAttr):
        self._PublicPrivateAttr = PublicPrivateAttr

    @property
    def ProtectStatusList(self):
        return self._ProtectStatusList

    @ProtectStatusList.setter
    def ProtectStatusList(self, ProtectStatusList):
        self._ProtectStatusList = ProtectStatusList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CVMAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("SystemTypeList") is not None:
            self._SystemTypeList = []
            for item in params.get("SystemTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SystemTypeList.append(obj)
        if params.get("IpTypeList") is not None:
            self._IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._IpTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        if params.get("OsList") is not None:
            self._OsList = []
            for item in params.get("OsList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._OsList.append(obj)
        if params.get("AssetMapInstanceTypeList") is not None:
            self._AssetMapInstanceTypeList = []
            for item in params.get("AssetMapInstanceTypeList"):
                obj = AssetInstanceTypeMap()
                obj._deserialize(item)
                self._AssetMapInstanceTypeList.append(obj)
        if params.get("PublicPrivateAttr") is not None:
            self._PublicPrivateAttr = []
            for item in params.get("PublicPrivateAttr"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PublicPrivateAttr.append(obj)
        if params.get("ProtectStatusList") is not None:
            self._ProtectStatusList = []
            for item in params.get("ProtectStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ProtectStatusList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterPodAssetsRequest(AbstractModel):
    """DescribeClusterPodAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPodAssetsResponse(AbstractModel):
    """DescribeClusterPodAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of AssetClusterPod
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _PodStatusList: 集群pod状态枚举
        :type PodStatusList: list of FilterDataObject
        :param _NamespaceList: 命名空间枚举
        :type NamespaceList: list of FilterDataObject
        :param _RegionList: 地域枚举
        :type RegionList: list of FilterDataObject
        :param _AppIdList: 租户枚举
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._PodStatusList = None
        self._NamespaceList = None
        self._RegionList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PodStatusList(self):
        return self._PodStatusList

    @PodStatusList.setter
    def PodStatusList(self, PodStatusList):
        self._PodStatusList = PodStatusList

    @property
    def NamespaceList(self):
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetClusterPod()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("PodStatusList") is not None:
            self._PodStatusList = []
            for item in params.get("PodStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PodStatusList.append(obj)
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbAssetInfoRequest(AbstractModel):
    """DescribeDbAssetInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetInfoResponse(AbstractModel):
    """DescribeDbAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: db资产详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.csip.v20221121.models.DbAssetInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DbAssetInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDbAssetsRequest(AbstractModel):
    """DescribeDbAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _AssetTypes: 资产类型:MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :type AssetTypes: list of str
        """
        self._MemberId = None
        self._Filter = None
        self._AssetTypes = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def AssetTypes(self):
        return self._AssetTypes

    @AssetTypes.setter
    def AssetTypes(self, AssetTypes):
        self._AssetTypes = AssetTypes


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._AssetTypes = params.get("AssetTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetsResponse(AbstractModel):
    """DescribeDbAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: 资产总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DBAssetVO
        :param _RegionList: 地域枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: Vpc枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcList: list of FilterDataObject
        :param _AppIdList: Appid枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of FilterDataObject
        :param _PublicPrivateAttr: 公网内网枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicPrivateAttr: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._PublicPrivateAttr = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def PublicPrivateAttr(self):
        return self._PublicPrivateAttr

    @PublicPrivateAttr.setter
    def PublicPrivateAttr(self, PublicPrivateAttr):
        self._PublicPrivateAttr = PublicPrivateAttr

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DBAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("PublicPrivateAttr") is not None:
            self._PublicPrivateAttr = []
            for item in params.get("PublicPrivateAttr"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PublicPrivateAttr.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainAssetsRequest(AbstractModel):
    """DescribeDomainAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 安全中心自定义标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAssetsResponse(AbstractModel):
    """DescribeDomainAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DomainAssetVO
        :param _DefenseStatusList: 防护状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseStatusList: list of FilterDataObject
        :param _AssetLocationList: 资产归属地列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetLocationList: list of FilterDataObject
        :param _SourceTypeList: 资产类型列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceTypeList: list of FilterDataObject
        :param _RegionList: 地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._DefenseStatusList = None
        self._AssetLocationList = None
        self._SourceTypeList = None
        self._RegionList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DefenseStatusList(self):
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def AssetLocationList(self):
        return self._AssetLocationList

    @AssetLocationList.setter
    def AssetLocationList(self, AssetLocationList):
        self._AssetLocationList = AssetLocationList

    @property
    def SourceTypeList(self):
        return self._SourceTypeList

    @SourceTypeList.setter
    def SourceTypeList(self, SourceTypeList):
        self._SourceTypeList = SourceTypeList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("AssetLocationList") is not None:
            self._AssetLocationList = []
            for item in params.get("AssetLocationList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetLocationList.append(obj)
        if params.get("SourceTypeList") is not None:
            self._SourceTypeList = []
            for item in params.get("SourceTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SourceTypeList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewayAssetsRequest(AbstractModel):
    """DescribeGatewayAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayAssetsResponse(AbstractModel):
    """DescribeGatewayAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of GateWayAsset
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: 资产类型列表
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = GateWayAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenerListRequest(AbstractModel):
    """DescribeListenerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerListResponse(AbstractModel):
    """DescribeListenerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: 监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ClbListenerListInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ClbListenerListInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNICAssetsRequest(AbstractModel):
    """DescribeNICAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNICAssetsResponse(AbstractModel):
    """DescribeNICAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of NICAsset
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: 资产类型列表
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = NICAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationUserInfoRequest(AbstractModel):
    """DescribeOrganizationUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _NotSupportCloud: 不支持多云
        :type NotSupportCloud: bool
        """
        self._MemberId = None
        self._Filter = None
        self._NotSupportCloud = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def NotSupportCloud(self):
        return self._NotSupportCloud

    @NotSupportCloud.setter
    def NotSupportCloud(self, NotSupportCloud):
        self._NotSupportCloud = NotSupportCloud


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._NotSupportCloud = params.get("NotSupportCloud")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationUserInfoResponse(AbstractModel):
    """DescribeOrganizationUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 集团用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of OrganizationUserInfo
        :param _JoinTypeLst: 加入方式枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTypeLst: list of FilterDataObject
        :param _CloudTypeLst: 云厂商枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudTypeLst: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._JoinTypeLst = None
        self._CloudTypeLst = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def JoinTypeLst(self):
        return self._JoinTypeLst

    @JoinTypeLst.setter
    def JoinTypeLst(self, JoinTypeLst):
        self._JoinTypeLst = JoinTypeLst

    @property
    def CloudTypeLst(self):
        return self._CloudTypeLst

    @CloudTypeLst.setter
    def CloudTypeLst(self, CloudTypeLst):
        self._CloudTypeLst = CloudTypeLst

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = OrganizationUserInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("JoinTypeLst") is not None:
            self._JoinTypeLst = []
            for item in params.get("JoinTypeLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._JoinTypeLst.append(obj)
        if params.get("CloudTypeLst") is not None:
            self._CloudTypeLst = []
            for item in params.get("CloudTypeLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CloudTypeLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublicIpAssetsRequest(AbstractModel):
    """DescribePublicIpAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: filte过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 安全中心自定义标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicIpAssetsResponse(AbstractModel):
    """DescribePublicIpAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of IpAssetListVO
        :param _Total: 总数
        :type Total: int
        :param _AssetLocationList: 资产归属地
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetLocationList: list of FilterDataObject
        :param _IpTypeList: ip列表枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTypeList: list of FilterDataObject
        :param _RegionList: 地域列表枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param _DefenseStatusList: 防护枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseStatusList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeList: list of FilterDataObject
        :param _AppIdList: AppId枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._AssetLocationList = None
        self._IpTypeList = None
        self._RegionList = None
        self._DefenseStatusList = None
        self._AssetTypeList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AssetLocationList(self):
        return self._AssetLocationList

    @AssetLocationList.setter
    def AssetLocationList(self, AssetLocationList):
        self._AssetLocationList = AssetLocationList

    @property
    def IpTypeList(self):
        return self._IpTypeList

    @IpTypeList.setter
    def IpTypeList(self, IpTypeList):
        self._IpTypeList = IpTypeList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def DefenseStatusList(self):
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def AssetTypeList(self):
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = IpAssetListVO()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("AssetLocationList") is not None:
            self._AssetLocationList = []
            for item in params.get("AssetLocationList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetLocationList.append(obj)
        if params.get("IpTypeList") is not None:
            self._IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._IpTypeList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewCFGRiskListRequest(AbstractModel):
    """DescribeRiskCenterAssetViewCFGRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewCFGRiskListResponse(AbstractModel):
    """DescribeRiskCenterAssetViewCFGRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的配置风险列表
        :type Data: list of AssetViewCFGRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _CFGNameLists: 配置名列表
        :type CFGNameLists: list of FilterDataObject
        :param _CheckTypeLists: 检查类型列表
        :type CheckTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._CFGNameLists = None
        self._CheckTypeLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def CFGNameLists(self):
        return self._CFGNameLists

    @CFGNameLists.setter
    def CFGNameLists(self, CFGNameLists):
        self._CFGNameLists = CFGNameLists

    @property
    def CheckTypeLists(self):
        return self._CheckTypeLists

    @CheckTypeLists.setter
    def CheckTypeLists(self, CheckTypeLists):
        self._CheckTypeLists = CheckTypeLists

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewCFGRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("CFGNameLists") is not None:
            self._CFGNameLists = []
            for item in params.get("CFGNameLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CFGNameLists.append(obj)
        if params.get("CheckTypeLists") is not None:
            self._CheckTypeLists = []
            for item in params.get("CheckTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewPortRiskListRequest(AbstractModel):
    """DescribeRiskCenterAssetViewPortRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewPortRiskListResponse(AbstractModel):
    """DescribeRiskCenterAssetViewPortRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的配置风险列表
        :type Data: list of AssetViewPortRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _SuggestionLists: 建议列表
        :type SuggestionLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._SuggestionLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def SuggestionLists(self):
        return self._SuggestionLists

    @SuggestionLists.setter
    def SuggestionLists(self, SuggestionLists):
        self._SuggestionLists = SuggestionLists

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewPortRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("SuggestionLists") is not None:
            self._SuggestionLists = []
            for item in params.get("SuggestionLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SuggestionLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewVULRiskListRequest(AbstractModel):
    """DescribeRiskCenterAssetViewVULRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewVULRiskListResponse(AbstractModel):
    """DescribeRiskCenterAssetViewVULRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的漏洞风险列表
        :type Data: list of AssetViewVULRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._InstanceTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewVULRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewWeakPasswordRiskListRequest(AbstractModel):
    """DescribeRiskCenterAssetViewWeakPasswordRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewWeakPasswordRiskListResponse(AbstractModel):
    """DescribeRiskCenterAssetViewWeakPasswordRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 风险列表
        :type Data: list of AssetViewWeakPassRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _PasswordTypeLists: 弱口令类型列表
        :type PasswordTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._InstanceTypeLists = None
        self._PasswordTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def PasswordTypeLists(self):
        return self._PasswordTypeLists

    @PasswordTypeLists.setter
    def PasswordTypeLists(self, PasswordTypeLists):
        self._PasswordTypeLists = PasswordTypeLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewWeakPassRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("PasswordTypeLists") is not None:
            self._PasswordTypeLists = []
            for item in params.get("PasswordTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PasswordTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterPortViewPortRiskListRequest(AbstractModel):
    """DescribeRiskCenterPortViewPortRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterPortViewPortRiskListResponse(AbstractModel):
    """DescribeRiskCenterPortViewPortRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 端口视角的端口风险列表
        :type Data: list of PortViewPortRisk
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _SuggestionLists: 处置建议列表
        :type SuggestionLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._SuggestionLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def SuggestionLists(self):
        return self._SuggestionLists

    @SuggestionLists.setter
    def SuggestionLists(self, SuggestionLists):
        self._SuggestionLists = SuggestionLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = PortViewPortRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("SuggestionLists") is not None:
            self._SuggestionLists = []
            for item in params.get("SuggestionLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SuggestionLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterServerRiskListRequest(AbstractModel):
    """DescribeRiskCenterServerRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterServerRiskListResponse(AbstractModel):
    """DescribeRiskCenterServerRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 风险服务列表
        :type Data: list of ServerRisk
        :param _InstanceTypeLists: 资产类型枚举
        :type InstanceTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._InstanceTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ServerRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterVULViewVULRiskListRequest(AbstractModel):
    """DescribeRiskCenterVULViewVULRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterVULViewVULRiskListResponse(AbstractModel):
    """DescribeRiskCenterVULViewVULRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 漏洞产视角的漏洞风险列表
        :type Data: list of VULViewVULRisk
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULViewVULRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterWebsiteRiskListRequest(AbstractModel):
    """DescribeRiskCenterWebsiteRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterWebsiteRiskListResponse(AbstractModel):
    """DescribeRiskCenterWebsiteRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 内容风险列表
        :type Data: list of WebsiteRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _DetectEngineLists: 风险类型列表
        :type DetectEngineLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._InstanceTypeLists = None
        self._DetectEngineLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def InstanceTypeLists(self):
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def DetectEngineLists(self):
        return self._DetectEngineLists

    @DetectEngineLists.setter
    def DetectEngineLists(self, DetectEngineLists):
        self._DetectEngineLists = DetectEngineLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WebsiteRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("DetectEngineLists") is not None:
            self._DetectEngineLists = []
            for item in params.get("DetectEngineLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DetectEngineLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScanReportListRequest(AbstractModel):
    """DescribeScanReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 列表过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanReportListResponse(AbstractModel):
    """DescribeScanReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 任务日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ScanTaskInfo
        :param _UINList: 主账户ID列表
        :type UINList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._UINList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UINList(self):
        return self._UINList

    @UINList.setter
    def UINList(self, UINList):
        self._UINList = UINList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ScanTaskInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._UINList = params.get("UINList")
        self._RequestId = params.get("RequestId")


class DescribeScanTaskListRequest(AbstractModel):
    """DescribeScanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 标签
        :type Tags: list of Tags
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskListResponse(AbstractModel):
    """DescribeScanTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 任务日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ScanTaskInfoList
        :param _UINList: 主账户ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UINList: list of str
        :param _TaskModeList: 体检模式过滤列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskModeList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._UINList = None
        self._TaskModeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UINList(self):
        return self._UINList

    @UINList.setter
    def UINList(self, UINList):
        self._UINList = UINList

    @property
    def TaskModeList(self):
        return self._TaskModeList

    @TaskModeList.setter
    def TaskModeList(self, TaskModeList):
        self._TaskModeList = TaskModeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ScanTaskInfoList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._UINList = params.get("UINList")
        if params.get("TaskModeList") is not None:
            self._TaskModeList = []
            for item in params.get("TaskModeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._TaskModeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSearchBugInfoRequest(AbstractModel):
    """DescribeSearchBugInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 无
        :type Id: str
        :param _CVEId: id=3时传入该参数
        :type CVEId: str
        """
        self._Id = None
        self._CVEId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CVEId(self):
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CVEId = params.get("CVEId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchBugInfoResponse(AbstractModel):
    """DescribeSearchBugInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 漏洞信息和资产信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.csip.v20221121.models.DataSearchBug`
        :param _ReturnCode: 状态值，0：查询成功，非0：查询失败
        :type ReturnCode: int
        :param _ReturnMsg: 状态信息，success：查询成功，fail：查询失败
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DataSearchBug()
            self._Data._deserialize(params.get("Data"))
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeSubnetAssetsRequest(AbstractModel):
    """DescribeSubnetAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetAssetsResponse(AbstractModel):
    """DescribeSubnetAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of SubnetAsset
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _ZoneList: 可用区列表
        :type ZoneList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._VpcList = None
        self._AppIdList = None
        self._ZoneList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ZoneList(self):
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubnetAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskLogListRequest(AbstractModel):
    """DescribeTaskLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogListResponse(AbstractModel):
    """DescribeTaskLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 报告列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TaskLogInfo
        :param _NotViewNumber: 待查看数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NotViewNumber: int
        :param _ReportTemplateNumber: 报告模板数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTemplateNumber: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._NotViewNumber = None
        self._ReportTemplateNumber = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def NotViewNumber(self):
        return self._NotViewNumber

    @NotViewNumber.setter
    def NotViewNumber(self, NotViewNumber):
        self._NotViewNumber = NotViewNumber

    @property
    def ReportTemplateNumber(self):
        return self._ReportTemplateNumber

    @ReportTemplateNumber.setter
    def ReportTemplateNumber(self, ReportTemplateNumber):
        self._ReportTemplateNumber = ReportTemplateNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskLogInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._NotViewNumber = params.get("NotViewNumber")
        self._ReportTemplateNumber = params.get("ReportTemplateNumber")
        self._RequestId = params.get("RequestId")


class DescribeTaskLogURLRequest(AbstractModel):
    """DescribeTaskLogURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 0: 预览， 1: 下载
        :type Type: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _ReportItemKeyList: 任务报告Id 列表
        :type ReportItemKeyList: list of ReportItemKey
        :param _ReportTaskIdList: 报告中任务id列表
        :type ReportTaskIdList: list of ReportTaskIdList
        """
        self._Type = None
        self._MemberId = None
        self._ReportItemKeyList = None
        self._ReportTaskIdList = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def ReportItemKeyList(self):
        return self._ReportItemKeyList

    @ReportItemKeyList.setter
    def ReportItemKeyList(self, ReportItemKeyList):
        self._ReportItemKeyList = ReportItemKeyList

    @property
    def ReportTaskIdList(self):
        return self._ReportTaskIdList

    @ReportTaskIdList.setter
    def ReportTaskIdList(self, ReportTaskIdList):
        self._ReportTaskIdList = ReportTaskIdList


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._MemberId = params.get("MemberId")
        if params.get("ReportItemKeyList") is not None:
            self._ReportItemKeyList = []
            for item in params.get("ReportItemKeyList"):
                obj = ReportItemKey()
                obj._deserialize(item)
                self._ReportItemKeyList.append(obj)
        if params.get("ReportTaskIdList") is not None:
            self._ReportTaskIdList = []
            for item in params.get("ReportTaskIdList"):
                obj = ReportTaskIdList()
                obj._deserialize(item)
                self._ReportTaskIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogURLResponse(AbstractModel):
    """DescribeTaskLogURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回报告临时下载url
        :type Data: list of TaskLogURL
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskLogURL()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopAttackInfoRequest(AbstractModel):
    """DescribeTopAttackInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OperatedMemberId: 被调用的集团账号的成员id
        :type OperatedMemberId: list of str
        """
        self._OperatedMemberId = None

    @property
    def OperatedMemberId(self):
        return self._OperatedMemberId

    @OperatedMemberId.setter
    def OperatedMemberId(self, OperatedMemberId):
        self._OperatedMemberId = OperatedMemberId


    def _deserialize(self, params):
        self._OperatedMemberId = params.get("OperatedMemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopAttackInfoResponse(AbstractModel):
    """DescribeTopAttackInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopAttackInfo: Top攻击类型/攻击者次数
        :type TopAttackInfo: list of TagCount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopAttackInfo = None
        self._RequestId = None

    @property
    def TopAttackInfo(self):
        return self._TopAttackInfo

    @TopAttackInfo.setter
    def TopAttackInfo(self, TopAttackInfo):
        self._TopAttackInfo = TopAttackInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopAttackInfo") is not None:
            self._TopAttackInfo = []
            for item in params.get("TopAttackInfo"):
                obj = TagCount()
                obj._deserialize(item)
                self._TopAttackInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVULRiskAdvanceCFGListRequest(AbstractModel):
    """DescribeVULRiskAdvanceCFGList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Filter: 过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._TaskId = None
        self._Filter = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._TaskId = params.get("TaskId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVULRiskAdvanceCFGListResponse(AbstractModel):
    """DescribeVULRiskAdvanceCFGList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 配置项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of VULRiskAdvanceCFGList
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RiskLevelLists: 风险等级过滤列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevelLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型过滤列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VULTypeLists: list of FilterDataObject
        :param _CheckFromLists: 识别来源过滤列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckFromLists: list of FilterDataObject
        :param _VulTagList: 漏洞标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulTagList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RiskLevelLists = None
        self._VULTypeLists = None
        self._CheckFromLists = None
        self._VulTagList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RiskLevelLists(self):
        return self._RiskLevelLists

    @RiskLevelLists.setter
    def RiskLevelLists(self, RiskLevelLists):
        self._RiskLevelLists = RiskLevelLists

    @property
    def VULTypeLists(self):
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def CheckFromLists(self):
        return self._CheckFromLists

    @CheckFromLists.setter
    def CheckFromLists(self, CheckFromLists):
        self._CheckFromLists = CheckFromLists

    @property
    def VulTagList(self):
        return self._VulTagList

    @VulTagList.setter
    def VulTagList(self, VulTagList):
        self._VulTagList = VulTagList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULRiskAdvanceCFGList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RiskLevelLists") is not None:
            self._RiskLevelLists = []
            for item in params.get("RiskLevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RiskLevelLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("CheckFromLists") is not None:
            self._CheckFromLists = []
            for item in params.get("CheckFromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckFromLists.append(obj)
        if params.get("VulTagList") is not None:
            self._VulTagList = []
            for item in params.get("VulTagList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VulTagList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVULRiskDetailRequest(AbstractModel):
    """DescribeVULRiskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _RiskId: 风险id
        :type RiskId: str
        :param _PCMGRId: pcMgrId
        :type PCMGRId: str
        """
        self._MemberId = None
        self._RiskId = None
        self._PCMGRId = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskId(self):
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def PCMGRId(self):
        return self._PCMGRId

    @PCMGRId.setter
    def PCMGRId(self, PCMGRId):
        self._PCMGRId = PCMGRId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._RiskId = params.get("RiskId")
        self._PCMGRId = params.get("PCMGRId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVULRiskDetailResponse(AbstractModel):
    """DescribeVULRiskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceSupport: 安全产品支持情况
        :type ServiceSupport: list of ServiceSupport
        :param _VulTrend: 漏洞趋势
        :type VulTrend: list of VulTrend
        :param _VulData: 漏洞补充信息
        :type VulData: :class:`tencentcloud.csip.v20221121.models.VULRiskInfo`
        :param _QuestionId: 小助手问答id
        :type QuestionId: str
        :param _SessionId: 会话id
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceSupport = None
        self._VulTrend = None
        self._VulData = None
        self._QuestionId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def ServiceSupport(self):
        return self._ServiceSupport

    @ServiceSupport.setter
    def ServiceSupport(self, ServiceSupport):
        self._ServiceSupport = ServiceSupport

    @property
    def VulTrend(self):
        return self._VulTrend

    @VulTrend.setter
    def VulTrend(self, VulTrend):
        self._VulTrend = VulTrend

    @property
    def VulData(self):
        return self._VulData

    @VulData.setter
    def VulData(self, VulData):
        self._VulData = VulData

    @property
    def QuestionId(self):
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceSupport") is not None:
            self._ServiceSupport = []
            for item in params.get("ServiceSupport"):
                obj = ServiceSupport()
                obj._deserialize(item)
                self._ServiceSupport.append(obj)
        if params.get("VulTrend") is not None:
            self._VulTrend = []
            for item in params.get("VulTrend"):
                obj = VulTrend()
                obj._deserialize(item)
                self._VulTrend.append(obj)
        if params.get("VulData") is not None:
            self._VulData = VULRiskInfo()
            self._VulData._deserialize(params.get("VulData"))
        self._QuestionId = params.get("QuestionId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeVpcAssetsRequest(AbstractModel):
    """DescribeVpcAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcAssetsResponse(AbstractModel):
    """DescribeVpcAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of Vpc
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._VpcList = None
        self._RegionList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Vpc()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulViewVulRiskListRequest(AbstractModel):
    """DescribeVulViewVulRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulViewVulRiskListResponse(AbstractModel):
    """DescribeVulViewVulRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 漏洞产视角的漏洞风险列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of VULViewVULRiskData
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _Tags: tag枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULViewVULRiskData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DomainAssetVO(AbstractModel):
    """域名资产

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: list of str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: list of str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: list of str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: list of str
        :param _WAFStatus: Waf状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WAFStatus: int
        :param _AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _AppId: Appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 账号id
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _IsCloud: 是否云上资产
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCloud: int
        :param _Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param _Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param _Intercept: 网络拦截
注意：此字段可能返回 null，表示取不到有效值。
        :type Intercept: int
        :param _InBandwidth: 入站峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InBandwidth: str
        :param _OutBandwidth: 出站峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type OutBandwidth: str
        :param _InFlow: 入站累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type InFlow: str
        :param _OutFlow: 出站累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _PortRisk: 端口风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param _SubDomain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDomain: str
        :param _SeverIp: 解析ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SeverIp: list of str
        :param _BotCount: bot攻击数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BotCount: int
        :param _WeakPassword: 弱口令风险
注意：此字段可能返回 null，表示取不到有效值。
        :type WeakPassword: int
        :param _WebContentRisk: 内容风险
注意：此字段可能返回 null，表示取不到有效值。
        :type WebContentRisk: int
        :param _Tag: tag标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _SourceType: 关联实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param _MemberId: memberiD
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param _CCAttack: cc攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type CCAttack: int
        :param _WebAttack: web攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type WebAttack: int
        :param _ServiceRisk: 风险服务暴露数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceRisk: int
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        :param _VerifyDomain: 待确认资产的随机三级域名
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyDomain: str
        :param _VerifyTXTRecord: 待确认资产的TXT记录内容
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTXTRecord: str
        :param _VerifyStatus: 待确认资产的认证状态，0-待认证，1-认证成功，2-认证中，3-txt认证失败，4-人工认证失败
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyStatus: int
        :param _BotAccessCount: bot访问数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BotAccessCount: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._WAFStatus = None
        self._AssetCreateTime = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._IsCore = None
        self._IsCloud = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._SubDomain = None
        self._SeverIp = None
        self._BotCount = None
        self._WeakPassword = None
        self._WebContentRisk = None
        self._Tag = None
        self._SourceType = None
        self._MemberId = None
        self._CCAttack = None
        self._WebAttack = None
        self._ServiceRisk = None
        self._IsNewAsset = None
        self._VerifyDomain = None
        self._VerifyTXTRecord = None
        self._VerifyStatus = None
        self._BotAccessCount = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def WAFStatus(self):
        return self._WAFStatus

    @WAFStatus.setter
    def WAFStatus(self, WAFStatus):
        self._WAFStatus = WAFStatus

    @property
    def AssetCreateTime(self):
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsCloud(self):
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def PortRisk(self):
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def SeverIp(self):
        return self._SeverIp

    @SeverIp.setter
    def SeverIp(self, SeverIp):
        self._SeverIp = SeverIp

    @property
    def BotCount(self):
        return self._BotCount

    @BotCount.setter
    def BotCount(self, BotCount):
        self._BotCount = BotCount

    @property
    def WeakPassword(self):
        return self._WeakPassword

    @WeakPassword.setter
    def WeakPassword(self, WeakPassword):
        self._WeakPassword = WeakPassword

    @property
    def WebContentRisk(self):
        return self._WebContentRisk

    @WebContentRisk.setter
    def WebContentRisk(self, WebContentRisk):
        self._WebContentRisk = WebContentRisk

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def CCAttack(self):
        return self._CCAttack

    @CCAttack.setter
    def CCAttack(self, CCAttack):
        self._CCAttack = CCAttack

    @property
    def WebAttack(self):
        return self._WebAttack

    @WebAttack.setter
    def WebAttack(self, WebAttack):
        self._WebAttack = WebAttack

    @property
    def ServiceRisk(self):
        return self._ServiceRisk

    @ServiceRisk.setter
    def ServiceRisk(self, ServiceRisk):
        self._ServiceRisk = ServiceRisk

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def VerifyDomain(self):
        return self._VerifyDomain

    @VerifyDomain.setter
    def VerifyDomain(self, VerifyDomain):
        self._VerifyDomain = VerifyDomain

    @property
    def VerifyTXTRecord(self):
        return self._VerifyTXTRecord

    @VerifyTXTRecord.setter
    def VerifyTXTRecord(self, VerifyTXTRecord):
        self._VerifyTXTRecord = VerifyTXTRecord

    @property
    def VerifyStatus(self):
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def BotAccessCount(self):
        return self._BotAccessCount

    @BotAccessCount.setter
    def BotAccessCount(self, BotAccessCount):
        self._BotAccessCount = BotAccessCount


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._WAFStatus = params.get("WAFStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._IsCore = params.get("IsCore")
        self._IsCloud = params.get("IsCloud")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        self._SubDomain = params.get("SubDomain")
        self._SeverIp = params.get("SeverIp")
        self._BotCount = params.get("BotCount")
        self._WeakPassword = params.get("WeakPassword")
        self._WebContentRisk = params.get("WebContentRisk")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._SourceType = params.get("SourceType")
        self._MemberId = params.get("MemberId")
        self._CCAttack = params.get("CCAttack")
        self._WebAttack = params.get("WebAttack")
        self._ServiceRisk = params.get("ServiceRisk")
        self._IsNewAsset = params.get("IsNewAsset")
        self._VerifyDomain = params.get("VerifyDomain")
        self._VerifyTXTRecord = params.get("VerifyTXTRecord")
        self._VerifyStatus = params.get("VerifyStatus")
        self._BotAccessCount = params.get("BotAccessCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Element(AbstractModel):
    """统计条目

    """

    def __init__(self):
        r"""
        :param _Key: 统计类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 统计对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """列表查询接口采用新filter 接口，直接传给后台供后台查询过滤

    """

    def __init__(self):
        r"""
        :param _Limit: 查询数量限制
        :type Limit: int
        :param _Offset: 查询偏移位置
        :type Offset: int
        :param _Order: 排序采用升序还是降序 升:asc 降 desc
        :type Order: str
        :param _By: 需排序的字段
        :type By: str
        :param _Filters: 过滤的列及内容
        :type Filters: list of WhereFilter
        :param _StartTime: 可填无， 日志使用查询时间
        :type StartTime: str
        :param _EndTime: 可填无， 日志使用查询时间
        :type EndTime: str
        """
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = WhereFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterDataObject(AbstractModel):
    """过滤数据对象

    """

    def __init__(self):
        r"""
        :param _Value: 英文翻译
        :type Value: str
        :param _Text: 中文翻译
        :type Text: str
        """
        self._Value = None
        self._Text = None

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GateWayAsset(AbstractModel):
    """网关资产

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _PrivateIp: 私有ip
        :type PrivateIp: str
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _Region: 区域
        :type Region: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _VpcName: 私有网络名
        :type VpcName: str
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _OutboundPeakBandwidth: 出向峰值带宽
        :type OutboundPeakBandwidth: str
        :param _InboundPeakBandwidth: 入向峰值带宽
        :type InboundPeakBandwidth: str
        :param _OutboundCumulativeFlow: 出站累计流量
        :type OutboundCumulativeFlow: str
        :param _InboundCumulativeFlow: 入站累计流量
        :type InboundCumulativeFlow: str
        :param _NetworkAttack: 网络攻击
        :type NetworkAttack: int
        :param _ExposedPort: 暴露端口
        :type ExposedPort: int
        :param _ExposedVUL: 暴露漏洞
        :type ExposedVUL: int
        :param _ConfigureRisk: 配置风险
        :type ConfigureRisk: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ScanTask: 任务数
        :type ScanTask: int
        :param _LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param _Nick: 昵称
        :type Nick: str
        :param _AddressIPV6: ipv6地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPV6: str
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _RiskExposure: 风险服务暴露
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskExposure: int
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        :param _Status: 网关状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _EngineRegion: TSE的网关真实地域
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._OutboundPeakBandwidth = None
        self._InboundPeakBandwidth = None
        self._OutboundCumulativeFlow = None
        self._InboundCumulativeFlow = None
        self._NetworkAttack = None
        self._ExposedPort = None
        self._ExposedVUL = None
        self._ConfigureRisk = None
        self._CreateTime = None
        self._ScanTask = None
        self._LastScanTime = None
        self._Nick = None
        self._AddressIPV6 = None
        self._IsCore = None
        self._RiskExposure = None
        self._IsNewAsset = None
        self._Status = None
        self._EngineRegion = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OutboundPeakBandwidth(self):
        return self._OutboundPeakBandwidth

    @OutboundPeakBandwidth.setter
    def OutboundPeakBandwidth(self, OutboundPeakBandwidth):
        self._OutboundPeakBandwidth = OutboundPeakBandwidth

    @property
    def InboundPeakBandwidth(self):
        return self._InboundPeakBandwidth

    @InboundPeakBandwidth.setter
    def InboundPeakBandwidth(self, InboundPeakBandwidth):
        self._InboundPeakBandwidth = InboundPeakBandwidth

    @property
    def OutboundCumulativeFlow(self):
        return self._OutboundCumulativeFlow

    @OutboundCumulativeFlow.setter
    def OutboundCumulativeFlow(self, OutboundCumulativeFlow):
        self._OutboundCumulativeFlow = OutboundCumulativeFlow

    @property
    def InboundCumulativeFlow(self):
        return self._InboundCumulativeFlow

    @InboundCumulativeFlow.setter
    def InboundCumulativeFlow(self, InboundCumulativeFlow):
        self._InboundCumulativeFlow = InboundCumulativeFlow

    @property
    def NetworkAttack(self):
        return self._NetworkAttack

    @NetworkAttack.setter
    def NetworkAttack(self, NetworkAttack):
        self._NetworkAttack = NetworkAttack

    @property
    def ExposedPort(self):
        return self._ExposedPort

    @ExposedPort.setter
    def ExposedPort(self, ExposedPort):
        self._ExposedPort = ExposedPort

    @property
    def ExposedVUL(self):
        return self._ExposedVUL

    @ExposedVUL.setter
    def ExposedVUL(self, ExposedVUL):
        self._ExposedVUL = ExposedVUL

    @property
    def ConfigureRisk(self):
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AddressIPV6(self):
        return self._AddressIPV6

    @AddressIPV6.setter
    def AddressIPV6(self, AddressIPV6):
        self._AddressIPV6 = AddressIPV6

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def RiskExposure(self):
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._OutboundPeakBandwidth = params.get("OutboundPeakBandwidth")
        self._InboundPeakBandwidth = params.get("InboundPeakBandwidth")
        self._OutboundCumulativeFlow = params.get("OutboundCumulativeFlow")
        self._InboundCumulativeFlow = params.get("InboundCumulativeFlow")
        self._NetworkAttack = params.get("NetworkAttack")
        self._ExposedPort = params.get("ExposedPort")
        self._ExposedVUL = params.get("ExposedVUL")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._CreateTime = params.get("CreateTime")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._Nick = params.get("Nick")
        self._AddressIPV6 = params.get("AddressIPV6")
        self._IsCore = params.get("IsCore")
        self._RiskExposure = params.get("RiskExposure")
        self._IsNewAsset = params.get("IsNewAsset")
        self._Status = params.get("Status")
        self._EngineRegion = params.get("EngineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAssetListVO(AbstractModel):
    """ip列表

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AssetName: 资产name
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _CFWStatus: 云防状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWStatus: int
        :param _AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PublicIpType: 公网ip类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpType: int
        :param _VpcId: vpc
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: vpc名
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _AppId: appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _IsCore: 核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _IsCloud: 云上
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCloud: int
        :param _Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param _Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param _Intercept: 网络拦截
注意：此字段可能返回 null，表示取不到有效值。
        :type Intercept: int
        :param _InBandwidth: 入向带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InBandwidth: str
        :param _OutBandwidth: 出向带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type OutBandwidth: str
        :param _InFlow: 入向流量
注意：此字段可能返回 null，表示取不到有效值。
        :type InFlow: str
        :param _OutFlow: 出向流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _PortRisk: 端口风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param _WeakPassword: 弱口令
注意：此字段可能返回 null，表示取不到有效值。
        :type WeakPassword: int
        :param _WebContentRisk: 内容风险
注意：此字段可能返回 null，表示取不到有效值。
        :type WebContentRisk: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _AddressId: eip主键
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressId: str
        :param _MemberId: memberid信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param _RiskExposure: 风险服务暴露
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskExposure: int
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        :param _VerifyStatus: 资产认证状态，0-待认证，1-认证成功，2-认证中，3+-认证失败
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyStatus: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._CFWStatus = None
        self._AssetCreateTime = None
        self._PublicIp = None
        self._PublicIpType = None
        self._VpcId = None
        self._VpcName = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._IsCore = None
        self._IsCloud = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._WeakPassword = None
        self._WebContentRisk = None
        self._Tag = None
        self._AddressId = None
        self._MemberId = None
        self._RiskExposure = None
        self._IsNewAsset = None
        self._VerifyStatus = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CFWStatus(self):
        return self._CFWStatus

    @CFWStatus.setter
    def CFWStatus(self, CFWStatus):
        self._CFWStatus = CFWStatus

    @property
    def AssetCreateTime(self):
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PublicIpType(self):
        return self._PublicIpType

    @PublicIpType.setter
    def PublicIpType(self, PublicIpType):
        self._PublicIpType = PublicIpType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsCloud(self):
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def PortRisk(self):
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def WeakPassword(self):
        return self._WeakPassword

    @WeakPassword.setter
    def WeakPassword(self, WeakPassword):
        self._WeakPassword = WeakPassword

    @property
    def WebContentRisk(self):
        return self._WebContentRisk

    @WebContentRisk.setter
    def WebContentRisk(self, WebContentRisk):
        self._WebContentRisk = WebContentRisk

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def AddressId(self):
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskExposure(self):
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def VerifyStatus(self):
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._CFWStatus = params.get("CFWStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._PublicIp = params.get("PublicIp")
        self._PublicIpType = params.get("PublicIpType")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._IsCore = params.get("IsCore")
        self._IsCloud = params.get("IsCloud")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        self._WeakPassword = params.get("WeakPassword")
        self._WebContentRisk = params.get("WebContentRisk")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._AddressId = params.get("AddressId")
        self._MemberId = params.get("MemberId")
        self._RiskExposure = params.get("RiskExposure")
        self._IsNewAsset = params.get("IsNewAsset")
        self._VerifyStatus = params.get("VerifyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """KeyValue对

    """

    def __init__(self):
        r"""
        :param _Key: 字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrganizationAccountStatusRequest(AbstractModel):
    """ModifyOrganizationAccountStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 修改集团账号状态，1 开启， 2关闭
        :type Status: int
        """
        self._Status = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrganizationAccountStatusResponse(AbstractModel):
    """ModifyOrganizationAccountStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 返回值为0，则修改成功
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyRiskCenterRiskStatusRequest(AbstractModel):
    """ModifyRiskCenterRiskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskStatusKeys: 风险资产相关数据
        :type RiskStatusKeys: list of RiskCenterStatusKey
        :param _Status: 处置状态，1为已处置、2为已忽略，3为取消已处置，4为取消已忽略
        :type Status: int
        :param _Type: 风险类型，0-端口风险， 1-漏洞风险，2-弱口令风险， 3-网站内容风险，4-配置风险，5-风险服务暴露
        :type Type: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._RiskStatusKeys = None
        self._Status = None
        self._Type = None
        self._MemberId = None

    @property
    def RiskStatusKeys(self):
        return self._RiskStatusKeys

    @RiskStatusKeys.setter
    def RiskStatusKeys(self, RiskStatusKeys):
        self._RiskStatusKeys = RiskStatusKeys

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        if params.get("RiskStatusKeys") is not None:
            self._RiskStatusKeys = []
            for item in params.get("RiskStatusKeys"):
                obj = RiskCenterStatusKey()
                obj._deserialize(item)
                self._RiskStatusKeys.append(obj)
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRiskCenterRiskStatusResponse(AbstractModel):
    """ModifyRiskCenterRiskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRiskCenterScanTaskRequest(AbstractModel):
    """ModifyRiskCenterScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ScanAssetType: 0-全扫，1-指定资产扫，2-排除资产扫，3-手动填写扫；1和2则Assets字段必填，3则SelfDefiningAssets必填
        :type ScanAssetType: int
        :param _ScanItem: 扫描项目；port/poc/weakpass/webcontent/configrisk
        :type ScanItem: list of str
        :param _ScanPlanType: 0-周期任务,1-立即扫描,2-定时扫描,3-自定义；0,2,3则ScanPlanContent必填
        :type ScanPlanType: int
        :param _TaskId: 要修改的任务id
        :type TaskId: str
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Assets: 扫描资产信息列表
        :type Assets: list of TaskAssetObject
        :param _ScanPlanContent: 扫描计划详情
        :type ScanPlanContent: str
        :param _SelfDefiningAssets: ip/域名/url数组
        :type SelfDefiningAssets: list of str
        :param _TaskAdvanceCFG: 高级配置
        :type TaskAdvanceCFG: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        :param _TaskMode: 体检模式，0-标准模式，1-快速模式，2-高级模式，默认标准模式
        :type TaskMode: int
        :param _FinishWebHook: 任务完成回调webhook地址
        :type FinishWebHook: str
        """
        self._TaskName = None
        self._ScanAssetType = None
        self._ScanItem = None
        self._ScanPlanType = None
        self._TaskId = None
        self._MemberId = None
        self._Assets = None
        self._ScanPlanContent = None
        self._SelfDefiningAssets = None
        self._TaskAdvanceCFG = None
        self._TaskMode = None
        self._FinishWebHook = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ScanAssetType(self):
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def ScanItem(self):
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanPlanType(self):
        return self._ScanPlanType

    @ScanPlanType.setter
    def ScanPlanType(self, ScanPlanType):
        self._ScanPlanType = ScanPlanType

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Assets(self):
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def ScanPlanContent(self):
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def SelfDefiningAssets(self):
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def TaskAdvanceCFG(self):
        return self._TaskAdvanceCFG

    @TaskAdvanceCFG.setter
    def TaskAdvanceCFG(self, TaskAdvanceCFG):
        self._TaskAdvanceCFG = TaskAdvanceCFG

    @property
    def TaskMode(self):
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def FinishWebHook(self):
        return self._FinishWebHook

    @FinishWebHook.setter
    def FinishWebHook(self, FinishWebHook):
        self._FinishWebHook = FinishWebHook


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._ScanAssetType = params.get("ScanAssetType")
        self._ScanItem = params.get("ScanItem")
        self._ScanPlanType = params.get("ScanPlanType")
        self._TaskId = params.get("TaskId")
        self._MemberId = params.get("MemberId")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        if params.get("TaskAdvanceCFG") is not None:
            self._TaskAdvanceCFG = TaskAdvanceCFG()
            self._TaskAdvanceCFG._deserialize(params.get("TaskAdvanceCFG"))
        self._TaskMode = params.get("TaskMode")
        self._FinishWebHook = params.get("FinishWebHook")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRiskCenterScanTaskResponse(AbstractModel):
    """ModifyRiskCenterScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _Status: 0，修改成功，其他失败；-1为存在资产未认证
        :type Status: int
        :param _UnAuthAsset: 未认证资产列表
        :type UnAuthAsset: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._UnAuthAsset = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnAuthAsset(self):
        return self._UnAuthAsset

    @UnAuthAsset.setter
    def UnAuthAsset(self, UnAuthAsset):
        self._UnAuthAsset = UnAuthAsset

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._UnAuthAsset = params.get("UnAuthAsset")
        self._RequestId = params.get("RequestId")


class NICAsset(AbstractModel):
    """网卡资产

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _PrivateIp: 私有ip
        :type PrivateIp: str
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _Region: 区域
        :type Region: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _VpcName: 私有网络名
        :type VpcName: str
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _OutboundPeakBandwidth: 出向峰值带宽
        :type OutboundPeakBandwidth: str
        :param _InboundPeakBandwidth: 入向峰值带宽
        :type InboundPeakBandwidth: str
        :param _OutboundCumulativeFlow: 出站累计流量
        :type OutboundCumulativeFlow: str
        :param _InboundCumulativeFlow: 入站累计流量
        :type InboundCumulativeFlow: str
        :param _NetworkAttack: 网络攻击
        :type NetworkAttack: int
        :param _ExposedPort: 暴露端口
        :type ExposedPort: int
        :param _ExposedVUL: 暴露漏洞
        :type ExposedVUL: int
        :param _ConfigureRisk: 配置风险
        :type ConfigureRisk: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ScanTask: 任务数
        :type ScanTask: int
        :param _LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param _Nick: 昵称
        :type Nick: str
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._OutboundPeakBandwidth = None
        self._InboundPeakBandwidth = None
        self._OutboundCumulativeFlow = None
        self._InboundCumulativeFlow = None
        self._NetworkAttack = None
        self._ExposedPort = None
        self._ExposedVUL = None
        self._ConfigureRisk = None
        self._CreateTime = None
        self._ScanTask = None
        self._LastScanTime = None
        self._Nick = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OutboundPeakBandwidth(self):
        return self._OutboundPeakBandwidth

    @OutboundPeakBandwidth.setter
    def OutboundPeakBandwidth(self, OutboundPeakBandwidth):
        self._OutboundPeakBandwidth = OutboundPeakBandwidth

    @property
    def InboundPeakBandwidth(self):
        return self._InboundPeakBandwidth

    @InboundPeakBandwidth.setter
    def InboundPeakBandwidth(self, InboundPeakBandwidth):
        self._InboundPeakBandwidth = InboundPeakBandwidth

    @property
    def OutboundCumulativeFlow(self):
        return self._OutboundCumulativeFlow

    @OutboundCumulativeFlow.setter
    def OutboundCumulativeFlow(self, OutboundCumulativeFlow):
        self._OutboundCumulativeFlow = OutboundCumulativeFlow

    @property
    def InboundCumulativeFlow(self):
        return self._InboundCumulativeFlow

    @InboundCumulativeFlow.setter
    def InboundCumulativeFlow(self, InboundCumulativeFlow):
        self._InboundCumulativeFlow = InboundCumulativeFlow

    @property
    def NetworkAttack(self):
        return self._NetworkAttack

    @NetworkAttack.setter
    def NetworkAttack(self, NetworkAttack):
        self._NetworkAttack = NetworkAttack

    @property
    def ExposedPort(self):
        return self._ExposedPort

    @ExposedPort.setter
    def ExposedPort(self, ExposedPort):
        self._ExposedPort = ExposedPort

    @property
    def ExposedVUL(self):
        return self._ExposedVUL

    @ExposedVUL.setter
    def ExposedVUL(self, ExposedVUL):
        self._ExposedVUL = ExposedVUL

    @property
    def ConfigureRisk(self):
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._OutboundPeakBandwidth = params.get("OutboundPeakBandwidth")
        self._InboundPeakBandwidth = params.get("InboundPeakBandwidth")
        self._OutboundCumulativeFlow = params.get("OutboundCumulativeFlow")
        self._InboundCumulativeFlow = params.get("InboundCumulativeFlow")
        self._NetworkAttack = params.get("NetworkAttack")
        self._ExposedPort = params.get("ExposedPort")
        self._ExposedVUL = params.get("ExposedVUL")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._CreateTime = params.get("CreateTime")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._Nick = params.get("Nick")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewAlertKey(AbstractModel):
    """该结构体用来传入告警的key，以更新告警的status

    """

    def __init__(self):
        r"""
        :param _AppId: 需要更改的用户appid
        :type AppId: str
        :param _Type: 告警类别
        :type Type: str
        :param _SubType: 告警子类别
        :type SubType: str
        :param _Source: 告警来源
        :type Source: str
        :param _Name: 告警名称
        :type Name: str
        :param _Key: 告警key
        :type Key: str
        :param _Date: 时间
        :type Date: str
        :param _Status: 状态
        :type Status: int
        """
        self._AppId = None
        self._Type = None
        self._SubType = None
        self._Source = None
        self._Name = None
        self._Key = None
        self._Date = None
        self._Status = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Type = params.get("Type")
        self._SubType = params.get("SubType")
        self._Source = params.get("Source")
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        self._Date = params.get("Date")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationUserInfo(AbstractModel):
    """集团账号成员详情

    """

    def __init__(self):
        r"""
        :param _Uin: 成员账号Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _NickName: 成员账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _NodeName: 部门节点名称，账号所属部门
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _AssetCount: 资产数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCount: int
        :param _RiskCount: 风险数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCount: int
        :param _AttackCount: 攻击数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackCount: int
        :param _Role: Member/Admin/;成员或者管理员
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _MemberId: 成员账号id
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param _AppId: 成员账号Appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _JoinType: 账号加入方式,create/invite
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinType: str
        :param _CFWProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWProtect: str
        :param _WAFProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
注意：此字段可能返回 null，表示取不到有效值。
        :type WAFProtect: str
        :param _CWPProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPProtect: str
        :param _Enable: 1启用，0未启用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param _CSIPProtect: "Free"       //免费版  "Advanced"   //高级版 "Enterprise" //企业版 "Ultimate"   //旗舰版
注意：此字段可能返回 null，表示取不到有效值。
        :type CSIPProtect: str
        :param _QuotaConsumer: 1为配额消耗者
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaConsumer: int
        :param _CloudType: 账户类型，0为腾讯云账户，1为AWS账户
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudType: int
        :param _SyncFrequency: 0为缺省值，1为10分钟，2为1小时，3为24小时
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncFrequency: int
        :param _IsExpired: 多云账户是否过期
注意：此字段可能返回 null，表示取不到有效值。
        :type IsExpired: bool
        :param _PermissionList: 多云账户 权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PermissionList: list of str
        :param _AuthType: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: int
        :param _TcMemberType: 0 腾讯云集团账户
1 腾讯云接入账户
2 非腾讯云
注意：此字段可能返回 null，表示取不到有效值。
        :type TcMemberType: int
        :param _SubUserCount: 子账号数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SubUserCount: int
        :param _JoinTypeInfo: 加入方式详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTypeInfo: str
        """
        self._Uin = None
        self._NickName = None
        self._NodeName = None
        self._AssetCount = None
        self._RiskCount = None
        self._AttackCount = None
        self._Role = None
        self._MemberId = None
        self._AppId = None
        self._JoinType = None
        self._CFWProtect = None
        self._WAFProtect = None
        self._CWPProtect = None
        self._Enable = None
        self._CSIPProtect = None
        self._QuotaConsumer = None
        self._CloudType = None
        self._SyncFrequency = None
        self._IsExpired = None
        self._PermissionList = None
        self._AuthType = None
        self._TcMemberType = None
        self._SubUserCount = None
        self._JoinTypeInfo = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def AssetCount(self):
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def RiskCount(self):
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def AttackCount(self):
        return self._AttackCount

    @AttackCount.setter
    def AttackCount(self, AttackCount):
        self._AttackCount = AttackCount

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def JoinType(self):
        return self._JoinType

    @JoinType.setter
    def JoinType(self, JoinType):
        self._JoinType = JoinType

    @property
    def CFWProtect(self):
        return self._CFWProtect

    @CFWProtect.setter
    def CFWProtect(self, CFWProtect):
        self._CFWProtect = CFWProtect

    @property
    def WAFProtect(self):
        return self._WAFProtect

    @WAFProtect.setter
    def WAFProtect(self, WAFProtect):
        self._WAFProtect = WAFProtect

    @property
    def CWPProtect(self):
        return self._CWPProtect

    @CWPProtect.setter
    def CWPProtect(self, CWPProtect):
        self._CWPProtect = CWPProtect

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CSIPProtect(self):
        return self._CSIPProtect

    @CSIPProtect.setter
    def CSIPProtect(self, CSIPProtect):
        self._CSIPProtect = CSIPProtect

    @property
    def QuotaConsumer(self):
        return self._QuotaConsumer

    @QuotaConsumer.setter
    def QuotaConsumer(self, QuotaConsumer):
        self._QuotaConsumer = QuotaConsumer

    @property
    def CloudType(self):
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def SyncFrequency(self):
        return self._SyncFrequency

    @SyncFrequency.setter
    def SyncFrequency(self, SyncFrequency):
        self._SyncFrequency = SyncFrequency

    @property
    def IsExpired(self):
        return self._IsExpired

    @IsExpired.setter
    def IsExpired(self, IsExpired):
        self._IsExpired = IsExpired

    @property
    def PermissionList(self):
        return self._PermissionList

    @PermissionList.setter
    def PermissionList(self, PermissionList):
        self._PermissionList = PermissionList

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def TcMemberType(self):
        return self._TcMemberType

    @TcMemberType.setter
    def TcMemberType(self, TcMemberType):
        self._TcMemberType = TcMemberType

    @property
    def SubUserCount(self):
        return self._SubUserCount

    @SubUserCount.setter
    def SubUserCount(self, SubUserCount):
        self._SubUserCount = SubUserCount

    @property
    def JoinTypeInfo(self):
        return self._JoinTypeInfo

    @JoinTypeInfo.setter
    def JoinTypeInfo(self, JoinTypeInfo):
        self._JoinTypeInfo = JoinTypeInfo


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._NodeName = params.get("NodeName")
        self._AssetCount = params.get("AssetCount")
        self._RiskCount = params.get("RiskCount")
        self._AttackCount = params.get("AttackCount")
        self._Role = params.get("Role")
        self._MemberId = params.get("MemberId")
        self._AppId = params.get("AppId")
        self._JoinType = params.get("JoinType")
        self._CFWProtect = params.get("CFWProtect")
        self._WAFProtect = params.get("WAFProtect")
        self._CWPProtect = params.get("CWPProtect")
        self._Enable = params.get("Enable")
        self._CSIPProtect = params.get("CSIPProtect")
        self._QuotaConsumer = params.get("QuotaConsumer")
        self._CloudType = params.get("CloudType")
        self._SyncFrequency = params.get("SyncFrequency")
        self._IsExpired = params.get("IsExpired")
        self._PermissionList = params.get("PermissionList")
        self._AuthType = params.get("AuthType")
        self._TcMemberType = params.get("TcMemberType")
        self._SubUserCount = params.get("SubUserCount")
        self._JoinTypeInfo = params.get("JoinTypeInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortRiskAdvanceCFGParamItem(AbstractModel):
    """端口风险高级配置项

    """

    def __init__(self):
        r"""
        :param _PortSets: 端口集合,以逗号分隔
        :type PortSets: str
        :param _CheckType: 检测项类型，0-系统定义，1-用户自定义
        :type CheckType: int
        :param _Detail: 检测项描述
        :type Detail: str
        :param _Enable: 是否启用，1-启用，0-禁用
        :type Enable: int
        """
        self._PortSets = None
        self._CheckType = None
        self._Detail = None
        self._Enable = None

    @property
    def PortSets(self):
        return self._PortSets

    @PortSets.setter
    def PortSets(self, PortSets):
        self._PortSets = PortSets

    @property
    def CheckType(self):
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._PortSets = params.get("PortSets")
        self._CheckType = params.get("CheckType")
        self._Detail = params.get("Detail")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortViewPortRisk(AbstractModel):
    """端口视角的端口风险对象

    """

    def __init__(self):
        r"""
        :param _NoHandleCount: 未处理数量
        :type NoHandleCount: int
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Component: 组件
        :type Component: str
        :param _Port: 端口
        :type Port: int
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Suggestion: 处置建议,0保持现状、1限制访问、2封禁端口
        :type Suggestion: int
        :param _AffectAssetCount: 影响资产数量
        :type AffectAssetCount: str
        :param _Id: ID
        :type Id: str
        :param _From: 识别来源
        :type From: str
        :param _Index: 前端索引
        :type Index: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _Service: 服务
        :type Service: str
        """
        self._NoHandleCount = None
        self._Level = None
        self._Protocol = None
        self._Component = None
        self._Port = None
        self._RecentTime = None
        self._FirstTime = None
        self._Suggestion = None
        self._AffectAssetCount = None
        self._Id = None
        self._From = None
        self._Index = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._Service = None

    @property
    def NoHandleCount(self):
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def AffectAssetCount(self):
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service


    def _deserialize(self, params):
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Port = params.get("Port")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Suggestion = params.get("Suggestion")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._Id = params.get("Id")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._Service = params.get("Service")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicIpDomainListKey(AbstractModel):
    """公网IP和域名资产列表key

    """

    def __init__(self):
        r"""
        :param _Asset: 资产值
        :type Asset: str
        """
        self._Asset = None

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset


    def _deserialize(self, params):
        self._Asset = params.get("Asset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedEvent(AbstractModel):
    """相关攻击事件结构

    """

    def __init__(self):
        r"""
        :param _EventID: 事件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventID: str
        :param _Description: 事件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _RelatedCount: 与事件关联的告警数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RelatedCount: int
        """
        self._EventID = None
        self._Description = None
        self._RelatedCount = None

    @property
    def EventID(self):
        return self._EventID

    @EventID.setter
    def EventID(self, EventID):
        self._EventID = EventID

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RelatedCount(self):
        return self._RelatedCount

    @RelatedCount.setter
    def RelatedCount(self, RelatedCount):
        self._RelatedCount = RelatedCount


    def _deserialize(self, params):
        self._EventID = params.get("EventID")
        self._Description = params.get("Description")
        self._RelatedCount = params.get("RelatedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportItemKey(AbstractModel):
    """报告项key

    """

    def __init__(self):
        r"""
        :param _TaskLogList: 日志Id列表
        :type TaskLogList: list of str
        """
        self._TaskLogList = None

    @property
    def TaskLogList(self):
        return self._TaskLogList

    @TaskLogList.setter
    def TaskLogList(self, TaskLogList):
        self._TaskLogList = TaskLogList


    def _deserialize(self, params):
        self._TaskLogList = params.get("TaskLogList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTaskIdList(AbstractModel):
    """报告中的task_id list

    """

    def __init__(self):
        r"""
        :param _TaskIdList: 任务id列表
        :type TaskIdList: list of str
        :param _AppId: 租户ID
        :type AppId: str
        """
        self._TaskIdList = None
        self._AppId = None

    @property
    def TaskIdList(self):
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._TaskIdList = params.get("TaskIdList")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskCenterStatusKey(AbstractModel):
    """风险中心状态处理Key

    """

    def __init__(self):
        r"""
        :param _Id: 风险ID
        :type Id: str
        :param _PublicIPDomain: 公网IP/域名
        :type PublicIPDomain: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AppId: APP ID
        :type AppId: str
        """
        self._Id = None
        self._PublicIPDomain = None
        self._InstanceId = None
        self._AppId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PublicIPDomain(self):
        return self._PublicIPDomain

    @PublicIPDomain.setter
    def PublicIPDomain(self, PublicIPDomain):
        self._PublicIPDomain = PublicIPDomain

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PublicIPDomain = params.get("PublicIPDomain")
        self._InstanceId = params.get("InstanceId")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleInfo(AbstractModel):
    """告警数据攻击者或受害者信息

    """

    def __init__(self):
        r"""
        :param _IP: IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _HostIP: HostIP
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIP: str
        :param _OriginIP: 原始IP
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginIP: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _InstanceID: 资产ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        :param _City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param _Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _Country: 国家
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param _Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _Latitude: 纬度
注意：此字段可能返回 null，表示取不到有效值。
        :type Latitude: str
        :param _Longitude: 经度
注意：此字段可能返回 null，表示取不到有效值。
        :type Longitude: str
        :param _Info: 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Name: 企业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Account: 账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param _Family: 家族团伙
注意：此字段可能返回 null，表示取不到有效值。
        :type Family: str
        :param _VirusName: 病毒名
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusName: str
        :param _MD5: MD5值
注意：此字段可能返回 null，表示取不到有效值。
        :type MD5: str
        :param _FileName: 恶意进程文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _AssetType: 1:主机资产 2:域名资产 3:网络资产
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: int
        :param _FromLogAnalysisData: 来源日志分析的信息字段
注意：此字段可能返回 null，表示取不到有效值。
        :type FromLogAnalysisData: list of KeyValue
        :param _ContainerName: 容器名
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param _ContainerID: 容器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerID: str
        """
        self._IP = None
        self._HostIP = None
        self._OriginIP = None
        self._Port = None
        self._InstanceID = None
        self._City = None
        self._Province = None
        self._Country = None
        self._Address = None
        self._Latitude = None
        self._Longitude = None
        self._Info = None
        self._Domain = None
        self._Name = None
        self._Account = None
        self._Family = None
        self._VirusName = None
        self._MD5 = None
        self._FileName = None
        self._AssetType = None
        self._FromLogAnalysisData = None
        self._ContainerName = None
        self._ContainerID = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def HostIP(self):
        return self._HostIP

    @HostIP.setter
    def HostIP(self, HostIP):
        self._HostIP = HostIP

    @property
    def OriginIP(self):
        return self._OriginIP

    @OriginIP.setter
    def OriginIP(self, OriginIP):
        self._OriginIP = OriginIP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Latitude(self):
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Longitude(self):
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Family(self):
        return self._Family

    @Family.setter
    def Family(self, Family):
        self._Family = Family

    @property
    def VirusName(self):
        return self._VirusName

    @VirusName.setter
    def VirusName(self, VirusName):
        self._VirusName = VirusName

    @property
    def MD5(self):
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def FromLogAnalysisData(self):
        return self._FromLogAnalysisData

    @FromLogAnalysisData.setter
    def FromLogAnalysisData(self, FromLogAnalysisData):
        self._FromLogAnalysisData = FromLogAnalysisData

    @property
    def ContainerName(self):
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def ContainerID(self):
        return self._ContainerID

    @ContainerID.setter
    def ContainerID(self, ContainerID):
        self._ContainerID = ContainerID


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._HostIP = params.get("HostIP")
        self._OriginIP = params.get("OriginIP")
        self._Port = params.get("Port")
        self._InstanceID = params.get("InstanceID")
        self._City = params.get("City")
        self._Province = params.get("Province")
        self._Country = params.get("Country")
        self._Address = params.get("Address")
        self._Latitude = params.get("Latitude")
        self._Longitude = params.get("Longitude")
        self._Info = params.get("Info")
        self._Domain = params.get("Domain")
        self._Name = params.get("Name")
        self._Account = params.get("Account")
        self._Family = params.get("Family")
        self._VirusName = params.get("VirusName")
        self._MD5 = params.get("MD5")
        self._FileName = params.get("FileName")
        self._AssetType = params.get("AssetType")
        if params.get("FromLogAnalysisData") is not None:
            self._FromLogAnalysisData = []
            for item in params.get("FromLogAnalysisData"):
                obj = KeyValue()
                obj._deserialize(item)
                self._FromLogAnalysisData.append(obj)
        self._ContainerName = params.get("ContainerName")
        self._ContainerID = params.get("ContainerID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskInfo(AbstractModel):
    """扫描任务详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _Status: 任务状态码：1等待开始  2正在扫描  3扫描出错 4扫描完成
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Progress: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _TaskTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTime: str
        :param _ReportId: 报告ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param _ReportName: 报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportName: str
        :param _ScanPlan: 扫描计划，0-周期任务,1-立即扫描,2-定时扫描,3-自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPlan: int
        :param _AssetCount: 关联的资产数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCount: int
        :param _AppId: APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _UIN: 用户主账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param _UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._TaskId = None
        self._TaskName = None
        self._Status = None
        self._Progress = None
        self._TaskTime = None
        self._ReportId = None
        self._ReportName = None
        self._ScanPlan = None
        self._AssetCount = None
        self._AppId = None
        self._UIN = None
        self._UserName = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskTime(self):
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ReportId(self):
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def ReportName(self):
        return self._ReportName

    @ReportName.setter
    def ReportName(self, ReportName):
        self._ReportName = ReportName

    @property
    def ScanPlan(self):
        return self._ScanPlan

    @ScanPlan.setter
    def ScanPlan(self, ScanPlan):
        self._ScanPlan = ScanPlan

    @property
    def AssetCount(self):
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._TaskTime = params.get("TaskTime")
        self._ReportId = params.get("ReportId")
        self._ReportName = params.get("ReportName")
        self._ScanPlan = params.get("ScanPlan")
        self._AssetCount = params.get("AssetCount")
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskInfoList(AbstractModel):
    """扫描任务列表展示信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _StartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _ScanPlanContent: cron格式
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPlanContent: str
        :param _TaskType: 0-周期任务,1-立即扫描,2-定时扫描,3-自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: int
        :param _InsertTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _SelfDefiningAssets: 自定义指定扫描资产信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfDefiningAssets: list of str
        :param _PredictTime: 预估时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PredictTime: int
        :param _PredictEndTime: 预估完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PredictEndTime: str
        :param _ReportNumber: 报告数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportNumber: int
        :param _AssetNumber: 资产数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetNumber: int
        :param _ScanStatus: 扫描状态, 0-初始值，1-正在扫描，2-扫描完成，3-扫描出错，4-停止扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanStatus: int
        :param _Percent: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: float
        :param _ScanItem: port/poc/weakpass/webcontent/configrisk
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanItem: str
        :param _ScanAssetType: 0-全扫，1-指定资产扫，2-排除资产扫，3-自定义指定资产扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanAssetType: int
        :param _VSSTaskId: vss子任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type VSSTaskId: str
        :param _CSPMTaskId: cspm子任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type CSPMTaskId: str
        :param _CWPPOCId: 主机漏扫子任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPPOCId: str
        :param _CWPBlId: 主机基线子任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPBlId: str
        :param _VSSTaskProcess: vss子任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type VSSTaskProcess: int
        :param _CSPMTaskProcess: cspm子任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CSPMTaskProcess: int
        :param _CWPPOCProcess: 主机漏扫子任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPPOCProcess: int
        :param _CWPBlProcess: 主机基线子任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPBlProcess: int
        :param _ErrorCode: 异常状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: int
        :param _ErrorInfo: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: str
        :param _StartDay: 周期任务开始的天数
注意：此字段可能返回 null，表示取不到有效值。
        :type StartDay: int
        :param _Frequency: 扫描频率,单位天,1-每天,7-每周,30-月,0-扫描一次
注意：此字段可能返回 null，表示取不到有效值。
        :type Frequency: int
        :param _CompleteNumber: 完成次数
注意：此字段可能返回 null，表示取不到有效值。
        :type CompleteNumber: int
        :param _CompleteAssetNumber: 已完成资产个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CompleteAssetNumber: int
        :param _RiskCount: 风险数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCount: int
        :param _Assets: 资产
注意：此字段可能返回 null，表示取不到有效值。
        :type Assets: list of TaskAssetObject
        :param _AppId: 用户Appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _UIN: 用户主账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param _UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _TaskMode: 体检模式，0-标准模式，1-快速模式，2-高级模式
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMode: int
        :param _ScanFrom: 扫描来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanFrom: str
        :param _IsFree: 是否限免体检0不是，1是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFree: int
        :param _IsDelete: 是否可以删除，1-可以，0-不可以，对应多账户管理使用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDelete: int
        :param _SourceType: 任务源类型，0-默认，1-小助手，2-体检项
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: int
        """
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._ScanPlanContent = None
        self._TaskType = None
        self._InsertTime = None
        self._TaskId = None
        self._SelfDefiningAssets = None
        self._PredictTime = None
        self._PredictEndTime = None
        self._ReportNumber = None
        self._AssetNumber = None
        self._ScanStatus = None
        self._Percent = None
        self._ScanItem = None
        self._ScanAssetType = None
        self._VSSTaskId = None
        self._CSPMTaskId = None
        self._CWPPOCId = None
        self._CWPBlId = None
        self._VSSTaskProcess = None
        self._CSPMTaskProcess = None
        self._CWPPOCProcess = None
        self._CWPBlProcess = None
        self._ErrorCode = None
        self._ErrorInfo = None
        self._StartDay = None
        self._Frequency = None
        self._CompleteNumber = None
        self._CompleteAssetNumber = None
        self._RiskCount = None
        self._Assets = None
        self._AppId = None
        self._UIN = None
        self._UserName = None
        self._TaskMode = None
        self._ScanFrom = None
        self._IsFree = None
        self._IsDelete = None
        self._SourceType = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ScanPlanContent(self):
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SelfDefiningAssets(self):
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def PredictTime(self):
        return self._PredictTime

    @PredictTime.setter
    def PredictTime(self, PredictTime):
        self._PredictTime = PredictTime

    @property
    def PredictEndTime(self):
        return self._PredictEndTime

    @PredictEndTime.setter
    def PredictEndTime(self, PredictEndTime):
        self._PredictEndTime = PredictEndTime

    @property
    def ReportNumber(self):
        return self._ReportNumber

    @ReportNumber.setter
    def ReportNumber(self, ReportNumber):
        self._ReportNumber = ReportNumber

    @property
    def AssetNumber(self):
        return self._AssetNumber

    @AssetNumber.setter
    def AssetNumber(self, AssetNumber):
        self._AssetNumber = AssetNumber

    @property
    def ScanStatus(self):
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def ScanItem(self):
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanAssetType(self):
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def VSSTaskId(self):
        return self._VSSTaskId

    @VSSTaskId.setter
    def VSSTaskId(self, VSSTaskId):
        self._VSSTaskId = VSSTaskId

    @property
    def CSPMTaskId(self):
        return self._CSPMTaskId

    @CSPMTaskId.setter
    def CSPMTaskId(self, CSPMTaskId):
        self._CSPMTaskId = CSPMTaskId

    @property
    def CWPPOCId(self):
        return self._CWPPOCId

    @CWPPOCId.setter
    def CWPPOCId(self, CWPPOCId):
        self._CWPPOCId = CWPPOCId

    @property
    def CWPBlId(self):
        return self._CWPBlId

    @CWPBlId.setter
    def CWPBlId(self, CWPBlId):
        self._CWPBlId = CWPBlId

    @property
    def VSSTaskProcess(self):
        return self._VSSTaskProcess

    @VSSTaskProcess.setter
    def VSSTaskProcess(self, VSSTaskProcess):
        self._VSSTaskProcess = VSSTaskProcess

    @property
    def CSPMTaskProcess(self):
        return self._CSPMTaskProcess

    @CSPMTaskProcess.setter
    def CSPMTaskProcess(self, CSPMTaskProcess):
        self._CSPMTaskProcess = CSPMTaskProcess

    @property
    def CWPPOCProcess(self):
        return self._CWPPOCProcess

    @CWPPOCProcess.setter
    def CWPPOCProcess(self, CWPPOCProcess):
        self._CWPPOCProcess = CWPPOCProcess

    @property
    def CWPBlProcess(self):
        return self._CWPBlProcess

    @CWPBlProcess.setter
    def CWPBlProcess(self, CWPBlProcess):
        self._CWPBlProcess = CWPBlProcess

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def StartDay(self):
        return self._StartDay

    @StartDay.setter
    def StartDay(self, StartDay):
        self._StartDay = StartDay

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def CompleteNumber(self):
        return self._CompleteNumber

    @CompleteNumber.setter
    def CompleteNumber(self, CompleteNumber):
        self._CompleteNumber = CompleteNumber

    @property
    def CompleteAssetNumber(self):
        return self._CompleteAssetNumber

    @CompleteAssetNumber.setter
    def CompleteAssetNumber(self, CompleteAssetNumber):
        self._CompleteAssetNumber = CompleteAssetNumber

    @property
    def RiskCount(self):
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def Assets(self):
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def TaskMode(self):
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def ScanFrom(self):
        return self._ScanFrom

    @ScanFrom.setter
    def ScanFrom(self, ScanFrom):
        self._ScanFrom = ScanFrom

    @property
    def IsFree(self):
        return self._IsFree

    @IsFree.setter
    def IsFree(self, IsFree):
        self._IsFree = IsFree

    @property
    def IsDelete(self):
        return self._IsDelete

    @IsDelete.setter
    def IsDelete(self, IsDelete):
        self._IsDelete = IsDelete

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._TaskType = params.get("TaskType")
        self._InsertTime = params.get("InsertTime")
        self._TaskId = params.get("TaskId")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        self._PredictTime = params.get("PredictTime")
        self._PredictEndTime = params.get("PredictEndTime")
        self._ReportNumber = params.get("ReportNumber")
        self._AssetNumber = params.get("AssetNumber")
        self._ScanStatus = params.get("ScanStatus")
        self._Percent = params.get("Percent")
        self._ScanItem = params.get("ScanItem")
        self._ScanAssetType = params.get("ScanAssetType")
        self._VSSTaskId = params.get("VSSTaskId")
        self._CSPMTaskId = params.get("CSPMTaskId")
        self._CWPPOCId = params.get("CWPPOCId")
        self._CWPBlId = params.get("CWPBlId")
        self._VSSTaskProcess = params.get("VSSTaskProcess")
        self._CSPMTaskProcess = params.get("CSPMTaskProcess")
        self._CWPPOCProcess = params.get("CWPPOCProcess")
        self._CWPBlProcess = params.get("CWPBlProcess")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorInfo = params.get("ErrorInfo")
        self._StartDay = params.get("StartDay")
        self._Frequency = params.get("Frequency")
        self._CompleteNumber = params.get("CompleteNumber")
        self._CompleteAssetNumber = params.get("CompleteAssetNumber")
        self._RiskCount = params.get("RiskCount")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        self._TaskMode = params.get("TaskMode")
        self._ScanFrom = params.get("ScanFrom")
        self._IsFree = params.get("IsFree")
        self._IsDelete = params.get("IsDelete")
        self._SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerRisk(AbstractModel):
    """服务风险

    """

    def __init__(self):
        r"""
        :param _ServiceTag: 测绘标签
        :type ServiceTag: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Level: 风险等级 low:低危 high:高危 middle:中危 info:提示 extreme:严重
        :type Level: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _RiskDetails: 风险详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskDetails: str
        :param _Suggestion: 处置建议
        :type Suggestion: str
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: 资产唯一id
        :type Id: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _ServiceSnapshot: 服务快照
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceSnapshot: str
        :param _Url: 服务访问的url
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Index: 列表索引值
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        :param _RiskList: 风险列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskList: list of ServerRiskSuggestion
        :param _SuggestionList: 建议列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuggestionList: list of ServerRiskSuggestion
        :param _StatusCode: HTTP响应状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCode: str
        """
        self._ServiceTag = None
        self._Port = None
        self._AffectAsset = None
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._Level = None
        self._Protocol = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._RiskDetails = None
        self._Suggestion = None
        self._Status = None
        self._Id = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._ServiceSnapshot = None
        self._Url = None
        self._Index = None
        self._RiskList = None
        self._SuggestionList = None
        self._StatusCode = None

    @property
    def ServiceTag(self):
        return self._ServiceTag

    @ServiceTag.setter
    def ServiceTag(self, ServiceTag):
        self._ServiceTag = ServiceTag

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def RiskDetails(self):
        return self._RiskDetails

    @RiskDetails.setter
    def RiskDetails(self, RiskDetails):
        self._RiskDetails = RiskDetails

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ServiceSnapshot(self):
        return self._ServiceSnapshot

    @ServiceSnapshot.setter
    def ServiceSnapshot(self, ServiceSnapshot):
        self._ServiceSnapshot = ServiceSnapshot

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def RiskList(self):
        return self._RiskList

    @RiskList.setter
    def RiskList(self, RiskList):
        self._RiskList = RiskList

    @property
    def SuggestionList(self):
        return self._SuggestionList

    @SuggestionList.setter
    def SuggestionList(self, SuggestionList):
        self._SuggestionList = SuggestionList

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode


    def _deserialize(self, params):
        self._ServiceTag = params.get("ServiceTag")
        self._Port = params.get("Port")
        self._AffectAsset = params.get("AffectAsset")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._Level = params.get("Level")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._RiskDetails = params.get("RiskDetails")
        self._Suggestion = params.get("Suggestion")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._ServiceSnapshot = params.get("ServiceSnapshot")
        self._Url = params.get("Url")
        self._Index = params.get("Index")
        if params.get("RiskList") is not None:
            self._RiskList = []
            for item in params.get("RiskList"):
                obj = ServerRiskSuggestion()
                obj._deserialize(item)
                self._RiskList.append(obj)
        if params.get("SuggestionList") is not None:
            self._SuggestionList = []
            for item in params.get("SuggestionList"):
                obj = ServerRiskSuggestion()
                obj._deserialize(item)
                self._SuggestionList.append(obj)
        self._StatusCode = params.get("StatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerRiskSuggestion(AbstractModel):
    """风险详情

    """

    def __init__(self):
        r"""
        :param _Title: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Body: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        """
        self._Title = None
        self._Body = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Body = params.get("Body")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSupport(AbstractModel):
    """产品支持情况

    """

    def __init__(self):
        r"""
        :param _ServiceName: 产品名称:
"cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix"
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _SupportHandledCount: 已处理的资产总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportHandledCount: int
        :param _SupportTotalCount: 支持的资产总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportTotalCount: int
        :param _IsSupport: 是否支持该产品1支持；0不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupport: bool
        """
        self._ServiceName = None
        self._SupportHandledCount = None
        self._SupportTotalCount = None
        self._IsSupport = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def SupportHandledCount(self):
        return self._SupportHandledCount

    @SupportHandledCount.setter
    def SupportHandledCount(self, SupportHandledCount):
        self._SupportHandledCount = SupportHandledCount

    @property
    def SupportTotalCount(self):
        return self._SupportTotalCount

    @SupportTotalCount.setter
    def SupportTotalCount(self, SupportTotalCount):
        self._SupportTotalCount = SupportTotalCount

    @property
    def IsSupport(self):
        return self._IsSupport

    @IsSupport.setter
    def IsSupport(self, IsSupport):
        self._IsSupport = IsSupport


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._SupportHandledCount = params.get("SupportHandledCount")
        self._SupportTotalCount = params.get("SupportTotalCount")
        self._IsSupport = params.get("IsSupport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRiskCenterTaskRequest(AbstractModel):
    """StopRiskCenterTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIdList: 任务id 列表
        :type TaskIdList: list of TaskIdListKey
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._TaskIdList = None
        self._MemberId = None

    @property
    def TaskIdList(self):
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList

    @property
    def MemberId(self):
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        if params.get("TaskIdList") is not None:
            self._TaskIdList = []
            for item in params.get("TaskIdList"):
                obj = TaskIdListKey()
                obj._deserialize(item)
                self._TaskIdList.append(obj)
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRiskCenterTaskResponse(AbstractModel):
    """StopRiskCenterTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: Status为0， 停止成功
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class SubnetAsset(AbstractModel):
    """子网资产

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _Region: 区域
        :type Region: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _VpcName: 私有网络名
        :type VpcName: str
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _Nick: 昵称
        :type Nick: str
        :param _CIDR: cidr
        :type CIDR: str
        :param _Zone: 可用区
        :type Zone: str
        :param _CVM: cvm数
        :type CVM: int
        :param _AvailableIp: 可用ip数
        :type AvailableIp: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ConfigureRisk: 配置风险
        :type ConfigureRisk: int
        :param _ScanTask: 任务数
        :type ScanTask: int
        :param _LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param _IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._Nick = None
        self._CIDR = None
        self._Zone = None
        self._CVM = None
        self._AvailableIp = None
        self._CreateTime = None
        self._ConfigureRisk = None
        self._ScanTask = None
        self._LastScanTime = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def CIDR(self):
        return self._CIDR

    @CIDR.setter
    def CIDR(self, CIDR):
        self._CIDR = CIDR

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CVM(self):
        return self._CVM

    @CVM.setter
    def CVM(self, CVM):
        self._CVM = CVM

    @property
    def AvailableIp(self):
        return self._AvailableIp

    @AvailableIp.setter
    def AvailableIp(self, AvailableIp):
        self._AvailableIp = AvailableIp

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ConfigureRisk(self):
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

    @property
    def ScanTask(self):
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._Nick = params.get("Nick")
        self._CIDR = params.get("CIDR")
        self._Zone = params.get("Zone")
        self._CVM = params.get("CVM")
        self._AvailableIp = params.get("AvailableIp")
        self._CreateTime = params.get("CreateTime")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _Name: 标签名称
        :type Name: str
        :param _Value: 标签内容
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagCount(AbstractModel):
    """产品日志条数

    """

    def __init__(self):
        r"""
        :param _Name: 产品名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Count: 日志条数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._Name = None
        self._Count = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
    """主机标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskAdvanceCFG(AbstractModel):
    """任务高级配置

    """

    def __init__(self):
        r"""
        :param _PortRisk: 端口风险高级配置
        :type PortRisk: list of PortRiskAdvanceCFGParamItem
        :param _VulRisk: 漏洞风险高级配置
        :type VulRisk: list of TaskCenterVulRiskInputParam
        :param _WeakPwdRisk: 弱口令风险高级配置
        :type WeakPwdRisk: list of TaskCenterWeakPwdRiskInputParam
        :param _CFGRisk: 配置风险高级配置
        :type CFGRisk: list of TaskCenterCFGRiskInputParam
        """
        self._PortRisk = None
        self._VulRisk = None
        self._WeakPwdRisk = None
        self._CFGRisk = None

    @property
    def PortRisk(self):
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulRisk(self):
        return self._VulRisk

    @VulRisk.setter
    def VulRisk(self, VulRisk):
        self._VulRisk = VulRisk

    @property
    def WeakPwdRisk(self):
        return self._WeakPwdRisk

    @WeakPwdRisk.setter
    def WeakPwdRisk(self, WeakPwdRisk):
        self._WeakPwdRisk = WeakPwdRisk

    @property
    def CFGRisk(self):
        return self._CFGRisk

    @CFGRisk.setter
    def CFGRisk(self, CFGRisk):
        self._CFGRisk = CFGRisk


    def _deserialize(self, params):
        if params.get("PortRisk") is not None:
            self._PortRisk = []
            for item in params.get("PortRisk"):
                obj = PortRiskAdvanceCFGParamItem()
                obj._deserialize(item)
                self._PortRisk.append(obj)
        if params.get("VulRisk") is not None:
            self._VulRisk = []
            for item in params.get("VulRisk"):
                obj = TaskCenterVulRiskInputParam()
                obj._deserialize(item)
                self._VulRisk.append(obj)
        if params.get("WeakPwdRisk") is not None:
            self._WeakPwdRisk = []
            for item in params.get("WeakPwdRisk"):
                obj = TaskCenterWeakPwdRiskInputParam()
                obj._deserialize(item)
                self._WeakPwdRisk.append(obj)
        if params.get("CFGRisk") is not None:
            self._CFGRisk = []
            for item in params.get("CFGRisk"):
                obj = TaskCenterCFGRiskInputParam()
                obj._deserialize(item)
                self._CFGRisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskAssetObject(AbstractModel):
    """任务资产项

    """

    def __init__(self):
        r"""
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _InstanceType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _AssetType: 资产分类
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _Asset: ip/域名/资产id，数据库id等
        :type Asset: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Arn: 多云资产唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type Arn: str
        """
        self._AssetName = None
        self._InstanceType = None
        self._AssetType = None
        self._Asset = None
        self._Region = None
        self._Arn = None

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AssetType(self):
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Asset(self):
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Arn(self):
        return self._Arn

    @Arn.setter
    def Arn(self, Arn):
        self._Arn = Arn


    def _deserialize(self, params):
        self._AssetName = params.get("AssetName")
        self._InstanceType = params.get("InstanceType")
        self._AssetType = params.get("AssetType")
        self._Asset = params.get("Asset")
        self._Region = params.get("Region")
        self._Arn = params.get("Arn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterCFGRiskInputParam(AbstractModel):
    """配置风险高级配置

    """

    def __init__(self):
        r"""
        :param _ItemId: 检测项ID
        :type ItemId: str
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        :param _ResourceType: 资源类型
        :type ResourceType: str
        """
        self._ItemId = None
        self._Enable = None
        self._ResourceType = None

    @property
    def ItemId(self):
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._Enable = params.get("Enable")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterVulRiskInputParam(AbstractModel):
    """漏洞风险高级配置

    """

    def __init__(self):
        r"""
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        """
        self._RiskId = None
        self._Enable = None

    @property
    def RiskId(self):
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterWeakPwdRiskInputParam(AbstractModel):
    """弱口令风险高级配置

    """

    def __init__(self):
        r"""
        :param _CheckItemId: 检测项ID
        :type CheckItemId: int
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        """
        self._CheckItemId = None
        self._Enable = None

    @property
    def CheckItemId(self):
        return self._CheckItemId

    @CheckItemId.setter
    def CheckItemId(self, CheckItemId):
        self._CheckItemId = CheckItemId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._CheckItemId = params.get("CheckItemId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskIdListKey(AbstractModel):
    """任务ID列表Key

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLogInfo(AbstractModel):
    """任务报告信息

    """

    def __init__(self):
        r"""
        :param _TaskLogName: 报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskLogName: str
        :param _TaskLogId: 报告ID
        :type TaskLogId: str
        :param _AssetsNumber: 关联资产个数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetsNumber: int
        :param _RiskNumber: 安全风险数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskNumber: int
        :param _Time: 报告生成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param _Status: 任务状态码：0 初始值  1正在扫描  2扫描完成  3扫描出错，4停止，5暂停，6该任务已被重启过
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _TaskName: 关联任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _StartTime: 扫描开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _TaskCenterTaskId: 任务中心扫描任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCenterTaskId: str
        :param _AppId: 租户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _UIN: 主账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param _UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _ReportType: 报告类型： 1安全体检 2日报 3周报 4月报
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportType: int
        :param _TemplateId: 报告模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: int
        """
        self._TaskLogName = None
        self._TaskLogId = None
        self._AssetsNumber = None
        self._RiskNumber = None
        self._Time = None
        self._Status = None
        self._TaskName = None
        self._StartTime = None
        self._TaskCenterTaskId = None
        self._AppId = None
        self._UIN = None
        self._UserName = None
        self._ReportType = None
        self._TemplateId = None

    @property
    def TaskLogName(self):
        return self._TaskLogName

    @TaskLogName.setter
    def TaskLogName(self, TaskLogName):
        self._TaskLogName = TaskLogName

    @property
    def TaskLogId(self):
        return self._TaskLogId

    @TaskLogId.setter
    def TaskLogId(self, TaskLogId):
        self._TaskLogId = TaskLogId

    @property
    def AssetsNumber(self):
        return self._AssetsNumber

    @AssetsNumber.setter
    def AssetsNumber(self, AssetsNumber):
        self._AssetsNumber = AssetsNumber

    @property
    def RiskNumber(self):
        return self._RiskNumber

    @RiskNumber.setter
    def RiskNumber(self, RiskNumber):
        self._RiskNumber = RiskNumber

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskCenterTaskId(self):
        return self._TaskCenterTaskId

    @TaskCenterTaskId.setter
    def TaskCenterTaskId(self, TaskCenterTaskId):
        self._TaskCenterTaskId = TaskCenterTaskId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TaskLogName = params.get("TaskLogName")
        self._TaskLogId = params.get("TaskLogId")
        self._AssetsNumber = params.get("AssetsNumber")
        self._RiskNumber = params.get("RiskNumber")
        self._Time = params.get("Time")
        self._Status = params.get("Status")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._TaskCenterTaskId = params.get("TaskCenterTaskId")
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        self._ReportType = params.get("ReportType")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLogURL(AbstractModel):
    """报告pdf下载的临时链接

    """

    def __init__(self):
        r"""
        :param _URL: 报告下载临时链接
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param _LogId: 任务报告id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogId: str
        :param _TaskLogName: 任务报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskLogName: str
        :param _AppId: APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        """
        self._URL = None
        self._LogId = None
        self._TaskLogName = None
        self._AppId = None

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def LogId(self):
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def TaskLogName(self):
        return self._TaskLogName

    @TaskLogName.setter
    def TaskLogName(self, TaskLogName):
        self._TaskLogName = TaskLogName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._LogId = params.get("LogId")
        self._TaskLogName = params.get("TaskLogName")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertStatusListRequest(AbstractModel):
    """UpdateAlertStatusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 告警ID列表
        :type ID: list of NewAlertKey
        :param _OperateType: 操作类型 
1:撤销处置 
2:标记为已处置 
3:标记忽略 
4:取消标记处置
5:取消标记忽略
        :type OperateType: int
        :param _OperatedMemberId: 被调用的集团账号的成员id
        :type OperatedMemberId: list of str
        """
        self._ID = None
        self._OperateType = None
        self._OperatedMemberId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def OperateType(self):
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType

    @property
    def OperatedMemberId(self):
        return self._OperatedMemberId

    @OperatedMemberId.setter
    def OperatedMemberId(self, OperatedMemberId):
        self._OperatedMemberId = OperatedMemberId


    def _deserialize(self, params):
        if params.get("ID") is not None:
            self._ID = []
            for item in params.get("ID"):
                obj = NewAlertKey()
                obj._deserialize(item)
                self._ID.append(obj)
        self._OperateType = params.get("OperateType")
        self._OperatedMemberId = params.get("OperatedMemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertStatusListResponse(AbstractModel):
    """UpdateAlertStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Code: 结果代码
        :type Code: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._Code = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class VULRiskAdvanceCFGList(AbstractModel):
    """漏洞风险高级配置列表

    """

    def __init__(self):
        r"""
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _VULName: 漏洞名称
        :type VULName: str
        :param _RiskLevel: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type RiskLevel: str
        :param _CheckFrom: 识别来源
        :type CheckFrom: str
        :param _Enable: 是否启用，1-启用，0-禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param _VULType: 风险类型
        :type VULType: str
        :param _ImpactVersion: 影响版本
        :type ImpactVersion: str
        :param _CVE: CVE
注意：此字段可能返回 null，表示取不到有效值。
        :type CVE: str
        :param _VULTag: 漏洞标签
        :type VULTag: list of str
        :param _FixMethod: 修复方式
注意：此字段可能返回 null，表示取不到有效值。
        :type FixMethod: list of str
        :param _ReleaseTime: 披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type EMGCVulType: int
        :param _VULDescribe: 漏洞描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VULDescribe: str
        :param _ImpactComponent: 影响组件
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactComponent: str
        :param _Payload: 漏洞Payload
注意：此字段可能返回 null，表示取不到有效值。
        :type Payload: str
        :param _References: 技术参考
注意：此字段可能返回 null，表示取不到有效值。
        :type References: str
        :param _CVSS: cvss评分
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSS: str
        :param _AttackHeat: 攻击热度
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackHeat: str
        :param _ServiceSupport: 安全产品支持情况
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceSupport: list of ServiceSupport
        :param _RecentScanTime: 最新检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RecentScanTime: str
        """
        self._RiskId = None
        self._VULName = None
        self._RiskLevel = None
        self._CheckFrom = None
        self._Enable = None
        self._VULType = None
        self._ImpactVersion = None
        self._CVE = None
        self._VULTag = None
        self._FixMethod = None
        self._ReleaseTime = None
        self._EMGCVulType = None
        self._VULDescribe = None
        self._ImpactComponent = None
        self._Payload = None
        self._References = None
        self._CVSS = None
        self._AttackHeat = None
        self._ServiceSupport = None
        self._RecentScanTime = None

    @property
    def RiskId(self):
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def VULName(self):
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def RiskLevel(self):
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def CheckFrom(self):
        return self._CheckFrom

    @CheckFrom.setter
    def CheckFrom(self, CheckFrom):
        self._CheckFrom = CheckFrom

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def VULType(self):
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def ImpactVersion(self):
        return self._ImpactVersion

    @ImpactVersion.setter
    def ImpactVersion(self, ImpactVersion):
        self._ImpactVersion = ImpactVersion

    @property
    def CVE(self):
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def VULTag(self):
        return self._VULTag

    @VULTag.setter
    def VULTag(self, VULTag):
        self._VULTag = VULTag

    @property
    def FixMethod(self):
        return self._FixMethod

    @FixMethod.setter
    def FixMethod(self, FixMethod):
        self._FixMethod = FixMethod

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def EMGCVulType(self):
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def VULDescribe(self):
        return self._VULDescribe

    @VULDescribe.setter
    def VULDescribe(self, VULDescribe):
        self._VULDescribe = VULDescribe

    @property
    def ImpactComponent(self):
        return self._ImpactComponent

    @ImpactComponent.setter
    def ImpactComponent(self, ImpactComponent):
        self._ImpactComponent = ImpactComponent

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def CVSS(self):
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def AttackHeat(self):
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def ServiceSupport(self):
        return self._ServiceSupport

    @ServiceSupport.setter
    def ServiceSupport(self, ServiceSupport):
        self._ServiceSupport = ServiceSupport

    @property
    def RecentScanTime(self):
        return self._RecentScanTime

    @RecentScanTime.setter
    def RecentScanTime(self, RecentScanTime):
        self._RecentScanTime = RecentScanTime


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._VULName = params.get("VULName")
        self._RiskLevel = params.get("RiskLevel")
        self._CheckFrom = params.get("CheckFrom")
        self._Enable = params.get("Enable")
        self._VULType = params.get("VULType")
        self._ImpactVersion = params.get("ImpactVersion")
        self._CVE = params.get("CVE")
        self._VULTag = params.get("VULTag")
        self._FixMethod = params.get("FixMethod")
        self._ReleaseTime = params.get("ReleaseTime")
        self._EMGCVulType = params.get("EMGCVulType")
        self._VULDescribe = params.get("VULDescribe")
        self._ImpactComponent = params.get("ImpactComponent")
        self._Payload = params.get("Payload")
        self._References = params.get("References")
        self._CVSS = params.get("CVSS")
        self._AttackHeat = params.get("AttackHeat")
        if params.get("ServiceSupport") is not None:
            self._ServiceSupport = []
            for item in params.get("ServiceSupport"):
                obj = ServiceSupport()
                obj._deserialize(item)
                self._ServiceSupport.append(obj)
        self._RecentScanTime = params.get("RecentScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULRiskInfo(AbstractModel):
    """漏洞风险信息

    """

    def __init__(self):
        r"""
        :param _Fix: 修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Fix: str
        :param _References: 技术参考/参考链接
注意：此字段可能返回 null，表示取不到有效值。
        :type References: str
        :param _Describe: 漏洞描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _ImpactComponent: 受影响组件
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactComponent: list of VulImpactComponentInfo
        """
        self._Fix = None
        self._References = None
        self._Describe = None
        self._ImpactComponent = None

    @property
    def Fix(self):
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ImpactComponent(self):
        return self._ImpactComponent

    @ImpactComponent.setter
    def ImpactComponent(self, ImpactComponent):
        self._ImpactComponent = ImpactComponent


    def _deserialize(self, params):
        self._Fix = params.get("Fix")
        self._References = params.get("References")
        self._Describe = params.get("Describe")
        if params.get("ImpactComponent") is not None:
            self._ImpactComponent = []
            for item in params.get("ImpactComponent"):
                obj = VulImpactComponentInfo()
                obj._deserialize(item)
                self._ImpactComponent.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULViewVULRisk(AbstractModel):
    """漏洞视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: str
        :param _NoHandleCount: 影响资产
        :type NoHandleCount: int
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _Component: 组件
        :type Component: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _AffectAssetCount: 影响资产数量
        :type AffectAssetCount: int
        :param _Id: 风险ID
        :type Id: str
        :param _From: 扫描来源，具体看接口返回枚举类型
        :type From: str
        :param _Index: 前端索引
        :type Index: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _VULName: 漏洞名
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Describe: 描述
        :type Describe: str
        :param _Payload: 漏洞payload
        :type Payload: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _References: 技术参考
        :type References: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _Fix: 修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Fix: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type EMGCVulType: int
        """
        self._Port = None
        self._NoHandleCount = None
        self._Level = None
        self._Component = None
        self._RecentTime = None
        self._FirstTime = None
        self._AffectAssetCount = None
        self._Id = None
        self._From = None
        self._Index = None
        self._VULType = None
        self._VULName = None
        self._CVE = None
        self._Describe = None
        self._Payload = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._Nick = None
        self._AppId = None
        self._Uin = None
        self._Fix = None
        self._EMGCVulType = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NoHandleCount(self):
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def AffectAssetCount(self):
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def VULType(self):
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULName(self):
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Fix(self):
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def EMGCVulType(self):
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Component = params.get("Component")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._Id = params.get("Id")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._VULType = params.get("VULType")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Describe = params.get("Describe")
        self._Payload = params.get("Payload")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._Nick = params.get("Nick")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Fix = params.get("Fix")
        self._EMGCVulType = params.get("EMGCVulType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULViewVULRiskData(AbstractModel):
    """漏洞视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: str
        :param _NoHandleCount: 影响资产
        :type NoHandleCount: int
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _Component: 组件
        :type Component: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _AffectAssetCount: 影响资产数量
        :type AffectAssetCount: int
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _From: 扫描来源，具体看接口返回枚举类型
        :type From: str
        :param _Index: 前端索引
        :type Index: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _VULName: 漏洞名
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Payload: 漏洞payload
        :type Payload: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type EMGCVulType: int
        :param _CVSS: CVSS评分
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSS: float
        :param _PCMGRId: PCMGRId
注意：此字段可能返回 null，表示取不到有效值。
        :type PCMGRId: str
        :param _VulTag: 漏洞标签。搜索时应急 必修传参VulTag=SuggestRepair/EMGCVul
注意：此字段可能返回 null，表示取不到有效值。
        :type VulTag: list of str
        :param _DisclosureTime: 漏洞披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DisclosureTime: str
        :param _AttackHeat: 攻击热度
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackHeat: int
        :param _IsSuggest: 是否必修漏洞，1-是，0-不是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSuggest: int
        :param _HandleTaskId: 处置任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type HandleTaskId: str
        :param _EngineSource: 引擎来源
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineSource: str
        :param _VulRiskId: 新的漏洞风险id
注意：此字段可能返回 null，表示取不到有效值。
        :type VulRiskId: str
        :param _TvdID: 新版漏洞id
注意：此字段可能返回 null，表示取不到有效值。
        :type TvdID: str
        :param _IsOneClick: 是否可以一键体检，1-可以，0-不可以
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOneClick: int
        """
        self._Port = None
        self._NoHandleCount = None
        self._Level = None
        self._Component = None
        self._RecentTime = None
        self._FirstTime = None
        self._AffectAssetCount = None
        self._RiskId = None
        self._From = None
        self._Index = None
        self._VULType = None
        self._VULName = None
        self._CVE = None
        self._Payload = None
        self._AppName = None
        self._AppVersion = None
        self._VULURL = None
        self._Nick = None
        self._AppId = None
        self._Uin = None
        self._EMGCVulType = None
        self._CVSS = None
        self._PCMGRId = None
        self._VulTag = None
        self._DisclosureTime = None
        self._AttackHeat = None
        self._IsSuggest = None
        self._HandleTaskId = None
        self._EngineSource = None
        self._VulRiskId = None
        self._TvdID = None
        self._IsOneClick = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NoHandleCount(self):
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def AffectAssetCount(self):
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def RiskId(self):
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def VULType(self):
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULName(self):
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def EMGCVulType(self):
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def CVSS(self):
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def PCMGRId(self):
        return self._PCMGRId

    @PCMGRId.setter
    def PCMGRId(self, PCMGRId):
        self._PCMGRId = PCMGRId

    @property
    def VulTag(self):
        return self._VulTag

    @VulTag.setter
    def VulTag(self, VulTag):
        self._VulTag = VulTag

    @property
    def DisclosureTime(self):
        return self._DisclosureTime

    @DisclosureTime.setter
    def DisclosureTime(self, DisclosureTime):
        self._DisclosureTime = DisclosureTime

    @property
    def AttackHeat(self):
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def IsSuggest(self):
        return self._IsSuggest

    @IsSuggest.setter
    def IsSuggest(self, IsSuggest):
        self._IsSuggest = IsSuggest

    @property
    def HandleTaskId(self):
        return self._HandleTaskId

    @HandleTaskId.setter
    def HandleTaskId(self, HandleTaskId):
        self._HandleTaskId = HandleTaskId

    @property
    def EngineSource(self):
        return self._EngineSource

    @EngineSource.setter
    def EngineSource(self, EngineSource):
        self._EngineSource = EngineSource

    @property
    def VulRiskId(self):
        return self._VulRiskId

    @VulRiskId.setter
    def VulRiskId(self, VulRiskId):
        self._VulRiskId = VulRiskId

    @property
    def TvdID(self):
        return self._TvdID

    @TvdID.setter
    def TvdID(self, TvdID):
        self._TvdID = TvdID

    @property
    def IsOneClick(self):
        return self._IsOneClick

    @IsOneClick.setter
    def IsOneClick(self, IsOneClick):
        self._IsOneClick = IsOneClick


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Component = params.get("Component")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._RiskId = params.get("RiskId")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._VULType = params.get("VULType")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Payload = params.get("Payload")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._Nick = params.get("Nick")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._EMGCVulType = params.get("EMGCVulType")
        self._CVSS = params.get("CVSS")
        self._PCMGRId = params.get("PCMGRId")
        self._VulTag = params.get("VulTag")
        self._DisclosureTime = params.get("DisclosureTime")
        self._AttackHeat = params.get("AttackHeat")
        self._IsSuggest = params.get("IsSuggest")
        self._HandleTaskId = params.get("HandleTaskId")
        self._EngineSource = params.get("EngineSource")
        self._VulRiskId = params.get("VulRiskId")
        self._TvdID = params.get("TvdID")
        self._IsOneClick = params.get("IsOneClick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vpc(AbstractModel):
    """vpc列表数据

    """

    def __init__(self):
        r"""
        :param _Subnet: 子网(只支持32位)
        :type Subnet: int
        :param _ConnectedVpc: 互通vpc(只支持32位)
        :type ConnectedVpc: int
        :param _AssetId: 资产id
        :type AssetId: str
        :param _Region: region区域
        :type Region: str
        :param _CVM: 云服务器(只支持32位)
        :type CVM: int
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _DNS: dns域名
注意：此字段可能返回 null，表示取不到有效值。
        :type DNS: list of str
        :param _AssetName: 资产名称
        :type AssetName: str
        :param _CIDR: cidr网段
        :type CIDR: str
        :param _CreateTime: 资产创建时间
        :type CreateTime: str
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _Nick: 昵称
        :type Nick: str
        :param _IsNewAsset: 是否新资产 1新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewAsset: int
        :param _IsCore: 是否核心资产1是 2不是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        """
        self._Subnet = None
        self._ConnectedVpc = None
        self._AssetId = None
        self._Region = None
        self._CVM = None
        self._Tag = None
        self._DNS = None
        self._AssetName = None
        self._CIDR = None
        self._CreateTime = None
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._IsNewAsset = None
        self._IsCore = None

    @property
    def Subnet(self):
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def ConnectedVpc(self):
        return self._ConnectedVpc

    @ConnectedVpc.setter
    def ConnectedVpc(self, ConnectedVpc):
        self._ConnectedVpc = ConnectedVpc

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CVM(self):
        return self._CVM

    @CVM.setter
    def CVM(self, CVM):
        self._CVM = CVM

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def DNS(self):
        return self._DNS

    @DNS.setter
    def DNS(self, DNS):
        self._DNS = DNS

    @property
    def AssetName(self):
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def CIDR(self):
        return self._CIDR

    @CIDR.setter
    def CIDR(self, CIDR):
        self._CIDR = CIDR

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def IsNewAsset(self):
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def IsCore(self):
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore


    def _deserialize(self, params):
        self._Subnet = params.get("Subnet")
        self._ConnectedVpc = params.get("ConnectedVpc")
        self._AssetId = params.get("AssetId")
        self._Region = params.get("Region")
        self._CVM = params.get("CVM")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._DNS = params.get("DNS")
        self._AssetName = params.get("AssetName")
        self._CIDR = params.get("CIDR")
        self._CreateTime = params.get("CreateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._IsNewAsset = params.get("IsNewAsset")
        self._IsCore = params.get("IsCore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulImpactComponentInfo(AbstractModel):
    """漏洞影响组件信息

    """

    def __init__(self):
        r"""
        :param _Component: 组件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Component: str
        :param _Version: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self._Component = None
        self._Version = None

    @property
    def Component(self):
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Component = params.get("Component")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulTrend(AbstractModel):
    """漏洞趋势-攻击趋势、影响用户、影响资产

    """

    def __init__(self):
        r"""
        :param _AffectAssetCount: 影响的资产数
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectAssetCount: int
        :param _AffectUserCount: 影响的用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectUserCount: int
        :param _AttackCount: 攻击数
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackCount: int
        :param _Date: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        """
        self._AffectAssetCount = None
        self._AffectUserCount = None
        self._AttackCount = None
        self._Date = None

    @property
    def AffectAssetCount(self):
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def AffectUserCount(self):
        return self._AffectUserCount

    @AffectUserCount.setter
    def AffectUserCount(self, AffectUserCount):
        self._AffectUserCount = AffectUserCount

    @property
    def AttackCount(self):
        return self._AttackCount

    @AttackCount.setter
    def AttackCount(self, AttackCount):
        self._AttackCount = AttackCount

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._AffectUserCount = params.get("AffectUserCount")
        self._AttackCount = params.get("AttackCount")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebsiteRisk(AbstractModel):
    """网站风险对象

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: ID,处理风险使用
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _URL: 风险链接
        :type URL: str
        :param _URLPath: 风险文件地址
        :type URLPath: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _DetectEngine: 类型
        :type DetectEngine: str
        :param _ResultDescribe: 结果描述
        :type ResultDescribe: str
        :param _SourceURL: 源地址url
        :type SourceURL: str
        :param _SourceURLPath: 源文件地址
        :type SourceURLPath: str
        """
        self._AffectAsset = None
        self._Level = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._URL = None
        self._URLPath = None
        self._InstanceType = None
        self._DetectEngine = None
        self._ResultDescribe = None
        self._SourceURL = None
        self._SourceURLPath = None

    @property
    def AffectAsset(self):
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def RecentTime(self):
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def URLPath(self):
        return self._URLPath

    @URLPath.setter
    def URLPath(self, URLPath):
        self._URLPath = URLPath

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DetectEngine(self):
        return self._DetectEngine

    @DetectEngine.setter
    def DetectEngine(self, DetectEngine):
        self._DetectEngine = DetectEngine

    @property
    def ResultDescribe(self):
        return self._ResultDescribe

    @ResultDescribe.setter
    def ResultDescribe(self, ResultDescribe):
        self._ResultDescribe = ResultDescribe

    @property
    def SourceURL(self):
        return self._SourceURL

    @SourceURL.setter
    def SourceURL(self, SourceURL):
        self._SourceURL = SourceURL

    @property
    def SourceURLPath(self):
        return self._SourceURLPath

    @SourceURLPath.setter
    def SourceURLPath(self, SourceURLPath):
        self._SourceURLPath = SourceURLPath


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._URL = params.get("URL")
        self._URLPath = params.get("URLPath")
        self._InstanceType = params.get("InstanceType")
        self._DetectEngine = params.get("DetectEngine")
        self._ResultDescribe = params.get("ResultDescribe")
        self._SourceURL = params.get("SourceURL")
        self._SourceURLPath = params.get("SourceURLPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhereFilter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤的项
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Values: 过滤的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        :param _OperatorType: 中台定义：
1等于 2大于 3小于 4大于等于 5小于等于 6不等于 9模糊匹配 13非模糊匹配 14按位与
精确匹配填 7 模糊匹配填9 

注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorType: int
        """
        self._Name = None
        self._Values = None
        self._OperatorType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def OperatorType(self):
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._OperatorType = params.get("OperatorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        