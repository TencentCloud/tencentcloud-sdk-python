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


class AffectedComponent(AbstractModel):
    r"""受漏洞影响的组件信息。

    """

    def __init__(self):
        r"""
        :param _Name: 受漏洞影响的组件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AffectedVersionList: 受漏洞影响的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedVersionList: list of str
        :param _FixedVersionList: 修复此漏洞的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FixedVersionList: list of str
        """
        self._Name = None
        self._AffectedVersionList = None
        self._FixedVersionList = None

    @property
    def Name(self):
        r"""受漏洞影响的组件名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AffectedVersionList(self):
        r"""受漏洞影响的版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AffectedVersionList

    @AffectedVersionList.setter
    def AffectedVersionList(self, AffectedVersionList):
        self._AffectedVersionList = AffectedVersionList

    @property
    def FixedVersionList(self):
        r"""修复此漏洞的版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FixedVersionList

    @FixedVersionList.setter
    def FixedVersionList(self, FixedVersionList):
        self._FixedVersionList = FixedVersionList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AffectedVersionList = params.get("AffectedVersionList")
        self._FixedVersionList = params.get("FixedVersionList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVSSV2Info(AbstractModel):
    r"""CVSSv2.0详细信息。

    """

    def __init__(self):
        r"""
        :param _CVSS: CVE评分。
        :type CVSS: float
        :param _AccessVector: AccessVector 攻击途径。
取值范围：
<li>NETWORK 远程</li>
<li>ADJACENT_NETWORK 近邻</li>
<li>LOCAL 本地</li>
        :type AccessVector: str
        :param _AccessComplexity: AccessComplexity 攻击复杂度。
取值范围：
<li>HIGH 高</li>
<li>MEDIUM 中</li>
<li>LOW 低</li>
        :type AccessComplexity: str
        :param _Authentication: Authentication 身份验证。
取值范围：
<li>MULTIPLE 多系统认证</li>
<li>SINGLE 单系统认证</li>
<li>NONE 无</li>
        :type Authentication: str
        :param _ConImpact: ConfidentialityImpact 机密性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :type ConImpact: str
        :param _IntegrityImpact: IntegrityImpact 完整性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :type IntegrityImpact: str
        :param _AvailabilityImpact: AvailabilityImpact 可用性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :type AvailabilityImpact: str
        """
        self._CVSS = None
        self._AccessVector = None
        self._AccessComplexity = None
        self._Authentication = None
        self._ConImpact = None
        self._IntegrityImpact = None
        self._AvailabilityImpact = None

    @property
    def CVSS(self):
        r"""CVE评分。
        :rtype: float
        """
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def AccessVector(self):
        r"""AccessVector 攻击途径。
取值范围：
<li>NETWORK 远程</li>
<li>ADJACENT_NETWORK 近邻</li>
<li>LOCAL 本地</li>
        :rtype: str
        """
        return self._AccessVector

    @AccessVector.setter
    def AccessVector(self, AccessVector):
        self._AccessVector = AccessVector

    @property
    def AccessComplexity(self):
        r"""AccessComplexity 攻击复杂度。
取值范围：
<li>HIGH 高</li>
<li>MEDIUM 中</li>
<li>LOW 低</li>
        :rtype: str
        """
        return self._AccessComplexity

    @AccessComplexity.setter
    def AccessComplexity(self, AccessComplexity):
        self._AccessComplexity = AccessComplexity

    @property
    def Authentication(self):
        r"""Authentication 身份验证。
取值范围：
<li>MULTIPLE 多系统认证</li>
<li>SINGLE 单系统认证</li>
<li>NONE 无</li>
        :rtype: str
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def ConImpact(self):
        r"""ConfidentialityImpact 机密性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :rtype: str
        """
        return self._ConImpact

    @ConImpact.setter
    def ConImpact(self, ConImpact):
        self._ConImpact = ConImpact

    @property
    def IntegrityImpact(self):
        r"""IntegrityImpact 完整性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :rtype: str
        """
        return self._IntegrityImpact

    @IntegrityImpact.setter
    def IntegrityImpact(self, IntegrityImpact):
        self._IntegrityImpact = IntegrityImpact

    @property
    def AvailabilityImpact(self):
        r"""AvailabilityImpact 可用性影响。
取值范围：
<li>NONE 无</li>
<li>PARTIAL 部分</li>
<li>COMPLETE 完整</li>
        :rtype: str
        """
        return self._AvailabilityImpact

    @AvailabilityImpact.setter
    def AvailabilityImpact(self, AvailabilityImpact):
        self._AvailabilityImpact = AvailabilityImpact


    def _deserialize(self, params):
        self._CVSS = params.get("CVSS")
        self._AccessVector = params.get("AccessVector")
        self._AccessComplexity = params.get("AccessComplexity")
        self._Authentication = params.get("Authentication")
        self._ConImpact = params.get("ConImpact")
        self._IntegrityImpact = params.get("IntegrityImpact")
        self._AvailabilityImpact = params.get("AvailabilityImpact")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVSSV3Info(AbstractModel):
    r"""Cvssv3.0详细信息。

    """

    def __init__(self):
        r"""
        :param _CVSS: CVE评分。
        :type CVSS: float
        :param _AttackVector: AttackVector 攻击途径。
取值范围：
<li>NETWORK 远程</li>
<li>ADJACENT_NETWORK 近邻</li>
<li>LOCAL 本地</li>
<li>PHYSICAL 物理</li>
        :type AttackVector: str
        :param _AttackComplexity: AttackComplexity 攻击复杂度。
取值范围：
<li>HIGH 高</li>
<li>LOW 低</li>
        :type AttackComplexity: str
        :param _PrivilegesRequired: PrivilegesRequired 触发特权。
取值范围：
<li>HIGH 高</li>
<li>LOW 低</li>
<li>NONE 无</li>
        :type PrivilegesRequired: str
        :param _UserInteraction: UserInteraction 交互必要性。
取值范围：
<li>NONE 无</li>
<li>REQUIRED 需要</li>
        :type UserInteraction: str
        :param _Scope: Scope 绕过安全边界。
取值范围：
<li>UNCHANGED 否</li>
<li>CHANGED 能</li>
        :type Scope: str
        :param _ConImpact: ConfidentialityImpact 机密性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :type ConImpact: str
        :param _IntegrityImpact: IntegrityImpact 完整性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :type IntegrityImpact: str
        :param _AvailabilityImpact: AvailabilityImpact 可用性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :type AvailabilityImpact: str
        """
        self._CVSS = None
        self._AttackVector = None
        self._AttackComplexity = None
        self._PrivilegesRequired = None
        self._UserInteraction = None
        self._Scope = None
        self._ConImpact = None
        self._IntegrityImpact = None
        self._AvailabilityImpact = None

    @property
    def CVSS(self):
        r"""CVE评分。
        :rtype: float
        """
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def AttackVector(self):
        r"""AttackVector 攻击途径。
取值范围：
<li>NETWORK 远程</li>
<li>ADJACENT_NETWORK 近邻</li>
<li>LOCAL 本地</li>
<li>PHYSICAL 物理</li>
        :rtype: str
        """
        return self._AttackVector

    @AttackVector.setter
    def AttackVector(self, AttackVector):
        self._AttackVector = AttackVector

    @property
    def AttackComplexity(self):
        r"""AttackComplexity 攻击复杂度。
取值范围：
<li>HIGH 高</li>
<li>LOW 低</li>
        :rtype: str
        """
        return self._AttackComplexity

    @AttackComplexity.setter
    def AttackComplexity(self, AttackComplexity):
        self._AttackComplexity = AttackComplexity

    @property
    def PrivilegesRequired(self):
        r"""PrivilegesRequired 触发特权。
取值范围：
<li>HIGH 高</li>
<li>LOW 低</li>
<li>NONE 无</li>
        :rtype: str
        """
        return self._PrivilegesRequired

    @PrivilegesRequired.setter
    def PrivilegesRequired(self, PrivilegesRequired):
        self._PrivilegesRequired = PrivilegesRequired

    @property
    def UserInteraction(self):
        r"""UserInteraction 交互必要性。
取值范围：
<li>NONE 无</li>
<li>REQUIRED 需要</li>
        :rtype: str
        """
        return self._UserInteraction

    @UserInteraction.setter
    def UserInteraction(self, UserInteraction):
        self._UserInteraction = UserInteraction

    @property
    def Scope(self):
        r"""Scope 绕过安全边界。
取值范围：
<li>UNCHANGED 否</li>
<li>CHANGED 能</li>
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ConImpact(self):
        r"""ConfidentialityImpact 机密性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :rtype: str
        """
        return self._ConImpact

    @ConImpact.setter
    def ConImpact(self, ConImpact):
        self._ConImpact = ConImpact

    @property
    def IntegrityImpact(self):
        r"""IntegrityImpact 完整性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :rtype: str
        """
        return self._IntegrityImpact

    @IntegrityImpact.setter
    def IntegrityImpact(self, IntegrityImpact):
        self._IntegrityImpact = IntegrityImpact

    @property
    def AvailabilityImpact(self):
        r"""AvailabilityImpact 可用性影响。
