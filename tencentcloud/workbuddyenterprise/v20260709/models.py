# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class A2AConfig(AbstractModel):
    r"""Agent 的 A2A 对外互通配置与注册态

    """

    def __init__(self):
        r"""
        :param _A2AEnabled: Agent 级唯一 A2A 开关
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AEnabled: bool
        :param _A2APublicRef: 对外 A2A handle（已注册时；仅 DescribeAgent / ModifyAgentA2AConfig 填充）
注意：此字段可能返回 null，表示取不到有效值。
        :type A2APublicRef: str
        :param _A2AEndpoint: 对外 A2A card 发现地址（已注册时）
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AEndpoint: str
        :param _A2AStatus: 注册状态：DRAFT / REGISTERED / DISABLED / NONE / UNKNOWN
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AStatus: str
        """
        self._A2AEnabled = None
        self._A2APublicRef = None
        self._A2AEndpoint = None
        self._A2AStatus = None

    @property
    def A2AEnabled(self):
        r"""Agent 级唯一 A2A 开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._A2AEnabled

    @A2AEnabled.setter
    def A2AEnabled(self, A2AEnabled):
        self._A2AEnabled = A2AEnabled

    @property
    def A2APublicRef(self):
        r"""对外 A2A handle（已注册时；仅 DescribeAgent / ModifyAgentA2AConfig 填充）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2APublicRef

    @A2APublicRef.setter
    def A2APublicRef(self, A2APublicRef):
        self._A2APublicRef = A2APublicRef

    @property
    def A2AEndpoint(self):
        r"""对外 A2A card 发现地址（已注册时）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2AEndpoint

    @A2AEndpoint.setter
    def A2AEndpoint(self, A2AEndpoint):
        self._A2AEndpoint = A2AEndpoint

    @property
    def A2AStatus(self):
        r"""注册状态：DRAFT / REGISTERED / DISABLED / NONE / UNKNOWN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2AStatus

    @A2AStatus.setter
    def A2AStatus(self, A2AStatus):
        self._A2AStatus = A2AStatus


    def _deserialize(self, params):
        self._A2AEnabled = params.get("A2AEnabled")
        self._A2APublicRef = params.get("A2APublicRef")
        self._A2AEndpoint = params.get("A2AEndpoint")
        self._A2AStatus = params.get("A2AStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class A2ASkillInput(AbstractModel):
    r"""A2A skill 录入项（注册外部 Agent 时传入）

    """

    def __init__(self):
        r"""
        :param _A2ASkillId: <p>A2A skill ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type A2ASkillId: str
        :param _Name: <p>skill 名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>skill 描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Tags: <p>标签</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _Examples: <p>示例</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Examples: list of str
        """
        self._A2ASkillId = None
        self._Name = None
        self._Description = None
        self._Tags = None
        self._Examples = None

    @property
    def A2ASkillId(self):
        r"""<p>A2A skill ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2ASkillId

    @A2ASkillId.setter
    def A2ASkillId(self, A2ASkillId):
        self._A2ASkillId = A2ASkillId

    @property
    def Name(self):
        r"""<p>skill 名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>skill 描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        r"""<p>标签</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Examples(self):
        r"""<p>示例</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Examples

    @Examples.setter
    def Examples(self, Examples):
        self._Examples = Examples


    def _deserialize(self, params):
        self._A2ASkillId = params.get("A2ASkillId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._Examples = params.get("Examples")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class A2ASkillItem(AbstractModel):
    r"""A2A skill 列表项（出参用，来自 A2A card 解析结果）

    """

    def __init__(self):
        r"""
        :param _A2ASkillId: A2A skill ID（加 A2A 前缀与内部 SkillId 概念区分）
注意：此字段可能返回 null，表示取不到有效值。
        :type A2ASkillId: str
        :param _Name: skill 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: skill 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._A2ASkillId = None
        self._Name = None
        self._Description = None

    @property
    def A2ASkillId(self):
        r"""A2A skill ID（加 A2A 前缀与内部 SkillId 概念区分）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2ASkillId

    @A2ASkillId.setter
    def A2ASkillId(self, A2ASkillId):
        self._A2ASkillId = A2ASkillId

    @property
    def Name(self):
        r"""skill 名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""skill 描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._A2ASkillId = params.get("A2ASkillId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentItem(AbstractModel):
    r"""Agent 列表项（原 AgentSummary；Agent 级纯字段，不再内嵌版本信息）

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID（全局唯一，数字字符串形态）
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param _AgentName: Agent 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentName: str
        :param _Description: Agent 描述；未填写时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _AvatarUrl: 头像 URL；未设置时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :type AvatarUrl: str
        :param _CreatedTime: 创建时间，RFC3339 UTC 格式（如 2026-06-01T09:00:00Z）
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间，RFC3339 UTC 格式（如 2026-09-10T15:20:00Z）
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _A2AEnabled: Agent 级 A2A 开关。false 恒输出（未开启不等于字段缺失）；A2AEndpoint / A2AStatus 由本接口在 A2A 开启时直接下发
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AEnabled: bool
        :param _SessionCount: 历史会话总数（t_managed_agent_sessions 未软删计数，含全部状态）。注意与 DescribeAgent.ActiveSessionCount（活跃会话数）口径不同
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionCount: int
        :param _Model: 最新版本的模型标识，取 latest_version_id 指向版本的 model；Agent 尚无版本时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: str
        :param _LatestVersionId: 最新版本 ID（latest_version_id 转字符串，19 位雪花数字形态）；Agent 尚无版本时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersionId: str
        :param _LatestVersionName: 最新版本名（可能为 default / test-N / prod-N 任意类型）；Agent 尚无版本时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersionName: str
        :param _A2AEndpoint: 对外 A2A card 发现地址（Agent Card JSON 地址），仅 A2AEnabled=true 的行下发；未注册 / registry 读失败时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AEndpoint: str
        :param _A2AStatus: A2A 注册态：DRAFT / REGISTERED / DISABLED / NONE / UNKNOWN，仅 A2AEnabled=true 的行下发，与 DescribeAgent.A2AConfig.A2AStatus 同枚举；用于「开关已开但地址尚未生成」的空态文案
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AStatus: str
        :param _PublicApiEnabled: 公网链接访问开关。false 恒输出（未开启不等于字段缺失）
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicApiEnabled: bool
        :param _PublicApiUrl: 公网访问地址，仅 PublicApiEnabled=true 的行下发。固定拼法 https://{AgentId}-{region}.{endpoint_suffix}，与 DescribeAgentPublicAccess.Url 同规则；endpoint_suffix 未配置时为空
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicApiUrl: str
        :param _CreatorUin: 创建人 UIN（建号时落库的 sub_account_uin；主账号自建时为主账号 uin）。注意语义为「实际操作建号的账号」
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param _AccountId: 绑定的 OneID 企业账号 ID（数字字符串形态，如 1438693592234206274）；空=未绑定（缺省）。与 DescribeAgent.AgentInfo.AccountId 同源同语义；创建时可选传入，之后不可变
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountId: str
        """
        self._AgentId = None
        self._AgentName = None
        self._Description = None
        self._AvatarUrl = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._A2AEnabled = None
        self._SessionCount = None
        self._Model = None
        self._LatestVersionId = None
        self._LatestVersionName = None
        self._A2AEndpoint = None
        self._A2AStatus = None
        self._PublicApiEnabled = None
        self._PublicApiUrl = None
        self._CreatorUin = None
        self._AccountId = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID（全局唯一，数字字符串形态）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""Agent 名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def Description(self):
        r"""Agent 描述；未填写时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""头像 URL；未设置时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def CreatedTime(self):
        r"""创建时间，RFC3339 UTC 格式（如 2026-06-01T09:00:00Z）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间，RFC3339 UTC 格式（如 2026-09-10T15:20:00Z）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def A2AEnabled(self):
        r"""Agent 级 A2A 开关。false 恒输出（未开启不等于字段缺失）；A2AEndpoint / A2AStatus 由本接口在 A2A 开启时直接下发
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._A2AEnabled

    @A2AEnabled.setter
    def A2AEnabled(self, A2AEnabled):
        self._A2AEnabled = A2AEnabled

    @property
    def SessionCount(self):
        r"""历史会话总数（t_managed_agent_sessions 未软删计数，含全部状态）。注意与 DescribeAgent.ActiveSessionCount（活跃会话数）口径不同
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SessionCount

    @SessionCount.setter
    def SessionCount(self, SessionCount):
        self._SessionCount = SessionCount

    @property
    def Model(self):
        r"""最新版本的模型标识，取 latest_version_id 指向版本的 model；Agent 尚无版本时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def LatestVersionId(self):
        r"""最新版本 ID（latest_version_id 转字符串，19 位雪花数字形态）；Agent 尚无版本时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestVersionId

    @LatestVersionId.setter
    def LatestVersionId(self, LatestVersionId):
        self._LatestVersionId = LatestVersionId

    @property
    def LatestVersionName(self):
        r"""最新版本名（可能为 default / test-N / prod-N 任意类型）；Agent 尚无版本时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestVersionName

    @LatestVersionName.setter
    def LatestVersionName(self, LatestVersionName):
        self._LatestVersionName = LatestVersionName

    @property
    def A2AEndpoint(self):
        r"""对外 A2A card 发现地址（Agent Card JSON 地址），仅 A2AEnabled=true 的行下发；未注册 / registry 读失败时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2AEndpoint

    @A2AEndpoint.setter
    def A2AEndpoint(self, A2AEndpoint):
        self._A2AEndpoint = A2AEndpoint

    @property
    def A2AStatus(self):
        r"""A2A 注册态：DRAFT / REGISTERED / DISABLED / NONE / UNKNOWN，仅 A2AEnabled=true 的行下发，与 DescribeAgent.A2AConfig.A2AStatus 同枚举；用于「开关已开但地址尚未生成」的空态文案
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2AStatus

    @A2AStatus.setter
    def A2AStatus(self, A2AStatus):
        self._A2AStatus = A2AStatus

    @property
    def PublicApiEnabled(self):
        r"""公网链接访问开关。false 恒输出（未开启不等于字段缺失）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._PublicApiEnabled

    @PublicApiEnabled.setter
    def PublicApiEnabled(self, PublicApiEnabled):
        self._PublicApiEnabled = PublicApiEnabled

    @property
    def PublicApiUrl(self):
        r"""公网访问地址，仅 PublicApiEnabled=true 的行下发。固定拼法 https://{AgentId}-{region}.{endpoint_suffix}，与 DescribeAgentPublicAccess.Url 同规则；endpoint_suffix 未配置时为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicApiUrl

    @PublicApiUrl.setter
    def PublicApiUrl(self, PublicApiUrl):
        self._PublicApiUrl = PublicApiUrl

    @property
    def CreatorUin(self):
        r"""创建人 UIN（建号时落库的 sub_account_uin；主账号自建时为主账号 uin）。注意语义为「实际操作建号的账号」
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def AccountId(self):
        r"""绑定的 OneID 企业账号 ID（数字字符串形态，如 1438693592234206274）；空=未绑定（缺省）。与 DescribeAgent.AgentInfo.AccountId 同源同语义；创建时可选传入，之后不可变
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._A2AEnabled = params.get("A2AEnabled")
        self._SessionCount = params.get("SessionCount")
        self._Model = params.get("Model")
        self._LatestVersionId = params.get("LatestVersionId")
        self._LatestVersionName = params.get("LatestVersionName")
        self._A2AEndpoint = params.get("A2AEndpoint")
        self._A2AStatus = params.get("A2AStatus")
        self._PublicApiEnabled = params.get("PublicApiEnabled")
        self._PublicApiUrl = params.get("PublicApiUrl")
        self._CreatorUin = params.get("CreatorUin")
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentVersionItem(AbstractModel):
    r"""Agent 版本列表项（原 AgentVersionSummary / AgentVersionBrief 合并，字段取并集）

    """

    def __init__(self):
        r"""
        :param _VersionId: 版本 ID（雪花算法生成的数字字符串，唯一标识）
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _VersionName: 版本名称，形如 default / test-N / prod-N（N 为同类型版本的自增序号）
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _VersionType: 版本类型（服务端按 VersionName 派生）：DEFAULT（默认版本，可编辑）/ TEST（测试版本，可编辑）/ PROD（生产版本，内容冻结）
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionType: str
        :param _Model: 版本绑定的模型标识；未设置时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: str
        :param _SandboxTemplateId: 版本运行时使用的沙箱模板业务 ID；空字符串表示使用默认沙箱
注意：此字段可能返回 null，表示取不到有效值。
        :type SandboxTemplateId: str
        :param _Status: 版本状态：DRAFT（草稿）/ ENABLED（已启用）/ DISABLED（已停用）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _SessionCount: <p>该版本累计承接的会话总数（历史累计值，只增不减）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionCount: int
        :param _CreatedTime: 创建时间，RFC3339 UTC 格式（如 2026-08-01T10:00:00Z）
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间，RFC3339 UTC 格式（如 2026-08-10T15:30:00Z）
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        """
        self._VersionId = None
        self._VersionName = None
        self._VersionType = None
        self._Model = None
        self._SandboxTemplateId = None
        self._Status = None
        self._SessionCount = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def VersionId(self):
        r"""版本 ID（雪花算法生成的数字字符串，唯一标识）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionName(self):
        r"""版本名称，形如 default / test-N / prod-N（N 为同类型版本的自增序号）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionType(self):
        r"""版本类型（服务端按 VersionName 派生）：DEFAULT（默认版本，可编辑）/ TEST（测试版本，可编辑）/ PROD（生产版本，内容冻结）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionType

    @VersionType.setter
    def VersionType(self, VersionType):
        self._VersionType = VersionType

    @property
    def Model(self):
        r"""版本绑定的模型标识；未设置时缺省
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def SandboxTemplateId(self):
        r"""版本运行时使用的沙箱模板业务 ID；空字符串表示使用默认沙箱
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SandboxTemplateId

    @SandboxTemplateId.setter
    def SandboxTemplateId(self, SandboxTemplateId):
        self._SandboxTemplateId = SandboxTemplateId

    @property
    def Status(self):
        r"""版本状态：DRAFT（草稿）/ ENABLED（已启用）/ DISABLED（已停用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SessionCount(self):
        r"""<p>该版本累计承接的会话总数（历史累计值，只增不减）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SessionCount

    @SessionCount.setter
    def SessionCount(self, SessionCount):
        self._SessionCount = SessionCount

    @property
    def CreatedTime(self):
        r"""创建时间，RFC3339 UTC 格式（如 2026-08-01T10:00:00Z）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间，RFC3339 UTC 格式（如 2026-08-10T15:30:00Z）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._VersionName = params.get("VersionName")
        self._VersionType = params.get("VersionType")
        self._Model = params.get("Model")
        self._SandboxTemplateId = params.get("SandboxTemplateId")
        self._Status = params.get("Status")
        self._SessionCount = params.get("SessionCount")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindExternalAgentRequest(AbstractModel):
    r"""BindExternalAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: TMA managed agent 业务 ID（CloudAgentID）
        :type AgentId: str
        :param _A2AAgentId: 已注册的外部 A2A agent ID
        :type A2AAgentId: str
        :param _VersionId: 版本 ID
        :type VersionId: str
        """
        self._AgentId = None
        self._A2AAgentId = None
        self._VersionId = None

    @property
    def AgentId(self):
        r"""TMA managed agent 业务 ID（CloudAgentID）
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def A2AAgentId(self):
        r"""已注册的外部 A2A agent ID
        :rtype: str
        """
        return self._A2AAgentId

    @A2AAgentId.setter
    def A2AAgentId(self, A2AAgentId):
        self._A2AAgentId = A2AAgentId

    @property
    def VersionId(self):
        r"""版本 ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._A2AAgentId = params.get("A2AAgentId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindExternalAgentResponse(AbstractModel):
    r"""BindExternalAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果状态（大写枚举）：BOUND=已绑定 / UNBOUND=已解绑
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _BindingId: 绑定记录 ID（自增 ID 字符串）
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._BindingId = None
        self._RequestId = None

    @property
    def Status(self):
        r"""操作结果状态（大写枚举）：BOUND=已绑定 / UNBOUND=已解绑
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BindingId(self):
        r"""绑定记录 ID（自增 ID 字符串）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._BindingId = params.get("BindingId")
        self._RequestId = params.get("RequestId")


class BuiltinModel(AbstractModel):
    r"""内置模型信息

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型唯一标识
        :type ModelId: str
        :param _Name: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Vendor: 供应商，如 TENCENT、OPENAI、ANTHROPIC、DEEPSEEK 等
注意：此字段可能返回 null，表示取不到有效值。
        :type Vendor: str
        :param _MaxOutputTokens: 最大输出 Token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxOutputTokens: int
        :param _MaxInputTokens: 最大输入 Token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxInputTokens: int
        :param _SupportsToolCall: 是否支持函数调用（Tool Call）
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportsToolCall: bool
        :param _SupportsImages: 是否支持视觉（图片输入）
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportsImages: bool
        :param _DescriptionZh: 模型中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionZh: str
        :param _DescriptionEn: 模型英文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionEn: str
        :param _Tags: 模型标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _Clients: 支持的客户端列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Clients: list of str
        :param _ServiceEndpoint: 服务接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceEndpoint: str
        :param _Status: 状态：ENABLED（已启用）/ DISABLED（已停用）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _AgentCount: 本企业内绑定该模型的 Agent 数（过滤软删除 Agent/版本与调试 Agent）
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentCount: int
        """
        self._ModelId = None
        self._Name = None
        self._Vendor = None
        self._MaxOutputTokens = None
        self._MaxInputTokens = None
        self._SupportsToolCall = None
        self._SupportsImages = None
        self._DescriptionZh = None
        self._DescriptionEn = None
        self._Tags = None
        self._Clients = None
        self._ServiceEndpoint = None
        self._Status = None
        self._AgentCount = None

    @property
    def ModelId(self):
        r"""模型唯一标识
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def Name(self):
        r"""模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Vendor(self):
        r"""供应商，如 TENCENT、OPENAI、ANTHROPIC、DEEPSEEK 等
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def MaxOutputTokens(self):
        r"""最大输出 Token 数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxOutputTokens

    @MaxOutputTokens.setter
    def MaxOutputTokens(self, MaxOutputTokens):
        self._MaxOutputTokens = MaxOutputTokens

    @property
    def MaxInputTokens(self):
        r"""最大输入 Token 数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxInputTokens

    @MaxInputTokens.setter
    def MaxInputTokens(self, MaxInputTokens):
        self._MaxInputTokens = MaxInputTokens

    @property
    def SupportsToolCall(self):
        r"""是否支持函数调用（Tool Call）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._SupportsToolCall

    @SupportsToolCall.setter
    def SupportsToolCall(self, SupportsToolCall):
        self._SupportsToolCall = SupportsToolCall

    @property
    def SupportsImages(self):
        r"""是否支持视觉（图片输入）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._SupportsImages

    @SupportsImages.setter
    def SupportsImages(self, SupportsImages):
        self._SupportsImages = SupportsImages

    @property
    def DescriptionZh(self):
        r"""模型中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DescriptionZh

    @DescriptionZh.setter
    def DescriptionZh(self, DescriptionZh):
        self._DescriptionZh = DescriptionZh

    @property
    def DescriptionEn(self):
        r"""模型英文描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DescriptionEn

    @DescriptionEn.setter
    def DescriptionEn(self, DescriptionEn):
        self._DescriptionEn = DescriptionEn

    @property
    def Tags(self):
        r"""模型标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Clients(self):
        r"""支持的客户端列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Clients

    @Clients.setter
    def Clients(self, Clients):
        self._Clients = Clients

    @property
    def ServiceEndpoint(self):
        r"""服务接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceEndpoint

    @ServiceEndpoint.setter
    def ServiceEndpoint(self, ServiceEndpoint):
        self._ServiceEndpoint = ServiceEndpoint

    @property
    def Status(self):
        r"""状态：ENABLED（已启用）/ DISABLED（已停用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AgentCount(self):
        r"""本企业内绑定该模型的 Agent 数（过滤软删除 Agent/版本与调试 Agent）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AgentCount

    @AgentCount.setter
    def AgentCount(self, AgentCount):
        self._AgentCount = AgentCount


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._Name = params.get("Name")
        self._Vendor = params.get("Vendor")
        self._MaxOutputTokens = params.get("MaxOutputTokens")
        self._MaxInputTokens = params.get("MaxInputTokens")
        self._SupportsToolCall = params.get("SupportsToolCall")
        self._SupportsImages = params.get("SupportsImages")
        self._DescriptionZh = params.get("DescriptionZh")
        self._DescriptionEn = params.get("DescriptionEn")
        self._Tags = params.get("Tags")
        self._Clients = params.get("Clients")
        self._ServiceEndpoint = params.get("ServiceEndpoint")
        self._Status = params.get("Status")
        self._AgentCount = params.get("AgentCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatEndpoint(AbstractModel):
    r"""聊天接入点。EndpointType 现在就引入枚举：当前仅返回一个 PUBLIC 元素，将来新增私网端点与 VPC 属性为纯增量。

    """

    def __init__(self):
        r"""
        :param _EndpointType: 接入点类型：PUBLIC（公网）/ PRIVATE（私网，预留）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndpointType: str
        :param _Url: 接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self._EndpointType = None
        self._Url = None

    @property
    def EndpointType(self):
        r"""接入点类型：PUBLIC（公网）/ PRIVATE（私网，预留）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndpointType

    @EndpointType.setter
    def EndpointType(self, EndpointType):
        self._EndpointType = EndpointType

    @property
    def Url(self):
        r"""接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._EndpointType = params.get("EndpointType")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectorInfo(AbstractModel):
    r"""连接器详情（主表 + 最新版本展开）。

    """

    def __init__(self):
        r"""
        :param _ConnectorId: 连接器 ID
        :type ConnectorId: str
        :param _ConnectorSlug: 连接器短标识（终身不变，跨版本稳定）
        :type ConnectorSlug: str
        :param _ConnectorKey: 版本级连接器密钥
        :type ConnectorKey: str
        :param _Name: 连接器名称
        :type Name: str
        :param _Description: 连接器描述
        :type Description: str
        :param _AvatarUrl: 头像 URL
        :type AvatarUrl: str
        :param _Source: 连接器来源：ENTERPRISE_AGENT / ASSISTANT
        :type Source: str
        :param _EnterpriseId: 归属企业 ID
        :type EnterpriseId: str
        :param _Type: 连接器类型：MCP_SERVER / A2A / API_SERVICE
        :type Type: str
        :param _ServiceUrl: 上游服务地址
        :type ServiceUrl: str
        :param _AuthModes: 授权方式列表：NONE / ONEID / OAUTH2_IDP
        :type AuthModes: list of str
        :param _LatestVersionNo: 最新版本号
        :type LatestVersionNo: int
        :param _Status: 连接器状态：ACTIVE / DISABLED
        :type Status: str
        :param _CreatorId: 创建人 ID
        :type CreatorId: str
        :param _CreatedTime: 创建时间（ISO8601，UTC）
        :type CreatedTime: str
        :param _ModifiedTime: 最后修改时间（ISO8601，UTC）
        :type ModifiedTime: str
        """
        self._ConnectorId = None
        self._ConnectorSlug = None
        self._ConnectorKey = None
        self._Name = None
        self._Description = None
        self._AvatarUrl = None
        self._Source = None
        self._EnterpriseId = None
        self._Type = None
        self._ServiceUrl = None
        self._AuthModes = None
        self._LatestVersionNo = None
        self._Status = None
        self._CreatorId = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def ConnectorId(self):
        r"""连接器 ID
        :rtype: str
        """
        return self._ConnectorId

    @ConnectorId.setter
    def ConnectorId(self, ConnectorId):
        self._ConnectorId = ConnectorId

    @property
    def ConnectorSlug(self):
        r"""连接器短标识（终身不变，跨版本稳定）
        :rtype: str
        """
        return self._ConnectorSlug

    @ConnectorSlug.setter
    def ConnectorSlug(self, ConnectorSlug):
        self._ConnectorSlug = ConnectorSlug

    @property
    def ConnectorKey(self):
        r"""版本级连接器密钥
        :rtype: str
        """
        return self._ConnectorKey

    @ConnectorKey.setter
    def ConnectorKey(self, ConnectorKey):
        self._ConnectorKey = ConnectorKey

    @property
    def Name(self):
        r"""连接器名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""连接器描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""头像 URL
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def Source(self):
        r"""连接器来源：ENTERPRISE_AGENT / ASSISTANT
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def EnterpriseId(self):
        r"""归属企业 ID
        :rtype: str
        """
        return self._EnterpriseId

    @EnterpriseId.setter
    def EnterpriseId(self, EnterpriseId):
        self._EnterpriseId = EnterpriseId

    @property
    def Type(self):
        r"""连接器类型：MCP_SERVER / A2A / API_SERVICE
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ServiceUrl(self):
        r"""上游服务地址
        :rtype: str
        """
        return self._ServiceUrl

    @ServiceUrl.setter
    def ServiceUrl(self, ServiceUrl):
        self._ServiceUrl = ServiceUrl

    @property
    def AuthModes(self):
        r"""授权方式列表：NONE / ONEID / OAUTH2_IDP
        :rtype: list of str
        """
        return self._AuthModes

    @AuthModes.setter
    def AuthModes(self, AuthModes):
        self._AuthModes = AuthModes

    @property
    def LatestVersionNo(self):
        r"""最新版本号
        :rtype: int
        """
        return self._LatestVersionNo

    @LatestVersionNo.setter
    def LatestVersionNo(self, LatestVersionNo):
        self._LatestVersionNo = LatestVersionNo

    @property
    def Status(self):
        r"""连接器状态：ACTIVE / DISABLED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatorId(self):
        r"""创建人 ID
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def CreatedTime(self):
        r"""创建时间（ISO8601，UTC）
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""最后修改时间（ISO8601，UTC）
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._ConnectorId = params.get("ConnectorId")
        self._ConnectorSlug = params.get("ConnectorSlug")
        self._ConnectorKey = params.get("ConnectorKey")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        self._Source = params.get("Source")
        self._EnterpriseId = params.get("EnterpriseId")
        self._Type = params.get("Type")
        self._ServiceUrl = params.get("ServiceUrl")
        self._AuthModes = params.get("AuthModes")
        self._LatestVersionNo = params.get("LatestVersionNo")
        self._Status = params.get("Status")
        self._CreatorId = params.get("CreatorId")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectorRefInput(AbstractModel):
    r"""连接器引用入参

    """

    def __init__(self):
        r"""
        :param _ConnectorId: connector 主表 ID（雪花 ID 数字串）
        :type ConnectorId: str
        """
        self._ConnectorId = None

    @property
    def ConnectorId(self):
        r"""connector 主表 ID（雪花 ID 数字串）
        :rtype: str
        """
        return self._ConnectorId

    @ConnectorId.setter
    def ConnectorId(self, ConnectorId):
        self._ConnectorId = ConnectorId


    def _deserialize(self, params):
        self._ConnectorId = params.get("ConnectorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentRequest(AbstractModel):
    r"""CreateAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentName: Agent 名称
        :type AgentName: str
        :param _Description: Agent 描述
        :type Description: str
        :param _AvatarUrl: 头像 URL
        :type AvatarUrl: str
        :param _Model: 模型标识
        :type Model: str
        :param _Manifest: Manifest v2.0 原文（JSON 字符串），作为 default 版本初始内容。ConnectorSet 非空时 Manifest 不可为空，否则返回 InvalidParameter
        :type Manifest: str
        :param _ConnectorSet: 该 Agent 最终绑定的连接器集合（全量覆盖语义）：缺省 = 不绑定连接器；非空 = 物化为 manifest v2 mcp_servers 网关条目。ConnectorSet 非空时 Manifest 不可为空，否则返回 InvalidParameter
        :type ConnectorSet: list of ConnectorRefInput
        :param _AccountId: 绑定的 OneID 企业账号 ID。非空时必须是当前主账号已在企业授权表（t_managed_agent_enterprise_authorization）中授权的租户，否则返回 UnauthorizedOperation.AccountNotAuthorized。绑定后不可修改。TrimSpace 后长度 1~64 字符
        :type AccountId: str
        """
        self._AgentName = None
        self._Description = None
        self._AvatarUrl = None
        self._Model = None
        self._Manifest = None
        self._ConnectorSet = None
        self._AccountId = None

    @property
    def AgentName(self):
        r"""Agent 名称
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def Description(self):
        r"""Agent 描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""头像 URL
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def Model(self):
        r"""模型标识
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Manifest(self):
        r"""Manifest v2.0 原文（JSON 字符串），作为 default 版本初始内容。ConnectorSet 非空时 Manifest 不可为空，否则返回 InvalidParameter
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def ConnectorSet(self):
        r"""该 Agent 最终绑定的连接器集合（全量覆盖语义）：缺省 = 不绑定连接器；非空 = 物化为 manifest v2 mcp_servers 网关条目。ConnectorSet 非空时 Manifest 不可为空，否则返回 InvalidParameter
        :rtype: list of ConnectorRefInput
        """
        return self._ConnectorSet

    @ConnectorSet.setter
    def ConnectorSet(self, ConnectorSet):
        self._ConnectorSet = ConnectorSet

    @property
    def AccountId(self):
        r"""绑定的 OneID 企业账号 ID。非空时必须是当前主账号已在企业授权表（t_managed_agent_enterprise_authorization）中授权的租户，否则返回 UnauthorizedOperation.AccountNotAuthorized。绑定后不可修改。TrimSpace 后长度 1~64 字符
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        self._AgentName = params.get("AgentName")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        self._Model = params.get("Model")
        self._Manifest = params.get("Manifest")
        if params.get("ConnectorSet") is not None:
            self._ConnectorSet = []
            for item in params.get("ConnectorSet"):
                obj = ConnectorRefInput()
                obj._deserialize(item)
                self._ConnectorSet.append(obj)
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentResponse(AbstractModel):
    r"""CreateAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _AgentName: Agent 名称
        :type AgentName: str
        :param _Description: Agent 描述
        :type Description: str
        :param _AvatarUrl: 头像 URL
        :type AvatarUrl: str
        :param _IsDebug: 是否调试 Agent
        :type IsDebug: bool
        :param _CreatedTime: 创建时间（RFC3339）
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间（RFC3339）
        :type ModifiedTime: str
        :param _RoutingSet: 流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）
        :type RoutingSet: list of RoutingItem
        :param _A2AConfig: A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）
        :type A2AConfig: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        :param _AccountId: 绑定的 OneID 企业账号 ID。允许为空：未绑定的存量与新建 Agent 该字段缺省，绑定后回显绑定值
        :type AccountId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._AgentName = None
        self._Description = None
        self._AvatarUrl = None
        self._IsDebug = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._RoutingSet = None
        self._A2AConfig = None
        self._AccountId = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""Agent 名称
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def Description(self):
        r"""Agent 描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""头像 URL
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def IsDebug(self):
        r"""是否调试 Agent
        :rtype: bool
        """
        return self._IsDebug

    @IsDebug.setter
    def IsDebug(self, IsDebug):
        self._IsDebug = IsDebug

    @property
    def CreatedTime(self):
        r"""创建时间（RFC3339）
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间（RFC3339）
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def RoutingSet(self):
        r"""流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）
        :rtype: list of RoutingItem
        """
        return self._RoutingSet

    @RoutingSet.setter
    def RoutingSet(self, RoutingSet):
        self._RoutingSet = RoutingSet

    @property
    def A2AConfig(self):
        r"""A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        """
        return self._A2AConfig

    @A2AConfig.setter
    def A2AConfig(self, A2AConfig):
        self._A2AConfig = A2AConfig

    @property
    def AccountId(self):
        r"""绑定的 OneID 企业账号 ID。允许为空：未绑定的存量与新建 Agent 该字段缺省，绑定后回显绑定值
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        self._IsDebug = params.get("IsDebug")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        if params.get("RoutingSet") is not None:
            self._RoutingSet = []
            for item in params.get("RoutingSet"):
                obj = RoutingItem()
                obj._deserialize(item)
                self._RoutingSet.append(obj)
        if params.get("A2AConfig") is not None:
            self._A2AConfig = A2AConfig()
            self._A2AConfig._deserialize(params.get("A2AConfig"))
        self._AccountId = params.get("AccountId")
        self._RequestId = params.get("RequestId")


class CreateAgentSessionRequest(AbstractModel):
    r"""CreateAgentSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _VersionId: <p>指定版本 ID（可选）。非空且合法时固定使用该版本，跳过 routing_config 权重挑选；指定版本需归属同一 Agent 且未被废弃</p>
        :type VersionId: str
        """
        self._AgentId = None
        self._VersionId = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def VersionId(self):
        r"""<p>指定版本 ID（可选）。非空且合法时固定使用该版本，跳过 routing_config 权重挑选；指定版本需归属同一 Agent 且未被废弃</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentSessionResponse(AbstractModel):
    r"""CreateAgentSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>会话 ID</p>
        :type SessionId: str
        :param _EndpointSet: <p>可用的聊天接入点列表（当前仅含一个 PUBLIC 公网接入点；空数组 = 无可用接入点）</p>
        :type EndpointSet: list of ChatEndpoint
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._EndpointSet = None
        self._RequestId = None

    @property
    def SessionId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def EndpointSet(self):
        r"""<p>可用的聊天接入点列表（当前仅含一个 PUBLIC 公网接入点；空数组 = 无可用接入点）</p>
        :rtype: list of ChatEndpoint
        """
        return self._EndpointSet

    @EndpointSet.setter
    def EndpointSet(self, EndpointSet):
        self._EndpointSet = EndpointSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        if params.get("EndpointSet") is not None:
            self._EndpointSet = []
            for item in params.get("EndpointSet"):
                obj = ChatEndpoint()
                obj._deserialize(item)
                self._EndpointSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateAgentVersionFromSourceRequest(AbstractModel):
    r"""CreateAgentVersionFromSource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _SourceVersionId: <p>源版本 ID，同 Agent 下未 DISABLED 的任意版本</p>
        :type SourceVersionId: str
        :param _Model: <p>可选，覆盖源版本的 Model</p>
        :type Model: str
        :param _Description: <p>可选，覆盖源版本的 Description</p>
        :type Description: str
        :param _Manifest: <p>可选，完整 v2.0 manifest JSON 字符串；传入则整体覆盖源版本 manifest</p>
        :type Manifest: str
        :param _SandboxTemplateId: <p>沙箱模板 ID。可选，patch 语义：null 沿用源版本绑定的模板；空串解绑（恢复系统默认模板）；非空时模板须属于当前企业且可用（未删除、状态正常）。</p>
        :type SandboxTemplateId: str
        """
        self._AgentId = None
        self._SourceVersionId = None
        self._Model = None
        self._Description = None
        self._Manifest = None
        self._SandboxTemplateId = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def SourceVersionId(self):
        r"""<p>源版本 ID，同 Agent 下未 DISABLED 的任意版本</p>
        :rtype: str
        """
        return self._SourceVersionId

    @SourceVersionId.setter
    def SourceVersionId(self, SourceVersionId):
        self._SourceVersionId = SourceVersionId

    @property
    def Model(self):
        r"""<p>可选，覆盖源版本的 Model</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Description(self):
        r"""<p>可选，覆盖源版本的 Description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Manifest(self):
        r"""<p>可选，完整 v2.0 manifest JSON 字符串；传入则整体覆盖源版本 manifest</p>
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def SandboxTemplateId(self):
        r"""<p>沙箱模板 ID。可选，patch 语义：null 沿用源版本绑定的模板；空串解绑（恢复系统默认模板）；非空时模板须属于当前企业且可用（未删除、状态正常）。</p>
        :rtype: str
        """
        return self._SandboxTemplateId

    @SandboxTemplateId.setter
    def SandboxTemplateId(self, SandboxTemplateId):
        self._SandboxTemplateId = SandboxTemplateId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._SourceVersionId = params.get("SourceVersionId")
        self._Model = params.get("Model")
        self._Description = params.get("Description")
        self._Manifest = params.get("Manifest")
        self._SandboxTemplateId = params.get("SandboxTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentVersionFromSourceResponse(AbstractModel):
    r"""CreateAgentVersionFromSource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionId: <p>版本 ID</p>
        :type VersionId: str
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _VersionName: <p>版本名称</p>
        :type VersionName: str
        :param _VersionType: <p>版本类型：DEFAULT / TEST / PROD</p>
        :type VersionType: str
        :param _Description: <p>版本变更说明</p>
        :type Description: str
        :param _Model: <p>模型标识</p>
        :type Model: str
        :param _Manifest: <p>Manifest v2.0 精简 manifest 原文（JSON 字符串）</p>
        :type Manifest: str
        :param _Status: <p>版本状态：DRAFT / ENABLED / DISABLED</p>
        :type Status: str
        :param _CreatedTime: <p>创建时间</p>
        :type CreatedTime: str
        :param _ModifiedTime: <p>更新时间</p>
        :type ModifiedTime: str
        :param _SandboxTemplateId: <p>绑定的沙箱模板 ID；未绑定时为空，创建会话沙箱使用系统默认模板。</p>
        :type SandboxTemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionId = None
        self._AgentId = None
        self._VersionName = None
        self._VersionType = None
        self._Description = None
        self._Model = None
        self._Manifest = None
        self._Status = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._SandboxTemplateId = None
        self._RequestId = None

    @property
    def VersionId(self):
        r"""<p>版本 ID</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def VersionName(self):
        r"""<p>版本名称</p>
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionType(self):
        r"""<p>版本类型：DEFAULT / TEST / PROD</p>
        :rtype: str
        """
        return self._VersionType

    @VersionType.setter
    def VersionType(self, VersionType):
        self._VersionType = VersionType

    @property
    def Description(self):
        r"""<p>版本变更说明</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Model(self):
        r"""<p>模型标识</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Manifest(self):
        r"""<p>Manifest v2.0 精简 manifest 原文（JSON 字符串）</p>
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Status(self):
        r"""<p>版本状态：DRAFT / ENABLED / DISABLED</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SandboxTemplateId(self):
        r"""<p>绑定的沙箱模板 ID；未绑定时为空，创建会话沙箱使用系统默认模板。</p>
        :rtype: str
        """
        return self._SandboxTemplateId

    @SandboxTemplateId.setter
    def SandboxTemplateId(self, SandboxTemplateId):
        self._SandboxTemplateId = SandboxTemplateId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._AgentId = params.get("AgentId")
        self._VersionName = params.get("VersionName")
        self._VersionType = params.get("VersionType")
        self._Description = params.get("Description")
        self._Model = params.get("Model")
        self._Manifest = params.get("Manifest")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SandboxTemplateId = params.get("SandboxTemplateId")
        self._RequestId = params.get("RequestId")


class CreateAgentVersionRequest(AbstractModel):
    r"""CreateAgentVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _Manifest: <p>Manifest v2.0 精简 manifest 原文（JSON 对象序列化后的字符串）</p>
        :type Manifest: str
        :param _Model: <p>模型标识</p>
        :type Model: str
        :param _Description: <p>版本变更说明</p>
        :type Description: str
        :param _SandboxTemplateId: <p>沙箱模板 ID。可选；传入时模板须属于当前企业且可用（未删除、状态正常），绑定到新建的 test/prod 版本。</p>
        :type SandboxTemplateId: str
        """
        self._AgentId = None
        self._Manifest = None
        self._Model = None
        self._Description = None
        self._SandboxTemplateId = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Manifest(self):
        r"""<p>Manifest v2.0 精简 manifest 原文（JSON 对象序列化后的字符串）</p>
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Model(self):
        r"""<p>模型标识</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Description(self):
        r"""<p>版本变更说明</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SandboxTemplateId(self):
        r"""<p>沙箱模板 ID。可选；传入时模板须属于当前企业且可用（未删除、状态正常），绑定到新建的 test/prod 版本。</p>
        :rtype: str
        """
        return self._SandboxTemplateId

    @SandboxTemplateId.setter
    def SandboxTemplateId(self, SandboxTemplateId):
        self._SandboxTemplateId = SandboxTemplateId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._Manifest = params.get("Manifest")
        self._Model = params.get("Model")
        self._Description = params.get("Description")
        self._SandboxTemplateId = params.get("SandboxTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentVersionResponse(AbstractModel):
    r"""CreateAgentVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionId: <p>版本 ID</p>
        :type VersionId: str
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _VersionName: <p>版本名称</p>
        :type VersionName: str
        :param _VersionType: <p>版本类型：DEFAULT / TEST / PROD</p>
        :type VersionType: str
        :param _Description: <p>版本变更说明</p>
        :type Description: str
        :param _Model: <p>模型标识</p>
        :type Model: str
        :param _Manifest: <p>Manifest v2.0 精简 manifest 原文（JSON 字符串）</p>
        :type Manifest: str
        :param _Status: <p>版本状态：DRAFT / ENABLED / DISABLED</p>
        :type Status: str
        :param _CreatedTime: <p>创建时间</p>
        :type CreatedTime: str
        :param _ModifiedTime: <p>更新时间</p>
        :type ModifiedTime: str
        :param _SandboxTemplateId: <p>绑定的沙箱模板 ID；未绑定时为空，创建会话沙箱使用系统默认模板。</p>
        :type SandboxTemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionId = None
        self._AgentId = None
        self._VersionName = None
        self._VersionType = None
        self._Description = None
        self._Model = None
        self._Manifest = None
        self._Status = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._SandboxTemplateId = None
        self._RequestId = None

    @property
    def VersionId(self):
        r"""<p>版本 ID</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def VersionName(self):
        r"""<p>版本名称</p>
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionType(self):
        r"""<p>版本类型：DEFAULT / TEST / PROD</p>
        :rtype: str
        """
        return self._VersionType

    @VersionType.setter
    def VersionType(self, VersionType):
        self._VersionType = VersionType

    @property
    def Description(self):
        r"""<p>版本变更说明</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Model(self):
        r"""<p>模型标识</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Manifest(self):
        r"""<p>Manifest v2.0 精简 manifest 原文（JSON 字符串）</p>
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Status(self):
        r"""<p>版本状态：DRAFT / ENABLED / DISABLED</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SandboxTemplateId(self):
        r"""<p>绑定的沙箱模板 ID；未绑定时为空，创建会话沙箱使用系统默认模板。</p>
        :rtype: str
        """
        return self._SandboxTemplateId

    @SandboxTemplateId.setter
    def SandboxTemplateId(self, SandboxTemplateId):
        self._SandboxTemplateId = SandboxTemplateId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._AgentId = params.get("AgentId")
        self._VersionName = params.get("VersionName")
        self._VersionType = params.get("VersionType")
        self._Description = params.get("Description")
        self._Model = params.get("Model")
        self._Manifest = params.get("Manifest")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SandboxTemplateId = params.get("SandboxTemplateId")
        self._RequestId = params.get("RequestId")


class DeleteAgentRequest(AbstractModel):
    r"""DeleteAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        """
        self._AgentId = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentResponse(AbstractModel):
    r"""DeleteAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAgentListRequest(AbstractModel):
    r"""DescribeAgentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，从 0 开始
        :type Offset: int
        :param _Limit: 返回数量，缺省为 20，最大 100
        :type Limit: int
        :param _Filters: 过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系
        :type Filters: list of Filter
        :param _SortBy: 排序字段
        :type SortBy: str
        :param _SortDirection: 排序方向：ASC / DESC
        :type SortDirection: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._SortBy = None
        self._SortDirection = None

    @property
    def Offset(self):
        r"""偏移量，从 0 开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，缺省为 20，最大 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        r"""排序字段
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def SortDirection(self):
        r"""排序方向：ASC / DESC
        :rtype: str
        """
        return self._SortDirection

    @SortDirection.setter
    def SortDirection(self, SortDirection):
        self._SortDirection = SortDirection


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortBy = params.get("SortBy")
        self._SortDirection = params.get("SortDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentListResponse(AbstractModel):
    r"""DescribeAgentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的 Agent 总数
        :type TotalCount: int
        :param _AgentSet: Agent 列表（分页后）；元素含 A2A / 公网 API 访问开关与地址、创建人 UIN、绑定的企业账号 ID
        :type AgentSet: list of AgentItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AgentSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的 Agent 总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AgentSet(self):
        r"""Agent 列表（分页后）；元素含 A2A / 公网 API 访问开关与地址、创建人 UIN、绑定的企业账号 ID
        :rtype: list of AgentItem
        """
        return self._AgentSet

    @AgentSet.setter
    def AgentSet(self, AgentSet):
        self._AgentSet = AgentSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AgentSet") is not None:
            self._AgentSet = []
            for item in params.get("AgentSet"):
                obj = AgentItem()
                obj._deserialize(item)
                self._AgentSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentRequest(AbstractModel):
    r"""DescribeAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        """
        self._AgentId = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentResponse(AbstractModel):
    r"""DescribeAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _AgentName: Agent 名称
        :type AgentName: str
        :param _Description: Agent 描述
        :type Description: str
        :param _AvatarUrl: 头像 URL
        :type AvatarUrl: str
        :param _IsDebug: 是否调试 Agent
        :type IsDebug: bool
        :param _CreatedTime: 创建时间（RFC3339）
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间（RFC3339）
        :type ModifiedTime: str
        :param _ActiveSessionCount: 当前活跃 session 数（ACTIVE/CREATING/MIGRATING，未软删）；仅 DescribeAgent 读路径填充，写路径回显不下发
        :type ActiveSessionCount: int
        :param _RoutingSet: 流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）
        :type RoutingSet: list of RoutingItem
        :param _A2AConfig: A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）
        :type A2AConfig: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        :param _AccountId: 绑定的 OneID 企业账号 ID。允许为空：未绑定的存量与新建 Agent 该字段缺省，绑定后回显绑定值
        :type AccountId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._AgentName = None
        self._Description = None
        self._AvatarUrl = None
        self._IsDebug = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ActiveSessionCount = None
        self._RoutingSet = None
        self._A2AConfig = None
        self._AccountId = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""Agent 名称
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def Description(self):
        r"""Agent 描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""头像 URL
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def IsDebug(self):
        r"""是否调试 Agent
        :rtype: bool
        """
        return self._IsDebug

    @IsDebug.setter
    def IsDebug(self, IsDebug):
        self._IsDebug = IsDebug

    @property
    def CreatedTime(self):
        r"""创建时间（RFC3339）
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间（RFC3339）
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ActiveSessionCount(self):
        r"""当前活跃 session 数（ACTIVE/CREATING/MIGRATING，未软删）；仅 DescribeAgent 读路径填充，写路径回显不下发
        :rtype: int
        """
        return self._ActiveSessionCount

    @ActiveSessionCount.setter
    def ActiveSessionCount(self, ActiveSessionCount):
        self._ActiveSessionCount = ActiveSessionCount

    @property
    def RoutingSet(self):
        r"""流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）
        :rtype: list of RoutingItem
        """
        return self._RoutingSet

    @RoutingSet.setter
    def RoutingSet(self, RoutingSet):
        self._RoutingSet = RoutingSet

    @property
    def A2AConfig(self):
        r"""A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        """
        return self._A2AConfig

    @A2AConfig.setter
    def A2AConfig(self, A2AConfig):
        self._A2AConfig = A2AConfig

    @property
    def AccountId(self):
        r"""绑定的 OneID 企业账号 ID。允许为空：未绑定的存量与新建 Agent 该字段缺省，绑定后回显绑定值
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        self._IsDebug = params.get("IsDebug")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ActiveSessionCount = params.get("ActiveSessionCount")
        if params.get("RoutingSet") is not None:
            self._RoutingSet = []
            for item in params.get("RoutingSet"):
                obj = RoutingItem()
                obj._deserialize(item)
                self._RoutingSet.append(obj)
        if params.get("A2AConfig") is not None:
            self._A2AConfig = A2AConfig()
            self._A2AConfig._deserialize(params.get("A2AConfig"))
        self._AccountId = params.get("AccountId")
        self._RequestId = params.get("RequestId")


class DescribeAgentSessionListRequest(AbstractModel):
    r"""DescribeAgentSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，从 0 开始
        :type Offset: int
        :param _Limit: 返回数量，缺省为 20，最大 100
        :type Limit: int
        :param _SortBy: 排序字段
        :type SortBy: str
        :param _SortDirection: 排序方向：ASC / DESC
        :type SortDirection: str
        :param _Filters: 过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._SortBy = None
        self._SortDirection = None
        self._Filters = None

    @property
    def Offset(self):
        r"""偏移量，从 0 开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，缺省为 20，最大 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        r"""排序字段
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def SortDirection(self):
        r"""排序方向：ASC / DESC
        :rtype: str
        """
        return self._SortDirection

    @SortDirection.setter
    def SortDirection(self, SortDirection):
        self._SortDirection = SortDirection

    @property
    def Filters(self):
        r"""过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._SortDirection = params.get("SortDirection")
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
        


class DescribeAgentSessionListResponse(AbstractModel):
    r"""DescribeAgentSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _SessionSet: 会话列表
        :type SessionSet: list of SessionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SessionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SessionSet(self):
        r"""会话列表
        :rtype: list of SessionItem
        """
        return self._SessionSet

    @SessionSet.setter
    def SessionSet(self, SessionSet):
        self._SessionSet = SessionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SessionSet") is not None:
            self._SessionSet = []
            for item in params.get("SessionSet"):
                obj = SessionItem()
                obj._deserialize(item)
                self._SessionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentSessionRequest(AbstractModel):
    r"""DescribeAgentSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话 ID
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        r"""会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentSessionResponse(AbstractModel):
    r"""DescribeAgentSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话 ID
        :type SessionId: str
        :param _SessionName: 会话名称（AgentOS 侧生成的 AI 标题 / 用户改名）；缺失时为空，调用方可兜底展示 SessionId 后缀
        :type SessionName: str
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _AgentName: Agent 名称
        :type AgentName: str
        :param _VersionId: 版本 ID
        :type VersionId: str
        :param _VersionName: 会话使用的版本名称（与 VersionId 区分：此为版本名，非 ID）
        :type VersionName: str
        :param _Status: 版本状态：DRAFT / ENABLED / DISABLED
        :type Status: str
        :param _Creator: 创建者 Uin
        :type Creator: str
        :param _Source: 连接器来源：ENTERPRISE_AGENT / ASSISTANT
        :type Source: str
        :param _EndpointSet: 可用的聊天接入点列表（详情独有）
        :type EndpointSet: list of ChatEndpoint
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间（RFC3339）
        :type ModifiedTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._SessionName = None
        self._AgentId = None
        self._AgentName = None
        self._VersionId = None
        self._VersionName = None
        self._Status = None
        self._Creator = None
        self._Source = None
        self._EndpointSet = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._RequestId = None

    @property
    def SessionId(self):
        r"""会话 ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SessionName(self):
        r"""会话名称（AgentOS 侧生成的 AI 标题 / 用户改名）；缺失时为空，调用方可兜底展示 SessionId 后缀
        :rtype: str
        """
        return self._SessionName

    @SessionName.setter
    def SessionName(self, SessionName):
        self._SessionName = SessionName

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""Agent 名称
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def VersionId(self):
        r"""版本 ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionName(self):
        r"""会话使用的版本名称（与 VersionId 区分：此为版本名，非 ID）
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Status(self):
        r"""版本状态：DRAFT / ENABLED / DISABLED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Creator(self):
        r"""创建者 Uin
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def Source(self):
        r"""连接器来源：ENTERPRISE_AGENT / ASSISTANT
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def EndpointSet(self):
        r"""可用的聊天接入点列表（详情独有）
        :rtype: list of ChatEndpoint
        """
        return self._EndpointSet

    @EndpointSet.setter
    def EndpointSet(self, EndpointSet):
        self._EndpointSet = EndpointSet

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间（RFC3339）
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._SessionName = params.get("SessionName")
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._VersionId = params.get("VersionId")
        self._VersionName = params.get("VersionName")
        self._Status = params.get("Status")
        self._Creator = params.get("Creator")
        self._Source = params.get("Source")
        if params.get("EndpointSet") is not None:
            self._EndpointSet = []
            for item in params.get("EndpointSet"):
                obj = ChatEndpoint()
                obj._deserialize(item)
                self._EndpointSet.append(obj)
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._RequestId = params.get("RequestId")


class DescribeAgentVersionListRequest(AbstractModel):
    r"""DescribeAgentVersionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _Offset: <p>偏移量，从 0 开始</p>
        :type Offset: int
        :param _Limit: <p>返回数量，缺省为 20，最大 100</p>
        :type Limit: int
        :param _Filters: <p>过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系</p>
        :type Filters: list of Filter
        """
        self._AgentId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Offset(self):
        r"""<p>偏移量，从 0 开始</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量，缺省为 20，最大 100</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
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
        


class DescribeAgentVersionListResponse(AbstractModel):
    r"""DescribeAgentVersionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数</p>
        :type TotalCount: int
        :param _AgentVersionSet: <p>版本列表（原 VersionSet；集合名带实体前缀以区分 Skill 版本接口的同名字段）</p>
        :type AgentVersionSet: list of AgentVersionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AgentVersionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AgentVersionSet(self):
        r"""<p>版本列表（原 VersionSet；集合名带实体前缀以区分 Skill 版本接口的同名字段）</p>
        :rtype: list of AgentVersionItem
        """
        return self._AgentVersionSet

    @AgentVersionSet.setter
    def AgentVersionSet(self, AgentVersionSet):
        self._AgentVersionSet = AgentVersionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AgentVersionSet") is not None:
            self._AgentVersionSet = []
            for item in params.get("AgentVersionSet"):
                obj = AgentVersionItem()
                obj._deserialize(item)
                self._AgentVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentVersionRequest(AbstractModel):
    r"""DescribeAgentVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _VersionId: <p>版本 ID</p>
        :type VersionId: str
        """
        self._AgentId = None
        self._VersionId = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def VersionId(self):
        r"""<p>版本 ID</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentVersionResponse(AbstractModel):
    r"""DescribeAgentVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionId: <p>版本 ID</p>
        :type VersionId: str
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _VersionName: <p>版本名称</p>
        :type VersionName: str
        :param _VersionType: <p>版本类型：DEFAULT / TEST / PROD</p>
        :type VersionType: str
        :param _Description: <p>版本变更说明</p>
        :type Description: str
        :param _Model: <p>模型标识</p>
        :type Model: str
        :param _Manifest: <p>Manifest v2.0 精简 manifest 原文（JSON 字符串）</p>
        :type Manifest: str
        :param _Status: <p>版本状态：DRAFT / ENABLED / DISABLED</p>
        :type Status: str
        :param _CreatedTime: <p>创建时间</p>
        :type CreatedTime: str
        :param _ModifiedTime: <p>更新时间</p>
        :type ModifiedTime: str
        :param _SandboxTemplateId: <p>绑定的沙箱模板 ID；未绑定时为空，创建会话沙箱使用系统默认模板。</p>
        :type SandboxTemplateId: str
        :param _SessionCount: <p>该版本累计承接的会话总数（历史累计值，只增不减）</p>
        :type SessionCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionId = None
        self._AgentId = None
        self._VersionName = None
        self._VersionType = None
        self._Description = None
        self._Model = None
        self._Manifest = None
        self._Status = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._SandboxTemplateId = None
        self._SessionCount = None
        self._RequestId = None

    @property
    def VersionId(self):
        r"""<p>版本 ID</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def VersionName(self):
        r"""<p>版本名称</p>
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionType(self):
        r"""<p>版本类型：DEFAULT / TEST / PROD</p>
        :rtype: str
        """
        return self._VersionType

    @VersionType.setter
    def VersionType(self, VersionType):
        self._VersionType = VersionType

    @property
    def Description(self):
        r"""<p>版本变更说明</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Model(self):
        r"""<p>模型标识</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Manifest(self):
        r"""<p>Manifest v2.0 精简 manifest 原文（JSON 字符串）</p>
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Status(self):
        r"""<p>版本状态：DRAFT / ENABLED / DISABLED</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SandboxTemplateId(self):
        r"""<p>绑定的沙箱模板 ID；未绑定时为空，创建会话沙箱使用系统默认模板。</p>
        :rtype: str
        """
        return self._SandboxTemplateId

    @SandboxTemplateId.setter
    def SandboxTemplateId(self, SandboxTemplateId):
        self._SandboxTemplateId = SandboxTemplateId

    @property
    def SessionCount(self):
        r"""<p>该版本累计承接的会话总数（历史累计值，只增不减）</p>
        :rtype: int
        """
        return self._SessionCount

    @SessionCount.setter
    def SessionCount(self, SessionCount):
        self._SessionCount = SessionCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._AgentId = params.get("AgentId")
        self._VersionName = params.get("VersionName")
        self._VersionType = params.get("VersionType")
        self._Description = params.get("Description")
        self._Model = params.get("Model")
        self._Manifest = params.get("Manifest")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SandboxTemplateId = params.get("SandboxTemplateId")
        self._SessionCount = params.get("SessionCount")
        self._RequestId = params.get("RequestId")


class DescribeBuiltinModelListRequest(AbstractModel):
    r"""DescribeBuiltinModelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，从 0 开始
        :type Offset: int
        :param _Limit: 返回数量，缺省为 20，最大 100
        :type Limit: int
        :param _Filters: 过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系
        :type Filters: list of Filter
        :param _AccountId: OneID 企业账号 ID，可选。传入时拉取该账号对应企业的模型（要求当前主账号 UIN 已授权该账号），不传时使用服务配置的企业 ID
        :type AccountId: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._AccountId = None

    @property
    def Offset(self):
        r"""偏移量，从 0 开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，缺省为 20，最大 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AccountId(self):
        r"""OneID 企业账号 ID，可选。传入时拉取该账号对应企业的模型（要求当前主账号 UIN 已授权该账号），不传时使用服务配置的企业 ID
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBuiltinModelListResponse(AbstractModel):
    r"""DescribeBuiltinModelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _BuiltinModelSet: 内置模型列表（分页后）
        :type BuiltinModelSet: list of BuiltinModel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BuiltinModelSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BuiltinModelSet(self):
        r"""内置模型列表（分页后）
        :rtype: list of BuiltinModel
        """
        return self._BuiltinModelSet

    @BuiltinModelSet.setter
    def BuiltinModelSet(self, BuiltinModelSet):
        self._BuiltinModelSet = BuiltinModelSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BuiltinModelSet") is not None:
            self._BuiltinModelSet = []
            for item in params.get("BuiltinModelSet"):
                obj = BuiltinModel()
                obj._deserialize(item)
                self._BuiltinModelSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConnectorListRequest(AbstractModel):
    r"""DescribeConnectorList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件数组，多个 Filter 之间为 AND 关系。支持 Name：Name（名称模糊匹配）/ Status（ACTIVE / DISABLED）/ Source（ENTERPRISE_AGENT / ASSISTANT）
        :type Filters: list of Filter
        :param _PageNumber: 已废弃：服务端不再读取，请使用 Offset/Limit。字段保留仅为过渡兼容，后续下线
        :type PageNumber: int
        :param _PageSize: 已废弃：服务端不再读取，请使用 Offset/Limit。字段保留仅为过渡兼容，后续下线
        :type PageSize: int
        :param _Offset: 偏移量，0 基准，缺省 0（标准 CAPI 分页参数）
        :type Offset: int
        :param _Limit: 每页数量，取值 1-100，缺省 20（标准 CAPI 分页参数）
        :type Limit: int
        """
        self._Filters = None
        self._PageNumber = None
        self._PageSize = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        r"""过滤条件数组，多个 Filter 之间为 AND 关系。支持 Name：Name（名称模糊匹配）/ Status（ACTIVE / DISABLED）/ Source（ENTERPRISE_AGENT / ASSISTANT）
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def PageNumber(self):
        r"""已废弃：服务端不再读取，请使用 Offset/Limit。字段保留仅为过渡兼容，后续下线
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""已废弃：服务端不再读取，请使用 Offset/Limit。字段保留仅为过渡兼容，后续下线
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Offset(self):
        r"""偏移量，0 基准，缺省 0（标准 CAPI 分页参数）
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，取值 1-100，缺省 20（标准 CAPI 分页参数）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConnectorListResponse(AbstractModel):
    r"""DescribeConnectorList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的连接器总数
        :type TotalCount: int
        :param _ConnectorSet: 连接器列表（分页后）；连接器挂调用方主账号 UIN 下，不挂 OneID 企业
        :type ConnectorSet: list of ConnectorInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConnectorSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的连接器总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConnectorSet(self):
        r"""连接器列表（分页后）；连接器挂调用方主账号 UIN 下，不挂 OneID 企业
        :rtype: list of ConnectorInfo
        """
        return self._ConnectorSet

    @ConnectorSet.setter
    def ConnectorSet(self, ConnectorSet):
        self._ConnectorSet = ConnectorSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConnectorSet") is not None:
            self._ConnectorSet = []
            for item in params.get("ConnectorSet"):
                obj = ConnectorInfo()
                obj._deserialize(item)
                self._ConnectorSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExpertListRequest(AbstractModel):
    r"""DescribeExpertList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: <p>专家来源，必填：BUILTIN（内置）/ CUSTOM（自建）</p>
        :type Source: str
        :param _Filters: <p>标准过滤条件：ExpertId（精确，多值 OR，携带即按 ID 批量查询，忽略分页）/ Keyword（模糊）</p>
        :type Filters: list of Filter
        :param _Offset: <p>偏移量，从 0 开始，默认 0（按 ID 批量查询时忽略）</p>
        :type Offset: int
        :param _Limit: <p>每页数量，默认 20，最大 200（按 ID 批量查询时忽略）</p>
        :type Limit: int
        """
        self._Source = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Source(self):
        r"""<p>专家来源，必填：BUILTIN（内置）/ CUSTOM（自建）</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Filters(self):
        r"""<p>标准过滤条件：ExpertId（精确，多值 OR，携带即按 ID 批量查询，忽略分页）/ Keyword（模糊）</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""<p>偏移量，从 0 开始，默认 0（按 ID 批量查询时忽略）</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>每页数量，默认 20，最大 200（按 ID 批量查询时忽略）</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Source = params.get("Source")
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
        


class DescribeExpertListResponse(AbstractModel):
    r"""DescribeExpertList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>符合条件的专家总数（按 ID 批量时为实际命中数）</p>
        :type TotalCount: int
        :param _ExpertSet: <p>专家列表</p>
        :type ExpertSet: list of ExpertItem
        :param _Counts: <p>全局计数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Counts: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ExpertCounts`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ExpertSet = None
        self._Counts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>符合条件的专家总数（按 ID 批量时为实际命中数）</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ExpertSet(self):
        r"""<p>专家列表</p>
        :rtype: list of ExpertItem
        """
        return self._ExpertSet

    @ExpertSet.setter
    def ExpertSet(self, ExpertSet):
        self._ExpertSet = ExpertSet

    @property
    def Counts(self):
        r"""<p>全局计数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.ExpertCounts`
        """
        return self._Counts

    @Counts.setter
    def Counts(self, Counts):
        self._Counts = Counts

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ExpertSet") is not None:
            self._ExpertSet = []
            for item in params.get("ExpertSet"):
                obj = ExpertItem()
                obj._deserialize(item)
                self._ExpertSet.append(obj)
        if params.get("Counts") is not None:
            self._Counts = ExpertCounts()
            self._Counts._deserialize(params.get("Counts"))
        self._RequestId = params.get("RequestId")


class DescribeExternalAgentListRequest(AbstractModel):
    r"""DescribeExternalAgentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID（必填：绑定状态的归属主体）
        :type AgentId: str
        :param _Filters: 标准过滤条件，支持的 Name：Bound（BOUND=仅已绑定 / UNBOUND=仅未绑定 / ALL=全部，缺省 ALL）
        :type Filters: list of Filter
        :param _Offset: 偏移量，从 0 开始，默认 0
        :type Offset: int
        :param _Limit: 每页数量，默认 20，最大 200
        :type Limit: int
        :param _DescribeExternalAgentList: 外部 Agent 列表查询关键字
        :type DescribeExternalAgentList: str
        :param _VersionId: 版本 ID
        :type VersionId: str
        """
        self._AgentId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._DescribeExternalAgentList = None
        self._VersionId = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID（必填：绑定状态的归属主体）
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Filters(self):
        r"""标准过滤条件，支持的 Name：Bound（BOUND=仅已绑定 / UNBOUND=仅未绑定 / ALL=全部，缺省 ALL）
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，从 0 开始，默认 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，默认 20，最大 200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DescribeExternalAgentList(self):
        r"""外部 Agent 列表查询关键字
        :rtype: str
        """
        return self._DescribeExternalAgentList

    @DescribeExternalAgentList.setter
    def DescribeExternalAgentList(self, DescribeExternalAgentList):
        self._DescribeExternalAgentList = DescribeExternalAgentList

    @property
    def VersionId(self):
        r"""版本 ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DescribeExternalAgentList = params.get("DescribeExternalAgentList")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExternalAgentListResponse(AbstractModel):
    r"""DescribeExternalAgentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的外部 Agent 总数
        :type TotalCount: int
        :param _ExternalAgentSet: 外部 Agent 集合（可见卡片全集 ∪ URL 直连型存量 binding 的合并视图）
        :type ExternalAgentSet: list of ExternalAgentInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ExternalAgentSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的外部 Agent 总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ExternalAgentSet(self):
        r"""外部 Agent 集合（可见卡片全集 ∪ URL 直连型存量 binding 的合并视图）
        :rtype: list of ExternalAgentInfo
        """
        return self._ExternalAgentSet

    @ExternalAgentSet.setter
    def ExternalAgentSet(self, ExternalAgentSet):
        self._ExternalAgentSet = ExternalAgentSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ExternalAgentSet") is not None:
            self._ExternalAgentSet = []
            for item in params.get("ExternalAgentSet"):
                obj = ExternalAgentInfo()
                obj._deserialize(item)
                self._ExternalAgentSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExternalAgentRequest(AbstractModel):
    r"""DescribeExternalAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>TMA managed agent 业务 ID（CloudAgentID）</p>
        :type AgentId: str
        :param _A2AAgentId: <p>已绑定的外部 A2A agent ID</p>
        :type A2AAgentId: str
        """
        self._AgentId = None
        self._A2AAgentId = None

    @property
    def AgentId(self):
        r"""<p>TMA managed agent 业务 ID（CloudAgentID）</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def A2AAgentId(self):
        r"""<p>已绑定的外部 A2A agent ID</p>
        :rtype: str
        """
        return self._A2AAgentId

    @A2AAgentId.setter
    def A2AAgentId(self, A2AAgentId):
        self._A2AAgentId = A2AAgentId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._A2AAgentId = params.get("A2AAgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExternalAgentResponse(AbstractModel):
    r"""DescribeExternalAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _A2AAgentId: <p>外部 A2A agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AAgentId: str
        :param _Name: <p>外部 Agent 名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Endpoint: <p>外部 A2A Server URL</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Endpoint: str
        :param _BindingId: <p>绑定记录 ID（已绑定时返回）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingId: str
        :param _Bound: <p>是否已绑定到当前 Agent</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Bound: bool
        :param _IconUrl: <p>头像地址（取自 provider card 的 iconUrl；为空时前端回落首字母头像）</p>
        :type IconUrl: str
        :param _A2AVersion: <p>外部 agent card 声明的版本号</p>
        :type A2AVersion: str
        :param _A2ASkillSet: <p>A2A card skills 集合</p>
        :type A2ASkillSet: list of A2ASkillItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._A2AAgentId = None
        self._Name = None
        self._Description = None
        self._Endpoint = None
        self._BindingId = None
        self._Bound = None
        self._IconUrl = None
        self._A2AVersion = None
        self._A2ASkillSet = None
        self._RequestId = None

    @property
    def A2AAgentId(self):
        r"""<p>外部 A2A agent ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2AAgentId

    @A2AAgentId.setter
    def A2AAgentId(self, A2AAgentId):
        self._A2AAgentId = A2AAgentId

    @property
    def Name(self):
        r"""<p>外部 Agent 名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Endpoint(self):
        r"""<p>外部 A2A Server URL</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def BindingId(self):
        r"""<p>绑定记录 ID（已绑定时返回）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

    @property
    def Bound(self):
        r"""<p>是否已绑定到当前 Agent</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Bound

    @Bound.setter
    def Bound(self, Bound):
        self._Bound = Bound

    @property
    def IconUrl(self):
        r"""<p>头像地址（取自 provider card 的 iconUrl；为空时前端回落首字母头像）</p>
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def A2AVersion(self):
        r"""<p>外部 agent card 声明的版本号</p>
        :rtype: str
        """
        return self._A2AVersion

    @A2AVersion.setter
    def A2AVersion(self, A2AVersion):
        self._A2AVersion = A2AVersion

    @property
    def A2ASkillSet(self):
        r"""<p>A2A card skills 集合</p>
        :rtype: list of A2ASkillItem
        """
        return self._A2ASkillSet

    @A2ASkillSet.setter
    def A2ASkillSet(self, A2ASkillSet):
        self._A2ASkillSet = A2ASkillSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._A2AAgentId = params.get("A2AAgentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Endpoint = params.get("Endpoint")
        self._BindingId = params.get("BindingId")
        self._Bound = params.get("Bound")
        self._IconUrl = params.get("IconUrl")
        self._A2AVersion = params.get("A2AVersion")
        if params.get("A2ASkillSet") is not None:
            self._A2ASkillSet = []
            for item in params.get("A2ASkillSet"):
                obj = A2ASkillItem()
                obj._deserialize(item)
                self._A2ASkillSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMessageEventListRequest(AbstractModel):
    r"""DescribeMessageEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>Session ID</p>
        :type SessionId: str
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        :param _Offset: <p>偏移量</p>
        :type Offset: int
        :param _Limit: <p>返回数量，默认 100，最大 100</p>
        :type Limit: int
        :param _Filters: <p>过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系</p>
        :type Filters: list of Filter
        """
        self._SessionId = None
        self._AgentId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def SessionId(self):
        r"""<p>Session ID</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Offset(self):
        r"""<p>偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量，默认 100，最大 100</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤条件数组，多个 Filter 之间为 AND 关系，同一 Filter 内多个 Values 为 OR 关系</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._AgentId = params.get("AgentId")
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
        


class DescribeMessageEventListResponse(AbstractModel):
    r"""DescribeMessageEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageEventSet: <p>消息事件列表</p>
        :type MessageEventSet: list of MessageEvent
        :param _TotalCount: <p>符合过滤条件的事件总数</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageEventSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def MessageEventSet(self):
        r"""<p>消息事件列表</p>
        :rtype: list of MessageEvent
        """
        return self._MessageEventSet

    @MessageEventSet.setter
    def MessageEventSet(self, MessageEventSet):
        self._MessageEventSet = MessageEventSet

    @property
    def TotalCount(self):
        r"""<p>符合过滤条件的事件总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MessageEventSet") is not None:
            self._MessageEventSet = []
            for item in params.get("MessageEventSet"):
                obj = MessageEvent()
                obj._deserialize(item)
                self._MessageEventSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSkillListRequest(AbstractModel):
    r"""DescribeSkillList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 技能来源，必填：BUILTIN（内置）/ CUSTOM（自建）/ AUTHORIZED（企业授权）。数据通路判别，非筛选条件
        :type Source: str
        :param _Filters: 标准过滤条件：SkillId（精确，多值 OR ≤100，携带即按 ID 批量查询）/ Keyword（模糊）/ PublishStatus（DRAFT/PUBLISHED/ALL）/ Status（ENABLED/DISABLED/ALL）
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认 0（按 ID 批量查询时忽略）
        :type Offset: int
        :param _Limit: 每页数量，默认 20，最大 200（按 ID 批量查询时忽略）
        :type Limit: int
        :param _AccountId: 授权方企业账号标识；仅 Source=AUTHORIZED 时生效。不传则由后端用 Uin 推导全部已授权范围；未携带 SkillId 的分页查询必传
        :type AccountId: str
        :param _AgentId: 仅 Source=AUTHORIZED 时生效。Agent 绑定了 OneID 租户时，授权集合强制收窄到绑定租户；显式传入的 AccountId 必须等于绑定值，否则请求被拒绝。绑定 Agent 的分页查询可不传 AccountId（服务端按绑定值收窄到单一授权方）
        :type AgentId: str
        """
        self._Source = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._AccountId = None
        self._AgentId = None

    @property
    def Source(self):
        r"""技能来源，必填：BUILTIN（内置）/ CUSTOM（自建）/ AUTHORIZED（企业授权）。数据通路判别，非筛选条件
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Filters(self):
        r"""标准过滤条件：SkillId（精确，多值 OR ≤100，携带即按 ID 批量查询）/ Keyword（模糊）/ PublishStatus（DRAFT/PUBLISHED/ALL）/ Status（ENABLED/DISABLED/ALL）
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认 0（按 ID 批量查询时忽略）
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，默认 20，最大 200（按 ID 批量查询时忽略）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AccountId(self):
        r"""授权方企业账号标识；仅 Source=AUTHORIZED 时生效。不传则由后端用 Uin 推导全部已授权范围；未携带 SkillId 的分页查询必传
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def AgentId(self):
        r"""仅 Source=AUTHORIZED 时生效。Agent 绑定了 OneID 租户时，授权集合强制收窄到绑定租户；显式传入的 AccountId 必须等于绑定值，否则请求被拒绝。绑定 Agent 的分页查询可不传 AccountId（服务端按绑定值收窄到单一授权方）
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._Source = params.get("Source")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AccountId = params.get("AccountId")
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSkillListResponse(AbstractModel):
    r"""DescribeSkillList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的技能总数（按 ID 批量时为实际命中数）
        :type TotalCount: int
        :param _SkillSet: 技能列表（仅列表展示所需字段，完整信息走 DescribeSkill）
        :type SkillSet: list of SkillItem
        :param _Counts: 全局计数（不受 keyword 影响）
注意：此字段可能返回 null，表示取不到有效值。
        :type Counts: :class:`tencentcloud.workbuddyenterprise.v20260709.models.SkillCounts`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SkillSet = None
        self._Counts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合条件的技能总数（按 ID 批量时为实际命中数）
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SkillSet(self):
        r"""技能列表（仅列表展示所需字段，完整信息走 DescribeSkill）
        :rtype: list of SkillItem
        """
        return self._SkillSet

    @SkillSet.setter
    def SkillSet(self, SkillSet):
        self._SkillSet = SkillSet

    @property
    def Counts(self):
        r"""全局计数（不受 keyword 影响）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.SkillCounts`
        """
        return self._Counts

    @Counts.setter
    def Counts(self, Counts):
        self._Counts = Counts

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SkillSet") is not None:
            self._SkillSet = []
            for item in params.get("SkillSet"):
                obj = SkillItem()
                obj._deserialize(item)
                self._SkillSet.append(obj)
        if params.get("Counts") is not None:
            self._Counts = SkillCounts()
            self._Counts._deserialize(params.get("Counts"))
        self._RequestId = params.get("RequestId")


class ExpertCounts(AbstractModel):
    r"""全局专家计数

    """

    def __init__(self):
        r"""
        :param _Builtin: <p>内置专家数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Builtin: int
        :param _Custom: <p>自建专家数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Custom: int
        :param _Total: <p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._Builtin = None
        self._Custom = None
        self._Total = None

    @property
    def Builtin(self):
        r"""<p>内置专家数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Builtin

    @Builtin.setter
    def Builtin(self, Builtin):
        self._Builtin = Builtin

    @property
    def Custom(self):
        r"""<p>自建专家数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def Total(self):
        r"""<p>总数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Builtin = params.get("Builtin")
        self._Custom = params.get("Custom")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpertItem(AbstractModel):
    r"""专家列表/详情项

    """

    def __init__(self):
        r"""
        :param _Source: <p>专家来源：builtin、custom</p>
        :type Source: str
        :param _DisplayName: <p>展示名</p>
        :type DisplayName: str
        :param _Description: <p>描述</p>
        :type Description: str
        :param _Icon: <p>图标 URL</p>
        :type Icon: str
        :param _Enabled: <p>是否启用</p>
        :type Enabled: bool
        :param _DownloadUrl: <p>下载 URL</p>
        :type DownloadUrl: str
        :param _ModifiedTime: <p>更新时间</p>
        :type ModifiedTime: str
        :param _Status: <p>启停状态：enabled、disabled</p>
        :type Status: str
        :param _ExpertId: <p>专家标识</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpertId: str
        :param _ExpertVersion: <p>当前生效版本号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpertVersion: str
        """
        self._Source = None
        self._DisplayName = None
        self._Description = None
        self._Icon = None
        self._Enabled = None
        self._DownloadUrl = None
        self._ModifiedTime = None
        self._Status = None
        self._ExpertId = None
        self._ExpertVersion = None

    @property
    def Source(self):
        r"""<p>专家来源：builtin、custom</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def DisplayName(self):
        r"""<p>展示名</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        r"""<p>描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Icon(self):
        r"""<p>图标 URL</p>
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Enabled(self):
        r"""<p>是否启用</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def DownloadUrl(self):
        r"""<p>下载 URL</p>
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def ModifiedTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def Status(self):
        r"""<p>启停状态：enabled、disabled</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpertId(self):
        r"""<p>专家标识</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpertId

    @ExpertId.setter
    def ExpertId(self, ExpertId):
        self._ExpertId = ExpertId

    @property
    def ExpertVersion(self):
        r"""<p>当前生效版本号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpertVersion

    @ExpertVersion.setter
    def ExpertVersion(self, ExpertVersion):
        self._ExpertVersion = ExpertVersion


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._Icon = params.get("Icon")
        self._Enabled = params.get("Enabled")
        self._DownloadUrl = params.get("DownloadUrl")
        self._ModifiedTime = params.get("ModifiedTime")
        self._Status = params.get("Status")
        self._ExpertId = params.get("ExpertId")
        self._ExpertVersion = params.get("ExpertVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalAgentInfo(AbstractModel):
    r"""外部 Agent 列表/详情项

    """

    def __init__(self):
        r"""
        :param _A2AAgentId: 外部 A2A agent ID
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AAgentId: str
        :param _Name: 外部 Agent 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Endpoint: 外部 A2A Server URL
注意：此字段可能返回 null，表示取不到有效值。
        :type Endpoint: str
        :param _BindingId: 绑定记录 ID（已绑定时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingId: str
        :param _Bound: 是否已绑定到当前 Agent
注意：此字段可能返回 null，表示取不到有效值。
        :type Bound: bool
        :param _IconUrl: 头像地址（取自 provider card 的 iconUrl）
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param _A2AVersion: 外部 agent card 声明的版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type A2AVersion: str
        :param _A2ASkillSet: A2A card skills 集合
注意：此字段可能返回 null，表示取不到有效值。
        :type A2ASkillSet: list of A2ASkillItem
        """
        self._A2AAgentId = None
        self._Name = None
        self._Description = None
        self._Endpoint = None
        self._BindingId = None
        self._Bound = None
        self._IconUrl = None
        self._A2AVersion = None
        self._A2ASkillSet = None

    @property
    def A2AAgentId(self):
        r"""外部 A2A agent ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2AAgentId

    @A2AAgentId.setter
    def A2AAgentId(self, A2AAgentId):
        self._A2AAgentId = A2AAgentId

    @property
    def Name(self):
        r"""外部 Agent 名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Endpoint(self):
        r"""外部 A2A Server URL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def BindingId(self):
        r"""绑定记录 ID（已绑定时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

    @property
    def Bound(self):
        r"""是否已绑定到当前 Agent
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Bound

    @Bound.setter
    def Bound(self, Bound):
        self._Bound = Bound

    @property
    def IconUrl(self):
        r"""头像地址（取自 provider card 的 iconUrl）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def A2AVersion(self):
        r"""外部 agent card 声明的版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._A2AVersion

    @A2AVersion.setter
    def A2AVersion(self, A2AVersion):
        self._A2AVersion = A2AVersion

    @property
    def A2ASkillSet(self):
        r"""A2A card skills 集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of A2ASkillItem
        """
        return self._A2ASkillSet

    @A2ASkillSet.setter
    def A2ASkillSet(self, A2ASkillSet):
        self._A2ASkillSet = A2ASkillSet


    def _deserialize(self, params):
        self._A2AAgentId = params.get("A2AAgentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Endpoint = params.get("Endpoint")
        self._BindingId = params.get("BindingId")
        self._Bound = params.get("Bound")
        self._IconUrl = params.get("IconUrl")
        self._A2AVersion = params.get("A2AVersion")
        if params.get("A2ASkillSet") is not None:
            self._A2ASkillSet = []
            for item in params.get("A2ASkillSet"):
                obj = A2ASkillItem()
                obj._deserialize(item)
                self._A2ASkillSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""云 API 通用过滤结构。多个 Filter 之间为 AND 关系；同一 Filter 内多个 Values 为 OR 关系。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤属性名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Values: 过滤值列表（同一 Filter 内多个值为 OR 关系）
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        :param _ExactMatch: 是否精确匹配，默认 false（模糊匹配）
注意：此字段可能返回 null，表示取不到有效值。
        :type ExactMatch: bool
        """
        self._Name = None
        self._Values = None
        self._ExactMatch = None

    @property
    def Name(self):
        r"""过滤属性名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""过滤值列表（同一 Filter 内多个值为 OR 关系）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        r"""是否精确匹配，默认 false（模糊匹配）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageEvent(AbstractModel):
    r"""消息事件

    """

    def __init__(self):
        r"""
        :param _Sequence: <p>序号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Sequence: int
        :param _EventType: <p>类型 USER/TOOL/ASSISTANT</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EventType: str
        :param _OccurredAt: <p>发生时间 ISO8601</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OccurredAt: str
        :param _Message: <p>消息内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: :class:`tencentcloud.workbuddyenterprise.v20260709.models.MessageEventMessage`
        :param _ToolCall: <p>工具调用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolCall: :class:`tencentcloud.workbuddyenterprise.v20260709.models.MessageEventToolCall`
        """
        self._Sequence = None
        self._EventType = None
        self._OccurredAt = None
        self._Message = None
        self._ToolCall = None

    @property
    def Sequence(self):
        r"""<p>序号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def EventType(self):
        r"""<p>类型 USER/TOOL/ASSISTANT</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def OccurredAt(self):
        r"""<p>发生时间 ISO8601</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OccurredAt

    @OccurredAt.setter
    def OccurredAt(self, OccurredAt):
        self._OccurredAt = OccurredAt

    @property
    def Message(self):
        r"""<p>消息内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.MessageEventMessage`
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ToolCall(self):
        r"""<p>工具调用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.MessageEventToolCall`
        """
        return self._ToolCall

    @ToolCall.setter
    def ToolCall(self, ToolCall):
        self._ToolCall = ToolCall


    def _deserialize(self, params):
        self._Sequence = params.get("Sequence")
        self._EventType = params.get("EventType")
        self._OccurredAt = params.get("OccurredAt")
        if params.get("Message") is not None:
            self._Message = MessageEventMessage()
            self._Message._deserialize(params.get("Message"))
        if params.get("ToolCall") is not None:
            self._ToolCall = MessageEventToolCall()
            self._ToolCall._deserialize(params.get("ToolCall"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageEventMessage(AbstractModel):
    r"""消息内容

    """

    def __init__(self):
        r"""
        :param _Content: <p>文本内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _TokenUsage: <p>Token用量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenUsage: :class:`tencentcloud.workbuddyenterprise.v20260709.models.TokenUsage`
        """
        self._Content = None
        self._TokenUsage = None

    @property
    def Content(self):
        r"""<p>文本内容</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def TokenUsage(self):
        r"""<p>Token用量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.TokenUsage`
        """
        return self._TokenUsage

    @TokenUsage.setter
    def TokenUsage(self, TokenUsage):
        self._TokenUsage = TokenUsage


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("TokenUsage") is not None:
            self._TokenUsage = TokenUsage()
            self._TokenUsage._deserialize(params.get("TokenUsage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageEventToolCall(AbstractModel):
    r"""工具调用

    """

    def __init__(self):
        r"""
        :param _ToolCallId: <p>调用ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolCallId: str
        :param _ToolName: <p>工具名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolName: str
        :param _Status: <p>状态 PENDING/IN_PROGRESS/SUCCEEDED/FAILED</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Input: <p>工具调用Input（已递归脱敏，JSON 字符串）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: str
        :param _Output: <p>工具调用Output（已递归脱敏，JSON 字符串）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        :param _EndedAt: <p>结束时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EndedAt: str
        :param _DurationMs: <p>耗时毫秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationMs: int
        :param _StartedAt: <p>调用开始时间（RFC3339 格式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedAt: str
        """
        self._ToolCallId = None
        self._ToolName = None
        self._Status = None
        self._Input = None
        self._Output = None
        self._EndedAt = None
        self._DurationMs = None
        self._StartedAt = None

    @property
    def ToolCallId(self):
        r"""<p>调用ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ToolCallId

    @ToolCallId.setter
    def ToolCallId(self, ToolCallId):
        self._ToolCallId = ToolCallId

    @property
    def ToolName(self):
        r"""<p>工具名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def Status(self):
        r"""<p>状态 PENDING/IN_PROGRESS/SUCCEEDED/FAILED</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        r"""<p>工具调用Input（已递归脱敏，JSON 字符串）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        r"""<p>工具调用Output（已递归脱敏，JSON 字符串）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def EndedAt(self):
        r"""<p>结束时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndedAt

    @EndedAt.setter
    def EndedAt(self, EndedAt):
        self._EndedAt = EndedAt

    @property
    def DurationMs(self):
        r"""<p>耗时毫秒</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def StartedAt(self):
        r"""<p>调用开始时间（RFC3339 格式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt


    def _deserialize(self, params):
        self._ToolCallId = params.get("ToolCallId")
        self._ToolName = params.get("ToolName")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._EndedAt = params.get("EndedAt")
        self._DurationMs = params.get("DurationMs")
        self._StartedAt = params.get("StartedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateAgentSessionRequest(AbstractModel):
    r"""MigrateAgentSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>待迁移的会话 ID（必填）</p>
        :type SessionId: str
        :param _AgentId: <p>目标 Agent 业务 ID（必填），必须与 Session 原 Agent 相同</p>
        :type AgentId: str
        :param _TargetVersionId: <p>目标版本 ID（必填，字符串形式）。需归属同一 Agent 且未被废弃</p>
        :type TargetVersionId: str
        """
        self._SessionId = None
        self._AgentId = None
        self._TargetVersionId = None

    @property
    def SessionId(self):
        r"""<p>待迁移的会话 ID（必填）</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AgentId(self):
        r"""<p>目标 Agent 业务 ID（必填），必须与 Session 原 Agent 相同</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def TargetVersionId(self):
        r"""<p>目标版本 ID（必填，字符串形式）。需归属同一 Agent 且未被废弃</p>
        :rtype: str
        """
        return self._TargetVersionId

    @TargetVersionId.setter
    def TargetVersionId(self, TargetVersionId):
        self._TargetVersionId = TargetVersionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._AgentId = params.get("AgentId")
        self._TargetVersionId = params.get("TargetVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateAgentSessionResponse(AbstractModel):
    r"""MigrateAgentSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>会话 ID（回显原值，保持不变）</p>
        :type SessionId: str
        :param _Status: <p>迁移后的会话状态</p>
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._Status = None
        self._RequestId = None

    @property
    def SessionId(self):
        r"""<p>会话 ID（回显原值，保持不变）</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Status(self):
        r"""<p>迁移后的会话状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyAgentA2AConfigRequest(AbstractModel):
    r"""ModifyAgentA2AConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _A2AEnabled: <p>Agent 级唯一 A2A 开关</p>
        :type A2AEnabled: bool
        :param _A2ASkillSet: <p>A2A 技能集合（原 A2ASkills）</p>
        :type A2ASkillSet: list of A2ASkillInput
        """
        self._AgentId = None
        self._A2AEnabled = None
        self._A2ASkillSet = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def A2AEnabled(self):
        r"""<p>Agent 级唯一 A2A 开关</p>
        :rtype: bool
        """
        return self._A2AEnabled

    @A2AEnabled.setter
    def A2AEnabled(self, A2AEnabled):
        self._A2AEnabled = A2AEnabled

    @property
    def A2ASkillSet(self):
        r"""<p>A2A 技能集合（原 A2ASkills）</p>
        :rtype: list of A2ASkillInput
        """
        return self._A2ASkillSet

    @A2ASkillSet.setter
    def A2ASkillSet(self, A2ASkillSet):
        self._A2ASkillSet = A2ASkillSet


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._A2AEnabled = params.get("A2AEnabled")
        if params.get("A2ASkillSet") is not None:
            self._A2ASkillSet = []
            for item in params.get("A2ASkillSet"):
                obj = A2ASkillInput()
                obj._deserialize(item)
                self._A2ASkillSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentA2AConfigResponse(AbstractModel):
    r"""ModifyAgentA2AConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent 业务 ID</p>
        :type AgentId: str
        :param _AgentName: <p>Agent 名称</p>
        :type AgentName: str
        :param _Description: <p>Agent 描述</p>
        :type Description: str
        :param _AvatarUrl: <p>头像 URL</p>
        :type AvatarUrl: str
        :param _IsDebug: <p>是否调试 Agent</p>
        :type IsDebug: bool
        :param _CreatedTime: <p>创建时间（RFC3339）</p>
        :type CreatedTime: str
        :param _ModifiedTime: <p>更新时间（RFC3339）</p>
        :type ModifiedTime: str
        :param _RoutingSet: <p>流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）</p>
        :type RoutingSet: list of RoutingItem
        :param _A2AConfig: <p>A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）</p>
        :type A2AConfig: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._AgentName = None
        self._Description = None
        self._AvatarUrl = None
        self._IsDebug = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._RoutingSet = None
        self._A2AConfig = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""<p>Agent 业务 ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""<p>Agent 名称</p>
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def Description(self):
        r"""<p>Agent 描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""<p>头像 URL</p>
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def IsDebug(self):
        r"""<p>是否调试 Agent</p>
        :rtype: bool
        """
        return self._IsDebug

    @IsDebug.setter
    def IsDebug(self, IsDebug):
        self._IsDebug = IsDebug

    @property
    def CreatedTime(self):
        r"""<p>创建时间（RFC3339）</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""<p>更新时间（RFC3339）</p>
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def RoutingSet(self):
        r"""<p>流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）</p>
        :rtype: list of RoutingItem
        """
        return self._RoutingSet

    @RoutingSet.setter
    def RoutingSet(self, RoutingSet):
        self._RoutingSet = RoutingSet

    @property
    def A2AConfig(self):
        r"""<p>A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）</p>
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        """
        return self._A2AConfig

    @A2AConfig.setter
    def A2AConfig(self, A2AConfig):
        self._A2AConfig = A2AConfig

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        self._IsDebug = params.get("IsDebug")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        if params.get("RoutingSet") is not None:
            self._RoutingSet = []
            for item in params.get("RoutingSet"):
                obj = RoutingItem()
                obj._deserialize(item)
                self._RoutingSet.append(obj)
        if params.get("A2AConfig") is not None:
            self._A2AConfig = A2AConfig()
            self._A2AConfig._deserialize(params.get("A2AConfig"))
        self._RequestId = params.get("RequestId")


class ModifyAgentRequest(AbstractModel):
    r"""ModifyAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _AgentName: Agent 名称（可选，仅传递需要更新的字段）
        :type AgentName: str
        :param _Description: Agent 描述（可选）
        :type Description: str
        :param _AvatarUrl: 头像 URL（可选）
        :type AvatarUrl: str
        """
        self._AgentId = None
        self._AgentName = None
        self._Description = None
        self._AvatarUrl = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""Agent 名称（可选，仅传递需要更新的字段）
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def Description(self):
        r"""Agent 描述（可选）
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""头像 URL（可选）
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentResponse(AbstractModel):
    r"""ModifyAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _AgentName: Agent 名称
        :type AgentName: str
        :param _Description: Agent 描述
        :type Description: str
        :param _AvatarUrl: 头像 URL
        :type AvatarUrl: str
        :param _IsDebug: 是否调试 Agent
        :type IsDebug: bool
        :param _CreatedTime: 创建时间（RFC3339）
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间（RFC3339）
        :type ModifiedTime: str
        :param _RoutingSet: 流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）
        :type RoutingSet: list of RoutingItem
        :param _A2AConfig: A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）
        :type A2AConfig: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        :param _AccountId: 绑定的 OneID 企业账号 ID。允许为空：未绑定的存量与新建 Agent 该字段缺省，绑定后回显绑定值
        :type AccountId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._AgentName = None
        self._Description = None
        self._AvatarUrl = None
        self._IsDebug = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._RoutingSet = None
        self._A2AConfig = None
        self._AccountId = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""Agent 名称
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def Description(self):
        r"""Agent 描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""头像 URL
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def IsDebug(self):
        r"""是否调试 Agent
        :rtype: bool
        """
        return self._IsDebug

    @IsDebug.setter
    def IsDebug(self, IsDebug):
        self._IsDebug = IsDebug

    @property
    def CreatedTime(self):
        r"""创建时间（RFC3339）
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间（RFC3339）
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def RoutingSet(self):
        r"""流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）
        :rtype: list of RoutingItem
        """
        return self._RoutingSet

    @RoutingSet.setter
    def RoutingSet(self, RoutingSet):
        self._RoutingSet = RoutingSet

    @property
    def A2AConfig(self):
        r"""A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        """
        return self._A2AConfig

    @A2AConfig.setter
    def A2AConfig(self, A2AConfig):
        self._A2AConfig = A2AConfig

    @property
    def AccountId(self):
        r"""绑定的 OneID 企业账号 ID。允许为空：未绑定的存量与新建 Agent 该字段缺省，绑定后回显绑定值
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        self._IsDebug = params.get("IsDebug")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        if params.get("RoutingSet") is not None:
            self._RoutingSet = []
            for item in params.get("RoutingSet"):
                obj = RoutingItem()
                obj._deserialize(item)
                self._RoutingSet.append(obj)
        if params.get("A2AConfig") is not None:
            self._A2AConfig = A2AConfig()
            self._A2AConfig._deserialize(params.get("A2AConfig"))
        self._AccountId = params.get("AccountId")
        self._RequestId = params.get("RequestId")


class ModifyAgentRoutingRequest(AbstractModel):
    r"""ModifyAgentRouting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _RoutingSet: 路由配置，覆盖式写入（与出参 AgentInfo.RoutingSet 命名对齐）
        :type RoutingSet: list of RoutingItem
        """
        self._AgentId = None
        self._RoutingSet = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def RoutingSet(self):
        r"""路由配置，覆盖式写入（与出参 AgentInfo.RoutingSet 命名对齐）
        :rtype: list of RoutingItem
        """
        return self._RoutingSet

    @RoutingSet.setter
    def RoutingSet(self, RoutingSet):
        self._RoutingSet = RoutingSet


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        if params.get("RoutingSet") is not None:
            self._RoutingSet = []
            for item in params.get("RoutingSet"):
                obj = RoutingItem()
                obj._deserialize(item)
                self._RoutingSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentRoutingResponse(AbstractModel):
    r"""ModifyAgentRouting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _AgentName: Agent 名称
        :type AgentName: str
        :param _Description: Agent 描述
        :type Description: str
        :param _AvatarUrl: 头像 URL
        :type AvatarUrl: str
        :param _IsDebug: 是否调试 Agent
        :type IsDebug: bool
        :param _CreatedTime: 创建时间（RFC3339）
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间（RFC3339）
        :type ModifiedTime: str
        :param _RoutingSet: 流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）
        :type RoutingSet: list of RoutingItem
        :param _A2AConfig: A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）
        :type A2AConfig: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        :param _AccountId: 绑定的 OneID 企业账号 ID。允许为空：未绑定的存量与新建 Agent 该字段缺省，绑定后回显绑定值
        :type AccountId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._AgentName = None
        self._Description = None
        self._AvatarUrl = None
        self._IsDebug = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._RoutingSet = None
        self._A2AConfig = None
        self._AccountId = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""Agent 名称
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def Description(self):
        r"""Agent 描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AvatarUrl(self):
        r"""头像 URL
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def IsDebug(self):
        r"""是否调试 Agent
        :rtype: bool
        """
        return self._IsDebug

    @IsDebug.setter
    def IsDebug(self, IsDebug):
        self._IsDebug = IsDebug

    @property
    def CreatedTime(self):
        r"""创建时间（RFC3339）
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间（RFC3339）
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def RoutingSet(self):
        r"""流量路由配置（VersionId 恒为字符串，防 JS 精度丢失）
        :rtype: list of RoutingItem
        """
        return self._RoutingSet

    @RoutingSet.setter
    def RoutingSet(self, RoutingSet):
        self._RoutingSet = RoutingSet

    @property
    def A2AConfig(self):
        r"""A2A 对外互通配置与注册态（只读回显；原四个平铺字段收进结构）
        :rtype: :class:`tencentcloud.workbuddyenterprise.v20260709.models.A2AConfig`
        """
        return self._A2AConfig

    @A2AConfig.setter
    def A2AConfig(self, A2AConfig):
        self._A2AConfig = A2AConfig

    @property
    def AccountId(self):
        r"""绑定的 OneID 企业账号 ID。允许为空：未绑定的存量与新建 Agent 该字段缺省，绑定后回显绑定值
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._Description = params.get("Description")
        self._AvatarUrl = params.get("AvatarUrl")
        self._IsDebug = params.get("IsDebug")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        if params.get("RoutingSet") is not None:
            self._RoutingSet = []
            for item in params.get("RoutingSet"):
                obj = RoutingItem()
                obj._deserialize(item)
                self._RoutingSet.append(obj)
        if params.get("A2AConfig") is not None:
            self._A2AConfig = A2AConfig()
            self._A2AConfig._deserialize(params.get("A2AConfig"))
        self._AccountId = params.get("AccountId")
        self._RequestId = params.get("RequestId")


class ModifyAgentVersionRequest(AbstractModel):
    r"""ModifyAgentVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _VersionId: 版本 ID（仅 default 或 test 版本可原地更新，prod 拒绝）
        :type VersionId: str
        :param _Manifest: Manifest v2.0 原文（可选；Manifest / Model / Description / SandboxTemplateId / ConnectorSet 五个可选字段至少提供一个）
        :type Manifest: str
        :param _Model: 模型标识（可选）
        :type Model: str
        :param _Description: 版本变更说明（可选）
        :type Description: str
        :param _SandboxTemplateId: 沙箱模板 ID。可选，patch 语义：null 不修改；空串解绑（恢复系统默认模板）；非空时模板须属于当前企业且可用（未删除、状态正常）。
        :type SandboxTemplateId: str
        :param _ConnectorSet: 该版本最终绑定的连接器集合（全量覆盖语义）：缺省 = 本次不改动连接器绑定；空数组 = 解绑全部连接器；非空 = 物化为 manifest v2 mcp_servers 网关条目，manifest 中不在本集合内的连接器条目会被移除（解绑在服务端闭环，无需调用方改写 Manifest）
        :type ConnectorSet: list of ConnectorRefInput
        """
        self._AgentId = None
        self._VersionId = None
        self._Manifest = None
        self._Model = None
        self._Description = None
        self._SandboxTemplateId = None
        self._ConnectorSet = None

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def VersionId(self):
        r"""版本 ID（仅 default 或 test 版本可原地更新，prod 拒绝）
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Manifest(self):
        r"""Manifest v2.0 原文（可选；Manifest / Model / Description / SandboxTemplateId / ConnectorSet 五个可选字段至少提供一个）
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Model(self):
        r"""模型标识（可选）
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Description(self):
        r"""版本变更说明（可选）
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SandboxTemplateId(self):
        r"""沙箱模板 ID。可选，patch 语义：null 不修改；空串解绑（恢复系统默认模板）；非空时模板须属于当前企业且可用（未删除、状态正常）。
        :rtype: str
        """
        return self._SandboxTemplateId

    @SandboxTemplateId.setter
    def SandboxTemplateId(self, SandboxTemplateId):
        self._SandboxTemplateId = SandboxTemplateId

    @property
    def ConnectorSet(self):
        r"""该版本最终绑定的连接器集合（全量覆盖语义）：缺省 = 本次不改动连接器绑定；空数组 = 解绑全部连接器；非空 = 物化为 manifest v2 mcp_servers 网关条目，manifest 中不在本集合内的连接器条目会被移除（解绑在服务端闭环，无需调用方改写 Manifest）
        :rtype: list of ConnectorRefInput
        """
        return self._ConnectorSet

    @ConnectorSet.setter
    def ConnectorSet(self, ConnectorSet):
        self._ConnectorSet = ConnectorSet


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._VersionId = params.get("VersionId")
        self._Manifest = params.get("Manifest")
        self._Model = params.get("Model")
        self._Description = params.get("Description")
        self._SandboxTemplateId = params.get("SandboxTemplateId")
        if params.get("ConnectorSet") is not None:
            self._ConnectorSet = []
            for item in params.get("ConnectorSet"):
                obj = ConnectorRefInput()
                obj._deserialize(item)
                self._ConnectorSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentVersionResponse(AbstractModel):
    r"""ModifyAgentVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionId: 版本 ID
        :type VersionId: str
        :param _AgentId: Agent 业务 ID
        :type AgentId: str
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _VersionType: 版本类型：DEFAULT / TEST / PROD
        :type VersionType: str
        :param _Description: 版本变更说明
        :type Description: str
        :param _Model: 模型标识
        :type Model: str
        :param _Manifest: Manifest v2.0 精简 manifest 原文（JSON 字符串）
        :type Manifest: str
        :param _Status: 版本状态：DRAFT / ENABLED / DISABLED
        :type Status: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间
        :type ModifiedTime: str
        :param _SandboxTemplateId: 绑定的沙箱模板 ID；未绑定时为空，创建会话沙箱使用系统默认模板。
        :type SandboxTemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionId = None
        self._AgentId = None
        self._VersionName = None
        self._VersionType = None
        self._Description = None
        self._Model = None
        self._Manifest = None
        self._Status = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._SandboxTemplateId = None
        self._RequestId = None

    @property
    def VersionId(self):
        r"""版本 ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def AgentId(self):
        r"""Agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def VersionName(self):
        r"""版本名称
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionType(self):
        r"""版本类型：DEFAULT / TEST / PROD
        :rtype: str
        """
        return self._VersionType

    @VersionType.setter
    def VersionType(self, VersionType):
        self._VersionType = VersionType

    @property
    def Description(self):
        r"""版本变更说明
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Model(self):
        r"""模型标识
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Manifest(self):
        r"""Manifest v2.0 精简 manifest 原文（JSON 字符串）
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Status(self):
        r"""版本状态：DRAFT / ENABLED / DISABLED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def SandboxTemplateId(self):
        r"""绑定的沙箱模板 ID；未绑定时为空，创建会话沙箱使用系统默认模板。
        :rtype: str
        """
        return self._SandboxTemplateId

    @SandboxTemplateId.setter
    def SandboxTemplateId(self, SandboxTemplateId):
        self._SandboxTemplateId = SandboxTemplateId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._AgentId = params.get("AgentId")
        self._VersionName = params.get("VersionName")
        self._VersionType = params.get("VersionType")
        self._Description = params.get("Description")
        self._Model = params.get("Model")
        self._Manifest = params.get("Manifest")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._SandboxTemplateId = params.get("SandboxTemplateId")
        self._RequestId = params.get("RequestId")


class RoutingItem(AbstractModel):
    r"""路由项

    """

    def __init__(self):
        r"""
        :param _VersionId: 版本 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _Weight: 权重，(0, 1] 之间的浮点百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: float
        """
        self._VersionId = None
        self._Weight = None

    @property
    def VersionId(self):
        r"""版本 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Weight(self):
        r"""权重，(0, 1] 之间的浮点百分比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionItem(AbstractModel):
    r"""会话列表项

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _SessionName: 会话名称（AI 生成标题或用户改名；缺失时为空）
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionName: str
        :param _AgentId: Agent 业务 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param _AgentName: Agent 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentName: str
        :param _VersionName: 会话使用的版本名称（与 VersionId 区分：此为版本名，非 ID；原 AgentVersion）
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _VersionId: 会话使用的 Agent 版本 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _Status: 会话状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Creator: 创建者 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _Source: 会话来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _CreatedTime: 创建时间（RFC3339）
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 更新时间（RFC3339）
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        """
        self._SessionId = None
        self._SessionName = None
        self._AgentId = None
        self._AgentName = None
        self._VersionName = None
        self._VersionId = None
        self._Status = None
        self._Creator = None
        self._Source = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def SessionId(self):
        r"""会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SessionName(self):
        r"""会话名称（AI 生成标题或用户改名；缺失时为空）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionName

    @SessionName.setter
    def SessionName(self, SessionName):
        self._SessionName = SessionName

    @property
    def AgentId(self):
        r"""Agent 业务 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def AgentName(self):
        r"""Agent 名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentName

    @AgentName.setter
    def AgentName(self, AgentName):
        self._AgentName = AgentName

    @property
    def VersionName(self):
        r"""会话使用的版本名称（与 VersionId 区分：此为版本名，非 ID；原 AgentVersion）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionId(self):
        r"""会话使用的 Agent 版本 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Status(self):
        r"""会话状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Creator(self):
        r"""创建者 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def Source(self):
        r"""会话来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def CreatedTime(self):
        r"""创建时间（RFC3339）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""更新时间（RFC3339）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._SessionName = params.get("SessionName")
        self._AgentId = params.get("AgentId")
        self._AgentName = params.get("AgentName")
        self._VersionName = params.get("VersionName")
        self._VersionId = params.get("VersionId")
        self._Status = params.get("Status")
        self._Creator = params.get("Creator")
        self._Source = params.get("Source")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillCounts(AbstractModel):
    r"""全局技能计数

    """

    def __init__(self):
        r"""
        :param _Builtin: 内置技能数
注意：此字段可能返回 null，表示取不到有效值。
        :type Builtin: int
        :param _Custom: 自建技能数
注意：此字段可能返回 null，表示取不到有效值。
        :type Custom: int
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._Builtin = None
        self._Custom = None
        self._Total = None

    @property
    def Builtin(self):
        r"""内置技能数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Builtin

    @Builtin.setter
    def Builtin(self, Builtin):
        self._Builtin = Builtin

    @property
    def Custom(self):
        r"""自建技能数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def Total(self):
        r"""总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Builtin = params.get("Builtin")
        self._Custom = params.get("Custom")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillItem(AbstractModel):
    r"""Skill 列表项（按列表页展示裁剪：名称/版本/描述/状态/操作五列 + 编排所需的 Source 与 DownloadUrl）

    """

    def __init__(self):
        r"""
        :param _Source: 技能来源：BUILTIN（内置）/ CUSTOM（自建）/ AUTHORIZED（企业授权）
        :type Source: str
        :param _Name: <p>slug（仅 custom 返回）</p>
        :type Name: str
        :param _DisplayName: <p>展示名</p>
        :type DisplayName: str
        :param _Description: <p>描述</p>
        :type Description: str
        :param _Icon: <p>图标 URL</p>
        :type Icon: str
        :param _Enabled: <p>是否启用</p>
        :type Enabled: bool
        :param _DownloadUrl: <p>下载 URL</p>
        :type DownloadUrl: str
        :param _SkillId: <p>技能标识</p>
        :type SkillId: str
        :param _SkillVersion: <p>当前生效版本号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillVersion: str
        :param _CreateTime: 创建时间，RFC3339 UTC 格式（如 2026-08-11T09:23:10Z）
        :type CreateTime: str
        :param _UpdateTime: 更新时间，RFC3339 UTC 格式（如 2026-09-15T06:51:26Z）
        :type UpdateTime: str
        """
        self._Source = None
        self._Name = None
        self._DisplayName = None
        self._Description = None
        self._Icon = None
        self._Enabled = None
        self._DownloadUrl = None
        self._SkillId = None
        self._SkillVersion = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Source(self):
        r"""技能来源：BUILTIN（内置）/ CUSTOM（自建）/ AUTHORIZED（企业授权）
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Name(self):
        r"""<p>slug（仅 custom 返回）</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DisplayName(self):
        r"""<p>展示名</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        r"""<p>描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Icon(self):
        r"""<p>图标 URL</p>
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Enabled(self):
        r"""<p>是否启用</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def DownloadUrl(self):
        r"""<p>下载 URL</p>
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def SkillId(self):
        r"""<p>技能标识</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SkillVersion(self):
        r"""<p>当前生效版本号</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SkillVersion

    @SkillVersion.setter
    def SkillVersion(self, SkillVersion):
        self._SkillVersion = SkillVersion

    @property
    def CreateTime(self):
        r"""创建时间，RFC3339 UTC 格式（如 2026-08-11T09:23:10Z）
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间，RFC3339 UTC 格式（如 2026-09-15T06:51:26Z）
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Name = params.get("Name")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._Icon = params.get("Icon")
        self._Enabled = params.get("Enabled")
        self._DownloadUrl = params.get("DownloadUrl")
        self._SkillId = params.get("SkillId")
        self._SkillVersion = params.get("SkillVersion")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenUsage(AbstractModel):
    r"""Token用量

    """

    def __init__(self):
        r"""
        :param _InputTokens: <p>输入Token</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InputTokens: int
        :param _OutputTokens: <p>输出Token</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputTokens: int
        :param _TotalTokens: <p>总Token</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTokens: int
        :param _Scope: <p>统计口径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Scope: str
        """
        self._InputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None
        self._Scope = None

    @property
    def InputTokens(self):
        r"""<p>输入Token</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def OutputTokens(self):
        r"""<p>输出Token</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        r"""<p>总Token</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def Scope(self):
        r"""<p>统计口径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._InputTokens = params.get("InputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindExternalAgentRequest(AbstractModel):
    r"""UnbindExternalAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: TMA managed agent 业务 ID
        :type AgentId: str
        :param _A2AAgentId: 已绑定的外部 A2A agent ID
        :type A2AAgentId: str
        :param _BindingId: 绑定记录 ID（自增 ID 字符串）
        :type BindingId: str
        :param _VersionId: 版本 ID
        :type VersionId: str
        """
        self._AgentId = None
        self._A2AAgentId = None
        self._BindingId = None
        self._VersionId = None

    @property
    def AgentId(self):
        r"""TMA managed agent 业务 ID
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def A2AAgentId(self):
        r"""已绑定的外部 A2A agent ID
        :rtype: str
        """
        return self._A2AAgentId

    @A2AAgentId.setter
    def A2AAgentId(self, A2AAgentId):
        self._A2AAgentId = A2AAgentId

    @property
    def BindingId(self):
        r"""绑定记录 ID（自增 ID 字符串）
        :rtype: str
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

    @property
    def VersionId(self):
        r"""版本 ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._A2AAgentId = params.get("A2AAgentId")
        self._BindingId = params.get("BindingId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindExternalAgentResponse(AbstractModel):
    r"""UnbindExternalAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果状态（大写枚举）：BOUND=已绑定 / UNBOUND=已解绑
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""操作结果状态（大写枚举）：BOUND=已绑定 / UNBOUND=已解绑
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")