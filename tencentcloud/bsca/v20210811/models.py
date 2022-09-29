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


class CVSSV2Info(AbstractModel):
    """CVSSv2.0详细信息。

    """

    def __init__(self):
        r"""
        :param CVSS: CVE评分。
        :type CVSS: float
        :param AccessVector: AccessVector 攻击途径。
取值范围：
<li>NETWORK 远程</li>
<li>ADJACENT_NETWORK 近邻</li>
<li>LOCAL 本地</li>
        :type AccessVector: str
        :param AccessComplexity: AccessComplexity 攻击复杂度。
取值范围：
<li>HIGH 高</li>
<li>MEDIUM 中</li>
<li>LOW 低</li>
        :type AccessComplexity: str
        :param Authentication: Authentication 身份验证。
取值范围：
<li>MULTIPLE 多系统认证</li>
<li>SINGLE 单系统认证</li>
<li>NONE 无</li>
        :type Authentication: str
        :param ConImpact: ConfidentialityImpact 机密性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :type ConImpact: str
        :param IntegrityImpact: IntegrityImpact 完整性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :type IntegrityImpact: str
        :param AvailabilityImpact: AvailabilityImpact 可用性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :type AvailabilityImpact: str
        """
        self.CVSS = None
        self.AccessVector = None
        self.AccessComplexity = None
        self.Authentication = None
        self.ConImpact = None
        self.IntegrityImpact = None
        self.AvailabilityImpact = None


    def _deserialize(self, params):
        self.CVSS = params.get("CVSS")
        self.AccessVector = params.get("AccessVector")
        self.AccessComplexity = params.get("AccessComplexity")
        self.Authentication = params.get("Authentication")
        self.ConImpact = params.get("ConImpact")
        self.IntegrityImpact = params.get("IntegrityImpact")
        self.AvailabilityImpact = params.get("AvailabilityImpact")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVSSV3Info(AbstractModel):
    """Cvssv3.0详细信息。

    """

    def __init__(self):
        r"""
        :param CVSS: CVE评分。
        :type CVSS: float
        :param AttackVector: AttackVector 攻击途径。
取值范围：
<li>NETWORK 远程</li>
<li>ADJACENT_NETWORK 近邻</li>
<li>LOCAL 本地</li>
<li>PHYSICAL 物理</li>
        :type AttackVector: str
        :param AttackComplexity: AttackComplexity 攻击复杂度。
取值范围：
<li>HIGH 高</li>
<li>LOW 低</li>
        :type AttackComplexity: str
        :param PrivilegesRequired: PrivilegesRequired 触发特权。
取值范围：
<li>HIGH 高</li>
<li>LOW 低</li>
<li>NONE 无</li>
        :type PrivilegesRequired: str
        :param UserInteraction: UserInteraction 交互必要性。
取值范围：
<li>NONE 无</li>
<li>REQUIRED 需要</li>
        :type UserInteraction: str
        :param Scope: Scope 绕过安全边界。
取值范围：
<li>UNCHANGED 否</li>
<li>CHANGED 能</li>
        :type Scope: str
        :param ConImpact: ConfidentialityImpact 机密性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :type ConImpact: str
        :param IntegrityImpact: IntegrityImpact 完整性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :type IntegrityImpact: str
        :param AvailabilityImpact: AvailabilityImpact 可用性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :type AvailabilityImpact: str
        """
        self.CVSS = None
        self.AttackVector = None
        self.AttackComplexity = None
        self.PrivilegesRequired = None
        self.UserInteraction = None
        self.Scope = None
        self.ConImpact = None
        self.IntegrityImpact = None
        self.AvailabilityImpact = None


    def _deserialize(self, params):
        self.CVSS = params.get("CVSS")
        self.AttackVector = params.get("AttackVector")
        self.AttackComplexity = params.get("AttackComplexity")
        self.PrivilegesRequired = params.get("PrivilegesRequired")
        self.UserInteraction = params.get("UserInteraction")
        self.Scope = params.get("Scope")
        self.ConImpact = params.get("ConImpact")
        self.IntegrityImpact = params.get("IntegrityImpact")
        self.AvailabilityImpact = params.get("AvailabilityImpact")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Component(AbstractModel):
    """描述一个第三方组件的源信息。

    """

    def __init__(self):
        r"""
        :param PURL: 第三方组件的PURL
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        :param Homepage: 第三方组件的主页
        :type Homepage: str
        :param Summary: 第三方组件的简介
        :type Summary: str
        :param NicknameList: 第三方组件的别名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NicknameList: list of str
        :param CodeLocationList: 第三方组件的代码位置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeLocationList: list of str
        :param LicenseExpression: 第三方组件的许可证表达式
        :type LicenseExpression: str
        """
        self.PURL = None
        self.Homepage = None
        self.Summary = None
        self.NicknameList = None
        self.CodeLocationList = None
        self.LicenseExpression = None


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self.PURL = PURL()
            self.PURL._deserialize(params.get("PURL"))
        self.Homepage = params.get("Homepage")
        self.Summary = params.get("Summary")
        self.NicknameList = params.get("NicknameList")
        self.CodeLocationList = params.get("CodeLocationList")
        self.LicenseExpression = params.get("LicenseExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentVulnerabilitySummary(AbstractModel):
    """与输入组件相关的漏洞信息摘要信息。

    """

    def __init__(self):
        r"""
        :param PURL: 用于匹配漏洞的PURL
注意：此字段可能返回 null，表示取不到有效值。
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        :param CanBeFixed: 该组件是否包含修复漏洞的官方补丁
        :type CanBeFixed: bool
        :param FixedVersion: 修复漏洞的组件版本号
        :type FixedVersion: str
        :param AffectedVersion: 漏洞影响的组件版本号
        :type AffectedVersion: str
        :param AffectedComponent: 漏洞影响组件
        :type AffectedComponent: str
        :param RiskLevel: 漏洞在该产品中的风险等级
<li>Critical</li>
<li>High</li>
<li>Medium</li>
<li>Low</li>
        :type RiskLevel: str
        """
        self.PURL = None
        self.CanBeFixed = None
        self.FixedVersion = None
        self.AffectedVersion = None
        self.AffectedComponent = None
        self.RiskLevel = None


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self.PURL = PURL()
            self.PURL._deserialize(params.get("PURL"))
        self.CanBeFixed = params.get("CanBeFixed")
        self.FixedVersion = params.get("FixedVersion")
        self.AffectedVersion = params.get("AffectedVersion")
        self.AffectedComponent = params.get("AffectedComponent")
        self.RiskLevel = params.get("RiskLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentVulnerabilityUnion(AbstractModel):
    """描述组件漏洞相关概览信息。

    """

    def __init__(self):
        r"""
        :param Summary: 漏洞概览信息
        :type Summary: :class:`tencentcloud.bsca.v20210811.models.VulnerabilitySummary`
        :param SummaryInComponent: 与组件相关的漏洞概览信息
        :type SummaryInComponent: :class:`tencentcloud.bsca.v20210811.models.ComponentVulnerabilitySummary`
        """
        self.Summary = None
        self.SummaryInComponent = None


    def _deserialize(self, params):
        if params.get("Summary") is not None:
            self.Summary = VulnerabilitySummary()
            self.Summary._deserialize(params.get("Summary"))
        if params.get("SummaryInComponent") is not None:
            self.SummaryInComponent = ComponentVulnerabilitySummary()
            self.SummaryInComponent._deserialize(params.get("SummaryInComponent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBComponentRequest(AbstractModel):
    """DescribeKBComponent请求参数结构体

    """

    def __init__(self):
        r"""
        :param PURL: 组件的PURL
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        self.PURL = None


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self.PURL = PURL()
            self.PURL._deserialize(params.get("PURL"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBComponentResponse(AbstractModel):
    """DescribeKBComponent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Component: 匹配的组件信息
        :type Component: :class:`tencentcloud.bsca.v20210811.models.Component`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Component = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Component") is not None:
            self.Component = Component()
            self.Component._deserialize(params.get("Component"))
        self.RequestId = params.get("RequestId")


class DescribeKBComponentVulnerabilityRequest(AbstractModel):
    """DescribeKBComponentVulnerability请求参数结构体

    """

    def __init__(self):
        r"""
        :param PURL: 组件的PURL，其中Name和Version为必填字段
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        self.PURL = None


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self.PURL = PURL()
            self.PURL._deserialize(params.get("PURL"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBComponentVulnerabilityResponse(AbstractModel):
    """DescribeKBComponentVulnerability返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulnerabilityList: 漏洞信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityList: list of ComponentVulnerabilityUnion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulnerabilityList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulnerabilityList") is not None:
            self.VulnerabilityList = []
            for item in params.get("VulnerabilityList"):
                obj = ComponentVulnerabilityUnion()
                obj._deserialize(item)
                self.VulnerabilityList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKBLicenseRequest(AbstractModel):
    """DescribeKBLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param LicenseExpression: License表达式
        :type LicenseExpression: str
        """
        self.LicenseExpression = None


    def _deserialize(self, params):
        self.LicenseExpression = params.get("LicenseExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBLicenseResponse(AbstractModel):
    """DescribeKBLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param LicenseList: 许可证列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseList: list of LicenseUnion
        :param NormalizedLicenseExpression: 用于匹配的License表达式
        :type NormalizedLicenseExpression: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LicenseList = None
        self.NormalizedLicenseExpression = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LicenseList") is not None:
            self.LicenseList = []
            for item in params.get("LicenseList"):
                obj = LicenseUnion()
                obj._deserialize(item)
                self.LicenseList.append(obj)
        self.NormalizedLicenseExpression = params.get("NormalizedLicenseExpression")
        self.RequestId = params.get("RequestId")


class DescribeKBVulnerabilityRequest(AbstractModel):
    """DescribeKBVulnerability请求参数结构体

    """

    def __init__(self):
        r"""
        :param CVEID: CVE ID列表（不能与Vul ID同时存在）
        :type CVEID: list of str
        :param VulID: Vul ID列表（不能与CVE ID 同时存在）
        :type VulID: list of str
        """
        self.CVEID = None
        self.VulID = None


    def _deserialize(self, params):
        self.CVEID = params.get("CVEID")
        self.VulID = params.get("VulID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBVulnerabilityResponse(AbstractModel):
    """DescribeKBVulnerability返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulnerabilityDetailList: 漏洞详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityDetailList: list of VulnerabilityUnion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulnerabilityDetailList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulnerabilityDetailList") is not None:
            self.VulnerabilityDetailList = []
            for item in params.get("VulnerabilityDetailList"):
                obj = VulnerabilityUnion()
                obj._deserialize(item)
                self.VulnerabilityDetailList.append(obj)
        self.RequestId = params.get("RequestId")


class LicenseDetail(AbstractModel):
    """描述许可证的详细信息。

    """

    def __init__(self):
        r"""
        :param Content: 许可证内容
        :type Content: str
        :param ConditionSet: 许可证允许信息列表
        :type ConditionSet: list of LicenseRestriction
        :param ForbiddenSet: 许可证要求信息列表
        :type ForbiddenSet: list of LicenseRestriction
        :param PermissionSet: 许可证禁止信息列表
        :type PermissionSet: list of LicenseRestriction
        """
        self.Content = None
        self.ConditionSet = None
        self.ForbiddenSet = None
        self.PermissionSet = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        if params.get("ConditionSet") is not None:
            self.ConditionSet = []
            for item in params.get("ConditionSet"):
                obj = LicenseRestriction()
                obj._deserialize(item)
                self.ConditionSet.append(obj)
        if params.get("ForbiddenSet") is not None:
            self.ForbiddenSet = []
            for item in params.get("ForbiddenSet"):
                obj = LicenseRestriction()
                obj._deserialize(item)
                self.ForbiddenSet.append(obj)
        if params.get("PermissionSet") is not None:
            self.PermissionSet = []
            for item in params.get("PermissionSet"):
                obj = LicenseRestriction()
                obj._deserialize(item)
                self.PermissionSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseRestriction(AbstractModel):
    """License约束信息。

    """

    def __init__(self):
        r"""
        :param Name: license约束的名称。
        :type Name: str
        :param Description: license约束的描述。
        :type Description: str
        """
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseSummary(AbstractModel):
    """描述许可证的概览信息。

    """

    def __init__(self):
        r"""
        :param Key: 许可证标识符
        :type Key: str
        :param SPDXKey: 许可证的SPDX标识符，见 https://spdx.org/licenses/
        :type SPDXKey: str
        :param ShortName: 许可证短名称
        :type ShortName: str
        :param Name: 许可证完整名称
        :type Name: str
        :param Risk: License风险等级
<li>NotDefined</li>
<li>LowRisk</li>
<li>MediumRisk</li>
<li>HighRisk</li>
        :type Risk: str
        :param Source: 许可证来源URL
        :type Source: str
        """
        self.Key = None
        self.SPDXKey = None
        self.ShortName = None
        self.Name = None
        self.Risk = None
        self.Source = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.SPDXKey = params.get("SPDXKey")
        self.ShortName = params.get("ShortName")
        self.Name = params.get("Name")
        self.Risk = params.get("Risk")
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseUnion(AbstractModel):
    """许可证详细信息。

    """

    def __init__(self):
        r"""
        :param LicenseSummary: 许可证概览信息
        :type LicenseSummary: :class:`tencentcloud.bsca.v20210811.models.LicenseSummary`
        :param LicenseDetail: 许可证详细信息
        :type LicenseDetail: :class:`tencentcloud.bsca.v20210811.models.LicenseDetail`
        """
        self.LicenseSummary = None
        self.LicenseDetail = None


    def _deserialize(self, params):
        if params.get("LicenseSummary") is not None:
            self.LicenseSummary = LicenseSummary()
            self.LicenseSummary._deserialize(params.get("LicenseSummary"))
        if params.get("LicenseDetail") is not None:
            self.LicenseDetail = LicenseDetail()
            self.LicenseDetail._deserialize(params.get("LicenseDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchKBPURLListRequest(AbstractModel):
    """MatchKBPURLList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SHA1: SHA1。
        :type SHA1: str
        """
        self.SHA1 = None


    def _deserialize(self, params):
        self.SHA1 = params.get("SHA1")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchKBPURLListResponse(AbstractModel):
    """MatchKBPURLList返回参数结构体

    """

    def __init__(self):
        r"""
        :param PURLList: 组件列表。
        :type PURLList: list of PURL
        :param Hit: 是否命中数据库。
        :type Hit: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PURLList = None
        self.Hit = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PURLList") is not None:
            self.PURLList = []
            for item in params.get("PURLList"):
                obj = PURL()
                obj._deserialize(item)
                self.PURLList.append(obj)
        self.Hit = params.get("Hit")
        self.RequestId = params.get("RequestId")


class PURL(AbstractModel):
    """PURL(Package URL)用于定位一个产品或组件，见 https://github.com/package-url/purl-spec。

    """

    def __init__(self):
        r"""
        :param Name: 组件名称
        :type Name: str
        :param Protocol: 组件所属的类型，如：github, gitlab, generic, deb, rpm, maven 等
        :type Protocol: str
        :param Namespace: 组件名的前缀名，如github和gitlab的用户名，deb的操作系统，maven包的group id等
        :type Namespace: str
        :param Qualifiers: 修饰组件的额外属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Qualifiers: list of Qualifier
        :param Subpath: 相对于组件包根位置的子目录
        :type Subpath: str
        :param Version: 组件版本号
        :type Version: str
        """
        self.Name = None
        self.Protocol = None
        self.Namespace = None
        self.Qualifiers = None
        self.Subpath = None
        self.Version = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Protocol = params.get("Protocol")
        self.Namespace = params.get("Namespace")
        if params.get("Qualifiers") is not None:
            self.Qualifiers = []
            for item in params.get("Qualifiers"):
                obj = Qualifier()
                obj._deserialize(item)
                self.Qualifiers.append(obj)
        self.Subpath = params.get("Subpath")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Qualifier(AbstractModel):
    """PURL下的Qualifier属性类型，用于定义第三方组件的额外属性，见 https://github.com/package-url/purl-spec。

    """

    def __init__(self):
        r"""
        :param Key: 额外属性的名称。
        :type Key: str
        :param Value: 额外属性的值。
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
        


class VulnerabilityDetail(AbstractModel):
    """描述漏洞详细信息。

    """

    def __init__(self):
        r"""
        :param Category: 漏洞类别
        :type Category: str
        :param CategoryType: 漏洞分类
        :type CategoryType: str
        :param Description: 漏洞描述
        :type Description: str
        :param OfficialSolution: 漏洞官方解决方案
        :type OfficialSolution: str
        :param ReferenceList: 漏洞信息参考列表
        :type ReferenceList: list of str
        :param DefenseSolution: 漏洞防御方案
        :type DefenseSolution: str
        :param CVSSv2Info: 漏洞CVSSv2信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSv2Info: :class:`tencentcloud.bsca.v20210811.models.CVSSV2Info`
        :param CVSSv3Info: 漏洞CVSSv3信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSv3Info: :class:`tencentcloud.bsca.v20210811.models.CVSSV3Info`
        :param SubmitTime: 漏洞提交时间
        :type SubmitTime: str
        :param CWEID: CWE编号
        :type CWEID: str
        :param CVSSv2Vector: 漏洞CVSSv2向量
        :type CVSSv2Vector: str
        :param CVSSv3Vector: 漏洞CVSSv3向量
        :type CVSSv3Vector: str
        """
        self.Category = None
        self.CategoryType = None
        self.Description = None
        self.OfficialSolution = None
        self.ReferenceList = None
        self.DefenseSolution = None
        self.CVSSv2Info = None
        self.CVSSv3Info = None
        self.SubmitTime = None
        self.CWEID = None
        self.CVSSv2Vector = None
        self.CVSSv3Vector = None


    def _deserialize(self, params):
        self.Category = params.get("Category")
        self.CategoryType = params.get("CategoryType")
        self.Description = params.get("Description")
        self.OfficialSolution = params.get("OfficialSolution")
        self.ReferenceList = params.get("ReferenceList")
        self.DefenseSolution = params.get("DefenseSolution")
        if params.get("CVSSv2Info") is not None:
            self.CVSSv2Info = CVSSV2Info()
            self.CVSSv2Info._deserialize(params.get("CVSSv2Info"))
        if params.get("CVSSv3Info") is not None:
            self.CVSSv3Info = CVSSV3Info()
            self.CVSSv3Info._deserialize(params.get("CVSSv3Info"))
        self.SubmitTime = params.get("SubmitTime")
        self.CWEID = params.get("CWEID")
        self.CVSSv2Vector = params.get("CVSSv2Vector")
        self.CVSSv3Vector = params.get("CVSSv3Vector")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulnerabilitySummary(AbstractModel):
    """描述漏洞的摘要信息。

    """

    def __init__(self):
        r"""
        :param VulID: 漏洞ID
        :type VulID: str
        :param CVEID: 漏洞所属CVE编号
        :type CVEID: str
        :param CNVDID: 漏洞所属CNVD编号
        :type CNVDID: str
        :param CNNVDID: 漏洞所属CNNVD编号
        :type CNNVDID: str
        :param Name: 漏洞名称
        :type Name: str
        :param IsSuggest: 该漏洞是否是需重点关注的漏洞
        :type IsSuggest: bool
        :param Severity: 漏洞风险等级
<li>Critical</li>
<li>High</li>
<li>Medium</li>
<li>Low</li>
        :type Severity: str
        """
        self.VulID = None
        self.CVEID = None
        self.CNVDID = None
        self.CNNVDID = None
        self.Name = None
        self.IsSuggest = None
        self.Severity = None


    def _deserialize(self, params):
        self.VulID = params.get("VulID")
        self.CVEID = params.get("CVEID")
        self.CNVDID = params.get("CNVDID")
        self.CNNVDID = params.get("CNNVDID")
        self.Name = params.get("Name")
        self.IsSuggest = params.get("IsSuggest")
        self.Severity = params.get("Severity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulnerabilityUnion(AbstractModel):
    """描述漏洞的详细信息。

    """

    def __init__(self):
        r"""
        :param Summary: 漏洞概览信息
        :type Summary: :class:`tencentcloud.bsca.v20210811.models.VulnerabilitySummary`
        :param Detail: 漏洞详细信息
        :type Detail: :class:`tencentcloud.bsca.v20210811.models.VulnerabilityDetail`
        """
        self.Summary = None
        self.Detail = None


    def _deserialize(self, params):
        if params.get("Summary") is not None:
            self.Summary = VulnerabilitySummary()
            self.Summary._deserialize(params.get("Summary"))
        if params.get("Detail") is not None:
            self.Detail = VulnerabilityDetail()
            self.Detail._deserialize(params.get("Detail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        