取值范围：
<li>NONE 无</li>
<li>LOW 低</li>
<li>HIGH 高</li>
        :rtype: str
        """
        return self._AvailabilityImpact

    @AvailabilityImpact.setter
    def AvailabilityImpact(self, AvailabilityImpact):
        self._AvailabilityImpact = AvailabilityImpact


    def _deserialize(self, params):
        self._CVSS = params.get("CVSS")
        self._AttackVector = params.get("AttackVector")
        self._AttackComplexity = params.get("AttackComplexity")
        self._PrivilegesRequired = params.get("PrivilegesRequired")
        self._UserInteraction = params.get("UserInteraction")
        self._Scope = params.get("Scope")
        self._ConImpact = params.get("ConImpact")
        self._IntegrityImpact = params.get("IntegrityImpact")
        self._AvailabilityImpact = params.get("AvailabilityImpact")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Component(AbstractModel):
    r"""描述一个第三方组件的源信息。

    """

    def __init__(self):
        r"""
        :param _PURL: 第三方组件的PURL
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        :param _Homepage: 第三方组件的主页
        :type Homepage: str
        :param _Summary: 第三方组件的简介
        :type Summary: str
        :param _NicknameList: 第三方组件的别名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NicknameList: list of str
        :param _CodeLocationList: 第三方组件的代码位置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeLocationList: list of str
        :param _LicenseExpression: 第三方组件的许可证表达式
        :type LicenseExpression: str
        :param _VersionInfo: 第三方组件的版本信息(如果匹配到版本)
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionInfo: :class:`tencentcloud.bsca.v20210811.models.ComponentVersionInfo`
        :param _LastUpdateTime: 第三方组件的最后更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param _TagList: 第三方组件的类型标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of str
        """
        self._PURL = None
        self._Homepage = None
        self._Summary = None
        self._NicknameList = None
        self._CodeLocationList = None
        self._LicenseExpression = None
        self._VersionInfo = None
        self._LastUpdateTime = None
        self._TagList = None

    @property
    def PURL(self):
        r"""第三方组件的PURL
        :rtype: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        return self._PURL

    @PURL.setter
    def PURL(self, PURL):
        self._PURL = PURL

    @property
    def Homepage(self):
        r"""第三方组件的主页
        :rtype: str
        """
        return self._Homepage

    @Homepage.setter
    def Homepage(self, Homepage):
        self._Homepage = Homepage

    @property
    def Summary(self):
        r"""第三方组件的简介
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def NicknameList(self):
        r"""第三方组件的别名列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._NicknameList

    @NicknameList.setter
    def NicknameList(self, NicknameList):
        self._NicknameList = NicknameList

    @property
    def CodeLocationList(self):
        r"""第三方组件的代码位置列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CodeLocationList

    @CodeLocationList.setter
    def CodeLocationList(self, CodeLocationList):
        self._CodeLocationList = CodeLocationList

    @property
    def LicenseExpression(self):
        r"""第三方组件的许可证表达式
        :rtype: str
        """
        return self._LicenseExpression

    @LicenseExpression.setter
    def LicenseExpression(self, LicenseExpression):
        self._LicenseExpression = LicenseExpression

    @property
    def VersionInfo(self):
        r"""第三方组件的版本信息(如果匹配到版本)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bsca.v20210811.models.ComponentVersionInfo`
        """
        return self._VersionInfo

    @VersionInfo.setter
    def VersionInfo(self, VersionInfo):
        self._VersionInfo = VersionInfo

    @property
    def LastUpdateTime(self):
        r"""第三方组件的最后更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def TagList(self):
        r"""第三方组件的类型标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self._PURL = PURL()
            self._PURL._deserialize(params.get("PURL"))
        self._Homepage = params.get("Homepage")
        self._Summary = params.get("Summary")
        self._NicknameList = params.get("NicknameList")
        self._CodeLocationList = params.get("CodeLocationList")
        self._LicenseExpression = params.get("LicenseExpression")
        if params.get("VersionInfo") is not None:
            self._VersionInfo = ComponentVersionInfo()
            self._VersionInfo._deserialize(params.get("VersionInfo"))
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._TagList = params.get("TagList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentTagFilter(AbstractModel):
    r"""筛选条件，同一个Tag不能同时出现在IncludeTags和ExcludeTags，可能的Tag包括："CopyrightUpdated", "LicenseUpdated", "ContainsVulnerability"

    """

    def __init__(self):
        r"""
        :param _IncludeTags: 包括的Tag

        :type IncludeTags: list of str
        :param _ExcludeTags: 排除的Tag
        :type ExcludeTags: list of str
        """
        self._IncludeTags = None
        self._ExcludeTags = None

    @property
    def IncludeTags(self):
        r"""包括的Tag

        :rtype: list of str
        """
        return self._IncludeTags

    @IncludeTags.setter
    def IncludeTags(self, IncludeTags):
        self._IncludeTags = IncludeTags

    @property
    def ExcludeTags(self):
        r"""排除的Tag
        :rtype: list of str
        """
        return self._ExcludeTags

    @ExcludeTags.setter
    def ExcludeTags(self, ExcludeTags):
        self._ExcludeTags = ExcludeTags


    def _deserialize(self, params):
        self._IncludeTags = params.get("IncludeTags")
        self._ExcludeTags = params.get("ExcludeTags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentVersion(AbstractModel):
    r"""描述一个组件版本。

    """

    def __init__(self):
        r"""
        :param _PURL: 该组件的PURL
注意：此字段可能返回 null，表示取不到有效值。
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        :param _LicenseExpression: 该组件版本的许可证表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseExpression: str
        :param _VersionInfo: 组件的版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionInfo: :class:`tencentcloud.bsca.v20210811.models.ComponentVersionInfo`
        """
        self._PURL = None
        self._LicenseExpression = None
        self._VersionInfo = None

    @property
    def PURL(self):
        r"""该组件的PURL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        return self._PURL

    @PURL.setter
    def PURL(self, PURL):
        self._PURL = PURL

    @property
    def LicenseExpression(self):
        r"""该组件版本的许可证表达式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LicenseExpression

    @LicenseExpression.setter
    def LicenseExpression(self, LicenseExpression):
        self._LicenseExpression = LicenseExpression

    @property
    def VersionInfo(self):
        r"""组件的版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bsca.v20210811.models.ComponentVersionInfo`
        """
        return self._VersionInfo

    @VersionInfo.setter
    def VersionInfo(self, VersionInfo):
        self._VersionInfo = VersionInfo


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self._PURL = PURL()
            self._PURL._deserialize(params.get("PURL"))
        self._LicenseExpression = params.get("LicenseExpression")
        if params.get("VersionInfo") is not None:
            self._VersionInfo = ComponentVersionInfo()
            self._VersionInfo._deserialize(params.get("VersionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentVersionInfo(AbstractModel):
    r"""描述组件版本的详情，包含组件发布时间、Copyright列表、组件描述Tag。

    """

    def __init__(self):
        r"""
        :param _PublishTime: 版本发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishTime: str
        :param _CopyrightList: 当前版本的所有copyright
