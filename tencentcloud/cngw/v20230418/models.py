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


class AIGWACLSubject(AbstractModel):
    r"""AI 网关 ACL 授权主体（Consumer / ConsumerGroup 共用结构），用于响应中回显 Id + Name，减少前端多次查询调用

    """

    def __init__(self):
        r"""
        :param _Id: <p>鉴权主体ID</p>
        :type Id: str
        :param _Name: <p>鉴权主体名称</p>
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        r"""<p>鉴权主体ID</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""<p>鉴权主体名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWCacheAwareRouteCandidate(AbstractModel):
    r"""缓存感知路由候选模型服务

    """

    def __init__(self):
        r"""
        :param _ModelServiceId: <p>模型服务ID</p>
        :type ModelServiceId: str
        :param _ModelServiceName: <p>模型服务名称</p>
        :type ModelServiceName: str
        """
        self._ModelServiceId = None
        self._ModelServiceName = None

    @property
    def ModelServiceId(self):
        r"""<p>模型服务ID</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId

    @property
    def ModelServiceName(self):
        r"""<p>模型服务名称</p>
        :rtype: str
        """
        return self._ModelServiceName

    @ModelServiceName.setter
    def ModelServiceName(self, ModelServiceName):
        self._ModelServiceName = ModelServiceName


    def _deserialize(self, params):
        self._ModelServiceId = params.get("ModelServiceId")
        self._ModelServiceName = params.get("ModelServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWCacheAwareRouteConfig(AbstractModel):
    r"""缓存感知路由

    """

    def __init__(self):
        r"""
        :param _Candidates: <p>前缀缓存感知路由模型服务列表</p>
        :type Candidates: list of AIGWCacheAwareRouteCandidate
        """
        self._Candidates = None

    @property
    def Candidates(self):
        r"""<p>前缀缓存感知路由模型服务列表</p>
        :rtype: list of AIGWCacheAwareRouteCandidate
        """
        return self._Candidates

    @Candidates.setter
    def Candidates(self, Candidates):
        self._Candidates = Candidates


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self._Candidates = []
            for item in params.get("Candidates"):
                obj = AIGWCacheAwareRouteCandidate()
                obj._deserialize(item)
                self._Candidates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWConsumerGroupBrief(AbstractModel):
    r"""AI 网关中消费者组简要信息

    """

    def __init__(self):
        r"""
        :param _Name: <p>消费者组名称</p>
        :type Name: str
        :param _ConsumerGroupId: <p>消费者组Id</p>
        :type ConsumerGroupId: str
        """
        self._Name = None
        self._ConsumerGroupId = None

    @property
    def Name(self):
        r"""<p>消费者组名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ConsumerGroupId(self):
        r"""<p>消费者组Id</p>
        :rtype: str
        """
        return self._ConsumerGroupId

    @ConsumerGroupId.setter
    def ConsumerGroupId(self, ConsumerGroupId):
        self._ConsumerGroupId = ConsumerGroupId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ConsumerGroupId = params.get("ConsumerGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWCrossServiceFallbackConfig(AbstractModel):
    r"""跨服务降级配置

    """

    def __init__(self):
        r"""
        :param _TriggerConditions: <p>触发条件</p><p>枚举值：</p><ul><li>ServiceUnavailable： 服务不可用</li><li>ConnectionTimeout： 连接超时</li><li>RateLimited： 限流</li></ul>
        :type TriggerConditions: list of str
        :param _FallbackServiceChain: <p>fallback 服务链</p>
        :type FallbackServiceChain: list of AIGWFallbackServiceItem
        :param _QuotaFallbackTrigger: <p>额度降级触发配置</p>
        :type QuotaFallbackTrigger: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMQuotaFallbackTrigger`
        """
        self._TriggerConditions = None
        self._FallbackServiceChain = None
        self._QuotaFallbackTrigger = None

    @property
    def TriggerConditions(self):
        r"""<p>触发条件</p><p>枚举值：</p><ul><li>ServiceUnavailable： 服务不可用</li><li>ConnectionTimeout： 连接超时</li><li>RateLimited： 限流</li></ul>
        :rtype: list of str
        """
        return self._TriggerConditions

    @TriggerConditions.setter
    def TriggerConditions(self, TriggerConditions):
        self._TriggerConditions = TriggerConditions

    @property
    def FallbackServiceChain(self):
        r"""<p>fallback 服务链</p>
        :rtype: list of AIGWFallbackServiceItem
        """
        return self._FallbackServiceChain

    @FallbackServiceChain.setter
    def FallbackServiceChain(self, FallbackServiceChain):
        self._FallbackServiceChain = FallbackServiceChain

    @property
    def QuotaFallbackTrigger(self):
        r"""<p>额度降级触发配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMQuotaFallbackTrigger`
        """
        return self._QuotaFallbackTrigger

    @QuotaFallbackTrigger.setter
    def QuotaFallbackTrigger(self, QuotaFallbackTrigger):
        self._QuotaFallbackTrigger = QuotaFallbackTrigger


    def _deserialize(self, params):
        self._TriggerConditions = params.get("TriggerConditions")
        if params.get("FallbackServiceChain") is not None:
            self._FallbackServiceChain = []
            for item in params.get("FallbackServiceChain"):
                obj = AIGWFallbackServiceItem()
                obj._deserialize(item)
                self._FallbackServiceChain.append(obj)
        if params.get("QuotaFallbackTrigger") is not None:
            self._QuotaFallbackTrigger = AIGWLLMQuotaFallbackTrigger()
            self._QuotaFallbackTrigger._deserialize(params.get("QuotaFallbackTrigger"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWCustomDesensitizeRule(AbstractModel):
    r"""AI 网关自定义脱敏规则（A 层 / B 层共用结构体，MaskFormat 含义随所属层不同）

    """

    def __init__(self):
        r"""
        :param _Name: <p>自定义脱敏规则名称</p>
        :type Name: str
        :param _Pattern: <p>自定义脱敏规则匹配正则</p>
        :type Pattern: str
        :param _MaskFormat: <p>自定义脱敏规则掩码</p>
        :type MaskFormat: str
        :param _Enabled: <p>自定义脱敏规则开关</p>
        :type Enabled: bool
        """
        self._Name = None
        self._Pattern = None
        self._MaskFormat = None
        self._Enabled = None

    @property
    def Name(self):
        r"""<p>自定义脱敏规则名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Pattern(self):
        r"""<p>自定义脱敏规则匹配正则</p>
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def MaskFormat(self):
        r"""<p>自定义脱敏规则掩码</p>
        :rtype: str
        """
        return self._MaskFormat

    @MaskFormat.setter
    def MaskFormat(self, MaskFormat):
        self._MaskFormat = MaskFormat

    @property
    def Enabled(self):
        r"""<p>自定义脱敏规则开关</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Pattern = params.get("Pattern")
        self._MaskFormat = params.get("MaskFormat")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWFallbackServiceItem(AbstractModel):
    r"""降级服务元素

    """

    def __init__(self):
        r"""
        :param _ModelServiceId: <p>模型服务 Id</p>
        :type ModelServiceId: str
        :param _ModelServiceName: <p>模型服务名</p>
        :type ModelServiceName: str
        """
        self._ModelServiceId = None
        self._ModelServiceName = None

    @property
    def ModelServiceId(self):
        r"""<p>模型服务 Id</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId

    @property
    def ModelServiceName(self):
        r"""<p>模型服务名</p>
        :rtype: str
        """
        return self._ModelServiceName

    @ModelServiceName.setter
    def ModelServiceName(self, ModelServiceName):
        self._ModelServiceName = ModelServiceName


    def _deserialize(self, params):
        self._ModelServiceId = params.get("ModelServiceId")
        self._ModelServiceName = params.get("ModelServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWForwardDesensitizeConfig(AbstractModel):
    r"""AI 网关 A 层转发脱敏配置（请求转发到 LLM 供应商前对 messages 替换为占位符）

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>转发脱敏开关</p>
        :type Enabled: bool
        :param _PredefinedRuleTypes: <p>预定义规则类型</p><p>枚举值：</p><ul><li>Phone： 电话号码</li><li>IdCard： 身份证号</li><li>BankCard： 银行卡号</li><li>Email： 电子邮箱地址</li><li>IP： IP地址</li><li>Name： 姓名</li></ul>
        :type PredefinedRuleTypes: list of str
        :param _CustomRules: <p>自定义脱敏规则</p>
        :type CustomRules: list of AIGWCustomDesensitizeRule
        :param _PlaceholderFormat: <p>掩码</p>
        :type PlaceholderFormat: str
        :param _OnFailure: <p>脱敏异常处理</p><p>枚举值：</p><ul><li>Reject： 拒绝请求</li><li>Skip： 跳过</li></ul>
        :type OnFailure: str
        """
        self._Enabled = None
        self._PredefinedRuleTypes = None
        self._CustomRules = None
        self._PlaceholderFormat = None
        self._OnFailure = None

    @property
    def Enabled(self):
        r"""<p>转发脱敏开关</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def PredefinedRuleTypes(self):
        r"""<p>预定义规则类型</p><p>枚举值：</p><ul><li>Phone： 电话号码</li><li>IdCard： 身份证号</li><li>BankCard： 银行卡号</li><li>Email： 电子邮箱地址</li><li>IP： IP地址</li><li>Name： 姓名</li></ul>
        :rtype: list of str
        """
        return self._PredefinedRuleTypes

    @PredefinedRuleTypes.setter
    def PredefinedRuleTypes(self, PredefinedRuleTypes):
        self._PredefinedRuleTypes = PredefinedRuleTypes

    @property
    def CustomRules(self):
        r"""<p>自定义脱敏规则</p>
        :rtype: list of AIGWCustomDesensitizeRule
        """
        return self._CustomRules

    @CustomRules.setter
    def CustomRules(self, CustomRules):
        self._CustomRules = CustomRules

    @property
    def PlaceholderFormat(self):
        r"""<p>掩码</p>
        :rtype: str
        """
        return self._PlaceholderFormat

    @PlaceholderFormat.setter
    def PlaceholderFormat(self, PlaceholderFormat):
        self._PlaceholderFormat = PlaceholderFormat

    @property
    def OnFailure(self):
        r"""<p>脱敏异常处理</p><p>枚举值：</p><ul><li>Reject： 拒绝请求</li><li>Skip： 跳过</li></ul>
        :rtype: str
        """
        return self._OnFailure

    @OnFailure.setter
    def OnFailure(self, OnFailure):
        self._OnFailure = OnFailure


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._PredefinedRuleTypes = params.get("PredefinedRuleTypes")
        if params.get("CustomRules") is not None:
            self._CustomRules = []
            for item in params.get("CustomRules"):
                obj = AIGWCustomDesensitizeRule()
                obj._deserialize(item)
                self._CustomRules.append(obj)
        self._PlaceholderFormat = params.get("PlaceholderFormat")
        self._OnFailure = params.get("OnFailure")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWHealthCheckSetting(AbstractModel):
    r"""用于定义kong插件自定义健康检查的配置

    """

    def __init__(self):
        r"""
        :param _HealthCheckType: <p>健康检查类型</p><p>枚举值：</p><ul><li>MCP： 标准mcp</li><li>HTTP： http</li></ul>
        :type HealthCheckType: str
        :param _HealthCheckIntervalSecond: <p>检查间隔</p>
        :type HealthCheckIntervalSecond: int
        :param _HealthCheckTimeout: <p>检查超时时间</p>
        :type HealthCheckTimeout: int
        :param _HealthCheckFailThreshold: <p>检查失败阈值</p>
        :type HealthCheckFailThreshold: int
        :param _HealthCheckRecoverThreshold: <p>检查恢复阈值</p>
        :type HealthCheckRecoverThreshold: int
        :param _HealthCheckPath: <p>检查路径</p>
        :type HealthCheckPath: str
        :param _HealthCheckMethod: <p>检查方法</p>
        :type HealthCheckMethod: str
        """
        self._HealthCheckType = None
        self._HealthCheckIntervalSecond = None
        self._HealthCheckTimeout = None
        self._HealthCheckFailThreshold = None
        self._HealthCheckRecoverThreshold = None
        self._HealthCheckPath = None
        self._HealthCheckMethod = None

    @property
    def HealthCheckType(self):
        r"""<p>健康检查类型</p><p>枚举值：</p><ul><li>MCP： 标准mcp</li><li>HTTP： http</li></ul>
        :rtype: str
        """
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def HealthCheckIntervalSecond(self):
        r"""<p>检查间隔</p>
        :rtype: int
        """
        return self._HealthCheckIntervalSecond

    @HealthCheckIntervalSecond.setter
    def HealthCheckIntervalSecond(self, HealthCheckIntervalSecond):
        self._HealthCheckIntervalSecond = HealthCheckIntervalSecond

    @property
    def HealthCheckTimeout(self):
        r"""<p>检查超时时间</p>
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckFailThreshold(self):
        r"""<p>检查失败阈值</p>
        :rtype: int
        """
        return self._HealthCheckFailThreshold

    @HealthCheckFailThreshold.setter
    def HealthCheckFailThreshold(self, HealthCheckFailThreshold):
        self._HealthCheckFailThreshold = HealthCheckFailThreshold

    @property
    def HealthCheckRecoverThreshold(self):
        r"""<p>检查恢复阈值</p>
        :rtype: int
        """
        return self._HealthCheckRecoverThreshold

    @HealthCheckRecoverThreshold.setter
    def HealthCheckRecoverThreshold(self, HealthCheckRecoverThreshold):
        self._HealthCheckRecoverThreshold = HealthCheckRecoverThreshold

    @property
    def HealthCheckPath(self):
        r"""<p>检查路径</p>
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckMethod(self):
        r"""<p>检查方法</p>
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod


    def _deserialize(self, params):
        self._HealthCheckType = params.get("HealthCheckType")
        self._HealthCheckIntervalSecond = params.get("HealthCheckIntervalSecond")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckFailThreshold = params.get("HealthCheckFailThreshold")
        self._HealthCheckRecoverThreshold = params.get("HealthCheckRecoverThreshold")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWIntentRoute(AbstractModel):
    r"""AI 网关意图路由配置

    """

    def __init__(self):
        r"""
        :param _IntentModelServiceId: <p>意图识别模型id</p>
        :type IntentModelServiceId: str
        :param _ConfidenceThreshold: <p>置信度</p>
        :type ConfidenceThreshold: float
        :param _DefaultModelServiceId: <p>默认服务id</p>
        :type DefaultModelServiceId: str
        :param _Rules: <p>规则</p>
        :type Rules: list of AIGWIntentRouteRule
        """
        self._IntentModelServiceId = None
        self._ConfidenceThreshold = None
        self._DefaultModelServiceId = None
        self._Rules = None

    @property
    def IntentModelServiceId(self):
        r"""<p>意图识别模型id</p>
        :rtype: str
        """
        return self._IntentModelServiceId

    @IntentModelServiceId.setter
    def IntentModelServiceId(self, IntentModelServiceId):
        self._IntentModelServiceId = IntentModelServiceId

    @property
    def ConfidenceThreshold(self):
        r"""<p>置信度</p>
        :rtype: float
        """
        return self._ConfidenceThreshold

    @ConfidenceThreshold.setter
    def ConfidenceThreshold(self, ConfidenceThreshold):
        self._ConfidenceThreshold = ConfidenceThreshold

    @property
    def DefaultModelServiceId(self):
        r"""<p>默认服务id</p>
        :rtype: str
        """
        return self._DefaultModelServiceId

    @DefaultModelServiceId.setter
    def DefaultModelServiceId(self, DefaultModelServiceId):
        self._DefaultModelServiceId = DefaultModelServiceId

    @property
    def Rules(self):
        r"""<p>规则</p>
        :rtype: list of AIGWIntentRouteRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._IntentModelServiceId = params.get("IntentModelServiceId")
        self._ConfidenceThreshold = params.get("ConfidenceThreshold")
        self._DefaultModelServiceId = params.get("DefaultModelServiceId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = AIGWIntentRouteRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWIntentRouteRule(AbstractModel):
    r"""AI 网关意图路由规则

    """

    def __init__(self):
        r"""
        :param _IntentCode: <p>意图编码</p><p>枚举值：</p><ul><li>Coder： 代码编写</li><li>Math： 数学计算</li><li>Translation： 翻译</li><li>Flash： 快速问答</li><li>Complex： 复杂推理</li></ul>
        :type IntentCode: str
        :param _ModelServiceId: <p>模型服务id</p>
        :type ModelServiceId: str
        """
        self._IntentCode = None
        self._ModelServiceId = None

    @property
    def IntentCode(self):
        r"""<p>意图编码</p><p>枚举值：</p><ul><li>Coder： 代码编写</li><li>Math： 数学计算</li><li>Translation： 翻译</li><li>Flash： 快速问答</li><li>Complex： 复杂推理</li></ul>
        :rtype: str
        """
        return self._IntentCode

    @IntentCode.setter
    def IntentCode(self, IntentCode):
        self._IntentCode = IntentCode

    @property
    def ModelServiceId(self):
        r"""<p>模型服务id</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId


    def _deserialize(self, params):
        self._IntentCode = params.get("IntentCode")
        self._ModelServiceId = params.get("ModelServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWJWTAuthPluginConfig(AbstractModel):
    r"""JWT 认证插件配置

    """

    def __init__(self):
        r"""
        :param _HeaderNames: <p>签名的header名称列表</p>
        :type HeaderNames: list of str
        :param _CookieNames: <p>签名的cookie名称列表</p>
        :type CookieNames: list of str
        :param _URIParamNames: <p>签名的URL参数名称列表</p>
        :type URIParamNames: list of str
        :param _KeyClaimName: <p>消费者标识</p>
        :type KeyClaimName: str
        :param _ClaimsToVerify: <p>标准消费者校验</p><p>枚举值：</p><ul><li>exp： exp</li><li>nbf： nbf</li></ul>
        :type ClaimsToVerify: list of str
        :param _MaximumExpiration: <p>最大有效期</p>
        :type MaximumExpiration: int
        :param _SecretIsBase64: <p>是否Base64编码</p>
        :type SecretIsBase64: bool
        :param _RunOnPreFlight: <p>CORS预检验证</p>
        :type RunOnPreFlight: bool
        """
        self._HeaderNames = None
        self._CookieNames = None
        self._URIParamNames = None
        self._KeyClaimName = None
        self._ClaimsToVerify = None
        self._MaximumExpiration = None
        self._SecretIsBase64 = None
        self._RunOnPreFlight = None

    @property
    def HeaderNames(self):
        r"""<p>签名的header名称列表</p>
        :rtype: list of str
        """
        return self._HeaderNames

    @HeaderNames.setter
    def HeaderNames(self, HeaderNames):
        self._HeaderNames = HeaderNames

    @property
    def CookieNames(self):
        r"""<p>签名的cookie名称列表</p>
        :rtype: list of str
        """
        return self._CookieNames

    @CookieNames.setter
    def CookieNames(self, CookieNames):
        self._CookieNames = CookieNames

    @property
    def URIParamNames(self):
        r"""<p>签名的URL参数名称列表</p>
        :rtype: list of str
        """
        return self._URIParamNames

    @URIParamNames.setter
    def URIParamNames(self, URIParamNames):
        self._URIParamNames = URIParamNames

    @property
    def KeyClaimName(self):
        r"""<p>消费者标识</p>
        :rtype: str
        """
        return self._KeyClaimName

    @KeyClaimName.setter
    def KeyClaimName(self, KeyClaimName):
        self._KeyClaimName = KeyClaimName

    @property
    def ClaimsToVerify(self):
        r"""<p>标准消费者校验</p><p>枚举值：</p><ul><li>exp： exp</li><li>nbf： nbf</li></ul>
        :rtype: list of str
        """
        return self._ClaimsToVerify

    @ClaimsToVerify.setter
    def ClaimsToVerify(self, ClaimsToVerify):
        self._ClaimsToVerify = ClaimsToVerify

    @property
    def MaximumExpiration(self):
        r"""<p>最大有效期</p>
        :rtype: int
        """
        return self._MaximumExpiration

    @MaximumExpiration.setter
    def MaximumExpiration(self, MaximumExpiration):
        self._MaximumExpiration = MaximumExpiration

    @property
    def SecretIsBase64(self):
        r"""<p>是否Base64编码</p>
        :rtype: bool
        """
        return self._SecretIsBase64

    @SecretIsBase64.setter
    def SecretIsBase64(self, SecretIsBase64):
        self._SecretIsBase64 = SecretIsBase64

    @property
    def RunOnPreFlight(self):
        r"""<p>CORS预检验证</p>
        :rtype: bool
        """
        return self._RunOnPreFlight

    @RunOnPreFlight.setter
    def RunOnPreFlight(self, RunOnPreFlight):
        self._RunOnPreFlight = RunOnPreFlight


    def _deserialize(self, params):
        self._HeaderNames = params.get("HeaderNames")
        self._CookieNames = params.get("CookieNames")
        self._URIParamNames = params.get("URIParamNames")
        self._KeyClaimName = params.get("KeyClaimName")
        self._ClaimsToVerify = params.get("ClaimsToVerify")
        self._MaximumExpiration = params.get("MaximumExpiration")
        self._SecretIsBase64 = params.get("SecretIsBase64")
        self._RunOnPreFlight = params.get("RunOnPreFlight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWJWTCredentialConfig(AbstractModel):
    r"""AI网关 JWT 凭证物料配置

    """

    def __init__(self):
        r"""
        :param _Algorithm: <p>签名算法，取值：HS256 HS384 HS512 RS256 RS384 RS512 ES256 ES384 ES512</p>
        :type Algorithm: str
        :param _Key: <p>JWT 消费者标识，iss claim</p>
        :type Key: str
        :param _RSAPublicKey: <p>RS/ES PEM 格式公钥，仅 Algorithm 为 RS256/RS384/RS512/ES256/ES384/ES512 时必填；HS* 时留空</p>
        :type RSAPublicKey: str
        :param _Secret: <p>HS 对称密钥，仅 Algorithm 为 HS256/HS384/HS512 时必填；RS/ES* 时留空</p>
        :type Secret: str
        """
        self._Algorithm = None
        self._Key = None
        self._RSAPublicKey = None
        self._Secret = None

    @property
    def Algorithm(self):
        r"""<p>签名算法，取值：HS256 HS384 HS512 RS256 RS384 RS512 ES256 ES384 ES512</p>
        :rtype: str
        """
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def Key(self):
        r"""<p>JWT 消费者标识，iss claim</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def RSAPublicKey(self):
        r"""<p>RS/ES PEM 格式公钥，仅 Algorithm 为 RS256/RS384/RS512/ES256/ES384/ES512 时必填；HS* 时留空</p>
        :rtype: str
        """
        return self._RSAPublicKey

    @RSAPublicKey.setter
    def RSAPublicKey(self, RSAPublicKey):
        self._RSAPublicKey = RSAPublicKey

    @property
    def Secret(self):
        r"""<p>HS 对称密钥，仅 Algorithm 为 HS256/HS384/HS512 时必填；RS/ES* 时留空</p>
        :rtype: str
        """
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret


    def _deserialize(self, params):
        self._Algorithm = params.get("Algorithm")
        self._Key = params.get("Key")
        self._RSAPublicKey = params.get("RSAPublicKey")
        self._Secret = params.get("Secret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWKVMatch(AbstractModel):
    r"""路由匹配规则

    """

    def __init__(self):
        r"""
        :param _Key: <p>键</p>
        :type Key: str
        :param _Value: <p>值</p>
        :type Value: str
        :param _Operator: <p>操作类型</p>
        :type Operator: str
        """
        self._Key = None
        self._Value = None
        self._Operator = None

    @property
    def Key(self):
        r"""<p>键</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>值</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Operator(self):
        r"""<p>操作类型</p>
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLLMModelServiceSubRoute(AbstractModel):
    r"""模型服务二级路由配置

    """

    def __init__(self):
        r"""
        :param _SelectedTypes: <p>生效的路由算法类型：权重路由，模型名称路由、参数路由等Weighted/ModelName/Query (预留多个，暂时只能填写一个)</p>
        :type SelectedTypes: list of str
        :param _WeightedConfig: <p>权重路由配置，最多10个</p>
        :type WeightedConfig: list of CloudNativeAPIGatewayLLMModelServiceRouteWeightedStrategy
        :param _LatencyPriorityConfig: <p>延迟路由</p>
        :type LatencyPriorityConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWLatencyPriorityConfig`
        :param _ModelServiceConfig: <p>指定模型路由（暂时只用在Token长度路由时的子路由选择）</p>
        :type ModelServiceConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWRouteModelServiceConfig`
        """
        self._SelectedTypes = None
        self._WeightedConfig = None
        self._LatencyPriorityConfig = None
        self._ModelServiceConfig = None

    @property
    def SelectedTypes(self):
        r"""<p>生效的路由算法类型：权重路由，模型名称路由、参数路由等Weighted/ModelName/Query (预留多个，暂时只能填写一个)</p>
        :rtype: list of str
        """
        return self._SelectedTypes

    @SelectedTypes.setter
    def SelectedTypes(self, SelectedTypes):
        self._SelectedTypes = SelectedTypes

    @property
    def WeightedConfig(self):
        r"""<p>权重路由配置，最多10个</p>
        :rtype: list of CloudNativeAPIGatewayLLMModelServiceRouteWeightedStrategy
        """
        return self._WeightedConfig

    @WeightedConfig.setter
    def WeightedConfig(self, WeightedConfig):
        self._WeightedConfig = WeightedConfig

    @property
    def LatencyPriorityConfig(self):
        r"""<p>延迟路由</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLatencyPriorityConfig`
        """
        return self._LatencyPriorityConfig

    @LatencyPriorityConfig.setter
    def LatencyPriorityConfig(self, LatencyPriorityConfig):
        self._LatencyPriorityConfig = LatencyPriorityConfig

    @property
    def ModelServiceConfig(self):
        r"""<p>指定模型路由（暂时只用在Token长度路由时的子路由选择）</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWRouteModelServiceConfig`
        """
        return self._ModelServiceConfig

    @ModelServiceConfig.setter
    def ModelServiceConfig(self, ModelServiceConfig):
        self._ModelServiceConfig = ModelServiceConfig


    def _deserialize(self, params):
        self._SelectedTypes = params.get("SelectedTypes")
        if params.get("WeightedConfig") is not None:
            self._WeightedConfig = []
            for item in params.get("WeightedConfig"):
                obj = CloudNativeAPIGatewayLLMModelServiceRouteWeightedStrategy()
                obj._deserialize(item)
                self._WeightedConfig.append(obj)
        if params.get("LatencyPriorityConfig") is not None:
            self._LatencyPriorityConfig = AIGWLatencyPriorityConfig()
            self._LatencyPriorityConfig._deserialize(params.get("LatencyPriorityConfig"))
        if params.get("ModelServiceConfig") is not None:
            self._ModelServiceConfig = AIGWRouteModelServiceConfig()
            self._ModelServiceConfig._deserialize(params.get("ModelServiceConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLLMQuotaFallbackTrigger(AbstractModel):
    r"""云原生网关模型API 配额降级触发条件信息

    """

    def __init__(self):
        r"""
        :param _ThresholdPercent: <p>配额感知阈值百分比（RPM 与 TPM 共用）</p><p>取值范围：[0, 99]</p>
        :type ThresholdPercent: int
        :param _CheckDimension: <p>检查维度策略</p><p>枚举值：</p><ul><li>AnyInsufficient：  RPM 或 TPM 任一不足即触发</li><li>AllInsufficient： RPM 和 TPM 同时不足才触发</li></ul>
        :type CheckDimension: str
        """
        self._ThresholdPercent = None
        self._CheckDimension = None

    @property
    def ThresholdPercent(self):
        r"""<p>配额感知阈值百分比（RPM 与 TPM 共用）</p><p>取值范围：[0, 99]</p>
        :rtype: int
        """
        return self._ThresholdPercent

    @ThresholdPercent.setter
    def ThresholdPercent(self, ThresholdPercent):
        self._ThresholdPercent = ThresholdPercent

    @property
    def CheckDimension(self):
        r"""<p>检查维度策略</p><p>枚举值：</p><ul><li>AnyInsufficient：  RPM 或 TPM 任一不足即触发</li><li>AllInsufficient： RPM 和 TPM 同时不足才触发</li></ul>
        :rtype: str
        """
        return self._CheckDimension

    @CheckDimension.setter
    def CheckDimension(self, CheckDimension):
        self._CheckDimension = CheckDimension


    def _deserialize(self, params):
        self._ThresholdPercent = params.get("ThresholdPercent")
        self._CheckDimension = params.get("CheckDimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLLMQuotaLimit(AbstractModel):
    r"""云原生网关模型LLM配额限制信息

    """

    def __init__(self):
        r"""
        :param _RPMLimit: <p>该模型服务每分钟请求数上限，0 表示该维度不限</p>
        :type RPMLimit: int
        :param _TPMLimit: <p>该模型服务每分钟 Token 数上限，0 表示该维度不限</p>
        :type TPMLimit: int
        :param _ConcurrentCountLimit: <p>并发数限流</p>
        :type ConcurrentCountLimit: int
        """
        self._RPMLimit = None
        self._TPMLimit = None
        self._ConcurrentCountLimit = None

    @property
    def RPMLimit(self):
        r"""<p>该模型服务每分钟请求数上限，0 表示该维度不限</p>
        :rtype: int
        """
        return self._RPMLimit

    @RPMLimit.setter
    def RPMLimit(self, RPMLimit):
        self._RPMLimit = RPMLimit

    @property
    def TPMLimit(self):
        r"""<p>该模型服务每分钟 Token 数上限，0 表示该维度不限</p>
        :rtype: int
        """
        return self._TPMLimit

    @TPMLimit.setter
    def TPMLimit(self, TPMLimit):
        self._TPMLimit = TPMLimit

    @property
    def ConcurrentCountLimit(self):
        r"""<p>并发数限流</p>
        :rtype: int
        """
        return self._ConcurrentCountLimit

    @ConcurrentCountLimit.setter
    def ConcurrentCountLimit(self, ConcurrentCountLimit):
        self._ConcurrentCountLimit = ConcurrentCountLimit


    def _deserialize(self, params):
        self._RPMLimit = params.get("RPMLimit")
        self._TPMLimit = params.get("TPMLimit")
        self._ConcurrentCountLimit = params.get("ConcurrentCountLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLLMTokenUsageItem(AbstractModel):
    r"""单个消费者 Token 用量查询结果

    """

    def __init__(self):
        r"""
        :param _ConsumerId: <p>消费者Id</p>
        :type ConsumerId: str
        :param _ConsumerName: <p>消费者名称</p>
        :type ConsumerName: str
        :param _ConsumerGroups: <p>消费者组信息列表</p>
        :type ConsumerGroups: list of AIGWConsumerGroupBrief
        :param _ModelServiceId: <p>模型服务Id</p>
        :type ModelServiceId: str
        :param _ModelServiceName: <p>模型服务名称</p>
        :type ModelServiceName: str
        :param _InputTokens: <p>输入Token数（包含缓存命中Token数）</p>
        :type InputTokens: int
        :param _CacheReadInputTokens: <p>命中缓存输入Token数</p>
        :type CacheReadInputTokens: int
        :param _OutputTokens: <p>输出Token数</p>
        :type OutputTokens: int
        :param _TotalTokens: <p>消耗总Token数</p>
        :type TotalTokens: int
        :param _RequestCount: <p>请求总数</p>
        :type RequestCount: int
        :param _Cost: <p>花费成本</p>
        :type Cost: str
        :param _Currency: <p>成本货币单位</p><p>枚举值：</p><ul><li>CNY： 人民币</li></ul><p>当前仅支持CNY</p>
        :type Currency: str
        """
        self._ConsumerId = None
        self._ConsumerName = None
        self._ConsumerGroups = None
        self._ModelServiceId = None
        self._ModelServiceName = None
        self._InputTokens = None
        self._CacheReadInputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None
        self._RequestCount = None
        self._Cost = None
        self._Currency = None

    @property
    def ConsumerId(self):
        r"""<p>消费者Id</p>
        :rtype: str
        """
        return self._ConsumerId

    @ConsumerId.setter
    def ConsumerId(self, ConsumerId):
        self._ConsumerId = ConsumerId

    @property
    def ConsumerName(self):
        r"""<p>消费者名称</p>
        :rtype: str
        """
        return self._ConsumerName

    @ConsumerName.setter
    def ConsumerName(self, ConsumerName):
        self._ConsumerName = ConsumerName

    @property
    def ConsumerGroups(self):
        r"""<p>消费者组信息列表</p>
        :rtype: list of AIGWConsumerGroupBrief
        """
        return self._ConsumerGroups

    @ConsumerGroups.setter
    def ConsumerGroups(self, ConsumerGroups):
        self._ConsumerGroups = ConsumerGroups

    @property
    def ModelServiceId(self):
        r"""<p>模型服务Id</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId

    @property
    def ModelServiceName(self):
        r"""<p>模型服务名称</p>
        :rtype: str
        """
        return self._ModelServiceName

    @ModelServiceName.setter
    def ModelServiceName(self, ModelServiceName):
        self._ModelServiceName = ModelServiceName

    @property
    def InputTokens(self):
        r"""<p>输入Token数（包含缓存命中Token数）</p>
        :rtype: int
        """
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def CacheReadInputTokens(self):
        r"""<p>命中缓存输入Token数</p>
        :rtype: int
        """
        return self._CacheReadInputTokens

    @CacheReadInputTokens.setter
    def CacheReadInputTokens(self, CacheReadInputTokens):
        self._CacheReadInputTokens = CacheReadInputTokens

    @property
    def OutputTokens(self):
        r"""<p>输出Token数</p>
        :rtype: int
        """
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        r"""<p>消耗总Token数</p>
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def RequestCount(self):
        r"""<p>请求总数</p>
        :rtype: int
        """
        return self._RequestCount

    @RequestCount.setter
    def RequestCount(self, RequestCount):
        self._RequestCount = RequestCount

    @property
    def Cost(self):
        r"""<p>花费成本</p>
        :rtype: str
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def Currency(self):
        r"""<p>成本货币单位</p><p>枚举值：</p><ul><li>CNY： 人民币</li></ul><p>当前仅支持CNY</p>
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency


    def _deserialize(self, params):
        self._ConsumerId = params.get("ConsumerId")
        self._ConsumerName = params.get("ConsumerName")
        if params.get("ConsumerGroups") is not None:
            self._ConsumerGroups = []
            for item in params.get("ConsumerGroups"):
                obj = AIGWConsumerGroupBrief()
                obj._deserialize(item)
                self._ConsumerGroups.append(obj)
        self._ModelServiceId = params.get("ModelServiceId")
        self._ModelServiceName = params.get("ModelServiceName")
        self._InputTokens = params.get("InputTokens")
        self._CacheReadInputTokens = params.get("CacheReadInputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        self._RequestCount = params.get("RequestCount")
        self._Cost = params.get("Cost")
        self._Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLLMTokenUsageListResult(AbstractModel):
    r"""Token用量统计结果

    """

    def __init__(self):
        r"""
        :param _DataList: <p>Token用量明细返回结果列表</p>
        :type DataList: list of AIGWLLMTokenUsageItem
        :param _TotalCount: <p>结果总数</p>
        :type TotalCount: int
        """
        self._DataList = None
        self._TotalCount = None

    @property
    def DataList(self):
        r"""<p>Token用量明细返回结果列表</p>
        :rtype: list of AIGWLLMTokenUsageItem
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def TotalCount(self):
        r"""<p>结果总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = AIGWLLMTokenUsageItem()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLLMTokenUsageStatisticsResult(AbstractModel):
    r"""AI 网关token消耗统计汇总响应结果

    """

    def __init__(self):
        r"""
        :param _TotalRequestCount: <p>查询时间范围内请求总数</p>
        :type TotalRequestCount: int
        :param _TotalInputTokens: <p>查询时间范围内总输入Token数（包含命中缓存的Token数）</p>
        :type TotalInputTokens: int
        :param _TotalOutputTokens: <p>查询时间范围内总输出Token数</p>
        :type TotalOutputTokens: int
        :param _TotalCachedReadInputTokens: <p>查询时间范围内总命中缓存输入Token数</p>
        :type TotalCachedReadInputTokens: int
        :param _TotalCost: <p>查询时间范围内总成本</p>
        :type TotalCost: str
        :param _Currency: <p>成本货币单位</p>
        :type Currency: str
        :param _TopConsumers: <p>查询时间范围内成本最高的消费者</p>
        :type TopConsumers: list of AIGWTopConsumersItem
        """
        self._TotalRequestCount = None
        self._TotalInputTokens = None
        self._TotalOutputTokens = None
        self._TotalCachedReadInputTokens = None
        self._TotalCost = None
        self._Currency = None
        self._TopConsumers = None

    @property
    def TotalRequestCount(self):
        r"""<p>查询时间范围内请求总数</p>
        :rtype: int
        """
        return self._TotalRequestCount

    @TotalRequestCount.setter
    def TotalRequestCount(self, TotalRequestCount):
        self._TotalRequestCount = TotalRequestCount

    @property
    def TotalInputTokens(self):
        r"""<p>查询时间范围内总输入Token数（包含命中缓存的Token数）</p>
        :rtype: int
        """
        return self._TotalInputTokens

    @TotalInputTokens.setter
    def TotalInputTokens(self, TotalInputTokens):
        self._TotalInputTokens = TotalInputTokens

    @property
    def TotalOutputTokens(self):
        r"""<p>查询时间范围内总输出Token数</p>
        :rtype: int
        """
        return self._TotalOutputTokens

    @TotalOutputTokens.setter
    def TotalOutputTokens(self, TotalOutputTokens):
        self._TotalOutputTokens = TotalOutputTokens

    @property
    def TotalCachedReadInputTokens(self):
        r"""<p>查询时间范围内总命中缓存输入Token数</p>
        :rtype: int
        """
        return self._TotalCachedReadInputTokens

    @TotalCachedReadInputTokens.setter
    def TotalCachedReadInputTokens(self, TotalCachedReadInputTokens):
        self._TotalCachedReadInputTokens = TotalCachedReadInputTokens

    @property
    def TotalCost(self):
        r"""<p>查询时间范围内总成本</p>
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Currency(self):
        r"""<p>成本货币单位</p>
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def TopConsumers(self):
        r"""<p>查询时间范围内成本最高的消费者</p>
        :rtype: list of AIGWTopConsumersItem
        """
        return self._TopConsumers

    @TopConsumers.setter
    def TopConsumers(self, TopConsumers):
        self._TopConsumers = TopConsumers


    def _deserialize(self, params):
        self._TotalRequestCount = params.get("TotalRequestCount")
        self._TotalInputTokens = params.get("TotalInputTokens")
        self._TotalOutputTokens = params.get("TotalOutputTokens")
        self._TotalCachedReadInputTokens = params.get("TotalCachedReadInputTokens")
        self._TotalCost = params.get("TotalCost")
        self._Currency = params.get("Currency")
        if params.get("TopConsumers") is not None:
            self._TopConsumers = []
            for item in params.get("TopConsumers"):
                obj = AIGWTopConsumersItem()
                obj._deserialize(item)
                self._TopConsumers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLatencyPriorityConfig(AbstractModel):
    r"""延迟优先路由配置

    """

    def __init__(self):
        r"""
        :param _Rules: <p>路由规则列表</p>
        :type Rules: list of AIGWLatencyPriorityRouteRule
        :param _LatencyMetric: <p>延迟指标</p><p>枚举值：</p><ul><li>LLMLatency： LLM 延迟</li><li>NetworkLatency： 网络延迟</li></ul>
        :type LatencyMetric: str
        :param _RouteMode: <p>路由策略</p><p>枚举值：</p><ul><li>FastMode： 快速模式</li><li>BalanceMode： 均衡模式</li></ul>
        :type RouteMode: str
        """
        self._Rules = None
        self._LatencyMetric = None
        self._RouteMode = None

    @property
    def Rules(self):
        r"""<p>路由规则列表</p>
        :rtype: list of AIGWLatencyPriorityRouteRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def LatencyMetric(self):
        r"""<p>延迟指标</p><p>枚举值：</p><ul><li>LLMLatency： LLM 延迟</li><li>NetworkLatency： 网络延迟</li></ul>
        :rtype: str
        """
        return self._LatencyMetric

    @LatencyMetric.setter
    def LatencyMetric(self, LatencyMetric):
        self._LatencyMetric = LatencyMetric

    @property
    def RouteMode(self):
        r"""<p>路由策略</p><p>枚举值：</p><ul><li>FastMode： 快速模式</li><li>BalanceMode： 均衡模式</li></ul>
        :rtype: str
        """
        return self._RouteMode

    @RouteMode.setter
    def RouteMode(self, RouteMode):
        self._RouteMode = RouteMode


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = AIGWLatencyPriorityRouteRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._LatencyMetric = params.get("LatencyMetric")
        self._RouteMode = params.get("RouteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLatencyPriorityRouteRule(AbstractModel):
    r"""AI 网关延迟优先路由模型服务

    """

    def __init__(self):
        r"""
        :param _ModelServiceId: <p>模型服务id</p>
        :type ModelServiceId: str
        """
        self._ModelServiceId = None

    @property
    def ModelServiceId(self):
        r"""<p>模型服务id</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId


    def _deserialize(self, params):
        self._ModelServiceId = params.get("ModelServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLogConfig(AbstractModel):
    r"""AI 网关日志输出配置

    """

    def __init__(self):
        r"""
        :param _EnableRequestLogPayloads: <p>是否开启请求 payload 记录日志</p>
        :type EnableRequestLogPayloads: bool
        :param _EnableResponseLogPayloads: <p>是否开启响应 payload 记录日志</p>
        :type EnableResponseLogPayloads: bool
        :param _RequestLogPayloadMaxSize: <p>日志记录的请求body的最大字节数</p><p>取值范围：[512, 1048576]</p><p>EnableRequestLogPayloads 为true时必填</p>
        :type RequestLogPayloadMaxSize: int
        :param _ResponseLogPayloadMaxSize: <p>日志记录的响应body的最大字节数</p><p>取值范围：[512, 1048576]</p><p>EnableResponseLogPayloads 为true时必填</p>
        :type ResponseLogPayloadMaxSize: int
        :param _RequestLogPayloadMode: <p>请求 payload access log 输出模式</p><p>枚举值：</p><ul><li>raw： access log 中 body 记录客户端原始请求</li><li>processed： access log 中 body 记录 AI 网关协议适配、改写、归一化后的 OpenAI-compatible 内容</li></ul>
        :type RequestLogPayloadMode: str
        :param _ResponseLogPayloadMode: <p>上游原始 payload access log 输出模式</p><p>枚举值：</p><ul><li>raw： access log 中 body 记录客户端原始上游响应</li><li>processed： access log 中 body 记录 AI 网关协议适配、改写、归一化后的 OpenAI-compatible 内容</li></ul>
        :type ResponseLogPayloadMode: str
        """
        self._EnableRequestLogPayloads = None
        self._EnableResponseLogPayloads = None
        self._RequestLogPayloadMaxSize = None
        self._ResponseLogPayloadMaxSize = None
        self._RequestLogPayloadMode = None
        self._ResponseLogPayloadMode = None

    @property
    def EnableRequestLogPayloads(self):
        r"""<p>是否开启请求 payload 记录日志</p>
        :rtype: bool
        """
        return self._EnableRequestLogPayloads

    @EnableRequestLogPayloads.setter
    def EnableRequestLogPayloads(self, EnableRequestLogPayloads):
        self._EnableRequestLogPayloads = EnableRequestLogPayloads

    @property
    def EnableResponseLogPayloads(self):
        r"""<p>是否开启响应 payload 记录日志</p>
        :rtype: bool
        """
        return self._EnableResponseLogPayloads

    @EnableResponseLogPayloads.setter
    def EnableResponseLogPayloads(self, EnableResponseLogPayloads):
        self._EnableResponseLogPayloads = EnableResponseLogPayloads

    @property
    def RequestLogPayloadMaxSize(self):
        r"""<p>日志记录的请求body的最大字节数</p><p>取值范围：[512, 1048576]</p><p>EnableRequestLogPayloads 为true时必填</p>
        :rtype: int
        """
        return self._RequestLogPayloadMaxSize

    @RequestLogPayloadMaxSize.setter
    def RequestLogPayloadMaxSize(self, RequestLogPayloadMaxSize):
        self._RequestLogPayloadMaxSize = RequestLogPayloadMaxSize

    @property
    def ResponseLogPayloadMaxSize(self):
        r"""<p>日志记录的响应body的最大字节数</p><p>取值范围：[512, 1048576]</p><p>EnableResponseLogPayloads 为true时必填</p>
        :rtype: int
        """
        return self._ResponseLogPayloadMaxSize

    @ResponseLogPayloadMaxSize.setter
    def ResponseLogPayloadMaxSize(self, ResponseLogPayloadMaxSize):
        self._ResponseLogPayloadMaxSize = ResponseLogPayloadMaxSize

    @property
    def RequestLogPayloadMode(self):
        r"""<p>请求 payload access log 输出模式</p><p>枚举值：</p><ul><li>raw： access log 中 body 记录客户端原始请求</li><li>processed： access log 中 body 记录 AI 网关协议适配、改写、归一化后的 OpenAI-compatible 内容</li></ul>
        :rtype: str
        """
        return self._RequestLogPayloadMode

    @RequestLogPayloadMode.setter
    def RequestLogPayloadMode(self, RequestLogPayloadMode):
        self._RequestLogPayloadMode = RequestLogPayloadMode

    @property
    def ResponseLogPayloadMode(self):
        r"""<p>上游原始 payload access log 输出模式</p><p>枚举值：</p><ul><li>raw： access log 中 body 记录客户端原始上游响应</li><li>processed： access log 中 body 记录 AI 网关协议适配、改写、归一化后的 OpenAI-compatible 内容</li></ul>
        :rtype: str
        """
        return self._ResponseLogPayloadMode

    @ResponseLogPayloadMode.setter
    def ResponseLogPayloadMode(self, ResponseLogPayloadMode):
        self._ResponseLogPayloadMode = ResponseLogPayloadMode


    def _deserialize(self, params):
        self._EnableRequestLogPayloads = params.get("EnableRequestLogPayloads")
        self._EnableResponseLogPayloads = params.get("EnableResponseLogPayloads")
        self._RequestLogPayloadMaxSize = params.get("RequestLogPayloadMaxSize")
        self._ResponseLogPayloadMaxSize = params.get("ResponseLogPayloadMaxSize")
        self._RequestLogPayloadMode = params.get("RequestLogPayloadMode")
        self._ResponseLogPayloadMode = params.get("ResponseLogPayloadMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWLogDesensitizeConfig(AbstractModel):
    r"""AI 网关 B 层日志脱敏配置（写入 LLM Log 前对 payload 掩码）

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>日志脱敏开关</p>
        :type Enabled: bool
        :param _PredefinedRuleTypes: <p>预定义规则类型</p><p>枚举值：</p><ul><li>Phone： 电话号码</li><li>IdCard： 身份证号</li><li>BankCard： 银行卡号</li><li>Email： 邮箱地址</li><li>IP： IP地址</li><li>Name： 姓名</li></ul>
        :type PredefinedRuleTypes: list of str
        :param _CustomRules: <p>自定义脱敏规则</p>
        :type CustomRules: list of AIGWCustomDesensitizeRule
        :param _Scope: <p>日志脱敏范围</p><p>枚举值：</p><ul><li>Request： 请求</li><li>Response： 响应</li></ul>
        :type Scope: list of str
        """
        self._Enabled = None
        self._PredefinedRuleTypes = None
        self._CustomRules = None
        self._Scope = None

    @property
    def Enabled(self):
        r"""<p>日志脱敏开关</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def PredefinedRuleTypes(self):
        r"""<p>预定义规则类型</p><p>枚举值：</p><ul><li>Phone： 电话号码</li><li>IdCard： 身份证号</li><li>BankCard： 银行卡号</li><li>Email： 邮箱地址</li><li>IP： IP地址</li><li>Name： 姓名</li></ul>
        :rtype: list of str
        """
        return self._PredefinedRuleTypes

    @PredefinedRuleTypes.setter
    def PredefinedRuleTypes(self, PredefinedRuleTypes):
        self._PredefinedRuleTypes = PredefinedRuleTypes

    @property
    def CustomRules(self):
        r"""<p>自定义脱敏规则</p>
        :rtype: list of AIGWCustomDesensitizeRule
        """
        return self._CustomRules

    @CustomRules.setter
    def CustomRules(self, CustomRules):
        self._CustomRules = CustomRules

    @property
    def Scope(self):
        r"""<p>日志脱敏范围</p><p>枚举值：</p><ul><li>Request： 请求</li><li>Response： 响应</li></ul>
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._PredefinedRuleTypes = params.get("PredefinedRuleTypes")
        if params.get("CustomRules") is not None:
            self._CustomRules = []
            for item in params.get("CustomRules"):
                obj = AIGWCustomDesensitizeRule()
                obj._deserialize(item)
                self._CustomRules.append(obj)
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPServer(AbstractModel):
    r"""MCP Server详情

    """

    def __init__(self):
        r"""
        :param _ServerId: <p>MCP Server ID</p>
        :type ServerId: str
        :param _Name: <p>MCP Server名称</p>
        :type Name: str
        :param _ServerType: <p>MCP Server类型，取值：MCP/Rest2MCP</p>
        :type ServerType: str
        :param _Transport: <p>协议类型，取值: StreamableHttp</p>
        :type Transport: str
        :param _UpstreamType: <p>服务类型：</p><ul><li>Registry  </li><li>HostIP</li></ul>
        :type UpstreamType: str
        :param _DisplayName: <p>展示名字</p>
        :type DisplayName: str
        :param _MCPEndpoint: <p>MCP提供给客户端的Endpoint</p>
        :type MCPEndpoint: str
        :param _UpstreamInfo: <p>注册中心来源信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamInfo: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPUpstreamInfoDetail`
        :param _SessionConfig: <p>会话配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPSessionConfig`
        :param _Timeout: <p>超时时间，单位ms</p>
        :type Timeout: int
        :param _RetryCount: <p>失败重试次数</p>
        :type RetryCount: int
        :param _CreateTime: <p>创建时间</p>
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间</p>
        :type UpdateTime: str
        :param _Description: <p>描述</p>
        :type Description: str
        :param _Status: <p>运行状态</p><p>枚举值：</p><ul><li>Online： 在线</li><li>Offline： 离线</li><li>Error： 错误</li></ul>
        :type Status: str
        :param _EnableHealthCheck: <p>是否启用健康检查</p>
        :type EnableHealthCheck: bool
        :param _HealthCheck: <p>健康检查配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.cngw.v20230418.models.AIGWHealthCheckSetting`
        :param _ToolCountLimit: <p>Tool分组内工具数量限制</p>
        :type ToolCountLimit: int
        :param _ConflictStrategy: <p>Tool分组内工具命名冲突策略</p><p>枚举值：</p><ul><li>AutoPrefix： 自动前缀</li><li>Reject： 拒绝</li></ul>
        :type ConflictStrategy: str
        :param _MarketStatus: <p>MCP 市场发布状态</p><p>枚举值：</p><ul><li>None： 未发布</li><li>Published： 已发布</li></ul>
        :type MarketStatus: str
        """
        self._ServerId = None
        self._Name = None
        self._ServerType = None
        self._Transport = None
        self._UpstreamType = None
        self._DisplayName = None
        self._MCPEndpoint = None
        self._UpstreamInfo = None
        self._SessionConfig = None
        self._Timeout = None
        self._RetryCount = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Description = None
        self._Status = None
        self._EnableHealthCheck = None
        self._HealthCheck = None
        self._ToolCountLimit = None
        self._ConflictStrategy = None
        self._MarketStatus = None

    @property
    def ServerId(self):
        r"""<p>MCP Server ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def Name(self):
        r"""<p>MCP Server名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ServerType(self):
        r"""<p>MCP Server类型，取值：MCP/Rest2MCP</p>
        :rtype: str
        """
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def Transport(self):
        r"""<p>协议类型，取值: StreamableHttp</p>
        :rtype: str
        """
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

    @property
    def UpstreamType(self):
        r"""<p>服务类型：</p><ul><li>Registry  </li><li>HostIP</li></ul>
        :rtype: str
        """
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def DisplayName(self):
        r"""<p>展示名字</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def MCPEndpoint(self):
        r"""<p>MCP提供给客户端的Endpoint</p>
        :rtype: str
        """
        return self._MCPEndpoint

    @MCPEndpoint.setter
    def MCPEndpoint(self, MCPEndpoint):
        self._MCPEndpoint = MCPEndpoint

    @property
    def UpstreamInfo(self):
        r"""<p>注册中心来源信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPUpstreamInfoDetail`
        """
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def SessionConfig(self):
        r"""<p>会话配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPSessionConfig`
        """
        return self._SessionConfig

    @SessionConfig.setter
    def SessionConfig(self, SessionConfig):
        self._SessionConfig = SessionConfig

    @property
    def Timeout(self):
        r"""<p>超时时间，单位ms</p>
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def RetryCount(self):
        r"""<p>失败重试次数</p>
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def CreateTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
    def Status(self):
        r"""<p>运行状态</p><p>枚举值：</p><ul><li>Online： 在线</li><li>Offline： 离线</li><li>Error： 错误</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EnableHealthCheck(self):
        r"""<p>是否启用健康检查</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def HealthCheck(self):
        r"""<p>健康检查配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWHealthCheckSetting`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def ToolCountLimit(self):
        r"""<p>Tool分组内工具数量限制</p>
        :rtype: int
        """
        return self._ToolCountLimit

    @ToolCountLimit.setter
    def ToolCountLimit(self, ToolCountLimit):
        self._ToolCountLimit = ToolCountLimit

    @property
    def ConflictStrategy(self):
        r"""<p>Tool分组内工具命名冲突策略</p><p>枚举值：</p><ul><li>AutoPrefix： 自动前缀</li><li>Reject： 拒绝</li></ul>
        :rtype: str
        """
        return self._ConflictStrategy

    @ConflictStrategy.setter
    def ConflictStrategy(self, ConflictStrategy):
        self._ConflictStrategy = ConflictStrategy

    @property
    def MarketStatus(self):
        r"""<p>MCP 市场发布状态</p><p>枚举值：</p><ul><li>None： 未发布</li><li>Published： 已发布</li></ul>
        :rtype: str
        """
        return self._MarketStatus

    @MarketStatus.setter
    def MarketStatus(self, MarketStatus):
        self._MarketStatus = MarketStatus


    def _deserialize(self, params):
        self._ServerId = params.get("ServerId")
        self._Name = params.get("Name")
        self._ServerType = params.get("ServerType")
        self._Transport = params.get("Transport")
        self._UpstreamType = params.get("UpstreamType")
        self._DisplayName = params.get("DisplayName")
        self._MCPEndpoint = params.get("MCPEndpoint")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = AIGWMCPUpstreamInfoDetail()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        if params.get("SessionConfig") is not None:
            self._SessionConfig = AIGWMCPSessionConfig()
            self._SessionConfig._deserialize(params.get("SessionConfig"))
        self._Timeout = params.get("Timeout")
        self._RetryCount = params.get("RetryCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = AIGWHealthCheckSetting()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._ToolCountLimit = params.get("ToolCountLimit")
        self._ConflictStrategy = params.get("ConflictStrategy")
        self._MarketStatus = params.get("MarketStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPServerACLResult(AbstractModel):
    r"""AI 网关 MCP Server ACL 配置详情

    """

    def __init__(self):
        r"""
        :param _ACLType: <p>黑白名单鉴权类型</p><p>枚举值：</p><ul><li>None： 不鉴权</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul>
        :type ACLType: str
        :param _ACLConsumers: <p>关联的消费者ID列表</p>
        :type ACLConsumers: list of AIGWACLSubject
        :param _ACLConsumerGroups: <p>关联的消费者组ID列表</p>
        :type ACLConsumerGroups: list of AIGWACLSubject
        :param _AuthType: <p>认证类型</p><p>枚举值：</p><ul><li>None： 无认证</li><li>ApiKey： API Key认证</li></ul>
        :type AuthType: str
        """
        self._ACLType = None
        self._ACLConsumers = None
        self._ACLConsumerGroups = None
        self._AuthType = None

    @property
    def ACLType(self):
        r"""<p>黑白名单鉴权类型</p><p>枚举值：</p><ul><li>None： 不鉴权</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul>
        :rtype: str
        """
        return self._ACLType

    @ACLType.setter
    def ACLType(self, ACLType):
        self._ACLType = ACLType

    @property
    def ACLConsumers(self):
        r"""<p>关联的消费者ID列表</p>
        :rtype: list of AIGWACLSubject
        """
        return self._ACLConsumers

    @ACLConsumers.setter
    def ACLConsumers(self, ACLConsumers):
        self._ACLConsumers = ACLConsumers

    @property
    def ACLConsumerGroups(self):
        r"""<p>关联的消费者组ID列表</p>
        :rtype: list of AIGWACLSubject
        """
        return self._ACLConsumerGroups

    @ACLConsumerGroups.setter
    def ACLConsumerGroups(self, ACLConsumerGroups):
        self._ACLConsumerGroups = ACLConsumerGroups

    @property
    def AuthType(self):
        r"""<p>认证类型</p><p>枚举值：</p><ul><li>None： 无认证</li><li>ApiKey： API Key认证</li></ul>
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType


    def _deserialize(self, params):
        self._ACLType = params.get("ACLType")
        if params.get("ACLConsumers") is not None:
            self._ACLConsumers = []
            for item in params.get("ACLConsumers"):
                obj = AIGWACLSubject()
                obj._deserialize(item)
                self._ACLConsumers.append(obj)
        if params.get("ACLConsumerGroups") is not None:
            self._ACLConsumerGroups = []
            for item in params.get("ACLConsumerGroups"):
                obj = AIGWACLSubject()
                obj._deserialize(item)
                self._ACLConsumerGroups.append(obj)
        self._AuthType = params.get("AuthType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPServerAuthResult(AbstractModel):
    r"""AI 网关 MCP Server 认证配置详情

    """

    def __init__(self):
        r"""
        :param _AuthType: <p>MCP服务认证类型</p><p>枚举值：</p><ul><li>None： 无认证</li><li>ApiKey： API Key认证</li></ul>
        :type AuthType: str
        :param _JWTAuthConfig: <p>JWT认证配置</p>
        :type JWTAuthConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWJWTAuthPluginConfig`
        :param _OAuthAuthConfig: <p>OAuth2认证配置</p>
        :type OAuthAuthConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWOAuthAuthPluginConfig`
        :param _OIDCAuthConfig: <p>OIDC认证配置</p>
        :type OIDCAuthConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWOIDCAuthPluginConfig`
        """
        self._AuthType = None
        self._JWTAuthConfig = None
        self._OAuthAuthConfig = None
        self._OIDCAuthConfig = None

    @property
    def AuthType(self):
        r"""<p>MCP服务认证类型</p><p>枚举值：</p><ul><li>None： 无认证</li><li>ApiKey： API Key认证</li></ul>
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def JWTAuthConfig(self):
        r"""<p>JWT认证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWJWTAuthPluginConfig`
        """
        return self._JWTAuthConfig

    @JWTAuthConfig.setter
    def JWTAuthConfig(self, JWTAuthConfig):
        self._JWTAuthConfig = JWTAuthConfig

    @property
    def OAuthAuthConfig(self):
        r"""<p>OAuth2认证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWOAuthAuthPluginConfig`
        """
        return self._OAuthAuthConfig

    @OAuthAuthConfig.setter
    def OAuthAuthConfig(self, OAuthAuthConfig):
        self._OAuthAuthConfig = OAuthAuthConfig

    @property
    def OIDCAuthConfig(self):
        r"""<p>OIDC认证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWOIDCAuthPluginConfig`
        """
        return self._OIDCAuthConfig

    @OIDCAuthConfig.setter
    def OIDCAuthConfig(self, OIDCAuthConfig):
        self._OIDCAuthConfig = OIDCAuthConfig


    def _deserialize(self, params):
        self._AuthType = params.get("AuthType")
        if params.get("JWTAuthConfig") is not None:
            self._JWTAuthConfig = AIGWJWTAuthPluginConfig()
            self._JWTAuthConfig._deserialize(params.get("JWTAuthConfig"))
        if params.get("OAuthAuthConfig") is not None:
            self._OAuthAuthConfig = AIGWOAuthAuthPluginConfig()
            self._OAuthAuthConfig._deserialize(params.get("OAuthAuthConfig"))
        if params.get("OIDCAuthConfig") is not None:
            self._OIDCAuthConfig = AIGWOIDCAuthPluginConfig()
            self._OIDCAuthConfig._deserialize(params.get("OIDCAuthConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPServerList(AbstractModel):
    r"""MCP Server 列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数</p>
        :type TotalCount: int
        :param _DataList: <p>mcp server 数据列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DataList: list of AIGWMCPServer
        """
        self._TotalCount = None
        self._DataList = None

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
    def DataList(self):
        r"""<p>mcp server 数据列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AIGWMCPServer
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = AIGWMCPServer()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPSessionConfig(AbstractModel):
    r"""云原生网关MCP会话配置

    """

    def __init__(self):
        r"""
        :param _SessionStorage: <p>会话存储类型</p><p>枚举值：</p><ul><li>memory： 内存</li><li>redis： redis</li></ul>
        :type SessionStorage: str
        :param _RedisConfig: <p>Redis配置</p>
        :type RedisConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWRedisConfig`
        """
        self._SessionStorage = None
        self._RedisConfig = None

    @property
    def SessionStorage(self):
        r"""<p>会话存储类型</p><p>枚举值：</p><ul><li>memory： 内存</li><li>redis： redis</li></ul>
        :rtype: str
        """
        return self._SessionStorage

    @SessionStorage.setter
    def SessionStorage(self, SessionStorage):
        self._SessionStorage = SessionStorage

    @property
    def RedisConfig(self):
        r"""<p>Redis配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWRedisConfig`
        """
        return self._RedisConfig

    @RedisConfig.setter
    def RedisConfig(self, RedisConfig):
        self._RedisConfig = RedisConfig


    def _deserialize(self, params):
        self._SessionStorage = params.get("SessionStorage")
        if params.get("RedisConfig") is not None:
            self._RedisConfig = AIGWRedisConfig()
            self._RedisConfig._deserialize(params.get("RedisConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPToolACLItem(AbstractModel):
    r"""AI 网关 Tool ACL 单条记录（DescribeMCPToolACLList 数组元素）

    """

    def __init__(self):
        r"""
        :param _ToolId: <p>MCP工具ID</p>
        :type ToolId: str
        :param _ToolName: <p>MCP工具名称</p>
        :type ToolName: str
        :param _ACLType: <p>MCP工具鉴权类型</p><p>枚举值：</p><ul><li>None： 继承server鉴权类型</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul>
        :type ACLType: str
        :param _ACLConsumers: <p>关联的消费者ID列表</p>
        :type ACLConsumers: list of AIGWACLSubject
        :param _ACLConsumerGroups: <p>关联的消费者组ID列表</p>
        :type ACLConsumerGroups: list of AIGWACLSubject
        """
        self._ToolId = None
        self._ToolName = None
        self._ACLType = None
        self._ACLConsumers = None
        self._ACLConsumerGroups = None

    @property
    def ToolId(self):
        r"""<p>MCP工具ID</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""<p>MCP工具名称</p>
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def ACLType(self):
        r"""<p>MCP工具鉴权类型</p><p>枚举值：</p><ul><li>None： 继承server鉴权类型</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul>
        :rtype: str
        """
        return self._ACLType

    @ACLType.setter
    def ACLType(self, ACLType):
        self._ACLType = ACLType

    @property
    def ACLConsumers(self):
        r"""<p>关联的消费者ID列表</p>
        :rtype: list of AIGWACLSubject
        """
        return self._ACLConsumers

    @ACLConsumers.setter
    def ACLConsumers(self, ACLConsumers):
        self._ACLConsumers = ACLConsumers

    @property
    def ACLConsumerGroups(self):
        r"""<p>关联的消费者组ID列表</p>
        :rtype: list of AIGWACLSubject
        """
        return self._ACLConsumerGroups

    @ACLConsumerGroups.setter
    def ACLConsumerGroups(self, ACLConsumerGroups):
        self._ACLConsumerGroups = ACLConsumerGroups


    def _deserialize(self, params):
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._ACLType = params.get("ACLType")
        if params.get("ACLConsumers") is not None:
            self._ACLConsumers = []
            for item in params.get("ACLConsumers"):
                obj = AIGWACLSubject()
                obj._deserialize(item)
                self._ACLConsumers.append(obj)
        if params.get("ACLConsumerGroups") is not None:
            self._ACLConsumerGroups = []
            for item in params.get("ACLConsumerGroups"):
                obj = AIGWACLSubject()
                obj._deserialize(item)
                self._ACLConsumerGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPToolACLListResult(AbstractModel):
    r"""AI 网关 mcp server 下所有 tool 的 ACL 状态

    """

    def __init__(self):
        r"""
        :param _ACLType: <p>黑白名单鉴权类型</p><p>枚举值：</p><ul><li>None： 不鉴权</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul>
        :type ACLType: str
        :param _DataList: <p>数据列表</p>
        :type DataList: list of AIGWMCPToolACLItem
        :param _TotalCount: <p>计数</p>
        :type TotalCount: int
        """
        self._ACLType = None
        self._DataList = None
        self._TotalCount = None

    @property
    def ACLType(self):
        r"""<p>黑白名单鉴权类型</p><p>枚举值：</p><ul><li>None： 不鉴权</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul>
        :rtype: str
        """
        return self._ACLType

    @ACLType.setter
    def ACLType(self, ACLType):
        self._ACLType = ACLType

    @property
    def DataList(self):
        r"""<p>数据列表</p>
        :rtype: list of AIGWMCPToolACLItem
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def TotalCount(self):
        r"""<p>计数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._ACLType = params.get("ACLType")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = AIGWMCPToolACLItem()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPUpstreamInfo(AbstractModel):
    r"""云原生网关MCP后端信息,用于创建、修改请求

    """

    def __init__(self):
        r"""
        :param _SourceId: <p>注册中心来源ID</p>
        :type SourceId: str
        :param _Namespace: <p>命名空间</p>
        :type Namespace: str
        :param _MCPServerId: <p>MCP服务 id</p>
        :type MCPServerId: str
        :param _Protocol: <p>协议，UpstreamType是Registry 时必传</p><ul><li>http</li><li>https</li></ul>
        :type Protocol: str
        :param _Host: <p>域名或ip</p>
        :type Host: str
        :param _Port: <p>端口</p>
        :type Port: int
        :param _ServiceId: <p>服务 id</p>
        :type ServiceId: str
        :param _ServiceGroup: <p>服务分组</p>
        :type ServiceGroup: str
        :param _MCPEndpoint: <p>mcp endpoint</p>
        :type MCPEndpoint: str
        :param _MessageEndpoint: <p>message端点路径，SSE协议时配置</p>
        :type MessageEndpoint: str
        """
        self._SourceId = None
        self._Namespace = None
        self._MCPServerId = None
        self._Protocol = None
        self._Host = None
        self._Port = None
        self._ServiceId = None
        self._ServiceGroup = None
        self._MCPEndpoint = None
        self._MessageEndpoint = None

    @property
    def SourceId(self):
        r"""<p>注册中心来源ID</p>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Namespace(self):
        r"""<p>命名空间</p>
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MCPServerId(self):
        r"""<p>MCP服务 id</p>
        :rtype: str
        """
        return self._MCPServerId

    @MCPServerId.setter
    def MCPServerId(self, MCPServerId):
        self._MCPServerId = MCPServerId

    @property
    def Protocol(self):
        r"""<p>协议，UpstreamType是Registry 时必传</p><ul><li>http</li><li>https</li></ul>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Host(self):
        r"""<p>域名或ip</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""<p>端口</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceId(self):
        r"""<p>服务 id</p>
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceGroup(self):
        r"""<p>服务分组</p>
        :rtype: str
        """
        return self._ServiceGroup

    @ServiceGroup.setter
    def ServiceGroup(self, ServiceGroup):
        self._ServiceGroup = ServiceGroup

    @property
    def MCPEndpoint(self):
        r"""<p>mcp endpoint</p>
        :rtype: str
        """
        return self._MCPEndpoint

    @MCPEndpoint.setter
    def MCPEndpoint(self, MCPEndpoint):
        self._MCPEndpoint = MCPEndpoint

    @property
    def MessageEndpoint(self):
        r"""<p>message端点路径，SSE协议时配置</p>
        :rtype: str
        """
        return self._MessageEndpoint

    @MessageEndpoint.setter
    def MessageEndpoint(self, MessageEndpoint):
        self._MessageEndpoint = MessageEndpoint


    def _deserialize(self, params):
        self._SourceId = params.get("SourceId")
        self._Namespace = params.get("Namespace")
        self._MCPServerId = params.get("MCPServerId")
        self._Protocol = params.get("Protocol")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._ServiceId = params.get("ServiceId")
        self._ServiceGroup = params.get("ServiceGroup")
        self._MCPEndpoint = params.get("MCPEndpoint")
        self._MessageEndpoint = params.get("MessageEndpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWMCPUpstreamInfoDetail(AbstractModel):
    r"""云原生网关MCP后端信息，用于展示

    """

    def __init__(self):
        r"""
        :param _SourceId: <p>注册中心来源ID</p>
        :type SourceId: str
        :param _SourceName: <p>注册中心来源名称, 入参不传，用于返回</p>
        :type SourceName: str
        :param _Namespace: <p>命名空间</p>
        :type Namespace: str
        :param _MCPServerId: <p>服务 id</p>
        :type MCPServerId: str
        :param _Protocol: <p>协议，UpstreamType是Registry 时必传</p><ul><li>http</li><li>https</li></ul>
        :type Protocol: str
        :param _Host: <p>域名或ip</p>
        :type Host: str
        :param _Port: <p>端口</p>
        :type Port: int
        :param _ServiceId: <p>服务 id</p>
        :type ServiceId: str
        :param _ServiceName: <p>服务名字</p>
        :type ServiceName: str
        :param _ServiceGroup: <p>服务分组</p>
        :type ServiceGroup: str
        :param _MCPEndpoint: <p>mcp endpoint</p>
        :type MCPEndpoint: str
        :param _MessageEndpoint: <p>SSE message路径</p>
        :type MessageEndpoint: str
        """
        self._SourceId = None
        self._SourceName = None
        self._Namespace = None
        self._MCPServerId = None
        self._Protocol = None
        self._Host = None
        self._Port = None
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceGroup = None
        self._MCPEndpoint = None
        self._MessageEndpoint = None

    @property
    def SourceId(self):
        r"""<p>注册中心来源ID</p>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceName(self):
        r"""<p>注册中心来源名称, 入参不传，用于返回</p>
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def Namespace(self):
        r"""<p>命名空间</p>
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MCPServerId(self):
        r"""<p>服务 id</p>
        :rtype: str
        """
        return self._MCPServerId

    @MCPServerId.setter
    def MCPServerId(self, MCPServerId):
        self._MCPServerId = MCPServerId

    @property
    def Protocol(self):
        r"""<p>协议，UpstreamType是Registry 时必传</p><ul><li>http</li><li>https</li></ul>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Host(self):
        r"""<p>域名或ip</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""<p>端口</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceId(self):
        r"""<p>服务 id</p>
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        r"""<p>服务名字</p>
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceGroup(self):
        r"""<p>服务分组</p>
        :rtype: str
        """
        return self._ServiceGroup

    @ServiceGroup.setter
    def ServiceGroup(self, ServiceGroup):
        self._ServiceGroup = ServiceGroup

    @property
    def MCPEndpoint(self):
        r"""<p>mcp endpoint</p>
        :rtype: str
        """
        return self._MCPEndpoint

    @MCPEndpoint.setter
    def MCPEndpoint(self, MCPEndpoint):
        self._MCPEndpoint = MCPEndpoint

    @property
    def MessageEndpoint(self):
        r"""<p>SSE message路径</p>
        :rtype: str
        """
        return self._MessageEndpoint

    @MessageEndpoint.setter
    def MessageEndpoint(self, MessageEndpoint):
        self._MessageEndpoint = MessageEndpoint


    def _deserialize(self, params):
        self._SourceId = params.get("SourceId")
        self._SourceName = params.get("SourceName")
        self._Namespace = params.get("Namespace")
        self._MCPServerId = params.get("MCPServerId")
        self._Protocol = params.get("Protocol")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceGroup = params.get("ServiceGroup")
        self._MCPEndpoint = params.get("MCPEndpoint")
        self._MessageEndpoint = params.get("MessageEndpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWModelRewriteRule(AbstractModel):
    r"""模型名字重写规则

    """

    def __init__(self):
        r"""
        :param _SourceModel: <p>原始模型</p>
        :type SourceModel: str
        :param _TargetModel: <p>目标模型</p>
        :type TargetModel: str
        """
        self._SourceModel = None
        self._TargetModel = None

    @property
    def SourceModel(self):
        r"""<p>原始模型</p>
        :rtype: str
        """
        return self._SourceModel

    @SourceModel.setter
    def SourceModel(self, SourceModel):
        self._SourceModel = SourceModel

    @property
    def TargetModel(self):
        r"""<p>目标模型</p>
        :rtype: str
        """
        return self._TargetModel

    @TargetModel.setter
    def TargetModel(self, TargetModel):
        self._TargetModel = TargetModel


    def _deserialize(self, params):
        self._SourceModel = params.get("SourceModel")
        self._TargetModel = params.get("TargetModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWOAuthAuthPluginConfig(AbstractModel):
    r"""资源端 OAuth2 认证插件配置

    """

    def __init__(self):
        r"""
        :param _HeaderNames: <p>取token的头部名称</p>
        :type HeaderNames: list of str
        :param _TokenExpiration: <p>过期时间</p>
        :type TokenExpiration: int
        :param _Scopes: <p>授权范围</p>
        :type Scopes: list of str
        :param _MandatoryScope: <p>是否强制判断授权范围</p>
        :type MandatoryScope: bool
        """
        self._HeaderNames = None
        self._TokenExpiration = None
        self._Scopes = None
        self._MandatoryScope = None

    @property
    def HeaderNames(self):
        r"""<p>取token的头部名称</p>
        :rtype: list of str
        """
        return self._HeaderNames

    @HeaderNames.setter
    def HeaderNames(self, HeaderNames):
        self._HeaderNames = HeaderNames

    @property
    def TokenExpiration(self):
        r"""<p>过期时间</p>
        :rtype: int
        """
        return self._TokenExpiration

    @TokenExpiration.setter
    def TokenExpiration(self, TokenExpiration):
        self._TokenExpiration = TokenExpiration

    @property
    def Scopes(self):
        r"""<p>授权范围</p>
        :rtype: list of str
        """
        return self._Scopes

    @Scopes.setter
    def Scopes(self, Scopes):
        self._Scopes = Scopes

    @property
    def MandatoryScope(self):
        r"""<p>是否强制判断授权范围</p>
        :rtype: bool
        """
        return self._MandatoryScope

    @MandatoryScope.setter
    def MandatoryScope(self, MandatoryScope):
        self._MandatoryScope = MandatoryScope


    def _deserialize(self, params):
        self._HeaderNames = params.get("HeaderNames")
        self._TokenExpiration = params.get("TokenExpiration")
        self._Scopes = params.get("Scopes")
        self._MandatoryScope = params.get("MandatoryScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWOAuthCredentialConfig(AbstractModel):
    r"""OAuth2 凭证物料配置

    """

    def __init__(self):
        r"""
        :param _ClientId: <p>OAuth2 client_id</p>
        :type ClientId: str
        :param _ClientSecret: <p>OAuth2 client_secret</p>
        :type ClientSecret: str
        :param _RedirectURIs: <p>OAuth2 授权回调地址</p>
        :type RedirectURIs: str
        """
        self._ClientId = None
        self._ClientSecret = None
        self._RedirectURIs = None

    @property
    def ClientId(self):
        r"""<p>OAuth2 client_id</p>
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientSecret(self):
        r"""<p>OAuth2 client_secret</p>
        :rtype: str
        """
        return self._ClientSecret

    @ClientSecret.setter
    def ClientSecret(self, ClientSecret):
        self._ClientSecret = ClientSecret

    @property
    def RedirectURIs(self):
        r"""<p>OAuth2 授权回调地址</p>
        :rtype: str
        """
        return self._RedirectURIs

    @RedirectURIs.setter
    def RedirectURIs(self, RedirectURIs):
        self._RedirectURIs = RedirectURIs


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._ClientSecret = params.get("ClientSecret")
        self._RedirectURIs = params.get("RedirectURIs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWOIDCAuthPluginConfig(AbstractModel):
    r"""资源端 OIDC 认证插件配置

    """

    def __init__(self):
        r"""
        :param _Audience: <p>目标受众</p>
        :type Audience: str
        :param _BearerOnly: <p>是否BearerOnly</p><p>目前只能为true</p>
        :type BearerOnly: bool
        :param _Scopes: <p>授权范围</p>
        :type Scopes: list of str
        :param _ConsumerClaim: <p>消费者标识</p>
        :type ConsumerClaim: str
        :param _Realm: <p>认证域</p>
        :type Realm: str
        :param _Timeout: <p>超时时间</p>
        :type Timeout: int
        :param _TokenEndpointAuthMethod: <p>令牌端点认证方法</p><p>枚举值：</p><ul><li>client_secret_post： client_secret_post</li><li>client_secret_basic： client_secret_basic</li><li>private_key_jwt： private_key_jwt</li></ul>
        :type TokenEndpointAuthMethod: str
        :param _IntrospectionEndpoint: <p>令牌内省端点</p>
        :type IntrospectionEndpoint: str
        :param _IntrospectionEndpointAuthMethod: <p>令牌内省端点认证方法</p><p>枚举值：</p><ul><li>client_secret_basic： client_secret_basic</li><li>client_secret_post： client_secret_post</li></ul>
        :type IntrospectionEndpointAuthMethod: str
        :param _IssuerURL: <p>签发者地址</p>
        :type IssuerURL: str
        :param _ClientId: <p>客户端 ID</p>
        :type ClientId: str
        :param _ClientSecret: <p>客户端密钥</p>
        :type ClientSecret: str
        """
        self._Audience = None
        self._BearerOnly = None
        self._Scopes = None
        self._ConsumerClaim = None
        self._Realm = None
        self._Timeout = None
        self._TokenEndpointAuthMethod = None
        self._IntrospectionEndpoint = None
        self._IntrospectionEndpointAuthMethod = None
        self._IssuerURL = None
        self._ClientId = None
        self._ClientSecret = None

    @property
    def Audience(self):
        r"""<p>目标受众</p>
        :rtype: str
        """
        return self._Audience

    @Audience.setter
    def Audience(self, Audience):
        self._Audience = Audience

    @property
    def BearerOnly(self):
        r"""<p>是否BearerOnly</p><p>目前只能为true</p>
        :rtype: bool
        """
        return self._BearerOnly

    @BearerOnly.setter
    def BearerOnly(self, BearerOnly):
        self._BearerOnly = BearerOnly

    @property
    def Scopes(self):
        r"""<p>授权范围</p>
        :rtype: list of str
        """
        return self._Scopes

    @Scopes.setter
    def Scopes(self, Scopes):
        self._Scopes = Scopes

    @property
    def ConsumerClaim(self):
        r"""<p>消费者标识</p>
        :rtype: str
        """
        return self._ConsumerClaim

    @ConsumerClaim.setter
    def ConsumerClaim(self, ConsumerClaim):
        self._ConsumerClaim = ConsumerClaim

    @property
    def Realm(self):
        r"""<p>认证域</p>
        :rtype: str
        """
        return self._Realm

    @Realm.setter
    def Realm(self, Realm):
        self._Realm = Realm

    @property
    def Timeout(self):
        r"""<p>超时时间</p>
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def TokenEndpointAuthMethod(self):
        r"""<p>令牌端点认证方法</p><p>枚举值：</p><ul><li>client_secret_post： client_secret_post</li><li>client_secret_basic： client_secret_basic</li><li>private_key_jwt： private_key_jwt</li></ul>
        :rtype: str
        """
        return self._TokenEndpointAuthMethod

    @TokenEndpointAuthMethod.setter
    def TokenEndpointAuthMethod(self, TokenEndpointAuthMethod):
        self._TokenEndpointAuthMethod = TokenEndpointAuthMethod

    @property
    def IntrospectionEndpoint(self):
        r"""<p>令牌内省端点</p>
        :rtype: str
        """
        return self._IntrospectionEndpoint

    @IntrospectionEndpoint.setter
    def IntrospectionEndpoint(self, IntrospectionEndpoint):
        self._IntrospectionEndpoint = IntrospectionEndpoint

    @property
    def IntrospectionEndpointAuthMethod(self):
        r"""<p>令牌内省端点认证方法</p><p>枚举值：</p><ul><li>client_secret_basic： client_secret_basic</li><li>client_secret_post： client_secret_post</li></ul>
        :rtype: str
        """
        return self._IntrospectionEndpointAuthMethod

    @IntrospectionEndpointAuthMethod.setter
    def IntrospectionEndpointAuthMethod(self, IntrospectionEndpointAuthMethod):
        self._IntrospectionEndpointAuthMethod = IntrospectionEndpointAuthMethod

    @property
    def IssuerURL(self):
        r"""<p>签发者地址</p>
        :rtype: str
        """
        return self._IssuerURL

    @IssuerURL.setter
    def IssuerURL(self, IssuerURL):
        self._IssuerURL = IssuerURL

    @property
    def ClientId(self):
        r"""<p>客户端 ID</p>
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientSecret(self):
        r"""<p>客户端密钥</p>
        :rtype: str
        """
        return self._ClientSecret

    @ClientSecret.setter
    def ClientSecret(self, ClientSecret):
        self._ClientSecret = ClientSecret


    def _deserialize(self, params):
        self._Audience = params.get("Audience")
        self._BearerOnly = params.get("BearerOnly")
        self._Scopes = params.get("Scopes")
        self._ConsumerClaim = params.get("ConsumerClaim")
        self._Realm = params.get("Realm")
        self._Timeout = params.get("Timeout")
        self._TokenEndpointAuthMethod = params.get("TokenEndpointAuthMethod")
        self._IntrospectionEndpoint = params.get("IntrospectionEndpoint")
        self._IntrospectionEndpointAuthMethod = params.get("IntrospectionEndpointAuthMethod")
        self._IssuerURL = params.get("IssuerURL")
        self._ClientId = params.get("ClientId")
        self._ClientSecret = params.get("ClientSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWOIDCCredentialConfig(AbstractModel):
    r"""OIDC 凭证物料配置

    """

    def __init__(self):
        r"""
        :param _ClientId: <p>IdP 注册的 client_id</p>
        :type ClientId: str
        :param _ClientSecret: <p>IdP 注册的 client_secret</p>
        :type ClientSecret: str
        :param _IssuerURL: <p>IdP Issuer URL</p>
        :type IssuerURL: str
        :param _ConsumerClaimValue: <p>IdP 中该用户的 claim 值</p>
        :type ConsumerClaimValue: str
        """
        self._ClientId = None
        self._ClientSecret = None
        self._IssuerURL = None
        self._ConsumerClaimValue = None

    @property
    def ClientId(self):
        r"""<p>IdP 注册的 client_id</p>
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientSecret(self):
        r"""<p>IdP 注册的 client_secret</p>
        :rtype: str
        """
        return self._ClientSecret

    @ClientSecret.setter
    def ClientSecret(self, ClientSecret):
        self._ClientSecret = ClientSecret

    @property
    def IssuerURL(self):
        r"""<p>IdP Issuer URL</p>
        :rtype: str
        """
        return self._IssuerURL

    @IssuerURL.setter
    def IssuerURL(self, IssuerURL):
        self._IssuerURL = IssuerURL

    @property
    def ConsumerClaimValue(self):
        r"""<p>IdP 中该用户的 claim 值</p>
        :rtype: str
        """
        return self._ConsumerClaimValue

    @ConsumerClaimValue.setter
    def ConsumerClaimValue(self, ConsumerClaimValue):
        self._ConsumerClaimValue = ConsumerClaimValue


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._ClientSecret = params.get("ClientSecret")
        self._IssuerURL = params.get("IssuerURL")
        self._ConsumerClaimValue = params.get("ConsumerClaimValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWRedisConfig(AbstractModel):
    r"""精确缓存 redis 配置

    """

    def __init__(self):
        r"""
        :param _Host: <p>Host</p>
        :type Host: str
        :param _Port: <p>端口</p>
        :type Port: int
        :param _Username: <p>用户名</p>
        :type Username: str
        :param _Password: <p>密码</p>
        :type Password: str
        :param _RedisConfigId: <p>Redis配置ID</p>
        :type RedisConfigId: str
        :param _Type: <p>Redis部署类型，如standalone（单机）、cluster（集群）</p>
        :type Type: str
        """
        self._Host = None
        self._Port = None
        self._Username = None
        self._Password = None
        self._RedisConfigId = None
        self._Type = None

    @property
    def Host(self):
        r"""<p>Host</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""<p>端口</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        r"""<p>用户名</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""<p>密码</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RedisConfigId(self):
        r"""<p>Redis配置ID</p>
        :rtype: str
        """
        return self._RedisConfigId

    @RedisConfigId.setter
    def RedisConfigId(self, RedisConfigId):
        self._RedisConfigId = RedisConfigId

    @property
    def Type(self):
        r"""<p>Redis部署类型，如standalone（单机）、cluster（集群）</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._RedisConfigId = params.get("RedisConfigId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWRouteModelServiceConfig(AbstractModel):
    r"""AI 网关指定模型路由（暂时只用在Token长度路由时的子路由选择）

    """

    def __init__(self):
        r"""
        :param _ModelServiceName: <p>模型服务名字</p>
        :type ModelServiceName: str
        """
        self._ModelServiceName = None

    @property
    def ModelServiceName(self):
        r"""<p>模型服务名字</p>
        :rtype: str
        """
        return self._ModelServiceName

    @ModelServiceName.setter
    def ModelServiceName(self, ModelServiceName):
        self._ModelServiceName = ModelServiceName


    def _deserialize(self, params):
        self._ModelServiceName = params.get("ModelServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWTagFilter(AbstractModel):
    r"""AI网关标签过滤

    """

    def __init__(self):
        r"""
        :param _MatchStrategy: <p>匹配策略</p><p>枚举值：</p><ul><li>AND： 并</li><li>OR： 或</li></ul>
        :type MatchStrategy: str
        :param _Tags: <p>标签</p>
        :type Tags: list of str
        """
        self._MatchStrategy = None
        self._Tags = None

    @property
    def MatchStrategy(self):
        r"""<p>匹配策略</p><p>枚举值：</p><ul><li>AND： 并</li><li>OR： 或</li></ul>
        :rtype: str
        """
        return self._MatchStrategy

    @MatchStrategy.setter
    def MatchStrategy(self, MatchStrategy):
        self._MatchStrategy = MatchStrategy

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MatchStrategy = params.get("MatchStrategy")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWTokenLengthRoute(AbstractModel):
    r"""AI 网关token长度路由配置

    """

    def __init__(self):
        r"""
        :param _DefaultEncodingName: <p>默认tokenizer编码器</p><p>枚举值：</p><ul><li>o200k_base： OpenApi o200k_base</li><li>cl100k_base： OpenApi cl100k_base</li><li>p50k_base： OpenApi p50k_base</li><li>r50k_base： OpenApi r50k_base</li></ul>
        :type DefaultEncodingName: str
        :param _DefaultTarget: <p>token 计数失败、规则为空或未命中任何规则时执行的默认二级路由（暂时只能选择一个指定模型路由）</p>
        :type DefaultTarget: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMModelServiceSubRoute`
        :param _Rules: <p>规则</p>
        :type Rules: list of AIGWTokenLengthRouteRule
        """
        self._DefaultEncodingName = None
        self._DefaultTarget = None
        self._Rules = None

    @property
    def DefaultEncodingName(self):
        r"""<p>默认tokenizer编码器</p><p>枚举值：</p><ul><li>o200k_base： OpenApi o200k_base</li><li>cl100k_base： OpenApi cl100k_base</li><li>p50k_base： OpenApi p50k_base</li><li>r50k_base： OpenApi r50k_base</li></ul>
        :rtype: str
        """
        return self._DefaultEncodingName

    @DefaultEncodingName.setter
    def DefaultEncodingName(self, DefaultEncodingName):
        self._DefaultEncodingName = DefaultEncodingName

    @property
    def DefaultTarget(self):
        r"""<p>token 计数失败、规则为空或未命中任何规则时执行的默认二级路由（暂时只能选择一个指定模型路由）</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMModelServiceSubRoute`
        """
        return self._DefaultTarget

    @DefaultTarget.setter
    def DefaultTarget(self, DefaultTarget):
        self._DefaultTarget = DefaultTarget

    @property
    def Rules(self):
        r"""<p>规则</p>
        :rtype: list of AIGWTokenLengthRouteRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._DefaultEncodingName = params.get("DefaultEncodingName")
        if params.get("DefaultTarget") is not None:
            self._DefaultTarget = AIGWLLMModelServiceSubRoute()
            self._DefaultTarget._deserialize(params.get("DefaultTarget"))
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = AIGWTokenLengthRouteRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWTokenLengthRouteRule(AbstractModel):
    r"""AI 网关Token长度路由规则

    """

    def __init__(self):
        r"""
        :param _MinTokenLength: <p>token 长度下界，闭区间；0 合法</p>
        :type MinTokenLength: int
        :param _MaxTokenLength: <p>token 长度上界，闭区间</p>
        :type MaxTokenLength: int
        :param _Target: <p>命中该分段后执行的二级路由</p>
        :type Target: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMModelServiceSubRoute`
        """
        self._MinTokenLength = None
        self._MaxTokenLength = None
        self._Target = None

    @property
    def MinTokenLength(self):
        r"""<p>token 长度下界，闭区间；0 合法</p>
        :rtype: int
        """
        return self._MinTokenLength

    @MinTokenLength.setter
    def MinTokenLength(self, MinTokenLength):
        self._MinTokenLength = MinTokenLength

    @property
    def MaxTokenLength(self):
        r"""<p>token 长度上界，闭区间</p>
        :rtype: int
        """
        return self._MaxTokenLength

    @MaxTokenLength.setter
    def MaxTokenLength(self, MaxTokenLength):
        self._MaxTokenLength = MaxTokenLength

    @property
    def Target(self):
        r"""<p>命中该分段后执行的二级路由</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMModelServiceSubRoute`
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._MinTokenLength = params.get("MinTokenLength")
        self._MaxTokenLength = params.get("MaxTokenLength")
        if params.get("Target") is not None:
            self._Target = AIGWLLMModelServiceSubRoute()
            self._Target._deserialize(params.get("Target"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIGWTopConsumersItem(AbstractModel):
    r"""最高Token用量消费者

    """

    def __init__(self):
        r"""
        :param _ConsumerId: <p>消费者Id</p>
        :type ConsumerId: str
        :param _ConsumerName: <p>消费者名称</p>
        :type ConsumerName: str
        :param _TotalTokens: <p>该消费者花费的Token数</p>
        :type TotalTokens: int
        """
        self._ConsumerId = None
        self._ConsumerName = None
        self._TotalTokens = None

    @property
    def ConsumerId(self):
        r"""<p>消费者Id</p>
        :rtype: str
        """
        return self._ConsumerId

    @ConsumerId.setter
    def ConsumerId(self, ConsumerId):
        self._ConsumerId = ConsumerId

    @property
    def ConsumerName(self):
        r"""<p>消费者名称</p>
        :rtype: str
        """
        return self._ConsumerName

    @ConsumerName.setter
    def ConsumerName(self, ConsumerName):
        self._ConsumerName = ConsumerName

    @property
    def TotalTokens(self):
        r"""<p>该消费者花费的Token数</p>
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._ConsumerId = params.get("ConsumerId")
        self._ConsumerName = params.get("ConsumerName")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCloudNativeAPIGatewayConsumerGroupAuthRequest(AbstractModel):
    r"""AddCloudNativeAPIGatewayConsumerGroupAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例id</p>
        :type GatewayId: str
        :param _ResourceType: <p>授权资源类型。</p><p>枚举值：</p><ul><li>ModelAPI：模型 API</li><li>MCPServer：MCP Server</li></ul>
        :type ResourceType: str
        :param _ResourceId: <p>对应资源的 ID。</p><ul><li>ResourceType=ModelAPI 时是模型 API ID</li><li>ResourceType=MCPServer 时是 MCP Server ID</li></ul>
        :type ResourceId: str
        :param _ConsumerGroupIds: <p>消费者组 ID 列表（每个 ID 以 cg- 开头），长度 1-10。</p>
        :type ConsumerGroupIds: list of str
        """
        self._GatewayId = None
        self._ResourceType = None
        self._ResourceId = None
        self._ConsumerGroupIds = None

    @property
    def GatewayId(self):
        r"""<p>网关实例id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ResourceType(self):
        r"""<p>授权资源类型。</p><p>枚举值：</p><ul><li>ModelAPI：模型 API</li><li>MCPServer：MCP Server</li></ul>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceId(self):
        r"""<p>对应资源的 ID。</p><ul><li>ResourceType=ModelAPI 时是模型 API ID</li><li>ResourceType=MCPServer 时是 MCP Server ID</li></ul>
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ConsumerGroupIds(self):
        r"""<p>消费者组 ID 列表（每个 ID 以 cg- 开头），长度 1-10。</p>
        :rtype: list of str
        """
        return self._ConsumerGroupIds

    @ConsumerGroupIds.setter
    def ConsumerGroupIds(self, ConsumerGroupIds):
        self._ConsumerGroupIds = ConsumerGroupIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceId = params.get("ResourceId")
        self._ConsumerGroupIds = params.get("ConsumerGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCloudNativeAPIGatewayConsumerGroupAuthResponse(AbstractModel):
    r"""AddCloudNativeAPIGatewayConsumerGroupAuth返回参数结构体

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


class AddCloudNativeAPIGatewayConsumerInGroupRequest(AbstractModel):
    r"""AddCloudNativeAPIGatewayConsumerInGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _ConsumerGroupId: <p>消费者组 ID（以 cg- 开头）。</p>
        :type ConsumerGroupId: str
        :param _ConsumerIds: <p>消费者 ID 列表，长度 1-10。</p>
        :type ConsumerIds: list of str
        """
        self._GatewayId = None
        self._ConsumerGroupId = None
        self._ConsumerIds = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConsumerGroupId(self):
        r"""<p>消费者组 ID（以 cg- 开头）。</p>
        :rtype: str
        """
        return self._ConsumerGroupId

    @ConsumerGroupId.setter
    def ConsumerGroupId(self, ConsumerGroupId):
        self._ConsumerGroupId = ConsumerGroupId

    @property
    def ConsumerIds(self):
        r"""<p>消费者 ID 列表，长度 1-10。</p>
        :rtype: list of str
        """
        return self._ConsumerIds

    @ConsumerIds.setter
    def ConsumerIds(self, ConsumerIds):
        self._ConsumerIds = ConsumerIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ConsumerGroupId = params.get("ConsumerGroupId")
        self._ConsumerIds = params.get("ConsumerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCloudNativeAPIGatewayConsumerInGroupResponse(AbstractModel):
    r"""AddCloudNativeAPIGatewayConsumerInGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>是否成功。</p>
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>是否成功。</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindCloudNativeAPIGatewaySecretKeyRequest(AbstractModel):
    r"""BindCloudNativeAPIGatewaySecretKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceIds: 资源ID，当前最多支持一个
        :type ResourceIds: list of str
        :param _SecretKeyId: 密钥id
        :type SecretKeyId: str
        """
        self._GatewayId = None
        self._ResourceType = None
        self._ResourceIds = None
        self._SecretKeyId = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceIds(self):
        r"""资源ID，当前最多支持一个
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def SecretKeyId(self):
        r"""密钥id
        :rtype: str
        """
        return self._SecretKeyId

    @SecretKeyId.setter
    def SecretKeyId(self, SecretKeyId):
        self._SecretKeyId = SecretKeyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceIds = params.get("ResourceIds")
        self._SecretKeyId = params.get("SecretKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudNativeAPIGatewaySecretKeyResponse(AbstractModel):
    r"""BindCloudNativeAPIGatewaySecretKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""结果
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CNAPIGwConsumer(AbstractModel):
    r"""消费者结构

    """

    def __init__(self):
        r"""
        :param _ConsumerId: <p>消费者 ID。</p>
        :type ConsumerId: str
        :param _Name: <p>名字</p>
        :type Name: str
        :param _CreateTime: <p>创建时间</p>
        :type CreateTime: str
        :param _ModifyTime: <p>更新时间 yyyy-MM-dd hh:mm:ss</p>
        :type ModifyTime: str
        :param _Description: <p>描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ConsumerGroups: <p>消费者分组</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerGroups: list of CNAPIGwConsumerGroup
        """
        self._ConsumerId = None
        self._Name = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Description = None
        self._ConsumerGroups = None

    @property
    def ConsumerId(self):
        r"""<p>消费者 ID。</p>
        :rtype: str
        """
        return self._ConsumerId

    @ConsumerId.setter
    def ConsumerId(self, ConsumerId):
        self._ConsumerId = ConsumerId

    @property
    def Name(self):
        r"""<p>名字</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""<p>更新时间 yyyy-MM-dd hh:mm:ss</p>
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

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
    def ConsumerGroups(self):
        r"""<p>消费者分组</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CNAPIGwConsumerGroup
        """
        return self._ConsumerGroups

    @ConsumerGroups.setter
    def ConsumerGroups(self, ConsumerGroups):
        self._ConsumerGroups = ConsumerGroups


    def _deserialize(self, params):
        self._ConsumerId = params.get("ConsumerId")
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Description = params.get("Description")
        if params.get("ConsumerGroups") is not None:
            self._ConsumerGroups = []
            for item in params.get("ConsumerGroups"):
                obj = CNAPIGwConsumerGroup()
                obj._deserialize(item)
                self._ConsumerGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNAPIGwConsumerGroup(AbstractModel):
    r"""消费者组结构

    """

    def __init__(self):
        r"""
        :param _ConsumerGroupId: 分组id
        :type ConsumerGroupId: str
        :param _Name: 名字
        :type Name: str
        :param _Status: 状态Disable/Enable
        :type Status: str
        :param _Description: 描述
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 更新时间 yyyy-MM-dd hh:mm:ss
        :type ModifyTime: str
        :param _BindCount: 绑定的消费者数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BindCount: int
        """
        self._ConsumerGroupId = None
        self._Name = None
        self._Status = None
        self._Description = None
        self._CreateTime = None
        self._ModifyTime = None
        self._BindCount = None

    @property
    def ConsumerGroupId(self):
        r"""分组id
        :rtype: str
        """
        return self._ConsumerGroupId

    @ConsumerGroupId.setter
    def ConsumerGroupId(self, ConsumerGroupId):
        self._ConsumerGroupId = ConsumerGroupId

    @property
    def Name(self):
        r"""名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""状态Disable/Enable
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""更新时间 yyyy-MM-dd hh:mm:ss
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def BindCount(self):
        r"""绑定的消费者数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BindCount

    @BindCount.setter
    def BindCount(self, BindCount):
        self._BindCount = BindCount


    def _deserialize(self, params):
        self._ConsumerGroupId = params.get("ConsumerGroupId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._BindCount = params.get("BindCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNAPIGwCreateCommonResult(AbstractModel):
    r"""创建资源通用结果

    """

    def __init__(self):
        r"""
        :param _ID: 对应的id 值
        :type ID: str
        :param _Success: 是否成功
        :type Success: bool
        """
        self._ID = None
        self._Success = None

    @property
    def ID(self):
        r"""对应的id 值
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Success(self):
        r"""是否成功
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Success = params.get("Success")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNAPIGwMCPTool(AbstractModel):
    r"""MCP Tool 信息

    """

    def __init__(self):
        r"""
        :param _Name: <p>名字</p>
        :type Name: str
        :param _DisplayName: <p>展示名字</p>
        :type DisplayName: str
        :param _Method: <p>方法</p><p>枚举值：</p><ul><li>GET： GET</li><li>POST： POST</li><li>PUT： PUT</li><li>DELETE： DELETE</li><li>PATCH： PATCH</li></ul>
        :type Method: str
        :param _Description: <p>描述</p>
        :type Description: str
        :param _ToolId: <p>工具 id</p>
        :type ToolId: str
        :param _ContentType: <p>报文格式</p>
        :type ContentType: str
        :param _ServiceId: <p>服务 id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _Path: <p>路径</p>
        :type Path: str
        :param _InputParams: <p>参数</p>
        :type InputParams: list of CNAPIGwMCPToolParam
        :param _CreateTime: <p>创建时间</p><p>参数格式：yyyy-MM-dd hh:mm:ss</p>
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间</p><p>参数格式：yyyy-MM-dd hh:mm:ss</p>
        :type UpdateTime: str
        :param _Status: <p>tool状态</p><p>枚举值：</p><ul><li>Enable： 启用</li><li>Disable： 禁用</li></ul>
        :type Status: str
        :param _CurrentVersion: <p>当前版本号</p>
        :type CurrentVersion: str
        """
        self._Name = None
        self._DisplayName = None
        self._Method = None
        self._Description = None
        self._ToolId = None
        self._ContentType = None
        self._ServiceId = None
        self._Path = None
        self._InputParams = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._CurrentVersion = None

    @property
    def Name(self):
        r"""<p>名字</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DisplayName(self):
        r"""<p>展示名字</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Method(self):
        r"""<p>方法</p><p>枚举值：</p><ul><li>GET： GET</li><li>POST： POST</li><li>PUT： PUT</li><li>DELETE： DELETE</li><li>PATCH： PATCH</li></ul>
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

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
    def ToolId(self):
        r"""<p>工具 id</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ContentType(self):
        r"""<p>报文格式</p>
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def ServiceId(self):
        r"""<p>服务 id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Path(self):
        r"""<p>路径</p>
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def InputParams(self):
        r"""<p>参数</p>
        :rtype: list of CNAPIGwMCPToolParam
        """
        return self._InputParams

    @InputParams.setter
    def InputParams(self, InputParams):
        self._InputParams = InputParams

    @property
    def CreateTime(self):
        r"""<p>创建时间</p><p>参数格式：yyyy-MM-dd hh:mm:ss</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间</p><p>参数格式：yyyy-MM-dd hh:mm:ss</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        r"""<p>tool状态</p><p>枚举值：</p><ul><li>Enable： 启用</li><li>Disable： 禁用</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CurrentVersion(self):
        r"""<p>当前版本号</p>
        :rtype: str
        """
        return self._CurrentVersion

    @CurrentVersion.setter
    def CurrentVersion(self, CurrentVersion):
        self._CurrentVersion = CurrentVersion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DisplayName = params.get("DisplayName")
        self._Method = params.get("Method")
        self._Description = params.get("Description")
        self._ToolId = params.get("ToolId")
        self._ContentType = params.get("ContentType")
        self._ServiceId = params.get("ServiceId")
        self._Path = params.get("Path")
        if params.get("InputParams") is not None:
            self._InputParams = []
            for item in params.get("InputParams"):
                obj = CNAPIGwMCPToolParam()
                obj._deserialize(item)
                self._InputParams.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._CurrentVersion = params.get("CurrentVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNAPIGwMCPToolList(AbstractModel):
    r"""MCP Tool 列表

    """

    def __init__(self):
        r"""
        :param _DataList: <p>MCPTool 列表</p>
        :type DataList: list of CNAPIGwMCPTool
        :param _TotalCount: <p>总数</p>
        :type TotalCount: int
        """
        self._DataList = None
        self._TotalCount = None

    @property
    def DataList(self):
        r"""<p>MCPTool 列表</p>
        :rtype: list of CNAPIGwMCPTool
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def TotalCount(self):
        r"""<p>总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = CNAPIGwMCPTool()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNAPIGwMCPToolParam(AbstractModel):
    r"""MCP tool 参数

    """

    def __init__(self):
        r"""
        :param _Name: <p>名字</p>
        :type Name: str
        :param _Type: <p>参数类型</p><p>枚举值：</p><ul><li>string： 字符串</li><li>number： 数字</li><li>boolean： 布尔</li><li>array： 数组</li><li>object： 对象</li></ul>
        :type Type: str
        :param _Required: <p>必填</p>
        :type Required: bool
        :param _Position: <p>位置</p><p>枚举值：</p><ul><li>query： query</li><li>path： query</li><li>header： header</li><li>body： body</li></ul>
        :type Position: str
        :param _Description: <p>描述</p>
        :type Description: str
        :param _Default: <p>默认值</p>
        :type Default: str
        :param _Items: <p>数组子项</p>
        :type Items: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwMCPToolParam`
        :param _Properties: <p>对象属性</p>
        :type Properties: list of CNAPIGwMCPToolParam
        :param _BackendName: <p>转发到后端的名称</p><p>不填则使用原始名称</p>
        :type BackendName: str
        """
        self._Name = None
        self._Type = None
        self._Required = None
        self._Position = None
        self._Description = None
        self._Default = None
        self._Items = None
        self._Properties = None
        self._BackendName = None

    @property
    def Name(self):
        r"""<p>名字</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>参数类型</p><p>枚举值：</p><ul><li>string： 字符串</li><li>number： 数字</li><li>boolean： 布尔</li><li>array： 数组</li><li>object： 对象</li></ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Required(self):
        r"""<p>必填</p>
        :rtype: bool
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def Position(self):
        r"""<p>位置</p><p>枚举值：</p><ul><li>query： query</li><li>path： query</li><li>header： header</li><li>body： body</li></ul>
        :rtype: str
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

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
    def Default(self):
        r"""<p>默认值</p>
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Items(self):
        r"""<p>数组子项</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwMCPToolParam`
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Properties(self):
        r"""<p>对象属性</p>
        :rtype: list of CNAPIGwMCPToolParam
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def BackendName(self):
        r"""<p>转发到后端的名称</p><p>不填则使用原始名称</p>
        :rtype: str
        """
        return self._BackendName

    @BackendName.setter
    def BackendName(self, BackendName):
        self._BackendName = BackendName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Required = params.get("Required")
        self._Position = params.get("Position")
        self._Description = params.get("Description")
        self._Default = params.get("Default")
        if params.get("Items") is not None:
            self._Items = CNAPIGwMCPToolParam()
            self._Items._deserialize(params.get("Items"))
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = CNAPIGwMCPToolParam()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._BackendName = params.get("BackendName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNAPIGwMCPToolPreview(AbstractModel):
    r"""通过OpenAPI文件导入MCP tools的预览内容

    """

    def __init__(self):
        r"""
        :param _ContentType: <p>MCP Tool入参的ContentType</p><p>枚举值：</p><ul><li>application/json： json格式</li><li>application/x-www-form-urlencoded： 表单格式</li></ul>
        :type ContentType: str
        :param _Description: <p>MCP Tool的描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _InputParams: <p>MCP Tool的参数</p>
        :type InputParams: list of CNAPIGwMCPToolParam
        :param _Method: <p>MCP Tool的请求方法</p>
        :type Method: str
        :param _Name: <p>MCP Tool名字</p>
        :type Name: str
        :param _Path: <p>MCP Tool的请求路径</p>
        :type Path: str
        :param _Status: <p>MCP Tool的状态</p><p>枚举值：</p><ul><li>Valid： 可导入</li><li>Invalid： 不可导入</li></ul>
        :type Status: str
        :param _StatusMessage: <p>不可导入的原因</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMessage: str
        :param _UpstreamUrl: <p>虚拟MCP Server的tools的完整url路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamUrl: str
        """
        self._ContentType = None
        self._Description = None
        self._InputParams = None
        self._Method = None
        self._Name = None
        self._Path = None
        self._Status = None
        self._StatusMessage = None
        self._UpstreamUrl = None

    @property
    def ContentType(self):
        r"""<p>MCP Tool入参的ContentType</p><p>枚举值：</p><ul><li>application/json： json格式</li><li>application/x-www-form-urlencoded： 表单格式</li></ul>
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Description(self):
        r"""<p>MCP Tool的描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InputParams(self):
        r"""<p>MCP Tool的参数</p>
        :rtype: list of CNAPIGwMCPToolParam
        """
        return self._InputParams

    @InputParams.setter
    def InputParams(self, InputParams):
        self._InputParams = InputParams

    @property
    def Method(self):
        r"""<p>MCP Tool的请求方法</p>
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Name(self):
        r"""<p>MCP Tool名字</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Path(self):
        r"""<p>MCP Tool的请求路径</p>
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Status(self):
        r"""<p>MCP Tool的状态</p><p>枚举值：</p><ul><li>Valid： 可导入</li><li>Invalid： 不可导入</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMessage(self):
        r"""<p>不可导入的原因</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusMessage

    @StatusMessage.setter
    def StatusMessage(self, StatusMessage):
        self._StatusMessage = StatusMessage

    @property
    def UpstreamUrl(self):
        r"""<p>虚拟MCP Server的tools的完整url路径</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpstreamUrl

    @UpstreamUrl.setter
    def UpstreamUrl(self, UpstreamUrl):
        self._UpstreamUrl = UpstreamUrl


    def _deserialize(self, params):
        self._ContentType = params.get("ContentType")
        self._Description = params.get("Description")
        if params.get("InputParams") is not None:
            self._InputParams = []
            for item in params.get("InputParams"):
                obj = CNAPIGwMCPToolParam()
                obj._deserialize(item)
                self._InputParams.append(obj)
        self._Method = params.get("Method")
        self._Name = params.get("Name")
        self._Path = params.get("Path")
        self._Status = params.get("Status")
        self._StatusMessage = params.get("StatusMessage")
        self._UpstreamUrl = params.get("UpstreamUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNAPIGwParseMCPToolsResult(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPToolsFromFile接口的出参

    """

    def __init__(self):
        r"""
        :param _DataList: <p>MCP Tools列表</p>
        :type DataList: list of CNAPIGwMCPToolPreview
        :param _TotalCount: <p>MCP tools的数量</p>
        :type TotalCount: int
        """
        self._DataList = None
        self._TotalCount = None

    @property
    def DataList(self):
        r"""<p>MCP Tools列表</p>
        :rtype: list of CNAPIGwMCPToolPreview
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def TotalCount(self):
        r"""<p>MCP tools的数量</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = CNAPIGwMCPToolPreview()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNAPIGwSecretKey(AbstractModel):
    r"""密钥信息

    """

    def __init__(self):
        r"""
        :param _BindCount: <p>绑定数</p>
        :type BindCount: int
        :param _CanBind: <p>是否可以绑定</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CanBind: bool
        :param _CreateTime: <p>创建时间</p>
        :type CreateTime: str
        :param _Description: <p>描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _GenerateType: <p>密钥生成方式。</p><p>枚举值：</p><ul><li>System： 系统自动生成</li><li>Custom： 用户自定义</li><li>KMS： 使用 KMS 密钥</li></ul>
        :type GenerateType: str
        :param _JWTCredentialConfig: <p>JWT凭证配置</p>
        :type JWTCredentialConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWJWTCredentialConfig`
        :param _KmsKeyName: <p>KMS凭证名字</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsKeyName: str
        :param _KmsKeyVersion: <p>KMS凭证版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsKeyVersion: str
        :param _ModifyTime: <p>修改时间</p>
        :type ModifyTime: str
        :param _Name: <p>密钥名字</p>
        :type Name: str
        :param _OAuthCredentialConfig: <p>OAuth凭证配置</p>
        :type OAuthCredentialConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWOAuthCredentialConfig`
        :param _OIDCCredentialConfig: <p>OIDC凭证配置</p>
        :type OIDCCredentialConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWOIDCCredentialConfig`
        :param _Provider: <p>secret key provider方</p><p>枚举值：</p><ul><li>Dify： Dify</li></ul>
        :type Provider: str
        :param _ResourceType: <p>密钥归属资源类型。</p><p>枚举值：</p><ul><li>Consumer： 消费者</li><li>ModelService： 模型服务</li></ul>
        :type ResourceType: str
        :param _SecretKeyId: <p>密钥id</p>
        :type SecretKeyId: str
        :param _SecretType: <p>密钥协议类型。</p>
        :type SecretType: str
        :param _SecretValue: <p>密钥明文</p>
        :type SecretValue: str
        :param _Status: <p>状态。</p><p>枚举值：</p><ul><li>Enable： 启用</li><li>Disable： 禁用</li></ul>
        :type Status: str
        """
        self._BindCount = None
        self._CanBind = None
        self._CreateTime = None
        self._Description = None
        self._GenerateType = None
        self._JWTCredentialConfig = None
        self._KmsKeyName = None
        self._KmsKeyVersion = None
        self._ModifyTime = None
        self._Name = None
        self._OAuthCredentialConfig = None
        self._OIDCCredentialConfig = None
        self._Provider = None
        self._ResourceType = None
        self._SecretKeyId = None
        self._SecretType = None
        self._SecretValue = None
        self._Status = None

    @property
    def BindCount(self):
        r"""<p>绑定数</p>
        :rtype: int
        """
        return self._BindCount

    @BindCount.setter
    def BindCount(self, BindCount):
        self._BindCount = BindCount

    @property
    def CanBind(self):
        r"""<p>是否可以绑定</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanBind

    @CanBind.setter
    def CanBind(self, CanBind):
        self._CanBind = CanBind

    @property
    def CreateTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def GenerateType(self):
        r"""<p>密钥生成方式。</p><p>枚举值：</p><ul><li>System： 系统自动生成</li><li>Custom： 用户自定义</li><li>KMS： 使用 KMS 密钥</li></ul>
        :rtype: str
        """
        return self._GenerateType

    @GenerateType.setter
    def GenerateType(self, GenerateType):
        self._GenerateType = GenerateType

    @property
    def JWTCredentialConfig(self):
        r"""<p>JWT凭证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWJWTCredentialConfig`
        """
        return self._JWTCredentialConfig

    @JWTCredentialConfig.setter
    def JWTCredentialConfig(self, JWTCredentialConfig):
        self._JWTCredentialConfig = JWTCredentialConfig

    @property
    def KmsKeyName(self):
        r"""<p>KMS凭证名字</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KmsKeyName

    @KmsKeyName.setter
    def KmsKeyName(self, KmsKeyName):
        self._KmsKeyName = KmsKeyName

    @property
    def KmsKeyVersion(self):
        r"""<p>KMS凭证版本</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KmsKeyVersion

    @KmsKeyVersion.setter
    def KmsKeyVersion(self, KmsKeyVersion):
        self._KmsKeyVersion = KmsKeyVersion

    @property
    def ModifyTime(self):
        r"""<p>修改时间</p>
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Name(self):
        r"""<p>密钥名字</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OAuthCredentialConfig(self):
        r"""<p>OAuth凭证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWOAuthCredentialConfig`
        """
        return self._OAuthCredentialConfig

    @OAuthCredentialConfig.setter
    def OAuthCredentialConfig(self, OAuthCredentialConfig):
        self._OAuthCredentialConfig = OAuthCredentialConfig

    @property
    def OIDCCredentialConfig(self):
        r"""<p>OIDC凭证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWOIDCCredentialConfig`
        """
        return self._OIDCCredentialConfig

    @OIDCCredentialConfig.setter
    def OIDCCredentialConfig(self, OIDCCredentialConfig):
        self._OIDCCredentialConfig = OIDCCredentialConfig

    @property
    def Provider(self):
        r"""<p>secret key provider方</p><p>枚举值：</p><ul><li>Dify： Dify</li></ul>
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def ResourceType(self):
        r"""<p>密钥归属资源类型。</p><p>枚举值：</p><ul><li>Consumer： 消费者</li><li>ModelService： 模型服务</li></ul>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def SecretKeyId(self):
        r"""<p>密钥id</p>
        :rtype: str
        """
        return self._SecretKeyId

    @SecretKeyId.setter
    def SecretKeyId(self, SecretKeyId):
        self._SecretKeyId = SecretKeyId

    @property
    def SecretType(self):
        r"""<p>密钥协议类型。</p>
        :rtype: str
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def SecretValue(self):
        r"""<p>密钥明文</p>
        :rtype: str
        """
        return self._SecretValue

    @SecretValue.setter
    def SecretValue(self, SecretValue):
        self._SecretValue = SecretValue

    @property
    def Status(self):
        r"""<p>状态。</p><p>枚举值：</p><ul><li>Enable： 启用</li><li>Disable： 禁用</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BindCount = params.get("BindCount")
        self._CanBind = params.get("CanBind")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._GenerateType = params.get("GenerateType")
        if params.get("JWTCredentialConfig") is not None:
            self._JWTCredentialConfig = AIGWJWTCredentialConfig()
            self._JWTCredentialConfig._deserialize(params.get("JWTCredentialConfig"))
        self._KmsKeyName = params.get("KmsKeyName")
        self._KmsKeyVersion = params.get("KmsKeyVersion")
        self._ModifyTime = params.get("ModifyTime")
        self._Name = params.get("Name")
        if params.get("OAuthCredentialConfig") is not None:
            self._OAuthCredentialConfig = AIGWOAuthCredentialConfig()
            self._OAuthCredentialConfig._deserialize(params.get("OAuthCredentialConfig"))
        if params.get("OIDCCredentialConfig") is not None:
            self._OIDCCredentialConfig = AIGWOIDCCredentialConfig()
            self._OIDCCredentialConfig._deserialize(params.get("OIDCCredentialConfig"))
        self._Provider = params.get("Provider")
        self._ResourceType = params.get("ResourceType")
        self._SecretKeyId = params.get("SecretKeyId")
        self._SecretType = params.get("SecretType")
        self._SecretValue = params.get("SecretValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayLLMModelAPI(AbstractModel):
    r"""LLM 模型 API

    """

    def __init__(self):
        r"""
        :param _Id: <p>模型 API ID。</p>
        :type Id: str
        :param _CreateTime: <p>创建时间</p>
        :type CreateTime: str
        :param _ModifyTime: <p>修改时间</p>
        :type ModifyTime: str
        :param _Name: <p>AI 网关 LLM 模型 API 的唯一标识名称，格式规则：2-50 字符，支持英文、数字、下划线。</p>
        :type Name: str
        :param _SceneType: <p>选择业务场景,xa0 选项：Chat（聊天）。</p>
        :type SceneType: str
        :param _RequestProtocol: <p>业务场景对应的请求协议，选项：OpenAI（目前只支持 OpenAI）。</p>
        :type RequestProtocol: str
        :param _RouteList: <p>路由列表</p>
        :type RouteList: list of DefaultKongRoute
        :param _BasePath: <p>为API设置统一的前缀，格式：以/开头，支持字母、数字、短横线。</p>
        :type BasePath: str
        :param _StripPath: <p>路径简化，<br>启用时：客户端请求路径 → 移除Base Path → 后端接收简洁路径<br>禁用时：客户端请求路径 → 完整传递给后端。</p>
        :type StripPath: bool
        :param _Description: <p>模型 API 的相关描述。</p>
        :type Description: str
        :param _ModelServiceId: <p>模型服务Id</p>
        :type ModelServiceId: str
        :param _ModelServiceName: <p>模型服务名称</p>
        :type ModelServiceName: str
        :param _ModelServiceRoute: <p>模型服务路由策略（是指如何路由到模型服务）</p>
        :type ModelServiceRoute: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelServiceRoute`
        :param _MatchHeaders: <p>HTTP 请求头匹配规则，用于按请求头路由到不同模型服务。</p>
        :type MatchHeaders: list of AIGWKVMatch
        :param _EnableCrossServiceFallback: <p>是否开启跨服务fallback</p>
        :type EnableCrossServiceFallback: bool
        :param _CrossServiceFallbackConfig: <p>跨服务fallback配置详情</p>
        :type CrossServiceFallbackConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWCrossServiceFallbackConfig`
        :param _DescribeCloudNativeAPIGatewayLLMModelAPI: <p>是否展示模型API</p>
        :type DescribeCloudNativeAPIGatewayLLMModelAPI: bool
        :param _TagFilter: <p>标签</p>
        :type TagFilter: :class:`tencentcloud.cngw.v20230418.models.AIGWTagFilter`
        :param _LogConfig: <p>日志显示相关开关</p>
        :type LogConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWLogConfig`
        :param _LogDesensitizeConfig: <p>日志脱敏规则</p>
        :type LogDesensitizeConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWLogDesensitizeConfig`
        :param _ForwardDesensitizeConfig: <p>转发脱敏规则</p>
        :type ForwardDesensitizeConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWForwardDesensitizeConfig`
        """
        self._Id = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Name = None
        self._SceneType = None
        self._RequestProtocol = None
        self._RouteList = None
        self._BasePath = None
        self._StripPath = None
        self._Description = None
        self._ModelServiceId = None
        self._ModelServiceName = None
        self._ModelServiceRoute = None
        self._MatchHeaders = None
        self._EnableCrossServiceFallback = None
        self._CrossServiceFallbackConfig = None
        self._DescribeCloudNativeAPIGatewayLLMModelAPI = None
        self._TagFilter = None
        self._LogConfig = None
        self._LogDesensitizeConfig = None
        self._ForwardDesensitizeConfig = None

    @property
    def Id(self):
        r"""<p>模型 API ID。</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CreateTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""<p>修改时间</p>
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Name(self):
        r"""<p>AI 网关 LLM 模型 API 的唯一标识名称，格式规则：2-50 字符，支持英文、数字、下划线。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SceneType(self):
        r"""<p>选择业务场景,xa0 选项：Chat（聊天）。</p>
        :rtype: str
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def RequestProtocol(self):
        r"""<p>业务场景对应的请求协议，选项：OpenAI（目前只支持 OpenAI）。</p>
        :rtype: str
        """
        return self._RequestProtocol

    @RequestProtocol.setter
    def RequestProtocol(self, RequestProtocol):
        self._RequestProtocol = RequestProtocol

    @property
    def RouteList(self):
        r"""<p>路由列表</p>
        :rtype: list of DefaultKongRoute
        """
        return self._RouteList

    @RouteList.setter
    def RouteList(self, RouteList):
        self._RouteList = RouteList

    @property
    def BasePath(self):
        r"""<p>为API设置统一的前缀，格式：以/开头，支持字母、数字、短横线。</p>
        :rtype: str
        """
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def StripPath(self):
        r"""<p>路径简化，<br>启用时：客户端请求路径 → 移除Base Path → 后端接收简洁路径<br>禁用时：客户端请求路径 → 完整传递给后端。</p>
        :rtype: bool
        """
        return self._StripPath

    @StripPath.setter
    def StripPath(self, StripPath):
        self._StripPath = StripPath

    @property
    def Description(self):
        r"""<p>模型 API 的相关描述。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ModelServiceId(self):
        r"""<p>模型服务Id</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId

    @property
    def ModelServiceName(self):
        r"""<p>模型服务名称</p>
        :rtype: str
        """
        return self._ModelServiceName

    @ModelServiceName.setter
    def ModelServiceName(self, ModelServiceName):
        self._ModelServiceName = ModelServiceName

    @property
    def ModelServiceRoute(self):
        r"""<p>模型服务路由策略（是指如何路由到模型服务）</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelServiceRoute`
        """
        return self._ModelServiceRoute

    @ModelServiceRoute.setter
    def ModelServiceRoute(self, ModelServiceRoute):
        self._ModelServiceRoute = ModelServiceRoute

    @property
    def MatchHeaders(self):
        r"""<p>HTTP 请求头匹配规则，用于按请求头路由到不同模型服务。</p>
        :rtype: list of AIGWKVMatch
        """
        return self._MatchHeaders

    @MatchHeaders.setter
    def MatchHeaders(self, MatchHeaders):
        self._MatchHeaders = MatchHeaders

    @property
    def EnableCrossServiceFallback(self):
        r"""<p>是否开启跨服务fallback</p>
        :rtype: bool
        """
        return self._EnableCrossServiceFallback

    @EnableCrossServiceFallback.setter
    def EnableCrossServiceFallback(self, EnableCrossServiceFallback):
        self._EnableCrossServiceFallback = EnableCrossServiceFallback

    @property
    def CrossServiceFallbackConfig(self):
        r"""<p>跨服务fallback配置详情</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWCrossServiceFallbackConfig`
        """
        return self._CrossServiceFallbackConfig

    @CrossServiceFallbackConfig.setter
    def CrossServiceFallbackConfig(self, CrossServiceFallbackConfig):
        self._CrossServiceFallbackConfig = CrossServiceFallbackConfig

    @property
    def DescribeCloudNativeAPIGatewayLLMModelAPI(self):
        r"""<p>是否展示模型API</p>
        :rtype: bool
        """
        return self._DescribeCloudNativeAPIGatewayLLMModelAPI

    @DescribeCloudNativeAPIGatewayLLMModelAPI.setter
    def DescribeCloudNativeAPIGatewayLLMModelAPI(self, DescribeCloudNativeAPIGatewayLLMModelAPI):
        self._DescribeCloudNativeAPIGatewayLLMModelAPI = DescribeCloudNativeAPIGatewayLLMModelAPI

    @property
    def TagFilter(self):
        r"""<p>标签</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWTagFilter`
        """
        return self._TagFilter

    @TagFilter.setter
    def TagFilter(self, TagFilter):
        self._TagFilter = TagFilter

    @property
    def LogConfig(self):
        r"""<p>日志显示相关开关</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLogConfig`
        """
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def LogDesensitizeConfig(self):
        r"""<p>日志脱敏规则</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLogDesensitizeConfig`
        """
        return self._LogDesensitizeConfig

    @LogDesensitizeConfig.setter
    def LogDesensitizeConfig(self, LogDesensitizeConfig):
        self._LogDesensitizeConfig = LogDesensitizeConfig

    @property
    def ForwardDesensitizeConfig(self):
        r"""<p>转发脱敏规则</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWForwardDesensitizeConfig`
        """
        return self._ForwardDesensitizeConfig

    @ForwardDesensitizeConfig.setter
    def ForwardDesensitizeConfig(self, ForwardDesensitizeConfig):
        self._ForwardDesensitizeConfig = ForwardDesensitizeConfig


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Name = params.get("Name")
        self._SceneType = params.get("SceneType")
        self._RequestProtocol = params.get("RequestProtocol")
        if params.get("RouteList") is not None:
            self._RouteList = []
            for item in params.get("RouteList"):
                obj = DefaultKongRoute()
                obj._deserialize(item)
                self._RouteList.append(obj)
        self._BasePath = params.get("BasePath")
        self._StripPath = params.get("StripPath")
        self._Description = params.get("Description")
        self._ModelServiceId = params.get("ModelServiceId")
        self._ModelServiceName = params.get("ModelServiceName")
        if params.get("ModelServiceRoute") is not None:
            self._ModelServiceRoute = CloudNativeAPIGatewayLLMModelServiceRoute()
            self._ModelServiceRoute._deserialize(params.get("ModelServiceRoute"))
        if params.get("MatchHeaders") is not None:
            self._MatchHeaders = []
            for item in params.get("MatchHeaders"):
                obj = AIGWKVMatch()
                obj._deserialize(item)
                self._MatchHeaders.append(obj)
        self._EnableCrossServiceFallback = params.get("EnableCrossServiceFallback")
        if params.get("CrossServiceFallbackConfig") is not None:
            self._CrossServiceFallbackConfig = AIGWCrossServiceFallbackConfig()
            self._CrossServiceFallbackConfig._deserialize(params.get("CrossServiceFallbackConfig"))
        self._DescribeCloudNativeAPIGatewayLLMModelAPI = params.get("DescribeCloudNativeAPIGatewayLLMModelAPI")
        if params.get("TagFilter") is not None:
            self._TagFilter = AIGWTagFilter()
            self._TagFilter._deserialize(params.get("TagFilter"))
        if params.get("LogConfig") is not None:
            self._LogConfig = AIGWLogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        if params.get("LogDesensitizeConfig") is not None:
            self._LogDesensitizeConfig = AIGWLogDesensitizeConfig()
            self._LogDesensitizeConfig._deserialize(params.get("LogDesensitizeConfig"))
        if params.get("ForwardDesensitizeConfig") is not None:
            self._ForwardDesensitizeConfig = AIGWForwardDesensitizeConfig()
            self._ForwardDesensitizeConfig._deserialize(params.get("ForwardDesensitizeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayLLMModelFallbackRule(AbstractModel):
    r"""LLM-单模型内降级规则

    """

    def __init__(self):
        r"""
        :param _FallbackModels: 备选模型，主模型不可用时将依次按顺序尝试。
        :type FallbackModels: list of str
        """
        self._FallbackModels = None

    @property
    def FallbackModels(self):
        r"""备选模型，主模型不可用时将依次按顺序尝试。
        :rtype: list of str
        """
        return self._FallbackModels

    @FallbackModels.setter
    def FallbackModels(self, FallbackModels):
        self._FallbackModels = FallbackModels


    def _deserialize(self, params):
        self._FallbackModels = params.get("FallbackModels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayLLMModelParamCheckInfo(AbstractModel):
    r"""LLM-模型参数检查信息

    """

    def __init__(self):
        r"""
        :param _AllowModelList: 允许的模型列表。
        :type AllowModelList: list of str
        :param _ModelValidationFailureStrategy: 模型参数校验失败时的处理策略，选项：Return404（返回404）、FallBackToDefaultModel（使用默认模型降级）。
        :type ModelValidationFailureStrategy: str
        """
        self._AllowModelList = None
        self._ModelValidationFailureStrategy = None

    @property
    def AllowModelList(self):
        r"""允许的模型列表。
        :rtype: list of str
        """
        return self._AllowModelList

    @AllowModelList.setter
    def AllowModelList(self, AllowModelList):
        self._AllowModelList = AllowModelList

    @property
    def ModelValidationFailureStrategy(self):
        r"""模型参数校验失败时的处理策略，选项：Return404（返回404）、FallBackToDefaultModel（使用默认模型降级）。
        :rtype: str
        """
        return self._ModelValidationFailureStrategy

    @ModelValidationFailureStrategy.setter
    def ModelValidationFailureStrategy(self, ModelValidationFailureStrategy):
        self._ModelValidationFailureStrategy = ModelValidationFailureStrategy


    def _deserialize(self, params):
        self._AllowModelList = params.get("AllowModelList")
        self._ModelValidationFailureStrategy = params.get("ModelValidationFailureStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayLLMModelService(AbstractModel):
    r"""LLM 模型服务

    """

    def __init__(self):
        r"""
        :param _Id: <p>模型服务 ID。</p>
        :type Id: str
        :param _Name: <p>模型服务名称。</p>
        :type Name: str
        :param _CreateTime: <p>创建时间。</p>
        :type CreateTime: str
        :param _ModifyTime: <p>修改时间。</p>
        :type ModifyTime: str
        :param _ServiceType: <p>服务类型，目前只支持xa0LLMService。</p>
        :type ServiceType: str
        :param _ModelProvider: <p>选择模型提供商, 选项：OpenAI、Anthropic、Azure OpenAI、自定义HTTP。</p>
        :type ModelProvider: str
        :param _ModelProtocol: <p>API协议标准，根据供应商动态变化：OpenAI→OpenAI/v1，Anthropic→Anthropic/v1等</p>
        :type ModelProtocol: str
        :param _UpstreamURL: <p>自定义的模型请求 URL。</p>
        :type UpstreamURL: str
        :param _ModelSelector: <p>模型选择方式，选项：Specify（指定模型）、PassThrough（透传请求模型）。</p>
        :type ModelSelector: str
        :param _DefaultModel: <p>默认模型，模型选择方式为 Specify 时必填。</p>
        :type DefaultModel: str
        :param _EnableModelFallback: <p>开启模型降级，模型选择方式为 Specify 时必填。</p>
        :type EnableModelFallback: bool
        :param _ModelFallbackRule: <p>可以配置备用模型规则，EnableSpecifyModelFallbackxa0为 true 时必填。</p>
        :type ModelFallbackRule: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelFallbackRule`
        :param _EnableModelParamCheck: <p>开启模型参数校验，是否校验客户端传递的 model 参数,xa0模型选择方式为 PassThrough 时必填。</p>
        :type EnableModelParamCheck: bool
        :param _ModelParamCheckRule: <p>模型检验信息，EnableModelParamCheckxa0为 true 时必填。</p>
        :type ModelParamCheckRule: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelParamCheckInfo`
        :param _Description: <p>描述。</p>
        :type Description: str
        :param _ConnectTimeout: <p>连接超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：10000</p>
        :type ConnectTimeout: int
        :param _WriteTimeout: <p>写入超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :type WriteTimeout: int
        :param _ReadTimeout: <p>读取超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p>
        :type ReadTimeout: int
        :param _Retries: <p>重试次数</p><p>取值范围：[0, 5]</p><p>单位：次</p><p>默认值：0</p>
        :type Retries: int
        :param _UpstreamUrlMode: <p>路径拼接模式</p><p>枚举值：</p><ul><li>FixedPath： 固定路径</li><li>AutoConcat： 自动拼接</li></ul>
        :type UpstreamUrlMode: str
        :param _SNI: <p>sni</p>
        :type SNI: str
        :param _QuotaLimit: <p>配额限制</p>
        :type QuotaLimit: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMQuotaLimit`
        :param _Tags: <p>标签</p>
        :type Tags: str
        :param _SecretKeyIds: <p>绑定的模型服务秘钥</p>
        :type SecretKeyIds: list of str
        :param _ModelRewriteRules: <p>模型改写规则</p>
        :type ModelRewriteRules: list of AIGWModelRewriteRule
        :param _SourceId: <p>服务来源</p>
        :type SourceId: str
        :param _Namespace: <p>命名空间</p>
        :type Namespace: str
        :param _ServiceName: <p>服务名称</p>
        :type ServiceName: str
        :param _Protocol: <p>命名空间</p>
        :type Protocol: str
        :param _ExtParams: <p>扩展参数</p>
        :type ExtParams: list of KeyValue
        :param _CustomProviderName: <p>模型自定义供应商名称</p>
        :type CustomProviderName: str
        :param _KeyRotationEnabled: <p>是否开启密钥轮转</p>
        :type KeyRotationEnabled: bool
        :param _KeyRotationPeriodDays: <p>密钥轮转周期</p><p>单位：天</p>
        :type KeyRotationPeriodDays: int
        :param _ExternalInstanceId: <p>外部服务来源ID</p>
        :type ExternalInstanceId: str
        """
        self._Id = None
        self._Name = None
        self._CreateTime = None
        self._ModifyTime = None
        self._ServiceType = None
        self._ModelProvider = None
        self._ModelProtocol = None
        self._UpstreamURL = None
        self._ModelSelector = None
        self._DefaultModel = None
        self._EnableModelFallback = None
        self._ModelFallbackRule = None
        self._EnableModelParamCheck = None
        self._ModelParamCheckRule = None
        self._Description = None
        self._ConnectTimeout = None
        self._WriteTimeout = None
        self._ReadTimeout = None
        self._Retries = None
        self._UpstreamUrlMode = None
        self._SNI = None
        self._QuotaLimit = None
        self._Tags = None
        self._SecretKeyIds = None
        self._ModelRewriteRules = None
        self._SourceId = None
        self._Namespace = None
        self._ServiceName = None
        self._Protocol = None
        self._ExtParams = None
        self._CustomProviderName = None
        self._KeyRotationEnabled = None
        self._KeyRotationPeriodDays = None
        self._ExternalInstanceId = None

    @property
    def Id(self):
        r"""<p>模型服务 ID。</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""<p>模型服务名称。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        r"""<p>创建时间。</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""<p>修改时间。</p>
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ServiceType(self):
        r"""<p>服务类型，目前只支持xa0LLMService。</p>
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ModelProvider(self):
        r"""<p>选择模型提供商, 选项：OpenAI、Anthropic、Azure OpenAI、自定义HTTP。</p>
        :rtype: str
        """
        return self._ModelProvider

    @ModelProvider.setter
    def ModelProvider(self, ModelProvider):
        self._ModelProvider = ModelProvider

    @property
    def ModelProtocol(self):
        r"""<p>API协议标准，根据供应商动态变化：OpenAI→OpenAI/v1，Anthropic→Anthropic/v1等</p>
        :rtype: str
        """
        return self._ModelProtocol

    @ModelProtocol.setter
    def ModelProtocol(self, ModelProtocol):
        self._ModelProtocol = ModelProtocol

    @property
    def UpstreamURL(self):
        r"""<p>自定义的模型请求 URL。</p>
        :rtype: str
        """
        return self._UpstreamURL

    @UpstreamURL.setter
    def UpstreamURL(self, UpstreamURL):
        self._UpstreamURL = UpstreamURL

    @property
    def ModelSelector(self):
        r"""<p>模型选择方式，选项：Specify（指定模型）、PassThrough（透传请求模型）。</p>
        :rtype: str
        """
        return self._ModelSelector

    @ModelSelector.setter
    def ModelSelector(self, ModelSelector):
        self._ModelSelector = ModelSelector

    @property
    def DefaultModel(self):
        r"""<p>默认模型，模型选择方式为 Specify 时必填。</p>
        :rtype: str
        """
        return self._DefaultModel

    @DefaultModel.setter
    def DefaultModel(self, DefaultModel):
        self._DefaultModel = DefaultModel

    @property
    def EnableModelFallback(self):
        r"""<p>开启模型降级，模型选择方式为 Specify 时必填。</p>
        :rtype: bool
        """
        return self._EnableModelFallback

    @EnableModelFallback.setter
    def EnableModelFallback(self, EnableModelFallback):
        self._EnableModelFallback = EnableModelFallback

    @property
    def ModelFallbackRule(self):
        r"""<p>可以配置备用模型规则，EnableSpecifyModelFallbackxa0为 true 时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelFallbackRule`
        """
        return self._ModelFallbackRule

    @ModelFallbackRule.setter
    def ModelFallbackRule(self, ModelFallbackRule):
        self._ModelFallbackRule = ModelFallbackRule

    @property
    def EnableModelParamCheck(self):
        r"""<p>开启模型参数校验，是否校验客户端传递的 model 参数,xa0模型选择方式为 PassThrough 时必填。</p>
        :rtype: bool
        """
        return self._EnableModelParamCheck

    @EnableModelParamCheck.setter
    def EnableModelParamCheck(self, EnableModelParamCheck):
        self._EnableModelParamCheck = EnableModelParamCheck

    @property
    def ModelParamCheckRule(self):
        r"""<p>模型检验信息，EnableModelParamCheckxa0为 true 时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelParamCheckInfo`
        """
        return self._ModelParamCheckRule

    @ModelParamCheckRule.setter
    def ModelParamCheckRule(self, ModelParamCheckRule):
        self._ModelParamCheckRule = ModelParamCheckRule

    @property
    def Description(self):
        r"""<p>描述。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConnectTimeout(self):
        r"""<p>连接超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：10000</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def WriteTimeout(self):
        r"""<p>写入超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :rtype: int
        """
        return self._WriteTimeout

    @WriteTimeout.setter
    def WriteTimeout(self, WriteTimeout):
        self._WriteTimeout = WriteTimeout

    @property
    def ReadTimeout(self):
        r"""<p>读取超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p>
        :rtype: int
        """
        return self._ReadTimeout

    @ReadTimeout.setter
    def ReadTimeout(self, ReadTimeout):
        self._ReadTimeout = ReadTimeout

    @property
    def Retries(self):
        r"""<p>重试次数</p><p>取值范围：[0, 5]</p><p>单位：次</p><p>默认值：0</p>
        :rtype: int
        """
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamUrlMode(self):
        r"""<p>路径拼接模式</p><p>枚举值：</p><ul><li>FixedPath： 固定路径</li><li>AutoConcat： 自动拼接</li></ul>
        :rtype: str
        """
        return self._UpstreamUrlMode

    @UpstreamUrlMode.setter
    def UpstreamUrlMode(self, UpstreamUrlMode):
        self._UpstreamUrlMode = UpstreamUrlMode

    @property
    def SNI(self):
        r"""<p>sni</p>
        :rtype: str
        """
        return self._SNI

    @SNI.setter
    def SNI(self, SNI):
        self._SNI = SNI

    @property
    def QuotaLimit(self):
        r"""<p>配额限制</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMQuotaLimit`
        """
        return self._QuotaLimit

    @QuotaLimit.setter
    def QuotaLimit(self, QuotaLimit):
        self._QuotaLimit = QuotaLimit

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SecretKeyIds(self):
        r"""<p>绑定的模型服务秘钥</p>
        :rtype: list of str
        """
        return self._SecretKeyIds

    @SecretKeyIds.setter
    def SecretKeyIds(self, SecretKeyIds):
        self._SecretKeyIds = SecretKeyIds

    @property
    def ModelRewriteRules(self):
        r"""<p>模型改写规则</p>
        :rtype: list of AIGWModelRewriteRule
        """
        return self._ModelRewriteRules

    @ModelRewriteRules.setter
    def ModelRewriteRules(self, ModelRewriteRules):
        self._ModelRewriteRules = ModelRewriteRules

    @property
    def SourceId(self):
        r"""<p>服务来源</p>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Namespace(self):
        r"""<p>命名空间</p>
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ServiceName(self):
        r"""<p>服务名称</p>
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Protocol(self):
        r"""<p>命名空间</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ExtParams(self):
        r"""<p>扩展参数</p>
        :rtype: list of KeyValue
        """
        return self._ExtParams

    @ExtParams.setter
    def ExtParams(self, ExtParams):
        self._ExtParams = ExtParams

    @property
    def CustomProviderName(self):
        r"""<p>模型自定义供应商名称</p>
        :rtype: str
        """
        return self._CustomProviderName

    @CustomProviderName.setter
    def CustomProviderName(self, CustomProviderName):
        self._CustomProviderName = CustomProviderName

    @property
    def KeyRotationEnabled(self):
        r"""<p>是否开启密钥轮转</p>
        :rtype: bool
        """
        return self._KeyRotationEnabled

    @KeyRotationEnabled.setter
    def KeyRotationEnabled(self, KeyRotationEnabled):
        self._KeyRotationEnabled = KeyRotationEnabled

    @property
    def KeyRotationPeriodDays(self):
        r"""<p>密钥轮转周期</p><p>单位：天</p>
        :rtype: int
        """
        return self._KeyRotationPeriodDays

    @KeyRotationPeriodDays.setter
    def KeyRotationPeriodDays(self, KeyRotationPeriodDays):
        self._KeyRotationPeriodDays = KeyRotationPeriodDays

    @property
    def ExternalInstanceId(self):
        r"""<p>外部服务来源ID</p>
        :rtype: str
        """
        return self._ExternalInstanceId

    @ExternalInstanceId.setter
    def ExternalInstanceId(self, ExternalInstanceId):
        self._ExternalInstanceId = ExternalInstanceId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._ServiceType = params.get("ServiceType")
        self._ModelProvider = params.get("ModelProvider")
        self._ModelProtocol = params.get("ModelProtocol")
        self._UpstreamURL = params.get("UpstreamURL")
        self._ModelSelector = params.get("ModelSelector")
        self._DefaultModel = params.get("DefaultModel")
        self._EnableModelFallback = params.get("EnableModelFallback")
        if params.get("ModelFallbackRule") is not None:
            self._ModelFallbackRule = CloudNativeAPIGatewayLLMModelFallbackRule()
            self._ModelFallbackRule._deserialize(params.get("ModelFallbackRule"))
        self._EnableModelParamCheck = params.get("EnableModelParamCheck")
        if params.get("ModelParamCheckRule") is not None:
            self._ModelParamCheckRule = CloudNativeAPIGatewayLLMModelParamCheckInfo()
            self._ModelParamCheckRule._deserialize(params.get("ModelParamCheckRule"))
        self._Description = params.get("Description")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._WriteTimeout = params.get("WriteTimeout")
        self._ReadTimeout = params.get("ReadTimeout")
        self._Retries = params.get("Retries")
        self._UpstreamUrlMode = params.get("UpstreamUrlMode")
        self._SNI = params.get("SNI")
        if params.get("QuotaLimit") is not None:
            self._QuotaLimit = AIGWLLMQuotaLimit()
            self._QuotaLimit._deserialize(params.get("QuotaLimit"))
        self._Tags = params.get("Tags")
        self._SecretKeyIds = params.get("SecretKeyIds")
        if params.get("ModelRewriteRules") is not None:
            self._ModelRewriteRules = []
            for item in params.get("ModelRewriteRules"):
                obj = AIGWModelRewriteRule()
                obj._deserialize(item)
                self._ModelRewriteRules.append(obj)
        self._SourceId = params.get("SourceId")
        self._Namespace = params.get("Namespace")
        self._ServiceName = params.get("ServiceName")
        self._Protocol = params.get("Protocol")
        if params.get("ExtParams") is not None:
            self._ExtParams = []
            for item in params.get("ExtParams"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ExtParams.append(obj)
        self._CustomProviderName = params.get("CustomProviderName")
        self._KeyRotationEnabled = params.get("KeyRotationEnabled")
        self._KeyRotationPeriodDays = params.get("KeyRotationPeriodDays")
        self._ExternalInstanceId = params.get("ExternalInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayLLMModelServiceRoute(AbstractModel):
    r"""模型服务路由配置

    """

    def __init__(self):
        r"""
        :param _SelectedTypes: <p>生效的路由算法类型：权重路由，模型名称路由、参数路由等Weighted/ModelName/Query (预留多个，暂时只能填写一个)</p>
        :type SelectedTypes: list of str
        :param _WeightedConfig: <p>权重路由配置，最多10个</p>
        :type WeightedConfig: list of CloudNativeAPIGatewayLLMModelServiceRouteWeightedStrategy
        :param _ModelNameConfig: <p>模型名称路由配置，最多10个</p>
        :type ModelNameConfig: list of CloudNativeAPIGatewayLLMModelServiceRouteModelNameStrategy
        :param _IntentRouteConfig: <p>意图识别</p>
        :type IntentRouteConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWIntentRoute`
        :param _LatencyPriorityConfig: <p>延迟路由</p>
        :type LatencyPriorityConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWLatencyPriorityConfig`
        :param _CacheAwareRouteConfig: <p>前缀缓存感知路由</p>
        :type CacheAwareRouteConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWCacheAwareRouteConfig`
        :param _TokenLengthRouteConfig: <p>token 长度路</p>
        :type TokenLengthRouteConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWTokenLengthRoute`
        """
        self._SelectedTypes = None
        self._WeightedConfig = None
        self._ModelNameConfig = None
        self._IntentRouteConfig = None
        self._LatencyPriorityConfig = None
        self._CacheAwareRouteConfig = None
        self._TokenLengthRouteConfig = None

    @property
    def SelectedTypes(self):
        r"""<p>生效的路由算法类型：权重路由，模型名称路由、参数路由等Weighted/ModelName/Query (预留多个，暂时只能填写一个)</p>
        :rtype: list of str
        """
        return self._SelectedTypes

    @SelectedTypes.setter
    def SelectedTypes(self, SelectedTypes):
        self._SelectedTypes = SelectedTypes

    @property
    def WeightedConfig(self):
        r"""<p>权重路由配置，最多10个</p>
        :rtype: list of CloudNativeAPIGatewayLLMModelServiceRouteWeightedStrategy
        """
        return self._WeightedConfig

    @WeightedConfig.setter
    def WeightedConfig(self, WeightedConfig):
        self._WeightedConfig = WeightedConfig

    @property
    def ModelNameConfig(self):
        r"""<p>模型名称路由配置，最多10个</p>
        :rtype: list of CloudNativeAPIGatewayLLMModelServiceRouteModelNameStrategy
        """
        return self._ModelNameConfig

    @ModelNameConfig.setter
    def ModelNameConfig(self, ModelNameConfig):
        self._ModelNameConfig = ModelNameConfig

    @property
    def IntentRouteConfig(self):
        r"""<p>意图识别</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWIntentRoute`
        """
        return self._IntentRouteConfig

    @IntentRouteConfig.setter
    def IntentRouteConfig(self, IntentRouteConfig):
        self._IntentRouteConfig = IntentRouteConfig

    @property
    def LatencyPriorityConfig(self):
        r"""<p>延迟路由</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLatencyPriorityConfig`
        """
        return self._LatencyPriorityConfig

    @LatencyPriorityConfig.setter
    def LatencyPriorityConfig(self, LatencyPriorityConfig):
        self._LatencyPriorityConfig = LatencyPriorityConfig

    @property
    def CacheAwareRouteConfig(self):
        r"""<p>前缀缓存感知路由</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWCacheAwareRouteConfig`
        """
        return self._CacheAwareRouteConfig

    @CacheAwareRouteConfig.setter
    def CacheAwareRouteConfig(self, CacheAwareRouteConfig):
        self._CacheAwareRouteConfig = CacheAwareRouteConfig

    @property
    def TokenLengthRouteConfig(self):
        r"""<p>token 长度路</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWTokenLengthRoute`
        """
        return self._TokenLengthRouteConfig

    @TokenLengthRouteConfig.setter
    def TokenLengthRouteConfig(self, TokenLengthRouteConfig):
        self._TokenLengthRouteConfig = TokenLengthRouteConfig


    def _deserialize(self, params):
        self._SelectedTypes = params.get("SelectedTypes")
        if params.get("WeightedConfig") is not None:
            self._WeightedConfig = []
            for item in params.get("WeightedConfig"):
                obj = CloudNativeAPIGatewayLLMModelServiceRouteWeightedStrategy()
                obj._deserialize(item)
                self._WeightedConfig.append(obj)
        if params.get("ModelNameConfig") is not None:
            self._ModelNameConfig = []
            for item in params.get("ModelNameConfig"):
                obj = CloudNativeAPIGatewayLLMModelServiceRouteModelNameStrategy()
                obj._deserialize(item)
                self._ModelNameConfig.append(obj)
        if params.get("IntentRouteConfig") is not None:
            self._IntentRouteConfig = AIGWIntentRoute()
            self._IntentRouteConfig._deserialize(params.get("IntentRouteConfig"))
        if params.get("LatencyPriorityConfig") is not None:
            self._LatencyPriorityConfig = AIGWLatencyPriorityConfig()
            self._LatencyPriorityConfig._deserialize(params.get("LatencyPriorityConfig"))
        if params.get("CacheAwareRouteConfig") is not None:
            self._CacheAwareRouteConfig = AIGWCacheAwareRouteConfig()
            self._CacheAwareRouteConfig._deserialize(params.get("CacheAwareRouteConfig"))
        if params.get("TokenLengthRouteConfig") is not None:
            self._TokenLengthRouteConfig = AIGWTokenLengthRoute()
            self._TokenLengthRouteConfig._deserialize(params.get("TokenLengthRouteConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayLLMModelServiceRouteModelNameStrategy(AbstractModel):
    r"""模型服务模型名称路由策略

    """

    def __init__(self):
        r"""
        :param _ModelServiceId: <p>模型服务id</p>
        :type ModelServiceId: str
        :param _MatchModelName: <p>匹配模型服务</p>
        :type MatchModelName: str
        :param _RewriteModelName: <p>重写模型</p>
        :type RewriteModelName: str
        """
        self._ModelServiceId = None
        self._MatchModelName = None
        self._RewriteModelName = None

    @property
    def ModelServiceId(self):
        r"""<p>模型服务id</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId

    @property
    def MatchModelName(self):
        r"""<p>匹配模型服务</p>
        :rtype: str
        """
        return self._MatchModelName

    @MatchModelName.setter
    def MatchModelName(self, MatchModelName):
        self._MatchModelName = MatchModelName

    @property
    def RewriteModelName(self):
        r"""<p>重写模型</p>
        :rtype: str
        """
        return self._RewriteModelName

    @RewriteModelName.setter
    def RewriteModelName(self, RewriteModelName):
        self._RewriteModelName = RewriteModelName


    def _deserialize(self, params):
        self._ModelServiceId = params.get("ModelServiceId")
        self._MatchModelName = params.get("MatchModelName")
        self._RewriteModelName = params.get("RewriteModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayLLMModelServiceRouteWeightedStrategy(AbstractModel):
    r"""权重路由配置

    """

    def __init__(self):
        r"""
        :param _ModelServiceId: <p>模型服务id</p>
        :type ModelServiceId: str
        :param _Weight: <p>权重值</p>
        :type Weight: int
        """
        self._ModelServiceId = None
        self._Weight = None

    @property
    def ModelServiceId(self):
        r"""<p>模型服务id</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId

    @property
    def Weight(self):
        r"""<p>权重值</p>
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._ModelServiceId = params.get("ModelServiceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayConsumerGroupRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例id</p>
        :type GatewayId: str
        :param _Name: <p>消费者组名称，最长 60 字符。同一网关下唯一。</p>
        :type Name: str
        :param _Status: <p>启用状态。</p><p>枚举值：</p><ul><li>Enable：启用</li><li>Disable：禁用</li></ul>
        :type Status: str
        :param _Description: <p>消费者组描述。最长 200 字符。</p>
        :type Description: str
        """
        self._GatewayId = None
        self._Name = None
        self._Status = None
        self._Description = None

    @property
    def GatewayId(self):
        r"""<p>网关实例id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""<p>消费者组名称，最长 60 字符。同一网关下唯一。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""<p>启用状态。</p><p>枚举值：</p><ul><li>Enable：启用</li><li>Disable：禁用</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        r"""<p>消费者组描述。最长 200 字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayConsumerGroupResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>创建结果。包含成功标识与新建资源 ID。</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>创建结果。包含成功标识与新建资源 ID。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwCreateCommonResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayConsumerRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _Name: <p>消费者名称，最长 60 字符。同一网关下唯一。</p>
        :type Name: str
        :param _Description: <p>消费者描述。最长 200 字符。</p>
        :type Description: str
        """
        self._GatewayId = None
        self._Name = None
        self._Description = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""<p>消费者名称，最长 60 字符。同一网关下唯一。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>消费者描述。最长 200 字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayConsumerResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>创建结果。包含成功标识与新建资源 ID。</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>创建结果。包含成功标识与新建资源 ID。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwCreateCommonResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayLLMModelAPIRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayLLMModelAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关 id。</p>
        :type GatewayId: str
        :param _Name: <p>模型 API 名称，最长 60 字符。同一网关下唯一。</p>
        :type Name: str
        :param _SceneType: <p>业务场景。</p><p>枚举值：</p><ul><li>Chat：聊天</li><li>Image：图像（需要网关版本 ≥ 3.9.3）</li></ul>
        :type SceneType: str
        :param _RequestProtocol: <p>请求协议（小写）。当前仅支持：</p><ul><li>openai</li></ul>
        :type RequestProtocol: str
        :param _ListModelServiceId: <p>关联的模型服务 ID 列表，长度 1-10。</p><p>注：字段名建议改为 ModelServiceIds，当前保留用于兼容。</p>
        :type ListModelServiceId: list of str
        :param _RouteList: <p>路由列表，至少 1 条。每条包含 Methods/Paths/Hosts 等 Kong 路由属性。</p>
        :type RouteList: list of DefaultKongRoute
        :param _BasePath: <p>统一前缀路径（可选）。例如 /v1/openai。</p>
        :type BasePath: str
        :param _Description: <p>模型 API 描述。最长 200 字符。</p>
        :type Description: str
        :param _ModelServiceRoute: <p>多模型服务路由策略。ListModelServiceId 多于 1 项时必填。</p>
        :type ModelServiceRoute: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelServiceRoute`
        :param _MatchHeaders: <p>Header 路由匹配规则。当前仅支持 Operator=exact。</p>
        :type MatchHeaders: list of AIGWKVMatch
        :param _EnableCrossServiceFallback: <p>是否启用跨服务 Fallback。开启后需提供 CrossServiceFallbackConfig。</p>
        :type EnableCrossServiceFallback: bool
        :param _CrossServiceFallbackConfig: <p>跨服务 Fallback 配置。EnableCrossServiceFallback=true 时必填。</p>
        :type CrossServiceFallbackConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWCrossServiceFallbackConfig`
        :param _TagFilter: <p>标签过滤策略。需要网关版本 ≥ 3.9.4。</p>
        :type TagFilter: :class:`tencentcloud.cngw.v20230418.models.AIGWTagFilter`
        :param _LogConfig: <p>日志输出配置（请求/响应 payload 落 LLM Log）。需要网关版本 ≥ 3.9.4。</p>
        :type LogConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWLogConfig`
        """
        self._GatewayId = None
        self._Name = None
        self._SceneType = None
        self._RequestProtocol = None
        self._ListModelServiceId = None
        self._RouteList = None
        self._BasePath = None
        self._Description = None
        self._ModelServiceRoute = None
        self._MatchHeaders = None
        self._EnableCrossServiceFallback = None
        self._CrossServiceFallbackConfig = None
        self._TagFilter = None
        self._LogConfig = None

    @property
    def GatewayId(self):
        r"""<p>网关 id。</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""<p>模型 API 名称，最长 60 字符。同一网关下唯一。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SceneType(self):
        r"""<p>业务场景。</p><p>枚举值：</p><ul><li>Chat：聊天</li><li>Image：图像（需要网关版本 ≥ 3.9.3）</li></ul>
        :rtype: str
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def RequestProtocol(self):
        r"""<p>请求协议（小写）。当前仅支持：</p><ul><li>openai</li></ul>
        :rtype: str
        """
        return self._RequestProtocol

    @RequestProtocol.setter
    def RequestProtocol(self, RequestProtocol):
        self._RequestProtocol = RequestProtocol

    @property
    def ListModelServiceId(self):
        r"""<p>关联的模型服务 ID 列表，长度 1-10。</p><p>注：字段名建议改为 ModelServiceIds，当前保留用于兼容。</p>
        :rtype: list of str
        """
        return self._ListModelServiceId

    @ListModelServiceId.setter
    def ListModelServiceId(self, ListModelServiceId):
        self._ListModelServiceId = ListModelServiceId

    @property
    def RouteList(self):
        r"""<p>路由列表，至少 1 条。每条包含 Methods/Paths/Hosts 等 Kong 路由属性。</p>
        :rtype: list of DefaultKongRoute
        """
        return self._RouteList

    @RouteList.setter
    def RouteList(self, RouteList):
        self._RouteList = RouteList

    @property
    def BasePath(self):
        r"""<p>统一前缀路径（可选）。例如 /v1/openai。</p>
        :rtype: str
        """
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def Description(self):
        r"""<p>模型 API 描述。最长 200 字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ModelServiceRoute(self):
        r"""<p>多模型服务路由策略。ListModelServiceId 多于 1 项时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelServiceRoute`
        """
        return self._ModelServiceRoute

    @ModelServiceRoute.setter
    def ModelServiceRoute(self, ModelServiceRoute):
        self._ModelServiceRoute = ModelServiceRoute

    @property
    def MatchHeaders(self):
        r"""<p>Header 路由匹配规则。当前仅支持 Operator=exact。</p>
        :rtype: list of AIGWKVMatch
        """
        return self._MatchHeaders

    @MatchHeaders.setter
    def MatchHeaders(self, MatchHeaders):
        self._MatchHeaders = MatchHeaders

    @property
    def EnableCrossServiceFallback(self):
        r"""<p>是否启用跨服务 Fallback。开启后需提供 CrossServiceFallbackConfig。</p>
        :rtype: bool
        """
        return self._EnableCrossServiceFallback

    @EnableCrossServiceFallback.setter
    def EnableCrossServiceFallback(self, EnableCrossServiceFallback):
        self._EnableCrossServiceFallback = EnableCrossServiceFallback

    @property
    def CrossServiceFallbackConfig(self):
        r"""<p>跨服务 Fallback 配置。EnableCrossServiceFallback=true 时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWCrossServiceFallbackConfig`
        """
        return self._CrossServiceFallbackConfig

    @CrossServiceFallbackConfig.setter
    def CrossServiceFallbackConfig(self, CrossServiceFallbackConfig):
        self._CrossServiceFallbackConfig = CrossServiceFallbackConfig

    @property
    def TagFilter(self):
        r"""<p>标签过滤策略。需要网关版本 ≥ 3.9.4。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWTagFilter`
        """
        return self._TagFilter

    @TagFilter.setter
    def TagFilter(self, TagFilter):
        self._TagFilter = TagFilter

    @property
    def LogConfig(self):
        r"""<p>日志输出配置（请求/响应 payload 落 LLM Log）。需要网关版本 ≥ 3.9.4。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLogConfig`
        """
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._SceneType = params.get("SceneType")
        self._RequestProtocol = params.get("RequestProtocol")
        self._ListModelServiceId = params.get("ListModelServiceId")
        if params.get("RouteList") is not None:
            self._RouteList = []
            for item in params.get("RouteList"):
                obj = DefaultKongRoute()
                obj._deserialize(item)
                self._RouteList.append(obj)
        self._BasePath = params.get("BasePath")
        self._Description = params.get("Description")
        if params.get("ModelServiceRoute") is not None:
            self._ModelServiceRoute = CloudNativeAPIGatewayLLMModelServiceRoute()
            self._ModelServiceRoute._deserialize(params.get("ModelServiceRoute"))
        if params.get("MatchHeaders") is not None:
            self._MatchHeaders = []
            for item in params.get("MatchHeaders"):
                obj = AIGWKVMatch()
                obj._deserialize(item)
                self._MatchHeaders.append(obj)
        self._EnableCrossServiceFallback = params.get("EnableCrossServiceFallback")
        if params.get("CrossServiceFallbackConfig") is not None:
            self._CrossServiceFallbackConfig = AIGWCrossServiceFallbackConfig()
            self._CrossServiceFallbackConfig._deserialize(params.get("CrossServiceFallbackConfig"))
        if params.get("TagFilter") is not None:
            self._TagFilter = AIGWTagFilter()
            self._TagFilter._deserialize(params.get("TagFilter"))
        if params.get("LogConfig") is not None:
            self._LogConfig = AIGWLogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayLLMModelAPIResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayLLMModelAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>是否成功。</p>
        :type Result: bool
        :param _ModelAPIId: <p>模型 API ID，全局唯一标识。</p>
        :type ModelAPIId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._ModelAPIId = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>是否成功。</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ModelAPIId(self):
        r"""<p>模型 API ID，全局唯一标识。</p>
        :rtype: str
        """
        return self._ModelAPIId

    @ModelAPIId.setter
    def ModelAPIId(self, ModelAPIId):
        self._ModelAPIId = ModelAPIId

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
        self._Result = params.get("Result")
        self._ModelAPIId = params.get("ModelAPIId")
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayLLMModelServiceRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayLLMModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关 id。</p>
        :type GatewayId: str
        :param _Name: <p>服务名称，最长60个字符，支持中英文大小写、数字及分隔符（“-”、“_”)，不能以数字和分隔符开头，不能以分隔符结尾。</p>
        :type Name: str
        :param _ServiceType: <p>服务类型。目前仅支持 LLMService。</p><p>枚举值：</p><ul><li>LLMService： 大语言模型服务</li></ul>
        :type ServiceType: str
        :param _ModelProvider: <p>选择模型提供商, 选项：OpenAI、Anthropic、Azure OpenAI等。</p>
        :type ModelProvider: str
        :param _ModelProtocol: <p>API协议标准，根据供应商动态变化：OpenAI→OpenAI/v1，Anthropic→Anthropic/v1等</p>
        :type ModelProtocol: str
        :param _ModelSelector: <p>模型选择方式，选项：Specify（指定模型）、PassThrough（透传请求模型）。</p>
        :type ModelSelector: str
        :param _SecretKeyIds: <p>LLM 厂商颁发的认证信息 token 。</p>
        :type SecretKeyIds: list of str
        :param _DefaultModel: <p>默认模型，模型选择方式为 Specify 时必填。</p>
        :type DefaultModel: str
        :param _EnableModelFallback: <p>开启模型降级，模型选择方式为 Specify 时必填。</p>
        :type EnableModelFallback: bool
        :param _ModelFallbackRule: <p>可以配置备用模型规则，EnableSpecifyModelFallbackxa0为 true 时必填。</p>
        :type ModelFallbackRule: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelFallbackRule`
        :param _EnableModelParamCheck: <p>开启模型参数校验，是否校验客户端传递的 model 参数,xa0模型选择方式为 PassThrough 时必填</p>
        :type EnableModelParamCheck: bool
        :param _ModelParamCheckRule: <p>模型检验信息，EnableModelParamCheckxa0为 true 时必填。</p>
        :type ModelParamCheckRule: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelParamCheckInfo`
        :param _Description: <p>描述。</p>
        :type Description: str
        :param _UpstreamURL: <p>服务提供商自定义 url</p>
        :type UpstreamURL: str
        :param _ConnectTimeout: <p>连接超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：10000</p>
        :type ConnectTimeout: int
        :param _WriteTimeout: <p>写入超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :type WriteTimeout: int
        :param _ReadTimeout: <p>读取超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :type ReadTimeout: int
        :param _Retries: <p>重试次数</p><p>取值范围：[0, 5]</p><p>单位：次</p><p>默认值：0</p>
        :type Retries: int
        :param _UpstreamUrlMode: <p>路径拼接模式</p><p>枚举值：</p><ul><li>FixedPath： 固定地址</li><li>AutoConcat： 自动拼接</li></ul>
        :type UpstreamUrlMode: str
        :param _SNI: <p>sni</p>
        :type SNI: str
        :param _QuotaLimit: <p>模型服务级别的配额上限（RPM/TPM）。需要网关版本 ≥ 3.9.4。</p>
        :type QuotaLimit: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMQuotaLimit`
        :param _Tags: <p>标签</p>
        :type Tags: list of str
        :param _ModelRewriteRules: <p>参数改写规则</p>
        :type ModelRewriteRules: list of AIGWModelRewriteRule
        :param _CustomProviderName: <p>模型自定义供应商名称</p>
        :type CustomProviderName: str
        :param _ExternalInstanceId: <p>外部服务来源ID</p>
        :type ExternalInstanceId: str
        :param _ExtParams: <p>其他参数</p>
        :type ExtParams: list of KeyValue
        :param _KeyRotationEnabled: <p>密钥轮转开关</p>
        :type KeyRotationEnabled: bool
        :param _KeyRotationPeriodDays: <p>密钥轮转周期</p><p>单位：天数</p>
        :type KeyRotationPeriodDays: int
        :param _SourceId: <p>来源服务 ID。</p>
        :type SourceId: str
        :param _Namespace: <p>命名空间。</p>
        :type Namespace: str
        :param _ServiceName: <p>服务名称。</p>
        :type ServiceName: str
        :param _Protocol: <p>协议类型，如 OpenAI、Custom。</p>
        :type Protocol: str
        """
        self._GatewayId = None
        self._Name = None
        self._ServiceType = None
        self._ModelProvider = None
        self._ModelProtocol = None
        self._ModelSelector = None
        self._SecretKeyIds = None
        self._DefaultModel = None
        self._EnableModelFallback = None
        self._ModelFallbackRule = None
        self._EnableModelParamCheck = None
        self._ModelParamCheckRule = None
        self._Description = None
        self._UpstreamURL = None
        self._ConnectTimeout = None
        self._WriteTimeout = None
        self._ReadTimeout = None
        self._Retries = None
        self._UpstreamUrlMode = None
        self._SNI = None
        self._QuotaLimit = None
        self._Tags = None
        self._ModelRewriteRules = None
        self._CustomProviderName = None
        self._ExternalInstanceId = None
        self._ExtParams = None
        self._KeyRotationEnabled = None
        self._KeyRotationPeriodDays = None
        self._SourceId = None
        self._Namespace = None
        self._ServiceName = None
        self._Protocol = None

    @property
    def GatewayId(self):
        r"""<p>网关 id。</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""<p>服务名称，最长60个字符，支持中英文大小写、数字及分隔符（“-”、“_”)，不能以数字和分隔符开头，不能以分隔符结尾。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ServiceType(self):
        r"""<p>服务类型。目前仅支持 LLMService。</p><p>枚举值：</p><ul><li>LLMService： 大语言模型服务</li></ul>
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ModelProvider(self):
        r"""<p>选择模型提供商, 选项：OpenAI、Anthropic、Azure OpenAI等。</p>
        :rtype: str
        """
        return self._ModelProvider

    @ModelProvider.setter
    def ModelProvider(self, ModelProvider):
        self._ModelProvider = ModelProvider

    @property
    def ModelProtocol(self):
        r"""<p>API协议标准，根据供应商动态变化：OpenAI→OpenAI/v1，Anthropic→Anthropic/v1等</p>
        :rtype: str
        """
        return self._ModelProtocol

    @ModelProtocol.setter
    def ModelProtocol(self, ModelProtocol):
        self._ModelProtocol = ModelProtocol

    @property
    def ModelSelector(self):
        r"""<p>模型选择方式，选项：Specify（指定模型）、PassThrough（透传请求模型）。</p>
        :rtype: str
        """
        return self._ModelSelector

    @ModelSelector.setter
    def ModelSelector(self, ModelSelector):
        self._ModelSelector = ModelSelector

    @property
    def SecretKeyIds(self):
        r"""<p>LLM 厂商颁发的认证信息 token 。</p>
        :rtype: list of str
        """
        return self._SecretKeyIds

    @SecretKeyIds.setter
    def SecretKeyIds(self, SecretKeyIds):
        self._SecretKeyIds = SecretKeyIds

    @property
    def DefaultModel(self):
        r"""<p>默认模型，模型选择方式为 Specify 时必填。</p>
        :rtype: str
        """
        return self._DefaultModel

    @DefaultModel.setter
    def DefaultModel(self, DefaultModel):
        self._DefaultModel = DefaultModel

    @property
    def EnableModelFallback(self):
        r"""<p>开启模型降级，模型选择方式为 Specify 时必填。</p>
        :rtype: bool
        """
        return self._EnableModelFallback

    @EnableModelFallback.setter
    def EnableModelFallback(self, EnableModelFallback):
        self._EnableModelFallback = EnableModelFallback

    @property
    def ModelFallbackRule(self):
        r"""<p>可以配置备用模型规则，EnableSpecifyModelFallbackxa0为 true 时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelFallbackRule`
        """
        return self._ModelFallbackRule

    @ModelFallbackRule.setter
    def ModelFallbackRule(self, ModelFallbackRule):
        self._ModelFallbackRule = ModelFallbackRule

    @property
    def EnableModelParamCheck(self):
        r"""<p>开启模型参数校验，是否校验客户端传递的 model 参数,xa0模型选择方式为 PassThrough 时必填</p>
        :rtype: bool
        """
        return self._EnableModelParamCheck

    @EnableModelParamCheck.setter
    def EnableModelParamCheck(self, EnableModelParamCheck):
        self._EnableModelParamCheck = EnableModelParamCheck

    @property
    def ModelParamCheckRule(self):
        r"""<p>模型检验信息，EnableModelParamCheckxa0为 true 时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelParamCheckInfo`
        """
        return self._ModelParamCheckRule

    @ModelParamCheckRule.setter
    def ModelParamCheckRule(self, ModelParamCheckRule):
        self._ModelParamCheckRule = ModelParamCheckRule

    @property
    def Description(self):
        r"""<p>描述。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UpstreamURL(self):
        r"""<p>服务提供商自定义 url</p>
        :rtype: str
        """
        return self._UpstreamURL

    @UpstreamURL.setter
    def UpstreamURL(self, UpstreamURL):
        self._UpstreamURL = UpstreamURL

    @property
    def ConnectTimeout(self):
        r"""<p>连接超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：10000</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def WriteTimeout(self):
        r"""<p>写入超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :rtype: int
        """
        return self._WriteTimeout

    @WriteTimeout.setter
    def WriteTimeout(self, WriteTimeout):
        self._WriteTimeout = WriteTimeout

    @property
    def ReadTimeout(self):
        r"""<p>读取超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :rtype: int
        """
        return self._ReadTimeout

    @ReadTimeout.setter
    def ReadTimeout(self, ReadTimeout):
        self._ReadTimeout = ReadTimeout

    @property
    def Retries(self):
        r"""<p>重试次数</p><p>取值范围：[0, 5]</p><p>单位：次</p><p>默认值：0</p>
        :rtype: int
        """
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamUrlMode(self):
        r"""<p>路径拼接模式</p><p>枚举值：</p><ul><li>FixedPath： 固定地址</li><li>AutoConcat： 自动拼接</li></ul>
        :rtype: str
        """
        return self._UpstreamUrlMode

    @UpstreamUrlMode.setter
    def UpstreamUrlMode(self, UpstreamUrlMode):
        self._UpstreamUrlMode = UpstreamUrlMode

    @property
    def SNI(self):
        r"""<p>sni</p>
        :rtype: str
        """
        return self._SNI

    @SNI.setter
    def SNI(self, SNI):
        self._SNI = SNI

    @property
    def QuotaLimit(self):
        r"""<p>模型服务级别的配额上限（RPM/TPM）。需要网关版本 ≥ 3.9.4。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMQuotaLimit`
        """
        return self._QuotaLimit

    @QuotaLimit.setter
    def QuotaLimit(self, QuotaLimit):
        self._QuotaLimit = QuotaLimit

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ModelRewriteRules(self):
        r"""<p>参数改写规则</p>
        :rtype: list of AIGWModelRewriteRule
        """
        return self._ModelRewriteRules

    @ModelRewriteRules.setter
    def ModelRewriteRules(self, ModelRewriteRules):
        self._ModelRewriteRules = ModelRewriteRules

    @property
    def CustomProviderName(self):
        r"""<p>模型自定义供应商名称</p>
        :rtype: str
        """
        return self._CustomProviderName

    @CustomProviderName.setter
    def CustomProviderName(self, CustomProviderName):
        self._CustomProviderName = CustomProviderName

    @property
    def ExternalInstanceId(self):
        r"""<p>外部服务来源ID</p>
        :rtype: str
        """
        return self._ExternalInstanceId

    @ExternalInstanceId.setter
    def ExternalInstanceId(self, ExternalInstanceId):
        self._ExternalInstanceId = ExternalInstanceId

    @property
    def ExtParams(self):
        r"""<p>其他参数</p>
        :rtype: list of KeyValue
        """
        return self._ExtParams

    @ExtParams.setter
    def ExtParams(self, ExtParams):
        self._ExtParams = ExtParams

    @property
    def KeyRotationEnabled(self):
        r"""<p>密钥轮转开关</p>
        :rtype: bool
        """
        return self._KeyRotationEnabled

    @KeyRotationEnabled.setter
    def KeyRotationEnabled(self, KeyRotationEnabled):
        self._KeyRotationEnabled = KeyRotationEnabled

    @property
    def KeyRotationPeriodDays(self):
        r"""<p>密钥轮转周期</p><p>单位：天数</p>
        :rtype: int
        """
        return self._KeyRotationPeriodDays

    @KeyRotationPeriodDays.setter
    def KeyRotationPeriodDays(self, KeyRotationPeriodDays):
        self._KeyRotationPeriodDays = KeyRotationPeriodDays

    @property
    def SourceId(self):
        r"""<p>来源服务 ID。</p>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Namespace(self):
        r"""<p>命名空间。</p>
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ServiceName(self):
        r"""<p>服务名称。</p>
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Protocol(self):
        r"""<p>协议类型，如 OpenAI、Custom。</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._ServiceType = params.get("ServiceType")
        self._ModelProvider = params.get("ModelProvider")
        self._ModelProtocol = params.get("ModelProtocol")
        self._ModelSelector = params.get("ModelSelector")
        self._SecretKeyIds = params.get("SecretKeyIds")
        self._DefaultModel = params.get("DefaultModel")
        self._EnableModelFallback = params.get("EnableModelFallback")
        if params.get("ModelFallbackRule") is not None:
            self._ModelFallbackRule = CloudNativeAPIGatewayLLMModelFallbackRule()
            self._ModelFallbackRule._deserialize(params.get("ModelFallbackRule"))
        self._EnableModelParamCheck = params.get("EnableModelParamCheck")
        if params.get("ModelParamCheckRule") is not None:
            self._ModelParamCheckRule = CloudNativeAPIGatewayLLMModelParamCheckInfo()
            self._ModelParamCheckRule._deserialize(params.get("ModelParamCheckRule"))
        self._Description = params.get("Description")
        self._UpstreamURL = params.get("UpstreamURL")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._WriteTimeout = params.get("WriteTimeout")
        self._ReadTimeout = params.get("ReadTimeout")
        self._Retries = params.get("Retries")
        self._UpstreamUrlMode = params.get("UpstreamUrlMode")
        self._SNI = params.get("SNI")
        if params.get("QuotaLimit") is not None:
            self._QuotaLimit = AIGWLLMQuotaLimit()
            self._QuotaLimit._deserialize(params.get("QuotaLimit"))
        self._Tags = params.get("Tags")
        if params.get("ModelRewriteRules") is not None:
            self._ModelRewriteRules = []
            for item in params.get("ModelRewriteRules"):
                obj = AIGWModelRewriteRule()
                obj._deserialize(item)
                self._ModelRewriteRules.append(obj)
        self._CustomProviderName = params.get("CustomProviderName")
        self._ExternalInstanceId = params.get("ExternalInstanceId")
        if params.get("ExtParams") is not None:
            self._ExtParams = []
            for item in params.get("ExtParams"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ExtParams.append(obj)
        self._KeyRotationEnabled = params.get("KeyRotationEnabled")
        self._KeyRotationPeriodDays = params.get("KeyRotationPeriodDays")
        self._SourceId = params.get("SourceId")
        self._Namespace = params.get("Namespace")
        self._ServiceName = params.get("ServiceName")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayLLMModelServiceResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayLLMModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>是否成功</p>
        :type Result: bool
        :param _ModelServiceId: <p>模型服务 ID，全局唯一标识。</p>
        :type ModelServiceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._ModelServiceId = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>是否成功</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ModelServiceId(self):
        r"""<p>模型服务 ID，全局唯一标识。</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId

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
        self._Result = params.get("Result")
        self._ModelServiceId = params.get("ModelServiceId")
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayMCPServerRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayMCPServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>实例 ID</p>
        :type GatewayId: str
        :param _Name: <p>名字</p>
        :type Name: str
        :param _DisplayName: <p>展示名字</p>
        :type DisplayName: str
        :param _ServerType: <p>MCP服务类型</p><ul><li>MCP</li><li>Rest2MCP</li></ul>
        :type ServerType: str
        :param _Transport: <p>传输协议：StreamableHttp或SSE</p><p>枚举值：</p><ul><li>StreamableHttp： Streamable HTTP</li><li>SSE： Server-Sent Events</li></ul>
        :type Transport: str
        :param _UpstreamType: <p>后端类型</p><p>枚举值：</p><ul><li>MCPRegistry： mcp 注册中心- Registry</li><li>Registry： 普通注册中心</li><li>HostIP： 域名或ip</li><li>VirtualMCPServer： 虚拟MCPServer</li></ul>
        :type UpstreamType: str
        :param _UpstreamInfo: <p>注册中心来源信息</p>
        :type UpstreamInfo: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPUpstreamInfo`
        :param _SessionConfig: <p>会话配置</p>
        :type SessionConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPSessionConfig`
        :param _Timeout: <p>超时时间，单位ms，最大60000</p>
        :type Timeout: int
        :param _RetryCount: <p>重试次数，最大3次</p>
        :type RetryCount: int
        :param _Description: <p>描述</p>
        :type Description: str
        :param _EnableHealthCheck: <p>是否启用健康检查</p>
        :type EnableHealthCheck: bool
        :param _HealthCheck: <p>健康检查配置</p>
        :type HealthCheck: :class:`tencentcloud.cngw.v20230418.models.AIGWHealthCheckSetting`
        """
        self._GatewayId = None
        self._Name = None
        self._DisplayName = None
        self._ServerType = None
        self._Transport = None
        self._UpstreamType = None
        self._UpstreamInfo = None
        self._SessionConfig = None
        self._Timeout = None
        self._RetryCount = None
        self._Description = None
        self._EnableHealthCheck = None
        self._HealthCheck = None

    @property
    def GatewayId(self):
        r"""<p>实例 ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""<p>名字</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DisplayName(self):
        r"""<p>展示名字</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def ServerType(self):
        r"""<p>MCP服务类型</p><ul><li>MCP</li><li>Rest2MCP</li></ul>
        :rtype: str
        """
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def Transport(self):
        r"""<p>传输协议：StreamableHttp或SSE</p><p>枚举值：</p><ul><li>StreamableHttp： Streamable HTTP</li><li>SSE： Server-Sent Events</li></ul>
        :rtype: str
        """
        return self._Transport

    @Transport.setter
    def Transport(self, Transport):
        self._Transport = Transport

    @property
    def UpstreamType(self):
        r"""<p>后端类型</p><p>枚举值：</p><ul><li>MCPRegistry： mcp 注册中心- Registry</li><li>Registry： 普通注册中心</li><li>HostIP： 域名或ip</li><li>VirtualMCPServer： 虚拟MCPServer</li></ul>
        :rtype: str
        """
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def UpstreamInfo(self):
        r"""<p>注册中心来源信息</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPUpstreamInfo`
        """
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def SessionConfig(self):
        r"""<p>会话配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPSessionConfig`
        """
        return self._SessionConfig

    @SessionConfig.setter
    def SessionConfig(self, SessionConfig):
        self._SessionConfig = SessionConfig

    @property
    def Timeout(self):
        r"""<p>超时时间，单位ms，最大60000</p>
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def RetryCount(self):
        r"""<p>重试次数，最大3次</p>
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

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
    def EnableHealthCheck(self):
        r"""<p>是否启用健康检查</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def HealthCheck(self):
        r"""<p>健康检查配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWHealthCheckSetting`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._DisplayName = params.get("DisplayName")
        self._ServerType = params.get("ServerType")
        self._Transport = params.get("Transport")
        self._UpstreamType = params.get("UpstreamType")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = AIGWMCPUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        if params.get("SessionConfig") is not None:
            self._SessionConfig = AIGWMCPSessionConfig()
            self._SessionConfig._deserialize(params.get("SessionConfig"))
        self._Timeout = params.get("Timeout")
        self._RetryCount = params.get("RetryCount")
        self._Description = params.get("Description")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = AIGWHealthCheckSetting()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayMCPServerResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayMCPServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>创建结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>创建结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwCreateCommonResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayMCPToolRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewayMCPTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ContentType: <p>内容类型</p>
        :type ContentType: str
        :param _DisplayName: <p>展示名字</p>
        :type DisplayName: str
        :param _ServiceId: <p>服务 id</p>
        :type ServiceId: str
        """
        self._ContentType = None
        self._DisplayName = None
        self._ServiceId = None

    @property
    def ContentType(self):
        r"""<p>内容类型</p>
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def DisplayName(self):
        r"""<p>展示名字</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def ServiceId(self):
        r"""<p>服务 id</p>
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._ContentType = params.get("ContentType")
        self._DisplayName = params.get("DisplayName")
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayMCPToolResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewayMCPTool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>创建结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>创建结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwCreateCommonResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewaySecretKeyRequest(AbstractModel):
    r"""CreateCloudNativeAPIGatewaySecretKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>实例 ID</p>
        :type GatewayId: str
        :param _GenerateType: <p>密钥生成方式。</p><p>枚举值：</p><ul><li>System：系统自动生成</li><li>Custom：用户自定义（需传 SecretValue）</li><li>KMS：使用 KMS 密钥（需传 KmsKeyName 与 KmsKeyVersion）</li></ul>
        :type GenerateType: str
        :param _Name: <p>密钥名称，2-60 字符。</p>
        :type Name: str
        :param _ResourceType: <p>密钥归属资源类型。</p><p>枚举值：</p><ul><li>Consumer：消费者</li><li>ModelService：模型服务</li></ul>
        :type ResourceType: str
        :param _SecretType: <p>密钥协议类型。</p><p>枚举值：</p><ul><li>ApiKey</li><li>Basic</li><li>Hmac</li><li>OAuth2</li><li>JWT</li></ul>
        :type SecretType: str
        :param _Description: <p>密钥描述。最长 200 字符。</p>
        :type Description: str
        :param _JWTCredentialConfig: <p>JWT凭证配置</p>
        :type JWTCredentialConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWJWTCredentialConfig`
        :param _KmsKeyName: <p>KMS 密钥名称。GenerateType=KMS 时必填。</p>
        :type KmsKeyName: str
        :param _KmsKeyVersion: <p>KMS 密钥版本。GenerateType=KMS 时必填。</p>
        :type KmsKeyVersion: str
        :param _OAuthCredentialConfig: <p>OAuth2.0凭证配置</p>
        :type OAuthCredentialConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWOAuthCredentialConfig`
        :param _OIDCCredentialConfig: <p>OIDC凭证配置</p>
        :type OIDCCredentialConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWOIDCCredentialConfig`
        :param _Provider: <p>第三方平台类型</p><p>枚举值：</p><ul><li>Dify： Dify平台</li></ul>
        :type Provider: str
        :param _SecretValue: <p>密钥值，长度 8-256。GenerateType=Custom 时必填。</p>
        :type SecretValue: str
        """
        self._GatewayId = None
        self._GenerateType = None
        self._Name = None
        self._ResourceType = None
        self._SecretType = None
        self._Description = None
        self._JWTCredentialConfig = None
        self._KmsKeyName = None
        self._KmsKeyVersion = None
        self._OAuthCredentialConfig = None
        self._OIDCCredentialConfig = None
        self._Provider = None
        self._SecretValue = None

    @property
    def GatewayId(self):
        r"""<p>实例 ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GenerateType(self):
        r"""<p>密钥生成方式。</p><p>枚举值：</p><ul><li>System：系统自动生成</li><li>Custom：用户自定义（需传 SecretValue）</li><li>KMS：使用 KMS 密钥（需传 KmsKeyName 与 KmsKeyVersion）</li></ul>
        :rtype: str
        """
        return self._GenerateType

    @GenerateType.setter
    def GenerateType(self, GenerateType):
        self._GenerateType = GenerateType

    @property
    def Name(self):
        r"""<p>密钥名称，2-60 字符。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ResourceType(self):
        r"""<p>密钥归属资源类型。</p><p>枚举值：</p><ul><li>Consumer：消费者</li><li>ModelService：模型服务</li></ul>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def SecretType(self):
        r"""<p>密钥协议类型。</p><p>枚举值：</p><ul><li>ApiKey</li><li>Basic</li><li>Hmac</li><li>OAuth2</li><li>JWT</li></ul>
        :rtype: str
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def Description(self):
        r"""<p>密钥描述。最长 200 字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def JWTCredentialConfig(self):
        r"""<p>JWT凭证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWJWTCredentialConfig`
        """
        return self._JWTCredentialConfig

    @JWTCredentialConfig.setter
    def JWTCredentialConfig(self, JWTCredentialConfig):
        self._JWTCredentialConfig = JWTCredentialConfig

    @property
    def KmsKeyName(self):
        r"""<p>KMS 密钥名称。GenerateType=KMS 时必填。</p>
        :rtype: str
        """
        return self._KmsKeyName

    @KmsKeyName.setter
    def KmsKeyName(self, KmsKeyName):
        self._KmsKeyName = KmsKeyName

    @property
    def KmsKeyVersion(self):
        r"""<p>KMS 密钥版本。GenerateType=KMS 时必填。</p>
        :rtype: str
        """
        return self._KmsKeyVersion

    @KmsKeyVersion.setter
    def KmsKeyVersion(self, KmsKeyVersion):
        self._KmsKeyVersion = KmsKeyVersion

    @property
    def OAuthCredentialConfig(self):
        r"""<p>OAuth2.0凭证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWOAuthCredentialConfig`
        """
        return self._OAuthCredentialConfig

    @OAuthCredentialConfig.setter
    def OAuthCredentialConfig(self, OAuthCredentialConfig):
        self._OAuthCredentialConfig = OAuthCredentialConfig

    @property
    def OIDCCredentialConfig(self):
        r"""<p>OIDC凭证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWOIDCCredentialConfig`
        """
        return self._OIDCCredentialConfig

    @OIDCCredentialConfig.setter
    def OIDCCredentialConfig(self, OIDCCredentialConfig):
        self._OIDCCredentialConfig = OIDCCredentialConfig

    @property
    def Provider(self):
        r"""<p>第三方平台类型</p><p>枚举值：</p><ul><li>Dify： Dify平台</li></ul>
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def SecretValue(self):
        r"""<p>密钥值，长度 8-256。GenerateType=Custom 时必填。</p>
        :rtype: str
        """
        return self._SecretValue

    @SecretValue.setter
    def SecretValue(self, SecretValue):
        self._SecretValue = SecretValue


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GenerateType = params.get("GenerateType")
        self._Name = params.get("Name")
        self._ResourceType = params.get("ResourceType")
        self._SecretType = params.get("SecretType")
        self._Description = params.get("Description")
        if params.get("JWTCredentialConfig") is not None:
            self._JWTCredentialConfig = AIGWJWTCredentialConfig()
            self._JWTCredentialConfig._deserialize(params.get("JWTCredentialConfig"))
        self._KmsKeyName = params.get("KmsKeyName")
        self._KmsKeyVersion = params.get("KmsKeyVersion")
        if params.get("OAuthCredentialConfig") is not None:
            self._OAuthCredentialConfig = AIGWOAuthCredentialConfig()
            self._OAuthCredentialConfig._deserialize(params.get("OAuthCredentialConfig"))
        if params.get("OIDCCredentialConfig") is not None:
            self._OIDCCredentialConfig = AIGWOIDCCredentialConfig()
            self._OIDCCredentialConfig._deserialize(params.get("OIDCCredentialConfig"))
        self._Provider = params.get("Provider")
        self._SecretValue = params.get("SecretValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewaySecretKeyResponse(AbstractModel):
    r"""CreateCloudNativeAPIGatewaySecretKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>创建结果。包含成功标识与新建资源 ID。</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>创建结果。包含成功标识与新建资源 ID。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwCreateCommonResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwCreateCommonResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DefaultKongRoute(AbstractModel):
    r"""默认kong路由，目前只在 LLM 模型 API相 关接口使用

    """

    def __init__(self):
        r"""
        :param _Name: <p>服务名字</p>
        :type Name: str
        :param _ID: <p>服务ID</p>
        :type ID: str
        :param _Methods: <p>HTTP Method</p>
        :type Methods: list of str
        :param _Paths: <p>Http Path</p>
        :type Paths: list of str
        """
        self._Name = None
        self._ID = None
        self._Methods = None
        self._Paths = None

    @property
    def Name(self):
        r"""<p>服务名字</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ID(self):
        r"""<p>服务ID</p>
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Methods(self):
        r"""<p>HTTP Method</p>
        :rtype: list of str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Paths(self):
        r"""<p>Http Path</p>
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ID = params.get("ID")
        self._Methods = params.get("Methods")
        self._Paths = params.get("Paths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayConsumerGroupRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _ConsumerGroupId: 消费者组ID
        :type ConsumerGroupId: str
        """
        self._GatewayId = None
        self._ConsumerGroupId = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConsumerGroupId(self):
        r"""消费者组ID
        :rtype: str
        """
        return self._ConsumerGroupId

    @ConsumerGroupId.setter
    def ConsumerGroupId(self, ConsumerGroupId):
        self._ConsumerGroupId = ConsumerGroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ConsumerGroupId = params.get("ConsumerGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayConsumerGroupResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayConsumerGroup返回参数结构体

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


class DeleteCloudNativeAPIGatewayConsumerRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _ConsumerId: 消费者ID
        :type ConsumerId: str
        """
        self._GatewayId = None
        self._ConsumerId = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConsumerId(self):
        r"""消费者ID
        :rtype: str
        """
        return self._ConsumerId

    @ConsumerId.setter
    def ConsumerId(self, ConsumerId):
        self._ConsumerId = ConsumerId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ConsumerId = params.get("ConsumerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayConsumerResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayConsumer返回参数结构体

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


class DeleteCloudNativeAPIGatewayLLMModelAPIRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayLLMModelAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关 id。
        :type GatewayId: str
        :param _ModelAPIId: 模型 API ID，全局唯一标识。
        :type ModelAPIId: str
        """
        self._GatewayId = None
        self._ModelAPIId = None

    @property
    def GatewayId(self):
        r"""网关 id。
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ModelAPIId(self):
        r"""模型 API ID，全局唯一标识。
        :rtype: str
        """
        return self._ModelAPIId

    @ModelAPIId.setter
    def ModelAPIId(self, ModelAPIId):
        self._ModelAPIId = ModelAPIId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ModelAPIId = params.get("ModelAPIId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayLLMModelAPIResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayLLMModelAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>是否成功。</p>
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>是否成功。</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayLLMModelServiceRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayLLMModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关 id。
        :type GatewayId: str
        :param _ModelServiceId: 模型服务 ID，全局唯一标识。
        :type ModelServiceId: str
        """
        self._GatewayId = None
        self._ModelServiceId = None

    @property
    def GatewayId(self):
        r"""网关 id。
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ModelServiceId(self):
        r"""模型服务 ID，全局唯一标识。
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ModelServiceId = params.get("ModelServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayLLMModelServiceResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayLLMModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>是否成功。</p>
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>是否成功。</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayMCPServerRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayMCPServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>云原生API网关实例ID</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP服务ID</p>
        :type ServerId: str
        """
        self._GatewayId = None
        self._ServerId = None

    @property
    def GatewayId(self):
        r"""<p>云原生API网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP服务ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayMCPServerResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayMCPServer返回参数结构体

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


class DeleteCloudNativeAPIGatewayMCPToolRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayMCPTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例ID</p>
        :type GatewayId: str
        :param _ToolId: <p>工具id</p>
        :type ToolId: str
        :param _ServerId: <p>MCP 服务 id</p>
        :type ServerId: str
        """
        self._GatewayId = None
        self._ToolId = None
        self._ServerId = None

    @property
    def GatewayId(self):
        r"""<p>网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ToolId(self):
        r"""<p>工具id</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ServerId(self):
        r"""<p>MCP 服务 id</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ToolId = params.get("ToolId")
        self._ServerId = params.get("ServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayMCPToolResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewayMCPTool返回参数结构体

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


class DeleteCloudNativeAPIGatewaySecretKeyRequest(AbstractModel):
    r"""DeleteCloudNativeAPIGatewaySecretKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _SecretKeyId: 密钥id
        :type SecretKeyId: str
        """
        self._GatewayId = None
        self._SecretKeyId = None

    @property
    def GatewayId(self):
        r"""网关ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def SecretKeyId(self):
        r"""密钥id
        :rtype: str
        """
        return self._SecretKeyId

    @SecretKeyId.setter
    def SecretKeyId(self, SecretKeyId):
        self._SecretKeyId = SecretKeyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._SecretKeyId = params.get("SecretKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewaySecretKeyResponse(AbstractModel):
    r"""DeleteCloudNativeAPIGatewaySecretKey返回参数结构体

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


class DescribeCloudNativeAPIGatewayConsumerGroupRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例id</p>
        :type GatewayId: str
        :param _ConsumerGroupId: <p>消费者组ID</p>
        :type ConsumerGroupId: str
        """
        self._GatewayId = None
        self._ConsumerGroupId = None

    @property
    def GatewayId(self):
        r"""<p>网关实例id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConsumerGroupId(self):
        r"""<p>消费者组ID</p>
        :rtype: str
        """
        return self._ConsumerGroupId

    @ConsumerGroupId.setter
    def ConsumerGroupId(self, ConsumerGroupId):
        self._ConsumerGroupId = ConsumerGroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ConsumerGroupId = params.get("ConsumerGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayConsumerGroupResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>消费者组详情。</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwConsumerGroup`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>消费者组详情。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwConsumerGroup`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwConsumerGroup()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayConsumerRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例id</p>
        :type GatewayId: str
        :param _ConsumerId: <p>消费者ID</p>
        :type ConsumerId: str
        """
        self._GatewayId = None
        self._ConsumerId = None

    @property
    def GatewayId(self):
        r"""<p>网关实例id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConsumerId(self):
        r"""<p>消费者ID</p>
        :rtype: str
        """
        return self._ConsumerId

    @ConsumerId.setter
    def ConsumerId(self, ConsumerId):
        self._ConsumerId = ConsumerId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ConsumerId = params.get("ConsumerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayConsumerResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>消费者详情</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwConsumer`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>消费者详情</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwConsumer`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwConsumer()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayLLMModelAPIRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMModelAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关 id。</p>
        :type GatewayId: str
        :param _ModelAPIId: <p>模型 API ID，全局唯一标识。</p>
        :type ModelAPIId: str
        """
        self._GatewayId = None
        self._ModelAPIId = None

    @property
    def GatewayId(self):
        r"""<p>网关 id。</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ModelAPIId(self):
        r"""<p>模型 API ID，全局唯一标识。</p>
        :rtype: str
        """
        return self._ModelAPIId

    @ModelAPIId.setter
    def ModelAPIId(self, ModelAPIId):
        self._ModelAPIId = ModelAPIId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ModelAPIId = params.get("ModelAPIId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayLLMModelAPIResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMModelAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>模型 API 信息。</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelAPI`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>模型 API 信息。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelAPI`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CloudNativeAPIGatewayLLMModelAPI()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayLLMModelAPIsRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMModelAPIs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关 id。
        :type GatewayId: str
        :param _Limit: <p>每页条数，范围 [1, 1000]，默认 10。</p>
        :type Limit: int
        :param _Offset: <p>起始位置，从 0 开始。</p>
        :type Offset: int
        :param _Filters: <p>过滤条件。当前未启用具体字段。</p>
        :type Filters: list of Filter
        :param _Keyword: <p>模糊匹配模型 API 名称。</p>
        :type Keyword: str
        :param _ConsumerGroupId: <p>消费者组 ID（以 cg- 开头），与 UseToBind 搭配使用。</p>
        :type ConsumerGroupId: str
        :param _UseToBind: <p>是否用于绑定场景。true 时仅返回可被绑定到指定消费者组的模型 API。</p>
        :type UseToBind: bool
        :param _ConsumerId: <p>消费者 ID（以 consumer- 开头）。</p>
        :type ConsumerId: str
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Keyword = None
        self._ConsumerGroupId = None
        self._UseToBind = None
        self._ConsumerId = None

    @property
    def GatewayId(self):
        r"""网关 id。
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        r"""<p>每页条数，范围 [1, 1000]，默认 10。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>起始位置，从 0 开始。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""<p>过滤条件。当前未启用具体字段。</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Keyword(self):
        r"""<p>模糊匹配模型 API 名称。</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ConsumerGroupId(self):
        r"""<p>消费者组 ID（以 cg- 开头），与 UseToBind 搭配使用。</p>
        :rtype: str
        """
        return self._ConsumerGroupId

    @ConsumerGroupId.setter
    def ConsumerGroupId(self, ConsumerGroupId):
        self._ConsumerGroupId = ConsumerGroupId

    @property
    def UseToBind(self):
        r"""<p>是否用于绑定场景。true 时仅返回可被绑定到指定消费者组的模型 API。</p>
        :rtype: bool
        """
        return self._UseToBind

    @UseToBind.setter
    def UseToBind(self, UseToBind):
        self._UseToBind = UseToBind

    @property
    def ConsumerId(self):
        r"""<p>消费者 ID（以 consumer- 开头）。</p>
        :rtype: str
        """
        return self._ConsumerId

    @ConsumerId.setter
    def ConsumerId(self, ConsumerId):
        self._ConsumerId = ConsumerId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Keyword = params.get("Keyword")
        self._ConsumerGroupId = params.get("ConsumerGroupId")
        self._UseToBind = params.get("UseToBind")
        self._ConsumerId = params.get("ConsumerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayLLMModelAPIsResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMModelAPIs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 模型 API 列表。
        :type Result: :class:`tencentcloud.cngw.v20230418.models.ListCloudNativeAPIGatewayLLMModelAPI`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""模型 API 列表。
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ListCloudNativeAPIGatewayLLMModelAPI`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ListCloudNativeAPIGatewayLLMModelAPI()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayLLMModelServiceRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关 id。</p>
        :type GatewayId: str
        :param _ModelServiceId: <p>模型服务 ID，全局唯一标识。</p>
        :type ModelServiceId: str
        """
        self._GatewayId = None
        self._ModelServiceId = None

    @property
    def GatewayId(self):
        r"""<p>网关 id。</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ModelServiceId(self):
        r"""<p>模型服务 ID，全局唯一标识。</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ModelServiceId = params.get("ModelServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayLLMModelServiceResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>模型服务。</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelService`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>模型服务。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelService`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CloudNativeAPIGatewayLLMModelService()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayLLMModelServicesRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMModelServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关 id。</p>
        :type GatewayId: str
        :param _Limit: <p>返回数量，默认为 10，最大值为 1000。</p>
        :type Limit: int
        :param _Offset: <p>偏移量，默认为 0。</p>
        :type Offset: int
        :param _Filters: <p>过滤条件，多个过滤条件之间是“与”的关系，支持 Name</p>
        :type Filters: list of Filter
        :param _ModelAPIId: <p>通过模型 API 筛选模型服务</p>
        :type ModelAPIId: str
        :param _SecretKeyId: <p>通过密匙查询绑定的模型服务</p>
        :type SecretKeyId: str
        :param _Keyword: <p>搜索关键词，模糊匹配 name 和 description</p>
        :type Keyword: str
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._ModelAPIId = None
        self._SecretKeyId = None
        self._Keyword = None

    @property
    def GatewayId(self):
        r"""<p>网关 id。</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        r"""<p>返回数量，默认为 10，最大值为 1000。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>偏移量，默认为 0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""<p>过滤条件，多个过滤条件之间是“与”的关系，支持 Name</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ModelAPIId(self):
        r"""<p>通过模型 API 筛选模型服务</p>
        :rtype: str
        """
        return self._ModelAPIId

    @ModelAPIId.setter
    def ModelAPIId(self, ModelAPIId):
        self._ModelAPIId = ModelAPIId

    @property
    def SecretKeyId(self):
        r"""<p>通过密匙查询绑定的模型服务</p>
        :rtype: str
        """
        return self._SecretKeyId

    @SecretKeyId.setter
    def SecretKeyId(self, SecretKeyId):
        self._SecretKeyId = SecretKeyId

    @property
    def Keyword(self):
        r"""<p>搜索关键词，模糊匹配 name 和 description</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ModelAPIId = params.get("ModelAPIId")
        self._SecretKeyId = params.get("SecretKeyId")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayLLMModelServicesResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMModelServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>模型服务列表。</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.ListCloudNativeAPIGatewayLLMModelService`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>模型服务列表。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ListCloudNativeAPIGatewayLLMModelService`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ListCloudNativeAPIGatewayLLMModelService()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayLLMTokenUsageListRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMTokenUsageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例Id</p>
        :type GatewayId: str
        :param _StartTime: <p>查询起始时间戳</p><p>单位：秒</p>
        :type StartTime: int
        :param _EndTime: <p>查询结束时间戳</p><p>单位：秒</p>
        :type EndTime: int
        :param _Filters: <p>查询过滤条件，Name取值为ConsumerId或ConsumerGroupId</p>
        :type Filters: list of Filter
        :param _Limit: <p>分页条件，每页条数</p>
        :type Limit: int
        :param _Offset: <p>分页条件，分页偏移量</p>
        :type Offset: int
        """
        self._GatewayId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def GatewayId(self):
        r"""<p>网关实例Id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StartTime(self):
        r"""<p>查询起始时间戳</p><p>单位：秒</p>
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>查询结束时间戳</p><p>单位：秒</p>
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""<p>查询过滤条件，Name取值为ConsumerId或ConsumerGroupId</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""<p>分页条件，每页条数</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>分页条件，分页偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayLLMTokenUsageListResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMTokenUsageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>查询Token用量明细结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMTokenUsageListResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>查询Token用量明细结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMTokenUsageListResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AIGWLLMTokenUsageListResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayLLMTokenUsageStatisticsRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例Id</p>
        :type GatewayId: str
        :param _StartTime: <p>查询开始时间戳</p><p>单位：秒</p>
        :type StartTime: int
        :param _EndTime: <p>查询结束时间戳</p><p>单位：秒</p>
        :type EndTime: int
        :param _Filters: <p>查询过滤条件</p>
        :type Filters: list of Filter
        """
        self._GatewayId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None

    @property
    def GatewayId(self):
        r"""<p>网关实例Id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StartTime(self):
        r"""<p>查询开始时间戳</p><p>单位：秒</p>
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>查询结束时间戳</p><p>单位：秒</p>
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""<p>查询过滤条件</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
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
        


class DescribeCloudNativeAPIGatewayLLMTokenUsageStatisticsResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>请求结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMTokenUsageStatisticsResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>请求结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMTokenUsageStatisticsResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AIGWLLMTokenUsageStatisticsResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayMCPServerACLRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPServerACL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例 ID</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP服务ID</p>
        :type ServerId: str
        """
        self._GatewayId = None
        self._ServerId = None

    @property
    def GatewayId(self):
        r"""<p>网关实例 ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP服务ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayMCPServerACLResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPServerACL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>MCP 服务 ACL 列表结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPServerACLResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>MCP 服务 ACL 列表结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPServerACLResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AIGWMCPServerACLResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayMCPServerAuthRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPServerAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例ID</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP服务ID</p>
        :type ServerId: str
        """
        self._GatewayId = None
        self._ServerId = None

    @property
    def GatewayId(self):
        r"""<p>网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP服务ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayMCPServerAuthResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPServerAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>MCP服务认证查询结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPServerAuthResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>MCP服务认证查询结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPServerAuthResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AIGWMCPServerAuthResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayMCPServerListRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPServerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>实例 ID</p>
        :type GatewayId: str
        :param _Limit: <p>分页大小</p>
        :type Limit: int
        :param _Offset: <p>分页偏移</p>
        :type Offset: int
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None

    @property
    def GatewayId(self):
        r"""<p>实例 ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        r"""<p>分页大小</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>分页偏移</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayMCPServerListResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPServerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>MCP Server 列表结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPServerList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>MCP Server 列表结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPServerList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AIGWMCPServerList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayMCPServerRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>云原生API网关实例ID</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP服务ID</p>
        :type ServerId: str
        """
        self._GatewayId = None
        self._ServerId = None

    @property
    def GatewayId(self):
        r"""<p>云原生API网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP服务ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayMCPServerResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>mcp server详情</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPServer`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>mcp server详情</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPServer`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AIGWMCPServer()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayMCPToolACLListRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPToolACLList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例ID</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP 服务ID</p>
        :type ServerId: str
        :param _Limit: <p>分页大小</p>
        :type Limit: int
        :param _Offset: <p>分页偏移</p>
        :type Offset: int
        :param _Keyword: <p>搜索关键词</p>
        :type Keyword: str
        """
        self._GatewayId = None
        self._ServerId = None
        self._Limit = None
        self._Offset = None
        self._Keyword = None

    @property
    def GatewayId(self):
        r"""<p>网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP 服务ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def Limit(self):
        r"""<p>分页大小</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>分页偏移</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Keyword(self):
        r"""<p>搜索关键词</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayMCPToolACLListResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPToolACLList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>MCP 服务 Tool ACL 列表结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPToolACLListResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>MCP 服务 Tool ACL 列表结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPToolACLListResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AIGWMCPToolACLListResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayMCPToolListRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPToolList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>实例 id</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP服务 id</p>
        :type ServerId: str
        :param _Limit: <p>条数</p><p>取值范围：[1, 100]</p>
        :type Limit: int
        :param _Offset: <p>开始位置</p><p>取值范围：[1, 100000]</p>
        :type Offset: int
        """
        self._GatewayId = None
        self._ServerId = None
        self._Limit = None
        self._Offset = None

    @property
    def GatewayId(self):
        r"""<p>实例 id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP服务 id</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def Limit(self):
        r"""<p>条数</p><p>取值范围：[1, 100]</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>开始位置</p><p>取值范围：[1, 100000]</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayMCPToolListResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPToolList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>tool 列表</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwMCPToolList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>tool 列表</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwMCPToolList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwMCPToolList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayMCPToolRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例 id</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP Server id</p>
        :type ServerId: str
        :param _ToolId: <p>工具 id</p>
        :type ToolId: str
        """
        self._GatewayId = None
        self._ServerId = None
        self._ToolId = None

    @property
    def GatewayId(self):
        r"""<p>网关实例 id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP Server id</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def ToolId(self):
        r"""<p>工具 id</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._ToolId = params.get("ToolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayMCPToolResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPTool返回参数结构体

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


class DescribeCloudNativeAPIGatewayMCPToolsFromFileRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPToolsFromFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: <p>OpenAPI文件内容</p>
        :type Content: str
        :param _Format: <p>文件内容格式</p>
        :type Format: str
        :param _GatewayId: <p>网关实例ID</p>
        :type GatewayId: str
        :param _MCPServerId: <p>MCP Server ID</p>
        :type MCPServerId: str
        """
        self._Content = None
        self._Format = None
        self._GatewayId = None
        self._MCPServerId = None

    @property
    def Content(self):
        r"""<p>OpenAPI文件内容</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Format(self):
        r"""<p>文件内容格式</p>
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def GatewayId(self):
        r"""<p>网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def MCPServerId(self):
        r"""<p>MCP Server ID</p>
        :rtype: str
        """
        return self._MCPServerId

    @MCPServerId.setter
    def MCPServerId(self, MCPServerId):
        self._MCPServerId = MCPServerId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Format = params.get("Format")
        self._GatewayId = params.get("GatewayId")
        self._MCPServerId = params.get("MCPServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayMCPToolsFromFileResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewayMCPToolsFromFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>解析结果</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwParseMCPToolsResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>解析结果</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwParseMCPToolsResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwParseMCPToolsResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewaySecretKeyRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewaySecretKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>实例 ID</p>
        :type GatewayId: str
        :param _SecretKeyId: <p>密钥id</p>
        :type SecretKeyId: str
        """
        self._GatewayId = None
        self._SecretKeyId = None

    @property
    def GatewayId(self):
        r"""<p>实例 ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def SecretKeyId(self):
        r"""<p>密钥id</p>
        :rtype: str
        """
        return self._SecretKeyId

    @SecretKeyId.setter
    def SecretKeyId(self, SecretKeyId):
        self._SecretKeyId = SecretKeyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._SecretKeyId = params.get("SecretKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewaySecretKeyResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewaySecretKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>密钥详情。</p>
        :type Result: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwSecretKey`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>密钥详情。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CNAPIGwSecretKey`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CNAPIGwSecretKey()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewaySecretKeyValueRequest(AbstractModel):
    r"""DescribeCloudNativeAPIGatewaySecretKeyValue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 实例 ID
        :type GatewayId: str
        :param _SecretKeyId: 密钥id
        :type SecretKeyId: str
        """
        self._GatewayId = None
        self._SecretKeyId = None

    @property
    def GatewayId(self):
        r"""实例 ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def SecretKeyId(self):
        r"""密钥id
        :rtype: str
        """
        return self._SecretKeyId

    @SecretKeyId.setter
    def SecretKeyId(self, SecretKeyId):
        self._SecretKeyId = SecretKeyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._SecretKeyId = params.get("SecretKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewaySecretKeyValueResponse(AbstractModel):
    r"""DescribeCloudNativeAPIGatewaySecretKeyValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 密钥值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""密钥值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""查询过滤通用对象

    """

    def __init__(self):
        r"""
        :param _Name: <p>过滤参数名</p>
        :type Name: str
        :param _Values: <p>过滤参数值</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>过滤参数名</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>过滤参数值</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    r"""Key/Value结构

    """

    def __init__(self):
        r"""
        :param _Key: 条件的Key
        :type Key: str
        :param _Value: 条件的Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""条件的Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""条件的Value
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
        


class ListCloudNativeAPIGatewayLLMModelAPI(AbstractModel):
    r"""LLM 模型 API 列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _DataList: AI 网关模型 API 列表。
        :type DataList: list of CloudNativeAPIGatewayLLMModelAPI
        """
        self._TotalCount = None
        self._DataList = None

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
    def DataList(self):
        r"""AI 网关模型 API 列表。
        :rtype: list of CloudNativeAPIGatewayLLMModelAPI
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = CloudNativeAPIGatewayLLMModelAPI()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCloudNativeAPIGatewayLLMModelService(AbstractModel):
    r"""LLM 模型服务列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 模型服务数量。
        :type TotalCount: int
        :param _DataList: 模型服务列表。
        :type DataList: list of CloudNativeAPIGatewayLLMModelService
        """
        self._TotalCount = None
        self._DataList = None

    @property
    def TotalCount(self):
        r"""模型服务数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataList(self):
        r"""模型服务列表。
        :rtype: list of CloudNativeAPIGatewayLLMModelService
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = CloudNativeAPIGatewayLLMModelService()
                obj._deserialize(item)
                self._DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayConsumerGroupRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _ConsumerGroupId: <p>消费者组 ID（以 cg- 开头）。</p>
        :type ConsumerGroupId: str
        :param _Name: <p>消费者组名称，最长 60 字符。</p>
        :type Name: str
        :param _Status: <p>启用状态。</p><p>枚举值：</p><ul><li>Enable：启用</li><li>Disable：禁用</li></ul>
        :type Status: str
        :param _Description: <p>消费者组描述。最长 200 字符。</p>
        :type Description: str
        """
        self._GatewayId = None
        self._ConsumerGroupId = None
        self._Name = None
        self._Status = None
        self._Description = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConsumerGroupId(self):
        r"""<p>消费者组 ID（以 cg- 开头）。</p>
        :rtype: str
        """
        return self._ConsumerGroupId

    @ConsumerGroupId.setter
    def ConsumerGroupId(self, ConsumerGroupId):
        self._ConsumerGroupId = ConsumerGroupId

    @property
    def Name(self):
        r"""<p>消费者组名称，最长 60 字符。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""<p>启用状态。</p><p>枚举值：</p><ul><li>Enable：启用</li><li>Disable：禁用</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        r"""<p>消费者组描述。最长 200 字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ConsumerGroupId = params.get("ConsumerGroupId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayConsumerGroupResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayConsumerGroup返回参数结构体

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


class ModifyCloudNativeAPIGatewayConsumerRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _ConsumerId: <p>消费者 ID。</p>
        :type ConsumerId: str
        :param _Name: <p>消费者名称，最长 60 字符。</p>
        :type Name: str
        :param _Description: <p>消费者描述。最长 200 字符。</p>
        :type Description: str
        """
        self._GatewayId = None
        self._ConsumerId = None
        self._Name = None
        self._Description = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConsumerId(self):
        r"""<p>消费者 ID。</p>
        :rtype: str
        """
        return self._ConsumerId

    @ConsumerId.setter
    def ConsumerId(self, ConsumerId):
        self._ConsumerId = ConsumerId

    @property
    def Name(self):
        r"""<p>消费者名称，最长 60 字符。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>消费者描述。最长 200 字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ConsumerId = params.get("ConsumerId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayConsumerResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayConsumer返回参数结构体

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


class ModifyCloudNativeAPIGatewayLLMModelAPIRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayLLMModelAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关 id。</p>
        :type GatewayId: str
        :param _ModelAPIId: <p>模型 API ID，全局唯一标识。</p>
        :type ModelAPIId: str
        :param _Name: <p>模型 API 名称，最长 60 字符。</p>
        :type Name: str
        :param _BasePath: <p>统一前缀路径（可选）。例如 /v1/openai。</p>
        :type BasePath: str
        :param _Description: <p>模型 API 描述。最长 200 字符。</p>
        :type Description: str
        :param _ListModelServiceId: <p>关联的模型服务 ID 列表，长度 1-10。</p>
        :type ListModelServiceId: list of str
        :param _ModelServiceRoute: <p>多模型服务路由策略。ListModelServiceId 多于 1 项时必填。</p>
        :type ModelServiceRoute: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelServiceRoute`
        :param _MatchHeaders: <p>Header 路由匹配规则。当前仅支持 Operator=exact。</p>
        :type MatchHeaders: list of AIGWKVMatch
        :param _EnableCrossServiceFallback: <p>是否启用跨服务 Fallback。</p>
        :type EnableCrossServiceFallback: bool
        :param _CrossServiceFallbackConfig: <p>跨服务 Fallback 配置。EnableCrossServiceFallback=true 时必填。</p>
        :type CrossServiceFallbackConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWCrossServiceFallbackConfig`
        :param _TagFilter: <p>标签过滤策略。需要网关版本 ≥ 3.9.4。</p>
        :type TagFilter: :class:`tencentcloud.cngw.v20230418.models.AIGWTagFilter`
        :param _LogConfig: <p>日志输出配置。需要网关版本 ≥ 3.9.4。</p>
        :type LogConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWLogConfig`
        """
        self._GatewayId = None
        self._ModelAPIId = None
        self._Name = None
        self._BasePath = None
        self._Description = None
        self._ListModelServiceId = None
        self._ModelServiceRoute = None
        self._MatchHeaders = None
        self._EnableCrossServiceFallback = None
        self._CrossServiceFallbackConfig = None
        self._TagFilter = None
        self._LogConfig = None

    @property
    def GatewayId(self):
        r"""<p>网关 id。</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ModelAPIId(self):
        r"""<p>模型 API ID，全局唯一标识。</p>
        :rtype: str
        """
        return self._ModelAPIId

    @ModelAPIId.setter
    def ModelAPIId(self, ModelAPIId):
        self._ModelAPIId = ModelAPIId

    @property
    def Name(self):
        r"""<p>模型 API 名称，最长 60 字符。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BasePath(self):
        r"""<p>统一前缀路径（可选）。例如 /v1/openai。</p>
        :rtype: str
        """
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def Description(self):
        r"""<p>模型 API 描述。最长 200 字符。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ListModelServiceId(self):
        r"""<p>关联的模型服务 ID 列表，长度 1-10。</p>
        :rtype: list of str
        """
        return self._ListModelServiceId

    @ListModelServiceId.setter
    def ListModelServiceId(self, ListModelServiceId):
        self._ListModelServiceId = ListModelServiceId

    @property
    def ModelServiceRoute(self):
        r"""<p>多模型服务路由策略。ListModelServiceId 多于 1 项时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelServiceRoute`
        """
        return self._ModelServiceRoute

    @ModelServiceRoute.setter
    def ModelServiceRoute(self, ModelServiceRoute):
        self._ModelServiceRoute = ModelServiceRoute

    @property
    def MatchHeaders(self):
        r"""<p>Header 路由匹配规则。当前仅支持 Operator=exact。</p>
        :rtype: list of AIGWKVMatch
        """
        return self._MatchHeaders

    @MatchHeaders.setter
    def MatchHeaders(self, MatchHeaders):
        self._MatchHeaders = MatchHeaders

    @property
    def EnableCrossServiceFallback(self):
        r"""<p>是否启用跨服务 Fallback。</p>
        :rtype: bool
        """
        return self._EnableCrossServiceFallback

    @EnableCrossServiceFallback.setter
    def EnableCrossServiceFallback(self, EnableCrossServiceFallback):
        self._EnableCrossServiceFallback = EnableCrossServiceFallback

    @property
    def CrossServiceFallbackConfig(self):
        r"""<p>跨服务 Fallback 配置。EnableCrossServiceFallback=true 时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWCrossServiceFallbackConfig`
        """
        return self._CrossServiceFallbackConfig

    @CrossServiceFallbackConfig.setter
    def CrossServiceFallbackConfig(self, CrossServiceFallbackConfig):
        self._CrossServiceFallbackConfig = CrossServiceFallbackConfig

    @property
    def TagFilter(self):
        r"""<p>标签过滤策略。需要网关版本 ≥ 3.9.4。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWTagFilter`
        """
        return self._TagFilter

    @TagFilter.setter
    def TagFilter(self, TagFilter):
        self._TagFilter = TagFilter

    @property
    def LogConfig(self):
        r"""<p>日志输出配置。需要网关版本 ≥ 3.9.4。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLogConfig`
        """
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ModelAPIId = params.get("ModelAPIId")
        self._Name = params.get("Name")
        self._BasePath = params.get("BasePath")
        self._Description = params.get("Description")
        self._ListModelServiceId = params.get("ListModelServiceId")
        if params.get("ModelServiceRoute") is not None:
            self._ModelServiceRoute = CloudNativeAPIGatewayLLMModelServiceRoute()
            self._ModelServiceRoute._deserialize(params.get("ModelServiceRoute"))
        if params.get("MatchHeaders") is not None:
            self._MatchHeaders = []
            for item in params.get("MatchHeaders"):
                obj = AIGWKVMatch()
                obj._deserialize(item)
                self._MatchHeaders.append(obj)
        self._EnableCrossServiceFallback = params.get("EnableCrossServiceFallback")
        if params.get("CrossServiceFallbackConfig") is not None:
            self._CrossServiceFallbackConfig = AIGWCrossServiceFallbackConfig()
            self._CrossServiceFallbackConfig._deserialize(params.get("CrossServiceFallbackConfig"))
        if params.get("TagFilter") is not None:
            self._TagFilter = AIGWTagFilter()
            self._TagFilter._deserialize(params.get("TagFilter"))
        if params.get("LogConfig") is not None:
            self._LogConfig = AIGWLogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayLLMModelAPIResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayLLMModelAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>是否成功。</p>
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>是否成功。</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayLLMModelServiceRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayLLMModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关 id。</p>
        :type GatewayId: str
        :param _ModelServiceId: <p>模型服务 ID，全局唯一标识。</p>
        :type ModelServiceId: str
        :param _Name: <p>修改服务名称，长度2-50字符，支持中英文、数字、下划线。</p>
        :type Name: str
        :param _DefaultModel: <p>修改默认模型，模型选择方式为 Specify 时必填。</p>
        :type DefaultModel: str
        :param _ModelSelector: <p>修改模型选择方式，选项：Specify（指定模型）、PassThrough（透传请求模型）。</p>
        :type ModelSelector: str
        :param _EnableModelFallback: <p>修改开启模型降级，模型选择方式为 Specify 时必填。</p>
        :type EnableModelFallback: bool
        :param _ModelFallbackRule: <p>修改可以配置备用模型规则，EnableSpecifyModelFallback 为 true 时必填。</p>
        :type ModelFallbackRule: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelFallbackRule`
        :param _EnableModelParamCheck: <p>修改开启模型参数校验，是否校验客户端传递的 model 参数, 模型选择方式为 PassThrough 时必填</p>
        :type EnableModelParamCheck: bool
        :param _ModelParamCheckRule: <p>修改模型检验信息，EnableModelParamCheck 为 true 时必填。</p>
        :type ModelParamCheckRule: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelParamCheckInfo`
        :param _Description: <p>修改描述。</p>
        :type Description: str
        :param _UpstreamURL: <p>修改模型服务地址</p>
        :type UpstreamURL: str
        :param _ConnectTimeout: <p>连接超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：10000</p>
        :type ConnectTimeout: int
        :param _WriteTimeout: <p>写入超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :type WriteTimeout: int
        :param _ReadTimeout: <p>读取超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :type ReadTimeout: int
        :param _Retries: <p>重试次数</p><p>取值范围：[0, 5]</p><p>单位：次</p><p>默认值：0</p>
        :type Retries: int
        :param _UpstreamUrlMode: <p>路径拼接模式</p><p>枚举值：</p><ul><li>FixedPath： 固定路径</li><li>AutoConcat： 自动拼接</li></ul>
        :type UpstreamUrlMode: str
        :param _SNI: <p>SNI</p>
        :type SNI: str
        :param _QuotaLimit: <p>模型服务级别的配额上限（RPM/TPM）。需要网关版本 ≥ 3.9.4。</p>
        :type QuotaLimit: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMQuotaLimit`
        :param _Tags: <p>标签</p>
        :type Tags: list of str
        :param _ModelRewriteRules: <p>参数改写规则</p>
        :type ModelRewriteRules: list of AIGWModelRewriteRule
        :param _ExternalInstanceId: <p>外部服务来源ID</p>
        :type ExternalInstanceId: str
        :param _ExtParams: <p>其他参数</p>
        :type ExtParams: list of KeyValue
        :param _KeyRotationEnabled: <p>密钥轮转开关</p>
        :type KeyRotationEnabled: bool
        :param _KeyRotationPeriodDays: <p>密钥轮转周期</p><p>单位：天数</p>
        :type KeyRotationPeriodDays: int
        :param _SourceId: <p>来源服务 ID。</p>
        :type SourceId: str
        :param _Namespace: <p>命名空间。</p>
        :type Namespace: str
        :param _ServiceName: <p>服务名称。</p>
        :type ServiceName: str
        :param _Protocol: <p>协议类型，如 OpenAI、Custom。</p>
        :type Protocol: str
        """
        self._GatewayId = None
        self._ModelServiceId = None
        self._Name = None
        self._DefaultModel = None
        self._ModelSelector = None
        self._EnableModelFallback = None
        self._ModelFallbackRule = None
        self._EnableModelParamCheck = None
        self._ModelParamCheckRule = None
        self._Description = None
        self._UpstreamURL = None
        self._ConnectTimeout = None
        self._WriteTimeout = None
        self._ReadTimeout = None
        self._Retries = None
        self._UpstreamUrlMode = None
        self._SNI = None
        self._QuotaLimit = None
        self._Tags = None
        self._ModelRewriteRules = None
        self._ExternalInstanceId = None
        self._ExtParams = None
        self._KeyRotationEnabled = None
        self._KeyRotationPeriodDays = None
        self._SourceId = None
        self._Namespace = None
        self._ServiceName = None
        self._Protocol = None

    @property
    def GatewayId(self):
        r"""<p>网关 id。</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ModelServiceId(self):
        r"""<p>模型服务 ID，全局唯一标识。</p>
        :rtype: str
        """
        return self._ModelServiceId

    @ModelServiceId.setter
    def ModelServiceId(self, ModelServiceId):
        self._ModelServiceId = ModelServiceId

    @property
    def Name(self):
        r"""<p>修改服务名称，长度2-50字符，支持中英文、数字、下划线。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DefaultModel(self):
        r"""<p>修改默认模型，模型选择方式为 Specify 时必填。</p>
        :rtype: str
        """
        return self._DefaultModel

    @DefaultModel.setter
    def DefaultModel(self, DefaultModel):
        self._DefaultModel = DefaultModel

    @property
    def ModelSelector(self):
        r"""<p>修改模型选择方式，选项：Specify（指定模型）、PassThrough（透传请求模型）。</p>
        :rtype: str
        """
        return self._ModelSelector

    @ModelSelector.setter
    def ModelSelector(self, ModelSelector):
        self._ModelSelector = ModelSelector

    @property
    def EnableModelFallback(self):
        r"""<p>修改开启模型降级，模型选择方式为 Specify 时必填。</p>
        :rtype: bool
        """
        return self._EnableModelFallback

    @EnableModelFallback.setter
    def EnableModelFallback(self, EnableModelFallback):
        self._EnableModelFallback = EnableModelFallback

    @property
    def ModelFallbackRule(self):
        r"""<p>修改可以配置备用模型规则，EnableSpecifyModelFallback 为 true 时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelFallbackRule`
        """
        return self._ModelFallbackRule

    @ModelFallbackRule.setter
    def ModelFallbackRule(self, ModelFallbackRule):
        self._ModelFallbackRule = ModelFallbackRule

    @property
    def EnableModelParamCheck(self):
        r"""<p>修改开启模型参数校验，是否校验客户端传递的 model 参数, 模型选择方式为 PassThrough 时必填</p>
        :rtype: bool
        """
        return self._EnableModelParamCheck

    @EnableModelParamCheck.setter
    def EnableModelParamCheck(self, EnableModelParamCheck):
        self._EnableModelParamCheck = EnableModelParamCheck

    @property
    def ModelParamCheckRule(self):
        r"""<p>修改模型检验信息，EnableModelParamCheck 为 true 时必填。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CloudNativeAPIGatewayLLMModelParamCheckInfo`
        """
        return self._ModelParamCheckRule

    @ModelParamCheckRule.setter
    def ModelParamCheckRule(self, ModelParamCheckRule):
        self._ModelParamCheckRule = ModelParamCheckRule

    @property
    def Description(self):
        r"""<p>修改描述。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UpstreamURL(self):
        r"""<p>修改模型服务地址</p>
        :rtype: str
        """
        return self._UpstreamURL

    @UpstreamURL.setter
    def UpstreamURL(self, UpstreamURL):
        self._UpstreamURL = UpstreamURL

    @property
    def ConnectTimeout(self):
        r"""<p>连接超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：10000</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def WriteTimeout(self):
        r"""<p>写入超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :rtype: int
        """
        return self._WriteTimeout

    @WriteTimeout.setter
    def WriteTimeout(self, WriteTimeout):
        self._WriteTimeout = WriteTimeout

    @property
    def ReadTimeout(self):
        r"""<p>读取超时时间</p><p>取值范围：[1, 3600000]</p><p>单位：毫秒</p><p>默认值：60000</p>
        :rtype: int
        """
        return self._ReadTimeout

    @ReadTimeout.setter
    def ReadTimeout(self, ReadTimeout):
        self._ReadTimeout = ReadTimeout

    @property
    def Retries(self):
        r"""<p>重试次数</p><p>取值范围：[0, 5]</p><p>单位：次</p><p>默认值：0</p>
        :rtype: int
        """
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamUrlMode(self):
        r"""<p>路径拼接模式</p><p>枚举值：</p><ul><li>FixedPath： 固定路径</li><li>AutoConcat： 自动拼接</li></ul>
        :rtype: str
        """
        return self._UpstreamUrlMode

    @UpstreamUrlMode.setter
    def UpstreamUrlMode(self, UpstreamUrlMode):
        self._UpstreamUrlMode = UpstreamUrlMode

    @property
    def SNI(self):
        r"""<p>SNI</p>
        :rtype: str
        """
        return self._SNI

    @SNI.setter
    def SNI(self, SNI):
        self._SNI = SNI

    @property
    def QuotaLimit(self):
        r"""<p>模型服务级别的配额上限（RPM/TPM）。需要网关版本 ≥ 3.9.4。</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWLLMQuotaLimit`
        """
        return self._QuotaLimit

    @QuotaLimit.setter
    def QuotaLimit(self, QuotaLimit):
        self._QuotaLimit = QuotaLimit

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ModelRewriteRules(self):
        r"""<p>参数改写规则</p>
        :rtype: list of AIGWModelRewriteRule
        """
        return self._ModelRewriteRules

    @ModelRewriteRules.setter
    def ModelRewriteRules(self, ModelRewriteRules):
        self._ModelRewriteRules = ModelRewriteRules

    @property
    def ExternalInstanceId(self):
        r"""<p>外部服务来源ID</p>
        :rtype: str
        """
        return self._ExternalInstanceId

    @ExternalInstanceId.setter
    def ExternalInstanceId(self, ExternalInstanceId):
        self._ExternalInstanceId = ExternalInstanceId

    @property
    def ExtParams(self):
        r"""<p>其他参数</p>
        :rtype: list of KeyValue
        """
        return self._ExtParams

    @ExtParams.setter
    def ExtParams(self, ExtParams):
        self._ExtParams = ExtParams

    @property
    def KeyRotationEnabled(self):
        r"""<p>密钥轮转开关</p>
        :rtype: bool
        """
        return self._KeyRotationEnabled

    @KeyRotationEnabled.setter
    def KeyRotationEnabled(self, KeyRotationEnabled):
        self._KeyRotationEnabled = KeyRotationEnabled

    @property
    def KeyRotationPeriodDays(self):
        r"""<p>密钥轮转周期</p><p>单位：天数</p>
        :rtype: int
        """
        return self._KeyRotationPeriodDays

    @KeyRotationPeriodDays.setter
    def KeyRotationPeriodDays(self, KeyRotationPeriodDays):
        self._KeyRotationPeriodDays = KeyRotationPeriodDays

    @property
    def SourceId(self):
        r"""<p>来源服务 ID。</p>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Namespace(self):
        r"""<p>命名空间。</p>
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ServiceName(self):
        r"""<p>服务名称。</p>
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Protocol(self):
        r"""<p>协议类型，如 OpenAI、Custom。</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ModelServiceId = params.get("ModelServiceId")
        self._Name = params.get("Name")
        self._DefaultModel = params.get("DefaultModel")
        self._ModelSelector = params.get("ModelSelector")
        self._EnableModelFallback = params.get("EnableModelFallback")
        if params.get("ModelFallbackRule") is not None:
            self._ModelFallbackRule = CloudNativeAPIGatewayLLMModelFallbackRule()
            self._ModelFallbackRule._deserialize(params.get("ModelFallbackRule"))
        self._EnableModelParamCheck = params.get("EnableModelParamCheck")
        if params.get("ModelParamCheckRule") is not None:
            self._ModelParamCheckRule = CloudNativeAPIGatewayLLMModelParamCheckInfo()
            self._ModelParamCheckRule._deserialize(params.get("ModelParamCheckRule"))
        self._Description = params.get("Description")
        self._UpstreamURL = params.get("UpstreamURL")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._WriteTimeout = params.get("WriteTimeout")
        self._ReadTimeout = params.get("ReadTimeout")
        self._Retries = params.get("Retries")
        self._UpstreamUrlMode = params.get("UpstreamUrlMode")
        self._SNI = params.get("SNI")
        if params.get("QuotaLimit") is not None:
            self._QuotaLimit = AIGWLLMQuotaLimit()
            self._QuotaLimit._deserialize(params.get("QuotaLimit"))
        self._Tags = params.get("Tags")
        if params.get("ModelRewriteRules") is not None:
            self._ModelRewriteRules = []
            for item in params.get("ModelRewriteRules"):
                obj = AIGWModelRewriteRule()
                obj._deserialize(item)
                self._ModelRewriteRules.append(obj)
        self._ExternalInstanceId = params.get("ExternalInstanceId")
        if params.get("ExtParams") is not None:
            self._ExtParams = []
            for item in params.get("ExtParams"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ExtParams.append(obj)
        self._KeyRotationEnabled = params.get("KeyRotationEnabled")
        self._KeyRotationPeriodDays = params.get("KeyRotationPeriodDays")
        self._SourceId = params.get("SourceId")
        self._Namespace = params.get("Namespace")
        self._ServiceName = params.get("ServiceName")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayLLMModelServiceResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayLLMModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>是否成功</p>
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>是否成功</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayMCPServerACLRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPServerACL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例ID</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP服务ID</p>
        :type ServerId: str
        :param _ACLType: <p>ACL类型</p><p>枚举值：</p><ul><li>None： 不开启</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul><p>默认值：None</p>
        :type ACLType: str
        :param _ACLConsumerIds: <p>需要关联的消费者ID列表</p>
        :type ACLConsumerIds: list of str
        :param _ACLConsumerGroupIds: <p>需要关联的消费者组ID列表</p>
        :type ACLConsumerGroupIds: list of str
        """
        self._GatewayId = None
        self._ServerId = None
        self._ACLType = None
        self._ACLConsumerIds = None
        self._ACLConsumerGroupIds = None

    @property
    def GatewayId(self):
        r"""<p>网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP服务ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def ACLType(self):
        r"""<p>ACL类型</p><p>枚举值：</p><ul><li>None： 不开启</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul><p>默认值：None</p>
        :rtype: str
        """
        return self._ACLType

    @ACLType.setter
    def ACLType(self, ACLType):
        self._ACLType = ACLType

    @property
    def ACLConsumerIds(self):
        r"""<p>需要关联的消费者ID列表</p>
        :rtype: list of str
        """
        return self._ACLConsumerIds

    @ACLConsumerIds.setter
    def ACLConsumerIds(self, ACLConsumerIds):
        self._ACLConsumerIds = ACLConsumerIds

    @property
    def ACLConsumerGroupIds(self):
        r"""<p>需要关联的消费者组ID列表</p>
        :rtype: list of str
        """
        return self._ACLConsumerGroupIds

    @ACLConsumerGroupIds.setter
    def ACLConsumerGroupIds(self, ACLConsumerGroupIds):
        self._ACLConsumerGroupIds = ACLConsumerGroupIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._ACLType = params.get("ACLType")
        self._ACLConsumerIds = params.get("ACLConsumerIds")
        self._ACLConsumerGroupIds = params.get("ACLConsumerGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayMCPServerACLResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPServerACL返回参数结构体

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


class ModifyCloudNativeAPIGatewayMCPServerAuthRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPServerAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例ID</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP服务ID</p>
        :type ServerId: str
        :param _AuthType: <p>认证类型</p><p>枚举值：</p><ul><li>None： 无认证</li><li>ApiKey： API Key认证</li></ul>
        :type AuthType: str
        :param _JWTAuthConfig: <p>JWT认证配置</p>
        :type JWTAuthConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWJWTAuthPluginConfig`
        :param _OAuthAuthConfig: <p>OAuth认证配置</p>
        :type OAuthAuthConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWOAuthAuthPluginConfig`
        :param _OIDCAuthConfig: <p>OIDC认证配置</p>
        :type OIDCAuthConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWOIDCAuthPluginConfig`
        """
        self._GatewayId = None
        self._ServerId = None
        self._AuthType = None
        self._JWTAuthConfig = None
        self._OAuthAuthConfig = None
        self._OIDCAuthConfig = None

    @property
    def GatewayId(self):
        r"""<p>网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP服务ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def AuthType(self):
        r"""<p>认证类型</p><p>枚举值：</p><ul><li>None： 无认证</li><li>ApiKey： API Key认证</li></ul>
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def JWTAuthConfig(self):
        r"""<p>JWT认证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWJWTAuthPluginConfig`
        """
        return self._JWTAuthConfig

    @JWTAuthConfig.setter
    def JWTAuthConfig(self, JWTAuthConfig):
        self._JWTAuthConfig = JWTAuthConfig

    @property
    def OAuthAuthConfig(self):
        r"""<p>OAuth认证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWOAuthAuthPluginConfig`
        """
        return self._OAuthAuthConfig

    @OAuthAuthConfig.setter
    def OAuthAuthConfig(self, OAuthAuthConfig):
        self._OAuthAuthConfig = OAuthAuthConfig

    @property
    def OIDCAuthConfig(self):
        r"""<p>OIDC认证配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWOIDCAuthPluginConfig`
        """
        return self._OIDCAuthConfig

    @OIDCAuthConfig.setter
    def OIDCAuthConfig(self, OIDCAuthConfig):
        self._OIDCAuthConfig = OIDCAuthConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._AuthType = params.get("AuthType")
        if params.get("JWTAuthConfig") is not None:
            self._JWTAuthConfig = AIGWJWTAuthPluginConfig()
            self._JWTAuthConfig._deserialize(params.get("JWTAuthConfig"))
        if params.get("OAuthAuthConfig") is not None:
            self._OAuthAuthConfig = AIGWOAuthAuthPluginConfig()
            self._OAuthAuthConfig._deserialize(params.get("OAuthAuthConfig"))
        if params.get("OIDCAuthConfig") is not None:
            self._OIDCAuthConfig = AIGWOIDCAuthPluginConfig()
            self._OIDCAuthConfig._deserialize(params.get("OIDCAuthConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayMCPServerAuthResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPServerAuth返回参数结构体

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


class ModifyCloudNativeAPIGatewayMCPServerRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>实例 ID</p>
        :type GatewayId: str
        :param _DisplayName: <p>展示名字</p>
        :type DisplayName: str
        :param _ServerId: <p>服务 id</p>
        :type ServerId: str
        :param _UpstreamType: <p>后端类型</p><p>枚举值：</p><ul><li>HostIP： 域名 ip</li><li>MCPRegistry： MCP 注册中心</li><li>VirtualMCPServer： 虚拟MCP 服务</li></ul>
        :type UpstreamType: str
        :param _Timeout: <p>超时时间，单位ms，最大60000</p>
        :type Timeout: int
        :param _RetryCount: <p>重试次数，最大3次</p>
        :type RetryCount: int
        :param _UpstreamInfo: <p>注册中心来源信息</p>
        :type UpstreamInfo: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPUpstreamInfo`
        :param _SessionConfig: <p>会话配置</p>
        :type SessionConfig: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPSessionConfig`
        :param _Description: <p>描述</p>
        :type Description: str
        :param _EnableHealthCheck: <p>是否启用健康检查</p>
        :type EnableHealthCheck: bool
        :param _HealthCheck: <p>健康检查配置</p>
        :type HealthCheck: :class:`tencentcloud.cngw.v20230418.models.AIGWHealthCheckSetting`
        """
        self._GatewayId = None
        self._DisplayName = None
        self._ServerId = None
        self._UpstreamType = None
        self._Timeout = None
        self._RetryCount = None
        self._UpstreamInfo = None
        self._SessionConfig = None
        self._Description = None
        self._EnableHealthCheck = None
        self._HealthCheck = None

    @property
    def GatewayId(self):
        r"""<p>实例 ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def DisplayName(self):
        r"""<p>展示名字</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def ServerId(self):
        r"""<p>服务 id</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def UpstreamType(self):
        r"""<p>后端类型</p><p>枚举值：</p><ul><li>HostIP： 域名 ip</li><li>MCPRegistry： MCP 注册中心</li><li>VirtualMCPServer： 虚拟MCP 服务</li></ul>
        :rtype: str
        """
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def Timeout(self):
        r"""<p>超时时间，单位ms，最大60000</p>
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def RetryCount(self):
        r"""<p>重试次数，最大3次</p>
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def UpstreamInfo(self):
        r"""<p>注册中心来源信息</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPUpstreamInfo`
        """
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def SessionConfig(self):
        r"""<p>会话配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWMCPSessionConfig`
        """
        return self._SessionConfig

    @SessionConfig.setter
    def SessionConfig(self, SessionConfig):
        self._SessionConfig = SessionConfig

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
    def EnableHealthCheck(self):
        r"""<p>是否启用健康检查</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def HealthCheck(self):
        r"""<p>健康检查配置</p>
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AIGWHealthCheckSetting`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._DisplayName = params.get("DisplayName")
        self._ServerId = params.get("ServerId")
        self._UpstreamType = params.get("UpstreamType")
        self._Timeout = params.get("Timeout")
        self._RetryCount = params.get("RetryCount")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = AIGWMCPUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        if params.get("SessionConfig") is not None:
            self._SessionConfig = AIGWMCPSessionConfig()
            self._SessionConfig._deserialize(params.get("SessionConfig"))
        self._Description = params.get("Description")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = AIGWHealthCheckSetting()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayMCPServerResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPServer返回参数结构体

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


class ModifyCloudNativeAPIGatewayMCPServerStatusRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPServerStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>实例 ID</p>
        :type GatewayId: str
        :param _ServerId: <p>mcp server id</p>
        :type ServerId: str
        :param _Status: <p>mcp server状态</p><p>枚举值：</p><ul><li>Online： 上线</li><li>Offline： 下线</li></ul>
        :type Status: str
        """
        self._GatewayId = None
        self._ServerId = None
        self._Status = None

    @property
    def GatewayId(self):
        r"""<p>实例 ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>mcp server id</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def Status(self):
        r"""<p>mcp server状态</p><p>枚举值：</p><ul><li>Online： 上线</li><li>Offline： 下线</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayMCPServerStatusResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPServerStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>创建结果</p>
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>创建结果</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayMCPToolACLRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPToolACL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例ID</p>
        :type GatewayId: str
        :param _ServerId: <p>MCP服务ID</p>
        :type ServerId: str
        :param _ToolId: <p>MCP工具ID</p>
        :type ToolId: str
        :param _ACLType: <p>鉴权类型</p><p>枚举值：</p><ul><li>None： 继承server鉴权类型</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul>
        :type ACLType: str
        :param _ACLConsumerIds: <p>需要关联的消费者ID列表</p>
        :type ACLConsumerIds: list of str
        :param _ACLConsumerGroupIds: <p>需要关联的消费者组ID列表</p>
        :type ACLConsumerGroupIds: list of str
        """
        self._GatewayId = None
        self._ServerId = None
        self._ToolId = None
        self._ACLType = None
        self._ACLConsumerIds = None
        self._ACLConsumerGroupIds = None

    @property
    def GatewayId(self):
        r"""<p>网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCP服务ID</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def ToolId(self):
        r"""<p>MCP工具ID</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ACLType(self):
        r"""<p>鉴权类型</p><p>枚举值：</p><ul><li>None： 继承server鉴权类型</li><li>Allow： 白名单</li><li>Deny： 黑名单</li></ul>
        :rtype: str
        """
        return self._ACLType

    @ACLType.setter
    def ACLType(self, ACLType):
        self._ACLType = ACLType

    @property
    def ACLConsumerIds(self):
        r"""<p>需要关联的消费者ID列表</p>
        :rtype: list of str
        """
        return self._ACLConsumerIds

    @ACLConsumerIds.setter
    def ACLConsumerIds(self, ACLConsumerIds):
        self._ACLConsumerIds = ACLConsumerIds

    @property
    def ACLConsumerGroupIds(self):
        r"""<p>需要关联的消费者组ID列表</p>
        :rtype: list of str
        """
        return self._ACLConsumerGroupIds

    @ACLConsumerGroupIds.setter
    def ACLConsumerGroupIds(self, ACLConsumerGroupIds):
        self._ACLConsumerGroupIds = ACLConsumerGroupIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._ToolId = params.get("ToolId")
        self._ACLType = params.get("ACLType")
        self._ACLConsumerIds = params.get("ACLConsumerIds")
        self._ACLConsumerGroupIds = params.get("ACLConsumerGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayMCPToolACLResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPToolACL返回参数结构体

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


class ModifyCloudNativeAPIGatewayMCPToolRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例 id</p>
        :type GatewayId: str
        :param _ServerId: <p>MCPserverId</p>
        :type ServerId: str
        :param _ToolId: <p>工具 id</p>
        :type ToolId: str
        :param _Name: <p>工具名字</p>
        :type Name: str
        :param _Path: <p>路径</p>
        :type Path: str
        :param _ContentType: <p>报文格式</p>
        :type ContentType: str
        :param _Method: <p>请求方法</p><p>枚举值：</p><ul><li>GET： GET</li><li>PUT： PUT</li><li>POST： POST</li><li>DELETE： DELETE</li><li>PATCH： PATCH</li></ul>
        :type Method: str
        :param _DisplayName: <p>展示</p>
        :type DisplayName: str
        :param _InputParams: <p>输入参数</p>
        :type InputParams: list of CNAPIGwMCPToolParam
        :param _Description: <p>描述</p>
        :type Description: str
        :param _ToolVersion: <p>tool版本</p>
        :type ToolVersion: str
        """
        self._GatewayId = None
        self._ServerId = None
        self._ToolId = None
        self._Name = None
        self._Path = None
        self._ContentType = None
        self._Method = None
        self._DisplayName = None
        self._InputParams = None
        self._Description = None
        self._ToolVersion = None

    @property
    def GatewayId(self):
        r"""<p>网关实例 id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>MCPserverId</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def ToolId(self):
        r"""<p>工具 id</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def Name(self):
        r"""<p>工具名字</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Path(self):
        r"""<p>路径</p>
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ContentType(self):
        r"""<p>报文格式</p>
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Method(self):
        r"""<p>请求方法</p><p>枚举值：</p><ul><li>GET： GET</li><li>PUT： PUT</li><li>POST： POST</li><li>DELETE： DELETE</li><li>PATCH： PATCH</li></ul>
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DisplayName(self):
        r"""<p>展示</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def InputParams(self):
        r"""<p>输入参数</p>
        :rtype: list of CNAPIGwMCPToolParam
        """
        return self._InputParams

    @InputParams.setter
    def InputParams(self, InputParams):
        self._InputParams = InputParams

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
    def ToolVersion(self):
        r"""<p>tool版本</p>
        :rtype: str
        """
        return self._ToolVersion

    @ToolVersion.setter
    def ToolVersion(self, ToolVersion):
        self._ToolVersion = ToolVersion


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._ToolId = params.get("ToolId")
        self._Name = params.get("Name")
        self._Path = params.get("Path")
        self._ContentType = params.get("ContentType")
        self._Method = params.get("Method")
        self._DisplayName = params.get("DisplayName")
        if params.get("InputParams") is not None:
            self._InputParams = []
            for item in params.get("InputParams"):
                obj = CNAPIGwMCPToolParam()
                obj._deserialize(item)
                self._InputParams.append(obj)
        self._Description = params.get("Description")
        self._ToolVersion = params.get("ToolVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayMCPToolResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPTool返回参数结构体

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


class ModifyCloudNativeAPIGatewayMCPToolStatusRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPToolStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>实例 ID</p>
        :type GatewayId: str
        :param _ServerId: <p>mcp server id</p>
        :type ServerId: str
        :param _Status: <p>mcp tool 状态</p><p>枚举值：</p><ul><li>Enable： 启用</li><li>Disable： 禁用</li></ul>
        :type Status: str
        :param _ToolId: <p>mcp tool id</p>
        :type ToolId: str
        """
        self._GatewayId = None
        self._ServerId = None
        self._Status = None
        self._ToolId = None

    @property
    def GatewayId(self):
        r"""<p>实例 ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServerId(self):
        r"""<p>mcp server id</p>
        :rtype: str
        """
        return self._ServerId

    @ServerId.setter
    def ServerId(self, ServerId):
        self._ServerId = ServerId

    @property
    def Status(self):
        r"""<p>mcp tool 状态</p><p>枚举值：</p><ul><li>Enable： 启用</li><li>Disable： 禁用</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ToolId(self):
        r"""<p>mcp tool id</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServerId = params.get("ServerId")
        self._Status = params.get("Status")
        self._ToolId = params.get("ToolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayMCPToolStatusResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewayMCPToolStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>创建结果</p>
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>创建结果</p>
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewaySecretKeyRequest(AbstractModel):
    r"""ModifyCloudNativeAPIGatewaySecretKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 实例 ID
        :type GatewayId: str
        :param _Name: 密钥名字
        :type Name: str
        :param _SecretKeyId: 密钥id
        :type SecretKeyId: str
        :param _Description: 描述,200字以内
        :type Description: str
        """
        self._GatewayId = None
        self._Name = None
        self._SecretKeyId = None
        self._Description = None

    @property
    def GatewayId(self):
        r"""实例 ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        r"""密钥名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SecretKeyId(self):
        r"""密钥id
        :rtype: str
        """
        return self._SecretKeyId

    @SecretKeyId.setter
    def SecretKeyId(self, SecretKeyId):
        self._SecretKeyId = SecretKeyId

    @property
    def Description(self):
        r"""描述,200字以内
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._SecretKeyId = params.get("SecretKeyId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewaySecretKeyResponse(AbstractModel):
    r"""ModifyCloudNativeAPIGatewaySecretKey返回参数结构体

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


class RemoveCloudNativeAPIGatewayConsumerGroupAuthRequest(AbstractModel):
    r"""RemoveCloudNativeAPIGatewayConsumerGroupAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例id</p>
        :type GatewayId: str
        :param _ResourceType: <p>授权资源类型。</p><p>枚举值：</p><ul><li>ModelAPI：模型 API</li><li>MCPServer：MCP Server</li></ul>
        :type ResourceType: str
        :param _ResourceId: <p>对应资源的 ID。</p><ul><li>ResourceType=ModelAPI 时是模型 API ID</li><li>ResourceType=MCPServer 时是 MCP Server ID</li></ul>
        :type ResourceId: str
        :param _ConsumerGroupIds: <p>消费者组 ID 列表（每个 ID 以 cg- 开头），长度 1-10。</p>
        :type ConsumerGroupIds: list of str
        """
        self._GatewayId = None
        self._ResourceType = None
        self._ResourceId = None
        self._ConsumerGroupIds = None

    @property
    def GatewayId(self):
        r"""<p>网关实例id</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ResourceType(self):
        r"""<p>授权资源类型。</p><p>枚举值：</p><ul><li>ModelAPI：模型 API</li><li>MCPServer：MCP Server</li></ul>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceId(self):
        r"""<p>对应资源的 ID。</p><ul><li>ResourceType=ModelAPI 时是模型 API ID</li><li>ResourceType=MCPServer 时是 MCP Server ID</li></ul>
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ConsumerGroupIds(self):
        r"""<p>消费者组 ID 列表（每个 ID 以 cg- 开头），长度 1-10。</p>
        :rtype: list of str
        """
        return self._ConsumerGroupIds

    @ConsumerGroupIds.setter
    def ConsumerGroupIds(self, ConsumerGroupIds):
        self._ConsumerGroupIds = ConsumerGroupIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceId = params.get("ResourceId")
        self._ConsumerGroupIds = params.get("ConsumerGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveCloudNativeAPIGatewayConsumerGroupAuthResponse(AbstractModel):
    r"""RemoveCloudNativeAPIGatewayConsumerGroupAuth返回参数结构体

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


class RemoveCloudNativeAPIGatewayConsumerInGroupRequest(AbstractModel):
    r"""RemoveCloudNativeAPIGatewayConsumerInGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _ConsumerGroupId: <p>消费者组 ID（以 cg- 开头）。</p>
        :type ConsumerGroupId: str
        :param _ConsumerIds: <p>消费者 ID 列表，长度 1-10。</p>
        :type ConsumerIds: list of str
        """
        self._GatewayId = None
        self._ConsumerGroupId = None
        self._ConsumerIds = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConsumerGroupId(self):
        r"""<p>消费者组 ID（以 cg- 开头）。</p>
        :rtype: str
        """
        return self._ConsumerGroupId

    @ConsumerGroupId.setter
    def ConsumerGroupId(self, ConsumerGroupId):
        self._ConsumerGroupId = ConsumerGroupId

    @property
    def ConsumerIds(self):
        r"""<p>消费者 ID 列表，长度 1-10。</p>
        :rtype: list of str
        """
        return self._ConsumerIds

    @ConsumerIds.setter
    def ConsumerIds(self, ConsumerIds):
        self._ConsumerIds = ConsumerIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ConsumerGroupId = params.get("ConsumerGroupId")
        self._ConsumerIds = params.get("ConsumerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveCloudNativeAPIGatewayConsumerInGroupResponse(AbstractModel):
    r"""RemoveCloudNativeAPIGatewayConsumerInGroup返回参数结构体

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


class UnbindCloudNativeAPIGatewaySecretKeyRequest(AbstractModel):
    r"""UnbindCloudNativeAPIGatewaySecretKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceIds: 资源ID，当前最多支持一个
        :type ResourceIds: list of str
        :param _SecretKeyId: 密钥id
        :type SecretKeyId: str
        """
        self._GatewayId = None
        self._ResourceType = None
        self._ResourceIds = None
        self._SecretKeyId = None

    @property
    def GatewayId(self):
        r"""网关实例id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceIds(self):
        r"""资源ID，当前最多支持一个
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def SecretKeyId(self):
        r"""密钥id
        :rtype: str
        """
        return self._SecretKeyId

    @SecretKeyId.setter
    def SecretKeyId(self, SecretKeyId):
        self._SecretKeyId = SecretKeyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceIds = params.get("ResourceIds")
        self._SecretKeyId = params.get("SecretKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudNativeAPIGatewaySecretKeyResponse(AbstractModel):
    r"""UnbindCloudNativeAPIGatewaySecretKey返回参数结构体

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


class UpdateCloudNativeAPIGatewayMCPToolsRequest(AbstractModel):
    r"""UpdateCloudNativeAPIGatewayMCPTools请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: <p>网关实例ID</p>
        :type GatewayId: str
        :param _MCPServerId: <p>MCP Server ID</p>
        :type MCPServerId: str
        :param _Tools: <p>待导入的MCP Tools列表</p>
        :type Tools: list of CNAPIGwMCPTool
        """
        self._GatewayId = None
        self._MCPServerId = None
        self._Tools = None

    @property
    def GatewayId(self):
        r"""<p>网关实例ID</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def MCPServerId(self):
        r"""<p>MCP Server ID</p>
        :rtype: str
        """
        return self._MCPServerId

    @MCPServerId.setter
    def MCPServerId(self, MCPServerId):
        self._MCPServerId = MCPServerId

    @property
    def Tools(self):
        r"""<p>待导入的MCP Tools列表</p>
        :rtype: list of CNAPIGwMCPTool
        """
        return self._Tools

    @Tools.setter
    def Tools(self, Tools):
        self._Tools = Tools


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._MCPServerId = params.get("MCPServerId")
        if params.get("Tools") is not None:
            self._Tools = []
            for item in params.get("Tools"):
                obj = CNAPIGwMCPTool()
                obj._deserialize(item)
                self._Tools.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudNativeAPIGatewayMCPToolsResponse(AbstractModel):
    r"""UpdateCloudNativeAPIGatewayMCPTools返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>导入任务的ID</p>
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>导入任务的ID</p>
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")