注意：此字段可能返回 null，表示取不到有效值。
        :type CopyrightList: list of str
        :param _TagList: 版本标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of str
        """
        self._PublishTime = None
        self._CopyrightList = None
        self._TagList = None

    @property
    def PublishTime(self):
        r"""版本发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublishTime

    @PublishTime.setter
    def PublishTime(self, PublishTime):
        self._PublishTime = PublishTime

    @property
    def CopyrightList(self):
        r"""当前版本的所有copyright
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CopyrightList

    @CopyrightList.setter
    def CopyrightList(self, CopyrightList):
        self._CopyrightList = CopyrightList

    @property
    def TagList(self):
        r"""版本标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._PublishTime = params.get("PublishTime")
        self._CopyrightList = params.get("CopyrightList")
        self._TagList = params.get("TagList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentVulnerabilitySummary(AbstractModel):
    r"""与输入组件相关的漏洞信息摘要信息。

    """

    def __init__(self):
        r"""
        :param _PURL: 用于匹配漏洞的PURL
注意：此字段可能返回 null，表示取不到有效值。
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        :param _CanBeFixed: 该组件是否包含修复漏洞的官方补丁
        :type CanBeFixed: bool
        :param _FixedVersion: 修复漏洞的组件版本号
        :type FixedVersion: str
        :param _AffectedVersion: 漏洞影响的组件版本号
        :type AffectedVersion: str
        :param _AffectedComponent: 漏洞影响组件
        :type AffectedComponent: str
        :param _RiskLevel: 漏洞在该产品中的风险等级
<li>Critical</li>
<li>High</li>
<li>Medium</li>
<li>Low</li>
        :type RiskLevel: str
        """
        self._PURL = None
        self._CanBeFixed = None
        self._FixedVersion = None
        self._AffectedVersion = None
        self._AffectedComponent = None
        self._RiskLevel = None

    @property
    def PURL(self):
        r"""用于匹配漏洞的PURL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        return self._PURL

    @PURL.setter
    def PURL(self, PURL):
        self._PURL = PURL

    @property
    def CanBeFixed(self):
        r"""该组件是否包含修复漏洞的官方补丁
        :rtype: bool
        """
        return self._CanBeFixed

    @CanBeFixed.setter
    def CanBeFixed(self, CanBeFixed):
        self._CanBeFixed = CanBeFixed

    @property
    def FixedVersion(self):
        r"""修复漏洞的组件版本号
        :rtype: str
        """
        return self._FixedVersion

    @FixedVersion.setter
    def FixedVersion(self, FixedVersion):
        self._FixedVersion = FixedVersion

    @property
    def AffectedVersion(self):
        r"""漏洞影响的组件版本号
        :rtype: str
        """
        return self._AffectedVersion

    @AffectedVersion.setter
    def AffectedVersion(self, AffectedVersion):
        self._AffectedVersion = AffectedVersion

    @property
    def AffectedComponent(self):
        r"""漏洞影响组件
        :rtype: str
        """
        return self._AffectedComponent

    @AffectedComponent.setter
    def AffectedComponent(self, AffectedComponent):
        self._AffectedComponent = AffectedComponent

    @property
    def RiskLevel(self):
        r"""漏洞在该产品中的风险等级
<li>Critical</li>
<li>High</li>
<li>Medium</li>
<li>Low</li>
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self._PURL = PURL()
            self._PURL._deserialize(params.get("PURL"))
        self._CanBeFixed = params.get("CanBeFixed")
        self._FixedVersion = params.get("FixedVersion")
        self._AffectedVersion = params.get("AffectedVersion")
        self._AffectedComponent = params.get("AffectedComponent")
        self._RiskLevel = params.get("RiskLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentVulnerabilityUnion(AbstractModel):
    r"""描述组件漏洞相关概览信息。

    """

    def __init__(self):
        r"""
        :param _Summary: 漏洞概览信息
        :type Summary: :class:`tencentcloud.bsca.v20210811.models.VulnerabilitySummary`
        :param _SummaryInComponent: 与组件相关的漏洞概览信息
        :type SummaryInComponent: :class:`tencentcloud.bsca.v20210811.models.ComponentVulnerabilitySummary`
        """
        self._Summary = None
        self._SummaryInComponent = None

    @property
    def Summary(self):
        r"""漏洞概览信息
        :rtype: :class:`tencentcloud.bsca.v20210811.models.VulnerabilitySummary`
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def SummaryInComponent(self):
        r"""与组件相关的漏洞概览信息
        :rtype: :class:`tencentcloud.bsca.v20210811.models.ComponentVulnerabilitySummary`
        """
        return self._SummaryInComponent

    @SummaryInComponent.setter
    def SummaryInComponent(self, SummaryInComponent):
        self._SummaryInComponent = SummaryInComponent


    def _deserialize(self, params):
        if params.get("Summary") is not None:
            self._Summary = VulnerabilitySummary()
            self._Summary._deserialize(params.get("Summary"))
        if params.get("SummaryInComponent") is not None:
            self._SummaryInComponent = ComponentVulnerabilitySummary()
            self._SummaryInComponent._deserialize(params.get("SummaryInComponent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBComponentRequest(AbstractModel):
    r"""DescribeKBComponent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PURL: 组件的PURL
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        self._PURL = None

    @property
    def PURL(self):
        r"""组件的PURL
        :rtype: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        return self._PURL

    @PURL.setter
    def PURL(self, PURL):
        self._PURL = PURL


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self._PURL = PURL()
            self._PURL._deserialize(params.get("PURL"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBComponentResponse(AbstractModel):
    r"""DescribeKBComponent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Component: 匹配的组件信息
        :type Component: :class:`tencentcloud.bsca.v20210811.models.Component`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Component = None
        self._RequestId = None

    @property
    def Component(self):
        r"""匹配的组件信息
        :rtype: :class:`tencentcloud.bsca.v20210811.models.Component`
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

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
        if params.get("Component") is not None:
            self._Component = Component()
            self._Component._deserialize(params.get("Component"))
        self._RequestId = params.get("RequestId")


class DescribeKBComponentVersionListRequest(AbstractModel):
    r"""DescribeKBComponentVersionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PURL: 要查询的组件 PURL
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        :param _PageNumber: 页号
        :type PageNumber: int
        :param _PageSize: 页大小
        :type PageSize: int
        :param _Order: 排序方式，可以是"ASC"或"DESC"，默认"DESC"
        :type Order: str
        :param _OrderBy: 排序字段，可能的字段包括“Version”、"PublishTime"
        :type OrderBy: list of str
        :param _Filter: Tag筛选
        :type Filter: :class:`tencentcloud.bsca.v20210811.models.ComponentTagFilter`
        """
        self._PURL = None
        self._PageNumber = None
        self._PageSize = None
        self._Order = None
        self._OrderBy = None
        self._Filter = None

    @property
    def PURL(self):
        r"""要查询的组件 PURL
        :rtype: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        return self._PURL

    @PURL.setter
    def PURL(self, PURL):
        self._PURL = PURL

    @property
    def PageNumber(self):
        r"""页号
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Order(self):
        r"""排序方式，可以是"ASC"或"DESC"，默认"DESC"
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        r"""排序字段，可能的字段包括“Version”、"PublishTime"
        :rtype: list of str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Filter(self):
        r"""Tag筛选
        :rtype: :class:`tencentcloud.bsca.v20210811.models.ComponentTagFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self._PURL = PURL()
            self._PURL._deserialize(params.get("PURL"))
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self._Filter = ComponentTagFilter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBComponentVersionListResponse(AbstractModel):
    r"""DescribeKBComponentVersionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionList: 该组件的版本列表信息
        :type VersionList: list of ComponentVersion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionList = None
        self._RequestId = None

    @property
    def VersionList(self):
        r"""该组件的版本列表信息
        :rtype: list of ComponentVersion
        """
        return self._VersionList

    @VersionList.setter
    def VersionList(self, VersionList):
        self._VersionList = VersionList

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
        if params.get("VersionList") is not None:
            self._VersionList = []
            for item in params.get("VersionList"):
                obj = ComponentVersion()
                obj._deserialize(item)
                self._VersionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKBComponentVulnerabilityRequest(AbstractModel):
    r"""DescribeKBComponentVulnerability请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PURL: 组件的PURL，其中Name和Version为必填字段
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        :param _Language: 语言，ZH或EN
        :type Language: str
        """
        self._PURL = None
        self._Language = None

    @property
    def PURL(self):
        r"""组件的PURL，其中Name和Version为必填字段
        :rtype: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        return self._PURL

    @PURL.setter
    def PURL(self, PURL):
        self._PURL = PURL

    @property
    def Language(self):
        r"""语言，ZH或EN
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        if params.get("PURL") is not None:
            self._PURL = PURL()
            self._PURL._deserialize(params.get("PURL"))
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBComponentVulnerabilityResponse(AbstractModel):
    r"""DescribeKBComponentVulnerability返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VulnerabilityList: 漏洞信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityList: list of ComponentVulnerabilityUnion
        :param _PURL: 组件purl
        :type PURL: :class:`tencentcloud.bsca.v20210811.models.PURL`
        :param _RecommendedVersion: 推荐版本，最小无高危/严重漏洞的版本。无法升级到安全版本时的备选方案。
        :type RecommendedVersion: str
        :param _SecureVersion: 安全版本（首选），最小无漏洞的版本。当无法升级到安全版本时可考虑使用推荐版本。
        :type SecureVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VulnerabilityList = None
        self._PURL = None
        self._RecommendedVersion = None
        self._SecureVersion = None
        self._RequestId = None

    @property
    def VulnerabilityList(self):
        r"""漏洞信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ComponentVulnerabilityUnion
        """
        return self._VulnerabilityList

    @VulnerabilityList.setter
    def VulnerabilityList(self, VulnerabilityList):
        self._VulnerabilityList = VulnerabilityList

    @property
    def PURL(self):
        r"""组件purl
        :rtype: :class:`tencentcloud.bsca.v20210811.models.PURL`
        """
        return self._PURL

    @PURL.setter
    def PURL(self, PURL):
        self._PURL = PURL

    @property
    def RecommendedVersion(self):
        r"""推荐版本，最小无高危/严重漏洞的版本。无法升级到安全版本时的备选方案。
        :rtype: str
        """
        return self._RecommendedVersion

    @RecommendedVersion.setter
    def RecommendedVersion(self, RecommendedVersion):
        self._RecommendedVersion = RecommendedVersion

    @property
    def SecureVersion(self):
        r"""安全版本（首选），最小无漏洞的版本。当无法升级到安全版本时可考虑使用推荐版本。
        :rtype: str
        """
        return self._SecureVersion

    @SecureVersion.setter
    def SecureVersion(self, SecureVersion):
        self._SecureVersion = SecureVersion

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
        if params.get("VulnerabilityList") is not None:
            self._VulnerabilityList = []
            for item in params.get("VulnerabilityList"):
                obj = ComponentVulnerabilityUnion()
                obj._deserialize(item)
                self._VulnerabilityList.append(obj)
        if params.get("PURL") is not None:
            self._PURL = PURL()
            self._PURL._deserialize(params.get("PURL"))
        self._RecommendedVersion = params.get("RecommendedVersion")
        self._SecureVersion = params.get("SecureVersion")
        self._RequestId = params.get("RequestId")


class DescribeKBLicenseRequest(AbstractModel):
    r"""DescribeKBLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseExpression: License表达式
        :type LicenseExpression: str
        """
        self._LicenseExpression = None

    @property
    def LicenseExpression(self):
        r"""License表达式
        :rtype: str
        """
        return self._LicenseExpression

    @LicenseExpression.setter
    def LicenseExpression(self, LicenseExpression):
        self._LicenseExpression = LicenseExpression


    def _deserialize(self, params):
        self._LicenseExpression = params.get("LicenseExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBLicenseResponse(AbstractModel):
    r"""DescribeKBLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseList: 许可证列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseList: list of LicenseUnion
        :param _NormalizedLicenseExpression: 用于匹配的License表达式
        :type NormalizedLicenseExpression: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LicenseList = None
        self._NormalizedLicenseExpression = None
        self._RequestId = None

    @property
    def LicenseList(self):
        r"""许可证列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LicenseUnion
        """
        return self._LicenseList

    @LicenseList.setter
    def LicenseList(self, LicenseList):
        self._LicenseList = LicenseList

    @property
    def NormalizedLicenseExpression(self):
        r"""用于匹配的License表达式
        :rtype: str
        """
        return self._NormalizedLicenseExpression

    @NormalizedLicenseExpression.setter
    def NormalizedLicenseExpression(self, NormalizedLicenseExpression):
        self._NormalizedLicenseExpression = NormalizedLicenseExpression

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
        if params.get("LicenseList") is not None:
            self._LicenseList = []
            for item in params.get("LicenseList"):
                obj = LicenseUnion()
                obj._deserialize(item)
                self._LicenseList.append(obj)
        self._NormalizedLicenseExpression = params.get("NormalizedLicenseExpression")
        self._RequestId = params.get("RequestId")


class DescribeKBVulnerabilityRequest(AbstractModel):
    r"""DescribeKBVulnerability请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CVEID: 根据CVE ID查询（不能与其他参数同时存在）
        :type CVEID: list of str
        :param _VulID: 根据Vul ID查询（不能与其他参数同时存在）
        :type VulID: list of str
        :param _CNVDID: 根据CNVD ID查询（不能与其他参数同时存在）
        :type CNVDID: list of str
        :param _CNNVDID: 根据CNNVD ID查询（不能与其他参数同时存在）
        :type CNNVDID: list of str
        :param _Language: 语言，ZH或EN
        :type Language: str
        """
        self._CVEID = None
        self._VulID = None
        self._CNVDID = None
        self._CNNVDID = None
        self._Language = None

    @property
    def CVEID(self):
        r"""根据CVE ID查询（不能与其他参数同时存在）
        :rtype: list of str
        """
        return self._CVEID

    @CVEID.setter
    def CVEID(self, CVEID):
        self._CVEID = CVEID

    @property
    def VulID(self):
        r"""根据Vul ID查询（不能与其他参数同时存在）
        :rtype: list of str
        """
        return self._VulID

    @VulID.setter
    def VulID(self, VulID):
        self._VulID = VulID

    @property
    def CNVDID(self):
        r"""根据CNVD ID查询（不能与其他参数同时存在）
        :rtype: list of str
        """
        return self._CNVDID

    @CNVDID.setter
    def CNVDID(self, CNVDID):
        self._CNVDID = CNVDID

    @property
    def CNNVDID(self):
        r"""根据CNNVD ID查询（不能与其他参数同时存在）
        :rtype: list of str
        """
        return self._CNNVDID

    @CNNVDID.setter
    def CNNVDID(self, CNNVDID):
        self._CNNVDID = CNNVDID

    @property
    def Language(self):
        r"""语言，ZH或EN
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        self._CVEID = params.get("CVEID")
        self._VulID = params.get("VulID")
        self._CNVDID = params.get("CNVDID")
        self._CNNVDID = params.get("CNNVDID")
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKBVulnerabilityResponse(AbstractModel):
    r"""DescribeKBVulnerability返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VulnerabilityDetailList: 漏洞详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityDetailList: list of VulnerabilityUnion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VulnerabilityDetailList = None
        self._RequestId = None

    @property
    def VulnerabilityDetailList(self):
        r"""漏洞详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VulnerabilityUnion
        """
        return self._VulnerabilityDetailList

    @VulnerabilityDetailList.setter
    def VulnerabilityDetailList(self, VulnerabilityDetailList):
        self._VulnerabilityDetailList = VulnerabilityDetailList

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
        if params.get("VulnerabilityDetailList") is not None:
            self._VulnerabilityDetailList = []
            for item in params.get("VulnerabilityDetailList"):
                obj = VulnerabilityUnion()
                obj._deserialize(item)
                self._VulnerabilityDetailList.append(obj)
        self._RequestId = params.get("RequestId")


class LicenseDetail(AbstractModel):
    r"""描述许可证的详细信息。

    """

    def __init__(self):
        r"""
        :param _Content: 许可证内容
        :type Content: str
        :param _ConditionSet: 许可证允许信息列表
        :type ConditionSet: list of LicenseRestriction
        :param _ForbiddenSet: 许可证要求信息列表
        :type ForbiddenSet: list of LicenseRestriction
        :param _PermissionSet: 许可证禁止信息列表
        :type PermissionSet: list of LicenseRestriction
        """
        self._Content = None
        self._ConditionSet = None
        self._ForbiddenSet = None
        self._PermissionSet = None

    @property
    def Content(self):
        r"""许可证内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ConditionSet(self):
        r"""许可证允许信息列表
        :rtype: list of LicenseRestriction
        """
        return self._ConditionSet

    @ConditionSet.setter
    def ConditionSet(self, ConditionSet):
        self._ConditionSet = ConditionSet

    @property
    def ForbiddenSet(self):
        r"""许可证要求信息列表
        :rtype: list of LicenseRestriction
        """
        return self._ForbiddenSet

    @ForbiddenSet.setter
    def ForbiddenSet(self, ForbiddenSet):
        self._ForbiddenSet = ForbiddenSet

    @property
    def PermissionSet(self):
        r"""许可证禁止信息列表
        :rtype: list of LicenseRestriction
        """
        return self._PermissionSet

    @PermissionSet.setter
    def PermissionSet(self, PermissionSet):
        self._PermissionSet = PermissionSet


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("ConditionSet") is not None:
            self._ConditionSet = []
            for item in params.get("ConditionSet"):
                obj = LicenseRestriction()
                obj._deserialize(item)
                self._ConditionSet.append(obj)
        if params.get("ForbiddenSet") is not None:
            self._ForbiddenSet = []
            for item in params.get("ForbiddenSet"):
                obj = LicenseRestriction()
                obj._deserialize(item)
                self._ForbiddenSet.append(obj)
        if params.get("PermissionSet") is not None:
            self._PermissionSet = []
            for item in params.get("PermissionSet"):
                obj = LicenseRestriction()
                obj._deserialize(item)
                self._PermissionSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseRestriction(AbstractModel):
    r"""License约束信息。

    """

    def __init__(self):
        r"""
        :param _Name: license约束的名称。
        :type Name: str
        :param _Description: license约束的描述。
        :type Description: str
        """
        self._Name = None
        self._Description = None

    @property
    def Name(self):
        r"""license约束的名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""license约束的描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseSummary(AbstractModel):
    r"""描述许可证的概览信息。

    """

    def __init__(self):
        r"""
        :param _Key: 许可证标识符
        :type Key: str
        :param _SPDXKey: 许可证的SPDX标识符，见 https://spdx.org/licenses/
        :type SPDXKey: str
        :param _ShortName: 许可证短名称
        :type ShortName: str
        :param _Name: 许可证完整名称
        :type Name: str
        :param _Risk: License风险等级
<li>NotDefined</li>
<li>LowRisk</li>
<li>MediumRisk</li>
<li>HighRisk</li>
        :type Risk: str
        :param _Source: 许可证来源URL
        :type Source: str
        """
        self._Key = None
        self._SPDXKey = None
        self._ShortName = None
        self._Name = None
        self._Risk = None
        self._Source = None

    @property
    def Key(self):
        r"""许可证标识符
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def SPDXKey(self):
        r"""许可证的SPDX标识符，见 https://spdx.org/licenses/
        :rtype: str
        """
        return self._SPDXKey

    @SPDXKey.setter
    def SPDXKey(self, SPDXKey):
        self._SPDXKey = SPDXKey

    @property
    def ShortName(self):
        r"""许可证短名称
        :rtype: str
        """
        return self._ShortName

    @ShortName.setter
    def ShortName(self, ShortName):
        self._ShortName = ShortName

    @property
    def Name(self):
        r"""许可证完整名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Risk(self):
        r"""License风险等级
<li>NotDefined</li>
<li>LowRisk</li>
<li>MediumRisk</li>
<li>HighRisk</li>
        :rtype: str
        """
        return self._Risk

    @Risk.setter
    def Risk(self, Risk):
        self._Risk = Risk

    @property
    def Source(self):
        r"""许可证来源URL
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._SPDXKey = params.get("SPDXKey")
        self._ShortName = params.get("ShortName")
        self._Name = params.get("Name")
        self._Risk = params.get("Risk")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseUnion(AbstractModel):
    r"""许可证详细信息。

    """

    def __init__(self):
        r"""
        :param _LicenseSummary: 许可证概览信息
        :type LicenseSummary: :class:`tencentcloud.bsca.v20210811.models.LicenseSummary`
        :param _LicenseDetail: 许可证详细信息
        :type LicenseDetail: :class:`tencentcloud.bsca.v20210811.models.LicenseDetail`
        """
        self._LicenseSummary = None
        self._LicenseDetail = None

    @property
    def LicenseSummary(self):
        r"""许可证概览信息
        :rtype: :class:`tencentcloud.bsca.v20210811.models.LicenseSummary`
        """
        return self._LicenseSummary

    @LicenseSummary.setter
    def LicenseSummary(self, LicenseSummary):
        self._LicenseSummary = LicenseSummary

    @property
    def LicenseDetail(self):
        r"""许可证详细信息
        :rtype: :class:`tencentcloud.bsca.v20210811.models.LicenseDetail`
        """
        return self._LicenseDetail

    @LicenseDetail.setter
    def LicenseDetail(self, LicenseDetail):
        self._LicenseDetail = LicenseDetail


    def _deserialize(self, params):
        if params.get("LicenseSummary") is not None:
            self._LicenseSummary = LicenseSummary()
            self._LicenseSummary._deserialize(params.get("LicenseSummary"))
        if params.get("LicenseDetail") is not None:
            self._LicenseDetail = LicenseDetail()
            self._LicenseDetail._deserialize(params.get("LicenseDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchKBPURLListRequest(AbstractModel):
    r"""MatchKBPURLList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SHA1: SHA1。
        :type SHA1: str
        """
        self._SHA1 = None

    @property
    def SHA1(self):
        r"""SHA1。
        :rtype: str
        """
        return self._SHA1

    @SHA1.setter
    def SHA1(self, SHA1):
        self._SHA1 = SHA1


    def _deserialize(self, params):
        self._SHA1 = params.get("SHA1")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchKBPURLListResponse(AbstractModel):
    r"""MatchKBPURLList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PURLList: 组件列表。
        :type PURLList: list of PURL
        :param _Hit: 是否命中数据库。
        :type Hit: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PURLList = None
        self._Hit = None
        self._RequestId = None

    @property
    def PURLList(self):
        r"""组件列表。
        :rtype: list of PURL
        """
        return self._PURLList

    @PURLList.setter
    def PURLList(self, PURLList):
        self._PURLList = PURLList

    @property
    def Hit(self):
        r"""是否命中数据库。
        :rtype: bool
        """
        return self._Hit

    @Hit.setter
    def Hit(self, Hit):
        self._Hit = Hit

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
        if params.get("PURLList") is not None:
            self._PURLList = []
            for item in params.get("PURLList"):
                obj = PURL()
                obj._deserialize(item)
                self._PURLList.append(obj)
        self._Hit = params.get("Hit")
        self._RequestId = params.get("RequestId")


class PURL(AbstractModel):
    r"""PURL(Package URL)用于定位一个产品或组件，见 https://github.com/package-url/purl-spec。

    """

    def __init__(self):
        r"""
        :param _Name: 组件名称
        :type Name: str
        :param _Protocol: 组件所属的类型，如：github, gitlab, generic, deb, rpm, maven 等
        :type Protocol: str
        :param _Namespace: 组件名的前缀名，如github和gitlab的用户名，deb的操作系统，maven包的group id等
        :type Namespace: str
        :param _Qualifiers: 修饰组件的额外属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Qualifiers: list of Qualifier
        :param _Subpath: 相对于组件包根位置的子目录
        :type Subpath: str
        :param _Version: 组件版本号
        :type Version: str
        """
        self._Name = None
        self._Protocol = None
        self._Namespace = None
        self._Qualifiers = None
        self._Subpath = None
        self._Version = None

    @property
    def Name(self):
        r"""组件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        r"""组件所属的类型，如：github, gitlab, generic, deb, rpm, maven 等
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Namespace(self):
        r"""组件名的前缀名，如github和gitlab的用户名，deb的操作系统，maven包的group id等
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifiers(self):
        r"""修饰组件的额外属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Qualifier
        """
        return self._Qualifiers

    @Qualifiers.setter
    def Qualifiers(self, Qualifiers):
        self._Qualifiers = Qualifiers

    @property
    def Subpath(self):
        r"""相对于组件包根位置的子目录
        :rtype: str
        """
        return self._Subpath

    @Subpath.setter
    def Subpath(self, Subpath):
        self._Subpath = Subpath

    @property
    def Version(self):
        r"""组件版本号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        self._Namespace = params.get("Namespace")
        if params.get("Qualifiers") is not None:
            self._Qualifiers = []
            for item in params.get("Qualifiers"):
                obj = Qualifier()
                obj._deserialize(item)
                self._Qualifiers.append(obj)
        self._Subpath = params.get("Subpath")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Qualifier(AbstractModel):
    r"""PURL下的Qualifier属性类型，用于定义第三方组件的额外属性，见 https://github.com/package-url/purl-spec。

    """

    def __init__(self):
        r"""
        :param _Key: 额外属性的名称。
        :type Key: str
        :param _Value: 额外属性的值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""额外属性的名称。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""额外属性的值。
        :rtype: str
        """
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
        


class SearchKBComponentRequest(AbstractModel):
    r"""SearchKBComponent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 需要搜索的组件名
        :type Query: str
        :param _Protocol: 需要搜索的组件类型
        :type Protocol: str
        :param _PageNumber: 分页参数，从 0 开始
        :type PageNumber: int
        :param _PageSize: 分页参数，设置每页返回的结果数量
        :type PageSize: int
        """
        self._Query = None
        self._Protocol = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Query(self):
        r"""需要搜索的组件名
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Protocol(self):
        r"""需要搜索的组件类型
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PageNumber(self):
        r"""分页参数，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页参数，设置每页返回的结果数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Protocol = params.get("Protocol")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKBComponentResponse(AbstractModel):
    r"""SearchKBComponent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ComponentList: 满足搜索条件的组件列表
        :type ComponentList: list of Component
        :param _Total: 满足搜索条件的总个数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ComponentList = None
        self._Total = None
        self._RequestId = None

    @property
    def ComponentList(self):
        r"""满足搜索条件的组件列表
        :rtype: list of Component
        """
        return self._ComponentList

    @ComponentList.setter
    def ComponentList(self, ComponentList):
        self._ComponentList = ComponentList

    @property
    def Total(self):
        r"""满足搜索条件的总个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("ComponentList") is not None:
            self._ComponentList = []
            for item in params.get("ComponentList"):
                obj = Component()
                obj._deserialize(item)
                self._ComponentList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class VulnerabilityDetail(AbstractModel):
    r"""描述漏洞详细信息。

    """

    def __init__(self):
        r"""
        :param _Category: 漏洞类别
        :type Category: str
        :param _CategoryType: 漏洞分类
        :type CategoryType: str
        :param _Description: 漏洞描述
        :type Description: str
        :param _OfficialSolution: 漏洞官方解决方案
        :type OfficialSolution: str
        :param _ReferenceList: 漏洞信息参考列表
        :type ReferenceList: list of str
        :param _DefenseSolution: 漏洞防御方案
        :type DefenseSolution: str
        :param _CVSSv2Info: 漏洞CVSSv2信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSv2Info: :class:`tencentcloud.bsca.v20210811.models.CVSSV2Info`
        :param _CVSSv3Info: 漏洞CVSSv3信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSSv3Info: :class:`tencentcloud.bsca.v20210811.models.CVSSV3Info`
        :param _SubmitTime: 漏洞提交时间
        :type SubmitTime: str
        :param _UpdateTime: 漏洞更新时间
        :type UpdateTime: str
        :param _CWEID: CWE编号
        :type CWEID: str
        :param _CVSSv2Vector: 漏洞CVSSv2向量
        :type CVSSv2Vector: str
        :param _CVSSv3Vector: 漏洞CVSSv3向量
        :type CVSSv3Vector: str
        :param _AffectedComponentList: 漏洞影响的组件列表，仅当查询单个漏洞时有效
        :type AffectedComponentList: list of AffectedComponent
        """
        self._Category = None
        self._CategoryType = None
        self._Description = None
        self._OfficialSolution = None
        self._ReferenceList = None
        self._DefenseSolution = None
        self._CVSSv2Info = None
        self._CVSSv3Info = None
        self._SubmitTime = None
        self._UpdateTime = None
        self._CWEID = None
        self._CVSSv2Vector = None
        self._CVSSv3Vector = None
        self._AffectedComponentList = None

    @property
    def Category(self):
        r"""漏洞类别
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def CategoryType(self):
        r"""漏洞分类
        :rtype: str
        """
        return self._CategoryType

    @CategoryType.setter
    def CategoryType(self, CategoryType):
        self._CategoryType = CategoryType

    @property
    def Description(self):
        r"""漏洞描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OfficialSolution(self):
        r"""漏洞官方解决方案
        :rtype: str
        """
        return self._OfficialSolution

    @OfficialSolution.setter
    def OfficialSolution(self, OfficialSolution):
        self._OfficialSolution = OfficialSolution

    @property
    def ReferenceList(self):
        r"""漏洞信息参考列表
        :rtype: list of str
        """
        return self._ReferenceList

    @ReferenceList.setter
    def ReferenceList(self, ReferenceList):
        self._ReferenceList = ReferenceList

    @property
    def DefenseSolution(self):
        r"""漏洞防御方案
        :rtype: str
        """
        return self._DefenseSolution

    @DefenseSolution.setter
    def DefenseSolution(self, DefenseSolution):
        self._DefenseSolution = DefenseSolution

    @property
    def CVSSv2Info(self):
        r"""漏洞CVSSv2信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bsca.v20210811.models.CVSSV2Info`
        """
        return self._CVSSv2Info

    @CVSSv2Info.setter
    def CVSSv2Info(self, CVSSv2Info):
        self._CVSSv2Info = CVSSv2Info

    @property
    def CVSSv3Info(self):
        r"""漏洞CVSSv3信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bsca.v20210811.models.CVSSV3Info`
        """
        return self._CVSSv3Info

    @CVSSv3Info.setter
    def CVSSv3Info(self, CVSSv3Info):
        self._CVSSv3Info = CVSSv3Info

    @property
    def SubmitTime(self):
        r"""漏洞提交时间
        :rtype: str
        """
        return self._SubmitTime

    @SubmitTime.setter
    def SubmitTime(self, SubmitTime):
        self._SubmitTime = SubmitTime

    @property
    def UpdateTime(self):
        r"""漏洞更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CWEID(self):
        r"""CWE编号
        :rtype: str
        """
        return self._CWEID

    @CWEID.setter
    def CWEID(self, CWEID):
        self._CWEID = CWEID

    @property
    def CVSSv2Vector(self):
        r"""漏洞CVSSv2向量
        :rtype: str
        """
        return self._CVSSv2Vector

    @CVSSv2Vector.setter
    def CVSSv2Vector(self, CVSSv2Vector):
        self._CVSSv2Vector = CVSSv2Vector

    @property
    def CVSSv3Vector(self):
        r"""漏洞CVSSv3向量
        :rtype: str
        """
        return self._CVSSv3Vector

    @CVSSv3Vector.setter
    def CVSSv3Vector(self, CVSSv3Vector):
        self._CVSSv3Vector = CVSSv3Vector

    @property
    def AffectedComponentList(self):
        r"""漏洞影响的组件列表，仅当查询单个漏洞时有效
        :rtype: list of AffectedComponent
        """
        return self._AffectedComponentList

    @AffectedComponentList.setter
    def AffectedComponentList(self, AffectedComponentList):
        self._AffectedComponentList = AffectedComponentList


    def _deserialize(self, params):
        self._Category = params.get("Category")
        self._CategoryType = params.get("CategoryType")
        self._Description = params.get("Description")
        self._OfficialSolution = params.get("OfficialSolution")
        self._ReferenceList = params.get("ReferenceList")
        self._DefenseSolution = params.get("DefenseSolution")
        if params.get("CVSSv2Info") is not None:
            self._CVSSv2Info = CVSSV2Info()
            self._CVSSv2Info._deserialize(params.get("CVSSv2Info"))
        if params.get("CVSSv3Info") is not None:
            self._CVSSv3Info = CVSSV3Info()
            self._CVSSv3Info._deserialize(params.get("CVSSv3Info"))
        self._SubmitTime = params.get("SubmitTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CWEID = params.get("CWEID")
        self._CVSSv2Vector = params.get("CVSSv2Vector")
        self._CVSSv3Vector = params.get("CVSSv3Vector")
        if params.get("AffectedComponentList") is not None:
            self._AffectedComponentList = []
            for item in params.get("AffectedComponentList"):
                obj = AffectedComponent()
                obj._deserialize(item)
                self._AffectedComponentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulnerabilitySummary(AbstractModel):
    r"""描述漏洞的摘要信息。

    """

    def __init__(self):
        r"""
        :param _VulID: 漏洞ID
        :type VulID: str
        :param _CVEID: 漏洞所属CVE编号
        :type CVEID: str
        :param _CNVDID: 漏洞所属CNVD编号
        :type CNVDID: str
        :param _CNNVDID: 漏洞所属CNNVD编号
        :type CNNVDID: str
        :param _Name: 漏洞名称
        :type Name: str
        :param _IsSuggest: 该漏洞是否是需重点关注的漏洞
        :type IsSuggest: bool
        :param _Severity: 漏洞风险等级
<li>Critical</li>
<li>High</li>
<li>Medium</li>
<li>Low</li>
        :type Severity: str
        :param _Architecture: 架构信息，如x86、ARM等，废弃，请使用ArchitectureList
注意：此字段可能返回 null，表示取不到有效值。
        :type Architecture: list of str
        :param _ArchitectureList: 架构信息，如x86、ARM等
注意：此字段可能返回 null，表示取不到有效值。
        :type ArchitectureList: list of str
        :param _PatchUrlList: patch链接
注意：此字段可能返回 null，表示取不到有效值。
        :type PatchUrlList: list of str
        """
        self._VulID = None
        self._CVEID = None
        self._CNVDID = None
        self._CNNVDID = None
        self._Name = None
        self._IsSuggest = None
        self._Severity = None
        self._Architecture = None
        self._ArchitectureList = None
        self._PatchUrlList = None

    @property
    def VulID(self):
        r"""漏洞ID
        :rtype: str
        """
        return self._VulID

    @VulID.setter
    def VulID(self, VulID):
        self._VulID = VulID

    @property
    def CVEID(self):
        r"""漏洞所属CVE编号
        :rtype: str
        """
        return self._CVEID

    @CVEID.setter
    def CVEID(self, CVEID):
        self._CVEID = CVEID

    @property
    def CNVDID(self):
        r"""漏洞所属CNVD编号
        :rtype: str
        """
        return self._CNVDID

    @CNVDID.setter
    def CNVDID(self, CNVDID):
        self._CNVDID = CNVDID

    @property
    def CNNVDID(self):
        r"""漏洞所属CNNVD编号
        :rtype: str
        """
        return self._CNNVDID

    @CNNVDID.setter
    def CNNVDID(self, CNNVDID):
        self._CNNVDID = CNNVDID

    @property
    def Name(self):
        r"""漏洞名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsSuggest(self):
        r"""该漏洞是否是需重点关注的漏洞
        :rtype: bool
        """
        return self._IsSuggest

    @IsSuggest.setter
    def IsSuggest(self, IsSuggest):
        self._IsSuggest = IsSuggest

    @property
    def Severity(self):
        r"""漏洞风险等级
<li>Critical</li>
<li>High</li>
<li>Medium</li>
<li>Low</li>
        :rtype: str
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def Architecture(self):
        warnings.warn("parameter `Architecture` is deprecated", DeprecationWarning) 

        r"""架构信息，如x86、ARM等，废弃，请使用ArchitectureList
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        warnings.warn("parameter `Architecture` is deprecated", DeprecationWarning) 

        self._Architecture = Architecture

    @property
    def ArchitectureList(self):
        r"""架构信息，如x86、ARM等
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ArchitectureList

    @ArchitectureList.setter
    def ArchitectureList(self, ArchitectureList):
        self._ArchitectureList = ArchitectureList

    @property
    def PatchUrlList(self):
        r"""patch链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PatchUrlList

    @PatchUrlList.setter
    def PatchUrlList(self, PatchUrlList):
        self._PatchUrlList = PatchUrlList


    def _deserialize(self, params):
        self._VulID = params.get("VulID")
        self._CVEID = params.get("CVEID")
        self._CNVDID = params.get("CNVDID")
        self._CNNVDID = params.get("CNNVDID")
        self._Name = params.get("Name")
        self._IsSuggest = params.get("IsSuggest")
        self._Severity = params.get("Severity")
        self._Architecture = params.get("Architecture")
        self._ArchitectureList = params.get("ArchitectureList")
        self._PatchUrlList = params.get("PatchUrlList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulnerabilityUnion(AbstractModel):
    r"""描述漏洞的详细信息。

    """

    def __init__(self):
        r"""
        :param _Summary: 漏洞概览信息
        :type Summary: :class:`tencentcloud.bsca.v20210811.models.VulnerabilitySummary`
        :param _Detail: 漏洞详细信息
        :type Detail: :class:`tencentcloud.bsca.v20210811.models.VulnerabilityDetail`
        """
        self._Summary = None
        self._Detail = None

    @property
    def Summary(self):
        r"""漏洞概览信息
        :rtype: :class:`tencentcloud.bsca.v20210811.models.VulnerabilitySummary`
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Detail(self):
        r"""漏洞详细信息
        :rtype: :class:`tencentcloud.bsca.v20210811.models.VulnerabilityDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        if params.get("Summary") is not None:
            self._Summary = VulnerabilitySummary()
            self._Summary._deserialize(params.get("Summary"))
        if params.get("Detail") is not None:
            self._Detail = VulnerabilityDetail()
            self._Detail._deserialize(params.get("Detail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        